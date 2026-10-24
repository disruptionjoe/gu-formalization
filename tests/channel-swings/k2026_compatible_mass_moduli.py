"""Complete fixed-core compatible mass space and two normalized Clifford masses.

Sage exact arithmetic. No source connection or physical-state selection is asserted.
"""
from pathlib import Path
import json,hashlib,argparse
from sage.all import QQ,matrix,identity_matrix,zero_matrix,block_matrix,block_diagonal_matrix
from k1967_paired_raw_coefficient_observation import setup
from k1836_k77_differential_dirac_quotient import enc,mat
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2026-compatible-mass-moduli.json'
def constraints(C,S,extra=()):
 n=S.nrows();edges=[]
 for i in range(n):
  for j in range(n):edges.append((i*n+j,QQ(1),j*n+i,QQ(1)))
 for A,sign in [(x,1) for x in C]+[(S,-1)]+[(x,1) for x in extra]:
  rows=[[] for _ in range(n)];cols=[[] for _ in range(n)]
  for (i,j),v in A.dict().items():rows[i].append((j,v));cols[j].append((i,v))
  assert all(len(x)==1 for x in rows+cols)
  for i in range(n):
   for j in range(n):
    k,a=cols[j][0];l,b=rows[i][0];edges.append((i*n+k,a,l*n+j,sign*b))
 return edges

def solve(C,S,extra=()):
 n=S.nrows();adj=[[] for _ in range(n*n)];zero=set();eq=constraints(C,S,extra)
 for u,a,v,b in eq:
  if u==v:
   if a+b:zero.add(u)
  else:adj[u].append((v,-a/b));adj[v].append((u,-b/a))
 seen=set();basis=[];counts={};forced=0
 for root in range(n*n):
  if root in seen:continue
  vals={root:QQ(1)};queue=[root];bad=False
  for u in queue:
   if u in zero:bad=True
   for v,w in adj[u]:
    z=vals[u]*w
    if v in vals:
     if vals[v]!=z:bad=True
    else:vals[v]=z;queue.append(v)
  seen.update(vals);key=str(len(vals))+(' forced' if bad else ' free');counts[key]=counts.get(key,0)+1
  if bad:forced+=len(vals)
  else:basis.append(matrix(QQ,n,n,{divmod(k,n):v for k,v in vals.items()},sparse=True))
 # Each graph component has exactly one parameter, or is forced to zero.
 # Disjoint support makes these nonzero basis matrices independent.
 assert len(seen)==n*n
 return basis,dict(equations=len(eq),variables=n*n,dimension=len(basis),forced_coordinates=forced,components=counts)

def normalized(basis,n):
 N=zero_matrix(QQ,n,n,sparse=True);covered=set();chosen=[]
 for k,B in enumerate(basis):
  active={i for i,j in B.dict()};sq=B*B
  if active&covered or not sq.is_diagonal() or len(set(sq[i,i] for i in active))!=1:continue
  z=-sq[next(iter(active)),next(iter(active))]
  if not z.is_square():continue
  N+=B/z.sqrt();covered|=active;chosen.append(k)
 assert len(covered)==n and N*N==-identity_matrix(QQ,n)
 return N,chosen

def full_extension(N,J,DJ,H,Ti):
 X=J[:1792,:];F=J[1792:,:];Y=H*DJ*N;Y1=Y[:1792,:];Y2=Y[1792:,:]
 O=zero_matrix(QQ,128,1792,sparse=True);O[:,:128]=Ti;assert O*X==identity_matrix(QQ,128)
 B=O.transpose()*Y2.transpose();Z=Y1-B*F;T=X.transpose()*Z;assert T==T.transpose()
 A=Z*O+O.transpose()*Z.transpose()-O.transpose()*T*O
 K=H*block_matrix(QQ,[[A,B],[B.transpose(),zero_matrix(QQ,128,128,sparse=True)]],sparse=True)
 assert H*K==K.transpose()*H and K*J==DJ*N and not K[1792:,1792:]
 return K

def produce():
 g,v,eta,js,C,P,djs,Fi,Ti,_=setup();I=identity_matrix(QQ,128);J=block_matrix(QQ,[[a] for a in js],sparse=True);DJ=block_matrix(QQ,[[a] for a in djs],sparse=True)
 B=g[7]
 for k in range(8,14):B=B*g[k]
 H=block_diagonal_matrix([eta[k]*B for k in range(14)]+[B],sparse=True);S=J.transpose()*H*DJ;V=C[0]*C[1]*C[2];T=-V*S
 assert S.transpose()==-S and V*V==-I and T==T.transpose() and all(S*c==c*S for c in C)
 bs,census=solve(C,S);N,chosen=normalized(bs,128);bs2,census2=solve(C,S,[N]);M,chosen2=normalized(bs2,128)
 for x in bs:
  assert x.transpose()==-x and x*S==S*x and all(x*c+c*x==0 for c in C)
 for x in bs2:assert x*N+N*x==0 and x*S==S*x and x.transpose()==-x and all(x*c+c*x==0 for c in C)
 assert N*M+M*N==0
 F=C[0]*N;assert F.transpose()==F and F*F==I and (F-I).rank()==64 and (F+I).rank()==64
 assert all(F*c==c*F for c in C[1:]) and F*M==M*F
 K=full_extension(N,J,DJ,H,Ti);L=full_extension(M,J,DJ,H,Ti)
 controls=[]
 for a,b in [(QQ(1),QQ(0)),(QQ(3)/5,QQ(4)/5),(QQ(0),QQ(1)),(QQ(-3)/5,QQ(4)/5),(QQ(-1),QQ(0))]:
  mass=a*N+b*M;assert mass*mass==-I and mass*S==S*mass and mass.transpose()==-mass
  full=a*K+b*L;assert full*J==DJ*mass and H*full==full.transpose()*H
  controls.append([str(a),str(b)])
 # Exact Fourier and wall restriction identities, for arbitrary real coefficients.
 coeffs=[C[1],C[2],M];plus=(I+F)/2
 for i,A in enumerate(coeffs):
  for j,B in enumerate(coeffs):
   rhs=2*(I if i<2 else -I) if i==j else zero_matrix(QQ,128,128)
   assert plus*(A*B+B*A)*plus==rhs*plus
 vals=[QQ(9)/70,QQ(-9)/70,QQ(9)/140,QQ(-9)/140];spectral={str(x):128-(T-x*I).rank() for x in vals};assert sum(spectral.values())==128
 inputs=['lab/process/k1951-coordinated-zero-southeast-principal.json','lab/process/k2024-full-odd-connection-compatibility.json']
 return dict(result_id='K2026',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',census=census,second_mass_census=census2,basis=[enc(x) for x in bs],second_basis=[enc(x) for x in bs2],normalized_mass=enc(N),second_normalized_mass=enc(M),chosen=chosen,second_chosen=chosen2,S=enc(S),T=enc(T),T_spectrum=spectral,wall_involution=enc(F),wall_kernel_dimension=64,full_extension=enc(K),second_extension=enc(L),circle_controls=controls,scope='Complete real linear mass space for fixed C_i, P=8I and S. Equal mass, gapped circle and domain-wall counterexample are conditional constructions; no source-selected connection, quotient, interacting positivity or GU prediction.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs})
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();r=produce()
 if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text())
 print('PASS K2026',r['census'],r['second_mass_census'],r['T_spectrum'],flush=True)
