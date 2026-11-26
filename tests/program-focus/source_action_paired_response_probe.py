"""Exact actual paired-current and fixed-domain audit.

One shared native context; finite and interval controls have distinct scopes.
The source-generated first shell is not a full invariant closure. The actual
weak integrated force and physical propagation are not computed by this probe.
"""
from fractions import Fraction as Q
import sys,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tests/program-focus'))
import source_action_deep_geometry as g
from source_action_deep_algebra import add,scale,Engine
from source_action_physical_probe import mul,gamma,components,contraction
from source_action_slice_completion_probe import inverse,sigma,inject,readout,covector,vadd,vscale,column
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
native_mul_original=mul
def mul(x,y):
 out={}
 for a,v in x.items():
  for b,w in y.items():
   c,q=E.cmul(a,b)
   out[c]=out.get(c,Q(0))+v*w*q
 return {c:v for c,v in out.items()if v}

def vertex_legacy(w,field):
 a=components(w);z,nu=field
 r=[add(*(scale(1/g.d[b],mul(gamma(b),add(mul(a[b],z[j]),scale(-1,mul(a[j],z[b])))))for b in range(14)),mul(a[j],nu))for j in range(14)]
 s=add(*(scale(1/g.d[j],mul(a[j],z[j]))for j in range(14)),*(scale(-Q(1,2)/g.d[j],mul(gamma(j),mul(a[j],nu)))for j in range(14)))
 return r,s

def prepare_vertex(w):
 a=components(w)
 slashA=add(*(scale(1/g.d[b],mul(gamma(b),a[b]))for b in range(14)))
 return a,slashA

def apply_vertex(prepared,field):
 a,slashA=prepared;z,nu=field
 r=[add(mul(slashA,z[j]),*(scale(-1/g.d[b],mul(gamma(b),mul(a[j],z[b])))for b in range(14)if z[b]),mul(a[j],nu))for j in range(14)]
 s=add(*(scale(1/g.d[j],mul(a[j],z[j]))for j in range(14)if z[j]),scale(-Q(1,2),mul(slashA,nu)))
 return r,s

def vertex(w,field):return apply_vertex(prepare_vertex(w),field)

def fast_vertex_controls():
 checks=0
 for a in [0,1,8,17,255,1024,8191,16383]:
  for b in [0,2,7,33,512,4095,8192,16383]:
   assert mul({a:Q(2,3)},{b:C(4,5)})==native_mul_original({a:Q(2,3)},{b:C(4,5)});checks+=1
 sample={k:v for k,v in basis()[0].items()}
 for w in [sample,{(1<<4,0):Q(2,3),(1<<3,17):Q(5,7)},spin_form()]:
  for j in range(15):
   v=column(j);assert vertex(w,v)==vertex_legacy(w,v);checks+=1
 u={k:C(v.a/Q(7),v.b/Q(11))for k,v in sample.items()}
 T={(1<<4,0):Q(5,13),(1<<3,17):Q(7,19)}
 assert center_full_R(u,T)==center_full_R_base(u,T);checks+=1
 return {'checks':checks,'cached_Clifford_matches_native':True,'collected_slash_vertex_matches_uncollected':True,'large_denominator_clearing_affine_identity':True}

def flat(cols):return {(i,j,c):C(v)for j,col in enumerate(cols)for i,x in enumerate(col)for c,v in x.items()if v}
def adj_sign(c):
 sign=(-1)**(c.bit_count()*(c.bit_count()-1)//2)
 for a in range(14):
  if c>>a&1 and g.d[a]<0:sign=-sign
 return sign

def adj(B):return {(j,i,c):C(v).conj()*adj_sign(c)for(i,j,c),v in B.items()}
def plus(A,B):return {k:C(A.get(k,0))+C(B.get(k,0))for k in A.keys()|B.keys()if C(A.get(k,0))+C(B.get(k,0))}
def herm(B):return {k:v/2 for k,v in plus(B,adj(B)).items()}
def jet(u,axis=3,zaxis=8,side='both'):
 tau=covector(3);nz=covector(zaxis);aa=covector(axis)
 out=[]
 for j in range(5):
  t1=sigma(aa,inverse(nz,vertex(u,inject(j))))
  t2=vertex(u,inverse(nz,sigma(aa,inject(j))))
  v=vadd(t1,vscale(-1,t2)) if side=='both' else (t1 if side=='row' else vscale(-1,t2))
  out.append(readout(inverse(tau,vscale(I,v))))
 return flat(out)

def basis():
 p={0:C(1)}
 for a,b in [(0,1),(10,12),(9,11),(5,8)]:p=E.cliff_product(p,{1<<a:C(1),1<<b:I})
 bs=[]
 for mask in range(64):
  z=[a for j,a in enumerate([2,3,4,6,7,13])if mask>>j&1]
  if (4+len(z))%4 not in (0,3):continue
  c=p
  for a in z:c=E.cliff_product(c,{1<<a:C(1)})
  u={(1<<a,k):f*v for a,f in [(5,C(1)),(8,I)]for k,v in c.items()}
  u=scale(1/u[min(u)],u);bs.append(u)
 return bs

class Ball:
 def __init__(self,c=0,e=0):
  if isinstance(c,Ball):self.c,self.e=c.c,c.e+Q(e)
  else:self.c,self.e=C(c),Q(e)
 def __add__(a,b):
  b=Ball(b);return Ball(a.c+b.c,a.e+b.e)
 __radd__=__add__
 def __neg__(a):return Ball(-a.c,a.e)
 def __sub__(a,b):return a+-Ball(b)
 def __rsub__(a,b):return Ball(b)+-a
 def __mul__(a,b):
  b=Ball(b);return Ball(a.c*b.c,cnorm(a.c)*b.e+cnorm(b.c)*a.e+a.e*b.e)
 __rmul__=__mul__
 def __truediv__(a,b):
  b=Ball(b);assert not b.e and not b.c.b and b.c.a
  return Ball(a.c/b.c,a.e/abs(b.c.a))
 def __bool__(a):return bool(a.c)or bool(a.e)
 def __eq__(a,b):
  b=Ball(b);return a.c==b.c and a.e==b.e

def cnorm(z):z=C(z);return abs(z.a)+abs(z.b)
def asball(u,err=None):return {k:Ball(v,(err or {}).get(k,0))for k,v in u.items()}
def spin_form():return {(1<<a,c):x for a,row in enumerate(g.spin)for c,x in row.items()}
def root_T(root,index):
 data=json.loads((Path(root)/'lab/process/source-action-deep-coefficients.json').read_text())
 witness=data['certified_roots'][index];radius=Q(witness['certificate']['radius']);out={}
 for coefficient,row in zip(witness['coordinates'],data['basis']):
  x=Ball(Q(coefficient),radius)
  for e,c,v in row:
   k=(int(e),int(c));out[k]=out.get(k,Ball())+x*Q(v)
 return out

_C0_PREPARED={}
def Czero(T,field):
 # Full Nomizu coordinate zeroth order at the origin, including the
 # covector-slot connection. d_A zeta is not a scalar-slot Dirac operator.
 key=id(T)
 if key not in _C0_PREPARED:_C0_PREPARED[key]=(T,prepare_vertex(add(spin_form(),T)))
 r,s=apply_vertex(_C0_PREPARED[key][1],field);z,nu=field
 correction=[]
 for j in range(14):
  terms=[]
  for a in range(14):
   for b,v in g.mbracket(a,j).items():
    terms.append(scale(-v/g.d[a],mul(gamma(a),z[b])))
  correction.append(add(*terms))
 scalar=add(*(scale(-g.Lambda[a][a][b]/g.d[a],z[b])for a in range(14)for b in range(14)if g.Lambda[a][a][b]))
 return vadd((r,s),(correction,scalar))

def full_jet(u,T,lam_k=None,lam_l=None,zaxis=8):
 # u and T may carry Ball coefficients. Constant coefficient u in the
 # homogeneous normal frame is B-parallel to first order at the origin.
 # This is one explicit member of the previously admitted lift family.
 lam_k=lam_k or [Q(0)]*4;lam_l=lam_l or lam_k
 tau=covector(3);nz=covector(zaxis)
 def P(lam,v):
  xi=list(map(Q,lam))+[Q(0)]*10
  return vadd(Czero(T,v),vscale(Ball(I),sigma(xi,v)))
 out=[]
 for j in range(5):
  UJ=vertex(u,inject(j));ZUJ=inverse(nz,UJ)
  term=vadd(P(lam_l,ZUJ),vscale(-1,vertex(u,inverse(nz,P(lam_k,inject(j))))))
  # Derivative of V(0,s)=q At(s)^-1, not a constant dual seed.
  # Vertical normal-coordinate coefficient derivatives vanish at origin.
  for sa in range(4,14):
   if sa==zaxis:continue
   atprime=[Q(g.A[sa-4][3][i])for i in range(4)]+[Q(0)]*10
   term=vadd(term,sigma(atprime,inverse(tau,sigma(covector(sa),ZUJ))))
  out.append(readout(inverse(tau,term)))
 return {(i,j,c):Ball(v)for j,col in enumerate(out)for i,x in enumerate(col)for c,v in x.items()if v}

def spectral_ball(u,lam,zaxis=8):
 tau=covector(3);nz=covector(zaxis);aa=list(map(Q,lam))+[Q(0)]*10;out=[]
 for j in range(5):
  t1=sigma(aa,inverse(nz,vertex(u,inject(j))))
  t2=vertex(u,inverse(nz,sigma(aa,inject(j))))
  out.append(readout(inverse(tau,vscale(Ball(I),vadd(t1,vscale(-1,t2))))))
 return {(i,j,c):Ball(v)for j,col in enumerate(out)for i,x in enumerate(col)for c,v in x.items()if v}

def root_report(B):
 from math import isqrt
 center={k:x.c for k,x in B.items()if x.c};errors={k:x.e for k,x in B.items()if x.e}
 H=herm(center)
 def weight(c):
  w=Q(1)
  for a in range(14):
   if c>>a&1:w*=abs(g.d[a])
  return w
 def hs2(A):return sum(weight(c)*(v.a*v.a+v.b*v.b)for(i,j,c),v in A.items())
 def sqbounds(q):
  q=Q(q);d=10**18;n=isqrt(q.numerator*d*d//q.denominator);lo=Q(n,d);hi=lo if lo*lo==q else Q(n+1,d);return lo,hi
 b2,h2=hs2(center),hs2(H);e2=sum(weight(k[2])*e*e for k,e in errors.items())
 blo,bhi=sqbounds(b2);hlo,hhi=sqbounds(h2);elo,ehi=sqbounds(e2)
 margin=2*hlo-bhi-3*ehi
 nonzero=[]
 for k,v in H.items():
  er=(errors.get(k,0)+errors.get((k[1],k[0],k[2]),0))/2
  if max(abs(v.a),abs(v.b))>er:nonzero.append((k,v,er))
 strongest=max(nonzero,key=lambda x:max(abs(x[1].a),abs(x[1].b))-x[2])if nonzero else None
 return {'terms':len(center),'hermitian_terms':len(H),'B_HS2':str(b2),'Herm_HS2':str(h2),'Herm_ratio':float(h2/b2)if b2 else None,'rootball_error_HS2':str(e2),'rootball_error_HS_upper':str(ehi),'gram_bound_half_robust':margin>0,'gram_robust_margin_lower':str(margin),'max_allowed_gram_deviation_lower':str((hlo-ehi)/(bhi+ehi))if bhi+ehi else None,'certified_Herm_coefficients':len(nonzero),'strongest':{'key':strongest[0],'center':strongest[1].ser(),'error':str(strongest[2])}if strongest else None}

def affine_gram_certificate(coeffs,global_hs_errors=None,real_split_certified=False):
 # Certify all real lambda at once, rather than choosing a new dispersion.
 from math import isqrt
 def weight(c):
  w=Q(1)
  for a in range(14):
   if c>>a&1:w*=abs(g.d[a])
  return w
 def inner(A,B):return sum(weight(k[2])*(v.conj()*B.get(k,C())).a for k,v in A.items())
 def upper(q):
  q=Q(q);d=10**18;n=isqrt(q.numerator*d*d//q.denominator)
  return Q(n,d)if Q(n,d)**2==q else Q(n+1,d)
 B=[{k:v.c for k,v in A.items()if v.c}for A in coeffs];H=[herm(A)for A in B]
 error=list(map(Q,global_hs_errors))if global_hs_errors is not None else [upper(sum(weight(k[2])*v.e*v.e for k,v in A.items()))for A in coeffs]
 # Positive diagonal congruence controls conditioning without changing PD.
 normalizers=[upper(inner(A,A))or Q(1)for A in B]
 B=[{k:v/normalizers[i]for k,v in A.items()}for i,A in enumerate(B)]
 H=[herm(A)for A in B];error=[e/n for e,n in zip(error,normalizers)]
 center_split=all(not v.b for v in B[0].values())and all(not v.a for A in B[1:]for v in A.values())
 if real_split_certified:assert center_split
 split=bool(real_split_certified)
 bn=[upper(inner(A,A))for A in B];hn=[upper(inner(A,A))for A in H]
 G=[[4*inner(H[i],H[j])-inner(B[i],B[j])for j in range(len(B))]for i in range(len(B))]
 radius=[[error[i]*(4*hn[j]+bn[j])+error[j]*(4*hn[i]+bn[i])+5*error[i]*error[j]for j in range(len(B))]for i in range(len(B))]
 if split:
  for j in range(1,len(B)):
   assert G[0][j]==G[j][0]==0
   radius[0][j]=radius[j][0]=Q(0)
 # Exact rational LDL, plus rigorous perturbation in spectral norm.
 n=len(G);L=[[Q(i==j)for j in range(n)]for i in range(n)];D=[]
 for i in range(n):
  d=G[i][i]-sum(L[i][k]**2*D[k]for k in range(i));D.append(d)
  if d<=0:return {'positive_definite':False,'LDL_pivots':list(map(str,D)),'G':[[str(x)for x in row]for row in G],'normalizers':list(map(str,normalizers)),'reason':'center matrix not positive definite; no all-frequency certificate'}
  for j in range(i+1,n):L[j][i]=(G[j][i]-sum(L[j][k]*L[i][k]*D[k]for k in range(i)))/d
 Linv=[[Q(i==j)for j in range(n)]for i in range(n)]
 for i in range(n):
  for j in range(i):Linv[i][j]=-sum(L[i][k]*Linv[k][j]for k in range(j,i))
 lower=min(D)/sum(x*x for row in Linv for x in row)
 perturb=max(sum(row)for row in radius)
 return {'positive_definite':lower>perturb,'center_positive_definite':True,'LDL_pivots':list(map(str,D)),'G':[[str(x)for x in row]for row in G],'normalizers':list(map(str,normalizers)),'real_imag_cross_error_exactly_zero':split,'real_split_premise':'Exact root coordinates, realified u and geometric C0 are real; spectral coefficients have exactly one i. Actual perturbations preserve this split.'if split else None,'lambda_min_lower':str(lower),'root_perturbation_norm_upper':str(perturb),'strict_margin':str(lower-perturb),'affine_order':['constant','x0','x1','x2','time'],'claim':'When positive definite, all actual real frequency points survive every existing normalized Gram deviation norm<1/2; no new support or dispersion chosen.'}

def center_full_R_base(u,T,zaxis=8):
 tau=covector(3);nz=covector(zaxis);out=[]
 for j in range(5):
  UJ=vertex(u,inject(j));ZUJ=inverse(nz,UJ)
  term=vadd(Czero(T,ZUJ),vscale(-1,vertex(u,inverse(nz,Czero(T,inject(j))))))
  for sa in range(4,14):
   if sa==zaxis:continue
   atprime=[Q(g.A[sa-4][3][i])for i in range(4)]+[Q(0)]*10
   term=vadd(term,sigma(atprime,inverse(tau,sigma(covector(sa),ZUJ))))
  out.append(readout(inverse(tau,term)))
 return flat(out)

def cleared_coefficients(form):
 from math import lcm
 denominator=1
 for value in form.values():
  value=C(value);denominator=lcm(denominator,value.a.denominator,value.b.denominator)
 integer={k:C(C(v).a*denominator,C(v).b*denominator)for k,v in form.items()}
 assert all(v.a.denominator==v.b.denominator==1 for v in integer.values())
 return integer,denominator

def center_full_R(u,T,zaxis=8):
 # R is linear in u and affine in T. Clear their large common exact
 # denominators before the dense Clifford products; divide only at return.
 U,du=cleared_coefficients(u);Tinteger,dt=cleared_coefficients(T)
 if du==dt==1:return center_full_R_base(U,Tinteger,zaxis)
 if not Tinteger:
  reference=center_full_R_base(U,{},zaxis)
  return {k:C(v.a/du,v.b/du)for k,v in reference.items()}
 reference=center_full_R_base(U,{},zaxis)
 dense=center_full_R_base(U,Tinteger,zaxis)
 numerator=add(dense,scale(dt-1,reference));denominator=du*dt
 return {k:C(v.a/denominator,v.b/denominator)for k,v in numerator.items()if v}

def global_error_report(center,error):
 from math import isqrt
 def weight(c):
  w=Q(1)
  for a in range(14):
   if c>>a&1:w*=abs(g.d[a])
  return w
 def hs2(A):return sum(weight(c)*(v.a*v.a+v.b*v.b)for(i,j,c),v in A.items())
 def sqbounds(q):
  q=Q(q);d=10**18;n=isqrt(q.numerator*d*d//q.denominator);lo=Q(n,d);hi=lo if lo*lo==q else Q(n+1,d);return lo,hi
 H=herm(center);b2,h2=hs2(center),hs2(H);blo,bhi=sqbounds(b2);hlo,hhi=sqbounds(h2);error=Q(error)
 return {'terms':len(center),'hermitian_terms':len(H),'B_HS2':str(b2),'Herm_HS2':str(h2),'Herm_ratio':float(h2/b2)if b2 else None,'rootball_error_HS_upper':str(error),'gram_bound_half_robust':2*hlo-bhi-3*error>0,'gram_robust_margin_lower':str(2*hlo-bhi-3*error),'max_allowed_gram_deviation_lower':str((hlo-error)/(bhi+error))if bhi+error else None,'Herm_nonzero_certified':hlo>error,'error_method':'global submultiplicative Clifford/block operator norm, normalized HS sqrt5 bound'}

def tangent_controls(ctx,zaxis=8):
 tau=covector(3);tests=0;forms=ctx['h'].bs+ctx['h'].N
 for u in forms:
  assert not contraction(components(u),range(14))
  assert not any(e in (1,2,4,8)for e,c in u)
  for j in range(5):
   image=inverse(tau,vertex(u,inject(j)))
   for sa in range(4,14):
    if sa==zaxis:continue
    atprime=[Q(g.A[sa-4][3][i])for i in range(4)]+[Q(0)]*10
    result=readout(inverse(tau,sigma(atprime,image)))
    assert not any(result),(sa,j)
    tests+=1
 return {'normal_solving_axis':zaxis,'normal_tangent_axes':[i for i in range(4,14)if i!=zaxis],'complex_forms_tested':len(forms),'all_five_observed_columns':True,'exact_zero_checks':tests,'scope':'Actual first normal derivatives tangent to constant-seed CK hypersurface vanish on normal gamma-traceless forms; realifications follow by complex linearity. This is not an all-jet statement.'}

from math import isqrt

def rational_sqrt_upper(q):
 q=Q(q);d=10**18;n=isqrt(q.numerator*d*d//q.denominator)
 return Q(n,d)if Q(n,d)**2==q else Q(n+1,d)

def blade_op_weight(c):
 out=Q(1)
 for a in range(14):
  if c>>a&1:
   n=isqrt(abs(g.d[a].numerator));assert g.d[a].denominator==1
   out*=n if n*n==abs(g.d[a])else n+1
 return out

def cliff_l1_op(v):return sum(cnorm(x)*blade_op_weight(c)for c,x in v.items())

def block_bound(blocks):
 rows=max(sum(r)for r in blocks)
 cols=max(sum(r[j]for r in blocks)for j in range(len(blocks[0])))
 return rational_sqrt_upper(rows*cols)

def linear_op_bound(fn,out_slots=15):
 # Clifford coefficient one in each full rolled-field slot.
 cols=[]
 for j in range(15):
  image=fn(column(j))
  if out_slots==15:image=image[0]+[image[1]]
  cols.append([cliff_l1_op(v)for v in image])
 return block_bound([list(row)for row in zip(*cols)])

def connection_component_norms(u):
 norms=[Q(0)]*14
 for(e,c),v in u.items():norms[e.bit_length()-1]+=cnorm(v)*blade_op_weight(c)
 return norms

def vertex_norm_from_component_norms(t):
 a=[blade_op_weight(1<<j)/abs(g.d[j])for j in range(14)]
 slash=sum(x*y for x,y in zip(a,t));M=[[Q(0)]*15 for _ in range(15)]
 for j in range(14):
  for k in range(14):M[j][k]=(slash if j==k else 0)+a[k]*t[j]
  M[j][14]=t[j];M[14][j]=t[j]/abs(g.d[j])
 M[14][14]=slash/2
 return block_bound(M)

def fixed_jet_norm_bounds(zaxis=8):
 tau=covector(3);nz=covector(zaxis)
 q=linear_op_bound(lambda v:readout(inverse(tau,v)),5)
 z=linear_op_bound(lambda v:inverse(nz,v))
 atinv=linear_op_bound(lambda v:inverse(tau,v))
 axes=[linear_op_bound(lambda v,a=a:sigma(covector(a),v))for a in range(14)]
 S=Q(0)
 for sa in range(4,14):
  if sa==zaxis:continue
  atprime=[Q(g.A[sa-4][3][i])for i in range(4)]+[Q(0)]*10
  S+=linear_op_bound(lambda v:sigma(atprime,v))*atinv*axes[sa]
 bg=linear_op_bound(lambda v:Czero({},v))
 return {'Q':q,'Z':z,'C_background':bg,'row_seed_factor':S,'axes':axes}

def full_jet_error_bounds(Tcenter,Terrors,ucenter,uerrors,fixed):
 t=vertex_norm_from_component_norms(connection_component_norms(Tcenter))
 dt=vertex_norm_from_component_norms(connection_component_norms(Terrors))
 u=vertex_norm_from_component_norms(connection_component_norms(ucenter))
 du=vertex_norm_from_component_norms(connection_component_norms(uerrors))
 c=fixed['C_background']+t;q=fixed['Q'];z=fixed['Z']
 # 5 visible output slots; normalized HS divides ordinary trace by128.
 # sqrt(640)/sqrt(128)=sqrt5 <9/4.
 hs=Q(9,4)
 rerr=hs*q*z*(2*(dt*u+c*du+dt*du)+fixed['row_seed_factor']*du)
 serr=[hs*2*q*z*fixed['axes'][a]*du for a in range(4)]
 return {'constant':rerr,'spectral':serr,'operator_bounds':{'q':q,'z':z,'c':c,'dc':dt,'u':u,'du':du}}

def fast_error_control(fixed):
 # Tiny independent Ball replay, including actual reference lower terms.
 # It is a norm-bound control, not a kappa-root evaluation.
 u0={k:C(v.a)for k,v in basis()[0].items()if v.a}
 keys=list(u0);du={keys[0]:Q(1,10**9)};T={(1<<4,0):Q(1,3)};dT={(1<<4,0):Q(1,10**8)}
 UB={k:Ball(v,du.get(k,0))for k,v in u0.items()}
 TB={k:Ball(v,dT.get(k,0))for k,v in T.items()}
 interval=full_jet(UB,TB,[0,0,0,0]);center=center_full_R(u0,T)
 assert {k:v.c for k,v in interval.items()if v.c}==center
 e2=Q(0)
 for(i,j,c),v in interval.items():
  weight=Q(1)
  for a in range(14):
   if c>>a&1:weight*=abs(g.d[a])
  e2+=weight*v.e*v.e
 bound=full_jet_error_bounds(T,dT,u0,du,fixed)['constant']
 assert bound*bound>=e2
 return {'center_matches_interval':True,'global_HS_bound':str(bound),'old_coefficient_interval_HS2':str(e2),'global_bound_dominates':True,'scope':'Tiny full-reference operator control, not a root or propagation certificate.'}


def run_paired_jet(root,ctx):
 global C,I,E
 C=ctx['C'];I=C(0,1);E=ctx['E'];h=ctx['h']
 old=json.loads((Path(root)/'lab/process/source-action-receiver-strategy.json').read_text())['exact_probe']['normal_energy']
 inv=json.loads((Path(root)/'lab/process/source-action-reduced-evolution.json').read_text())['spin7_inverse_candidates']
 prior=json.loads((Path(root)/'lab/process/source-action-kappa1-constraints.json').read_text())['exact_probe']['spin7']
 import hashlib
 def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 assert digest([[C(x).ser()for x in row]for row in ctx['G7']])==prior['kernel_gram_sha256']
 for ri,p in enumerate(inv):
  assert digest(p['inverse'])==prior['root_certificates'][ri]['inverse_sha256']
  assert p['neumann_bound']==prior['root_certificates'][ri]['neumann_bound'] and Q(p['neumann_bound'])<1
 # Establish nonzero real paired spectral coefficients on every supplied
 # realification, no lower/root terms substituted for them.
 principal=[]
 for bi,b in enumerate(h.bs):
  for part in ('a','b'):
   u={k:getattr(C(v),part)for k,v in b.items()if getattr(C(v),part)}
   for a in range(4):
    B=jet(u,a);H=herm(B)
    principal.append({'basis':bi,'part':part,'axis':a,'raw_terms':len(B),'Herm_terms':len(H)})
 fast_controls=fast_vertex_controls();fixed=fixed_jet_norm_bounds();control=fast_error_control(fixed);roots=[]
 for ri in range(2):
  row=next(x for x in old['roots'][ri]['rows']if x['axis']==4 and x['sign']=='negative')
  source=[C()for _ in h.N]
  for j,z in row['source_coordinates']:source[j]=C(*z)
  R=[[C(*z)for z in rr]for rr in inv[ri]['inverse']]
  coeff=[-sum((a*b for a,b in zip(rr,source)),C())for rr in R]
  eta=Q(inv[ri]['neumann_bound']);error=eta/(1-eta)*max(map(cnorm,coeff))
  energy=sum((b.conj()*c for b,c in zip(source,coeff)),C())
  energy_error=error*sum(map(cnorm,source))+abs(energy.b)
  assert energy.a+energy_error<0
  n={}
  for a,v in zip(coeff,h.N):
   for k,b in v.items():n[k]=n.get(k,Ball())+Ball(a,error)*Ball(b)
  Tball=root_T(root,ri);T={k:v.c for k,v in Tball.items()if v.c};Terrors={k:v.e for k,v in Tball.items()if v.e}
  ncenter={k:v.c for k,v in n.items()if v.c};nerrors={k:v.e for k,v in n.items()if v.e}
  print('paired center full R start root',ri,flush=True)
  Rcomplex=center_full_R(ncenter,T)
  print('paired center full R complete root',ri,'terms',len(Rcomplex),flush=True)
  for part in ('a','b'):
   u={k:C(getattr(v,part))for k,v in ncenter.items()if getattr(v,part)}
   # These are fixed spectral-point controls; their membership in the
   # actually held K/omega remains an explicit applicability premise.
   points=[];B0={k:C(getattr(v,part))for k,v in Rcomplex.items()if getattr(v,part)}
   affine_centers=[B0]+[jet(u,a)for a in range(4)]
   affine=[{k:Ball(v)for k,v in B.items()}for B in affine_centers]
   norms=full_jet_error_bounds(T,Terrors,u,nerrors,fixed)
   errors=[norms['constant']]+norms['spectral']
   for name,lam in [('zero_frequency',[0,0,0,0]),('unit_frequency_at_zero_spatial',[0,0,0,-1]),('unit_time_and_x0',[1,0,0,-1])]:
    B=add(B0,*(scale(lam[a],affine_centers[a+1])for a in range(4)))
    err=errors[0]+sum(abs(lam[a])*errors[a+1]for a in range(4))
    points.append({'name':name,'lambda_covector_order_x0_x1_x2_t':lam,'report':global_error_report(B,err)})
   roots.append({'root':ri,'normal_energy_axis':4,'range_basis_index':row['range_basis_index'],'realification':part,'coefficient_error':str(error),'certified_each_real_energy_center':str(energy.a/2),'certified_each_real_energy_error':str(energy_error/2),'points':points,'global_HS_coefficient_errors':list(map(str,errors)),'operator_error_bounds':{k:str(v)for k,v in norms['operator_bounds'].items()},'all_frequency_gram':affine_gram_certificate(affine,errors,real_split_certified=True)})
 return {'spectral_coefficients':principal,'normal_negative_response_full_jet':roots,'tangential_normal_zeros':tangent_controls(ctx),'global_error_control':control,'fast_vertex_controls':fast_controls,'scope':'Actual homogeneous normal-chart first jet with both CK legs and real current; isolated spectral controls require held support membership, while a passing all-frequency Gram certificate needs no added spectral premise. Negative energy uses theta4 and the opened current derivative uses theta8: amplitude access is not matching normal-wavecovector support or negative forced-response energy. No coupled propagation/physical ghost.'}


"""Root-serialized actual lower-source and missing-block diagnostics.

Call run(root, ctx) with the one shared native build_context. No native writes.
"""
from fractions import Fraction as Q
from pathlib import Path
import json, hashlib

def run_weak_sources(root, ctx):
    root=Path(root)
    C,E,h=ctx['C'],ctx['E'],ctx['h']
    import source_action_deep_geometry as g
    from source_action_deep_algebra import add,scale
    from source_action_metric_symbol_probe import symbols
    from functools import lru_cache
    def cov(a):
        x=[Q(0)]*14;x[a]=Q(1);return x
    def K(a,v):return symbols(E,cov(a),v)[0]
    def ser(v):return [[e,c,C(x).ser()]for(e,c),x in sorted(v.items())]
    def digest(v):return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    def rref(a):
        a=[[C(x)for x in row]for row in a];piv=[];row=0
        for col in range(len(a[0])):
            k=next((k for k in range(row,len(a))if a[k][col]),None)
            if k is None:continue
            a[k],a[row]=a[row],a[k];s=a[row][col];a[row]=[x/s for x in a[row]]
            for k in range(len(a)):
                if k!=row and a[k][col]:
                    s=a[k][col];a[k]=[x-s*y for x,y in zip(a[k],a[row])]
            piv.append(col);row+=1
            if row==len(a):break
        return a,piv
    def inv(a):
        n=len(a);b,p=rref([row+[C(i==j)for j in range(n)]for i,row in enumerate(a)])
        assert p==list(range(n));return [row[n:]for row in b]
    @lru_cache(maxsize=256)
    def block(r):
        bs=[(1<<i,(1<<i)^r^z)for z in (0,8)for i in range(14)]
        columns=[K(3,{k:Q(1)})for k in bs]
        assert all(set(c)<=set(bs)for c in columns)
        a=[[c.get(k,0)for c in columns]for k in bs]
        rr,piv=rref(a);zs=[]
        for j in range(28):
            if j in piv:continue
            z=[C()for _ in range(28)];z[j]=C(1)
            for i,c in enumerate(piv):z[c]=-rr[i][j]
            zs.append({bs[i]:x for i,x in enumerate(z)if x})
        gram=[[E.pair(u,v)for v in zs]for u in zs]
        return zs,inv(gram)
    def P(v):
        groups={}
        for(e,c),x in v.items():groups.setdefault((e^c)&~8,{})[(e,c)]=x
        out={}
        for r,w in groups.items():
            zs,gi=block(r);b=[E.pair(z,w)for z in zs]
            coeff=[sum((x*y for x,y in zip(row,b)),C())for row in gi]
            out=add(out,*(scale(a,z)for a,z in zip(coeff,zs)))
        return out
    def cas(v):return scale(-1,add(*(h.rot(a,b,h.rot(a,b,v))for a,b in [(0,1),(0,2),(1,2)])))
    def cm(v,l):return add(cas(v),scale(-l*(l+1),v))
    def spin5(v):
        # spin2 tensor spin7 and no carrier above7: only5,6,7.
        return scale(Q(1,312),cm(cm(v,6),7))
    def high7(v):
        piv=[min(b)for b in h.bs]
        co=[C(v.get(k,0))for k in piv]
        assert v==add(*(scale(c,b)for c,b in zip(co,h.bs)if c))
        return co
    rows=[]
    for index in (5,12):
        V=K(3,h.bs[index]);assert not P(V)
        high7(V)
        # The full Nomizu first-order lower part includes connection, frame,
        # and divergence/density terms through Engine.K=D/Phi+Dad/Phiadj.
        kv=E.K(V);high7(kv)
        dlow=P(add(kv,V));high7(dlow)
        assert not K(3,dlow)
        row={'range_basis_index':index,'range_terms':len(V),
             'nomizu_lower_terms':len(kv),'nomizu_lower_sha256':digest(ser(kv)),
             'reference_lower_source_terms':len(dlow),'reference_lower_source_sha256':digest(ser(dlow)),
             'normal_sources':[]}
        for axis in (0,4,5,7,8):
            F=K(axis,V);pf=P(F)
            assert not K(3,pf)
            w=spin5(pf)
            if w:
                assert not cm(w,5)
                assert P(w)==w and not K(3,w)
            row['normal_sources'].append({'axis':axis,'full_source_terms':len(F),'kernel_source_terms':len(pf),
                'kernel_source_sha256':digest(ser(pf)),'spin5_terms':len(w),'spin5_sha256':digest(ser(w)),
                'spin5_witness':ser(w)[:3]})
        rows.append(row)
    # Actual lower displacement is affine in the same59 owned coefficients.
    # Covariant SO3 maps preserve highest7; test every coefficient without
    # using approximate roots or asserting their inverse is globally regular.
    data=json.loads((root/'lab/process/source-action-deep-coefficients.json').read_text())
    basis=[{(int(e),int(c)):Q(v)for e,c,v in b}for b in data['basis']]
    lower=[]
    for index in (5,12):
        V=K(3,h.bs[index]);cols=[]
        for j,T in enumerate(basis):
            f=scale(2,E.N(T,V));high7(f)
            pf=P(f);high7(pf)
            cols.append({'background_basis':j,'terms':len(pf),'sha256':digest(ser(pf))})
        lower.append({'range_basis_index':index,'all59_full_lower_sources_highest7':True,'columns':cols})
    return {'scope':'Complete pointwise lower-source projection and normal spin5 demand, not integrated weak current or actual propagated response.',
            'range_lift_projector_derivative':'dR(V) lies in N and P K^a P=0; projected lift derivatives vanish. Reference lower terms are retained by Engine.K.',
            'reference_and_normal_sources':rows,'displacement_lower_sources':lower,
            'next_required_object':'Projected spin5 auxiliary M_N restriction and actual normal paired-current divergence; higher normal covectors cannot generically be replaced by horizontal-only inverse.'}


"""Root-serialized actual lower-source and missing-block diagnostics.

Call run(root, ctx) with the one shared native build_context. No native writes.
"""
from fractions import Fraction as Q
from pathlib import Path
import json, hashlib

def build_api(root, ctx):
    root=Path(root)
    C,E,h=ctx['C'],ctx['E'],ctx['h']
    import source_action_deep_geometry as g
    from source_action_deep_algebra import add,scale
    from source_action_metric_symbol_probe import symbols
    from functools import lru_cache
    def cov(a):
        x=[Q(0)]*14;x[a]=Q(1);return x
    def K(a,v):return symbols(E,cov(a),v)[0]
    def ser(v):return [[e,c,C(x).ser()]for(e,c),x in sorted(v.items())]
    def digest(v):return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    def rref(a):
        a=[[C(x)for x in row]for row in a];piv=[];row=0
        for col in range(len(a[0])):
            k=next((k for k in range(row,len(a))if a[k][col]),None)
            if k is None:continue
            a[k],a[row]=a[row],a[k];s=a[row][col];a[row]=[x/s for x in a[row]]
            for k in range(len(a)):
                if k!=row and a[k][col]:
                    s=a[k][col];a[k]=[x-s*y for x,y in zip(a[k],a[row])]
            piv.append(col);row+=1
            if row==len(a):break
        return a,piv
    def inv(a):
        n=len(a);b,p=rref([row+[C(i==j)for j in range(n)]for i,row in enumerate(a)])
        assert p==list(range(n));return [row[n:]for row in b]
    def qrref(a):
        # K_dt and every XOR-block Gram are real rational, even though the
        # supplied highest-weight fields are complex. Avoid gratuitous C work.
        a=[[Q(x)for x in row]for row in a];piv=[];row=0
        for col in range(len(a[0])):
            k=next((k for k in range(row,len(a))if a[k][col]),None)
            if k is None:continue
            a[k],a[row]=a[row],a[k];s=a[row][col];a[row]=[x/s for x in a[row]]
            for k in range(len(a)):
                if k!=row and a[k][col]:
                    s=a[k][col];a[k]=[x-s*y for x,y in zip(a[k],a[row])]
            piv.append(col);row+=1
            if row==len(a):break
        return a,piv
    @lru_cache(maxsize=None)
    def block(r):
        bs=[(1<<i,(1<<i)^r^z)for z in (0,8)for i in range(14)]
        columns=[K(3,{k:Q(1)})for k in bs]
        assert all(set(c)<=set(bs)for c in columns)
        a=[[c.get(k,0)for c in columns]for k in bs]
        rr,piv=qrref(a);zs=[]
        for j in range(28):
            if j in piv:continue
            z=[Q(0)]*28;z[j]=Q(1)
            for i,c in enumerate(piv):z[c]=-rr[i][j]
            zs.append({bs[i]:x for i,x in enumerate(z)if x})
        gram=[[E.pair(u,v)for v in zs]for u in zs]
        n=len(gram)
        gi,gp=qrref([row+[Q(i==j)for j in range(n)]for i,row in enumerate(gram)])
        assert gp==list(range(n))
        return zs,[row[n:]for row in gi]
    def P(v):
        groups={}
        for(e,c),x in v.items():groups.setdefault((e^c)&~8,{})[(e,c)]=x
        out={}
        for r,w in groups.items():
            zs,gi=block(r);b=[E.pair(z,w)for z in zs]
            coeff=[sum((x*y for x,y in zip(row,b)),C())for row in gi]
            out=add(out,*(scale(a,z)for a,z in zip(coeff,zs)))
        return out
    def cas(v):return scale(-1,add(*(h.rot(a,b,h.rot(a,b,v))for a,b in [(0,1),(0,2),(1,2)])))
    def cm(v,l):return add(cas(v),scale(-l*(l+1),v))
    def spin5(v):
        # spin2 tensor spin7 and no carrier above7: only5,6,7.
        return scale(Q(1,312),cm(cm(v,6),7))
    def high7(v):
        piv=[min(b)for b in h.bs]
        co=[C(v.get(k,0))for k in piv]
        assert v==add(*(scale(c,b)for c,b in zip(co,h.bs)if c))
        return co
    return locals()

def run_first_shell(root,ctx,return_work=False):
    q=build_api(root,ctx)
    C,E,h,P,K,spin5,ser,digest=(q[k]for k in ('C','E','h','P','K','spin5','ser','digest'))
    from source_action_deep_algebra import add,scale
    def norm(x):x=C(x);return abs(x.a)+abs(x.b)
    def sparse_basis(vectors):
        basis=[];piv=[];expressions=[]
        def reduce(v):
            coeff=[]
            for p,b in zip(piv,basis):
                c=C(v.get(p,0));coeff.append(c)
                if c:v=add(v,scale(-c,b))
            return v,coeff
        for v in vectors:
            remainder,coeff=reduce(v)
            if remainder:
                p=min(remainder);c=remainder[p];piv.append(p);basis.append(scale(1/c,remainder));coeff.append(c)
            assert add(*(scale(c,b)for c,b in zip(coeff,basis)if c))==v
            expressions.append(coeff)
        return basis,piv,reduce,expressions
    seeds=[spin5(P(K(5,K(3,h.bs[index]))))for index in (5,12)]
    assert all(seeds)
    for i,index in enumerate((5,12)):
        x=spin5(P(K(8,K(3,h.bs[index]))))
        assert x==scale(h.I,seeds[i])
    sb,sp,remainder,sc=sparse_basis(seeds);assert len(sb)==2
    data=json.loads((Path(root)/'lab/process/source-action-deep-coefficients.json').read_text())
    Ts=[{(int(e),int(c)):Q(v)for e,c,v in row}for row in data['basis']]
    images=[];labels=[];outside=[]
    for i,s in enumerate(seeds):
        for j,T in enumerate(Ts):
            w=P(scale(2,E.N(T,s)))
            # M preserves the entire highest5 kernel, not necessarily these seeds.
            assert not K(3,w)
            assert q['cas'](w)==scale(30,w)
            assert h.rot(0,1,w)==scale(5*h.I,w)
            assert not add(h.rot(0,2,w),scale(h.I,h.rot(1,2,w)))
            images.append(w);labels.append([i,j]);r,_=remainder(w);outside.append(r)
            if j%8==7 or j==58:
                print('spin5 first shell',i,j+1,'of59','P-cache',q['block'].cache_info(),flush=True)
    shell,piv,red,exp=sparse_basis(seeds+images)
    rootrows=[]
    for ri,rootdata in enumerate(data['certified_roots']):
        co=list(map(Q,rootdata['coordinates']));radius=Q(rootdata['certificate']['radius']);rows=[]
        for i in range(2):
            columns=outside[i*59:(i+1)*59]
            r=add(*(scale(c,w)for c,w in zip(co,columns)if c))
            err={k:radius*sum(norm(w.get(k,0))for w in columns)for k in set().union(*(set(w)for w in columns))}
            # Choose a real/imag coefficient strictly separated over whole root ball.
            witnesses=[]
            for k,z in r.items():
                z=C(z)
                for part in ('a','b'):
                    v=getattr(z,part);e=err.get(k,Q(0))
                    if abs(v)>e:witnesses.append((abs(v)-e,k,part,v,e))
            best=max(witnesses)if witnesses else None
            rows.append({'seed':i,'rational_center_outside_terms':len(r),
                'rootball_seed_span_not_invariant':bool(best),
                'witness':None if best is None else {'key':list(best[1]),'part':best[2],
                    'center':str(best[3]),'error_bound':str(best[4]),'strict_margin':str(best[0])}})
        rootrows.append({'root':ri,'seeds':rows})
    result={'initial_source_dimension':2,'coefficient_maps':59,'images_tested':118,
        'dimension_field':'Complex Gaussian-rational highest-weight multiplicity; not a physical state count or full real spin5 carrier dimension.',
        'first_source_generated_shell_dimension':len(shell),
        'first_shell_basis_sha256':digest([ser(v)for v in shell]),
        'image_sha256':digest([ser(v)for v in images]),
        'all_images_highest_spin5_time_kernel':True,
        'normal_axis8_equals_i_axis5':True,'roots':rootrows,
        'scope':'Exact first affine-family closure shell, not the smallest invariant closure or full spin5 inverse. Actual-root nonclosure is certified over existing root balls. No physical response or extra choice.'}

    return (result,seeds,images) if return_work else result


"""Tiny root-only seed/current annihilator discriminator; no inverse."""
from fractions import Fraction as Q
from pathlib import Path
import json,hashlib

def run_spin5_current(root,ctx,seeds,images,pair_helpers):
    h=pair_helpers
    if isinstance(h,dict):
        from types import SimpleNamespace
        h=SimpleNamespace(**h)
    assert len(seeds)==2 and len(images)>=59
    C=h.C
    def convert(v):return {k:C(x.a,x.b) if hasattr(x,'a') else C(x)for k,x in v.items()}
    def serial(B):return [[i,j,c,C(z).ser()]for(i,j,c),z in sorted(B.items())]
    def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    def receiver(w):
        W,den=h.cleared_coefficients(convert(w));prepared=h.prepare_vertex(W)
        cols=[h.readout(h.inverse(h.covector(3),h.apply_vertex(prepared,h.inject(j))))for j in range(5)]
        B=h.flat(cols)
        return {k:C(z)/den for k,z in B.items()if z}
    def asreport(B,errors,part):
        real={k:C(getattr(C(v),part))for k,v in B.items()if getattr(C(v),part)}
        balls={k:h.Ball(real.get(k,C()),errors.get(k,Q(0)))for k in real.keys()|errors.keys()}
        report=h.root_report(balls)
        report['raw_matrix_sha256']=digest(serial(real))
        report['physical_current']='minus Herm(N^-1 B), from physical imaginary connection variation and inherited +i dual phase'
        return report
    assert receiver({(8,0):Q(1)})=={(j,j,0):C(1)for j in range(5)}
    bseed=receiver(seeds[0])
    # all59 images here are P 2N(T_j,seed0) in original coefficient order.
    bm=[receiver(w)for w in images[:59]]
    data=json.loads((Path(root)/'lab/process/source-action-deep-coefficients.json').read_text())
    roots=[]
    for ri,r in enumerate(data['certified_roots']):
        xs=list(map(Q,r['coordinates']));radius=Q(r['certificate']['radius'])
        B=dict(bseed)
        for x,b in zip(xs,bm):
            for k,z in b.items():B[k]=B.get(k,C())+x*z
        B={k:v for k,v in B.items()if v}
        parts={}
        for part in ('a','b'):
            keys=set().union(*(set(b)for b in bm))
            err={k:radius*sum(abs(getattr(C(b.get(k,0)),part))for b in bm)for k in keys}
            err={k:v for k,v in err.items()if v}
            parts[part]=asreport(B,err,part)
        roots.append({'root':ri,'test':'M(root) seed0 = seed0 + sum x_j P2N(T_j,seed0)','realifications':parts})
    return {'seed0_realifications':{part:asreport(bseed,{},part)for part in ('a','b')},
            'affine_image_current_sha256':digest([serial(b)for b in bm]),
            'affine_images_tested':59,'roots':roots,
            'scope':'Current on reached spin5 source and its actual-M image only. A Gram-robust nonzero excludes the easy claim that current annihilates the whole reached spin5 module. It is not current on M^-1 source, the full weak scalar, physical forced energy or propagation. Dimensions are not physical state counts.'}


"""Exact native/finite controls for the fixed CK domain Lorentz audit.

No CK solve, large native inverse or local build is run.  Geometry is the
existing rational normal isotropy representation; seed-jet and norm arguments
are written theorems whose finite algebra is guarded here.
"""
from fractions import Fraction as Q
from pathlib import Path
import sys
import json

def run_lorentz(root):
    sys.path.insert(0, str(Path(root)/'tests/program-focus'))
    import source_action_deep_geometry as geo
    import source_action_slice_completion_probe as s
    from source_action_deep_algebra import add, scale
    controls=[]
    rows=[]
    for j,other in [(0,12),(1,10)]:
        H=geo.zero();H[j][3]=H[3][j]=Q(1)
        a=geo.h_action(H,8);b=geo.h_action(H,other)
        assert a=={other:Q(-1)} and b=={8:Q(-1)}
        rows.append({'boost_spatial_axis':j,'normal_axis':8,'tangent_axis':other,
                     'K_e8':{str(k):str(v) for k,v in a.items()},
                     'K_tangent':{str(k):str(v) for k,v in b.items()}})
        controls.append('native_hyperplane_mixing_'+str(j))
    H=geo.zero();H[2][3]=H[3][2]=Q(1)
    assert geo.h_action(H,8)=={}
    controls.append('boost2_preserves_axis8_at_first_order_control')

    # Entire horizontal-covector source map is injective on scalar input:
    # sigma(delta_lambda) I_scalar has first four slots exactly delta_lambda.
    # This coefficient identity is independent of the background lower C.
    for mu in range(4):
        xi=s.covector(mu)
        col=s.sigma(xi,s.inject(4))
        for nu in range(4):
            assert col[0][nu]==({0:Q(1)} if nu==mu else {})
        assert s.sigma(s.covector(8),s.inverse(s.covector(8),col))==col
    controls.append('horizontal_source_injective_on_scalar_input_all4_columns')
    # Non-nullness not needed: a nonzero null delta_lambda still injects.
    xi=s.covector(0);xi[3]=Q(1)
    assert s.norm(xi)==0
    col=s.sigma(xi,s.inject(4))
    assert col!=s.zero() and s.inverse(s.covector(8),col)!=s.zero()
    controls.append('null_frequency_difference_not_a_loophole')

    # Rational finite boost: normal (8,12) action is cosh*I-sinh*swap.
    c=Q(5,4);h=Q(3,4)
    assert c*c-h*h==1 and h!=0
    assert (Q(0)*c-Q(1)*h)==-Q(3,4)
    controls.append('finite_boost_maps_tangent_e12_out_of_CK_hyperplane')

    # Same observed spinor in the two horizontal covector polarizations.
    # A geometric boost gives distinct norm multipliers4 and1/4. Any common
    # spinor norm and Fourier Jacobian factors cancel in their ratio.
    plus=(Q(1),Q(1));minus=(Q(1),Q(-1))
    def boost(v):return(c*v[0]+h*v[1],h*v[0]+c*v[1])
    def n2(v):return sum(x*x for x in v)
    p=n2(boost(plus))/n2(plus);m=n2(boost(minus))/n2(minus)
    assert p==4 and m==Q(1,4) and p/m==16
    assert p!=m
    controls.append('full_covector_polarizations_not_isometric_up_to_common_scalar')
    # For a rotation the same obstruction vanishes (negative control).
    rot=lambda v:(Q(3,5)*v[0]-Q(4,5)*v[1],Q(4,5)*v[0]+Q(3,5)*v[1])
    assert n2(rot(plus))==n2(plus) and n2(rot(minus))==n2(minus)
    controls.append('rotation_norm_control')

    return {'basis_revision':'f373f00fe94f251a9f4231e1cace71c396eaa610',
            'native_CK_axis':8,'native_boost_mixing':rows,
            'finite_boost':{'cosh':'5/4','sinh':'3/4','tangent_to_normal_coefficient':'-3/4'},
            'charge_polarization_multipliers':{'plus':'4','minus':'1/4','ratio':'16'},
            'controls':controls,
            'scope':'Native normal isotropy and repaired principal source injection; finite boost/norm arithmetic. Written frame-independent seed-jet and direct-integral norm arguments carry their explicit geometric-lift and same-domain premises. No GU, physical ghost or changed-domain completion verdict.'}


def run(root):
    from source_action_reduced_evolution_probe import build_context
    ctx=build_context(root)
    paired=run_paired_jet(root,ctx)
    weak=run_weak_sources(root,ctx)
    closure,seeds,images=run_first_shell(root,ctx,return_work=True)
    out={'paired_current':paired,'weak_sources':weak,'first_shell':closure,
         'spin5_current':run_spin5_current(root,ctx,seeds,images,globals()),
         'lorentz_domain':run_lorentz(root)}
    return out

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=ROOT)
    p.add_argument('--output',type=Path)
    a=p.parse_args();result=run(a.root);encoded=json.dumps(result,indent=2)+'\n'
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(encoded)
    else:print(encoded)
