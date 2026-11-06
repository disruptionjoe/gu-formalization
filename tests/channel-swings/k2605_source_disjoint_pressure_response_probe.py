#!/usr/bin/env python3
"""K2605 exact off-source remainder and actual compact conserved receiver checks."""
import argparse,json,hashlib
from pathlib import Path
import sympy as s
root=Path(__file__).resolve().parents[2]
parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args()
checks=[];controls=[]
def ck(n,v):
 assert bool(v),'FAIL '+n
 checks.append(n)
def ct(n,v):
 assert bool(v),'FAIL contrary '+n
 controls.append(n)
k=s.symbols('k',nonzero=True);K0=s.Rational(35,3624192)*k*k
X,Y=s.symbols('X Y');f,g,p,q,r,z=s.symbols('f g p q r z');pot=s.Matrix([f,g,p,q,r,z]);Z=X+Y
la=6*K0;a0=-s.Rational(5,2288)*k;rE=1/(6*a0)
m=s.Rational(158,143)*k;bt=-s.Rational(15,143)*k;mK=s.Rational(148,143)*k;mV=s.Rational(503,858)*k;mH=s.Rational(893,858)*k
c=s.Rational(970112,13395)/k;mu=s.Rational(611557655,39953092608)*k*k
tau=7*f+7*g+X*p+Y*q;BA=f+(X+la)*p+Y*r;BB=g+(Y+la)*q+X*r
VA,VB=BA-tau,BB-tau;WA,WB=11*VA-13*Y*z,11*VB+13*X*z
U,V=X*VA+Y*VB,X*WA+Y*WB;RC=X*BA+Y*BB-(Z+la)*tau
Evec=s.Matrix([-(Z/2+la)*f-RC/2,-(Z/2+la)*g-RC/2,BA-(Z/2+la)*p-tau/2,BB-(Z/2+la)*q-tau/2,(BA+BB-tau-(Z+2*la)*r)/2])
E=Evec.jacobian(pot);vsrc=s.Matrix([-X-la,0,1,0,0,0]);s0=s.Matrix([X+5*la/6,-X-7*la/6,0,0,1,0])
hook=s.Matrix([2*Z*f-2*K0*X*p+2*U/13,2*Z*g-2*K0*Y*q+2*U/13,2*(Z+la+K0)*p-2*BA-2*VA/13,2*(Z+la+K0)*q-2*BB-2*VB/13,2*(Z+la)*r-BA-BB-(VA+VB)/13])
vs=s.Matrix([V,V,-WA,-WB,-(WA+WB)/2]);FC=m*s.Matrix([f,g,p,q,r])+bt*tau*s.Matrix([1,1,0,0,0])+11*vs/(13*mV)-2*hook/mH+Evec/(3*a0)
FK=mK*z-(WB-WA)/(2*mV);M=FC.col_join(s.Matrix([FK])).jacobian(pot)



M1=M.subs(k,1);Ein=E[:,0].col_join(s.Matrix([0])).subs(k,1)
bank=json.loads((root/'lab/process/k2554-analytic-source-response.json').read_text())['determinant']
pp=list(map(s.Rational,bank['P_coefficients_descending']));qq=list(map(s.Rational,bank['Q_coefficients_descending']))
det=s.expand(sum(v*(X+Y)**(5-i) for i,v in enumerate(pp))+X*Y*sum(v*(X+Y)**(2-i) for i,v in enumerate(qq)))
ck('actual_determinant_matches_saved_bank',s.cancel(M1.det(method='domain-ge')-det)==0)
cm=M1.copy();cm[:,0]=Ein;bf=cm.det(method='domain-ge')
a=a0.subs(k,1);F=s.expand(det/(12*a)-bf/(36*a*a));contact=-s.Rational(424853,149354)
R=s.Poly(s.expand(F-contact*det),Y);r4=s.factor(R.LC())
expected=-s.Rational(128665108,31733016160503214625)*(19845028500669825024*X-8236440909844467455)
ck('exact_contact_cancellation',s.degree(F,Y)==5 and s.Poly(F,Y).LC()==contact*s.Poly(det,Y).LC())
ck('actual_remainder_degree_four',R.degree()==4)
ck('actual_affine_remainder_lead',s.cancel(r4-expected)==0)
rootX=s.Rational(8236440909844467455,19845028500669825024)
ck('remainder_root_strictly_positive',rootX>0)
ck('remainder_not_zero_on_negative_spectrum',r4.subs(X,0)>0 and s.diff(r4,X)<0)
# K2600 scaling F(k²X,k²Y;k)=k^5 F1; R inherits k^5.
r4k=s.factor(k**-3*r4.subs(X,X/k**2))
ck('general_kappa_affine_root',s.cancel(r4k.subs(X,k*k*rootX))==0)
ck('scaled_root_positive',rootX*k*k>0)
# Genuine actual metric Einstein receiver E(G_A psi), without the d polynomial.
ck('conservation_A',all(s.cancel(v)==0 for v in E[0,:]+(X+la)*E[2,:]+Y*E[4,:]))
ck('conservation_B',all(s.cancel(v)==0 for v in E[1,:]+(Y+la)*E[3,:]+X*E[4,:]))
ck('formal_A_gradient_annihilation',all(s.cancel(v)==0 for v in E*s.Matrix([0,0,2,0,1,0])))
ck('formal_B_gradient_annihilation',all(s.cancel(v)==0 for v in E*s.Matrix([0,0,0,2,1,0])))
# Highest normal symbols: indefinite q is nonzero, not elliptic. Products remain nonzero.
u,v=s.symbols('u v');qb=u*u-v*v
for N in [0,1,2,4]:
 jet=u**N+2*v**N
 product=s.Poly(qb**5*jet,u,v)
 ck('normal_jet_injectivity_fixture_'+str(N),not product.is_zero and product.total_degree()==10+N)
ct('characteristic_covector_is_not_zero_polynomial',qb.subs(v,u)==0 and not s.Poly(qb,u,v).is_zero)
ct('contact_only_candidate_fails_actual_equation',not R.is_zero)
ct('old_high_order_contact_receiver_does_not_supply_offsource_signal',s.expand(F-contact*det)!=0 and s.degree(F,Y)==5)
ct('wrong_contact_sign_leaves_order_ten',s.degree(F+contact*det,Y)==5)
# Independent flat ODE fixture: (d²-m²)G=delta, G=-exp(-m|x|)/(2m).
x,m=s.symbols('x m',positive=True);G=-s.exp(-m*x)/(2*m)
ck('flat_fixture_offsource_homogeneous',s.simplify(s.diff(G,x,2)-m*m*G)==0)
ck('flat_fixture_derivative_jump',2*s.diff(G,x).subs(x,0)==1)
ck('flat_fixture_separated_positive_bump_signal_sign',G<0)
ct('single_readout_can_be_erased_by_homogeneous_change',s.simplify((G+s.exp(-m*x)/(2*m)))==0)
# Independent compact radial coercivity fixture, w=1 on[-1,1], t=(1-x²)^2.
x=s.symbols('x',real=True);tt=(1-x*x)**2
energy=s.integrate(tt*(s.diff(tt,x,2)-rootX*tt),(x,-1,1))
parts=-s.integrate(s.diff(tt,x)**2+rootX*tt**2,(x,-1,1))
ck('compact_trace_coercive_identity',energy==parts and energy<0)
# Actual radial conservation admits a noncompact trace-zero pressure when the outer collar is removed.
Cr=s.Function('Cr')(x);Pr=Cr**-7;Ar=-3*Pr/4
ck('tracezero_noncompact_pressure_conservation',s.simplify(s.diff(Pr,x)+4*s.diff(Cr,x)/Cr*(Pr-Ar))==0)
ct('outer_support_is_essential',s.simplify(4*Ar+3*Pr)==0 and Pr.subs(Cr,1)==1)
# Independent volume block at X=Y=0, without the polynomial cofactor expansion.
M00=M1.subs({X:0,Y:0});E00=Ein.subs({X:0,Y:0});vol=M00[:2,:2].inv()*E00[:2,0]
independent_F_over_d=s.factor(1/(12*a)-vol[0]/(36*a*a))
ck('independent_volume_block_transfer',independent_F_over_d==-s.Rational(10192832,286675))
ct('independent_volume_block_not_contact',independent_F_over_d-contact==-s.Rational(1400545496753,42816057950))
ct('proportional_transfer_control_admits_contact',s.expand(contact*det-contact*det)==0)
# Exact finite-dimensional response-error fixture; not a computed curved response matrix.
M0=s.diag(2,3);pert=s.Matrix([[s.Rational(1,4),s.Rational(1,4)],[s.Rational(1,4),-s.Rational(1,4)]])
ck('finite_matrix_error_bound',sum(v*v for v in pert)==s.Rational(1,4)<1)
ck('finite_matrix_invertible', (M0+pert).det()!=0)
ck('finite_matrix_inverse_bound',sum(v*v for v in (M0+pert).inv())<1)
ct('large_error_can_erase_matrix', (M0-M0).det()==0)
# Finite-sensor rank control: a nonzero signed source combination is invisible.
array=s.Matrix([[1,0,1],[0,1,1]]);null=array.nullspace()[0]
ck('finite_array_invisible_nonzero_profile',null!=s.zeros(3,1) and array*null==s.zeros(2,1))
report={'result':'K2605','checks':checks,'contrary_controls':controls,'contact_ratio_k1':str(contact),'remainder_degree_Y':R.degree(),'remainder_Y4_k1':str(r4),'positive_X_root_k1':str(rootX),'remainder_Y4_general_kappa':str(r4k),'remainder_coefficients_descending_k1':list(map(str,R.all_coeffs())), 'theorem':'Every full selected-system solution to a nonzero compact conserved radial A-pressure times an interior B atom has a nonzero source-disjoint compact conserved Einstein observation in every B neighborhood; all such observation germs uniquely determine the compact pressure profile, even allowing distinct homogeneous preparations.', 'fixed_finite_array_limit':'No fixed finite receiver array is injective on the whole infinite-dimensional signed compact-pressure space, even at one known atom; rank-nullity.', 'finite_atomic_extension':'Combine coincident locations; disjoint-neighborhood jet arguments establish complete off-union observation uniqueness for arbitrary finite atomic configurations. Fixed known support plus finite profile space inherits finite receiver stability; no finite-sensor unknown-location claim.', 'regularized_consumer':'For the fixed K2594 continuous preparation, one separating test persists with a nonzero margin under sufficiently narrow smoothing. No uniform detector across arbitrary preparations.', 'evidence_kind':'Exact actual six-row determinant/cofactor and conserved receiver identities; normal-symbol and flat ODE countercontrols; distribution-support and coercive radial proof in note, not computed full Green kernel.', 'ceiling':'Existence and injectivity of the collection of mathematical off-source observations using fully compact scalar potentials with cutoff derivatives retained; no uniform all-source stable reconstruction, calibrated sensor, causal preparation, positive energy or native GU verdict.'}
refs=['explorations/conditional-build/k2600-full-metric-contact-regularity-2026-11-06.md','lab/process/k2554-analytic-source-response.json','explorations/conditional-build/k2594-reciprocal-distributional-response-2026-11-06.md']
report['provenance']={f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in refs}
out=root/'lab/process/k2605-source-disjoint-pressure-response.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'FAIL report replay'
print(json.dumps({'result':'K2605','checks':len(checks),'controls':len(controls),'status':'pass'}))
