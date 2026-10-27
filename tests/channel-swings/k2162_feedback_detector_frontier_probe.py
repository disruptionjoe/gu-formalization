#!/usr/bin/env python3
"""Exact finite-tail construction, weak-budget algebra and outward energy witness."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
import sympy as sp
from flint import arb,ctx
from k2160_outcome_conditioned_squeezing_probe import certificate as threshold_certificate
ROOT=Path(__file__).resolve().parents[2];ctx.prec=256
Z=F(1,4);N=F(1,3);S=F(2,3);ES=F(10);C=F(40,3)
def ar(q):q=F(q);return arb(q.numerator)/q.denominator
def moments(e,fault=None):
 m=len(e)-1
 w=sum(Z**n*(1-Z)*e[n] for n in range(m))+Z**m*e[m]
 occ=sum(n*Z**n*(1-Z)*e[n] for n in range(m))+Z**m*(m+N)*e[m]
 t=sum((ar((1-Z)*(n+1)*Z**n/2)*(ar(e[n])*ar(e[n+1])).sqrt() for n in range(m)),arb(0))
 tail=ar(Z**m*(m+1+N)/2*e[m])
 t+=0 if fault=='drop_overlap_tail' else tail
 return w,occ,t

def energy(e,x0,x1,fault=None):
 total=arb(0)
 for r,x in [(0,x0),(1,x1)]:
  eff=e if r else [1-v for v in e]
  w,m,t=moments(eff,fault);rr=m+w/2
  if fault=='normalize_branches' and w:w,m,t,rr=F(1),m/w,t/ar(w),rr/w
  d=5*(N*m+(N-1)*w/2)+5*((N+1)*m+N*w/2)
  total+=ar(F(41,6)*rr*x*x+F(3,2)*rr/(x*x)+d)-ar(C*x)*t
 return total

def contrast(e):
 m=len(e)-1
 return sum(((n*(1-Z)**2*Z**(n-1) if n else 0)-(1-Z)*Z**n)*e[n] for n in range(m))+m*(1-Z)*Z**(m-1)*e[m]

def controls(fault=None,symbolic=False):
 out={};ck=lambda k,v:out.__setitem__(k,bool(v));eps=F(1,100);slope=F(729,2720)
 e=[F(1,2)+eps*F(2*n-3,2) for n in range(4)];delta=contrast(e)
 x0=1-eps*slope;x1=1+eps*slope
 if fault=='same_feedback_sign':x0=x1
 val=energy(e,x0,x1,fault)
 e0=F(5,2)*delta*delta;common_lower=e0-e0*e0/F(205,9)
 ck('actual_effects_and_exact_signal_contrast',all(0<v<1 for v in e) and delta==F(81,6400))
 ck('actual_finite_budget_strict_advantage',val>0 and val<ar(common_lower))
 ck('actual_energy_enclosure',val>ar(F(354,10**6)) and val<ar(F(355,10**6)))
 ck('weak_squeezes_expand_click_contract_no_click',x0<1<x1)
 sm=sum((n+1)*Z**(n+1) for n in range(3));d3=3*sm;h0=F(170,9);D=F(2)
 kap=Z*ES-2*D*D/h0;kap3=ES/(9*sm)-2*D*D/h0
 ck('exact_weak_coefficients',sm==F(27,64) and d3==F(81,64) and kap==F(353,170) and kap3==F(45652,20655)<F(5,2))
 ck('finite_clipped_profile_beta',ES*sm-2*D*D*d3*d3/h0==F(308151,87040))
 ck('rational_squeeze_slope',2*D*d3/h0==slope)
 # Independent moments of the unchanged threshold, with exact infinite tails.
 w,m,t=moments([F(0),F(1)]);ck('threshold_exact_infinite_moments',w==F(1,4) and m==N and t.contains(ar(F(7,24))))
 w0,m0,t0=moments([F(1),F(0)]);ck('threshold_complement_moments',w0==F(3,4) and m0==0 and t0.is_zero())
 const=energy([F(2,5),F(2,5)],F(1),F(1),fault);ck('constant_effect_zero_energy',const.contains(0))
 # Common squeeze identity independent of per-branch optimization.
 xx=F(4,5);w1,m1,t1=moments(e);w0,m0,t0=moments([1-v for v in e]);ediag=ar(2*ES)*(ar(S*S)-ar(S)*(t0+t1))
 A=F(5,4)*(xx**-2+2*xx-3)+F(205,36)*(xx-1)**2
 ck('common_squeeze_recovery',energy(e,xx,xx,fault).overlaps(ar(xx)*ediag+ar(A)))
 # Convexity implementation control at fixed squeeze pair, with both overlap branches.
 a=[F(1,10),F(4,5),F(1,3),F(9,10)];b=[F(4,5),F(1,5),F(3,5),F(1,10)];mix=[(u+v)/2 for u,v in zip(a,b)]
 ck('fixed_squeeze_convexity_control',energy(mix,F(3,4),F(6,5))<(energy(a,F(3,4),F(6,5))+energy(b,F(3,4),F(6,5)))/2)
 # Actual arbitrary nonmonotone finite tail, compared with a flattened prefix.
 long=[F(1,7),F(6,7),F(2,7),F(5,7),F(1,3),F(9,10),F(1,10),F(2,5)];flat=long[:4];M=3
 rw=Z**(M+1);rm=rw*(M+1+N);rt=Z**M*(M+1+N)/2
 if fault=='zero_tail_allowance':rw=rm=rt=F(0)
 err=F(100,3)*(rm+rw/2)+2*C*2*rt
 tails=True
 for xx,yy in [(F(1,2),F(2)),(F(2),F(1,2)),(F(4,5),F(6,5))]:tails &= abs(energy(long,xx,yy)-energy(flat,xx,yy))<ar(err)
 ck('uniform_energy_tail_controls',tails)
 ck('contrast_tail_bound',abs(contrast(long)-contrast(flat))<=(M+1)*(1-Z)*Z**M)
 # Vacuum squeeze A is uniformly strongly convex: exact global common lower bound.
 if symbolic:
  x=sp.symbols('x',positive=True);m1,L,E=sp.symbols('m1 L E',positive=True)
  ax=m1*(x**-2+2*x-3)/4+L*(x-1)**2/4
  ck('global_common_strong_convexity',sp.simplify(sp.diff(ax,x,2)-L/2-3*m1/(2*x**4))==0)
  n,es,mv,wv=sp.symbols('n es mv wv',positive=True)
  deriv=4*n*(n+1)*es/(2*n+1)*(mv+wv/2)-n*es*(wv+(2*n+1)*mv/n)
  ck('general_linear_branch_derivative',sp.simplify(deriv+es*(mv-n*wv)/(2*n+1))==0)
  u,v,t,h=sp.symbols('u v t h',positive=True)
  gm=sp.sqrt((t+h*u)*(t+h*v));coef=sp.diff(gm,h,2).subs(h,0)/2
  ck('geometric_mean_second_variation',sp.simplify(coef+(v-u)**2/(8*t))==0)
  ep=sp.symbols('ep',real=True);eff=[sp.Rational(1,2)+ep*sp.Rational(2*n-3,2) for n in range(4)]
  actual=0
  for r in [0,1]:
   ef=eff if r else [1-v for v in eff];xs=1+(1 if r else -1)*sp.Rational(729,2720)*ep
   ww=sum(sp.Rational(3,4)*sp.Rational(1,4)**n*ef[n] for n in range(3))+sp.Rational(1,4)**3*ef[3]
   mm=sum(n*sp.Rational(3,4)*sp.Rational(1,4)**n*ef[n] for n in range(3))+sp.Rational(1,4)**3*sp.Rational(10,3)*ef[3]
   tt=sum(sp.Rational(3,8)*(n+1)*sp.Rational(1,4)**n*sp.sqrt(ef[n]*ef[n+1]) for n in range(3))+sp.Rational(1,2)*sp.Rational(1,4)**3*sp.Rational(13,3)*ef[3]
   rr=mm+ww/2;dd=5*(sp.Rational(1,3)*mm-sp.Rational(1,3)*ww)+5*(sp.Rational(4,3)*mm+ww/6)
   actual+=sp.Rational(41,6)*rr*xs**2+sp.Rational(3,2)*rr/xs**2-sp.Rational(40,3)*xs*tt+dd
  beta=sp.simplify(sp.diff(actual,ep,2).subs(ep,0)/2)
  ck('independent_full_branch_weak_expansion',sp.simplify(actual.subs(ep,0))==0 and sp.simplify(sp.diff(actual,ep).subs(ep,0))==0 and beta==sp.Rational(308151,87040))
 return out,dict(contrast=str(delta),energy=str(val),common_squeeze_lower=str(common_lower),x_no_click=str(x0),x_click=str(x1))
FAULTS=['drop_overlap_tail','normalize_branches','same_feedback_sign','zero_tail_allowance']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();base,witness=controls(symbolic=True);assert all(base.values()),[k for k,v in base.items() if not v]
 faults={}
 for f in FAULTS:
  c,_=controls(f);bad=[k for k,v in c.items() if not v];assert bad,('undetected',f);faults[f]=bad
 certs=[threshold_certificate(r) for r in [0,1]];lo=sum(F(c['energy_lower']) for c in certs);hi=sum(F(c['energy_upper']) for c in certs)
 assert F('4.2304967688817322')<lo<hi<F('4.2304967688817324')
 deps=['explorations/conditional-build/k2162-feedback-detector-frontier-2026-10-27.md','explorations/conditional-build/k2160-outcome-conditioned-squeezing-2026-10-27.md','tests/channel-swings/k2160_outcome_conditioned_squeezing_probe.py','explorations/conditional-build/k2156-energy-budget-detector-frontier-2026-10-27.md']
 report=dict(result_id='K2162',status='conditional_exact_and_interval_controls',checks=base,fault_failures=faults,finite_budget_witness=witness,saturation_certificate=certs,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Written compactness, convex subproblem, global budget-slack approximation, endpoint and achievable asymptotic proofs separately reviewed. Finite controls are not a full grid solve or sharp global low-budget asymptote.')
 p=ROOT/'lab/process/k2162-feedback-detector-frontier.json'
 if args.write:p.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(p.read_text())==report,'stored report differs'
 print(json.dumps(dict(result='K2162',checks=len(base),faults=faults,witness=witness)))
if __name__=='__main__':main()
