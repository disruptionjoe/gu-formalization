#!/usr/bin/env python3
"""K2610 exact original-law expansions and finite rational policy consumers.
Uniform asymptotic claims are proved in the note, not inferred from residual samples.
"""
import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction as F
import sympy as s
from flint import arb,ctx
root=Path(__file__).resolve().parents[2]
ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
ctx.prec=192
checks=[];controls=[]
def ck(name,value):
    assert bool(value),'FAIL '+name
    checks.append(name)
def ct(name,value):
    assert bool(value),'FAIL contrary '+name
    controls.append(name)
e,h,u,v,mu=s.symbols('e h u v mu',positive=True)
def trunc(z,n=4):return s.series(z,e,0,n).removeO().expand()
def original_w(a,b):return s.log(1+(b-a)**2/(2*(a+b)*(2-a-b)))
w1=trunc(original_w(e**2*u,e*h));w2=trunc(original_w(e**2*v,e*h))
expected=e*h/4+e**2*(-3*u/4+3*h*h/32)+e**3*(u*u/h-h*u/16+7*h**3/192)
ck('original_log_cubic_exact',s.simplify(w1-expected)==0)
P1=trunc(1/(1+e**2*u));P2=trunc(P1/(1+e**2*v));lam=s.Rational(2,3)+e*mu
J2=trunc(P2-2*(P1*(lam*w1+e*e)+P2*(lam*w2+e*e)))
G=-3*mu*h*h/8-7*h**3/72+(3*mu/2+3*h/4)*u+(3*mu/2+5*h/12)*v-4*(u*u+v*v)/(3*h)
ck('actual_two_stage_prefix_cubic',s.simplify(J2.coeff(e,3)-G)==0)
ck('actual_two_stage_leading',s.simplify(J2.coeff(e,2)-(-mu*h-4-h*h/4))==0)
Jwrong=trunc(P2-2*(lam*w1+lam*w2+2*e*e))
ct('omitting_survival_prefix_changes_cubic',s.simplify(Jwrong.coeff(e,3)-G)!=0)
L,beta,alpha=s.symbols('L beta alpha',positive=True)
ck('constrained_square_identity',s.expand(alpha*L-s.Rational(4,3)*alpha**2/beta-(s.Rational(3,16)*beta*L*L-s.Rational(4,3)/beta*(alpha-s.Rational(3,8)*beta*L)**2))==0)
ct('negative_linear_term_needs_zero_constraint',(-alpha-s.Rational(4,3)*alpha**2/beta).subs({alpha:1,beta:1})<0)
x,n=s.symbols('x n',positive=True)
An=lambda nn:2*nn+x*x/(8*nn)
ck('adjacent_count_difference',s.factor(An(n)-An(n+1)+2-x*x/(8*n*(n+1)))==0)
ck('count_threshold',s.simplify((An(n)-An(n+1)).subs(x,4*s.sqrt(n*(n+1))))==0)
ck('one_stage_endpoint_coefficient',An(1).subs(x,1)==s.Rational(17,8))
ck('one_stage_action_profile',s.Rational(3,8)*(s.Rational(1,12)+s.Rational(1,3))==s.Rational(5,32))
B1=-s.Rational(7,144)+s.Rational(3,16)*s.Rational(5,12)**2
ck('one_stage_endpoint_cubic',B1==-s.Rational(37,2304))
ct('continuum_endpoint_coefficient_false',An(1).subs(x,1)-1==s.Rational(9,8))
xstar=4*s.sqrt(2)
Bn=lambda nn:-3*mu*x*x/(16*nn)-7*x**3/(144*nn*nn)
shift=s.simplify(s.sqrt(2)*(Bn(1)-Bn(2)).subs({x:xstar,mu:-2}))
ck('inactive_shift_exact',s.simplify(shift-(6*s.sqrt(2)-s.Rational(28,3)))==0)
# Original zero-action logarithmic tie, independently expanded at shifted x.
xi=s.symbols('xi',real=True);S=e*xstar+e*e*xi
w0=lambda bb:s.log((4-bb)/(4-2*bb))
tie=trunc(-2*(s.Rational(2,3)-2*e)*(w0(S)-2*w0(S/2))+2*e*e)
ck('original_inactive_count_tie_shift',s.simplify(tie.coeff(e,3).subs(xi,shift))==0)
# Uniform interpolation coefficient from the convergent exact-tail series.
y,theta,score,lambda0=s.symbols('y theta score lambda0',positive=True)
AA=3*score**2/32;BB=7*score**3/192;DD=15*score**4/1024
H=lambda tt:score/4+AA/tt+BB/tt**2+DD/tt**3
expr=s.series(2*lambda0*((1-theta)*H(1/y-theta)+theta*H(1/y+1-theta)-score/4),y,0,4).removeO().expand()
ck('interpolation_linear_deviation_cancels',s.simplify(expr.coeff(y,2)-2*lambda0*BB)==0)
ck('actual_third_resource_coefficient',s.simplify(8*expr.coeff(y,3)-(15*lambda0*score**4/64+3*lambda0*score**2*theta*(1-theta)/2))==0)
ct('constant_third_resource_coefficient_false',s.simplify(8*(expr.coeff(y,3).subs(theta,s.Rational(1,2))-expr.coeff(y,3).subs(theta,0)))==3*lambda0*score**2/8)
# Price rounding: independent expansion about real count center.
a0,b0,d0,t0,z=s.symbols('a0 b0 d0 t0 z',positive=True)
nn=t0/e+b0/a0+z
loss=trunc(a0/nn+b0/nn**2+d0/nn**3+2*e*e*nn)
coef=s.simplify(loss.coeff(e,3).subs(a0,2*t0*t0))
ck('priced_rounding_square',s.simplify(coef-(d0/t0**3-b0*b0/(2*t0**5)+2*z*z/t0))==0)
ct('half_integer_price_phase_changes_cubic',s.simplify(coef.subs(z,s.Rational(1,2))-coef.subs(z,0))==1/(2*t0))
ck('exact_count_center_shift',s.simplify((7*lambda0*score**3/96)/(3*lambda0*score**2/16))==7*score/18)
def ab(q):
    q=F(q);return arb(q.numerator)/q.denominator
def exact_policy(bs,acts,ll,price):
    P=F(1);R=F(0);leak=arb(0)
    for bb,aa in zip(bs,acts):
        assert bb>0 and 0<=aa<=bb
        P/=1+aa;R+=2*P
        arg=1+(bb-aa)**2/(2*(aa+bb)*(2-aa-bb))
        leak+=2*ab(P)*ab(arg).log()
    return ab(P)-ab(ll)*leak-ab(price*R),P,R
consumers=[]
for xx,mm in [(F(1),F(0)),(F(5),F(0)),(F(7),F(-2)),(F(10),F(1))]:
    count=min(range(1,8),key=lambda j:2*j+xx*xx/F(8*j));hh=xx/count
    Ls=[F(3,2)*mm+hh/12+hh*(count-j)/3 for j in range(count)]
    Aval=2*count+xx*xx/F(8*count)
    Bval=-3*mm*xx*xx/F(16*count)-7*xx**3/F(144*count*count)+F(3,16)*hh*sum(max(F(0),ll)**2 for ll in Ls)
    for den in [100,200,400]:
        ee=F(1,den);ll=F(2,3)+ee*mm
        bs=[ee*hh]*count;acts=[ee*ee*F(3,8)*hh*max(F(0),l) for l in Ls]
        value,P,R=exact_policy(bs,acts,ll,ee*ee)
        pred=ab(1-ll*ee*xx/2-ee**2*Aval+ee**3*Bval)
        residual=(value-pred)/ab(ee**4)
        # Bounded finite examples support execution only; not the uniform theorem.
        ck('feasible_endpoint_'+str((xx,mm,den)),sum(bs)==ee*xx and all(0<=a<=b for a,b in zip(acts,bs)))
        consumers.append({'x':str(xx),'mu':str(mm),'e':str(ee),'n':count,'a':list(map(str,acts)),'b':list(map(str,bs)),'expected_trials':str(R),'priced_value_Arb':str(value),'residual_over_e4_illustration':str(residual)})
# Exact tail optimal value at prescribed integer/half count phases.
rounding=[]
ss=F(1,2);ll=F(1,6);tt=F(1,16);cc=F(7,36)
a=F(3,16)*ll*ss**2;b=F(7,96)*ll*ss**3;d=F(15,512)*ll*ss**4
Dconst=d/tt**3-b*b/(2*tt**5);C=F(3,8)*ll*ss**2;Z=-7*ss/9;V=1-ll*ss/2
for phase in [F(0),F(1,2)]:
    for m in [20,40]:
        ee=tt/(m+phase-cc)
        vals=[]
        for count in range(m-2,m+3):
            vv,_,_=exact_policy([ss/count]*count,[F(0)]*count,ll,ee*ee);vals.append((count,vv))
        # Arb separates the unique best in these fixtures; the theorem handles ties.
        best=max(vals,key=lambda item:float(item[1].mid()))
        ck('tail_interval_separated_'+str((phase,m)),all(best[1]>vv for nn,vv in vals if nn!=best[0]))
        ck('tail_winner_interior_for_global_convexity_'+str((phase,m)),m-2<best[0]<m+2)
        cubic=Dconst+2*phase*phase/tt
        pred=ab(V)-2*ab(C).sqrt()*ab(ee)+ab(Z*ee**2-cubic*ee**3)
        rounding.append({'phase':str(phase),'e':str(ee),'optimal_count_fixture':best[0],'priced_value_Arb':str(best[1]),'cubic_loss':str(cubic),'residual_over_e4_illustration':str((best[1]-pred)/ab(ee**4))})
report={'result':'K2610','checks':checks,'contrary_controls':controls,'terminal_consumers':consumers,'price_rounding_consumers':rounding,'endpoint_scope':'S=e x, lambda=2/3+e mu, compact positive x and bounded mu; O(e4) value','tail_scope':'fixed positive S<=1/2, 0<lambda<=2/5; resource O(M^-4) and price O(e4)','evidence_kind':'exact original-law symbolic identities, Arb enclosures of rational finite policies; universal asymptotic/count arguments in note; residual illustrations do not certify uniform bounds','ceiling':'no exact finite-price tie at cubic equality, general positive-action third coefficient, pathwise resource cap or physical probability'}
refs=['explorations/conditional-build/k2608-switching-stopping-second-corrector-2026-11-06.md','explorations/conditional-build/k2577-exact-resource-tail-2026-11-05.md','explorations/conditional-build/k2571-stopping-resource-price-2026-11-05.md']
report['provenance']={f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in refs}
out=root/'lab/process/k2610-terminal-stopping-count-layer.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'FAIL report replay'
print(json.dumps({'result':'K2610','checks':len(checks),'controls':len(controls),'finite_policies':len(consumers),'rounding_policies':len(rounding),'status':'pass'}))
