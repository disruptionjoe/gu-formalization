"""Exact sufficient orbit third-jet family on K2381 K,L. No native/smooth PDE claim."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from itertools import combinations,combinations_with_replacement,permutations,product
import sympy as sp
import json,hashlib,sys,time
ROOT=Path(__file__).resolve().parents[2]
if '--root' in sys.argv:ROOT=Path(sys.argv[sys.argv.index('--root')+1]).resolve()
start=time.time();checks={}
def check(name,value):
 checks[name]=bool(value)
 assert value,name
# Reuse exact lower tensor decoding only, not the K2387 solver.
p=ROOT/'tests/channel-swings/k2387_coupled_hook_jet_blocks_probe.py';s=p.read_text()
ns={'__file__':str(p),'__name__':'lower_tensor_decoder'}
exec(compile(s[:s.index('# Rational basis:')],str(p),'exec'),ns)
n=ns['n'];eta=ns['eta'];K=ns['K'];rho=ns['rho'];tensor=ns['tensor'];pol=ns['pol'];L=ns['L'];prior=ns['prior'];pairs=ns['pairs']
rt=sp.sqrt(2)
def clean(h):return {k:v for k,v in h.items() if v}
def add(*terms):
 out=defaultdict(F)
 for scale,h in terms:
  if scale:
   for k,v in h.items():out[k]+=scale*v
 return clean(out)
def split(v):
 v=sp.expand(v);b=v.coeff(rt);a=sp.expand(v-b*rt)
 assert a.is_Rational and b.is_Rational,(a,b)
 return (F(int(a.p),int(a.q)),F(int(b.p),int(b.q)))
def mul(z,w):return (z[0]*w[0]+2*z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def plus(z,w):return (z[0]+w[0],z[1]+w[1])
Z=(F(0),F(0))
def pairscale(a,z):return (a*z[0],a*z[1])
# Actual metric/curvature and adapted connection, without running old solves.
p=ROOT/'tests/channel-swings/k2381_rotated_null_hook_prolongation_probe.py';s=p.read_text();lo=s.index('root=Path(__file__)');hi=s.index("print('R entries'",lo)
g={'__file__':str(p),'__name__':'actual_geometry','Path':Path,'sp':sp,'n':n,'eta':eta};exec(compile(s[lo:hi],str(p),'exec'),g)
Rc={k:split(v) for k,v in g['Rc'].items()};Ga={a:{(i,j):split(g['GaF'][a][i,j]) for i,j in product(range(n),repeat=2) if g['GaF'][a][i,j]} for a in range(n)}
print('actual geometry',len(Rc),'seconds',time.time()-start,flush=True,file=sys.stderr)
Ric={}
for i,j in product(range(n),repeat=2):
 z=Z
 for a in range(n):z=plus(z,pairscale(eta[a],Rc.get((a,i,a,j),Z)))
 if z!=Z:Ric[i,j]=z
C={}
for a in range(4):
 for i,j in product(range(n),repeat=2):
  z=Z
  for q in range(n):
   z=plus(z,pairscale(2,plus(mul(Ga[a].get((q,i),Z),Ric.get((q,j),Z)),mul(Ga[a].get((q,j),Z),Ric.get((i,q),Z)))))
  if z!=Z:C[a,i,j]=z
# Independent K2381 known mixed receiver formula.
known={};diags={4:(1,1,-1,-1),5:(1,-1,1,-1),6:(1,-1,-1,1)}
for a,diag in diags.items():
 for l in range(4):
  known[l,l,a]=(F(3,4)*eta[l]*diag[l],F(0));known[l,a,l]=known[l,l,a]
for a,(mu,nu) in zip((7,8,9,11,12,13),((1,2),(1,3),(2,3),(0,1),(0,2),(0,3))):
 for u,v in [(mu,nu),(nu,mu)]:known[u,v,a]=(F(0),F(3,4));known[u,a,v]=known[u,v,a]
check('actual_first_Ricci_derivative',C==known)
Q={}
for a in range(4):
 for b,i,j in product(range(n),repeat=3):
  z=Z
  for q in range(n):
   z=plus(z,mul(Ga[a].get((q,b),Z),C.get((q,i,j),Z)))
   z=plus(z,mul(Ga[a].get((q,i),Z),C.get((b,q,j),Z)))
   z=plus(z,mul(Ga[a].get((q,j),Z),C.get((b,i,q),Z)))
  if z!=Z:Q[a,b,i,j]=pairscale(-1,z)
for a,b,i,j in product(range(n),repeat=4):
 actual=plus(Q.get((a,b,i,j),Z),pairscale(-1,Q.get((b,a,i,j),Z)))
 expect=Z
 for q in range(n):
  expect=plus(expect,pairscale(2*eta[q],plus(mul(Rc.get((q,i,a,b),Z),Ric.get((q,j),Z)),mul(Rc.get((q,j,a,b),Z),Ric.get((i,q),Z)))))
 assert actual==expect,('Hessian_commutator',a,b,i,j,actual,expect)
check('all_ordered_Ricci_Hessian_commutators',True)
for a,b in product(range(n),repeat=2):
 assert all(sum(eta[i]*Q.get((a,b,i,i),Z)[p] for i in range(n))==0 for p in range(2))
check('all_Ricci_Hessian_traces',True)
# Independent coordinate differentiation of the explicit actual Ricci field.
# RV=-5/4 G_vertical-3/8 theta tensor theta, theta_E=tr(g^-1 E).
mb=g['ns'];gb=mb['g'];Es=mb['Es'];FM=g['FM'];Gam=g['Gam'];z14=sp.zeros(n)
th=sp.Matrix([sp.trace(gb*E) for E in Es])
dth={a+4:sp.Matrix([-sp.trace(gb*Es[a]*gb*E) for E in Es]) for a in range(10)}
Ricco=sp.diag(gb/4,-sp.Rational(5,4)*mb['G'][4:,4:]-sp.Rational(3,8)*th*th.T)
dr={}
for a in range(n):
 dr[a]=sp.zeros(n)
 if a>=4:
  dr[a][:4,:4]=Es[a-4]/4
  dr[a][4:,4:]=-sp.Rational(5,4)*mb['dg'][a][4:,4:]-sp.Rational(3,8)*(dth[a]*th.T+th*dth[a].T)
CC={b:-2*(dr[b]-Gam[b].T*Ricco-Ricco*Gam[b]) for b in range(n)}
QQ={}
for a,b in product(range(n),repeat=2):
 ddr=sp.zeros(n)
 if a>=4 and b>=4:
  W=gb*Es[a-4]*gb*Es[b-4]*gb+gb*Es[b-4]*gb*Es[a-4]*gb
  ddth=sp.Matrix([sp.trace(W*E) for E in Es])
  ddr[4:,4:]=-sp.Rational(5,4)*mb['ddg'][a,b][4:,4:]-sp.Rational(3,8)*(ddth*th.T+dth[a]*dth[b].T+dth[b]*dth[a].T+th*ddth.T)
 dGamma=sp.Matrix.hstack(*[mb['D'](a,b,k) for k in range(n)])
 deriv=-2*(ddr-dGamma.T*Ricco-Gam[b].T*dr[a]-dr[a]*Gam[b]-Ricco*dGamma)
 QQ[a,b]=deriv-Gam[a].T*CC[b]-CC[b]*Gam[a]-sum((mb['Ga'][a,b][q]*CC[q] for q in range(n)),sp.zeros(n))
for a,b in product(range(n),repeat=2):
 out=FM.T*sum((FM[aa,a]*FM[bb,b]*QQ[aa,bb] for aa,bb in product(range(n),repeat=2) if FM[aa,a] and FM[bb,b]),sp.zeros(n))*FM
 for i,j in product(range(n),repeat=2):assert split(out[i,j])==Q.get((a,b,i,j),Z),('direct_coordinate_Hessian',a,b,i,j)
check('independent_coordinate_Ricci_Hessian_all_entries',True)
print('Hessian nonzero',len(Q),'seconds',time.time()-start,flush=True,file=sys.stderr)
if '--geometry-only' in sys.argv:
 print(json.dumps({'checks':checks,'Q_nonzero':len(Q),'outer_vertical_zero':all(k[0]<4 for k in Q)},sort_keys=True));sys.exit(0)
# Decode the SAME A,N decomposition used for the stored L.
A=[[defaultdict(F) for a in range(n)] for part in range(2)]
N=[defaultdict(lambda:defaultdict(F)) for part in range(2)]
for part,partname in enumerate(['rational_solution','sqrt2_solution']):
 for name,x in prior[partname]:
  x=F(x)
  if name[0]=='A':_,a,u,v=name;A[part][a][u,v]+=x
  else:
   _,a,b,r,i,last=name;d=[0]*n;d[i]=1;d[last]=-1
   for k,y in tensor(r,d).items():N[part][a,b][k]+=x*y
N=[{k:clean(v) for k,v in part.items()} for part in N]
def nget(part,a,b):return N[part].get(tuple(sorted((a,b))),{})
def act(part,a,h):return add(*[(v,rho(h,u,w)) for (u,w),v in A[part][a].items()])
for a,b in combinations_with_replacement(range(n),2):
 for part in range(2):assert add((1,act(part,a,K[b])),(1,act(part,b,K[a])),(1,nget(part,a,b)))==L[part][a,b]
check('same_stored_K_L_and_decomposition',True)
triples=list(combinations_with_replacement(range(n),3));quads=list(combinations_with_replacement(range(n),4));dp=list(combinations_with_replacement(range(n),2));ij=dp
S0=[{} for part in range(2)]
for a,b,c in triples:
 acc=[defaultdict(F),defaultdict(F)]
 for pa,pb,out,factor in [(0,0,0,1),(1,1,0,2),(0,1,1,1),(1,0,1,1)]:
  for u,v,w in [(a,b,c),(b,a,c),(c,a,b)]:
   for k,x in act(pa,u,nget(pb,v,w)).items():acc[out][k]+=factor*x
  for u,v,w in [(a,b,c),(a,c,b),(b,c,a)]:
   for k,x in add((F(1,2),act(pa,u,act(pb,v,K[w]))),(F(1,2),act(pa,v,act(pb,u,K[w])))).items():acc[out][k]+=factor*x
 for part in range(2):S0[part][a,b,c]=clean(acc[part])
# Curvature action on hook fibre; cache only small actual inputs.
Ract_cache={}
def Ract(a,b,c,part):
 key=(a,b,c,part)
 if key in Ract_cache:return Ract_cache[key]
 out=defaultdict(F)
 for hk,v in K[c].items():
  for slot,old in enumerate(hk):
   for new in range(n):
    coeff=-eta[old]*Rc.get((old,new,a,b),Z)[part]
    if coeff:kk=list(hk);kk[slot]=new;out[tuple(kk)]+=coeff*v
 Ract_cache[key]=clean(out);return Ract_cache[key]
def PP(a,b,c,part):return add((1,Ract(a,b,c,part)),* [(-eta[q]*Rc.get((q,c,a,b),Z)[part],K[q]) for q in range(n)])
M0=[{} for _ in range(2)]
for a,b,c in product(range(n),repeat=3):
 for part in range(2):M0[part][a,b,c]=add((F(1,2),Ract(b,c,a,part)),(F(1,3),PP(a,b,c,part)),(F(1,3),PP(a,c,b,part)),(F(1,6),Ract(a,c,b,part)),(F(1,6),Ract(a,b,c,part)))
for a,b,c in product(range(n),repeat=3):
 for part in range(2):
  assert add((1,M0[part][a,b,c]),(-1,M0[part][b,a,c]))==PP(a,b,c,part)
  assert add((1,M0[part][a,b,c]),(-1,M0[part][a,c,b]))==Ract(b,c,a,part)
for t in triples:
 for part in range(2):assert not add(*[(1,M0[part][p]) for p in set(permutations(t))])
check('actual_curved_M0_both_adjacent_swaps_and_zero_sym',True)
def fp(P,Q,i,j):
 out=F(0)
 for a,b in product(range(n),repeat=2):
  out+=F(2,3)*eta[a]*eta[b]*(P.get((a,i,b),0)*Q.get((a,j,b),0)+Q.get((a,i,b),0)*P.get((a,j,b),0)-P.get((i,a,b),0)*Q.get((j,a,b),0)-Q.get((i,a,b),0)*P.get((j,a,b),0))
 return out
rows=[(a,b,i,j) for a,b in dp for i,j in ij];ri={k:v for v,k in enumerate(rows)}
def Dordered(part,a,b,i,j):return sum(eta[m]*(M0[part][a,b,m].get((i,m,j),0)+M0[part][a,b,m].get((j,m,i),0)) for m in range(n))
def DS(S,part,a,b,i,j):return sum(eta[m]*(S[part][tuple(sorted((a,b,m)))].get((i,m,j),0)+S[part][tuple(sorted((a,b,m)))].get((j,m,i),0)) for m in range(n))
rhs=[{},{}];Etarget=[{},{}]
for a,b,i,j in rows:
 for part in range(2):
  target=Q.get((a,b,i,j),Z)[part]+(2*fp(K[a],K[b],i,j) if part==0 else 0)-Dordered(part,a,b,i,j)
  if a!=b:assert target==Q.get((b,a,i,j),Z)[part]+(2*fp(K[b],K[a],i,j) if part==0 else 0)-Dordered(part,b,a,i,j),('Euler_symmetry',a,b,i,j,part)
  if target:Etarget[part][ri[a,b,i,j]]=target
  val=target-DS(S0,part,a,b,i,j)
  if val:rhs[part][ri[a,b,i,j]]=val
check('actual_Euler_residual_derivative_symmetry',True)
# Direct quartic checker, independent from future Euler matrix.
def quartic(S):
 count=0
 for a,b,c,d in quads:
  for part in range(2):
   acc=defaultdict(F)
   for u,v,w,z in [(a,b,c,d),(a,b,d,c),(a,c,d,b),(b,c,d,a)]:
    for k,x in pol(S[part][tuple(sorted((u,v,w)))],K[z]).items():acc[k]+=x
   for pa,pb,factor in ([(0,0,1),(1,1,2)] if part==0 else [(0,1,1),(1,0,1)]):
    for u,v,w,z in [(a,b,c,d),(a,c,b,d),(a,d,b,c)]:
     for k,x in pol(L[pa][tuple(sorted((u,v)))],L[pb][tuple(sorted((w,z)))]).items():acc[k]+=factor*x
   assert not any(acc.values()),('quartic',a,b,c,d,part,next(((k,v) for k,v in acc.items() if v),None))
   count+=1
 return count
check('orbit_baseline_all_quartic',quartic(S0)==4760)
print('baseline ready rhs',list(map(len,rhs)),'seconds',time.time()-start,flush=True,file=sys.stderr)
if '--baseline-only' in sys.argv:
 print(json.dumps({'checks':checks,'rhs_support':list(map(len,rhs))}));sys.exit(0)
# Sparse column operator, free symmetric T in N77 and symmetric B in so(7,7).
nb=[]
for r,(p,q) in enumerate(pairs):
 avail=[i for i in range(n) if i not in (p,q)];last=avail[-1]
 for i in avail[:-1]:
  d=[0]*n;d[i]=1;d[last]=-1;nb.append(((r,i,last),tensor(r,d)))
check('N_basis_dimension',len(nb)==77)
rots=list(combinations(range(n),2));rk={(u,v):[rho(h,u,v) for h in K] for u,v in rots}
def Dcol(tensors):
 out=defaultdict(F)
 for t,h in tensors.items():
  for m in set(t):
   rest=list(t);rest.remove(m);a,b=rest
   for (i,k,j),v in h.items():
    if k==m:
     if i<=j:out[ri[a,b,i,j]]+=eta[m]*v
     if j<=i:out[ri[a,b,j,i]]+=eta[m]*v
 return clean(out)
def column_stream():
 for a,b,c in triples:
  for idx,(name,h) in enumerate(nb):yield ('T',a,b,c,idx),Dcol({(a,b,c):h})
 for a,b in dp:
  for u,v in rots:
   tensors={}
   for c in range(n):
    t=tuple(sorted((a,b,c)))
    mult=sum(tuple(sorted(pair))==(a,b) for pair in [(t[0],t[1]),(t[0],t[2]),(t[1],t[2])])
    if rk[u,v][c]:tensors[t]=add((mult,rk[u,v][c]))
   yield ('B',a,b,u,v),Dcol(tensors)
basis={};records={};columns={};counts={}
def put(name,col):
 original=dict(col);used={}
 while col:
  p=min(col);v=col[p]
  if p not in basis:
   basis[p]={k:x/v for k,x in col.items()};records[p]=(name,v,used);columns[name]=original;return
  used[p]=v
  for k,x in basis[p].items():
   z=col.get(k,F(0))-v*x
   if z:col[k]=z
   elif k in col:del col[k]
for num,(name,col) in enumerate(column_stream()):
 put(name,col)
 if num==43119:counts['N_rank']=len(basis)
 if num%1000==0:print('columns',num,'rank',len(basis),'seconds',time.time()-start,flush=True,file=sys.stderr)
counts['combined_rank']=len(basis)
def solve(target):
 col=dict(target);used={}
 while col:
  p=min(col);v=col[p]
  if p not in basis:return None,col,p
  used[p]=v
  for k,x in basis[p].items():
   z=col.get(k,F(0))-v*x
   if z:col[k]=z
   elif k in col:del col[k]
 out=defaultdict(F)
 for p in reversed(records):
  if p not in used:continue
  q=used[p];name,v,history=records[p];out[name]+=q/v
  for j,x in history.items():used[j]=used.get(j,F(0))-q*x/v
 replay=defaultdict(F)
 for name,x in out.items():
  for k,v in columns[name].items():replay[k]+=x*v
 assert clean(replay)==target
 return clean(out),{},None
sol=[];failure=None
for part in range(2):
 x,res,p=solve(rhs[part]);sol.append(x)
 if x is None:
  # y reconstructs the missing residual pivot as a functional on original rows.
  co=defaultdict(F);co[p]=1
  for q in sorted([q for q in basis if q<p],reverse=True):
   co[q]-=sum(v*co.get(k,F(0)) for k,v in basis[q].items() if k!=q)
  dual=clean(co)
  for name,col in column_stream():assert sum(v*dual.get(k,F(0)) for k,v in col.items())==0,('dual_column',name)
  val=sum(v*dual.get(k,F(0)) for k,v in rhs[part].items());assert val
  failure={'part':part,'dual':[[list(rows[k]),str(v)] for k,v in sorted(dual.items())],'target_value':str(val),'verified_all_columns':True};break
orbit_failure=failure;extra_count=0;tk=[];tk_free=[]
if failure is not None:
 # Compute the complete pointwise polar annihilator T_K, independently of Euler.
 hs=[]
 for a in range(n):
  ii=[i for i in range(n) if i!=a];j=ii[-1]
  for i in ii[:-1]:hs.append({(i,i,a):eta[i],(i,a,i):-eta[i],(j,j,a):-eta[j],(j,a,j):eta[j]})
 for a,b,c in combinations(range(n),3):
  for x,y in [(1,0),(0,1)]:
   h={}
   for i,j,k,v in [(a,b,c,x),(b,c,a,y),(c,a,b,-x-y)]:
    if v:h[i,j,k]=v;h[i,k,j]=-v
   hs.append(h)
 pr=defaultdict(dict)
 for idx,h in enumerate(hs):
  for u in range(n):
   for key,v in pol(h,K[u]).items():pr[u,key][idx]=v
 pb={}
 for label,row in pr.items():
  row=dict(row)
  while row:
   p=min(row);v=row[p]
   if p not in pb:pb[p]={k:x/v for k,x in row.items()};break
   for k,x in pb[p].items():
    z=row.get(k,F(0))-v*x
    if z:row[k]=z
    elif k in row:del row[k]
 for free in range(896):
  if free in pb:continue
  coords={free:F(1)}
  for p in sorted(pb,reverse=True):
   val=-sum(x*coords.get(k,F(0)) for k,x in pb[p].items() if k!=p)
   if val:coords[p]=val
  tk_free.append(free)
  h=add(*[(v,hs[k]) for k,v in coords.items()]);assert all(not pol(h,k) for k in K);tk.append(h)
 check('full_pointwise_polar_kernel_basis',len(tk)==896-len(pb))
 print('T_K dimension',len(tk),'polar rank',len(pb),'seconds',time.time()-start,flush=True,file=sys.stderr)
 # Every generated cubic tensor independently annihilates all homogeneous quartic rows.
 def extra_columns():
  for a,b,c in triples:
   for idx,h in enumerate(tk):yield ('Y',a,b,c,idx),Dcol({(a,b,c):h})
 for name,col in extra_columns():
  put(name,col);extra_count+=1
  if extra_count%1000==0:
   trial=[solve(r)[0] for r in rhs]
   print('polar columns',extra_count,'rank',len(basis),'solvable',[x is not None for x in trial],'seconds',time.time()-start,flush=True,file=sys.stderr)
   if all(x is not None for x in trial):break
 sol=[];failure=None
 for part in range(2):
  x,res,p=solve(rhs[part]);sol.append(x)
  if x is None:
   co=defaultdict(F);co[p]=1
   for q in sorted([q for q in basis if q<p],reverse=True):co[q]-=sum(v*co.get(k,F(0)) for k,v in basis[q].items() if k!=q)
   dual=clean(co)
   for name,col in list(column_stream())+list(extra_columns()):assert sum(v*dual.get(k,F(0)) for k,v in col.items())==0,('enlarged_dual',name)
   val=sum(v*dual.get(k,F(0)) for k,v in rhs[part].items());assert val
   failure={'part':part,'dual':[[list(rows[k]),str(v)] for k,v in sorted(dual.items())],'target_value':str(val),'verified_all_columns':True};break
 counts['with_polar_kernel_prefix_rank']=len(basis)
report={'result_id':'K2390','checks':checks,'ranks':counts,'unknowns':52675+extra_count,'extra_polar_kernel_columns':extra_count,'polar_kernel_dimension':len(tk),'polar_basis_free_indices':tk_free,'initial_orbit_failure':orbit_failure,'symmetric_Euler_rows':len(rows),'full_system_claim':failure is None,'scope':'same fixed K,L; orbit cubic baseline plus homogeneous pointwise polar-kernel cubic additions; finite jet only','failure':failure}
if failure is None:
 S=[{t:dict(h) for t,h in part.items()} for part in S0]
 for part,x in enumerate(sol):
  for name,v in x.items():
   if name[0] in ('T','Y'):
    typ,a,b,c,idx=name;S[part][a,b,c]=add((1,S[part][a,b,c]),(v,nb[idx][1] if typ=='T' else tk[idx]))
   else:
    _,a,b,u,w=name
    for c in range(n):
     t=tuple(sorted((a,b,c)));mult=sum(tuple(sorted(pair))==(a,b) for pair in [(t[0],t[1]),(t[0],t[2]),(t[1],t[2])])
     S[part][t]=add((1,S[part][t]),(v*mult,rk[u,w][c]))
 for part in S:
  for t,h in part.items():
   for (i,j,k),v in h.items():
    assert v==-h.get((i,k,j),0)
    assert v+h.get((j,k,i),0)+h.get((k,i,j),0)==0
   assert all(sum(eta[i]*h.get((i,i,k),0) for i in range(n))==0 for k in range(n))
 check('reconstructed_S_hook_symmetries_and_traces',True)
 for a,b,i,j in product(range(n),repeat=4):
  for part in range(2):
   value=DS(S,part,a,b,i,j)+Dordered(part,a,b,i,j)
   expect=Q.get((a,b,i,j),Z)[part]+(2*fp(K[a],K[b],i,j) if part==0 else 0)
   assert value==expect,('direct_Euler',a,b,i,j,part)
 check('all_38416_ordered_Euler_components_both_field_parts',True)
 check('all_4760_quartic_polynomial_identities',quartic(S)==4760)
 chosen=next(name for name,x in sol[0].items() if x and columns[name] and name[0] in ('T','Y'))
 typ,a,b,c,idx=chosen;badS=[dict(p) for p in S]
 badS[0][a,b,c]=add((1,badS[0][a,b,c]),(1,nb[idx][1] if typ=='T' else tk[idx]))
 changed_rows=sum(DS(badS,0,a,b,i,j)!=Etarget[0].get(ri[a,b,i,j],F(0)) for a,b,i,j in rows)
 check('changed_solution_coefficient_direct_Euler_rejected',changed_rows>0)
 report['changed_coefficient_control']={'parameter':list(chosen),'delta':'1','failed_symmetric_Euler_rows':changed_rows}
 # Actual curvature mutation must fail the unchanged full Hessian commutator.
 key=next(k for k in Rc if k[0]<4 and k[1]>=4 and k[1]!=10)
 old,i,a,b=key;badRc=dict(Rc);badRc[key]=plus(badRc[key],(F(1),F(0)));j=old
 wanted=Z
 for q in range(n):wanted=plus(wanted,pairscale(2*eta[q],plus(mul(badRc.get((q,i,a,b),Z),Ric.get((q,j),Z)),mul(badRc.get((q,j,a,b),Z),Ric.get((i,q),Z)))))
 actual=plus(Q.get((a,b,i,j),Z),pairscale(-1,Q.get((b,a,i,j),Z)))
 check('changed_actual_curvature_Hessian_commutator_rejected',wanted!=actual)
 report['changed_curvature_control']={'component':list(key),'delta':'1','tested_Hessian_entry':[a,b,i,j],'residual':list(map(str,plus(wanted,pairscale(-1,actual))))}
 # Next order necessary test on the SAME chosen S: all-five-W rows have no
 # fourth-jet unknown. Failure excludes this representative only.
 bs=ns['bs'];W=[{i:v for i,v in [(p,bs[r]),(q,-1-bs[r])] if v} for r,(p,q) in enumerate(pairs)]
 check('all_seven_actual_W_kernel_relations',all(not add(*[(v,K[i]) for i,v in w.items()]) for w in W))
 def evalS(part,t):
  terms=[]
  for inds in product(*[list(W[r]) for r in t]):
   scale=F(1)
   for r,i in zip(t,inds):scale*=W[r][i]
   terms.append((scale,S[part][tuple(sorted(inds))]))
  return add(*terms)
 def evalL(part,t):return add(*[(W[t[0]][i]*W[t[1]][j],L[part][tuple(sorted((i,j)))]) for i in W[t[0]] for j in W[t[1]]])
 sw=[{t:evalS(part,t) for t in combinations_with_replacement(range(7),3)} for part in range(2)]
 lw=[{t:evalL(part,t) for t in combinations_with_replacement(range(7),2)} for part in range(2)]
 fifth_bad=[];fifth_count=0
 for five in combinations_with_replacement(range(7),5):
  for part in range(2):
   acc=defaultdict(F)
   for pair in combinations(range(5),2):
    lt=tuple(five[i] for i in pair);st=tuple(five[i] for i in range(5) if i not in pair)
    for pa,pb,factor in ([(0,0,1),(1,1,2)] if part==0 else [(0,1,1),(1,0,1)]):
     for k,v in pol(sw[pa][st],lw[pb][lt]).items():acc[k]+=factor*v
   nz=clean(acc)
   if nz:fifth_bad.append({'five':list(five),'part':part,'first_output':list(next(iter(sorted(nz)))),'value':str(nz[next(iter(sorted(nz)))])})
   fifth_count+=1
 report['next_order_all_W_fifth']={'polynomial_groups_checked':fifth_count,'failed_groups':len(fifth_bad),'first_failure':fifth_bad[0] if fifth_bad else None,'scope':'same chosen third-jet representative only; full affine solution freedom must remain available','formula':'sum over ten unordered pairs P(S_WWW,L_WW)=0; fourth-jet term vanishes because K_W=0'}
 check('all_W_fifth_sector_evaluated',fifth_count==924)
 # Necessary four-W fifth rows: one unknown hook for each W quadruple.
 # Phi(h)_u=P(h,K_u), so the same exact rank612 operator handles210 targets.
 pf_basis={};pf_records={};pf_cols={}
 for idx,h in enumerate(hs):
  col={(u,key):v for u in range(n) for key,v in pol(h,K[u]).items()};original=dict(col);used={}
  while col:
   p=min(col);v=col[p]
   if p not in pf_basis:
    pf_basis[p]={k:x/v for k,x in col.items()};pf_records[p]=(idx,v,used);pf_cols[idx]=original;break
   used[p]=v
   for k,x in pf_basis[p].items():
    z=col.get(k,F(0))-v*x
    if z:col[k]=z
    elif k in col:del col[k]
 check('four_W_polar_image_rank',len(pf_basis)==612)
 check('Gram_rank7_sigma_rank605',sum(p[1]==() for p in pf_basis)==7 and sum(p[1]!=() for p in pf_basis)==605)
 # Exact repeated-hook pairing blocks are eta_a*(I_12+ones_12), det=13.
 check('repeated_Gram_block_determinants_nonzero',all(sp.det(sp.Matrix(12,12,lambda i,j:sp.Rational(ns['gram'](hs[a*12+i],hs[a*12+j]))))==13 for a in range(n)))
 def psolve(target):
  col=dict(target);used={}
  while col:
   p=min(col);v=col[p]
   if p not in pf_basis:return None,col,p
   used[p]=v
   for k,x in pf_basis[p].items():
    z=col.get(k,F(0))-v*x
    if z:col[k]=z
    elif k in col:del col[k]
  out=defaultdict(F)
  for p in reversed(pf_records):
   if p not in used:continue
   q=used[p];idx,v,history=pf_records[p];out[idx]+=q/v
   for j,x in history.items():used[j]=used.get(j,F(0))-q*x/v
  return clean(out),{},None
 def eval_mixed_S(parts,t,u):
  return add(*[(W[t[0]][i]*W[t[1]][j],parts.get(tuple(sorted((i,j,u))),{})) for i in W[t[0]] for j in W[t[1]]])
 swu=[{(t,u):eval_mixed_S(S[part],t,u) for t in combinations_with_replacement(range(7),2) for u in range(n)} for part in range(2)]
 lwu=[{(r,u):add(*[(v,L[part][tuple(sorted((i,u)))]) for i,v in W[r].items()]) for r in range(7) for u in range(n)} for part in range(2)]
 def four_target(quad,part):
  target=defaultdict(F)
  for u in range(n):
   for a in range(4):
    st=tuple(quad[i] for i in range(4) if i!=a)
    for pa,pb,factor in ([(0,0,1),(1,1,2)] if part==0 else [(0,1,1),(1,0,1)]):
     for k,v in pol(sw[pa][st],lwu[pb][quad[a],u]).items():target[u,k]-=factor*v
   for pair in combinations(range(4),2):
    lt=tuple(quad[i] for i in pair);st=tuple(quad[i] for i in range(4) if i not in pair)
    for pa,pb,factor in ([(0,0,1),(1,1,2)] if part==0 else [(0,1,1),(1,0,1)]):
     for k,v in pol(swu[pa][st,u],lw[pb][lt]).items():target[u,k]-=factor*v
  return clean(target)
 fourw_bad=[];fourw_sol=[];first_dual=None;first_target=None
 for quad in combinations_with_replacement(range(7),4):
  for part in range(2):
   target=four_target(quad,part);answer,res,p=psolve(target)
   if answer is None:
    co=defaultdict(F);co[p]=1
    for q in sorted([q for q in pf_basis if q<p],reverse=True):co[q]-=sum(v*co.get(k,F(0)) for k,v in pf_basis[q].items() if k!=q)
    dual=clean(co)
    for h in hs:
     value=sum(v*dual.get((u,k),F(0)) for u in range(n) for k,v in pol(h,K[u]).items())
     assert value==0
    val=sum(v*dual.get(k,F(0)) for k,v in target.items());assert val
    fourw_bad.append({'quad':list(quad),'part':part,'dual_target':str(val)})
    if first_dual is None:
     first_dual={'quad':list(quad),'part':part,'dual':[[[u,list(k)],str(v)] for (u,k),v in sorted(dual.items())],'target_value':str(val),'all896_columns_annihilated':True};first_target=target
   else:
    h=add(*[(v,hs[idx]) for idx,v in answer.items()])
    replay={(u,k):v for u in range(n) for k,v in pol(h,K[u]).items()}
    assert replay==target
    fourw_sol.append({'quad':list(quad),'part':part,'coefficients':[[idx,str(v)] for idx,v in sorted(answer.items())]})
  if (len(fourw_sol)+len(fourw_bad))%40==0:print('four-W progress',len(fourw_sol)+len(fourw_bad),file=sys.stderr,flush=True)
 check('all210_four_W_fifth_targets_evaluated',len(fourw_sol)+len(fourw_bad)==420)
 report['next_order_four_W_fifth']={'quadruples':210,'field_part_targets':420,'image_rank':len(pf_basis),'Gram_rank':7,'sigma_rank':605,'passed_field_part_targets':len(fourw_sol),'failed_field_part_targets':len(fourw_bad),'failures':fourw_bad,'first_exact_dual':first_dual,'solutions':fourw_sol,'scope':'Necessary fifth-algebraic sector for chosen S only; no fourth-Euler coupling or fewer-W sectors implied'}
 report['fifth_Gram_theorem']={'proof_role':'written constructive ideal-and-nondegenerate-pairing argument; no U coefficient array claimed','all_W_Gram_passed':not fifth_bad,'K_rank':7,'pointwise_Gram_rank':7,'repeated_sector_dimension':168,'repeated_block_determinant_absolute':'13','sigma_Gram_decoupling':'repeated-repeated polarization has zero four-form output'}
 print('four-W result',len(fourw_sol),len(fourw_bad),'seconds',time.time()-start,file=sys.stderr,flush=True)

 if first_dual is not None:
  # Probe retained homogeneous Euler/quartic freedom, not a changed lower jet.
  quad=tuple(first_dual['quad']);dual={(u,tuple(k)):F(v) for (u,k),v in first_dual['dual']};wanted=[F(0),F(0)]
  for part in range(2):wanted[part]=sum(v*dual.get(k,F(0)) for k,v in four_target(quad,part).items())
  def parameter_tensor(name):
   if name[0] in ('T','Y'):
    typ,a,b,c,idx=name;return {(a,b,c):nb[idx][1] if typ=='T' else tk[idx]}
   _,a,b,u,w=name;out={}
   for c in range(n):
    t=tuple(sorted((a,b,c)));mult=sum(tuple(sorted(pair))==(a,b) for pair in [(t[0],t[1]),(t[0],t[2]),(t[1],t[2])])
    if rk[u,w][c]:out[t]=add((mult,rk[u,w][c]))
   return out
  def combine_parameters(parameters):
   out={}
   for name,v in parameters.items():
    for t,h in parameter_tensor(name).items():out[t]=add((1,out.get(t,{})),(v,h))
   return {t:h for t,h in out.items() if h}
  def evalW3(fields,t):
   terms=[]
   for inds in product(*[list(W[r]) for r in t]):
    scale=F(1)
    for r,i in zip(t,inds):scale*=W[r][i]
    terms.append((scale,fields.get(tuple(sorted(inds)),{})))
   return add(*terms)
  def first_dual_change(fields):
   result=[]
   for part in range(2):
    acc=F(0)
    for u in sorted({u for u,k in dual}):
     vals=defaultdict(F)
     for a in range(4):
      st=tuple(quad[i] for i in range(4) if i!=a)
      for k,v in pol(evalW3(fields,st),lwu[part][quad[a],u]).items():vals[k]-=v
     for pair in combinations(range(4),2):
      lt=tuple(quad[i] for i in pair);st=tuple(quad[i] for i in range(4) if i not in pair)
      for k,v in pol(eval_mixed_S(fields,st,u),lw[part][lt]).items():vals[k]-=v
     acc+=sum(v*dual.get((u,k),F(0)) for k,v in vals.items())
    result.append(acc)
   return tuple(result)
  repair=None;tried=0
  rawtriples=sorted({tuple(sorted((i,j,u))) for r,s in combinations_with_replacement(quad,2) for i in W[r] for j in W[s] for u,k in dual})
  for t in rawtriples:
   for idx,h in enumerate(tk):
    name=('Y',*t,idx);col=Dcol({t:h});projection,res,p=solve(col)
    if projection is None:continue
    parms=defaultdict(F);parms[name]=1
    for nm,v in projection.items():parms[nm]-=v
    parms=clean(parms);tried+=1
    if not parms:continue
    fields=combine_parameters(parms)
    # Preserve every already-passed all-W fifth row by vanishing on W^3.
    if any(evalW3(fields,t) for t in combinations_with_replacement(range(7),3)):continue
    change=first_dual_change(fields)
    if change==Z:continue
    check('repair_direction_Euler_kernel',not Dcol(fields))
    check('repair_direction_all_W_cubic_zero',not any(evalW3(fields,t) for t in combinations_with_replacement(range(7),3)))
    # Every parameter used is T/B/Y and hence preserves homogeneous quartic rows.
    den=change[0]*change[0]-2*change[1]*change[1];assert den
    scale=pairscale(-1,mul(tuple(wanted),(change[0]/den,-change[1]/den)))
    repaired=[{t:dict(h) for t,h in p.items()} for p in S]
    for part in range(2):
     for t,h in fields.items():repaired[part][t]=add((1,repaired[part][t]),(scale[part],h))
    for a,b,i,j in rows:
     for part in range(2):assert DS(repaired,part,a,b,i,j)==Etarget[part].get(ri[a,b,i,j],F(0))
    check('first_dual_repair_full_symmetric_Euler_replay',True)
    check('first_dual_repair_full_quartic_replay',quartic(repaired)==4760)
    after=plus(tuple(wanted),mul(scale,change));assert after==Z
    # Independently recompute chosen-quad target with repaired tensors.
    oldS=S;oldsw=sw;oldswu=swu;S=repaired
    sw=[{t:evalS(part,t) for t in combinations_with_replacement(range(7),3)} for part in range(2)]
    swu=[{(t,u):eval_mixed_S(S[part],t,u) for t in combinations_with_replacement(range(7),2) for u in range(n)} for part in range(2)]
    direct_after=[sum(v*dual.get(k,F(0)) for k,v in four_target(quad,part).items()) for part in range(2)]
    assert direct_after==[0,0]
    repair={'scope':'first exact dual repaired only; no assertion all13 failing targets repaired','raw_candidate':list(name),'tried_candidates':tried,'kernel_parameters':[[list(k),str(v)] for k,v in sorted(parms.items())],'kernel_change':list(map(str,change)),'scale':list(map(str,scale)),'before':list(map(str,wanted)),'after':list(map(str,direct_after)),'vanishes_on_W_cubic':True,'full_Euler_replay':True,'full_quartic_replay':True}
    # Evaluate all420 necessary targets after repair to keep the outcome honest.
    afterbad=[]
    for q4 in combinations_with_replacement(range(7),4):
     for part in range(2):
      ans,res,p=psolve(four_target(q4,part))
      if ans is None:afterbad.append({'quad':list(q4),'part':part,'first_reduced_row':[p[0],list(p[1])],'residual':str(res[p])})
    repair['four_W_failed_targets_after']=len(afterbad);repair['remaining_failures']=afterbad
    S=oldS;sw=oldsw;swu=oldswu
    break
   if repair is not None:break
  report['four_W_first_dual_kernel_repair']=repair if repair is not None else {'found':False,'tried_candidates':tried,'scope':'limited homogeneous-polar-kernel candidate search; not an impossibility result'}
  print('first-dual repair',repair is not None,'trials',tried,file=sys.stderr,flush=True)

 # Joint follow-through: a finite safe family, preserving Euler/quartic and W^3.
 def pquot(target):
  col=dict(target);res={}
  while col:
   p=min(col);v=col[p]
   if p not in pf_basis:res[p]=v;del col[p];continue
   for k,x in pf_basis[p].items():
    z=col.get(k,F(0))-v*x
    if z:col[k]=z
    elif k in col:del col[k]
  return res
 jr={}
 for quad in combinations_with_replacement(range(7),4):
  for part in range(2):
   for k,v in pquot(four_target(quad,part)).items():jr[quad,part,k]=-v
 Wsupport=sorted({i for w in W for i in w});outside=sorted(set(range(n))-set(Wsupport))
 alphas=[]
 for r,(p,q) in enumerate(pairs):
  z={i:v for i,v in [(p,1+bs[r]),(q,bs[r])] if v}
  if r==1:z={4:F(8519),2:F(9012)}
  assert all(sum(v*w.get(i,0) for i,v in z.items())==0 for w in W);alphas.append(z)
 check('seven_transverse_covectors_annihilate_actual_W',len(alphas)==7)
 coordowner={i:r for r,w in enumerate(W) for i in w}
 quiet={}
 for idx,h in enumerate(tk):
  quiet[idx]={m for m in range(n) if not Dcol({(m,m,m):h})}
 didx=[idx for idx,h in enumerate(tk) if all(len(set(k))==3 for k in h)]
 check('distinct_polar_kernel_dimension123',len(didx)==123)
 lpairs=list(combinations_with_replacement(range(7),2));qcache={};rawcache={}
 def small_quot(ar,idx,lp,part):
  key=ar,idx,lp,part
  if key not in qcache:
   raw={(u,k):-c*v for u,c in alphas[ar].items() for k,v in pol(tk[idx],lw[part][lp]).items()}
   rawcache[key]=raw;qcache[key]=pquot(raw)
  return qcache[key]
 def safe_fields(name):
  ar,i,j,idx=name;out={}
  for a,v in alphas[ar].items():
   t=tuple(sorted((a,i,j)));mult=6 if len(set(t))==1 else (2 if len(set(t))==2 else 1)
   out[t]=add((mult*v,tk[idx]))
  return out
 def joint_candidates():
  for ar,alpha in enumerate(alphas):
   for i,j in combinations_with_replacement(Wsupport,2):
    r,s=sorted((coordowner[i],coordowner[j]))
    # i,j have sorted coordinate order, which need not match owner order.
    paircoef=W[coordowner[i]][i]*W[coordowner[j]][j]*(2 if r==s else 1)
    for idx in didx:
     if not (set(alpha)|{i,j}).issubset(quiet[idx]):continue
     name=(ar,i,j,idx);c0={};c1={}
     for lp in lpairs:
      quad=tuple(sorted((r,s,*lp)));count_r=quad.count(r);count_s=quad.count(s)
      mult=F(count_r*(count_r-1),2) if r==s else F(count_r*count_s)
      factor=paircoef*mult
      for part in range(2):
       for key,v in small_quot(ar,idx,lp,part).items():c0[quad,part,key]=factor*v
     c1={(q,1-p,k):(2 if p==1 else 1)*v for (q,p,k),v in c0.items()}
     yield name,clean(c0),clean(c1)
 jb={};jrec={};jcols={};jcount=0;rawcount=0
 def jput(name,col):
  original=dict(col);used={}
  while col:
   p=min(col);v=col[p]
   if p not in jb:jb[p]={k:x/v for k,x in col.items()};jrec[p]=(name,v,used);jcols[name]=original;return
   used[p]=v
   for k,x in jb[p].items():
    z=col.get(k,F(0))-v*x
    if z:col[k]=z
    elif k in col:del col[k]
 def jsolve(target):
  col=dict(target);used={}
  while col:
   p=min(col);v=col[p]
   if p not in jb:return None,col,p
   used[p]=v
   for k,x in jb[p].items():
    z=col.get(k,F(0))-v*x
    if z:col[k]=z
    elif k in col:del col[k]
  out=defaultdict(F)
  for p in reversed(jrec):
   if p not in used:continue
   q=used[p];name,v,history=jrec[p];out[name]+=q/v
   for k,x in history.items():used[k]=used.get(k,F(0))-q*x/v
  replay=defaultdict(F)
  for name,v in out.items():
   for k,x in jcols[name].items():replay[k]+=v*x
  assert clean(replay)==target
  return clean(out),{},None
 jsolution=None;jsamples={}
 for name,c0,c1 in joint_candidates():
  rawcount+=1
  if c0 or c1:
   if name[0] in (0,1,6) and name[0] not in jsamples:jsamples[name[0]]=(name,dict(c0),dict(c1))
   for part,col in enumerate((c0,c1)):jput((name,part),col);jcount+=1
   if jcount%100==0:
    jsolution,res,p=jsolve(jr)
    print('joint safe directions',rawcount,'columns',jcount,'rank',len(jb),'remaining',len(res),'seconds',time.time()-start,file=sys.stderr,flush=True)
    if jsolution is not None:break
 if jsolution is None:jsolution,res,p=jsolve(jr)
 # Independent direct tensor receiver checks for separated transverse directions.
 for sample_name,expected0,expected1 in jsamples.values():
  fields=safe_fields(sample_name);assert not Dcol(fields)
  assert not any(evalW3(fields,t) for t in combinations_with_replacement(range(7),3))
  oldS=S;oldsw=sw;oldswu=swu;S=[{t:fields.get(t,{}) for t in triples},{t:{} for t in triples}]
  sw=[{t:evalS(part,t) for t in combinations_with_replacement(range(7),3)} for part in range(2)]
  swu=[{(t,u):eval_mixed_S(S[part],t,u) for t in combinations_with_replacement(range(7),2) for u in range(n)} for part in range(2)]
  actual={}
  for quad in combinations_with_replacement(range(7),4):
   for part in range(2):
    for key,v in pquot(four_target(quad,part)).items():actual[quad,part,key]=v
  assert actual==expected0,('joint_map_direct',sample_name)
  actual1={(q,1-p,k):(2 if p==1 else 1)*v for (q,p,k),v in actual.items()}
  assert actual1==expected1
  S=oldS;sw=oldsw;swu=oldswu
 check('joint_map_independent_tensor_replay_three_transverse_samples',len(jsamples)==3)
 joint={'family':'sym(alpha_r tensor dx_i tensor dx_j) times one of the fixed 123 distinct T_K basis tensors individually passing all support-contraction tests; basis-filtered family, not full quiet intersection','W_coordinate_support':Wsupport,'coordinate_axes_outside_W_support':outside,'transverse_covectors':[[[i,str(v)] for i,v in sorted(a.items())] for a in alphas],'safe_directions_examined':rawcount,'rationalized_nonzero_columns':jcount,'computed_prefix_rank':len(jb),'original_quotient_residual_entries':len(jr),'solved':jsolution is not None}
 if jsolution is None:
  co=defaultdict(F);co[p]=1
  for q in sorted([q for q in jb if q<p],reverse=True):co[q]-=sum(v*co.get(k,F(0)) for k,v in jb[q].items() if k!=q)
  dualj=clean(co)
  for name,c0,c1 in joint_candidates():
   for col in (c0,c1):assert sum(v*dualj.get(k,F(0)) for k,v in col.items())==0
  val=sum(v*dualj.get(k,F(0)) for k,v in jr.items());assert val
  # Lift the quotient dual to original polynomial receiver labels and replay
  # against every admitted raw direction without calling the quotient reducer.
  lifted=defaultdict(F)
  for (quad,part,pfrow),coeff in dualj.items():
   ell=defaultdict(F);ell[pfrow]=1
   for q in sorted([q for q in pf_basis if q<pfrow],reverse=True):ell[q]-=sum(v*ell.get(k,F(0)) for k,v in pf_basis[q].items() if k!=q)
   for key,v in ell.items():lifted[quad,part,key]+=coeff*v
  lifted=clean(lifted);targets={(q,p):four_target(q,p) for q,p,k in lifted}
  direct_value=-sum(v*targets[q,p].get(k,F(0)) for (q,p,k),v in lifted.items());assert direct_value==val
  for name,c0,c1 in joint_candidates():
   ar,i,j,idx=name;r,s=sorted((coordowner[i],coordowner[j]));factor0=W[coordowner[i]][i]*W[coordowner[j]][j]*(2 if r==s else 1)
   for fieldpart in range(2):
    total=F(0)
    for (quad,p,key),v in lifted.items():
     remain=list(quad)
     if r not in remain:continue
     remain.remove(r)
     if s not in remain:continue
     remain.remove(s);lp=tuple(remain)
     mult=F(quad.count(r)*(quad.count(r)-1),2) if r==s else F(quad.count(r)*quad.count(s))
     sourcepart=p if fieldpart==0 else 1-p;scale=2 if fieldpart==1 and p==0 else 1
     small_quot(ar,idx,lp,sourcepart)
     total+=v*factor0*mult*scale*rawcache[ar,idx,lp,sourcepart].get(key,F(0))
    assert total==0,('lifted_dual_raw_column',name,fieldpart)
  check('joint_family_dual_all_raw_columns_independent_replay',True)
  joint['lifted_original_receiver_dual']=[[[list(q),part,[k[0],list(k[1])]],str(v)] for (q,part,k),v in sorted(lifted.items())]
  joint['lifted_original_target_value']=str(direct_value)
  joint['family_exhausted']=True;joint['dual']=[[[list(q),part,[k[0],list(k[1])]],str(v)] for (q,part,k),v in sorted(dualj.items())];joint['dual_target']=str(val)
 else:
  best=[{t:dict(h) for t,h in part.items()} for part in S];direction=[{},{}]
  for (name,part),v in jsolution.items():
   fields=safe_fields(name);assert not Dcol(fields)
   for t,h in fields.items():
    direction[part][t]=add((1,direction[part].get(t,{})),(v,h));best[part][t]=add((1,best[part][t]),(v,h))
  assert all(not evalW3(direction[part],t) for part in range(2) for t in combinations_with_replacement(range(7),3))
  check('joint_repair_preserves_all_W_cubic',True)
  for a,b,i,j in rows:
   for part in range(2):assert DS(best,part,a,b,i,j)==Etarget[part].get(ri[a,b,i,j],F(0))
  check('joint_repair_full_Euler_replay',True);check('joint_repair_full_quartic_replay',quartic(best)==4760)
  oldS=S;oldsw=sw;oldswu=swu;S=best
  sw=[{t:evalS(part,t) for t in combinations_with_replacement(range(7),3)} for part in range(2)]
  swu=[{(t,u):eval_mixed_S(S[part],t,u) for t in combinations_with_replacement(range(7),2) for u in range(n)} for part in range(2)]
  solutions4=[]
  for quad in combinations_with_replacement(range(7),4):
   for part in range(2):
    target=four_target(quad,part);ans,res,p=psolve(target);assert ans is not None,('joint_four_W',quad,part)
    h=add(*[(v,hs[i]) for i,v in ans.items()]);assert {(u,k):v for u in range(n) for k,v in pol(h,K[u]).items()}==target
    solutions4.append({'quad':list(quad),'part':part,'coefficients':[[i,str(v)] for i,v in sorted(ans.items())]})
  check('joint_repair_all420_four_W_targets_direct_replay',len(solutions4)==420)
  joint['coefficients']=[[[list(name),part],str(v)] for (name,part),v in sorted(jsolution.items())]
  joint['four_W_solutions']=solutions4
  expandedbest=[[[list(t),[[list(k),str(v)] for k,v in sorted(h.items())]] for t,h in sorted(p.items()) if h] for p in best]
  joint['repaired_tensor_sha256']=hashlib.sha256(json.dumps(expandedbest,sort_keys=True,separators=(',',':')).encode()).hexdigest()
  joint['family_exhausted']=False;joint['scope']='Same K,L and repaired S; full third Euler/fourth algebraic plus five-W and four-W necessary fifth sectors only. Other fifth sectors and fourth Euler intersection open.'
  S=oldS;sw=oldsw;swu=oldswu
 report['four_W_joint_safe_kernel_repair']=joint
 print('joint repair result',joint['solved'],'rank',len(jb),'directions',rawcount,file=sys.stderr,flush=True)

 # Strengthening: solve each entire supportwise quiet contraction intersection.
 base_distinct=list(didx)
 axiscols={(m,idx):Dcol({(m,m,m):tk[idx]}) for m in range(n) for idx in base_distinct}
 supports=sorted({tuple(sorted(set(alpha)|{i,j})) for alpha in alphas for i,j in combinations_with_replacement(Wsupport,2)})
 support_bases={};support_records=[];combo_index={};combo_records={}
 for support in supports:
  rr={}
  for m in support:
   for j,idx in enumerate(base_distinct):
    for row,v in axiscols[m,idx].items():rr.setdefault((m,row),{})[j]=v
  eb={}
  for row in sorted(rr):
   vec=dict(rr[row])
   while vec:
    pivot=min(vec);v=vec[pivot]
    if pivot not in eb:eb[pivot]={k:x/v for k,x in vec.items()};break
    for k,x in eb[pivot].items():
     z=vec.get(k,F(0))-v*x
     if z:vec[k]=z
     elif k in vec:del vec[k]
  free=[j for j in range(len(base_distinct)) if j not in eb];ids=[];combinations_record=[]
  for f in free:
   combo={f:F(1)}
   for pivot in sorted(eb,reverse=True):
    v=-sum(x*combo.get(k,F(0)) for k,x in eb[pivot].items() if k!=pivot)
    if v:combo[pivot]=v
   assert all(sum(v*combo.get(k,F(0)) for k,v in row.items())==0 for row in rr.values())
   cc=tuple(sorted((base_distinct[j],v) for j,v in combo.items()))
   if cc not in combo_index:
    h=add(*[(v,tk[idx]) for idx,v in cc]);idx=len(tk);tk.append(h);combo_index[cc]=idx;combo_records[idx]=cc
   idx=combo_index[cc]
   assert all(not Dcol({(m,m,m):tk[idx]}) for m in support)
   ids.append(idx);combinations_record.append([base_distinct[f],idx])
  support_bases[support]=ids
  support_records.append({'support':list(support),'contraction_rank':len(eb),'kernel_dimension':len(free),'basis_free_coordinate_and_hook_index':combinations_record})
 check('full_quiet_support_nullspaces_exact_rank_and_replay',len(support_records)==len(supports))
 print('full quiet intersections',len(supports),'unique hooks',len(combo_index),'directions',sum(len(support_bases[tuple(sorted(set(alpha)|{i,j}))]) for alpha in alphas for i,j in combinations_with_replacement(Wsupport,2)),file=sys.stderr,flush=True)
 def joint_candidates():
  for ar,alpha in enumerate(alphas):
   for i,j in combinations_with_replacement(Wsupport,2):
    r,s=sorted((coordowner[i],coordowner[j]))
    paircoef=W[coordowner[i]][i]*W[coordowner[j]][j]*(2 if r==s else 1)
    for idx in support_bases[tuple(sorted(set(alpha)|{i,j}))]:
     name=(ar,i,j,idx);c0={}
     for lp in lpairs:
      quad=tuple(sorted((r,s,*lp)));count_r=quad.count(r);count_s=quad.count(s)
      mult=F(count_r*(count_r-1),2) if r==s else F(count_r*count_s)
      factor=paircoef*mult
      for part in range(2):
       for key,v in small_quot(ar,idx,lp,part).items():c0[quad,part,key]=factor*v
     c1={(q,1-p,k):(2 if p==1 else 1)*v for (q,p,k),v in c0.items()}
     yield name,clean(c0),clean(c1)
 jb={};jrec={};jcols={};jcount=0;rawcount=0
 def jput(name,col):
  original=dict(col);used={}
  while col:
   p=min(col);v=col[p]
   if p not in jb:jb[p]={k:x/v for k,x in col.items()};jrec[p]=(name,v,used);jcols[name]=original;return
   used[p]=v
   for k,x in jb[p].items():
    z=col.get(k,F(0))-v*x
    if z:col[k]=z
    elif k in col:del col[k]
 def jsolve(target):
  col=dict(target);used={}
  while col:
   p=min(col);v=col[p]
   if p not in jb:return None,col,p
   used[p]=v
   for k,x in jb[p].items():
    z=col.get(k,F(0))-v*x
    if z:col[k]=z
    elif k in col:del col[k]
  out=defaultdict(F)
  for p in reversed(jrec):
   if p not in used:continue
   q=used[p];name,v,history=jrec[p];out[name]+=q/v
   for k,x in history.items():used[k]=used.get(k,F(0))-q*x/v
  replay=defaultdict(F)
  for name,v in out.items():
   for k,x in jcols[name].items():replay[k]+=v*x
  assert clean(replay)==target
  return clean(out),{},None
 jsolution=None;jsamples={}
 for name,c0,c1 in joint_candidates():
  rawcount+=1
  if c0 or c1:
   if name[0] in (0,1,6) and name[0] not in jsamples:jsamples[name[0]]=(name,dict(c0),dict(c1))
   for part,col in enumerate((c0,c1)):jput((name,part),col);jcount+=1
   if jcount%100==0:
    jsolution,res,p=jsolve(jr)
    print('full quiet directions',rawcount,'columns',jcount,'rank',len(jb),'remaining',len(res),'seconds',time.time()-start,file=sys.stderr,flush=True)
    if jsolution is not None:break
 if jsolution is None:jsolution,res,p=jsolve(jr)
 # Independent direct tensor receiver checks for separated transverse directions.
 for sample_name,expected0,expected1 in jsamples.values():
  fields=safe_fields(sample_name);assert not Dcol(fields)
  assert not any(evalW3(fields,t) for t in combinations_with_replacement(range(7),3))
  oldS=S;oldsw=sw;oldswu=swu;S=[{t:fields.get(t,{}) for t in triples},{t:{} for t in triples}]
  sw=[{t:evalS(part,t) for t in combinations_with_replacement(range(7),3)} for part in range(2)]
  swu=[{(t,u):eval_mixed_S(S[part],t,u) for t in combinations_with_replacement(range(7),2) for u in range(n)} for part in range(2)]
  actual={}
  for quad in combinations_with_replacement(range(7),4):
   for part in range(2):
    for key,v in pquot(four_target(quad,part)).items():actual[quad,part,key]=v
  assert actual==expected0,('joint_map_direct',sample_name)
  actual1={(q,1-p,k):(2 if p==1 else 1)*v for (q,p,k),v in actual.items()}
  assert actual1==expected1
  S=oldS;sw=oldsw;swu=oldswu
 check('full_quiet_map_independent_tensor_replay_three_transverse_samples',len(jsamples)==3)
 joint={'family':'sym(alpha_r tensor dx_i tensor dx_j) times the FULL intersection of distinct T_K with each D_m kernel on support(alpha_r) union {i,j}; alpha annihilates W','W_coordinate_support':Wsupport,'coordinate_axes_outside_W_support':outside,'transverse_covectors':[[[i,str(v)] for i,v in sorted(a.items())] for a in alphas],'safe_directions_examined':rawcount,'rationalized_nonzero_columns':jcount,'computed_prefix_rank':len(jb),'original_quotient_residual_entries':len(jr),'solved':jsolution is not None}
 if jsolution is None:
  co=defaultdict(F);co[p]=1
  for q in sorted([q for q in jb if q<p],reverse=True):co[q]-=sum(v*co.get(k,F(0)) for k,v in jb[q].items() if k!=q)
  dualj=clean(co)
  for name,c0,c1 in joint_candidates():
   for col in (c0,c1):assert sum(v*dualj.get(k,F(0)) for k,v in col.items())==0
  val=sum(v*dualj.get(k,F(0)) for k,v in jr.items());assert val
  # Lift the quotient dual to original polynomial receiver labels and replay
  # against every admitted raw direction without calling the quotient reducer.
  lifted=defaultdict(F)
  for (quad,part,pfrow),coeff in dualj.items():
   ell=defaultdict(F);ell[pfrow]=1
   for q in sorted([q for q in pf_basis if q<pfrow],reverse=True):ell[q]-=sum(v*ell.get(k,F(0)) for k,v in pf_basis[q].items() if k!=q)
   for key,v in ell.items():lifted[quad,part,key]+=coeff*v
  lifted=clean(lifted);targets={(q,p):four_target(q,p) for q,p,k in lifted}
  direct_value=-sum(v*targets[q,p].get(k,F(0)) for (q,p,k),v in lifted.items());assert direct_value==val
  for name,c0,c1 in joint_candidates():
   ar,i,j,idx=name;r,s=sorted((coordowner[i],coordowner[j]));factor0=W[coordowner[i]][i]*W[coordowner[j]][j]*(2 if r==s else 1)
   for fieldpart in range(2):
    total=F(0)
    for (quad,p,key),v in lifted.items():
     remain=list(quad)
     if r not in remain:continue
     remain.remove(r)
     if s not in remain:continue
     remain.remove(s);lp=tuple(remain)
     mult=F(quad.count(r)*(quad.count(r)-1),2) if r==s else F(quad.count(r)*quad.count(s))
     sourcepart=p if fieldpart==0 else 1-p;scale=2 if fieldpart==1 and p==0 else 1
     small_quot(ar,idx,lp,sourcepart)
     total+=v*factor0*mult*scale*rawcache[ar,idx,lp,sourcepart].get(key,F(0))
    assert total==0,('lifted_dual_raw_column',name,fieldpart)
  check('full_quiet_family_dual_all_raw_columns_independent_replay',True)
  joint['lifted_original_receiver_dual']=[[[list(q),part,[k[0],list(k[1])]],str(v)] for (q,part,k),v in sorted(lifted.items())]
  joint['lifted_original_target_value']=str(direct_value)
  joint['family_exhausted']=True;joint['dual']=[[[list(q),part,[k[0],list(k[1])]],str(v)] for (q,part,k),v in sorted(dualj.items())];joint['dual_target']=str(val)
 else:
  best=[{t:dict(h) for t,h in part.items()} for part in S];direction=[{},{}]
  for (name,part),v in jsolution.items():
   fields=safe_fields(name);assert not Dcol(fields)
   for t,h in fields.items():
    direction[part][t]=add((1,direction[part].get(t,{})),(v,h));best[part][t]=add((1,best[part][t]),(v,h))
  assert all(not evalW3(direction[part],t) for part in range(2) for t in combinations_with_replacement(range(7),3))
  check('full_quiet_repair_preserves_all_W_cubic',True)
  for a,b,i,j in rows:
   for part in range(2):assert DS(best,part,a,b,i,j)==Etarget[part].get(ri[a,b,i,j],F(0))
  check('full_quiet_repair_full_Euler_replay',True);check('full_quiet_repair_full_quartic_replay',quartic(best)==4760)
  oldS=S;oldsw=sw;oldswu=swu;S=best
  sw=[{t:evalS(part,t) for t in combinations_with_replacement(range(7),3)} for part in range(2)]
  swu=[{(t,u):eval_mixed_S(S[part],t,u) for t in combinations_with_replacement(range(7),2) for u in range(n)} for part in range(2)]
  solutions4=[]
  for quad in combinations_with_replacement(range(7),4):
   for part in range(2):
    target=four_target(quad,part);ans,res,p=psolve(target);assert ans is not None,('joint_four_W',quad,part)
    h=add(*[(v,hs[i]) for i,v in ans.items()]);assert {(u,k):v for u in range(n) for k,v in pol(h,K[u]).items()}==target
    solutions4.append({'quad':list(quad),'part':part,'coefficients':[[i,str(v)] for i,v in sorted(ans.items())]})
  check('full_quiet_repair_all420_four_W_targets_direct_replay',len(solutions4)==420)
  joint['coefficients']=[[[list(name),part],str(v)] for (name,part),v in sorted(jsolution.items())]
  joint['four_W_solutions']=solutions4
  expandedbest=[[[list(t),[[list(k),str(v)] for k,v in sorted(h.items())]] for t,h in sorted(p.items()) if h] for p in best]
  joint['repaired_tensor_sha256']=hashlib.sha256(json.dumps(expandedbest,sort_keys=True,separators=(',',':')).encode()).hexdigest()
  joint['family_exhausted']=False;joint['scope']='Same K,L and repaired S; full third Euler/fourth algebraic plus five-W and four-W necessary fifth sectors only. Other fifth sectors and fourth Euler intersection open.'
  S=oldS;sw=oldsw;swu=oldswu
 joint['supportwise_contraction_kernels']=support_records
 joint['reconstructed_hook_combinations']=[[idx,[[j,str(v)] for j,v in cc]] for idx,cc in sorted(combo_records.items())]
 report['four_W_full_quiet_kernel_repair']=joint
 print('full quiet result',joint['solved'],'rank',len(jb),'directions',rawcount,file=sys.stderr,flush=True)

 report['solutions']=[[[list(k),str(v)] for k,v in sorted(x.items())] for x in sol]
 expanded=[[[list(t),[[list(k),str(v)] for k,v in sorted(h.items())]] for t,h in sorted(p.items()) if h] for p in S]
 report['reconstructed_tensor_sha256']=hashlib.sha256(json.dumps(expanded,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 report['reconstructed_tensor_nonzero_counts']=[sum(len(h) for h in part.values()) for part in S]
 report['checks']=checks
report['dependencies']={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [ROOT/'tests/channel-swings/k2387_coupled_hook_jet_blocks_probe.py',ROOT/'tests/channel-swings/k2381_rotated_null_hook_prolongation_probe.py',ROOT/'tests/channel-swings/k2345_curved_bundle_ricci_obstruction_probe.py',ROOT/'lab/process/k2381-rotated-null-hook-prolongation.json',ROOT/'lab/process/k2384-third-hook-jet-compatibility.json']}
report['probe_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
out=json.dumps(report,indent=2,sort_keys=True)+'\n'
if '--output' in sys.argv:Path(sys.argv[sys.argv.index('--output')+1]).write_text(out)
elif '--write' in sys.argv:(ROOT/'lab/process/k2390-full-hook-jet.json').write_text(out)
if '--write' in sys.argv or '--output' in sys.argv:
 print(json.dumps({'result_id':'K2390','checks':len(checks),'full_system_claim':report['full_system_claim'],'prefix_rank':counts.get('with_polar_kernel_prefix_rank'),'next_order_all_W_fifth':report.get('next_order_all_W_fifth')}),flush=True)
else:print(out,end='')
