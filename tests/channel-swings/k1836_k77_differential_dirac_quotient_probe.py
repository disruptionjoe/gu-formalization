#!/usr/bin/env sage-python
"""Independent Kronecker rank bounds and direct polynomial certificate controls."""
from pathlib import Path
import json,hashlib
from copy import deepcopy
from sage.all import QQ,GF,matrix,identity_matrix,block_matrix
ROOT=Path(__file__).resolve().parents[2]
def mat(x,F=QQ):return matrix(F,x.get('rows',16),x.get('columns',16),{(i,j):F(QQ(v)) for i,j,v in x['entries']})
def run():
 cert=json.loads((ROOT/'lab/process/k1836-k77-differential-dirac-quotient.json').read_text());src=json.loads((ROOT/'lab/process/k1832-k77-common-energy-form.json').read_text());count=0
 def ck(v):
  nonlocal count
  assert v,'mathematical control failed';count+=1
 for p,digest in cert['inputs'].items():ck(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==digest)
 for entry,raw in zip(cert['blocks'],src['blocks']):
  T=list(map(mat,entry['T']));Q=list(map(mat,entry['Q']));A=list(map(mat,raw['matrices']));D=list(map(mat,cert['target_D']));H=mat(raw['H']);al=QQ(entry['alpha'])
  # Separate modular lower bound on the complete coefficient system.
  f=GF(1009);L=[identity_matrix(f,4).tensor_product(a.change_ring(f).transpose())-d.change_ring(f).tensor_product(identity_matrix(f,16))/f(24) for a,d in zip(A,D)]
  z=matrix(f,64,64);E=block_matrix([[L[0],z,z],[z,L[1],z],[z,z,L[2]],[L[1],L[0],z],[L[2],z,L[0]],[z,L[2],L[1]]]);ck(E.rank()==190);ck(block_matrix([[m] for m in L]).rank()==64)
  for n in [(1,0,0),(0,1,0),(0,0,1),(2,-3,6),(1,1,1),(-7,2,4)]:
   r2=sum(x*x for x in n);t=sum((n[i]*T[i] for i in range(3)),matrix(QQ,4,16));q=sum((n[i]*Q[i] for i in range(3)),matrix(QQ,16,4));a=sum((n[i]*A[i] for i in range(3)),matrix(QQ,16,16));d=sum((n[i]*D[i] for i in range(3)),matrix(QQ,4,4))/24
   ck(t*q==r2*identity_matrix(QQ,4));ck(q*t==576*(r2*identity_matrix(QQ,16)-a*a)/575);ck(t*a==d*t and a*q==q*d);ck(t.right_kernel()==(a*a-r2*identity_matrix(QQ,16)).right_kernel());ck(t*H.inverse()*t.transpose()==al*r2*identity_matrix(QQ,4))
  for pair in entry['energy_skew_basis']:
   C=mat(pair['C']);B=mat(pair['B']);ck(C.transpose()*H+H*C==0 and B.transpose()+B==0 and all(t*C==B*t for t in T))
  for pair in entry['mass_lifts']:
   C=mat(pair['C']);B=mat(pair['B']);ck(C.transpose()*H+H*C==0 and all(t*C==B*t for t in T));ck(B*B==-identity_matrix(QQ,4) and all(B*d+d*B==0 for d in D))
  bad=deepcopy(T);bad[0]=matrix(QQ,bad[0]);bad[0][0,0]+=1
  ck(bad[0]*A[0]!=D[0]*bad[0]/24)
  ck(T[0]*A[0]!=D[0]*T[0]) # Wrong speed is detected.
  ck(T[0]*A[0]!=-D[0]*T[0]/24) # Wrong target orientation is detected.
  ck(Q[0]*T[0]!=identity_matrix(QQ,16)) # Differential quotient is not invertible.
 expected={'source_owned':False,'inverse_local':False,'constant_observation_exists':False,'full_slow_target_real_dimension':128}
 def valid(c):return all(c['results'].get(k)==v for k,v in expected.items())
 assert valid(cert)
 for k in expected:
  bad=deepcopy(cert);bad['results'][k]=not expected[k] if isinstance(expected[k],bool) else 512
  assert not valid(bad),'reporting corruption not detected'
 print('PASS K1836 independent',count,'matrix/rank/negative controls; 4 reporting faults')
if __name__=='__main__':run()
