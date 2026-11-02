"""Exact K2505 polynomial certificate and original stopping-law controls."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import sympy as s
import json,hashlib,sys
from flint import arb,ctx
ctx.prec=160
ROOT=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ct(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
q,r,x,y=s.symbols('q r x y');g=(1-r)**2/(2*(1+r));c=(1-r)**2/8-(1-r)**4/(32*(1+r)**2)
J=(-3+22*r*r-16*r**3-3*r**4)/(16*(1+r)**2)
ck('binary_split_second_coefficient',s.factor(-c-r*r*s.diff(g,r)/4+r*g/4-J/2)==0)
# Independent expansion of rational input log's first two coefficients.
b=s.symbols('b',positive=True);z=(b-r*b)**2/(2*(b+r*b)*(2-b-r*b))
ck('stage_first_coefficient',s.simplify(s.limit(z/b,b,0)-g/2)==0)
ck('stage_second_coefficient',s.simplify(s.limit((z-z*z/2-g*b/2)/b**2,b,0)-c)==0)
M,n,L=s.symbols('M n L',positive=True)
correction=(1-1/n)*(M*r*r/2+r*g/2-2*c)/L
ck('hierarchy_coefficient_identity',s.factor(correction.subs(M,-s.diff(g,r))-(1-1/n)*J/L)==0)
ct('omit_main_hazard_correction',s.factor((r*g/2-2*c)-J)!=0)
ct('omit_survival_weights',s.factor((-s.diff(g,r)*r*r/2-2*c)-J)!=0)
P=s.together(J*16*(1+r)**2)
ck('numerator_derivative',s.factor(s.diff(P,r)-4*r*(11-12*r-3*r*r))==0)
ck('left_endpoint',P.subs(r,s.Rational(2,5))==-s.Rational(363,625))
ck('right_endpoint',P.subs(r,s.Rational(9,20))==-s.Rational(20163,160000))
ck('derivative_positive_whole_box',11-12*s.Rational(9,20)-3*s.Rational(9,20)**2>0)
ck('beta_infinity_positive',s.Rational(1,67)-s.Rational(363,26068)==s.Rational(1747,1746556)>s.Rational(1,1000))
# Unequal equal-ratio partitions: product cross terms and weighted survival.
for lam in [[F(1,2),F(1,2)],[F(1,3)]*3,[F(1,5),F(3,10),F(1,2)],[F(1,10),F(1,10),F(1,5),F(3,5)]]:
 ck('partition_pair_identity_'+str(lam),sum(lam[i]*lam[j] for i in range(len(lam)) for j in range(i+1,len(lam)))==(1-sum(v*v for v in lam))/2)
 ck('partition_CS_'+str(lam),sum(v*v for v in lam)>=F(1,len(lam)))
ct('unequal_partition_not_better',F(1,5)**2+F(3,10)**2+F(1,2)**2>F(1,3))
# Whole-domain log comparison with an explicitly positive denominator.
a=q*(2+q);bb=a/r
def zz(a,b):return s.cancel((b-a)**2/(2*(a+b)*(2-a-b)))
xo=zz(a,bb);xs=zz(q,bb/2)
lo4=lambda z:z-z*z/2+z**3/3-z**4/4
hi3=lambda z:z-z*z/2+z**3/3
D=s.factor(lo4(xo)-(2+q)*hi3(xs))
H=192*(r+1)**4*(q+2*r+2)**3*(4*r-q*q-2*q*r-2*q)**3*(2*r-(r+1)*q*(q+2))**4
poly=s.Poly(s.cancel(H*D/q**2),q,r)
ck('certificate_degrees',poly.degree_list()==(16,14))
ck('certificate_rational_identity',s.cancel(q*q*poly.as_expr()/H-D)==0)
ck('first_denominator_positive_box',s.Rational(1,40000)+s.Rational(29,2000)<s.Rational(8,5))
ck('second_denominator_positive_box',s.Rational(29*401,800000)<s.Rational(4,5))
trans=s.Poly(poly.as_expr().subs({r:s.Rational(2,5)+x/20,q:y/200}).expand(),x,y)
coeff=[]
for i in range(15):
 for j in range(17):
  v=sum(v*s.Rational(comb(i,k),comb(14,k))*s.Rational(comb(j,l),comb(16,l)) for (k,l),v in trans.terms() if k<=i and l<=j)
  ck('positive_Bernstein_'+str((i,j)),v>0);coeff.append(v)
ck('Bernstein_minimum',min(coeff)==s.Rational(73262028865500189,50000000000000))
# Reconstruct polynomial exactly from Bernstein coefficients; checks transform itself.
# Evaluate coefficient convolution (expand only small univariate bases).
bx=[s.Poly(comb(14,i)*x**i*(1-x)**(14-i),x) for i in range(15)]
by=[s.Poly(comb(16,j)*y**j*(1-y)**(16-j),y) for j in range(17)]
reconstructed={}
for i in range(15):
 for j in range(17):
  for (k,),u in bx[i].terms():
   for (l,),v in by[j].terms():reconstructed[k,l]=reconstructed.get((k,l),0)+coeff[i*17+j]*u*v
ck('Bernstein_exact_reconstruction',all(reconstructed.get((k,l),0)==trans.coeff_monomial(x**k*y**l) for k in range(15) for l in range(17)))
# Genuine contrary direction: splitting a free positive stage adds cost.
bv=F(1,100);qv=F(1,1000);av=2*qv+qv*qv
ck('binary_exact_product', (1+qv)**2==1+av)
ck('binary_feasible',0<qv<=bv/2)
ct('sum_hazard_not_product', (1+av/2)**2!=1+av)
# Exact rational logarithmic enclosures; no sampled/logarithm rounding.
def arg(a,b):
 if a==b==0:return F(0)
 return (b-a)**2/(2*(a+b)*(2-a-b))
def logs(z):
 low=sum((-1)**(j+1)*z**j/F(j) for j in range(1,9))
 high=low+z**9/9
 return low,high
def costs(stages):
 p=F(1);low=F(0);high=F(0)
 for a,b in stages:
  assert 0<=a<=b
  p/=1+a;z=arg(a,b);assert 0<=z<1
  lo,hi=logs(z);low+=2*p*lo;high+=2*p*hi
 return p,low,high
old=[(F(691,2109),F(49,100)),(F(3,700),F(1,100))]
new=[(F(1934773,5905227),F(49,100)),(F(3,1400),F(1,200)),(F(3,1400),F(1,200))]
po,lo,ho=costs(old);pn,ln,hn=costs(new);budget=F(106307,5000000)
ck('finite_exact_score',sum(b for a,b in new)==F(1,2))
ck('finite_exact_success',po==pn==F(3,4))
ck('new_budget',hn<budget)
ck('strict_improvement',lo-hn>F(3929,10**10))
gap=F(417,19600)-budget;ck('mixture_gap',gap>0 and F(3,4)-2*gap<F(3,4))
# An exact survival-preserving split at r=3/7, with rational square root.
a1=2*qv+qv*qv;b1=a1*F(7,3)
p1,l1,h1=costs([(a1,b1)]);p2,l2,h2=costs([(qv,b1/2)]*2)
ck('binary_finite_same_success',p1==p2 and F(0)<b1<F(1,100))
ck('binary_finite_lower_cost',h2<l1)
# Splitting free original a=b produces q<b/2 and strictly positive replacement cost.
pf,lf,hf=costs([(F(21,100),F(21,100))]);ps,ls,hs=costs([(F(1,10),F(21,200))]*2)
ct('free_stage_split_can_increase_cost',pf==ps and lf==hf==0 and ls>0)
# Exact refutation of an overstrong, unweighted global merge.
a1,b1=F(153,5000),F(3,50);a2,b2=F(1547,5153),F(11,25)
ck('merge_counter_effective_hazard',(1+a1)*(1+a2)-1==F(17,50) and b1+b2==F(1,2))
ct('unweighted_merge_false',(1+arg(a1,b1))*(1+arg(a2,b2))<1+arg(F(17,50),F(1,2)))
# It is NOT a cheaper original policy at that same success.
pc,lc,hc=costs([(a1,b1),(a2,b2)]);p1,l1,h1=costs([(F(17,50),F(1,2))])
ck('merge_failure_not_original_advantage',pc==p1 and lc>h1)
# Original finite-n family and exact limit structure.
for nn in [1,2,3,5,10]:
 t=F(1,100);rr=F(3,7);LL=F(4,3);zn=(1+rr*t/nn)**nn
 stages=[(LL/zn-1,F(1,2)-t)]+[(rr*t/nn,t/nn)]*nn
 pp,ll,hh=costs(stages)
 ck('family_score_success_'+str(nn),sum(b for a,b in stages)==F(1,2) and pp==1/LL)
 z=arg(rr*t/nn,t/nn);lw,hw=logs(z);lm,hm=logs(arg(stages[0][0],stages[0][1]));geo=sum((1+rr*t/nn)**j for j in range(nn))
 ck('family_cost_formula_'+str(nn),ll==2/LL*(zn*lm+geo*lw) and hh==2/LL*(zn*hm+geo*hw))
 ck('geometric_sum_'+str(nn),geo==(zn-1)*nn/(rr*t))
# Strict upper-feasibility margin cannot be dropped from the limiting argument.
limL=arb(7)/5*(arb(1)/25).exp()
ck('limit_boundary_d_positive',(arb(3)/2-limL).lower()>0)
for nn in [1,2,5,10]:
 zn=(F(1)+F(1,25)/nn)**nn
 ct('boundary_finite_infeasible_'+str(nn),(limL/(arb(zn.numerator)/zn.denominator)-1).lower()>arb(2)/5)
# Ratio curvature required for the fixed-n local branch and first-order penalty.
ck('g_curvature',s.factor(s.diff(g,r,2)-4/(1+r)**3)==0)
ck('g_strong_convexity',F(4,2**3)==F(1,2))
report={'result':'K2505','scope':'finite fragmentation and onset-local hierarchy, not global optimum','evidence_kind':'universal proof plus exact symbolic identities, whole-box Bernstein certificate, rational logarithm enclosures and finite controls','checks':checks,'contrary_controls':controls,'bernstein_certificate':{'degrees_q_r':[16,14],'count':len(coeff),'minimum':str(min(coeff)),'coefficients_order_r_then_q':[str(v) for v in coeff]},'finite_witness':{'old_lower':str(lo),'new_upper':str(hn),'new_budget':str(budget),'strict_gain_lower':str(lo-hn),'one_stage_mixture_gap':str(2*gap)},'dependencies':{}}
for p in [__file__,str(ROOT/'explorations/conditional-build/k2505-stopping-satellite-hierarchy-2026-11-02.md'),str(ROOT/'explorations/conditional-build/k2503-stopping-instability-boundary-2026-11-02.md')]:
 p=Path(p);report['dependencies'][str(p.relative_to(ROOT))]=hashlib.sha256(p.read_bytes()).hexdigest()
path=ROOT/'lab/process/k2505-stopping-satellite-hierarchy.json'
if '--write' in sys.argv:path.write_text(json.dumps(report,indent=2)+'\n')
else:ck('saved_report_matches_reproduction',json.loads(path.read_text())==report)
print(f'K2505 PASS: {len(checks)} checks; {len(controls)} contrary controls')
