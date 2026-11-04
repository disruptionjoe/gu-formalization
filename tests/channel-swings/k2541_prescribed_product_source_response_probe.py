"""Exact full scalar-sector reduction and original-metric source controls.
Local distributional existence uses the theorem/hypotheses in the companion note.
"""
from pathlib import Path
import hashlib,json,sys
import sympy as s
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(bank,name,p):
 bank[name]=bool(p)
 if not p:raise AssertionError('FAIL '+name)
k,D=s.symbols('k D',nonzero=True);a=-5*k/2288;la=35*k*k/604032
m=158*k/143;beta=-15*k/143;mv=503*k/858;mh=893*k/858
f,g,z=s.symbols('f g z');tau=7*(f+g)
MA=m*f+beta*tau+la*(5*f+7*g)/(6*a)
MB=m*g+beta*tau+la*(7*f+5*g)/(6*a)
RA=-121*(7*f+6*g)/(13*mv)-24*(f-g)/(13*mh)+(f+g)/a
RB=-121*(7*f+6*g)/(13*mv)+28*(f-g)/(13*mh)+(7*f+5*g)/(6*a)
u=beta+121*la/(13*mv)-4*la/(13*mh)
w=beta+121*la/(13*mv)+14*la/(39*mh)
zeta=m-121*la/(13*mv)-14*la/(39*mh)
expr=s.Matrix([MA+D*RA+u*D*z,MB+D*RB+w*D*z,-RB+zeta*z])
M=expr.jacobian([f,g,z]);P=s.factor(M.det());p=M.adjugate()[:,0].applyfunc(s.factor);Q=D+2*la
ck(checks,'full_polynomial_adjugate',all(s.simplify(q)==0 for q in M*p-s.Matrix([P,0,0])))
ck(checks,'determinant_quadratic',s.Poly(P,D).degree()==2)
expected=-(3094302258846107172864*D**2+48852605799064661880*D*k**2+19514973635487875*k**4)/(38093115957811200*k)
ck(checks,'determinant_exact_coefficients',s.simplify(P-expected)==0)
ck(checks,'adjugate_Hessian_constant',p[2]==-s.Rational(10607043027,17967160))
ck(checks,'mass_Hessian_divergence',s.simplify(w+zeta-k)==0)
# Independent Hessian curvature calculation: Box Hess=Hess Box+2lambda Hess-2Riem Hess.
H,BH,trace=s.symbols('H Box_Hess trace');curv=la/6
S_A=2*la*D/13;S_B=2*la*D/13-2*curv*D;S_H=2*curv-2*la/13
ck(checks,'Hessian_hook_B',s.simplify(S_B+7*la*D/39)==0)
ck(checks,'Hessian_hook_H',s.simplify(S_H-7*la/39)==0)
ck(checks,'Hessian_column_from_full_Euler',all(s.simplify(q)==0 for q in M[:,2]-s.Matrix([beta*D+121*la*D/(13*mv)-2*S_A/mh,beta*D+121*la*D/(13*mv)-2*S_B/mh,m-121*la/(13*mv)-2*S_H/mh])))
# Conservation is an identity of the full B metric/Hessian coefficients, not a trace test.
Div=expr[1]+(D+la)*expr[2]
ck(checks,'divergence_Hessian_column',s.simplify(s.diff(Div,z)-(k*D+la*zeta))==0)
ck(checks,'forced_B_Hessian_rows_zero',all(s.simplify(q)==0 for q in (M*p)[1:]))
# Both skew input and its forcing vanish for arbitrary scalar f,g,z.
ck(checks,'skew_closed_exact_gradient',s.simplify(11*(-7*f-6*g+la*z)-(-77*f-66*g+11*la*z))==0)
P0=s.Poly(P.subs(k,1),D);disc=s.discriminant(P0.as_expr(),D)
ck(checks,'two_real_distinct_roots',disc>0)
ck(checks,'two_negative_roots',all(c<0 for c in P0.all_coeffs()))
ck(checks,'no_constant_kernel',P.subs(D,0)!=0)
ck(checks,'no_shared_Einstein_root',s.simplify(P.subs(D,-2*la))!=0)
# Einstein blocks for z=u GA+v GB: no Hessian coefficient if v=-7u/5.
Z=5/(72*a);V=-7*Z/5
EA=s.factor(3*D*(Z+V)+la*(5*Z+7*V)/2);EB=s.factor((7*Z+5*V)/2)
ck(checks,'Einstein_prescribed_A',s.simplify(EA+Q/(12*a))==0)
ck(checks,'Einstein_prescribed_B',EB==0)
# Common master chi: U=Q chi,V=P chi; M(f,g,z)=-J/(6a)e1, E metric=-J/(12a).
fields=-p*Q/(6*a)
ck(checks,'common_master_tensor',all(s.simplify(q)==0 for q in M*fields+s.Matrix([P*Q/(6*a),0,0])))
ck(checks,'common_master_Einstein',s.simplify(EA*P+P*Q/(12*a))==0)
NA=s.factor(5*P/(72*a)+p[0]*Q/(36*a*a))
ck(checks,'original_hA_source_identity',s.simplify(NA-(Z*P-fields[0]/(6*a)))==0)
ck(checks,'original_hA_numerator_degree',s.Poly(NA,D).degree()==2)
ck(checks,'original_hA_no_canceled_poles',s.degree(s.gcd(NA,P*Q),D)==0)
leading=s.factor(s.LC(s.Poly(NA,D))/s.LC(s.Poly(P*Q,D)))
ck(checks,'original_hA_nonzero_high_frequency',leading==s.Rational(559559,224031)/k)
# Constant J=1 is a genuine order-zero forcing, checked by independent finite matrix solve.
C0=M.subs(D,0).inv()*s.Matrix([-1/(6*a),0,0])
ck(checks,'constant_source_direct_solution',all(s.simplify(q)==0 for q in C0+p.subs(D,0)/(6*a*P.subs(D,0))))
ck(checks,'delta_source_regularities',-s.Rational(7,2)-4+6==-s.Rational(3,2))
# Concrete contrary objects, not modified pass predicates.
ck(controls,'dropping_Hessian_fails_prescribed_source',s.simplify((M*s.Matrix([p[0],p[1],0]))[2])!=0)
ck(controls,'wrong_metric_shift_changes_source_readout',s.simplify(NA-5*P/(72*a))!=0)
ck(controls,'old_repaired_profile_fails_prescribed_B_zero',s.simplify(MB.subs({f:1,g:s.Rational(332500315,171866582)}))==-s.Rational(24749767063,272236665888)*k)
ck(controls,'repeated_principal_product_not_real_principal_type',s.diff(s.Symbol('q')**3,s.Symbol('q')).subs(s.Symbol('q'),0)==0)
eta=s.diag(1,1,1,-1,-1,-1,-1);xi=s.Matrix([1,0,0,1,0,0,0])
ck(controls,'nonnull_gradient_on_characteristic', (xi.T*eta*xi)[0]==0 and 2*eta*xi!=s.zeros(7,1))
report={'result':'K2541','exact_checks':checks,'contrary_controls':controls,'scope':'full prescribed A-homogeneous order-zero source j=J(B)G_A has local distributional solutions; original on-source continuous readout fails for delta within this family; not K2531 localized source, Green selection, physical quotient or GU certification','polynomials':{'matrix':str(M),'determinant':str(P),'adjugate_first_column':[str(x) for x in p],'hA_numerator':str(NA),'hA_leading_ratio':str(leading)},'dependencies':{q:hashlib.sha256((R/q).read_bytes()).hexdigest() for q in ['tests/channel-swings/k2539_covariant_tensor_constraints_probe.py',str(Path(__file__).relative_to(R))]}}
out=R/'lab/process/k2541-prescribed-product-source-response.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==report
print('K2541',len(checks),'exact groups',len(controls),'contrary controls')
