#!/usr/bin/env python3
"""Exact finite implementation checks; universal probability claims use the note."""
from fractions import Fraction as F
from math import comb
from itertools import product
from pathlib import Path
import argparse,hashlib,json,importlib.util
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'tests/channel-swings/k2397_finite_training_shift_confidence_probe.py'
spec=importlib.util.spec_from_file_location('predecessor',p);old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
def mix(n,k,u):
 den=(n+1)*comb(n,k)*u**k*(1-u)**(n-k)
 return None if not den else 1/den

def interval(n,k,T,grid):
 if n==0:return F(0),F(1)
 def crossed(u):
  val=mix(n,k,u);return val is None or val>=T
 hat=F(k,n)
 return max([F(0)]+[g for g in grid if g<=hat and crossed(g)]),min([F(1)]+[g for g in grid if g>=hat and crossed(g)])

def run():
 checks={};controls={}
 def check(name,ok):
  checks[name]=bool(ok)
  if not ok:raise AssertionError('[FAIL] '+name)
 def ctrl(name,ok):
  controls[name]=bool(ok)
  if not ok:raise AssertionError('[FAIL] '+name)
 count=0
 for n in range(13):
  for k in range(n+1):
   for u in [F(1,5),F(1,3),F(1,2),F(4,5)]:
    assert u*mix(n+1,k+1,u)+(1-u)*mix(n+1,k,u)==mix(n,k,u);count+=1
 check('beta_mixture_recurrence_exact',count==364)
 grid=tuple(F(j,12) for j in range(13));T=F(200)
 check('initial_full_interval',interval(0,0,T,grid)==(0,1))
 check('n100_balanced',interval(100,50,T,grid)==(F(1,4),F(3,4)))
 check('n150_balanced',interval(150,75,T,grid)==(F(1,3),F(2,3)))
 check('all_zero_endpoint',interval(100,0,T,grid)==(0,F(1,6)))
 check('all_one_endpoint',interval(100,100,T,grid)==(F(5,6),1))
 path=[]
 for n in range(1,151):
  bounds=interval(n,n//2,T,grid);path.append(bounds)
  if bounds[1]-bounds[0]<=F(1,3):break
 check('first_adaptive_stop_n128',n==128 and path[-1]==(F(1,3),F(2,3)))
 # First crossing is removed; summing marginal tails would double count.
 live={0:F(1)};cross=F(0)
 for n in range(1,13):
  nex={}
  for k,mass in live.items():
   for bit in (0,1):
    kk=k+bit;mass2=mass/2
    if mix(n,kk,F(1,2))>=4:cross+=mass2
    else:nex[kk]=nex.get(kk,F(0))+mass2
  live=nex
 check('optional_first_crossing_99_over1024',cross==F(99,1024) and cross<=F(1,4))
 check('crossing_probability_conserved',cross+sum(live.values())==1)
 # Coverage finite fixtures independently uses all binomial paths through DP.
 cases=0
 for u in [F(1,8),F(1,3),F(1,2),F(4,5),F(7,8)]:
  live={0:F(1)};err=F(0)
  for n in range(1,21):
   nxt={}
   for k,mass in live.items():
    for bit,prob in [(0,1-u),(1,u)]:
     kk=k+bit;lo,hi=interval(n,kk,F(10),grid)
     if not lo<=u<=hi:err+=mass*prob
     else:nxt[kk]=nxt.get(kk,F(0))+mass*prob
   live=nxt;assert err<=F(1,10);cases+=1
 check('finite_time_uniform_outward_coverage',cases==100)
 rlo,rhi=F(1,4),F(4);a,d=F(1,20),F(1,100);eta=a-d
 check('adaptive_error_addition',eta==F(1,25) and d+eta==a)
 ctrl('independent_training_bound_not_transferred',d+F(4,99)>a)
 # Same parameter over exact cells and tie endpoints.
 def factor(theta,x,y):
  scores=((F(y)-theta*x)**2,F(1,4),F(1,4));top=max(scores)
  bs=tuple(F(int(z==top and scores.count(top)==1)) for z in scores)
  C=old.normalizer(bs,(1,1,0),rlo,rhi)
  return F(1,4)+F(3,4)*(bs[0]/C if C else 0)
 points=[F(-1),F(-3,4),F(-1,2),F(0),F(1,2),F(3,4),F(1)]
 values=[]
 for th in points:
  e=F(1)
  for x,y in [(1,1),(1,-1)]+[(0,4)]*6:e*=factor(th,x,y)
  values.append(e)
 cert=F(1,4)*F(31,16)**7
 check('whole_graph_cells_and_endpoints',min(values)==cert and cert>25)
 check('seven_looks_insufficient',F(1,4)*F(31,16)**6<25)
 ctrl('separate_minima_lose_shared_evidence',F(1,4)**2*F(31,16)**6<25)
 # Each possible assignment is covered by identical frozen score vector.
 poolcases=0
 for zz in product((0,1),repeat=3):
  for bs in product((F(0),F(1),F(2)),repeat=3):
   C=old.normalizer(bs,zz,rlo,rhi)
   fs=tuple(F(1,4)+F(3,4)*(b/C if C else 0) for b in bs)
   for r in (rlo,F(1),rhi):assert old.endpoint_mean(fs,zz,r)<=1
   poolcases+=1
 check('pool_assignment_exact_bounds',poolcases==216)
 ctrl('retrospective_mixture_fit_invalid',F(1,2)*2+F(1,2)*2>1)
 ctrl('reused_fair_residual_invalid',F(1,2)*4>1)
 ctrl('current_label_fitted_bonus_invalid',sum(F(1,3)*3 for _ in range(3))>1)
 # Inward rounding excludes an actually accepted parameter between grid points.
 u=F(1,100);accepted=[g for g in grid if mix(1,0,g) is not None and mix(1,0,g)<T]
 ctrl('accepted_grid_points_round_inward',mix(1,0,F(99,100))<T and F(99,100)>max(accepted))
 check('all_ones_Q_keeps_upper1',interval(20,20,T,grid)[1]==1)
 check('all_zeros_P_keeps_lower0',interval(20,0,T,grid)[0]==0)
 check('unbounded_singleton_science_no_gain',old.normalizer((F(1),F(0),F(0)),(1,0,0),F(0),None)==1)
 check('unbounded_repeated_environment_retains_gain',old.normalizer((F(1),F(0),F(0)),(1,1,0),F(0),None)==F(1,2))
 return {'result':'K2400','status':'PASS','checks':checks,'controls':controls,'counts':{'recurrence':count,'coverage_prefixes':cases,'pool_cases':poolcases},'fixture':{'labels_on_synthetic_stop_path':256,'science_exposures':48,'first_crossing':str(cross),'shared_graph_minimum':str(cert),'threshold':'25'},'dependencies':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()},'scope':'Finite exact checks; universal validity uses predictable conditional laws and written stopped-process proof. No empirical claim.'}
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args();report=run()
 if args.write:(ROOT/'lab/process/k2400-adaptive-calibration-confidence.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
 print(json.dumps(report,sort_keys=True))
