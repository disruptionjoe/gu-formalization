"""Exact incoming-aware first-terminal certificate; candidate search is not optimality."""
from pathlib import Path
import importlib.util,json
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('base',ROOT/'tests/channel-swings/k2059_energy_aware_thermal_tail.py');b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
Lh={1:(F(14,15),F(7,15)),2:(F(4,5),F(1,5)),3:(F(8,15),F(1,15))}
bank=json.loads((ROOT/b.REF).read_text())['bank'];old=json.loads((ROOT/'lab/process/k2059-energy-aware-thermal-tail.json').read_text())
def incoming(s,v):
 p=F(v['p'][-1])
 if len(s)==1:return p
 L,H=Lh[s[-1]-s[-2]];return max(F(0),p-max(F(0),H*F(v['p'][-2])-L*p))
def envelope(g,p,A,d):
 L,H=Lh[d];return max(g*b.K[d]*p,(g-F(1,2))*H*p/L+(F(1,2)+(g-F(1,2))/L)*A)
def constraints(ci=188,seed=None):
 s=bank[ci]['s'];ell=b.shift(s);seed=seed or [F(old['assignments'][ci]['a']),-F(old['assignments'][ci]['s'])];a0,t0=map(F,seed);pol=b.policy(a0,t0,64);hp=b.policy(a0-t0*ell,t0,64)
 first={(s[-1]+d,d) for d in b.allowed(s)};deep=b.reachable(s,64)-first
 cons=[]
 def add(A,B,C,tag):cons.append((F(A),F(B),F(C),tag)) # A*a-B*t<=C
 add(1,65,0,'cutoff')
 for n,d in sorted(first):A,B=pol[n,d];add(A,B,F(1,2),('firstcap',n,d))
 for n,d in sorted(deep):A,B=pol[n,d];add(A,B,b.C[d],('deepcap',n,d))
 for (n,d),(A,B) in hp.items():add(A,B+ell*A,b.C[d],('highcap',n,d))
 for n in range(12,65):
  for d in b.K:
   A,B=hp.get((n+d,d),(0,0));add(1+b.K[d]*A,n+ell+b.K[d]*(B+ell*A),F(1,2),('root',n,d))
 for j,v in enumerate(bank[ci]['vertices']):
  p=F(v['p'][-1]);aa=incoming(s,v);e=F(v['energy']);r=F(v['value'])
  add(1,e,r,('low',j,None,'zero'))
  for d in b.allowed(s):
   A,B=pol[s[-1]+d,d];L,H=Lh[d];q=(H*p+aa)/L
   add(1+b.K[d]*p*A,e+b.K[d]*p*B,r,('low',j,d,0))
   add(1+q*A,e+q*B,r-aa/2+q/2,('low',j,d,1))
 for ii,c in enumerate(bank):
  for j,v in enumerate(c['vertices']):
   p=F(v['p'][-1]);e=F(v['energy']);r=F(v['value'])
   choices=b.allowed(c['s']) or [None]
   for d in choices:
    A,B=(0,0) if d is None else hp.get((c['s'][-1]+d,d),(0,0));k=0 if d is None else b.K[d]
    add(1+p*k*A,e+ell+p*k*(B+ell*A),r,('high',ii,j,d))
 return cons

def optimize(cons,E=F(5,2)):
 # Exact lower envelope of affine upper bounds on a. Active slopes decrease
 # with t. Every generated constraint has nonnegative coefficient of a.
 by_slope={};low=F(0);high=F(1) # explicit candidate search box, not a dual-optimality claim
 for A,B,C,tag in cons:
  if A==0:
   if B>0:low=max(low,-C/B)
   elif B<0:
    val=-C/B;high=val if high is None else min(high,val)
   elif C<0:raise ValueError(('infeasible constant',tag))
   continue
  assert A>0
  slope=B/A;intercept=C/A
  if slope not in by_slope or intercept<by_slope[slope][0]:by_slope[slope]=(intercept,tag)
 hull=[]
 for slope,(intercept,tag) in sorted(by_slope.items(),reverse=True):
  start=None
  while hull:
   ps,pi,pt,pstart=hull[-1]
   start=(intercept-pi)/(ps-slope)
   if pstart is None or start>pstart:break
   hull.pop()
  if not hull:start=None
  hull.append((slope,intercept,tag,start))
 assert high is None or low<=high
 candidates={low}
 if high is not None:candidates.add(high)
 candidates.update(start for _,_,_,start in hull if start is not None and start>=low and (high is None or start<=high))
 # Evaluate only hull lines, then independently check all original constraints.
 best=None
 for t in candidates:
  a,tag=min(((intercept+slope*t,tag) for slope,intercept,tag,_ in hull),key=lambda pair:pair[0])
  rec=(a-E*t,a,t,tag)
  if best is None or rec[:3]>best[:3]:best=rec
 _,a,t,tag=best
 assert all(A*a-B*t<=C for A,B,C,_ in cons)
 if high is None:assert hull[-1][0]<=E, 'unbounded objective at infinity'
 return a,t,tag,len(hull)

def run(ci=188,vi=57,seed=None,max_iterations=40):
 # Each Bellman policy supplies globally valid affine lower pieces of G.
 # Keep old cuts; actual-policy separation closes their finite max envelope.
 seed=seed or [F(old['assignments'][ci]['a']),-F(old['assignments'][ci]['s'])]
 allcuts={};history=[]
 for step in range(max_iterations):
  current=constraints(ci,seed)
  for A,B,C,tag in current:allcuts[(A,B,C)]=tag
  con=[(*key,tag) for key,tag in allcuts.items()]
  a,t,tag,nhull=optimize(con)
  assert t>0
  actual=constraints(ci,[a,t])
  bad=[(C-A*a+B*t,tag) for A,B,C,tag in actual if A*a-B*t>C]
  history.append(dict(iteration=step,a=str(a),t=str(t),value=str(a-F(5,2)*t),decimal=float(a-F(5,2)*t),cut_count=len(con),hull_count=nhull,violations=len(bad),worst=None if not bad else [str(min(bad,key=lambda pair:pair[0])[0]),min(bad,key=lambda pair:pair[0])[1]]))
  if not bad:
   # This recomputed true policy covers every local/high vertex, deep/first
   # cap, wholly erased root and cutoff, so it is the exact final verifier.
   assert all(A*a-B*t<=C for A,B,C,_ in actual)
   return dict(cell=ci,a=str(a),s=str(-t),value=str(a-F(5,2)*t),decimal=float(a-F(5,2)*t),active_tag=tag,constraint_count=len(con),history=history)
  seed=[a,t]
 return dict(failure='policy-cut iteration limit; not certified',cell=ci,a=str(a),t=str(t),history=history)

PINS={'tests/channel-swings/k2059_energy_aware_thermal_tail.py': 'd66117b5a168586aaf5abb5be4a37e22c573b5798959d1e7118afec2f0502143', 'lab/process/k2059-energy-aware-thermal-tail.json': '4aaa708aa2835f50c397b2c1ac7669b71d092706d8da387f322301f70948112e', 'lab/process/k2045-third-thermal-spacing-phase.json': '6641419ca109d3cbbcd21014913ed22a710f9b1c2249974ba0bb593b9591a637'}

def produce():
 for p,h in PINS.items():assert __import__('hashlib').sha256((ROOT/p).read_bytes()).hexdigest()==h
 replacements={}
 for ci in [152,187,188,212,235]:
  result=run(ci);assert 'failure' not in result,result;replacements[str(ci)]=result
 assignments=list(old['assignments'])
 for ci,v in replacements.items():assignments[int(ci)]=v
 E=F(5,2);lower,ci=min((F(v['a'])+E*F(v['s']),i) for i,v in enumerate(assignments));a,t=F(assignments[ci]['a']),F(assignments[ci]['s'])
 left,right=map(F,old['interval'])
 for v in assignments:
  da,ds=F(v['a'])-a,F(v['s'])-t
  if ds>0:left=max(left,-da/ds)
  elif ds<0:right=min(right,-da/ds)
  else:assert da>=0
 assert left<E<right and F(old['lower'])<lower<F(old['upper'])
 return dict(id='K2066',scope='conditional finite/countable four-state thermal model; no GU verdict or exact optimality',inputs=PINS,base_ref='lab/process/k2059-energy-aware-thermal-tail.json',replacements=replacements,lower=str(lower),upper=old['upper'],width=str(F(old['upper'])-lower),gain=str(lower-F(old['lower'])),bottleneck=ci,lower_line=[str(a),str(t)],interval=[str(left),str(right)],price_search_box=['0','1'],inherited_scope='671 complete subcells/20975 raw vertices, physical packing and upper construction reused by pinned K2059; five new low assignments fully rechecked against all high vertices')
if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');args=p.parse_args();data=produce();dest=ROOT/'lab/process/k2066-thermal-terminal-response.json'
 if args.write:dest.write_text(json.dumps(data,indent=2)+'\n')
 else:assert json.loads(dest.read_text())==data
 print('PASS five complete assignments; lower',data['lower'],'=',float(F(data['lower'])),'bottleneck',data['bottleneck'])
