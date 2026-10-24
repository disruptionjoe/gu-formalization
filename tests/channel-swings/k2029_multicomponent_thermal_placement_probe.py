"""Independent bath-shell reconstruction of all duals and placement controls."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from copy import deepcopy
import json,zlib,base64,hashlib
from k2027_thermal_pattern_frontier_probe import reconstruct,physical
ROOT=Path(__file__).resolve().parents[2];A=F(985095,2040416);C=F(61407,2040416);B=F(1,41);lo,hi=F(7,5),F(8,5)
def words(limit):
 yield (1,)
 def visit(xs,old):
  yield tuple(xs)
  for gap in (1,2,3):
   if old+gap>=4 and xs[-1]+gap<=limit:yield from visit(xs+[xs[-1]+gap],gap)
 for gap in (1,2,3):
  x=max(1,3-gap)
  if x+gap<=limit:yield from visit([x,x+gap],gap)
def raw(s,o):
 rows,_,_=reconstruct(s,o,'energy');return rows

def dual(cost,rows,rhs,eq,cert):
 y=list(map(F,cert['y']));z=F(cert['z']);assert len(y)==len(rows) and all(v<=0 for v in y)
 for j,c in enumerate(cost):assert sum(a[j]*v for a,v in zip(rows,y))+z*eq[j]<=c
 value=z+sum(v*b for v,b in zip(y,rhs));assert value==F(cert['value']);return value

def run():
 r=json.loads((ROOT/'lab/process/k2029-multicomponent-thermal-placement.json').read_text());data=zlib.decompress(base64.b85decode(r['payload']));assert hashlib.sha256(data).hexdigest()==r['payload_sha256'];d=json.loads(data);count=0;pen=[];faultfixture=None
 for bank in d['banks']:
  slope,intercept=F(bank['slope']),F(bank['intercept']);expected=iter((s,o) for s in words(14) for o in product((-1,1),repeat=len(s)-1))
  for row in bank['rows']:
   s,o=next(expected);assert row['s']==list(s) and row['o']==list(o);n=len(s);rows=raw(s,o);cost=[slope*x for x in s]+[F(1)]*n;rhs=[F(0)]*len(rows);eq=[F(1)]*n+[F(0)]*n
   assert dual(cost,rows,rhs,eq,row['cert'])>=intercept;count+=1;faultfixture=(cost,rows,rhs,eq,row['cert'])
  assert next(expected,None) is None and 15*slope>intercept;pen.append((slope,intercept))
 pen.extend([(F(1,4),F(3,4)),(F(3,20),F(63,100))]);short=[]
 for s in words(6):
  if s[0]!=1:continue
  L=1 if len(s)==1 else s[-2]+3
  if L>=7:continue
  for o in product((-1,1),repeat=len(s)-1):short.append((s,o,L))
 assert len(short)==len(d['short'])==13
 for row,(s,o,L) in zip(d['short'],short):
  assert row['s']==list(s) and row['o']==list(o);n=len(s);offset=min(F(L)+F(1,2),F(s[-1]+2));rows=[x+[F(0)]*3 for x in raw(s,o)];rhs=[F(0)]*len(rows)
  energy=list(map(F,s))+[F(0)]*n+[F(0),F(1),F(0)];rows.extend([energy,[-x for x in energy],[F(0)]*(2*n)+[offset+1,-F(1),F(0)]]);rhs.extend([hi,-lo,F(0)])
  for b,a in pen:rows.append([F(0)]*(2*n)+[a+b*offset,-b,-F(1)]);rhs.append(F(0))
  cost=[C*x for x in s]+[F(1)]*n+[F(0),C,F(1)];eq=[F(1)]*n+[F(0)]*n+[F(1),F(0),F(0)]
  assert dual(cost,rows,rhs,eq,row['cert'])>A
 # Every gap word forces its interval from actual four-input shell capacity.
 patterns=0
 for s in words(20):
  if s[0]!=1:continue
  forced={0,1};L=1 if len(s)==1 else s[-2]+3
  for z in {x+b for x in s for b in range(4)}:
   inputs=sum(z-x in (0,1,2,3) for x in s)
   assert inputs<=2
   if inputs==2:forced.update(z-b for b in range(4))
  assert set(range(L+1))<=forced;patterns+=1
  # Any distinct fractional residue inside [0,L] is within1/2 of a forced integer.
  for numerator in range(1,20):
   x=F(numerator,20)
   for j in range(L):assert min(abs(j+x-k) for k in forced)<=F(1,2)
  if len(s)>1:assert s[-1]+2>=L
 assert F(r['long_back_margin'])>0 and F(r['long_main_margin'])>0
 assert min(F(101,100)-F(17,50)*e-(A-C*e) for e in (F(3,2),hi))==F(r['no_first_one_margin'])>0
 # Hostile boundary: actual interlaced components at delta=1/2 defeat F.
 boundary=[]
 for E in (lo,F(3,2),hi):
  w=(E-F(6,5))/F(3,2);s=[F(1),F(3,2),F(3),F(7,2)];p=[(1-w)*F(9,10),w*F(2,5),(1-w)*F(1,10),w*F(3,5)];spec=[F(j,2) for j in range(10)];ret=F(57,100)-E/10
  assert sum(p)==1 and sum(x*y for x,y in zip(s,p))==E
  bath=[F(8,15),F(4,15),F(2,15),F(1,15)]
  for z in {x+b for x in s for b in range(4)}:assert sum(z-x in (0,1,2,3) for x in spec)>=2*sum(z-x in (0,1,2,3) for x in s)
  rr=sum(max(p[i]-sum(max(p[j]*bath[k] for j,x in enumerate(s) for k in range(4) if x+k==y+b)/2 for b in range(4)),0) for i,y in enumerate(s))
  assert rr==ret<A-C*E;boundary.append(str(A-C*E-ret))
 # Actual optimal shells and minimum dimension are inherited with unchanged hash.
 for w in r['witnesses']:assert physical(w)[0]==A-C*F(w['energy'])
 forced=set();s=r['witnesses'][0]['support']
 for z in {x+b for x in s for b in range(4)}:
  if sum(z-x in (0,1,2,3) for x in s)==2:forced.update(z-b for b in range(4))
 assert forced==set(range(17))
 faults=[];cost,rows,rhs,eq,c=faultfixture
 for kind in ('multiplier','normalization'):
  cc=deepcopy(c)
  if kind=='multiplier':cc['y'][0]='1'
  else:cc['z']=str(F(cc['z'])+1)
  try:dual(cost,rows,rhs,eq,cc)
  except AssertionError:faults.append(kind)
  else:raise AssertionError('accepted actual dual fault')
 for kind in ('completion','return','population'):
  w=deepcopy(r['witnesses'][0])
  if kind=='completion':w['spectrum'].remove(8)
  elif kind=='return':w['return_value']=str(F(w['return_value'])-F(1,100))
  else:w['population'][0]=str(F(w['population'][0])+F(1,100))
  try:physical(w)
  except AssertionError:faults.append(kind)
  else:raise AssertionError('accepted physical fault')
 for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 print('PASS K2029 separate shell replay',count,'global+13 short duals;',patterns,'forced-prefix controls;3 actual half-spacing counterexamples;17 mandatory levels;',len(faults),'actual faults;',len(r['inputs']),'provenance hashes; jump lower controls',boundary,flush=True)
if __name__=='__main__':run()
