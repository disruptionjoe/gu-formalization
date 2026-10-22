"""Independent prefix census, bath-label dual reconstruction and tail controls."""
from fractions import Fraction as F
from itertools import combinations,product
from pathlib import Path
from copy import deepcopy
import json,hashlib
from k1950_global_catalyst_energy_certificates_probe import independent_cell,shell_return,rank
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1952-catalyst-path-energy-extension.json'
def prefixes(K):
 out=[]
 for n in range(1,K+4):
  for s in combinations(range(1,K+4),n):
   ds=[b-a for a,b in zip(s,s[1:])]
   if not ds:
    if s==(1,):out.append((s,False))
    continue
   if s[0]!=max(1,3-ds[0]) or any(d not in [1,2,3] for d in ds) or any(a+b<4 for a,b in zip(ds,ds[1:])):continue
   if s[-1]<=K:out.append((s,False))
   elif s[-2]<=K:out.append((s,True))
 return out

def audit(v,math_only=False):
 count=0;dot=lambda x,y:sum(a*b for a,b in zip(x,y))
 if not math_only:
  assert v['result_id']=='K1952','report identity'
  for p,h in v['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'input pin'
 for idx,cert in enumerate(v['global_duals']):
  t,b,a=map(F,[cert['t'],cert['slope'],cert['intercept']]);K=cert['cutoff']
  expected={(s,o,tail) for s,tail in prefixes(K) for o in product([-1,1],repeat=len(s)-1)}
  keys=[(tuple(r['support']),tuple(r['orientation']),r['tail']) for r in cert['cells']]
  assert len(keys)==len(set(keys)) and set(keys)==expected,'independent exhaustive crossing census'
  for r in cert['cells']:
   s=r['support'];n=len(s);A,c,eq=independent_cell(s,r['orientation'],t,b)
   if r['tail']:A=A[:-1];c[-1]=F(0)
   x=list(map(F,r['x']));y=list(map(F,r['y']));val=F(r['intercept'])
   assert len(x)==len(c) and len(y)==len(A),'exact dimensions'
   assert min(x)>=0 and dot(eq,x)==1 and all(dot(row,x)<=0 for row in A),'independent primal restrictions'
   assert max(y)<=0,'dual sign'
   slack=[c[j]-val*eq[j]-sum(row[j]*z for row,z in zip(A,y)) for j in range(2*n)]
   assert min(slack)>=0 and dot(c,x)==val>=a,'actual bath dual coefficients'
   if idx==2 and val==a:
    active=[eq]+[row for row,z in zip(A,y) if z<0]+[[F(int(i==j)) for i in range(2*n)] for j,z in enumerate(slack) if z>0]
    rr=rank(active)
    assert all(rank(active+[[F(int(i==j)) for i in range(2*n)]])==rr for j in range(n)),'fixed equality populations'
    endpoints=[list(zip(p['support'],map(F,p['weights']))) for p in v['points'][2:]]
    assert [(e,p) for e,p in zip(s,x) if p] in endpoints,'only endpoint equality'
    if r['tail']:assert x[n-1]==0,'equality forbids omitted tail'
    count+=3
   count+=4
  count+=1
 for rec in v['consumers']:
  s=list(map(F,rec['support']));p=list(map(F,rec['weights']));E=F(rec['energy']);r=F(rec['return_cost']);assert sum(p)==1 and dot(s,p)==E,'physical mass and energy'
  assert shell_return(F(1,2),s,p)==r,'independent all-bath return'
  if rec['kind']=='attained':
   bank=v['global_duals'][rec['segment']];assert r==F(bank['intercept'])-F(bank['slope'])*E,'matching supporting line'
  else:assert r>F(rec['infimum']),'finite approximation is strictly above infimum'
  count+=3
 return count

def tail_controls():
 count=0
 for t in [F(1,4),F(1,2),F(3,4)]:
  bath=[t**j/sum(t**k for k in range(4)) for j in range(4)]
  for s in [[1,3,5,7,9],[2,3,6,7,10],[1,4,5,8,9]]:
   for weights in [[1,2,3,4,5],[10,1,1,1,10],[1,10,1,10,1]]:
    p=[F(w,sum(weights)) for w in weights];whole=shell_return(t,s,p)
    for cut in range(1,len(s)):
     ss=s[:cut+1];pp=p[:cut]+[sum(p[cut:])];incoming=[F(0)]*len(ss)
     for i in range(len(ss)-1):
      d=ss[i+1]-ss[i];lo=sum(bath[j] for j in range(4-d));hi=sum(bath[j] for j in range(d,4));diff=hi*pp[i]-lo*pp[i+1]
      incoming[i]+=max(F(0),-diff);incoming[i+1]+=max(F(0),diff)
     relaxed=sum(max(F(0),w-inc) for w,inc in zip(pp[:-1],incoming[:-1]))/2
     assert relaxed<=whole,'collapsed tail lower return'
     assert sum(e*w for e,w in zip(ss,pp))<=sum(e*w for e,w in zip(s,p)),'collapsed energy lower bound'
     count+=2
 return count
if __name__=='__main__':
 v=json.loads(OUT.read_text());print('PASS K1952 independent baseline',audit(v)+tail_controls(),'exact controls',flush=True)
 catches=[]
 for kind in ['missing_crossing','dual','population','tail_energy']:
  w=deepcopy(v);bank=w['global_duals'][0];r=next(r for r in bank['cells'] if r['tail'])
  if kind=='missing_crossing':bank['cells'].remove(r)
  elif kind=='dual':r['intercept']=str(F(r['intercept'])+1)
  elif kind=='population':r['x'][0]=str(F(r['x'][0])+F(1,100))
  else:r['support'][-1]+=1
  try:audit(w,True)
  except AssertionError as e:catches.append((kind,str(e)))
  else:raise AssertionError('undetected input fault '+kind)
 print('PASS genuine mathematical faults',catches,flush=True)
 for kind in ['identity','pin']:
  w=deepcopy(v)
  if kind=='identity':w['result_id']='K0'
  else:w['inputs'][next(iter(w['inputs']))]='0'*64
  try:audit(w)
  except AssertionError as e:print('PASS reporting fault',kind,str(e))
  else:raise AssertionError('undetected reporting fault')
