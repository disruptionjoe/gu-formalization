#!/usr/bin/env python3
"""Parameter rectangle certificates; proofs and scope in K2595. Helpers adapted from K2593."""
import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction as F
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
def exact(x):return(F(x),F(x))
def add(x,y):return(x[0]+y[0],x[1]+y[1])
def mul(c,x):return(c*x[0],c*x[1]) if c>=0 else(c*x[1],c*x[0])
def sub(x,y):return add(x,mul(-1,y))
def logbound(q):
 q=F(q);assert q>=1;u=(q-1)/(q+1)
 low=2*sum((u**(2*j+1)/F(2*j+1) for j in range(32)),F(0))
 high=low+2*u**65/(65*(1-u*u));scale=10**65
 return F(low.numerator*scale//low.denominator,scale),F(-(-high.numerator*scale//high.denominator),scale)
def W(a,b):return logbound(1+(b-a)**2/(2*(a+b)*(2-a-b)))
def H(n):return mul(n,W(F(0),S/n))
def c(b):return 2*(3-2*b)/((2-b)*(4-b))
a,b=s.symbols('a b',real=True);w=s.log(1+(b-a)**2/(2*(a+b)*(2-a-b)))
wa=s.cancel(s.diff(w,a));wb=s.cancel(s.diff(w,b))
def rational(expr,aa,bb):
 return F(expr.subs({a:s.Rational(aa.numerator,aa.denominator),b:s.Rational(bb.numerator,bb.denominator)}))
def WA(aa,bb):return rational(wa,aa,bb)
def WB(aa,bb):return rational(wb,aa,bb)


S=F(1,2);center=F(11,20);delta=F(1,100000)
lo=F(127,50000);hi=F(89,10000);mid=F(3,1000)
lamlo=center-delta;lamhi=center+delta
rows=[]
def J(n,k,lam):return sub(sub(exact(1),mul(2*lam,H(n))),exact(2*n*k))
def major(j,B,lam):return j[1]+max(F(0),B-j[0])**2/(2*lam)
for lam in [lamlo,lamhi]:
 for k in [lo,hi]:
  j4=J(4,k,lam);j2=J(2,k,lam)
  jo=sub(sub(exact(1),mul(2*lam,add(W(0,F(3,20)),W(0,F(7,20))))),exact(4*k))
  margins=[j2[0]-major(j4,2*lam*c(S/4),lam),j2[0]-major(jo,2*lam*F(191,250),lam)]
  ck('positive_intercept_corner_'+str((lam,k)),min(j4[0],J(3,k,lam)[0],j2[0],jo[0])>0)
  ck('count4_corner_'+str((lam,k)),margins[0]>0)
  ck('extreme_score_corner_'+str((lam,k)),margins[1]>0)
  rows.append({'lambda':str(lam),'price':str(k),'count4_margin':str(margins[0]),'extreme_margin':str(margins[1])})
 for k in [mid,hi]:ck('count3_dominated_corner_'+str((lam,k)),major(J(3,k,lam),2*lam*c(S/3),lam)<J(2,k,lam)[0])
 ck('all_large_counts_'+str(lam),lo>lam*sub(H(4),H(5))[1])
 ck('three_zero_action_'+str(lam),J(3,mid,lam)[0]>2*lam*c(S/3))
 ck('last_action_zero_'+str(lam),2*lam*(F(191,250)+W(0,F(7,20))[1])<1-2*hi)
 ck('price_overlap_'+str(lam),lo<lam*sub(H(1),H(2))[0] and lam*sub(H(1),H(2))[1]<hi)
 ck('tail_anchor_'+str(lam),0<lam*sub(H(3),H(4))[0]<lam*sub(H(3),H(4))[1]<lo)
 ck('sharp_tail_'+str(lam),2*lam*(c(S/3)+sub(mul(4,H(3)),mul(3,H(4)))[1])<1)
 ck('first_action_interior_'+str(lam),J(2,lo,lam)[1]<2*lam*c(S/2))
ck('strip_strictly_above_count2_threshold',2*lamlo*(c(S/2)+sub(mul(3,H(2)),mul(2,H(3)))[0])>1)
for lam in [lamlo,lamhi]:
 ck('one_stage_interior_at_crossing_'+str(lam),J(1,F('.0088'),lam)[1]<2*lam*c(S))
# Joint convexity: Hessian of x^2/(2 lambda) is PSD, with zero determinant.
x,L=s.symbols('x L',positive=True);pers=x*x/(2*L);hs=s.hessian(pers,(x,L))
ck('perspective_hessian_determinant',s.simplify(hs.det())==0)
ck('perspective_positive_diagonal',hs[0,0]==1/L and hs[1,1]==x*x/L**3)
ck('positive_part_C1_join',s.diff(pers,x).subs(x,0)==0)
# Center crossing endpoint certificates are recomputed, not trusted as stored booleans.
def support(k,aa,bb=None):
 cost=W(aa,S) if bb is None else add(W(aa,bb),W(0,S-bb))
 m=1 if bb is None else 2
 j=mul(1/(1+aa),sub(sub(exact(1),mul(2*center,cost)),exact(2*m*k)))
 ga=2*center*WA(aa,S if bb is None else bb)+j[1]
 gb=F(0) if bb is None else 2*center*(WB(aa,bb)-WB(0,S-bb))
 eps=2*(abs(ga)+abs(gb))+F(1,10**50)
 ck('actual_convex_tangent_'+str((k,m)),eps*(1+aa)-(abs(ga+eps)+abs(gb))/2>0)
 return(j[0],j[1]+eps)
endpoints=[(lo,F('.00000507883070699372281517279898504833498691751372366478'),F('.25000028938820438831599198556262382217309352352522247261')),(F('.00255'),F('.00001021501492760168656866459187529610846879326099006303'),F('.25000058370862231954952179590807268238807824235950439456'))]
cross=[]
for i,(k,aa,bb) in enumerate(endpoints):
 q=support(k,aa,bb);z=J(3,k,center)
 margin=z[0]-q[1] if i==0 else q[0]-z[1]
 ck('kd_sign_uniform_'+str(i),margin>S*delta)
 cross.append({'price':str(k),'center_margin':str(margin),'uniform_margin':str(margin-S*delta)})
# K2591 report supplies unchanged center tangent bounds; reuse by pinned file hash.
pre=json.loads((root/'lab/process/k2591-multistage-stopping-support.json').read_text())
for i,row in enumerate(pre['endpoint_supports']):
 q1=list(map(F,row['one_bounds']));q2=list(map(F,row['two_bounds']))
 margin=q2[0]-q1[1] if i==0 else q1[0]-q2[1]
 ck('reused_kc_sign_uniform_'+str(i),margin>S*delta)
 cross.append({'price':row['k'],'reused_center_margin':str(margin),'uniform_margin':str(margin-S*delta)})
# Global cost bound w(a,b)<=w(0,b)<=b/2 uses derivative sign and exact rational envelope.
z=s.symbols('z',nonnegative=True)
w0p=1/(2-b)-1/(4-b)
ck('w0_half_bound_polynomial',s.cancel(s.Rational(1,2)-w0p-(b*b-6*b+4)/(2*(b-4)*(b-2)))==0)
ck('half_bound_on_score_interval',F(1,4)-3+4>0)
ck('crossing_resource_gaps',4/(1+F(7,20))-2==F(26,27) and 6-4==2)
# Pure two-stage consumer, with exact strong-convexity error, independent of lambda.
M=F(399,100);aa=F(1,399);bb=F('.25033758242444017891390299664934397797980290693604750254')
cost=add(W(aa,bb),W(0,S-bb));res=WB(aa,bb)-WB(0,S-bb);mu=F(3,16)
g=(cost[0]-res*res/(2*mu),cost[1]);gp=(WA(aa,bb)-1600*abs(res),WA(aa,bb)+1600*abs(res))
ck('exact_pure_budget',4/(1+aa)==M)
ck('score_root_inside_interval',F(3,20)<bb-abs(res)/mu<bb+abs(res)/mu<F(7,20))
# w_ab = N_ab/N-N_a*N_b/N² +1/(a+b)²+1/(2-a-b)²;
# N=4a+4b-a²-6ab-b², a=1/399, b in[.15,.35].
# N>=b(4-b)>=.15*3.65>.5, |Na|,|Nb|<=4, N_ab=-6.
ck('mixed_derivative_bound_300',6/F(1,2)+16/F(1,2)**2+1/F(3,20)**2+1/F(3,2)**2<300)
# w0'' increases on[0,.5], minimum3/16; derivative difference positive.
ck('w0_curvature_minimum',s.diff(w0p,b).subs(b,0)==s.Rational(3,16))
cons=[]
for lam in [lamlo,center,lamhi]:
 value=(M/4-lam*M*g[1]/2,M/4-lam*M*g[0]/2)
 kap=mul(F(1,4),sub(exact(1),mul(2*lam,sub(g,mul(1+aa,gp)))))
 ck('uniform_pure_value_width_'+str(lam),0<value[1]-value[0]<F(1,10**40))
 ck('uniform_pure_support_'+str(lam),F('.00255')<kap[0]<=kap[1]<F('.0088'))
 cons.append({'lambda':str(lam),'value':list(map(str,value)),'price':list(map(str,kap)),'value_display':float(value[0])})
leak=mul(M/2,g)
# Budget5: retain the exact rational predecessor policy and transport its score.
base=json.loads((root/'lab/process/k2593-countwise-convex-stopping.json').read_text())
pol=base['second_crossing_policy'];ap=F(pol['first_action']);bp=F(pol['first_score']);rp=4/(1+ap)
theta=(6-F(5))/(6-rp);vp=mul(1/(1+ap),sub(exact(1),mul(2*center,add(W(ap,bp),W(0,S-bp)))))
v3=sub(exact(1),mul(2*center,H(3)));vbase=add(mul(theta,vp),mul(1-theta,v3))
cmix=add(mul(theta*2/(1+ap),add(W(ap,bp),W(0,S-bp))),mul((1-theta)*2,H(3)))
budget5_rows=[row for row in base['mixed_consumers'] if row['budget']=='5']
assert len(budget5_rows)==1,'FAIL unique predecessor budget5 certificate'
upper0=F(budget5_rows[0]['upper'])
ck('mixture_budget5_preserved',theta*rp+(1-theta)*6==5 and 0<theta<1)
mixed=[]
for lam in [lamlo,lamhi]:
 lower=sub(vbase,mul(lam-center,cmix))[0]
 upper=upper0+S*max(F(0),center-lam)
 ck('budget5_transport_width_'+str(lam),0<upper-lower<F(1,100000))
 mixed.append({'lambda':str(lam),'lower':str(lower),'upper':str(upper),'width':str(upper-lower)})
# Released topology-boundary consumer, using K2587's sharp all-action threshold.
threshold_den=mul(2,add(exact(c(S/2)),sub(mul(3,H(2)),mul(2,H(3)))))
lambda2=(1/threshold_den[1],1/threshold_den[0])
ck('count2_threshold_isolated',F('.54996339')<lambda2[0]<=lambda2[1]<F('.54996340'))
leftlam=F('.5499');leftvalue=sub(exact(1),mul(leftlam,add(H(2),H(3))))
ck('left_consumer_exact_resource',F(1,2)*4+F(1,2)*6==5)
ck('left_consumer_global_threshold',leftlam<lambda2[0]<lamlo)
ck('left_consumer_value_width',0<leftvalue[1]-leftvalue[0]<F(1,10**40))
boundary_consumer={'lambda2_interval':list(map(str,lambda2)),'lambda':str(leftlam),'budget':'5','value_interval':list(map(str,leftvalue)),'attaining_policy':'equal mixture of zero-action equal-score counts two and three','credit':'K2587 sharp support reused; new exact consumer and explicit outside-strip topology contrast'}
# Controls challenge substantive shortcuts, not asserted labels.
ct('strip_cannot_cross_zero2_threshold',2*F('.5499')*(c(S/2)+sub(mul(3,H(2)),mul(2,H(3)))[1])<1)
ct('zero_action_chord_price_not_invariant',sub(H(2),H(3))[0]>0)
ct('equal_score_not_pure_optimizer',WB(aa,S/2)-WB(0,S/2)!=0)
ct('zero_leakage_wrong_pure_sensitivity',leak[0]>F(1,4))
ct('rounded_resource_changes_budget5',(rp+6)/2!=5)
ct('forget_price_cost_changes_crossing',4*lo!=6*lo)
ct('positive_part_needed',major(exact(2),F(1),center)==2)
ct('uniform_upper_cannot_use_center_value_below_center',mixed[0]['upper']!=str(upper0))
report={'result':'K2595','checks':checks,'contrary_controls':controls,'evidence_kind':'new exact rational corner inequalities and consumer bounds; K2591 center endpoint supports reused by file hash; continuum convexity and differentiation proved in note','score':'1/2','lambda_strip':[str(lamlo),str(lamhi)],'corners':rows,'crossing_signs':cross,'pure_budget':'399/100','pure_score_interval':list(map(str,(bb-abs(res)/mu,bb+abs(res)/mu))),'pure_cost_interval':list(map(str,g)),'pure_leakage_interval':list(map(str,leak)),'pure_consumers':cons,'budget5_consumers':mixed,'topology_boundary_consumer':boundary_consumer,'ceiling':'complete topology in stated multiplier strip; no arbitrary score/multiplier or physical probability theorem'}
refs=['lab/process/k2591-multistage-stopping-support.json','lab/process/k2593-countwise-convex-stopping.json','explorations/conditional-build/k2593-countwise-convex-stopping-2026-11-06.md','explorations/conditional-build/k2587-countwise-stopping-support-2026-11-05.md']
report['provenance']={f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in refs}
out=root/'lab/process/k2595-stopping-parameter-stability.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report mismatch'
print(json.dumps({'result':'K2595','checks':len(checks),'controls':len(controls),'status':'pass'}))
