"""Exact coupled vertical W-pair blocks on the stored K,L; --write saves certificate."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from itertools import combinations,combinations_with_replacement,product
import sympy as sp
import json,hashlib,sys,time
root=Path(__file__).resolve().parents[2];start=time.time();n=14
eta=(1,-1,-1,-1,1,1,1,1,1,1,-1,-1,-1,-1);pairs=((0,1),(4,2),(5,3),(6,10),(7,11),(8,12),(9,13));owner={i:r for r,p in enumerate(pairs) for i in p}
lam=[F(27,28) if i in {0,1,2,3,10} else F(-15,28) for i in range(n)];ts=[lam[p]+lam[q] for p,q in pairs]
def tensor(r,d):
 out={}
 for i,v in enumerate(d):
  if v:
   for a in pairs[r]:out[i,i,a]=eta[i]*v;out[i,a,i]=-eta[i]*v
 return out
H=[tensor(r,[F(0) if owner[i]==r else lam[i]/6+ts[r]/70+ts[owner[i]]/420 for i in range(n)]) for r in range(7)]
bs=[F(0)]*7;bs[1]=-F(9012,493);K=[{} for _ in range(n)]
for r,(p,q) in enumerate(pairs):
 for l,v in ((p,1+bs[r]),(q,bs[r])):K[l]={k:v*x for k,x in H[r].items() if v*x}
def rho(h,a,b):
 out=defaultdict(F)
 for key,v in h.items():
  for slot,i in enumerate(key):
   if i==a:j=b;sign=1
   elif i==b:j=a;sign=-eta[a]*eta[b]
   else:continue
   kk=list(key);kk[slot]=j;out[tuple(kk)]+=sign*v
 return {k:v for k,v in out.items() if v}
def lk(a,b,k):return (min(a,b),max(a,b),*k)
def terms(name):
 typ,a,b,*rest=name
 if typ=='N':
  r,i,last=rest;d=[0]*n;d[i]=1;d[last]=-1
  return {lk(a,b,k):v for k,v in tensor(r,d).items()}
 out=defaultdict(F);u=b;v=rest[0]
 for m in range(n):
  for k,x in rho(K[m],u,v).items():out[lk(a,m,k)]+=x*(2 if a==m else 1)
 return dict(out)
prior=json.loads((root/'lab/process/k2381-rotated-null-hook-prolongation.json').read_text());Ls=[]
for part in ['rational_solution','sqrt2_solution']:
 out=defaultdict(F)
 for name,c in prior[part]:
  for k,x in terms(name).items():out[k]+=F(c)*x
 Ls.append({k:v for k,v in out.items() if v})
def sl(L,a,b):return {k[2:]:v for k,v in L.items() if k[:2]==(min(a,b),max(a,b))}
L=[{(a,b):sl(p,a,b) for a,b in combinations_with_replacement(range(n),2)} for p in Ls]
def lget(part,a,b):return L[part][min(a,b),max(a,b)]
def gram(A,B):return sum(F(eta[i]*eta[j]*eta[k],2)*v*B.get((i,j,k),F(0)) for (i,j,k),v in A.items())
def sigma(A,B):
 out=defaultdict(F);byi=defaultdict(list)
 for (i,j,k),v in B.items():
  if j<k:byi[i].append((j,k,v))
 for (i,j,k),v in A.items():
  if j>=k:continue
  for u,w,x in byi[i]:
   if len({j,k,u,w})<4:continue
   seq=(j,k,u,w);sgn=(-1)**sum(seq[a]>seq[b] for a in range(4) for b in range(a+1,4));out[tuple(sorted(seq))]+=eta[i]*sgn*v*x
 return {k:v for k,v in out.items() if v}
def pol(A,B):
 out=sigma(A,B);g=gram(A,B)
 if g:out[()]=g
 return out
# Rational basis: 168 repeated-index and 728 distinct-index hook tensors.
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
assert len(hs)==896
maps=[[pol(h,k) for k in K] for h in hs]
assert all(not any(key for key in p) for row in maps[:168] for p in row)
assert all(() not in p for row in maps[168:] for p in row)
# Assemble all simultaneous Gram/sigma equations and Euler receivers. Rows use
# original tensor labels, columns m*896+j. No quotient or numeric rank guess.
rows=defaultdict(dict)
for j,mp in enumerate(maps):
 for m in range(n):
  col=m*len(hs)+j
  for t,p in enumerate(mp):
   u,v=sorted((m,t))
   for key,x in p.items():rows['P',u,v,key][col]=rows['P',u,v,key].get(col,F(0))+x*(2 if m==t else 1)
  for i in range(n):
   for q in range(i,n):
    x=eta[m]*(hs[j].get((i,m,q),0)+hs[j].get((q,m,i),0))
    if x:rows['E',i,q][col]=F(x)
print('assembled',len(rows),'rows',sum(map(len,rows.values())),'entries',flush=True)
# Actual curvature backend, only the stored metric and its derivatives.
path=root/'tests/channel-swings/k2381_rotated_null_hook_prolongation_probe.py';src=path.read_text()
lo=src.index("root=Path(__file__)");hi=src.index("print('R entries'",lo)
ns=dict(globals());ns['__file__']=str(path);exec(compile(src[lo:hi],str(path),'exec'),ns)
Rc=ns['Rc'];Ga=ns['Ga'];assert all(ns['Ga'][a,b][i]==0 for a in range(4,n) for b in range(4,n) for i in range(4))
def split(v):
 v=sp.expand(v);b=v.coeff(sp.sqrt(2));a=sp.expand(v-b*sp.sqrt(2));assert a.is_Rational and b.is_Rational
 return F(int(a.p),int(a.q)),F(int(b.p),int(b.q))
vv=[10,11,12,13];rhs=defaultdict(lambda:[F(0)]*8)
for vindex,v in enumerate(vv):
 assert not K[v]
 for u,t in combinations_with_replacement(range(n),2):
  for pa,pb,part,factor in [(0,0,0,1),(1,1,0,2),(0,1,1,1),(1,0,1,1)]:
   for aa,bb,mul in [(lget(pa,v,v),lget(pb,u,t),1),(lget(pa,v,u),lget(pb,v,t),2)]:
    for key,x in pol(aa,bb).items():rhs['P',u,t,key][2*vindex+part]-=factor*mul*x
 # Hessian Ric(v,v)=0 for vertical v; remaining actual curved baseline.
 for m in range(n):
  h=defaultdict(lambda:sp.Integer(0))
  for a in range(n):
   coeff=eta[a]*Rc.get((a,v,v,m),0)
   for key,x in K[a].items():h[key]+=coeff*x
  for i in range(n):
   for j in range(i,n):
    val=eta[m]*(h.get((i,m,j),0)+h.get((j,m,i),0))/3
    if val:
     for part,x in enumerate(split(val)):rhs['E',i,j][2*vindex+part]+=x
print('rhs ready',len(rhs),'seconds',time.time()-start,flush=True)
# Fraction row elimination with original rows retained for exact solution replay.
keys=sorted(set(rows)|set(rhs),key=str);basis={};incons=[]
for num,key in enumerate(keys):
 row={k:F(v) for k,v in rows[key].items() if v};b=list(rhs[key])
 while row:
  p=min(row);v=row[p]
  if p not in basis:
   basis[p]=({k:x/v for k,x in row.items()},[x/v for x in b]);break
  rr,bb=basis[p]
  for k,x in rr.items():
   z=row.get(k,F(0))-v*x
   if z:row[k]=z
   elif k in row:del row[k]
  b=[x-v*y for x,y in zip(b,bb)]
 else:
  if any(b):incons.append((key,b));print('inconsistent row',key,list(map(str,b)),flush=True);break
 if num%1000==0:print('elimination',num,'rank',len(basis),'seconds',time.time()-start,flush=True)
assert not incons,'Exact inconsistent block; reconstruct dual certificate before claiming result'
# Pivots may not be introduced in increasing order; true back substitution must
# follow descending pivot order, since each row's other indices exceed its pivot.
sol={}
for p in sorted(basis,reverse=True):
 rr,bb=basis[p];sol[p]=[bb[j]-sum(x*sol.get(k,[F(0)]*8)[j] for k,x in rr.items() if k!=p) for j in range(8)]
for key in keys:
 got=[sum(x*sol.get(k,[F(0)]*8)[j] for k,x in rows[key].items()) for j in range(8)]
 assert got==rhs[key],key
cert=[{'v':v,'rational':[[k,str(x[2*i])] for k,x in sorted(sol.items()) if x[2*i]],'sqrt2':[[k,str(x[2*i+1])] for k,x in sorted(sol.items()) if x[2*i+1]]} for i,v in enumerate(vv)]
# A changed affine receiver must be detected by original row replay.
changed=dict(rows[keys[0]]);bad=list(rhs[keys[0]]);bad[0]+=1
assert [sum(x*sol.get(k,[F(0)]*8)[j] for k,x in changed.items()) for j in range(8)]!=bad

# Follow-through: ten purevertical pairs with shared symmetric cubic coordinates.
# Same row operator for each pair, but columns now identify all overlapping triples.
V=[10,11,12,13];vp=list(combinations_with_replacement(V,2))
triples=sorted({tuple(sorted((a,b,m))) for a,b in vp for m in range(n)})
tridx={t:i for i,t in enumerate(triples)};joined_basis={};joined_original=[]
joined_rhs=[];joined_labels=[]
for vi,(v,w) in enumerate(vp):
 target=defaultdict(lambda:[F(0),F(0)])
 for u,t in combinations_with_replacement(range(n),2):
  for pa,pb,part,factor in [(0,0,0,1),(1,1,0,2),(0,1,1,1),(1,0,1,1)]:
   for aa,bb in [(lget(pa,v,w),lget(pb,u,t)),(lget(pa,v,u),lget(pb,w,t)),(lget(pa,v,t),lget(pb,w,u))]:
    for key,x in pol(aa,bb).items():target['P',u,t,key][part]-=factor*x
 for m in range(n):
  h=defaultdict(lambda:sp.Integer(0))
  for a in range(n):
   coeff=eta[a]*(Rc.get((a,w,v,m),0)+Rc.get((a,v,w,m),0))
   for key,x in K[a].items():h[key]+=coeff*x
  for i in range(n):
   for j in range(i,n):
    val=eta[m]*(h.get((i,m,j),0)+h.get((j,m,i),0))/6
    if val:
     for part,x in enumerate(split(val)):target['E',i,j][part]+=x
 for key in sorted(set(rows)|set(target),key=str):
  row={tridx[tuple(sorted((v,w,k//896)))]*896+k%896:x for k,x in rows[key].items() if x}
  b=list(target[key]);joined_original.append(row);joined_rhs.append(b);joined_labels.append((v,w,key))
  row=dict(row)
  while row:
   p=min(row);q=row[p]
   if p not in joined_basis:
    joined_basis[p]=({k:x/q for k,x in row.items()},[x/q for x in b]);break
   rr,bb=joined_basis[p]
   for k,x in rr.items():
    z=row.get(k,F(0))-q*x
    if z:row[k]=z
    elif k in row:del row[k]
   b=[x-q*y for x,y in zip(b,bb)]
  else:
   assert not any(b),('joined_inconsistent',v,w,key,b)
 print('joined',v,w,'rank',len(joined_basis),'seconds',time.time()-start,flush=True)
jsol={}
for p in sorted(joined_basis,reverse=True):
 rr,bb=joined_basis[p];jsol[p]=[bb[j]-sum(x*jsol.get(k,[F(0),F(0)])[j] for k,x in rr.items() if k!=p) for j in range(2)]
for row,b in zip(joined_original,joined_rhs):
 assert [sum(x*jsol.get(k,[F(0),F(0)])[j] for k,x in row.items()) for j in range(2)]==b
joined={'vertical_pairs':[list(z) for z in vp],'derivative_triples':[list(z) for z in triples],'unknowns':len(triples)*896,'rows':len(joined_original),'rank':len(joined_basis),'original_rows_replayed':True,'solution_rational':[[k,str(x[0])] for k,x in sorted(jsol.items()) if x[0]],'solution_sqrt2':[[k,str(x[1])] for k,x in sorted(jsol.items()) if x[1]]}

# Reconstruct tensor values independently of sparse receiver assembly.
ST=[defaultdict(lambda:defaultdict(F)) for _ in range(2)]
for col,coeff in jsol.items():
 triple=triples[col//896];h=hs[col%896]
 for part in range(2):
  for key,x in h.items():ST[part][triple][key]+=coeff[part]*x
ST=[{t:{k:v for k,v in h.items() if v} for t,h in part.items()} for part in ST]
def getS(part,v,w,m):return ST[part].get(tuple(sorted((v,w,m))),{})
direct_quartic=direct_euler=0
for v,w in vp:
 for u,t in combinations_with_replacement(range(n),2):
  for part in range(2):
   acc=defaultdict(F)
   for a,b in [(getS(part,v,w,u),K[t]),(getS(part,v,w,t),K[u])]:
    for key,x in pol(a,b).items():acc[key]+=x
   for pa,pb,factor in ([(0,0,1),(1,1,2)] if part==0 else [(0,1,1),(1,0,1)]):
    for a,b in [(lget(pa,v,w),lget(pb,u,t)),(lget(pa,v,u),lget(pb,w,t)),(lget(pa,v,t),lget(pb,w,u))]:
     for key,x in pol(a,b).items():acc[key]+=factor*x
   assert not any(acc.values()),('direct_quartic',v,w,u,t,part)
   direct_quartic+=1
 for i,j in combinations_with_replacement(range(n),2):
  got=[sum(eta[m]*(getS(part,v,w,m).get((i,m,j),F(0))+getS(part,v,w,m).get((j,m,i),F(0))) for m in range(n)) for part in range(2)]
  val=0
  for m in range(n):
   for a in range(n):
    val+=sp.Rational(eta[m]*eta[a],6)*(Rc.get((a,w,v,m),0)+Rc.get((a,v,w,m),0))*(K[a].get((i,m,j),0)+K[a].get((j,m,i),0))
  assert tuple(got)==split(val),('direct_euler',v,w,i,j)
  direct_euler+=1
# Corrupt an actual solution coefficient, not the test predicate.
chosen=next(c for c in jsol if jsol[c][0] and any(c in row for row in joined_original))
assert any(sum(x*(jsol.get(k,[F(0),F(0)])[0]+(1 if k==chosen else 0)) for k,x in row.items())!=b[0] for row,b in zip(joined_original,joined_rhs))
joined['direct_tensor_quartic_checks']=direct_quartic
joined['direct_tensor_euler_checks']=direct_euler
joined['perturbed_solution_coefficient_detected']=True
print('joined replay PASS',flush=True)
paths=['tests/channel-swings/k2381_rotated_null_hook_prolongation_probe.py','lab/process/k2381-rotated-null-hook-prolongation.json','lab/process/k2384-third-hook-jet-compatibility.json','tests/channel-swings/k2345_curved_bundle_ricci_obstruction_probe.py','tests/channel-swings/k2378_null_hook_jet_compatibility_probe.py']
report={'result_id':'K2387','block_directions':vv,'unknowns_per_block':12544,'assembled_rows':len(keys),'rank':len(basis),'original_row_replay':True,'solutions':cert,'joined_vertical_system':joined,'controls':{'changed_affine_receiver_detected':True,'repeated_distinct_polarization_split':True,'actual_vertical_totally_geodesic':True},'scope':'Four separate blocks and the ten joined purevertical W-pair blocks have exact simultaneous solutions with shared cubic symmetry. Remaining W directions and fewer-W sectors of the full coupled third-Euler/fourth-algebraic system remain open.','dependencies':{p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in paths}}
out=json.dumps(report,sort_keys=True,indent=2)+'\n'
if '--write' in sys.argv:(root/'lab/process/k2387-coupled-hook-jet-blocks.json').write_text(out)
print(json.dumps({k:v for k,v in report.items() if k not in ['solutions','dependencies','joined_vertical_system']}))
