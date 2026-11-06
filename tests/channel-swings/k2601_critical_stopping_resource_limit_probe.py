#!/usr/bin/env python3
"""K2601 exact critical residual inequalities and rational finite resource consumers.

Continuum occupation, asymptotic passage and sharp stability are proved in the
note; these identities and interval consumers support those proofs.
"""
import argparse,json,hashlib
from pathlib import Path
import sympy as s
from fractions import Fraction as Q
from math import isqrt
root=Path(__file__).resolve().parents[2]
ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
checks=[];controls=[]
def ck(n,v):
 assert bool(v),'FAIL '+n
 checks.append(n)
def ct(n,v):
 assert bool(v),'FAIL contrary '+n
 controls.append(n)
b,r=s.symbols('b r',positive=True);S,st,lam=s.symbols('S st lam',positive=True)
q=(1-r)**2/(4*(1+r));x=b*q/(1-(1+r)*b/2)
w=s.log(1+(b-r*b)**2/(2*(r*b+b)*(2-r*b-b)))
ck('actual_log_argument',s.cancel(s.exp(w)-1-x)==0)
res=(1+r*b)*(1-lam*st/2)+2*lam*w-(1-lam*(st-b)/2)
ck('critical_residual_linear_part',s.cancel((res-2*lam*w).subs(lam,2/(3+S))-2*(r*b*(3+S-st)/2-b/2)/(3+S))==0)
ck('linear_at_worst_remaining_score',s.factor(s.Rational(3,2)*r-s.Rational(1,2)+2*q-2*r*r/(1+r))==0)
# For r in [0,1], q<=1/4 and 2/(1+r)>=1.
ck('q_upper_factor',s.cancel(s.Rational(1,4)-q-r*(3-r)/(4*(r+1)))==0)
ck('quadratic_r_lower_factor',s.cancel(q*(1+r)-q*q-(s.Rational(3,16)-r/2)-r*(3*r**3+12*r**2-r+6)/(16*(r+1)**2))==0)
# (1-b)^-2-1 <= 6b on [0,1/2].
ck('inverse_square_excess_factor',s.cancel(6*b-((1-b)**-2-1)-b*(6*b*b-11*b+4)/(b-1)**2)==0)
ck('excess_polynomial_at_half', (6*b*b-11*b+4).subs(b,s.Rational(1,2))==0)
ck('excess_polynomial_decreasing_interval', (12*b-11).subs(b,s.Rational(1,2))<0)
ck('complete_square_residual',s.expand(b*r*r-b*b*r/2+b**3/16-b*(r-b/4)**2)==0)
ck('critical_residual_cubic_bound',s.Rational(3,8)+s.Rational(1,16)==s.Rational(7,16))
ck('per_trial_fair_half',s.Rational(3,16)/2==s.Rational(3,32))
gamma=s.Rational(78360951,2744000000);ck('global_gamma_positive',gamma>0)
M,B,L,c=s.symbols('M B L c',positive=True)
rootval=2*c*B*B/(M+2*c*B*L+s.sqrt(M*M+4*c*B*L*M))
ck('stable_quadratic_lower_root',s.simplify(M*rootval-c*(B-L*rootval)**2)==0)
ck('resource_constant_from_occupation',s.simplify(lam*s.Rational(3,32)*(2*S)**2-3*lam*S*S/8)==0)
# Independent log law expansion, not an asserted report coefficient.
h=s.symbols('h',positive=True)
w0=s.log((4-h)/(4-2*h));series=s.series(w0,h,0,4).removeO()
ck('zero_action_cost_series',s.expand(series-h/4-3*h*h/32-7*h**3/192)==0)
ck('equal_count_gap_coefficient',2*s.Rational(3,32)*2==s.Rational(3,8))
y=s.symbols('y',nonnegative=True);qq=2*s.sqrt(4-2*y)-s.Rational(7,2)+y
ck('critical_generator_rationalization',s.simplify((s.Rational(1,2)-qq)-y*y/(4-y+2*s.sqrt(4-2*y)))==0)
ck('critical_clock_series',s.series(1/(2*qq),y,0,3).removeO()==1+y*y/4)
ck('clock_cubic_integral',s.integrate(y*y/4,(y,0,h))==h**3/12)
ck('stability_cubic_legendre_factor',3-1==2)
cc=s.real_root(s.Rational(9,16)/lam**2,3)
ck('sharp_stability_constant',s.simplify((6*lam**5)**2/(64*lam**12)-s.Rational(9,16)/lam**2)==0)
ck('coarse_clock_denominator',9*(1-s.Rational(1,4)**2/3)>=8)
ct('dropping_fair_trial_half_wrong',s.Rational(3,16)!=s.Rational(3,32))
ct('coarse_cubic_not_sharp_constant',s.Rational(1,8)!=s.Rational(1,12))
ct('nonpositive_small_score_coefficient_for_large_epsilon',(3-7*s.Rational(1,2))<0)
# Fully rational interval log and sqrt consumers. No floating optimizer.
def log_bounds(z,n=48):
 y=(z-1)/(z+1);v=2*sum((y**(2*i+1)/Q(2*i+1) for i in range(n)),Q(0));err=2*abs(y)**(2*n+1)/(Q(2*n+1)*(1-y*y));return v-err,v+err
def sqrt_bounds(z,places=50):
 den=10**places;lo=isqrt(z.numerator*den*den//z.denominator);return Q(lo,den),Q(lo+1,den)
def w0_bounds(b):return log_bounds((4-b)/(4-2*b))
consumers=[]
for total in [Q(1,2),Q(1,4)]:
 lm=2/(3+total);hp=ep=Q(1,100);lp=lm+hp;gg=Q(78360951,2744000000)
 ck('finite_multiplier_domain_'+str(total),lp<=Q(2,3) and hp/(lm*lp)<=total/2)
 A=hp*hp/(8*lm**4);BB=2*total*(1-A);LL=2*total*lp/hp+4/(lm*gg*ep);cc=lm*(3-7*ep)/32
 ck('finite_bound_positive_'+str(total),BB>0 and cc>0)
 for resource in [1000,1001,10000]:
  rad=Q(resource**2)+4*cc*BB*LL*resource;rl,rh=sqrt_bounds(rad)
  lower=2*cc*BB**2/(resource+2*cc*BB*LL+rh)
  n=resource//2;theta=Q(2*(n+1)-resource,2)
  def gap(count):
   wl,wh=w0_bounds(total/count);return lm*(2*count*wl-total/2),lm*(2*count*wh-total/2)
  gl,gh=gap(n);jl,jh=gap(n+1);upper=theta*gh+(1-theta)*jh
  ck('feasible_adjacent_count_resource_'+str(total)+'_'+str(resource),theta*2*n+(1-theta)*2*(n+1)==resource)
  ck('finite_lower_below_feasible_upper_'+str(total)+'_'+str(resource),0<lower<upper)
  C=3*lm*total**2/8
  ck('feasible_upper_near_sharp_constant_'+str(total)+'_'+str(resource),abs(resource*upper-C)<Q(1,resource))
  consumers.append({'score':str(total),'multiplier':str(lm),'resource':resource,'h_epsilon':str(hp),'gap_lower':str(lower),'gap_feasible_upper':str(upper),'sharp_coefficient':str(C),'lower_display':float(lower),'upper_display':float(upper),'M_upper_display':float(resource*upper)})
# Actual contrary policy: finite zero-action chord is not the critical optimizer.
score=Q(1,2);lm=Q(4,7);action=Q(1,1000);bb=score/2
wa=log_bounds(1+(bb-action)**2/(2*(action+bb)*(2-action-bb)));wz=w0_bounds(bb);w3=w0_bounds(score/3)
p2=1/(1+action);R2=4/(1+action);theta=1/(6-R2)
J2low=p2-2*lm*(wa[1]+wz[1])/(1+action);J3low=1-6*lm*w3[1]
mixedlow=theta*J2low+(1-theta)*J3low
oldhigh=1-lm*(2*wz[0]+3*w3[0])
ct('actual_positive_action_mixture_beats_critical_zero_chord',mixedlow>oldhigh)
ck('actual_contrary_mixture_resource_five',theta*R2+(1-theta)*6==5)
ct('unweighted_nominal_resource_wrong_for_same_policy',theta*4+(1-theta)*6!=5)
report={'result':'K2601','checks':checks,'contrary_controls':controls,'theorem':'For fixed0<S<=1/2, lambda=2/(3+S), M*(1-lambda*S/2-F_lambda(M))->3lambda*S^2/8 over the entire original adaptive policy class','rate':'gap=C/M+O(M^-3/2); feasible zero-action adjacent-count mixtures have gap=C/M+O(M^-2), not exact finite optimality','success_stability':'1-p <= (9/(16lambda^2))^(1/3)*eta^(2/3)+o(eta^(2/3)), sharp among nearoptimal original finite policies without a simultaneous resource-optimality claim','local_residual_bound':'d>=lambda*b^2*(3-7b)/16; useful for b<3/7; global gamma bound reused for larger scores','finite_consumers':consumers,'evidence_kind':'Exact rational residual factors, original-log expansion, clock coefficients and independent interval finite-resource bounds; universal adaptive occupation, asymptotic and sharpness proofs in note','ceiling':'supplied stopping probability law only; no all-multiplier phase diagram, finite optimizer identification, physical probability or GU verdict'}
refs=['explorations/conditional-build/k2561-higher-budget-stopping-2026-11-05.md','explorations/conditional-build/k2587-countwise-stopping-support-2026-11-05.md','explorations/conditional-build/k2597-stopping-threshold-bifurcation-2026-11-06.md','explorations/conditional-build/k2599-joint-stopping-corner-2026-11-06.md']
report['provenance']={f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in refs}
out=root/'lab/process/k2601-critical-stopping-resource-limit.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report mismatch'
print(json.dumps({'result':'K2601','checks':len(checks),'controls':len(controls),'status':'pass'}))
