"""Exact incoming-ratio subdivision; finite checks accompany the analytic transfer."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import importlib.util,json,hashlib,argparse,sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tests/channel-swings'))
from k2015_finite_thermal_ray_separation import matrices,vertex,rate
sp=importlib.util.spec_from_file_location('packing',ROOT/'tests/channel-swings/k2072_compulsory_ladder_thermal_bound.py');k=importlib.util.module_from_spec(sp);sp.loader.exec_module(k)
o=k.o
PREV='lab/process/k2072-compulsory-ladder-thermal-bound.json'
EXTENDED={(3,1,3),(3,2,2),(3,2,3),(3,3,2)}
NEW_GEOMETRY={}
RAW_FOUR=k.four_geometry
def decode(d):
 return {tuple(map(int,key.split(','))):tuple([tuple(map(F,row)) for row in d[key][typ]] for typ in ['vertices','rays']) for key in d}
def setup():
 prev=json.loads((ROOT/PREV).read_text());joint=json.loads((ROOT/'lab/process/k2070-joint-terminal-thermal-bound.json').read_text())
 for data in [prev,joint]:
  for p,h in data['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'inherited pin'
 q4=decode(prev['quad_arrangements']);q3=decode(joint['triple_arrangements']);q2=decode(joint['arrangements'])
 NEW_GEOMETRY.update({(*prefix,h):RAW_FOUR((*prefix,h)) for prefix in sorted(EXTENDED) for h in o.b.K if prefix[-1]+h>=4 and (*prefix,h) not in q4});q4.update(NEW_GEOMETRY)
 k.four_geometry=lambda gaps:q4[tuple(gaps)];o.triple_geometry=lambda gaps:q3[tuple(gaps)];o.arrangement=lambda d,e:q2[d,e];o.b.shift=k.shift
 return prev

def extended_more_constraints(ci,seed):
 if ci not in [164,188]:return k.BASE_CONSTRAINTS(ci,seed)
 cons=[]
 for row in k.BASE_CONSTRAINTS(ci,seed):
  tag=row[3]
  if isinstance(tag,tuple):
   if tag in [('fourthpluscap',18,2),('fourthpluscap',19,2)]:continue
   if tag[0] in ['triple','triple_ray']:
    gaps=tag[2:5] if tag[0]=='triple' else tag[2:5]
    if tuple(gaps) in EXTENDED:continue
  cons.append(row)
 ss=o.bank[ci]['s'];pol=o.b.policy(*seed,64)
 def add(A,B,C,tag):cons.append((F(A),F(B),F(C),tag))
 for gaps in sorted(EXTENDED):
  d,e,f=gaps;n=ss[-1]+d;n2=n+e;n3=n2+f
  vs,rs=o.triple_geometry(gaps)
  # The shorter three-terminal tail is retained with its actual final reward.
  for x,y,z,c in rs:add(x+y+z,n*x+n2*y+n3*z,c,('triple_ray',n,d,e,f,'short'))
  for j,v in enumerate(o.bank[ci]['vertices']):
   p=F(v['p'][-1]);en=F(v['energy']);r=F(v['value'])
   for x,y,z,c in vs:add(1+p*(x+y+z),en+p*(n*x+n2*y+n3*z),r+p*c,('triple',j,d,e,f,str(x),str(y),str(z),'short'))
  for h in o.b.K:
   if f+h<4:continue
   n4=n3+h;A,B=pol.get((n4,h),(F(0),F(0)));vs4,rs4=k.four_geometry((*gaps,h))
   for x,y,z,w,c in rs4:add(x+y+z+w*A,n*x+n2*y+n3*z+w*B,c,('triple_ray',n,d,e,f,h,'four'))
   for j,v in enumerate(o.bank[ci]['vertices']):
    p=F(v['p'][-1]);en=F(v['energy']);r=F(v['value'])
    for x,y,z,w,c in vs4:add(1+p*(x+y+z+w*A),en+p*(n*x+n2*y+n3*z+w*B),r+p*c,('triple',j,d,e,f,str(x),str(y),str(z),str(w),h,'four'))
 return cons

def correlated_constraints(ci,seed):
 cons=extended_more_constraints(ci,seed);out=[]
 for A,B,C,tag in cons:
  if isinstance(tag,tuple) and tag[0] in ['single','pair','triple']:
   v=o.bank[ci]['vertices'][tag[1]];p=F(v['p'][-1]);av=o.one.incoming(o.bank[ci]['s'],v);L,H=o.LH[tag[2]];idx={'single':3,'pair':4,'triple':5}[tag[0]];x=F(tag[idx]);C0=C+p*min(F(1),max(F(0),L*x-H))/2-av/2
   C=(1-THETA)*C+THETA*C0
  out.append((A,B,C,tag))
 return out
THETA=F(69,100)
def produce():
 prev=setup();o.worst_incoming_constraints=correlated_constraints
 ass=list(o.one.old['assignments'])
 for file in ['k2066-thermal-terminal-response','k2070-joint-terminal-thermal-bound','k2072-compulsory-ladder-thermal-bound']:
  for ci,v in json.loads((ROOT/f'lab/process/{file}.json').read_text())['replacements'].items():ass[int(ci)]=v
 replacements={};threshold=None
 for ci in sorted(range(len(ass)),key=lambda i:F(ass[i]['a'])+F(5,2)*F(ass[i]['s'])):
  oldvalue=F(ass[ci]['a'])+F(5,2)*F(ass[ci]['s'])
  if threshold is not None and oldvalue>=threshold:continue
  r=o.solve(ci,[F(ass[ci]['a']),-F(ass[ci]['s'])]);r['common_tail_weight']=str(THETA);r.pop('mixture')
  print('certified',ci,float(F(r['value'])),r['active_tag'],flush=True)
  if F(r['value'])>oldvalue:ass[ci]=r;replacements[str(ci)]=r
  threshold=min(F(ass[i]['a'])+F(5,2)*F(ass[i]['s']) for i in map(int,replacements)) if replacements else oldvalue
 lower,ci=min((F(v['a'])+F(5,2)*F(v['s']),i) for i,v in enumerate(ass));a,s=F(ass[ci]['a']),F(ass[ci]['s']);left,right=map(F,prev['interval'])
 for v in ass:
  da,ds=F(v['a'])-a,F(v['s'])-s
  if ds>0:left=max(left,-da/ds)
  elif ds<0:right=min(right,-da/ds)
  else:assert da>=0
 assert left<F(5,2)<right
 assert lower<=F(prev['upper']),'lower exceeds physical upper'
 refs=[PREV,'tests/channel-swings/k2072_compulsory_ladder_thermal_bound.py','tests/channel-swings/k2015_finite_thermal_ray_separation.py','lab/process/k2068-thermal-population-construction.json','tests/channel-swings/k2068_thermal_population_construction_probe.py']
 return dict(id='K2074',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in refs},method='common-tail-before-maximization-and-selective-cap19-response',quad_arrangements={','.join(map(str,g)):dict(vertices=[[str(x) for x in r] for r in vs],rays=[[str(x) for x in r] for r in rs]) for g,(vs,rs) in NEW_GEOMETRY.items()},weight=str(THETA),replacements=replacements,lower=str(lower),lower_line=[str(a),str(s)],upper=prev['upper'],width=str(F(prev['upper'])-lower),width_reduction=str((lower-F(prev['lower']))/(F(prev['upper'])-F(prev['lower']))),bottleneck=ci,interval=list(map(str,[left,right])),rejected_subdivision=dict(cut='1/4',value='0.2784000433091823',role='rejected candidate discovery; never accepted bound'),scope='shared-tail convex transfer and exact finite/countable bound; no optimum or source claim')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');args=p.parse_args();d=json.loads(json.dumps(produce()));dest=ROOT/'lab/process/k2074-subdivided-incoming-thermal-bound.json'
 if args.write:dest.write_text(json.dumps(d,indent=2)+'\n')
 else:assert json.loads(dest.read_text())==d
 print('PASS',d['lower'],float(F(d['width_reduction'])))
