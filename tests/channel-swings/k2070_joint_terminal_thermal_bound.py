"""Exact joint two-terminal thermal certificate; analytical transfer is in the note."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations,product
import importlib.util,json,hashlib,argparse
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('one',ROOT/'tests/channel-swings/k2066_thermal_terminal_response.py');one=importlib.util.module_from_spec(spec);spec.loader.exec_module(one)
b=one.b;bank=one.bank;LH=one.Lh

def loss(p,A,u,v,d,e):
 L,H=LH[d];M,J=LH[e]
 incoming=max(F(0),H*p-L*u);outgoing=max(F(0),L*u-H*p)
 return (max(F(0),A-outgoing)-A+max(F(0),u-incoming-max(F(0),M*v-J*u))+max(F(0),v-max(F(0),J*u-M*v)))/2

@lru_cache(None)
def arrangement(d,e):
 L,H=LH[d];M,J=LH[e]
 # Ax+By=C. All possible positive-part break loci, including extensions
 # outside their active cells; redundant lines cannot lose a true extremum.
 lines=[(1,0,0),(0,1,0),(1,0,H/L),(1,0,(1+H)/L),(1,0,H/(1+L)),
        (-J,M,0),(-J,1+M,0),(-(1+J),M,0),(-(1+L+J),M,-H)]
 vertices=set()
 for (a,b0,c),(d0,e0,f) in combinations(lines,2):
  det=a*e0-b0*d0
  if det:
   x,y=F(c*e0-b0*f)/det,F(a*f-c*d0)/det
   if x>=0 and y>=0:vertices.add((x,y))
 rays={(F(0),F(1)),(F(1),F(0))}
 for a,b0,c in lines:
  if b0 and -F(a)/b0>=0:rays.add((F(1),-F(a)/b0))
 return [(x,y,loss(F(1),F(1),x,y,d,e)) for x,y in sorted(vertices)],[(x,y,loss(F(0),F(0),x,y,d,e)) for x,y in sorted(rays)]

def chain_loss(pop,gaps):
 deficits=[]
 for i,pop_i in enumerate(pop):
  incoming=0 if i==0 else max(F(0),LH[gaps[i-1]][1]*pop[i-1]-LH[gaps[i-1]][0]*pop_i)
  outgoing=0 if i==len(gaps) else max(F(0),LH[gaps[i]][0]*pop[i+1]-LH[gaps[i]][1]*pop_i)
  deficits.append(max(F(0),pop_i-incoming-outgoing))
 return (sum(deficits)-pop[0])/2

def triple_lines(gaps):
 # Four populations p0=1,x,y,z. Include every possible flow/deficit boundary.
 unit=[[F(int(i==j)) for j in range(4)] for i in range(4)]
 forms=list(unit)
 flows=[]
 for i,d in enumerate(gaps):
  L,H=LH[d];flows.append([H*x-L*y for x,y in zip(unit[i],unit[i+1])])
 forms+=flows
 for i in range(4):
  for inc in ([0] if i==0 else [0,1]):
   for out in ([0] if i==3 else [0,1]):
    forms.append([unit[i][j]-(inc*flows[i-1][j] if inc else 0)+(out*flows[i][j] if out else 0) for j in range(4)])
 lines=set()
 for v in forms:
  if not any(v[1:]):continue
  pivot=next(x for x in v[1:] if x);lines.add(tuple(x/pivot for x in v[1:]+[-v[0]]))
 return sorted(lines)
def det3(rows):
 (a,b,c),(d,e,f),(g,h,i)=rows
 return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
@lru_cache(None)
def triple_geometry(gaps):
 lines=triple_lines(gaps);vs=set();rs=set()
 for rows in combinations(lines,3):
  mat=[r[:3] for r in rows];det=det3(mat)
  if det:
   xyz=tuple(det3([[r[3] if j==k else r[j] for j in range(3)] for r in rows])/det for k in range(3))
   if min(xyz)>=0:vs.add(xyz)
 for r,s in combinations(lines,2):
  cross=(r[1]*s[2]-r[2]*s[1],r[2]*s[0]-r[0]*s[2],r[0]*s[1]-r[1]*s[0])
  if not any(cross):continue
  if max(cross)<=0:cross=tuple(-x for x in cross)
  if min(cross)<0:continue
  pivot=next(x for x in cross if x);rs.add(tuple(x/pivot for x in cross))
 return [(*v,chain_loss([F(1),*v],gaps)) for v in sorted(vs)],[(*v,chain_loss([F(0),*v],gaps)) for v in sorted(rs)]

def deep_reachable(s,cutoff=64):
 states={(s[-1]+d,d,1) for d in b.allowed(s)}
 for n in range(12,cutoff+1):
  for d in b.K:
   for depth in [1,2,3,4]:
    if (n,d,depth) in states:
     states.update((n+e,e,min(4,depth+1)) for e in b.K if d+e>=4 and n+e<=cutoff)
 return {(n,d) for n,d,depth in states if depth==4}

def constraints(ci,seed):
 s=bank[ci]['s'];pol=b.policy(*seed,64)
 # Preserve EVERY cutoff, high-component and erased-root constraint.
 cons=[c for c in one.constraints(ci,seed) if not (isinstance(c[3],tuple) and c[3][0] in ['low','firstcap','deepcap'])]
 def add(A,B,C,tag):cons.append((F(A),F(B),F(C),tag))
 for n,d in sorted(deep_reachable(s)):
  A,B=pol[n,d];add(A,B,b.C[d],('fourthpluscap',n,d))
 for j,v in enumerate(bank[ci]['vertices']):
  p=F(v['p'][-1]);en=F(v['energy']);r=F(v['value']);add(1,en,r,('lowzero',j))
  for d in b.allowed(s):
   n=s[-1]+d;L,H=LH[d]
   # One actual terminal, including no following terminal.
   add(1,n,F(1,2),('single_ray',n,d))
   for x in [F(0),b.K[d],H/L,(1+H)/L]:
    delta=loss(F(1),F(1),x,F(0),d,1)
    add(1+p*x,en+p*n*x,r+p*delta,('single',j,d,str(x)))
   for e in b.K:
    if d+e<4:continue
    A,B=F(1),F(n+e)
    vertices,rays=arrangement(d,e)
    for x,y,c in rays:add(x+y*A,n*x+y*B,c,('pair_ray',n,d,e,str(x),str(y)))
    for x,y,c in vertices:add(1+p*(x+y*A),en+p*(n*x+y*B),r+p*c,('pair',j,d,e,str(x),str(y)))
    for f in b.K:
     if e+f<4:continue
     AA,BB=pol.get((n+e+f,f),(F(0),F(0)));vertices3,rays3=triple_geometry((d,e,f))
     for x,y,z,c in rays3:add(x+y+z*AA,n*x+(n+e)*y+z*BB,c,('triple_ray',n,d,e,f))
     for x,y,z,c in vertices3:add(1+p*(x+y+z*AA),en+p*(n*x+(n+e)*y+z*BB),r+p*c,('triple',j,d,e,f,str(x),str(y),str(z)))
 return cons

worst_incoming_constraints=constraints
def mixture_constraints(theta):
 def constraints(ci,seed):
  out=[];groups={};ss=bank[ci]['s']
  for A,B,C,tag in worst_incoming_constraints(ci,seed):
   if isinstance(tag,tuple) and tag[0] in ['single','pair','triple']:
    v=bank[ci]['vertices'][tag[1]];p=F(v['p'][-1]);av=one.incoming(ss,v);d=tag[2];L,H=LH[d];point_index={'single':3,'pair':4,'triple':5}[tag[0]];x=F(tag[point_index]);C0=C+p*min(F(1),max(F(0),L*x-H))/2-av/2
    key=tag[:point_index];groups.setdefault(key,[]).append(((A,B,C,tag),(A,B,C0,tag)))
   else:out.append((A,B,C,tag))
  for key,rows in groups.items():
   x=max((r[0] for r in rows),key=lambda z:z[0]*seed[0]-z[1]*seed[1]-z[2]);y=max((r[1] for r in rows),key=lambda z:z[0]*seed[0]-z[1]*seed[1]-z[2]);out.append(tuple((1-theta)*x[i]+theta*y[i] for i in range(3))+(('mix',str(theta),key,x[3],y[3]),))
  return out
 return constraints
def solve(ci,seed=None,mixture=None):
 con_builder=worst_incoming_constraints if mixture is None else mixture_constraints(F(mixture))
 seed=seed or [F(one.old['assignments'][ci]['a']),-F(one.old['assignments'][ci]['s'])]
 cuts={};history=[]
 for it in range(40):
  for A,B,C,tag in con_builder(ci,seed):cuts[A,B,C]=tag
  a,t,tag,nh=one.optimize([(*k,v) for k,v in cuts.items()])
  actual=con_builder(ci,[a,t]);bad=[(A*a-B*t-C,tag) for A,B,C,tag in actual if A*a-B*t>C]
  history.append(dict(iteration=it,value=str(a-F(5,2)*t),violations=len(bad),cuts=len(cuts)))
  if not bad:
   return dict(cell=ci,mixture=None if mixture is None else str(F(mixture)),a=str(a),s=str(-t),value=str(a-F(5,2)*t),active_tag=tag,constraint_count=len(actual),history=history)
  seed=[a,t]
 raise AssertionError('policy separation did not certify; no scientific acceptance')

PINS={'tests/channel-swings/k2059_energy_aware_thermal_tail.py': 'd66117b5a168586aaf5abb5be4a37e22c573b5798959d1e7118afec2f0502143', 'tests/channel-swings/k2066_thermal_terminal_response.py': '5c26c714bd9e151bdb57216720ad2287a09b86388c34d86bccdc40ef68f1f7aa', 'lab/process/k2059-energy-aware-thermal-tail.json': '4aaa708aa2835f50c397b2c1ac7669b71d092706d8da387f322301f70948112e', 'lab/process/k2066-thermal-terminal-response.json': 'bfceece25ab2f8eea62995167c4a23f4541db5ed38c7f72faa8b63ac7e961be3', 'lab/process/k2068-thermal-population-construction.json': '73720b55b6b636a7b7d10ad068c6d7081b121d63fd4a471a22741ab031feda42', 'lab/process/k2045-third-thermal-spacing-phase.json': '6641419ca109d3cbbcd21014913ed22a710f9b1c2249974ba0bb593b9591a637'}

def produce(cells):
 pins=PINS
 for p,h in pins.items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,('input changed',p)
 prev=json.loads((ROOT/'lab/process/k2066-thermal-terminal-response.json').read_text());ass=list(one.old['assignments'])
 for ci,x in prev['replacements'].items():ass[int(ci)]=x
 replacements={}
 for ci in cells:
  r=solve(ci,mixture='7/10' if ci==164 else None);print('certified',ci,float(F(r['value'])),r['active_tag'],flush=True)
  if F(r['value'])>F(ass[ci]['a'])+F(5,2)*F(ass[ci]['s']):ass[ci]=r;replacements[str(ci)]=r
 lower,ci=min((F(v['a'])+F(5,2)*F(v['s']),i) for i,v in enumerate(ass));a,s=F(ass[ci]['a']),F(ass[ci]['s']);left,right=map(F,prev['interval'])
 for v in ass:
  da,ds=F(v['a'])-a,F(v['s'])-s
  if ds>0:left=max(left,-da/ds)
  elif ds<0:right=min(right,-da/ds)
  else:assert da>=0
 assert left<F(5,2)<right
 upper=json.loads((ROOT/'lab/process/k2068-thermal-population-construction.json').read_text())
 return dict(id='K2070',inputs=pins,base_ref='lab/process/k2066-thermal-terminal-response.json',cells=cells,replacements=replacements,lower=str(lower),lower_line=[str(a),str(s)],bottleneck=ci,upper=upper['value'],width=str(F(upper['value'])-lower),gain=str(lower-F(prev['lower'])),width_reduction=str((lower-F(prev['lower']))/(F(upper['value'])-F(prev['lower']))),interval=[str(left),str(right)],arrangements={f'{d},{e}':dict(vertices=[[str(z) for z in v] for v in arrangement(d,e)[0]],rays=[[str(z) for z in v] for v in arrangement(d,e)[1]]) for d in b.K for e in b.K if d+e>=4},triple_arrangements={','.join(map(str,gaps)):dict(vertices=[[str(z) for z in v] for v in triple_geometry(gaps)[0]],rays=[[str(z) for z in v] for v in triple_geometry(gaps)[1]]) for gaps in product(b.K,repeat=3) if gaps[0]+gaps[1]>=4 and gaps[1]+gaps[2]>=4},scope='exact two/three-terminal envelope and finite/countable global lower certificate; no unrestricted optimum, source or GU claim')

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');p.add_argument('--cells',default='164,188,212,187,234,211,233,236,152');args=p.parse_args();data=json.loads(json.dumps(produce(list(map(int,args.cells.split(','))))));dest=ROOT/'lab/process/k2070-joint-terminal-thermal-bound.json'
 if args.write:dest.write_text(json.dumps(data,indent=2)+'\n')
 else:assert json.loads(dest.read_text())==data
 print('PASS lower',data['lower'],'bottleneck',data['bottleneck'])
