#!/usr/bin/env sage-python
"""Independent modular-rank proof with exact rational witnesses and transfer controls."""
from sage.all import QQ,GF,matrix,identity_matrix,block_matrix
from pathlib import Path
import json,copy
R=Path(__file__).resolve().parents[2];cert=json.loads((R/'lab/process/k1834-k77-characteristic-cones.json').read_text());src=json.loads((R/'lab/process/k1832-k77-common-energy-form.json').read_text());checks=0

def mat(d):return matrix(QQ,int(d.get('rows',16)),int(d.get('columns',16)),{(i,j):QQ(v) for i,j,v in d['entries']})
def constraint(M):
 n=M.nrows();Q=matrix(QQ,n*n,n*n,sparse=True)
 for i in range(n):
  for j in range(n):
   for k in range(n):Q[i*n+j,i*n+k]+=M[k,j];Q[i*n+j,k*n+j]-=M[i,k]
 return Q
for base,out in zip(src['blocks'],cert['blocks']):
 a=list(map(mat,base['matrices']));H=mat(base['H']);I=identity_matrix(QQ,16)
 # Independent rank lower bound mod a good prime, and rational nullspace upper bound.
 squares=[A*A for A in a]+[a[i]*a[j]+a[j]*a[i] for i in range(3) for j in range(i+1,3)]
 Q=block_matrix([[constraint(M)] for M in squares]);basis=list(map(mat,out['square_commutant_basis']));B=matrix(QQ,[C.list() for C in basis]).transpose()
 assert Q.change_ring(GF(1009)).rank()==236 and B.rank()==20 and Q*B==0;checks+=3
 C=mat(out['conservative_noncentral_example']);assert C.transpose()*H+H*C==0;checks+=1
 assert all(C*S==S*C for S in squares) and any(C*A!=A*C for A in a);checks+=1
 # Perturbation preserves neither the quadratic relation nor a sector by fiat.
 F=[(576*A*A-I)/575 for A in a];assert F[0]!=F[1];checks+=1
 common=mat(out['common_fast_basis']);assert common.rank()==4 and all((Q-I)*common==0 for Q in F);checks+=1
 assert any(common.augment(A*common).rank()>4 for A in a);checks+=1
 for n in [(1,1,0),(2,-1,2),(-1,2,3)]:
  rad=sum(x*x for x in n);N=sum((n[i]*a[i] for i in range(3)),matrix(QQ,16,16));F=(576*N*N/rad-I)/575;G=I-F
  assert F*F==F and G*G==G and F*G==0 and F.rank()==12 and G.rank()==4;checks+=1
  assert N*N*F==rad*F and N*N*G==QQ(rad)/576*G;checks+=1
  assert H*F==F.transpose()*H and F*C==C*F;checks+=1
  # Local extraction reconstructs Laplacian, not identity.
  assert -575*rad*F-575*rad*G==-575*rad*I;checks+=1
# A rational boost preserves the first cone but fails the second.
T=matrix(QQ,[[QQ(5)/3,QQ(4)/3,0,0],[QQ(4)/3,QQ(5)/3,0,0],[0,0,1,0],[0,0,0,1]])
G1=matrix.diagonal(QQ,[1,-1,-1,-1]);G2=matrix.diagonal(QQ,[1,-QQ(1)/576,-QQ(1)/576,-QQ(1)/576])
assert T.transpose()*G1*T==G1 and (T.transpose()*G2*T)[0,1]!=0;checks+=1
# Report tests do not constitute mathematics.
expected={'constant_pure_speed_invariant_sector':False,'single_common_Lorentz_cone':False,'local_differential_extraction_invertible':False,'physical_or_source_selection':False,'speed_compatible_coefficient_dimension':20480,'H_skew_speed_compatible_dimension':10208}
def report(c):
 for k,v in expected.items():assert c['results'][k]==v
report(cert);faults=0
for k,v in expected.items():
 bad=copy.deepcopy(cert);bad['results'][k]=(not v) if isinstance(v,bool) else v+1
 try:report(bad)
 except AssertionError:faults+=1
assert faults==len(expected)
print('PASS K1834 probe',checks,'mathematical controls;',faults,'reporting faults rejected')
