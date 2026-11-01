"""Sharp original binary compensator: exact identities and Arb256 contrary laws."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import json,hashlib,sys
from flint import arb,ctx
ctx.prec=256
ROOT=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ctrl(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
def ar(v):
 v=F(v);return arb(v.numerator)/v.denominator
c=arb(2).log();L=c-ar(F(1,2));J=(1-c)/2;Cs=(1+L)**2/(4*L);gamma=2*Cs
old=(arb(1)/2+J/2)**2/J
ck('strict_coefficient_improvement',ar(F(9,5))<Cs<2<old)
ck('exact_log_bounds',ar(F(56,81))<c<ar(F(25,36)))
ck('simplex_first_moment_lower',ar(F(2,3))**3/12>ar(F(3,125)))
ck('simplex_first_moment_upper',ar(F(7,10))**3/6<ar(F(3,50)))
ck('simplex_second_moment_upper',ar(F(7,10))**4/12<ar(F(21,1000)))
ck('convexity_rational_margin',2*F(3,25)**2+2*F(2,5)*F(3,80)-2*F(21,1000)==F(21,1250))
ck('left_endpoint_margin',ar(F(289,240))<ar(F(9,5))<Cs)
ck('right_endpoint_identity',((1+L)**2/4-Cs*L).contains(0))
# These finite inequalities support code/formula reproduction; universal proof is written.
for ai in range(21):
 for bi in range(21):
  a=F(ai,20);b=F(bi,20);d=max(b-a,F(0));q=a+d/2
  v=d*d/(4*q*(1-q)) if 0<q<1 else F(0)
  G=(1-ar(a))/2+(c*ar(b)-c).exp()
  if a==b and a in (0,1):ck(f'endpoint_{ai}',(G-1).contains(0));continue
  ck(f'moment_{ai}_{bi}',G<1+Cs*ar(v))
  if v:ck(f'log_transfer_{ai}_{bi}',(1+Cs*ar(v)).log()<gamma*(1+ar(v)/2).log())
  if d:
   B=b*(1-b);ck(f'original_q_identity_{ai}_{bi}',B==d*d/(4*v)-(2*b-1)*d/2+d*d/4)
# Sharpness sequence is on original probabilities, no surrogate quadratic law.
t=4*L/(1-L);limits=[]
for exponent in [3,6,12,24]:
 z=arb(10)**(-exponent);b=1-z;d=t*z;a=b-d;q=b-d/2;v=d*d/(4*q*(1-q));G=(1-a)/2+(c*b-c).exp()
 ck('sharp_admissible_'+str(exponent),0<a<b<1 and v>0)
 ratio=(G-1)/v;tr=G.log()/(1+v/2).log();limits.append({'z':str(z),'linear_ratio':str(ratio),'budget_ratio':str(tr)})
 ck('sharp_approach_'+str(exponent),ratio<Cs and ratio>Cs-ar(F(100,10**exponent)))
 ck('transfer_approach_'+str(exponent),tr<gamma and tr>gamma-ar(F(300,10**exponent)))
a=F(49,50);b=F(99,100);d=b-a;q=(a+b)/2;v=d*d/(4*q*(1-q));G=(1-ar(a))/2+(c*ar(b)-c).exp()
ck('counterpair_original_v',v==F(1,591));ctrl('too_small_9_over5_coefficient',G>1+ar(F(9,5)*v))
ctrl('unit_original_transfer_fails',F(5,4)>1+F(1,6))
ctrl('signed_log_refunds',arb(1)/4+arb(2).sqrt()/2<1)
# Exact geometric waiting law: mean m/u; finite partial sum plus exact remainder.
u=F(1,2)
for N in [1,4,20]:
 expectation=sum(F(k,2**k) for k in range(1,N+1));remainder=F(N+2,2**N)
 ck('geometric_mean_tail_'+str(N),expectation+remainder==2)
# Actual binary rare-mode violation of half expected-H confidence penalty.
epsilon=F(1,20);p=F(3,50);delta=F(1,100);m=10000
hdelta=(arb(1)/2+(c*ar(delta)).exp()/2).log();Kh=ar(p*m/u)*hdelta;Z=c*ar(delta*m)
threshold=(1/ar(epsilon)).log()+Kh/(2*ar(epsilon))
ctrl('actual_binary_half_penalty_fails',p>epsilon and Z>threshold)
ck('proper_expected_threshold_covers',Z<(1/ar(epsilon)).log()+Kh/ar(epsilon))
ck('binary_ratio_approaches_one',ar(F(99,100))<ar(u)*c*ar(delta)/hdelta<1)
# Original-budget necessary coefficient is distinct from exact-H sharpness.
for expn in [3,6,12]:
 delta0=arb(10)**(-expn);q0=delta0/2;v0=q0/(1-q0);cost=(1+v0/2).log()
 ratio=ar(u)*c*delta0/cost
 ck('original_budget_lower_limit_'+str(expn),ratio<2*c and ratio>2*c-ar(F(10,10**expn)))
ck('expected_original_gap_stays_open',2*c<gamma)
# Original success-weighted output consumer; same calibration and heralding premises.
e=(F(1,100)-F(1,1000000)/F(1,4))/2;beta=F(1,100000000);outcomes=[]
for budget_kind,mult in [('pathwise',1),('expected',20)]:
 for nu0 in [F(2,5),F(9,20)]:
  D=nu0*e*e-beta;num=arb(20).log()+gamma*ar(F(mult,1000000));realn=num/(c*ar(D));n=int(realn.upper().ceil().unique_fmpz())
  ck('count_'+budget_kind+'_'+str(nu0),n>=realn and n-1<realn)
  oldreal=(arb(20).log()+2*old*ar(F(mult,1000000)))/(c*ar(D))
  ck('continuous_improvement_'+budget_kind+'_'+str(nu0),realn<oldreal)
  ck('positive_actual_success_'+budget_kind+'_'+str(nu0),ar(F(1,4))-(2*((num/(c*n)+ar(beta))/ar(nu0)).sqrt()+ar(F(1,1000000)))>0)
  outcomes.append({'budget':budget_kind,'gap':str(nu0),'uses':n,'continuous':str(realn),'old_continuous':str(oldreal)})
note='explorations/conditional-build/k2465-sharp-leakage-compensator-2026-11-01.md'
deps=[note,str(Path(__file__).relative_to(ROOT)),'explorations/conditional-build/k2459-direct-leakage-certificate-2026-11-01.md','explorations/conditional-build/k2462-expected-leakage-certificate-2026-11-01.md']
report={'result_id':'K2465','checks':checks,'controls':controls,'Cstar':str(Cs),'gamma_star':str(gamma),'original_sharpness_sequence':limits,'actual_binary_half_penalty_counterlaw':{'epsilon':str(epsilon),'rare_probability':str(p),'m':m,'delta':str(delta),'expected_exact_H':str(Kh),'crossing_Z':str(Z),'false_threshold':str(threshold)},'prospective_consumers':outcomes,'evidence_kinds':{'universal':'divided-difference/convexity sharp coefficient proof; exact compensator/Jensen and actual binary sharpness','finite':'original binary laws, exact geometric mean, Arb256 coefficients and counts','ceiling':'fixed parameters only; expected original-B minimax gap remains; no measured leakage'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}}
out=ROOT/'lab/process/k2465-sharp-leakage-compensator.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('K2465',len(checks),'checks',len(controls),'controls PASS',json.dumps(outcomes))
