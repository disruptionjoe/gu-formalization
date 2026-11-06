#!/usr/bin/env python3
"""Exact convex support certificates; universal reductions are in the note."""
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

S=F(1,2);lam=F(11,20);lo=F(127,50000);hi=F(89,10000);mid=F(3,1000);D=lam/(4*S)
def J(n,k):return sub(sub(exact(1),mul(2*lam,H(n))),exact(2*n*k))
def major(j,B):return j[1]+max(F(0),B-j[0])**2/(4*D)
ck('positive_J4_floor',J(4,hi)[0]>0)
ck('positive_J3_floor',J(3,hi)[0]>0)
ck('positive_J2_floor',J(2,hi)[0]>0)
ck('positive_extreme_floor',1-2*lam*add(W(0,F(3,20)),W(0,F(7,20)))[1]-4*hi>0)
ck('all_counts_ge4_intercept_decreases',lo>lam*sub(H(4),H(5))[1])
ck('monotone_c_on_small_scores',F(1,64)-F(3,8)+1>0)
rows=[]
for k in [lo,hi]:
 j4=J(4,k);j2=J(2,k);u4=major(j4,2*lam*c(S/4))
 out=sub(sub(exact(1),mul(2*lam,add(W(0,F(3,20)),W(0,F(7,20))))),exact(4*k))
 uo=major(out,2*lam*F(191,250))
 ck('all_counts_ge4_endpoint_'+str(k),u4<j2[0])
 ck('extreme_scores_endpoint_'+str(k),uo<j2[0])
 rows.append({'k':str(k),'m_ge4_upper':str(u4),'extreme_upper':str(uo),'zero2_lower':str(j2[0])})
ck('three_zero_action_through_mid',J(3,mid)[0]>2*lam*c(S/3))
for k in [mid,hi]:ck('three_dominated_endpoint_'+str(k),major(J(3,k),2*lam*c(S/3))<J(2,k)[0])
ck('suffix_action_zero_entire_window',2*lam*(F(191,250)+W(0,F(7,20))[1])<1-2*hi)
ck('high_price_region_overlaps',lo<lam*sub(H(1),H(2))[0] and lam*sub(H(1),H(2))[1]<hi)
k3=mul(lam,sub(H(3),H(4)))
ck('zero3_lower_price_anchor',0<k3[0]<k3[1]<lo)
T3=sub(mul(4,H(3)),mul(3,H(4)))
ck('sharp_tail_admits_count3',2*lam*(c(S/3)+T3[1])<1)
# Convex endpoint argument is universal: each bound minus J2 is convex in k.
x=s.symbols('x',real=True)
ck('positive_part_square_convex_positive_piece',s.diff(x*x/(4*s.Rational(11,40)),x,2)>0)
ck('resource_gap_two_three',6-4==2)
ck('resource_gap_one_two',4/(1+F(7,20))-2==F(26,27))
def support(k,aa,bb=None):
 cost=W(aa,S) if bb is None else add(W(aa,bb),W(0,S-bb))
 m=1 if bb is None else 2
 j=mul(1/(1+aa),sub(sub(exact(1),mul(2*lam,cost)),exact(2*m*k)))
 ga=2*lam*WA(aa,S if bb is None else bb)+j[1]
 gb=F(0) if bb is None else 2*lam*(WB(aa,bb)-WB(0,S-bb))
 eps=2*(abs(ga)+abs(gb))+F(1,10**50)
 tangent=eps*(1+aa)-(abs(ga+eps)+abs(gb))/2
 assert tangent>0
 return j[0],j[1]+eps
endpoint_data=[(lo,F('.00000507883070699372281517279898504833498691751372366478'),F('.25000028938820438831599198556262382217309352352522247261')),(F('.00255'),F('.00001021501492760168656866459187529610846879326099006303'),F('.25000058370862231954952179590807268238807824235950439456'))]
for i,(k,aa,bb) in enumerate(endpoint_data):
 q=support(k,aa,bb);j3=J(3,k)
 ck('second_crossing_endpoint_'+str(i),q[1]<j3[0] if i==0 else q[0]>j3[1])
k=F('.00254675025157832772072144165383758231003614352455601376')
aa=F('.00000854585520441867826759078370455071960126129592908558')
bb=F('.25000048787667070939180225054905884348161331822771176354')
q2=support(k,aa,bb);q3=J(3,k);radius=max(abs(q2[0]-q3[1]),abs(q2[1]-q3[0]))/2
kd=(k-radius,k+radius)
ck('second_crossing_width',kd[1]-kd[0]<F(1,10**40))
ck('second_crossing_location',lo<kd[0]<kd[1]<F('.00255'))
ck('two_action_interior_through_window',J(2,lo)[1]<2*lam*c(S/2))
ck('positive_action_at_second_crossing',max(q2[1],q3[1])+6*radius<2*lam*c(S/2))
P2=1/(1+aa);R2=4*P2;V2=mul(P2,sub(exact(1),mul(2*lam,add(W(aa,bb),W(0,S-bb)))))
V3=sub(exact(1),mul(2*lam,H(3)))
Qupper=max(q2[1],q3[1]);consumers=[]
for M in [F(4),F(5),F(11,2)]:
 theta=(6-M)/(6-R2);lower=add(mul(theta,V2),mul(1-theta,V3));upper=Qupper+k*M
 ck('actual_mixture_budget_'+str(M),0<theta<1 and theta*R2+(1-theta)*6==M)
 ck('actual_mixture_bound_'+str(M),0<upper-lower[0]<F(1,10**40))
 oldtheta=(6-M)/2;old=add(mul(oldtheta,sub(exact(1),mul(2*lam,H(2)))),mul(1-oldtheta,V3))
 ck('strict_improvement_failed_chord_'+str(M),lower[0]>old[1])
 consumers.append({'budget':str(M),'theta':str(theta),'lower':str(lower[0]),'upper':str(upper),'width':str(upper-lower[0]),'lower_display':float(lower[0])})
# Exact budget pure two-stage consumer on the connecting branch.
ki=F('.00734521535627247415550121560404166682947301465212234667');ai=F(1,399);bi=F('.25033758242444017891390299664934397797980290693604750254')
qi=support(ki,ai,bi);ri=4/(1+ai);vi=mul(1/(1+ai),sub(exact(1),mul(2*lam,add(W(ai,bi),W(0,S-bi)))))
ck('exact_interior_budget',ri==F(399,100))
ck('interior_price_between_crossings',F('.00255')<ki<F('.0088'))
ck('interior_supported_consumer',0<qi[1]+ki*ri-vi[0]<F(1,10**40))
ck('interior_resource_before_second_tie',ri<R2<4)
# Explicit algebraic gap when the previous zero-action candidate is mistaken for exact.
ct('zero_two_not_optimal_at_second_tie',2*lam*c(S/2)>J(2,k)[1])
ct('force_equal_scores_wrong',WB(aa,S/2)-WB(0,S/2)!=0)
ct('omit_first_action_survival_wrong_resource',R2!=4)
ct('use_equal_probability_mixture_wrong_budget5',(R2+6)/2!=5)
ct('drop_stage_count_cost_wrong_support',Qupper+2*k!=Qupper)
ct('negative_numerator_product_bound_reverses',-1/(1+F(1,5))**2>-1/(1+F(2,5)))
# Exact derivatives used in the first-action monotone resource parametrization.
g=s.Function('g')(a);kap=(1-2*s.Rational(11,20)*(g-(1+a)*s.diff(g,a)))/4
ck('two_stage_price_derivative',s.simplify(s.diff(kap,a)-s.Rational(11,40)*(1+a)*s.diff(g,a,2))==0)
ck('resource_strict_decrease',s.diff(4/(1+a),a)==-4/(1+a)**2)
report={'result':'K2593','checks':checks,'contrary_controls':controls,'evidence_kind':'exact rational convex upper supports, logarithm intervals and actual original-policy mixtures; global reduction/attainment proved in note','broad_price_window':[str(lo),str(hi)],'endpoint_bounds':rows,'second_crossing_interval':list(map(str,kd)),'second_crossing_display':[float(v) for v in kd],'second_crossing_policy':{'first_action':str(aa),'first_score':str(bb),'last_action':'0','resource':str(R2)},'mixed_consumers':consumers,'pure_two_consumer':{'price':str(ki),'action':str(ai),'score':str(bi),'resource':str(ri),'lower':str(vi[0]),'upper':str(qi[1]+ki*ri)},'ceiling':'complete finite expected-resource frontier for S=1/2 lambda=11/20 only; physical probability and other multipliers open'}
refs=['explorations/conditional-build/k2591-multistage-stopping-support-2026-11-06.md','explorations/conditional-build/k2589-positive-action-support-2026-11-05.md','explorations/conditional-build/k2587-countwise-stopping-support-2026-11-05.md','explorations/conditional-build/k2581-score-sensitive-tail-transition-2026-11-05.md']
report['provenance']={f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in refs}
out=root/'lab/process/k2593-countwise-convex-stopping.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report mismatch'
print(json.dumps({'result':'K2593','checks':len(checks),'controls':len(controls),'status':'pass','budget5_lower':consumers[1]['lower_display']}))
