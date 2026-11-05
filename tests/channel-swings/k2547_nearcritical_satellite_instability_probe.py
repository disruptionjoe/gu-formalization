"""Original-law exact coefficients; fixed-cloud analytic proof is in companion note.
High-precision policy evaluation is supplemental, not an interval proof.
"""
from pathlib import Path
import hashlib,json,sys
import sympy as s
import mpmath as mp
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(bank,name,v):
 bank[name]=bool(v)
 if not bank[name]:raise AssertionError('FAIL '+name)
def eq(name,a,b=0):ck(checks,name,s.simplify(a-b)==0)
r,b,lam=s.symbols('r b lam');rt=2*s.sqrt(3)-3;lt=4*s.sqrt(3)/3
al=(1-r)**2/(4*(1+r));be=(1+r)/2;c=be-al
co=[0]+[(be**n-c**n)/n for n in range(1,5)];q,t,h=co[2:]
f=r+2*lam*al;B=r*f-2*lam*q;C=-r*B-2*lam*t;D4=-r*C-2*lam*h
F=s.diff(f,r,2);v=s.diff(B,r)/F;v2=(s.diff(B,r,2)*v+s.diff(C,r)-s.diff(f,r,3)*v*v/2)/F
# Independent original-log argument and prefix-weighted value expansion.
eq('original_log_argument',1+(b-r*b)**2/(2*(b+r*b)*(2-b-r*b)),(1-c*b)/(1-be*b))
wc=sum(co[n]*b**n for n in range(1,5));prefix=sum((-r*b)**n for n in range(5));orig=s.Poly(s.expand((1-2*lam*wc)*prefix),b)
for n,expected in [(1,-f),(2,B),(3,C),(4,D4)]:eq('original_weighted_coefficient_'+str(n),orig.nth(n),expected)
# Independent original logarithm derivative at fixed action, before series use.
a=s.symbols('a');original_w=s.log(1+(b-a)**2/(2*(a+b)*(2-a-b)))
original_rb=s.log(1-c*b)-s.log(1-be*b)
eq('exact_fixed_action_score_derivative',s.diff(original_w,b).subs(a,r*b),s.diff(original_rb,b)-r*s.diff(original_rb,r)/b)
eq('exact_fixed_score_action_derivative',s.diff(original_w,a).subs(a,r*b),s.diff(original_rb,r)/b)
# w_b at fixed a = partial_b w(rb,b) - (r/b)partial_r w(rb,b).
wb=s.diff(wc,b)-r*s.diff(wc,r)/b
# At the optimum the derivative identity replaces w_a using exact stationarity.
# Direct numerator: 2lambda wb-A; identity 2lambda wb-A=f-A+H1 b+H2 b²+H3 b³ after stationarity.
H1=4*lam*q-r*f;H2=6*lam*t+r*B;H3=8*lam*h+r*C
# Check insertion identity modulo original ratio stationarity through cubic order.
A=s.symbols('A');M=2*wc-2*(1+r*b)*s.diff(wc,r)/b
num=2*lam*wb-A
identity=f-A+H1*b+H2*b*b+H3*b**3
# Difference is r*(lambda M-1), after using original value to expand terms;
# derive exact form instead: wb|a=w_b|r-r*w_a, and lambdaM=1 gives 2lam*r*w_a=r*(2lam*w-1)/(1+rb).
alt=2*lam*s.diff(wc,b)-A+r*(1-2*lam*wc)*prefix
for n in range(4):eq('original_fixed_action_numerator_mod_stationarity_'+str(n),s.Poly(s.expand(num-alt-r*(lam*M-1)*prefix),b).nth(n),0)
eq('original_insertion_stationarity_reduction_constant',s.Poly(s.expand(alt-identity),b).nth(0),0)
for n in range(1,4):eq('original_insertion_stationarity_reduction_'+str(n),s.Poly(s.expand(alt-identity),b).nth(n),0)
N2=F*v*v/2+s.diff(H1,r)*v+H2
N3=F*v*v2+s.diff(f,r,3)*v**3/6+s.diff(H1,r)*v2+s.diff(H1,r,2)*v*v/2+s.diff(H2,r)*v+H3
L2=N2-r*H1;L3=N3-r*N2+(r*r-v)*H1
lr=2*(1+r)**2/((1-r)*(r+3));HH=(3*r+1)*(r*r+6*r-3)/(8*(r+3))
L2r=s.factor(L2.subs(lam,lr));L3r=s.factor(L3.subs(lam,lr))
eq('leading_insertion_minus_twice_H',H1.subs(lam,lr),-2*HH)
eq('stationary_curve',s.diff(f,r).subs(lam,lr))
Hp=s.simplify((s.diff(HH,r)/s.diff(lr,r)).subs(r,rt));Hpp=s.simplify((s.diff(s.diff(HH,r)/s.diff(lr,r),r)/s.diff(lr,r)).subs(r,rt))
c1=(2841-1643*s.sqrt(3))/48;cL=(249*s.sqrt(3)-431)/2;mu0=s.Rational(37,66)-257*s.sqrt(3)/396
L2p=s.simplify((s.diff(L2r,r)/s.diff(lr,r)).subs(r,rt));L3star=s.simplify(L3r.subs(r,rt))
eq('critical_L2',L2r.subs(r,rt),c1);eq('critical_L2_lambda_derivative',L2p,(-105583+60963*s.sqrt(3))/128)
eq('critical_L3',L3star,s.Rational(211309,96)-40665*s.sqrt(3)/32)
eq('critical_Hprime',Hp,(141-81*s.sqrt(3))/8);eq('critical_Hsecond',Hpp,(6021-3477*s.sqrt(3))/64)
eq('cubic_boundary_cancellation',c1,2*Hp*mu0)
gamma=s.simplify(L3star+mu0*L2p-Hpp*mu0**2);expected=(202353685-116818417*s.sqrt(3))/371712
eq('fifth_order_insertion_gamma',gamma,expected)
ck(checks,'exact_gamma_positive',202353685**2-3*116818417**2==7386181921558>0)
nu0=s.simplify(gamma/(2*Hp));eq('local_insertion_phase_second_coefficient',nu0,(24165709-13458052*s.sqrt(3))/3066624)
Kinf=s.simplify(cL+c1/2);eq('cloud_limit_curvature',Kinf,(10309*s.sqrt(3)-17847)/96)
ck(checks,'cloud_curvature_positive',3*10309**2-17847**2==311034>0)
ck(checks,'c1_negative',3*1643**2-2841**2>0)
x,y,S,nu=s.symbols('x y S nu');c0=c1-cL
xx=[1-S*(x+y),S*x,S*y];RR=sum(xx[i]*xx[j]**2 for i in range(3) for j in range(i+1,3));TT=s.prod(xx)
cloud=s.expand(-cL*RR+(2*c0-3*c1)*TT)
eq('independent_ordered_cloud_quadratic',cloud.coeff(S,2),-cL*(x*x+y*y)-(c1+2*cL)*x*y)
eq('cloud_square_rewrite',cL*(x*x+y*y)+(c1+2*cL)*x*y,Kinf*(x+y)**2-c1*(x*x+y*y)/2)
K1=cL;K2=Kinf-c1/4;gain1=gamma**2/(4*K1);gain2=gamma**2/(4*K2)
eq('two_satellites_improve_coefficient',gain2-gain1,-c1*gamma**2/(16*K1*K2))
ck(controls,'one_satellite_not_cloud_optimum',s.simplify(K1-K2)>0)
ck(controls,'wrong_lambda_derivative_order_detected',s.simplify(s.diff(f.subs(lam,lr),r).subs(r,rt))!=0)
ck(controls,'omitted_ratio_reoptimization_detected',s.simplify(L2r.subs(r,rt)-H2.subs({lam:lt,r:rt}))!=0)
ck(controls,'omitted_moving_multiplier_terms_detected',s.simplify(gamma-L3star)!=0)
# Original-law high precision backward optimization. No asymptotic surrogate in value.
mp.mp.dps=85
mlt=4*mp.sqrt(3)/3;mmu=mp.mpf(37)/66-257*mp.sqrt(3)/396
gam=mp.mpf(str(s.N(gamma,90)));kl=mp.mpf(str(s.N(cL,90)));ki=mp.mpf(str(s.N(Kinf,90)));cc1=mp.mpf(str(s.N(c1,90)))
def stage(score,mult,suffix):
 if score==0:return suffix
 def cost(act):return mp.log1p((score-act)**2/(2*(act+score)*(2-act-score)))
 def wprime(act):
  # Exact derivative of log[1+(b-a)^2/(2(a+b)(2-a-b))].
  z=(score-act)**2/(2*(act+score)*(2-act-score))
  zp=z*(-2/(score-act)-1/(act+score)+1/(2-act-score))
  return zp/(1+z)
 def station(ratio):
  act=ratio*score
  return mult*(2*cost(act)-2*(1+act)*wprime(act))-suffix
 ratio=mp.findroot(station,(mp.mpf('.43'),mp.mpf('.49')),solver='secant',tol=mp.mpf('1e-78'))
 assert 0<ratio<1
 act=ratio*score
 return (suffix-2*mult*cost(act))/(1+act)
def value(scores,mult):
 out=mp.mpf(1)
 for score in reversed(scores):out=stage(score,mult,out)
 return out
nums=[]
for score in [mp.mpf('0.001'),mp.mpf('0.0005')]:
 mult=mlt+mmu*score;one=value([score],mult)
 row={'S':str(score),'policy_gains_over_S5':{}}
 for m in [1,2]:
  km=ki-cc1/(2*m);Z=gam/(2*km);tail=Z*score**2/m
  val=value([score-m*tail]+[tail]*m,mult);coef=(val-one)/score**5
  assert val>one
  row['policy_gains_over_S5'][str(m)]=mp.nstr(coef,30)
 row['two_satellites_better']=mp.mpf(row['policy_gains_over_S5']['2'])>mp.mpf(row['policy_gains_over_S5']['1']);assert row['two_satellites_better'];nums.append(row)
paths=['explorations/conditional-build/k2547-nearcritical-satellite-instability-2026-11-04.md',str(Path(__file__).relative_to(R)),'explorations/conditional-build/k2545-critical-stopping-aggregation-2026-11-04.md']
report={'result':'K2547','exact_algebra':checks,'contrary_controls':controls,'supplemental_numerical_original_law':nums,'coefficients':{n:str(s.simplify(vv)) for n,vv in dict(gamma=gamma,nu0=nu0,Kinf=Kinf,K1=K1,K2=K2,gain1=gain1,gain2=gain2).items()},'scope':'fixed finite satellite clouds and ordered-limit lower bound; no all-policy upper bound or explicit certified finite-score interval','dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths}}
p=R/'lab/process/k2547-nearcritical-satellite-instability.json'
if '--write' in sys.argv:p.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(p.read_text())==report,'saved report mismatch'
print('K2547',len(checks),'exact algebra groups',len(controls),'contrary controls; supplemental original-law evaluations',len(nums))
