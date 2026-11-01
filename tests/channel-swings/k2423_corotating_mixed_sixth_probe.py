"""Co-rotating original finite-jet discriminator, exact Q(sqrt(2)) arithmetic."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict,Counter
from itertools import permutations
import json,hashlib,sys
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'tests/channel-swings/k2405_fifth_euler_compatibility_probe.py';src=p.read_text()
exec(compile(src[:src.index('# Pair-field covariant derivative')],str(p),'exec'),globals())
inherited_checks=dict(checks);checks={};controls={}
def ck(k,v):
 checks[k]=bool(v)
 if not v:raise AssertionError(k)
def ctrl(k,v):
 controls[k]=bool(v)
 if not v:raise AssertionError(k)
r20=json.loads((ROOT/'lab/process/k2420-coupled-nuisance-image.json').read_text())
solution=r20['actual_affine_target']['solution']
ck('all571_repair_terms_repeated',len(solution)==571 and all(all(len(set(k))<3 for k in tk[name[1]]) for name,co in solution))
# This proves repaired and baseline cubic have identical distinct components.
A=[defaultdict(dict),defaultdict(dict)];r81=json.loads((ROOT/'lab/process/k2381-rotated-null-hook-prolongation.json').read_text())
for ip,key in enumerate(['rational_solution','sqrt2_solution']):
 for name,c in r81[key]:
  if name[0]=='A':
   _,a,u,v=name;A[ip][a]=add((1,A[ip][a]),(F(c),{(u,v):F(1)}))
def pad(out,m,c,h):
 out[m]=add((1,out.get(m,{})),(c,h))
 if not out[m]:del out[m]
def combine(a,b,c):
 out=[dict(p) for p in a]
 for ip in range(2):
  for m,h in b[ip].items():pad(out[ip],m,c,h)
 return out
def rotate(h,a):return add(*[(v,rho(h,u,w)) for (u,w),v in a.items()])
def aop(P):
 out=[{},{}]
 for pa,pb,ip,c in [(0,0,0,1),(1,1,0,2),(0,1,1,1),(1,0,1,1)]:
  for r,aa in A[pa].items():
   for mon,h in P[pb].items():pad(out[ip],tuple(sorted((r,)+mon)),c,rotate(h,aa))
 return out
def diagonal(T):return [{m:add((len(set(permutations(m))),h)) for m,h in part.items() if h} for part in T]
def distinct(P):return [{m:{k:v for k,v in h.items() if len(set(k))==3} for m,h in part.items() if any(len(set(k))==3 for k in h)} for part in P]
kap=[{(i,):h for i,h in enumerate(K) if h},{}];ell=diagonal(L);ess=diagonal(S)
nn=combine(ell,aop(kap),-2);ck('full_L_corotates_to_repeated',not any(distinct(nn)))
sbar=combine(combine(ess,aop(ell),-3),aop(aop(kap)),3)
# Original transverse covectors and W frame, independent of temporary symbols.
rr90=json.loads((ROOT/'lab/process/k2390-full-hook-jet.json').read_text())
alphas=[{i:F(v) for i,v in row} for row in rr90['four_W_full_quiet_kernel_repair']['transverse_covectors']]
W=[]
for r,(p0,q0) in enumerate(pairs):
 den=alphas[r].get(p0,F(0))-alphas[r].get(q0,F(0))
 W.append({i:v/den for i,v in [(p0,alphas[r].get(q0,F(0))),(q0,-alphas[r].get(p0,F(0)))] if v})
ck('all_W_annihilate_K',all(not add(*[(v,K[i]) for i,v in w.items()]) for w in W))
# Evaluate every W3 coefficient directly; higher rotation B*K vanishes there.
def eval_slots(T,slots):
 out={}
 from itertools import product
 for inds in product(*[list(v.items()) for v in slots]):
  ids=tuple(sorted(x[0] for x in inds));c=F(1)
  for _,v in inds:c*=v
  out=add((1,out),(c,T.get(ids,{})))
 return out
# sbar is ordinary polynomial coefficients; convert to derivative values first.
sbt=[{m:add((F(1,len(set(permutations(m)))),h)) for m,h in part.items()} for part in sbar]
w3=[{},{}]
for ip in range(2):
 for t in combinations_with_replacement(range(7),3):
  h=eval_slots(sbt[ip],[W[i] for i in t]);dh={k:v for k,v in h.items() if len(set(k))==3}
  if dh:w3[ip][t]=dh
print('DISTINCT',[(len(x),sum(map(len,x.values()))) for x in distinct(sbar)],'W3',[(len(x),sum(map(len,x.values()))) for x in w3],flush=True)
report={'result_id':'K2423','checks':checks,'controls':controls,'inherited_checks':inherited_checks,'corotated_distinct_cubic_counts':[(len(x),sum(map(len,x.values()))) for x in distinct(sbar)],'W3_distinct_counts':[(len(x),sum(map(len,x.values()))) for x in w3], 'W3_distinct':[[[list(m),[[list(k),str(v)] for k,v in sorted(h.items())]] for m,h in sorted(part.items())] for part in w3]}

# Test whether ANY quadratic frame rotation can remove the first mixed sector.
# Symmetric derivative convention: Sbar(e,w,w)=rho(B(w,w))K(e).
Es=[{p:F(1)/alphas[r][p]} for r,(p,q) in enumerate(pairs)]
KE=[add(*[(v,K[i]) for i,v in e.items()]) for e in Es]
rots=list(combinations(range(n),2));basis={};lifts={}
for idx,(u,v) in enumerate(rots):
 col={(e,k):x for e,h in enumerate(KE) for k,x in rho(h,u,v).items() if len(set(k))==3};lift={idx:F(1)}
 while col:
  p=min(col);x=col[p]
  if p not in basis:
   basis[p]={k:v/x for k,v in col.items()};lifts[p]={k:v/x for k,v in lift.items()};break
  col=add((1,col),(-x,basis[p]));lift=add((1,lift),(-x,lifts[p]))
fails=[];sols=[]
for ip in range(2):
 for ww in combinations_with_replacement(range(7),2):
  target={(e,k):x for e in range(7) for k,x in eval_slots(sbt[ip],[Es[e],W[ww[0]],W[ww[1]]]).items() if len(set(k))==3};res=dict(target);sol={}
  for p,b in sorted(basis.items()):
   x=res.get(p,F(0))
   if x:res=add((1,res),(-x,b));sol=add((1,sol),(x,lifts[p]))
  if res:
   k=min(res);fails.append({'field':ip,'W_pair':list(ww),'residual_entries':len(res),'first_key':[k[0],list(k[1])],'first_value':str(res[k])})
  else:sols.append([ip,list(ww),[[i,str(v)] for i,v in sorted(sol.items())]])
print('W2E rotation rank',len(basis),'failed',len(fails),'of56','first',fails[:1],flush=True)
report['W2E_rotation']={'rank':len(basis),'columns':len(rots),'targets':56,'failures':fails,'solutions':sols}

# Next independent sector E2W. Store full lifts; original replay validates solutions.
rotcols=[{(e,k):x for e,h in enumerate(KE) for k,x in rho(h,u,v).items() if len(set(k))==3} for u,v in rots]
def reduce_columns(cols):
 bas={};lif={}
 for name,col0 in cols:
  col=dict(col0);li={name:F(1)}
  while col:
   p=min(col);x=col[p]
   if p not in bas:
    bas[p]={k:v/x for k,v in col.items()};lif[p]={k:v/x for k,v in li.items()};break
   col=add((1,col),(-x,bas[p]));li=add((1,li),(-x,lif[p]))
 return bas,lif
e2=list(combinations_with_replacement(range(7),2))
def e2cols():
 for r in range(7):
  for idx,col in enumerate(rotcols):
   out={}
   for ee in e2:
    for pos in range(2):
     if ee[pos]==r:
      other=ee[1-pos]
      for (e,k),v in col.items():
       if e==other:out[(ee,k)]=out.get((ee,k),F(0))+v
   yield (r,idx),clean(out)
b2,l2=reduce_columns(e2cols());f2=[];ss2=[]
for ip in range(2):
 for w in range(7):
  target={(ee,k):v for ee in e2 for k,v in eval_slots(sbt[ip],[Es[ee[0]],Es[ee[1]],W[w]]).items() if len(set(k))==3};res=dict(target);sol={}
  for p,b in sorted(b2.items()):
   v=res.get(p,F(0))
   if v:res=add((1,res),(-v,b));sol=add((1,sol),(v,l2[p]))
  if res:
   key=min(res);f2.append({'field':ip,'W':w,'residual_entries':len(res),'first_key':[list(key[0]),list(key[1])],'first_value':str(res[key])})
  else:ss2.append([ip,w,[[list(k),str(v)] for k,v in sorted(sol.items())]])
print('E2W rotation rank',len(b2),'failed',len(f2),'of14','first',f2[:1],flush=True)
report['E2W_rotation']={'rank':len(b2),'columns':637,'targets':14,'failures':f2,'solutions':ss2}

e3=list(combinations_with_replacement(range(7),3))
def e3cols():
 for pair in e2:
  for idx,col in enumerate(rotcols):
   out={}
   for triple in e3:
    for pos in range(3):
     selected=tuple(triple[j] for j in range(3) if j!=pos)
     if selected==pair:
      for (e,k),v in col.items():
       if e==triple[pos]:out[(triple,k)]=out.get((triple,k),F(0))+v
   yield (pair,idx),clean(out)
b3,l3=reduce_columns(e3cols());f3=[];ss3=[]
for ip in range(2):
 target={(ee,k):v for ee in e3 for k,v in eval_slots(sbt[ip],[Es[e] for e in ee]).items() if len(set(k))==3};res=dict(target);sol={}
 for p,b in sorted(b3.items()):
  v=res.get(p,F(0))
  if v:res=add((1,res),(-v,b));sol=add((1,sol),(v,l3[p]))
 if res:
  key=min(res);f3.append({'field':ip,'residual_entries':len(res),'first_key':[list(key[0]),list(key[1])],'first_value':str(res[key])})
 else:ss3.append([ip,[[[list(k[0]),k[1]],str(v)] for k,v in sorted(sol.items())]])
print('E3 rotation rank',len(b3),'failed',len(f3),'of2','first',f3[:1],flush=True)
report['E3_rotation']={'rank':len(b3),'columns':2548,'targets':2,'failures':f3,'solutions':ss3}

# Reconstruct one shared quadratic rotation in ambient coordinates.
Ba=[{},{}]
for ip,ww,sol in sols:
 Ba[ip][tuple(7+w for w in ww)]={rots[i]:F(v) for i,v in sol}
for ip,w,sol in ss2:
 for (r,idx),v in sol:pad(Ba[ip],(r,7+w),F(v),{rots[idx]:F(1)})
for ip,sol in ss3:
 for (pair,idx),v in sol:pad(Ba[ip],tuple(pair),F(v),{rots[idx]:F(1)})
vec=Es+W;frame=sp.Matrix([[sp.Rational(vec[j].get(i,0)) for j in range(n)] for i in range(n)]);covs=[{j:F(v) for j,v in enumerate(row) if v} for row in frame.inv().tolist()]
Bamb=[{},{}]
for ip,part in enumerate(Ba):
 for tr,h in part.items():
  for ids in set(permutations(tr)):
   for aa,va in covs[ids[0]].items():
    for bb,vb in covs[ids[1]].items():
     if aa<=bb:pad(Bamb[ip],(aa,bb),va*vb,h)
Bpoly=diagonal(Bamb)
def op_poly(rotpoly,P):
 out=[{},{}]
 for pa,pb,ip,c in [(0,0,0,1),(1,1,0,2),(0,1,1,1),(1,0,1,1)]:
  for mon,a in rotpoly[pa].items():
   for mon2,h in P[pb].items():pad(out[ip],tuple(sorted(mon+mon2)),c,rotate(h,a))
 return out
bk=op_poly(Bpoly,kap);tt=combine(sbar,bk,-3)
ck('all_ambient_baseline_cubic_repeated_after_two_rotations',not any(distinct(tt)))
# Reconstruct K2420's actual ambient repair and check its exact stored digest.
deltaS=[{t:{} for t in combinations_with_replacement(range(n),3)} for ip in range(2)]
for (tr,hi),coeff in solution:
 for ids in set(permutations(tr)):
  for aa,va in covs[ids[0]].items():
   for bb,vb in covs[ids[1]].items():
    for cc,vc in covs[ids[2]].items():
     if aa<=bb<=cc:
      for ip in range(2):
       if F(coeff[ip]):deltaS[ip][aa,bb,cc]=add((1,deltaS[ip][aa,bb,cc]),(F(coeff[ip])*va*vb*vc,tk[hi]))
repaired=[{t:add((1,h),(1,deltaS[ip][t])) for t,h in part.items()} for ip,part in enumerate(S)]
ck('actual_repaired_cubic_digest',digest(repaired)==r20['actual_affine_target']['repaired_ambient_cubic_sha256'])
Trep=combine(tt,diagonal(deltaS),1)
ck('actual_repaired_cubic_repeated_frame',not any(distinct(Trep)))
ctrl('omitting_quadratic_rotation_fails',any(distinct(sbar)))
ctrl('wrong_cubic_rotation_factor_fails',any(distinct(combine(sbar,bk,-2))))
# Original reconstruction in ambient polynomial coordinates, with noncommuting order.
rebuild=combine(combine(combine(Trep,bk,3),aop(nn),3),aop(aop(kap)),3)
ck('all_original_repaired_cubic_entries_reconstructed',not any(combine(rebuild,diagonal(repaired),-1)))
# Full repeated space, independently verify its pairwise sigma-null property.
rep168=[h for h in hs if all(len(set(k))<3 for k in h)]
ck('all_repeated_pairings_sigma_zero',len(rep168)==168 and all(all(k==() for k in pol(a,b)) for i,a in enumerate(rep168) for b in rep168[i:]))
report['repeated_frame']={'repaired_cubic_sha256':digest(repaired),'ambient_B':[[[list(m),[[list(k),str(v)] for k,v in sorted(h.items())]] for m,h in sorted(part.items())] for part in Bamb],'ambient_repeated_T_sha256':digest([{m:add((F(1,len(set(permutations(m)))),h)) for m,h in part.items()} for part in Trep])}
# Load only the original W4 Phi solve, not a prior full elimination.
import ast
p08=ROOT/'tests/channel-swings/k2408_joint_cubic_compatibility_probe.py';st08=p08.read_text()
for node in ast.parse(st08).body:
 if isinstance(node,ast.FunctionDef) and node.name=='final_fourW_target':exec(compile(ast.Module(body=[node],type_ignores=[]),str(p08),'exec'),globals())
w2=list(combinations_with_replacement(range(7),2));ws=list(combinations_with_replacement(range(7),3));W4=list(combinations_with_replacement(range(7),4))
lw=[{t:eval_slots(part,[W[i] for i in t]) for t in w2} for part in L]
lwu=[{(a,u):eval_slots(part,[W[a],{u:F(1)}]) for a in range(7) for u in range(n)} for part in L]
sc3=[{t:eval_slots(part,[W[i] for i in t]) for t in ws} for part in S];sc2=[{(t,u):eval_slots(part,[W[t[0]],W[t[1]],{u:F(1)}]) for t in w2 for u in range(n)} for part in S]
p02=ROOT/'tests/channel-swings/k2402_coupled_polar_compatibility_probe.py';st02=p02.read_text()
exec(compile(st02[st02.index('phi={};prec={}'):st02.index('def target6(')],str(p02),'exec'),globals())
r02=json.loads((ROOT/'lab/process/k2402-coupled-polar-compatibility.json').read_text())
for (qi,hi,ip),v in r02['mixed_all_W_sixth_extension']['polar_solution']:U0[ip][W4[qi]]=add((1,U0[ip][W4[qi]]),(F(v),tk[hi]))
# K2420 changes W4 only by repeated hooks, hence this is exactly its distinct W4.
Jorth=[{tuple(k):F(v) for k,v in h} for h in r20['actual_affine_target']['all_W_sixth_followthrough']['orthogonal_duals']]
ck('K2420_W4_change_repeated',all(len(set(k))<3 for h in Jorth for k in h))
# Restrict ordinary polynomials before multiplication to keep the calculation small.
def wrestrict(P,degree):
 deriv=[{m:add((F(1,len(set(permutations(m)))),h)) for m,h in part.items()} for part in P]
 return [{m:add((len(set(permutations(m))),eval_slots(part,[W[i] for i in m]))) for m in combinations_with_replacement(range(7),degree)} for part in deriv]
Aw=[{(r,):add(*[(v,A[ip][i]) for i,v in w.items()]) for r,w in enumerate(W)} for ip in range(2)]
Bw=[{m:add((len(set(permutations(m))),Ba[ip].get(tuple(7+i for i in m),{}))) for m in w2} for ip in range(2)]
Nw=wrestrict(nn,2);Tw=wrestrict(Trep,3)
u0w=combine(combine([{},{}],op_poly(Aw,Tw),4),op_poly(Bw,Nw),6);u0w=combine(u0w,op_poly(Aw,op_poly(Aw,Nw)),6)
actualUw=diagonal(U0);wdiff=distinct(combine(actualUw,u0w,-1))
print('fixed W4 distinct residual',[(len(p),sum(map(len,p.values()))) for p in wdiff],flush=True)
report['fixed_W4_distinct_residual_counts']=[(len(p),sum(map(len,p.values()))) for p in wdiff]

# All four null rotations, recovered against ORIGINAL91 columns.
nullrots=[]
for idx,col0 in enumerate(rotcols):
 res=dict(col0);sol={}
 for p,b in sorted(basis.items()):
  v=res.get(p,F(0))
  if v:res=add((1,res),(-v,b));sol=add((1,sol),(v,lifts[p]))
 ker=add((1,{idx:F(1)}),(-1,sol))
 if ker:nullrots.append(ker)
ck('all_four_null_rotations',len(nullrots)==4 and all(not add(*[(v,rotcols[i]) for i,v in ker.items()]) for ker in nullrots))
nullmat=[add(*[(v,{rots[i]:F(1)}) for i,v in ker.items()]) for ker in nullrots]
nonrep=[(j,ip,mon) for j,rot in enumerate(nullmat) for ip in range(2) for mon,h in Nw[ip].items() if any(len(set(k))==3 for k in rotate(h,rot))]
print('kernel acts nonrepeated N',len(nonrep),flush=True)
report['quadratic_rotation_kernel']={'dimension':len(nullmat),'basis':[[[list(k),str(v)] for k,v in sorted(a.items())] for a in nullmat],'nonrepeated_N_actions':len(nonrep)}
# Complete realified112-field-coordinate map, using polynomial multiplicities.
cols112=[]
for mon in w2:
 for j,rot in enumerate(nullmat):
  for ip in range(2):
   rp=[{},{}];rp[ip][mon]=add((len(set(permutations(mon))),rot));delta=distinct(op_poly(rp,Nw));flat={(op,m,k):6*v for op,part in enumerate(delta) for m,h in part.items() for k,v in h.items()};cols112.append(((mon,j,ip),flat))
b112,l112=reduce_columns(cols112);raw={(ip,m,k):v for ip,part in enumerate(wdiff) for m,h in part.items() for k,v in h.items()};res=dict(raw);sol={}
for p,b in sorted(b112.items()):
 v=res.get(p,F(0))
 if v:res=add((1,res),(-v,b));sol=add((1,sol),(v,l112[p]))
print('full W4 frame kernel rank',len(b112),'residual',len(res),flush=True)
obstruction=None
if res:
 obs=min(res);du={obs:F(1)}
 for p in sorted(b112,reverse=True):
  v=-sum(x*du.get(k,F(0)) for k,x in b112[p].items() if k!=p)
  if v:du[p]=v
 ck('W4_raw_dual_annihilates_all224_original_columns',all(sum(v*col.get(k,F(0)) for k,v in du.items())==0 for name,col in cols112))
 value=sum(v*raw.get(k,F(0)) for k,v in du.items());ck('W4_raw_dual_nonzero_actual_target',value==res[obs] and value!=0)
 obstruction={'dual':[[ip,list(m),list(k),str(v)] for (ip,m,k),v in sorted(du.items())],'value':str(value)}
report['complete_W4_frame_kernel']={'field_parameters':112,'realified_columns':len(cols112),'rank':len(b112),'residual_entries':len(res),'obstruction':obstruction,'solution':[[[list(m),j,ip],str(v)] for (m,j,ip),v in sorted(sol.items())] if not res else None}

# Execute the admissible changed-W4 repair, rather than stop at the fixed-witness exclusion.
ck('K2402_full_W4_digest',digest(U0)==r02['mixed_all_W_sixth_extension']['quartic_W4_sha256'])
newsc3=[{t:eval_slots(part,[W[i] for i in t]) for t in ws} for part in repaired];newsc2=[{(t,u):eval_slots(part,[W[t[0]],W[t[1]],{u:F(1)}]) for t in w2 for u in range(n)} for part in repaired]
ck('repaired_W3_exactly_unchanged',newsc3==sc3)
oldW4=[{} for ip in range(2)];targets=[{} for ip in range(2)]
for ip in range(2):
 for q in W4:
  old=final_fourW_target(q,ip,sc3,sc2);want=final_fourW_target(q,ip,newsc3,newsc2);dd=add((1,want),(-1,old));ck('changed_Phi_Gram_only',all(k==() for u,k in dd))
  coeff=[sum(v*dd.get((u,()),F(0)) for u,v in e.items()) for e in Es];dh=add(*zip(coeff,Jorth));oldW4[ip][q]=add((1,U0[ip][q]),(1,dh));targets[ip][q]=want
ck('K2420_full_W4_digest',digest(oldW4)==r20['actual_affine_target']['all_W_sixth_followthrough']['quartic_W4_sha256'])
ck('current_W4_same_distinct_residual',distinct(combine(diagonal(oldW4),u0w,-1))==wdiff)
frameW4=[{} for ip in range(2)];innerW4=[{} for ip in range(2)]
for ip in range(2):
 for q in W4:
  forced=add((F(1,len(set(permutations(q)))),u0w[ip].get(q,{})));diff=add((1,oldW4[ip][q]),(-1,forced));rep={k:v for k,v in diff.items() if len(set(k))<3};innerW4[ip][q]=rep;frameW4[ip][q]=add((1,forced),(1,rep))
ck('all420_new_W4_original_Phi',all({(u,k):v for u in range(n) for k,v in pol(frameW4[ip][q],K[u]).items()}==targets[ip][q] for q in W4 for ip in range(2)))
ck('new_W4_preserves_all_repeated_Gram_pairings',all(not pol(k,add((1,frameW4[ip][q]),(-1,oldW4[ip][q]))).get((),F(0)) for q in W4 for ip in range(2) for k in KE+[h for part in lw for h in part.values()]))
exec(compile(st02[st02.index('def target6('):st02.index('# Exact555-coefficient witness')],str(p02),'exec'),globals())
W6=list(combinations_with_replacement(range(7),6));ck('all1848_new_W4_original_sixth',all(not target6(q,ip,frameW4) for q in W6 for ip in range(2)))
ctrl('fixed_W4_change_is_essential',digest(frameW4)!=digest(oldW4))
report['changed_W4_repair']={'old_current_digest':digest(oldW4),'new_digest':digest(frameW4),'original_Phi_field_targets':420,'original_all_W_sixth_field_targets':1848,'inner_repeated_W4':[[[list(m),[[list(k),str(v)] for k,v in sorted(h.items())]] for m,h in sorted(part.items())] for part in innerW4],'scope':'Explicit replacement W4 matches the same repaired cubic, all original Phi and all-W sixth targets, and the fixed repeated-frame construction. A simultaneous full frame-quartic Euler solve remains open.'}
# Structural follow-through: compare the repeated-polar Euler symbol with full103.
rep161=[h for h in tk if all(len(set(k))<3 for k in h)]
def symbol(h,xi):return clean({(i,j):sum(eta[a]*v*(h.get((i,a,j),F(0))+h.get((j,a,i),F(0))) for a,v in xi.items()) for i,j in combinations_with_replacement(range(n),2)})
xi={i:F(i+1) for i in range(n)}
rb,_=reduce_columns([(j,symbol(h,xi)) for j,h in enumerate(rep161)])
cb,_=reduce_columns([((r,j),symbol(h,a)) for r,a in enumerate(alphas) for j,h in enumerate(rep161)])
cubic_rotation_cols=[]
for ri,(u,v) in enumerate(rots):
 col={}
 for a in range(n):col=add((1,col),(1,symbol(rho(K[a],u,v),{a:F(1)})))
 cubic_rotation_cols.append((('rotation',ri),col))
combined,_=reduce_columns([((r,j),symbol(h,a)) for r,a in enumerate(alphas) for j,h in enumerate(rep161)]+cubic_rotation_cols)
print('repeated plus third rotation boundary Euler image',len(combined),flush=True)
report['third_rotation_boundary_Euler_rank']=len(combined)
print('repeated polar symbol rank',len(rb),'transverse C image',len(cb),flush=True)
report['repeated_polar_Euler_diagnostic']={'constant_polar_dimension':len(rep161),'generic_covector':list(map(str,xi.values())),'symbol_rank':len(rb),'transverse_C_image_rank':len(cb),'scope':'Exact two finite maps; no all-degree or fixed-W4 Euler image conclusion.'}
ck('complete_cubic_sectors_pass',not any(w3) and len(sols)==56 and len(ss2)==14 and len(ss3)==2)
# Original repeated Gram duals for constructive fifth/sixth ideal division.
GM=sp.Matrix([[sp.Rational(pol(k,h).get((),0)) for h in rep168] for k in KE]);gp=GM.rref()[1];GI=GM[:,list(gp)].inv();Jr=[add(*[(F(GI[j,r]),rep168[hi]) for j,hi in enumerate(gp)]) for r in range(7)]
ck('original_repeated_Gram_duals',all(pol(KE[i],Jr[j])==({():F(1)} if i==j else {}) for i in range(7) for j in range(7)))
# Scalar normalization and transverse support for monomial ideal division.
for deg,factor,mons in [(5,5,[(0,0,7,8,9),(1,2,7,7,7)]),(6,6,[(0,7,7,8,9,10),(1,1,2,7,8,9)])]:
 for mon in mons:
  r=next(i for i in mon if i<7);rem=list(mon);rem.remove(r);co=F(7,13)
  ck('Gram_ideal_division_degree'+str(deg),factor*pol(KE[r],add((-co/factor,Jr[r]))).get((),0)==-co)
  if deg==5:ck('quartic_ideal_correction_preserves_W4',any(i<7 for i in rem))
report['algebraic_completion']='The repaired K,L,S and changed W4 admit one formal fifth/sixth-algebraic quartic/quintic: repeated inner frame makes sigma identically zero; repeated Gram duals divide degree5 residual of E-degree>=2 and degree6 residual of E-degree>=1. Fourth Euler on that SAME quartic remains unresolved.'
report['scope']='Same repaired cubic has an explicit two-rotation repeated frame and formal all-order sigma-null extension. The old fixed W4 is excluded for every second rotation at fixed A by a224-column original dual. An actual changed W4 repairs that mismatch and passes420 Phi and1848 all-W sixth targets. A shared full fifth/sixth algebraic extension follows by repeated Gram ideal division; fourth Euler on that same quartic remains open. No smooth Euler solution or native GU claim.'
report['dependencies']={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps+['tests/channel-swings/k2405_fifth_euler_compatibility_probe.py','tests/channel-swings/k2408_joint_cubic_compatibility_probe.py','tests/channel-swings/k2402_coupled_polar_compatibility_probe.py','lab/process/k2402-coupled-polar-compatibility.json','lab/process/k2420-coupled-nuisance-image.json']}
report['software']={'sympy':sp.__version__};report=json.loads(json.dumps(report));out=ROOT/'lab/process/k2423-corotating-mixed-sixth.json'
if '--write' in sys.argv:out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
else:assert json.loads(out.read_text())==report
print(json.dumps({'checks':len(checks),'controls':len(controls),'changed_W4':report['changed_W4_repair']['new_digest'],'status':'pass'}))
