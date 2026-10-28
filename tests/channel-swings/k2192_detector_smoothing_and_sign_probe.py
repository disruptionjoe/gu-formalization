#!/usr/bin/env python3
"""Exact controls for the paired inequality; universal proof is in the note."""
import sys
sys.dont_write_bytecode=True
from fractions import Fraction as F
from pathlib import Path
import argparse, hashlib, json
import sympy as S

ROOT=Path(__file__).resolve().parents[2]
C=F(40,3)
def p(n): return F(3,4)*F(1,4)**n
def A(s): return F(41,6)*s*s+F(3,2)/s**2
def ap(s): return F(41,3)*s-3/s**3
def Ep(s): return F(5,6)*A(s)-F(80,9)*s+F(35,18)

def controls(fault=None):
 cs={}
 q=F(1,5) if fault=='thermal_ratio' else F(1,4)
 def p(n): return (1-q)*q**n
 def ck(k,v): cs[k]=bool(v)
 s,u,a,b=S.symbols('s u a b',positive=True)
 aa=S.Rational(41,6)*s*s+S.Rational(3,2)/s**2
 ep=S.Rational(5,6)*aa-S.Rational(80,9)*s+S.Rational(35,18)
 coeff=S.Rational(124 if fault=='scalar_coefficient' else 125,4608)
 P=210125*s**6-143910*s**5-1305*s**4+60660*s**3+30375*s**2+20250*s+10125
 ck('scalar_factorization',S.factor(coeff*s*(S.diff(aa,s)-S.Rational(32,3))**2-ep-(s-1)**2*P/(41472*s**5))==0)
 shift=S.Poly(P.subs(s,u+S.Rational(2,3)),u)
 ck('all_shift_coefficients_positive',all(x>0 for x in shift.all_coeffs()))
 ck('exact_shift_coefficients',list(reversed(shift.all_coeffs()))==[S.Rational(39611405,729),S.Rational(13281950,81),S.Rational(9299005,27),S.Rational(17894660,27),S.Rational(2759485,3),696590,210125])
 ck('edge_derivative_in_a',S.expand(S.diff(a*b*(4*a-b)**2,a)-b*(4*a-b)*(12*a-b))==0)
 ck('edge_derivative_at_a1',S.factor(S.diff(b*(4-b)**2,b)-(4-b)*(4-3*b))==0)
 ck('Cauchy_constant',F(9,25)*F(4,3)==F(12,25))
 ck('heavy_branch_constant',F(25,12)*F(5,12)**2/C==F(125,4608))
 ck('squeeze_lower',ap(F(2,3))<0)
 ck('squeeze_upper',ap(F(113,100))>C)
 ck('neutral_energy',Ep(F(1))==0 and ap(F(1))==F(32,3))
 # Infinite profiles: b_n=sqrt(e_n) is rational on a finite head and constant thereafter.
 examples=[[F(3,4),F(4,5),F(5,6)], [F(9,10),F(3,4)], [F(4,5),F(9,10),F(3,4),F(5,6)]]
 witnesses=[]
 for i,bs in enumerate(examples):
  N=len(bs);tail=F(4,5);z=[p(n)*v*v for n,v in enumerate(bs)]
  mass=sum(z)+tail**2*F(1,4)**N
  M=sum(n*v for n,v in enumerate(z))+tail**2*F(1,4)**N*(N+F(1,3))
  R=M+mass/2
  T=sum(F(n+1,2)*p(n)*bs[n]*(bs[n+1] if n+1<N else tail) for n in range(N))
  T+=tail**2*F(1,4)**N*(N+F(4,3))/2
  J=sum(F(n+1,4)*p(n)*(bs[n]-(bs[n+1] if n+1<N else tail))**2/(bs[n]*(bs[n+1] if n+1<N else tail)) for n in range(N))
  if fault=='derivative_weight':J*=F(9,10)
  delta=sum((n+1)*p(n)*((bs[n+1] if n+1<N else tail)-bs[n])*(F(2,5)*bs[n]-F(1,10)*(bs[n+1] if n+1<N else tail)) for n in range(N))
  DD=F(2,3)+sum(F(n+1,4)*p(n)*((bs[n+1] if n+1<N else tail)/bs[n]+bs[n]/(bs[n+1] if n+1<N else tail)-2) for n in range(N))
  ck(f'full_tail_delta_{i}',delta==T-F(4,5)*R)
  ck(f'full_tail_derivative_{i}',DD-F(2,3)==J)
  ck(f'capped_heavy_{i}',all(0<v<1 for v in bs+[tail]) and R>=F(5,12))
  ck(f'cauchy_{i}',delta*delta<=F(12,25)*J and J>0)
  lo,hi=F(2,3),F(113,100)
  for _ in range(70):
   mid=(lo+hi)/2
   if R*ap(mid)<C*T:lo=mid
   else:hi=mid
  ck(f'squeeze_bracket_{i}',R*ap(lo)<C*T<R*ap(hi))
  upper=max(Ep(lo),Ep(hi))-C*lo*J
  ck(f'negative_Q_{i}',upper<0)
  witnesses.append({'R':str(R),'J':str(J),'Q_upper':str(upper)})
 # The geometric normalization is load-bearing, not a replaceable tail cutoff.
 ck('geometric_moments',q/(1-q)==F(1,3) and 1/(1-q)==F(4,3))
 # A strictly monotone exact oracle with interval uncertainty tests equality cases,
 # zero and clipped upper endpoint without a nonterminating equality branch.
 for B in [F(0),F(1,16),F(1,4),F(9,16),F(1)]:
  lo,hi=F(0),F(3,4)
  for _ in range(14):
   aa=lo+(hi-lo)/3;bb=lo+2*(hi-lo)/3;k=1
   while True:
    err=F(1,2)**k
    if aa*aa+err<B-err:lo=aa;break
    if bb*bb-err>B+err:hi=bb;break
    k+=1
    assert k<200
   target=min(B,F(9,16))
   ck(f'inverse_preserves_{B}_{_}',lo*lo<=target<=hi*hi)
  ck(f'inverse_width_{B}',hi-lo==F(3,4)*F(2,3)**14)
 ck('ratio_derivative_identity',S.simplify(S.diff(S.Function('F')(s)/s,s)-(s*S.diff(S.Function('F')(s),s)-S.Function('F')(s))/s**2)==0)
 return cs,witnesses

def main():
 pa=argparse.ArgumentParser();pa.add_argument('--write',action='store_true');args=pa.parse_args()
 cs,w=controls();assert all(cs.values()),[k for k,v in cs.items() if not v]
 faults={}
 for f in ['scalar_coefficient','derivative_weight','thermal_ratio']:
  bad=[k for k,v in controls(f)[0].items() if not v];assert bad,f;faults[f]=bad
 deps=['explorations/conditional-build/k2192-detector-smoothing-and-sign-2026-10-28.md','explorations/conditional-build/k2180-detector-contrast-frontier-2026-10-28.md','explorations/conditional-build/k2188-detector-variational-structure-2026-10-28.md','explorations/conditional-build/k2162-feedback-detector-frontier-2026-10-27.md']
 report=dict(result_id='K2192',status='conditional_exact_controls',checks=cs,fault_failures=faults,witnesses=w,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Written full-tail Cauchy inequality, scalar polynomial positivity, minimizing multiplier and absolute-continuity proof. Finite controls and inverse toy oracle do not certify a numerical optimum or joint uniqueness. No apparatus or GU physical claim.')
 dest=ROOT/'lab/process/k2192-detector-smoothing-and-sign.json'
 if args.write:dest.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(dest.read_text())==report
 print(json.dumps(dict(result='K2192',controls=len(cs),faults=len(faults))))
if __name__=='__main__':main()
