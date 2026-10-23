"""Independent shell census, fixed-budget arrangement vertices and physical witness checks."""
from fractions import Fraction as F
from itertools import product,combinations
from pathlib import Path
import json,copy
ROOT=Path(__file__).resolve().parents[2]
def shellok(A,S):
 for z in range(min(A),max(A)+4):
  if 2*sum(0<=z-e<=3 for e in S)>sum(0<=z-e<=3 for e in A):return False
 return True
def census():
 found={};count=0
 for n in range(3,9):
  for gaps in product([1,2,3],repeat=n-1):
   A=[0]
   for g in gaps:A.append(A[-1]+g)
   count+=1
   for k in range(1,(n-1)//2+1):
    for S in combinations(A[1:-1],k):
     if shellok(A,S):found[S]=min(n,found.get(S,99))
 return found,count
def solve(A,b):
 n=len(b);m=[[F(v) for v in row]+[F(v)] for row,v in zip(A,b)]
 for j in range(n):
  ii=next((i for i in range(j,n) if m[i][j]),None)
  if ii is None:return None
  m[j],m[ii]=m[ii],m[j];f=m[j][j];m[j]=[x/f for x in m[j]]
  for i in range(n):
   if i!=j:
    f=m[i][j];m[i]=[x-f*y for x,y in zip(m[i],m[j])]
 return tuple(row[-1] for row in m)
def ret(S,p,t=F(1,2)):
 inflow=[F(0)]*len(S);Z=sum(t**b for b in range(4))
 for i,e in enumerate(S):
  for j,f in enumerate(S):
   g=f-e
   if g not in [1,2,3]:continue
   L=sum(t**b for b in range(4-int(g)))/Z;delta=L*p[j]-t**int(g)*L*p[i]
   inflow[i]+=max(delta,0);inflow[j]+=max(-delta,0)
 return sum(max(F(0),a-b) for a,b in zip(p,inflow))/2
 # Each unordered pair is visited only once because positive g required.
def minimum(S,E):
 n=len(S);identity=[tuple(F(i==j) for j in range(n)) for i in range(n)];planes={(row,F(0)) for row in identity};planes.add((tuple(map(F,S)),E));edges=[]
 for i,j in combinations(range(n),2):
  g=S[j]-S[i]
  if g not in [1,2,3]:continue
  L=sum(F(1,2)**b for b in range(4-g))/sum(F(1,2)**b for b in range(4));v=[F(0)]*n;v[i]=L*F(1,2)**g;v[j]=-L;v=tuple(v);edges.append((i,j,v));planes.add((v,F(0)))
 for signs in product([-1,1],repeat=len(edges)):
  inc=[[F(0)]*n for _ in range(n)]
  for (i,j,v),s in zip(edges,signs):
   ix=j if s==1 else i;inc[ix]=[a+s*b for a,b in zip(inc[ix],v)]
  for i in range(n):planes.add((tuple(a-b for a,b in zip(identity[i],inc[i])),F(0)))
 best=None
 for rows in combinations(list(planes),n-1):
  p=solve([[F(1)]*n]+[r for r,b in rows],[F(1)]+[b for r,b in rows])
  if p is None or min(p)<0 or sum(e*w for e,w in zip(S,p))>E:continue
  val=ret(S,p)
  if best is None or val<best:best=val
 return best
def tagged_min(delta,shift_a,E=F(7,5)):
 # Fixed5+3 component types; tagged return suppresses cross-component resonances.
 energies=[1+delta,3+delta,F(1)] if shift_a else [F(1),F(3),1+delta]
 boundary={(tuple(F(i==j) for j in range(3)),F(0)) for i in range(3)}
 boundary.add((tuple(energies),E));v=(F(1,5),F(-4,5),F(0));boundary.add((v,F(0)))
 for sign in [-1,1]:
  target=1 if sign==1 else 0
  for i in range(3):boundary.add((tuple(F(i==j)-(sign*v[j] if i==target else 0) for j in range(3)),F(0)))
 best=None
 for rows in combinations(list(boundary),2):
  p=solve([[1,1,1]]+[r for r,b in rows],[1]+[b for r,b in rows])
  if p is None or min(p)<0 or sum(e*w for e,w in zip(energies,p))>E:continue
  diff=(p[0]-4*p[1])/5
  value=(max(F(0),p[0]-max(-diff,0))+max(F(0),p[1]-max(diff,0))+p[2])/2
  if best is None or value<best:best=value
 return best
def check(d,found=None):
 if found is None:found,count=census()
 else:found,count=found
 assert count==d['connected_shape_count'],'complete shape count';bs=d['pareto_blocks']
 for S,n in found.items():
  assert any(len(b['A'])<=n and b['S'][0]<=S[0] and tuple(x-b['S'][0] for x in b['S'])==tuple(x-S[0] for x in S) for b in bs),'coverage'
 for b in bs:assert shellok(b['A'],b['S']),'shell completion'
 vals=[minimum(b['S'],F(7,5)) for b in bs];answer=min(x for x in vals if x is not None);assert answer==F(81,182),'fixed-budget optimum'
 # Check the first reported connected frontier's actual value, not only its label.
 for p in d['connected_eight_level_curve']:
  if F(p['lo'])<=F(7,5) and (p['hi'] is None or F(p['hi'])>=F(7,5)):
   assert F(p['slope'])*F(7,5)+F(p['intercept'])==answer,'curve coefficient'
 for w in d['eight_level_witnesses']:
  A=list(map(F,w['spectrum']));S=list(map(F,w['support']));p=list(map(F,w['weights']));delta=F(w['spacing']);assert min(p)>0 and sum(p)==1
  assert len(A)==len(set(A))==8 and min(b-a for a,b in zip(A,A[1:]))==delta,'spacing'
  for z in {e+b for e in S for b in range(4)}:assert sum(z-e in range(4) for e in A)>=2*sum(z-e in range(4) for e in S),'shell rank'
  assert sum(e*x for e,x in zip(S,p))==F(w['energy'])==F(7,5),'energy'
  assert ret(S,p)==F(w['return_error'])<=answer,'physical return';assert w['strict']==(ret(S,p)<answer),'strictness'
 checked=0
 assert F(d['sharp_spacing_transition'])==F(32,125),'transition'
 for delta in [F(i,100) for i in range(1,101)]+[F(32,125)]:
  expected=min(F(81,182),F(1,2)-F(2,5)/(6+5*delta))
  options=[F(81,182)]+[v for v in [tagged_min(delta,True),tagged_min(delta,False)] if v is not None]
  assert min(options)==expected,'independent tagged optimization';checked+=2
 for c in d['optimal_spacing_controls']:
  delta=F(c['spacing']);expected=min(F(81,182),F(1,2)-F(2,5)/(6+5*delta));assert F(c['value'])==expected,'sharp curve'
  if 'spectrum' in c:
   A=list(map(F,c['spectrum']));S=list(map(F,c['support']));p=list(map(F,c['weights']));assert min(b-a for a,b in zip(A,A[1:]))==delta
   assert sum(e*w for e,w in zip(S,p))==F(7,5) and ret(S,p)==expected,'sharp witness'
 curve=d['delta_one_twentieth_energy_curve'];points={F(p['lo']) for p in curve}
 points|={(F(p['lo'])+F(p['hi']))/2 for p in curve if p['hi'] is not None};points.add(F(curve[-1]['lo'])+1)
 for E in sorted(points):
  connected=min(x for b in bs if (x:=minimum(b['S'],E)) is not None)
  expected=min([connected]+[v for v in [tagged_min(F(1,20),True,E),tagged_min(F(1,20),False,E)] if v is not None])
  value=next(F(p['slope'])*E+F(p['intercept']) for p in curve if F(p['lo'])<=E and (p['hi'] is None or E<=F(p['hi'])))
  assert expected==value,'complete energy curve controls';checked+=1
 return len(found)+len(bs)+len(w['spectrum'])+checked
if __name__=='__main__':
 d=json.load(open(ROOT/'lab/process/k1990-small-dimension-thermal-frontier.json'));fc=census();n=check(d,fc);faults=[]
 for kind in ['coverage','curve','spectrum','return']:
  b=copy.deepcopy(d)
  if kind=='coverage':b['pareto_blocks']=[x for x in b['pareto_blocks'] if x['S']!=[1,3]]
  if kind=='curve':
   next(p for p in b['connected_eight_level_curve'] if p['intercept']=='81/182')['intercept']='4/9'
  if kind=='spectrum':b['eight_level_witnesses'][0]['spectrum'][1]='0'
  if kind=='return':b['eight_level_witnesses'][0]['return_error']='0'
  try:check(b,fc)
  except AssertionError as e:faults.append((kind,str(e)))
  else:raise AssertionError('undetected '+kind)
 print('PASS K1990 independent',n,'coverage/optimization/witness controls; faults',faults)
