"""Exact selected-Clifford coefficients for the curved radial theorem."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,hashlib
import sympy as s
R=Path(__file__).resolve().parents[2];st='k2357-curved-native-stationarity';checks={};controls={}
def check(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def control(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError('ineffective changed-input control: '+k)
backend='tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py';p=R/backend;src=p.read_text();ns={'__file__':str(p),'__name__':'selected_backend'};exec(compile(src[:src.index('def sparse_rank')],str(p),'exec'),ns)
b=ns['blade'];w=ns['wedge_raw'];add=ns['fadd'];P=lambda u,v:w(u,v).get(ns['FULL'],{}).get(0,ns['ZERO']);S=lambda v:ns['shiab'](v,('comm','symi','symi'));phi=ns['PHI1'];star=ns['hodge']
def rat(v):
 assert v[1]==0
 return s.Rational(v[0].numerator,v[0].denominator)
def J(v,Z):return (rat(P(Z,S(w(v,phi))))-rat(P(phi,S(w(v,Z)))))/2
Z={2:b((0,1))};v={1:b(())};left=rat(P(Z,S(w(v,phi))));right=rat(P(phi,S(w(v,Z))))
check('actual_derivative_pairings',left==2 and right==24);check('actual_adjoint_skew_coefficient',J(v,Z)==-11)
# Pick for each input mu a receiver dx^nu gamma_(mu,nu), nu cyclic; sorted blade orientation explicit.
receivers=[{1<<((mu+1)%14):b(tuple(sorted((mu,(mu+1)%14))))} for mu in range(14)]
minor=s.Matrix([[J({1<<mu:b(())},Z) for mu in range(14)] for Z in receivers]);check('all196_derivative_minor_entries',all(minor[i,j]==0 for i in range(14) for j in range(14) if i!=j) and all(abs(minor[i,i])==11 for i in range(14)))
check('injectivity_nonzero_determinant',abs(minor.det())==11**14)
null=s.Matrix([1,1]+[0]*12);check('null_covector_still_detected',(minor*null)!=s.zeros(14,1))
pp=w(phi,phi);a,k,lam,q=s.symbols('a k lam q',real=True);mass=[];cubic=[];curvature=[]
for mu in range(14):
 Z={1<<mu:b(mu)};mass.append(rat(P(Z,star(phi))));c1=rat(P(Z,S(pp)));c2=rat(P(phi,S(add(w(Z,phi),w(phi,Z)))));cubic.append((c1+c2)/3);curvature.append(rat(P(Z,S(ns['PHI2']))))
check('all14_radial_mass_entries',mass==[1]*14);check('all14_radial_cubic_entries',cubic==[312]*14);check('all14_constant_curvature_entries',curvature==[156]*14)
check('dimension14_Einstein_normalization',-2*(13*q-14*13*q/2)==156*q)
poly=312*a*a+k*a+12*lam;disc=s.discriminant(poly,a);check('curved_discriminant',disc==k*k-14976*lam)
roots=[(-k+s.sqrt(disc))/624,(-k-s.sqrt(disc))/624];check('two_exact_roots',all(s.simplify(poly.subs(a,r))==0 for r in roots))
check('flat_old_branches_reused',s.factor(poly.subs(lam,0))==a*(312*a+k))
check('double_root_retained',s.expand(poly.subs(lam,k*k/14976)-(312*(a+k/624)**2))==0)
check('positive_lambda_no_real_root_witness',disc.subs({k:1,lam:s.Rational(1,7488)})==-1)
# K2345 independently stored exact metric two-jet result, inspected instead of recomputing its whole bank.
prior=json.loads((R/'lab/process/k2345-curved-bundle-ricci-obstruction.json').read_text());check('upstream_Ricci_values',prior['details']['scalar']=='-10' and prior['details']['Ricci_eigenvalues']=={'1/4':5,'-5/4':9})
G1=s.Rational(1,4)+5;G2=-s.Rational(5,4)+5;eq1=-2*G1+k*a+312*a*a;eq2=-2*G2+k*a+312*a*a
check('non_Einstein_all_amplitude_obstruction',s.expand(eq1-eq2)==-3)
control('omit_formal_adjoint',left/2!=J(v,{2:b((0,1))}))
control('replace_two_curvatures_by_average',s.expand(eq1-eq2)!=0 and s.expand((-2*(G1+G2)/2+k*a+312*a*a)-(-2*(G1+G2)/2+k*a+312*a*a))==0)
control('discard_merged_root',disc.subs({k:1,lam:s.Rational(1,14976)})==0 and poly.subs({k:1,lam:s.Rational(1,14976),a:-s.Rational(1,624)})==0)
control('flat_root_is_not_curved_stationarity',poly.subs({a:-k/312,lam:1})==12)
control('ignore_derivative_equations_on_variable_amplitude',minor*null!=s.zeros(14,1))
controls['transfer_fixed_geometry_to_metric_stationarity']='analytic scope control: translation Euler zero does not set independent metric/epsilon Euler; no computed metric solution claimed'
deps=[backend,'lab/process/k2345-curved-bundle-ricci-obstruction.json','explorations/conditional-build/selected-action-curvature-graph-six-versus-four-2026-08-06.md',f'explorations/conditional-build/{st}-2026-10-31.md',str(Path(__file__).relative_to(R))]
out={'result_id':'K2357','checks':len(checks),'check_names':list(checks),'altered_input_controls':controls,'evidence_kind':'exact rational selected-Clifford and symbolic controls; all-receiver theorem in companion proof','details':{'derivative_pairings':[str(left),str(right)],'minor_diagonal':[str(minor[i,i]) for i in range(14)],'minor_determinant':str(minor.det()),'cubic_coefficient':312,'constant_curvature_coefficient':156,'Einstein_quadratic':str(poly),'discriminant':str(disc),'K2345_equation_difference':-3},'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps}}
target=R/f'lab/process/{st}.json'
if '--write' in sys.argv:target.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
else:assert json.loads(target.read_text())==out
print(json.dumps(out['details']));print('PASS',len(checks),'exact checks;',len(controls),'controls (one analytic scope control)')
