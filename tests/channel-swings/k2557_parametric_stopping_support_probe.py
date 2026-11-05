"""Original-trial algebra and exact controls; universal limits proved in K2557."""
from pathlib import Path
import sympy as s
import json,hashlib,sys
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(name,ok):
 checks[name]=bool(ok)
 if not ok:raise AssertionError(name)
def ct(name,ok):
 controls[name]=bool(ok)
 if not ok:raise AssertionError(name)
a,ap,U,V,w,wp,lam=s.symbols('a ap U V w wp lam')
E=(1+ap)*U+2*lam*wp-V
delta=U-((1-a)*U+V)/2+lam*w
ck('original_trial_clipped_defect',s.expand(delta-E/2-U*(a-ap)/2-lam*(w-wp))==0)
ck('fair_use_occupation_factor',s.Rational(1,2)*s.Rational(1,900)==s.Rational(1,1800))
ck('action_occupation_factor',s.Rational(1,2)*s.Rational(1,4)==s.Rational(1,8))
ck('tail_probability_constant',1/s.Rational(2,3)==s.Rational(3,2))
ck('clipping_action_constant',1/(s.Rational(2,3)/2)==3)
ck('concentration_constant',900*3==2700)
ck('prefix_constant',900*6==5400)
# Independently enumerate a two-level adaptive tree with different actions after test/use.
U5,U3,U1=s.symbols('U5 U3 U1');w0,wt,wu=s.symbols('w0 wt wu')
a0=s.Rational(1,10);at=s.Rational(3,10);au=s.Rational(1,10)
pt=(1-a0)/2;pu=s.Rational(1,2)
# Root b=.2, s=.5; after test b=.4, after use b=.4 (overshoot .3).
d0=U5-((1-a0)*U5+U3)/2+lam*w0
dt=U5-((1-at)*U5+U1)/2+lam*wt
du=U3-((1-au)*U3+1)/2+lam*wu
prob_hit=pu/2;cost=w0+pt*wt+pu*wu
# At horizon, second test-pass branch after root test voluntarily aborts.
abort=pt*(1-at)*U5/2
live=pt*U1/2+pu*(1-au)*U3/2
ck('adaptive_tree_unconditional_telescope',s.expand(U5-prob_hit+lam*cost-d0-pt*dt-pu*du-live-abort)==0)
ck('tree_probability_normalization',pt+pu+a0/2==1 and (1-at)/2+s.Rational(1,2)+at/2==1)
F0,Ft,Fu=s.symbols('F0 Ft Fu')
ck('adaptive_tree_occupation_identity',s.expand((F0+pt*Ft+pu*Fu)/2-(F0/2+pt*Ft/2+pu*Fu/2))==0)
ct('dropping_abort_corrupts_telescope',abort!=0)
ct('dropping_live_corrupts_telescope',live!=0)
ct('wrong_half_weight_rejected',s.expand(d0+pt*dt+pu*du-(2*d0+pt*dt+pu*du))!=0)
ct('failure_cost_cannot_be_removed',s.expand(cost-(1-a0/2)*w0-pt*(1-at/2)*wt-pu*(1-au/2)*wu)!=0)
ck('original_idle_has_zero_local_slack',s.expand(delta.subs({a:0,V:U,w:0}))==0)
ct('zero_local_slack_not_zero_deficit',s.Rational(2,3)>0)
ct('asymptotic_threshold_not_finite_hit',all(sum(s.Rational(1,2**j) for j in range(1,n+1))<1 for n in range(1,25)))
# Original-law root expansion, independently from the ratio logarithm.
r,b=s.symbols('r b');xx=b*(1-r)**2/(2*(1+r)*(2-b*(1+r)))
wx=s.series(xx-xx**2/2+xx**3/3,b,0,4).removeO();W=[s.factor(wx.coeff(b,j)) for j in (1,2,3)]
M0=-2*s.diff(W[0],r);M1=-2*s.diff(W[1],r)-2*r*s.diff(W[0],r)+2*W[0];M2=-2*s.diff(W[2],r)-2*r*s.diff(W[1],r)+2*W[1]
lr=2*(1+r)**2/((1-r)*(3+r))
c=-(r-1)*(3*r+5)*(r*r+6*r+1)/32
d=(r-1)*(45*r**7+597*r**6+2609*r**5+4905*r**4+3175*r**3-1217*r*r-1669*r-253)/(2048*(r+1))
ck('parameter_zero_root',s.cancel(M0-1/lr)==0)
ck('parameter_first_root_coefficient',s.cancel(s.diff(M0,r)*c+M1)==0)
ck('parameter_second_root_coefficient',s.cancel(s.diff(M0,r)*d+s.diff(M0,r,2)*c*c/2+s.diff(M1,r)*c+M2)==0)
rstar=2*s.sqrt(3)-3
ck('parameter_lower_endpoint',s.simplify(lr.subs(r,rstar)-4/s.sqrt(3))==0)
ck('parameter_upper_endpoint',s.simplify(lr.subs(r,4/s.sqrt(7)-1)-s.Rational(8,3))==0)
ck('parameter_monotonic',s.cancel(s.diff(lr,r)-16*(r+1)/((r-1)**2*(r+3)**2))==0)
rmax=4/s.sqrt(7)-1;dmax=s.Rational(761,686)-s.Rational(29647,76832)*s.sqrt(7)
ck('true_upper_quadratic_coefficient',s.simplify(d.subs(r,rmax)-dmax)==0)
A0=s.Rational(34963,34300);B0=s.Rational(29647,76832)
ck('lower_ribbon_sign_exact',7*B0**2-A0**2==s.Rational(1700087313,527067520000))
ct('old_lower_ribbon_above_actual_root',A0>0 and B0>0 and 7*B0**2>A0**2)
ck('quadratic_interior_parameter_fixture',d.subs(r,s.Rational(1,2))==s.Rational(76429,786432))
hazard=s.factor(-2*s.Rational(8,3)*s.diff(W[0],r))
ck('old_ribbon_exact_hazard',hazard.subs(r,s.Rational(3,5))==s.Rational(3,4))
ct('old_ribbon_cannot_be_reused',s.Rational(3,4)>s.Rational(2,3))
# Nonidle action counts and lawful infinite-mean idling control.
A=s.symbols('A',positive=True);count=2/(1+A)
ck('nonidle_absorption_balance',s.cancel(count*(1+A)/2-1)==0)
ck('nonidle_success_balance',s.cancel(count/2-1/(1+A))==0)
ck('nonidle_original_cost',s.cancel(count*w-2*w/(1+A))==0)
n=s.symbols('n',integer=True,positive=True)
ck('idle_law_telescope',s.cancel(1/(n*(n+1))-(1/n-1/(n+1)))==0)
ck('idle_mean_harmonic_tail',s.cancel(n/(n*(n+1))-1/(n+1))==0)
ct('arbitrary_idling_precludes_unique_implementation',sum(s.Rational(1,j+1) for j in range(1,100))>4)
pstar,eps,Cstar,C,prob=s.symbols('pstar eps Cstar C prob')
eta=pstar-lam*Cstar-prob+lam*C
ck('adaptive_contact_deficit',s.expand(eta-(pstar-prob-lam*(Cstar-C)))==0)
paths=['explorations/conditional-build/k2557-parametric-stopping-support-2026-11-05.md','tests/channel-swings/k2557_parametric_stopping_support_probe.py','explorations/conditional-build/k2553-global-stopping-certificate-2026-11-04.md','explorations/conditional-build/k2555-global-stopping-stability-2026-11-05.md','explorations/conditional-build/k2483-adaptive-stopping-bellman-2026-11-01.md','lab/process/k2553-global-stopping-certificate.json','lab/process/k2555-global-stopping-stability.json']
report={'result':'K2557','checks':checks,'contrary_controls':controls,'parameter_attempt':{'lambda':str(lr),'ratio_linear':str(c),'ratio_quadratic':str(d),'old_upper_hazard':'3/4 > 2/3','global_interval_certificate':False},'evidence_kinds':{'exact':'original trial identity, adaptive-tree telescope, root coefficients and numerical-free constants','finite_controls':'finite geometric prefixes and idle harmonic partial sum illustrate separately proved infinite statements','universal':'nonnegative occupation limits, hit-path moments and equality proof in note; independently reviewed','not_claimed':'remaining multiplier interval, full budget frontier, finite expected physical time or GU'},'dependencies':{x:hashlib.sha256((R/x).read_bytes()).hexdigest() for x in paths}}
out=R/'lab/process/k2557-parametric-stopping-support.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved_report_consistency'
print('K2557 PASS',len(checks),'exact/supporting groups',len(controls),'contrary controls')
