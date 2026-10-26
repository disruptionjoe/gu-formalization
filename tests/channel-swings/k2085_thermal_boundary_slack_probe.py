"""Independent raw-return, affine certificate, physical witness and equality checks."""
from pathlib import Path
from fractions import Fraction as Q
from copy import deepcopy
import json,hashlib,importlib.util
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('raw_probe',ROOT/'tests/channel-swings/k2074_subdivided_incoming_thermal_bound_probe.py');rawmod=importlib.util.module_from_spec(spec);spec.loader.exec_module(rawmod)
A={1:Q(14,55),2:Q(1,8),3:Q(3,55)}
def boundary(s):
 incoming=s[-1]-s[-2] if len(s)>1 else 4
 return max([Q(0)]+[A[d] for d in [1,2,3] if s[-1]+d>=12 and incoming+d>=4])
def check(doc,bank,assignments,raw_values,witness):
 ass=deepcopy(assignments);counts=0
 for key,v in doc['replacements'].items():
  ci=int(key);a,t,eta=Q(v['a']),-Q(v['s']),Q(v['eta']);shift=Q(v['shift']);D=Q(v['boundary_shift']);s=bank[ci]['s']
  assert s==([1,3,5,7,9] if ci==163 else [1,3,5,7,9,11]),'unchanged support'
  assert shift==(8 if ci==163 else 10),'actual high packing offset'
  assert Q(v['tail_floor'])==min(s[-1]+g for g in [1,2,3] if s[-1]+g>=12 and 2+g>=4),'true low tail'
  assert eta==Q(4,25) and 0<t<eta and a-Q(v['tail_floor'])*t<=eta and a-(12+shift)*t<=eta,'all tail coefficients'
  assert D==(Q(3,55)-Q(1,23) if ci==163 else 0),'derived gap3 shift'
  low=[];high=[]
  for vi,x in enumerate(bank[ci]['vertices']):
   pop=list(map(Q,x['p']));e=sum(Q(n)*p for n,p in zip(s,pop));assert sum(pop)==1 and e==Q(x['energy']),'low population energy'
   low.append(raw_values[ci][vi]-eta*boundary(s)*pop[-1]-a+t*(e+D*pop[-1]));counts+=1
  for j,c in enumerate(bank):
   for vi,x in enumerate(c['vertices']):
    high.append(raw_values[j][vi]-eta*boundary(c['s'])*Q(x['p'][-1])-a+t*(Q(x['energy'])+shift));counts+=1
  assert min(low)>=0 and min(high)>0,'exact low/high margins'
  if ci==163:
   assert [i for i,x in enumerate(low) if x==0]==[16],'unique163 equality vertex'
   assert list(map(Q,bank[ci]['vertices'][16]['p']))==[Q(n,581) for n in [216,324,36,4,1]],'positive terminal163'
   assert min(x for x,vv in zip(low,bank[ci]['vertices']) if Q(vv['p'][-1])==0)>0,'zero face strict'
   # Two-tail equality impossibility: r=Dp9, q12=k3p9, tail only13.
   k1,k3,c1=Q(7,29),Q(1,23),Q(29,135)
   assert D-k1*k3==Q(21,36685) and c1*(D-k1*k3)==Q(7,56925)>0,'strict final tail loss'
  ass[ci]=v
 a,s=map(Q,doc['lower_line']);left,right=map(Q,doc['interval']);oldleft,oldright=map(Q,doc['previous_interval'])
 assert left==oldleft<oldright<right,'strict right extension'
 for E in [left,right]:
  assert all(Q(v['a'])+E*Q(v['s'])>=a+E*s for v in ass),'all-cell global dominance'
 ties=[[i for i,v in enumerate(ass) if Q(v['a'])+E*Q(v['s'])==a+E*s] for E in [left,right]]
 assert ties==[[164,187],[163,187]]==doc['ties'],'endpoint tie census'
 mid=(left+right)/2
 assert all(Q(v['a'])+mid*Q(v['s'])>a+mid*s for i,v in enumerate(ass) if i!=187),'strict interior'
 wl,wr=map(Q,witness['energy_interval']);assert wl<left<right<wr,'physical chamber'
 assert list(map(Q,witness['line']))==[a,s],'same optimizer'
 for E in [left,mid,right]:
  pop=[Q(x)+E*Q(y) for x,y in witness['population_affine']];sup=witness['occupied_support']
  assert min(pop)>0 and sum(pop)==1 and sum(Q(n)*p for n,p in zip(sup,pop))==E,'physical population'
  assert rawmod.raw(sup,pop)==a+E*s,'actual physical return'
  assert set().union(*(set(range(n-1,n+2)) for n in sup))==set(range(41)),'physical minimum shell union'
 return counts

def main():
 doc=json.loads((ROOT/'lab/process/k2085-thermal-boundary-slack.json').read_text())
 for r,h in doc['inputs'].items():assert hashlib.sha256((ROOT/r).read_bytes()).hexdigest()==h,'pinned predecessor'
 prev=json.loads((ROOT/'lab/process/k2074-subdivided-incoming-thermal-bound.json').read_text());_,bank,ass,*_=rawmod.inputs(prev)
 for slug in ['k2074-subdivided-incoming-thermal-bound','k2083-thermal-certificate-strengthening']:
  for ci,v in json.loads((ROOT/f'lab/process/{slug}.json').read_text())['replacements'].items():ass[int(ci)]=v
 raw_values=[]
 for cell in bank:
  vals=[]
  for v in cell['vertices']:
   value=rawmod.raw(cell['s'],list(map(Q,v['p'])));assert value==Q(v['value']),'independent raw bath return';vals.append(value)
  raw_values.append(vals)
 witness=json.loads((ROOT/'lab/process/k2068-thermal-population-construction.json').read_text())
 print('PASS baseline',check(doc,bank,ass,raw_values,witness),'low/high inequalities; 20975 independent raw returns;671 lines;3 witnesses',flush=True)
 jobs=[]
 for ci,key,value in [('185','a','1'),('186','tail_floor',14),('163','boundary_shift','1/8'),('163','shift',9),('163','eta','1')]:
  b=deepcopy(doc);b['replacements'][ci][key]=value;jobs.append((ci+' '+key,lambda d=b:check(d,bank,ass,raw_values,witness)))
 b=deepcopy(doc);b['interval'][1]='3';jobs.append(('false endpoint',lambda:check(b,bank,ass,raw_values,witness)))
 r=deepcopy(raw_values);r[185][29]-=1;jobs.append(('corrupted raw contact',lambda:check(doc,bank,ass,r,witness)))
 w=deepcopy(witness);w['population_affine'][0][0]='0';jobs.append(('corrupted physical optimizer',lambda:check(doc,bank,ass,raw_values,w)))
 for name,fn in jobs:
  try:fn()
  except AssertionError as e:assert str(e);print('DETECTED',name,str(e),flush=True)
  else:raise AssertionError('undetected '+name)
 print('PASS8 mathematical faults; inherited geometry/countable transfer explicitly reused')
if __name__=='__main__':main()
