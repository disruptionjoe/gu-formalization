#!/usr/bin/env python3
"""K2597 exact threshold bifurcation and original-policy consumer; interval helpers reused from K2595."""
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

S=F(1,2);ll=F('.5499');lu=F('.55001');kl=F('.00254');ku=F('.00255')
def J(n,k,lam):return sub(sub(exact(1),mul(2*lam,H(n))),exact(2*n*k))
def major(j,B,lam):return j[1]+max(F(0),B-j[0])**2/(2*lam)
rows=[]
for lam in [ll,lu]:
 for k in [kl,ku]:
  j2=J(2,k,lam);j4=J(4,k,lam);j1=J(1,k,lam)
  jout=sub(sub(exact(1),mul(2*lam,add(W(0,F('.15')),W(0,F('.35'))))),exact(4*k))
  vals={'count4':j2[0]-major(j4,2*lam*c(S/4),lam),'count1':j2[0]-major(j1,2*lam*c(S),lam),'extreme_scores':j2[0]-major(jout,2*lam*F(191,250),lam)}
  ck('positive_intercepts_'+str((lam,k)),min(j1[0],j2[0],j4[0],jout[0])>0)
  for name,v in vals.items():ck(name+'_corner_'+str((lam,k)),v>0)
  rows.append({'lambda':str(lam),'k':str(k),'margins':{n:str(v) for n,v in vals.items()}})
 ck('all_counts_monotone_'+str(lam),kl>lam*sub(H(4),H(5))[1])
 ck('count3_zero_'+str(lam),J(3,ku,lam)[0]>2*lam*c(S/3))
 ck('last_action_zero_'+str(lam),2*lam*(F(191,250)+W(0,F('.35'))[1])<1-2*ku)
T=sub(mul(3,H(2)),mul(2,H(3)));D0=mul(2,add(exact(c(S/2)),T));lambda0=(1/D0[1],1/D0[0]);deltaH=sub(H(2),H(3));k0=(lambda0[0]*deltaH[0],lambda0[1]*deltaH[1])
ck('lambda0_strict_in_rectangle',ll<lambda0[0]<lambda0[1]<lu)
ck('k0_strict_in_rectangle',kl<k0[0]<k0[1]<ku)
ww=w+(s.log((4-(s.Rational(1,2)-b))/(4-2*(s.Rational(1,2)-b))))
subs={a:0,b:s.Rational(1,4)}
haa=s.cancel(s.diff(ww,a,2)).subs(subs);hab=s.cancel(s.diff(ww,a,b)).subs(subs);hbb=s.cancel(s.diff(ww,b,2)).subs(subs)
h=s.factor(haa-hab**2/hbb);bp=-hab/hbb
ck('actual_Waa',haa==s.Rational(15616,2205));ck('actual_Wab',hab==-s.Rational(64,2205));ck('actual_Wbb',hbb==s.Rational(5632,11025));ck('score_slope',bp==s.Rational(5,88));ck('effective_curvature',h==s.Rational(171736,24255));ck('strict_effective_curvature',h>0)
x,L=s.symbols('x L',positive=True);gg=s.Function('g')(x);E=3*gg-(1+3*x)*s.diff(gg,x)
ck('crossing_E_derivative',s.simplify(s.diff(E,x)+(1+3*x)*s.diff(gg,x,2))==0)
# Eliminate the exact crossing E=1/(2lambda) from the stationarity price.
L=s.symbols('L',positive=True);H2,H3=s.symbols('H2 H3');G,Gp=s.symbols('G Gp');E=3*G-(1+3*x)*Gp-2*H3
price=(2*L*E-2*L*(G-(1+x)*Gp))/4
ck('crossing_price_identity',s.simplify(price-L*(G-x*Gp-H3))==0)
# General-score effective curvature: only fixed S, no uniform S->0 claim.
t=s.symbols('t',positive=True);w0=s.log((4-b)/(4-2*b))
haa_t=s.factor(s.diff(w,a,2).subs({a:0,b:t}));hab_t=s.factor(s.diff(w,a,b).subs({a:0,b:t}));hbb_t=2*s.factor(s.diff(w0,b,2).subs(b,t));ht=s.factor(haa_t-hab_t**2/hbb_t)
ck('general_curvature_specialization',s.simplify(ht.subs(t,s.Rational(1,4))-h)==0)
ck('general_h_numerator_negative_bound',s.Rational(1,4)**5+137*s.Rational(1,4)**3+431*s.Rational(1,4)<192)
# Direct expansion of the exact crossing-price identity; no fitted powers.
z,L0,hh,B2,G3,CC=s.symbols('z L0 hh B2 G3 CC',nonzero=True)
AA=1/(2*L0**2*hh);az=AA*z+B2*z*z
Gz=H2-CC*az+hh*az**2/2+G3*az**3/6
GPz=-CC+hh*az+G3*az**2/2
shift=s.expand((L0+z)*(Gz-az*GPz-H2))
ck('price_shift_no_linear_term',shift.coeff(z,1)==0)
ck('price_shift_quadratic_coefficient',s.simplify(shift.coeff(z,2)+1/(8*L0**3*hh))==0)

M,K,D=s.symbols('M K D');val=1-2*L*H3+(M-6)*K;old=1-L*((6-M)*H2+(M-4)*H3)
ck('exact_gain_identity',s.expand(val-old-(6-M)*(L*(H2-H3)-K))==0)
# Fixed rational scout candidates; all acceptance below uses exact bounds.
lam=F('.54997')
aa=F('752851249268491117835177250760958916939671381679334423763175176575122673/488281250000000000000000000000000000000000000000000000000000000000000000000000');bb=F('312500109599906239942905378433564833261290005268580285022217732942771686353/1250000000000000000000000000000000000000000000000000000000000000000000000000');k=F('2546611475484400309734477472155909646694366149727001060514674050121895512549/1000000000000000000000000000000000000000000000000000000000000000000000000000000')
cost=add(W(aa,bb),W(0,S-bb));gp=WA(aa,bb)
ck('consumer_policy_admissible',0<aa<bb<S and kl<k<ku)
q=mul(1/(1+aa),sub(sub(exact(1),mul(2*lam,cost)),exact(4*k)))
ga=2*lam*gp+q[1];gb=2*lam*(WB(aa,bb)-WB(0,S-bb));err=2*(abs(ga)+abs(gb))+F(1,10**60)
ck('convex_tangent_support',err*(1+aa)>(abs(ga+err)+abs(gb))/2)
q2upper=q[1]+err;j3=J(3,k,lam);qglobal=max(q2upper,j3[1]);R2=4/(1+aa);M=F(5);theta=(6-M)/(6-R2)
ck('exact_original_mixture_budget',theta*R2+(1-theta)*6==M)
actual2=mul(1/(1+aa),sub(exact(1),mul(2*lam,cost)));actual3=sub(exact(1),mul(2*lam,H(3)));lower=add(mul(theta,actual2),mul(1-theta,actual3))[0];upper=qglobal+k*M
old= sub(exact(1),mul(lam,add(H(2),H(3))))
ck('consumer_global_enclosure',0<=upper-lower<F(1,10**50));ck('strict_improvement_over_old_chord',lower-old[1]>F('4.62e-12'));ck('crossing_nearby',max(abs(q[0]-j3[1]),abs(q[1]-j3[0]))<F(1,10**60))
# Report coefficient intervals from rigorously enclosed lambda0.
hf=F(h);coefA=(1/(2*lambda0[1]**2*hf),1/(2*lambda0[0]**2*hf));coefG=(1/(8*lambda0[1]**3*hf),1/(8*lambda0[0]**3*hf))
ct('frozen_equal_score_wrong',hab!=0 and bp!=0)
ct('ignoring_score_optimization_wrong',h!=haa)
ct('linear_gain_wrong',shift.coeff(z,1)==0 and shift.coeff(z,2)!=0)
ct('zero_action_policy_suboptimal_above',lower>old[1])
ct('wrong_mixture_resource',theta*4+(1-theta)*6!=M)
ct('budget6_has_no_gain',(6-F(6))*coefG[0]==0)
ct('reversed_price_shift_wrong',k<lam*deltaH[0])

# General fixed-count successor: exact algebra, not a uniform-in-count theorem.
n=s.symbols('n',integer=True,positive=True);gg=s.Function('gg')(x);hnext=s.symbols('Hnext')
en=(n+1)*gg-(1+(n+1)*x)*s.diff(gg,x)-n*hnext
ck('all_count_crossing_derivative',s.simplify(s.diff(en,x)+(1+(n+1)*x)*s.diff(gg,x,2))==0)
G,Gp=s.symbols('G Gp');En=(n+1)*G-(1+(n+1)*x)*Gp-n*hnext
kn=(2*L*En-2*L*hnext+2*L*Gp)/(2*(n+1))
ck('all_count_price_elimination',s.simplify(kn-L*(G-x*Gp-hnext))==0)
R=2*n/(1+x);budget=s.symbols('budget');mix=(2*(n+1)-budget)/(2*(n+1)-R)
ck('all_count_exact_budget',s.simplify(mix*R+(1-mix)*2*(n+1)-budget)==0)
Hn=s.symbols('Hn');kv=s.symbols('kv');fv=1-2*L*hnext+(budget-2*(n+1))*kv
oldv=1-L*((2*(n+1)-budget)*Hn+(budget-2*n)*hnext)
ck('all_count_exact_gain',s.simplify(fv-oldv-(2*(n+1)-budget)*(L*(Hn-hnext)-kv))==0)
# Original law with only action j perturbed: earlier stages survive unchanged.
m,jj=s.symbols('m jj',integer=True,positive=True);lm,kk=s.symbols('lm kk',positive=True)
w0t=s.log((4-t)/(4-2*t));we=w.subs(b,t)
Cstage=2*((jj-1)*w0t+(we+(m-jj)*w0t)/(1+a));Rstage=2*((jj-1)+(m-jj+1)/(1+a))
Jstage=1/(1+a)-lm*Cstage-kk*Rstage
ct_expr=2*(3-2*t)/((2-t)*(4-t));Jm=1-2*lm*m*w0t-2*kk*m
ck('all_stage_action_derivative_from_original_law',s.simplify(s.diff(Jstage,a).subs(a,0)-(2*lm*ct_expr-Jm-2*(jj-1)*(lm*w0t+kk)))==0)
Hbbn=n*hbb_t/(2*(n-1));hn=s.factor(haa_t-hab_t**2/Hbbn);rhon=s.factor(-hab_t/Hbbn)
ck('n2_curvature_recovered',s.simplify(hn.subs(n,2)-ht)==0)
ck('n2_score_slope_recovered',s.simplify(rhon.subs({n:2,t:s.Rational(1,4)})-s.Rational(5,88))==0)
coefficient_consumers=[]
for score in [F(1,2),F(1,4)]:
 for count in [3,5,10]:
  tt=s.Rational(score.numerator,score.denominator)/count
  hv=s.factor(hn.subs({n:count,t:tt}));rv=s.factor(rhon.subs({n:count,t:tt}))
  ck('positive_higher_count_Schur_'+str((score,count)),hv>0 and rv>0)
  cn=c(score/count);hm=mul(count,W(0,score/count));hp=mul(count+1,W(0,score/(count+1)))
  tn=sub(mul(count+1,hm),mul(count,hp));den=mul(2,add(exact(cn),tn));ln=(1/den[1],1/den[0]);hf1=F(hv)
  ac=(1/(2*ln[1]**2*hf1),1/(2*ln[0]**2*hf1));gc=(1/(8*ln[1]**3*hf1),1/(8*ln[0]**3*hf1))
  ck('higher_count_positive_value_curvature_'+str((score,count)),gc[0]>0)
  coefficient_consumers.append({'score':str(score),'count':count,'h':str(hv),'first_score_slope':str(rv),'lambda_threshold':[str(q) for q in ln],'action_slope':[str(q) for q in ac],'gain_coefficient_per_upper_budget_distance':[str(q) for q in gc]})
# The excluded n=1/S=1/2 corner has TWO critical first actions, not one.
ck('n1_halfscore_double_criticality',c(F(1,2))==c(F(1,4)))
ct('blind_n1_extension_rejected',c(F(1,2))-c(F(1,4))==0)
ct('equal_suffix_score_derivative_not_zero',rhon.subs({n:3,t:s.Rational(1,6)})!=0)

# Count-one extension and the actual double-critical half-score corner.
SS=s.symbols('SS',positive=True)
cs=lambda z:2*(3-2*z)/((2-z)*(4-z))
cdiff=s.factor(cs(SS)-cs(SS/2))
ck('count_one_score_gap',s.simplify(cdiff-2*SS*(1-2*SS)/((2-SS)*(4-SS)*(8-SS)))==0)
h1=s.factor(s.diff(w,a,2).subs({a:0,b:s.Rational(1,2)}));h2=s.Rational(171736,24255)
ck('actual_count_one_halfscore_curvature',h1==s.Rational(1312,441));ck('distinct_positive_critical_curvatures',0<h1<h2)
d,Lzero,hh1,hh2,Bcorr,qcoef=s.symbols('d Lzero hh1 hh2 Bcorr qcoef',nonzero=True)
HH1,HH2=s.symbols('HH1 HH2');TT1=2*HH1-HH2;cc=1/(2*Lzero)-TT1;lamx=Lzero+d;kx=lamx*(HH1-HH2)+qcoef*d*d
support_coeff=[]
for mm,hh,HH in [(1,hh1,HH1),(2,hh2,HH2)]:
 ax=d/(2*Lzero**2*hh)+Bcorr*d*d;gx=HH-cc*ax+hh*ax*ax/2
 priced=(1-2*lamx*gx-2*mm*kx)/(1+ax);Qbase=1-2*lamx*TT1
 coeff=s.expand(s.series(priced-Qbase,d,0,3).removeO()).coeff(d,2)
 ck('double_critical_support_expansion_'+str(mm),s.simplify(coeff-(-2*mm*qcoef+1/(4*Lzero**3*hh)))==0);support_coeff.append(coeff)
qc=(1/hh2-1/hh1)/(8*Lzero**3)
ck('coupled_tie_price_shift',s.simplify((support_coeff[0]-support_coeff[1]).subs(qcoef,qc))==0)
mb=s.symbols('mb',real=True);gainfixed=(support_coeff[0]+mb*qcoef).subs(qcoef,qc)
ck('coupled_fixed_budget_gain',s.simplify(gainfixed-((4-mb)/hh1+(mb-2)/hh2)/(8*Lzero**3))==0)
# Global pure branch stationarity derivative, then exact small-layer expansion.
kfun=(1-2*L*(gg-(1+x)*s.diff(gg,x)))/4
ck('pure_two_price_derivative',s.simplify(s.diff(kfun,x)-L*(1+x)*s.diff(gg,x,2)/2)==0)
endprice=(1-2*lamx*(HH2+cc))/4
ck('pure_two_zero_action_endpoint',s.simplify(endprice-(lamx*(HH1-HH2)-d/(4*Lzero)))==0)
ss=s.symbols('ss',nonnegative=True);Mlayer=4-ss*d;alayer=4/Mlayer-1;glayer=HH2-cc*alayer+hh2*alayer**2/2
Fpure=Mlayer/4-lamx*Mlayer*glayer/2;Fold=1-lamx*((4-Mlayer)*HH1+(Mlayer-2)*HH2)
layercoeff=s.expand(s.series(Fpure-Fold,d,0,3).removeO()).coeff(d,2);expect=ss/(4*Lzero)-Lzero*hh2*ss**2/16
ck('moving_endpoint_layer',s.simplify(layercoeff-expect)==0)
sc=2/(Lzero**2*hh2);cap=1/(4*Lzero**3*hh2)
ck('layer_value_matches_mixture',s.simplify(expect.subs(ss,sc)-cap)==0)
ck('layer_first_derivative_matches',s.simplify(s.diff(expect,ss).subs(ss,sc))==0)
ck('exact_budget_four_no_gain',s.simplify((Fpure-Fold).subs(ss,0))==0)
ct('single_critical_halfscore_price_wrong',s.simplify(qc+1/(8*Lzero**3*hh1))!=0)
ct('fixed_budget_expansion_not_uniform_to_four',s.simplify(gainfixed.subs(mb,4)-cap)==0 and cap!=0)
ct('pure_layer_not_constant',s.diff(expect,ss)!=0)
# Exact log intervals enclose the half-score lambda1 coefficients.
T1=sub(mul(2,H(1)),H(2));den1=mul(2,add(exact(c(S)),T1));lone=(1/den1[1],1/den1[0]);h1f=F(h1);h2f=F(h2)
qraw=1/h2f-1/h1f;qs=(qraw/(8*lone[0]**3),qraw/(8*lone[1]**3))
ck('coupled_price_shift_negative_interval',qs[0]<qs[1]<0)
count_one={'lambda1':[str(v) for v in lone],'h1':str(h1),'h2':str(h2),'coupled_price_quadratic_coefficient':[str(v) for v in qs],'layer_threshold_s':[str(2/(v*v*h2f)) for v in (lone[1],lone[0])],'scope':'local halfscore; fixed budget2<=M<4 and moving M=4-s delta with fixed bounded s; no finite-offset optimizer certificate'}
report={'result':'K2597','checks':checks,'contrary_controls':controls,'evidence_kind':'exact actual Hessian, rational continuum-corner support inequalities and feasible-policy/convex-tangent enclosure; local analytic theorem in note','rectangle':rows,'lambda0':[str(v) for v in lambda0],'k0':[str(v) for v in k0],'curvature':str(h),'score_slope':str(bp),'action_linear_coefficient':[str(v) for v in coefA],'gain_quadratic_coefficient_per_6_minus_M':[str(v) for v in coefG],'consumer':{'lambda':str(lam),'budget':str(M),'action':str(aa),'score':str(bb),'price':str(k),'weight':str(theta),'value_bounds':[str(lower),str(upper)],'gain_bounds':[str(lower-old[1]),str(upper-old[0])]},'general_curvature':str(ht),'higher_count_coefficient_consumers':coefficient_consumers,'count_one_extension':count_one,'general_count_curvature':str(hn),'ceiling':'all fixed finite n>=1 local bifurcations; n1 halfscore coupled branch and moving endpoint treated separately; no uniform large-count or two-parameter radius; separate n2 finite consumer'}
refs=['lab/process/k2595-stopping-parameter-stability.json','explorations/conditional-build/k2587-countwise-stopping-support-2026-11-05.md','explorations/conditional-build/k2593-countwise-convex-stopping-2026-11-06.md']
report['provenance']={f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in refs}
out=root/'lab/process/k2597-stopping-threshold-bifurcation.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'saved report mismatch'
print(json.dumps({'result':'K2597','checks':len(checks),'controls':len(controls),'status':'pass','consumer_gain_lower':float(lower-old[1])}))
