#!/usr/bin/env python3
"""Exact algebraic controls for the declared classical thin-wall action."""
from pathlib import Path
from fractions import Fraction as Q
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]
def verify(d):
 count=0
 for alpha in [Q(-2),Q(1,2),Q(3)]:
  for drho in [Q(-3),Q(0),Q(5,2)]:
   q=alpha*drho;dl=Q(d['multiplier_jump_charge_factor'])*q/alpha
   assert alpha*dl+q==0 and drho+dl==0;count+=2
   for offset in [Q(-1,3),Q(2,5)]:
    assert drho+Q(d['multiplier_jump_charge_factor'])*(q+offset)/alpha==-offset/alpha;count+=1
   Cminus=Q(2,3);Cplus=Q(-3,5)
   qnew=q+Q(d['charge_update_factor'])*alpha*(Cplus-Cminus)
   assert alpha*(dl-Cplus+Cminus)+qnew==0;count+=1
 for K in [Q(1),Q(2),Q(5,3)]:
  for T in [Q(0),Q(1,2),Q(3)]:
   z=Q(d['tension_jump_factor'])*T/K;trace=d['wall_dimension']*z
   assert z-trace==-Q(d['israel_stress_factor'])*T/K;count+=1
   if T:
    R=4*K/T;rad=Q(d['opposite_radical_factor'])*T*R/K
    assert 2*rad==Q(d['angular_tension_factor'])*T*R/K;count+=1
    # H=0 turning point: rad²=1, Rdot=0. Temporal acceleration gives same curvature.
    assert rad*rad==1 and 1/R==T/(4*K);count+=2
 assert d['wall_dimension']==3 and d['metric_trace_factor']==4
 assert Q(d['israel_stress_factor'])==-1
 # Exact rational hyperbolic controls c²-s²=1, no sampled trajectory claim.
 for t in [Q(0),Q(1,3),Q(2,3)]:
  c=(1+t*t)/(1-t*t);s=2*t/(1-t*t)
  for omega in [Q(1,2),Q(2)]:
   R=c/omega;Rdot=s;assert Rdot**2==omega**2*R**2-1;count+=1
 for dep in d['dependencies']:assert hashlib.sha256((ROOT/dep['path']).read_bytes()).hexdigest()==dep['sha256']
 assert d['global_current_exact'] and d['uniform_shift_survives']
 assert not d['all_equal_curvature_walls_impossible'] and not d['GU_adapter'] and not d['nucleation_theorem']
 return count
if __name__=='__main__':
 d=json.loads((ROOT/'lab/process/k1852-membrane-screening-junction.json').read_text());print('K1852 exact algebra controls PASS:',verify(d),'checks; continuum claims remain in written proof')
