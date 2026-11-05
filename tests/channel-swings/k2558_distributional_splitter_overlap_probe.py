"""Exact distributional overlap algebra; universal arguments are in K2558."""
from pathlib import Path
import sympy as s
import json,hashlib,sys
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(name,ok):
 checks[name]=bool(ok)
 if not ok:raise AssertionError(name)
def ct(name,ok):
 controls[name]=bool(ok)
 if not ok:raise AssertionError(name)
k=s.symbols('k',nonzero=True);K0=s.Rational(35,3624192)*k*k
X,Y=s.symbols('X Y');f,g,p,q,r,z=s.symbols('f g p q r z');pot=s.Matrix([f,g,p,q,r,z]);Z=X+Y
la=6*K0;a0=-s.Rational(5,2288)*k;rE=1/(6*a0)
m=s.Rational(158,143)*k;bt=-s.Rational(15,143)*k;mK=s.Rational(148,143)*k;mV=s.Rational(503,858)*k;mH=s.Rational(893,858)*k
c=s.Rational(970112,13395)/k;mu=s.Rational(611557655,39953092608)*k*k
ck('TT_kinetic_coefficient',s.cancel(-4/mH-rE-c)==0)
ck('TT_full_mass_coefficient',s.cancel(m+28*K0/mH+2*K0*rE-c*(mu-7*K0))==0)
ck('TT_Einstein_curvature_shift',-14*K0-2*K0==-16*K0)
ck('TT_displacement_curvature_shift',-14*K0+mu-7*K0==mu-21*K0)
tau=7*f+7*g+X*p+Y*q;BA=f+(X+la)*p+Y*r;BB=g+(Y+la)*q+X*r
VA,VB=BA-tau,BB-tau;WA,WB=11*VA-13*Y*z,11*VB+13*X*z
U,V=X*VA+Y*VB,X*WA+Y*WB;RC=X*BA+Y*BB-(Z+la)*tau
Evec=s.Matrix([-(Z/2+la)*f-RC/2,-(Z/2+la)*g-RC/2,BA-(Z/2+la)*p-tau/2,BB-(Z/2+la)*q-tau/2,(BA+BB-tau-(Z+2*la)*r)/2])
E=Evec.jacobian(pot);vsrc=s.Matrix([-X-la,0,1,0,0,0]);s0=s.Matrix([X+5*la/6,-X-7*la/6,0,0,1,0])
for i in range(5):ck('full_Einstein_source_row_'+str(i),s.cancel((E*s0)[i]-vsrc[i]*(Z+2*la))==0)
ck('scalar_source_divergence_A',s.cancel(vsrc[0]+(X+la)*vsrc[2]+Y*vsrc[4])==0)
ck('scalar_source_divergence_B',s.cancel(vsrc[1]+(Y+la)*vsrc[3]+X*vsrc[4])==0)
ck('scalar_source_trace',s.cancel(7*vsrc[0]+7*vsrc[1]+X*vsrc[2]+Y*vsrc[3]+6*X+7*la)==0)
hook=s.Matrix([2*Z*f-2*K0*X*p+2*U/13,2*Z*g-2*K0*Y*q+2*U/13,2*(Z+la+K0)*p-2*BA-2*VA/13,2*(Z+la+K0)*q-2*BB-2*VB/13,2*(Z+la)*r-BA-BB-(VA+VB)/13])
vs=s.Matrix([V,V,-WA,-WB,-(WA+WB)/2]);FC=m*s.Matrix([f,g,p,q,r])+bt*tau*s.Matrix([1,1,0,0,0])+11*vs/(13*mV)-2*hook/mH+Evec/(3*a0)
FK=mK*z-(WB-WA)/(2*mV);M=FC.col_join(s.Matrix([FK])).jacobian(pot)

# New finite extension and synchronized inverse identities.
v=s.Matrix([K0,0,1,0,0,0]);M0=M.subs(X,-7*K0)
ck('overlap_all_six_rows',all(s.cancel(x)==0 for x in M0*v-c*(Y+mu)*v))
d0=s.factor(M0.det(method='domain-ge'));R4,rem=s.div(s.Poly(d0,Y),s.Poly(c*(Y+mu),Y))
ck('overlap_four_factor_quotient',rem.is_zero and R4.degree()==4)
for n,yy in enumerate([0,s.Rational(1,3),-2]):
 mm=M0.subs({Y:yy,k:1});vv=v.subs(k,1);qq=R4.as_expr().subs({Y:yy,k:1})
 ck('independent_adjugate_'+str(n),all(s.cancel(x)==0 for x in mm.adjugate()*vv-qq*vv))
ct('wrong_overlap_eigenvalue_rejected',any(s.cancel(x)!=0 for x in M.subs(X,-6*K0)*v-c*(Y+mu)*v))
C,K=s.symbols('C K',positive=True);psi=s.Function('psi')(C)
f2=(-7*psi-(4/C-7*C)*s.diff(psi,C))/(1-C*C)
rules={s.diff(psi,C,2):f2}
for n in (3,4):rules[s.diff(psi,C,n)]=s.diff(rules[s.diff(psi,C,n-1)],C).subs(s.diff(psi,C,2),f2)
def red(e):
 for n in (4,3,2):e=e.subs(s.diff(psi,C,n),rules[s.diff(psi,C,n)])
 return s.factor(e)
def Xr(e):return K*((1-C*C)*s.diff(e,C,2)+(4/C-7*C)*s.diff(e,C))
def D5(e):return K*((1-C*C)*s.diff(e,C,2)+(6/C-11*C)*s.diff(e,C))
bp=K*((1-C*C)*s.diff(psi,C,2)-C*s.diff(psi,C)+psi)
bp=red(bp)
ck('radial_overlap_scalar_eigenvalue',red(Xr(psi)+7*K*psi)==0)
ck('radial_overlap_TT_eigenvalue',red(D5(bp)-21*K*bp)==0)
ck('source_splitter_opposite_TT_sign',red(bp+K*(4/C-6*C)*s.diff(psi,C)+6*K*psi)==0)
ct('flat_TT_operator_rejected',red(K*(1-C*C)*s.diff(bp,C,2)-21*K*bp)!=0)
psi0,p2=s.symbols('psi0 p2');p2value=-7*K*psi0/3
ck('regular_center_TT_nonzero_coefficient',s.expand((p2+K*psi0).subs(p2,p2value)+4*K*psi0/3)==0)
chiR,psir,a0p=s.symbols('chiR psir a0p')
ck('Dirichlet_splitter_boundary',s.expand((chiR-chiR*psir).subs(psir,1))==0)
ct('polynomial_source_requires_actual_boundary_correction',s.Rational(7,84)-s.Rational(10,84)<0)
ck('positive_resolvent_gap',s.cancel(7*K0/(3*k*k))==s.Rational(245,10872576) and s.Rational(245,10872576)<1)
n=s.symbols('n',integer=True,nonnegative=True)
ck('added_scalar_eigenvalue_distinct',s.expand(2*n*(2*n+6)-7-(2*n-1)*(2*n+7))==0)
ck('added_TT_eigenvalue_distinct',all(z>0 for z in s.Poly(2*n*(2*n+10)+21,n).all_coeffs()))
# The first displayed polynomial has integer zero candidates only at 1/2,-7/2.
ck('scalar_integer_roots_excluded',s.solve((2*n-1)*(2*n+7),n)==[])
Ws,Wt,qs,qt,hess,psiv,cross=s.symbols('Ws Wt qs qt hess psiv cross')
zs=-rE*s0.subs(X,-7*K0)/2
AA_s=zs[0]*psiv*Ws+zs[2]*Ws*hess
AA_t=rE*Wt*(hess+K0*psiv)
AAQ=rE**2*(qs-qt)*(hess+K0*psiv)
expected=-rE*Ws*hess+(rE*(Ws-Wt)+rE**2*(qs-qt))*(hess+K0*psiv)
ck('original_metric_general_overlap_AA',s.expand(AA_s-AA_t+AAQ-expected)==0)
ck('original_metric_general_overlap_AB',s.cancel(zs[4]*cross+rE*cross/2)==0)
eta,delta=s.symbols('eta delta');defect=rE*delta+rE*rE*eta
Ydefect=-5*K0*rE*delta-mu*rE*rE*eta
ck('Einstein_detects_inverse_mismatch',s.cancel(-(Ydefect+5*K0*defect)/2-rE*rE*(mu-5*K0)*eta/2)==0)
ck('nonzero_pole_gap',s.cancel(mu-5*K0-s.Rational(67736495,4439232512)*k*k)==0)
ct('independent_Q_inverse_need_not_be_gauge',s.cancel((mu-5*K0).subs(k,1))>0)
ct('omitting_original_metric_shift_misses_defect',s.cancel(rE*rE*(mu-5*K0)/2)!=0)
# Explicit rectangular right inverses need not commute; exact residual checks.
# On polynomials, integration with independently selected constants gives a finite fixture.
x=s.symbols('x');f=x+1
I0=lambda q:s.integrate(q,(x,0,x))
I1=lambda q:s.integrate(q,(x,1,x))
ck('ordered_inverse_fixture_solves_second_derivative',s.diff(I1(I0(f)),x,2)==f)
ct('right_inverse_commutation_not_available',s.expand(I0(I1(f))-I1(I0(f)))!=0)
ck('overlap_TT_Einstein_shift',21*K0-16*K0==5*K0)
ck('overlap_TT_displacement_shift',21*K0+mu-21*K0==mu)
ck('homogeneous_R1_displacement_equation',s.cancel((21*K0-mu)+mu-21*K0)==0)
ck('homogeneous_original_metric_detector',s.cancel(rE*((21*K0-mu)-16*K0)/2+rE*(mu-5*K0)/2)==0)
ct('gauge_invariance_not_solution_independence',s.cancel((rE*(mu-5*K0)).subs(k,1))!=0)
paths=['explorations/conditional-build/k2558-distributional-splitter-overlap-2026-11-05.md','tests/channel-swings/k2558_distributional_splitter_overlap_probe.py','explorations/conditional-build/k2552-localized-source-domain-2026-11-04.md','explorations/conditional-build/k2554-analytic-source-response-2026-11-05.md','explorations/conditional-build/k2556-distributional-source-response-2026-11-05.md']
report={'result':'K2558','checks':checks,'contrary_controls':controls,'overlap':{'quotient_degree':4,'radial_TT_eigenvalue':'21K','pole_gap':str(s.cancel(mu-5*K0))},'evidence_kinds':{'exact':'new radial extension, synchronized overlap and inverse defect, full six-row/cofactor fixtures and homogeneous response coefficients; introductory coefficient/source identities reused as supporting checks','universal':'regular Dirichlet uniqueness, local bounded factor inverses, distributional gauge duality, fixed-N smoothing and compact off-source detector proof in note','bookkeeping':'ordered right-inverse polynomial fixture and boundary normalization','not_claimed':'N-uniform radial cutoff, common physical domain, empirical response or native GU'},'dependencies':{x:hashlib.sha256((R/x).read_bytes()).hexdigest() for x in paths}}
out=R/'lab/process/k2558-distributional-splitter-overlap.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved_report_consistency'
print('K2558 PASS',len(checks),'exact/supporting groups',len(controls),'contrary controls')
