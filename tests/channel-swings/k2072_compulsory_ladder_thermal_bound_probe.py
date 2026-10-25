"""Reused raw checker with independently derived stronger physical shift.
Only the new assignments are rechecked; old bank completeness is pinned reuse.
"""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util,json,hashlib,copy
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('prior_probe',ROOT/'tests/channel-swings/k2070_joint_terminal_thermal_bound_probe.py');prior=importlib.util.module_from_spec(spec);spec.loader.exec_module(prior)
Z=Q(0);K=prior.K;C=prior.C;LH=prior.LH;bell=prior.bell;allowed=prior.allowed;raw=prior.raw
def strong_shift(s):
 if len(s)==1:return Q(1)
 # Lowest forced integer segment ends at penultimate+3.
 fractional=Q(s[-2]+3)+Q(1,2)
 same_residue=Q(s[-1]+4)-2
 return max(Q(1),min(fractional,same_residue))
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
 assert all(g[n,d]<=C[d] for n,d in third if n<=64 and not (ci==164 and (n,d)==(18,2))),'fourth-plus caps'
 theta=Q(v.get('mixture') or 0);assert 0<=theta<=1
 prices=[]
 def add_price(points,rewards,d):
  L,H=LH[d]
  bw=max(sum(q*x for q,x in zip(rewards,row[:-1]))-row[-1] for row in points)
  b0=max(sum(q*x for q,x in zip(rewards,row[:-1]))-row[-1]-min(Q(1),max(Z,L*row[0]-H))/2 for row in points)
  prices.append((1-theta)*bw+theta*b0)
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
    extended=ci==164 and (d,e,f) in [(3,1,3),(3,2,2)];g3=a-t*(n+e+f) if extended else g[n+e+f,f];vs3,rs3=geom3[d,e,f]
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


from itertools import combinations
def geometry4(gaps):
 # Independent rational row reduction instead of integer determinant minors.
 flows=[]
 for i,d in enumerate(gaps):
  L,H=LH[d];r=[Z]*5;r[i]=H;r[i+1]=-L;flows.append(r)
 forms=list(flows)
 for i in range(5):
  for incoming in ([False] if i==0 else [False,True]):
   for outgoing in ([False] if i==4 else [False,True]):
    r=[Q(int(j==i)) for j in range(5)]
    if incoming:r=[x-y for x,y in zip(r,flows[i-1])]
    if outgoing:r=[x+y for x,y in zip(r,flows[i])]
    forms.append(r)
 lines=set()
 for r in forms:
  if not any(r[1:]):continue
  a=next(x for x in r[1:] if x);lines.add(tuple(x/a for x in r[1:]+[-r[0]]))
 vertices=set();rays=set()
 for rows in combinations(sorted(lines),4):
  rr,piv=prior.rref(rows)
  if len(piv)==4:
   v=tuple(row[4] for row in rr)
   if min(v)>=0:vertices.add(v)
 for rows in combinations(sorted(lines),3):
  rr,piv=prior.rref([list(r[:4])+[Z] for r in rows])
  if len(piv)!=3:continue
  free=next(j for j in range(4) if j not in piv);v=[Z]*4;v[free]=Q(1)
  for row,j in zip(rr,piv):v[j]=-row[free]
  if min(v)<0:continue
  a=next(x for x in v if x);rays.add(tuple(x/a for x in v))
 return vertices,rays

def quad_check(geom4):
 assert set(geom4)=={(3,1,3,1),(3,1,3,2),(3,1,3,3),(3,2,2,2),(3,2,2,3)}
 count=0
 for gaps,(vs,rs) in geom4.items():
  points,rays=geometry4(gaps)
  assert {row[:-1] for row in vs}==points,'complete four-terminal vertices'
  assert {row[:-1] for row in rs}==rays,'complete four-terminal rays'
  support=[0]
  for gap in gaps:support.append(support[-1]+gap)
  for row in vs:assert raw(support,[Q(1),*row[:-1]])-Q(1,2)==row[-1],'raw four-terminal loss';count+=1
  for row in rs:assert raw(support,[Z,*row[:-1]])==row[-1],'raw four-terminal recession';count+=1
 return count

def check_shifts(data,bank):
 for i,cell in enumerate(bank):assert Q(data['shifts'][str(i)])==strong_shift(cell['s']),'geometry shift'

def check(data):
 for p,h in data['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'input pin'
 prev=json.loads((ROOT/'lab/process/k2070-joint-terminal-thermal-bound.json').read_text())
 for pp,hh in prev['inputs'].items():assert hashlib.sha256((ROOT/pp).read_bytes()).hexdigest()==hh,'inherited dependency pin'
 geom={tuple(map(int,k.split(','))):([tuple(map(Q,v)) for v in a['vertices']],[tuple(map(Q,v)) for v in a['rays']]) for k,a in prev['arrangements'].items()}
 geom3={tuple(map(int,k.split(','))):([tuple(map(Q,v)) for v in a['vertices']],[tuple(map(Q,v)) for v in a['rays']]) for k,a in prev['triple_arrangements'].items()}
 old=json.loads((ROOT/'lab/process/k2059-energy-aware-thermal-tail.json').read_text());bank=json.loads((ROOT/old['bank_ref']).read_text())['bank'];ass=list(old['assignments'])
 for path in ['lab/process/k2066-thermal-terminal-response.json','lab/process/k2070-joint-terminal-thermal-bound.json']:
  for i,v in json.loads((ROOT/path).read_text())['replacements'].items():ass[int(i)]=v
 for i,cell in enumerate(bank):assert Q(data['shifts'][str(i)])==strong_shift(cell['s']),'geometry shift'
 geom4={tuple(map(int,k.split(','))):([tuple(map(Q,v)) for v in a['vertices']],[tuple(map(Q,v)) for v in a['rays']]) for k,a in data['quad_arrangements'].items()}
 count=0
 for i,v in data['replacements'].items():count+=assignment(int(i),v,bank,geom,geom3,geom4);ass[int(i)]=v
 a,s=map(Q,data['lower_line']);left,right=map(Q,data['interval']);assert left<Q(5,2)<right
 for v in ass:
  for E in [left,right]:assert Q(v['a'])+Q(v['s'])*E>=a+s*E,'all-cell affine dominance'
 lower,ci=min((Q(v['a'])+Q(5,2)*Q(v['s']),i) for i,v in enumerate(ass));assert lower==Q(data['lower'])==a+Q(5,2)*s and ci==data['bottleneck'],'global lower'
 upper=Q(prev['upper']);assert Q(prev['lower'])<lower<upper
 assert Q(data['upper'])==upper and Q(data['width'])==upper-lower
 assert Q(data['width_reduction'])==(lower-Q(prev['lower']))/(upper-Q(prev['lower']))
 return count,len(bank),bank,geom,geom3,geom4
if __name__=='__main__':
 d=json.loads((ROOT/'lab/process/k2072-compulsory-ladder-thermal-bound.json').read_text());count,n,bank,geom,geom3,geom4=check(d)
 geometry_count=quad_check(geom4);faults=[]
 bad=copy.deepcopy(geom4);bad[(3,2,2,2)][0].pop()
 try:quad_check(bad)
 except AssertionError:faults.append('missing four-terminal vertex')
 else:raise AssertionError('missed four geometry fault')
 v=copy.deepcopy(d['replacements']['164']);v['a']=str(Q(v['a'])+Q(1,100))
 try:assignment(164,v,bank,geom,geom3,geom4,False)
 except AssertionError:faults.append('inflated price')
 else:raise AssertionError('missed inflated price')
 # A forged placement must fail even if its certificate was recomputed.
 assert strong_shift([1,3,5,7,9])==Q(21,2)
 assert strong_shift([2,3])==5
 for support,wrong in [([1],Q(2)),([1,3,5,7,9],Q(11)),([2,3],Q(11,2))]:
  index=next(i for i,cell in enumerate(bank) if cell['s']==support);bad=copy.deepcopy(d);bad['shifts'][str(index)]=str(wrong)
  try:check_shifts(bad,bank)
  except AssertionError:faults.append('wrong mandatory shift')
  else:raise AssertionError('missed placement fault')
 v=copy.deepcopy(d['replacements']['164']);v['mixture']='11/10'
 try:assignment(164,v,bank,geom,geom3,geom4,False)
 except AssertionError:faults.append('nonconvex incoming weight')
 else:raise AssertionError('missed weight')
 # Independently enumerate every path to the removed cap.
 paths=[(9,())];hits=[]
 while paths:
  node,gaps=paths.pop()
  for gap in [1,2,3]:
   nxt=node+gap
   if nxt>18 or (not gaps and nxt<12) or (gaps and gaps[-1]+gap<4):continue
   ng=(*gaps,gap)
   if nxt==18 and gap==2:hits.append(ng)
   paths.append((nxt,ng))
 assert set(hits)=={(3,1,3,2),(3,2,2,2)}
 # Real same-residue counterexample to replacing min by fractional-only shift.
 occupied=[2,3,7,8];physical=set(range(11))
 for shell in range(12):
  inputs=sum(0<=shell-y<=3 for y in occupied)
  assert inputs<=2
  if inputs:assert sum(shell-b in physical for b in range(4))>=2*inputs
 assert 7-2==5<Q(11,2)
 print('PASS',count,'low/high inequalities;',n,'global interval cells;',geometry_count,'four-terminal raw geometry controls;',len(faults),'faults')
