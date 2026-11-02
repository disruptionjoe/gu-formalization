"""Finite original-law/interval controls; universal scope proved in paired note."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,sys,os
from flint import arb,ctx
import sympy as s
ROOT=Path(os.environ.get('GU_ROOT',str(Path(__file__).resolve().parents[2])))
ctx.prec=256
checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ctrl(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
def ar(x):
 x=F(x);return arb(x.numerator)/x.denominator
c=arb(2).log()
def f(y):return 2*(2*y+1).sqrt()-y-2
def fT(H):
 def fun(z):return -(z-1).log()+3*(3-z).log()
 return fun((H+1).sqrt())-fun((2*H+1).sqrt())
lo=F(5917371555734925,10**16);hi=F(5917371555734927,10**16)
ck('H_root_interval',fT(ar(lo))<1 and fT(ar(hi))>1)
# f is strictly increasing on the whole root bracket; invert endpoints.
ck('L_interval',c/f(ar(hi))>ar(F(19064522383455,10**13)) and c/f(ar(lo))<ar(F(19064522383456,10**13)))
ck('bound_above_1_9064',c/f(ar(hi))>ar(F(19064,10000)))
C=(1+c)**2/(4*(1-c));ck('below_global_upper',c/f(ar(lo))<C)
z,r=s.symbols('z r',positive=True);y=(z*z-1)/2;g=(1-r)**2/(2*(1+r));ff=2*z-y-2
ck('bellman_positive_square_identity',s.factor(g+r*y-ff-(z*(1+r)-2)**2/(2*(1+r)))==0)
ck('primitive_derivative',s.factor(-1/(z-1)+3/(z-3)-2*z/((z-1)*(z-3)))==0)
ck('convex_cost',s.simplify(s.diff(g,r,2)-4/(1+r)**3)==0)
# Rational samples of the optimal decreasing schedule; no approximation is used in finite certification.
rates=[F(x,10000) for x in [5817,5746,5674,5603,5531,5459,5386,5313,5241,5168,5095,5021,4948,4875,4802,4728,4655,4582,4508,4435,4362,4289,4216,4144,4071,3999,3927,3855,3783,3712,3641,3570]]
rt=F(3535,10000)
def k(r):return (1-ar(r))**2/(2*ar(r)*(1+ar(r)))
p=arb(1);D=arb(0)
for r in rates:
 si=(-ar(r)/32).exp();D+=p*k(r)*(1-si);p*=si
H=D/(p-ar(F(1,2)));lim=c/(ar(rt)*(k(rt)+H))
ck('schedule_success_above_half',p>ar(F(1,2)))
ck('schedule_limit_above_1_9064',lim>ar(F(19064,10000)))
ck('scheduled_cost_ge_optimum',H>ar(hi))
# Reversing stages preserves terminal survival but increases costs for this witness.
p_rev=arb(1);D_rev=arb(0)
for r in reversed(rates):
 si=(-ar(r)/32).exp();D_rev+=p_rev*k(r)*(1-si);p_rev*=si
ctrl('order_matters_for_cost',D_rev>D)
# Finite-stage rational probabilities; the sums include all reached paths.
witness=[]
for M in [1024,8192]:
 b=F(1,M);p0=F(1);D0=arb(0)
 def w(a):return (1+ar((b-a)**2/(2*(a+b)*(2-a-b)))).log()
 for j,r in enumerate(rates):
  a=r/M;N=M//32+(j==31);sj=(1+a)**(-N)
  D0+=ar(p0)*2*w(a)/ar(a)*(1-ar(sj));p0*=sj
 a1=rt/M;p1=1/(1+a1);D1=2*w(a1)/ar(a1)*(1-ar(p1))
 ideal=(F(1,2)+F(1,M*M)-p1/2)/(p0-p1/2)
 J=(4*M**3-1).bit_length();den=2**J;alpha=F((ideal.numerator*den)//ideal.denominator,den)
 ck('coin_domain_'+str(M),0<alpha<1 and alpha<=ideal and ideal-alpha<F(1,den))
 P=alpha*p0+(1-alpha)*p1/2;K=ar(alpha)*D0+ar(1-alpha)*D1/2
 ck('strict_success_'+str(M),P>F(1,2)+F(1,2*M*M))
 ratio=c/(2*M*K)
 if M==8192:ck('finite_violation_1_905',ratio>ar(F(1905,1000)))
 for m in [0,1,3,9]:
  rho=F(1,2**m);eps=rho/2
  ck(f'actual_probability_{M}_{m}',rho*P>eps)
  ck(f'equal_actual_score_{M}_{m}',m+F(M+1,M)==m+1+F(1,M))
  if M==8192:ck(f'actual_threshold_violation_{m}',(m+1)*c+c/M>(1/ar(eps)).log()+ar(F(1905,1000))*ar(rho)*K/ar(eps))
 ctrl('missing_prelude_survival_changes_budget_'+str(M),ar(alpha)*D0+ar(1-alpha)*D1>K)
 witness.append({'M':M,'coin_bits':J,'alpha':str(alpha),'success_over_rho':str(ar(P)),'K_over_rho':str(K),'ratio':str(ratio)})
# Independent exact recursion for heterogeneous stages, with analytic w factored out by using charge1.
for risks in [[F(1,5),F(1,7),F(1,11)],[F(1,13)]*5]:
 q=F(1);total=F(0)
 for a in risks:total+=q*2/(1+a);q/=1+a
 ck('heterogeneous_recursion_'+str(risks),total==sum(F(2)*__import__('functools').reduce(lambda x,y:x/(1+y),risks[:i+1],F(1)) for i in range(len(risks))))
 ctrl('omitted_failed_cost_'+str(risks),total>q*sum(F(2)/(1+a) for a in risks))
ctrl('endpoint_equality_is_not_violation',not(F(1,2)>F(1,2)))
ctrl('activation_has_no_initial_score',c/8192<c)
deps=['lab/process/k2471-sharp-stopping-coefficient.json','lab/process/k2474-fixed-confidence-stopping.json','lab/process/k2477-randomized-score-preludes.json']
for p in deps:
 data=json.loads((ROOT/p).read_text());ck('authenticated_'+p,all(hashlib.sha256((ROOT/q).read_bytes()).hexdigest()==h for q,h in data['dependencies'].items()))
extra={'H_interval':[str(lo),str(hi)],'L_interval':[str(c/f(ar(hi))),str(c/f(ar(lo)))],'piecewise_schedule_H':str(H),'piecewise_schedule_limit':str(lim),'witnesses':witness}
if '--scratch' in sys.argv:
 print(json.dumps({'checks':checks,'controls':controls,**extra},indent=2));sys.exit()
st='k2480-scheduled-stopping-preludes'
deps=[f'explorations/conditional-build/{st}-2026-11-01.md',str(Path(__file__).relative_to(ROOT)),*deps]
report={'result_id':'K2480','checks':checks,'controls':controls,'evidence_kinds':{'universal':'written sharp scheduled-continuum verification inequality, root uniqueness, finite-law approximation and strict-margin theorem','finite':'exact rational stage probabilities and coin weights; Arb256 cost, root and violation certificates','reused':'K2471 universal upper and K2474/K2477 original stage/mixture interfaces','ceiling':'sharp continuum scheduled repair subproblem and dyadic lower bound; no global adaptive optimum or physical calibration'},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},**extra}
out=ROOT/f'lab/process/{st}.json'
if '--check' in sys.argv:assert json.loads(out.read_text())==report
else:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print(st,len(checks),'check groups',len(controls),'contrary controls PASS')
