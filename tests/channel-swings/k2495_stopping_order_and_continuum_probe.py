"""Exact algebra and rational controls; continuum theorem is in paired note."""
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations
import sympy as s
import json,hashlib,sys
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ct(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
def xc(a,b):
 if not 0<=a<=b<=F(1,2):raise ValueError('stage domain')
 return F(0) if a==b else (b-a)**2/(2*(a+b)*(2-a-b))
def lb(x):
 if not 0<=x<=1:raise ValueError('log domain')
 return x-x*x/2,x-x*x/2+x*x*x/3
def policy(st):
 P=F(1);lo=hi=B=F(0)
 for a,b in st:
  P/=1+a;ll,hh=lb(xc(a,b));lo+=2*P*ll;hi+=2*P*hh;B+=b
 return P,lo,hi,B
ai,aj,wi,wj,q=s.symbols('ai aj wi wj q',nonnegative=True)
D=2*q*(wi/(1+ai)+wj/((1+ai)*(1+aj))-wj/(1+aj)-wi/((1+ai)*(1+aj)))
ck('adjacent_exchange_identity',s.factor(D-2*q*(aj*wi-ai*wj)/((1+ai)*(1+aj)))==0)
ck('merge_success_identity',s.expand((1+ai)*(1+aj)-(1+ai+aj+ai*aj))==0)
# The actual previous witness, with rigorous logarithm bounds.
old=[(F(1,200),F(1,100)),(F(59,201),F(49,100))];new=list(reversed(old))
p,lo,hi,B=policy(new);po,loo,hio,Bo=policy(old);K=F(633,20000)
ck('same_success_score',p==po==F(10,13) and B==Bo==F(1,2))
ck('strict_revised_budget',hi<K<F(475,14976))
z=xc(*old[0]);x=xc(*old[1]);difflo=2/((1+old[0][0])*(1+old[1][0]))*(old[1][0]*lb(z)[0]-old[0][0]*x)
ck('exact_reversal_gap',difflo==F(964434753491869,28545820923554510940) and difflo>F(1,30000))
ck('previous_order_wrong',lb(z)[0]/old[0][0]>x/old[1][0])
ck('probability_gap_positive',F(5,3)*(F(475,14976)-K)>0)
ct('reversal_really_improves',loo>hi)
ct('costs_not_unweighted',sum(2*lb(xc(a,b))[1]/(1+a) for a,b in new)!=hi)
ct('merge_not_universal',policy([(F(3,10),F(1,2))])[1]>hi)
ct('some_merges_inadmissible',F(1,4)+F(1,4)+F(1,16)>F(1,2))
# Fixed-multiset global ordering fixture; rigorously separated indices.
stages=[(F(1,10),F(1,10)),(F(1,20),F(1,10)),(F(0),F(1,10))]
base=policy(stages)
for k,perm in enumerate(permutations(stages)):
 trial=policy(perm);ck('permutation_constraints_'+str(k),trial[0]==base[0] and trial[3]==base[3])
 if perm!=tuple(stages):ck('sorted_cost_'+str(k),trial[1]>base[2])
r,y,v=s.symbols('r y v',positive=True);g=(1-r)**2/(2*(1+r));Q=(1-r)*(1+3*r)/(2*(1+r)**2);f=-(1-r)*(1+r)*(1+3*r)/8
Ft=-s.log(1-r)-2*s.log(1+r)+3*s.log(1+3*r)
ck('g_second',s.factor(s.diff(g,r,2)-4/(1+r)**3)==0)
ck('g_first',s.factor(s.diff(g,r)-(s.Rational(1,2)-2/(1+r)**2))==0)
ck('beltrami_identity',s.factor(g-r*s.diff(g,r)-Q)==0)
ck('conserved_quantity',s.factor(-r*Q+s.diff(Q,r)*f)==0)
ck('time_primitive',s.factor(s.diff(Ft,r)*f+1)==0)
# Euler: L=y*g(-v/y), d/dt L_v=-g'' r', L_y=g-r*g'.
ck('Euler_equation',s.factor(Q+s.diff(g,r,2)*f)==0)
# Quadratic Hessian form of perspective is g''/y*(dv+r*dy)^2.
L=y*g.subs(r,-v/y);dy,dv=s.symbols('dy dv')
H=s.diff(L,y,2)*dy*dy+2*s.diff(L,y,v)*dy*dv+s.diff(L,v,2)*dv*dv
ck('perspective_Hessian',s.factor(H-4/(y*(1-v/y)**3)*(dv-v/y*dy)**2)==0)
# Cost primitive: y=Q0/Q(r), dt=-F'(r)dr.
q0=s.symbols('q0',positive=True);Cprim=8*q0/(3*(1+3*r))
ck('cost_primitive',s.factor(s.diff(Cprim,r)*f-q0*g/Q)==0)
ck('zero_arc_variation',g.subs(r,0)==s.Rational(1,2) and -s.diff(g,r).subs(r,0)==s.Rational(3,2))
# Exact nonempty interior fixture with no numerical logarithm decisions.
r0=s.Rational(1,2);rt=s.Rational(2,5);Q0=Q.subs(r,r0);QT=Q.subs(r,rt)
ck('fixture_Q',Q0==s.Rational(5,18) and QT==s.Rational(33,98))
ck('fixture_success',Q0/QT==s.Rational(245,297))
expS=(1-rt)/(1-r0)*((1+rt)/(1+r0))**2*((1+3*r0)/(1+3*rt))**3
ck('fixture_score_ratio',expS==s.Rational(6125,3993))
ck('fixture_cost',8*Q0/s.Integer(3)*(1/(1+3*rt)-1/(1+3*r0))==s.Rational(4,99))
xS=F(2132,3993);ck('fixture_score_below_half',F(1,2)-lb(xS)[1]==F(22105434323,381987525942)>0)
ck('fixture_H_below_S',F(1)<F(297,245)<F(6125,3993))
# Zero-arc fixture r0=1/100, rT=0, ell=1/10. Score log(E)+ell<1/2.
z0=F(1,100);eS=(1+3*z0)**3/((1-z0)*(1+z0)**2);Qz=(1-z0)*(1+3*z0)/(2*(1+z0)**2)
Cz=8*Qz/F(3)*(1-1/(1+3*z0))+2*Qz/F(20)
ck('zero_arc_fixture_domain',eS-1+F(1,10)<F(1,2) and 0<2*Qz<1 and Cz>0)
# Rational inequalities enclosing the exact logarithmic uniform stage bound.
for k in range(11):
 qq=F(k,10);gg=(1-qq)**2/(2*(1+qq));hh=gg/2
 for b in [F(1,100),F(1,10),F(1,2)]:
  zz=(1+qq)*b/2;xx=xc(qq*b,b)
  ck('stage_argument_'+str((k,b)),xx==b*hh/(1-zz))
  ck('stage_bounds_'+str((k,b)),zz>=b*hh and xx/(1+xx)>=b*hh and 2*xx-b*gg<=b*b/2)
 ck('field_lipschitz_'+str(k),0<=(1-qq)*(1+qq)*(1+3*qq)/8<=F(1,2))
 ck('g_Lipschitz_'+str(k),abs(F(1,2)-2/(1+qq)**2)<=F(3,2))
ck('approximation_constant',F(1,2)+F(9,4)+F(1,2)==F(13,4))
ct('negative_ratio_continuation_invalid',f.subs(r,0)<0)
ct('all_free_single_stage',xc(F(1,2),F(1,2))==0 and policy([(F(1,2),F(1,2))])[0]==F(2,3))
# log(3/2)<1/2 and >0 show H/S<1 => positive g, contrary to continuum=full.
ck('free_finite_vs_continuum',0<lb(F(1,2))[0] and lb(F(1,2))[1]<F(1,2))
ct('finite_n_never_H_equals_S',F(1,2)-lb(F(1,2))[1]>0)
for bad in [(F(-1),F(1,2)),(F(1,2),F(1,4))]:
 try:xc(*bad);failed=False
 except ValueError:failed=True
 ct('domain_'+str(bad),failed)
deps=['explorations/conditional-build/k2493-stopping-stage-splitting-2026-11-02.md','explorations/conditional-build/k2485-constrained-stopping-frontier-2026-11-01.md']
report={'result':'K2495','checks':checks,'contrary_controls':controls,'reversed_witness':{'stages':[[str(a),str(b)] for a,b in new],'success':str(p),'cost_lower':str(lo),'cost_upper':str(hi),'budget':str(K),'improvement_lower':str(difflo),'single_mixture_probability_gap':str(F(5,3)*(F(475,14976)-K))},'continuum_fixture':{'score':'log(6125/3993)','H':'log(297/245)','success':'245/297','cost':'4/99','r0':'1/2','rT':'2/5'},'approximation_bound':'13*S^2/(4*n), Delta<=min(1/2,1-r0), H<S','dependencies':{f:hashlib.sha256((R/f).read_bytes()).hexdigest() for f in deps},'evidence_kinds':{'universal':'written adjacent exchanges, convex perspective with boundary arc, monotone shooting and finite approximation','exact':'symbolic identities and rational inequality fixtures','not_claimed':'unrestricted original optimum, finite attainment, numerical calibrated control, GU physics, novelty'}}
pth=R/'lab/process/k2495-stopping-order-and-continuum.json'
if '--write' in sys.argv:pth.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
else:ck('saved_reproduction',json.loads(pth.read_text())==report)
print(json.dumps({'result':'PASS','checks':len(checks),'controls':len(controls),'witness':report['reversed_witness']}))
