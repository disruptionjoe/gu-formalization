"""Exact parametric thermal strip, physical-component transfer and equality.

Inherited low-energy and all-energy banks are reused by exact digest. Every
new strip and placement certificate is replayed without an optimizer.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import json,zlib,base64,hashlib,argparse
import k2027_thermal_pattern_frontier as c
import k2029_multicomponent_thermal_placement as p
import k2031_thermal_phase_boundaries as old
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2033-thermal-transition-completion.json'
def unpack(r):
 raw=zlib.decompress(base64.b64decode(r['payload']));assert hashlib.sha256(raw).hexdigest()==r['payload_sha256'];return json.loads(raw)
def parameters(r):return tuple(map(Q,[r[k] for k in ['intercept','slope','backward_slope','lower','upper']]))
def check(r):
 A,C,B,lo,hi=parameters(r);c.A,c.C,c.B,c.LO,c.HI=A,C,B,lo,hi;p.A,p.C,p.B,p.lo,p.hi=A,C,B,lo,hi
 for f,h in r['inputs'].items():assert hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h
 d=unpack(r);expected=iter((ss,o) for ss in c.supports(21) if min(ss)<=hi for o in product((-1,1),repeat=len(ss)-1));n=0;contacts=[]
 for row in d['connected']:
  ss,o=next(expected);assert row['s']==list(ss) and row['o']==list(o);cc=row['certificate'];assert cc['kind']=='strip'
  if 'infeasible_energy' in cc:assert c.dual(ss,o,cc['infeasible_energy'])>hi
  elif 'infeasible_maxenergy' in cc:assert -c.dual(ss,o,cc['infeasible_maxenergy'])<lo
  else:
   value=c.dual(ss,o,cc);assert value==Q(cc['value'])>=A
   if value==A:contacts.append(row)
  n+=1
 assert next(expected,None) is None and n==r['connected_cells']
 # Two previously proved all-energy banks, now composed with a new interval.
 bankB=old.global_unpack(json.loads(old.OUT.read_text())['certified_interval'])['components']['banks'][0]
 bankC=p.unpack(json.loads(p.OUT.read_text()))['banks'][1];banks=[bankB,bankC];pen=[];nb=0
 for bank in banks:
  lam,alpha=Q(bank['slope']),Q(bank['intercept']);ex=iter((ss,o) for ss in c.supports(14) for o in product((-1,1),repeat=len(ss)-1))
  for row in bank['rows']:
   ss,o=next(ex);assert row['s']==list(ss) and row['o']==list(o);nn=len(ss)
   assert p.verify([lam*x for x in ss]+[Q(1)]*nn,p.cell(ss,o),[Q(0)]*(2*nn-1),[Q(1)]*nn+[Q(0)]*nn,row['cert'])>=alpha;nb+=1
  assert next(ex,None) is None and 15*lam>alpha;pen.append((lam,alpha))
 assert [x[0] for x in pen]==[B,C];pen +=[(Q(1,4),Q(3,4)),(Q(3,20),Q(63,100))]
 ex=iter((ss,o) for ss in c.supports(7) if ss[0]==1 and (1 if len(ss)==1 else ss[-2]+3)<8 for o in product((-1,1),repeat=len(ss)-1));margins=[]
 for row in d['short']:
  ss,o=next(ex);assert row['s']==list(ss) and row['o']==list(o);co,aa,bb,eq,off=p.shortprogram(ss,o,pen);assert off==Q(row['offset'])
  if 'infeasible_energy' in row:
   nn=len(ss);k=2*nn-1;en=list(map(Q,ss))+[Q(0)]*nn+[Q(0),Q(1),Q(0)];assert p.verify(en,aa[:k]+aa[k+2:],bb[:k]+bb[k+2:],eq,row['infeasible_energy'])>hi
  else:
   margin=p.verify(co,aa,bb,eq,row['cert'])-A;assert margin>=0;margins.append(margin)
   if margin==0:
    yy=list(map(Q,row['cert']['y']));zz=Q(row['cert']['z']);nn=len(ss)
    reduced=[v-zz*e-sum(ar[j]*y for ar,y in zip(aa,yy)) for j,(v,e) in enumerate(zip(co,eq))]
    assert yy[2*nn-1]<0 and reduced[2*nn+1]>0 and off+1>0
    # Equality forces upper endpoint, aggregate h=0 and hence q=0.

 assert next(ex,None) is None and min(margins)>=0
 assert pen[0][1]+8*B-(A-C*lo+B*lo)>0 and pen[1][1]+8*C-A>0
 assert min((22-e)*B-(A-C*e) for e in (lo,hi))==Q(r['tail_mass_coefficient'])>0
 assert min(Q(101,100)-Q(17,50)*e-(A-C*e) for e in (Q(3,2),hi))>0
 # The inherited backward line follows from K2031 on[13/10,lo].
 A21,C21=Q(15398019,32499160),Q(761157,32499160)
 assert A21-C21*lo==A-C*lo and C21>B and lo>=Q(13,10)
 from k2031_thermal_phase_boundaries_probe import physical
 for w in r['witnesses']:assert physical(w)==A-C*Q(w['energy'])
 for side in ['left','right']:
  for v in r['equality'][side]['vertices']:
   ss=[x[0] for x in v];pp=list(map(Q,[x[1] for x in v]));E=lo if side=='left' else hi
   spec=list(range(1+max(ss)+1));w=dict(support=ss,population=list(map(str,pp)),spectrum=spec,energy=str(E),return_value=str(A-C*E));assert physical(w)==A-C*E
 # Actual previously proposed13-family phase edge is refuted by physical5 levels.
 w=r['failed_extrapolation'];assert physical(w)<A-C*Q(w['energy'])
 return dict(connected=n,component=nb,short=len(d['short']),strict_short=sum(x>0 for x in margins),endpoint_short=sum(x==0 for x in margins),contacts=len(contacts),provenance=len(r['inputs']))
if __name__=='__main__':print('PASS K2033',check(json.loads(OUT.read_text())),flush=True)
