"""Independent bath-shell witness and exhaustive finite-family lower replay."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from copy import deepcopy
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
def deficits(s,p):
 b=[F(8,15),F(4,15),F(2,15),F(1,15)]
 return [v-sum(max(w*b[k] for y,w in zip(s,p) for k in range(4) if y+k==x+j)/2 for j in range(4)) for x,v in zip(s,p)]
def physical(w,d,E,value):
 a=list(map(F,w['spectrum']));s=list(map(F,w['support']));p=list(map(F,w['population']));active=[x for x,y in zip(s,p) if y]
 assert a==sorted(set(a)) and a[0]==0 and min(y-x for x,y in zip(a,a[1:]))>=d
 assert sum(p)==1 and min(p)>=0 and sum(x*y for x,y in zip(s,p))==F(w['mean'])<=E
 for z in {x+j for x in active for j in range(4)}:
  assert sum(z-x in (0,1,2,3) for x in a)>=2*sum(z-x in (0,1,2,3) for x in active)
 assert sum(max(x,0) for x in deficits(s,p))==F(w['return_value'])==value

def main():
 z=json.loads((ROOT/'lab/process/k2025-wide-spacing-ladder-program.json').read_text());c=json.loads((ROOT/'lab/process/k2015-finite-thermal-ray-separation.json').read_text())['census'];rays=set();segments=set();checked=0
 for cell in c['cells']:
  s=cell['support'];N=s[-1]+2+int(len(s)>1 and s[-1]-s[-2]==1);vv=cell['vertices'];ds=[]
  for v in vv:
   p=list(map(F,v['p']));d=deficits(s,p);e=sum(x*y for x,y in zip(s,p));r=sum(max(x,0) for x in d)
   assert e==F(v['energy']) and r==F(v['return']);rays.add((e,r,N));ds.append(d);checked+=1
  for i,j in combinations(range(len(vv)),2):
   if any(x*y<0 for x,y in zip(ds[i],ds[j])):continue
   a,b=vv[i],vv[j];e,r,f,t=map(F,[a['energy'],a['return'],b['energy'],b['return']])
   if e>f:e,f,r,t=f,e,t,r
   if e<f and e<F(11,5) and f>F(6,5):segments.add((e,r,f,t))
 assert len(rays)==z['rays'] and len(segments)==z['segments']
 obligations=0
 for row in z['rows']:
  d,E,v=map(F,[row['delta'],row['energy'],row['value']]);physical(row['witness'],d,E,v)
  for e,r,N in rays:
   if e<=E:assert r>=v;obligations+=1
  for e,r,f,t in segments:
   if e<=E<=f:assert (f-E)*r+(E-e)*t>=v*(f-e);obligations+=1
  for e,r,N in rays:
   if e>E:continue
   for f,t,M in rays:
    f=f+N-1+d
    if f>=E and (r<v or t<v):assert (f-E)*r+(E-e)*t>=v*(f-e);obligations+=1
  print('certified finite family',str(d),str(E),flush=True)
 rect=z['rectangle_certificate'];aa,bb=map(F,[rect['intercept'],rect['slope']]);lo,hi=F(7,5),F(8,5);corners=0
 assert any(e<=lo and f>=hi and (t-r)/(f-e)==bb and r-bb*e==aa for e,r,f,t in segments)
 def test(gap):
  nonlocal corners
  assert gap>=0;corners+=1
 for e,r,N in rays:
  if e<=hi:test(r-aa-bb*max(e,lo))
 for e,r,f,t in segments:
  a,b=max(e,lo),min(f,hi)
  if a<=b:
   for E in (a,b):test((f-E)*r+(E-e)*t-(aa+bb*E)*(f-e))
 for e,r,N in rays:
  if e>hi:continue
  for f,t,M in rays:
   assert f+N-F(1,2)>hi
   for d in (F(1,2),F(1)):
    for E in (max(e,lo),hi):test((f+N-1+d-E)*r+(E-e)*t-(aa+bb*E)*(f+N-1+d-e))
 assert corners==rect['corner_inequalities']
 for w in z['larger_witnesses']:
  physical(w,F(1),F(w['energy']),F(w['return_value']))
  for comparison in w['comparisons']:
   old=next(r for r in z['rows'] if r['delta']==comparison['delta'] and r['energy']==w['energy'])
   assert F(old['value'])-F(w['return_value'])==F(comparison['strict_improvement'])>0
 for branch in z['larger_affine_branches']:
  ends=[next(w for w in z['larger_witnesses'] if len(w['spectrum'])==branch['levels'] and w['energy']==E) for E in ('7/5','8/5')]
  S=list(map(F,ends[0]['support']));ps=[list(map(F,w['population'])) for w in ends]
  # One bath-label maximizer works at both endpoints in every shell.
  bath=[F(8,15),F(4,15),F(2,15),F(1,15)]
  for shell in {x+j for x in S for j in range(4)}:
   candidates=[(i,j) for i,x in enumerate(S) for j in range(4) if x+j==shell]
   winners=[]
   for p in ps:
    mx=max(p[i]*bath[j] for i,j in candidates);winners.append({(i,j) for i,j in candidates if p[i]*bath[j]==mx})
   assert winners[0]&winners[1]
  dd=[deficits(S,p) for p in ps];assert all(x*y>=0 for x,y in zip(*dd))
  a,b=map(F,[branch['intercept'],branch['slope']]);gaps=[]
  for E,w in zip((lo,hi),ends):
   assert a+b*E==F(w['return_value']);gaps.append(aa+bb*E-a-b*E)
  assert min(gaps)==F(branch['minimum_improvement'])>0

 tail=z['geometric_tail_family'];assert tail['unique_minimizing_m']==3 and tail['minimizing_levels']==17
 for w in tail['finite_controls']:
  E=F(w['energy']);physical(w,F(1),E,F(w['return_value']))
  m=w['m'];q=F(1,9**(m+1));closed=(64875-4044*E+1215*q*(4*E-8*m-45))/(134375-27*q*(808*m+4045))
  assert closed==F(w['return_value'])
  if m==3:assert closed==F(tail['minimum_intercept'])+F(tail['minimum_slope'])*E
 for E in (lo,hi):
  A=64875-4044*E;B=1215*(4*E-45);C=-9720;D=134375;c=21816;d=109215
  alpha=A*c+D*C;beta=A*d+D*B;h=c*B-C*d
  assert alpha<0 and h>0 and -8*beta-23*alpha>0
  for m in range(3):assert -8*beta+alpha*(1-8*m)+F(1,9**(m+1))*h<0
  # Independent cross-multiplication at 32 rational members checks formula;
  # the signs above, affine in E, prove all m>=3 without finite sampling.
  for m in range(32):
   q=F(1,9**(m+1));r=(A+q*(B+C*m))/(D-q*(d+c*m));ss=(A+q/9*(B+C*(m+1)))/(D-q/9*(d+c*(m+1)))
   diff=q/F(9)*(-8*beta+alpha*(1-8*m)+q*h)/((D-q*(d+c*m))*(D-q/9*(d+c*(m+1))))
   assert ss-r==diff and ((diff<0)==(m<3))
  assert F(tail['minimum_intercept'])+F(tail['minimum_slope'])*E<A/D
 print('PASS geometric-tail universal step-sign certificate; finite17 is family minimum, below countable limit',flush=True)
 print('PASS full rectangle',corners,'corner inequalities; eight larger physical witnesses and two affine families',flush=True)
 base=next(x for x in z['rows'] if x['ref'][0]=='separated');d,E,v=map(F,[base['delta'],base['energy'],base['value']]);faults=[]
 for name in ['completion','normalization','spacing','return']:
  w=deepcopy(base['witness']);dd=d
  if name=='completion':w['spectrum']=sorted(set(w['support']),key=F)
  elif name=='normalization':w['population'][0]=str(F(w['population'][0])+F(1,100))
  elif name=='spacing':dd=F(1)
  else:w['return_value']=str(v-F(1,100))
  try:physical(w,dd,E,v)
  except AssertionError:faults.append(name)
  else:raise AssertionError('accepted '+name)
 for p,h in z['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 print('PASS K2025',checked,'bath-shell vertices',obligations,'exact candidate inequalities',len(z['rows']),'physical witnesses',len(faults),'actual faults;',len(z['inputs']),'provenance hashes',flush=True)
if __name__=='__main__':main()
