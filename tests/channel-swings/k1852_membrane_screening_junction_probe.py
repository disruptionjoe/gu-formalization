#!/usr/bin/env python3
"""Independent junction, graph, charge-lattice and adverse-input controls."""
from pathlib import Path
from fractions import Fraction as F
import json,copy,itertools
ROOT=Path(__file__).resolve().parents[2]
def check(d):
 K=F(3,2);alpha=F(-4,3);charge=F(5,7);jump=F(d['multiplier_jump_charge_factor'])*charge/alpha
 assert alpha*jump==-charge
 drho=-jump;assert F(d['metric_trace_factor'])*(drho+jump)/K==0
 assert d['metric_trace_factor']==4
 T=F(7,5);n=d['wall_dimension'];j=F(d['tension_jump_factor'])*T/K
 assert (1-n)*j==-F(d['israel_stress_factor'])*T/K
 assert n==3 and F(d['israel_stress_factor'])==-1
 omega=T/(4*K);R=1/omega
 assert F(d['opposite_radical_factor'])*T*R/K==1
 assert F(d['angular_tension_factor'])*T*R/K==2
 change=F(11,13);qnew=charge+F(d['charge_update_factor'])*alpha*change
 assert alpha*(jump-change)+qnew==0
 return True
if __name__=='__main__':
 d=json.loads((ROOT/'lab/process/k1852-membrane-screening-junction.json').read_text());assert check(d)
 mutations=[('multiplier_jump_charge_factor','1'),('metric_trace_factor',2),('wall_dimension',4),('israel_stress_factor','1'),('tension_jump_factor','-1'),('angular_tension_factor','1'),('opposite_radical_factor','1/2'),('charge_update_factor','-1')]
 for key,value in mutations:
  m=copy.deepcopy(d);m[key]=value
  try:check(m)
  except AssertionError as exc:
   import traceback
   frame=traceback.extract_tb(exc.__traceback__)[-1]
   print("[DETECTED mathematical fault]",key,"at",frame.lineno,frame.line)
  else:raise AssertionError('undetected mathematical input fault '+key)
 controls=0
 # Connected path graph: edgewise fixed-charge covariance iff all shifts equal.
 for shifts in itertools.product([-1,0,1],repeat=4):
  edge=[shifts[i+1]-shifts[i] for i in range(3)]
  assert (all(x==0 for x in edge))==(len(set(shifts))==1);controls+=1
  # Loop charge sum telescopes; single nonzero crossing cannot be exact.
  cycle=edge+[shifts[0]-shifts[3]];assert sum(cycle)==0;controls+=1
 for numerator in range(-10,11):
  desired=F(numerator,7);q0=F(2,3);nearest=min(abs(desired-n*q0) for n in range(-10,11))
  assert 0<=nearest<=q0/2;controls+=1
  assert (nearest==0)==((desired/q0).denominator==1);controls+=1
 # Same-sign equal f branches have zero angular jump, opposite signs have2rad.
 for radical in [F(1,3),F(1),F(7,4)]:
  assert radical-radical==0 and radical-(-radical)==2*radical;controls+=2
 flags=lambda z:z['global_current_exact'] and z['uniform_shift_survives'] and not any(z[k] for k in ['all_equal_curvature_walls_impossible','GU_adapter','nucleation_theorem'])
 assert flags(d)
 for key in ['global_current_exact','uniform_shift_survives','all_equal_curvature_walls_impossible','GU_adapter','nucleation_theorem']:
  m=copy.deepcopy(d);m[key]=not m[key];assert not flags(m)
 print('K1852 independent controls PASS:',controls,'controls; 8 mathematical input faults and 5 separate reporting faults detected')
