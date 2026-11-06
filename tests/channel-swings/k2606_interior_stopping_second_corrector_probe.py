#!/usr/bin/env python3
"""K2606 exact residual algebra and numerical original-policy illustrations.

Universal bounds are analytic, not inferred from numerical convergence.
"""
import argparse, json, hashlib
from pathlib import Path
from fractions import Fraction
import sympy as sy
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from flint import arb, fmpq, ctx
ctx.prec=192
root=Path(__file__).resolve().parents[2]
ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
checks=[];controls=[]
def ck(name,value):
    assert bool(value),'FAIL '+name
    checks.append(name)
def ct(name,value):
    assert bool(value),'FAIL contrary '+name
    controls.append(name)
r,b,e,x,dd=sy.symbols('r b e x dd',real=True)
alpha=(1+6*r+r*r)/(4*(1+r));beta=(1+r)/2
g=(1-r)**2/(2*(1+r));B=beta**2-alpha**2;G=sy.diff(g,r,2)
q=(1-r)*(3*r+1)/(2*(1+r)**2);D=sy.factor(B-q*r/2)
vp3=-q*r*r+q*q/G;E=2*(beta**3-alpha**3)/3+vp3/6
ck('original_log_cubic',sy.simplify(sy.diff(2*(sy.log(1-alpha*b)-sy.log(1-beta*b)),b,3).subs(b,0)/6-2*(beta**3-alpha**3)/3)==0)
ck('actual_strong_convexity',sy.factor(G-4/(1+r)**3)==0)
v=2/(1+r)**2-sy.Rational(1,2)
ck('stationary_action_relation',sy.cancel(v+sy.diff(g,r))==0)
ck('actual_r_flow',sy.cancel(sy.diff(v,r)*(q/G)+q)==0)
ck('actual_v_third',sy.cancel(sy.diff(q*r,r)*q/G-vp3)==0)
lam,c,W,Wpp,Zp,Z,Bp,GG,EE,rr,L=sy.symbols('lam c W Wpp Zp Z Bp GG EE rr L',positive=True)
A=c*lam*Bp-W
xc=-A/(lam*GG)
zrhs=A*A/(2*lam*GG)-c*c*lam*EE-c*Wpp/2
cubic=c*(lam*GG*x*x/2+A*x+c*c*lam*EE+c*Wpp/2+Zp+rr*Z)
ck('cubic_action_square',sy.expand(cubic-c*(lam*GG*(x-xc)**2/2-A*A/(2*lam*GG)+c*c*lam*EE+c*Wpp/2+Zp+rr*Z))==0)
ck('second_corrector_cancels_actual_cubic',sy.simplify(cubic.subs(x,xc).subs(Zp,zrhs-rr*Z))==0)
ck('step_rounding_starts_fourth_order',sy.expand(L*((e*c+e*e*dd)-e*c)**2)==L*e**4*dd**2)
ct('clipped_half_final_cell_loses_second_order',sy.expand(L*(e*c/2-e*c)**2)==L*c*c*e*e/4)
ct('one_price_instead_of_two_breaks_square',(L*b*b-2*sy.sqrt(2*L)*e*b+e*e).subs(b,e*sy.sqrt(2/L)).simplify()==-e*e)
r0=sy.Rational(1,16);lam0=sy.Rational(578,735)
ck('rational_initial_multiplier',v.subs(r,r0)==1/lam0)
Ds=sy.diff(D,r)*q/G
z0=sy.factor((sy.diff(B,r)**2/(D*G)-2*E/D-Ds/D+2*r).subs(r,r0))
c0=sy.sqrt(2/(lam0*D.subs(r,r0)));wp0=2*sy.sqrt(2*lam0*D.subs(r,r0));wpp0=sy.sqrt(2*lam0)*Ds.subs(r,r0)/sy.sqrt(D.subs(r,r0))-r0*wp0
zother=(c0*lam0*sy.diff(B,r).subs(r,r0))**2/(2*lam0*G.subs(r,r0))-c0*c0*lam0*E.subs(r,r0)-c0*wpp0/2
ck('rational_Z_initial_derivative',sy.simplify(zother-z0)==0 and z0.is_Rational)
# Exact two-stage original-law telescope, with arbitrary potential values.
a1,a2,b1,b2,lw1,lw2,k,U0,U1,U2=sy.symbols('a1 a2 b1 b2 lw1 lw2 k U0 U1 U2')
p1=1/(1+a1);p2=p1/(1+a2)
d1=(1+a1)*U0+2*lw1+2*k-U1;d2=(1+a2)*U1+2*lw2+2*k-U2
ck('original_prefix_telescope',sy.cancel(U0-p1*d1-p2*d2-(p2*U2-2*(p1*lw1+p2*lw2)-2*k*(p1+p2)))==0)
ct('unweighted_trial_count_wrong',sy.cancel(2*(p1+p2)-4)!=0)
M,C,zz,eta=sy.symbols('M C zz eta',positive=True)
obj=-2*sy.sqrt(C)*e+(M+zz)*e*e
ck('dual_square_completion',sy.simplify(obj-(M+zz)*(e-sy.sqrt(C)/(M+zz))**2+C/(M+zz))==0)
t=sy.symbols('t');series=sy.series(C*t/(1+zz*t),t,0,3).removeO()
ck('constrained_second_coefficient',sy.expand(series-C*t+C*zz*t*t)==0)
ck('inverse_offset',sy.simplify(C/(C/eta-zz+zz)-eta)==0)
ct('interior_formula_requires_positive_margin',(2/sy.sqrt(1+2/sy.Rational(3,5))-1)<0)
# Whole-interval sign theorem for the second corrector; exact Bernstein certificates.
Az=sy.factor((q-2*sy.diff(B,r))/G-r*r)
Kz=sy.factor(sy.diff(B,r)**2/(D*G)-2*E/D-Ds/D+2*r)
zv=sy.symbols('zv');h=sy.symbols('h',positive=True)
# Verify the transformation with independent coefficient symbols before substituting
# the rational flow: this avoids symbolic expansion of repeated rational denominators.
bpr,dp,qq,gg,er,rv=sy.symbols('bpr dp qq gg er rv',real=True,nonzero=True)
wl=sy.sqrt(2*lam)*h*zv;cl=sy.sqrt(2/lam)/h
wpl=2*sy.sqrt(2*lam)*h-rv*wl
wppl=sy.sqrt(2*lam)*dp/h-qq/gg*wl-rv*wpl
transformed=(cl*lam*bpr-wl)**2/(2*lam*gg)-cl**2*lam*er-cl*wppl/2
expected=h*h/gg*zv*zv+((qq-2*bpr)/gg-rv*rv)*zv+bpr*bpr/(h*h*gg)-2*er/(h*h)-dp/(h*h)+2*rv
ck('corrector_signed_quadratic_identity',sy.expand(transformed-expected)==0)
ck('actual_signed_A_formula',sy.cancel(Az+(3*r**4+14*r**3+24*r*r-22*r-3)/16)==0)
ck('actual_signed_K_formula',sy.cancel(Kz-(27*r**7+279*r**6+1151*r**5+2939*r**4+641*r**3-1451*r*r-91*r+89)/(48*(r+1)*(3*r+1)*(r*r+6*r-3)))==0)
signcerts={}
def bernstein(expr,name):
    xx=sy.symbols('xx');num,den=sy.fraction(sy.cancel(expr.subs(r,xx/6)))
    def coeff(poly):
        pp=sy.Poly(poly,xx);n=pp.degree()
        return [sum(pp.nth(k)*sy.binomial(i,k)/sy.binomial(n,k) for k in range(i+1)) for i in range(n+1)]
    nc,dc=coeff(num),coeff(den)
    if all(v<0 for v in dc):nc=[-v for v in nc];dc=[-v for v in dc]
    ck(name,all(v>=0 for v in nc) and all(v>0 for v in dc))
    signcerts[name]={'interval':['0','1/6'],'numerator':list(map(str,nc)),'denominator':list(map(str,dc))}
for name,expr in [('A_nonnegative',Az),('A_upper',sy.Rational(3,8)-Az),('DG_upper',sy.Rational(1,16)-D/G),('K_increasing',sy.diff(Kz,r)),('K_slope_upper',sy.Rational(11,4)-sy.diff(Kz,r)),('r_flow_upper',sy.Rational(1,5)-q/G)]:bernstein(expr,name)
ck('K_initial_lower',Kz.subs(r,0)==-sy.Rational(89,144))
ck('initial_r_uniform_upper',sy.Rational(8,7)<sy.Rational(107,100)**2)
ck('K_at_initial_r_upper',Kz.subs(r,sy.Rational(7,100))<-sy.Rational(47,100))
ck('z_bound_slope',sy.Rational(30,4)<sy.Rational(11,4)**2)
ss=sy.symbols('ss',nonnegative=True)
upper=-sy.Rational(517,1200)*ss+sy.Rational(737,960)*ss**2+sy.Rational(121,768)*ss**3
integrand=sy.Rational(11,12)*(-sy.Rational(47,100)+sy.Rational(11,20)*ss)+sy.Rational(3,8)*sy.Rational(11,4)*ss+sy.Rational(1,16)*sy.Rational(121,16)*ss**2
ck('integrated_sign_bound',sy.diff(upper,ss)==sy.expand(integrand))
ck('worst_half_score_negative',sy.simplify((upper/ss).subs(ss,sy.Rational(1,2)))==-sy.Rational(583,76800))
ck('strict_positive_inverse_offset',sy.Rational(583,76800)>sy.Rational(1,200))
ct('dropping_negative_constant_loses_sign',Az.subs(r,0)>0 and (D/G).subs(r,0)>0)

# Actual finite schedules: smooth ODE coefficients, equal-clock mesh, rational actions.
Df=sy.lambdify(r,D,'numpy');Drf=sy.lambdify(r,sy.diff(D,r),'numpy');Bpf=sy.lambdify(r,sy.diff(B,r),'numpy');Ef=sy.lambdify(r,E,'numpy')
def ode(lm):
    def fun(s,y):
        vv,ww,zz,tt=y;rv=2/np.sqrt(1+2*vv)-1;qv=2*np.sqrt(1+2*vv)-2-vv;gg=4/(1+rv)**3;dv=float(Df(rv));ds=float(Drf(rv))*qv/gg;cc=np.sqrt(2/(lm*dv));wp=2*np.sqrt(2*lm*dv)-rv*ww;wpp=np.sqrt(2*lm)*ds/np.sqrt(dv)-qv/gg*ww-rv*wp
        zp=(cc*lm*float(Bpf(rv))-ww)**2/(2*lm*gg)-cc*cc*lm*float(Ef(rv))-cc*wpp/2-rv*zz
        return [-qv,wp,zp,1/cc]
    return fun

def aa(f):
    f=Fraction(f);return arb(fmpq(f.numerator,f.denominator))
consumers=[]
for lm in [0.7,0.8]:
    sol=solve_ivp(ode(lm),(0,.5),[1/lm,0,0,0],method='DOP853',rtol=2e-13,atol=2e-14,dense_output=True)
    coarse=solve_ivp(ode(lm),(0,.5),[1/lm,0,0,0],method='DOP853',rtol=1e-11,atol=1e-12,dense_output=True)
    ck('numerical_ODE_refinement_'+str(lm),sol.success and coarse.success and max(abs(sol.y[:,-1]-coarse.y[:,-1]))<1e-10)
    vv,ww,zz,clock=sol.y[:,-1]
    for ee in [.002,.001,.0005]:
        n=int(np.floor(clock/ee+.5));states=[Fraction(1,2)]
        for i in range(1,n):
            target=clock*(n-i)/n
            sx=brentq(lambda ss: sol.sol(ss)[3]-target,0,.5,xtol=5e-15)
            states.append(Fraction(round(sx*10**14),10**14))
        states.append(Fraction(0));schedule=[];P=arb(1);resource=arb(0);cost=arb(0);max_step_error=0.
        for s0,s1 in zip(states,states[1:]):
            bb=s0-s1;v0,w0,zv,_=sol.sol(float(s0));rv=2/np.sqrt(1+2*v0)-1;gg=4/(1+rv)**3;dv=float(Df(rv));cc=np.sqrt(2/(lm*dv));ratio=rv+ee*(w0-cc*lm*float(Bpf(rv)))/(lm*gg)
            av=bb*Fraction(round(ratio*10**14),10**14)
            assert 0<av<bb,'FAIL actual feasible action'
            P/=1+aa(av);resource+=2*P
            cost+=2*P*(1+(aa(bb)-aa(av))**2/(2*(aa(bb)+aa(av))*(2-aa(bb)-aa(av)))).log()
            schedule.append([str(av),str(bb)]);max_step_error=max(max_step_error,abs(float(bb)-ee*cc))
        tag=str(lm)+'_'+str(ee)
        ck('actual_score_and_count_'+tag,sum((Fraction(v[1]) for v in schedule),Fraction(0))==Fraction(1,2) and len(schedule)==n)
        value=P-aa(Fraction(str(lm)))*cost-aa(Fraction(str(ee))**2)*resource
        U=lm*vv-ee*ww+ee*ee*zz
        error=float(value.mid())-U
        ck('numerical_constructed_value_residual_'+tag,abs(error)<20*ee**3)
        ck('numerical_whole_mesh_step_error_'+tag,max_step_error<100*ee**2)
        consumers.append({'lambda':str(lm),'e':str(ee),'count':n,'schedule':schedule,'resource_interval':resource.str(25,more=True),'original_priced_value_interval':value.str(25,more=True),'numerical_U':format(U,'.14g'),'numerical_error_over_e3':format(error/ee**3,'.7g'),'numerical_Z':format(zz,'.12g'),'numerical_max_step_error_over_e2':format(max_step_error/ee**2,'.7g')})
report={'result':'K2606','checks':checks,'contrary_controls':controls,'sign_certificates':signcerts,'corrector_sign':'-89S/144 <= Z(S) <= -583S/76800 < -S/200; compact strict-interior theorem domain only', 'initial_fixture':{'r':'1/16','lambda':str(lam0),'Z_derivative':str(z0)},'finite_consumers':consumers,'theorem_scope':'compact rectangles 0<S0<=S<=1/2,2/3<lambda0<=lambda<=4/5','asymptotics':['Q(k)=V-2sqrt(Ck)+Zk+O(k^1.5)','V-F(M)=C/M-CZ/M²+O(M^-3)','Rmin(eta)=C/eta-Z+O(eta)','all price optimizers R=sqrt(C/k)-Z+O(1), no convergent constant correction asserted'],'evidence_kind':'exact rational/symbolic original-law identities and coefficient controls; actual rational finite schedules with Arb192-bit costs; SciPy ODE and equal-clock numerical illustration is NOT a universal or interval proof of asymptotics; analytic proof in note','ceiling':'no switch-uniform extension, no exact finite optimum/count or third coefficient, no physical probability or GU inference'}
refs=['explorations/conditional-build/k2604-second-order-stopping-resource-bound-2026-11-06.md','explorations/conditional-build/k2602-continuum-stopping-resource-law-2026-11-06.md','explorations/conditional-build/k2571-stopping-resource-price-2026-11-05.md']
report['provenance']={f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in refs}
out=root/'lab/process/k2606-interior-stopping-second-corrector.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'FAIL report replay'
print(json.dumps({'result':'K2606','checks':len(checks),'controls':len(controls),'finite_consumers':len(consumers),'status':'pass'}))
