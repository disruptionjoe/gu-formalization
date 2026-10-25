"""Separate bath-label polytope replay, physical witnesses and real fault controls."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,product
import json,hashlib
from sage.all import QQ,matrix
ROOT=Path(__file__).resolve().parents[2]
bath=[F(8,15),F(4,15),F(2,15),F(1,15)]
def physical(s,p,spec):
 assert sum(p)==1 and min(p)>=0,'population'
 active=[x for x,v in zip(s,p) if v]
 for z in {x+b for x in active for b in range(4)}:
  assert sum(z-x in range(4) for x in spec)>=2*sum(z-x in range(4) for x in active),'shell capacity'
 deficits=[]
 for x,v in zip(s,p):deficits.append(v-sum(max(q*bath[z-y] for y,q in zip(s,p) if z-y in range(4)) for z in range(x,x+4))/2)
 return sum(max(v,0) for v in deficits),deficits

def shape_words(N):
 yield (1,)
 for n in range(2,(N+1)//2+2):
  for gaps in product((1,2,3),repeat=n-1):
   if any(a+b<4 for a,b in zip(gaps,gaps[1:])):continue
   start=max(1,3-gaps[0]);s=[start]
   for d in gaps:s.append(s[-1]+d)
   if s[-1]<=N:yield tuple(s)
def planes(s,o):
 n=len(s);edges=[];defs=[]
 for i,sgn in enumerate(o):
  d=s[i+1]-s[i];row=[F(0)]*n;row[i]=sgn*sum(bath[d:]);row[i+1]=-sgn*sum(bath[:4-d]);edges.append(row)
 for i,x in enumerate(s):
  row=[F(j==i) for j in range(n)]
  for z in range(x,x+4):
   entries=[(j,z-y) for j,y in enumerate(s) if z-y in range(4)];assert len(entries)<=2
   j,k=entries[0] if len(entries)==1 or o[entries[0][0]]==1 else entries[1];row[j]-=bath[k]/2
  defs.append(row)
 def normal(row):
  first=next((v for v in row if v),None)
  return tuple(v/first for v in row) if first else None
 ps={normal(row) for row in edges+defs+[[F(i==j) for j in range(n)] for i in range(n)]};ps.discard(None)
 return edges,defs,sorted(ps)
def replay(r):
 for path,digest in r['inputs'].items():assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,'input provenance'
 count=0;contacts={};look={}
 for N,cells in r['banks'].items():
  expected={(s,o) for s in shape_words(int(N)) for o in product((-1,1),repeat=len(s)-1)};assert expected=={(tuple(c['s']),tuple(c['o'])) for c in cells}
  for cell in cells:
   ss,o=cell['s'],cell['o'];n=len(ss);ed,df,ps=planes(ss,o);vertices=set()
   for rows in combinations(ps,n-1):
    T=matrix(QQ,[list(row) for row in rows]) if rows else matrix(QQ,0,n);ker=T.right_kernel().basis_matrix()
    if ker.nrows()!=1:continue
    v=list(ker[0]);den=sum(v)
    if not den:continue
    pv=tuple(F(int((x/den).numerator()),int((x/den).denominator())) for x in v)
    if min(pv)<0 or any(sum(a*b for a,b in zip(row,pv))<0 for row in ed):continue
    vertices.add(pv)
   assert vertices=={tuple(map(F,v['p'])) for v in cell['vertices']},'complete vertex set'
   for v in cell['vertices']:
    pv=list(map(F,v['p']));en=sum(x*y for x,y in zip(ss,pv));rr=sum(max(sum(a*b for a,b in zip(row,pv)),0) for row in df)
    assert (en,rr)==(F(v['energy']),F(v['value'])),'bath return'
    count+=1
 for phase in r['phases']:
  A,C=map(F,[phase['intercept'],phase['slope']]);N=phase['cutoff'];lo,hi=map(F,phase['phase']);seen=set()
  for cell in r['banks'][str(N)]:
   for v in cell['vertices']:
    gap=F(v['value'])+C*F(v['energy'])-A;assert gap>=0,'global supporting line'
    if gap==0:seen.add(tuple((x,y) for x,y in zip(cell['s'],v['p']) if F(y)))
  assert len(seen)==2 and seen=={tuple(tuple(v) for v in x) for x in phase['contacts']}
  assert C*(N+1)-A==F(phase['tail_gap'])>0,'tail coefficient'
  ends=phase['witnesses'][::2];ss=ends[1]['support'];pp=[list(map(F,w['population'])) for w in ends];dd=[]
  for w in phase['witnesses']:
   value,df=physical(w['support'],list(map(F,w['population'])),w['spectrum']);assert value==F(w['return_value'])==A-C*F(w['energy'])
  for p,w in zip(pp,ends):dd.append(physical(ss,p,w['spectrum'])[1])
  assert all(a*b>=0 for a,b in zip(*dd)),'affine deficit signs'
  for z in {x+b for x in ss for b in range(4)}:
   terms=[(j,z-x) for j,x in enumerate(ss) if z-x in range(4)];winners=[]
   for p in pp:
    maximum=max(p[j]*bath[k] for j,k in terms);winners.append({(j,k) for j,k in terms if p[j]*bath[k]==maximum})
   assert winners[0]&winners[1],'shared whole-interval shell maximum'
  # Each pair of consecutive positive odd inputs forces every level in the shared shells.
  mandatory=set()
  for a,b in zip(ss,ss[1:]):
   assert b-a==2
   for z in [b,b+1]:mandatory.update(range(z-3,z+1))
  assert mandatory==set(range(N+2)), 'sharp completion'
  contacts[str(N)]=len(seen)
 gap=r['supporting_gap'];A,C=F(gap['intercept']),F(gap['slope'])
 for c in r['banks']['9']:
  for v in c['vertices']:assert F(v['value'])+C*F(v['energy'])>=A
 # Recompute the failed chord from its actual diagonal and full physical completion.
 ss=[1,3,5,7,9];pa=[F(x,1306) for x in (486,729,81,9,1)];pb=[F(x,181) for x in (36,54,81,9,1)];pm=[(a+b)/2 for a,b in zip(pa,pb)]
 actual,_=physical(ss,pm,list(range(11)));energy=sum(x*y for x,y in zip(ss,pm))
 assert actual==F(gap['midpoint_actual']) and energy==F(gap['energy']) and A-C*energy==F(gap['midpoint_bound'])
 assert F(gap['midpoint_actual'])-F(gap['midpoint_bound'])==F(gap['gap'])>0
 assert 10*C-A==F(549,13840)>0
 for item in r['tail_family']:
  m=item['tail'];weights=[F(1)]+[F(3,2)*F(1,9)**j for j in range(m+1)];s=list(range(1,2*len(weights),2));p=[x/sum(weights) for x in weights]
  value,_=physical(s,p,list(range(item['physical_dimension'])))
  assert value==F(item['value'])==p[1]/2 and sum(x*y for x,y in zip(s,p))==F(item['energy'])
 # Infinite-tail moments from geometric series; equality is algebraic, not a finite-tail extrapolation.
 Z=F(1)+F(3,2)/(1-F(1,9));moment=F(1)+F(3,2)*(3/(1-F(1,9))+2*F(1,9)/(1-F(1,9))**2)
 assert moment/Z==F(415,172) and F(3,4)/Z==F(12,43)
 assert F(12,43)-(A-C*F(415,172))==F(21,2380480)
 return dict(vertices=count,phases=len(r['phases']),contact_vertices=contacts)
def faults(r):
 w=r['phases'][0]['witnesses'][1];s=w['support'];p=list(map(F,w['population']));spec=w['spectrum'];physical(s,p,spec)
 caught=[]
 for name,ss,pp,sp in [('normalization',s,[x*2 for x in p],spec),('missing completion',s,p,[x for x in spec if x!=2])]:
  try:physical(ss,pp,sp)
  except AssertionError as e:print('DETECTED',name,str(e));caught.append(name)
  else:raise AssertionError('missed physical fault')
 rr,_=physical(s,p,spec);assert rr!=F(w['return_value'])+F(1,100),'return corruption';caught.append('return corruption')
 # A raised supporting intercept fails an actual equality vertex.
 v=r['banks']['5'][0]['vertices'][0];c=r['phases'][0]['contacts'][0];e=sum(x*F(y) for x,y in c);rr,_=physical([x for x,y in c],[F(y) for x,y in c],list(range(5)))
 assert rr+F(3,28)*e<F(15,28)+F(1,100);caught.append('raised intercept')
 assert F(3,28)*5-F(15,28)==0;assert F(3,28)*6-F(15,28)>0;caught.append('tail cutoff without strict gap')
 return caught
if __name__=='__main__':
 r=json.loads((ROOT/'lab/process/k2037-thermal-seven-level-boundary.json').read_text());print('BASELINE',replay(r));print('PASS faults',faults(r))
