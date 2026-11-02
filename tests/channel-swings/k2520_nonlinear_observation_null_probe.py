"""K2520 exact nonlinear identities, rational action discriminator and numerical witness."""
from pathlib import Path
import hashlib,json,sys,itertools
import sympy as S
import numpy as np
from scipy.integrate import solve_ivp
from numpy.polynomial.legendre import leggauss
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not checks[k]:raise AssertionError(k)
def ct(k,v):
 controls[k]=bool(v)
 if not controls[k]:raise AssertionError(k)
z,s,t=S.symbols('z s t',real=True);a,b,A,B,n=S.symbols('a b A B n',positive=True)
chi=S.log(1+z);N=n*chi**2*S.diff(chi,z)
ck('exact_current_cube_primitive',S.simplify(S.diff(n*chi**3/3,z)-N)==0)
x,y,u,v=S.symbols('x y u v');beta=B*n/(3*A**3)
d1=A**3*(y**3-x**3);d2=A**3*(v**3-u**3)
c1=B*n*(y**3-x**3)/3;c2=B*n*(v**3-u**3)/3
ck('finite_shell_calibrated_cross_product',S.expand(c1*d2-c2*d1)==0)
ck('shared_amplitudes',S.simplify(c1-beta*d1)==0)
ct('independent_shell_selection_breaks',S.expand(2*c1*d2-c2*d1)!=0)
ct('cube_of_mean_is_not_mean_cube',S.Rational(1,2)*(1**3+3**3)!=S.Rational(1,2)**3*(1+3)**3)
D,d=S.symbols('D d',positive=True)
ck('nonlinear_cube_error',S.expand((D+d)**3-D**3-(3*D**2*d+3*D*d*d+d**3))==0)
C,E,dc,de=S.symbols('C E dc de')
ck('bilinear_error_terms',S.expand((C+dc)*(E+de)-C*E-(C*de+E*dc+dc*de))==0)
U=S.Function('U')(s);phi=S.Function('phi')(s)
boundary=phi*S.diff(U,s)-S.diff(phi,s)*U-phi*U
ck('weak_integration_by_parts',S.simplify(phi*(S.diff(U,s,2)-S.diff(U,s))-U*(S.diff(phi,s,2)+S.diff(phi,s))-S.diff(boundary,s))==0)
alpha,rho,q,r=S.symbols('alpha rho q r',positive=True)
ck('slope_to_U',S.simplify((r**S.Rational(-3,2))**S.Rational(-1,3)-S.sqrt(r))==0)
ck('slope_to_source',S.simplify((r**S.Rational(-3,2))**S.Rational(-5,3)-r**S.Rational(5,2))==0)
w,f=S.symbols('w f');expr=w*r**S.Rational(-3,2)+alpha*f*S.sqrt(r)/36-(rho+2*q*S.exp(s))*f*r**S.Rational(5,2)/216
cal=S.simplify(expr.subs(r,r/A)/A**S.Rational(3,2)-expr.subs({alpha:alpha/A**2,rho:rho/A**4,q:q/A**4},simultaneous=True))
ck('shared_distance_calibration',cal==0)
ck('fixed_action_scale_invariant',S.simplify((rho/A**4)/(alpha/A**2)**2-rho/alpha**2)==0)
ck('L_derivative_for_band',S.diff(r**S.Rational(-3,2),r)==-S.Rational(3,2)*r**S.Rational(-5,2))
ck('C_derivative_for_band',S.diff(S.sqrt(r)/36,r)==1/(72*S.sqrt(r)))
ck('source_derivative_for_band',S.diff(r**S.Rational(5,2)/216,r)==S.Rational(5,432)*r**S.Rational(3,2))
# Exact continuum counterhistory, direct strong residual and independent weak moment matrix.
Ut=S.exp(s/2);res=S.diff(Ut,s,2)-S.diff(Ut,s)+alpha/(36*Ut**S.Rational(1,3))-(rho+2*q*S.exp(s))/(216*Ut**S.Rational(5,3))
ck('log_history_strong_residual',S.simplify(res+S.exp(s/2)/4-alpha*S.exp(-s/6)/36+rho*S.exp(-5*s/6)/216+q*S.exp(s/6)/108)==0)
ww=(t-1)**2*(S.Rational(6,5)-t)**2
Ds=lambda h:t*S.diff(h,t)/6
M=S.Matrix([[S.integrate(ww*t**(j+k),(t,1,S.Rational(6,5))) for k in (0,4,6,8)] for j in range(4)])
det=M.det();expected=S.Rational(12587308921,53806725372851360589265823364257812500000000)
ck('exact_four_window_determinant',det==expected)
ck('every_three_row_subset_can_fit',all(M.extract(rows,[0,1,2]).det()!=0 for rows in itertools.combinations(range(4),3)))
for j in range(4):
 ph=t**(6+j)*ww
 ck(f'window_{j}_boundary',all(S.simplify(g.subs(t,h))==0 for g in (ph,Ds(ph)) for h in (1,S.Rational(6,5))))
 L=S.integrate((Ds(Ds(ph))+Ds(ph))*t**3*6/t,(t,1,S.Rational(6,5)))
 ck(f'window_{j}_direct_weak_L',S.simplify(L+S.Rational(3,2)*M[j,3])==0)
 ck(f'window_{j}_source_columns',all(S.simplify(S.integrate(ph*t**k*6/t,(t,1,S.Rational(6,5)))-6*M[j,l])==0 for k,l in [(-1,1),(-5,0),(1,2)]))
ct('missing_source_exponential_changes_column',M[:,0]!=M[:,2])
ct('fourth_rejects_three_row_fit',S.simplify((M[3,:3]*M[:3,:3].inv()*M[:3,3])[0]-M[3,3])!=0)
ph=s;uu=S.exp(2*s);bb=ph*S.diff(uu,s)-S.diff(ph,s)*uu-ph*uu
ct('dropping_endpoint_term_fails',S.simplify(bb.subs(s,1)-bb.subs(s,0))!=0)
# Exact conditioning for augmented moment witness; entrywise perturbation epsilon gives ||dM||inf<=4epsilon.
invnorm=max(sum(abs(x) for x in M.inv().row(i)) for i in range(4));eps=1/(8*invnorm)
ck('robust_rank_sufficient_half_margin',4*invnorm*eps==S.Rational(1,2))
H=6*M[:,[1,0,2,3]]*S.diag(S.Rational(1,36),-S.Rational(1,216),-S.Rational(1,108),-S.Rational(1,4))
hnorm=max(sum(abs(x) for x in H.inv().row(i)) for i in range(4));heps=1/(8*hnorm)
ck('actual_augmented_matrix_invertible',H.det()!=0)
ck('actual_augmented_half_margin',4*hnorm*heps==S.Rational(1,2))
ct('rank_one_update_at_boundary_singular',(S.eye(4)-S.diag(1,0,0,0)).det()==0)
# Finite distance points do not supply a slope band: zero-node polynomial with nonzero derivative.
bump=(z-S.Rational(1,10))*(z-S.Rational(2,10))
ct('point_samples_do_not_control_slope',bump.subs(z,S.Rational(1,10))==0 and bump.subs(z,S.Rational(2,10))==0 and S.diff(bump,z).subs(z,S.Rational(1,10))!=0)
# Original rounded fitted member, independent U integration; numerical evidence only.
al=775.88047141;rh=8540.41820373;U0=2.;p0=.3175541986;F0=al+12*U0**(1/3)*(U0-p0);qq=3*F0*U0**(4/3)*.3
hi=3*np.log1p(.22)
def rhs(ss,y):
 uv,pv=y;return [pv,pv-al/(36*uv**(1/3))+(rh+2*qq*np.exp(ss))/(216*uv**(5/3))]
sol=solve_ivp(rhs,(0,hi),[U0,p0],method='DOP853',rtol=2e-12,atol=2e-14,dense_output=True,max_step=.01)
ck('fitted_member_integrates',sol.success)
ph=s*s*(S.Float(hi)-s)**2
funcs=[S.lambdify(s,g,'numpy') for g in [ph,S.diff(ph,s,2)+S.diff(ph,s)]]
def weak(nnodes):
 nodes,weights=leggauss(nnodes);ss=(nodes+1)*hi/2;uv=sol.sol(ss)[0];pp=funcs[0](ss);wv=funcs[1](ss)
 return float(np.dot(weights,(wv*uv+al*pp/(36*uv**(1/3))-(rh+2*qq*np.exp(ss))*pp/(216*uv**(5/3))))*hi/2)
v48=weak(48);v96=weak(96)
ck('fitted_member_weak_residual_numeric',abs(v96)<1e-10)
ck('quadrature_agrees_numeric',abs(v48-v96)<1e-11)
paths=['explorations/conditional-build/k2520-nonlinear-observation-null-2026-11-02.md','tests/channel-swings/k2520_nonlinear_observation_null_probe.py','explorations/conditional-build/k2518-lightcone-count-access-2026-11-02.md','explorations/conditional-build/k2367-sourced-fit-dust-transfer-2026-10-31.md','explorations/conditional-build/k2266-windowed-cosmology-test-2026-10-29.md']
report={'result':'K2520','exact_checks':{k:v for k,v in checks.items() if k not in ['fitted_member_integrates','fitted_member_weak_residual_numeric','quadrature_agrees_numeric']},'numerical_checks':{k:v for k,v in checks.items() if k in ['fitted_member_integrates','fitted_member_weak_residual_numeric','quadrature_agrees_numeric']},'contrary_controls':controls,'moment_matrix':[[str(x) for x in M.row(i)] for i in range(4)],'determinant':str(det),'inverse_infinity_norm':str(invnorm),'conservative_entrywise_error':str(eps),'augmented_window_matrix':[[str(x) for x in H.row(i)] for i in range(4)],'augmented_inverse_infinity_norm':str(hnorm),'augmented_conservative_entrywise_error':str(heps),'numeric_residual':v96,'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths}}
pth=R/'lab/process/k2520-nonlinear-observation-null.json'
if '--write' in sys.argv:pth.write_text(json.dumps(report,indent=2)+'\n')
else:
 saved=json.loads(pth.read_text());ck('saved_exact_report',all(saved[k]==v for k,v in report.items() if k!='numeric_residual'));ck('saved_numeric_report',abs(saved['numeric_residual']-v96)<1e-10)
print('K2520 PASS',len(checks),'checks',len(controls),'controls; numerical residual',v96)
