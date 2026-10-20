#!/usr/bin/env sage-python
"""Independent symmetric-coordinate linear system and positivity controls."""
import json,copy
from pathlib import Path
from sage.all import QQ,matrix,identity_matrix,block_matrix,zero_matrix
R=Path(__file__).resolve().parents[2];v=json.loads((R/'lab/process/k1832-k77-common-energy-form.json').read_text())
def mat(x):return matrix(QQ,*x['shape'],{(i,j):QQ(t) for i,j,t in x['entries']})
checks=0
for block in v['blocks']:
 a=list(map(mat,block['matrices']));H=mat(block['H']);n=16;pairs=[(i,j) for i in range(n) for j in range(i,n)]
 basis=[]
 for i,j in pairs:
  E=zero_matrix(QQ,n);E[i,j]=1;E[j,i]=1;basis.append(E)
 cols=[sum([(E*A-A.transpose()*E).list() for A in a],[]) for E in basis]
 equations=matrix(QQ,cols).transpose();ker=equations.right_kernel();assert ker.dimension()==1
 h=sum((x*E for x,E in zip(ker.basis()[0],basis)),zero_matrix(QQ,n));h/=h[0,0];assert h==H
 assert all(H[:k,:k].det()>0 for k in range(1,n+1));checks+=18
 # Independently test the exact Fourier conservation identity coefficientwise.
 for A in a:assert H*A-A.transpose()*H==0;checks+=1
# Different small models: positive energy does not imply nilpotent damping.
for w in [1,2,7,QQ(1)/3]:
 H=matrix(QQ,[[w,0],[0,1]]);C=matrix(QQ,[[0,1],[0,0]])
 D=H*C+C.transpose()*H;assert C*C==0 and D.det()<0
 for t in [1,2,5]:
  U=identity_matrix(QQ,2)-t*C;x=matrix(QQ,[[0],[1]])
  assert (x.transpose()*U.transpose()*H*U*x)[0,0]==1+w*t*t
 checks+=4
# Cross-copy complex Hermitian forms produce real symmetric forms; imaginary mixing matters.
J=matrix(QQ,[[0,-1],[1,0]]);I=identity_matrix(QQ,2)
G=block_matrix([[2*I,J],[-J,2*I]])
assert G==G.transpose() and all(G[:k,:k].det()>0 for k in range(1,5));checks+=1
for scale in [0,QQ(1)/2,1,2]:
 # Boundary flux outgoing norm minus incoming norm, incoming=scale*outgoing.
 flux=1-scale**2;assert (flux>=0)==(scale<=1);checks+=1
expected={'common_positive_symmetrizer':True,'constant_coefficient_energy_estimate':True,'physical_pairing_selected':False,'source_or_canon_promotion':False,'nonzero_nilpotent_dissipative_zero_order_possible':False}
def validate_report(data):
 for key,val in expected.items():
  assert data['results'][key]==val,'REPORT_MISMATCH:'+key
validate_report(v);mutations=0
for key,val in expected.items():
 b=copy.deepcopy(v);b['results'][key]=not val
 try:validate_report(b)
 except AssertionError as err:
  assert str(err)=='REPORT_MISMATCH:'+key;mutations+=1
 else:raise AssertionError('missed reporting fault '+key)
print('PASS K1832 independent mathematical controls',checks,'reporting faults rejected',mutations)
