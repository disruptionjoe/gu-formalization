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
ck('action_derivative_at_zero',s.cancel(wa.subs(a,0)+2*(3-2*b)/((2-b)*(4-b)))==0)
ck('strict_c_bound_identity',s.expand(191*(2-b)*(4-b)-500*(3-2*b))==191*b*b-146*b+28)
ck('strict_c_bound_discriminant',146**2-4*191*28==-76)
S=F(1,2);lam=F(11,20);klo=F(11,1250);khi=F(89,10000);D=lam/(4*S);B=2*lam*F(16,21)
J3=sub(sub(exact(1),mul(2*lam,H(3))),exact(6*klo))
ck('all_counts_after_three_decrease',klo>lam*sub(H(3),H(4))[1])
ck('c_small_score_endpoint',c(F(1,6))<F(16,21))
cp=s.cancel(s.diff(2*(3-2*b)/((2-b)*(4-b)),b))
ck('c_small_score_derivative',s.cancel(cp-4*(b*b-3*b+1)/((b-4)**2*(b-2)**2))==0)
ck('c_small_score_polynomial_positive',F(1,16)-F(3,4)+1>0)
U3=J3[1]+max(F(0),B-J3[0])**2/(4*D)
ck('uniform_all_m_ge3_exclusion',U3<F(802,1000))
Hout=add(W(F(0),F(3,20)),W(F(0),F(7,20)))
Jo=sub(sub(exact(1),mul(2*lam,Hout)),exact(4*klo));Bo=2*lam*F(191,250)
Uo=Jo[1]+max(F(0),Bo-Jo[0])**2/(4*D)
ck('extreme_score_split_exclusion',Uo<F(812,1000))
suffix=2*lam*(F(191,250)+W(F(0),F(7,20))[1])
ck('last_action_zero_for_entire_price_window',suffix<1-2*khi)
floor=sub(sub(exact(1),mul(2*lam,H(1))),exact(2*khi))
ck('common_feasible_floor',floor[0]>F(4063,5000))
twofloor=sub(sub(exact(1),mul(2*lam,H(2))),exact(4*khi))
ck('two_stage_class_feasible_floor',twofloor[0]>F(4063,5000))
J2=sub(sub(exact(1),mul(2*lam,H(2))),exact(4*klo));A=F(1,3)
ck('large_action_majorant_decreases',Bo-J2[0]-2*D*A-D*A*A<0)
Ularge=(J2[1]+Bo*A-D*A*A)/(1+A)
ck('all_large_first_actions_excluded',Ularge<F(797,1000)<floor[0])
A7=F(1,7)
ck('released_action_cutoff_decreases',Bo-J2[0]-2*D*A7-D*A7*A7<0)
ck('released_resource_beyond_seven_halves',(J2[1]+Bo*A7-D*A7*A7)/(1+A7)<F(812,1000)<floor[0])

ck('resource_gap_for_crossing',4/(1+F(7,20))-2==F(26,27))
def support(k,aa,bb=None):
 cost=W(aa,S) if bb is None else add(W(aa,bb),W(F(0),S-bb))
 m=1 if bb is None else 2
 j=mul(1/(1+aa),sub(sub(exact(1),mul(2*lam,cost)),exact(2*m*k)))
 ga=2*lam*WA(aa,S if bb is None else bb)+j[1]
 gb=F(0) if bb is None else 2*lam*(WB(aa,bb)-WB(F(0),S-bb))
 eps=2*(abs(ga)+abs(gb))+F(1,10**40);upper=j[1]+eps
 tangent=eps*(1+aa)-(abs(ga+eps)+abs(gb))/2
 assert tangent>0
 return j[0],upper,tangent
endpoints=[(klo,F('.007821220993702630272600075848'),F('.003277974216066690213603726640'),F('.250517823503353603454183473228')),(khi,F('.007883968406223127224476241175'),F('.003331291940743367691429414869'),F('.250531559881635757304624324759'))]
endpoint_rows=[]
for i,(k,x,aa,bb) in enumerate(endpoints):
 q1=support(k,x);q2=support(k,aa,bb)
 ck('price_endpoint_'+str(i),q2[0]>q1[1] if i==0 else q1[0]>q2[1])
 endpoint_rows.append({'k':str(k),'one_bounds':list(map(str,q1[:2])),'two_bounds':list(map(str,q2[:2]))})
k=F('.008862098631999326756366633770');x=F('.007860184739077877095759650372');aa=F('.003311079593696313372893924722');bb=F('.250526333168434758520687944132')
q1=support(k,x);q2=support(k,aa,bb);Qupper=max(q1[1],q2[1]);Qlower=max(q1[0],q2[0]);diff=(q1[0]-q2[1],q1[1]-q2[0]);radius=max(abs(v) for v in diff)*F(27,26);kc=(k-radius,k+radius)
ck('critical_price_bracket_inside_window',klo<kc[0]<kc[1]<khi)
ck('critical_price_bracket_width',kc[1]-kc[0]<F(1,10**24))
ck('one_stage_action_positive_at_crossing',lam*(2*c(S)+2*H(1)[0])>1-2*kc[0])
ck('two_stage_action_positive_at_crossing',Qupper+4*radius<2*lam*c(S/2))
ck('two_stage_diagonal_boundary_not_optimal',Qlower>0)
# Exact original policies with the second action zero: equal survival, NOT equal scores.
p1=1/(1+x);p2=1/(1+aa);R1=2*p1;R2=4*p2
V1=mul(p1,sub(exact(1),mul(2*lam,W(x,S))))
V2=mul(p2,sub(exact(1),mul(2*lam,add(W(aa,bb),W(F(0),S-bb)))))
rows=[]
for M in [F(5,2),F(3),F(7,2)]:
 theta=(R2-M)/(R2-R1)
 ck('mixture_feasible_'+str(M),0<theta<1 and theta*R1+(1-theta)*R2==M)
 low=add(mul(theta,V1),mul(1-theta,V2));upper=Qupper+k*M
 ck('global_consumer_width_'+str(M),0<upper-low[0]<F(1,10**24))
 rows.append({'budget':str(M),'theta':str(theta),'feasible_value':list(map(str,low)),'global_upper':str(upper),'width':str(upper-low[0]),'display_lower':float(low[0]),'display_upper':float(upper)})
ct('zero_action_two_stage_is_not_optimal',2*lam*c(S/2)>(1-2*lam*H(2)[0]-4*k))
equaldiff=s.cancel(wb.subs(b,s.Rational(1,4))-wb.subs({a:0,b:s.Rational(1,4)}))
equalformula=-64*a*(128*a**3-2192*a**2+2824*a+5)/(105*(4*a-7)*(4*a+1)*(16*a*a-40*a-15))
ck('unequal_score_derivative_identity',s.cancel(equaldiff-equalformula)==0)
ck('unequal_score_cubic_bound',2824-2192*s.Rational(1,4)>0)
ck('unequal_score_denominator_signs',4*s.Rational(1,4)-7<0 and 16*s.Rational(1,4)-40<0)
ct('equal_score_shortcut_has_nonzero_score_derivative',WB(aa,S/2)-WB(F(0),S/2)!=0)
ct('omit_failed_trial_cost_changes_resource',R2!=2*p2)
ct('unit_survival_changes_resource',R2!=4)
ct('wrong_mixture_weight_misses_budget3',F(1,2)*R1+F(1,2)*R2!=3)
ct('negative_numerator_wrong_product_sign',-1/((1+F(1,5))**2)>-1/(1+F(2,5)))
ct('omit_suffix_score_restriction_fails',lam*(2*c(S)+2*H(1)[0])>1-2*k)
# Independent finite exact nonlinear example confirms tangent direction; not the convexity proof.
rat=F(1,100);test=support(k,x)
jtest=mul(1/(1+rat),sub(sub(exact(1),mul(2*lam,W(rat,S))),exact(2*k)))
ck('independent_one_stage_support_consumer',jtest[1]<test[1])
report={'result':'K2591','checks':checks,'contrary_controls':controls,'evidence_kind':'exact rational supporting planes, derivative identities and original-policy mixtures; universal reductions and exact crossing theorem in note','uniform_exclusion_bounds':{'m_ge3':str(U3),'extreme_scores':str(Uo),'large_action':str(Ularge),'feasible_floor':str(floor[0])},'endpoint_supports':endpoint_rows,'critical_price_interval':list(map(str,kc)),'critical_price_display':[float(v) for v in kc],'critical_price_test':str(k),'support_bounds':{'one':list(map(str,q1[:2])),'two':list(map(str,q2[:2]))},'rational_policy':{'one_action':str(x),'two_first_action':str(aa),'two_first_score':str(bb),'two_last_action':'0','resources':[str(R1),str(R2)]},'consumers':rows,'ceiling':'exact implicit mixed segment at S=.5 lambda=.55; other price windows and multipliers open'}
refs=['explorations/conditional-build/k2589-positive-action-support-2026-11-05.md','explorations/conditional-build/k2587-countwise-stopping-support-2026-11-05.md','explorations/conditional-build/k2581-score-sensitive-tail-transition-2026-11-05.md']
report['provenance']={f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in refs}
out=root/'lab/process/k2591-multistage-stopping-support.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report mismatch'
print(json.dumps({'result':'K2591','checks':len(checks),'controls':len(controls),'status':'pass','budget3_lower':rows[1]['display_lower']}))
