"""Exact radial-geodesic measurement identities and conditional weak-test consumer."""
from pathlib import Path
import sympy as s
import json,hashlib,sys
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not checks[k]:raise AssertionError(k)
def ct(k,v):
 controls[k]=bool(v)
 if not controls[k]:raise AssertionError(k)
y,X,K,H0,He=s.symbols('y X K H0 He',positive=True);p=s.symbols('p',real=True);v=s.symbols('v',real=True);d=s.symbols('d',positive=True)
D=s.sqrt(1+2*p*X);yy=X/D;Sp=s.sqrt(1+p*p*y*y);Dp=Sp+p*y;Xp=y*Dp
# Exact source momentum and null clock differentiated before algebraic elimination.
gamma=1/s.sqrt(1-v*v);Pe=s.symbols('Pe');ae=s.symbols('ae',positive=True)
vdot=-He*v*(1-v*v)
ck('geodesic_momentum_conserved',s.simplify(He*ae*gamma*v+ae*s.diff(gamma*v,v)*vdot)==0)
ck('rapidity_derivative',s.simplify(s.diff(s.log(gamma*(1+v)),v)-1/(1-v*v))==0)
clock=1/(y*(1+v));logdrift=H0-He*clock+vdot/(1-v*v)*clock
ck('exact_geodesic_observed_drift',s.simplify(logdrift-(H0-He/y))==0)
ck('null_emission_clock',s.simplify((1+v)*clock-1/y)==0)
ct('holding_source_speed_constant_changes_drift',s.simplify(H0-He*clock-logdrift)!=0)
# Reference lightcone relation and correct observer-time p_dot.
ck('D_square_inversion',s.simplify(Dp**2-1-2*p*Xp)==0)
ck('redshift_map_monotone_derivative',s.simplify(s.diff(yy,X)-(1+p*X)/D**3)==0)
ck('momentum_derivative_X',s.simplify(s.diff(Xp,p)-y*y*Dp/Sp)==0)
# Algebraic independent rapidity parameter eliminates square roots in drift control.
vr=(d*d-1)/(d*d+1);pr=(d-1/d)/(2*y);spr=(d+1/d)/2
Xy=s.diff(Xp,y).subs({Sp:spr,p:pr},simultaneous=True)
Xpp=s.diff(Xp,p).subs({Sp:spr,p:pr},simultaneous=True)
ydot=y*H0-He/(1+vr)
actual=s.factor(Xy*ydot+Xpp*(-H0*pr))
ck('reference_p_time_evolution_restores_drift',s.simplify(actual-(y*d*H0-d*He))==0)
ct('fixed_reference_p_time_derivative_wrong',s.simplify(Xy*ydot-(y*d*H0-d*He))!=0)
ck('reference_origin',s.simplify((s.sqrt(1+p*p)+p)**2-1-2*p*(s.sqrt(1+p*p)+p))==0)
ct('observed_one_is_not_origin',s.simplify(yy.subs(X,1)-1)!=0)
# Physical reciprocity: transverse screen unchanged under radial Lorentz boost.
eta=s.diag(1,-1,-1,-1);gam=(d+1/d)/2;vel=(d*d-1)/(d*d+1);boost=s.eye(4);boost[0,0]=boost[1,1]=gam;boost[0,1]=boost[1,0]=gam*vel
ck('radial_boost_Lorentz',s.simplify(boost.T*eta*boost-eta)==s.zeros(4))
ck('transverse_screen_unchanged',boost[:,2]==s.eye(4)[:,2] and boost[:,3]==s.eye(4)[:,3])
chi=s.symbols('chi',positive=True);DL=(y*d)**2*chi/y
ck('luminosity_reciprocity_squared_Doppler',s.expand(DL-y*d*d*chi)==0)
ck('reduced_distance_has_D_factor',s.cancel(DL/(y*d)-d*chi)==0)
ct('dropping_Doppler_anchor_factor_changes_distance',s.expand(d*chi-chi)!=0)
# Jacobian and nonlinear anchor, including zero-baseline and effective calibration.
q,G,b=s.symbols('q G b');Hrep=yy*(q-G/X)
ck('observed_anchor_Jacobian',s.simplify(s.diff(yy,X)/Hrep-(1+p*X)/(D**2*(X*q-G)))==0)
ck('common_calibration_cancels',s.expand(yy*((q+b)-(G+b*X)/X)-Hrep)==0)
ck('p_zero_comoving_limit',yy.subs(p,0)==X and D.subs(p,0)==1)
ct('Jacobian_omission_changes_integral',s.simplify(s.diff(yy,X)/Hrep-1/(X*q-G))!=0)
# Exact deSitter and coasting histories; source and anchor repaired together.
Gd=K*(X-D);hd=s.simplify(Hrep.subs({q:K,G:Gd}));ck('deSitter_full_reconstruction',hd==K)
integ=(1+p*X)/(D**2*(X*K-Gd));ck('deSitter_anchor_antiderivative',s.simplify(integ-s.diff((yy-1)/K,X))==0)
ck('coasting_geodesic_drift_zero',s.expand(y*d*K-d*(K*y))==0)
ck('Minkowski_inertial_drift_zero',s.expand(y*d*H0-d*He).subs({H0:0,He:0})==0)
Xa=s.Rational(3,2);pm=s.Rational(1,100);Da=s.sqrt(1+2*p*Xa);ya=Xa/Da;La=s.symbols('La',positive=True)
wrongL=(Xa-Da)/K;correctC=(ya-1)/K
ct('wrong_deSitter_anchor_strictly_larger',s.simplify(wrongL-Da*correctC)==0 and Da.subs(p,pm)>1 and ya.subs(p,pm)>1)
ck('wrong_anchor_infers_nonconstant_history',s.simplify(y*(q-K*(1-1/y))-(K+(q-K)*y))==0)
fa=Da*s.log(ya);hscale=fa/La
ck('constant_Q_anchor_family',s.simplify(s.log(ya)/hscale-La/Da)==0)
ct('one_anchor_does_not_identify_scale',s.simplify(s.diff(hscale,p)).subs(p,0)!=0)
# Actual implicit root derivative at fixed observed anchor.
ck('anchor_endpoint_p_derivative',s.simplify(s.diff(ya,p)+Xa**2/Da**3)==0)
ck('anchor_value_p_derivative',s.simplify(s.diff(La/Da,p)+La*Xa/Da**3)==0)
# Explicit Q=0 solution tests endpoint terms of the implicit differentiation formula.
J=(s.log(ya)/hscale**2);rhs=(s.diff(ya,p)/(ya*hscale)-s.diff(La/Da,p))/J
ck('implicit_sensitivity_matches_exact_family',s.simplify(s.diff(hscale,p)-rhs)==0)
ct('omitting_moving_endpoint_breaks_sensitivity',s.simplify(s.diff(hscale,p)+s.diff(La/Da,p)/J)!=0)
# Nonconstant normalized-rate curve exercises the integral Q-prime sensitivity term.
cc=s.symbols('cc',real=True);H_nonconstant=y*(q-cc/Xp)
reciprocal_p=s.simplify(s.diff(1/H_nonconstant,p).subs(p,0))
ck('nonzero_Qprime_sensitivity_term',s.simplify(reciprocal_p+cc*y/(q*y-cc)**2)==0)
ct('opposite_Qprime_sign_is_rejected',s.simplify(reciprocal_p-cc*y/(q*y-cc)**2)!=0)
# Uniform physical parameter envelope and actual inherited consumer.
Y=s.Rational(36,25);a=s.Rational(9,29)
ck('all_p_endpoint_square_bound',Xa**2>s.Rational(29,20)**2*(1+2*pm*Xa))
ck('common_consumer_domain',s.Rational(29,20)>Y)
t=s.symbols('t',positive=True);ck('log_lower_bound_derivative',s.simplify(s.diff(s.log(t)-(t-1)/t,t)-(t-1)/t**2)==0)
ck('log_lower_bound_basepoint',(s.log(t)-(t-1)/t).subs(t,1)==0)
ck('anchor_scale_lower_constant',(s.Rational(29,20)-1)/s.Rational(29,20)==a)
prior=json.loads((R/'lab/process/k2522-redshift-drift-interface.json').read_text());eta_star=s.Rational(prior['normalized_same_window_h_error_sufficient']);Rmax=a*eta_star/(Y+eta_star)
ck('actual_velocity_uniform_halfmargin',s.cancel(Y*Rmax/(a-Rmax)-eta_star)==0)
ck('positive_anchor_scale_at_tolerance',a-Rmax>0)
ck('inherited_normalized_history_envelope',eta_star<s.Rational(1,2) and Y+eta_star<2)
EQ=Rmax/2;ck('constant_measured_Q_joint_band',2*EQ==Rmax)
# Scaling all four actual weak columns uses ONE common positive scale.
h0,h=s.symbols('h0 h',positive=True);alpha,rho,c0=s.symbols('alpha rho c0');phi,ps,es=s.symbols('phi ps es')
weak=alpha*phi*h**(-s.Rational(1,2))/36-rho*phi*h**(-s.Rational(5,2))/216-c0*es*phi*h**(-s.Rational(5,2))/108+ps*h**s.Rational(3,2)
scaled=s.expand(weak.subs(h,h0*h)/h0**s.Rational(3,2));target=weak.subs({alpha:alpha/h0**2,rho:rho/h0**4,c0:c0/h0**4})
ck('all_four_weak_columns_scale_together',s.simplify(scaled-target)==0)
# Nonconstant physical shape is not removed by subtracting one common rate.
ct('shape_nuisance_not_common_mode',s.diff(X**2/X,X)!=0)
# A finite set of exact nodes cannot certify the continuum error without regularity.
nodes=[s.S(1),s.Rational(5,4),s.Rational(3,2)];bump=s.prod(X-z for z in nodes)
ct('between_node_bump_escapes_point_data',all(bump.subs(X,z)==0 for z in nodes) and bump.subs(X,s.Rational(9,8))!=0)
# Distinct physical velocity fixtures directly check source normalization and inverses.
for vv,ye in [(s.Rational(3,5),s.Rational(3,2)),(-s.Rational(3,5),s.Rational(3,2)),(s.S(0),s.S(2)),(s.Rational(5,13),s.Rational(7,5))]:
 gg=1/s.sqrt(1-vv**2);dd=gg*(1+vv);pp=gg*vv/ye;xx=ye*dd
 ck(f'physical_inverse_v{vv}_y{ye}',s.simplify(s.sqrt(1+2*pp*xx)-dd)==0 and s.simplify(xx/dd-ye)==0)
# Two-anchor identification: derivative numerator is uniformly positive.
A=s.symbols('A',positive=True);DD=s.sqrt(1+2*p*A);yb=A/DD;f=DD*s.log(yb)
ck('two_anchor_log_derivative',s.simplify(s.diff(s.log(f),p)-(yb/DD)*(1-1/s.log(yb)))==0)
ll=s.symbols('ell',real=True);SS=s.symbols('S',positive=True)
ck('two_anchor_positive_numerator_decomposition',s.expand(ll**2-ll+(d*d+1)/2-((ll-s.Rational(1,2))**2+d*d/2+s.Rational(1,4)))==0)
# Rational rapidity substitution checks h'(y) identity without sign ambiguity.
hfun=y/Dp*(1-1/s.log(y));den=Dp**2*Sp*s.log(y)**2
expected=(s.log(y)**2-s.log(y)+Dp*Sp)/den
ck('two_anchor_monotonicity_derivative',s.simplify(s.diff(hfun,y)-expected)==0)
ck('D_gamma_positive_identity',s.simplify(Dp*Sp-(Dp**2+1)/2)==0)
# Endpoint limit establishing onto range; all common scale ratios are retained.
z=s.symbols('z',positive=True);ck('lower_anchor_Dlog_limit',s.limit(z*s.log(A/z),z,0,dir='+')==0)
ck('upper_anchor_y_one_zero',s.log(1)==0)
ct('duplicate_anchors_have_no_identification',s.diff(s.log(f/f),p)==0)
refs=['explorations/conditional-build/k2520-nonlinear-observation-null-2026-11-02.md','explorations/conditional-build/k2522-redshift-drift-interface-2026-11-02.md','lab/process/k2522-redshift-drift-interface.json','explorations/conditional-build/k2524-anchored-drift-nuisance-quotient-2026-11-02.md']
report={'result':'K2526','scope':'conditional common-momentum radial geodesic test emitters; no measured error band or GU verdict','checks':checks,'contrary_controls':controls,'inherited_normalized_h_error':str(eta_star),'velocity_uniform_Q_oscillation_sufficient':str(Rmax),'velocity_uniform_Q_oscillation_decimal':str(s.N(Rmax,16)),'evidence_kinds':{'exact':'kinematics, reciprocity, Jacobians, sensitivity, weak columns and conditional tolerance','universal':'functional proof and positivity/monotonicity arguments in note','inherited':'K2522 exact same-window half-margin, dependency pinned without unrelated replay','reporting':'saved report equality and hashes'},'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in refs}}
path=R/'lab/process/k2526-geodesic-emitter-drift-repair.json'
if '--write' in sys.argv:path.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(path.read_text())==report,'saved report differs'
print(json.dumps({'checks':len(checks),'contrary_controls':len(controls),'all_pass':True,'report_written':'--write' in sys.argv}))
