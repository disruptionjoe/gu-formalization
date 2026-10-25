"""Bath-label replay of all three regimes; imported necessity is kept separate."""
from fractions import Fraction as Q
from pathlib import Path
import json,hashlib,copy
from k2045_third_thermal_spacing_phase_probe import physical
ROOT=Path(__file__).resolve().parents[2]
def replay(r):
 E=Q(r['energy']);R=[Q(4,19),Q(6,19),Q(9,19)];C=[Q(3,8),Q(9,16),Q(1,16)];X=[Q(8,23),Q(12,23),Q(3,23)]
 ER,EC,EX=Q(67,19),Q(19,8),Q(59,23);m=(ER-E)/(ER-EC-Q(1,2));ss=list(map(Q,[1,3,5]));n=(E-EX)/(ER-EX)
 half=physical(ss+[x+Q(1,2) for x in ss],[(1-m)*x for x in R]+[m*x for x in C],list(map(Q,range(7)))+[Q(x)+Q(1,2) for x in range(7)],Q(1,2));assert half==(E,Q(r['regimes'][0]['value'])),'half boundary witness'
 pp=[(1-n)*x+n*y for x,y in zip(X,R)];wide=physical(ss,pp,list(map(Q,range(7))),Q(1));assert wide==(E,Q(r['regimes'][1]['value'])),'wide witness'
 for d in [Q(1001,1000),Q(3,2),Q(2)]:
  e,v=physical([Q(2)],[Q(1)],list(map(Q,[0,2,4])),d);assert e<=E and v==Q(r['regimes'][2]['value']),'superunit witness'
 assert Q(r['jumps']['half'])==wide[1]-half[1],'half jump'
 assert Q(r['jumps']['one'])==Q(1,2)-wide[1],'one jump'
 for p in r['high_energy_jump_at_one']:
  a,s=map(Q,p['jump_at_one']);lo,hi=map(Q,p['interval']);original={'XR':(Q(79,140),-Q(13,140)),'RQ':(Q(21,44),-Q(3,44)),'QB':(Q(81,212),-Q(9,212))}[p['name']]
  for e in [lo,(lo+hi)/2,hi]:assert a+s*e==Q(1,2)-(original[0]+original[1]*e)>0,'whole segment jump formula'
 # Physical deletions test realization necessity, not an exhaustive optimizer proof.
 removed=0
 for support,pop,spec,d in [(ss,pp,list(map(Q,range(7))),Q(1)),([Q(2)],[Q(1)],list(map(Q,[0,2,4])),Q(2))]:
  for x in spec:
   try:physical(support,pop,[y for y in spec if y!=x],d)
   except AssertionError as e:assert str(e) in ['shell capacity','spectrum'];removed+=1
   else:raise AssertionError('completion deletion accepted')
 assert [x['minimum_physical_levels'] for x in r['regimes']]==[14,7,3,None],'imported dimension custody'
 return dict(physical_regime_witnesses=5,exact_jump_values=2,affine_formulas=3,completion_deletions=removed)
if __name__=='__main__':
 r=json.loads((ROOT/'lab/process/k2051-composed-spacing-transitions.json').read_text())
 for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 print('BASELINE',replay(r));faults=[]
 for kind in ['half','wide','superunit','jump']:
  b=copy.deepcopy(r)
  if kind=='jump':b['jumps']['one']='72/280'
  else:b['regimes'][['half','wide','superunit'].index(kind)]['value']='1/3'
  try:replay(b)
  except AssertionError as e:assert str(e);faults.append([kind,str(e)])
  else:raise AssertionError('missed '+kind)
 print('PASS four mathematical faults',faults)
