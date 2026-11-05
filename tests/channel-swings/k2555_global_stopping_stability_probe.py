"""Exact supporting algebra and finite controls; universal stability proof in K2555."""
from pathlib import Path
from math import comb
from itertools import product
import sympy as s
import mpmath as mp
import hashlib,json,sys
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(name,ok):
 checks[name]=bool(ok)
 if not ok:raise AssertionError(name)
def ct(name,ok):
 controls[name]=bool(ok)
 if not ok:raise AssertionError(name)
a,b,r,y=s.symbols('a b r y');D=2*(a+b)*(2-a-b);N=D+(b-a)**2
wa=s.cancel(s.diff(N,a)/N-s.diff(D,a)/D);waa=s.diff(wa,a)
# Exact independent whole-domain lower bound on action curvature.
num,den=s.fraction(s.factor((b*waa-s.Rational(1,4)).subs(a,r*b)))
def bern(expr):
 p=s.Poly(expr.subs(b,y/2),r,y);n,m=p.degree_list();cs=dict(p.terms());grid=[]
 for i in range(n+1):
  grid.append([sum(c*s.Rational(comb(i,k),comb(n,k))*s.Rational(comb(j,l),comb(m,l)) for (k,l),c in cs.items() if k<=i and l<=j) for j in range(m+1)])
 # Reconstruct polynomial using explicit Bernstein basis, independent of forward conversion.
 reconstructed=sum(grid[i][j]*comb(n,i)*r**i*(1-r)**(n-i)*comb(m,j)*y**j*(1-y)**(m-j) for i in range(n+1) for j in range(m+1))
 ck('inverse_basis_'+str(len(checks)),s.Poly(reconstructed-p.as_expr(),r,y).is_zero)
 return p.degree_list(),[v for row in grid for v in row]
nd,nv=bern(num);dd,dv=bern(den)
ck('curvature_numerator_nonnegative',all(v>=0 for v in nv))
ck('curvature_denominator_positive',all(v>0 for v in dv))
ct('corrupt_curvature_bound_rejected',min([v-1 for v in nv])<0)
wb=s.cancel(s.diff(N,b)/N-s.diff(D,b)/D)
cn,cd=s.fraction(s.factor((s.Rational(1,2)-wb).subs(a,r*b)))
cnd,cnv=bern(cn);cdd,cdv=bern(cd)
ck('collapse_derivative_upper_whole_domain',all(v>=0 for v in cnv) and all(v>0 for v in cdv))
ck('collapse_derivative_lower_factor',s.expand(2*D-(b-a)*s.diff(D,b)-4*(b+a*(3-2*(a+b))))==0)
ck('satellite_cost_bound',s.Rational(1,3)==1/(4-2*s.Rational(1,2)))
q0,wM,wS,aa=s.symbols('q0 wM wS aa')
ck('collapse_cost_decomposition',s.cancel(2*wS/(1+aa)-2*q0*wM/(1+aa)-2*((wS-wM)+(1-q0)*wM)/(1+aa))==0)
ck('stronger_D_bound_factorization',s.expand(8*b*(1-b)-D-2*(b-a)*(2-a-3*b))==0)
# 2-a-3b >= 0 on a<=b<=1/2. This plus K2509's algebra proves stronger bound.
ck('stronger_D_remaining_factor',s.expand(2-a-3*b-(2-4*b)-(b-a))==0)
Dprime=s.diff(D,a);Nprime=s.diff(N,a)
ck('original_log_curvature_identity',s.cancel(waa-(4/D-2/N+Dprime**2/D**2-Nprime**2/N**2))==0)
B,C,T=s.symbols('B C T');ck('adjacent_exchange',s.expand(B*(C+T)**2+C*T*T-C*(B+T)**2-B*T*T-B*C*(C-B))==0)
S,M=s.symbols('S M');ck('global_concentration_factor',s.expand(S**3/3-M*S*S/2+M**3/6-(S-M)**2*(2*S+M)/6)==0)
ck('global_concentration_lower',s.expand((S-M)**2*(2*S+M)/6-S*(S-M)**2/3-M*(S-M)**2/6)==0)
# Exact finite fixtures probe algebra, ordering, edge cases and bounds; not universal proof.
fixture_count=0
for n in range(1,5):
 for raw in product(range(1,4),repeat=n):
  bs=[s.Rational(v,2*sum(raw)) for v in raw];ss=sum(bs);ts=[sum(bs[i+1:]) for i in range(n)]
  ee=sum(x*t*t for x,t in zip(bs,ts));mm=max(bs);j=bs.index(mm);ll=sum(bs[:j]);dd0=ss-mm
  assert s.expand(ss**3/3-ee-sum(x*x*t for x,t in zip(bs,ts))-sum(x**3 for x in bs)/3)==0
  assert ee>=dd0**2*(2*ss+mm)/6 and ee>=mm*dd0**2 and ee>=ss**2*ll/6
  assert ee>=ll*mm*mm
  fixture_count+=1
ck('exact_finite_moment_and_order_fixtures',fixture_count==120)
ct('order_cannot_be_discarded',s.Rational(1,10)*s.Rational(2,5)**2>s.Rational(2,5)*s.Rational(1,10)**2)
ct('unit_constant_concentration_false',s.Rational(1,4)**3<s.Rational(1,2)*s.Rational(1,4)**2)
a1,a2,w1,w2,U0,U1,lam=s.symbols('a1 a2 w1 w2 U0 U1 lam');p1=1/(1+a1);p2=p1/(1+a2)
ck('original_prefix_deficit_identity',s.factor(p1*((1+a1)*U0+2*lam*w1-U1)+p2*((1+a2)*U1+2*lam*w2-1)-(U0-p2+2*lam*(p1*w1+p2*w2)))==0)
ct('unweighted_cost_is_different',s.factor(w1+w2-p1*w1-p2*w2)!=0)
pstar,eps,cstar,cost,prob=s.symbols('pstar eps cstar cost prob')
eta=pstar-lam*cstar-prob+lam*cost
ck('contact_deficit_identity',s.expand(eta-(pstar-prob-lam*(cstar-cost)))==0)
ck('dominant_action_upper_identity',s.cancel(1/(pstar-eps)-1/pstar-eps/(pstar*(pstar-eps)))==0)
weight,e1,e2=s.symbols('weight e1 e2');ck('mixture_deficit_linearity',s.expand(weight*e1+(1-weight)*e2-(e2+weight*(e1-e2)))==0)
budget,slack=s.symbols('budget slack',positive=True);theta=budget/(budget+slack)
ck('exact_budget_repair_cost',s.cancel(theta*(budget+slack)-budget)==0)
ck('exact_budget_repair_loss',s.cancel(1-theta-slack/(budget+slack))==0)
ct('zero_budget_repair_needs_case',theta.subs({budget:0,slack:0},simultaneous=True) is s.nan)
# Illustrative original-law values only; numerical root is NOT part of proof.
mp.mp.dps=60;lm=4/mp.sqrt(3);score=mp.mpf('.5')
def w0(aa,bb):return mp.log1p((bb-aa)**2/(2*(aa+bb)*(2-aa-bb)))
def c0(aa):return 2*w0(aa,score)/(1+aa)
def froot(aa):return -2*(1+aa)*mp.diff(lambda z:w0(z,score),aa)+2*w0(aa,score)-1/lm
lo=mp.mpf(0);hi=score
for _ in range(220):
 mid=(lo+hi)/2
 if froot(mid)>0:lo=mid
 else:hi=mid
astar=(lo+hi)/2;cs=c0(astar);mix_weight=cs/c0(mp.mpf(0))
ct('expected_budget_not_component_budget',0<mix_weight<1 and c0(0)>cs and c0(score)<cs)
ck('illustrative_contact_mixture_budget',abs(mix_weight*c0(0)+(1-mix_weight)*c0(score)-cs)<mp.mpf('1e-55'))
paths=['explorations/conditional-build/k2555-global-stopping-stability-2026-11-05.md','tests/channel-swings/k2555_global_stopping_stability_probe.py','explorations/conditional-build/k2553-global-stopping-certificate-2026-11-04.md','lab/process/k2553-global-stopping-certificate.json']
paths+=list(str(p.relative_to(R)) for p in (R/'explorations/conditional-build').glob('k2509-*.md'))
report={'result':'K2555','checks':checks,'contrary_controls':controls,'curvature_certificate':{'numerator_degree':list(nd),'denominator_degree':list(dd),'numerator_min':str(min(nv)),'denominator_min':str(min(dv)),'coefficient_digest':hashlib.sha256('\n'.join(map(str,nv+dv)).encode()).hexdigest(),'inverse_Bernstein_reconstruction':True},'compression_certificate':{'numerator_degree':list(cnd),'denominator_degree':list(cdd),'numerator_min':str(min(cnv)),'denominator_min':str(min(cdv)),'coefficient_digest':hashlib.sha256('\n'.join(map(str,cnv+cdv)).encode()).hexdigest(),'inverse_Bernstein_reconstruction':True},'finite_fixture_count':fixture_count,'illustrative_not_certified':{'a_star':str(astar),'contact_cost':str(cs),'overspending_component_weight':str(mix_weight)},'evidence_kinds':{'exact':'original derivative, Bernstein and moment/exchange/prefix identities and finite rational fixtures','universal':'stage-count-uniform stability, equality and mixture arguments in note','numerical':'contact mixture illustration only','not_claimed':'quantitative adaptive/infinite-policy transfer, multiplier interval, full frontier or GU'},'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths}}
p=R/'lab/process/k2555-global-stopping-stability.json'
if '--write' in sys.argv:p.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(p.read_text())==report,'saved_report_consistency'
print('K2555 PASS',len(checks),'algebra/fixture groups',len(controls),'contrary controls')
