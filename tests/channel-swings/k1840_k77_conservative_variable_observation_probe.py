#!/usr/bin/env sage-python
"""Independent raw-entry ranks and polynomial-field checks for K1840."""
import copy,json
from pathlib import Path
from sage.all import QQ,GF,matrix,vector,identity_matrix,PolynomialRing
ROOT=Path(__file__).resolve().parents[2]
def mat(x):return matrix(QQ,x.get('rows',16),x.get('columns',16),{(i,j):QQ(v) for i,j,v in x['entries']})
def raw_system(T,A,d,H,axes=()):
 # Independent unknowns: all C entries256, B entries16, S entries64.
 rows=[]
 for i in range(3):
  for a in range(4):
   for b in range(16):
    r={}
    def add(k,v):r[k]=r.get(k,0)+v
    for h in range(16):add(h*16+b,T[i][a,h]);add(272+a*16+h,A[i][h,b])
    for h in range(4):add(256+a*4+h,-T[i][h,b]);add(272+h*16+b,-d[i][a,h])
    rows.append(r)
 for a in range(16):
  for b in range(a,16):
   r={}
   for h in range(16):
    for k,v in [(h*16+b,H[a,h]),(h*16+a,H[h,b])]:r[k]=r.get(k,0)+v
   rows.append(r)
 for a in range(4):
  for b in range(a,4):
   r={256+a*4+b:1};r[256+b*4+a]=r.get(256+b*4+a,0)+1;rows.append(r)
 for i in axes:
  for a in range(4):
   for b in range(16):
    r={h*16+b:T[i][a,h] for h in range(16)}
    for h in range(4):r[272+h*16+b]=-d[i][a,h]
    rows.append(r)
 return matrix(QQ,len(rows),336,{(i,j):v for i,r in enumerate(rows) for j,v in r.items()},sparse=True)
def decode(w,H):
 U=matrix(QQ,16);off=0
 for i in range(16):
  for j in range(i+1,16):U[i,j]=w[off];U[j,i]=-w[off];off+=1
 B=matrix(QQ,4)
 for i in range(4):
  for j in range(i+1,4):B[i,j]=w[off];B[j,i]=-w[off];off+=1
 return H.inverse()*U,B,matrix(QQ,4,16,w[126:])
def witness_ok(T,A,d,H,C,B,S):
 return (H*C+C.transpose()*H==0 and B+B.transpose()==0
  and all(T[i]*C-B*T[i]+S*A[i]-d[i]*S==0 for i in range(3))
  and T[0]*C-d[0]*S==0 and S*C-B*S==0)
def main():
 data=json.loads((ROOT/'lab/process/k1840-k77-conservative-variable-observation.json').read_text())
 old=json.loads((ROOT/'lab/process/k1836-k77-differential-dirac-quotient.json').read_text());eng=json.loads((ROOT/'lab/process/k1832-k77-common-energy-form.json').read_text())
 D=[mat(x) for x in old['target_D']];d=[x/24 for x in D];n=0
 def ck(v):
  nonlocal n
  assert v;n+=1
 ring=PolynomialRing(QQ,['t','x','y','z']);t,x,y,z=ring.gens();coords=[x,y,z]
 for ix,(row,prev,en) in enumerate(zip(data['blocks'],old['blocks'],eng['blocks'])):
  T=list(map(mat,prev['T']));A=list(map(mat,en['matrices']));H=mat(en['H']);Hi=H.inverse();alpha=QQ(prev['alpha']);raw=raw_system(T,A,d,H)
  for prime in [65521,65519]:ck(raw.change_ring(GF(prime)).rank()==292)
  basis=mat(row['full_conservative_kernel']);ck(basis.nrows()==44 and basis.rank()==44)
  for w in basis.rows():
   C,B,S=decode(w,H);ck(raw*vector(QQ,C.list()+B.list()+S.list())==0)
  both=raw_system(T,A,d,H,[0,1])
  for prime in [65521,65519]:ck(both.change_ring(GF(prime)).rank()==330)
  repairs=[tuple(mat(p[k]) for k in ['C','B','S']) for p in row['repairs']]
  for C,B,S in repairs:ck(witness_ok(T,A,d,H,C,B,S))
  C1,B1,S1=repairs[0];C2,B2,S2=repairs[1]
  # Direct arbitrary mixed-profile polynomial operator composition.
  m1=x+x*x;m2=1-2*x+x**3;C=m1*C1+m2*C2;B=m1*B1+m2*B2;S=m1*S1+m2*S2
  u=vector(ring,[(i+1)*t*x+(i%3+1)*y*z+x**(i%3+1)+t*t for i in range(16)])
  def drv(v,a):return vector(ring,[f.derivative(a) for f in v])
  def P(v):return drv(v,t)+sum((A[i]*drv(v,coords[i]) for i in range(3)),vector(ring,16))+C*v
  def Q(v):return drv(v,t)+sum((d[i]*drv(v,coords[i]) for i in range(3)),vector(ring,4))+B*v
  def O(v):return sum((T[i]*drv(v,coords[i]) for i in range(3)),vector(ring,4))+S*v
  ck(O(P(u))==Q(O(u)))
  # Direct adjoint-square evaluation against a separate target polynomial field.
  psi=vector(ring,[t*x+y*z+x**(i+1)+(i+1)*y for i in range(4)])
  def Lt(v):return sum((d[i]*drv(v,coords[i]) for i in range(3)),vector(ring,4))+B*v
  def adj(v):return -sum((Hi*T[i].transpose()*drv(v,coords[i]) for i in range(3)),vector(ring,16))+Hi*S.transpose()*v
  ck(O(adj(psi))==-576*alpha*Lt(Lt(psi)))
  def L0(v):return sum((d[i]*drv(v,coords[i]) for i in range(3)),vector(ring,4))+m1*B1*v
  ck(L0(B2*psi)+B2*L0(psi)==0)
  mu=QQ(2)/3
  def Lgap(v):return L0(v)+mu*B2*v
  ck(-Lgap(Lgap(psi))==-L0(L0(psi))+mu*mu*psi)
  ck(T[0]*C1-B1*T[0]!=0) # Old restricted pointwise lift is genuinely relaxed.
  K=D[0]*B1;proj=(identity_matrix(QQ,4)+K)/2
  ck((24*T[0]+S1).transpose()*proj==0)
  ck(proj.rank()==2 and all(q*proj==proj*q for q in [D[1],D[2],B2]))
  # Direction limitation: selected mass repair fails an independent y derivative.
  ck(T[1]*C1-d[1]*S1!=0)
  # Concrete mathematical negative controls, distinct from report fields.
  badC=copy.copy(C1);badC[0,0]+=1;ck(not witness_ok(T,A,d,H,badC,B1,S1))
  ck(not witness_ok(T,A,d,H,C1,B1,matrix(QQ,4,16)))
  ck(T[0]*C1+d[0]*S1!=0)
  ck(S1*Hi*S1.transpose()!=alpha*identity_matrix(QQ,4))
 # Reporting controls are not independent proof of the continuum theorem.
 expected={'full_conservative_pointwise_dimension':44,'arbitrary_static_one_coordinate_two_mass_profiles':True,'two_coordinate_factorized_nonzero_mass':False,'normal_target_zero_modes_observed_in_L2':False,'source_owned':False,'general_nonlinear_class_solved':False}
 assert all(data['results'][k]==v for k,v in expected.items())
 faults=0
 for key,value in expected.items():
  bad=copy.deepcopy(data);bad['results'][key]=(43 if key=='full_conservative_pointwise_dimension' else not value)
  assert not all(bad['results'][k]==v for k,v in expected.items());faults+=1
 print('PASS K1840 independent',n,'mathematical controls; rejected',faults,'reporting mutations')
if __name__=='__main__':main()
