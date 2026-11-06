#!/usr/bin/env python3
"""K2599 joint corner identities and independent global certificates at score49/100."""
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
S=F(49,100);lmin=F('.5385');lmax=F('.5395');klo=F('.00825');khi=F('.0084');blo=F('.15');bhi=F('.34')
Bsym=s.symbols('B',positive=True);cs=2*(3-2*Bsym)/((2-Bsym)*(4-Bsym))
gap=s.factor(cs-cs.subs(Bsym,Bsym/2));gapform=2*Bsym*(1-2*Bsym)/((2-Bsym)*(4-Bsym)*(8-Bsym))
ck('exact_score_gap',s.cancel(gap-gapform)==0)
ck('corner_gap_slope',s.diff(gap,Bsym).subs(Bsym,s.Rational(1,2))==-s.Rational(16,315))
h1=s.factor(s.diff(w,a,2).subs({a:0,b:Bsym}));h2=s.factor((s.diff(w,a,2)-s.diff(w,a,b)**2/(2*s.diff(w,b,2))).subs({a:0,b:Bsym/2}))
ck('corner_hessian_one',h1.subs(Bsym,s.Rational(1,2))==s.Rational(1312,441))
ck('corner_hessian_two_Schur',h2.subs(Bsym,s.Rational(1,2))==s.Rational(171736,24255))
# Exact activation transversality derived from the envelope resources/costs.
A,G,HH,C,Lam=s.symbols('A G HH C Lam',positive=True);R1=2/(1+A);C1=2*G/(1+A)
kp=(C1-2*HH)/(4-R1);Dp=2*(C+HH)+4*kp
ck('activation_transversality_identity',s.factor((Dp-1/(Lam*(1+2*A))).subs(Lam,1/(2*(2*G-HH+(1+2*A)*C))))==0)
G1,G2,MM=s.symbols('G1 G2 MM');kap=(G2-G1)/2
ck('joint_fixed_budget_gain',s.expand(G1+(MM-2)*kap-((4-MM)*G1+(MM-2)*G2)/2)==0)
v,ss,hh,ll=s.symbols('v ss hh ll',positive=True);sc=2*v/(ll*hh);layer=ss*v/4-ll*hh*ss**2/16;flat=v*v/(4*ll*hh)
ck('endpoint_layer_value_match',s.simplify(layer.subs(ss,sc)-flat)==0)
ck('endpoint_layer_slope_match',s.diff(layer,ss).subs(ss,sc)==0)
ck('endpoint_exact_zero_leading',layer.subs(ss,0)==0)
ct('two_corner_Hessians_not_one',s.Rational(1312,441)!=s.Rational(171736,24255))
ct('fixed_score_limit_not_uniform',gap.subs(Bsym,s.Rational(49,100))>0 and gap.subs(Bsym,s.Rational(1,2))==0)
ct('wrong_single_action_corner_gain',s.simplify(((4-MM)*G1+(MM-2)*G2)/2-(4-MM)*G1/2)!=0)
# Four corners prove whole rectangle via the convex quadratic perspective.
Hout=add(W(F(0),blo),W(F(0),bhi));corners=[]
ck('all_counts_decrease_after_three',klo>lmax*sub(H(3),H(4))[1])
ck('small_score_c_monotone',1-3*(S/3)+(S/3)**2>0)
for lam in [lmin,lmax]:
 for k in [klo,khi]:
  D=lam/(4*S);J2=sub(sub(exact(1),mul(2*lam,H(2))),exact(4*k));J3=sub(sub(exact(1),mul(2*lam,H(3))),exact(6*k));B3=2*lam*c(S/3)
  U3=J3[1]+max(F(0),B3-J3[0])**2/(4*D)
  Jo=sub(sub(exact(1),mul(2*lam,Hout)),exact(4*k));Bo=2*lam*F(191,250);Uo=Jo[1]+max(F(0),Bo-Jo[0])**2/(4*D)
  ck('corner_higher_counts_'+str(lam)+'_'+str(k),0<J3[0] and U3<J2[0])
  ck('corner_extreme_scores_'+str(lam)+'_'+str(k),0<Jo[0] and Uo<J2[0])
  corners.append({'lambda':str(lam),'k':str(k),'count_gap':str(J2[0]-U3),'score_gap':str(J2[0]-Uo)})
ck('uniform_zero_suffix',2*lmax*(F(191,250)+W(F(0),bhi)[1])<1-2*khi)
resourcegap=4/(1+bhi)-2
ck('uniform_resource_separation',resourcegap==F(66,67)>0)
# Exact bracket for a_A, using rational derivative signs only.
alo=F(0);ahi=S
for _ in range(210):
 mid=(alo+ahi)/2
 if WA(mid,S)+c(S/2)<0:alo=mid
 else:ahi=mid
ck('activation_action_bracket',WA(alo,S)+c(S/2)<0<WA(ahi,S)+c(S/2))
# w decreases in action on [0,S]; include both action endpoints in denominator.
gA=(W(ahi,S)[0],W(alo,S)[1]);den=mul(2,add(sub(mul(2,gA),H(2)),( (1+2*alo)*c(S/2),(1+2*ahi)*c(S/2))))
lamA=(1/den[1],1/den[0]);lam1den=mul(2,add(sub(mul(2,H(1)),H(2)),exact(c(S))))
lam1=(1/lam1den[1],1/lam1den[0]);kA=mul(F(1,4),sub(exact(1),(2*lamA[0]*(H(2)[0]+c(S/2)),2*lamA[1]*(H(2)[1]+c(S/2)))))
ck('activation_lambda_enclosure',F('.5390654299881028092179425483')<lamA[0]<lamA[1]<F('.5390654299881028092179425485'))
ck('first_second_activation_separated',lam1[1]<F('.5390')<lamA[0]<lamA[1]<F('.5391'))
ck('activation_price_inside_global_box',klo<kA[0]<kA[1]<khi)
# Convex support on the whole reduced domain, including a=0 boundary KKT.
def support(k,lam,aa,bb=None):
 assert 0<=aa<=S, 'infeasible one-stage action'
 if bb is not None:assert 0<=aa<=bb<=S and blo<=bb<=bhi, 'infeasible two-stage policy'
 cost=W(aa,S) if bb is None else add(W(aa,bb),W(F(0),S-bb));m=1 if bb is None else 2
 j=mul(1/(1+aa),sub(sub(exact(1),mul(2*lam,cost)),exact(2*m*k)))
 ga=2*lam*WA(aa,S if bb is None else bb)+j[1];gb=F(0) if bb is None else 2*lam*(WB(aa,bb)-WB(F(0),S-bb))
 defect=(max(F(0),-ga) if aa==0 else abs(ga))+abs(gb)
 eps=4*defect+F(1,10**55);upper=j[1]+eps
 tangent=eps*(1+aa)+min(-(ga+eps)*aa,(ga+eps)*(S-aa))
 if bb is not None:tangent+=min(gb*(blo-bb),gb*(bhi-bb))
 assert tangent>0,'invalid global tangent'
 return j[0],upper,tangent
# Structural continuum crossing proof, using uniform optimizer cost separation.
a_cut=F(1,100)
N1max=-1+2*khi+2*lmax*(W(a_cut,S)[1]-(1+a_cut)*WA(a_cut,S))
ck('uniform_one_action_cutoff',N1max<0)
C1min=2*W(a_cut,S)[0]/(1+a_cut);C2max=2*H(2)[1]
ck('uniform_optimizer_cost_separation',C1min>C2max)
J1left=sub(sub(exact(1),mul(2*lmin,H(1))),exact(2*klo));J2left=sub(sub(exact(1),mul(2*lmin,H(2))),exact(4*klo))
ck('left_corner_one_stage_zero_action',2*lmin*c(S)<J1left[0])
ck('left_corner_support_sign',J1left[1]<J2left[0])
J1right=sub(sub(exact(1),mul(2*lmax,H(1))),exact(2*khi));J2right=sub(sub(exact(1),mul(2*lmax,H(2))),exact(4*khi))
U2right=J2right[1]+max(F(0),2*lmax*c(S/2)-J2right[0])**2*S/lmax
ck('right_corner_global_support_sign',U2right<J1right[0])
policies=[{'lambda': '.5390', 'endpoints': [{'k': '.00825', 'x': '0.00008865469032971204865825039751647182211418089313927006492486425865628259', 'a': '0', 'b': '0.245'}, {'k': '.0084', 'x': '0.0001796190002364257455869991565427397602708006843124306203711889498939458', 'a': '0.00003131926866746805764171493915969115565417776976801555387674840817830094', 'b': '0.2450018800564923714867414188487940006668154867037929681129500678446448'}], 'crossing': {'k': '0.008308516314323890182595582573833341577041522398558651412252278623446719', 'x': '0.0001241372121095361594300645975187574210226435553334172062233721817419206', 'a': '0', 'b': '0.245'}}, {'lambda': '.5391', 'endpoints': [{'k': '.00825', 'x': '0.0001439677464798464192311218485574014628986123162449011978238908250712573', 'a': '0', 'b': '0.245'}, {'k': '.0084', 'x': '0.0002349328282412878621966279590404361128423308843130803726408852170007491', 'a': '0.0000542795841590600006337750065003749183900899735807636636896309747719678', 'b': '0.2450032997237326034408543351313090576121035957884808809817742471618977'}], 'crossing': {'k': '0.008310043794909240349719376014048548758474694363699215267432228671027021', 'x': '0.0001803768548396008522473943184532022104506098234848450114384326850398207', 'a': '0.000008206334442859598083422454906658879696869052657680445228512304045846276', 'b': '0.2450004863147535884187414269323763912055283227583835096384874981601532'}}]
consumers=[];endrows=[]
for row in policies:
 lam=F(row['lambda'])
 for e in row['endpoints']:
  kk=F(e['k']);x=F(e['x']);aa=F(e['a']);bb=F(e['b']);q1=support(kk,lam,x);q2=support(kk,lam,aa,bb)
  ck('crossing_endpoint_'+str(lam)+'_'+str(kk),q2[0]>q1[1] if kk==klo else q1[0]>q2[1]);endrows.append({'lambda':str(lam),'k':str(kk),'one':list(map(str,q1[:2])),'two':list(map(str,q2[:2]))})
 e=row['crossing'];kk=F(e['k']);x=F(e['x']);aa=F(e['a']);bb=F(e['b']);q1=support(kk,lam,x);q2=support(kk,lam,aa,bb);Q=max(q1[1],q2[1]);dif=(q1[0]-q2[1],q1[1]-q2[0]);rad=max(map(abs,dif))/resourcegap;kc=(kk-rad,kk+rad)
 ck('crossing_enclosed_'+str(lam),klo<kc[0]<kc[1]<khi and kc[1]-kc[0]<F(1,10**50))
 # Sign of the unique a2=0 score minimizer derivative across the entire kc bracket.
 drive=sub(exact(2*lam*c(S/2)),sub(sub(exact(1),mul(2*lam,H(2))),(4*kc[0],4*kc[1])))
 ck('opposite_activation_'+str(lam),drive[1]<0 if aa==0 else drive[0]>0)
 r1=2/(1+x);r2=4/(1+aa);M=F(3);theta=(r2-M)/(r2-r1)
 ck('actual_resource3_'+str(lam),0<theta<1 and theta*r1+(1-theta)*r2==M)
 v1=mul(1/(1+x),sub(exact(1),mul(2*lam,W(x,S))));v2=mul(1/(1+aa),sub(exact(1),mul(2*lam,add(W(aa,bb),W(F(0),S-bb)))))
 lower=add(mul(theta,v1),mul(1-theta,v2));upper=Q+kk*M
 ck('global_budget3_width_'+str(lam),0<upper-lower[0]<F(1,10**50))
 uniform_width=max(Q-q1[0],Q-q2[0]);ck('whole_candidate_budget_interval_'+str(lam),0<uniform_width<F(1,10**50))
 old=1-lam*(H(1)[0]+H(2)[0]);ck('actual_gain_over_zero_action_'+str(lam),lower[0]>old)
 consumers.append({'lambda':str(lam),'critical_price':list(map(str,kc)),'first_action':str(x),'two_action':str(aa),'two_score':str(bb),'uniform_budget_interval':list(map(str,[r1,r2])),'uniform_value_enclosure_width':str(uniform_width),'budget':'3','theta':str(theta),'value_lower':str(lower[0]),'value_upper':str(upper),'width':str(upper-lower[0]),'display':[float(lower[0]),float(upper)],'two_action_active':aa>0})
ct('positive_second_action_only_on_upper_side',consumers[0]['two_action']=='0' and consumers[1]['two_action']!='0')
ct('charge_failed_trials',r2!=2/(1+aa))
ct('half_half_mixture_wrong_resource',(r1+r2)/2!=3)
ct('naive_equal_positive_score_stationarity',WB(aa,S/2)-WB(F(0),S/2)!=0)
ct('endpoint_fixed_budget_formula_wrong',((4-MM)*G1+(MM-2)*G2).subs(MM,4)/2!=0)
report={'result':'K2599','checks':checks,'contrary_controls':controls,'joint_normal_form':{'gamma':'16/315','h1':'1312/441','h2':'171736/24255','activation_wedge':'lambda_A-lambda1 = (32 lambda_star^2/315)(1/2-S)+O((1/2-S)^2)','gain':'[(4-M)G1+(M-2)G2]/2+O(r^3); G_i=[u_i]_+^2/(4 lambda_star h_i)'},'finite_box':{'S':str(S),'lambda':list(map(str,[lmin,lmax])),'k':list(map(str,[klo,khi])),'score':list(map(str,[blo,bhi]))},'uniform_lambda_crossing':{'one_action_cutoff':str(a_cut),'action_derivative_margin':str(-N1max),'optimizer_cost_gap':str(C1min-C2max),'left_price_gap':str(J2left[0]-J1left[1]),'right_price_gap':str(J1right[0]-U2right),'claim':'unique increasing crossing and exact zero/one-active/both-active topology throughout rectangle lambda range'},'corner_gaps':corners,'activation':{'action':list(map(str,[alo,ahi])),'lambda1':list(map(str,lam1)),'lambda_A':list(map(str,lamA)),'k_A':list(map(str,kA))},'endpoint_supports':endrows,'consumers':consumers,'evidence_kind':'exact symbolic identities, rational-log global rectangle bounds and independent convex supports plus actual original-law mixtures; uniform local compactness/KKT and regularity proof in note','ceiling':'joint local S-to-half and multiplier unfolding, exact score49/100 finite consumers; not arbitrary score/multiplier frontier, uniform large-count limit, physical probability or GU recovery'}
refs=['explorations/conditional-build/k2597-stopping-threshold-bifurcation-2026-11-06.md','explorations/conditional-build/k2591-multistage-stopping-support-2026-11-06.md','explorations/conditional-build/k2587-countwise-stopping-support-2026-11-05.md']
report['provenance']={f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in refs}
out=root/'lab/process/k2599-joint-stopping-corner.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report mismatch'
print(json.dumps({'result':'K2599','checks':len(checks),'controls':len(controls),'status':'pass','consumer_displays':[r['display'] for r in consumers]}))
