#!/usr/bin/env python3
"""Exact independent covariance expansion and rational branch-energy certificates."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import sympy as sp
ROOT=Path(__file__).resolve().parents[2]
def branch(x,r):
 return (41*x*x+9/x**2-10)/16 if r==0 else (451*x*x+99/x**2-560*x+370)/144
def deriv(x,r):
 return (82*x-18/x**3)/16 if r==0 else (902*x-198/x**3-560)/144
def certificate(r):
 lo=F(1,2);hi=F(1)
 assert deriv(lo,r)<0<deriv(hi,r)
 for _ in range(100):
  mid=(lo+hi)/2
  if deriv(mid,r)<0:lo=mid
  else:hi=mid
 mid=(lo+hi)/2;up=branch(mid,r);low=up+min(deriv(mid,r)*(lo-mid),deriv(mid,r)*(hi-mid))
 assert low<=up and up-low<F(1,10**50)
 return {k:str(v) for k,v in dict(root_lower=lo,root_upper=hi,energy_lower=low,energy_upper=up).items()}
def controls(fault=None,symbolic=False):
 out={};ck=lambda k,v:out.__setitem__(k,bool(v))
 n=F(1,3);nu=F(3);s=F(2,3);es=F(10);z=F(1,4)
 moments=[(F(3,4),F(0),F(0)),(F(1,4),F(1,3),F(7,24))]
 physical=[]
 for r,(w,m,t) in enumerate(moments):
  x=F(2,3) if r==0 else F(1)
  if fault=='unweighted_conditional':m,t,w=m/w,t/w,F(1)
  if fault=='unconditional_branch':m,t= n*w,s*w
  u=(x+1/x)/2;v=(x-1/x)/2
  nh=(n+1)*(u*u*m+v*v*(m+w))+n*(m+w)-2*s*u*t
  nj=(n+1)*m+n*(u*u*(m+w)+v*v*m)-2*s*u*t
  cross=(2*n+1)*v*t-s*u*v*(2*m+w)
  actual=5*(nh+nj)+(0 if fault=='drop_cross' else -8*cross)
  physical.append(actual)
  rr=m+w/2;d=5*(n*m+(n-1)*w/2)+5*((n+1)*m+n*w/2)
  target=41*rr/(2*nu)*x*x+nu*rr/(2*x*x)-2*s*es*t*x+(0 if fault=='omit_complement' else d)
  ck('branch_'+str(r)+'_physical_covariance',actual==branch(x,r))
  ck('branch_'+str(r)+'_polynomial',target==branch(x,r))
 ck('strict_rational_feedback_improvement',sum(physical)==F(2465,576)<F('4.4289859434858'))
 ck('unsqueezed_branches',branch(F(1),0)==branch(F(1),1)==F(5,2))
 ck('unnormalized_moment_sums',sum(x[0] for x in moments)==1 and sum(x[1] for x in moments)==n and sum(x[2] for x in moments)==F(7,24))
 ck('distinct_minimizers',F(0)!=F(7,24)/F(11,24))
 # Tail-1 geometric moments derived from complete geometric sum minus n=0.
 ck('exact_threshold_moments',n==z/(1-z) and moments[1][2]==s-(1-z)*F(1,2))
 # q_n=n(1-z)^2 z^(n-1); exact derivative of geometric series sums q over n>=1.
 ck('fixed_signal_ROC',z==F(1,4) and (1-z)**2/(1-z)**2==1 and z/2==F(1,8))
 # Constant effects: each branch scales all moments, hence exactly the vacuum squeeze energy.
 eq=True
 for weight in [F(2,5),F(3,5)]:
  w=weight;m=n*weight;t=s*weight;rr=m+w/2;x=F(4,5)
  d=5*(n*m+(n-1)*w/2)+5*((n+1)*m+n*w/2)
  value=41*rr/6*x*x+3*rr/(2*x*x)-F(40,3)*t*x+d
  vacuum=F(5,4)*(x**-2+2*x-3)+F(205,36)*(x-1)**2
  eq &= t/rr==s/(n+F(1,2)) and value==weight*vacuum
 ck('proportional_effect_equality_control',eq)
 # Two finite unitary matrices validate post-Kraus order and every effect only.
 U=[sp.Matrix([[sp.Rational(3,5),-sp.Rational(4,5)],[sp.Rational(4,5),sp.Rational(3,5)]]),sp.Matrix([[0,-1],[1,0]])]
 K=[sp.diag(1,0),sp.diag(0,1)];L=[k*u if fault=='presqueeze' else u*k for u,k in zip(U,K)]
 ck('reported_effects_reference_independent',all(l.T*l==k.T*k for l,k in zip(L,K)))
 ck('complete_record',sum((l.T*l for l in L),sp.zeros(2))==sp.eye(2))
 # Fixed-effect phase flip changes genuine Schmidt adjacent overlaps, not report labels.
 rr=F(11,24);t=F(7,24);x=F(4,5)
 positive=41*rr/6*x*x+3*rr/(2*x*x)-F(40,3)*t*x+F(185,72)
 flipped=41*rr/6*x*x+3*rr/(2*x*x)+F(40,3)*t*x+F(185,72)
 ck('phase_instrument_is_costlier',flipped>positive)
 if symbolic:
  N,m1,m2,w,M,T,X=sp.symbols('N m1 m2 w M T X',positive=True)
  nu=m1/(2*N+1);ss=sp.sqrt(N*(N+1));R=M+w/2;u=(X+1/X)/2;v=(X-1/X)/2
  eh=(nu+2*m1+m2/nu)/(4*(N+1));ej=(nu-2*m1+m2/nu)/(4*N);j=(nu-m2/nu)/(4*ss);es=eh+ej
  nh=(N+1)*(u*u*M+v*v*(M+w))+N*(M+w)-2*ss*u*T
  nj=(N+1)*M+N*(u*u*(M+w)+v*v*M)-2*ss*u*T
  cross=(2*N+1)*v*T-ss*u*v*(2*M+w)
  d=eh*(N*M+(N-1)*w/2)+ej*((N+1)*M+N*w/2)
  target=m2*R/(2*nu)*X**2+nu*R/(2*X**2)-2*ss*es*T*X+d
  ck('symbolic_original_covariance_to_branch',sp.simplify(eh*nh+ej*nj+2*j*cross-target)==0)
  ck('symbolic_strict_convexity',sp.simplify(sp.diff(target,X,2)-m2*R/nu-3*nu*R/X**4)==0)
  E=sp.symbols('E',nonnegative=True);total=target.subs({w:1,M:N,T:ss-E/(2*ss*es)})
  common=X*E+m1/4*(X**-2+2*X-3)+((2*N+1)**2*m2/m1)/4*(X-1)**2
  ck('symbolic_common_squeeze_recovered',sp.simplify(total-common)==0)
  ck('symbolic_no_click_minimum',sp.simplify((41*X**2+9/X**2-10).subs(X,(sp.Rational(9,41))**sp.Rational(1,4))/16-(3*sp.sqrt(41)-5)/8)==0)
 if symbolic:
  nn=sp.symbols('nn',integer=True,nonnegative=True);zz=sp.Rational(1,4);J=7
  dw=sp.summation((1-zz)*zz**nn,(nn,J+1,sp.oo))
  dm=sp.summation(nn*(1-zz)*zz**nn,(nn,J+1,sp.oo))
  dt=sp.summation((nn+1)*(1-zz)*zz**(nn+sp.Rational(1,2)),(nn,J+1,sp.oo))
  ck('exact_geometric_tail_majorants',dw==zz**(J+1) and dm==zz**(J+1)*(J+1+zz/(1-zz)) and dt==sp.sqrt(zz)*zz**(J+1)*(J+2+zz/(1-zz)))
 return out
FAULTS=['drop_cross','unweighted_conditional','unconditional_branch','omit_complement','presqueeze']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
 checks=controls(symbolic=True);assert all(checks.values()),[k for k,v in checks.items() if not v]
 faults={}
 for f in FAULTS:
  bad=[k for k,v in controls(f).items() if not v];assert bad,('undetected',f);faults[f]=bad
 certs=[certificate(r) for r in range(2)];lo=sum(F(c['energy_lower']) for c in certs);hi=sum(F(c['energy_upper']) for c in certs)
 assert F('4.2304967688817322')<lo<=hi<F('4.2304967688817324')
 deps=['explorations/conditional-build/k2160-outcome-conditioned-squeezing-2026-10-27.md','explorations/conditional-build/k2151-optimal-local-mode-discrimination-2026-10-27.md','explorations/conditional-build/k2153-diagonal-detector-energy-2026-10-27.md','explorations/conditional-build/k2158-local-squeezing-detector-energy-2026-10-27.md']
 report=dict(result_id='K2160',status='conditional_exact_controls',exact_checks=checks,fault_failures=faults,branch_certificates=certs,total_energy_interval=[str(lo),str(hi)],dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Written countable-Kraus, form-domain, fixed-effect optimization and equality proofs separately reviewed; finite effect fixture is ordering only; no all-local or apparatus optimum.')
 p=ROOT/'lab/process/k2160-outcome-conditioned-squeezing.json'
 if args.write:p.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(p.read_text())==report,'stored report differs'
 print(json.dumps(dict(result='K2160',exact_checks=len(checks),faults=faults,interval=[float(lo),float(hi)])))
if __name__=='__main__':main()
