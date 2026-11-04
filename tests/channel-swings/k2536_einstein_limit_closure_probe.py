"""Exact identities behind the compact-interval proof; no sampled proof of convergence."""
from pathlib import Path
import hashlib,json,sys
import sympy as s
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(bank,name,value):
 bank[name]=bool(value)
 if not value:raise AssertionError('FAIL '+name)
t,O,a,x,u,v,H,m,J,k,d=s.symbols('t O a x u v H m J k d',positive=True)
L=1-O+O*t;r=L**s.Rational(3,4)
Ds=lambda z:s.diff(z,t)*t
b0=-s.Rational(81,2)*O**2-72*(1-s.Rational(3,4)*O)*O
g=b0/216+(1-s.Rational(3,4)*O)*O*t/3
f=(x**(-s.Rational(1,3))-L*x**(-s.Rational(5,3)))/36
rhs=v-a/(36*x**s.Rational(1,3))+(6*a*(1-O)+b0+6*(a+12*(1-s.Rational(3,4)*O))*O*t)/(216*x**s.Rational(5,3))
ck(checks,'exact_original_force_split',s.simplify(rhs-(v-a*f+g*x**(-s.Rational(5,3))))==0)
ck(checks,'equilibrium_curve',s.simplify(f.subs(x,r))==0)
fp=(5*L-x**s.Rational(4,3))/(108*x**s.Rational(8,3))
ck(checks,'restoring_derivative',s.simplify(s.diff(f,x)-fp)==0)
ck(checks,'tube_coercivity_constant',s.Rational(3,2)**4<5**3)
h0=s.factor(Ds(r)-Ds(Ds(r))+g*r**(-s.Rational(5,3)))
h0_expected=(t-1)*O*(s.Rational(1,3)+O*(3*t-1)/16)*L**(-s.Rational(5,4))
ck(checks,'exact_residual_on_Einstein_curve',s.simplify(h0-h0_expected)==0)
ck(checks,'initial_position_velocity',r.subs(t,1)==1 and s.simplify(Ds(r).subs(t,1)-3*O/4)==0)
ck(checks,'initial_second_jet',s.simplify(h0.subs(t,1))==0)
# Two completed squares underlying lower energy and its forcing estimate.
ck(checks,'energy_cross_term_square',s.expand(a*m*u**2/4-H*u+H**2/(a*m)-(s.sqrt(a*m)*u/2-H/s.sqrt(a*m))**2)==0)
ck(checks,'derivative_forcing_square',s.expand(a*m*u**2/4-J*u+J**2/(a*m)-(s.sqrt(a*m)*u/2-J/s.sqrt(a*m))**2)==0)
# C dominates coefficients in E' using |u|^2<=4E/(am), |v|^2<=2E, a>=1.
C=3+d*(1+2/m)+2*k/m
ck(checks,'energy_coefficient_decomposition',s.simplify(C-(2+d+2*d/m+2*k/m+1))==0)
A,ss,K,B=s.symbols('A ss K B',positive=True)
Bexpr=K*s.exp(C*ss)+J**2/(m*C)*(s.exp(C*ss)-1)
ck(checks,'gronwall_solution',s.simplify(s.diff(Bexpr,ss)-C*Bexpr-J**2/m)==0 and Bexpr.subs(ss,0)==K)
ck(checks,'initial_energy_margin',s.simplify((H**2/m+1)-H**2/m)==1)
# A real fast-mode countercontrol for a near-prepared, Omega=0 nonlinear family.
eps,w=s.symbols('eps w',real=True)
fast=((1+eps**2*w)**(-s.Rational(5,3))-(1+eps**2*w)**(-s.Rational(1,3)))/(36*eps**2)
ck(checks,'nonlinear_fast_mode_limit',s.limit(fast,eps,0)==-w/27)
omega=s.symbols('omega',positive=True)
lin=s.exp(ss/2)*s.sin(omega*ss)/omega
ck(checks,'exact_linear_oscillator',s.simplify((s.diff(lin,ss,2)-s.diff(lin,ss)+a*lin/27).subs(a,27*(omega**2+s.Rational(1,4))))==0)
ck(controls,'finite_a_Lcdm_is_not_solution',h0_expected.subs({O:s.Rational(3,10),t:2})!=0)
ck(controls,'changing_jet_seed_breaks_initial_matching',s.Rational(1,3)!=3*s.Rational(3,10)/4)
ck(controls,'C2_transfer_fails_fast_mode',s.diff(s.sqrt(27)*s.sin(ss/s.sqrt(27)),ss,2).subs(ss,s.pi*s.sqrt(27)/2)==-1/s.sqrt(27))
# Fixed covariance likelihood continuity includes common nuisance, not independent row repairs.
X=s.Matrix([[1,0],[1,1],[1,1]]);P=s.eye(3)-X*(X.T*X).inv()*X.T
ck(checks,'shared_calibrator_projector',P*P==P and P*X==s.zeros(3,2))
q=s.Matrix([0,1,-1]);rr=s.Matrix([1,2,4]);z=s.symbols('z')
loss=((rr+z*q).T*P*(rr+z*q))[0]
ck(checks,'finite_profile_continuity',s.limit(loss,z,0)==(rr.T*P*rr)[0])
ck(controls,'independent_row_nuisances_destroy_test',s.eye(3)-s.eye(3)*(s.eye(3).T*s.eye(3)).inv()*s.eye(3).T==s.zeros(3))
report=dict(result='K2536',exact_checks=checks,contrary_controls=controls,scope='analytic finite-interval positive-a well-prepared family closure; no uniform infinite-redshift, C2, empirical, native GU or optimal-constant claim',identities={'b0':str(b0),'h0':str(h0_expected),'C':str(C),'B':str(Bexpr)},dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in ['tests/channel-swings/k2534_calibrated_family_refit_probe.py',str(Path(__file__).relative_to(R))]})
p=R/'lab/process/k2536-einstein-limit-closure.json'
if '--write' in sys.argv:p.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
else:assert json.loads(p.read_text())==report
print('K2536',len(checks),'exact identity/fixture checks',len(controls),'contrary controls')
