"""Contraction identities and independent original-channel attainment replay."""
from pathlib import Path
import contextlib,io,json,hashlib,sys
import sympy as s
R=Path(__file__).resolve().parents[2]
p=R/'tests/channel-swings/k2410_variable_loss_recovery_probe.py'
# Execute unchanged original CP/TP and complete-channel checks; never write its report.
ns={'__file__':str(p),'__name__':'k2410_inherited'}
args=sys.argv;sys.argv=[str(p),'--verify-only']
with contextlib.redirect_stdout(io.StringIO()):exec(compile(p.read_text(),str(p),'exec'),ns)
sys.argv=args
checks={};controls={}
def ck(name,ok):
 checks[name]=bool(ok)
 if not ok:raise AssertionError(name)
def ctrl(name,ok):
 controls[name]=bool(ok)
 if not ok:raise AssertionError(name)
Q=s.Rational
u,v,z,h,tx,tz,mx,mz,w=s.symbols('u v z h tx tz mx mz w',real=True)
G=s.Matrix([[u,v],[z,h]]);J=s.Matrix([[0,1],[-1,0]]);P=(G+J*G*J.T)/2
ck('conformal_projection',P==s.Matrix([[(u+h)/2,(v-z)/2],[(z-v)/2,(u+h)/2]]))
a=(u+h)/2;b=(v-z)/2
ck('conformal_norm_identity',s.simplify(P.T*P-(a*a+b*b)*s.eye(2))==s.zeros(2))
t=s.Matrix([tx,tz]);m=s.Matrix([mx,mz]);n2=m.dot(m)
C=s.eye(2)-(1-w)*G-w*t*m.T
A=2*m/(w*n2);B=(1-w)*A;c=A-P*B
L2=s.trace(C)**2+(C[0,1]-C[1,0])**2
ck('unrestricted_center_polynomial_identity',s.factor(L2-w*w*n2*((t-c).dot(t-c)))==0)
wrong=A-P.T*B
ctrl('transpose_rotation_breaks_identity',s.factor(L2-w*w*n2*((t-wrong).dot(t-wrong)))!=0)
ctrl('omit_conformal_skew_breaks_identity',s.factor(L2-w*w*n2*((t-A+a*B).dot(t-A+a*B)))!=0)
alpha=ns['al'];q=[alpha[1]/sum(alpha),alpha[0]/sum(alpha)];k=alpha[0]*alpha[1]/sum(alpha)
ck('exact_fixture_alphas',alpha==[Q(365,520),Q(259,520)])
ck('positive_balancing_weights',q==ns['p'] and q[0]*alpha[0]==q[1]*alpha[1]==k)
AA=ns['avec'];BB=ns['bvec'];aa=AA.dot(AA);bb=BB.dot(BB)
ck('positive_norm_gap',aa>bb>0)
ck('original_norm_squares',aa==Q(75168976896,1787373245) and bb==Q(741956311296,223421655625))
hcoef=sum(qi*(1-wi) for qi,wi in zip(q,ns['weights']))
ck('strict_attenuation_penalty',hcoef>0 and k>0 and bb>0)
# Analytic lower interval assembled independently from the balancing expression.
lo=(sum(qi*wi for qi,wi in zip(q,ns['weights']))+k*(ns['an'][0]-ns['bn'][1]))/4
hi=(sum(qi*wi for qi,wi in zip(q,ns['weights']))+k*(ns['an'][1]-ns['bn'][0]))/4
ck('global_value_interval',Q(5194114591,10**10)<lo<hi<Q(5194114592,10**10))
ck('same_attaining_value',s.simplify((ns['weights'][0]*alpha[1]+ns['weights'][1]*alpha[0]+alpha[0]*alpha[1]*(s.sqrt(aa)-s.sqrt(bb)))/(4*sum(alpha))-(sum(qi*wi for qi,wi in zip(q,ns['weights']))+k*(s.sqrt(aa)-s.sqrt(bb)))/4)==0)
# Universal singular-value polynomial for G=P+S, S symmetric trace-free.
aa0,bb0,cc0,dd0,lam=s.symbols('a b c d lam',real=True)
M=s.Matrix([[aa0+cc0,bb0+dd0],[-bb0+dd0,aa0-cc0]])
r2=aa0**2+bb0**2;s2=cc0**2+dd0**2
ck('anisotropy_singular_value_polynomial',s.expand((lam*s.eye(2)-M.T*M).det()-(lam**2-2*(r2+s2)*lam+(r2-s2)**2))==0)
ctrl('unphysical_expansion_breaks_distance_bound', (s.Matrix([3,0])-2*s.Matrix([1,0])).dot(s.Matrix([3,0])-2*s.Matrix([1,0])) < (3-1)**2 and (2*s.eye(2)).norm(2)>1)
# Rational upper bound on rounded controller; compare original squared radii.
upper=Q(519411461,10**9)
for i,wi in enumerate(ns['weights']):
 rad2=(4*ns['E0']-wi)**2-ns['gaps'][i]
 ck('rounded_controller_upper_'+str(i),4*upper-wi>0 and (4*upper-wi)**2>rad2)
ck('rounded_controller_within_two_billionths',upper-lo<Q(2,10**9))
report={'result_id':'K2413','checks':checks,'controls':controls,'inherited_checks':len(ns['checks']),'inherited_controls':len(ns['controls']),'optimum_interval':['5194114591/10000000000','5194114592/10000000000'],'rounded_optimality_gap_upper':'1/500000000','scope':'Universal analytic contraction lower bound plus exact original-channel attainment. No empirical or GU credit.'}
deps=['tests/channel-swings/k2410_variable_loss_recovery_probe.py','explorations/conditional-build/k2410-variable-loss-recovery-2026-10-31.md','lab/process/k2410-variable-loss-recovery.json']
report['dependencies']={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps}
out=R/'lab/process/k2413-joint-recovery-optimum.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
elif '--verify-only' not in sys.argv:assert json.loads(out.read_text())==report
print(json.dumps(report,sort_keys=True))
