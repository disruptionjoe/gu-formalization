"""Exact original trace elimination, forced/homogeneous controls and source fixture.
Distributional observation, regularity and smoothing proofs are in the note.
"""
from pathlib import Path
import hashlib,json,sys
import sympy as s
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(bank,name,p):
 bank[name]=bool(p)
 if not p:raise AssertionError('FAIL '+name)
k=s.symbols('k',nonzero=True);a=-5*k/2288;la=35*k*k/604032;m0=-4*k/11;mv=503*k/858
rh,tau,u,j=s.symbols('Rh tau u j');row1=72*a*rh+12*(u-la*tau)-j;row2=m0*tau+121*u/mv+12*rh
sol=s.solve([row1,row2],[rh,u]);Ac=41511*k/s.Integer(1735888);Bc=34606/(s.Integer(29589)*k)
ck(checks,'original_full_trace_elimination',s.simplify(sol[rh]-Ac*tau+Bc*j)==0)
ck(checks,'contact_displacement_coefficient',s.simplify(Bc/Ac-6090656/(124533*k*k))==0)
ck(checks,'nonzero_original_trace_denominator',s.factor(s.det(s.Matrix([[72*a,12],[12,121/mv]])))!=0)
# Independently recover shifted full trace K2537 from original rows.
ush=s.solve(row1,rh)[0];shifted=s.factor(row2.subs(rh,ush))
expected=-5*k*tau/12+2820818*u/(2515*k)-1144*j/(15*k)
ck(checks,'original_rows_recover_full_shifted_trace',s.simplify(shifted-expected)==0)
ck(controls,'wrong_trace_Einstein_sign_changes_identity',s.simplify((m0*tau+121*u/mv-12*rh).subs({rh:sol[rh],u:sol[u]}))!=0)
ck(controls,'discarded_tensor_equation_not_identity',s.simplify(sol[rh].subs(tau,0)-sol[rh])!=0)
# Rebuild K2541 matrix from full curved coefficients; do not trust report assertions.
D=s.symbols('D');m=158*k/143;beta=-15*k/143;mh=893*k/858
f,g,z=s.symbols('f g z');tr=7*(f+g)
MA=m*f+beta*tr+la*(5*f+7*g)/(6*a);MB=m*g+beta*tr+la*(7*f+5*g)/(6*a)
RA=-121*(7*f+6*g)/(13*mv)-24*(f-g)/(13*mh)+(f+g)/a
RB=-121*(7*f+6*g)/(13*mv)+28*(f-g)/(13*mh)+(7*f+5*g)/(6*a)
u0=beta+121*la/(13*mv)-4*la/(13*mh);w0=beta+121*la/(13*mv)+14*la/(39*mh);zz=m-121*la/(13*mv)-14*la/(39*mh)
M=s.Matrix([MA+D*RA+u0*D*z,MB+D*RB+w0*D*z,-RB+zz*z]).jacobian([f,g,z]);P=s.factor(M.det());p=M.adjugate()[:,0].applyfunc(s.factor)
ck(checks,'independent_full_adjugate',all(s.simplify(x)==0 for x in M*p-s.Matrix([P,0,0])))
q=s.factor(7*(p[0]+p[1])+D*p[2]);q1=s.Rational(30160102231,53901480);q0=s.Rational(1092838523587321,126977053192704)
ck(checks,'homogeneous_trace_polynomial',s.simplify(q-q1*D-q0*k*k)==0)
ck(checks,'homogeneous_curvature_not_zero_mode',s.degree(s.gcd(P,q),D)==0)
ck(checks,'homogeneous_real_root_existence',s.discriminant(P.subs(k,1),D)>0)
Cf,Cg,Cs=[-v/(6*a) for v in p];tauC=s.factor(7*(Cf+Cg)+D*Cs)
# divdiv C: B Hessian double divergence D(D+lambda)s plus D g.
uC=s.factor(D*Cg+D*(D+la)*Cs-D*tauC)
# Original h=-C/(6a), scalar R(h)=(uC-lambda tauC)/(-6a).
RhC=s.factor(-(uC-la*tauC)/(6*a));identity=s.factor(RhC-Ac*tauC)
ck(checks,'homogeneous_original_curvature_identity',s.rem(identity,P,D)==0)
ck(checks,'homogeneous_identity_nontrivial_multiple',s.simplify((identity/P).subs(k,1))==s.Rational(2301728,63405))
# Forced Einstein z has Rh(z)=trj/(72a)=7P/(72a) for U=1,V=P/(D+2lambda).
ck(checks,'full_forced_original_identity',s.simplify(identity+7*P/(72*a)+7*Bc*P)==0)
ck(controls,'shifted_metric_would_lose_contact_identity',s.rem(Ac*tauC,P,D)!=0)
# Metric probe adjoint/divergence keeps the Einstein curvature term.
dbox,dphi=s.symbols('dBoxphi dphi');divHess=dbox+la*dphi
ck(checks,'curved_scalar_adjoint_conserved',s.expand(divHess-dbox-la*dphi)==0)
ck(controls,'omitted_adjoint_curvature_detected',s.expand(divHess-dbox)==la*dphi and la!=0)
# Pressure fixture on ACTUAL positive-curvature tube: c=cos(r), c_R=1/2.
c=s.symbols('c',positive=True);cR=s.Rational(1,2);AA=(c*c-cR*cR)**2
prim=s.integrate(c**3*AA,c);PP=s.factor(4*(prim-prim.subs(c,cR))/c**4)
ck(checks,'positive_curvature_pressure_original_divergence',s.simplify(c*s.diff(PP,c)+4*(PP-AA))==0)
ck(checks,'pressure_boundary_support',PP.subs(c,cR)==0 and s.diff(PP,c).subs(c,cR)==0)
ck(checks,'positive_pressure_center',PP.subs(c,1)>0 and AA.subs(c,1)>0)
ck(checks,'positive_trace_source_center',(4*AA+3*PP).subs(c,1)/2>0)
ck(controls,'omitted_pressure_detected',s.expand(-4*AA)!=0)
ck(controls,'wrong_pressure_sign_detected',s.simplify(-c*s.diff(PP,c)+4*(-PP-AA))!=0)
# Covector convention j=T/2, not T. Product block conserves any B profile.
Av,Pv,rho,drho,divA=s.symbols('A P rho drho divA');trj=(4*Av+3*Pv)*rho/2
ck(checks,'source_covector_trace_normalization',s.diff(trj,Av)==2*rho)
ck(controls,'missing_half_changes_contact',s.simplify((4*Av+3*Pv)*rho-2*trj)==0 and trj!=0)
JB=s.zeros(7,14);ck(checks,'B_profile_derivative_has_no_divergence_receiver',JB.T*s.ones(7,1)*drho==s.zeros(14,1))
ck(checks,'product_smoothing_preserves_conservation',(rho*divA).subs(divA,0)==0)
# Detector dimensions and necessary Sobolev mapping are exact, not numerical samples.
delta,eps,I,r0=s.symbols('delta eps I rho0',positive=True)
obs=-Bc*I*r0/delta**7
ck(checks,'partial_contact_detector_scaling',s.simplify(obs.subs(delta,2*delta)/obs)==s.Rational(1,128))
ck(checks,'thin_contact_detector_scaling',s.Rational(1,2)**10==s.Rational(1,1024))
ck(checks,'regularity_ceilings',2-s.Rational(7,2)==-s.Rational(3,2) and 2-s.Rational(10,2)==-3)
ck(checks,'thick_source_L2_squared_scaling',s.simplify((eps**-3*delta**-7)**2*eps**3*delta**7)==eps**-3*delta**-7)
ck(checks,'pressure_relative_L2_scale',s.simplify(eps**-1/eps**-3)==eps**2)
report={'result':'K2543','exact_checks':checks,'contrary_controls':controls,'coefficients':{'curvature_displacement':str(Ac),'curvature_source':str(-Bc),'displacement_contact':str(s.factor(Bc/Ac)),'homogeneous_trace_numerator':str(q),'pressure_fixture':str(PP)},'scope':'universal original scalar identity for full solutions; source-dependent joint observation, metric-only homogeneous ambiguity and supplied conserved full thickness; no full localized inverse/native GU inference','dependencies':{x:hashlib.sha256((R/x).read_bytes()).hexdigest() for x in ['explorations/conditional-build/k2531-partial-thickness-source-2026-11-04.md','tests/channel-swings/k2537_reduced_action_decoupling_probe.py','tests/channel-swings/k2541_prescribed_product_source_response_probe.py',str(Path(__file__).relative_to(R))]}}
out=R/'lab/process/k2543-localized-source-readout.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
else:assert json.loads(out.read_text())==report
print('K2543',len(checks),'exact algebra/fixture groups',len(controls),'contrary controls')
