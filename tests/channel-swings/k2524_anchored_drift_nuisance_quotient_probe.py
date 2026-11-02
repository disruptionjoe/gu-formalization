"""Exact instrument/anchor identities and contrary constructions; no survey data."""
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
z,t,p,g,b0,b1=s.symbols('z t p g b0 b1',real=True);x=1+z
l1,l2,K=s.symbols('l1 l2 K',positive=True);A=s.Function('A')(t);B=s.Function('B')(t);X=s.Function('X')(t)
rate=s.diff(A*l1*X+B,t).subs({s.diff(A,t):b1,s.diff(B,t):b0,s.diff(X,t):g,A:1,X:x})/l1
ck('differentiated_affine_wavelength_map',s.simplify(rate-g-b1*x-b0/l1)==0)
m1=g+b1*x+b0/l1;m2=g+b1*x+b0/l2
G=s.cancel((l1*m1-l2*m2)/(l1-l2));ck('two_line_offset_removal',s.expand(G-g-b1*x)==0)
ck('nonlinear_anchor_equivariance',s.expand(x*(p+b1)-(g+b1*x)-(x*p-g))==0)
ck('physical_H0_from_effective_parameter',s.expand((p+b1)-(g+b1*x)).subs(z,0)==p-g)
ct('positive_effective_parameter_not_required',s.simplify(x*0-(-K))==K)
ct('one_line_offset_not_anchor_null',s.diff((b0/l1)/x,z)!=0)
# Exact full-history witness on inherited interval, and action membership.
a=s.Rational(11,25);C=s.log(1+a);Kv=a/C
ck('positive_counterfamily_scale',Kv>0)
ck('coasting_exact_anchor',s.integrate(1/x,(z,0,a))==C)
ck('deSitter_same_anchor',s.simplify(a/Kv-C)==0)
gd=K*z
ck('one_line_deSitter_mimics_zero_drift',s.expand(gd-K*x+K*l1/l1)==0)
Gd=s.simplify(G.subs({g:gd,b1:-K,b0:K*l1}));ck('two_lines_recover_shifted_drift',Gd==-K)
ck('zero_effective_root_recovers_positive_history',s.simplify(x*0-Gd)==K)
alpha=s.symbols('alpha',real=True);U=K**s.Rational(3,2)
ck('deSitter_vacuum_action_equation',s.simplify(alpha/(36*U**s.Rational(1,3))-6*alpha*K**2/(216*U**s.Rational(5,3)))==0)
RR=12*K**2;FF=alpha+RR;fval=alpha*RR+RR**2/2-6*alpha*K**2
ck('full_vacuum_trace_equation',s.expand(FF*RR-2*fval)==0)
ck('full_vacuum_Friedmann_equation',s.expand(3*FF*K*K-(FF*RR-fval)/2)==0)
ct('positive_dust_breaks_same_deSitter_solution',s.exp(t)/(108*U**s.Rational(5,3))!=0)
z0=s.symbols('z0',positive=True);xt=1+z0*s.exp(K*t);calA=s.exp(-K*t);calB=l1*(1-calA)
ck('exact_finite_time_one_line_counterfamily',s.simplify(calA*l1*xt+calB-l1*(1+z0))==0)
ck('correct_reference_calibration',calA.subs(t,0)==1 and calB.subs(t,0)==0)
ck('reference_rate_matches_counterfamily',s.diff(calA,t).subs(t,0)==-K and s.diff(calB,t).subs(t,0)==K*l1)
ct('second_line_exposes_offset',s.simplify(s.diff(calA*l2*xt+calB,t).subs(t,0))==K*(l1-l2))
# A second exact anchor at b with 1+b=sqrt(1+a) is explicitly unequal.
b=s.Rational(1,5)
ck('second_anchor_pair_separation',s.simplify(s.expand_log(s.log(1+b)-b*C/a-s.Rational(1,11)*s.log(s.Rational(6,5)),force=True))==0)
# Joint line noise and the exact constrained least-squares design.
w=s.Matrix([[-1,2]]);ck('affine_equal_noise_cost',(w*w.T)[0]==5)
ck('common_rate_noise_cost',(w*s.ones(2)*w.T)[0]==1)
ct('ignoring_line_covariance_changes_cost',(w*s.ones(2)*w.T)[0]!=(w*w.T)[0])
ls=[s.Integer(1),s.Integer(2),s.Integer(3)];D=s.Matrix([[1,1/l] for l in ls]);S=s.Matrix([[2,1,0],[1,3,1],[0,1,2]]);c=s.Matrix([1,0]);M=D.T*S.inv()*D;wg=S.inv()*D*M.inv()*c
ck('GLS_physical_constraints',D.T*wg==c)
ck('GLS_positive_covariance',S.is_positive_definite is True)
ck('GLS_variance_identity',s.simplify((wg.T*S*wg)[0]-(c.T*M.inv()*c)[0])==0)
v=D.T.nullspace()[0];q=s.symbols('q',real=True)
ck('GLS_all_feasible_perturbations_increase_cost',s.expand(((wg+q*v).T*S*(wg+q*v))[0]-(wg.T*S*wg)[0]-q*q*(v.T*S*v)[0])==0 and (v.T*S*v)[0]>0)
ct('duplicate_lines_cannot_remove_offset',s.Matrix([[1,1],[1,1]]).rank()==1)
# Exact subtraction of reciprocal histories gives finite-error formula pointwise.
h,hh,e,dp,xx=s.symbols('h hh e dp xx',nonzero=True,real=True)
ck('finite_anchor_reciprocal_identity',s.cancel(1/(h+xx*dp-e)-1/h-(e-xx*dp)/(h*(h+xx*dp-e)))==0)
# Exact quadrature analogue tests SAME realization, never asserts continuum quadrature accuracy.
xs=s.Matrix([1,s.Rational(6,5),s.Rational(36,25)]);hs=xs;es=s.Matrix([s.Rational(1,20),-s.Rational(1,30),s.Rational(1,40)]);delta=s.Rational(1,25);hhs=hs+xs*delta-es;omega=[s.Rational(1,7),s.Rational(2,7),s.Rational(4,7)]
Js=sum(omega[i]*xs[i]/(hs[i]*hhs[i]) for i in range(3));cs=sum(omega[i]*(1/hhs[i]-1/hs[i]) for i in range(3));mean=sum(omega[i]*es[i]/(hs[i]*hhs[i]) for i in range(3))/Js
ck('finite_shared_anchor_identity',s.simplify(delta-mean+cs/Js)==0)
rs=[es[i]/xs[i] for i in range(3)];osc=max(rs)-min(rs)
ck('finite_oscillation_bound',all(abs(hhs[i]-hs[i])<=xs[i]*(osc+abs(cs)/Js) for i in range(3)))
common=s.Rational(7,3);shifted=es+common*xs
ck('finite_shape_oscillation_common_mode_invariant',max(shifted[i]/xs[i] for i in range(3))-min(shifted[i]/xs[i] for i in range(3))==osc)
J0=sum(omega[i]*xs[i]/hs[i]**2 for i in range(3));av=s.Matrix([omega[i]/hs[i]**2/J0 for i in range(3)]);P=xs*av.T-s.eye(3);T=P.row_join(-xs/J0)
ck('actual_anchor_linear_map_annihilates_common_mode',P*xs==s.zeros(3,1))
ck('anchor_projection_idempotent_with_sign',P*P==-P)
Sig=s.eye(4);Sig[0,3]=Sig[3,0]=s.Rational(1,3)
Cjoint=T*Sig*T.T;ck('joint_anchor_covariance_symmetric',Cjoint==Cjoint.T and Sig.is_positive_definite is True)
ct('dropping_anchor_cross_covariance_changes_result',Cjoint!=T*T.T)
ct('redshift_shape_survives_projection',P*s.ones(3,1)!=s.zeros(3,1))
# Sufficient consumer inherited by exact rational value; no old bank replay.
prior=json.loads((R/'lab/process/k2522-redshift-drift-interface.json').read_text())
# Report key read explicitly; equality bound is already a strict half-margin there.
eta=s.Rational(prior['normalized_same_window_h_error_sufficient'])
xmax=s.Rational(36,25);Jmin=(xmax**2-1)/8;shape=eta/(2*xmax);anchor=Jmin*eta/(2*xmax)
ck('actual_weak_consumer_allocation',xmax*(shape+anchor/Jmin)==eta)
ck('anchor_J_lower_bound_integral',s.integrate(x/4,(z,0,a))==Jmin)
# Polynomial distortion recovery and sharp pointwise line count.
ll=s.symbols('ll');banks={}
for degree in [1,2,3,4]:
 wavelengths=list(map(s.Integer,range(1,degree+2)));weights=[]
 for li in wavelengths:
  Li=s.prod((ll-lj)/(li-lj) for lj in wavelengths if lj!=li);weights.append(s.simplify(li*s.diff(Li,ll).subs(ll,0)))
 ck('degree_'+str(degree)+'_all_distortion_moments',all(sum(wi*li**(rr-1) for wi,li in zip(weights,wavelengths))==(1 if rr==1 else 0) for rr in range(degree+1)))
 banks[str(degree)]={'weights':list(map(str,weights)),'independent_equal_noise_multiplier':str(sum(wi**2 for wi in weights))}
 for n in range(1,degree+1):
  pol=s.prod(ll-j for j in range(1,n+1));ck(f'degree_{degree}_missing_line_{n}_counterpolynomial',all(pol.subs(ll,j)==0 for j in range(1,n+1)) and s.diff(pol,ll).subs(ll,0)!=0)
ck('quadratic_three_line_weights',banks['2']['weights']==['-5/2','8','-9/2'])
ck('quadratic_three_line_noise_cost',s.Rational(banks['2']['independent_equal_noise_multiplier'])==s.Rational(181,2))
a2=s.symbols('a2');res=s.cancel((l1*(a2*x*x*l1)-l2*(a2*x*x*l2))/(l1-l2))
ct('quadratic_error_survives_two_line_repair',s.expand(res-a2*x*x*(l1+l2))==0 and s.diff(res/x,z)!=0)
ct('wrong_affine_weight_does_not_cancel_offset',s.simplify((m1+m2)/2-g-b1*x)!=0)
ct('common_acceleration_is_not_offset_calibration',sum([-1,2])==1)
ck('polynomial_remainder_triangle_fixture',abs(-s.Rational(5,2)*s.Rational(1,10)+8*s.Rational(1,20)/2-s.Rational(9,2)*s.Rational(1,30)/3)<=s.Rational(5,2)/10+8/s.Integer(40)+s.Rational(9,2)/90)
st='k2524-anchored-drift-nuisance-quotient';deps=[f'explorations/conditional-build/{st}-2026-11-02.md',str(Path(__file__).relative_to(R)),'lab/process/k2522-redshift-drift-interface.json','explorations/conditional-build/k2520-nonlinear-observation-null-2026-11-02.md']
out={'result_id':'K2524','checks':checks,'contrary_controls':controls,'evidence_kind':'universal instrument, interpolation, convex-hull and variational proofs in note; exact finite identities and same-realization quadrature controls; report checks do not certify surveys or continuum quadrature','polynomial_line_designs':banks,'consumer':{'inherited_eta':str(eta),'Jmin':str(Jmin),'shape_allocation':str(shape),'absolute_anchor_allocation':str(anchor)},'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps}}
f=R/f'lab/process/{st}.json'
if '--write' in sys.argv:f.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
else:assert json.loads(f.read_text())==out
print(json.dumps({'result':'K2524','exact_checks':len(checks),'contrary_controls':len(controls)}))
