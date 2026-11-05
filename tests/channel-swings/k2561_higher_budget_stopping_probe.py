"""Exact high-budget generator certificate; universal claims proved in K2561 note."""
from pathlib import Path
from math import comb
import itertools,hashlib,json,sys
import sympy as s
R=Path(__file__).resolve().parents[2]
checks={};controls={};certificates={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ct(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError('contrary '+k)
a,b,r,X,Y=s.symbols('a b r X Y');D=2*(a+b)*(2-a-b);N=D+(b-a)**2;x=(b-a)**2/D
wa=s.cancel(s.diff(N,a)/N-s.diff(D,a)/D);wb=s.cancel(s.diff(N,b)/N-s.diff(D,b)/D)
waa=s.diff(wa,a);wab=s.diff(wa,b);wbb=s.diff(wb,b);w=s.log(N/D)
M=-2*(1+a)*wa+2*w
K=s.factor((wbb-wab**2/waa+wb*wab/((1+a)*waa)).subs(a,r*b))
ck('constant_output_chain_derivative',s.cancel((wbb+wab*(wb-(1+a)*wab)/((1+a)*waa)).subs(a,r*b)-K)==0)
ck('output_root_decreases_with_a',s.cancel(s.diff(M,a)+2*(1+a)*waa)==0)
def bern(expr,variables,label):
 p=s.Poly(s.expand(expr),*variables);degrees=p.degree_list();out={}
 for ij in itertools.product(*[range(n+1) for n in degrees]):
  out[ij]=sum(c*s.prod(s.Rational(comb(i,j),comb(n,j)) for i,j,n in zip(ij,ij0,degrees)) for ij0,c in p.terms() if all(i>=j for i,j in zip(ij,ij0)))
 # Invert using power coefficients of Bernstein polynomials. This is a
 # different calculation from the forward power-to-Bernstein sums.
 back={}
 for powers in itertools.product(*[range(n+1) for n in degrees]):
  back[powers]=sum(c*s.prod(comb(n,i)*comb(n-i,k-i)*(-1)**(k-i) for n,i,k in zip(degrees,ij,powers)) for ij,c in out.items() if all(k>=i for i,k in zip(ij,powers)))
 ck('inverse_basis_'+label,all(s.expand(back.get(ij,0)-dict(p.terms()).get(ij,0))==0 for ij in back))
 return p,out

def certify(name,rat,subs,variables):
 num,den=s.fraction(s.factor(rat));pn,bn=bern(num.subs(subs),variables,name+'_numerator');pd,bd=bern(den.subs(subs),variables,name+'_denominator')
 ck(name+'_positive_numerator',all(c>0 for c in bn.values()));ck(name+'_positive_denominator',all(c>0 for c in bd.values()))
 certificates[name]={'numerator_degree':list(pn.degree_list()),'denominator_degree':list(pd.degree_list()),'numerator_coefficients':len(bn),'denominator_coefficients':len(bd),'minimum_numerator':str(min(bn.values())),'maximum_denominator':str(max(bd.values())),'minimum_denominator':str(min(bd.values())),'numerator_sha256':hashlib.sha256(str(sorted(bn.items())).encode()).hexdigest(),'denominator_sha256':hashlib.sha256(str(sorted(bd.items())).encode()).hexdigest()}
 return bn,bd
kn,kd=certify('increasing_generator',K,{r:2*X/5,b:Y/2},(X,Y))
gamma=s.Rational(78360951,2744000000)
ck('uniform_generator_increment',2*min(kn.values())/max(kd.values())==gamma)
bar=s.factor((1+2*(1+a)*wa-2*x).subs(a,2*b/5))
ck('logarithmic_root_barrier_identity',s.cancel(bar-2*(3421*b*b-6095*b+2350)/(7*(7*b-10)*(89*b-140)))==0)
certify('root_barrier',bar,{b:Y/2},(Y,))
bound=s.factor(2*wbb.subs(a,0));ck('boundary_generator_derivative',s.cancel(bound-8*(3-b)/((2-b)**2*(4-b)**2))==0)
ck('boundary_minimum',bound.subs(b,0)==s.Rational(3,8)>gamma)
# Positive derivative proves the claimed boundary minimum, no sample inference.
certify('boundary_generator_increases',s.diff(bound,b),{b:Y/2},(Y,))
threshold=s.factor(s.diff(M.subs(a,0),b))
ck('unique_branch_crossing_derivative',s.cancel(threshold-4*(3*b*b-12*b+10)/((b-4)**2*(b-2)**2))==0)
certify('boundary_threshold_increases',threshold,{b:Y/2},(Y,))
v=s.symbols('v',positive=True);q=2*s.sqrt(1+2*v)-2-v;rr=2/s.sqrt(1+2*v)-1;g=(1-r)**2/(2*(1+r))
ck('fluid_minimizer_stationarity',s.simplify((v+s.diff(g,r)).subs(r,rr))==0)
ck('fluid_minimum_value',s.simplify((r*v+g).subs(r,rr)-q)==0)
ck('fluid_derivative_equals_ratio',s.simplify(s.diff(q,v)-rr)==0)
ck('fluid_boundary_C1',q.subs(v,s.Rational(3,2))==s.Rational(1,2) and s.diff(q,v).subs(v,s.Rational(3,2))==0)
ck('valid_input_floor',s.Rational(5,4)-s.Rational(1,2)/2==1)
z=s.sqrt(1+2*v);tau=s.log(z-1)-3*s.log(3-z)
ck('integrated_clock_derivative',s.simplify(s.diff(tau,v)-1/q)==0)
ck('clock_branch_match',tau.subs(v,s.Rational(3,2))==0 and s.diff(tau,v).subs(v,s.Rational(3,2))==2)
# Abstract exact chain-rule identities; strict signs are supplied in note.
theta,u,qu,qt,ru,rt=s.symbols('theta u qu qt ru rt',positive=True);J=qu/qt;Jp=J*(ru-rt)/qt
ck('budget_derivative_cancellation',s.cancel(s.diff(theta*J-u,theta)+theta*(s.diff(J,qu)*ru*J+s.diff(J,qt)*rt)-J-theta*Jp)==0)
ck('constrained_marginal',s.cancel(Jp/(theta*Jp)-1/theta)==0)
ck('strict_curvature_formula',s.cancel((-1/theta**2)/(theta*Jp)+1/(theta**3*Jp))==0)
A1,A2,A3,w1,w2,w3,U,T,lam=s.symbols('A1 A2 A3 w1 w2 w3 U T lam',positive=True)
composed=A3*(A2*(A1*U+2*w1)+2*w2)+2*w3;prod=A1*A2*A3
p=1/prod;C=2*w1/A1+2*w2/(A1*A2)+2*w3/prod
ck('original_prefix_affine_composition',s.expand(composed-prod*U-prod*C)==0)
ck('finite_dual_error_identity',s.cancel((p-lam*C)-(lam*U-lam*(composed-T)/prod)).subs(T,1/lam)==0)
ct('wrong_cost_prefix_rejected',s.cancel(C-2*(w1+w2+w3))!=0)
ct('wrong_composition_order_rejected',s.expand(composed-(A1*(A2*(A3*U+2*w3)+2*w2)+2*w1))!=0)
ct('input_root_not_output_root',s.cancel(s.diff(M+2*wa,a))!=0)
ct('positive_generator_not_global',K.subs({r:s.Rational(4,5),b:s.Rational(1,10)})<0)
ct('boundary_minimizer_cannot_be_omitted',(2/s.sqrt(1+2*s.Integer(2))-1)<0)
# Formal expansions derive the saturation coefficients from exact q and tau'.
eps,xx,t0=s.symbols('eps xx t0',positive=True)
qseries=s.series(q.subs(v,s.Rational(3,2)-xx),xx,0,4).removeO()
ck('saturation_q_coefficients',s.expand(qseries-(s.Rational(1,2)-xx**2/8-xx**3/32))==0)
tauprime=s.series((-1/q).subs(v,s.Rational(3,2)-xx),xx,0,4).removeO();tauseries=s.integrate(tauprime,(xx,0,xx))
thetaseries=t0+tauseries/2
ck('saturation_theta_coefficients',s.series(thetaseries,xx,0,4).removeO()==t0-xx-xx**3/12)
prob=2*qseries;budget=s.series(thetaseries*prob-(s.Rational(3,2)-xx),xx,0,4).removeO();deficit=t0-s.Rational(3,2)-budget
ck('saturation_budget_coefficients',s.expand(deficit-(t0*xx**2/4+(t0/16-s.Rational(1,6))*xx**3))==0)
ck('frontier_three_halves_coefficient',s.expand(1-prob-deficit/t0-xx**3/(6*t0))==0)
ck('square_root_conversion',s.simplify((2/s.sqrt(t0))**3/(6*t0)-4/(3*t0**s.Rational(5,2)))==0)
ck('marginal_square_root_conversion',s.simplify((2/s.sqrt(t0))/t0**2-2/t0**s.Rational(5,2))==0)
# Exact finite-stage gap: log(1+x)>x/(1+x), x=1/6.
ct('finite_zero_failure_stage_not_fluid_exact',2*s.Rational(1,7)-s.Rational(1,4)>0)
# A new exact intermediate-output contrary fixture, not a decimal sign.
point={a:s.Rational(7,20),b:s.Rational(1,2)};xp=s.cancel(x.subs(point))
loglo=xp-xp**2/2+xp**3/3-xp**4/4;loghi=xp-xp**2/2+xp**3/3
vbase=s.cancel((-2*(1+a)*wa).subs(point));vlo=vbase+2*loglo;vhi=vbase+2*loghi;G=s.cancel(2*wb.subs(point))
fp=lambda vv:(G+2+vv)**2-4-8*vv
ct('intermediate_output_criterion_extension_rejected',vlo>0 and 16*vlo**2>3 and vhi<1 and fp(vlo)<0 and fp(vhi)<0)
certificates['intermediate_output_counterexample']={'a':'7/20','score':'1/2','x':str(xp),'output_lower':str(vlo),'output_upper':str(vhi),'generator':str(G),'squared_difference_lower_endpoint':str(fp(vlo)),'squared_difference_upper_endpoint':str(fp(vhi)),'claim':'G_score(v)<q(v) at exact logarithmic output v in(sqrt(3)/4,1); criterion failure only, not complete optimal phase'}
from fractions import Fraction as F
from math import isqrt

def log_bounds(x,n=24):
 # Atanh expansion with absolute geometric tail; rational x>0.
 assert x>0
 z=(x-1)/(x+1);series=2*sum((z**(2*k+1)/F(2*k+1) for k in range(n)),F(0))
 err=2*abs(z)**(2*n+1)/(F(2*n+1)*(1-z*z))
 return series-err,series+err

def sqrt_bounds(x,digits=16):
 den=10**digits;j=isqrt(x.numerator*den*den//x.denominator)
 return F(j,den),F(j+1,den)

def w_bounds(a,b):
 xx=(b-a)**2/(2*(a+b)*(2-a-b));return log_bounds(1+xx)

def k(a,b):
 D=2*(a+b)*(2-a-b);N=D+(b-a)**2
 return (4-4*(a+b))/D-(4-4*(a+b)+2*(a-b))/N

def M_bounds(a,b):
 l,h=w_bounds(a,b);q=2*(1+a)*k(a,b)
 return q+2*l,q+2*h

def tau_bounds(v):
 zl,zh=sqrt_bounds(1+2*v)
 l1,h1=log_bounds(zl-1);l2,h2=log_bounds(zh-1)
 l3,h3=log_bounds(3-zl);l4,h4=log_bounds(3-zh)
 return l1-3*h3,h2-3*l4

def round_out(lo,hi,den=10**12):
 return F(lo.numerator*den//lo.denominator,den),F(-((-hi.numerator*den)//hi.denominator),den)
lam=F(19,10);S=F(1,2);theta=1/lam
A0=1+F(349,2000);a=F(21,5000);b=F(1,100);n=20;tail=(1+a)**(-n);p=tail/A0
w0=w_bounds(F(349,2000),F(3,10));wt=w_bounds(a,b)
Clo=2*w0[0]/A0+2*wt[0]*(1-tail)/(A0*a);Chi=2*w0[1]/A0+2*wt[1]*(1-tail)/(A0*a)
hybridlo=p-lam*Chi;hybridhi=p-lam*Clo
ck('finite_hybrid_original_dual_lower',hybridlo>F(711,1000))
a0,a1=F(3219,10000),F(3221,10000)
ck('global_one_stage_optimizer_bracket',M_bounds(a0,S)[0]>theta>M_bounds(a1,S)[1])
oneupper=(1-2*lam*w_bounds(a1,S)[0])/(1+a0)
ck('global_one_stage_upper_below_hybrid',oneupper<F(71,100))
ubar=F(187,500);tautheta=tau_bounds(theta);tauubar=tau_bounds(ubar)
ck('fluid_clock_root_upper_bound',tautheta[1]-tauubar[0]<S)
fluidupper=lam*ubar
ck('fluid_value_upper_bound',fluidupper==F(3553,5000))
ck('hybrid_two_candidate_separation',F(711,1000)-fluidupper==F(1,2500))

ck('hybrid_same_budget_one_stage_mixture_margin',F(711,1000)-F(71,100)==F(1,1000))
ck('finite_hybrid_total_score',F(3,10)+20*F(1,100)==F(1,2))
ck('finite_hybrid_geometric_prefix',sum(((1+a)**(-i) for i in range(1,n+1)),F(0))==(1-tail)/a)
certificates['finite_hybrid_successor']={'multiplier':'19/10','score':'1/2','first_action':['349/2000','3/10'],'tail_action':['21/5000','1/100'],'tail_stages':20,'dual_interval':[str(z) for z in round_out(hybridlo,hybridhi)],'exact_budget_interval':[str(z) for z in round_out(Clo,Chi)],'same_budget_one_stage_mixture_margin':'1/1000','global_one_stage_upper':'71/100','fluid_candidate_upper':'3553/5000','strict_margin_over_both':'1/2500','clock_difference_upper':[str(z) for z in round_out(tautheta[0]-tauubar[1],tautheta[1]-tauubar[0])],'claim':'explicit finite policy superiority to both named candidates; no globally optimal hybrid or complete phase'}

paths=['explorations/conditional-build/k2561-higher-budget-stopping-2026-11-05.md','tests/channel-swings/k2561_higher_budget_stopping_probe.py','explorations/conditional-build/k2559-parametric-stopping-concavity-2026-11-05.md','explorations/conditional-build/k2557-parametric-stopping-support-2026-11-05.md','explorations/conditional-build/k2485-constrained-stopping-frontier-2026-11-01.md']
report={'result':'K2561','multiplier_domain':'0<lambda<=4/5','score_domain':'0<S<=1/2','checks':checks,'contrary_controls':controls,'certificates':certificates,'generator_increment':str(gamma),'evidence_kinds':{'exact':'rational whole-domain Bernstein certificate and independent inversion; clock, original prefix accounting, saturation series','universal':'ODE comparison, original-policy telescope, finite-stage approximation, exact-budget repair and nonattainment proved in note','not_claimed':'full intermediate frontier, physical law, external certification, native GU'},'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths}}
out=R/'lab/process/k2561-higher-budget-stopping.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved_report_consistency'
print('K2561 PASS',len(checks),'exact/supporting groups',len(controls),'contrary controls')
