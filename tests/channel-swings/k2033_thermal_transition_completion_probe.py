"""Separate bath-label certificate, equality and physical-resource replay."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from copy import deepcopy
import json,hashlib
from sage.all import QQ,matrix,vector,Polyhedron
import k2027_thermal_pattern_frontier_probe as c
import k2029_multicomponent_thermal_placement_probe as p
import k2033_thermal_transition_completion as primary
ROOT=Path(__file__).resolve().parents[2]
def endpoint_face(xs,o,cc,E):
 aa,bb,cost=c.reconstruct(xs,o,'strip');n=len(xs);yy=list(map(F,cc['y']));z=F(cc['z'])
 if E==c.lo and yy[-2]<0:return []
 if E==c.hi and yy[-1]<0:return []
 red=[cost[j]-z*int(j<n)-sum(a[j]*v for a,v in zip(aa,yy)) for j in range(2*n)]
 assert min(red)>=0
 eqs=[[-QQ(1)]+[QQ(j<n) for j in range(2*n)],[-QQ(E)]+[QQ(xs[j]) if j<n else QQ(0) for j in range(2*n)],[-QQ(c.intercept-c.slope*E)]+[QQ(j>=n) for j in range(2*n)]]
 for j,v in enumerate(red):
  if v>0:eqs.append([QQ(0)]+[QQ(k==j) for k in range(2*n)])
 for ar,v,b in zip(aa,yy,bb):
  if v<0:eqs.append([-QQ(b)]+list(map(QQ,ar)))
 M=matrix(QQ,[r[1:] for r in eqs]);rhs=vector(QQ,[-r[0] for r in eqs])
 try:x=M.solve_right(rhs)
 except ValueError:return []
 ker=M.right_kernel().basis_matrix()
 if all(all(v[j]==0 for j in range(n)) for v in ker.rows()):
  # Unique p determines minimal epigraph z; check the primal point directly.
  pv=list(map(F,map(str,x[:n])))
  if min(pv)<0:return []
  zz=[]
  for a in aa[n-1:2*n-1]:zz.append(max(sum(a[j]*pv[j] for j in range(n)),F(0)))
  xx=pv+zz
  if any(sum(a*b for a,b in zip(ar,xx))>b for ar,b in zip(aa,bb)):return []
  if sum(zz)!=c.intercept-c.slope*E:return []
  return [tuple((e,str(v)) for e,v in zip(xs,pv) if v)]
 ieqs=[[QQ(b)]+[-QQ(v) for v in ar] for ar,b in zip(aa,bb)]+[[QQ(0)]+[QQ(k==j) for k in range(2*n)] for j in range(2*n)]
 poly=Polyhedron(ieqs=ieqs,eqns=eqs,base_ring=QQ,backend='ppl');assert poly.is_compact() and poly.dim()<=0,'nonisolated equality face'
 return [tuple((e,str(v)) for e,v in zip(xs,v[:n]) if v) for v in poly.vertices_list()]
def run():
 r=json.loads(primary.OUT.read_text());A,C,B,lo,hi=primary.parameters(r);c.intercept,c.slope,c.back,c.lo,c.hi=A,C,B,lo,hi
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
 w0,w1=r['witnesses'][:2];sp=w0['support'];v0=list(map(F,w0['population']));v1=list(map(F,w1['population']));beta=[(b-a)/(hi-lo) for a,b in zip(v0,v1)];alpha=[a-b*lo for a,b in zip(v0,beta)];interior=0
 ends={'left':set(),'right':set()}
 for ix,(xs,o,cc) in enumerate(contacts):
  if F(cc['y'][-1])==0 and F(cc['y'][-2])==0:
   aa,bb,cost=c.reconstruct(xs,o,'strip');nn=len(xs);yy=list(map(F,cc['y']));z=F(cc['z']);red=[cost[j]-z*int(j<nn)-sum(a[j]*v for a,v in zip(aa,yy)) for j in range(2*nn)]
   eq=[[QQ(j<nn) for j in range(2*nn)]+[QQ(0),QQ(-1)],[QQ(xs[j]) if j<nn else QQ(0) for j in range(2*nn)]+[QQ(-1),QQ(0)]]
   for j,v in enumerate(red):
    if v>0:eq.append([QQ(k==j) for k in range(2*nn)]+[QQ(0),QQ(0)])
   for ar,v,b in zip(aa,yy,bb):
    if v<0:eq.append(list(map(QQ,ar))+[QQ(0),-QQ(b)])
   kernel=matrix(QQ,eq).right_kernel().basis_matrix()
   for j,e in enumerate(xs):
    a,b=(alpha[sp.index(e)],beta[sp.index(e)]) if e in sp else (F(0),F(0))
    assert kernel*vector(QQ,[QQ(k==j) for k in range(2*nn)]+[-QQ(b),-QQ(a)])==0
   interior+=1
  for side,E in [('left',lo),('right',hi)]:ends[side].update(endpoint_face(xs,o,cc,E))
  if ix%3000==0:print('separate equality',ix,flush=True)
 for side in ends:
  expected={tuple((x[0],x[1]) for x in v) for v in r['equality'][side]['vertices']};assert ends[side]==expected and len(expected)==2
  for v in expected:
   support=[x[0] for x in v];forced=set()
   for shell in {x+b for x in support for b in range(4)}:
    if sum(shell-x in (0,1,2,3) for x in support)==2:forced.update(shell-b for b in range(4))
   assert forced==set(range(max(support)+2))
 # Each exact diagonal is physically attained; shell overlap, not occupancy count,
 # gives minimum dimensions. No convexity of the unrestricted problem is assumed.
 for w in r['witnesses']:assert c.physical(w)[0]==A-C*F(w['energy'])
 assert c.physical(r['failed_extrapolation'])[0]<A-C*F(r['failed_extrapolation']['energy'])
 # Reconstruct the new short-placement constraints from bath labels.
 pen=list((F(a),F(b)) for a,b in r['component_lines'])+[(F(1,4),F(3,4)),(F(3,20),F(63,100))]
 ex=iter((xs,o) for xs in p.words(7) if xs[0]==1 and (1 if len(xs)==1 else xs[-2]+3)<8 for o in product((-1,1),repeat=len(xs)-1));short=0
 for row in d['short']:
  xs,o=next(ex);assert row['s']==list(xs) and row['o']==list(o);nn=len(xs);L=1 if nn==1 else xs[-2]+3;off=min(F(L)+F(1,2),F(xs[-1]+2));aa=[ar+[F(0)]*3 for ar in p.raw(xs,o)];bb=[F(0)]*len(aa);en=list(map(F,xs))+[F(0)]*nn+[F(0),F(1),F(0)];aa +=[en,[-x for x in en],[F(0)]*(2*nn)+[off+1,-F(1),F(0)]];bb +=[hi,-lo,F(0)]
  for lam,alpha0 in pen:aa.append([F(0)]*(2*nn)+[alpha0+lam*off,-lam,-F(1)]);bb.append(F(0))
  eq=[F(1)]*nn+[F(0)]*nn+[F(1),F(0),F(0)]
  if 'infeasible_energy' in row:
   k=2*nn-1;assert p.dual(en,aa[:k]+aa[k+2:],bb[:k]+bb[k+2:],eq,row['infeasible_energy'])>hi
  else:
   cost=[C*x for x in xs]+[F(1)]*nn+[F(0),C,F(1)];value=p.dual(cost,aa,bb,eq,row['cert']);assert value>=A
   if value==A:
    yy=list(map(F,row['cert']['y']));zz=F(row['cert']['z']);red=[v-zz*e-sum(ar[j]*y for ar,y in zip(aa,yy)) for j,(v,e) in enumerate(zip(cost,eq))]
    assert yy[2*nn-1]<0 and red[2*nn+1]>0 and off+1>0,'endpoint excludes other components'

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
 print('PASS K2033 separate',n,'strip;',len(contacts),'contacts;',interior,'interior affine cells;both endpoint sets exact;5/17/21 forced dimensions;',short,'placement;',faults,flush=True)
if __name__=='__main__':run()
