"""Exact physical-time spin-7 algebraic constraint block at both fixed roots.

Reconstructs the complete highest-weight multiplicity space, native time
kernel, actual cubic compression and exact rational-root-ball inverse bound.
No physical particle spin, propagated ghost or full-carrier inverse is claimed.
Standard-library only. Root coordinates and certificate balls are held data.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import argparse,json,sys,time,hashlib

def run_spin7(root):
 sys.path.insert(0,str(root/'tests/program-focus'))
 import source_action_deep_geometry as g
 from source_action_deep_algebra import Engine,add,scale
 from source_action_metric_symbol_probe import symbols
 class C:
  def __init__(self,a=0,b=0):
   if isinstance(a,C):self.a,self.b=a.a,a.b
   else:self.a,self.b=Q(a),Q(b)
  def __add__(x,y):
   y=C(y);return C(x.a+y.a,x.b+y.b)
  __radd__=__add__
  def __neg__(x):return C(-x.a,-x.b)
  def __sub__(x,y):return x+-C(y)
  def __rsub__(x,y):return C(y)+-x
  def __mul__(x,y):
   y=C(y);return C(x.a*y.a-x.b*y.b,x.a*y.b+x.b*y.a)
  __rmul__=__mul__
  def __truediv__(x,y):
   y=C(y);d=y.a*y.a+y.b*y.b;return C((x.a*y.a+x.b*y.b)/d,(x.b*y.a-x.a*y.b)/d)
  def __rtruediv__(x,y):return C(y)/x
  def __bool__(x):return bool(x.a or x.b)
  def __eq__(x,y):
   y=C(y);return x.a==y.a and x.b==y.b
  def __repr__(x):return str(x.a)+'+i*'+str(x.b)
  def conj(x):return C(x.a,-x.b)
  def ser(x):return [str(x.a),str(x.b)]
 I=C(0,1);E=Engine(g)

 def rankker(a):
  a=[[C(x)for x in row]for row in a];row=0;ps=[]
  for c in range(len(a[0])):
   k=next((j for j in range(row,len(a))if a[j][c]),None)
   if k is None:continue
   a[k],a[row]=a[row],a[k];q=a[row][c];a[row]=[x/q for x in a[row]]
   for j in range(len(a)):
    q=a[j][c]
    if j!=row and q:a[j]=[x-q*y for x,y in zip(a[j],a[row])]
   ps.append(c);row+=1
   if row==len(a):break
  z=[]
  for k in range(len(a[0])):
   if k in ps:continue
   v=[C()for _ in range(len(a[0]))];v[k]=C(1)
   for j,p in enumerate(ps):v[p]=-a[j][k]
   z.append(v)
  return ps,z

 def conj(x):return {k:C(v).conj()for k,v in x.items()}
 def rot(i,j,x):
  H=g.zero();H[i][j]=Q(1);H[j][i]=Q(-1)
  act=[g.h_action(H,a)for a in range(14)];sp={}
  for a in range(14):
   for b in range(a+1,14):
    q=act[b].get(a,Q(0))/(2*g.d[b])
    if q:sp[(1<<a)|(1<<b)]=q
  out={}
  for(e,c),v in x.items():
   ai=e.bit_length()-1
   # theta_ai transforms - transpose of tangent generator
   for b in range(14):
    q=-act[b].get(ai,Q(0))
    if q:
     k=(1<<b,c);out[k]=out.get(k,0)+v*q
   for cc,q in E.cliff_product(sp,{c:Q(1)},'comm').items():
    k=(e,cc);out[k]=out.get(k,0)+v*q
  return {k:v for k,v in out.items()if v}

 pos=[(0,1),(10,12),(9,11),(5,8)];zero=[2,3,4,6,7,13]
 p={0:C(1)}
 for a,b in pos:
  p=E.cliff_product(p,{1<<a:C(1),1<<b:I})
 bs=[];meta=[];piv=[]
 for mask in range(64):
  z=[zero[j]for j in range(6)if mask>>j&1]
  if (4+len(z))%4 not in(0,3):continue
  cliff=p
  for a in z:cliff=E.cliff_product(cliff,{1<<a:C(1)})
  v={}
  for a,f in[(5,C(1)),(8,I)]:
   for c,q in cliff.items():v[(1<<a,c)]=f*q
  key=min(v);v=scale(1/v[key],v)
  bs.append(v);piv.append(key);meta.append({'zeros':z,'degree':4+len(z)})
 assert len(bs)==36
 assert all(B.get(p,C(0))==int(i==j)for i,p in enumerate(piv)for j,B in enumerate(bs))
 for b in bs:
  assert rot(0,1,b)==scale(7*I,b),('weight',rot(0,1,b),scale(7*I,b))
  # If J01 has +i*m, J02+i J12 annihilates highestweight (checked scalarvector).
  assert not add(rot(0,2,b),scale(I,rot(1,2,b))),('raise',add(rot(0,2,b),scale(I,rot(1,2,b))))

 def coords(v):
  cs=[C(v.get(k,0))for k in piv]
  assert v==add(*(scale(c,b)for c,b in zip(cs,bs)if c)),('outside_spin7',len(v))
  return cs
 xi=[Q(0)]*14;xi[3]=1
 cols=[coords(symbols(E,xi,b)[0])for b in bs]
 K=[list(row)for row in zip(*cols)]
 ps,zs=rankker(K)
 N=[add(*(scale(c,b)for c,b in zip(z,bs)if c))for z in zs]
 G=[[E.pair(conj(u),v)for v in bs]for u in bs]
 GN=[[E.pair(conj(u),v)for v in N]for u in N]
 D=json.load(open(root/'lab/process/source-action-deep-coefficients.json'))
 basis=[{(int(e),int(c)):Q(v)for e,c,v in row}for row in D['basis']]
 n=len(N);Z=C(0)
 coeff=[[[C(0)for q in range(59)]for j in range(n)]for i in range(n)]
 start=time.monotonic()
 for i in range(n):
  for j in range(i,n):
   receiver=scale(2,E.N(conj(N[i]),N[j]))
   v=[C(E.pair(T,receiver))for T in basis]
   if i==j:assert all(not z.b for z in v)
   coeff[i][j]=v
   coeff[j][i]=[x.conj()for x in v]



 def inverse(a):
  n=len(a);a=[[C(x)for x in row]+[C(i==j)for j in range(n)]for i,row in enumerate(a)]
  for c in range(n):
   k=next((j for j in range(c,n)if a[j][c]),None)
   if k is None:return None
   a[k],a[c]=a[c],a[k];q=a[c][c];a[c]=[x/q for x in a[c]]
   for j in range(n):
    q=a[j][c]
    if j!=c and q:a[j]=[x-q*y for x,y in zip(a[j],a[c])]
  return [row[n:]for row in a]

 def norm1(z):z=C(z);return abs(z.a)+abs(z.b)
 results=[]
 for ri,root in enumerate(D['certified_roots']):
  x=list(map(Q,root['coordinates']));r=Q(root['certificate']['radius'])
  H=[[C(GN[i][j])+sum((a*b for a,b in zip(coeff[i][j],x)),C())for j in range(n)]for i in range(n)]
  assert all(H[i][j]==H[j][i].conj()for i in range(n)for j in range(n))

  R=inverse(H)
  if R is None:results.append({'root':ri,'status':'singular_center_not_certificate'});continue
  # Exact center residual, and rootball Neumann coefficient norm.
  defect=max(sum(norm1(sum((R[i][k]*H[k][j]for k in range(n)),C())-C(i==j))for j in range(n))for i in range(n))
  assert not defect
  # Bound after R applied to each actual affine coefficient: often tighter than product norms.
  B=max(sum(sum(norm1(sum((R[i][k]*coeff[k][j][q]for k in range(n)),C()))for q in range(59))for j in range(n))for i in range(n))
  eta=r*B
  result={'root':ri,'status':'exact_rootball_invertibility_certified'if eta<1 else 'inconclusive_bound',
  'radius':str(r),'affine_inverse_coefficient_bound':str(B),'neumann_bound':str(eta),'approximate_neumann_bound':float(eta),
  'matrix_center':[[z.ser()for z in row]for row in H],'inverse':[[z.ser()for z in row]for row in R],
  'center_defect':str(defect)}
  results.append(result)
 # Confirm the complete highest-weight character count independently.
 weights=[0]*6+[1]*3+[-1]*3+[2,-2]
 dp={(0,0):1}
 for w in weights:
  nxt=dict(dp)
  for (degree,weight),count in dp.items():
   key=(degree+1,weight+w);nxt[key]=nxt.get(key,0)+count
  dp=nxt
 char={}
 for (degree,weight),count in dp.items():
  if degree%4 in (0,3):
   for w in weights:char[weight+w]=char.get(weight+w,0)+count
 assert sum(char.values())==115584 and max(char)==7 and char[7]==36
 assert len(N)==16 and len(ps)==20 and len(rankker(GN)[0])==16
 # Existing repository-built stationary59 family is SO(3)-invariant.
 rotation_controls=0
 for T in basis:
  for a,b in ((0,1),(0,2),(1,2)):
   assert not rot(a,b,T)
   rotation_controls+=1
 # Direct-versus-trilinear/cubic-factor controls on nonzero entries.
 trilinear_controls=0
 for i,j,q in ((0,0,0),(1,2,4),(3,5,7),(8,8,1)):
  lhs=C(E.pair(conj(N[i]),scale(2,E.N(basis[q],N[j]))))
  assert lhs==coeff[i][j][q]
  if lhs:assert lhs!=lhs/2
  trilinear_controls+=1
 # Character coset graph of this actual compression; no sampled-root zeros.
 adjacency={i:set()for i in range(n)}
 for i in range(n):
  for j in range(n):
   if C(GN[i][j]) or any(coeff[i][j]):adjacency[i].add(j);adjacency[j].add(i)
 components=[];seen=set()
 for i in range(n):
  if i in seen:continue
  todo=[i];component=[]
  while todo:
   u=todo.pop()
   if u in seen:continue
   seen.add(u);component.append(u);todo+=list(adjacency[u]-seen)
  components.append(sorted(component))
 assert sorted(map(len,components))==[1,1,4,4,6]
 scalar=[]
 for component in components:
  if len(component)!=1:continue
  i=component[0];g0=C(GN[i][i]);assert g0 and not g0.b
  linear=[z/g0 for z in coeff[i][i]];assert all(not z.b for z in linear)
  intervals=[]
  for ri,r in enumerate(results):
   center=C(*r['matrix_center'][i][i])/g0
   error=Q(r['radius'])*sum(abs(z.a)for z in linear)
   assert not center.b and (center.a>error if ri==0 else center.a < -error)
   intervals.append({'root':ri,'center':str(center.a),'error':str(error),
     'lower':str(center.a-error),'upper':str(center.a+error),
     'approximate_center':float(center.a),'sign':'positive'if center.a>0 else 'negative'})
  scalar.append({'kernel_index':i,'kappa_coefficient':'1','background59_coefficients':[str(z.a)for z in linear],'root_intervals':intervals})
 def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 # Direct literal connection readout is horizontal-form restriction.
 def qread(v):return {k:x for k,x in v.items()if k[0] < 16}
 observation=[]
 for v in bs:
  assert not qread(v)
  receivers=[]
  for a in range(14):
   cov=[Q(0)]*14;cov[a]=Q(1)
   if qread(symbols(E,cov,v)[0]):receivers.append(a)
  assert receivers
  observation.append(receivers)
 # Keep exact certificates compact: probe reconstructs the matrices/inverses.
 for r in results:
  r['matrix_center_sha256']=digest(r.pop('matrix_center'))
  r['inverse_sha256']=digest(r.pop('inverse'))
 return {'highest_weight':7,'highest_weight_multiplicity':36,
   'direct_readout_zero_controls':36,'nonzero_q_symbol_receiver_axes':observation,
   'time_rank':20,'time_kernel':16,'kernel_gram_rank':16,
   'real_spin7_carrier_dimension':540,'real_spin7_kernel_dimension':240,
   'full_imaginary_kernel':49154,'remaining_imaginary_kernel':48914,
   'source_family_rotation_controls':rotation_controls,'trilinear_controls':trilinear_controls,
   'constraint_components':components,'constraint_coefficients_sha256':digest([[[z.ser()for z in col]for col in row]for row in coeff]),
   'time_matrix_sha256':digest([[z.ser()for z in row]for row in K]),
   'kernel_gram_sha256':digest([[C(z).ser()for z in row]for row in GN]),
   'root_certificates':results,'isolated_scalar_eigenvalues':scalar,
   'root_certificates_recomputed_here':False,
   'scope':'Actual pointwise closed-time algebraic spin7 constraint block only; all59 fixed backgrounds covered. Neither full49154 inverse nor autonomousPDE nor observed particle spin nor ghost inferred.'}



def run_structure(root):
 from functools import lru_cache
 sys.path.insert(0,str(root/'tests/program-focus'))
 import source_action_deep_geometry as g
 from source_action_deep_algebra import Engine,add,scale
 from source_action_metric_symbol_probe import symbols
 from source_action_physical_probe import interval
 E=Engine(g); t=3

 def Kaxis(axis,v):
  xi=[Q(0)]*14;xi[axis]=Q(1)
  return symbols(E,xi,v)[0]

 def rref(a):
  a=[list(r)for r in a];row=0;piv=[]
  for c in range(len(a[0])):
   k=next((k for k in range(row,len(a))if a[k][c]),None)
   if k is None:continue
   a[row],a[k]=a[k],a[row];q=a[row][c];a[row]=[x/q for x in a[row]]
   for k in range(len(a)):
    if k!=row and a[k][c]:
     q=a[k][c];a[k]=[x-q*y for x,y in zip(a[k],a[row])]
   piv.append(c);row+=1
   if row==len(a):break
  return a,piv

 def inverse(a):
  n=len(a);r,p=rref([row+[Q(i==j)for j in range(n)]for i,row in enumerate(a)])
  assert p==list(range(n)),p
  return [row[n:]for row in r]

 @lru_cache(maxsize=256)
 def block(r):
  assert not(r>>t&1)
  bs=[(1<<i,(1<<i)^r^z)for z in (0,1<<t)for i in range(14)]
  cs=[Kaxis(t,{k:Q(1)})for k in bs]
  assert all(set(c)<=set(bs)for c in cs)
  a=[[c.get(k,Q(0))for c in cs]for k in bs]
  rr,piv=rref(a);zs=[]
  for k in range(28):
   if k in piv:continue
   v=[Q(0)]*28;v[k]=Q(1)
   for j,c in enumerate(piv):v[c]=-rr[j][k]
   zs.append({bs[i]:x for i,x in enumerate(v)if x})
  gram=[[E.pair(u,v)for v in zs]for u in zs]
  return bs,zs,inverse(gram)

 def project(v):
  by={}
  for (e,c),x in v.items():by.setdefault((e^c)&~(1<<t),{})[(e,c)]=x
  out={}
  for r,w in by.items():
   bs,zs,ginv=block(r);b=[E.pair(z,w)for z in zs]
   co=[sum(x*y for x,y in zip(row,b))for row in ginv]
   out=add(out,*(scale(x,z)for x,z in zip(co,zs)))
  return out

 def boost(j,v):
  # Active Lorentz tangent generator has J[j,t]=J[t,j]=1.
  # Covectors: theta_t -> -theta_j; Clifford: gamma_t -> gamma_j.
  b={(1<<j)|(1<<t):Q(-1,2)}
  out={}
  for (e,c),x in v.items():
   a=e.bit_length()-1
   if a in (j,t):
    k=(1<<(t if a==j else j),c);out[k]=out.get(k,Q(0))-x
   for cc,y in E.cliff_product(b,{c:Q(1)},'comm').items():
    k=(e,cc);out[k]=out.get(k,Q(0))+x*y
  return {k:x for k,x in out.items()if x}

 def derivative(j,n):
  # R J n, the N-orthogonal local lift derivative.
  z=boost(j,n);return add(z,scale(-1,project(z)))

 def correction(n):
  # physical dt at the section: dxi along A03,A13,A23 is -theta_j.
  return project(add(*(Kaxis(A,derivative(j,n))for j,A in [(0,10),(1,12),(2,13)])))

 def serial(x):return [[e,c,str(v)]for(e,c),v in sorted(x.items())]

 n={(8,0):Q(1)}
 covariance=0
 for j in range(3):
  for v in [n,{(1<<j,0):Q(1)},{(1<<4,11):Q(1)}]:
   lhs=add(boost(j,Kaxis(t,v)),scale(-1,Kaxis(t,boost(j,v))))
   assert lhs==scale(-1,Kaxis(j,v));covariance+=1
 geom=project(E.K(n));move=correction(n)
 assert geom and move and not add(geom,move)
 assert geom=={(8,1033):Q(1,4),(8,4106):Q(1,4),(8,8204):Q(1,4)}
 D=json.loads((root/'lab/process/source-action-deep-coefficients.json').read_text())
 basis=[{(int(e),int(c)):Q(v)for e,c,v in row}for row in D['basis']]
 ms=[project(scale(2,E.N(basis[i],n)))for i in (3,4)]
 cols=[scale(2,E.N(T,n))for T in basis]
 cubic=[]
 for m in ms:
  assert not Kaxis(t,m) and not E.pair(m,n)
  cf=[E.pair(m,col)for col in cols]
  iv=[interval(cf,r)for r in D['certified_roots']]
  assert all(Q(z['lower'])>0 or Q(z['upper'])<0 for z in iv)
  cubic.append({'raw_receiver':serial(m),'linear59':list(map(str,cf)),
                'raw_gram':str(E.pair(m,m)),'root_intervals':iv})
 trans=[j for j in range(14)if j!=t]
 common=[];phase=[];transport=[]
 for s in range(14):
  r=sum(1<<a for a in trans[:s]);bs,zs,inv=block(r)
  rows=[];progress=[]
  for axis in trans:
   cs=[Kaxis(axis,z)for z in zs]
   keys=sorted(set().union(*(set(c)for c in cs)))
   rows += [[c.get(k,Q(0))for c in cs]for k in keys]
   rk=len(rref(rows)[1]);progress.append([axis,len(zs)-rk])
   if rk==len(zs):break
  assert rk==len(zs)
  common.append({'s':s,'time_kernel':len(zs),'joint_kernel':0,'progress':progress})
  im=[z for z in zs if all(c.bit_count()%4 in(0,3)for e,c in z)]
  phase.append((sum(c.bit_count()%4 in(0,3)for e,c in bs),len(im)))
  for z in im[:2]:
   a=project(E.K(z));b=correction(z);assert not add(a,b)
   transport.append({'s':s,'homogeneous_support':len(a),'moving_support':len(b)})
 labels=sorted({e^c for T in basis for e,c in T})
 def red(x,ps):
  for k in sorted(ps,reverse=True):
   if x>>k&1:x^=ps[k]
  return x
 ps={}
 for x in labels:
  x=red(x,ps)
  if x:ps[x.bit_length()-1]=x
 assert len(ps)==10
 x=red(8,ps);assert x;ps[x.bit_length()-1]=x
 assert len(ps)==11
 sectors={}
 for r in range(1<<14):
  if r&8:continue
  coset=red(r,ps);s=r.bit_count()
  item=sectors.setdefault(coset,{'time_blocks':0,'imaginary_dimension':0,'imaginary_kernel':0})
  item['time_blocks']+=1;item['imaginary_dimension']+=phase[s][0];item['imaginary_kernel']+=phase[s][1]
 assert len(sectors)==8 and sum(v['imaginary_kernel']for v in sectors.values())==49154
 assert sum(v['imaginary_dimension']for v in sectors.values())==115584
 assert sorted(v['imaginary_kernel']for v in sectors.values())==[6144]*7+[6146]
 return {'covariance_controls':covariance,'homogeneous_mutation':serial(geom),'moving_correction':serial(move),
         'transport_controls':transport,'common_symbol_radical':common,'cubic_nonzero_couplings':cubic,
         'label_rank':10,'label_plus_time_rank':11,'label_basis':sorted(ps.values()),'cosets':sectors}


def run_spin6(root):
    """Complete highest-spin6 counts/readout and spin7 direct-observation controls.
    Pure finite native algebra; no PDE propagation or physical particle count.
    Standard library only; root is the GU repository root.
    """
    from pathlib import Path
    from fractions import Fraction as Q
    from types import SimpleNamespace
    import sys
    sys.path.insert(0,str(Path(root)/'tests/program-focus'))
    import source_action_deep_geometry as g
    from source_action_deep_algebra import Engine,add,scale
    from source_action_metric_symbol_probe import symbols
    class C:
     def __init__(self,a=0,b=0):
      if isinstance(a,C):self.a,self.b=a.a,a.b
      else:self.a,self.b=Q(a),Q(b)
     def __add__(x,y):
      y=C(y);return C(x.a+y.a,x.b+y.b)
     __radd__=__add__
     def __neg__(x):return C(-x.a,-x.b)
     def __sub__(x,y):return x+-C(y)
     def __rsub__(x,y):return C(y)+-x
     def __mul__(x,y):
      y=C(y);return C(x.a*y.a-x.b*y.b,x.a*y.b+x.b*y.a)
     __rmul__=__mul__
     def __truediv__(x,y):
      y=C(y);d=y.a*y.a+y.b*y.b;return C((x.a*y.a+x.b*y.b)/d,(x.b*y.a-x.a*y.b)/d)
     def __rtruediv__(x,y):return C(y)/x
     def __bool__(x):return bool(x.a or x.b)
     def __eq__(x,y):
      y=C(y);return x.a==y.a and x.b==y.b
     def __repr__(x):return str(x.a)+'+i*'+str(x.b)
     def conj(x):return C(x.a,-x.b)
     def ser(x):return [str(x.a),str(x.b)]
    I=C(0,1);E=Engine(g)

    def rankker(a):
     a=[[C(x)for x in row]for row in a];row=0;ps=[]
     for c in range(len(a[0])):
      k=next((j for j in range(row,len(a))if a[j][c]),None)
      if k is None:continue
      a[k],a[row]=a[row],a[k];q=a[row][c];a[row]=[x/q for x in a[row]]
      for j in range(len(a)):
       q=a[j][c]
       if j!=row and q:a[j]=[x-q*y for x,y in zip(a[j],a[row])]
      ps.append(c);row+=1
      if row==len(a):break
     z=[]
     for k in range(len(a[0])):
      if k in ps:continue
      v=[C()for _ in range(len(a[0]))];v[k]=C(1)
      for j,p in enumerate(ps):v[p]=-a[j][k]
      z.append(v)
     return ps,z

    def conj(x):return {k:C(v).conj()for k,v in x.items()}
    def rot(i,j,x):
     H=g.zero();H[i][j]=Q(1);H[j][i]=Q(-1)
     act=[g.h_action(H,a)for a in range(14)];sp={}
     for a in range(14):
      for b in range(a+1,14):
       q=act[b].get(a,Q(0))/(2*g.d[b])
       if q:sp[(1<<a)|(1<<b)]=q
     out={}
     for(e,c),v in x.items():
      ai=e.bit_length()-1
      # theta_ai transforms - transpose of tangent generator
      for b in range(14):
       q=-act[b].get(ai,Q(0))
       if q:
        k=(1<<b,c);out[k]=out.get(k,0)+v*q
      for cc,q in E.cliff_product(sp,{c:Q(1)},'comm').items():
       k=(e,cc);out[k]=out.get(k,0)+v*q
     return {k:v for k,v in out.items()if v}

    pos=[(0,1),(10,12),(9,11),(5,8)];zero=[2,3,4,6,7,13]
    p={0:C(1)}
    for a,b in pos:
     p=E.cliff_product(p,{1<<a:C(1),1<<b:I})
    bs=[];meta=[];piv=[]
    for mask in range(64):
     z=[zero[j]for j in range(6)if mask>>j&1]
     if (4+len(z))%4 not in(0,3):continue
     cliff=p
     for a in z:cliff=E.cliff_product(cliff,{1<<a:C(1)})
     v={}
     for a,f in[(5,C(1)),(8,I)]:
      for c,q in cliff.items():v[(1<<a,c)]=f*q
     key=min(v);v=scale(1/v[key],v)
     bs.append(v);piv.append(key);meta.append({'zeros':z,'degree':4+len(z)})
    assert len(bs)==36
    assert all(B.get(p,C(0))==int(i==j)for i,p in enumerate(piv)for j,B in enumerate(bs))
    for b in bs:
     assert rot(0,1,b)==scale(7*I,b),('weight',rot(0,1,b),scale(7*I,b))
     # If J01 has +i*m, J02+i J12 annihilates highestweight (checked scalarvector).
     assert not add(rot(0,2,b),scale(I,rot(1,2,b))),('raise',add(rot(0,2,b),scale(I,rot(1,2,b))))

    def coords(v):
     cs=[C(v.get(k,0))for k in piv]
     assert v==add(*(scale(c,b)for c,b in zip(cs,bs)if c)),('outside_spin7',len(v))
     return cs
    xi=[Q(0)]*14;xi[3]=1
    cols=[coords(symbols(E,xi,b)[0])for b in bs]
    K=[list(row)for row in zip(*cols)]
    ps,zs=rankker(K)
    N=[add(*(scale(c,b)for c,b in zip(z,bs)if c))for z in zs]
    G=[[E.pair(conj(u),v)for v in bs]for u in bs]
    GN=[[E.pair(conj(u),v)for v in N]for u in N]

    h=SimpleNamespace(C=C,I=I,E=E,pos=pos,zero=zero,bs=bs,N=N,meta=meta,rot=rot,add=add,scale=scale,symbols=symbols,conj=conj)
    spin7_obs=lambda v:{k:x for k,x in v.items()if k[0]in(1,2,4,8)}
    assert all(not spin7_obs(v)for v in bs)
    spin7_witnesses=[]
    for i,v in enumerate(bs):
     for a in range(14):
      xi=[Q(0)]*14;xi[a]=Q(1)
      image=spin7_obs(symbols(E,xi,v)[0])
      if image:
       spin7_witnesses.append({'basis':i,'axis':a,'receivers':[[e,c,C(x).ser()]for(e,c),x in sorted(image.items())]})
       break
    assert len(spin7_witnesses)==36
    def cwedge(a,b):
     out={}
     for c,x in a.items():
      for d,y in b.items():
       if c&d:continue
       k=c|d;out[k]=out.get(k,0)+E.sign(c,d)*x*y
     return {k:v for k,v in out.items()if v}
    def cmulti(vs):
     out={0:C(1)}
     for v in vs:out=cwedge(out,v)
     return out
    pos=[{1<<a:C(1),1<<b:I}for a,b in h.pos]
    neg=[{a:x.conj()for a,x in v.items()}for v in pos]
    zero=[{1<<a:C(1)}for a in h.zero]
    cl4=[]
    for omitted in range(3):
     for m in range(64):
      vs=[pos[j]for j in range(4)if j!=omitted]+[zero[j]for j in range(6)if m>>j&1]
      if len(vs)%4 in(0,3):cl4.append(cmulti(vs))
    for included in range(3):
     for m in range(64):
      vs=pos+[neg[included]]+[zero[j]for j in range(6)if m>>j&1]
      if len(vs)%4 in(0,3):cl4.append(cmulti(vs))
    assert len(cl4)==192
    cl5=[]
    for m in range(64):
     vs=pos+[zero[j]for j in range(6)if m>>j&1]
     if len(vs)%4 in(0,3):cl5.append(cmulti(vs))
    assert len(cl5)==36
    bs=[]
    for ext,cliffs in[(pos[3],cl4),(pos[0],cl5),(pos[1],cl5),(pos[2],cl5)]:
     for c in cliffs:
      v={(e,k):x*y for e,x in ext.items()for k,y in c.items()}
      bs.append(v)
    assert len(bs)==300

    def sparse_kernel(cols,progress=False):
     piv={};basis=[];kernels=[]
     for i,v in enumerate(cols):
      v=dict(v);cs={i:C(1)}
      while v:
       p=min(v)
       if p not in piv:
        q=v[p];v={k:x/q for k,x in v.items()};cs={k:x/q for k,x in cs.items()}
        piv[p]=len(basis);basis.append((v,cs));break
       b,bc=basis[piv[p]];q=v[p]
       for k,x in b.items():
        y=v.get(k,C(0))-q*x
        if y:v[k]=y
        elif k in v:del v[k]
       for k,x in bc.items():
        y=cs.get(k,C(0))-q*x
        if y:cs[k]=y
        elif k in cs:del cs[k]
      if not v:kernels.append(cs)
      # exact sparse elimination; no progress side effect
     return len(basis),kernels

    assert all(h.rot(0,1,b)==h.scale(6*I,b)for b in bs)

    rank,z=sparse_kernel(bs);assert rank==300

    xi=[Q(0)]*14;xi[3]=1
    cols=[]
    for i,b in enumerate(bs):
     cols.append(h.symbols(E,xi,b)[0])

    rank,z=sparse_kernel(cols)
    # Raising maps weight6 toweight7. Its kernel is the264 highestspin6 module.
    raised=[h.add(h.rot(0,2,b),h.scale(I,h.rot(1,2,b)))for b in bs]
    rraise,zraise=sparse_kernel(raised);assert rraise==36 and len(zraise)==264
    high6=[h.add(*(h.scale(c,bs[i])for i,c in z.items()))for z in zraise]
    assert all(not h.add(h.rot(0,2,b),h.scale(I,h.rot(1,2,b)))for b in high6)
    # Direct literal connection readout on completehighestspin6 basis.
    obs=lambda v:{k:x for k,x in v.items()if k[0]in(1,2,4,8)}
    qrank,qker=sparse_kernel([obs(b)for b in high6])
    # Timekernel withinhighestspin6: Ktime(high6) fullreceiver sparse eliminate.
    kh=[h.symbols(E,xi,b)[0]for b in high6]
    rhigh,zhigh=sparse_kernel(kh)
    Nh=[h.add(*(h.scale(c,high6[i])for i,c in z.items()))for z in zhigh]
    qNrank,qNker=sparse_kernel([obs(b)for b in Nh])
    assert len(zhigh)==len(z)-16
    result={'weight6_dimension':300,'weight6_time_rank':rank,'weight6_time_kernel':len(z),'spin7_weight6_kernel_subtracted':16,'spin6_multiplicity':264,'spin6_time_rank':rhigh,'spin6_time_kernel_multiplicity':len(zhigh),'spin6_real_carrier_dim':264*13,'spin6_real_kernel_dim':len(zhigh)*13,'literal_highestweight_readout_rank':qrank,'literal_readout_real_rank':qrank*13,'literal_kernel_highestweight_readout_rank':qNrank,'literal_kernel_readout_real_rank':qNrank*13,'certificate':'exact Gaussian-rational receiver elimination'}

    certificate=run_spin6_constraints(root,C,E,Nh,h.conj,h.scale)
    candidates=json.loads((root/'lab/process/source-action-kappa1-constraints.json').read_text())['spin6_inverse_candidates']
    checked=[]
    for proved,original in zip(certificate['root_certificates'],candidates):
        blocks=[]
        for fresh,witness in zip(proved['blocks'],original['blocks']):
            blocks.append(dict(fresh,indices=witness['indices'],rational_inverse=witness['rational_inverse']))
        checked.append({'root':proved['root'],'blocks':blocks})
    transfer=certify_spin7_to_observed_spin6(C,E,h.add,h.scale,h.symbols,h.conj,Nh,h.bs,{'roots':checked})
    return {'spin6':result,'constraint_inverse':certificate,'readout_constraint_transfer':transfer,
            'spin7_observation':{'direct_readout_all_zero':True,'derivative_symbol_witnesses':spin7_witnesses,
             'scope':'Equation-symbol image only, not reduced evolution or propagated observed modes.'},
            'highest6_in_weight6':[{str(i):c.ser()for i,c in z.items()}for z in zraise],
            'time_kernel_in_highest6':[{str(i):c.ser()for i,c in z.items()}for z in zhigh]}



def run_spin6_constraints(root,C,E,Nh,conj,scale):
 """Rebuild actual spin6 matrix; validate supplied rational inverse candidates.

 The candidates originated in floating discovery. Acceptance uses only exact
 rational arithmetic, native all59 cubic coefficients and certified root balls.
 This function does not fit roots, add states or treat auxiliary signs as energy.
 """
 import json,hashlib
 from fractions import Fraction as Q
 data=json.loads((root/'lab/process/source-action-deep-coefficients.json').read_text())
 witness=json.loads((root/'lab/process/source-action-kappa1-constraints.json').read_text())['spin6_inverse_candidates']
 basis=[{(int(e),int(c)):Q(v)for e,c,v in row}for row in data['basis']]
 n=len(Nh);assert n==128 and len(basis)==59
 labels=sorted({e^c for b in basis for e,c in b})
 def reduce(x,p):
  for k in sorted(p,reverse=True):
   if x>>k&1:x^=p[k]
  return x
 p={}
 for x in labels:
  x=reduce(x,p)
  if x:p[x.bit_length()-1]=x
 assert len(p)==10
 cosets=[{reduce(e^c,p)for e,c in v}for v in Nh]
 assert all(len(s)==2 for s in cosets)
 # Necessary XOR condition screens pairs without inspecting any root values.
 pairs=[(i,j)for i in range(n)for j in range(i,n)if cosets[i]&cosets[j]]
 assert len(pairs)==2112
 gram=[[C(E.pair(conj(u),v))for v in Nh]for u in Nh]
 coeff={}
 for i,j in pairs:
  receiver=scale(2,E.N(conj(Nh[i]),Nh[j]))
  row=[C(E.pair(T,receiver))for T in basis]
  if i==j:assert all(not z.b for z in row)
  if any(row):coeff[i,j]=row;coeff[j,i]=[x.conj()for x in row]
 # Kernel pairing rank: full SO3 sector, not a selected nondegenerate minor.
 a=[row[:]for row in gram];rank=0
 for col in range(n):
  k=next((k for k in range(rank,n)if a[k][col]),None)
  if k is None:continue
  a[rank],a[k]=a[k],a[rank];z=a[rank][col]
  a[rank]=[x/z for x in a[rank]]
  for k in range(rank+1,n):
   if a[k][col]:
    z=a[k][col];a[k]=[x-z*y for x,y in zip(a[k],a[rank])]
  rank+=1
 assert rank==128
 adjacency={i:set()for i in range(n)}
 for i in range(n):
  for j in range(n):
   if gram[i][j]or(i,j)in coeff:adjacency[i].add(j);adjacency[j].add(i)
 components=[];seen=set()
 for i in range(n):
  if i in seen:continue
  todo=[i];component=[]
  while todo:
   z=todo.pop()
   if z in seen:continue
   seen.add(z);component.append(z);todo+=list(adjacency[z]-seen)
  components.append(sorted(component))
 assert list(map(len,components))==[32,32,32,32]
 def norm(z):z=C(z);return abs(z.a)+abs(z.b)
 def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 assert len(witness)==2 and len(data['certified_roots'])==2
 roots=[]
 for ri,root_data in enumerate(data['certified_roots']):
  assert Q(str(root_data['h']))==1 and witness[ri]['root']==ri
  x=list(map(Q,root_data['coordinates']));radius=Q(root_data['certificate']['radius'])
  blocks=[];wb=witness[ri]['blocks'];assert len(wb)==4
  for bi,comp in enumerate(components):
   m=len(comp);assert wb[bi]['component']==bi and wb[bi]['indices']==comp
   H=[[gram[i][j]+sum((a*b for a,b in zip(coeff.get((i,j),[]),x)),C())for j in comp]for i in comp]
   assert all(H[i][j]==H[j][i].conj()for i in range(m)for j in range(m))
   R=[[C(*z)for z in row]for row in wb[bi]['rational_inverse']]
   assert len(R)==m and all(len(row)==m for row in R)
   defect=max(sum(norm(sum((R[i][k]*H[k][j]for k in range(m)),C())-C(i==j))for j in range(m))for i in range(m))
   rnorm=max(sum(norm(z)for z in row)for row in R)
   cnorm=max(sum(sum(norm(z)for z in coeff.get((i,j),[]))for j in comp)for i in comp)
   eta=defect+rnorm*radius*cnorm
   assert eta<1,(ri,bi,'rootball inverse certificate failed',str(eta))
   blocks.append({'component':bi,'dimension':m,'status':'exact_rootball_invertibility_certified',
     'center_defect':str(defect),'inverse_norm_bound':str(rnorm),'coefficient_norm_bound':str(cnorm),
     'root_radius':str(radius),'neumann_bound':str(eta),'approximate_neumann_bound':float(eta),
     'matrix_center_sha256':digest([[z.ser()for z in row]for row in H]),
     'rational_inverse_sha256':digest([[z.ser()for z in row]for row in R])})
  roots.append({'root':ri,'all_certified':True,'blocks':blocks})
 # Inspect actual cubic order/factor independently of the efficient transpose.
 controls=0
 for (i,j),row in sorted(coeff.items()):
  if i>j:continue
  q=next(q for q,z in enumerate(row)if z)
  direct=C(E.pair(conj(Nh[i]),scale(2,E.N(basis[q],Nh[j]))))
  assert direct==row[q]and direct!=direct/2
  controls+=1
  if controls==4:break
 # Verify a nontrivial screened pair using the actual cubic algebra.
 i,j=next((i,j)for i in range(n)for j in range(i,n)if not cosets[i]&cosets[j])
 receiver=scale(2,E.N(conj(Nh[i]),Nh[j]))
 assert all(not E.pair(T,receiver)for T in basis)
 return {'multiplicity_kernel_dimension':128,'kernel_pairing_rank':rank,
   'real_rotation_spin6_kernel_dimension':1664,
   'candidate_pairs_before_screen':8256,'pairs_after_exact_xor_screen':len(pairs),
   'ordered_nonzero_affine_entries':len(coeff),'constraint_components':components,
   'coefficient_sha256':digest({f'{i},{j}':[z.ser()for z in row]for(i,j),row in sorted(coeff.items())}),
   'gram_sha256':digest([[z.ser()for z in row]for row in gram]),
   'root_certificates':roots,'direct_trilinear_controls':controls,'screened_pair_control':[i,j],
   'candidate_inverse_origin':'floating discovery rationalized to exact decimal fractions; origin supplies no acceptance claim',
   'acceptance':'exact rational center residual and all59 coefficient rootball Neumann bound <1, independently reconstructed',
   'scope':'Complete pointwise SO3-spin6 algebraic kernel sector, highest rotation sector with literal connection readout. No autonomous PDE, total inverse, positive energy, physical spin or GU verdict.'}

def certify_spin7_to_observed_spin6(C,E,add,scale,symbols,conj,N6,bs7,inverse_cert):
    """Exact readout response to one fixed native horizontal derivative source.

    The supplied inverse certificates must already be independently checked.
    N6 is the full128 multiplicity kernel and bs7 the complete36highest basis.
    This computes algebraic constraint response, not a propagated state.
    """
    from fractions import Fraction as Q
    norm=lambda v:abs(C(v).a)+abs(C(v).b)
    obs=lambda v:{k:x for k,x in v.items()if k[0]in(1,2,4,8)}
    tau=[Q(0)]*14;tau[3]=Q(1)
    xi=[Q(0)]*14;xi[0]=Q(1)
    v=symbols(E,tau,bs7[7])[0]
    assert v and not obs(v)
    source=symbols(E,xi,v)[0]
    b=[C(E.pair(conj(n),source))for n in N6]
    expected={18:C(-3145728),27:C(9437184),117:C(6291456)}
    assert {i:z for i,z in enumerate(b)if z}==expected
    Qcols=[obs(n)for n in N6]
    receiver=(1,1597)
    roots=[]
    for proof in inverse_cert['roots']:
        cs=[C()for _ in N6];errs=[Q(0)for _ in N6]
        for block in proof['blocks']:
            assert block['status']=='exact_rootball_invertibility_certified'
            comp=block['indices']
            R=[[C(*z)for z in row]for row in block['rational_inverse']]
            c0=[-sum((a*b[j]for a,j in zip(row,comp)),C())for row in R]
            eta=Q(block['neumann_bound']);assert 0<=eta<1
            error=eta/(1-eta)*max(map(norm,c0))
            for i,c in zip(comp,c0):cs[i]=c;errs[i]=error
        center=sum((c*q.get(receiver,0)for c,q in zip(cs,Qcols)),C())
        error=sum(norm(q.get(receiver,0))*er for q,er in zip(Qcols,errs))
        assert abs(center.a)>error
        assert (center.a>0)==(proof['root']==0)
        roots.append({'root':proof['root'],
            'status':'nonzero_readout_constraint_transfer_certified',
            'receiver':list(receiver),'component':'real',
            'center':str(center.a),'error_bound':str(error),
            'lower':str(center.a-error),'upper':str(center.a+error)})
    assert len(roots)==2
    return {'spin7_basis_index':7,'range_data':'K_dt b_7','horizontal_axis':0,
        'source_coefficients':[[i,z.ser()]for i,z in enumerate(b)if z],
        'roots':roots,
        'scope':'Actual algebraic constraint response to a specified derivative source; other data may compensate it. Not a propagated state, instability, particle count or generic confinement result.'}

def run(root):
 return {'structure':run_structure(root),'spin7':run_spin7(root),'spin6':run_spin6(root)}

if __name__=='__main__':
 parser=argparse.ArgumentParser()
 parser.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[2])
 parser.add_argument('--output',type=Path)
 args=parser.parse_args()
 result=run(args.repo)
 text=json.dumps(result,indent=2)+'\n'
 if args.output:args.output.write_text(text)
 else:print(text)
