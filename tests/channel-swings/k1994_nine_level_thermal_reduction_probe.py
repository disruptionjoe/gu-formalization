"""Independent raw shell census and fixed-budget probability-arrangement solver."""
from fractions import Fraction as F
from itertools import product,combinations
from pathlib import Path
import json,copy
from k1992_wide_spacing_eight_level_rigidity_probe import minimum,ok
ROOT=Path(__file__).resolve().parents[2]
def independent_census():
 found={};small=[];count=0
 for n in range(3,10):
  for word in product([1,2,3],repeat=n-1):
   A=[0]
   for step in word:A.append(A[-1]+step)
   count+=1
   for k in range(1,(n-1)//2+1):
    for S in combinations(A[1:-1],k):
     if ok(A,S):
      found[S]=min(n,found.get(S,99))
      if n<=6 and k==2 and S[-1]-S[0]<=3:small.append((tuple(A),S))
 return found,small,count

def check(d,cache=None):
 if cache is None:
  found,small,count=independent_census();computed={};supports=[list(map(F,b['S'])) for b in d['pareto_blocks']]+[sorted(map(F,b['support'])) for b in d['shifted_templates']]
  for E in [F(7,5),F(2),F(3)]:
   computed[E]=min(v for S in supports if (v:=minimum(F(1,2),S,E)) is not None)
  cache=found,small,count,computed
 found,small,count,computed=cache
 assert count==d['connected_shape_count']==9837,'complete connected enumeration'
 assert set(small)=={(tuple(b['spectrum']),tuple(b['support'])) for b in d['improving_small_components']},'complete improving component list'
 assert len(small)==17,'small component count'
 bs=d['pareto_blocks'];n=0
 for S,k in found.items():
  assert any(len(b['A'])<=k and b['S'][0]<=S[0] and tuple(x-b['S'][0] for x in b['S'])==tuple(x-S[0] for x in S) for b in bs),'Pareto support coverage';n+=1
 for b in bs:assert ok(b['A'],b['S']),'actual connected shells'
 assert len(d['shifted_templates'])==6,'six physical placements'
 for b in d['shifted_templates']:
  A=list(map(F,b['spectrum']));S=list(map(F,b['support']))
  assert len(A)<=9 and len(set(A))==len(A) and min(y-x for x,y in zip(A,A[1:]))>=F(1,20),'actual shifted spacing'
  assert ok(A,S),'actual shifted shells';n+=1
 for E,v in computed.items():
  claimed=next(F(p['slope'])*E+F(p['intercept']) for p in d['small_spacing_curve'] if F(p['lo'])<=E and (p['hi'] is None or E<=F(p['hi'])))
  assert claimed==v,'independent budget optimum';n+=1
 old=json.loads((ROOT/'lab/process/k1990-small-dimension-thermal-frontier.json').read_text())['delta_one_twentieth_energy_curve']
 def value(curve,x):
  return next(F(p['slope'])*x+F(p['intercept']) for p in curve if F(p['lo'])<=x and(p['hi'] is None or x<=F(p['hi'])))
 for piece in d['dimension8_benefit']:
  lo=F(piece['lo']);hi=lo+1 if piece['hi'] is None else F(piece['hi'])
  for E in [lo,(lo+hi)/2,hi]:
   diff=value(old,E)-value(d['small_spacing_curve'],E)
   assert diff==F(piece['benefit_slope'])*E+F(piece['benefit_intercept'])>=0,'exact dimension benefit';n+=1
 return n,cache
if __name__=='__main__':
 d=json.loads((ROOT/'lab/process/k1994-nine-level-thermal-reduction.json').read_text());n,c=check(d);faults=[]
 for name in ['component','coverage','spacing','curve']:
  b=copy.deepcopy(d)
  if name=='component':b['improving_small_components'].pop()
  if name=='coverage':b['pareto_blocks']=[a for a in b['pareto_blocks'] if len(a['S'])<4]
  if name=='spacing':b['shifted_templates'][0]['spectrum'][1]='0'
  if name=='curve':
   p=next(p for p in b['small_spacing_curve'] if F(p['lo'])<=F(2) and (p['hi'] is None or F(p['hi'])>=2));p['intercept']=str(F(p['intercept'])+1)
  try:check(b,c)
  except AssertionError as e:faults.append((name,str(e)))
  else:raise AssertionError('undetected '+name)
 print('PASS K1994 separate',n,'coverage/physical/optimization obligations; mathematical faults',faults)
