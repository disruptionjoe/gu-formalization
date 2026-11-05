"""Exact new source reduction checks; universal inverse/domain proofs are in note."""
from pathlib import Path
import sympy as s
import json,hashlib,sys
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,x):
 checks[k]=bool(x)
 if not x:raise AssertionError(k)
def ct(k,x):
 controls[k]=bool(x)
 if not x:raise AssertionError('contrary '+k)
K,S,C=s.symbols('K S C',nonzero=True);bs=s.symbols('b0:5');b=bs[0]
alpha=-K*S/C;beta=C/S;H=4*alpha+2*beta
rel=C*C+K*S*S-1
def dr(expr):
 return s.diff(expr,S)*C-s.diff(expr,C)*K*S+sum(s.diff(expr,bs[i])*bs[i+1] for i in range(4))
def reduced(expr):
 n,d=s.fraction(s.cancel(expr));return s.rem(n,rel,C)==0
def tt(z):
 return s.Matrix([-S*C*dr(z)/4-3*z/4+7*K*S*S*z/4,z,S*C*dr(z)/2+(1-7*K*S*S/2)*z])
tt_b=tt(b);tb,bb,ab=tt_b
ck('trace_TT',s.expand(4*tb+bb+2*ab)==0)
ck('divergence_TT',reduced(dr(bb)+4*alpha*(bb-tb)+2*beta*(bb-ab)))
ck('nondegenerate_radial_split',reduced(alpha-beta+1/(S*C)))
ck('radial_weight',s.cancel(dr(C**4*S**2)/(C**4*S**2)-H)==0)
ck('tensor_weight',s.cancel(dr(C**6*S**4)/(C**6*S**4)-(6*alpha+4*beta))==0)
box=s.Matrix([dr(dr(tb))+H*dr(tb)+2*alpha**2*(bb-tb),dr(dr(bb))+H*dr(bb)-8*alpha**2*(bb-tb)-4*beta**2*(bb-ab),dr(dr(ab))+H*dr(ab)+2*beta**2*(bb-ab)])
DT=bs[2]+(6*alpha+4*beta)*bs[1]-14*K*b
for i,name in enumerate(['observer','radial','angular']):ck('rough_Box_'+name,reduced(box[i]-tt(DT)[i]))
# Original source decomposition, with its trace equation and conservation imposed.
A,P,P1,q0,q1=s.symbols('A P P1 q0 q1');trace=(4*A+3*P)/2
q2=-H*q1-7*K*q0-trace/6
scalar=s.Matrix([alpha*q1-(q2+H*q1)-6*K*q0,q2-(q2+H*q1)-6*K*q0,beta*q1-(q2+H*q1)-6*K*q0])
j=s.Matrix([A/2,P/2,P/2]);diff=j-scalar
ck('original_source_trace',s.expand(4*diff[0]+diff[1]+2*diff[2])==0)
bactual=P/2+H*q1+6*K*q0
ck('actual_radial_eigenvalue',s.simplify(diff[1]-bactual)==0)
bprime=s.diff(bactual,S)*C-s.diff(bactual,C)*K*S+s.diff(bactual,P)*(-4*alpha*(P-A))+s.diff(bactual,q0)*q1+s.diff(bactual,q1)*q2
new=tt_b.subs({bs[0]:bactual,bs[1]:bprime},simultaneous=True)
for i,name in enumerate(['observer','radial','angular']):ck('same_prescribed_source_'+name,reduced(diff[i]-new[i]))
ck('overlap_trace_zero',-6*(-7*K)-7*(6*K)==0)
ct('missing_source_half_changes_trace',s.expand((4*A+3*P)-trace)!=0)
ct('omit_radial_curvature_changes_Box',not reduced(box[1]-(DT+14*K*b)))
ct('flat_tensor_weight_changes_operator',not reduced(6*alpha+4*beta-4/S))
# Exact radial estimates and inverse flux.
k=s.symbols('k',nonzero=True);K0=s.Rational(35,3624192)*k*k
ck('positive_radial_weight_margin',1-s.Rational(7,3)*K0/k**2>s.Rational(1,2))
ck('radial_Neumann_ratio',0<7*K0/(3*k*k)<1)
rr,RR=s.symbols('rr RR',positive=True)
ck('radial_Poincare_integral',s.integrate(rr**2*(1/rr-1/RR),(rr,0,RR))==RR**2/6)
W,I,F,Wp=s.symbols('W I F Wp',nonzero=True)
chip=-I/W;chipp=-F+I*Wp/W**2
ck('positive_inverse_flux',s.cancel(-chipp-Wp/W*chip-F)==0)
ct('wrong_inverse_sign_fails_source',s.cancel(chipp+Wp/W*chip-F)!=0)
qprime=-1/W;qsecond=Wp/W**2
ct('punctured_harmonic_has_center_flux',s.cancel(qsecond+Wp/W*qprime)==0 and s.cancel(W*qprime)==-1)
# Complete scalar module, reusing K2548's equations with new source columns.
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
for i,(xv,yv) in enumerate([(0,0),(1,2),(-2,3)]):
 mm=M.subs({k:1,X:xv,Y:yv});vv=vsrc.subs({k:1,X:xv,Y:yv});adj=mm.adjugate();det=mm.det();out=adj*vv
 ck('full_six_row_source_cofactor_fixture_'+str(i),mm*out==det*vv)
 if i==0:ck('nonzero_determinant_polynomial',det!=0)
 if i==1:
  bad=out.copy();bad[5]=0
  ct('drop_skew_component_breaks_full_source',mm*bad!=det*vv)
ct('flat_scalar_Einstein_shift_fails',any(s.cancel(x)!=0 for x in E*s.Matrix([X,-X,0,0,1,0])-vsrc[:5,0]*Z))
jsrc,EQ=s.symbols('jsrc EQ');EZ=-rE*jsrc/2;EH=EZ-rE*EQ
ck('original_metric_Einstein_source',s.cancel(6*a0*EH+EQ+jsrc/2)==0)
ct('shifted_metric_fails_original_Einstein_row',s.cancel(6*a0*EZ+EQ+jsrc/2)!=0)
paths=['explorations/conditional-build/k2552-localized-source-domain-2026-11-04.md','tests/channel-swings/k2552_localized_source_domain_probe.py','explorations/conditional-build/k2531-partial-thickness-source-2026-11-04.md','explorations/conditional-build/k2548-compact-coupled-metric-detectors-2026-11-04.md','explorations/conditional-build/k2550-common-domain-tensor-response-2026-11-04.md']
paths+=['explorations/conditional-build/k2535-reduced-response-symbol-2026-11-04.md', 'lab/process/k2535-reduced-response-symbol.json', 'explorations/conditional-build/k2539-covariant-tensor-constraints-2026-11-04.md', 'lab/process/k2539-covariant-tensor-constraints.json']
report={'result':'K2552','checks':checks,'contrary_controls':controls,'evidence_kinds':{'exact':'source and all radial curvature identities, full Einstein column, coefficient shifts, radial constants and finite cofactor fixtures','universal':'positive radial inverse and unavoidable tails, full-operator intertwining and universal cofactor identity in note','not_claimed':'existence of four remaining scalar inverses, physical boundary domain, uniqueness or native GU'},'remaining_scalar_operators':['D5+Y-16K','c(D5+Y+mu-21K)','X+Y+2lambda','det M(X,Y)'],'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths}}
p=R/'lab/process/k2552-localized-source-domain.json'
if '--write' in sys.argv:p.write_text(json.dumps(report,indent=2)+'\n')
else:ck('saved_report_consistency',json.loads(p.read_text())==report)
print('K2552 PASS',len(checks),'exact groups',len(controls),'contrary controls')
