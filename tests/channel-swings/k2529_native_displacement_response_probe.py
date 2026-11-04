"""Exact selected-action homogeneous Hessian and paired source response."""
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
x,y,a,b,k,l1,l2=s.symbols('x y a b k l1 l2',real=True)
u=a+b;v=a-b
f=s.exp(7*(x+y))*(7*((6*u-v)*l1*s.exp(-2*x)+(6*u+v)*l2*s.exp(-2*y))+182*u**3-42*u*v**2+s.Rational(7,4)*k*(u*u+v*v))
coords=[x,y,a,b];seed={x:0,y:0,a:-5*k/s.Integer(2288),b:-5*k/s.Integer(2288),l1:35*k*k/s.Integer(604032),l2:35*k*k/s.Integer(604032)}
ck('radial_full_family_stationarity',all(s.factor(s.diff(f,z).subs(seed))==0 for z in coords))
H=s.hessian(f,coords).subs(seed).applyfunc(s.factor);A=H[:2,:2];B=H[:2,2:];D=H[2:,2:]
Aref=k**3/s.Integer(57584384)*s.Matrix([[6125,8575],[8575,6125]])
Bref=-k**2/s.Integer(302016)*s.Matrix([[1225,1715],[1715,1225]])
Dref=k/s.Integer(143)*s.Matrix([[371,-735],[-735,371]])
ck('radial_A_actual_second_derivative',A==Aref);ck('radial_B_actual_mixed_derivative',B==Bref);ck('radial_D_actual_displacement_derivative',D==Dref)
ck('radial_full_determinant',s.factor(H.det())==s.Rational(4215878384375,17070568672834879488)*k**8)
E=(A-B*D.inv()*B.T).applyfunc(s.factor)
ck('radial_effective_block',E==k**3/s.Integer(655079952384)*s.Matrix([[81760175,109854325],[109854325,81760175]]))
ck('radial_effective_plus',s.factor(E[0,0]+E[0,1])==s.Rational(6125,20939776)*k**3)
ck('radial_effective_minus',s.factor(E[0,0]-E[0,1])==-s.Rational(14047075,327539976192)*k**3)
for sign in [1,-1]:
 block=s.Matrix([[A[0,0]+sign*A[0,1],B[0,0]+sign*B[0,1]],[B[0,0]+sign*B[0,1],D[0,0]+sign*D[0,1]]])
 ck('radial_sector_indefinite_'+str(sign),s.factor(block.det()/k**4)<0)
jh=s.Matrix(s.symbols('jh0:2'));jd=s.Matrix(s.symbols('jd0:2'));hh=s.Matrix(s.symbols('h0:2'));dd=D.inv()*(jd-B.T*hh)
S2=(hh.T*A*hh)[0]/2+(hh.T*B*dd)[0]+(dd.T*D*dd)[0]/2-(jh.T*hh)[0]-(jd.T*dd)[0]
Se=(hh.T*E*hh)[0]/2-((jh-B*D.inv()*jd).T*hh)[0]-(jd.T*D.inv()*jd)[0]/2
ck('source_contact_elimination_identity',s.factor(S2-Se)==0)
response=E.inv()*(jh-B*D.inv()*jd);dfull=D.inv()*(jd-B.T*response)
ck('full_original_source_equations', (H*s.Matrix.vstack(response,dfull)-s.Matrix.vstack(jh,jd)).applyfunc(s.simplify)==s.zeros(4,1))
ct('freezing_displacement_changes_response',(A.inv()-E.inv()).applyfunc(s.factor)!=s.zeros(2))
ct('dropping_contact_changes_action',s.factor((jd.T*D.inv()*jd)[0])!=0)
ct('branch_first_substitution_erases_hessian',s.hessian(f.subs(seed),coords)==s.zeros(4) and H!=s.zeros(4))
ck('zero_branch_constant_family_hessian',H.subs(k,0)==s.zeros(4))
ct('zero_kappa_not_invertible',H.subs(k,0).det()==0)
# Independent coordinate transformation checks factor-of-four normalization.
u,v=s.symbols('u v',real=True);g=f.subs({a:(u+v)/2,b:(u-v)/2},simultaneous=True)
J=s.diag(1,1,1,1);J[2:,2:]=s.Matrix([[s.Rational(1,2),s.Rational(1,2)],[s.Rational(1,2),-s.Rational(1,2)]])
Huv_rad=s.hessian(g,[x,y,u,v]).subs({x:0,y:0,u:-5*k/s.Integer(1144),v:0,l1:35*k*k/s.Integer(604032),l2:35*k*k/s.Integer(604032)}).applyfunc(s.factor)
ck('moving_amplitude_coordinate_congruence',Huv_rad==(J.T*H*J).applyfunc(s.factor))
ck('determinant_coordinate_factor',s.factor(Huv_rad.det()-H.det()/4)==0)
# Nonradial exact quotient calculation; differentiation occurs BEFORE constraints.
raw=s.hessian(g,[x,y,u,v]).subs({x:0,y:0,k:1})
ll=-u/12-13*u*u+v*v;mm=v*(1-24*u)/2
subs={l1:(ll+mm)/2,l2:(ll-mm)/2}
w=u*(s.Rational(37,12)-59*u);pol=200640*u*u-13248*u+185
def red(z):
 return s.rem(s.rem(s.Poly(s.expand(z),v),s.Poly(v*v-w,v)).as_expr(),pol,u)
Nh=raw.subs(subs).applyfunc(red)
ck('nonradial_full_family_stationarity',all(red(s.diff(g,z).subs({x:0,y:0,k:1}).subs(subs))==0 for z in [x,y,u,v]))
detH=s.factor(red(Nh.det(method='domain-ge')));Nd=Nh[2:,2:];detD=s.factor(red(Nd.det()))
ck('nonradial_determinant',s.expand(detH+s.Rational(117649,1515995281338278400000)*(6770965254529032408*u-331145834811398885))==0)
ck('nonradial_displacement_determinant',s.expand(detD-s.Rational(49,4180)*(273264*u-24485))==0)
N=(Nh[:2,:2]*detD-Nh[:2,2:]*Nd.adjugate()*Nh[:2,2:].T).applyfunc(red)
ck('schur_determinant_quotient',red(N.det()-detH*detD)==0)
num=s.factor(red(N[1,1]-N[0,0]))
ck('paired_branch_discriminator',s.expand(num-s.Rational(266511,4368100)*v*(118088*u-5735))==0)
# Verify inverse metric block without trusting the Schur formula alone.
Adj=Nh.adjugate().applyfunc(red)
ck('original_adjugate_metric_response',all(red(Adj[i,j]-N.adjugate()[i,j])==0 for i in range(2) for j in range(2)))
upper=s.Rational(1153,25080)
ck('root_rational_isolation',324**2<105609<325**2 and 828>325)
ck('roots_below_both_determinant_thresholds',upper<s.Rational(331145834811398885,6770965254529032408) and upper<s.Rational(24485,273264))
ck('discriminator_never_zero',upper<s.Rational(5735,118088) and upper<s.Rational(37,720))
ct('factor_blind_scalar_misses_readout',s.simplify(detH.subs(v,-v)-detH)==0 and s.simplify(num.subs(v,-v)+num)==0 and num!=0)
# Scaling covariance: metric block k^3, mixed k^2, distortion block k.
scaled=s.hessian(g,[x,y,u,v]).subs({x:0,y:0}).subs({u:k*u,v:k*v,l1:k*k*l1,l2:k*k*l2},simultaneous=True)
base=s.hessian(g,[x,y,u,v]).subs({x:0,y:0,k:1})
ck('all_entry_kappa_scalings',all(s.simplify(scaled[i,j]-k**(3-(i>=2)-(j>=2))*base[i,j])==0 for i in range(4) for j in range(4)))
# Supplied four-dimensional tension source: volume and conformal test normalization.
z,eps,tau=s.symbols('z eps tau',real=True)
volume=s.exp(4*z)
ck('four_dimensional_tension_metric_source',s.diff(-eps*tau*volume,z).subs(z,0)==-4*eps*tau)
# H=chi G has trace4chi; metric source convention contains one half.
chi=s.symbols('chi',real=True)
ck('nonzero_conformal_source_test',tau*s.trace(chi*s.eye(4))/2==2*tau*chi)
# Contrary regularity control: a shrinking normal test has delta action1 but
# any bounded smooth density integral tends to0 as epsilon^10. This polynomial
# extends by zero as C3, sufficient for this order-zero measure control only.
# The universal
# manifold proof uses dense complement, independently of this flat model.
r,eta=s.symbols('r eta',positive=True)
bump=(1-(r/eta)**2)**4
normal_integral=s.integrate(bump,(r,-eta,eta))
ck('normal_test_volume_scales_codimension10',s.simplify(normal_integral**10/(eta**10))==s.Rational(256,315)**10)
ct('delta_source_not_smooth_density',bump.subs(r,0)==1 and s.limit(normal_integral**10,eta,0,dir='+')==0)
refs=['explorations/conditional-build/k2519-stationary-product-receiver-2026-11-02.md','lab/process/k2519-stationary-product-receiver.json','explorations/conditional-build/k2345-curved-bundle-ricci-obstruction-2026-10-30.md','explorations/conditional-build/k2527-coupled-horizontal-bending-action-2026-11-02.md']
report={'result':'K2529','scope':'selected I1 completion, homogeneous four-coordinate Hessian and supplied coordinate-source response; no full Green or physical source','checks':checks,'contrary_controls':controls,'radial_hessian_ab':[[str(t) for t in H.row(i)] for i in range(4)],'radial_effective_metric':[[str(t) for t in E.row(i)] for i in range(2)],'nonradial_detH_uv_k1':str(detH),'nonradial_detD_uv_k1':str(detD),'nonradial_inverse_metric_diagonal_difference_numerator':str(num),'evidence_kinds':{'exact':'original density differentiation, source elimination, quotient determinants and branch discriminator','inherited':'K2519 full first-variation admissibility, K2345 nonstationary metric-bundle control','universal':'finite-dimensional inverse-function consequence; thin-source first variation, Ward identity and smoothness obstruction in note; no field-domain inverse','reporting':'saved report equality and dependency pins'},'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in refs}}
path=R/'lab/process/k2529-native-displacement-response.json'
if '--write' in sys.argv:path.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(path.read_text())==report,'saved report differs'
print(json.dumps({'checks':len(checks),'contrary_controls':len(controls),'all_pass':True}))
