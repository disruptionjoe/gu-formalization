#!/usr/bin/env python3
"""Independent finite POVM/instrument and CHSH controls, not a continuum proof."""
import itertools
import sympy as s
R=s.Rational;I=s.eye(2);X=s.Matrix([[0,1],[1,0]])
def checks(fault=None):
 out=[]
 def ck(n,v):out.append((n,bool(v)))
 def eq(M):return all(s.simplify(x)==0 for x in M)
 vs=[s.Matrix([1,0]),s.Matrix([-R(1,2),s.sqrt(3)/2]),s.Matrix([-R(1,2),-s.sqrt(3)/2])];gs=[R(2,3)*v*v.T for v in vs];F,G=gs[:2]
 ck('parent_sum',eq(sum(gs,s.zeros(2))-I));ck('commutator_nonzero',not eq(F*G-G*F))
 J=s.Matrix.vstack(*(s.sqrt(R(2,3))*v.T for v in vs));ck('isometry',eq(J.T*J-I))
 for j in range(3):
  d=s.zeros(3);d[j,j]=1;ck('compression_'+str(j),eq(J.T*d*J-gs[j]))
 K=s.diag(s.sqrt(R(2,3)),0);L=s.diag(1/s.sqrt(3),1);ck('instrument_complete',eq(K*K+L*L-I));D=K*G*K+L*G*L-G
 c=(s.sqrt(3)-1)/6*(-1 if fault=='disturbance_sign' else 1);ck('disturbance_formula',eq(D-c*X));psi=s.Matrix([1,1])/s.sqrt(2);ck('disturbance_witness',s.simplify((psi.T*D*psi)[0]-c)==0)
 for a,b,c,d in itertools.product([-1,1],repeat=4):ck('deterministic_'+str((a,b,c,d)),abs(a*(c+d)+b*(c-d))<=2)
 completeness=K*K if fault=='missing_outcome' else K*K+L*L;B=s.Matrix([[R(1,4),R(1,8)],[R(1,8),R(3,4)]])
 ck('tensor_marginal',eq(s.kronecker_product(completeness,B)-s.kronecker_product(I,B)));ck('postselection_not_complete',not eq(K*K-I))
 resource=(s.sqrt(2)-1)/(4 if fault=='resource_factor' else 2);ck('resource_lower_bound',s.simplify(resource-(2*s.sqrt(2)-2)/4)==0)
 return out
if __name__=='__main__':
 clean=checks();bad=[n for n,v in clean if not v]
 if bad:print('[FAIL] baseline',bad);raise SystemExit(1)
 print('PASS independent finite controls',len(clean))
 for fault in ['disturbance_sign','missing_outcome','resource_factor']:
  bad=[n for n,v in checks(fault) if not v]
  if not bad:print('[FAIL] undetected',fault);raise SystemExit(1)
  print('DETECTED',fault,bad[0])
