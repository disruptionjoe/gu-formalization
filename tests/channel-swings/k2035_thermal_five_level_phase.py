"""Optimizer-free rational certificate replay of the unrestricted five-level phase."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import json,zlib,base64,hashlib
import k2027_thermal_pattern_frontier as c
import k2029_multicomponent_thermal_placement as p
import k2031_thermal_phase_boundaries as older
import k2033_thermal_transition_completion as old
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2035-thermal-five-level-phase.json'
def unpack(r):
 raw=zlib.decompress(base64.b64decode(r['payload']));assert hashlib.sha256(raw).hexdigest()==r['payload_sha256'];return json.loads(raw)
def check(r):
 A,C,B,lo,hi=map(Q,[r[k] for k in ['intercept','slope','backward_slope','lower','certificate_upper']]);end=Q(r['phase_upper'])
 assert (A,C,B,hi,end)==(Q(17,20),Q(1,4),Q(43,2000),Q(17,5),Q(11,5))
 c.A,c.C,c.B,c.LO,c.HI=A,C,B,lo,hi;p.A,p.C,p.B,p.lo,p.hi=A,C,B,lo,end
 for f,h in r['inputs'].items():assert hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h
 d=unpack(r);expected=iter((ss,o) for ss in c.supports(21) if min(ss)<=hi for o in product((-1,1),repeat=len(ss)-1));n=0;contacts=0
 for row in d['connected']:
  ss,o=next(expected);assert row['s']==list(ss) and row['o']==list(o);cc=row['certificate']
  if 'infeasible_energy' in cc:assert c.dual(ss,o,cc['infeasible_energy'])>hi
  elif 'infeasible_maxenergy' in cc:assert -c.dual(ss,o,cc['infeasible_maxenergy'])<lo
  else:
   value=c.dual(ss,o,cc);assert value==Q(cc['value'])>=A;contacts+=value==A
  n+=1
  if n%50000==0:print('primary strip',n,flush=True)
 assert next(expected,None) is None and n==r['connected_cells']
 # Unchanged banks and their all-size transfer were certified by K2033; reuse by digest.
 bankB=older.global_unpack(json.loads(older.OUT.read_text())['certified_interval'])['components']['banks'][0]
 bankC=p.unpack(json.loads(p.OUT.read_text()))['banks'][1]
 pen=[(Q(x['slope']),Q(x['intercept'])) for x in [bankB,bankC]]+[(Q(1,4),Q(3,4)),(Q(3,20),Q(63,100))]
 assert [[str(a),str(b)] for a,b in pen[:2]]==r['component_lines']
 A17,C17=Q(985095,2040416),Q(61407,2040416)
 assert A17-C17*lo==A-C*lo and C17>B and hi*C==A
 assert pen[0][1]+8*B-(A-C*lo+B*lo)>0 and Q(3,4)+8*C>A
 assert min((22-e)*B-(A-C*e) for e in [lo,hi])==Q(r['tail_mass_coefficient'])>0
 # No first occupied1: first mean>=2 gets new all-high-energy bound;
 # later components have offset>1/2 and the old R+e/4>=3/4 gives gap1/40.
 assert lo<2 and Q(3,4)+C/2-A==Q(1,40)>0
 ex=iter((ss,o) for ss in c.supports(7) if ss[0]==1 and (1 if len(ss)==1 else ss[-2]+3)<8 for o in product((-1,1),repeat=len(ss)-1));margins=[];qgaps=[]
 for row in d['short']:
  ss,o=next(ex);assert row['s']==list(ss) and row['o']==list(o);co,aa,bb,eq,off=p.shortprogram(ss,o,pen);assert off==Q(row['offset'])
  value=p.verify(co,aa,bb,eq,row['cert']);assert value>=A;margins.append(value-A)
  if value==A:
   y=list(map(Q,row['cert']['y']));z=Q(row['cert']['z']);nn=len(ss);red=[v-z*e-sum(ar[j]*yy for ar,yy in zip(aa,y)) for j,(v,e) in enumerate(zip(co,eq))]
   gap=red[2*nn]+(off+1)*red[2*nn+1];assert gap>0;qgaps.append(gap)
 assert next(ex,None) is None
 from k2031_thermal_phase_boundaries_probe import physical
 for w in r['witnesses']:assert physical(w)==A-C*Q(w['energy'])
 for w in r['successor_witnesses']:assert physical(w)==Q(3,28)*(5-Q(w['energy']))<Q(3,10)
 return dict(connected=n,contacts=contacts,short=len(margins),strict_short=sum(x>0 for x in margins),zero_short=len(qgaps),outside_population_gap=str(min(qgaps)),physical_witnesses=len(r['witnesses']),successors=len(r['successor_witnesses']),reused_component_banks=2,provenance=len(r['inputs']))
if __name__=='__main__':print('PASS K2035',check(json.loads(OUT.read_text())),flush=True)
