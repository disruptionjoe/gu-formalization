#!/usr/bin/env python3
"""K2607 exact source-jet algebra and independent inverse-problem controls.
Universal distribution/spectral arguments are in the note; fixtures are labeled.
"""
import argparse,json,hashlib
from pathlib import Path
import sympy as s
root=Path(__file__).resolve().parents[2]
ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
checks=[];controls=[]
def ck(name,value):
    assert bool(value),'FAIL '+name
    checks.append(name)
def ct(name,value):
    assert bool(value),'FAIL contrary '+name
    controls.append(name)
prior=json.loads((root/'lab/process/k2605-source-disjoint-pressure-response.json').read_text())
X,k=s.symbols('X k',real=True,nonzero=True)
r4=s.sympify(prior['remainder_Y4_k1'],locals={'X':X})
positive=s.Rational(8236440909844467455,19845028500669825024)
ck('actual_remainder_affine_positive_root',s.degree(r4,X)==1 and r4.subs(X,positive)==0 and positive>0)
ck('actual_nonzero_principal_slope',s.diff(r4,X)!=0)
ck('kappa_scaled_root',s.cancel((k**-3*r4.subs(X,X/k**2)).subs(X,positive*k*k))==0)
# Exact indefinite normal polynomial, representative monomial injection and jet orders.
u,v=s.symbols('u v');q=u*u-v*v
jet=3*u-2*v
ck('first_jet_remainder_order',s.Poly(q**4*jet,u,v).total_degree()==9)
ck('first_jet_full_forcing_order',s.Poly(q**5*jet,u,v).total_degree()==11)
ck('nonzero_supported_residual_minimum_order',s.Poly(q**5,u,v).total_degree()==10>9)
ct('second_jet_breaks_strict_order_gap',s.Poly(q**4*u*u,u,v).total_degree()==10)
ct('null_covector_not_zero_polynomial',q.subs(u,v)==0 and not s.Poly(q,u,v).is_zero)
# Actual remainder supports no negative-spectrum compact radial eigenfunction.
x=s.symbols('x',real=True);t=(1-x*x)**2
lhs=s.integrate(t*(s.diff(t,x,2)-positive*t),(x,-1,1));rhs=-s.integrate(s.diff(t,x)**2+positive*t*t,(x,-1,1))
ck('independent_radial_energy_fixture',lhs==rhs and rhs<0)
C=s.Function('C')(x);P=C**-7;A=-3*P/4
ck('actual_tracezero_pressure_ode',s.simplify(s.diff(P,x)+4*s.diff(C,x)/C*(P-A))==0)
ct('outer_zero_collar_essential',4*A+3*P==0 and P.subs(C,1)==1)
# Independent tenth-order Green kernel fixture in one normal coordinate.
z=s.symbols('z',positive=True);G=z**9/(2*s.factorial(9))
ck('tenth_order_kernel_ninth_jump',2*s.diff(G,z,9)==1)
ck('eighth_derivative_absolute_value_fixture',s.diff(G,z,8)==z/2)
ck('ninth_derivative_step_fixture',s.diff(G,z,9)==s.Rational(1,2))
# In distributions, second source derivative of |x-t|/2 is delta_t, not zero.
ct('classical_off_diagonal_derivative_drops_delta',s.diff(z/2,z,2)==0 and 2*s.diff(z/2,z)==1)
ck('angular_C2_sobolev_margin',6>2+6/2)
ck('conservative_second_derivative_ceiling',1+25+4+8+26==64)
ck('conservative_radial_loss',25+80+30==135)
# A fully explicit nonlinear finite observation fixture, NOT the curved receiver.
y=s.symbols('y',real=True);F=s.Matrix([2*x+x*x,3*y]);J=F.jacobian([x,y]);J0=J.subs({x:0,y:0})
ck('nonlinear_fixture_invertible_reference',J0.det()==6)
ck('safe_ball_derivative_margin',J.subs(x,-s.Rational(1,4))[0,0]==s.Rational(3,2)>1)
u0,v0=s.symbols('u0 v0',real=True)
ck('fixed_J_segment_identity',s.factor((2*x+x*x)-(2*u0+u0*u0))==(x-u0)*(x+u0+2))
H=s.Matrix([s.exp(x)*s.cos(y),s.exp(x)*s.sin(y)])
ct('pointwise_invertibility_not_global_injectivity',s.simplify(H.jacobian([x,y]).det()-s.exp(2*x))==0 and H.subs({x:0,y:0})==H.subs({x:0,y:2*s.pi}))
# Noise accounting: fit residual and true noise may point in opposite directions.
d=s.Rational(1,100);true=s.Rational(0);data=d;fit=2*d
ck('least_squares_two_errors',abs(data-true)==d and abs(fit-data)==d and abs(fit-true)==2*d)
ct('one_error_bound_for_feasible_fit_false',abs(fit-true)>d)
# Exact moving-source moment fixture shows zero amplitude and collision degeneracies.
a1,a2,b1,b2=s.symbols('a1 a2 b1 b2',real=True)
mom=s.Matrix([a1*b1**i+a2*b2**i for i in range(4)])
JM=mom.jacobian([a1,a2,b1,b2]);det=s.factor(JM.det())
ck('moment_fixture_full_local_dimension',det==-a1*a2*(b1-b2)**4)
ct('zero_amplitude_unobservable_position',JM[:,2].subs(a1,0)==s.zeros(4,1))
ct('coincident_sources_lose_amplitude_difference',JM[:,0].subs(b1,b2)==JM[:,1])
ct('label_permutation_ambiguity',mom.xreplace({a1:a2,a2:a1,b1:b2,b2:b1})==mom)
ck('smoothed_moving_atom_derivative_identity',s.diff((x+s.Symbol('eps')*y)**2,x)==2*(x+s.Symbol('eps')*y))
# Explicit nonzero direction killed by fewer than N scalar channels.
short=JM[:3,:];null=short.subs({a1:1,a2:2,b1:0,b2:1}).nullspace()[0]
ct('insufficient_receiver_rank',null!=s.zeros(4,1) and short.subs({a1:1,a2:2,b1:0,b2:1})*null==s.zeros(3,1))
h=s.symbols('h',positive=True)
ck('jump_L2_continuity_fixture',s.integrate(s.Integer(1),(x,0,h))==h)
ct('moving_jump_not_Linfinity_continuous',abs(-s.Rational(1,2)-s.Rational(1,2))==1)
ct('injectivity_does_not_imply_lipschitz_inverse',s.diff(x**3,x).subs(x,0)==0 and (x**3).subs(x,1)!=(x**3).subs(x,0))
vv=s.symbols('vv',real=True)
ck('actual_linear_source_symmetric_split_fixture',s.expand((x+vv)**2+(x-vv)**2-2*x*x)==2*vv*vv)
ck('two_separated_pair_quadratic_difference',s.expand((x+vv)**2+(x-vv)**2-(x+vv/2)**2-(x-vv/2)**2)==3*vv*vv/2)
report={'result':'K2607','checks':checks,'contrary_controls':controls,'source_derivative_scope':'monopoles and first positional derivatives only; arbitrary higher multipoles open','local_dimension':'N=m(n+7), m separated nonzero nodes, n independent compact radial profiles','preparation':'C2 point response in local H^-64 with smooth radial input, fixed K2594 preparation','local_condition':'sigma_min(J0)>0; L*rho<=sigma/2; inverse Lipschitz<=2/sigma','smoothing_condition':'L*rho<=sigma/4; C1*epsilon<=sigma/4; source-detector distance retained','noise':'exact inverse <=2delta/sigma; feasible fit <=4delta/sigma; atomic calibration adds 2C0epsilon/sigma','evidence_kind':'pinned actual cofactor coefficient; exact normal polynomial, radial/Green and independent nonlinear moment fixtures; universal jet/spectral/local inverse proof in note','ceiling':'existence and conditional local stability, no computed curved receiver matrix, physical detector, global finite array, source-count inference or uniform collision conditioning'}
refs=['explorations/conditional-build/k2605-source-disjoint-pressure-response-2026-11-06.md','lab/process/k2605-source-disjoint-pressure-response.json','explorations/conditional-build/k2594-reciprocal-distributional-response-2026-11-06.md']
report['provenance']={f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in refs}
out=root/'lab/process/k2607-local-pressure-source-recovery.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'FAIL report replay'
print(json.dumps({'result':'K2607','checks':len(checks),'controls':len(controls),'status':'pass'}))
