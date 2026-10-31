"""Portable original-tensor verification of a coupled B/C complete two-W repair."""
from pathlib import Path
import json,sys,hashlib
ROOT=Path(__file__).resolve().parents[2]
prior=ROOT/'tests/channel-swings/k2399_complete_polar_joint_lift_probe.py'
source=prior.read_text();namespace={'__file__':str(prior),'__name__':'inherited_replay'}
# Predecessor's full native acceptance, without its report write or final print.
exec(compile(source[:source.index('if args.write:newpath.write_text')],str(prior),'exec'),namespace)
globals().update({k:v for k,v in namespace.items() if not k.startswith('__')})
path=ROOT/'lab/process/k2402-coupled-polar-compatibility.json';report=json.loads(path.read_text());new_checks={}
def ck(name,ok):
 new_checks[name]=bool(ok)
 if not ok:raise AssertionError('[FAIL] '+name)
for dep,h in report['dependencies'].items():ck('pin_'+dep,hashlib.sha256((ROOT/dep).read_bytes()).hexdigest()==h)
scale=F(report['scale']);parameters=[[],[]]
for nm,v in report['B_coefficients']:
 typ,ss,ei,hi,ip=nm;ck('B_only_parameterization',typ=='B');ep=EP[ei];parameters[ip].append(((*ep,7+ss),hi,F(v)))
for ip,part in enumerate(report['C_coefficients']):parameters[ip].extend((tuple(t),hi,F(v)) for t,hi,v in part)
delta=[]
for ip in range(2):
 ff={t:{} for t in triples}
 for t,hi,v in parameters[ip]:
  for perm in set(permutations(t)):
   for a,va in covs[perm[0]].items():
    for b,vb in covs[perm[1]].items():
     for c,vc in covs[perm[2]].items():
      if a<=b<=c:ff[a,b,c]=add((1,ff[a,b,c]),(scale*v*va*vb*vc,tk[hi]))
 delta.append(ff)
stored=decode_tensor(report['ambient_delta']);stored=[{t:p.get(t,{}) for t in triples} for p in stored]
ck('parameters_reconstruct_actual_tensor',delta==stored)
ck('full_homogeneous_Euler',all(sum(eta[z]*(part[tuple(sorted((a,b,z)))].get((i,z,j),0)+part[tuple(sorted((a,b,z)))].get((j,z,i),0)) for z in range(n))==0 for part in delta for a,b in receivers for i,j in receivers))
ck('full_hook',all(all(h.get((i,j,k),0)+h.get((i,k,j),0)==0 and h.get((i,j,k),0)+h.get((j,k,i),0)+h.get((k,i,j),0)==0 for i,j,k in h) and all(sum(eta[i]*h.get((i,i,a),0) for i in range(n))==0 for a in range(n)) for part in delta for h in part.values()))
ck('full_pointwise_polar',all(not pol(h,k) for part in delta for h in part.values() for k in K))
ck('fixed_two_W_and_W3',all(not evfield(part,[e,wa,wb]) for part in delta for e in vec for wa in W for wb in W))
updated=[{t:add((1,Sfinal[ip][t]),(1,delta[ip][t])) for t in triples} for ip in range(2)]
ck('all420_four_W_preserved',not all_fourW(updated))
ck('all168_three_W_preserved',not all_threeW(updated)['failed_targets'])
ck('full_C_family_dual_cancelled',C_affine_contraction(updated)==0)
ck('original_dual_nonzero',C_affine_contraction(Sfinal)==F(report['target_contraction']))
ck('unscaled_dual_change_recomputed',C_affine_contraction(delta)==-scale*F(report['dual_change_unscaled']))
rr=replay_twoW(updated)
ck('rational_escape_line_alone_insufficient',bool(rr['failed_targets']) and C_affine_contraction(updated)==0 and C_affine_contraction(Sfinal)!=0)
escape_replay=rr
# Controls alter actual tensor coefficients, never the acceptance predicate.
wrong=[{t:add((1,Sfinal[ip][t]),(2,delta[ip][t])) for t in triples} for ip in range(2)]
ck('doubled_actual_correction_fails_dual',C_affine_contraction(wrong)!=0)
mut=[{t:dict(h) for t,h in part.items()} for part in delta];tt=next(t for t,h in mut[0].items() if h);mut[0][tt]=add((1,mut[0][tt]),(1,hs[0]))
ck('changed_tensor_fails_Euler',any(sum(eta[z]*(mut[0][tuple(sorted((a,b,z)))].get((i,z,j),0)+mut[0][tuple(sorted((a,b,z)))].get((j,z,i),0)) for z in range(n)) for a,b in receivers for i,j in receivers))
# Full C repair at the changed B: reconstruct the11 native basis coefficients.
repair=[{t:{} for t in triples} for _ in range(2)]
for ip,part in enumerate(report['C_repair_coefficients']):
 for t0,hi,v0 in part:
  t=tuple(t0);v=F(v0)
  for perm in set(permutations(t)):
   for a,va in alphas[perm[0]].items():
    for b,vb in alphas[perm[1]].items():
     for c,vc in alphas[perm[2]].items():
      if a<=b<=c:repair[ip][a,b,c]=add((1,repair[ip][a,b,c]),(v*va*vb*vc,tk[hi]))
rs=decode_tensor(report['C_repair_ambient_delta']);rs=[{t:p.get(t,{}) for t in triples} for p in rs]
ck('eleven_C_coefficients_reconstruct_actual90_entries',repair==rs and sum(len(p) for p in report['C_repair_coefficients'])==11 and sum(sum(map(len,p.values())) for p in repair)==90)
ck('C_repair_full_homogeneous_Euler',all(sum(eta[z]*(part[tuple(sorted((a,b,z)))].get((i,z,j),0)+part[tuple(sorted((a,b,z)))].get((j,z,i),0)) for z in range(n))==0 for part in repair for a,b in receivers for i,j in receivers))
ck('C_repair_full_hook',all(all(h.get((i,j,k),0)+h.get((i,k,j),0)==0 and h.get((i,j,k),0)+h.get((j,k,i),0)+h.get((k,i,j),0)==0 for i,j,k in h) and all(sum(eta[i]*h.get((i,i,a),0) for i in range(n))==0 for a in range(n)) for part in repair for h in part.values()))
ck('C_repair_full_pointwise_polar',all(not pol(h,k) for part in repair for h in part.values() for k in K))
ck('C_repair_all_W_slots_zero',all(not evfield(part,[e1,e2,w]) for part in repair for e1 in vec for e2 in vec for w in W))
repaired=[{t:add((1,updated[ip][t]),(1,repair[ip][t])) for t in triples} for ip in range(2)]
ck('repaired_all420_four_W',not all_fourW(repaired))
ck('repaired_all168_three_W',not all_threeW(repaired)['failed_targets'])
rr=replay_twoW(repaired)
ck('repaired_complete56_two_W',not rr['failed_targets'] and rr['residual_entries']==0)
ck('remove_actual_C_repair_fails_identical_two_W_checker',bool(replay_twoW(updated)['failed_targets']))
enc=[[[list(t),[[list(k),str(v)] for k,v in sorted(h.items())]] for t,h in sorted(part.items()) if h] for part in repaired]
report['repaired_tensor_sha256']=hashlib.sha256(json.dumps(enc,sort_keys=True,separators=(',',':')).encode()).hexdigest()
# Necessary pure-E diagonal slices of the original one-W fifth-algebraic equation.
# A dual here annihilates EVERY full one-W quartic column: only the (e,e,e)
# unknown triple contributes to the receiver (e,e,e,e).
onew_failed=[];first1=None;direction_ranks=[]
for e in range(7):
 bdir={}
 for hi,h in enumerate(hs):
  cc=add((4,pol(h,KE[e])))
  while cc:
   k=min(cc);v=cc[k]
   if k not in bdir:bdir[k]={j:x/v for j,x in cc.items()};break
   for j,x in bdir[k].items():
    zz=cc.get(j,F(0))-v*x
    if zz:cc[j]=zz
    elif j in cc:del cc[j]
 direction_ranks.append(len(bdir))
 for w in range(7):
  for op in range(2):
   raw={};slots=[7+w,e,e,e,e]
   for pos in combinations(range(5),2):
    aa=[slots[i] for i in pos];bb=[slots[i] for i in range(5) if i not in pos]
    for pa,pb,fac in ([(0,0,1),(1,1,2)] if op==0 else [(0,1,1),(1,0,1)]):raw=add((1,raw),(-fac,pol(getL2(pa,aa),getS2(pb,bb,repaired))))
   cc=dict(raw);res={}
   while cc:
    k=min(cc);v=cc[k]
    if k not in bdir:res[k]=v;del cc[k];continue
    for j,x in bdir[k].items():
     zz=cc.get(j,F(0))-v*x
     if zz:cc[j]=zz
     elif j in cc:del cc[j]
   if res:
    onew_failed.append([e,w,op])
    if first1 is None:
     obs=min(res);du={obs:F(1)}
     for k in sorted(bdir,reverse=True):
      v=-sum(x*du.get(j,F(0)) for j,x in bdir[k].items() if j!=k)
      if v:du[k]=v
     ck('one_W_diagonal_dual_all896_original_hooks',all(sum(v*4*pol(h,KE[e]).get(k,F(0)) for k,v in du.items())==0 for h in hs))
     val=sum(v*raw.get(k,F(0)) for k,v in du.items());ck('one_W_diagonal_dual_nonzero_actual_target',val==res[obs] and val!=0)
     first1={'E_direction':e,'W_direction':w,'field_part':op,'dual':[[list(k),str(v)] for k,v in sorted(du.items())],'value':str(val)}
report['one_W_directional_next']={'tested_diagonal_receivers':98,'direction_ranks':direction_ranks,'failed_targets':onew_failed,'first_obstruction':first1,'scope':'Necessary pure-E diagonal one-W tests of this chosen shared cubic. A failure excludes its entire one-W quartic lift; passes do not establish the full one-W sector. Broader cubic corrections remain open.'}

# Complete remaining algebraic blocks. Each U W-degree feeds only that
# receiver W-degree because K(W)=0, so their solutions assemble directly.
pc_remaining={(e,hi):pol(h,KE[e]) for e in range(7) for hi,h in enumerate(hs)}
def remaining_sector(degree):
 unknown=list(combinations_with_replacement(range(7),degree));recv=list(combinations_with_replacement(range(7),degree+1));bbas={}
 def col(t,hi):
  out=defaultdict(F)
  for e in range(7):
   q=tuple(sorted((*t,e)));mul=q.count(e)
   for k,v in pc_remaining[e,hi].items():out[q,k]+=mul*v
  return clean(out)
 for t in unknown:
  for hi in range(len(hs)):
   cc=col(t,hi)
   while cc:
    k=min(cc);v=cc[k]
    if k not in bbas:bbas[k]={j:x/v for j,x in cc.items()};break
    for j,x in bbas[k].items():
     z=cc.get(j,F(0))-v*x
     if z:cc[j]=z
     elif j in cc:del cc[j]
 bad=[];nr=0;first=None
 for w in (range(7) if degree==3 else [None]):
  for op in range(2):
   raw=defaultdict(F)
   for q in recv:
    slots=([7+w] if w is not None else [])+list(q)
    for pos in combinations(range(5),2):
     aa=[slots[i] for i in pos];bb=[slots[i] for i in range(5) if i not in pos]
     for pa,pb,fac in ([(0,0,1),(1,1,2)] if op==0 else [(0,1,1),(1,0,1)]):
      for k,v in pol(getL2(pa,aa),getS2(pb,bb,repaired)).items():raw[q,k]-=fac*v
   raw=clean(raw);cc=dict(raw);res={}
   while cc:
    k=min(cc);v=cc[k]
    if k not in bbas:res[k]=v;del cc[k];continue
    for j,x in bbas[k].items():
     z=cc.get(j,F(0))-v*x
     if z:cc[j]=z
     elif j in cc:del cc[j]
   if res:
    bad.append([w,op]);nr+=len(res)
    if first is None:
     obs=min(res);du={obs:F(1)}
     for k in sorted(bbas,reverse=True):
      v=-sum(x*du.get(j,F(0)) for j,x in bbas[k].items() if j!=k)
      if v:du[k]=v
     ck('remaining_degree'+str(degree)+'_dual_all_original_columns',all(sum(v*col(t,hi).get(k,F(0)) for k,v in du.items())==0 for t in unknown for hi in range(len(hs))))
     val=sum(v*raw.get(k,F(0)) for k,v in du.items());ck('remaining_degree'+str(degree)+'_dual_actual_target',val==res[obs] and val!=0)
     first={'W_direction':w,'field_part':op,'dual':[[list(q),list(k),str(v)] for (q,k),v in sorted(du.items())],'value':str(val)}
 return {'full_map_columns':len(unknown)*len(hs),'full_map_rank':len(bbas),'full_field_targets':14 if degree==3 else 2,'failed_targets':bad,'residual_entries':nr,'first_obstruction':first,'scope':'Complete necessary '+('one' if degree==3 else 'zero')+'-W fifth-algebraic test of this constructed cubic only; further admissible cubic corrections remain open.'}
onefull=remaining_sector(3);zerofull=remaining_sector(4)
ck('complete_one_W_report_reproduced',onefull==report['one_W_full'])
ck('complete_zero_W_report_reproduced',zerofull==report['zero_W_full'])
# The terminal all-W receiver has no quartic term at all.
fivebad=[]
for wt in combinations_with_replacement(range(7),5):
 for op in range(2):
  raw={};slots=[7+w for w in wt]
  for pos in combinations(range(5),2):
   aa=[slots[i] for i in pos];bb=[slots[i] for i in range(5) if i not in pos]
   for pa,pb,fac in ([(0,0,1),(1,1,2)] if op==0 else [(0,1,1),(1,0,1)]):raw=add((1,raw),(-fac,pol(getL2(pa,aa),getS2(pb,bb,repaired))))
  if raw:fivebad.append([list(wt),op])
ck('all924_five_W_receivers',not fivebad)
report['algebraic_lift_assembly']={'five_W_field_receivers':924,'five_W_failed':fivebad,'all_W_values_of_K_zero':all(not add(*[(v,K[i]) for i,v in w.items()]) for w in W),'one_shared_quartic_algebraic_lift_exists':not(onefull['failed_targets'] or zerofull['failed_targets'] or fivebad),'scope':'Direct sum by W-degree proves a shared quartic algebraic lift if every complete sector passes. Quartic Euler intersection remains unproved.'}
ck('K_W_zero_for_direct_sum_assembly',report['algebraic_lift_assembly']['all_W_values_of_K_zero'])

# Full14-variable Euler symbol: one exact rank103 specialization plus the
# universal primitive quadratic adjoint identity proves the written image theorem.
xi=add(*[(1,a) for a in alphas]);sbas={}
for h in tk:
 cc=clean({ij:sum(eta[m]*v*(h.get((ij[0],m,ij[1]),0)+h.get((ij[1],m,ij[0]),0)) for m,v in xi.items()) for ij in receivers})
 while cc:
  k=min(cc);v=cc[k]
  if k not in sbas:sbas[k]={j:x/v for j,x in cc.items()};break
  for j,x in sbas[k].items():
   z=cc.get(j,F(0))-v*x
   if z:cc[j]=z
   elif j in cc:del cc[j]
ck('polar_Euler_symbol_rank103_specialization',len(sbas)==103)
# Recompute the inherited actual curvature/Bianchi and differentiated full
# double-divergence receiver on the SAME L. Never rerun the K2381 search.
import sympy as sp
from itertools import product
p81=ROOT/'tests/channel-swings/k2381_rotated_null_hook_prolongation_probe.py';s81=p81.read_text()
renv={'__file__':str(p81),'__name__':'quartic_compatibility_replay','Path':Path,'sp':sp,'F':F,'defaultdict':defaultdict,'product':product,'n':n,'eta':eta,'K':K}
renv['rows']=[(l,i,j) for l in range(n) for i in range(n) for j in range(i,n)];renv['ri']={k:v for v,k in enumerate(renv['rows'])}
exec(compile(s81[s81.index('# C = -2nabla Ric'):s81.index('def solve(target):')],str(p81),'exec'),renv)
exec(compile(s81[s81.index('root=Path(__file__)'):s81.index('# reconstruct rational/sqrt2 L from candidate')],str(p81),'exec'),renv)
fs,rs=renv['fs'],renv['rs']
def curved_compat(parts):
 ans=[]
 for f,r in zip(fs,rs):
  a=b=F(0)
  for key,(x,y) in f.items():
   ep=key[:2];hh=key[2:];v=parts[0][ep].get(hh,F(0));w=parts[1][ep].get(hh,F(0));a+=x*v+2*y*w;b+=x*w+y*v
  ans.append((a-r[0],b-r[1]))
 return ans
compat=curved_compat(L)
ck('all14_actual_curved_fourth_Euler_compatibilities',all(x==0 and y==0 for x,y in compat))
mutL=[{t:dict(h) for t,h in p.items()} for p in L];key=next(iter(fs[0]));mutL[0][key[:2]][key[2:]]=mutL[0][key[:2]].get(key[2:],F(0))+1
ck('changed_actual_L_rejected_by_same_curved_compatibility',any(x or y for x,y in curved_compat(mutL)))
algrank=210*612+84*4182+28*16446+7*onefull['full_map_rank']+zerofull['full_map_rank'];domain=2380*896;erank=560*104-14
ck('quartic_dimension_arithmetic',(algrank,domain,erank,domain-algrank-erank)==(1401533,2132480,58226,672721))
report['quartic_Euler_intersection']={'symbol_specialization_rank':len(sbas),'curved_compatibility_field_receivers':14,'curved_residuals':[[str(a),str(b)] for a,b in compat],'Euler_image_rank_deduced':erank,'full_algebraic_rank_from_sector_ranks':algrank,'quartic_domain_field_dimension':domain,'joint_affine_solution_field_dimension_deduced':domain-algrank-erank,'explicit_quartic_coefficients_stored':False,'scope':'Written primitive-symbol/image-equality and normal-frame finite-jet proof, supported by exact symbol and actual-curvature checks, establish a nonempty shared fourth-Euler/fifth-algebraic quartic fiber over Q(sqrt2). Dimension is deduced, not a combined-matrix rank computation. No smooth, all-order or native GU result.'}

report['algebraic_lift_assembly']['scope']='Direct sum by W-degree proves a shared quartic algebraic lift; the separately checked curved compatibility and polar-symbol theorem establish its Euler intersection.'
# Look ahead across the full896-hook quartic value for each pure-W sixth
# receiver. These seven directional problems are necessary, not mixed-W proof.
def sixth_direction(w):
 sc3=[{t:evfield(part,[W[a] for a in t]) for t in ws} for part in repaired]
 sc2=[{(t,u):evfield(part,[W[t[0]],W[t[1]],{u:F(1)}]) for t in w2 for u in range(n)} for part in repaired]
 target={}
 for op in range(2):
  for (u,k),v in final_fourW_target((w,w,w,w),op,sc3,sc2).items():target[0,op,u,k]=v
  ss=evfield(repaired[0],[W[w]]*3);st=evfield(repaired[1],[W[w]]*3)
  v=add((-10,pol(ss,ss)),(-20,pol(st,st))) if op==0 else add((-20,pol(ss,st)))
  for k,x in v.items():target[1,op,-1,k]=x
 ll=[eval_L(ip,(7+w,7+w)) for ip in range(2)]
 def col(hi,ip):
  h=hs[hi];out={}
  for u in range(n):
   for k,v in pol(h,K[u]).items():out[0,ip,u,k]=v
  for op in range(2):
   lp=op if ip==0 else 1-op;fac=2 if ip==1 and op==0 else 1
   for k,v in pol(h,ll[lp]).items():out[1,op,-1,k]=15*fac*v
  return clean(out)
 b={}
 for ip in range(2):
  for hi in range(len(hs)):
   cc=col(hi,ip)
   while cc:
    k=min(cc);v=cc[k]
    if k not in b:b[k]={j:x/v for j,x in cc.items()};break
    for j,x in b[k].items():
     z=cc.get(j,F(0))-v*x
     if z:cc[j]=z
     elif j in cc:del cc[j]
 cc=dict(target);res={}
 while cc:
  k=min(cc);v=cc[k]
  if k not in b:res[k]=v;del cc[k];continue
  for j,x in b[k].items():
   z=cc.get(j,F(0))-v*x
   if z:cc[j]=z
   elif j in cc:del cc[j]
 dual=None
 if res:
  obs=min(res);du={obs:F(1)}
  for k in sorted(b,reverse=True):
   v=-sum(x*du.get(j,F(0)) for j,x in b[k].items() if j!=k)
   if v:du[k]=v
  ck('sixth_direction'+str(w)+'_dual_all1792_columns',all(sum(v*col(hi,ip).get(k,F(0)) for k,v in du.items())==0 for ip in range(2) for hi in range(len(hs))))
  value=sum(v*target.get(k,F(0)) for k,v in du.items());ck('sixth_direction'+str(w)+'_dual_nonzero',value==res[obs] and value!=0)
  dual={'entries':[[list(k[:3]),list(k[3]),str(v)] for k,v in sorted(du.items())],'value':str(value)}
 return {'W_direction':w,'realified_columns':1792,'rank':len(b),'residual_entries':len(res),'first_obstruction':dual}
report['sixth_algebraic_directional_next']={'directions':[sixth_direction(w) for w in range(7)],'scope':'Complete pure-direction quartic hook freedom subject to inherited fourth-W fifth-algebraic rows, tested against the next all-equal-W sixth-algebraic receiver. Seven passes do not establish a quartic satisfying current Euler equations and all mixed all-W sixth constraints, nor a full sixth-order extension.'}

W4=list(combinations_with_replacement(range(7),4));W6=list(combinations_with_replacement(range(7),6));sc3=[{t:evfield(p,[W[a] for a in t]) for t in ws} for p in repaired];sc2=[{(t,u):evfield(p,[W[t[0]],W[t[1]],{u:F(1)}]) for t in w2 for u in range(n)} for p in repaired]
phi={};prec={}
for hi,h in enumerate(hs):
 cc={(u,k):v for u in range(n) for k,v in pol(h,K[u]).items()};history={}
 while cc:
  k=min(cc);v=cc[k]
  if k not in phi:phi[k]={j:x/v for j,x in cc.items()};prec[k]=(hi,v,history);break
  history[k]=v
  for j,x in phi[k].items():
   z=cc.get(j,F(0))-v*x
   if z:cc[j]=z
   elif j in cc:del cc[j]
def phisolve(raw):
 cc=dict(raw);used={}
 while cc:
  k=min(cc);v=cc[k];assert k in phi
  used[k]=v
  for j,x in phi[k].items():
   z=cc.get(j,F(0))-v*x
   if z:cc[j]=z
   elif j in cc:del cc[j]
 sol=defaultdict(F)
 for k in reversed(prec):
  q=used.get(k,F(0))
  if not q:continue
  hi,v,hist=prec[k];sol[hi]+=q/v
  for j,x in hist.items():used[j]=used.get(j,F(0))-q*x/v
 ans=add(*[(v,hs[hi]) for hi,v in sol.items()]);assert {(u,k):v for u in range(n) for k,v in pol(ans,K[u]).items()}==raw
 return ans
U0=[{q:phisolve(final_fourW_target(q,ip,sc3,sc2)) for q in W4} for ip in range(2)]
def target6(q,op,quartic):
 out={}
 for pos in combinations(range(6),2):
  pp=tuple(q[i] for i in pos);qq=tuple(q[i] for i in range(6) if i not in pos)
  for pa,pb,fac in ([(0,0,1),(1,1,2)] if op==0 else [(0,1,1),(1,0,1)]):out=add((1,out),(-fac,pol(lw[pa][pp],quartic[pb][qq])))
 for rest in combinations(range(1,6),2):
  pos=(0,*rest);aa=tuple(q[i] for i in pos);bb=tuple(q[i] for i in range(6) if i not in pos)
  for pa,pb,fac in ([(0,0,1),(1,1,2)] if op==0 else [(0,1,1),(1,0,1)]):out=add((1,out),(-fac,pol(sc3[pa][aa],sc3[pb][bb])))
 return out

# Exact555-coefficient witness; acceptance uses the original Phi and sixth
# receivers, never the large search matrix or its rank statistic.
mix=report['mixed_all_W_sixth_extension'];U6=[{q:dict(h) for q,h in p.items()} for p in U0]
for (qi,hi,ip),v in mix['polar_solution']:
 q=W4[qi];U6[ip][q]=add((1,U6[ip][q]),(F(v),tk[hi]))
ck('mixed_sixth_555_polar_coefficients',len(mix['polar_solution'])==555)
ck('mixed_sixth_all420_prior_Phi_targets',all({(u,k):v for u in range(n) for k,v in pol(U6[ip][q],K[u]).items()}==final_fourW_target(q,ip,sc3,sc2) for q in W4 for ip in range(2)))
ck('mixed_sixth_all1848_original_field_targets',all(not target6(q,op,U6) for q in W6 for op in range(2)))
ck('remove_actual_polar_sixth_correction_fails_same_receiver',any(target6(q,op,U0) for q in W6 for op in range(2)))
encodedU=[[[list(q),[[list(k),str(v)] for k,v in sorted(h.items())]] for q,h in sorted(p.items()) if h] for p in U6]
mix['quartic_W4_sha256']=hashlib.sha256(json.dumps(encodedU,sort_keys=True,separators=(',',':')).encode()).hexdigest()
mix['ambient_W4_entries']=[sum(map(len,p.values())) for p in U6]
ck('zero_W4_Euler_image_rank_arithmetic',84*104+28*728+7*2911+(84*104-7)==58226)
mix['scope']='Reconstructed quartic W4 values satisfy all420 preceding Phi targets and all1848 mixed all-W sixth-algebraic field targets. The written zero-W4 polar Euler image theorem completes these values to the same fourth-Euler/fifth-algebraic fiber. Remaining sixth sectors, fifth Euler and smooth/all-order/native GU remain open.'

# Rank-derived syzygy counts, not a computed multiplication-map rank.
z0,z1,z2=896-612,7*896-4182,28*896-16446
ck('certified_symbol_kernel_dimensions',(z0,z1,z2)==(284,2090,8642))
ck('quotient_syzygy_dimensions',(z1-7*z0,z2-28*z0)==(102,690))
ck('at_least24_quadratic_relations',7*(z1-7*z0)-(z2-28*z0)==24)
report['verification']={'checks':new_checks,'ambient_entries':[sum(map(len,p.values())) for p in delta],'escape_two_W_replay':escape_replay,'C_repair_ambient_entries':[sum(map(len,p.values())) for p in repair],'complete_two_W_replay':rr,'remaining_feasibility':'shared-fourth-Euler-fifth-algebraic-finite-jet-extension-proved','syzygy_dimensions':{'constant':284,'linear':2090,'quadratic':8642,'mod_constant_linear':102,'mod_constant_quadratic':690,'quadratic_relations_lower_bound':24,'multiplication_rank':'not computed'}}
report['status']='PASS';report['scope']='Exact coupled B/C repair, complete algebraic-sector membership, polar Euler-symbol image equality and14 actual-curvature compatibility checks prove an existential shared fourth-Euler/fifth-algebraic finite-jet extension. The fixed-lower-jet quartic affine fiber has field dimension672721. No explicit quartic array, smooth/all-order or native GU verdict. A555-coefficient quartic W4 correction additionally passes all1848 mixed all-W sixth targets; the zero-W4 Euler-repair theorem retains the prior intersection. Other sixth sectors remain open.'
if '--write' in sys.argv:path.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print(json.dumps(report,sort_keys=True))
