"""Separate integer elimination census and direct bath-label realizations."""
from fractions import Fraction as F
from itertools import product,combinations
from math import gcd
from functools import reduce
from pathlib import Path
import json,hashlib,copy
ROOT=Path(__file__).resolve().parents[2];weights=[F(8,15),F(4,15),F(2,15),F(1,15)]
P={'A':[F(x,1306) for x in [486,729,81,9,1]],'B':[F(x,181) for x in [36,54,81,9,1]],'D':[F(x,145) for x in [54,81,9,1]],'Q':[F(1,5),F(3,10),F(9,20),F(1,20)],'T':[F(x,11755) for x in [4374,6561,729,81,9,1]],'C':[F(3,8),F(9,16),F(1,16)]}
def physical(ss,pp,spec,d):
 assert sum(pp)==1 and min(pp)>=0,'population'
 spec=sorted(spec);assert len(set(spec))==len(spec) and min(spec)>=0,'spectrum'
 assert all(y-x>=d for x,y in zip(spec,spec[1:])),'spacing'
 active=[s for s,p in zip(ss,pp) if p]
 for e in {s+b for s in active for b in range(4)}:
  assert sum(e-s in range(4) for s in spec)>=2*sum(e-s in range(4) for s in active),'shell capacity'
 ret=F(0)
 for s,p in zip(ss,pp):
  capture=sum(max(q*weights[int(s+b-y)] for y,q in zip(ss,pp) if s+b-y in range(4)) for b in range(4))
  ret+=max(F(0),p-capture/2)
 return sum(x*y for x,y in zip(ss,pp)),ret

def common_return_cell(support,p,q):
 # Endpoint signs certify the whole population segment, not a sample grid.
 captures=[[F(0)]*len(support),[F(0)]*len(support)]
 for i,x in enumerate(support):
  for b in range(4):
   indices=[j for j,y in enumerate(support) if x+b-y in range(4)]
   vals=[[v[j]*weights[int(x+b-support[j])] for j in indices] for v in [p,q]]
   winners=[{indices[k] for k,v in enumerate(row) if v==max(row)} for row in vals]
   assert winners[0]&winners[1],'shared shell maximum'
   for t,row in enumerate(vals):captures[t][i]+=max(row)/2
 for i in range(len(support)):
  assert (p[i]-captures[0][i])*(q[i]-captures[1][i])>=0,'shared clipping chamber'

def normalized(row):
 g=reduce(gcd,map(abs,row),0)
 if not g:return None
 row=tuple(v//g for v in row)
 return row if next(x for x in row if x)>0 else tuple(-x for x in row)
def nullpoint(rows,n):
 # Fraction-free row elimination, distinct from producer's signed cofactors.
 a=[list(x) for x in rows];piv=[];rank=0
 for col in range(n):
  p=next((j for j in range(rank,len(a)) if a[j][col]),None)
  if p is None:continue
  a[rank],a[p]=a[p],a[rank];lead=a[rank][col]
  for j in range(rank+1,len(a)):
   if a[j][col]:
    row=[lead*x-a[j][col]*y for x,y in zip(a[j],a[rank])];g=reduce(gcd,map(abs,row),0);a[j]=[x//g for x in row] if g else row
  piv.append(col);rank+=1
  if rank==len(a):break
 if rank!=n-1:return None
 free=next(j for j in range(n) if j not in piv);v=[F(0)]*n;v[free]=F(1)
 for i in range(rank-1,-1,-1):
  col=piv[i];v[col]=-sum((F(a[i][j])*v[j] for j in range(col+1,n)),F(0))/F(a[i][col])
 total=sum(v)
 if total==0:return None
 v=tuple(x/total for x in v);return v if min(v)>=0 else None

def independent_bank(bank):
 # Generate supports by advancing physical roots, independent of producer gap recursion.
 supp={(1,)}
 def go(s):
  supp.add(s)
  for gap in range(1,4):
   if s[-1]+gap<=11 and (len(s)==1 or s[-1]-s[-2]+gap>=4):go(s+(s[-1]+gap,))
 for gap in range(1,4):
  root=max(1,3-gap);go((root,root+gap))
 expected={(ss,o) for ss in supp for o in product([-1,1],repeat=len(ss)-1)}
 actual={(tuple(c['s']),tuple(c['o'])) for c in bank};assert actual==expected,'support/orientation completeness'
 bases=0
 for c in bank:
  ss=c['s'];o=c['o'];n=len(ss);edges=[];incoming=[[0]*n for _ in ss]
  for i,sign in enumerate(o):
   gap=ss[i+1]-ss[i];H=sum(weights[gap:])*15;L=sum(weights[:4-gap])*15
   row=[0]*n;row[i]=int(H);row[i+1]=-int(L);edges.append([sign*x for x in row]);j=i+1 if sign==1 else i
   incoming[j]=[x+sign*y for x,y in zip(incoming[j],row)]
  deficit=[[15*int(i==j)-incoming[i][j] for j in range(n)] for i in range(n)]
  planes=sorted({r for row in edges+deficit+[[int(i==j) for i in range(n)] for j in range(n)] if (r:=normalized(row)) is not None});points=set()
  for rows in combinations(planes,n-1):
   bases+=1;p=nullpoint(rows,n)
   if p is not None and all(sum(x*y for x,y in zip(e,p))>=0 for e in edges):points.add(p)
  expected_points={tuple(map(F,v['p'])) for v in c['vertices']}
  assert points==expected_points,('complete vertex set',ss,o,points-expected_points,expected_points-points)
 return bases

def replay(r,enumerate_bank=False):
 bank=r['bank'];direct=[];count=0
 for c in bank:
  vals=[]
  for v in c['vertices']:
   e,val=physical(list(map(F,c['s'])),list(map(F,v['p'])),list(map(F,range(15))),F(1));assert e==F(v['energy']) and val==F(v['value']),'bath vertex';vals.append((e,val));count+=1
  direct.append(vals)
 ep={}
 for name,p in P.items():
  e,v=physical(list(map(F,range(1,2*len(p),2))),p,list(map(F,range(2*len(p)+1))),F(1));assert [str(e),str(v)]==r['endpoints'][name],'endpoint actual';ep[name]=(e,v)
 def points(side,d):
  names={'A':('A','B'),'DQ':('D','Q'),'QB':('Q','B'),'AT':('A','T'),'TB':('T','B')};n,m=names[side];x,y=ep[n];z,w=ep[m]
  if side in ['A','TB']:z+=d
  if side=='DQ':x+=d
  return x,y,z,w
 def residual(side,d,e,v):
  x,y,z,w=points(side,d);return (z-x)*(v-y)-(w-y)*(e-x)
 def value(side,d,e):
  x,y,z,w=points(side,d);return y+(w-y)*(e-x)/(z-x)
 for phase in r['phases']:
  lo,hi=map(F,phase['interval']);sides=set()
  for pair,labels in phase['assignments'].items():
   assert len(labels)==len(bank)
   for i,labels_i in enumerate(labels):
    assert labels_i
    for side in labels_i:
     assert side in pair.split('+');sides.add(side)
     for d in [lo,hi]:assert all(residual(side,d,e,v)>=0 for e,v in direct[i]),'low coefficient'
  for side in sides:
   for d in [lo,hi]:
    assert all(residual(side,d,e+d,v)>=0 for vs in direct for e,v in vs),'high coefficient'
    assert residual(side,d,F(12),F(0))>0,'tail coefficient'
 physical_count=0
 for d in [F(1,50),F(1,10),F(1,3),F(628,1629),F(39,100),F(2,5)]:
  for low,high,side in [('A','B','A'),('Q','D','DQ'),('T','B','TB')]:
   for mass in [F(1,10),F(1,2),F(9,10)]:
    p,q=P[low],P[high];ss=[F(k) for k in range(1,2*len(p),2)]+[F(k)+d for k in range(1,2*len(q),2)];pp=[(1-mass)*v for v in p]+[mass*v for v in q];sp=[F(k) for k in range(2*len(p)+1)]+[F(k)+d for k in range(2*len(q)+1)];e,v=physical(ss,pp,sp,d);assert residual(side,d,e,v)==0,'separated attainment';physical_count+=1
 for low,high,side in [('Q','B','QB'),('A','T','AT')]:
  common_return_cell(list(range(1,2*len(P[high]),2)),P[low]+[F(0)]*(len(P[high])-len(P[low])),P[high])
  for mass in [F(0),F(1,10),F(1,2),F(9,10),F(1)]:
   p,q=P[low],P[high];p=p+[F(0)]*(len(q)-len(p));pp=[(1-mass)*x+mass*y for x,y in zip(p,q)];e,v=physical(list(map(F,range(1,2*len(q),2))),pp,list(map(F,range(2*len(q)+1))),F(1));assert residual(side,F(1,3),e,v)==0,'connected attainment';physical_count+=1
 for w in r['boundary_rivals']:
  d,e,v=F(w['delta']),F(w['energy']),F(w['value'])
  if w['kind']=='unshifted T':
   p=P['T'];ae,av=physical(list(map(F,range(1,12,2))),p,list(map(F,range(13))),d);old=min(value('A',d,e),max(value('DQ',d,e),value('QB',d,e)))
  else:
   m=F(w['shifted_C_mass']);p=P['Q'];q=P['C'];ae,av=physical([F(k) for k in [1,3,5,7]]+[F(k)+d for k in [1,3,5]],[(1-m)*v for v in p]+[m*v for v in q],[F(k) for k in range(9)]+[F(k)+d for k in range(7)],d);old=min(max(value('AT',d,e),value('TB',d,e)),max(value('DQ',d,e),value('QB',d,e)))
  assert (ae,av)==(e,v) and v<old==F(w['previous']),'physical rival'
 removed=0
 for name in ['A','B','D','Q','T']:
  p=P[name];ss=list(map(F,range(1,2*len(p),2)));spec=list(map(F,range(2*len(p)+1)))
  for x in spec:
   try:physical(ss,p,[q for q in spec if q!=x],F(1))
   except AssertionError as er:assert str(er)=='shell capacity';removed+=1
   else:raise AssertionError('completion removal passed')
 if enumerate_bank:assert independent_bank(bank)==r['basis_count']==626412
 return dict(records=count,physical_controls=physical_count,boundary_rivals=2,necessary_completion_removals=removed,complete_basis_replay=enumerate_bank)
if __name__=='__main__':
 r=json.loads((ROOT/'lab/process/k2045-third-thermal-spacing-phase.json').read_text())
 for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 print('BASELINE',replay(r,True),flush=True)
 # Do not rerun independent enumeration for faults whose changed mathematics is downstream.
 faults=[]
 for label,edit in [('third interval',lambda v:v['phases'][0]['interval'].__setitem__(1,'2/5')),('fourth interval',lambda v:v['phases'][1]['interval'].__setitem__(1,'401/1000')),('actual endpoint',lambda v:v['endpoints']['T'].__setitem__(1,'1/4')),('rival mass',lambda v:v['boundary_rivals'][1].__setitem__('shifted_C_mass','1/2'))]:
  z=copy.deepcopy(r);edit(z)
  try:replay(z)
  except AssertionError as er:faults.append([label,str(er)])
  else:raise AssertionError('missed '+label)
 print('PASS four mathematical faults',faults)
