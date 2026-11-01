"""Exact combined nuisance image; original Euler/J derivative coordinates."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from itertools import combinations_with_replacement,product,permutations
import json,hashlib,sys,time
ROOT=Path(__file__).resolve().parents[2]
p05=ROOT/'tests/channel-swings/k2405_fifth_euler_compatibility_probe.py';src=p05.read_text();exec(compile(src[:src.index('# Search exact realified D2 and J')],str(p05),'exec'),globals())
inherited=dict(checks);inherited_deps=list(deps);checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ctrl(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
zq=(F(0),F(0));oq=(F(1),F(0))
def qa(a,b):return (a[0]+b[0],a[1]+b[1])
def qneg(a):return (-a[0],-a[1])
def qm(a,b):return (a[0]*b[0]+2*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def qi(a):
 den=a[0]*a[0]-2*a[1]*a[1];assert den;return (a[0]/den,-a[1]/den)
def qs(a,c):return (a[0]*c,a[1]*c)
def accum(out,k,v):
 v=qa(out.get(k,zq),v)
 if v!=zq:out[k]=v
 else:out.pop(k,None)
# Exactly the inherited coframe, assembled without replaying the full three-W solve.
w_alphas=[{i:F(v) for i,v in aa} for aa in json.loads((ROOT/'lab/process/k2390-full-hook-jet.json').read_text())['four_W_full_quiet_kernel_repair']['transverse_covectors']]
W=[{i:v/(w_alphas[r].get(p,F(0))-w_alphas[r].get(q,F(0))) for i,v in [(p,w_alphas[r].get(q,F(0))),(q,-w_alphas[r].get(p,F(0)))] if v} for r,(p,q) in enumerate(pairs)]
Es=[{p:F(1)/w_alphas[r][p]} for r,(p,q) in enumerate(pairs)];vec=Es+W
vm=sp.Matrix([[sp.Rational(v.get(a,0)) for v in vec] for a in range(n)]);ci=vm.inv();covs=[{a:F(str(ci[i,a])) for a in range(n) if ci[i,a]} for i in range(n)]
ck('actual_adapted_coframe',all(sum(co.get(a,0)*v for a,v in vec[j].items())==int(i==j) for i,co in enumerate(covs) for j in range(n)))
pairs14=list(combinations_with_replacement(range(14),2));pairid={p:i for i,p in enumerate(pairs14)};assert list(receivers)==pairs14;JBASE=11025
repeated=[h for h,tensor0 in enumerate(tk) if all(len(set(k))<3 for k in tensor0)];rep_set=set(repeated);distinct=[h for h in range(len(tk)) if h not in rep_set]
ck('complete_hook_split',len(repeated)==161 and len(distinct)==123 and all(all(len(set(k))==3 for k in tk[h]) for h in distinct))
triples=list(combinations_with_replacement(range(n),3));adapted=[t for t in triples if t[0]<7]
co_at=[[(r,F(covs[r][a])) for r in range(n) if covs[r].get(a,0)] for a in range(n)]
Jad={}
for row,fun in enumerate(Jfs):
 for (abc,hk),coef in fun.items():
  coef=tuple(map(F,coef))
  for ia,ib,ic in product(*(co_at[a] for a in abc)):
   t=tuple(sorted((ia[0],ib[0],ic[0])))
   if t[0]>=7:continue
   accum(Jad.setdefault((t,hk),{}),row,qs(coef,ia[1]*ib[1]*ic[1]))
Jad={k:v for k,v in Jad.items() if v};Dcov={}
for r in range(n):
 for hi,hook in enumerate(tk):
  dd=defaultdict(F)
  for (i,z,j),value in hook.items():
   c=F(covs[r].get(z,0))
   if c:dd[pairid[tuple(sorted((i,j)))]]+=eta[z]*c*value*(2 if i==j else 1)
  Dcov[r,hi]={k:v for k,v in dd.items() if v}
def combined_column(t,hi,wrong_multiplicity=False):
 outcol={}
 for r in set(t):
  rest=list(t);rest.remove(r);base=105*pairid[tuple(rest)]
  for ij,val in Dcov[r,hi].items():accum(outcol,base+ij,(val*(t.count(r) if wrong_multiplicity else 1),F(0)))
 for hk,val in tk[hi].items():
  for row,co in Jad.get((t,hk),{}).items():accum(outcol,JBASE+row,qs(co,val))
 return outcol

def original_column(t,hi):
 native={}
 for abc in triples:
  fac=sum(sp.prod(covs[r].get(a,0) for r,a in zip(ids,abc)) for ids in set(permutations(t)))
  if fac:native[abc]={hk:F(fac)*val for hk,val in tk[hi].items()}
 raw={}
 for ab in pairs14:
  for ij in receivers:
   i,j=ij;val=sum(eta[z]*(native.get(tuple(sorted((*ab,z))),{}).get((i,z,j),0)+native.get(tuple(sorted((*ab,z))),{}).get((j,z,i),0)) for z in range(n))
   if val:raw[ab,ij]=val
 result={}
 for ab in pairs14:
  for ij in receivers:
   val=sum(va*vb*raw.get((tuple(sorted((a,b))),ij),0) for a,va in vec[ab[0]].items() for b,vb in vec[ab[1]].items())
   if val:result[105*pairid[ab]+pairid[ij]]=(val,F(0))
 for row,fun in enumerate(Jfs):
  val=zq
  for (abc,hk),co in fun.items():val=qa(val,qs(co,native.get(abc,{}).get(hk,F(0))))
  if val!=zq:result[JBASE+row]=val
 return result,native
fixtures=[]
for t in [(0,0,7),(0,7,7),(0,1,7),(0,0,0),(0,0,1)]:
 for hi in [repeated[0],repeated[-1],distinct[0],distinct[-1]]:
  raw,native=original_column(t,hi);col=combined_column(t,hi);assert raw==col,(t,hi);fixtures.append((t,hi))
ck('twenty_original_ambient_Euler_J_columns',len(fixtures)==20)
ctrl('occurrence_multiplier_changes_original_operator',any(combined_column(t,h,True)!=combined_column(t,h) for t,h in fixtures))
# Independent original curved defect difference, including the sqrt2 field part.
mt0={(a,b,c):MP(a,b,c,T=S) for a,b,c in product(range(n),repeat=3)}
base_def={ab:defect(*ab,MT=mt0) for ab in receivers};mixed=[{t:dict(h) for t,h in part.items()} for part in S];linear={}
for ip,t,hi,scale in [(0,(0,0,7),repeated[-1],F(2)),(1,(0,1,7),distinct[-1],F(3))]:
 col,native=original_column(t,hi)
 for abc,hook in native.items():mixed[ip][abc]=add((1,mixed[ip][abc]),(scale,hook))
 for row,v in col.items():
  if row>=JBASE:accum(linear,row,qm((scale,F(0)) if ip==0 else (F(0),scale),v))
mt1={(a,b,c):MP(a,b,c,T=mixed) for a,b,c in product(range(n),repeat=3)}
ck('actual_curved_defect_mixed_field_replay',all(qa(defect(*ab,MT=mt1),qneg(base_def[ab]))==linear.get(JBASE+i,zq) for i,ab in enumerate(receivers)))
class ExactImage:
 def __init__(self):self.basis={};self.records={};self.order=[];self.examined=0
 def reduce(self,source):
  col=dict(source);used={};res={}
  while col:
   pivot=min(col);factor=col[pivot]
   if pivot not in self.basis:res[pivot]=col.pop(pivot);continue
   used[pivot]=factor
   for row,val in self.basis[pivot].items():accum(col,row,qneg(qm(factor,val)))
  return res,used
 def insert(self,name,source):
  residual,used=self.reduce(source);self.examined+=1
  if not residual:return False
  pivot=min(residual);scale=residual[pivot];inv=qi(scale);self.basis[pivot]={r:qm(v,inv) for r,v in residual.items()};self.records[pivot]=(name,scale,used);self.order.append(pivot);return True
 def solve(self,source):
  residual,used=self.reduce(source)
  if residual:return None,residual
  weights=dict(used);answer={}
  for p in reversed(self.order):
   amount=weights.pop(p,zq)
   if amount==zq:continue
   name,scale,hist=self.records[p];co=qm(amount,qi(scale));accum(answer,name,co)
   for prev,factor in hist.items():accum(weights,prev,qneg(qm(co,factor)))
  assert not weights;return answer,{}
 def raw_dual(self,weights):
  assert not set(weights)&set(self.basis);dual=dict(weights)
  for p in sorted(self.basis,reverse=True):
   v=zq
   for row,co in self.basis[p].items():
    if row!=p:v=qa(v,qm(co,dual.get(row,zq)))
   if v!=zq:dual[p]=qneg(v)
  return dual

def names():
 for wc in (0,1,2):
  for t in adapted:
   if sum(i>=7 for i in t)!=wc:continue
   for hi in (range(len(tk)) if wc==0 else repeated):yield t,hi
image=ExactImage();stage_ranks={};started=time.monotonic()
for name in names():
 image.insert(name,combined_column(*name))
 if image.examined%2000==0:print('nuisance',image.examined,'rank',len(image.basis),'seconds',round(time.monotonic()-started),flush=True,file=sys.stderr)
 if image.examined in (23856,55412,86968):stage_ranks[str(image.examined)]=len(image.basis)
ck('complete_nuisance_columns',image.examined==86968)
# Exact basis reconstruction witnesses, using both field components.
source={}
for j,pivot in enumerate(image.order[::max(1,len(image.order)//19)]):
 name=image.records[pivot][0];co=(F(j+1,7),F(j%3,5))
 for row,val in combined_column(*name).items():accum(source,row,qm(co,val))
sol,res=image.solve(source);replay={}
for name,co in sol.items():
 for row,val in combined_column(*name).items():accum(replay,row,qm(co,val))
ck('original_column_back_substitution',not res and replay==source)
# A deterministic cokernel sample, with full original-column annihilation.
nonp=[r for r in range(11130) if r not in image.basis];dual=image.raw_dual({nonp[0]:oq})
def pairing(ell,col):
 v=zq
 for row,co in col.items():v=qa(v,qm(ell.get(row,zq),co))
 return v
ck('full_original_nuisance_dual_annihilation',all(pairing(dual,combined_column(*name))==zq for name in names()))
ctrl('planted_outside_image_rejected',image.solve({nonp[0]:oq})[0] is None)
# Reconstruct the original lower Euler target, then test the actual affine J defect.
exec(compile(s90[s90.index('def fp('):s90.index('# Direct quartic checker')],str(p90),'exec'),globals())
ck('actual_baseline_all22050_Euler_entries',all(DS(S,ip,a,b,i,j)==Etarget[ip].get(ri[a,b,i,j],F(0)) for a,b,i,j in rows for ip in range(2)))
affine={JBASE+i:qneg(out[ab]) for i,ab in enumerate(receivers) if out[ab]!=zq}
actual_sol,actual_res=image.solve(affine);affine_report={'nuisance_feasible':actual_sol is not None,'quotient_residual_entries':len(actual_res)}
if actual_sol is None:
 obs=min(actual_res);ell=image.raw_dual({obs:oq});val=pairing(ell,affine)
 ck('actual_target_dual_nonzero',val==actual_res[obs] and val!=zq)
 ck('actual_target_dual_all86968_columns',all(pairing(ell,combined_column(*name))==zq for name in names()))
 affine_report.update(raw_dual=[(r,list(map(str,v))) for r,v in sorted(ell.items())],target_pairing=list(map(str,val)))
else:
 rep={}
 for name,co in actual_sol.items():
  for row,v in combined_column(*name).items():accum(rep,row,qm(co,v))
 ck('actual_target_original_replay',rep==affine)
 affine_report['solution']=[([list(name[0]),name[1]],list(map(str,co))) for name,co in actual_sol.items()]
# Retain the full distinct A/B lower compatibility map, not one chosen A projection.
reduced=ExactImage()
for tr in adapted:
 if sum(i>=7 for i in tr) not in (1,2):continue
 for hi in distinct:reduced.insert((tr,hi),image.reduce(combined_column(tr,hi))[0])
ck('all48216_distinct_AB_columns',reduced.examined==48216)
dsol,dres=reduced.solve(actual_res)
ck('full_lower_affine_family_feasible',dsol is not None and not dres)
# Independent original full-family back-substitution of the actual affine target.
remaining=dict(affine)
for name,co in dsol.items():
 for row,v in combined_column(*name).items():accum(remaining,row,qneg(qm(co,v)))
nsol,nres=image.solve(remaining);assert nsol is not None and not nres
replay={}
for sol0 in [dsol,nsol]:
 for name,co in sol0.items():
  for row,v in combined_column(*name).items():accum(replay,row,qm(co,v))
ck('complete_lower_affine_original_columns_replayed',replay==affine)
affine_report.update(distinct_AB_quotient_rank=len(reduced.basis),remaining_identity_rows=11130-len(image.basis)-len(reduced.basis),full_lower_solution_terms=len(dsol)+len(nsol))
# Stronger follow-through: can a wholly repeated ABC correction repair J?
# If so K2417 preserves every algebraic sector with one shared primitive.
repeat_image=ExactImage()
for tr in adapted:
 for hi in repeated:repeat_image.insert((tr,hi),combined_column(tr,hi))
rsol,rres=repeat_image.solve(affine)
repeat_report={'columns':repeat_image.examined,'rank':len(repeat_image.basis),'feasible':rsol is not None,'residual_entries':len(rres)}
ck('all76636_repeated_ABC_columns',repeat_image.examined==76636)
ck('repeated_image_equals_full_nuisance_image',len(repeat_image.basis)==len(image.basis))
ck('actual_affine_target_repeated_only_feasible',rsol is not None and not rres)
if rsol is not None:
 rreplay={}
 for name,co in rsol.items():
  for row,v in combined_column(*name).items():accum(rreplay,row,qm(co,v))
 ck('repeated_only_original_column_reconstruction',rreplay==affine)
 dsol={};nsol=rsol
 repeat_report['solution_terms']=len(rsol)
 affine_report['solution']=[([list(name[0]),name[1]],list(map(str,co))) for name,co in rsol.items()]
 affine_report['full_lower_solution_terms']=len(rsol)
else:
 obs=min(rres);ell=repeat_image.raw_dual({obs:oq});value=pairing(ell,affine)
 ck('repeated_only_dual_all76636_columns',all(pairing(ell,combined_column(tr,hi))==zq for tr in adapted for hi in repeated))
 ck('repeated_only_dual_actual_target_nonzero',value==rres[obs] and value!=zq)
 repeat_report.update(raw_dual=[(r,list(map(str,v))) for r,v in sorted(ell.items())],target_pairing=list(map(str,value)))
affine_report['all_repeated_attempt']=repeat_report
print('repeated-only',repeat_report['rank'],repeat_report['feasible'],flush=True)

# Reconstruct the complete ambient cubic, not only the reduced matrix solution.
full_delta=[{tr:{} for tr in triples} for _ in range(2)]
for solution0 in [dsol,nsol]:
 for (tr,hi),co in solution0.items():
  for ids in set(permutations(tr)):
   for aa,va in covs[ids[0]].items():
    for bb,vb in covs[ids[1]].items():
     for cc,vc in covs[ids[2]].items():
      if aa<=bb<=cc:
       for ip in range(2):
        if co[ip]:full_delta[ip][aa,bb,cc]=add((1,full_delta[ip][aa,bb,cc]),(co[ip]*va*vb*vc,tk[hi]))
repaired=[{tr:add((1,S[ip][tr]),(1,full_delta[ip][tr])) for tr in triples} for ip in range(2)]
ck('reconstructed_all22050_original_Euler_entries',all(DS(repaired,ip,a,b,i,j)==Etarget[ip].get(ri[a,b,i,j],F(0)) for a,b,i,j in rows for ip in range(2)))
repairedM={(a,b,c):MP(a,b,c,T=repaired) for a,b,c in product(range(n),repeat=3)}
ck('reconstructed_all105_actual_curved_J_zero',all(defect(*ab,MT=repairedM)==zq for ab in receivers))
affine_report['repaired_ambient_cubic_sha256']=digest(repaired)
affine_report['ambient_delta_entries']=[sum(map(len,part.values())) for part in full_delta]
affine_report['full_lower_rank']=len(image.basis)+len(reduced.basis)
affine_report['full_lower_kernel_dimension']=135184-len(image.basis)-len(reduced.basis)
affine_report['distinct_AB_kernel_dimension']=48216-len(reduced.basis)
# Outcome follow-through on the SAME repaired ambient cubic. The loaded K2402
# anchor passed all algebraic sectors; its J repair must be tested at that anchor.
p08=ROOT/'tests/channel-swings/k2408_joint_cubic_compatibility_probe.py';s08=p08.read_text()
def section08(a,b):exec(compile(s08[s08.index(a):s08.index(b)],str(p08),'exec'),globals())
Snew=repaired
section08('w_alphas=','fivebad=[]')
section08('pfb={}','new3=[')
section08('alphas=w_alphas','three=all_threeW')
ck('same_cubic_all420_four_W',not all_fourW(repaired))
three_replay=all_threeW(repaired)
ck('same_cubic_all168_three_W',not three_replay['failed_targets'])
ck('same_cubic_fixed_W3',all(not evfield(part,[W[a] for a in tr]) for part in full_delta for tr in ws))
# Every two-W quartic column, then every actual target, with an original dual.
p99=ROOT/'tests/channel-swings/k2399_complete_polar_joint_lift_probe.py';s99=p99.read_text()
exec(compile(s99[s99.index('ET=list('):s99.index('failed2=[]')],str(p99),'exec'),globals())
exec(compile(s99[s99.index('def replay_twoW('):s99.index("nc('C_escape_complete56_replay'")],str(p99),'exec'),globals())
two_replay=replay_twoW(repaired);first2=None
ck('same_cubic_all56_two_W_evaluated',len(two_replay['failed_targets'])<=56)
if two_replay['failed_targets']:
 wp,op=two_replay['failed_targets'][0];raw=target2(wp,op,repaired);cc=dict(raw);res={}
 while cc:
  k=min(cc);v=cc[k]
  if k not in bas2:res[k]=v;del cc[k];continue
  for j,x in bas2[k].items():
   z=cc.get(j,F(0))-v*x
   if z:cc[j]=z
   elif j in cc:del cc[j]
 obs=min(res);du={obs:F(1)}
 for k in sorted(bas2,reverse=True):
  v=-sum(x*du.get(j,F(0)) for j,x in bas2[k].items() if j!=k)
  if v:du[k]=v
 ck('two_W_dual_all25088_original_columns',annihilates_twoW(du))
 value=sum(v*raw.get(k,F(0)) for k,v in du.items())
 ck('two_W_dual_actual_repaired_cubic_nonzero',value==res[obs] and value!=0)
 first2={'W_pair':wp,'field_part':op,'dual':[[list(et),list(k),str(v)] for (et,k),v in sorted(du.items())],'value':str(value)}
affine_report['algebraic_followthrough']={'four_W_failures':[],'three_W':three_replay,'two_W':two_replay,'two_W_map_rank':len(bas2),'two_W_first_obstruction':first2,'scope':'Same lower-Euler/J repaired cubic passes four-W and three-W; two-W result tests this representative only, not all lower-compatible cubics.'}

# Preserve the inherited complete all-W sixth witness at the NEW cubic.
# Independent original Gram duals: dual to KE, orthogonal to all L(W,W).
Lww=[eval_L(ip,[7+a,7+b]) for ip in range(2) for a,b in w2]
rep_hooks=[h for h in hs if all(len(set(k))<3 for k in h)]
ck('full_repeated_hook_space168',len(rep_hooks)==168)
G=sp.Matrix([[sp.Rational(pol(k,h).get((),0)) for h in rep_hooks] for k in KE+Lww])
rowidx=G.T.rref()[1];GR=G[list(rowidx),:];colidx=GR.rref()[1];GI=GR[:,list(colidx)].inv()
ck('K_and_LWW_combined_Gram_rank18',len(rowidx)==18 and list(rowidx[:7])==list(range(7)))
Jorth=[]
for rr in range(7):
 rhs=sp.Matrix([int(i==rr) for i in rowidx]);coeff=GI*rhs
 Jorth.append(add(*[(F(str(coeff[j])),rep_hooks[hi]) for j,hi in enumerate(colidx)]))
ck('original_KE_orthogonal_Gram_duals',all(pol(k,h)==({():F(1)} if i==j else {}) for i,k in enumerate(KE) for j,h in enumerate(Jorth)))
ck('original_all56_LWW_annihilate_duals',all(not pol(k,h) for k in Lww for h in Jorth))
ck('LWW_Gram_constraints_nontrivial',any(pol(k,h) for k in Lww for h in rep_hooks))
p02=ROOT/'tests/channel-swings/k2402_coupled_polar_compatibility_probe.py';s02=p02.read_text();old02=json.loads((ROOT/'lab/process/k2402-coupled-polar-compatibility.json').read_text())
e6=dict(globals());e6['repaired']=S
exec(compile(s02[s02.index('W4=list('):s02.index('# Exact555-coefficient witness')],str(p02),'exec'),e6)
W4=e6['W4'];W6=e6['W6'];oldU=[{q:dict(h) for q,h in part.items()} for part in e6['U0']]
for (qi,hi,ip),vv in old02['mixed_all_W_sixth_extension']['polar_solution']:
 q=W4[qi];oldU[ip][q]=add((1,oldU[ip][q]),(F(vv),tk[hi]))
newsc3=[{tr:evfield(part,[W[a] for a in tr]) for tr in ws} for part in repaired]
newsc2=[{(tr,u):evfield(part,[W[tr[0]],W[tr[1]],{u:F(1)}]) for tr in w2 for u in range(n)} for part in repaired]
ck('actual_W3_unchanged_for_sixth',newsc3==e6['sc3'])
newU=[{} for _ in range(2)];deltaU=[{} for _ in range(2)]
for ip in range(2):
 for q in W4:
  prev=final_fourW_target(q,ip,e6['sc3'],e6['sc2']);want=final_fourW_target(q,ip,newsc3,newsc2)
  dd=add((1,want),(-1,prev));assert all(key==() for u,key in dd)
  coeff=[sum(v*dd.get((u,()),F(0)) for u,v in ev.items()) for ev in Es]
  dh=add(*zip(coeff,Jorth));deltaU[ip][q]=dh;newU[ip][q]=add((1,oldU[ip][q]),(1,dh))
  assert {(u,k):v for u in range(n) for k,v in pol(dh,K[u]).items()}==dd
  assert {(u,k):v for u in range(n) for k,v in pol(newU[ip][q],K[u]).items()}==want
ck('new_shared_W4_all420_original_Phi_targets',True)
ck('all_quartic_corrections_annihilate_original_LWW',all(not pol(k,h) for k in Lww for part in deltaU for h in part.values()))
ck('new_shared_W4_all1848_original_sixth_targets',all(not e6['target6'](q,op,newU) for q in W6 for op in range(2)))
ctrl('old_quartic_fails_changed_Phi',any(final_fourW_target(q,ip,e6['sc3'],e6['sc2'])!=final_fourW_target(q,ip,newsc3,newsc2) for q in W4 for ip in range(2)))
# Fourth-Euler compatibility is on unchanged K,L; replay its original14 rows.
exec(compile(s02[s02.index('# Recompute the inherited actual curvature/Bianchi'):s02.index('algrank=')],str(p02),'exec'),e6)
ck('unchanged_KL_all14_quartic_curved_compatibilities',all(a==0 and b==0 for a,b in e6['compat']))
encU=[[[list(q),[[list(k),str(v)] for k,v in sorted(h.items())]] for q,h in sorted(part.items()) if h] for part in newU]
affine_report['all_W_sixth_followthrough']={'combined_Gram_rank':len(rowidx),'orthogonal_duals':[[[list(k),str(v)] for k,v in sorted(h.items())] for h in Jorth],'quartic_W4_sha256':hashlib.sha256(json.dumps(encU,sort_keys=True,separators=(',',':')).encode()).hexdigest(),'quartic_W4_entries':[sum(map(len,part.values())) for part in newU],'changed_Phi_field_targets':420,'sixth_all_W_field_targets':1848,'fourth_Euler_curved_receivers':14,'scope':'New repeated cubic and constructed W4 quartic values pass original Phi/all-W sixth. Written shared primitive and W4-preserving Euler-image theorem give a shared fourth-Euler/fifth-algebraic extension retaining these W4 values. All105 next-Euler J conditions hold. Mixed sixth/shared fifth-Euler completion remains open.'}

# Every original column was reduced; basis and triangular expressions are reproducible.
enc=[(p,[(r,list(map(str,v))) for r,v in sorted(image.basis[p].items())]) for p in sorted(image.basis)]
report={'result_id':'K2420','checks':checks,'controls':controls,'inherited_lower_checks':len(inherited),'field':'Q(sqrt2)','nuisance_columns':image.examined,'nuisance_rank':len(image.basis),'nuisance_kernel_dimension':image.examined-len(image.basis),'codomain_rows':11130,'cokernel_dimension':11130-len(image.basis),'stage_ranks':stage_ranks,'retained_distinct_AB_columns':48216,'basis_sha256':hashlib.sha256(json.dumps(enc,separators=(',',':')).encode()).hexdigest(),'sample_raw_dual':[(r,list(map(str,v))) for r,v in sorted(dual.items())],'actual_affine_target':affine_report,'scope':'Exact complete repeated-AB/all-C lower Euler/J image with original-coordinate controls and back-substitution. Repeated-only repair admits shared fourth-Euler/fifth-algebraic extension with original all-W sixth and105 next-Euler J conditions; mixed sixth/shared fifth-Euler completion remains unresolved.'}
deps=inherited_deps+['tests/channel-swings/k2402_coupled_polar_compatibility_probe.py','tests/channel-swings/k2408_joint_cubic_compatibility_probe.py','tests/channel-swings/k2399_complete_polar_joint_lift_probe.py','tests/channel-swings/k2405_fifth_euler_compatibility_probe.py','lab/process/k2390-full-hook-jet.json','explorations/conditional-build/k2417-coupled-three-w-compatibility-2026-10-31.md'];report['dependencies']={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps};out=ROOT/'lab/process/k2420-coupled-nuisance-image.json'
# Compare the JSON representation: sparse coefficient records use tuples internally.
report=json.loads(json.dumps(report))
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
elif '--verify-only' not in sys.argv:
 saved=json.loads(out.read_text());assert saved==report,[k for k in report if saved.get(k)!=report[k]]
print(json.dumps({k:report[k] for k in ['nuisance_columns','nuisance_rank','cokernel_dimension','basis_sha256']}))
