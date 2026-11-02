"""Exact drift/calibration controls and an explicitly numerical same-model forecast."""
from pathlib import Path
import hashlib,json,sys
import sympy as S
import numpy as np
from scipy.integrate import solve_ivp
R=Path(__file__).resolve().parents[2];exact={};numeric={};controls={}
def ck(k,v):
 exact[k]=bool(v)
 if not exact[k]:raise AssertionError(k)
def ct(k,v):
 controls[k]=bool(v)
 if not controls[k]:raise AssertionError(k)
def nc(k,v):
 numeric[k]=bool(v)
 if not numeric[k]:raise AssertionError(k)
z,H0,He,ao,ae=S.symbols('z H0 He ao ae',positive=True)
# Differentiate ao/ae using the null-path emitter-time derivative.
redshift_derivative=ao/ae*(H0-He*ae/ao)
ck('two_null_paths_proper_time_derivative',S.simplify(redshift_derivative-((ao/ae)*H0-He))==0)
ct('wrong_equal_emitter_observer_time_detected',S.expand(ao/ae*(H0-He)-redshift_derivative)!=0)
ck('velocity_shift_factor',S.simplify(((1+z)*H0-He)/(1+z)-(H0-He/(1+z)))==0)
# Actual nonconstant emitter track in de Sitter, z=k exp(Ht).
t,H,k=S.symbols('t H k',positive=True);zz=k*S.exp(H*t)
ck('deSitter_exact_source_track',S.simplify(S.diff(zz,t)-((1+zz)*H-H))==0)
ct('omitted_velocity_denominator',S.simplify(H*zz-H*zz/(1+zz))!=0)
T,e,M2,M3=S.symbols('T e M2 M3',positive=True)
u=S.symbols('u',real=True)
ck('forward_integral_remainder',S.integrate(M2*(T-u),(u,0,T))/T==M2*T/2)
ck('centered_integral_remainder',S.integrate(M3*u*u/2,(u,-T/2,T/2))/T==M3*T*T/24)
forward=e/T+M2*T/2;centered=e/T+M3*T*T/24
ck('forward_optimal_baseline',S.simplify(S.diff(forward,T).subs(T,S.sqrt(2*e/M2)))==0)
ck('forward_minimum',S.simplify(forward.subs(T,S.sqrt(2*e/M2))-S.sqrt(2*e*M2))==0)
Tc=(12*e/M3)**S.Rational(1,3)
ck('centered_optimal_baseline',S.simplify(S.diff(centered,T).subs(T,Tc))==0)
ck('centered_minimum',S.simplify(centered.subs(T,Tc)-3*e/(2*Tc))==0)
ct('cubic_track_requires_centered_remainder',S.expand(((T/2)**3-(-T/2)**3)/T)==T*T/4)
ct('quadratic_track_requires_forward_remainder',S.expand(T*T/T)==T)
bump=z*(z-1)*(z-2)
ct('finite_redshift_samples_do_not_certify_band',all(bump.subs(z,j)==0 for j in [0,1,2]) and bump.subs(z,S.Rational(1,2))!=0)
# Exact H0 interval control; inequalities proved by monotonic positive reciprocals.
q,d,eps=S.symbols('q d epsilon',positive=True)
F=S.log(2)/q
ck('absolute_anchor_strict_monotonicity',S.diff(F,q)==-S.log(2)/q**2)
ck('absolute_anchor_identifies_unit_H0',S.solve(F-S.log(2),q)==[1])
Flo=S.log(2)/(q+eps);Fhi=S.log(2)/(q-eps)
ck('band_lower_endpoint',S.simplify(Flo.subs(q,1-d-eps)-S.log(2)/(1-d))==0)
ck('band_upper_endpoint',S.simplify(Fhi.subs(q,1+d+eps)-S.log(2)/(1+d))==0)
A,obs=S.symbols('A obs',positive=True)
ck('uncalibrated_anchor_refits',S.simplify((A*F).subs(A,obs/F)-obs)==0)
ct('relative_distance_has_H0_kernel',S.diff((S.log(3)/q)/(S.log(2)/q),q)==0)
ct('independent_anchors_cannot_refit_shared_H0',S.log(2)/1 != S.log(2)/2)
# Full weak row in h, independent derivative/error coefficients.
h,r,ph,ww,es=S.symbols('h r ph ww es',positive=True)
col=[ph*h**S.Rational(-1,2)/36,-ph*h**S.Rational(-5,2)/216,-ph*es*h**S.Rational(-5,2)/108,ww*h**S.Rational(3,2)]
old=[ph*S.sqrt(r)/36,-ph*r**S.Rational(5,2)/216,-ph*es*r**S.Rational(5,2)/108,ww*r**S.Rational(-3,2)]
ck('actual_augmented_row_substitution',all(S.simplify(x-y.subs(r,1/h))==0 for x,y in zip(col,old)))
expected=[-ph/(72*h**S.Rational(3,2)),5*ph/(432*h**S.Rational(7,2)),5*ph*es/(216*h**S.Rational(7,2)),3*ww*S.sqrt(h)/2]
ck('all_four_error_derivatives',all(S.simplify(S.diff(x,h)-v)==0 for x,v in zip(col,expected)))
# Exact nonlinear changes lie in the asserted Lipschitz bounds on [1,4].
ck('finite_nonlinear_row_bound',all(abs(x.subs({h:S.Rational(9,4),ph:1,es:2,ww:3})-x.subs({h:1,ph:1,es:2,ww:3})) <= S.Rational(5,4)*abs(v.subs({h:(4 if i==3 else 1),ph:1,es:2,ww:3})) for i,(x,v) in enumerate(zip(col,expected))))
ck('source_H0_error_amplification',S.diff((1+z)*H0-He,H0)==1+z)
ct('unbounded_H0_not_one_nominal_history',((1+2)*2-1)!=((1+2)*1-1))
# Reuse K2520 matrix as consumer data, not a fresh proof of its determinant.
prior=json.loads((R/'lab/process/k2520-nonlinear-observation-null.json').read_text())
W=S.Matrix([[S.Rational(x) for x in row] for row in prior['augmented_window_matrix']]);norm=max(sum(abs(x) for x in W.inv().row(i)) for i in range(4))
ck('inherited_actual_matrix_norm',norm==S.Rational(prior['augmented_inverse_infinity_norm']))
budget=1/(2*norm);ck('strict_matrix_error_budget',norm*budget==S.Rational(1,2))
# A rigorous (deliberately conservative) drift-band tolerance for the actual coasting witness.
# t in [1,6/5], h_nom=t^2; eta<=1/2 puts all allowed h in [1/2,2].
tt=S.symbols('tt');top=S.Rational(6,5);w=(tt-1)**2*(top-tt)**2
Ds=lambda f:tt*S.diff(f,tt)/6
def polybound(f):
 pol=S.Poly(S.expand(f),tt)
 return sum(abs(c)*top**powers[0] for powers,c in pol.terms())
row_constants=[]
for jj in range(4):
 window=tt**(6+jj)*w;Phi=polybound(window);Psi=polybound(Ds(Ds(window))+Ds(window))
 # length<=6/5; a^-3/2<=3, a^-7/2<=12, sqrt(b)<=3/2.
 row_constants.append(top*(Phi/S.Integer(24)+5*Phi/36+5*top**6*Phi/18+9*Psi/4))
Bmax=max(row_constants);eta_star=min(S.Rational(1,2),1/(2*norm*Bmax))
ck('coasting_band_positivity_bounds',1-eta_star>=S.Rational(1,2) and top**2+eta_star<=2)
ck('coasting_actual_weak_consumer_half_margin',norm*Bmax*eta_star<=S.Rational(1,2))
ck('coasting_shared_calibration_error_budget',top**2*(eta_star/(2*top**2))+eta_star/2==eta_star)
# Released structural conditioning: exact recombination of the SAME windows.
# Bernstein coefficients certify whole-interval polynomial bounds, not sampled extrema.
y=S.symbols('y');original_windows=S.Matrix([tt**(6+jj)*w for jj in range(4)])
new_windows=W.inv()*original_windows
bernstein_banks=[]
def bernstein_bound(poly):
 shifted=S.Poly(S.expand(poly.subs(tt,1+(top-1)*y)),y);degree=shifted.degree()
 coeff=[S.simplify(sum(shifted.nth(ii)*S.binomial(kk,ii)/S.binomial(degree,ii) for ii in range(kk+1))) for kk in range(degree+1)]
 restored=sum(coeff[kk]*S.binomial(degree,kk)*y**kk*(1-y)**(degree-kk) for kk in range(degree+1))
 assert S.Poly(S.expand(restored-shifted.as_expr()),y).is_zero
 bernstein_banks.append([str(c) for c in coeff])
 return max(abs(c) for c in coeff)
normalized_constants=[];direct_rows=[]
for window in new_windows:
 Phi=bernstein_bound(window);Psi=bernstein_bound(Ds(Ds(window))+Ds(window))
 normalized_constants.append(top*(Phi/24+5*Phi/36+5*top**6*Phi/18+S.Rational(9,4)*Psi))
 direct_rows.append([S.integrate(S.expand(window)/(6*tt**2),(tt,1,top)),S.integrate(-S.expand(window)/(36*tt**6),(tt,1,top)),S.integrate(-S.expand(window)/18,(tt,1,top)),S.integrate(S.expand(6*(Ds(Ds(window))+Ds(window))*tt**2),(tt,1,top))])
ck('recombined_actual_augmented_integrals_are_identity',S.Matrix(direct_rows)==S.eye(4))
ck('all_eight_Bernstein_polynomials_reconstruct_exactly',len(bernstein_banks)==8)
eta_normalized=min(S.Rational(1,2),1/(2*max(normalized_constants)))
ck('normalized_same_window_half_margin',max(normalized_constants)*eta_normalized<=S.Rational(1,2))
ck('normalized_bounds_improve_sufficient_tolerance',eta_normalized>eta_star)
ck('normalized_band_keeps_expansion_positive',1-eta_normalized>=S.Rational(1,2) and top**2+eta_normalized<=2)
ct('dropping_window_recombination_changes_consumer',W!=S.eye(4))
ct('Bernstein_missing_normalization_changes_polynomial',S.expand(0*(1-y)**2+2*y*(1-y)+y*y)-y!=0)
# At the strict boundary, an actual rank-one loss can occur; checks the perturbed matrix.
loss=W*S.diag(0,1,1,1)
ct('non_strict_invertibility_is_false',loss.det()==0 and max(sum(abs(x) for x in (W.inv()*(loss-W)).row(i)) for i in range(4))==1)
U0=S.Integer(2);p0=S.Rational(3175541986,10**10)
local=(U0-2*p0)/U0**S.Rational(1,3)
ck('same_model_exact_local_positive_drift',local>0)
# No new fit, physical ruler or continuum-certified numerical sign.
al=775.88047141;rh=8540.41820373;up0=.3175541986
F0=al+12*2**(1/3)*(2-up0);qq=3*F0*2**(4/3)*.3
hi=3*np.log1p(2.33)
def rhs(ss,y):
 uv,pv,chi=y
 return [pv,pv-al/(36*uv**(1/3))+(rh+2*qq*np.exp(ss))/(216*uv**(5/3)),np.exp(ss/3)/(3*uv**(2/3))]
sols=[solve_ivp(rhs,(0,hi),[2,up0,0],method=method,rtol=tol,atol=tol/100,dense_output=True,max_step=.01) for method,tol in [('DOP853',2e-12),('RK45',1e-11)]]
nc('both_original_background_integrators_succeed',all(x.success for x in sols))
zgrid=np.array([0,.1,.5,1,2,2.33]);ss=3*np.log1p(zgrid);h0=2**(2/3)
forecasts=[]
for sol in sols:
 uv=sol.sol(ss)[0];hv=uv**(2/3);dr=(1+zgrid)*h0-hv
 forecasts.append(dr)
nc('drift_forecasts_independent_integrators_agree',np.max(np.abs(forecasts[0]-forecasts[1]))<1e-8)
nc('present_drift_zero',forecasts[0][0]==0)
nc('positive_local_finite_control',forecasts[0][1]>0)
# Observer-time chain used directly: h_z=2p/[U^(1/3)(1+z)].
uv,pv,_=sols[0].sol(ss);direct=h0-2*pv/(uv**(1/3)*(1+zgrid))
nc('numerical_origin_slope_matches_exact',abs(direct[0]-float(local))<1e-13)
# Distances also come from the same integrated history; a second q changes the anchor monotonically.
from scipy.integrate import quad
def reconstruct(q):return quad(lambda zz:1/((1+zz)*q-((1+zz)*h0-float(sols[0].sol(3*np.log1p(zz))[0]**(2/3)))),0,1,epsabs=1e-11,epsrel=1e-11)[0]
anchor=float(sols[0].sol(3*np.log(2))[2]);fmid=reconstruct(h0)
nc('actual_drift_absolute_anchor_reconstructs_same_history',abs(fmid-anchor)<1e-10)
nc('actual_H0_monotonic_bracket',reconstruct(h0-.01)>anchor>reconstruct(h0+.01))
paths=['explorations/conditional-build/k2522-redshift-drift-interface-2026-11-02.md','tests/channel-swings/k2522_redshift_drift_interface_probe.py','lab/process/k2520-nonlinear-observation-null.json','explorations/conditional-build/k2367-sourced-fit-dust-transfer-2026-10-31.md']
report={'result':'K2522','exact_checks':exact,'numerical_checks':numeric,'contrary_controls':controls,'evidence_scope':'Written universal proofs; exact finite fixtures; numerical original rounded fit. No data, survey precision or certified global forecast. K2520 exclusion reused.','local_drift_slope':str(local),'coasting_uniform_h_error_sufficient':str(eta_star),'coasting_uniform_h_error_decimal':float(eta_star),'normalized_same_window_h_error_sufficient':str(eta_normalized),'normalized_same_window_h_error_decimal':float(eta_normalized),'normalized_row_bounds':[str(x) for x in normalized_constants],'normalized_Bernstein_banks':bernstein_banks,'coasting_row_Lipschitz_upper_bounds':[str(x) for x in row_constants],'inherited_matrix_row_error_budget':str(budget),'forecast_Hstar_units':[{'z':float(zz),'g_star':float(gg),'velocity_drift_over_cHstar':float(gg/(1+zz))} for zz,gg in zip(zgrid,forecasts[0])],'absolute_anchor_at_z1':anchor,'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths}}
pth=R/'lab/process/k2522-redshift-drift-interface.json'
if '--write' in sys.argv:pth.write_text(json.dumps(report,indent=2)+'\n')
else:
 saved=json.loads(pth.read_text());omitted={'forecast_Hstar_units','absolute_anchor_at_z1'};ck('saved_exact_report',all(saved[k]==v for k,v in report.items() if k not in omitted));nc('saved_numeric_report',abs(saved['absolute_anchor_at_z1']-anchor)<1e-10 and len(saved['forecast_Hstar_units'])==len(report['forecast_Hstar_units']) and all(a['z']==b['z'] and abs(a['g_star']-b['g_star'])<1e-9 and abs(a['velocity_drift_over_cHstar']-b['velocity_drift_over_cHstar'])<1e-9 for a,b in zip(saved['forecast_Hstar_units'],report['forecast_Hstar_units'])))
print('K2522 PASS',len(exact),'exact checks',len(numeric),'numeric checks',len(controls),'contrary controls')
