#!/usr/bin/env sage-python
"""Independent polynomial-field product-rule and modular rank controls."""
import copy,json
from pathlib import Path
from sage.all import QQ,GF,PolynomialRing,matrix,vector,identity_matrix,block_matrix
ROOT=Path(__file__).resolve().parents[2]
def m(a):return matrix(QQ,a.get('rows',16),a.get('columns',16),{(i,j):QQ(x) for i,j,x in a['entries']})
def main():
 s=json.loads((ROOT/'lab/process/k1836-k77-differential-dirac-quotient.json').read_text());e=json.loads((ROOT/'lab/process/k1832-k77-common-energy-form.json').read_text());n=0
 def ck(x):
  nonlocal n
  assert x;n+=1
 d=[m(x)/24 for x in s['target_D']]
 for b in range(4):
  T=list(map(m,s['blocks'][b]['T']));A=list(map(m,e['blocks'][b]['matrices']));W=block_matrix([[x] for x in T]);F=GF(1000003)
  ck(W.change_ring(F).rank()==12)
  # Kronecker construction uses column-vectorization, independent of producer's rows.
  eq=block_matrix([[a.transpose().tensor_product(identity_matrix(QQ,4))-identity_matrix(QQ,16).tensor_product(q)] for a,q in zip(A,d)])
  ck(eq.change_ring(F).rank()==64)
  R=PolynomialRing(QQ,['t','x','y','z']);t,x,y,z=R.gens();xs=[x,y,z];u=vector(R,[(j+1)*x*x+(j%3+1)*y*z+t*z*z+j*t*x for j in range(16)])
  C=m(s['blocks'][b]['mass_lifts'][0]['C']);B=m(s['blocks'][b]['mass_lifts'][0]['B'])
  def O(w):return sum((T[i]*w.derivative(xs[i]) for i in range(3)),vector(R,4))
  def P(w,V):return w.derivative(t)+sum((A[i]*w.derivative(xs[i]) for i in range(3)),vector(R,16))+V*w
  def Q(w,V):return w.derivative(t)+sum((d[i]*w.derivative(xs[i]) for i in range(3)),vector(R,4))+V*w
  ck(O(P(u,t*C))-Q(O(u),t*B)==0)
  defect=O(P(u,x*C))-Q(O(u),x*B)
  ck(defect==B*T[0]*u);ck(defect!=0)
  # Independently construct one invisible skew map from the common kernel.
  H=m(e['blocks'][b]['H']);N=W.right_kernel().basis_matrix().transpose();L=matrix(QQ,4,4,{(0,1):1,(1,0):-1});K=N*L*N.transpose()*H
  ck(K!=0 and K.transpose()*H+H*K==0)
  ck(O(P(u,t*C+(x*y+t*z)*K))-Q(O(u),t*B)==0)
  # Direct target covariance with variable leading observation, all spacetime variables.
  J=24**3*d[0]*d[1]*d[2];rr=R.fraction_field();theta=rr(x*y+t*z);I=identity_matrix(QQ,4);U=(I+theta*J)*(I-theta*J).inverse();Ui=U.transpose()
  V=U*B*Ui-U.derivative(t)*Ui-sum((d[i]*U.derivative(xs[i])*Ui for i in range(3)),matrix(rr,4,4))
  Ou=U*O(u);Qu=Ou.derivative(t)+sum((d[i]*Ou.derivative(xs[i]) for i in range(3)),vector(rr,4))+V*Ou
  ck(U*O(P(u,C))==Qu);ck(V+V.transpose()==0)
  def Os(w):return O(w)-2*x*T[0]*w
  ck(Os(P(u,-2*x*A[0]))==Q(Os(u),-2*x*d[0]))
  ck(any(T[i]*(-2*x*A[0])!=(-2*x*d[0])*T[i] for i in range(3)))
  bad=U*B*Ui
  ck(Ou.derivative(t)+sum((d[i]*Ou.derivative(xs[i]) for i in range(3)),vector(rr,4))+bad*Ou!=U*O(P(u,C)))
 v=json.loads((ROOT/'lab/process/k1838-k77-variable-dirac-observation.json').read_text())
 def report(q):
  assert q['results']['fixed_observation_requires_spatially_constant_target_B']
  assert q['results']['time_dependence_allowed'] and q['results']['moving_frame_repair']
  assert not q['results']['source_owned'] and not q['results']['variable_mass_magnitude_selected']
 report(v);mut=0
 for key in ['fixed_observation_requires_spatially_constant_target_B','time_dependence_allowed','moving_frame_repair','source_owned','variable_mass_magnitude_selected']:
  z=copy.deepcopy(v);z['results'][key]=not z['results'][key]
  try:report(z)
  except AssertionError:mut+=1
  else:raise AssertionError('reporting fault escaped')
 print('PASS K1838 probe',n,'independent mathematical controls;',mut,'reporting faults')
if __name__=='__main__':main()
