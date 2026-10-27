#!/usr/bin/env python3
"""Exact finite controls and outward interval certificate; no optimizer needed."""
from pathlib import Path
import argparse,hashlib,json
from fractions import Fraction as F
import sympy as sy
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[2]
CANDIDATE={'M': 12, 'z': '1/4', 'budget': '1/10', 'denominator': '1000000000000000000000000000000000000000000000000000000000000', 'x': ['128631326600160450356311754099926550825090184400223475567356', '668692154901606077451728437792582080887600215272562599535767', '925673496081470978826111308071223203557525107983297003751602', '985569547743234729368936125464778593697115942478295652534410', '997311374921460599137897401643182945532448748944608754025065', '999507068742000957014659751435295649851948994805887738853024', '999910417576094279605413443794187117696364715577969526495935', '999983815131770021251151727838612417875900288862608378532755', '999997088474449178297919339424257414441169860486459258527324', '999999477997325914333043002786106648880596541007782660597182', '999999906706213337546724065798032570040291027754141111058269', '999999983530935089289358028452519876741195986752226952388905', '999999997678369825911692808062858369977852091628730413060842'], 'lam_numerator': '1803524578347813863847979800899597208605744553037452727188564'}
FAULTS=['missing_z','tail_coefficient','wrong_signal','tight_budget','negative_dual','gradient_sign','hard_tie']
def A(x):
 x=F(x);return arb(x.numerator)/arb(x.denominator)
def energy(x,w):return sum((2*ww*(1-(u*v).sqrt()-((1-u)*(1-v)).sqrt()) for u,v,ww in zip(x[:-1],x[1:],w)),arb(0))
def gradient(x,w,fault=None):
 g=[arb(0) for _ in x]
 for n,ww in enumerate(w):
  u=x[n];v=x[n+1];sgn=-1 if fault!='gradient_sign' else 1
  g[n]+=ww*(sgn*(v/u).sqrt()+((1-v)/(1-u)).sqrt())
  g[n+1]+=ww*(sgn*(u/v).sqrt()+((1-u)/(1-v)).sqrt())
 return g
def finite_certificate(fault=None):
 ctx.prec=256;M=CANDIDATE['M'];z=F(CANDIDATE['z']);b=F(1,100) if fault=='tight_budget' else F(CANDIDATE['budget']);D=int(CANDIDATE['denominator'])
 xf=[F(int(v),D) for v in CANDIDATE['x']];x=list(map(A,xf));rho=F(1,10**30);yf=[(1-rho)*v+rho/2 for v in xf];y=list(map(A,yf))
 wf=[(n+1)*z**(n if fault=='missing_z' else n+1) for n in range(M)];w=list(map(A,wf))
 cf=[(1-z)*z**n*(n*(1-z)/z-(0 if fault=='wrong_signal' else 1)) for n in range(M)]+[F(0) if fault=='tail_coefficient' else M*(1-z)*z**(M-1)]
 c=list(map(A,cf));lam=arb(-1) if fault=='negative_dual' else A(F(int(CANDIDATE['lam_numerator']),D));C=energy(x,w);Cy=energy(y,w);gr=gradient(x,w,fault);g=[cc-lam*gg for cc,gg in zip(c,gr)]
 # Interval upper endpoints bound each box support, including a gradient interval crossing zero.
 support=sum((max((gg*(1-xx)).upper(),(-gg*xx).upper()) for gg,xx in zip(g,x)),arb(0))
 U=lam*A(b)+sum((cc*xx for cc,xx in zip(c,x)),arb(0))-lam*C+support
 R=A((M+1)*(1-z)*z**M);L=sum((cc*yy for cc,yy in zip(c,y)),arb(0));upper=U+R
 checks=dict(candidate_interior=all(0<t<1 for t in xf),dual_nonnegative=lam>=0,actual_candidate_feasible=Cy<A(b),finite_lower_value=L>A(F(51042093979,10**11)),infinite_upper_value=upper<A(F(510421521,10**9)),ordered_bracket=L<upper,tail_exact=R==A(F(39,4**13)),objective_zero_on_constants=sum(cf)==0)
 # Independently differentiated single edge; an altered derivative must genuinely fail.
 u,v=sy.symbols('u v',positive=True);h=2*(1-sy.sqrt(u*v)-sy.sqrt((1-u)*(1-v)));du=sy.diff(h,u).subs({u:sy.Rational(1,4),v:sy.Rational(3,4)})
 gd=gradient([A(F(1,4)),A(F(3,4))],[arb(1)],fault)[0]
 # Exact derivative here is -2/sqrt(3).
 checks['gradient_edge']=gd.contains(-2/arb(3).sqrt()) and sy.simplify(du+2/sy.sqrt(3))==0
 return {k:bool(v) for k,v in checks.items()},dict(z=str(z),budget=str(b),M=M,feasible_energy=str(Cy),lower=str(L),finite_dual_upper=str(U),tail=str(R),infinite_upper=str(upper),precision_bits=256)
def exact_controls(fault=None):
 out={};check=lambda n,v:out.__setitem__(n,bool(v));z=sy.symbols('z',positive=True);S=z/(1-z)**2
 pgen=(1-z)/(1-z*sy.Symbol('t'))
 # Geometric derivative computes tails independently of optimization code.
 M=12;zz=sy.Rational(1,4);tail=zz**M/(1-zz)
 qtail=(1-zz)**2*sy.diff(z**M/(1-z),z).subs(z,zz)
 ptail=zz**M
 check('constant_tail_contrast',sy.simplify(qtail-ptail)==M*(1-zz)*zz**(M-1))
 RR=(M+1)*(1-zz)*zz**M
 qtail2=(1-zz)**2*sy.diff(z**(M+1)/(1-z),z).subs(z,zz)
 check('deleted_tail_bound',qtail2-zz**(M+1)==RR)
 check('summable_weight',sy.simplify(z*sy.diff(z/(1-z),z)-S)==0)
 # Nonmonotone, finitely supported changes: direct probability sum vs weighted difference.
 e=[sy.Rational(1,5),sy.Rational(4,5),sy.Rational(2,7),sy.Rational(3,4)];last=e[-1]
 d=[(1-zz)*zz**n*(n*(1-zz)/zz-1) for n in range(3)]
 direct=sum(d[n]*e[n] for n in range(3))+3*(1-zz)*zz**2*last
 byparts=(1-zz)*sum((n+1)*zz**n*(e[n+1]-e[n]) for n in range(3))
 check('summation_by_parts',direct==byparts)
 check('positive_threshold_budget',2*zz==sy.Rational(1,2))
 check('positive_threshold_contrast',1-zz==sy.Rational(3,4))
 t=sy.Integer(1) if fault=='hard_tie' else sy.Rational(1,2)
 tie=2-sy.sqrt(t)-sy.sqrt(1-t)
 check('likelihood_tie_energy',sy.simplify(tie-(2-sy.sqrt(2)))==0)
 alpha=t/4+sy.Rational(1,4);eta=t/4+sy.Rational(3,4)
 check('likelihood_tie_contrast',eta-alpha==sy.Rational(1,2))
 x,y=sy.symbols('x y',real=True);h=2*(1-sy.cos(y-x));delta=sy.sin(y)**2-sy.sin(x)**2
 check('edge_jensen_identity',sy.trigsimp(delta-sy.sin(x+y)*sy.sin(y-x))==0)
 check('edge_cost_identity',sy.trigsimp(h*(1-h/4)-sy.sin(y-x)**2)==0)
 hh=sy.symbols('h',positive=True);fun=sy.sqrt(hh-hh**2/4)
 check('jensen_concavity',sy.simplify(sy.diff(fun,hh,2)+1/(4*fun**3))==0)
 return out
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
 exact=exact_controls();interval,cert=finite_certificate();bad=[k for k,v in {**exact,**interval}.items() if not v];assert not bad,('BASELINE FAIL',bad)
 faults={}
 for f in FAULTS:
  v={**exact_controls(f),**finite_certificate(f)[0]};bad=[k for k,b in v.items() if not b];assert bad,('UNDETECTED',f);faults[f]=bad
 deps=['explorations/conditional-build/k2156-energy-budget-detector-frontier-2026-10-27.md','lab/process/k2153-diagonal-detector-energy.json','lab/process/k2151-optimal-local-mode-discrimination.json']
 report=dict(result_id='K2156',status='conditional_exact_and_interval_certificate',exact_checks=exact,interval_checks=interval,certificate=cert,fault_failures=faults,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Written compactness, convexity, infinite-tail, low-budget, Jensen and saturation proofs separately reviewed. Rational candidate certifies finite nonzero budget independent of search solver.')
 p=ROOT/'lab/process/k2156-energy-budget-detector-frontier.json'
 if args.write:p.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(p.read_text())==report,'stored report differs'
 print(json.dumps(dict(result='K2156',exact_checks=len(exact),interval_checks=len(interval),faults=len(faults),certificate=cert),indent=2))
if __name__=='__main__':main()
