"""Consume the proved stronger compulsory-ladder shift; no claim of optimality."""
from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,hashlib,argparse
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('joint',ROOT/'tests/channel-swings/k2070_joint_terminal_thermal_bound.py');o=importlib.util.module_from_spec(spec);spec.loader.exec_module(o)
def shift(s):
 return F(1) if len(s)==1 else max(F(1),min(F(s[-2])+F(7,2),F(s[-1]+2)))

from itertools import combinations,product
from functools import lru_cache
from math import lcm,gcd
EXTENDED={(3,1,3),(3,2,2)}
def determinant(rows):
 if len(rows)==1:return rows[0][0]
 return sum((-1)**j*rows[0][j]*determinant([r[:j]+r[j+1:] for r in rows[1:]]) for j in range(len(rows)))
def four_lines(gaps):
 unit=[[F(int(i==j)) for j in range(5)] for i in range(5)];forms=list(unit);flows=[]
 for i,d in enumerate(gaps):
  L,H=o.LH[d];flows.append([H*x-L*y for x,y in zip(unit[i],unit[i+1])])
 forms+=flows
 for i in range(5):
  for inc in ([0] if i==0 else [0,1]):
   for out in ([0] if i==4 else [0,1]):forms.append([unit[i][j]-(inc*flows[i-1][j] if inc else 0)+(out*flows[i][j] if out else 0) for j in range(5)])
 lines=set()
 for v in forms:
  if not any(v[1:]):continue
  row=v[1:]+[-v[0]];den=lcm(*(x.denominator for x in row));r=[int(x*den) for x in row];div=gcd(*r);r=[x//div for x in r]
  if next(x for x in r[:-1] if x)<0:r=[-x for x in r]
  lines.add(tuple(r))
 return sorted(lines)
@lru_cache(None)
def four_geometry(gaps):
 lines=four_lines(gaps);vs=set();rs=set()
 for rows in combinations(lines,4):
  mat=[list(r[:4]) for r in rows];det=determinant(mat)
  if det:
   v=tuple(F(determinant([[r[4] if j==k else r[j] for j in range(4)] for r in rows]),det) for k in range(4))
   if min(v)>=0:vs.add(v)
 for rows in combinations(lines,3):
  v=tuple((-1)**j*determinant([[r[k] for k in range(4) if k!=j] for r in rows]) for j in range(4))
  if not any(v):continue
  if max(v)<=0:v=tuple(-x for x in v)
  if min(v)<0:continue
  pivot=next(x for x in v if x);rs.add(tuple(F(x,pivot) for x in v))
 return [(*v,o.chain_loss([F(1),*v],gaps)) for v in sorted(vs)],[(*v,o.chain_loss([F(0),*v],gaps)) for v in sorted(rs)]
BASE_CONSTRAINTS=o.worst_incoming_constraints
def extended_constraints(ci,seed):
 if ci!=164:return BASE_CONSTRAINTS(ci,seed)
 cons=[]
 for row in BASE_CONSTRAINTS(ci,seed):
  tag=row[3]
  if isinstance(tag,tuple):
   if tag==('fourthpluscap',18,2):continue
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
   n4=n3+h;A,B=pol.get((n4,h),(F(0),F(0)));vs4,rs4=four_geometry((*gaps,h))
   for x,y,z,w,c in rs4:add(x+y+z+w*A,n*x+n2*y+n3*z+w*B,c,('triple_ray',n,d,e,f,h,'four'))
   for j,v in enumerate(o.bank[ci]['vertices']):
    p=F(v['p'][-1]);en=F(v['energy']);r=F(v['value'])
    for x,y,z,w,c in vs4:add(1+p*(x+y+z+w*A),en+p*(n*x+n2*y+n3*z+w*B),r+p*c,('triple',j,d,e,f,str(x),str(y),str(z),str(w),h,'four'))
 return cons

def produce():
 refs=['tests/channel-swings/k2070_joint_terminal_thermal_bound.py','lab/process/k2070-joint-terminal-thermal-bound.json','lab/process/k2068-thermal-population-construction.json','explorations/conditional-build/k2029-multicomponent-thermal-placement-2026-10-24.md','explorations/conditional-build/k2059-energy-aware-thermal-tail-2026-10-25.md']
 pins={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in refs}
 prev=json.loads((ROOT/refs[1]).read_text());ass=list(o.one.old['assignments'])
 for pp,hh in prev['inputs'].items():assert hashlib.sha256((ROOT/pp).read_bytes()).hexdigest()==hh,'inherited dependency pin'
 for path in ['lab/process/k2066-thermal-terminal-response.json',refs[1]]:
  for ci,r in json.loads((ROOT/path).read_text())['replacements'].items():ass[int(ci)]=r
 oldshift=o.b.shift;o.b.shift=shift;o.worst_incoming_constraints=extended_constraints
 # Refresh every assignment below the new first candidate, retaining exact older
 # certificates for all others. No hidden assumption that the old bottleneck stays.
 replacements={};threshold=None
 for ci in sorted(range(len(ass)),key=lambda i:F(ass[i]['a'])+F(5,2)*F(ass[i]['s'])):
  oldvalue=F(ass[ci]['a'])+F(5,2)*F(ass[ci]['s'])
  if threshold is not None and oldvalue>=threshold:continue
  r=o.solve(ci,[F(ass[ci]['a']),-F(ass[ci]['s'])],mixture='69/100' if ci==164 else ass[ci].get('mixture'))
  print('certified',ci,float(F(r['value'])),r['active_tag'],flush=True)
  if F(r['value'])>oldvalue:ass[ci]=r;replacements[str(ci)]=r
  threshold=min(F(ass[i]['a'])+F(5,2)*F(ass[i]['s']) for i in map(int,replacements)) if replacements else oldvalue
 o.b.shift=oldshift
 lower,ci=min((F(r['a'])+F(5,2)*F(r['s']),i) for i,r in enumerate(ass));a,s=F(ass[ci]['a']),F(ass[ci]['s']);left,right=map(F,prev['interval'])
 for r in ass:
  da,ds=F(r['a'])-a,F(r['s'])-s
  if ds>0:left=max(left,-da/ds)
  elif ds<0:right=min(right,-da/ds)
  else:assert da>=0
 assert left<F(5,2)<right
 upper=F(prev['upper']);assert lower<=upper
 return dict(id='K2072',inputs=pins,replacements=replacements,lower=str(lower),lower_line=[str(a),str(s)],upper=str(upper),width=str(upper-lower),width_reduction=str((lower-F(prev['lower']))/(upper-F(prev['lower']))),interval=[str(left),str(right)],bottleneck=ci,quad_arrangements={','.join(map(str,gaps)):dict(vertices=[[str(x) for x in v] for v in four_geometry(gaps)[0]],rays=[[str(x) for x in v] for v in four_geometry(gaps)[1]]) for prefix in sorted(EXTENDED) for h in o.b.K if prefix[-1]+h>=4 for gaps in [(*prefix,h)]},shifts={str(i):str(shift(c['s'])) for i,c in enumerate(o.bank)},scope='stronger physical packing transfer; exact global finite/countable certificate; no unrestricted optimum or GU claim')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');args=p.parse_args();d=json.loads(json.dumps(produce()));dest=ROOT/'lab/process/k2072-compulsory-ladder-thermal-bound.json'
 if args.write:dest.write_text(json.dumps(d,indent=2)+'\n')
 else:assert json.loads(dest.read_text())==d
 print('PASS',d['lower'],float(F(d['lower'])),d['bottleneck'])
