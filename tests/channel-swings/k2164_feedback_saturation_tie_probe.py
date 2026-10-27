#!/usr/bin/env python3
"""Rational global saturation bounds, derivative and spectral-moment controls."""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import argparse,hashlib,heapq,json
ROOT=Path(__file__).resolve().parents[2]
def sqrt_bounds(x, digits=18):
 d=10**digits;k=isqrt(x.numerator*d*d//x.denominator)
 return F(k,d),F(k+1,d)
def A(x):return (17*x*x+x**-2)/2
def Ap(x):return 17*x-x**-3
def moments(t):return [(5-3*t)/8,(7+3*t)/8]
def ks(t):
 a,b=sqrt_bounds(1-t);c,d=sqrt_bounds(t)
 return [(6*a,6*b),(12+6*c,12+6*d)]
def branch_bound(r,k):
 """Exact convex minimum lower bound for r*A(x)-k*x, x>0."""
 lo=F(1,4);hi=F(2)
 assert r*Ap(lo)-k<0<r*Ap(hi)-k
 for _ in range(42):
  mid=(lo+hi)/2
  if r*Ap(mid)<k:lo=mid
  else:hi=mid
 x=(lo+hi)/2;f=r*A(x)-k*x;df=r*Ap(x)-k
 return f+min(df*(lo-x),df*(hi-x)),x

def actual_upper(t,xs):return F(21,2)+sum(r*A(x)-k[0]*x for r,k,x in zip(moments(t),ks(t),xs))
def optimized_bracket(t):
 rs=moments(t);kk=ks(t);cert=[branch_bound(r,k[1]) for r,k in zip(rs,kk)];xs=[c[1] for c in cert]
 return sum(c[0] for c in cert)+F(21,2),actual_upper(t,xs),xs

def interval_lower(a,b,fault=None):
 # A(x),x positive. Independently lower R and upper k on the entire t interval.
 r0=(5-3*b)/8;r1=(7+3*a)/8
 if fault=="interval_wrong_endpoints":r0=(5-3*a)/8;r1=(7+3*b)/8
 k0=6*sqrt_bounds(1-a)[1];k1=12+6*sqrt_bounds(b)[1]
 if fault=="interval_wrong_endpoints":k0=6*sqrt_bounds(1-b)[0];k1=12+6*sqrt_bounds(a)[0]
 return F(21,2)+branch_bound(r0,k0)[0]+branch_bound(r1,k1)[0]

def global_certificate(tol=F(1,10**6)):
 t=F(49,100);_,best,xs=optimized_bracket(t);witness=(t,xs);heap=[(interval_lower(F(0),F(1)),F(0),F(1))];nodes=0
 while best-heap[0][0]>tol:
  lower,a,b=heapq.heappop(heap);m=(a+b)/2
  _,upper,xx=optimized_bracket(m)
  if upper<best:best=upper;witness=(m,xx)
  for aa,bb in [(a,m),(m,b)]:
   lb=interval_lower(aa,bb)
   if lb<=best:heapq.heappush(heap,(lb,aa,bb))
  nodes+=1
  assert heap,'best point must remain covered'
 return dict(lower=str(heap[0][0]),upper=str(best),witness_t=str(witness[0]),witness_x=[str(x) for x in witness[1]],subdivisions=nodes,active_intervals=len(heap),tolerance=str(tol))

def controls(fault=None):
 out={};ck=lambda n,v:out.__setitem__(n,bool(v))
 import sympy as s
 rt=s.sqrt(2);freq=[3-2*rt,3+2*rt]
 m1=s.simplify(sum(freq)/2);mi=s.simplify(sum(1/x for x in freq)/2);m2=s.simplify(sum(x*x for x in freq)/2)
 if fault=='spectral_frequency':freq[0]+=1;m1=s.simplify(sum(freq)/2)
 ck('physical_positive_spectral_moments',all(x>0 for x in freq) and m1==mi==3 and m2==17)
 t=s.symbols('t',positive=True);R0=(5-3*t)/8;R1=(7+3*t)/8
 if fault=='branch_moment':R1-=s.Rational(1,2)
 ck('complete_unnormalized_R',s.simplify(R0+R1)==s.Rational(3,2))
 n=s.symbols('n',integer=True,nonnegative=True)
 w1=s.Rational(1,4)+t/4;M1=s.summation(n*s.Rational(1,2)**(n+1),(n,2,s.oo))+t/4
 ck('geometric_threshold_R',s.simplify(M1+w1/2-R1)==0)
 T1=1/rt+s.sqrt(t)/(2*rt);T0=s.sqrt(1-t)/(2*rt)
 ck('threshold_adjacent_moments',s.simplify(T1.subs(t,s.Rational(1,2)))==1/rt+s.Rational(1,4) and T0.subs(t,s.Rational(1,2))==s.Rational(1,4))
 alpha=F(1,4)+F(49,100)/4;eta=F(3,4)+F(49,100)/4
 if fault=='fixed_ROC':alpha=F(3,8)
 ck('maximal_contrast_changed_ROC',alpha==F(149,400) and eta==F(349,400) and eta-alpha==F(1,2) and alpha!=F(3,8))
 # Exact half-root and factored derivative certificates, intentionally broad rational endpoints.
 s2lo,s2hi=F(14142,10000),F(14143,10000);x0a,x0b=F(724,1000),F(726,1000);x1a,x1b=F(964,1000),F(966,1000)
 ck('half_squeeze_roots',Ap(x0a)<48*s2lo/7 and Ap(x0b)>48*s2hi/7 and Ap(x1a)<(192+48*s2lo)/17 and Ap(x1b)>(192+48*s2hi)/17)
 blo=F(3,16)*(x1a+x0a)*(17-1/(x0a*x1a)**2)-3*s2hi
 bhi=F(3,16)*(x1b+x0b)*(17-1/(x0b*x1b)**2)-3*s2lo
 if fault=='derivative_sign':blo,bhi=-bhi,-blo
 ck('strict_positive_half_derivative',F(11,100)<(x1a-x0b)*blo and (x1b-x0a)*bhi<F(13,100))
 half=optimized_bracket(F(1,2));xx=[F(3627,5000),F(4827,5000)]
 if fault=='pre_feedback_energy':xx=[F(1),F(1)]
 up=actual_upper(F(49,100),xx)
 ck('actual_witness_beats_optimized_half',up<F('3.1006')<F('3.1013')<half[0])
 # Interval lower must include both endpoint exact optima, plus interior; not a proof by sampling.
 ck('interval_lower_control',all(interval_lower(a,b,fault)<optimized_bracket(t)[0] for a,b in [(F(0),F(1)),(F(2,5),F(3,5))] for t in [a,(a+b)/2,b]))
 ck('rational_sqrt_outward_control',all(a*a<=q<=b*b for q in [F(2),F(51),F(49,100),F(0),F(1)] for a,b in [sqrt_bounds(q)]))
 return out
FAULTS=['spectral_frequency','branch_moment','fixed_ROC','derivative_sign','pre_feedback_energy','interval_wrong_endpoints']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();checks=controls();assert all(checks.values()),[k for k,v in checks.items() if not v]
 failures={}
 for fault in FAULTS:
  bad=[k for k,v in controls(fault).items() if not v];assert bad,('undetected',fault);failures[fault]=bad
 cert=global_certificate();assert F(cert['upper'])-F(cert['lower'])<=F(cert['tolerance'])
 deps=['explorations/conditional-build/k2164-feedback-saturation-tie-2026-10-27.md','explorations/conditional-build/k2160-outcome-conditioned-squeezing-2026-10-27.md','explorations/conditional-build/k2162-feedback-detector-frontier-2026-10-27.md']
 report=dict(result_id='K2164',status='conditional_exact_certificate',exact_checks=checks,fault_failures=failures,global_certificate=cert,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Fixed positive two-mode scalar Fock model. Global energy bracket for integer N1 maximal contrast; no uniqueness, universal half-tie or apparatus cost. Separate analytic compact-smear existence transfer; no explicit support-size bound.')
 p=ROOT/'lab/process/k2164-feedback-saturation-tie.json'
 if args.write:p.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(p.read_text())==report,'stored report differs'
 print(json.dumps(dict(result='K2164',checks=len(checks),faults=failures,global_interval=[float(F(cert['lower'])),float(F(cert['upper']))],subdivisions=cert['subdivisions'])))
if __name__=='__main__':main()
