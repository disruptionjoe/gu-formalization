"""Independent physical dominance and exact fixed-budget arrangement solver."""
from fractions import Fraction as F
from itertools import product,combinations
from pathlib import Path
import json,copy
ROOT=Path(__file__).resolve().parents[2]
def solve(rows,rhs):
 n=len(rhs);a=[list(map(F,r))+[F(b)] for r,b in zip(rows,rhs)]
 for j in range(n):
  z=next((i for i in range(j,n) if a[i][j]),None)
  if z is None:return None
  a[j],a[z]=a[z],a[j];v=a[j][j];a[j]=[x/v for x in a[j]]
  for i in range(n):
   if i!=j:
    v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[j])]
 return tuple(r[-1] for r in a)
def ret(t,S,p):
 inc=[F(0)]*len(S);Z=sum(t**i for i in range(4))
 for i,j in combinations(range(len(S)),2):
  if S[i]>S[j]:i,j=j,i
  g=S[j]-S[i]
  if g not in (1,2,3):continue
  low=sum(t**b for b in range(4-int(g)))/Z;diff=low*(t**int(g)*p[i]-p[j]);inc[j]+=max(diff,0);inc[i]+=max(-diff,0)
 return sum(max(a-b,0) for a,b in zip(p,inc))/2
def ok(A,S):
 return all(sum(z-a in range(4) for a in A)>=2*sum(z-a in range(4) for a in S) for z in {e+b for e in S for b in range(4)})
def minimum(t,S,E):
 n=len(S);I=[tuple(F(i==j) for j in range(n)) for i in range(n)];planes={(r,F(0)) for r in I}|{(tuple(S),E)};edges=[];Z=sum(t**b for b in range(4))
 for i,j in combinations(range(n),2):
  g=S[j]-S[i]
  if g not in (1,2,3):continue
  lo=sum(t**b for b in range(4-int(g)))/Z;r=[F(0)]*n;r[i]=lo*t**int(g);r[j]=-lo;r=tuple(r);edges.append((i,j,r));planes.add((r,F(0)))
 for signs in product([-1,1],repeat=len(edges)):
  inc=[[F(0)]*n for _ in range(n)]
  for (i,j,r),sgn in zip(edges,signs):
   ix=j if sgn==1 else i;inc[ix]=[a+sgn*b for a,b in zip(inc[ix],r)]
  for i in range(n):planes.add((tuple(a-b for a,b in zip(I[i],inc[i])),F(0)))
 best=None
 for choice in combinations(list(planes),n-1):
  p=solve([[1]*n]+[a for a,b in choice],[1]+[b for a,b in choice])
  if p is None or min(p)<0 or sum(e*w for e,w in zip(S,p))>E:continue
  v=ret(t,S,p)
  if best is None or v<best:best=v
 return best
def check(d,calculated=None):
 count=0
 # Enumerate all three-level component shapes independently, including
 # nonconsecutive completions omitted by a naive pure{0,1,2} assumption.
 three=[dict(spectrum=[0,a,b],occupied=a) for b in range(2,7) for a in range(1,b) if max(a,b-a)<=3 and ok([0,a,b],[a])]
 assert sorted(three,key=lambda a:a['spectrum'])==sorted(d['three_level_types'],key=lambda a:a['spectrum']),'complete three-level types'
 assert ok(list(range(7)),[1,3,5]),'seven-level completion'
 for t in [F(1,7),F(2,5),F(5,6)]:
  for a,b in product(range(11),repeat=2):
   if a+b>10:continue
   p=[F(a,10),F(b,10),1-F(a+b,10)];alpha=1-p[0]
   old=p[0]/2+(alpha*ret(t,[F(1),F(3)],[p[1]/alpha,p[2]/alpha]) if alpha else 0)
   assert ret(t,[F(1),F(3),F(5)],p)<=old,'actual shell return dominance';count+=1
 w=d['sharp_boundary_witness'];A=list(map(F,w['spectrum']));S=list(map(F,w['support']));p=list(map(F,w['weights']))
 assert len(set(A))==8 and min(b-a for a,b in zip(A,A[1:]))==F(1,2),'physical spacing'
 assert ok(A,S) and sum(p)==1 and min(p)>=0,'physical shell support'
 assert sum(e*x for e,x in zip(S,p))==F(18,11),'exact budget'
 assert ret(F(1,2),S,p)==F(w['optimum'])==F(159,374),'physical return'
 assert F(w['right_limit'])-F(w['optimum'])==F(w['right_jump'])==F(59,3740),'right jump'
 if calculated is None:
  prior=json.loads((ROOT/'lab/process/k1990-small-dimension-thermal-frontier.json').read_text());supports=[list(map(F,b['S'])) for b in prior['pareto_blocks']];calculated={}
  for t in [F(1,3),F(1,2),F(2,3)]:
   for E in [F(18,11),F(2),F(3)]:
    conn=min(v for s in supports if (v:=minimum(t,s,E)) is not None)
    for delta in [F(1,2),F(3,4)]:
     candidates=[conn]
     if delta==F(1,2):
      for S in [[F(1),1+delta,3+delta],[F(1),1+delta,F(3)]]:
       v=minimum(t,S,E)
       if v is not None:candidates.append(v)
     calculated[(t,delta,E)]=min(candidates)
 for c in d['curves']:
  t,delta=F(c['temperature']),F(c['spacing'])
  for E in [F(18,11),F(2),F(3)]:
   v=next(F(p['slope'])*E+F(p['intercept']) for p in c['pieces'] if F(p['lo'])<=E and (p['hi'] is None or E<=F(p['hi'])))
   assert v==calculated[(t,delta,E)],'independent budget optimum';count+=1
 return count,calculated
if __name__=='__main__':
 d=json.loads((ROOT/'lab/process/k1992-wide-spacing-eight-level-rigidity.json').read_text());n,cache=check(d);faults=[]
 for kind in ['shape','spectrum','return','curve']:
  b=copy.deepcopy(d)
  if kind=='shape':b['three_level_types'].pop()
  if kind=='spectrum':b['sharp_boundary_witness']['spectrum'][1]='0'
  if kind=='return':b['sharp_boundary_witness']['optimum']='0'
  if kind=='curve':
   row=b['curves'][0];piece=next(p for p in row['pieces'] if F(p['lo'])<=F(18,11) and (p['hi'] is None or F(p['hi'])>=F(18,11)));piece['intercept']=str(F(piece['intercept'])+1)
  try:check(b,cache)
  except AssertionError as e:faults.append((kind,str(e)))
  else:raise AssertionError('undetected '+kind)
 print('PASS K1992 separate',n,'physical and independent optimization controls; mathematical faults',faults)
