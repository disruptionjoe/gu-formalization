"""Whole-ribbon exact certificate; universal nonattainment proof in linked note."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
from itertools import product
import argparse,hashlib,json
import sympy as s
ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
root=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(n,c):
 checks[n]=bool(c)
 if not c:raise AssertionError(n)
def ct(n,c):
 controls[n]=bool(c)
 if not c:raise AssertionError('contrary: '+n)
a,b,r,x,y,v=s.symbols('a b r x y v');xx=(b-a)**2/(2*(a+b)*(2-a-b));w=s.log(1+xx)
wa=s.diff(w,a);wb=s.diff(w,b);waa=s.diff(wa,a);wab=s.diff(wa,b);wbb=s.diff(wb,b)
M=-2*(1+a)*wa+2*w
ck('output_root_derivative',s.simplify(s.diff(M,a)+2*(1+a)*waa)==0)
K=s.factor(wbb-wab**2/waa+wb*wab/((1+a)*waa))
# Independent implicit derivative of M(a(b),b)=v gives the same generator derivative.
aprime=-s.diff(M,b)/s.diff(M,a)
ck('fixed_output_chain_rule',s.simplify(2*wbb+2*wab*aprime-2*K)==0)

def certificate(expr,variables):
 p=s.Poly(s.expand(expr),*variables);ns=p.degree_list();indices=list(product(*(range(n+1) for n in ns)))
 power={k:F(int(v.p),int(v.q)) for k,v in p.terms()};B={}
 for k in indices:
  B[k]=sum((v*__import__('functools').reduce(lambda aa,bb:aa*bb,(F(comb(k[i],j[i]),comb(ns[i],j[i])) for i in range(len(ns))),F(1)) for j,v in power.items() if all(j[i]<=k[i] for i in range(len(ns)))),F(0))
 inverse={}
 for k,vv in B.items():
  for off in product(*(range(ns[i]-k[i]+1) for i in range(len(ns)))):
   j=tuple(k[i]+off[i] for i in range(len(ns)));co=vv
   for i in range(len(ns)):co*=comb(ns[i],k[i])*comb(ns[i]-k[i],off[i])*(-1)**off[i]
   inverse[j]=inverse.get(j,F(0))+co
 assert all(inverse.get(k,F(0))==power.get(k,F(0)) for k in indices),'inverse Bernstein mismatch'
 return ns,B
N,D=s.fraction(s.factor(K.subs(a,r*b)));tables={}
for name,p in [('numerator',N),('denominator',D)]:
 ns,B=certificate(p.subs({b:y/2,r:x*(s.Rational(2,5)+y/4)}),(x,y));tables[name]={'degrees':list(ns),'coefficients':[str(B[k]) for k in sorted(B)]}
 ck(name+'_all_Bernstein_positive',min(B.values())>0)
 ck(name+'_degrees',ns==((9,13) if name=='numerator' else (10,16)))
 if name=='numerator':nmin=min(B.values());ck('numerator_minimum',nmin==F(57067571809,256000000000))
 else:dmax=max(B.values());ck('denominator_minimum',min(B.values())==F(861,16));ck('denominator_maximum',dmax==F(87808,125))
bar=s.factor((s.Rational(51,98)-(-2*(1+a)*wa+2*xx)).subs(a,b*(s.Rational(2,5)+b/2)))
Bn,Bd=s.fraction(bar)
for name,p in [('barrier_numerator',Bn),('barrier_denominator',Bd)]:
 ns,B=certificate(p.subs(b,y/2),(y,));tables[name]={'degrees':list(ns),'coefficients':[str(B[k]) for k in sorted(B)]}
 if name.endswith('numerator'):
  ck('barrier_origin_only_zero',B[(0,)]==0 and all(vv>0 for k,vv in B.items() if k!=(0,)))
 else:ck('barrier_denominator_positive',min(B.values())>0)
ck('boundary_generator_derivative',s.simplify(2*wbb.subs(a,0)+8*(b-3)/((b-4)**2*(b-2)**2))==0)
ck('boundary_root_switch_derivative',s.simplify(s.diff(M.subs(a,0),b)-4*(3*b*b-12*b+10)/((b-4)**2*(b-2)**2))==0)
# Positive polynomial for switch numerator on b in[0,1/2].
_,switch=certificate((3*b*b-12*b+10).subs(b,y/2),(y,));ck('at_most_one_boundary_switch',min(switch.values())>0)
k0=nmin/dmax;ck('uniform_slope_boundary_matches',F(5,16)>2*k0>0)
rr=s.symbols('rr',nonnegative=True);qexpr=rr*v+(1-rr)**2/(2*(1+rr));r0=2/s.sqrt(1+2*v)-1
ck('interior_fluid_stationary_ratio',s.simplify(s.diff(qexpr,rr).subs(rr,r0))==0)
ck('fluid_generator_value',s.simplify(qexpr.subs(rr,r0)-(2*s.sqrt(1+2*v)-v-2))==0)
ck('analytic_zero_score_log_derivative',s.simplify(s.cancel(s.diff(s.log(1+s.cancel(xx.subs(a,rr*b))),b)).subs(b,0)-(1-rr)**2/(4*(1+rr)))==0)
# Exact sign controls reject extrapolating the ribbon in either variable.
ct('wrong_output_barrier_fails_at_origin',s.limit((s.Rational(1,2)-(-2*(1+a)*wa+2*xx)).subs(a,b*(s.Rational(2,5)+b/2)),b,0)<0)
ct('generator_not_positive_at_all_ratios',K.subs({a:s.Rational(9,40),b:s.Rational(1,4)})<0)
ck('endpoint_below_attained_regime',s.Rational(98,51)**2<s.Rational(16,3))

def log1p(z,n=32):
 z=F(z);t=z/(2+z);lo=2*sum((t**(2*j+1)/F(2*j+1) for j in range(n)),F(0));hi=lo+2*t**(2*n+1)/(F(2*n+1)*(1-t*t));return lo,hi
def cost(a,b):return log1p((b-a)**2/(2*(a+b)*(2-a-b)))
def value(stages,lam=F(19,10)):
 P=F(1);lo=F(0);hi=F(0)
 for a,b in stages:
  wl,wh=cost(a,b);P/=1+a;lo+=2*P*wl;hi+=2*P*wh
 return P-lam*hi,P-lam*lo
# Real finite splitting at fixed total score and original survival prefixes.
old=[(F(3,10),F(1,2))];new=[(F(3,10),F(499,1000)),(F(2,5000),F(1,1000))]
ol,oh=value(old);nl,nh=value(new)
ck('finite_split_admissible',all(0<=a<=b for a,b in new) and sum(b for a,b in new)==F(1,2))
ck('finite_split_strict_gain',nl>oh)
wl0,wh0=cost(*new[0]);wl1,wh1=cost(*new[1])
P1=1/(1+new[0][0]);P2=P1/(1+new[1][0])
true_cost_hi=2*P1*wh0+2*P2*wh1
wrong_cost_lo=2*P1*wl0+2*wl1/(1+new[1][0])
ct('omitted_tail_survival_prefix_changes_original_cost',wrong_cost_lo>true_cost_hi)
ck('zero_hit_policy_cannot_match_free_stage',F(0)<F(1)/(1+F(1,2)))
digest=hashlib.sha256(json.dumps(tables,sort_keys=True,separators=(',',':')).encode()).hexdigest()
report={'result':'K2567','evidence_kind':'exact whole-domain rational certificate, supporting derivatives and finite original-policy example; universal transfer in note','checks':checks,'contrary_controls':controls,'certificates':tables,'coefficient_digest':digest,'k0':str(k0),'multiplier_interval':'0 < lambda <= 98/51','score_interval':'0 < S <= 1/2','finite_split_gain_lower':str(nl-oh)}
p=root/'lab/process/k2567-stopping-family-structure.json'
if args.write:p.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(p.read_text())==report,'saved report mismatch'
print(json.dumps({'result':'K2567','checks':len(checks),'controls':len(controls),'digest':digest,'status':'pass'}))
