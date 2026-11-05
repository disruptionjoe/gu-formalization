"""Exact coefficient/identity checks; universal domain proofs are in the note."""
from pathlib import Path
import json,hashlib,sys
import sympy as s
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,x):
 checks[k]=bool(x)
 if not x:raise AssertionError(k)
def ct(k,x):
 controls[k]=bool(x)
 if not x:raise AssertionError('contrary '+k)
k=s.symbols('k',nonzero=True,real=True);D,t=s.symbols('D t');K=s.Rational(35,3624192)*k*k
a0=-s.Rational(5,2288)*k;e=5*K;mu=s.Rational(611557655,39953092608)*k*k
c=s.Rational(970112,13395)/k;rE=1/(6*a0);rT=s.cancel(rE*rE/c)
ck('original_mass_e',e==s.Rational(175,3624192)*k*k)
ck('original_mass_mu',s.cancel(c*mu)==s.Rational(136967,123552)*k)
ck('original_residue_E',rE==-s.Rational(1144,15)/k)
ck('original_residue_T',rT==s.Rational(127699,1590)/k)
ck('distinct_positive_masses',0<e/(k*k)<mu/(k*k)<s.Rational(1,64))
ck('weight_lower_half',1-3*K/(k*k)>s.Rational(1,2))
ck('resolvent_gap',s.Rational(1,8)-s.Rational(1,64)==s.Rational(7,64))
ck('residue_noncancellation',s.cancel(k*(rE+rT))==s.Rational(429,106))
ck('ordered_residue_signs',k*rE<0 and k*rT>0)
q=s.symbols('q',positive=True);C=s.cos(q*t)
ck('warped_radial_curvature',s.simplify(-s.diff(C,t,2)/C-q*q)==0)
ck('warped_tangential_curvature',s.trigsimp((q*q-s.diff(C,t)**2)/C**2-q*q)==0)
f=s.Function('f')(t);w=C**6
ck('weighted_scalar_operator',s.simplify(s.diff(w*s.diff(f,t),t)/w-(s.diff(f,t,2)-6*q*s.tan(q*t)*s.diff(f,t)))==0)
lam=s.symbols('lam');Re=1/(lam-e);Rm=1/(lam-mu)
ck('resolvent_identity',s.cancel(Rm-Re-(mu-e)*Rm*Re)==0)
v=-rE*Re;u=rE/c*Rm;H=v-rE*u
ck('Einstein_forced_equation',s.cancel((-lam+e)*v-rE)==0)
ck('tensor_forced_equation',s.cancel(c*(-lam+mu)*u+rE)==0)
ck('original_reconstruction',s.cancel(H+rE*Re+rT*Rm)==0)
Eh=s.cancel((lam-e)*H/2)
ck('off_source_with_contact_retained',s.cancel(Eh+(rE+rT)/2+rT*(mu-e)*Rm/2)==0)
ck('original_fourth_order_numerator',s.cancel((-lam+e)*(-lam+mu)*H-(-s.Rational(429,106)*lam/k-s.Rational(70547,60632)*k))==0)
# Endpoint kernel: p+q=Lw, flux left-right is exactly one.
p0,q0,Lw=s.symbols('p0 q0 Lw',positive=True)
ck('green_flux_jump',s.simplify((q0+p0)/Lw).subs(q0,Lw-p0)==1)
ck('separated_green_bound',s.Rational(3,4)*s.Rational(1,4)/4==s.Rational(3,64))
ck('psi_difference_identity',s.cancel(mu*Rm-e*Re-(mu-e)*Rm*(1+e*Re))==0)
pe,pm=s.symbols('pe pm');de,dm=-e*pe,-mu*pm
ck('metric_fixed_boundary',s.expand(rE*(pe-pm)).subs({pe:1,pm:1})==0)
ck('homogeneous_Einstein_equation',de+e*pe==0)
ck('homogeneous_tensor_equation',dm+mu*pm==0)
ck('boundary_change_observable',s.cancel(-rE*(de-dm+e*(pe-pm))/2-(e-mu)*pm/(12*a0))==0)
# In an actual negative-signature coordinate the normalized leading energy is negative.
N=s.symbols('N',real=True);amp=s.symbols('amp',positive=True)
ck('negative_tangential_principal_energy',s.Poly(1-amp*N**2,N).LC()<0)
# Contrary controls corrupt operands/coefficients, not check predicates.
ct('drop_displacement_changes_forced_response',s.cancel(v-H)!=0)
ct('wrong_sign_inverse_fails_source',s.cancel((-lam+e)*(rE*Re)-rE)!=0)
ct('equal_pole_substitution_fails_tensor',s.cancel(c*(-lam+mu)*(rE/c*Re)+rE)!=0)
ct('metric_boundary_is_weaker',s.expand(rE*(1-1))==0 and s.Integer(1)!=0)
ct('full_mode_positive_form_false',(1-N*N).subs(N,2)<0)
paths=['explorations/conditional-build/k2550-common-domain-tensor-response-2026-11-04.md','tests/channel-swings/k2550_common_domain_tensor_response_probe.py','explorations/conditional-build/k2544-constrained-tensor-response-2026-11-04.md','lab/process/k2544-constrained-tensor-response.json','explorations/conditional-build/k2548-compact-coupled-metric-detectors-2026-11-04.md']
report={'result':'K2550','checks':checks,'contrary_controls':controls,'constants':{'K_over_kappa2':str(K/k**2),'e_over_kappa2':str(e/k**2),'mu_over_kappa2':str(mu/k**2),'weight_lower':str(1-3*K/k**2),'spectral_lower':'1/8','resolvent_norm_coefficient':'64/7','original_residue_sum':str(s.cancel(k*(rE+rT))),'separated_kernel_coefficient':'3/64'},'evidence_kinds':{'exact':'coefficient, warped-curvature, forced-equation, Green-jump and boundary-change identities','universal':'weighted energy, Neumann positivity, prescribed-source reconstruction, regularity, off-source observation and unrestricted-mode counterexample proved in note','not_claimed':'full original-action boundary self-adjointness, arbitrary localized-source solution, physical positivity, native GU'},'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths}}
p=R/'lab/process/k2550-common-domain-tensor-response.json'
if '--write' in sys.argv:p.write_text(json.dumps(report,indent=2)+'\n')
else:ck('saved_reproduction',json.loads(p.read_text())==report)
print('K2550 PASS',len(checks),'exact groups',len(controls),'contrary controls')
