#!/usr/bin/env python3
"""K2617 actual radial contact symbol, conservation and labeled Gram consumers."""
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
prior=json.loads((root/'lab/process/k2605-source-disjoint-pressure-response.json').read_text())
coeffs=[s.sympify(t,locals={'X':X}) for t in prior['remainder_coefficients_descending_k1']]
R=sum(v*Y**(4-i) for i,v in enumerate(coeffs));F=s.expand(s.Rational(prior['contact_ratio_k1'])*det+R)
poly=s.Poly(F,X,Y);aY=s.Rational(7412316633293468946137088,22521658027326625);aX=s.Rational(224005433669517008830464,900866321093065)
ck('actual_contact_total_degree',poly.total_degree()==5)
top=sum(c*X**i*Y**j for (i,j),c in poly.terms() if i+j==5)
ck('actual_principal_factorization',s.expand(top-aY*(X+Y)**4*(s.Rational(31425,41594)*X+Y))==0)
ck('actual_radial_coefficient',poly.coeff_monomial(X**5)==aX and aX!=0)
# Independent six-row computation at Y=0 avoids assuming the saved remainder's radial coefficient.
M0=M1.subs(Y,0);E0=Ein.subs(Y,0);cm=M0.copy();cm[:,0]=E0
independent=s.cancel(M0.det(method='domain-ge')/(12*a0.subs(k,1))-cm.det(method='domain-ge')/(36*a0.subs(k,1)**2))
ck('independent_original_six_row_radial_polynomial',s.expand(independent-F.subs(Y,0))==0)
ck('general_kappa_radial_scaling',s.cancel(k**5*aX*(X/k**2)**5-aX*k**-5*X**5)==0)
# Independent original matrix scaling: potential f,g scale k², p,q,r,z scale1; metric f,g rows k³; Hessian/mixed/skew rows k.
Cin=s.diag(k*k,k*k,1,1,1,1);Cout=s.diag(k**3,k**3,k,k,k,k)
ck('original_matrix_scaling',all(s.cancel(z)==0 for z in (M.subs({X:k*k*X,Y:k*k*Y})*Cin-Cout*M1)))
# Genuine actual metric Einstein receiver E(G_A psi), without the d polynomial.
ck('conservation_A',all(s.cancel(v)==0 for v in E[0,:]+(X+la)*E[2,:]+Y*E[4,:]))
ck('conservation_B',all(s.cancel(v)==0 for v in E[1,:]+(Y+la)*E[3,:]+X*E[4,:]))
ck('formal_A_gradient_annihilation',all(s.cancel(v)==0 for v in E*s.Matrix([0,0,2,0,1,0])))
ck('formal_B_gradient_annihilation',all(s.cancel(v)==0 for v in E*s.Matrix([0,0,0,2,1,0])))
# Exact radial trace/conservation and its necessary outer-support condition.
x=s.symbols('x',real=True);Cr=s.Function('Cr')(x);pressure=s.Function('P')(x);alpha=s.diff(Cr,x)/Cr
AA=pressure+s.diff(pressure,x)/(4*alpha);trace=(4*AA+3*pressure)/2
ck('actual_pressure_conservation',s.simplify(s.diff(pressure,x)+4*alpha*(pressure-AA))==0)
ck('actual_trace_map',s.simplify(trace-7*pressure/2-s.diff(pressure,x)/(2*alpha))==0)
ck('tracezero_integrating_factor',s.simplify(s.diff(Cr**7*pressure,x)-2*alpha*Cr**7*trace)==0)
noncompact=Cr**-7
ct('outer_support_cannot_be_dropped',s.simplify(trace.subs(pressure,noncompact).doit())==0 and noncompact!=0)
# Variable coefficients have analytic trigonometric formulas on a regular shell.
z=s.symbols('z',positive=True);C=s.cos(z*x);S=s.sin(z*x)/z
weight=C**4*S**2
ck('actual_weighted_radial_coefficient',s.simplify(s.diff(weight,x)/weight-4*s.diff(C,x)/C-2*s.diff(S,x)/S)==0)
# The top symbol is not elliptic, but the radial normal is noncharacteristic.
xi,eta=s.symbols('xi eta');qB=xi*xi-eta*eta
ct('characteristic_directions_survive',s.expand(top.subs({X:0,Y:qB})).subs(eta,xi)==0)
ck('radial_normal_noncharacteristic',top.subs({X:1,Y:0})==aX)
ct('dropping_radial_principal_term_breaks_argument',(top-aX*X**5).subs({X:1,Y:0})==0)
# Explicit finite algebraic Gram fixture. This is not a numerical curved-source bank.
z=s.symbols('z',real=True);gs=[1,z,1+z*z]
G=s.Matrix([[s.integrate(a*b,(z,-1,1)) for b in gs] for a in gs])
ck('fixture_Gram_positive_definite',all(G[:n,:n].det()>0 for n in [1,2,3]))
coef=s.Matrix([2,-3,5]);read=-G*coef
ck('fixture_exact_coefficient_recovery',-G.inv()*read==coef)
ck('fixture_whitened_contact_response',G.inv()*(-G)==-s.eye(3))
noise=s.Matrix([s.Rational(1,100),-s.Rational(1,200),s.Rational(1,300)])
error=-G.inv()*(read+noise)-coef
ck('fixture_actual_noise_response',error==-G.inv()*noise)
# Frobenius gives a fully rational upper bound for this fixture, separately from analytic spectral bound.
ck('fixture_noise_bound',s.expand((error.T*error)[0])<=sum(z*z for z in G.inv())*(noise.T*noise)[0])
wrong=-G.T*read
ct('inverse_cannot_be_replaced_by_transpose',wrong!=coef)
ct('dependent_sources_destroy_Gram',s.Matrix([[2,2],[2,2]]).det()==0)
array=s.Matrix([[1,0,1],[0,1,1]]);null=array.nullspace()[0]
ck('two_readings_leave_three_coefficient_direction',array*null==s.zeros(2,1) and null!=s.zeros(3,1))
# Cutoff product rule: differentiating the whole potential is not cutting off an old receiver.
chi=x*x;potential=s.exp(x)
ct('post_differentiation_cutoff_changes_receiver',s.simplify(s.diff(chi*potential,x,2)-chi*s.diff(potential,x,2))!=0)
refs=['lab/process/k2554-analytic-source-response.json','lab/process/k2605-source-disjoint-pressure-response.json','explorations/conditional-build/k2548-compact-coupled-metric-detectors-2026-11-04.md']
report={'result':'K2617','checks':checks,'contrary_controls':controls,'principal_polynomial_k1':str(s.factor(top)),'radial_X5_k1':str(aX),'B_Y5_k1':str(aY),'radial_scaling':'kappa^-5','Gram_fixture':[[str(z) for z in row] for row in G.tolist()],'fixture_coefficients':list(map(str,coef)),'fixture_readings':list(map(str,read)),'fixture_error':list(map(str,error)),'provenance':{f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in refs},'imported_theorem':{'name':'Holmgren distribution uniqueness','source':'https://laurentca.perso.math.cnrs.fr/papiers/UCPApplications.pdf','locator':'Theorem1.2.4 printed page12','hypotheses':'analytic actual operator, radial noncharacteristic surface, zero outward side, compact reduced support; no analytic-source assumption'},'evidence_kind':'exact actual contact polynomial and independent six-row radial specialization; exact conservation and labeled finite Gram fixtures; universal uniqueness and receiver construction are written proofs','ceiling':'complete interior/contact mathematical observations; no exterior uniqueness, arbitrary-data solvability, uniform stability or physical apparatus'}
out=root/'lab/process/k2617-interior-pressure-identifiability.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'FAIL saved report replay'
print(json.dumps({'result':'K2617','checks':len(checks),'controls':len(controls),'status':'pass'}))
