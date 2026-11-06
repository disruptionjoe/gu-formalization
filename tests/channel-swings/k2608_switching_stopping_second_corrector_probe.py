#!/usr/bin/env python3
"""K2608 switching residual algebra and numerical original-policy illustrations.

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
# Boundary branch is a different constrained minimizer, not continuation of r.
ck('zero_branch_D',D.subs(r,0)==sy.Rational(3,16))
ck('zero_branch_E',2*(beta**3-alpha**3).subs(r,0)/3==sy.Rational(7,96))
ck('zero_branch_corrector',-2*sy.Rational(7,96)/sy.Rational(3,16)==-sy.Rational(7,9))
ck('switch_positive_speed',q.subs(r,0)==sy.Rational(1,2))
ck('boundary_B_derivative',sy.diff(B,r).subs(r,0)==-sy.Rational(1,8))
ct('interior_corrector_is_not_tail_corrector',z0!=-sy.Rational(7,9))
# At W=0, the interior limit is -89/144 whereas the constrained tail is -112/144.
Ds=sy.diff(D,r)*q/G
Kzero=sy.factor((sy.diff(B,r)**2/(D*G)-2*E/D-Ds/D).subs(r,0))
ck('actual_interior_endpoint_derivative',Kzero==-sy.Rational(89,144))
ct('corrector_derivative_jump',Kzero-(-sy.Rational(7,9))==sy.Rational(23,144))
S0,l0=sy.symbols('S0 l0',positive=True)
Ztail=-7*S0/9;Ctail=3*l0*S0**2/8
ck('tail_second_gap_matches_original_log',sy.expand(-Ctail*Ztail-7*l0*S0**3/24)==0)
ck('tail_inverse_overhead',-Ztail==7*S0/9)
ck('tail_switch_threshold',sy.simplify((1/l0-S0/2-sy.Rational(3,2)).subs(l0,2/(3+S0)))==0)
ct('old_interior_lower_bound_invalid_on_tail',-sy.Rational(7,9)<-sy.Rational(89,144))
# A band occupation primitive pays O(e^3) globally; crossing intervals must be covered.
u=sy.symbols('u',positive=True)
ck('band_barrier_total_order',sy.expand(e**2*(2*u*e))==2*u*e**3)
def band_increment(start,step,lo,hi):
    return max(sy.Integer(0),min(start,hi)-max(start-step,lo))
start=sy.Rational(11,10);step=sy.Rational(1,5)
ck('enlarged_band_pays_whole_crossing',band_increment(start,step,sy.Rational(9,10),sy.Rational(11,10))==step)
ct('start_point_only_indicator_misses_crossing',start>sy.Rational(21,20) and band_increment(start,step,sy.Rational(19,20),sy.Rational(21,20))==sy.Rational(1,10))

# Exact actual switch matching and price-dependent activation coefficients.
ss,ll=sy.symbols('ss ll',positive=True)
W0=sy.sqrt(3*ll/2)*ss;cc0=sy.sqrt(32/(3*ll))
Wpp0=-sy.sqrt(6*ll)/16-W0/8
Zright=(cc0*ll*(-sy.Rational(1,8))-W0)**2/(8*ll)-cc0**2*ll/sy.Integer(12)-cc0*Wpp0/2
ck('switch_derivative_jump_with_nonzero_W',sy.simplify(Zright-(-sy.Rational(89,144)+3*ss/8+3*ss**2/16))==0)
ck('interior_switch_exact_fixture',sy.simplify(Zright.subs(ss,sy.Rational(1,3)))==-sy.Rational(17,36))
ck('activation_constant_actual_law',sy.simplify(W0/ll+cc0/8-(3*ss+1)/sy.sqrt(6*ll))==0)
ck('lambda_three_fifths_activation',sy.simplify(((3*ss+1)/sy.sqrt(6*ll)).subs({ss:sy.Rational(1,3),ll:sy.Rational(3,5)})-sy.sqrt(10)/3)==0)
ct('continuum_switch_is_not_priced_activation',((3*ss+1)/sy.sqrt(6*ll))>0)
# On either side of the actual transition, the linearized KKT derivative has opposite signs.
xx=sy.symbols('xx',real=True);offset=sy.sqrt(10)/3
ck('activation_negative_margin',(-xx/2-offset).subs(xx,-2*offset-1)>0)
ck('activation_positive_margin',(-xx/2-offset).subs(xx,-2*offset+1)<0)

# Actual finite schedules: smooth ODE coefficients, equal-clock mesh, rational actions.
Df=sy.lambdify(r,D,'numpy');Drf=sy.lambdify(r,sy.diff(D,r),'numpy');Bpf=sy.lambdify(r,sy.diff(B,r),'numpy');Ef=sy.lambdify(r,E,'numpy')
def ode(lm):
    def fun(s,y):
        vv,ww,zz,tt=y
        if vv>=1.5:
            rv=0.;qv=.5;dv=3/16;cc=np.sqrt(2/(lm*dv));wp=2*np.sqrt(2*lm*dv);zp=-7/9
        else:
            rv=2/np.sqrt(1+2*vv)-1;qv=2*np.sqrt(1+2*vv)-2-vv;gg=4/(1+rv)**3;dv=float(Df(rv));ds=float(Drf(rv))*qv/gg;cc=np.sqrt(2/(lm*dv));wp=2*np.sqrt(2*lm*dv)-rv*ww;wpp=np.sqrt(2*lm)*ds/np.sqrt(dv)-qv/gg*ww-rv*wp
            zp=(cc*lm*float(Bpf(rv))-ww)**2/(2*lm*gg)-cc*cc*lm*float(Ef(rv))-cc*wpp/2-rv*zz
        return [-qv,wp,zp,1/cc]
    return fun

def solve(lm,rtol,atol):
    switch=2/lm-3
    if 0<switch<.5:
        first=solve_ivp(ode(lm),(0,switch),[1/lm,0,0,0],method='DOP853',rtol=rtol,atol=atol,dense_output=True)
        init=first.y[:,-1];init[0]=1.5
        second=solve_ivp(ode(lm),(switch,.5),init,method='DOP853',rtol=rtol,atol=atol,dense_output=True)
        class Combined:
            success=first.success and second.success
            y=second.y
            def sol(self,t):return first.sol(t) if t<=switch else second.sol(t)
        return Combined()
    return solve_ivp(ode(lm),(0,.5),[1/lm,0,0,0],method='DOP853',rtol=rtol,atol=atol,dense_output=True)

def aa(f):
    f=Fraction(f);return arb(fmpq(f.numerator,f.denominator))
consumers=[]
for exact_lm in [Fraction(2,5),Fraction(4,7),Fraction(3,5),Fraction(2,3),Fraction(4,5)]:
    lm=float(exact_lm)
    sol=solve(lm,2e-13,2e-14)
    coarse=solve(lm,1e-11,1e-12)
    ck('numerical_ODE_refinement_'+str(lm),sol.success and coarse.success and max(abs(sol.y[:,-1]-coarse.y[:,-1]))<1e-10)
    vv,ww,zz,clock=sol.y[:,-1]
    for ee in [.001,.0005]:
        n=int(np.floor(clock/ee+.5));states=[Fraction(1,2)]
        for i in range(1,n):
            target=clock*(n-i)/n
            sx=brentq(lambda ss: sol.sol(ss)[3]-target,0,.5,xtol=5e-15)
            states.append(Fraction(round(sx*10**14),10**14))
        states.append(Fraction(0));schedule=[];P=arb(1);resource=arb(0);cost=arb(0);max_step_error=0.
        for s0,s1 in zip(states,states[1:]):
            bb=s0-s1;v0,w0,zv,_=sol.sol(float(s0));rv=max(0.,2/np.sqrt(1+2*v0)-1);gg=4/(1+rv)**3;dv=float(Df(rv));cc=np.sqrt(2/(lm*dv));ratio=max(0.,rv+ee*(w0-cc*lm*float(Bpf(rv)))/(lm*gg)-(max(0.,v0-1.5)/gg))
            av=bb*Fraction(round(ratio*10**14),10**14)
            assert 0<=av<bb,'FAIL actual feasible action'
            P/=1+aa(av);resource+=2*P
            cost+=2*P*(1+(aa(bb)-aa(av))**2/(2*(aa(bb)+aa(av))*(2-aa(bb)-aa(av)))).log()
            schedule.append([str(av),str(bb)]);max_step_error=max(max_step_error,abs(float(bb)-ee*cc))
        tag=str(lm)+'_'+str(ee)
        ck('actual_score_and_count_'+tag,sum((Fraction(v[1]) for v in schedule),Fraction(0))==Fraction(1,2) and len(schedule)==n)
        value=P-aa(exact_lm)*cost-aa(Fraction(str(ee))**2)*resource
        U=lm*vv-ee*ww+ee*ee*zz
        error=float(value.mid())-U
        ck('numerical_constructed_value_residual_'+tag,abs(error)<20*ee**3)
        ck('numerical_whole_mesh_step_error_'+tag,max_step_error<100*ee**2)
        consumers.append({'lambda':str(exact_lm),'e':str(ee),'count':n,'schedule':schedule,'resource_interval':resource.str(25,more=True),'original_priced_value_interval':value.str(25,more=True),'numerical_U':format(U,'.14g'),'numerical_error_over_e3':format(error/ee**3,'.7g'),'numerical_Z':format(zz,'.12g'),'numerical_max_step_error_over_e2':format(max_step_error/ee**2,'.7g')})
report={'result':'K2608','checks':checks,'contrary_controls':controls,'finite_consumers':consumers,'corrector':'Z continuous; Zprime=-7/9 where v>=3/2; interior K2606 ODE where v<3/2','sign':'-7S/9 <= Z <= -583S/76800 < -S/200','theorem_scope':'compact positive S,lambda rectangles in 0<S<=1/2,0<lambda<=4/5, including both switch curves','asymptotics':['Q(k)=V-2sqrt(Ck)+Zk+O(k^1.5)','V-F(M)=C/M-CZ/M²+O(M^-3)','Rmin(eta)=C/eta-Z+O(eta)','every price optimizer R=sqrt(C/k)-Z+O(1)'],'evidence_kind':'exact original-law algebra and constrained-branch controls; rational finite policies evaluated with Arb192; ODE values numerical illustrations, universal band estimates proved analytically in note','activation':'fixed interior switch: r/e=(x/2+(3s0+1)/sqrt(6lambda))_+/4+O(sqrt(e)); not endpoint uniform','ceiling':'no third coefficient, exact optimal count, endpoint-uniform activation, beyond4/5 comparison, physical probability or GU inference'}
refs=['explorations/conditional-build/k2606-interior-stopping-second-corrector-2026-11-06.md','explorations/conditional-build/k2604-second-order-stopping-resource-bound-2026-11-06.md','explorations/conditional-build/k2577-exact-resource-tail-2026-11-05.md']
report['provenance']={f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in refs}
out=root/'lab/process/k2608-switching-stopping-second-corrector.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'FAIL report replay'
print(json.dumps({'result':'K2608','checks':len(checks),'controls':len(controls),'finite_consumers':len(consumers),'status':'pass'}))
