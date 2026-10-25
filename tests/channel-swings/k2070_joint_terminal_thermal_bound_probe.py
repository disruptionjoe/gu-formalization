"""Separate bath-shell, polyhedral and all-bank checks. Samples are controls only."""
from fractions import Fraction as Q
from pathlib import Path
from itertools import combinations,product
import json,hashlib,copy
ROOT=Path(__file__).resolve().parents[2];Z=Q(0)
K={1:Q(7,29),2:Q(1,9),3:Q(1,23)};C={1:Q(29,135),2:Q(9,50),3:Q(23,90)}
LH={1:(Q(14,15),Q(7,15)),2:(Q(4,5),Q(1,5)),3:(Q(8,15),Q(1,15))};bath=list(map(Q,['8/15','4/15','2/15','1/15']))
def raw(s,p):
 return sum(max(Z,px-sum(max([Z]+[py*bath[x+j-y] for y,py in zip(s,p) if x+j-y in range(4)]) for j in range(4))/2) for x,px in zip(s,p))
def joint(p,A,u,v,d,e):
 L,H=LH[d];M,J=LH[e]
 first=max(Z,A-max(Z,L*u-H*p));middle=max(Z,u-max(Z,H*p-L*u)-max(Z,M*v-J*u));last=max(Z,v-max(Z,J*u-M*v))
 return (first+middle+last-A)/2

def geometry(d,e):
 L,H=LH[d];M,J=LH[e]
 # Vertical, flow-reversal, middle-zero and final-zero boundaries.
 lines=[(Q(1),Z,x) for x in [Z,H/L,(1+H)/L,H/(1+L)]]+[(Z,Q(1),Z),(-J,M,Z),(-J,1+M,Z),(-(1+J),M,Z),(-(1+L+J),M,-H)]
 points=set();rays={(Q(1),Z),(Z,Q(1))}
 for l,r in combinations(lines,2):
  det=l[0]*r[1]-l[1]*r[0]
  if det:
   u=(l[2]*r[1]-l[1]*r[2])/det;v=(l[0]*r[2]-l[2]*r[0])/det
   if min(u,v)>=0:points.add((u,v))
 for a,b,c in lines:
  if b and -a/b>=0:rays.add((Q(1),-a/b))
 return points,rays

def arrangements(data):
 count=0;out={}
 for d in K:
  for e in K:
   if d+e<4:continue
   a=data['arrangements'][f'{d},{e}'];vs=[tuple(map(Q,v)) for v in a['vertices']];rs=[tuple(map(Q,v)) for v in a['rays']];points,rays=geometry(d,e)
   assert {(x,y) for x,y,c in vs}==points and {(x,y) for x,y,c in rs}==rays,'complete arrangement and recession directions'
   for x,y,c in vs:
    assert raw([0,d,d+e],[Q(1),x,y])-Q(1,2)==c,'vertex raw shell loss';count+=1
   for x,y,c in rs:
    assert raw([0,d,d+e],[Z,x,y])==c,'ray raw shell loss';count+=1
   for p in [Z,Q(1,3),Q(1)]:
    for u in [Z,Q(1,9),Q(1),Q(3)]:
     for v in [Z,Q(1,81),Q(1),Q(5)]:
      assert raw([0,d,d+e],[p,u,v])-p/2==joint(p,p,u,v,d,e),'direct two-terminal response';count+=1
      for r in K:
       if r+d<4:continue
       prev=Q(2);LL,HH=LH[r];A=max(Z,p-max(Z,HH*prev-LL*p))
       assert raw([-r,0,d,d+e],[prev,p,u,v])-raw([-r,0],[prev,p])==joint(p,A,u,v,d,e),'actual incoming response'
       assert joint(p,A,u,v,d,e)>=joint(p,p,u,v,d,e),'worst incoming boundary';count+=2
   out[d,e]=vs,rs
 return out,count

def rref(matrix):
 a=[list(row) for row in matrix];piv=[];i=0
 for j in range(len(a[0])-1):
  k=next((k for k in range(i,len(a)) if a[k][j]),None)
  if k is None:continue
  a[i],a[k]=a[k],a[i];v=a[i][j];a[i]=[x/v for x in a[i]]
  for k in range(len(a)):
   if k!=i:
    v=a[k][j];a[k]=[x-v*y for x,y in zip(a[k],a[i])]
  piv.append(j);i+=1
  if i==len(a):break
 return a,piv

def geometry3(gaps):
 # Independently form affine equations from all neighboring flow branches.
 flows=[]
 for i,d in enumerate(gaps):
  L,H=LH[d];v=[Z]*4;v[i]=H;v[i+1]=-L;flows.append(v)
 forms=[]
 for i in range(4):
  for incoming in ([False] if i==0 else [False,True]):
   for outgoing in ([False] if i==3 else [False,True]):
    v=[Q(int(j==i)) for j in range(4)]
    if incoming:v=[x-y for x,y in zip(v,flows[i-1])]
    if outgoing:v=[x+y for x,y in zip(v,flows[i])]
    forms.append(v)
 forms+=flows;lines=set()
 for v in forms:
  if not any(v[1:]):continue
  a=next(x for x in v[1:] if x);lines.add(tuple(x/a for x in v[1:]+[-v[0]]))
 points=set();rays=set()
 for rows in combinations(sorted(lines),3):
  rr,piv=rref(rows)
  if len(piv)==3:
   x=tuple(row[3] for row in rr)
   if min(x)>=0:points.add(x)
 for rows in combinations(sorted(lines),2):
  rr,piv=rref([list(r[:3])+[Z] for r in rows])
  if len(piv)!=2:continue
  free=next(j for j in range(3) if j not in piv);x=[Z]*3;x[free]=Q(1)
  for row,j in zip(rr,piv):x[j]=-row[free]
  if min(x)<0:continue
  a=next(xx for xx in x if xx);rays.add(tuple(xx/a for xx in x))
 return points,rays

def triple_checks(data):
 out={};count=0
 for gaps in product(K,repeat=3):
  if gaps[0]+gaps[1]<4 or gaps[1]+gaps[2]<4:continue
  rec=data['triple_arrangements'][','.join(map(str,gaps))];vs=[tuple(map(Q,v)) for v in rec['vertices']];rs=[tuple(map(Q,v)) for v in rec['rays']];pts,rays=geometry3(gaps)
  assert {v[:3] for v in vs}==pts and {v[:3] for v in rs}==rays,'complete three-terminal arrangement'
  support=[0,gaps[0],sum(gaps[:2]),sum(gaps)]
  for x,y,z,c in vs:assert raw(support,[Q(1),x,y,z])-Q(1,2)==c,'three-terminal vertex raw cost';count+=1
  for x,y,z,c in rs:assert raw(support,[Z,x,y,z])==c,'three-terminal ray raw cost';count+=1
  out[gaps]=vs,rs
 return out,count

def allowed(s):return [d for d in K if s[-1]+d>=12 and (len(s)==1 or s[-1]-s[-2]+d>=4)]
def bell(a,t,offset=0):
 assert t>0 and a<=65*t,'finite cutoff'
 g={}
 for n in range(64,11,-1):
  for d in K:g[n,d]=max([Z]+[a-t*(n+offset)+K[e]*g.get((n+e,e),Z) for e in K if d+e>=4])
 return g

def assignment(ci,v,bank,geom,geom3,high=True):
 a,t=Q(v['a']),-Q(v['s']);s=bank[ci]['s'];z=s[-1];ell=max(1,s[-2]+1) if len(s)>1 else 1;g=bell(a,t);h=bell(a,t,ell);count=0
 third=set()
 for d in allowed(s):
  for e in K:
   if d+e>=4:
    for f in K:
     if e+f>=4:third.update((z+d+e+f+h,h) for h in K if f+h>=4)
 for n in range(12,65):
  for d in K:
   if (n,d) in third:third.update((n+e,e) for e in K if d+e>=4 and n+e<=64)
 assert all(g[n,d]<=C[d] for n,d in third if n<=64),'fourth-plus caps'
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
    g3=g[n+e+f,f];vs3,rs3=geom3[d,e,f]
    assert all(q*x+gg*y+g3*z<=c for x,y,z,c in rs3),'triple recession';add_price(vs3,[q,gg,g3],d)
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

def certificate(data):
 for p,h in data['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'pin'
 geom,raw_count=arrangements(data);geom3,n3=triple_checks(data);raw_count+=n3;old=json.loads((ROOT/'lab/process/k2059-energy-aware-thermal-tail.json').read_text());prev=json.loads((ROOT/data['base_ref']).read_text());bank=json.loads((ROOT/old['bank_ref']).read_text())['bank'];ass=list(old['assignments'])
 for k,v in prev['replacements'].items():ass[int(k)]=v
 count=0
 for k,v in data['replacements'].items():count+=assignment(int(k),v,bank,geom,geom3);ass[int(k)]=v
 a,s=map(Q,data['lower_line']);left,right=map(Q,data['interval']);assert left<Q(5,2)<right
 assert all(Q(v['a'])+Q(v['s'])*E>=a+s*E for v in ass for E in [left,right]),'671 interval assignments'
 value,ci=min((Q(v['a'])+Q(5,2)*Q(v['s']),i) for i,v in enumerate(ass));assert value==Q(data['lower'])==a+Q(5,2)*s and ci==data['bottleneck'],'global lower'
 upper=json.loads((ROOT/'lab/process/k2068-thermal-population-construction.json').read_text());assert Q(prev['lower'])<value<Q(upper['value']),'strict bracket improvement'
 assert Q(data['upper'])==Q(upper['value']) and Q(data['width'])==Q(upper['value'])-value,'reported width'
 assert Q(data['gain'])==value-Q(prev['lower']) and Q(data['width_reduction'])==(value-Q(prev['lower']))/(Q(upper['value'])-Q(prev['lower'])),'reported gain'
 return raw_count,count,bank,geom,geom3
if __name__=='__main__':
 data=json.loads((ROOT/'lab/process/k2070-joint-terminal-thermal-bound.json').read_text());nr,nc,bank,geom,geom3=certificate(data)
 faults=[]
 bad=copy.deepcopy(data);bad['arrangements']['2,2']['vertices'].pop()
 try:arrangements(bad)
 except AssertionError as e:faults.append(('missing_vertex',str(e)))
 else:raise AssertionError('missed geometry mutation')
 bad=copy.deepcopy(data);bad['arrangements']['2,2']['rays'][0][2]='0'
 try:arrangements(bad)
 except AssertionError as e:faults.append(('recession_cost',str(e)))
 else:raise AssertionError('missed ray mutation')
 ci=int(next(iter(data['replacements'])));v=copy.deepcopy(data['replacements'][str(ci)]);v['a']=str(Q(v['a'])+Q(1,100))
 try:assignment(ci,v,bank,geom,geom3,False)
 except AssertionError as e:faults.append(('inflated_price',str(e)))
 else:raise AssertionError('missed price mutation')
 assert joint(Q(1),Q(1),Q(2),Q(3),2,2)!=2*joint(Q(1),Q(1),Q(2),Q(3),2,2);faults.append(('lost_half','raw finite shell counterexample'))
 bad=copy.deepcopy(data);bad['triple_arrangements']['2,2,2']['vertices'].pop()
 try:triple_checks(bad)
 except AssertionError as e:faults.append(('missing_triple_vertex',str(e)))
 else:raise AssertionError('missed triple geometry mutation')
 v=copy.deepcopy(data['replacements']['164']);v['mixture']='11/10'
 try:assignment(164,v,bank,geom,geom3,False)
 except AssertionError:faults.append(('nonconvex_weight','weight outside [0,1]'))
 else:raise AssertionError('missed mixture mutation')
 print('PASS raw/geometry controls',nr,'new low/high inequalities',nc,'all671 interval lines; faults',faults)
