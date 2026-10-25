"""Separate bath-label certificate, equality and physical-resource replay."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from copy import deepcopy
import json,hashlib
from sage.all import QQ,matrix,vector,Polyhedron
import k2027_thermal_pattern_frontier_probe as c
import k2029_multicomponent_thermal_placement_probe as p
import k2035_thermal_five_level_phase as primary
ROOT=Path(__file__).resolve().parents[2]
def run():
 r=json.loads(primary.OUT.read_text());A,C,B,lo,hi=map(F,[r[k] for k in ['intercept','slope','backward_slope','lower','certificate_upper']]);end=F(r['phase_upper']);c.intercept,c.slope,c.back,c.lo,c.hi=A,C,B,lo,hi
 d=primary.unpack(r);exp=iter((xs,o) for xs in p.words(21) if xs[0]<=hi for o in product((-1,1),repeat=len(xs)-1));contacts=[];n=0
 for row in d['connected']:
  xs,o=next(exp);assert row['s']==list(xs) and row['o']==list(o);cc=row['certificate']
  if 'infeasible_energy' in cc:assert c.validate_dual(xs,o,cc['infeasible_energy'])>hi
  elif 'infeasible_maxenergy' in cc:assert -c.validate_dual(xs,o,cc['infeasible_maxenergy'])<lo
  else:
   val=c.validate_dual(xs,o,cc);assert val>=A
   if val==A:contacts.append((xs,o,cc))
  n+=1
  if n%50000==0:print('separate strip',n,flush=True)
 assert next(exp,None) is None and n==r['connected_cells']
 # Strict-interior equality: neither endpoint multiplier may be negative.
 interior=0;left_only=0
 for ix,(xs,o,cc) in enumerate(contacts):
  if F(cc['y'][-1])<0:left_only+=1;continue
  aa,bb,cost=c.reconstruct(xs,o,'strip');nn=len(xs);yy=list(map(F,cc['y']));z=F(cc['z']);red=[cost[j]-z*int(j<nn)-sum(a[j]*v for a,v in zip(aa,yy)) for j in range(2*nn)]
  eq=[[QQ(j<nn) for j in range(2*nn)]+[QQ(0),QQ(-1)],[QQ(xs[j]) if j<nn else QQ(0) for j in range(2*nn)]+[QQ(-1),QQ(0)]]
  for j,v in enumerate(red):
   if v>0:eq.append([QQ(k==j) for k in range(2*nn)]+[QQ(0),QQ(0)])
  for ar,v,b in zip(aa,yy,bb):
   if v<0:eq.append(list(map(QQ,ar))+[QQ(0),-QQ(b)])
  kernel=matrix(QQ,eq).right_kernel().basis_matrix()
  for j,e in enumerate(xs):
   a,b=(F(3,2),F(-1,2)) if e==1 else ((F(-1,2),F(1,2)) if e==3 else (F(0),F(0)))
   assert kernel*vector(QQ,[QQ(k==j) for k in range(2*nn)]+[-QQ(b),-QQ(a)])==0,'unique affine diagonal'
  interior+=1
  if ix%5000==0:print('separate equality',ix,flush=True)
 assert (len(contacts),interior,left_only)==(r['equality']['contacts'],r['equality']['interior'],r['equality']['left_only'])
 # Physical completion is forced by the two doubly occupied shells3,4.
 forced={shell-b for shell in [3,4] for b in range(4)};assert forced==set(range(5))
 for w in r['witnesses']:assert c.physical(w)[0]==A-C*F(w['energy'])
 for w in r['successor_witnesses']:assert c.physical(w)[0]==F(3,28)*(5-F(w['energy']))<F(3,10)
 # Exact entire successor interval: reduce each shell maximum to its branch,
 # then prove all population/deficit inequalities by endpoint linearity.
 from sympy import symbols,Rational,simplify
 E=symbols('E');pop=[(5-E)/7,3*(5-E)/14,(5*E-11)/14]
 assert simplify(sum(pop)-1)==0 and simplify(sum(x*y for x,y in zip([1,3,5],pop))-E)==0
 assert simplify(pop[1]-Rational(3,2)*pop[0])==0
 for z in [pop[0],pop[1],pop[2],pop[1]/9-pop[2]]:
  assert z.subs(E,Rational(11,5))>=0 and z.subs(E,Rational(19,8))>=0
 assert simplify(pop[1]/2-3*(5-E)/28)==0
 # Reconstruct the new short-placement constraints from bath labels.
 pen=list((F(a),F(b)) for a,b in r['component_lines'])+[(F(1,4),F(3,4)),(F(3,20),F(63,100))]
 ex=iter((xs,o) for xs in p.words(7) if xs[0]==1 and (1 if len(xs)==1 else xs[-2]+3)<8 for o in product((-1,1),repeat=len(xs)-1));short=0
 for row in d['short']:
  xs,o=next(ex);assert row['s']==list(xs) and row['o']==list(o);nn=len(xs);L=1 if nn==1 else xs[-2]+3;off=min(F(L)+F(1,2),F(xs[-1]+2));aa=[ar+[F(0)]*3 for ar in p.raw(xs,o)];bb=[F(0)]*len(aa);en=list(map(F,xs))+[F(0)]*nn+[F(0),F(1),F(0)];aa +=[en,[-x for x in en],[F(0)]*(2*nn)+[off+1,-F(1),F(0)]];bb +=[end,-lo,F(0)]
  for lam,alpha0 in pen:aa.append([F(0)]*(2*nn)+[alpha0+lam*off,-lam,-F(1)]);bb.append(F(0))
  eq=[F(1)]*nn+[F(0)]*nn+[F(1),F(0),F(0)]
  if 'infeasible_energy' in row:
   k=2*nn-1;assert p.dual(en,aa[:k]+aa[k+2:],bb[:k]+bb[k+2:],eq,row['infeasible_energy'])>end
  else:
   cost=[C*x for x in xs]+[F(1)]*nn+[F(0),C,F(1)];value=p.dual(cost,aa,bb,eq,row['cert']);assert value>=A
   if value==A:
    yy=list(map(F,row['cert']['y']));zz=F(row['cert']['z']);red=[v-zz*e-sum(ar[j]*y for ar,y in zip(aa,yy)) for j,(v,e) in enumerate(zip(cost,eq))]
    assert red[2*nn]+(off+1)*red[2*nn+1]>0,'equality excludes other components'

  short+=1
 assert next(ex,None) is None
 faults=[];xs,o,cc=contacts[0]
 for kind in ['dual_normalization','dual_sign']:
  bad=deepcopy(cc)
  if kind=='dual_sign':bad['y'][0]='1'
  else:bad['z']=str(F(bad['z'])+1)
  try:c.validate_dual(xs,o,bad)
  except AssertionError:faults.append(kind)
  else:raise AssertionError('accepted '+kind)
 for kind in ['population','shell_completion','return']:
  bad=deepcopy(r['witnesses'][0])
  if kind=='population':bad['population'][0]=str(F(bad['population'][0])+F(1,10))
  elif kind=='shell_completion':bad['spectrum']=bad['support']
  else:bad['return_value']=str(F(bad['return_value'])-F(1,10))
  try:c.physical(bad)
  except AssertionError:faults.append(kind)
  else:raise AssertionError('accepted '+kind)
 for f,h in r['inputs'].items():assert hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h
 print('PASS K2035 separate',n,'strip;',len(contacts),'contacts;',interior,'affine cells;',left_only,'lower endpoint cells;five forced physical levels;entire seven-level successor;',short,'placement;',faults,flush=True)
if __name__=='__main__':run()
