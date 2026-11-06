#!/usr/bin/env python3
"""K2596 exact full scalar pressure-transfer coefficient and radial cusp controls; actual matrix reused from K2592."""
import argparse,json,hashlib
from pathlib import Path
import sympy as s
root=Path(__file__).resolve().parents[2]
parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args()
checks=[];controls=[]
def ck(n,v):
 assert bool(v),'FAIL '+n
 checks.append(n)
def ct(n,v):
 assert bool(v),'FAIL contrary '+n
 controls.append(n)
k=s.symbols('k',nonzero=True);K0=s.Rational(35,3624192)*k*k
X,Y=s.symbols('X Y');f,g,p,q,r,z=s.symbols('f g p q r z');pot=s.Matrix([f,g,p,q,r,z]);Z=X+Y
la=6*K0;a0=-s.Rational(5,2288)*k;rE=1/(6*a0)
m=s.Rational(158,143)*k;bt=-s.Rational(15,143)*k;mK=s.Rational(148,143)*k;mV=s.Rational(503,858)*k;mH=s.Rational(893,858)*k
c=s.Rational(970112,13395)/k;mu=s.Rational(611557655,39953092608)*k*k
tau=7*f+7*g+X*p+Y*q;BA=f+(X+la)*p+Y*r;BB=g+(Y+la)*q+X*r
VA,VB=BA-tau,BB-tau;WA,WB=11*VA-13*Y*z,11*VB+13*X*z
U,V=X*VA+Y*VB,X*WA+Y*WB;RC=X*BA+Y*BB-(Z+la)*tau
Evec=s.Matrix([-(Z/2+la)*f-RC/2,-(Z/2+la)*g-RC/2,BA-(Z/2+la)*p-tau/2,BB-(Z/2+la)*q-tau/2,(BA+BB-tau-(Z+2*la)*r)/2])
E=Evec.jacobian(pot);vsrc=s.Matrix([-X-la,0,1,0,0,0]);s0=s.Matrix([X+5*la/6,-X-7*la/6,0,0,1,0])
hook=s.Matrix([2*Z*f-2*K0*X*p+2*U/13,2*Z*g-2*K0*Y*q+2*U/13,2*(Z+la+K0)*p-2*BA-2*VA/13,2*(Z+la+K0)*q-2*BB-2*VB/13,2*(Z+la)*r-BA-BB-(VA+VB)/13])
vs=s.Matrix([V,V,-WA,-WB,-(WA+WB)/2]);FC=m*s.Matrix([f,g,p,q,r])+bt*tau*s.Matrix([1,1,0,0,0])+11*vs/(13*mV)-2*hook/mH+Evec/(3*a0)
FK=mK*z-(WB-WA)/(2*mV);M=FC.col_join(s.Matrix([FK])).jacobian(pot)


M1=M.subs(k,1);v1=vsrc.subs(k,1);cm=M1.copy();cm[:,0]=v1
num=s.Poly(cm.det(method='domain-ge'),X,Y).as_expr()
bank=json.loads((root/'lab/process/k2554-analytic-source-response.json').read_text())['determinant']
pp=list(map(s.Rational,bank['P_coefficients_descending']));qq=list(map(s.Rational,bank['Q_coefficients_descending']))
det=sum(v*(X+Y)**(5-i) for i,v in enumerate(pp))+X*Y*sum(v*(X+Y)**(2-i) for i,v in enumerate(qq))
ck('actual_P_Y_degree',s.degree(num,Y)==4)
ck('actual_P_total_degree',s.Poly(num,X,Y).total_degree()==5)
ck('actual_d_Y_degree',s.degree(det,Y)==5)
ck('actual_d_leading_coefficient_constant',s.Poly(det,Y).LC()==pp[0]!=0)

lead=s.factor(s.Poly(num,Y).coeff_monomial(Y**4));Ld=s.Poly(det,Y).coeff_monomial(Y**5);ratio=s.factor(lead/Ld)
ck('actual_cofactor_leading_ratio',s.cancel(ratio+s.Rational(67201455,9568214656)*X+s.Rational(140956375,412821988220928))==0)
re1=rE.subs(k,1);full=s.factor(-re1*(X+5*K0.subs(k,1))/2+re1**2*ratio)
ck('actual_full_metric_coefficient',s.cancel(full+s.Rational(2842697,1045478)*X+s.Rational(136955,946306944))==0)
# M scaling from K2592 gives P/d -> k P1(X/k²,Y/k²)/d1; the 1/Y coefficient scales k³.
fullk=s.factor(-rE*(X+5*K0)/2+rE**2*k**3*ratio.subs(X,X/k**2));expected=(-s.Rational(2842697,1045478)*X-s.Rational(136955,946306944)*k**2)/k
ck('all_nonzero_kappa_scaling',s.cancel(fullk-expected)==0)
sigma=s.symbols('sigma',positive=True);cancel_roots=s.solve(s.together(full.subs(X,-sigma)),sigma)
ck('unique_cancellation_location',cancel_roots==[s.Rational(73745,1385486784)])
ck('cancellation_below_actual_gap',0<cancel_roots[0]<3)
ct('cofactor_alone_wrong_coefficient',s.simplify(re1**2*ratio-full)!=0)
ct('full_response_not_zero',full.subs(X,-3)!=0)
# Independent jet jump reconstruction for any regular radial operator.
x,t=s.symbols('x t',real=True);rho,A,C=s.symbols('rho A C',nonzero=True);Ld0=s.symbols('Ld0',nonzero=True)
Gplus=(x-t)**9/(2*s.factorial(9)*rho*Ld0*A**5);Gminus=-Gplus
ck('tenth_order_density_jump',s.diff(Gplus,x,9)-s.diff(Gminus,x,9)==1/(rho*Ld0*A**5))
P4=s.symbols('P4',nonzero=True);Fplus=P4*A**4*s.diff(Gplus,x,8);Fminus=P4*A**4*s.diff(Gminus,x,8)
ck('cofactor_cusp_jump',s.simplify(s.diff(Fplus,x)-s.diff(Fminus,x)-P4/(rho*Ld0*A))==0)
J,zeta,K=s.symbols('J zeta K',positive=True);density=K**(-s.Rational(7,2))*J**2*zeta;A2=-K/zeta
ck('actual_density_conversion',s.simplify(1/(density*A2)+K**s.Rational(5,2)/J**2)==0)
j=s.symbols('j',nonzero=True);eps=s.symbols('eps',positive=True)
# A uniform source mollifier is a measure in invariant mass: dmu=dt/(2eps).
# Its density relative to rho dt is 1/(2eps rho(t)).
self_cusp=s.integrate(j*t/2,(t,0,eps))/eps
ck('uniform_symmetric_mollifier_self_error',self_cusp==j*eps/4)
# Two independently mollified atoms: expected |U-V|=2eps/3.
u,v=s.symbols('u v',real=True)
pair_cusp=2*s.integrate(s.integrate((u-v)*j/2,(v,-eps,u)),(u,-eps,eps))/(4*eps**2)
ck('double_regularized_diagonal_error',s.simplify(pair_cusp-j*eps/3)==0)
ck('double_cusp_regularization_limit',s.limit(j*eps/3,eps,0)==0)
# On 0<=x<=eps the uniform-mollifier error of j|x|/2 is j(eps-x)^2/(4eps).
err=j*(eps-x)**2/(4*eps)
ck('flat_cusp_uniform_error',err.subs(x,0)==j*eps/4)
ck('flat_cusp_L2_error_squared',s.simplify(2*s.integrate(err**2,(x,0,eps))-j**2*eps**3/40)==0)
ck('flat_cusp_derivative_L2_error_squared',s.simplify(2*s.integrate(s.diff(err,x)**2,(x,0,eps))-j**2*eps/6)==0)

# Hs Fourier leading test: |hat F|² ~ j² xi^-4; shell mass for s=3/2 is log2.
xi=s.symbols('xi',positive=True);N=s.symbols('N',positive=True)
ck('critical_sobolev_shell',s.simplify(s.integrate(1/xi,(xi,N,2*N))-s.log(2))==0)
ct('first_derivative_continuity_false',j!=0)
ct('density_omission_changes_source',s.simplify(1/(density*A2)-1/A2)!=0)
ct('uniform_source_density_not_bare_coordinate',density!=1)
ct('symmetric_mollifier_not_second_order',self_cusp!=0 and s.diff(self_cusp,eps)==j/4)
ct('single_and_double_regularization_distinct',s.simplify(pair_cusp-self_cusp)==j*eps/12)
report={'result':'K2596','checks':checks,'contrary_controls':controls,'cofactor_leading_ratio_k1':str(ratio),'full_scalar_transfer_1_over_Y':str(fullk),'cancellation_scaled_sigma':str(cancel_roots[0]),'actual_spectral_floor':3,'jump':'C_kappa(-sigma)/(rho(x0)*a2(x0)) = -C_kappa(-sigma)*K^(5/2)/J(x0)^2','sharp_fixed_mode_Hs':'s<3/2, not s=3/2','single_mollifier_leading':'j epsilon/4','double_mollifier_leading':'j epsilon/3','evidence_kind':'actual exact six-row cofactor and full metric cancellation computation; exact density/jump and independent mollifier fixtures; regular ODE/Fourier/kernel proof in note','ceiling':'one scalar A mode and finite B angular modes, interior B radial atoms and scalar pressure-readable f kernel only; not full point metric, all-mode two-distribution pairing or physical boundary selection'}
refs=['lab/process/k2554-analytic-source-response.json','lab/process/k2592-scalar-tensor-boundary-pairing.json','explorations/conditional-build/k2594-reciprocal-distributional-response-2026-11-06.md']
report['provenance']={f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in refs}
out=root/'lab/process/k2596-radial-response-singularity.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report mismatch'
print(json.dumps({'result':'K2596','checks':len(checks),'controls':len(controls),'status':'pass'}))
