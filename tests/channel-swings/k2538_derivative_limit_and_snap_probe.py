"""Exact identities/contrary controls; continuum proof resides in companion note."""
from pathlib import Path
import hashlib,json,sys
import sympy as s
ROOT=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(bank,name,p):
 bank[name]=bool(p)
 if not p:raise AssertionError('FAIL '+name)
t,O,a,x,y=s.symbols('t O a x y',positive=True);L=1-O+O*t;r=L**s.Rational(3,4);Ds=lambda z:t*s.diff(z,t)
b0=-s.Rational(81,2)*O**2-72*(1-3*O/4)*O
g=b0/216+(1-3*O/4)*O*t/3
f=(x**(-s.Rational(1,3))-L*x**(-s.Rational(5,3)))/36
h0=s.factor(Ds(r)-Ds(Ds(r))+g*r**(-s.Rational(5,3)))
c=s.simplify(s.diff(f,x).subs(x,r));p=s.simplify(h0/c)
ck(checks,'restoring_coefficient',s.simplify(c-1/(27*L))==0)
ck(checks,'slow_correction_cancels',s.simplify(c*p-h0)==0)
ck(checks,'zero_initial_position_correction',p.subs(t,1)==0)
d0=s.simplify(Ds(h0).subs(t,1));ck(checks,'initial_third_difference',s.simplify(d0-O/3-O**2/8)==0)
# Compute the original x''' by total differentiation of the unshifted ODE.
rhs=y-a*f+g*x**(-s.Rational(5,3))
r2=s.simplify(Ds(Ds(r)).subs(t,1));seed={x:1,y:3*O/4,t:1}
ck(checks,'original_second_jet',s.simplify(rhs.subs(seed)-r2)==0)
x3=s.simplify((Ds(rhs)+s.diff(rhs,x)*y+s.diff(rhs,y)*rhs).subs(seed))
ck(checks,'original_third_jet_independent_a',s.simplify(x3-Ds(Ds(Ds(r))).subs(t,1)-d0)==0)
# Universal shifted-energy coefficient accounting and Young residual control.
m,d,k,M,w,wp=s.symbols('m d k M w wp',positive=True)
C=3+d*(1+1/m)+k/m
ck(checks,'energy_bound_coefficients',s.expand(C-(2+d+d/m+1+k/m))==0)
ck(checks,'residual_young_square',s.expand(wp**2/2+M**2/(2*a**2)-M*wp/a-(wp-M/a)**2/2)==0)
# Proper-time jet algebra; D_t=-3H D_s, no cosmography imported.
jets=s.symbols('x0:5',positive=True);H0=s.symbols('H0',positive=True)
DS=lambda z:sum(s.diff(z,jets[i])*jets[i+1] for i in range(4))
HH=H0*jets[0]**s.Rational(2,3);DT=lambda z:s.expand(-3*HH*DS(z))
Hd=DT(HH);Hdd=DT(Hd);Hddd=DT(Hdd)
q=s.simplify(-1-Hd/HH**2);jerk=s.simplify(1+3*Hd/HH**2+Hdd/HH**3)
snap=s.simplify(1+6*Hd/HH**2+3*(Hd/HH**2)**2+4*Hdd/HH**3+Hddd/HH**4)
ck(checks,'deceleration_formula',s.simplify(q-(-1+2*jets[1]/jets[0]))==0)
ck(checks,'jerk_formula',s.simplify(jerk-(1-6*jets[1]/jets[0]+2*(jets[1]/jets[0])**2+6*jets[2]/jets[0]))==0)
ck(checks,'curvature_formula',s.simplify(6*(2*HH**2+Hd)-12*H0**2*jets[0]**s.Rational(1,3)*(jets[0]-jets[1]))==0)
ck(checks,'snap_highest_jet_coefficient',s.diff(snap,jets[3])==-18/jets[0])
snapgap=s.factor(-18*d0);ck(checks,'actual_Omega03_snap_gap',snapgap.subs(O,s.Rational(3,10))==-s.Rational(801,400))
# Fast rescaling derivatives of original residual; no sampled convergence claim.
e,T,U=s.symbols('e T U',real=True);ct0=s.Rational(1,27)
# Taylor coefficients suffice for smooth extension: f(s,0)=0, h0(0)=0.
ck(checks,'fast_restoring_limit',c.subs(t,1)==ct0)
ck(checks,'fast_forcing_slope',s.simplify(s.limit(h0.subs(t,s.exp(e*T))/e,e,0)-d0*T)==0)
UU=d0/ct0*(T-s.sin(s.sqrt(ct0)*T)/s.sqrt(ct0))
ck(checks,'fast_limit_original_ivp',s.simplify(s.diff(UU,T,2)+ct0*UU-d0*T)==0 and UU.subs(T,0)==0 and s.diff(UU,T).subs(T,0)==0)
b=s.symbols('b',positive=True);D3=lambda z:s.simplify((z.subs(T,3*b)-3*z.subs(T,2*b)+3*z.subs(T,b)-z.subs(T,0))/b**3)
fd=D3(UU)
ck(checks,'shrinking_window_derivative_limit',s.simplify(s.limit(fd,b,0)-d0)==0)
ck(checks,'third_difference_cubic_normalization',D3(T**3)==6)
ck(checks,'absolute_noise_weights',sum(map(abs,[1,-3,3,-1]))==8)
err=s.symbols('err',positive=True);ck(checks,'worst_case_noise_attained',s.Matrix([1,-3,3,-1]).dot(s.Matrix([err,-err,err,-err]))==8*err)
ck(controls,'fixed_window_loses_derivative_signal',s.limit(8/(a*b**3),a,s.oo)==0 and d0.subs(O,s.Rational(3,10))!=0)
ck(controls,'one_period_sampling_alias',s.simplify(fd.subs(b,2*s.pi/s.sqrt(ct0)))==0)
ck(controls,'dropping_proper_time_minus_sign_changes_snap',18*d0!=-18*d0)
ck(controls,'near_prepared_different_seed',s.diff(p,t).subs(t,1)!=0)
ck(controls,'nonzero_initial_third_jet_prevents_C3',d0.subs(O,s.Rational(3,10))==s.Rational(89,800))
report={'result':'K2538','exact_checks':checks,'contrary_controls':controls,'scope':'same jet-matched family C2 not C3 on observer-inclusive compact interval; exact snap and conditional finite-window/noise scaling; no empirical/native GU claim','identities':{'c':str(c),'d0':str(d0),'snap_gap':str(snapgap),'fast_profile':str(UU),'finite_difference':str(fd)},'dependencies':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['tests/channel-swings/k2536_einstein_limit_closure_probe.py',str(Path(__file__).relative_to(ROOT))]}}
out=ROOT/'lab/process/k2538-derivative-limit-and-snap.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==report
print('K2538',len(checks),'exact identity/fixture checks',len(controls),'contrary controls')
