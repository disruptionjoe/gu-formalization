#!/usr/bin/env python3
"""Exact Clifford/parent/interference controls; continuum claims need the written proof."""
import sys,itertools
import sympy as s
I=s.I;R=s.Rational;X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-I],[I,0]]);Z=s.diag(1,-1)
C=[s.kronecker_product(X,X),s.kronecker_product(X,Y),s.kronecker_product(X,Z),s.kronecker_product(Z,s.eye(2))]
def checks(fault=None):
 out=[]
 def ck(n,v):out.append((n,bool(v)))
 def zero(M):return all(s.simplify(v)==0 for v in M)
 for j in range(4):
  for k in range(4):ck('clifford_%s_%s'%(j,k),zero(C[j]*C[k]+C[k]*C[j]-(2*s.eye(4) if j==k else s.zeros(4))))
 vectors=[(0,0,0,1),(R(4,5),0,0,R(3,5)),(0,R(4,5),0,R(3,5)),(0,0,R(4,5),R(3,5))]
 def proj(q):return (s.eye(4)+sum((q[j]*C[j] for j in range(4)),s.zeros(4)))/2
 for i,q in enumerate(vectors):
  P=proj(q);ck('projector_'+str(i),zero(P*P-P))
  for j,r in enumerate(vectors):
   factor=(1+sum(a*b for a,b in zip(q,r)))/(1 if fault=='sandwich_factor' else 2)
   ck('sandwich_%s_%s'%(i,j),zero(P*proj(r)*P-factor*P))
 p,k,mu=s.Integer(4),s.Integer(4),s.Integer(3);q=lambda x:s.Matrix([x,0,0,mu])/s.sqrt(x*x+mu*mu)
 P=proj(q(p));difference=(q(p).dot(q(p-k))-q(p).dot(q(p+k)))/2
 ck('shift_orientation',zero(P*proj(q(p-k))*P-P*proj(q(p+k))*P-(-1 if fault=='shift_sign' else 1)*difference*P));ck('nonzero_open_witness',difference<0)
 f,g=s.symbols('f g');parents=[f*g,f*(1-g),(1-f)*g,(1-f)*(1-g)]
 if fault=='parent_missing':parents[-1]=0
 ck('parent_normalized',s.expand(sum(parents)-1)==0);ck('marginal_f',s.expand(parents[0]+parents[1]-f)==0);ck('marginal_g',s.expand(parents[0]+parents[2]-g)==0)
 u=s.Matrix([1,0,0,0]);P0=proj(vectors[0]);Pk=proj(vectors[1]);c=R(4,5);v=Pk*u/s.sqrt(c)
 ck('initial_positive',zero(P0*u-u));ck('final_positive',zero(Pk*v-v));ck('mode_unit',s.simplify((v.T.conjugate()*v)[0]-1)==0)
 ck('interference_visibility',s.simplify((u.T.conjugate()*v)[0]-(c if fault=='visibility' else s.sqrt(c)))==0)
 psi=s.Matrix([0,1,-1,0])/s.sqrt(2);B0=-(Z+X)/s.sqrt(2);B1=-(Z-X)/s.sqrt(2)
 bell=s.kronecker_product(Z,B0+B1)+s.kronecker_product(X,B0-B1)
 ck('extra_measurement_resource',s.simplify((psi.T*bell*psi)[0]-2*s.sqrt(2))==0)
 for spin in [X,Z]:
  obs=s.kronecker_product(s.eye(4),spin)
  for j in range(4):ck('multiplicity_commutes_'+str(j)+str(spin),zero(obs*s.kronecker_product(C[j],s.eye(2))-s.kronecker_product(C[j],s.eye(2))*obs))
  effect=(s.eye(2)+spin)/2
  ck('half_distance_attained',zero((effect-s.eye(2)/2)**2-s.eye(2)/4))
 ck('robust_column_identity',zero((B0+B1)**2+(B0-B1)**2-2*(B0**2+B1**2)))
 return out
if __name__=='__main__':
 clean=checks();bad=[n for n,v in clean if not v]
 if bad:print('[FAIL] baseline',bad);raise SystemExit(1)
 print('PASS exact algebra controls',len(clean))
 if '--selftest' in sys.argv:
  for fault in ['sandwich_factor','shift_sign','parent_missing','visibility']:
   bad=[n for n,v in checks(fault) if not v]
   if not bad:print('[FAIL] undetected',fault);raise SystemExit(1)
   print('DETECTED',fault,bad[0])
