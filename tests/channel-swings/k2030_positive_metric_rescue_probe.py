"""Separate direct contraction, projector and instability checks with actual faults."""
from pathlib import Path
import json,hashlib
from sage.all import QQ,matrix,identity_matrix,zero_matrix,prod,QuadraticField
from k1967_paired_raw_coefficient_observation import setup
from k1836_k77_differential_dirac_quotient import mat
ROOT=Path(__file__).resolve().parents[2]
def algebra(M,N,C):
 I=identity_matrix(QQ,128);alpha=QQ(4193408)/1087849
 assert M*M==alpha*I,'real generator square'
 assert N*N==-I/2,'imaginary generator square'
 assert M*N+N*M==0,'mixed anticommutator'
 for c in C:
  assert c*c==I and c==c.transpose(),'principal Clifford coefficient'
  assert M*c+c*M==0 and N*c+c*N==0,'mass/principal anticommutator'
 K=QuadraticField(-1,'ii');ii=K.gen();M=M.change_ring(K);N=N.change_ring(K)
 # Momentum cancels the arbitrary vector coefficients. Both masses, not
 # only each pure direction, then have a positive squared generator.
 for s,t in [(1,0),(0,1),(3,4),(-2,3)]:
  X=s*M+ii*t*N;v=alpha*s*s+QQ(t*t)/2
  assert X*X==v*I and X.trace()==0 and v>0,'growing-mode polynomial'
 V=prod(C).change_ring(K);I=I.change_ring(K);star=lambda x:x.conjugate().transpose()
 H=I+ii*V/2
 assert H==star(H) and all(H*c==c*H for c in C),'alternative principal metric'
 for sign in (-1,1):
  Q=(I+sign*ii*V)/2
  assert Q*Q==Q and Q==star(Q) and Q.rank()==64,'central projector'
  for sig in (-1,1):
   P=Q*(I+sig*C[2])/2
   assert P*P==P and P.rank()==32,'multiplicity projector'
 return 6

def run():
 r=json.loads((ROOT/'lab/process/k2030-positive-metric-rescue.json').read_text());g,v,eta,J,C,P,DJ,Fi,Ti,_=setup();I=identity_matrix(QQ,128,sparse=True);Z=zero_matrix(QQ,128,128,sparse=True);W=(3*I-v)/2;B=prod(g[7:]);count=0
 for encoded,expected in zip(r['imaginary_coefficients'],r['imaginary_images']):
  O=list(map(mat,encoded));N=mat(expected)
  # Expand the upper contraction in the opposite order from D_k(Omega_k J).
  common=[sum((g[c]*W*O[k]*J[c] for c in range(14)),Z) for k in range(14)]
  for a in range(14):
   actual=O[a]*J[14]+eta[a]*g[a]*sum((g[k]*(common[k]-g[a]*W*O[k]*J[a]-g[k]*W*O[k]*J[k]) for k in range(14) if k!=a),Z)
   assert actual==DJ[a]*N,'raw upper return';count+=1
  assert -sum((eta[k]*B*O[k].transpose()*B*J[k] for k in range(14)),Z)==DJ[14]*N,'raw lower return';count+=1
 M=mat(r['real_generator']);N=mat(r['extra_imaginary_generator']);assert all(mat(x)==y for x,y in zip(r['principal'],C))
 expected=[I]+C+[N];T=matrix(QQ,[x.list() for x in expected]).transpose()
 assert T.rank()==5
 for e,c in zip(r['imaginary_images'],r['image_coordinates']):assert T*matrix(QQ,5,1,list(map(QQ,c)))==matrix(QQ,128**2,1,mat(e).list())
 baseline=algebra(M,N,C);faults=[]
 for kind in ('imaginary_scale','mixed_direction','principal_sign','real_entry'):
  mm=matrix(M);nn=matrix(N);cc=[matrix(c) for c in C]
  if kind=='imaginary_scale':nn*=2
  elif kind=='mixed_direction':nn=M
  elif kind=='principal_sign':cc[0]=-cc[0]*cc[1]
  else:mm[0,0]+=1
  try:algebra(mm,nn,cc)
  except AssertionError as e:assert str(e);faults.append([kind,str(e)])
  else:raise AssertionError('accepted mathematical fault')
 for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 print('PASS K2030 separate direct contraction:',count,'raw returns;6 central/multiplicity projectors;4 mixed Fourier controls;',faults,';3 provenance hashes',flush=True)
if __name__=='__main__':run()
