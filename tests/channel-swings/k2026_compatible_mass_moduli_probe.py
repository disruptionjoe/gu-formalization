"""Separate signed-conjugation orbit proof and raw full-matrix replay."""
from pathlib import Path
import json,hashlib
from sage.all import QQ,matrix,identity_matrix,zero_matrix,block_matrix,block_diagonal_matrix
from k1967_paired_raw_coefficient_observation import setup
from k1836_k77_differential_dirac_quotient import mat
ROOT=Path(__file__).resolve().parents[2]
def orbit_dimension(C,S,extra=()):
 n=128;maps=[]
 for A,sign in [(a,-1) for a in C]+[(S,1)]+[(a,-1) for a in extra]:
  cols=[[] for _ in range(n)]
  for (i,j),v in A.dict().items():cols[j].append((i,v))
  assert all(len(c)==1 for c in cols)
  maps.append((cols,sign))
 seen=set();dimension=0
 for i in range(n):
  for j in range(n):
   if (i,j) in seen:continue
   weights={(i,j):QQ(1)};queue=[(i,j)];consistent=True
   for a,b in queue:
    successors=[((b,a),-weights[a,b])]
    for cols,sign in maps:
     (aa,x),=cols[a];(bb,y),=cols[b]
     successors.append(((aa,bb),sign*x/y*weights[a,b]))
    for target,z in successors:
     if target in weights:
      if weights[target]!=z:consistent=False
     else:weights[target]=z;queue.append(target)
   seen.update(weights);dimension+=int(consistent)
 assert len(seen)==n*n
 return dimension

def verify(r):
 g,v,eta,js,C,P,ds,Fi,Ti,_=setup();I=identity_matrix(QQ,128);J=block_matrix(QQ,[[a] for a in js],sparse=True);DJ=block_matrix(QQ,[[a] for a in ds],sparse=True)
 B=g[7]
 for k in range(8,14):B*=g[k]
 H=block_diagonal_matrix([eta[k]*B for k in range(14)]+[B],sparse=True);S=J.transpose()*H*DJ
 assert S==mat(r['S']);N,M=map(mat,[r['normalized_mass'],r['second_normalized_mass']]);T=-C[0]*C[1]*C[2]*S;assert T==mat(r['T'])
 for label,extra in [('basis',[]),('second_basis',[N])]:
  used=set();bs=list(map(mat,r[label]));dim=orbit_dimension(C,S,extra)
  assert len(bs)==dim==(256 if label=='basis' else 128)
  for b in bs:
   support=set(b.dict());assert support and not support&used;used|=support
   assert b+b.transpose()==0 and b*S-S*b==0 and all(b*c+c*b==0 for c in C+extra)
 for a,k in [(N,mat(r['full_extension'])),(M,mat(r['second_extension']))]:
  assert a.transpose()==-a and a*a==-I and a*S==S*a and all(a*c+c*a==0 for c in C)
  assert H*k==k.transpose()*H and k*J==DJ*a and k[1792:,1792:]==0
 assert N*M+M*N==0
 F=C[0]*N;plus=(I+F)/2;assert F==mat(r['wall_involution']) and plus*plus==plus and plus.rank()==64
 assert F.transpose()==F and (I-plus).rank()==64
 # The second mass preserves the wall space and is invertible there.
 assert M*plus==plus*M and (M*plus).rank()==64 and (M*plus)**2==-plus
 for A in C[1:]:assert A*plus==plus*A and A*M+M*A==0
 # Exact normalized homotopy points and rational arbitrary-mass dispersion.
 for a,b in r['circle_controls']:
  Z=QQ(a)*N+QQ(b)*M;assert Z*Z==-I
 for x,y,z,mu in [(1,2,3,4),(-2,0,1,3),(0,0,0,1)]:
  spatial=x*C[0]+y*C[1]+z*C[2]
  assert spatial*spatial-mu*mu*N*N==(x*x+y*y+z*z+mu*mu)*I
 for x,mult in r['T_spectrum'].items():assert 128-(T-QQ(x)*I).rank()==mult
 return C,S,N,M,H,J,DJ

def main():
 r=json.loads((ROOT/'lab/process/k2026-compatible-mass-moduli.json').read_text());C,S,N,M,H,J,DJ=verify(r);I=identity_matrix(QQ,128)
 faults=[]
 # Fault checks touch equations/inputs, never their predicates.
 bad=matrix(N);bad[0,0]+=1
 tests=[('nonconservative_mass',lambda:bad+bad.transpose()==0),('false_second_mass',lambda:N*N+N*N==0),('wrong_gap',lambda:N*N==-4*I)]
 K=mat(r['full_extension']);K[0,0]+=1;tests.append(('full_extension',lambda:K*J==DJ*N))
 bad_basis=list(map(mat,r['basis']))[:-1];tests.append(('missing_basis_direction',lambda:len(bad_basis)==orbit_dimension(C,S)))
 for name,check in tests:
  assert not check(),name;faults.append(name)
 for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 print('PASS K2026 separate full256/second128 orbit completeness;384 disjoint basis identities;2 full extensions; normalized circle,64 wall and gapping mass;',len(faults),'actual faults;',len(r['inputs']),'provenance hashes',flush=True)
if __name__=='__main__':main()
