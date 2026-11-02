"""K2517 exact original-law asymptotic and finite witness checks.
Default verifies saved report. Universal bounds are proved in the note.
"""
from pathlib import Path
import hashlib,json,sys
import sympy as s
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not checks[k]:raise AssertionError(k)
def ct(k,v):
 controls[k]=bool(v)
 if not controls[k]:raise AssertionError(k)
r,b,S,lam,x=s.symbols('r b S lam x',positive=True)
alpha=(1-r)**2/(4*(1+r));beta=(1+r)/2;g=2*alpha;q=alpha*beta-alpha**2/2;t=alpha*beta**2-alpha**2*beta+alpha**3/3
f=r+lam*g;w=s.log(1+(b-r*b)**2/(2*(b+r*b)*(2-b-r*b)))
series=s.series(w,b,0,4).removeO()
for n,co in [(1,alpha),(2,q),(3,t)]:ck('original_log_coefficient_'+str(n),s.factor(series.coeff(b,n)-co)==0)
ck('g_second_derivative',s.factor(s.diff(g,r,2)-4/(1+r)**3)==0)
ck('g_prime_formula',s.factor(s.diff(g,r)-(r*r+2*r-3)/(2*(1+r)**2))==0)
ck('q_nonnegative_factor',s.factor(q-(1-r)**2*(3*r+1)*(r+3)/(32*(r+1)**2))==0)
ck('q_upper_identity',s.factor(alpha*beta-(1-r)**2/8)==0)
ck('log_error_constants',s.Rational(1,3)+s.Rational(1,9)+s.Rational(1,81)==s.Rational(37,81)<s.Rational(1,2))
ck('q_derivative_bound_constants',s.Rational(3,4)+s.Rational(1,8)+s.Rational(3,16)==s.Rational(17,16))
ck('cost_remainder_constants',s.Rational(1,2)+s.Rational(1,4)+1==s.Rational(7,4))
ck('L_constants',2+s.Rational(17,8)==s.Rational(33,8))
LR=2*(1+r)**2/((1-r)*(r+3));AA=(3*r+1)/(r+3)
ck('stationarity_ratio',s.factor(s.diff(f,r).subs(lam,LR))==0)
ck('minimum_value',s.factor(f.subs(lam,LR)-AA)==0)
ck('lambda_ratio_increasing',s.factor(s.diff(LR,r)-16*(r+1)/((r-1)**2*(r+3)**2))==0)
H=(3*r+1)*(r*r+6*r-3)/(8*(r+3));Bone=(3*r+1)*(r*r+10*r-3)/(8*(r+3))
ck('one_stage_quadratic',s.factor((r*r+lam*g*r-2*lam*q).subs(lam,LR)-Bone)==0)
ck('partition_H',s.factor((r*r/2+lam*g*r/2-2*lam*q).subs(lam,LR)-H)==0)
ck('Bone_decomposition',s.factor(Bone-r*AA/2-H)==0)
# Three independent ratios retain the true ordered prefix cost.
r1,r2,r3,b1,b2,b3=s.symbols('r1 r2 r3 b1 b2 b3',nonnegative=True)
rs=[r1,r2,r3];bs=[b1,b2,b3];acts=[rs[i]*bs[i] for i in range(3)]
pref=s.Integer(1);cost=0
for ri,bi,ai in zip(rs,bs,acts):
 pref=s.series(pref/(1+ai*S),S,0,3).removeO().expand()
 wi=alpha.subs(r,ri)*bi*S+q.subs(r,ri)*bi*bi*S*S
 cost+=s.series(pref*wi,S,0,3).removeO()
value=s.expand(pref-2*lam*cost)
Q=sum(acts)**2/2+sum(a*a for a in acts)/2+lam*sum(g.subs(r,rs[i])*bs[i]*sum(acts[:i+1]) for i in range(3))-2*lam*sum(q.subs(r,rs[i])*bs[i]**2 for i in range(3))
ck('three_stage_original_quadratic',s.factor(value.coeff(S,2)-Q)==0)
ck('three_stage_original_linear',s.factor(value.coeff(S,1)+sum(bs[i]*f.subs(r,rs[i]) for i in range(3)))==0)
ck('common_ratio_partition_identity',s.factor(Q.subs({r1:r,r2:r,r3:r,lam:LR})-(r*AA*(b1+b2+b3)**2/2+H*(b1*b1+b2*b2+b3*b3)))==0)
L,T=s.symbols('L T',positive=True)
ck('Young_completion',s.expand(L*S*T-lam*T*T/(4*S)-(L*L*S**3/lam-lam/(4*S)*(T-2*L*S*S/lam)**2))==0)
rt=2*s.sqrt(3)-3;lt=4*s.sqrt(3)/3
ck('transition_root',s.simplify(rt*rt+6*rt-3)==0)
ck('transition_multiplier',s.simplify(LR.subs(r,rt)-lt)==0)
rv=s.Rational(5,11);lv=s.Rational(128,57);score=s.Rational(1,100000)
ck('finite_witness_ratio',LR.subs(r,rv)==lv)
ck('finite_witness_A',AA.subs(r,rv)==s.Rational(13,19))
ck('finite_witness_H',H.subs(r,rv)==-s.Rational(13,2299))
D=-H.subs(r,rv)/2;R0=1+7*lv/4;LL=2+33*lv/8;RR=2*R0+LL*LL/lv
ck('finite_witness_D',D==s.Rational(13,4598))
ck('finite_witness_R0',R0==s.Rational(281,57))
ck('finite_witness_L',LL==s.Rational(214,19))
ck('finite_witness_combined_error',RR==s.Rational(121025,1824))
gap=D*score*score-RR*score**3
ck('finite_exact_gap',gap==s.Rational(1910239,8828160000000000000)>0)
ck('original_two_stage_actions',rv*score/2==s.Rational(1,440000) and score/2==s.Rational(1,200000))
ck('score_within_uniform_range',0<score<s.Rational(1,4) and score<D/RR)
# Cubic equality: derive ordered costs independently from truncated products.
y=1-x;ps1=s.series(1/(1+r*x*S),S,0,4).removeO();ps2=s.series(1/((1+r*x*S)*(1+r*y*S)),S,0,4).removeO()
w1=alpha*x*S+q*x*x*S*S+t*x**3*S**3;w2=alpha*y*S+q*y*y*S*S+t*y**3*S**3
cubic2=s.expand(ps2-2*lam*(ps1*w1+ps2*w2)).coeff(S,3)
C2=-r**3*(1-2*x*y)-2*lam*(t*(1-3*x*y)-r*q*(x**3+y**2)+alpha*r*r*(1-2*x*y))
C1=-r**3-2*lam*(t-r*q+r*r*alpha)
ck('ordered_cubic_two_stage',s.factor(cubic2-C2)==0)
BoneRaw=r*r+lam*g*r-2*lam*q;Bp=s.diff(BoneRaw,r);F2=s.diff(f,r,2)
Bpstar=s.simplify(Bp.subs({r:rt,lam:lt}));Fstar=s.simplify(F2.subs({r:rt,lam:lt}));Astar=s.simplify(AA.subs(r,rt))
ck('equality_Bprime',s.simplify(Bpstar-(s.Rational(1,4)+7*s.sqrt(3)/12))==0)
ck('equality_strong_curvature',s.simplify(Fstar-(s.Rational(3,2)+5*s.sqrt(3)/6))==0)
Q2=Q.subs({b1:x,b2:y,b3:0})
d1=s.factor(s.diff(Q2,r1).subs({r1:r,r2:r,r3:r,lam:LR}));d2=s.factor(s.diff(Q2,r2).subs({r1:r,r2:r,r3:r,lam:LR}))
ck('first_ratio_gradient',s.factor(d1-x*(x*Bp.subs(lam,LR)+y*AA))==0)
ck('second_ratio_gradient',s.factor(d2-y*y*Bp.subs(lam,LR))==0)
raw=s.simplify((C2-C1).subs({r:rt,lam:lt}));gain=(x*(x*Bpstar+y*Astar)**2+y**3*Bpstar**2-Bpstar**2)/(2*Fstar)
c0=(13185-7619*s.sqrt(3))/48;c1=(2841-1643*s.sqrt(3))/48
ck('optimized_cubic_difference',s.simplify(s.expand(raw+gain-x*y*(c0*y+c1*x)))==0)
ck('cubic_sign_certificate_0',3*7619**2-13185**2==303258>0)
ck('cubic_sign_certificate_1',3*1643**2-2841**2==27066>0)
ct('above_transition_fixed_ratio_not_instability',H.subs(r,s.Rational(3,5))>0)
ct('below_transition_actual_improvement',H.subs(r,rv)<0 and gap>0)
ct('same_intercept_barrier_not_actual_threshold',s.Rational(18,7)>lt)
ct('equality_quadratic_silent',s.simplify(H.subs(r,rt))==0 and c0<0 and c1<0)
ct('cubic_split_not_uniform_at_boundary',s.simplify((x*y*(c0*y+c1*x)).subs(x,0))==0)
# Wrong prefix cost changes even the first nontrivial composed coefficient.
wrongQ=sum(acts)**2/2+sum(a*a for a in acts)/2-2*lam*sum(q.subs(r,rs[i])*bs[i]**2 for i in range(3))
ct('unweighted_cost_detected',s.factor((Q-wrongQ).subs({r1:s.Rational(1,2),r2:s.Rational(1,3),r3:0,b1:s.Rational(1,5),b2:s.Rational(1,7),b3:0,lam:3}))>0)
ct('omit_optimization_error_invalid_witness_bound',RR>2*R0)
ct('large_score_not_licensed_by_asymptotic',D*s.Rational(1,2)**2-RR*s.Rational(1,2)**3<0)
ct('equal_ratio_is_not_arbitrary_policy',s.factor(s.diff(f,r).subs({r:s.Rational(1,2),lam:lv}))!=0)
paths=['explorations/conditional-build/k2517-small-score-stopping-transition-2026-11-02.md','tests/channel-swings/k2517_small_score_stopping_transition_probe.py','explorations/conditional-build/k2515-stopping-transition-certificate-2026-11-02.md','explorations/conditional-build/k2485-constrained-stopping-frontier-2026-11-01.md','explorations/conditional-build/k2483-adaptive-stopping-bellman-2026-11-01.md']
report={'result':'K2517','scope':'exact identities and finite original-law witness; uniform universal proof in note','checks':checks,'contrary_controls':controls,'threshold':str(lt),'finite_witness':{'lambda':str(lv),'score':str(score),'a_each':'1/440000','b_each':'1/200000','guaranteed_gap':str(gap)},'equality_cubic':{'c0':str(c0),'c1':str(c1)},'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in paths}}
p=R/'lab/process/k2517-small-score-stopping-transition.json'
if '--write' in sys.argv:p.write_text(json.dumps(report,indent=2)+'\n')
else:ck('saved_report_consistency',json.loads(p.read_text())==report)
print('K2517 PASS',len(checks),'checks',len(controls),'contrary controls')
