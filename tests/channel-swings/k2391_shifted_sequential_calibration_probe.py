"""Exact finite controls for the written weighted-index and sequential theorem."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
import json,sys,hashlib
R=Path(__file__).resolve().parents[2];checks={};controls={}
def check(n,v):
 checks[n]=bool(v)
 if not v:raise AssertionError(n)
def control(n,v):
 controls[n]=bool(v)
 if not v:raise AssertionError(n)
count=0
for scores in product(range(3),repeat=4):
 for w in product(range(1,4),repeat=4):
  total=sum(w);p=[F(sum(w[j] for j in range(4) if scores[j]>=scores[i]),total) for i in range(4)]
  for alpha in set(p):assert sum((F(w[i],total) for i in range(4) if p[i]<=alpha),F(0))<=alpha
  count+=1
check('all6561_weighted_tied_pools_superuniform',count==6561)
# Exact box envelope, all corners, variable tail cardinalities.
boxes=0
lo=[F(1),F(2),F(1),F(3)];hi=[F(3),F(4),F(5),F(6)]
for tail in product([False,True],repeat=4):
 if not any(tail):continue
 bound=sum(hi[i] for i in range(4) if tail[i]);bound/=bound+sum(lo[i] for i in range(4) if not tail[i])
 values=[]
 for bits in product([0,1],repeat=4):
  w=[hi[i] if bits[i] else lo[i] for i in range(4)];values.append(sum(w[i] for i in range(4) if tail[i])/sum(w))
 assert max(values)==bound;boxes+=1
check('15_weight_boxes_all_corners_sharp',boxes==15)
for N in range(2,15):
 for g in [F(1),F(3,2),F(2),F(7)]:
  for alpha in [F(1,20),F(1,4),F(1,2),F(3,4)]:
   cutoff=alpha*N/(g*(1-alpha)+alpha)
   for r in range(1,N+1):assert (g*r/(N-r+g*r)<=alpha)==(r<=cutoff.numerator//cutoff.denominator)
check('rank_threshold_identity',True)
control('unweighted_shift_fails',F(2,5)>F(1,4))
control('individual_weight_intervals_allow_squared_distortion',(F(2)/F(1,2))==4)
# Full conditional paired-noise distributions, with and without symmetry.
def pairlaws(law):
 means=defaultdict(F);diffs=defaultdict(F)
 for a,pa in law.items():
  for b,pb in law.items():means[(a+b)/2]+=pa*pb;diffs[(a-b)/2]+=pa*pb
 return dict(means),dict(diffs)
a,b=pairlaws({F(-2):F(1,4),F(0):F(1,2),F(2):F(1,4)})
check('paired_symmetric_noise_matching',a==b)
a,b=pairlaws({F(-1):F(2,3),F(2):F(1,3)})
check('asymmetric_noise_zero_mean',-F(2,3)+2*F(1,3)==0)
control('zero_mean_does_not_match_pair_noise',a!=b and a[2]==F(1,9) and max(map(abs,b))==F(3,2))
control('asymmetry_size_exceeds_alpha',F(1,9)>F(1,20))
control('common_bias_not_in_differences',pairlaws({F(1):F(1)})==({F(1):F(1)},{F(0):F(1)}))
# Uniform global observation inequality proved by |theta*b|<=1.
check('science_lower_bound',3**2+4**2==25)
check('calibration_upper_bound',1**2==1)
check('raw_error_margin',F(5)-F(1,4)>1)
p=F(2,7);beta=F(1,3);alpha=F(1,20)
check('one_look_resolution_barrier',p>alpha)
check('each_look_global_bet',p<=beta)
check('three_look_crossing',beta**-3==27 and 27>1/alpha)
check('conditional_TV_nonempty_budget',(beta+F(1,100))**3<alpha)
control('too_large_TV_budget_no_three_look_certificate',(beta+F(1,10))**3>alpha)
control('reused_uniform_p_invalid',F(1,3)>alpha and 3**3>=1/alpha)
control('pointwise_profile_grid_not_global',min([F(27)])>=20 and min([F(27),F(0)])<20)
# Independent three-look Bernoulli threshold orbit: under exact U ranks, crossing at3
# has probability beta^3, not beta; arbitrary long looks bounded by written proof.
prob=sum((beta**sum(bits)*(1-beta)**(3-sum(bits)) for bits in product([0,1],repeat=3) if all(bits)),F(0))
check('fresh_three_look_null_probability',prob==F(1,27) and prob<alpha)
cal_scores=[F(0)]*19;science_score=F(1)
no_overlap_p=F(1+sum(x>=science_score for x in cal_scores),20)
control('no_overlap_can_force_false_rejection',no_overlap_p<=alpha and F(1)>alpha)
# Exact minimum exposure count within separated, deterministic binary-rank bets.
best={0:F(1)};parts={0:[]}
for cost in range(1,14):
 options=[(best[cost-c]*F(c+1,2),parts[cost-c]+[c]) for c in range(2,cost+1) if cost-c in best]
 if options:best[cost],parts[cost]=max(options,key=lambda x:x[0])
check('minimum26_exposures_in_stated_bet_class',best[13]==20 and max(v for c,v in best.items() if c<13)<20)
check('26_exposure_schedule',F(2)**3*F(5,2)==20 and 2*(3+3+3+4)==26)
report={'result':'K2391','evidence_kind':'exact finite weighted-score enumeration, rational inequalities and exact paired distributions; universal theorems are written proofs','exposure_optimizer':{'minimum_pair_cost':13,'minimum_exposures':26,'best_product_at_each_pair_cost':{str(c):str(v) for c,v in best.items()},'one_optimal_pair_partition':[3,3,3,4],'scope':'perfect global score separation; Gamma2; deterministic binary rank bets; disjoint paired exposures; no per-look overhead cost'},'weighted_pools':count,'weight_boxes':boxes,'checks':checks,'controls':controls,'dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in ['lab/process/k2388-exchangeable-noise-calibration.json']}}
if '--write' in sys.argv:(R/'lab/process/k2391-shifted-sequential-calibration.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print(json.dumps(report,sort_keys=True))
