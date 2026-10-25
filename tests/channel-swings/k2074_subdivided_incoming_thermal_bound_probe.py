"""Separate raw-bath acceptance of the shared-tail convex upper price."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,importlib.util,copy
ROOT=Path(__file__).resolve().parents[2]
sp=importlib.util.spec_from_file_location('old_probe',ROOT/'tests/channel-swings/k2072_compulsory_ladder_thermal_bound_probe.py');old=importlib.util.module_from_spec(sp);sp.loader.exec_module(old)
Z=Q(0);K=old.K;C=old.C;LH=old.LH;bell=old.bell;allowed=old.allowed;raw=old.raw;strong_shift=old.strong_shift
def assignment(ci,v,bank,geom,geom3,geom4=None,high=True):
 a,t=Q(v['a']),-Q(v['s']);s=bank[ci]['s'];z=s[-1];ell=strong_shift(s);g=bell(a,t);h=bell(a,t,ell);count=0
 third=set()
 for d in allowed(s):
  for e in K:
   if d+e>=4:
    for f in K:
     if e+f>=4:third.update((z+d+e+f+h,h) for h in K if f+h>=4)
 for n in range(12,65):
  for d in K:
   if (n,d) in third:third.update((n+e,e) for e in K if d+e>=4 and n+e<=64)
 assert all(g[n,d]<=C[d] for n,d in third if n<=64 and not (ci in [164,188] and (n,d) in [(18,2),(19,2)])),'fourth-plus caps'
 theta=Q(v['common_tail_weight']);assert 0<=theta<=1
 prices=[]
 def add_price(points,rewards,d):
  L,H=LH[d]
  price=max(sum(q*x for q,x in zip(rewards,row[:-1]))-row[-1]-theta*min(Q(1),max(Z,L*row[0]-H))/2 for row in points)
  prices.append(price)
 for d in allowed(s):
  n=z+d;q=a-t*n;L,H=LH[d]
  assert q<=Q(1,2),'single recession'
  pts=[(x,raw([0,d],[Q(1),x])-Q(1,2)) for x in [Z,K[d],H/L,(1+H)/L]];add_price(pts,[q],d)
  for e in K:
   if d+e<4:continue
   gg=a-t*(n+e);vs,rs=geom[d,e]
   assert all(q*x+gg*y<=c for x,y,c in rs),'joint recession';add_price(vs,[q,gg],d)
   for f in K:
    if e+f<4:continue
    extended=ci in [164,188] and (d,e,f) in [(3,1,3),(3,2,2),(3,2,3),(3,3,2)];g3=a-t*(n+e+f) if extended else g[n+e+f,f];vs3,rs3=geom3[d,e,f]
    assert all(q*x+gg*y+g3*z<=c for x,y,z,c in rs3),'triple recession';add_price(vs3,[q,gg,g3],d)
    if extended:
     for h4 in K:
      if f+h4<4:continue
      vs4,rs4=geom4[d,e,f,h4];gg4=g[n+e+f+h4,h4]
      assert all(q*x+gg*y+g3*z+gg4*w<=c for x,y,z,w,c in rs4),'four-terminal recession'
      add_price(vs4,[q,gg,g3,gg4],d)
 for vv in bank[ci]['vertices']:
  pp=list(map(Q,vv['p']));p=pp[-1];A=p
  if len(s)>1:
   L,H=LH[s[-1]-s[-2]];A=max(Z,p-max(Z,H*pp[-2]-L*p))
  boundary=max([Z]+[p*price+theta*A/2 for price in prices])
  assert Q(vv['value'])>=a-t*Q(vv['energy'])+boundary,'low joint inequality'
  assert raw(s,pp)==Q(vv['value']),'low raw bath return';count+=1
 if high:
  assert all(x<=C[d] for (n,d),x in h.items()),'high caps'
  assert all(a-t*(n+ell)+K[d]*h.get((n+d,d),Z)<=Q(1,2) for n in range(12,65) for d in K),'erased root'
  for cell in bank:
   coef=max([Z]+[K[d]*h.get((cell['s'][-1]+d,d),Z) for d in allowed(cell['s'])])
   for vv in cell['vertices']:
    assert Q(vv['value'])>=a-t*(Q(vv['energy'])+ell)+coef*Q(vv['p'][-1]),'high-component inequality';count+=1
 return count

def decode(d):
 return {tuple(map(int,key.split(','))):tuple([tuple(map(Q,row)) for row in d[key][typ]] for typ in ['vertices','rays']) for key in d}
def inputs(d):
 for p,h in d['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'input pin'
 prev=json.loads((ROOT/'lab/process/k2072-compulsory-ladder-thermal-bound.json').read_text());joint=json.loads((ROOT/'lab/process/k2070-joint-terminal-thermal-bound.json').read_text())
 for doc in [prev,joint]:
  for p,h in doc['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'inherited pin'
 base=json.loads((ROOT/'lab/process/k2059-energy-aware-thermal-tail.json').read_text());bank=json.loads((ROOT/base['bank_ref']).read_text())['bank'];ass=list(base['assignments'])
 for name in ['k2066-thermal-terminal-response','k2070-joint-terminal-thermal-bound','k2072-compulsory-ladder-thermal-bound']:
  for i,v in json.loads((ROOT/f'lab/process/{name}.json').read_text())['replacements'].items():ass[int(i)]=v
 g4=decode(prev['quad_arrangements']);g4.update(decode(d['quad_arrangements']))
 return prev,bank,ass,decode(joint['arrangements']),decode(joint['triple_arrangements']),g4
def global_check(d,ass,prev):
 ass=copy.deepcopy(ass)
 for i,v in d['replacements'].items():ass[int(i)]=v
 a,s=map(Q,d['lower_line']);left,right=map(Q,d['interval']);assert left<Q(5,2)<right
 for v in ass:
  for E in [left,right]:assert Q(v['a'])+Q(v['s'])*E>=a+s*E,'all-cell affine dominance'
 lo,ci=min((Q(v['a'])+Q(5,2)*Q(v['s']),i) for i,v in enumerate(ass))
 assert lo==Q(d['lower'])==a+Q(5,2)*s and ci==d['bottleneck'],'global lower'
 upper=Q(prev['upper']);assert Q(d['upper'])==upper,'upper witness'
 assert Q(prev['lower'])<lo<=upper and Q(d['width'])==upper-lo,'bracket width'
 assert Q(d['width_reduction'])==(lo-Q(prev['lower']))/(upper-Q(prev['lower'])),'gap reduction'
 return len(ass)
def scalar_controls():
 count=0
 for p in [Q(0),Q(1,3),Q(1),Q(7)]:
  for ratio in [Q(0),Q(1,10),Q(1,2),Q(1)]:
   A=p*ratio
   for O in [Q(0),p/3,p,2*p]:
    for theta in [Q(0),Q(1,5),Q(69,100),Q(1)]:
     assert min(A,O)<=theta*A+(1-theta)*min(p,O),'shared tail inequality';count+=1
 # Common-max is strictly below separate-max for a real two-tail control.
 # f0=f_w-min(1,O)/2, so enforce the actual difference relation.
 vals=[(Q(1,10),Q(1)),(Q(0),Q(0))];theta=Q(69,100)
 fw=max(x for x,o in vals);f0=max(x-min(Q(1),o)/2 for x,o in vals)
 same=max(x-theta*min(Q(1),o)/2 for x,o in vals)
 assert same<(1-theta)*fw+theta*f0;count+=1
 return count
if __name__=='__main__':
 d=json.loads((ROOT/'lab/process/k2074-subdivided-incoming-thermal-bound.json').read_text());prev,bank,ass,g2,g3,g4=inputs(d);count=0
 for i,v in d['replacements'].items():count+=assignment(int(i),v,bank,g2,g3,g4)
 glob=global_check(d,ass,prev);sc=scalar_controls();geometry=0
 for gaps,(vs,rs) in decode(d['quad_arrangements']).items():
  pts,rays=old.geometry4(gaps)
  assert {r[:-1] for r in vs}==pts and {r[:-1] for r in rs}==rays,'new geometry completeness'
  support=[0]
  for gap in gaps:support.append(support[-1]+gap)
  for row in vs:assert raw(support,[Q(1),*row[:-1]])-Q(1,2)==row[-1],'raw tail return';geometry+=1
  for row in rs:assert raw(support,[Z,*row[:-1]])==row[-1],'raw tail recession';geometry+=1
 inherited=old.assignment(187,ass[187],bank,g2,g3,g4)
 us=importlib.util.spec_from_file_location('upper_probe',ROOT/'tests/channel-swings/k2068_thermal_population_construction_probe.py');up=importlib.util.module_from_spec(us);us.loader.exec_module(up)
 witness=json.loads((ROOT/'lab/process/k2068-thermal-population-construction.json').read_text());left,right=map(Q,d['interval']);ul,ur=map(Q,witness['energy_interval']);assert ul<=left<right<=ur,'upper interval'
 assert list(map(Q,witness['line']))==list(map(Q,d['lower_line'])),'same affine witness'
 for E in [left,Q(5,2),right]:
  p=[Q(a)+E*Q(b) for a,b in witness['population_affine']];s=witness['occupied_support'];value=Q(d['lower_line'][0])+E*Q(d['lower_line'][1])
  assert min(p)>=0 and sum(p)==1 and sum(Q(n)*x for n,x in zip(s,p))==E,'witness population'
  assert up.raw(s,p)==up.output(s,p)==value,'physical equality witness'
 paths=[]
 def walk(ds,total,last):
  if total>10:return
  if last==2 and total in [9,10]:paths.append(tuple(ds))
  for gap in K:
   if last+gap>=4:walk(ds+[gap],total+gap,gap)
 walk([3],3,3)
 assert set(paths)=={(3,1,3,2),(3,2,2,2),(3,2,3,2),(3,3,2,2)},'all removed-cap paths'
 print('BASELINE',count,glob,sc,geometry,'inherited187',inherited,'physical witnesses3 paths4',flush=True)
 faults=[]
 for key in ['lower','upper','width','width_reduction']:
  z=copy.deepcopy(d);z[key]=str(Q(z[key])+Q(1,100));faults.append((key,z))
 for key,z in faults:
  try:global_check(z,ass,prev)
  except AssertionError as e:assert str(e);print('REJECT',key,str(e))
  else:raise AssertionError('accepted mutation '+key)
 for key,val in [('common_tail_weight','-1/10'),('a','1')]:
  v=copy.deepcopy(d['replacements']['164']);v[key]=val
  try:assignment(164,v,bank,g2,g3,g4,high=False)
  except AssertionError:print('REJECT',key,'actual inequality')
  else:raise AssertionError('accepted mutation '+key)
 print('PASS',count,'low/high inequalities',glob,'affine assignments',sc,'finite scalar controls;6 faults rejected')
