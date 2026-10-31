"""Exact coupled-drift fixtures; proofs live in the note, no measured observations."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product, permutations
import hashlib,json,sys
import sympy as s
R=Path(__file__).resolve().parents[2]
checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ctrl(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
def odds(p):return p/(1-p)
def es(o,k):
 vals=[F(1)]+[F(0)]*len(o)
 for z in o:
  for j in range(len(o),0,-1):vals[j]+=z*vals[j-1]
 return vals[k] if 0<=k<=len(o) else F(0)
def eff(p,q,t):
 o=list(map(odds,p));return odds(q)*F(len(p)-t+1,t)*es(o,t-1)/es(o,t)
def feasible(v,lo,hi,d):
 return all(lo[i]<=v[i]<=hi[i] for i in range(len(v))) and all(abs(v[i]-v[j])<=d[i][j] for i in range(len(v)) for j in range(len(v)))
def envelopes(lo,hi,d):
 n=len(lo)
 return ([max(lo[j]-d[i][j] for j in range(n)) for i in range(n)],
         [min(hi[j]+d[i][j] for j in range(n)) for i in range(n)])
# All lattice possibilities independently establish feasibility for these finite fixtures.
ends=[F(1,4),F(1,2),F(3,4)]
intervals=[(a,b) for a in ends for b in ends if a<=b]
grid=[F(k,8) for k in range(2,7)];f_cases=0;nonempty=0
for bounds in product(intervals,repeat=3):
 lo,hi=map(list,zip(*bounds))
 for L in [F(0),F(1,8),F(1,4)]:
  d=[[L*abs(i-j) for j in range(3)] for i in range(3)]
  condition=all(lo[i]<=hi[j]+d[i][j] for i in range(3) for j in range(3))
  valid=[v for v in product(grid,repeat=3) if feasible(v,lo,hi,d)]
  assert bool(valid)==condition
  a,b=envelopes(lo,hi,d)
  if condition:
   assert feasible(a,lo,hi,d) and feasible(b,lo,hi,d)
   assert all(all(a[i]<=v[i]<=b[i] for i in range(3)) for v in valid)
   nonempty+=1
  f_cases+=1
ck('finite_feasibility_and_simultaneous_extremal_witnesses',f_cases==648 and nonempty>0)
# Whole-cell identities; signs established analytically in the note and checked at exact range extrema.
x=s.symbols('x',real=True)
UP=[(3*x*(9-8*x),(1-x)*(8*x+3)),(x*(32*x*x-76*x+45),(1-x)*(-32*x*x+44*x-7))]
LOW=[(x*(32*x*x-52*x+21),(1-x)*(-32*x*x+20*x+5)),(x*(7-8*x),(1-x)*(11-8*x))]
upcert=[3*(2*x-1)*(8*x-15),(2*x-1)*(128*x*x-240*x+105)]
locert=[(2*x-1)*(64*x*x-72*x+15),(2*x-1)*(33-40*x)]
ck('upper_whole_cell_polynomial_identities',all(s.expand(15*d-7*n-v)==0 for (n,d),v in zip(UP,upcert)))
ck('lower_whole_cell_polynomial_identities',all(s.expand(7*n-3*d-v)==0 for (n,d),v in zip(LOW,locert)))
ck('whole_cell_sign_certificates',128*F(5,8)**2-240*F(5,8)+105==5 and 256*F(5,8)-240<0 and 64*F(3,8)**2-72*F(3,8)+15==-3 and 128*F(1,2)-72<0 and 33-40*F(5,8)==8)
def tube(x):
 return ([max(F(1,4),x-F(1,8)),max(F(1,4),x-F(1,4))],
         [min(F(3,4),x+F(1,8)),min(F(3,4),x+F(1,4))])
symbolic_tubes=[([x-s.Rational(1,8),s.Rational(1,4)],[x+s.Rational(1,8),x+s.Rational(1,4)]),([x-s.Rational(1,8),x-s.Rational(1,4)],[x+s.Rational(1,8),s.Rational(3,4)])]
for branch,(aa,bb) in enumerate(symbolic_tubes):
 for vector,forms in [(aa,UP),(bb,LOW)]:
  nn,dd=forms[branch]
  original=2*x/(1-x)/sum(z/(1-z) for z in vector)
  ck('original_odds_whole_cell_'+str(branch)+'_'+('upper' if forms is UP else 'lower'),s.cancel(original-nn/dd)==0)
amin,bmax=tube(F(1,2))
ck('sharp_t1_attainment',eff(bmax,F(1,2),1)==F(3,7) and eff(amin,F(1,2),1)==F(15,7))
ck('sharp_t2_attainment',eff(bmax,F(1,2),2)==F(7,15) and eff(amin,F(1,2),2)==F(7,3))
ck('rectangular_relaxation',eff([F(3,4)]*2,F(3,8),1)==F(1,5) and eff([F(1,4)]*2,F(5,8),1)==5)
ctrl('rectangle_extreme_corner_is_infeasible',not feasible([F(5,8),F(1,4),F(1,4)],[F(3,8),F(1,4),F(1,4)],[F(5,8),F(3,4),F(3,4)],[[F(abs(i-j),8) for j in range(3)] for i in range(3)]))
# Affine subset interior extremum: r=N/(N+1), N=49/32-8(x-7/16)^2.
N=x*(7-8*x);D=(1-x)*(8*x+1)
ck('interior_stationary_maximum_identity',s.expand(D-N-1)==0 and s.expand(N-s.Rational(49,32)+8*(x-s.Rational(7,16))**2)==0)
ctrl('endpoint_only_coupled_optimizer_misses_maximum',F(49,81)>max(F(5,9),F(3,7)) and eff([F(9,16)],F(7,16),1)==F(49,81))
# Full original hidden-role experiment, independently of odds formula.
def original_assignment(params,labels):
 masses=[F(0)]*len(params)
 for perm in permutations(range(len(params))):
  prob=F(1,6)
  for pos,src in enumerate(perm):prob*=params[src] if labels[pos] else 1-params[src]
  masses[perm.index(0)]+=prob
 total=sum(masses)
 return [z/total for z in masses]
pool_cases=0
for q in [F(k,32) for k in range(12,21)]:
 for p in product([F(k,16) for k in range(4,13)],repeat=2):
  if abs(p[0]-q)>F(1,8) or abs(p[1]-q)>F(1,4) or abs(p[0]-p[1])>F(1,8):continue
  a,b=tube(q)
  assert all(a[i]<=p[i]<=b[i] for i in range(2))
  for labels in [(1,0,0),(1,1,0)]:
   t=sum(labels);post=original_assignment([q]+list(p),labels);r=eff(p,q,t)
   assert post==[r/(t*r+3-t) if z else 1/(t*r+3-t) for z in labels]
   assert F(3,7)<=r<=F(15,7) if t==1 else F(7,15)<=r<=F(7,3)
   # Single-bonus score consumer with the correct robust normalizer.
   c=F(15,29) if t==1 else F(7,17)
   assert post[0]/c<=1
   pool_cases+=1
ck('original_hidden_role_probabilities_and_actual_e_factor',pool_cases>0)
ck('sharp_consumer_attainment',original_assignment([F(1,2)]+amin,[1,0,0])[0]==F(15,29))
ck('consumer_factor_improvement',1/F(15,29)==F(29,15) and 1/F(5,7)==F(7,5) and F(29,15)>F(7,5))
# Changed-assumption control: same marginals but copying destroys product likelihood.
# q=p1=p2=1/2 marginally; science fair independent of copied calibration labels.
# Conditional on total1, science must be1; iid formula would assign probability1/3.
dep_total=dep_science_one=F(0)
marginals=[F(0)]*3
for science,copied in product([0,1],repeat=2):
 labels=[science,copied,copied]
 for i,z in enumerate(labels):marginals[i]+=F(z,4)
 if sum(labels)==1:
  dep_total+=F(1,4);dep_science_one+=F(science,4)
ctrl('marginal_fairness_does_not_supply_independent_pool',marginals==[F(1,2)]*3 and dep_science_one/dep_total==1 and original_assignment([F(1,2)]*3,[1,0,0])[0]==F(1,3))
# Honest adaptation under stationary history, not merely under a rough alternative.
a=F(1,9);L=F(1,72);f=[max(a-L*r,0) for r in range(1,8)]
chi_plus_one=F(1)
for v in f:
 p=F(1,2)+v;single=p*p/F(1,2)+(1-p)**2/F(1,2)
 assert single==1+4*v*v;chi_plus_one*=single
ck('stationary_reference_chisquare_exact',chi_plus_one==F(164741122962235625,148074416822550528))
ck('stationary_reference_TV_bound',chi_plus_one<F(9,8) and F(1,32)<F(1,25))
direct=F(0);histories=0
for bits in product([0,1],repeat=7):
 pa=F(1)
 for z,v in zip(bits,f):pa*=F(1,2)+v if z else F(1,2)-v
 direct+=pa*pa/F(1,128);histories+=1
ck('original_128_history_likelihood_sum',direct==chi_plus_one and histories==128)
ck('width_probability_under_stationary_truth',1-2*F(1,20)-2*F(1,5)==F(1,2) and 2*a==F(2,9))
ck('ramp_integral_scale_bound',sum(v*v for v in f)<=a**3/(3*L))
ctrl('arbitrarily_many_older_observations_identical',all(max(a-L*r,0)==0 for r in range(8,108)))
# Exact same-history full-current-range control, even with finite (unspecified) Lipschitz bound.
models=[[F(0)]+[F(1,2)]*7,[F(1)]+[F(1,2)]*7]
same_likelihoods=True
for bits in product([0,1],repeat=7):
 masses=[]
 for model in models:
  prob=F(1)
  for z,p in zip(bits,model[1:]):prob*=p if z else 1-p
  masses.append(prob)
 same_likelihoods &= masses[0]==masses[1]
ctrl('unbounded_future_drift_current_zero_or_one_share_history',same_likelihoods and models[0][0]==0 and models[1][0]==1 and all(abs(model[i]-model[i+1])<=F(1,2) for model in models for i in range(7)))
deps=['explorations/conditional-build/k2406-optimal-local-calibration-2026-10-31.md','tests/channel-swings/k2406_optimal_local_calibration_probe.py']
report={'result_id':'K2409','checks':checks,'controls':controls,'finite_feasibility_cases':f_cases,'nonempty_feasibility_cases':nonempty,'original_pool_cases':pool_cases,'original_likelihood_histories':histories,'stationary_reference_chi_square_plus_one':str(chi_plus_one),'sharp_t1_odds':['3/7','15/7'],'sharp_t2_odds':['7/15','7/3'],'realized_max_factor':'29/15','scope':'Conditional mathematical derivation with exact finite fixtures; no empirical calibration or native GU verdict.','dependencies':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in deps}}
out=R/'lab/process/k2409-coupled-drift-calibration.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
else:assert json.loads(out.read_text())==report
print(json.dumps(report,sort_keys=True))
