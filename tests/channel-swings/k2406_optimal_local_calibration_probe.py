"""Exact fixtures for the written temporal calibration theorems; no measured data."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import factorial
import sympy as s
import json,hashlib,sys
R=Path(__file__).resolve().parents[2];checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ctrl(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
h=(5+s.sqrt(11))/2;L=s.Rational(1,32);c=2
ck('active_ages_exact',4<h<5)
ck('taper_root',s.simplify(L**2*256*sum((h-a)**2 for a in [1,2,3,4])-c*c)==0)
d=[h-a for a in [1,2,3,4]];mass=[s.simplify(x/sum(d)) for x in d];norm=s.sqrt(sum(w*w/256 for w in mass))
ck('weights_nonnegative_normalized',all(w>0 for w in mass) and s.simplify(sum(mass))==1)
ck('objective_exact',s.simplify(L*sum(a*w for a,w in zip([1,2,3,4],mass))+c*norm-L*h)==0)
ck('better_than_uniform',L*h<s.Rational(9,64))
rm=[s.Rational(1,2),s.Rational(1,3),s.Rational(1,6),s.Integer(0)]
ck('rational_drift',L*sum((i+1)*w for i,w in enumerate(rm))==s.Rational(5,96))
ck('rational_noise',s.simplify(c*s.sqrt(sum(w*w/256 for w in rm))-s.sqrt(14)/48)==0)
ck('outward_noise',s.Rational(14,48**2)<s.Rational(25,64**2))
ck('confidence_exp_bound',sum(F(8)**k/factorial(k) for k in range(12))>400)
ck('interval',F(1,2)-F(25,192)==F(71,192) and F(1,2)+F(25,192)==F(121,192))
a,b,c0,d0,x=s.symbols('a b c d x')
ck('log_concavity_induction_identity',s.expand((b+x*c0)**2-(a+x*b)*(c0+x*d0)-(b*b-a*c0+x*(b*c0-a*d0)+x*x*(c0*c0-b*d0)))==0)
def es(o,k):
 v=[F(1)]+[F(0)]*len(o)
 for z in o:
  for j in range(len(o),0,-1):v[j]+=z*v[j-1]
 return v[k] if 0<=k<=len(o) else F(0)
def odds(p):return p/(1-p)
def eff(p,q,t):return odds(q)*F(len(p)-t+1,t)*es([odds(z) for z in p],t-1)/es([odds(z) for z in p],t)
lo=[F(1,4),F(1,2)];hi=[F(1,2),F(3,4)]
ck('sharp_box_t1',(eff(hi,F(1,2),1),eff(lo,F(1,2),1))==(F(1,2),F(3,2)))
ck('sharp_box_t2',(eff(hi,F(1,2),2),eff(lo,F(1,2),2))==(F(2,3),F(2)))
cases=0
for ps in product([F(1,4),F(1,2),F(3,4)],repeat=3):
 for q in [F(1,4),F(1,2),F(3,4)]:
  for t in [1,2,3]:
   rr=eff(list(ps),q,t)
   for j in range(3):
    pp=list(ps);pp[j]=(pp[j]+1)/2
    assert eff(pp,q,t)<=rr
   # Compare labelled Bernoulli count probabilities before the hidden permutation.
   probs=[]
   for k in [t-1,t]:
    z=F(0)
    for labels in product([0,1],repeat=3):
     if sum(labels)==k:
      vv=F(1)
      for p,v in zip(ps,labels):vv*=p if v else 1-p
      z+=vv
    probs.append(z)
   assert rr==odds(q)*F(4-t,t)*probs[0]/probs[1];cases+=1
ck('all_heterogeneous_exact_cases',cases==243)
ck('score_normalizer',F(3,2)/(F(3,2)+2)==F(3,7) and 1/F(3,7)==F(7,3))
ctrl('coarse_envelope_loses_evidence',F(7,3)>F(5,3))
ctrl('hindsight_weight_bias',sum(F(max(z),4) for z in product([0,1],repeat=2))==F(3,4))
A=F(1,9);D=F(1,72);f=[max(A-D*r,0) for r in range(1,10)]
chi=F(1)
for v in f:
 p=F(1,2)+v;q=F(1,2)-v
 single=p*p/q+(1-p)**2/(1-q)
 assert single==1+16*v*v/(1-4*v*v)
 chi*=single
ck('seven_distinguishing_innovations',sum(v!=0 for v in f)==7)
ck('exact_chisquare_product',chi==F(4292603444493,2815640580500))
ck('TV_strict_bound',chi<2)
ck('width_probability',1-2*F(1,20)-F(1,2)==F(2,5) and 2*A==F(2,9))
# Exhaustive direct likelihood product, independently of the factorization.
direct=F(0)
for labels in product([0,1],repeat=7):
 pp=qq=F(1)
 for v,z in zip(f,labels):
  pp*=F(1,2)+v if z else F(1,2)-v
  qq*=F(1,2)-v if z else F(1,2)+v
 direct+=pp*pp/qq
ck('128_histories_direct_chisquare',direct==chi)
ctrl('omitted_drift_creates_population_bias',sum(f[:7],F(0))/7!=A)
ctrl('old_samples_do_not_distinguish',all(max(A-D*r,0)==0 for r in range(8,80)))
ctrl('pool_average_substitution_fails',eff([F(1,4),F(3,4)],F(1,2),1)!=1)
deps=['explorations/conditional-build/k2403-drift-robust-calibration-2026-10-31.md','tests/channel-swings/k2403_drift_robust_calibration_probe.py']
report={'result_id':'K2406','checks':checks,'controls':controls,'exact_pool_cases':cases,'likelihood_histories':128,'chi_square_plus_one':str(chi),'taper_radius':'(5+sqrt(11))/64','scope':'Written martingale, optimization and testing proofs with exact finite fixtures; no empirical drift or GU verdict.','dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps}}
p=R/'lab/process/k2406-optimal-local-calibration.json'
if '--write' in sys.argv:p.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
else:assert json.loads(p.read_text())==report
print(json.dumps(report,sort_keys=True))
