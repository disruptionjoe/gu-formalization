#!/usr/bin/env python3
"""Original-log/prefix coefficient identities and certified terminal consumers.
Uniform all-policy localization and optimization are the analytic proof in the note.
"""
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F
import sympy as s
from flint import arb,ctx
root=Path(__file__).resolve().parents[2]
ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();ctx.prec=256
checks=[];controls=[]
def ck(name,cond):
    assert bool(cond),'FAIL '+name
    checks.append(name)
def ct(name,cond):
    assert bool(cond),'FAIL contrary '+name
    controls.append(name)
e,al,be,mu,x=s.symbols('e al be mu x',positive=True)
def cut(f,n=5):return s.series(f,e,0,n).removeO().expand()
def w(a,b):return s.log(1+(b-a)**2/(2*(a+b)*(2-a-b)))
cs=[be/2,-3*al/2+3*be**2/16,2*al**2/be-al*be/8+7*be**3/96,-2*al**3/be**2-13*al**2/16+3*al*be**2/32+15*be**4/512]
# Derive the logarithm via its factored original rational argument.
t= cut(e*(be-e*al)**2/(2*(be+e*al)*(2-e*be-e**2*al)))
series=cut(2*sum((-1)**(k+1)*t**k/s.Integer(k) for k in range(1,5)))
for k,c in enumerate(cs,1):ck('original_log_coefficient_'+str(k),s.factor(series.coeff(e,k)-c)==0)
def GH(betas,alphas,m):
    n=len(betas);L=[3*m/2+betas[j]/12+sum(betas[j:])/3 for j in range(n)]
    G=-3*m*sum(v*v for v in betas)/16-7*sum(v**3 for v in betas)/144+sum(alphas[j]*L[j]-s.Rational(4,3)*alphas[j]**2/betas[j] for j in range(n))
    H=0
    for i,(bb,aa) in enumerate(zip(betas,alphas)):
        c3=cs[2].subs({al:aa,be:bb});c4=cs[3].subs({al:aa,be:bb})
        H+=-s.Rational(2,3)*c4-m*c3+sum(alphas[:i+1])*(bb*bb/8+m*bb/2+2)
    return s.factor(G),s.factor(H)
# Independent direct original prefix expansion on unequal score/action fixtures.
for count in [1,2,3]:
    bs=[s.Rational(i+1,7) for i in range(count)];aa=[s.Rational(i+1,23) for i in range(count)];mm=s.Rational(-2,7)
    P=s.Integer(1);cost=0
    for bb,av in zip(bs,aa):
        P=cut(P/(1+e**2*av));c=cut(series.subs({al:av,be:bb}));cost=cut(cost+P*((s.Rational(2,3)+e*mm)*c+2*e**2))
    J=cut(P-cost);G,H=GH(bs,aa,mm)
    ck('actual_prefix_cubic_'+str(count),s.factor(J.coeff(e,3)-G)==0)
    ck('actual_prefix_quartic_'+str(count),s.factor(J.coeff(e,4)-H)==0)
    if count==2:ct('discarding_prefix_price_is_wrong',H!=H-2*sum(sum(aa[:i+1]) for i in range(count)))
# Independent constrained-square identity and continuity at its activation face.
L=s.symbols('L',real=True)
ck('constrained_action_square',s.expand(al*L-s.Rational(4,3)*al**2/be-(3*be*L**2/16-s.Rational(4,3)*(al-3*be*L/8)**2/be))==0)
ck('activation_value_matches', (3*be*L**2/16).subs(L,0)==0)
ck('activation_first_derivative_matches',s.diff(3*be*L**2/16,L).subs(L,0)==0)
ct('activation_is_not_C2',s.diff(3*be*L**2/16,L,2)!=0)
# Exact envelope gradient and D on chosen active sets; formula is piecewise but C1,1.
def coefficients(n,active,m=mu):
    betas=s.symbols('b0:'+str(n),positive=True);h=x/n
    L=[3*m/2+betas[j]/12+sum(betas[j:])/3 for j in range(n)]
    aa=[3*betas[j]*L[j]/8 if j in active else s.Integer(0) for j in range(n)]
    G,H=GH(betas,aa,m);sub={bb:h for bb in betas}
    g=[s.factor(s.diff(G,bb).subs(sub)) for bb in betas];pg=[s.factor(v-sum(g)/n) for v in g]
    B=s.factor(G.subs(sub));D=s.factor(H.subs(sub)+2*sum(v*v for v in pg))
    return B,D,[4*v for v in pg],s.factor(H.subs(sub))
B1,D1,_,_=coefficients(1,{0});B2,D2,delta2,H2=coefficients(2,{0,1})
ck('active_B1',s.factor(B1-x*(972*mu**2+108*mu*x-37*x*x)/2304)==0)
ck('active_D1',s.factor(D1-x*(-4860*mu**3+4536*mu**2*x+1981*mu*x*x+13824*mu+105*x**3+3840*x)/12288)==0)
ck('active_D2',s.factor(D2-x*(-19440*mu**3+11016*mu**2*x+4309*mu*x*x+82944*mu+354*x**3+17664*x)/49152)==0)
ck('active_count2_score_correction',delta2==[x*x/64,-x*x/64])
ct('equal_score_quartic_misses_gain',s.factor(D2-H2)==x**4/s.Integer(16384))
ck('unit_active_D1',D1.subs({x:1,mu:0})==s.Rational(1315,4096))
shifts=[]
for name,mval,active in [('active',s.Integer(0),True),('inactive',s.Integer(-2),False)]:
    b1,d1,_,_=coefficients(1,{0} if active else set(),mval);b2,d2,_,_=coefficients(2,{0,1} if active else set(),mval)
    x0=4*s.sqrt(2);db=b1-b2;dd=d1-d2;xi=s.simplify(s.sqrt(2)*db.subs(x,x0));zeta=s.simplify(s.sqrt(2)*(dd.subs(x,x0)+xi*s.diff(db,x).subs(x,x0)-xi**2/16))
    expectedxi=-s.Rational(65,12) if active else 6*s.sqrt(2)-s.Rational(28,3)
    expectedz=20837*s.sqrt(2)/2304 if active else -28+209*s.sqrt(2)/9
    ck(name+'_first_shift',s.simplify(xi-expectedxi)==0);ck(name+'_second_shift',s.simplify(zeta-expectedz)==0)
    shifts.append({'branch':name,'xi':str(xi),'zeta':str(zeta)})
# Exact lower-bound derivative of the original one-stage objective.
a,b,k,ll=s.symbols('a b k ll',positive=True);ww=w(a,b);wa=s.diff(ww,a);M=2*((ww-wa).subs(a,0))
J=(1-2*ll*ww-2*k)/(1+a);num=s.simplify(s.diff(J,a)*(1+a)**2)
ck('exact_activation_numerator',s.simplify(num.subs(a,0)-(ll*M-(1-2*k)))==0)
ck('derivative_numerator_monotone',s.simplify(s.diff(num,a)+2*ll*(1+a)*s.diff(ww,a,2))==0)
lc=cut(((1-2*e**2)/M.subs(b,e*x)),4)
expected=s.Rational(2,3)-5*e*x/18+e**2*(2*x*x/27-s.Rational(4,3))+e**3*(-5*x**3/648+5*x/9)
ck('exact_threshold_series',s.simplify(lc-expected)==0)
nu=s.symbols('nu',real=True);alpha3=s.factor(3*x*(3*nu/2+2-x*x/9)/8)
ck('unit_finer_activation',alpha3.subs({x:1,nu:0})==s.Rational(17,24))
ct('zero_cubic_action_not_exact_zero',alpha3.subs({x:1,nu:0})>0)
# Outward interval original-law consumers, with rational feasible inputs.
def ab(q):
    if isinstance(q,arb):return q
    q=F(q);return arb(q.numerator)/q.denominator
def costw(a0,b0):return (1+(ab(b0)-ab(a0))**2/(2*(ab(a0)+ab(b0))*(2-ab(a0)-ab(b0)))).log()
def wa_arb(a0,b0):
    a0=ab(a0);b0=ab(b0);den=2*(a0+b0)*(2-a0-b0);nd=den+(b0-a0)**2
    return (4-2*a0-6*b0)/nd-(4-4*a0-4*b0)/den
finite=[]
for denom in [100,200,400]:
    ee=F(1,denom);bb=ee;lam=F(2,3);a0=F(5,32)*ee*ee
    actual=(1-2*ab(lam)*costw(a0,bb)-2*ab(ee*ee))/(1+ab(a0))
    pred=1-ab(lam*ee/2)-ab(F(17,8)*ee**2)-ab(F(37,2304)*ee**3)+ab(F(1315,4096)*ee**4)
    residual=(actual-pred)/ab(ee**5)
    ck('rational_active_feasible_'+str(denom),0<a0<bb)
    ck('rational_active_residual_bounded_'+str(denom),abs(residual)<10)
    finite.append({'e':str(ee),'a':str(a0),'value_Arb':str(actual),'scaled_e5_residual_illustration':str(residual)})
# A certified finer-corner action bracket from the actual derivative.
ee=F(1,1000);bb=ee;lam=F(2,3)-F(5,18)*ee
lo=F(7,10)*ee**3;hi=F(18,25)*ee**3
def derivnum(av,score=bb,multiplier=lam,price=ee*ee):
    return -2*ab(multiplier)*(1+ab(av))*wa_arb(av,score)-(1-2*ab(multiplier)*costw(av,score)-2*ab(price))
ck('finer_corner_bracket_signs',derivnum(lo)>0 and derivnum(hi)<0)
threshold=(1-2*ab(ee*ee))/(2*(costw(F(0),bb)-wa_arb(F(0),bb)))
ck('finer_corner_exact_activation',ab(lam)>threshold)
ct('wrong_no_price_threshold',threshold<1/(2*(costw(F(0),bb)-wa_arb(F(0),bb))))
# Exact inactive branch tie, independent of the quartic optimizer formula.
tie_e=F(1,1000);tie_lam=F(2,3)-2*tie_e
def tie_res(score):
    return ab(tie_lam)*(costw(F(0),score)-2*costw(F(0),score/2))-ab(tie_e*tie_e)
tlo=5*tie_e;thi=6*tie_e
ck('inactive_tie_initial_bracket',tie_res(tlo)<0 and tie_res(thi)>0)
for _ in range(140):
    mid=(tlo+thi)/2;val=tie_res(mid)
    if val<0:tlo=mid
    elif val>0:thi=mid
    else:raise AssertionError('FAIL unresolved exact tie sign')
ck('inactive_tie_certified_bracket',tie_res(tlo)<0 and tie_res(thi)>0)
# First-stage derivative is the largest of the zero-action schedule derivatives.
for nn in [1,2]:
    bb=arb(ab((tlo+thi)/(2*nn)),ab((thi-tlo)/(2*nn)))
    first=ab(tie_lam)*(2*(costw(F(0),bb)-wa_arb(F(0),bb))+2*(nn-1)*costw(F(0),bb))-1+2*ab(tie_e*tie_e)*nn
    ck('inactive_branch_action_margin_'+str(nn),first<0)
tie_report={'e':str(tie_e),'lambda':str(tie_lam),'score_bracket':[str(tlo),str(thi)],'left_residual_Arb':str(tie_res(tlo)),'right_residual_Arb':str(tie_res(thi)),'ceiling':'exact two-branch tie; no explicit numerical global-validity radius'}
report={'result':'K2614','checks':checks,'contrary_controls':controls,'coefficients_2w':list(map(str,cs)),'active_D1':str(D1),'active_D2':str(D2),'active_count2_score_correction':list(map(str,delta2)),'count_shifts':shifts,'exact_inactive_tie':tie_report,'finite_policy_consumers':finite,'activation_consumer':{'e':str(ee),'lambda':str(lam),'action_bracket':[str(lo),str(hi)],'left_derivative_Arb':str(derivnum(lo)),'right_derivative_Arb':str(derivnum(hi)),'lambda_c_Arb':str(threshold)},'evidence_kind':'exact symbolic original log/prefix and optimization identities; outward Arb finite-policy and action-root signs; uniform all-policy theorem in note using predecessor localization','ceiling':'fixed compact terminal scaling, no infinite-count uniformity, exact tie from truncation or physical probability','provenance':{f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in ['explorations/conditional-build/k2610-terminal-stopping-count-layer-2026-11-06.md','lab/process/k2610-terminal-stopping-count-layer.json']}}
out=root/'lab/process/k2614-quartic-terminal-stopping.json'
if args.write:out.write_text(json.dumps(report,indent=2)+'\n')
else:assert json.loads(out.read_text())==report,'FAIL saved report replay'
print(json.dumps({'result':'K2614','checks':len(checks),'controls':len(controls),'status':'pass'}))
