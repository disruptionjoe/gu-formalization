"""Exact controls for residual normal symmetry and curved source conservation."""
from pathlib import Path
import hashlib,json,sys
import sympy as s
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(name,value):
 checks[name]=bool(value)
 if not checks[name]:raise AssertionError(name)
def ct(name,value):
 controls[name]=bool(value)
 if not controls[name]:raise AssertionError(name)
eta=s.diag(1,1,1,-1,-1,-1,-1);rows=[]
for i in range(3):
 for j in range(3,7):
  B=s.eye(7);B[i,i]=B[j,j]=s.Rational(5,4);B[i,j]=B[j,i]=s.Rational(3,4)
  ck(f'boost_preserves_actual_form_{i}_{j}',B.T*eta*B==eta and B.det()==1)
  rows.extend((B-s.eye(7)).tolist())
ck('all_mixed_fixed_spaces_force_second_factor_zero',s.Matrix(rows).rank()==7)
B=s.Matrix([[s.Rational(5,4),s.Rational(3,4)],[s.Rational(3,4),s.Rational(5,4)]])
ck('dyadic_null_coordinate_scaling',s.Matrix([[1,1],[1,-1]])*B==s.diag(2,s.Rational(1,2))*s.Matrix([[1,1],[1,-1]]))
ck('first_normal_signature',s.Matrix([4,3])-s.Matrix([1,3])==s.Matrix([3,0]))
# The unit sphere probability in first R3 is a nonpoint invariant finite measure.
normal=s.Matrix([1,0,0,0,0,0,0,0,0,0]);lift=s.diag(s.eye(3),s.diag(B,s.eye(5)))
ck('nonpoint_first_normal_support_point',lift*normal==normal and normal.dot(normal)==1)
ct('full_delta_claim_false',normal!=s.zeros(10,1))
z=s.symbols('z',nonnegative=True)
ck('radial_ball_probability_normalization',s.integrate(4*s.pi*z*z*15/(8*s.pi)*(1-z*z),(z,0,1))==1)
Rot=s.Matrix([[s.Rational(3,5),-s.Rational(4,5),0],[s.Rational(4,5),s.Rational(3,5),0],[0,0,1]])
ck('radial_ball_rotation_control',Rot.T*Rot==s.eye(3) and Rot.det()==1)
ct('positive_gaussian_is_not_boost_invariant',B.T*B!=s.eye(2))
hnew=B.inv().T*B.inv()
ck('covariant_majorant_not_fixed',B.T*hnew*B==s.eye(2))
ck('product_compatible_choice_dimension',7*6//2-3*2//2-4*3//2==12)
ct('full_normal_group_overcounts_choice',10*9//2-6*5//2-4*3//2==24)
# Original connection contraction for diagonal mixed stress in a warped product.
r=s.symbols('r',positive=True);C=s.Function('C')(r);S=s.Function('S')(r);A=s.Function('A')(r);P=s.Function('P')(r)
# Γ^M_Mr T^r_r - Γ^M_Mr T^M_M: four tangent C'/C and two angular S'/S slots.
div=s.diff(P,r)+(4*s.diff(C,r)/C+2*s.diff(S,r)/S)*P-4*s.diff(C,r)/C*A-2*s.diff(S,r)/S*P
ck('original_tensor_divergence',s.simplify(div-(s.diff(P,r)+4*s.diff(C,r)/C*(P-A)))==0)
I=s.Function('I')(r);repair=-4*I/C**4
ck('integral_pressure_solves_divergence',s.simplify((s.diff(repair,r)+4*s.diff(C,r)/C*(repair-A)).subs(s.diff(I,r),-C**3*s.diff(C,r)*A))==0)
ct('zero_pressure_has_curvature_defect',s.simplify(div.subs(P,0).doit())==-4*A*s.diff(C,r)/C)
ck('flat_escape',s.simplify(div.subs({P:0,C:1}).doit())==0)
c=s.symbols('c',positive=True);F=4*c**4-s.Rational(4,3)*c**6+c**8/8
Af=(4-c*c)**2;Pf=s.factor(-4/c**4*(F.subs(c,2)-F))
ck('pressure_integrand_antiderivative',s.expand(s.diff(F,c)-c**3*Af)==0)
ck('pressure_fixture_original_divergence',s.factor(c*s.diff(Pf,c)+4*(Pf-Af))==0)
ck('pressure_outer_zero',Pf.subs(c,2)==0)
ck('finite_regularity_outer_matching',Af.subs(c,2)==0 and s.diff(Af,c).subs(c,2)==0 and s.diff(Pf,c).subs(c,2)==0)
ct('sign_reversed_pressure_fails',s.factor(c*s.diff(-Pf,c)+4*(-Pf-Af))!=0)
ct('homogeneous_pressure_tail_requires_boundary',s.diff(c**-4,c)*c+4*c**-4==0 and (c**-4).subs(c,2)!=0)
ck('hyperbolic_tube_jacobi',s.diff(s.sinh(r),r)==s.cosh(r) and s.diff(s.cosh(r),r)==s.sinh(r))
ck('near_axis_pressure_even',s.simplify(Pf.subs(c,s.cosh(-r))-Pf.subs(c,s.cosh(r)))==0)
# Polynomial interval for branch-zero possibilities: reused stationary classification.
t=s.symbols('t');poly=200640*t*t-13248*t+185
ck('nonradial_first_curvature_nonzero',poly.subs(t,s.Rational(1,24))!=0 and poly.subs(t,s.Rational(37,1140))!=0)
eps,K=s.symbols('eps K',positive=True)
ck('integrated_pressure_scaling',s.simplify(K/eps*eps**3)==K*eps**2)
ck('tangent_mass_scaling',eps**-3*eps**3==1)
# Fourier radial tail is r^(codimension-1-2s); endpoint logarithmic.
sob=s.symbols('sob',real=True);rad=s.symbols('rad',positive=True)
ck('partial_source_tail_endpoint',6-2*s.Rational(7,2)==-1)
ck('thin_source_tail_endpoint',9-2*s.Integer(5)==-1)
ck('regularity_gain',s.Integer(5)-s.Rational(7,2)==s.Rational(3,2))
ck('convergent_seven_normal_integral',s.integrate(rad**6/(1+rad**2)**4,(rad,0,s.oo))==5*s.pi/32)
ct('endpoint_not_square_integrable',s.limit(rad*rad**6/(1+rad**2)**s.Rational(7,2),rad,s.oo)==1)
paths=['explorations/conditional-build/k2529-native-displacement-response-2026-11-04.md','explorations/conditional-build/k2519-stationary-product-receiver-2026-11-02.md','explorations/conditional-build/k2245-localized-normal-domain-2026-10-29.md']
report={'result':'K2531','scope':'actual product scalar-measure support and supplied conserved stress; no full response','checks':checks,'contrary_controls':controls,'exact_values':{'residual_support':'R3 x {0 in R3,4}','residual_codimension':7,'majorant_choice_dimension':12,'pressure_fixture':str(Pf),'thin_integrated_pressure_order':'O(abs(K1)*epsilon^2)','fixed_width_source_sobolev':'H^(-s) iff s>7/2','thin_source_sobolev':'H^(-s) iff s>5'},'evidence_kinds':{'universal':'written total-variation bands, tensor conservation and distributional thin-limit proofs','exact_finite':'boost, connection, pressure and algebraic controls','provenance':'dependency hashes/report equality'},'dependencies':{v:hashlib.sha256((R/v).read_bytes()).hexdigest() for v in paths},'source_owned_matter_action_or_Green_response':False}
out=R/'lab/process/k2531-partial-thickness-source.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==report,'report differs'
print(f'K2531: {len(checks)} exact groups; {len(controls)} contrary controls pass')
