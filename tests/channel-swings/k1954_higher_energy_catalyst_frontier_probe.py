"""Independent bath-label tail pricing and rational global certificate verifier."""
from fractions import Fraction as F
from pathlib import Path
from copy import deepcopy
from itertools import product
import json,hashlib
from k1952_catalyst_path_energy_extension_probe import prefixes
from k1950_global_catalyst_energy_certificates_probe import independent_cell,shell_return,rank
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1954-higher-energy-catalyst-frontier.json'
def audit(v,math_only=False,fault=None):
 count=0;dot=lambda x,y:sum(a*b for a,b in zip(x,y))
 if not math_only:
  assert v['result_id']=='K1954','report identity'
  for p,h in v['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,'input pin'
 for idx,bank in enumerate(v['global_duals']):
  t,b,a=map(F,[bank['t'],bank['slope'],bank['intercept']]);K=bank['cutoff'];bath=[t**j/sum(t**k for k in range(4)) for j in range(4)]
  expected={(s,o,tail) for s,tail in prefixes(K) for o in product([-1,1],repeat=len(s)-1)};keys=[(tuple(r['support']),tuple(r['orientation']),r['tail']) for r in bank['cells']]
  assert len(keys)==len(set(keys)) and set(keys)==expected,'independent complete prefix census'
  populations=[];fixed=True;tail_positive=False
  for r in bank['cells']:
   s=r['support'];n=len(s);A,c,eq=independent_cell(s,r['orientation'],t,b)
   if r['tail']:
    d=s[-1]-s[-2];hi=sum(bath[d:]);floor=t*t/(1+t*t)**2
    A[-1]=[F(0)]*(2*n);A[-1][n-2]=-hi;A[-1][n-1]=0 if fault=='tail_price' else 2*floor;A[-1][-1]=-1
   x=list(map(F,r['x']));y=list(map(F,r['y']));val=F(r['intercept'])
   assert len(x)==len(c) and len(y)==len(A),'dimensions'
   assert min(x)>=0 and dot(eq,x)==1 and all(dot(row,x)<=0 for row in A),'independent primal constraints'
   assert max(y)<=0,'dual signs'
   slack=[c[j]-val*eq[j]-sum(row[j]*z for row,z in zip(A,y)) for j in range(2*n)]
   assert min(slack)>=0 and dot(c,x)==val>=a,'independent exact priced-tail dual'
   if val==a:
    active=[eq]+[row for row,z in zip(A,y) if z<0]+[[F(int(i==j)) for i in range(2*n)] for j,z in enumerate(slack) if z>0];rk=rank(active)
    fixed &= all(rank(active+[[F(int(i==j)) for i in range(2*n)]])==rk for j in range(n))
    pop=[(e,str(p)) for e,p in zip(s,x) if p]
    if pop not in populations:populations.append(pop)
    tail_positive |= bool(r['tail'] and x[n-1]);count+=1
   count+=4
  face=bank.get('expected_face',v['equality_faces'][idx]);assert fixed==face['all_equality_populations_fixed'] and tail_positive==face['positive_equality_tail'],'equality face'
  assert sorted(populations)==sorted([list(map(tuple,p)) for p in face['equality_populations']]),'equality support/population';count+=2
 for k,bank in enumerate(v['global_duals'][:2]):
  levels=bank['right']['support'];ps=[list(map(F,bank['left']['weights']))+[F(0)],list(map(F,bank['right']['weights']))];edges=[];deficits=[]
  bath=[F(1,2)**i/sum(F(1,2)**j for j in range(4)) for i in range(4)]
  for p in ps:
   inc=[F(0)]*len(p);edge=[]
   for i in range(len(p)-1):
    d=levels[i+1]-levels[i];vflow=sum(bath[d:])*p[i]-sum(bath[:4-d])*p[i+1];edge.append(vflow);inc[i]+=max(F(0),-vflow);inc[i+1]+=max(F(0),vflow)
   edges.append(edge);deficits.append([p0-in0 for p0,in0 in zip(p,inc)])
  assert all(x*y>=0 for x,y in zip(*edges)) and all(x*y>=0 for x,y in zip(*deficits)),'whole interval affine sign-cell proof'
  cert=v['interval_cells'][k];assert edges==[list(map(F,r)) for r in cert['edge_sign_values']] and deficits==[list(map(F,r)) for r in cert['deficit_sign_values']],'interval coefficients'
  for p in ps:assert shell_return(F(1,2),levels,p)==F(bank['intercept'])-F(bank['slope'])*dot(levels,p),'interval endpoint equality'
  count+=4
 for rec in v.get('consumers',[]):
  s=list(map(F,rec['support']));p=list(map(F,rec['weights']));E=F(rec['energy']);r=F(rec['return_cost']);assert sum(p)==1 and dot(s,p)==E and shell_return(F(1,2),s,p)==r,'physical bath-label consumer';count+=3
  if rec['kind']=='rejected_secant_counterexample':
   candidate=F(31271,107400)-F(1943,107400)*E
   assert F(54787,14671)<E<F(4781,923) and r<candidate and candidate-r==F(rec['gap']),'independent physical counterexample'
   count+=1
 return count

def tail_controls():
 count=0
 for t in [F(1,4),F(1,2),F(3,4)]:
  bath=[t**j/sum(t**k for k in range(4)) for j in range(4)];floor=t*t/(1+t*t)**2
  for S in [[1,3,5,7,9],[2,3,6,7,10],[1,4,5,8,9]]:
   for ws in [[1,2,3,4,5],[100,1,1,1,100],[1,100,1,100,1]]:
    p=[F(w,sum(ws)) for w in ws];whole=shell_return(t,S,p)
    for cut in range(1,len(S)):
     ss=S[:cut+1];pp=p[:cut]+[sum(p[cut:])];inc=[F(0)]*len(ss)
     for i in range(len(ss)-1):
      d=ss[i+1]-ss[i];lo=sum(bath[:4-d]);hi=sum(bath[d:]);v=hi*pp[i]-lo*pp[i+1];inc[i]+=max(F(0),-v);inc[i+1]+=max(F(0),v)
     low=sum(max(F(0),w-z) for w,z in zip(pp[:-1],inc[:-1]))/2
     penalty=max(F(0),floor*pp[-1]-sum(bath[ss[-1]-ss[-2]:])*pp[-2]/2)
     assert low+penalty<=whole,'priced collapsed-tail inequality';count+=1
 return count
if __name__=='__main__':
 v=json.loads(OUT.read_text());print('PASS K1954 independent',audit(v)+tail_controls(),'exact controls',flush=True)
 for kind in ['missing_crossing','dual','population','tail_price']:
  w=deepcopy(v);bank=w['global_duals'][0];r=next(r for r in bank['cells'] if r['tail'])
  if kind=='missing_crossing':bank['cells'].remove(r)
  elif kind=='dual':r['intercept']=str(F(r['intercept'])+1)
  elif kind=='population':r['x'][0]=str(F(r['x'][0])+F(1,100))
  try:audit(w,True,fault=kind)
  except AssertionError as e:print('PASS mathematical fault',kind,str(e),flush=True)
  else:raise AssertionError('undetected mathematical fault')
 for kind in ['identity','pin']:
  w=deepcopy(v)
  if kind=='identity':w['result_id']='WRONG'
  else:w['inputs'][next(iter(w['inputs']))]='0'*64
  try:audit(w)
  except AssertionError as e:print('PASS reporting fault',kind,str(e),flush=True)
  else:raise AssertionError('undetected reporting fault')
