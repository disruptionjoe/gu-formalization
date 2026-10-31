"""Exact rotating-null hook jets and differentiated compatibility; --write saves evidence."""
from pathlib import Path
from itertools import product
import sympy as sp
import sys,hashlib
from fractions import Fraction as F
from collections import defaultdict
from itertools import combinations_with_replacement,combinations
import time,json
n=14;eta=(1,-1,-1,-1,1,1,1,1,1,1,-1,-1,-1,-1);pairs=((0,1),(4,2),(5,3),(6,10),(7,11),(8,12),(9,13));owner={i:r for r,p in enumerate(pairs) for i in p};lam=[F(27,28) if i in {0,1,2,3,10} else F(-15,28) for i in range(n)];ts=[lam[p]+lam[q] for p,q in pairs];ds=[[F(0) if owner[i]==r else lam[i]/6+ts[r]/70+ts[owner[i]]/420 for i in range(n)] for r in range(7)]
rows=[(l,i,j) for l in range(n) for i in range(n) for j in range(i,n)];ri={k:v for v,k in enumerate(rows)}
def tensor(r,d):
 out={}
 for i,v in enumerate(d):
  if v:
   for a in pairs[r]:out[i,i,a]=eta[i]*v;out[i,a,i]=-eta[i]*v
 return out
H=[tensor(r,ds[r]) for r in range(7)];bs=[F(0)]*7;bs[1]=-F(9012,493);K=[{} for _ in range(n)]
for r,(p,q) in enumerate(pairs):
 for l,v in ((p,1+bs[r]),(q,bs[r])):K[l]={k:v*x for k,x in H[r].items() if v*x}
def rho(H,a,b):
 out=defaultdict(F)
 for key,v in H.items():
  for slot,i in enumerate(key):
   if i==a:j=b;sign=1
   elif i==b:j=a;sign=-eta[a]*eta[b]
   else:continue
   kk=list(key);kk[slot]=j;out[tuple(kk)]+=sign*v
 return {k:v for k,v in out.items() if v}
def add_D(out,l,m,H):
 for (i,k,j),v in H.items():
  if k==m:
   if i<=j:out[ri[l,i,j]]+=eta[m]*v
   if j<=i:out[ri[l,j,i]]+=eta[m]*v
 return out
basis={};records={};columns={};counts={};start=time.time()
def put(name,col):
 col={k:F(v) for k,v in col.items() if v};original=dict(col);used={}
 while col:
  p=min(col);v=col[p]
  if p not in basis:
   basis[p]={k:x/v for k,x in col.items()};records[p]=(name,v,used);columns[name]=original;return
  used[p]=v
  for k,x in basis[p].items():
   nv=col.get(k,F(0))-v*x
   if nv:col[k]=nv
   elif k in col:del col[k]
# N symmetric second derivatives in full77 space
for a,b in combinations_with_replacement(range(n),2):
 for r,(p,q) in enumerate(pairs):
  avail=[i for i in range(n) if i not in (p,q)];last=avail[-1]
  for i in avail[:-1]:
   d=[0]*n;d[i]=1;d[last]=-1;h=tensor(r,d);out=defaultdict(F);add_D(out,a,b,h)
   if a!=b:add_D(out,b,a,h)
   put(('N',a,b,r,i,last),out)
counts['N_rank']=len(basis)
for a in range(n):
 for u,v in combinations(range(n),2):
  rot=[rho(h,u,v) for h in K];out=defaultdict(F)
  for m in range(n):add_D(out,a,m,rot[m])
  for l in range(n):add_D(out,l,a,rot[l])
  put(('A',a,u,v),out)

counts['combined_rank']=len(basis)
# C = -2nabla Ric; independent actual mixed formula 3/2 g(h,S_U x).
# coefficients as rational + sqrt2*rational. S4,5,6 diagonal, S10 trace omitted.
C0={};C1={}
diags={4:(1,1,-1,-1),5:(1,-1,1,-1),6:(1,-1,-1,1)}
for a,diag in diags.items():
 for l in range(4):C0[ri[l,l,a]]=F(3,4)*eta[l]*diag[l]
for a,(mu,nu) in zip((7,8,9,11,12,13),((1,2),(1,3),(2,3),(0,1),(0,2),(0,3))):
 C1[ri[mu,nu,a]]=F(3,4);C1[ri[nu,mu,a]]=F(3,4)
def solve(target):
 col=dict(target);used={}
 while col:
  p=min(col);v=col[p]
  if p not in basis:return None,{str(rows[k]):str(x) for k,x in col.items()}
  used[p]=v
  for k,x in basis[p].items():
   nv=col.get(k,F(0))-v*x
   if nv:col[k]=nv
   elif k in col:del col[k]
 out=defaultdict(F)
 for p in reversed(records):
  if p not in used:continue
  q=used[p];name,v,history=records[p];out[name]+=q/v
  for j,x in history.items():used[j]=used.get(j,F(0))-q*x/v
 check=defaultdict(F)
 for name,v in out.items():
  for k,x in columns[name].items():check[k]+=v*x
 assert {k:v for k,v in check.items() if v}==target
 return [[list(k),str(v)] for k,v in out.items() if v],{}
s0,r0=solve(C0);s1,r1=solve(C1);result={**counts,'rational_solution':s0,'sqrt2_solution':s1,'rational_residual':r0,'sqrt2_residual':r1,'seconds':time.time()-start}
initial=result

root=Path(__file__).resolve().parents[2];path=root/'tests/channel-swings/k2345_curved_bundle_ricci_obstruction_probe.py';src=path.read_text();ns={'__file__':str(path),'__name__':'backend'};exec(compile(src[:src.index('Ric=ricci()')],str(path),'exec'),ns)
G=ns['G'];Ga=ns['Ga'];D=ns['D'];g=sp.diag(1,-1,-1,-1);rt=sp.sqrt(2)
Ss={4:sp.diag(1,1,-1,-1)/2,5:sp.diag(1,-1,1,-1)/2,6:sp.diag(1,-1,-1,1)/2,10:sp.eye(4)/2}
for a,(mu,nu) in zip((7,8,9,11,12,13),((1,2),(1,3),(2,3),(0,1),(0,2),(0,3))):
 E=sp.zeros(4);E[mu,nu]=E[nu,mu]=1/rt;Ss[a]=g*E
frame=[]
for a in range(n):
 v=sp.zeros(n,1)
 if a<4:v[a]=1
 else:
  E=g*Ss[a]
  for b,(i,j) in enumerate(((i,j) for i in range(4) for j in range(i,4))):v[b+4]=E[i,j]
 frame.append(v)
FM=sp.Matrix.hstack(*frame);FI=FM.inv();assert sp.simplify(FM.T*G*FM)==sp.diag(*eta)
Gam=[sp.Matrix.hstack(*[Ga[i,j] for j in range(n)]) for i in range(n)]
GaF={a:sp.simplify(FI*sum((frame[a][i]*Gam[i] for i in range(n) if frame[a][i]),sp.zeros(n))*FM) for a in range(n)}
# Verify vertical parallel transport from actual backend.
for a in range(4,n):
 J=sp.zeros(n);J[:4,:4]=-Ss[a]/2
 for b in range(4,n):
  E=g*Ss[b];out=(Ss[a].T*E+E*Ss[a])/2;vec=sp.zeros(n,1)
  for q,(i,j) in enumerate(((i,j) for i in range(4) for j in range(i,4))):vec[q+4]=out[i,j]
  J[:,b]=FI*vec
 assert GaF[a]+J==sp.zeros(n)
cache={}
def rr(i,j):
 if (i,j) not in cache:cache[i,j]=sp.Matrix.hstack(*[D(i,j,k)-D(j,i,k) for k in range(n)])+Gam[i]*Gam[j]-Gam[j]*Gam[i]
 return cache[i,j]
Rc={}
for j in range(n):
 for k in range(j+1,n):
  mat=sp.simplify(FI*sum((frame[j][u]*frame[k][v]*rr(u,v) for u in range(n) for v in range(n) if frame[j][u] and frame[k][v]),sp.zeros(n))*FM)
  for a in range(n):
   for i in range(n):
    if mat[a,i]:Rc[a,i,j,k]=eta[a]*mat[a,i];Rc[a,i,k,j]=-eta[a]*mat[a,i]
print('R entries',len(Rc),flush=True)
NR=[]
for l in range(n):
 out=defaultdict(lambda:sp.Integer(0))
 if l<4:
  for key,v in Rc.items():
   for slot,b in enumerate(key):
    for a in range(n):
     if GaF[l][b,a]:kk=list(key);kk[slot]=a;out[tuple(kk)]-=GaF[l][b,a]*v
 NR.append({k:sp.expand(v) for k,v in out.items() if sp.expand(v)})
C={}
Ric={}
for i in range(n):
 for j in range(n):
  Ric[i,j]=sum(eta[a]*Rc.get((a,i,a,j),0) for a in range(n))
for l in range(n):
 for i in range(n):
  for j in range(n):
   v=-2*sum(eta[a]*NR[l].get((a,i,a,j),0) for a in range(n))
   if v:C[l,i,j]=sp.expand(v)
# Independent known C.
assert C[2,4,2]==sp.Rational(3,4)
for l,i,j in product(range(n),repeat=3):
 row=ri[l,min(i,j),max(i,j)]
 assert sp.expand(C.get((l,i,j),0)-C0.get(row,F(0))-rt*C1.get(row,F(0)))==0
for a,j,k in product(range(n),repeat=3):
 got=sp.expand(sum(eta[q]*NR[q].get((a,q,j,k),0) for q in range(n)))
 want=sp.Rational(1,2)*(C.get((j,a,k),0)-C.get((k,a,j),0))
 assert sp.expand(got-want)==0,(a,j,k,got,want)
print('nablaR and contracted Bianchi PASS',flush=True)
# Affine row A(L)=rhs from differentiated full double divergence.
# canonical L index uses unordered derivative pair then 3 tensor slots.
def lk(l,m,key):return (min(l,m),max(l,m),*key)
fun=[defaultdict(lambda:sp.Integer(0)) for _ in range(n)];rhs=[]
for l in range(n):
 const=0
 for (a,i,j,k),v in Rc.items():fun[l][lk(l,i,(a,k,j))]-=eta[a]*eta[i]*eta[j]*eta[k]*v
 # derivative terms range beyond nonzero R support
 for (a,i,j,k),v in NR[l].items():const-=eta[a]*eta[i]*eta[j]*eta[k]*v*K[i].get((a,k,j),0)
 for a in range(n):
  for j in range(n):
   for k in range(n):
    div=sp.Rational(1,2)*(C.get((j,a,k),0)-C.get((k,a,j),0))
    const-=eta[a]*eta[j]*eta[k]*div*K[l].get((a,k,j),0)
 rhs.append(-sp.expand(const))
def Fcoeff(Q,i,j):
 out=defaultdict(F)
 for (a,c,b),v in Q.items():
  if c==j:out[a,i,b]+=F(2,3)*eta[a]*eta[b]*v
  if c==i:out[a,j,b]+=F(2,3)*eta[a]*eta[b]*v
  if a==j:out[i,c,b]-=F(2,3)*eta[c]*eta[b]*v
  if a==i:out[j,c,b]-=F(2,3)*eta[c]*eta[b]*v
 return {k:v for k,v in out.items() if v}
for l in range(n):
 for i in range(n):
  for j in range(n):
   # symmetry combines first two differentiated-product terms
   for key,v in Fcoeff(K[j],i,j).items():fun[l][lk(l,i,key)]-=4*eta[i]*eta[j]*v
   for key,v in Fcoeff(K[l],i,j).items():fun[l][lk(i,j,key)]-=2*eta[i]*eta[j]*v
fun=[{k:sp.expand(v) for k,v in f.items() if sp.expand(v)} for f in fun]
def split(v):
 v=sp.expand(v);a=v.coeff(rt);b=sp.expand(v-a*rt);assert a.is_Rational and b.is_Rational,(a,b);return (F(int(b.p),int(b.q)),F(int(a.p),int(a.q)))
fs=[{k:split(v) for k,v in f.items()} for f in fun];rs=[split(v) for v in rhs]
# reconstruct rational/sqrt2 L from candidate
sln=initial
def terms(name):
 typ,a,b,*rest=name
 if typ=='N':
  r,i,last=rest;dd=[0]*n;dd[i]=1;dd[last]=-1
  return {lk(a,b,key):v for key,v in tensor(r,dd).items()}
 # A: typ, derivative a, u=b, v=rest0
 u=b;v=rest[0];out=defaultdict(F)
 for m in range(n):
  for key,x in rho(K[m],u,v).items():out[lk(a,m,key)]+=x*(2 if a==m else 1)
 return dict(out)
Ls=[]
for key in ['rational_solution','sqrt2_solution']:
 out=defaultdict(F)
 for name,v in sln[key]:
  for k,x in terms(name).items():out[k]+=F(v)*x
 Ls.append({k:v for k,v in out.items() if v})
def val(f,L0,L1):
 a=b=F(0)
 for k,(x,y) in f.items():
  v=L0.get(k,F(0));w=L1.get(k,F(0));a+=x*v+2*y*w;b+=x*w+y*v
 return a,b
res=[tuple(x-y for x,y in zip(val(f,*Ls),r)) for f,r in zip(fs,rs)]
print('CURRENT differentiated defects',[[str(a),str(b)] for a,b in res],flush=True)
# save exact functional system, no model fit or numeric threshold
out={'curvature':[[list(k),list(map(str,split(v)))] for k,v in Rc.items()],'functionals':[[[list(k),list(map(str,v))] for k,v in f.items()] for f in fs],'rhs':[list(map(str,v)) for v in rs],'current_defect':[list(map(str,v)) for v in res],'C':[[list(k),list(map(str,split(v)))] for k,v in C.items()]}
ex=out

basis={};records={};columns={};start=time.time()
idx=defaultdict(list)
for l,fun in enumerate(ex['functionals']):
 for k,(a,b) in fun:idx[tuple(k)].append((l,F(a),F(b)))
def lk(a,b,key):return(min(a,b),max(a,b),*key)
def augmented(name,top,L):
 ext=defaultdict(F)
 for key,v in L.items():
  for l,a,b in idx.get(key,[]):ext[2*l]+=v*a;ext[2*l+1]+=v*b
 for part in (0,1):
  col={2*k+part:v for k,v in top.items() if v}
  for k,v in ext.items():
   if part==0:col[2*len(rows)+k]=v
   elif k%2==0:col[2*len(rows)+k+1]=v
   else:col[2*len(rows)+k-1]=2*v
  put((*name,part),col)
for a,b in combinations_with_replacement(range(n),2):
 for r,(p,q) in enumerate(pairs):
  avail=[i for i in range(n) if i not in (p,q)];last=avail[-1]
  for i in avail[:-1]:
   dd=[0]*n;dd[i]=1;dd[last]=-1;h=tensor(r,dd);out=defaultdict(F);add_D(out,a,b,h)
   if a!=b:add_D(out,b,a,h)
   augmented(('N',a,b,r,i,last),out,{lk(a,b,k):v for k,v in h.items()})
augmented_N_rank=len(basis)
print('aug N rank',len(basis),'time',time.time()-start,flush=True)
for a in range(n):
 for u,v in combinations(range(n),2):
  rot=[rho(h,u,v) for h in K];out=defaultdict(F);L=defaultdict(F)
  for m in range(n):
   add_D(out,a,m,rot[m])
   for key,x in rot[m].items():L[lk(a,m,key)]+=x*(2 if a==m else 1)
  for l in range(n):add_D(out,l,a,rot[l])
  augmented(('A',a,u,v),out,L)
 print('aug A',a,len(basis),time.time()-start,flush=True)
target={}
for (l,i,j),(a,b) in ex['C']:
 if i>j:continue
 for part,v in enumerate((a,b)):
  if F(v):target[2*ri[l,i,j]+part]=F(v)
for l,ab in enumerate(ex['rhs']):
 for part,v in enumerate(ab):
  if F(v):target[2*len(rows)+2*l+part]=F(v)
col=dict(target);used={}
while col:
 p=min(col);v=col[p]
 if p not in basis:print('INCONSISTENT',p,str(v));break
 used[p]=v
 for k,x in basis[p].items():
  nv=col.get(k,F(0))-v*x
  if nv:col[k]=nv
  elif k in col:del col[k]
if not col:
 out=defaultdict(F)
 for p in reversed(records):
  if p not in used:continue
  q=used[p];name,v,hist=records[p];out[name]+=q/v
  for j,x in hist.items():used[j]=used.get(j,F(0))-q*x/v
 check=defaultdict(F)
 for name,v in out.items():
  for k,x in columns[name].items():check[k]+=v*x
 assert {k:v for k,v in check.items() if v}==target
 res={'rank':len(basis),'rational_solution':[[list(k[:-1]),str(v)] for k,v in out.items() if v and k[-1]==0],'sqrt2_solution':[[list(k[:-1]),str(v)] for k,v in out.items() if v and k[-1]==1]}
 repaired=res
else:raise AssertionError('augmented system inconsistent')

# Independently reconstruct final full tensors, not only receiver columns.
Ls=[]
for key in ['rational_solution','sqrt2_solution']:
 L=defaultdict(F)
 for name,v in repaired[key]:
  for k,x in terms(name).items():L[k]+=F(v)*x
 Ls.append({k:v for k,v in L.items() if v})
def sliceL(L,a,b):return {tuple(k[2:]):v for k,v in L.items() if k[:2]==(min(a,b),max(a,b))}
def hget(H,i,j,k):return H.get((i,j,k),F(0))
for L in Ls:
 for a,b in combinations_with_replacement(range(n),2):
  h=sliceL(L,a,b)
  for i,j,k in h:
   assert hget(h,i,j,k)==-hget(h,i,k,j)
   assert hget(h,i,j,k)+hget(h,j,k,i)+hget(h,k,i,j)==0
  assert all(sum(eta[i]*hget(h,i,i,k) for i in range(n))==0 for k in range(n))
for part,L in enumerate(Ls):
 for l,i,j in product(range(n),repeat=3):
  got=sum(eta[k]*(L.get(lk(l,k,(i,k,j)),F(0))+L.get(lk(l,k,(j,k,i)),F(0))) for k in range(n))
  assert got==split(C.get((l,i,j),sp.Integer(0)))[part]
assert all(val(f,*Ls)==r for f,r in zip(fs,rs))
# Mixed cubic constraints checked directly, separately in both number-field parts.
def gram(A,B):return sum(F(eta[i]*eta[j]*eta[k],2)*v*hget(B,i,j,k) for (i,j,k),v in A.items())
def sigma(A,B):
 out=defaultdict(F);byi=defaultdict(list)
 for (i,j,k),v in B.items():
  if j<k:byi[i].append((j,k,v))
 for (i,j,k),v in A.items():
  if j>=k:continue
  for u,w,x in byi[i]:
   if len({j,k,u,w})<4:continue
   seq=(j,k,u,w);sign=(-1)**sum(seq[a]>seq[b] for a in range(4) for b in range(a+1,4))
   out[tuple(sorted(seq))]+=eta[i]*sign*v*x
 return {k:v for k,v in out.items() if v}
for L in Ls:
 slices={(a,b):sliceL(L,a,b) for a,b in combinations_with_replacement(range(n),2)}
 for a,b,c in combinations_with_replacement(range(n),3):
  triples=[(slices[a,b],K[c]),(slices[a,c],K[b]),(slices[b,c],K[a])]
  assert sum(gram(P,Q) for P,Q in triples)==0
  sig=defaultdict(F)
  for P,Q in triples:
   for k,v in sigma(P,Q).items():sig[k]+=v
  assert not any(sig.values())
# Failure-capable controls: frozen common-null obstruction, missing rotations,
# and the original unextended L versus new derivative receiver.
assert counts['N_rank']==1057 and counts['combined_rank']==1403
assert initial['rational_residual']==initial['sqrt2_residual']=={}
assert any(any(F(x) for x in row) for row in ex['current_defect'])
assert repaired['rank']==2834 and augmented_N_rank-2*counts['N_rank']==28
# Direct paired receiver failure of the complete old N space.
for r,(p,q) in enumerate(pairs):
 avail=[i for i in range(n) if i not in (p,q)]
 for i in avail[:-1]:
  dd=[0]*n;dd[i]=1;dd[avail[-1]]=-1;h=tensor(r,dd)
  assert all(hget(h,4,m,2)+hget(h,2,m,4)==0 for m in range(n))
assert C[2,4,2]==sp.Rational(3,4)
# Check scalar K repair independently using K2378's exact retained defect formula.
beta=bs
scalar=-(1120*beta[1]*beta[2]+1120*beta[1]*beta[3]+1972*beta[1]+1120*beta[2]*beta[3]+1972*beta[2]+1114*beta[3]-3*beta[4]-3*beta[6]+36048)/F(3360)
assert scalar==0
report={'result_id':'K2381','checks':12,'check_names':['actual_metric_connection_and_frame','all2744_contracted_Bianchi_rows','all_ordered_receiver_rows_two_parts','all_second_jet_hook_constraints','all560_mixed_cubic_norm_rows_two_parts','all560_mixed_cubic_sigma_rows_two_parts','original_scalar_compatibility','original_second_jet_rejected_by_differentiated_identity','full14_differentiated_identity_repaired','exact_augmented_column_replay','kernel_surjectivity_by_exact_ranks','local_algebraic_extension_written_proof'], 'ranks':{'N_receiver':1057,'orbit_N_receiver':1403,'split_N_augmented':augmented_N_rank,'split_orbit_N_augmented':2834},'initial_support':[len(initial['rational_solution']),len(initial['sqrt2_solution'])],'initial_differentiated_defects':ex['current_defect'],'final_support':[len(repaired['rational_solution']),len(repaired['sqrt2_solution'])],'rational_solution':repaired['rational_solution'],'sqrt2_solution':repaired['sqrt2_solution'],'changed_input_controls':{'common_null_paired_receiver_fails':True,'unextended_witness_fails_next_identity':True},'scope':'Finite hook second jet, all mixed third algebraic constraints, and differentiated contracted PDE compatibility. No full third Euler jet or stationary local solution.','dependencies':{str(path.relative_to(root)):hashlib.sha256(path.read_bytes()).hexdigest(),'tests/channel-swings/k2378_null_hook_jet_compatibility_probe.py':hashlib.sha256((root/'tests/channel-swings/k2378_null_hook_jet_compatibility_probe.py').read_bytes()).hexdigest()}}
text=json.dumps(report,sort_keys=True,indent=2)+'\n'
if '--write' in sys.argv:(root/'lab/process/k2381-rotated-null-hook-prolongation.json').write_text(text)
print(json.dumps({k:report[k] for k in ['result_id','checks','ranks','initial_support','final_support','scope']}))
