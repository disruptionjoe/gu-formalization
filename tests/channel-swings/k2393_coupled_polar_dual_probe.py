"""Exact extension test of K2390's restricted dual; no smooth-solution claim."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from itertools import combinations,combinations_with_replacement,product
import json,hashlib,sys,time
import sympy as sp
ROOT=Path(__file__).resolve().parents[2];start=time.time();checks={}
def check(n,v):
 checks[n]=bool(v)
 if not v:raise AssertionError(n)
def clean(h):return {k:v for k,v in h.items() if v}
def add(*terms):
 d=defaultdict(F)
 for scale,h in terms:
  for k,v in h.items():d[k]+=scale*v
 return clean(d)
p=ROOT/'tests/channel-swings/k2387_coupled_hook_jet_blocks_probe.py';source=p.read_text();ns={'__file__':str(p),'__name__':'lower_only'};exec(compile(source[:source.index('# Rational basis:')],str(p),'exec'),ns)
n=ns['n'];eta=ns['eta'];K=ns['K'];L=ns['L'];pol=ns['pol'];pairs=ns['pairs'];bs=ns['bs']
print('lower tensors loaded',time.time()-start,flush=True)
hs=[];tk=[];tk_free=[]
p=ROOT/'tests/channel-swings/k2390_full_hook_jet_probe.py';source90=p.read_text();part=source90[source90.index(' for a in range(n):\n  ii='):source90.index(" check('full_pointwise_polar_kernel_basis'")];exec(compile('\n'.join(x[1:] for x in part.splitlines()),str(p),'exec'))
check('polar_rank612_kernel284',len(pb)==612 and len(tk)==284)
W=[{i:v for i,v in [(p,bs[r]),(q,-1-bs[r])] if v} for r,(p,q) in enumerate(pairs)]
prior=json.loads((ROOT/'lab/process/k2390-full-hook-jet.json').read_text());r=prior['four_W_full_quiet_kernel_repair'];alphas=[{i:F(v) for i,v in a} for a in r['transverse_covectors']]
check('all_transverse_covectors_annihilate_W',all(sum(v*w.get(i,0) for i,v in a.items())==0 for a in alphas for w in W))
lw=[{(a,b):add(*[(W[a][i]*W[b][j],L[part][tuple(sorted((i,j)))]) for i in W[a] for j in W[b]]) for a,b in combinations_with_replacement(range(7),2)} for part in range(2)]
ell=[(tuple(q),part,u,tuple(k),F(v)) for (q,part,(u,k)),v in r['lifted_original_receiver_dual']]
check('old_raw_dual_annihilates_all_polar_columns',all(sum(v*pol(h,K[u]).get(k,F(0)) for q,part,u,k,v in ell if q==qq and part==pp)==0 for qq,pp in {(q,part) for q,part,u,k,v in ell} for h in hs))
# C columns for WW Euler; trace rows included as harmless dependencies.
rows=list(combinations_with_replacement(range(n),2));cols={}
for ar,a in enumerate(alphas):
 for hi,h in enumerate(tk):
  col={ij:sum(eta[m]*v*(h.get((ij[0],m,ij[1]),0)+h.get((ij[1],m,ij[0]),0)) for m,v in a.items()) for ij in rows};cols[ar,hi]=clean(col)
# Incremental row elimination of C^T, retaining exact equation combinations.
basis={};records={};colnames=list(cols)
for name in colnames:
 row=dict(cols[name]);hist={}
 while row:
  pivot=min(row);v=row[pivot]
  if pivot not in basis:
   basis[pivot]={k:x/v for k,x in row.items()};records[pivot]=(name,v,hist);break
  hist[pivot]=v
  for k,x in basis[pivot].items():
   z=row.get(k,F(0))-v*x
   if z:row[k]=z
   elif k in row:del row[k]
print('C rank',len(basis),'columns',len(cols),flush=True)
# solve C^T lambda=f, obtaining either multiplier or null-vector witness.
def solve(f):
 values={}
 for p,(name,v,hist) in records.items():values[p]=(f.get(name,F(0))-sum(x*values[q] for q,x in hist.items()))/v
 lam={}
 for p in sorted(basis,reverse=True):lam[p]=values[p]-sum(x*lam.get(k,F(0)) for k,x in basis[p].items() if k!=p)
 for name,col in cols.items():
  residual=f.get(name,F(0))-sum(v*lam.get(k,F(0)) for k,v in col.items())
  if residual:
   # Reconstruct this column as a combination of original pivot columns.
   row=dict(col);used={}
   while row:
    p=min(row);v=row[p];used[p]=v
    for k,x in basis[p].items():
     z=row.get(k,F(0))-v*x
     if z:row[k]=z
     elif k in row:del row[k]
   coeff=defaultdict(F);coeff[name]=1
   for p in reversed(records):
    q=used.get(p,F(0))
    if not q:continue
    orig,v,hist=records[p];coeff[orig]-=q/v
    for j,x in hist.items():used[j]=used.get(j,F(0))-q*x/v
   coeff=clean(coeff)
   check('kernel_witness_C_zero',all(sum(v*cols[j].get(ij,F(0)) for j,v in coeff.items())==0 for ij in rows))
   check('kernel_witness_breaks_dual',sum(v*f.get(j,F(0)) for j,v in coeff.items())==residual)
   return None,coeff,residual
 check('dual_multiplier_all1988_columns',all(sum(v*lam.get(k,F(0)) for k,v in col.items())==f.get(j,F(0)) for j,col in cols.items()))
 return clean(lam),None,F(0)
results=[]
for pair in combinations_with_replacement(range(7),2):
 for ip in range(2):
  f=defaultdict(F)
  for quad,op,u,key,ev in ell:
   lp=op if ip==0 else 1-op;factor=2 if ip==1 and op==0 else 1
   for pos in combinations(range(4),2):
    lt=tuple(quad[i] for i in pos);st=tuple(quad[i] for i in range(4) if i not in pos)
    if st!=pair:continue
    for ar,a in enumerate(alphas):
     av=a.get(u,0)
     if not av:continue
     for hi,h in enumerate(tk):f[ar,hi]-=ev*av*factor*pol(h,lw[lp][lt]).get(key,F(0))
  f=clean(f)
  if not f:continue
  lam,witness,res=solve(f)
  results.append({'W_pair':list(pair),'input_part':ip,'f_nonzero':len(f),'lifted':lam is not None,'multiplier':[[list(k),str(v)] for k,v in (lam or {}).items()],'kernel_witness':[[list(k),str(v)] for k,v in (witness or {}).items()],'dual_change':str(res)})
  print('pair',pair,'part',ip,'lifted',lam is not None,'res',res,flush=True)
# Generic transverse symbols: rank is computed, never inferred from aggregate C.
generic=[]
for co in ([1]*7,[2,3,5,7,11,13,17]):
 xi=add(*[(F(v),a) for v,a in zip(co,alphas)]);sb={}
 for h in tk:
  col=clean({ij:sum(eta[m]*v*(h.get((ij[0],m,ij[1]),0)+h.get((ij[1],m,ij[0]),0)) for m,v in xi.items()) for ij in rows})
  while col:
   p=min(col);v=col[p]
   if p not in sb:sb[p]={k:x/v for k,x in col.items()};break
   for k,x in sb[p].items():
    z=col.get(k,F(0))-v*x
    if z:col[k]=z
    elif k in col:del col[k]
 generic.append({'transverse_coefficients':co,'rank':len(sb)})
 print('generic symbol',co,'rank',len(sb),flush=True)
check('all56_pair_field_inputs_examined',len(list(combinations_with_replacement(range(7),2)))*2==56)
repeated=[hi for hi,h in enumerate(tk) if all(len(set(k))<3 for k in h)];rb={}
for (ar,hi),cc in cols.items():
 if hi not in repeated:continue
 col=dict(cc)
 while col:
  p=min(col);v=col[p]
  if p not in rb:rb[p]={k:x/v for k,x in col.items()};break
  for k,x in rb[p].items():
   z=col.get(k,F(0))-v*x
   if z:col[k]=z
   elif k in col:del col[k]
print('repeated-only C rank',len(rb),'hooks',len(repeated),flush=True)
check('W_second_derivatives_repeated',all(all(len(set(k))<3 for k in h) for part in lw for h in part.values()))
# Complete first A witness through the two remaining Euler blocks.
betas=[{q:F(1)/W[r][q]} for r,(p,q) in enumerate(pairs)]
Es=[{p:F(1)/alphas[r][p]} for r,(p,q) in enumerate(pairs)]
check('adapted_coordinate_inverse',all(sum(v*E.get(i,0) for i,v in a.items())==int(r==u) for r,a in enumerate(alphas) for u,E in enumerate(Es)) and all(sum(v*w.get(i,0) for i,v in b.items())==int(r==u) for r,b in enumerate(betas) for u,w in enumerate(W)))
def contract(h,cov):return clean({ij:sum(eta[m]*v*(h.get((ij[0],m,ij[1]),0)+h.get((ij[1],m,ij[0]),0)) for m,v in cov.items()) for ij in rows})
dbeta={(r,hi):contract(h,b) for r,b in enumerate(betas) for hi,h in enumerate(tk)}
def poly_solve(degree,targets):
 bas={};rec={};original={};count=0
 def reduce_target(target):
  d=dict(target);used={}
  while d:
   p=min(d);v=d[p]
   if p not in bas:return None
   used[p]=v
   for k,x in bas[p].items():
    z=d.get(k,F(0))-v*x
    if z:d[k]=z
    elif k in d:del d[k]
  ans=defaultdict(F)
  for p in reversed(rec):
   if p not in used:continue
   q=used[p];name,v,hist=rec[p];ans[name]+=q/v
   for k,x in hist.items():used[k]=used.get(k,F(0))-q*x/v
  return clean(ans)
 for triple in combinations_with_replacement(range(7),degree):
  for hi in range(len(tk)):
   col={}
   for a in set(triple):
    rest=list(triple);rest.remove(a);rest=tuple(rest)
    for ij,v in cols[a,hi].items():col[rest,ij]=v
   if not col:continue
   name=(triple,hi);original[name]=dict(col);hist={};count+=1
   while col:
    p=min(col);v=col[p]
    if p not in bas:bas[p]={k:x/v for k,x in col.items()};rec[p]=(name,v,hist);break
    hist[p]=v
    for k,x in bas[p].items():
     z=col.get(k,F(0))-v*x
     if z:col[k]=z
     elif k in col:del col[k]
   if count%100==0:
    answers=[reduce_target(t) for t in targets]
    if all(a is not None for a in answers):break
  else:continue
  break
 answers=[reduce_target(t) for t in targets]
 check('completion_degree'+str(degree)+'_solved',all(a is not None for a in answers))
 for ans,target in zip(answers,targets):
  check('completion_degree'+str(degree)+'_column_replay',add(*[(v,original[name]) for name,v in ans.items()])==target)
 print('completion degree',degree,'prefix columns',count,'rank',len(bas),'nonzero',[len(a) for a in answers],flush=True)
 return answers,{'degree':degree,'computed_prefix_columns':count,'computed_prefix_rank':len(bas)}
first=results[0];pair=tuple(first['W_pair']);Avec={(ar,pair,hi):F(v) for (ar,hi),v in first['kernel_witness']}
# targets for seven fixed W slots; mixed Euler receiver indexed by E_r.
btargets=[]
for ss in range(7):
 target=defaultdict(F)
 for (ar,pair,hi),v in Avec.items():
  for tt in range(7):
   if tuple(sorted((ss,tt)))!=pair:continue
   for ij,x in dbeta[tt,hi].items():target[(ar,),ij]-=v*x
 btargets.append(clean(target))
bsol,bmeta=poly_solve(2,btargets)
ctarget=defaultdict(F)
for ss,ans in enumerate(bsol):
 for (pair,hi),v in ans.items():
  for ij,x in dbeta[ss,hi].items():ctarget[pair,ij]-=v*x
csol,cmeta=poly_solve(3,[clean(ctarget)]);csol=csol[0]
# Reconstruct symmetric cubic tensor in original e_a coordinates, independently
# of the column assemblers. Coefficients are actual multilinear values.
from itertools import permutations
fields={t:{} for t in combinations_with_replacement(range(n),3)}
params=[]
for (ar,pair,hi),v in Avec.items():params.append(((ar,7+pair[0],7+pair[1]),hi,v))
for ss,ans in enumerate(bsol):
 for (pair,hi),v in ans.items():params.append(((pair[0],pair[1],7+ss),hi,v))
for (triple,hi),v in csol.items():params.append((triple,hi,v))
covs=alphas+betas
for triple,hi,v in params:
 for inds in set(permutations(triple)):
  for a,va in covs[inds[0]].items():
   for b,vb in covs[inds[1]].items():
    for c,vc in covs[inds[2]].items():
     if a<=b<=c:fields[a,b,c]=add((1,fields[a,b,c]),(v*va*vb*vc,tk[hi]))
for a,b in combinations_with_replacement(range(n),2):
 for i,j in rows:
  val=sum(eta[z]*(fields[tuple(sorted((a,b,z)))].get((i,z,j),0)+fields[tuple(sorted((a,b,z)))].get((j,z,i),0)) for z in range(n))
  if val:raise AssertionError(('direct_full_Euler',a,b,i,j,val))
check('completed_tensor_full_Euler11025_entries',True)
check('completed_tensor_every_value_in_polar_kernel',all(not pol(h,k) for h in fields.values() for k in K))
def eval3(vs):return add(*[(va*vb*vc,fields[tuple(sorted((a,b,c)))]) for a,va in vs[0].items() for b,vb in vs[1].items() for c,vc in vs[2].items()])
check('completed_tensor_all84_W_cubics_zero',all(not eval3([W[a],W[b],W[c]]) for a,b,c in combinations_with_replacement(range(7),3)))
change=F(0)
for quad,op,u,key,ev in ell:
 for pos in combinations(range(4),2):
  lt=tuple(quad[i] for i in pos);st=tuple(quad[i] for i in range(4) if i not in pos)
  h=eval3([W[st[0]],W[st[1]],{u:F(1)}]);change-=ev*pol(h,lw[op][lt]).get(key,F(0))
check('completed_tensor_old_dual_change_direct_replay',change==F(first['dual_change']))
scale=F(r['lifted_original_target_value'])/change
check('one_old_dual_exactly_repaired',scale*change==F(r['lifted_original_target_value']))
# Coefficient mutation genuinely breaks independent Euler identities.
mut=dict(fields);chosen=next(t for t,h in fields.items() if h);mut[chosen]=add((1,mut[chosen]),(1,hs[0]))
changed=any(sum(eta[z]*(mut[tuple(sorted((a,b,z)))].get((i,z,j),0)+mut[tuple(sorted((a,b,z)))].get((j,z,i),0)) for z in range(n)) for a,b in combinations_with_replacement(range(n),2) for i,j in rows)
check('changed_tensor_coefficient_rejected_by_Euler',changed)
completion={'A':first,'B':[[[list(t),hi,str(v)] for (t,hi),v in ans.items()] for ans in bsol],'C':[[list(t),hi,str(v)] for (t,hi),v in csol.items()],'prefix_maps':[bmeta,cmeta],'full_tensor_nonzero':sum(len(h) for h in fields.values()),'old_dual_change':str(change),'one_dual_repair_scale':str(scale),'scope':'full homogeneous Euler and quartic correction, W^3 fixed; exactly one inherited dual repaired, not all420 targets'}
# Reconstruct the original certified tensor from saved coefficients, without
# rerunning its large solve. Verify its exact expansion digest before use.
rho=ns['rho'];tensor=ns['tensor'];lower=ns['prior']
A=[[defaultdict(F) for a in range(n)] for part in range(2)];N=[defaultdict(lambda:defaultdict(F)) for part in range(2)]
for part,partname in enumerate(['rational_solution','sqrt2_solution']):
 for name,x0 in lower[partname]:
  x0=F(x0)
  if name[0]=='A':_,a,u,v=name;A[part][a][u,v]+=x0
  else:
   _,a,b,r0,i0,last=name;dd=[0]*n;dd[i0]=1;dd[last]=-1
   for k0,y0 in tensor(r0,dd).items():N[part][a,b][k0]+=x0*y0
N=[{k0:clean(v0) for k0,v0 in part.items()} for part in N]
def nget(part,a,b):return N[part].get(tuple(sorted((a,b))),{})
def act(part,a,h):return add(*[(v0,rho(h,u,v)) for (u,v),v0 in A[part][a].items()])
S0=[{},{}]
for a,b,c in combinations_with_replacement(range(n),3):
 acc=[defaultdict(F),defaultdict(F)]
 for pa,pb0,out,factor in [(0,0,0,1),(1,1,0,2),(0,1,1,1),(1,0,1,1)]:
  for u,v,w in [(a,b,c),(b,a,c),(c,a,b)]:
   for k0,x0 in act(pa,u,nget(pb0,v,w)).items():acc[out][k0]+=factor*x0
  for u,v,w in [(a,b,c),(a,c,b),(b,c,a)]:
   for k0,x0 in add((F(1,2),act(pa,u,act(pb0,v,K[w]))),(F(1,2),act(pa,v,act(pb0,u,K[w])))).items():acc[out][k0]+=factor*x0
 for part in range(2):S0[part][a,b,c]=clean(acc[part])
nb=[]
for r0,(p,q) in enumerate(pairs):
 avail=[i0 for i0 in range(n) if i0 not in (p,q)];last=avail[-1]
 for i0 in avail[:-1]:
  dd=[0]*n;dd[i0]=1;dd[last]=-1;nb.append(tensor(r0,dd))
S=[{t:dict(h) for t,h in part.items()} for part in S0]
for part,sol in enumerate(prior['solutions']):
 for name,v0 in sol:
  v0=F(v0)
  if name[0] in ('T','Y'):
   typ,a,b,c,idx=name;S[part][a,b,c]=add((1,S[part][a,b,c]),(v0,nb[idx] if typ=='T' else tk[idx]))
  else:
   _,a,b,u,w=name
   for c in range(n):
    tt=tuple(sorted((a,b,c)));mult=sum(tuple(sorted(pp))==(a,b) for pp in [(tt[0],tt[1]),(tt[0],tt[2]),(tt[1],tt[2])]);S[part][tt]=add((1,S[part][tt]),(v0*mult,rho(K[c],u,w)))
expanded=[[[list(t),[[list(k0),str(v0)] for k0,v0 in sorted(h.items())]] for t,h in sorted(part.items()) if h] for part in S]
check('original_S_digest_reconstructed',hashlib.sha256(json.dumps(expanded,sort_keys=True,separators=(',',':')).encode()).hexdigest()==prior['reconstructed_tensor_sha256'])
# Pointwise full polarization image, then every four-W target before/after.
pfb={}
for h in hs:
 col={(u,k0):v0 for u in range(n) for k0,v0 in pol(h,K[u]).items()}
 while col:
  p=min(col);v0=col[p]
  if p not in pfb:pfb[p]={k0:x0/v0 for k0,x0 in col.items()};break
  for k0,x0 in pfb[p].items():
   z=col.get(k0,F(0))-v0*x0
   if z:col[k0]=z
   elif k0 in col:del col[k0]
def quotient(target):
 col=dict(target);out={}
 while col:
  p=min(col);v0=col[p]
  if p not in pfb:out[p]=v0;del col[p];continue
  for k0,x0 in pfb[p].items():
   z=col.get(k0,F(0))-v0*x0
   if z:col[k0]=z
   elif k0 in col:del col[k0]
 return out
def evfield(part,vs):return add(*[(va*vb*vc,part[tuple(sorted((a,b,c)))]) for a,va in vs[0].items() for b,vb in vs[1].items() for c,vc in vs[2].items()])
ws=list(combinations_with_replacement(range(7),3));w2=list(combinations_with_replacement(range(7),2))
sw=[{t:evfield(part,[W[a] for a in t]) for t in ws} for part in S]
swu=[{(t,u):evfield(part,[W[t[0]],W[t[1]],{u:F(1)}]) for t in w2 for u in range(n)} for part in S]
lwu=[{(a,u):add(*[(v0,L[part][tuple(sorted((i0,u)))]) for i0,v0 in W[a].items()]) for a in range(7) for u in range(n)} for part in range(2)]
def original_target(quad,part):
 out=defaultdict(F)
 for u in range(n):
  for a in range(4):
   st=tuple(quad[i0] for i0 in range(4) if i0!=a)
   for pa,pb0,fac in ([(0,0,1),(1,1,2)] if part==0 else [(0,1,1),(1,0,1)]):
    for k0,v0 in pol(sw[pa][st],lwu[pb0][quad[a],u]).items():out[u,k0]-=fac*v0
  for pos in combinations(range(4),2):
   lt=tuple(quad[i0] for i0 in pos);st=tuple(quad[i0] for i0 in range(4) if i0 not in pos)
   for pa,pb0,fac in ([(0,0,1),(1,1,2)] if part==0 else [(0,1,1),(1,0,1)]):
    for k0,v0 in pol(swu[pa][st,u],lw[pb0][lt]).items():out[u,k0]-=fac*v0
 return clean(out)
before=[];after=[];raw_dual=F(0);after_dual=F(0)
for quad in combinations_with_replacement(range(7),4):
 for part in range(2):
  orig=original_target(quad,part);delta=defaultdict(F)
  for u in range(n):
   for pos in combinations(range(4),2):
    lt=tuple(quad[i0] for i0 in pos);st=tuple(quad[i0] for i0 in range(4) if i0 not in pos)
    h=eval3([W[st[0]],W[st[1]],{u:F(1)}])
    for k0,v0 in pol(h,lw[part][lt]).items():delta[u,k0]-=scale*v0
  new=add((1,orig),(1,clean(delta)));qb=quotient(orig);qa=quotient(new)
  if qb:before.append([list(quad),part])
  if qa:after.append([list(quad),part])
  for qq,pp,u,key,ev in ell:
   if qq==quad and pp==part:raw_dual+=ev*orig.get((u,key),0);after_dual+=ev*new.get((u,key),0)
check('original420_targets_replayed_13_fail',len(before)==13)
check('old_dual_target_directly_recomputed',-raw_dual==F(r['lifted_original_target_value']))
check('repaired_old_dual_direct_all_receiver_replay',after_dual==0)
completion['four_W_before_failures']=before;completion['four_W_after_failures']=after;completion['remaining_failed_field_targets']=len(after)
print('four-W after full correction',len(after),'of420 fail',flush=True)
# Exact common quotient for ALL distinct A coefficients, not supportwise quiet.
def reduce_repeated(cc):
 col=dict(cc);res={}
 while col:
  p=min(col);v0=col[p]
  if p not in rb:res[p]=v0;del col[p];continue
  for k0,x0 in rb[p].items():
   z=col.get(k0,F(0))-v0*x0
   if z:col[k0]=z
   elif k0 in col:del col[k0]
 return res
distinct=[hi for hi in range(len(tk)) if hi not in repeated];dnames=[(ar,hi) for ar in range(7) for hi in distinct];qcols={j:reduce_repeated(cols[name]) for j,name in enumerate(dnames)}
qrows=defaultdict(dict)
for j,col in qcols.items():
 for key,v0 in col.items():qrows[key][j]=v0
qb={}
for row in qrows.values():
 row=dict(row)
 while row:
  p=min(row);v0=row[p]
  if p not in qb:qb[p]={k0:x0/v0 for k0,x0 in row.items()};break
  for k0,x0 in qb[p].items():
   z=row.get(k0,F(0))-v0*x0
   if z:row[k0]=z
   elif k0 in row:del row[k0]
kn=[]
for free in range(len(dnames)):
 if free in qb:continue
 coords={free:F(1)}
 for p in sorted(qb,reverse=True):
  val=-sum(x0*coords.get(j,F(0)) for j,x0 in qb[p].items() if j!=p)
  if val:coords[p]=val
 check('reduced_kernel_column_replay',not add(*[(v0,qcols[j]) for j,v0 in coords.items()]))
 kn.append(coords)
check('full_common_quotient_rank15_kernel846',len(qb)==15 and len(kn)==846 and len(dnames)==861)
check('repeated_hooks_sigma_with_all_WW_zero',all(all(k0==() for k0 in pol(tk[hi],h)) for hi in repeated for part in lw for h in part.values()))
# Primitive polynomial coefficient check underlying the written prolongation proof.
y0,y2,y3=sp.symbols('y0 y2 y3')
check('primitive_quadratic_symbol_gcd',sp.gcd(sp.gcd(y0*y2,y0*y3),y2*y3)==1)
reduction={'repeated_WW_rank':len(rb),'full_WW_rank':len(basis),'distinct_columns':len(dnames),'quotient_rank':len(qb),'common_kernel_dimension':len(kn),'W_pairs':28,'full_reduced_field_coordinates':28*len(kn),'kernel_free_columns':[next(j for j,v0 in kk.items() if j not in qb) for kk in kn],'kernel_sha256':hashlib.sha256(json.dumps([[[j,str(v0)] for j,v0 in sorted(kk.items())] for kk in kn],separators=(',',':')).encode()).hexdigest(),'scope':'exact full pointwise-polar fixed-W3 reduction; resulting23688-column coupled four-W system not solved'}
report={'result':'K2393','completion':completion,'full_family_reduction':reduction,'scope':'Full homogeneous Euler/quartic correction with zero W-cubic restriction repairs one stored dual; complete four-W replay leaves24 failed field-part targets, so no full coupled fifth repair.','C_rows_including_trace':len(rows),'C_columns':len(cols),'C_rank':len(basis),'generic_symbols':generic,'repeated_C_rank':len(rb),'repeated_hooks':len(repeated),'polar_basis_free':tk_free,'old_dual_target':r['lifted_original_target_value'],'tests':results,'all_nonzero_tests_lift':all(z['lifted'] for z in results),'checks':checks,'dependencies':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [ROOT/'tests/channel-swings/k2387_coupled_hook_jet_blocks_probe.py',ROOT/'tests/channel-swings/k2390_full_hook_jet_probe.py',ROOT/'lab/process/k2390-full-hook-jet.json',ROOT/'lab/process/k2381-rotated-null-hook-prolongation.json']}}
if '--write' in sys.argv:(ROOT/'lab/process/k2393-coupled-polar-dual.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print(json.dumps(report,sort_keys=True))
