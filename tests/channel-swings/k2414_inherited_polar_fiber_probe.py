"""Inherited A witness and original three-W dual pullback; no full-family solve."""
from pathlib import Path
import json,hashlib,sys
ROOT=Path(__file__).resolve().parents[2]
p05=ROOT/'tests/channel-swings/k2405_fifth_euler_compatibility_probe.py';s05=p05.read_text()
exec(compile(s05[:s05.index('# Search exact realified D2 and J')],str(p05),'exec'),globals())
inherited=dict(checks);checks={};controls={}
p08=ROOT/'tests/channel-swings/k2408_joint_cubic_compatibility_probe.py';s08=p08.read_text();r08=json.loads((ROOT/'lab/process/k2408-joint-cubic-compatibility.json').read_text())
polar_coefficients=r08['raw_coefficients']
def section(a,b):exec(compile(s08[s08.index(a):s08.index(b)],str(p08),'exec'),globals())
section('triples=list(',"ck('polar_repair_full_hook'")
Snew=[{t:add((1,S[ip][t]),(1,polar_delta[ip][t])) for t in triples} for ip in range(2)]
ck('inherited_original_tensor_digest',digest(Snew)==r08['repaired_cubic_sha256'])
section('w_alphas=','fivebad=[]');section('pfb={}','new3=[');section('alphas=w_alphas','bas3={}')
# Build the exact dual covectors; entries are derivative values, not polynomial coefficients.
vm=sp.Matrix([[sp.Rational(v.get(a,0)) for v in vec] for a in range(n)]);ci=vm.inv()
covs=[{a:F(str(ci[i,a])) for a in range(n) if ci[i,a]} for i in range(n)]
ck('adapted_dual_coframe',all(sum(co.get(a,0)*v for a,v in vec[j].items())==int(i==j) for i,co in enumerate(covs) for j in range(n)))
adapted_A=[{(r,st):evfield(part,[Es[r],W[st[0]],W[st[1]]]) for r in range(7) for st in w2} for part in polar_delta]
projected=[{t:{} for t in triples} for _ in range(2)]
for ip in range(2):
 for (r,st),hook in adapted_A[ip].items():
  if not hook:continue
  for ids in set(permutations((r,7+st[0],7+st[1]))):
   for a,va in covs[ids[0]].items():
    for b,vb in covs[ids[1]].items():
     for c,vc in covs[ids[2]].items():
      if a<=b<=c:projected[ip][a,b,c]=add((1,projected[ip][a,b,c]),(va*vb*vc,hook))
ck('all392_A_values_roundtrip',all(evfield(projected[ip],[Es[r],W[st[0]],W[st[1]]])==hook for ip in range(2) for (r,st),hook in adapted_A[ip].items()))
ck('all_off_A_adapted_values_zero',all(not evfield(part,[vec[a] for a in t]) for part in projected for t in triples if sum(a>=7 for a in t)!=2))
# Direct Euler rows on W,W; do not infer full Euler closure of the projection.
for ip in range(2):
 for st in w2:
  hz=[evfield(projected[ip],[W[st[0]],W[st[1]],{z:F(1)}]) for z in range(n)]
  assert all(sum(eta[z]*(hz[z].get((i,z,j),0)+hz[z].get((j,z,i),0)) for z in range(n))==0 for i,j in receivers)
ck('all5880_WW_Euler_entries',True)
SA=[{t:add((1,S[ip][t]),(1,projected[ip][t])) for t in triples} for ip in range(2)]
MT={(a,b,c):MP(a,b,c,T=SA) for a,b,c in product(range(n),repeat=3)}
support=sorted({a for wv in W for a in wv});direct={t:defect(*t,MT=MT) for t in combinations_with_replacement(support,2)}
# Independent original-J pullback versus actual curved evaluation.
jvals={}
for t,fun in zip(receivers,Jfs):
 val=out[t]
 for (tr,hk),co in fun.items():val=plus(val,mul(co,tuple(projected[ip][tr].get(hk,F(0)) for ip in range(2))))
 jvals[t]=val
ck('original_curved_J_pullback_agrees',all(jvals[t]==v for t,v in direct.items()))
ww=[]
for st in w2:
 val=Z
 for a,va in W[st[0]].items():
  for b,vb in W[st[1]].items():val=plus(val,pairscale(va*vb,direct[tuple(sorted((a,b)))]))
 ww.append(val)
ck('all28_actual_curved_WW_receivers',all(z==Z for z in ww))
ck('all420_original_fourW_quotients',not all_fourW(SA))
newSW=[{t:evfield(part,[W[a] for a in t]) for t in ws} for part in SA]
for wt in combinations_with_replacement(range(7),5):
 for op in range(2):
  raw={}
  for pos in combinations(range(5),2):
   aa=tuple(wt[i] for i in pos);bb=tuple(wt[i] for i in range(5) if i not in pos)
   for pa,pb,fac in ([(0,0,1),(1,1,2)] if op==0 else [(0,1,1),(1,0,1)]):raw=add((1,raw),(-fac,pol(lw[pa][aa],newSW[pb][bb])))
  assert not raw
ck('all924_original_allW_targets',True)
# One raw three-W dual against original quartic columns, with no rank search.
du={(tuple(ep),tuple(key)):F(v) for ep,key,v in r08['three_W_first_obstruction']['raw_dual']}
ck('short_dual_all6272_original_columns',all(sum(v*raw_Ucol(r,h).get(key,F(0)) for key,v in du.items())==0 for r in range(7) for h in hs))
wt=r08['three_W_first_obstruction']['W_indices'];op=r08['three_W_first_obstruction']['field_part']
assert wt==[0,0,0] and op==0 and {ep for ep,key in du}=={(0,0),(0,1)}
def dual_target(parts):
 val=F(0)
 for (ep,key),dv in du.items():
  slots=[7+a for a in wt]+list(ep)
  for pos in combinations(range(5),2):
   aa=[slots[i] for i in pos];bb=[slots[i] for i in range(5) if i not in pos]
   for pa,pb,fac in ([(0,0,1),(1,1,2)] if op==0 else [(0,1,1),(1,0,1)]):val-=dv*fac*pol(eval_L(pa,aa),evfield(parts[pb],[vec[a] for a in bb])).get(key,F(0))
 return val
vfull=dual_target(Snew);vA=dual_target(SA)
ck('short_dual_original_target_reproduced',vfull==F(r08['three_W_first_obstruction']['target_value']) and bool(vfull))
# Entire B pullback: other slots do not occur in the three-term functional.
bpull=[];apull=[]
for block in ('A','B'):
 for ip in range(2):
  for idx in (0,1):
   for hi,h in enumerate(tk):
    val=F(0)
    for (ep,key),dv in du.items():
     a,b=ep
     for pa,pb,fac in ([(0,0,1),(1,1,2)] if op==0 else [(0,1,1),(1,0,1)]):
      if pb!=ip:continue
      if block=='B' and ep==((0,0) if idx==0 else (0,1)):val-=3*dv*fac*pol(eval_L(pa,[7,7]),h).get(key,F(0))
      if block=='A':
       if b==idx:val-=3*dv*fac*pol(eval_L(pa,[a,7]),h).get(key,F(0))
       if a==idx:val-=3*dv*fac*pol(eval_L(pa,[b,7]),h).get(key,F(0))
    if val:(bpull if block=='B' else apull).append([ip,idx,hi,str(val)])
ck('complete_B_pullback_evaluated',True)
# A-only does not assert the downstream system is solved.
ctrl('projection_does_not_solve_every_curved_receiver',any(v!=Z for v in jvals.values()))
baseww=[]
for a,b in w2:
 z=Z
 for i,u in W[a].items():
  for j,v in W[b].items():z=plus(z,pairscale(u*v,out[tuple(sorted((i,j)))]))
 baseww.append(z)
ctrl('zero_correction_fails_curved_WW',any(z!=Z for z in baseww))
# Follow-through: does the apparent B escape survive the EW Euler kernel?
def alpha_contract(h,r):
 return clean({ij:sum(eta[z]*v*(h.get((ij[0],z,ij[1]),0)+h.get((ij[1],z,ij[0]),0)) for z,v in alphas[r].items()) for ij in receivers})
dac={(r,hi):alpha_contract(h,r) for r in range(7) for hi,h in enumerate(tk)}
bfunc={(tuple((0,0) if idx==0 else (0,1)),hi):F(v) for ip,idx,hi,v in bpull if ip==1}
basisB={};recsB={};fB={};bescape=None;examined=0
for ep in EP:
 for hi,h in enumerate(tk):
  name=(ep,hi);col={}
  for r in set(ep):
   rest=list(ep);rest.remove(r)
   for ij,v in dac[r,hi].items():col[rest[0],ij]=v
  original=dict(col);fv=bfunc.get(name,F(0));hist={};examined+=1
  while col:
   pv=min(col);vv=col[pv]
   if pv not in basisB:
    basisB[pv]={k:v/vv for k,v in col.items()};recsB[pv]=(name,vv,hist);fB[pv]=fv/vv;break
   hist[pv]=vv;fv-=vv*fB[pv]
   for k,v in basisB[pv].items():
    z=col.get(k,F(0))-vv*v
    if z:col[k]=z
    elif k in col:del col[k]
  if not col and fv:
   ans=defaultdict(F);ans[name]=F(1);used=dict(hist)
   for pv in reversed(recsB):
    if pv not in used:continue
    amount=used[pv];nm,scale,prev=recsB[pv];ans[nm]-=amount/scale
    for k,v in prev.items():used[k]=used.get(k,F(0))-amount*v/scale
   ans=clean(ans);test=defaultdict(F)
   for (ee,hh),v in ans.items():
    for r in set(ee):
     rest=list(ee);rest.remove(r)
     for ij,u in dac[r,hh].items():test[rest[0],ij]+=v*u
   ck('B_escape_original_EW_Euler',not clean(test))
   delta=sum(v*bfunc.get(nm,F(0)) for nm,v in ans.items())
   ck('B_escape_short_dual_nonzero',delta==fv and bool(delta))
   bescape={'coefficients':[[list(ee),hh,str(v)] for (ee,hh),v in sorted(ans.items())],'dual_change':str(delta),'field_part':1,'W_slot':0,'prefix_columns':examined,'prefix_rank':len(basisB)}
   break
 if bescape:break
if bescape is None:
 ck('complete_B_functional_in_Euler_rowspace',examined==28*284)
 bkernel={'status':'annihilates_complete_EW_Euler_kernel','columns':examined,'rank':len(basisB)}
else:
 # Reconstruct original ambient tensor and independently verify its EW rows
 # and actual three-W target change; do not silently accept its remaining J/EE rows.
 bd=[{tr:{} for tr in triples} for _ in range(2)]
 for ee,hh,v in bescape['coefficients']:
  for ids in set(permutations((*ee,7))):
   for a,va in covs[ids[0]].items():
    for b,vb in covs[ids[1]].items():
     for c,vc in covs[ids[2]].items():
      if a<=b<=c:bd[1][a,b,c]=add((1,bd[1][a,b,c]),(F(v)*va*vb*vc,tk[hh]))
 for ip in range(2):
  for a,b in product(range(7),repeat=2):
   hz=[evfield(bd[ip],[Es[a],W[b],{z:F(1)}]) for z in range(n)]
   assert all(sum(eta[z]*(hz[z].get((i,z,j),0)+hz[z].get((j,z,i),0)) for z in range(n))==0 for i,j in receivers)
 ck('B_escape_direct_ambient_EW_Euler',True)
 ck('B_escape_direct_threeW_delta',dual_target(bd)==F(bescape['dual_change']))
 jchange=[]
 for fun in Jfs:
  val=Z
  for (tr,hk),co in fun.items():val=plus(val,mul(co,tuple(bd[ip][tr].get(hk,F(0)) for ip in range(2))))
  jchange.append(val)
 jd=dict(zip(receivers,jchange));jc={}
 for label,pairs in [('WW',[(W[a],W[b]) for a,b in w2]),('EW',[(Es[a],W[b]) for a,b in product(range(7),repeat=2)]),('EE',[(Es[a],Es[b]) for a,b in EP])]:
  vals=[]
  for va,vb in pairs:
   z=Z
   for a,u in va.items():
    for b,v in vb.items():z=plus(z,pairscale(u*v,jd[tuple(sorted((a,b)))]))
   vals.append(z)
  jc[label]=sum(v!=Z for v in vals)
 bescape['adapted_J_nonzero_receivers']=jc
 bescape['nonzero_ambient_J_receivers']=sum(v!=Z for v in jchange)
 bescape['ambient_J_residual']=[[list(t),list(map(str,v))] for t,v in zip(receivers,jchange) if v!=Z]
 ee_fail=0
 for a,b in EP:
  hz=[evfield(bd[1],[Es[a],Es[b],{z:F(1)}]) for z in range(n)]
  ee_fail+=sum(sum(eta[z]*(hz[z].get((i,z,j),0)+hz[z].get((j,z,i),0)) for z in range(n))!=0 for i,j in receivers)
 bescape['EE_Euler_nonzero_entries']=ee_fail
 bkernel={'status':'explicit_EW_Euler_kernel_escape','witness':bescape}
# Follow through to the same B kernel with all original curved EW-J rows.
ejf={}
for a,b in product(range(7),repeat=2):
 fun={}
 for i,u in Es[a].items():
  for j,v in W[b].items():
   for k,co in Jfs[receivers.index(tuple(sorted((i,j))))].items():
    fun[k]=plus(fun.get(k,Z),pairscale(u*v,co))
 ejf[a,b]={k:v for k,v in fun.items() if v!=Z}
bj={}
for ep in EP:
 scalar=defaultdict(F)
 for ids in set(permutations((*ep,7))):
  for a,va in covs[ids[0]].items():
   for b,vb in covs[ids[1]].items():
    for c,vc in covs[ids[2]].items():
     if a<=b<=c:scalar[a,b,c]+=va*vb*vc
 for receiver,fun in ejf.items():
  hf={}
  for (tr,hk),co in fun.items():
   if tr in scalar:hf[hk]=plus(hf.get(hk,Z),pairscale(scalar[tr],co))
  for hi,h in enumerate(tk):
   value=Z
   for hk,co in hf.items():
    if hk in h:value=plus(value,mul(co,(F(0),h[hk])))
   if value!=Z:
    for ip,v in enumerate(value):
     if v:bj.setdefault((ep,hi),{})[(1,*receiver,ip)]=v
jbasis={};jrecords={};jvalues={};joint=None;jexamined=0
for ep in EP:
 for hi,h in enumerate(tk):
  name=(ep,hi);col=dict(bj.get(name,{}))
  for r in set(ep):
   rest=list(ep);rest.remove(r)
   for ij,v in dac[r,hi].items():col[(0,rest[0],*ij)]=v
  fv=bfunc.get(name,F(0));hist={};jexamined+=1
  while col:
   pv=min(col);vv=col[pv]
   if pv not in jbasis:
    jbasis[pv]={k:v/vv for k,v in col.items()};jrecords[pv]=(name,vv,hist);jvalues[pv]=fv/vv;break
   hist[pv]=vv;fv-=vv*jvalues[pv]
   for k,v in jbasis[pv].items():
    z=col.get(k,F(0))-vv*v
    if z:col[k]=z
    elif k in col:del col[k]
  if not col and fv:
   ans=defaultdict(F);ans[name]=F(1);used=dict(hist)
   for pv in reversed(jrecords):
    if pv not in used:continue
    amount=used[pv];nm,scale,prev=jrecords[pv];ans[nm]-=amount/scale
    for k,v in prev.items():used[k]=used.get(k,F(0))-amount*v/scale
   ans=clean(ans)
   jdlt=[{tr:{} for tr in triples} for _ in range(2)]
   for (ee,hh),v in ans.items():
    for ids in set(permutations((*ee,7))):
     for a,va in covs[ids[0]].items():
      for b,vb in covs[ids[1]].items():
       for c,vc in covs[ids[2]].items():
        if a<=b<=c:jdlt[1][a,b,c]=add((1,jdlt[1][a,b,c]),(v*va*vb*vc,tk[hh]))
   for ip in range(2):
    for a,b in product(range(7),repeat=2):
     hz=[evfield(jdlt[ip],[Es[a],W[b],{z:F(1)}]) for z in range(n)]
     assert all(sum(eta[z]*(hz[z].get((i,z,j),0)+hz[z].get((j,z,i),0)) for z in range(n))==0 for i,j in receivers)
   directj={}
   for rr,fun in zip(receivers,Jfs):
    val=Z
    for (tr,hk),co in fun.items():val=plus(val,mul(co,tuple(jdlt[ip][tr].get(hk,F(0)) for ip in range(2))))
    directj[rr]=val
   for a,b in product(range(7),repeat=2):
    val=Z
    for i,u in Es[a].items():
     for j,v in W[b].items():val=plus(val,pairscale(u*v,directj[tuple(sorted((i,j)))]))
    assert val==Z
   ck('joint_B_direct_EW_Euler_and_curved_J',True)
   val=dual_target(jdlt);ck('joint_B_original_short_dual_escape',val==fv and bool(val))
   ee_count=0
   for a,b in EP:
    hz=[evfield(jdlt[1],[Es[a],Es[b],{z:F(1)}]) for z in range(n)]
    ee_count+=sum(sum(eta[z]*(hz[z].get((i,z,j),0)+hz[z].get((j,z,i),0)) for z in range(n))!=0 for i,j in receivers)
   joint={'EE_Euler_nonzero_entries':ee_count,'status':'explicit_EW_Euler_and_J_kernel_escape','field_part':1,'W_slot':0,'coefficients':[[list(ee),hh,str(v)] for (ee,hh),v in sorted(ans.items())],'dual_change':str(val),'prefix_columns':jexamined,'prefix_rank':len(jbasis),'remaining_ambient_J':[[list(rr),list(map(str,v))] for rr,v in directj.items() if v!=Z]}
   break
 if joint:break
if joint is None:
 ck('complete_one_field_B_joint_rowspace',jexamined==28*284)
 cert={}
 for pv in sorted(jbasis,reverse=True):
  cert[pv]=jvalues[pv]-sum(v*cert.get(k,F(0)) for k,v in jbasis[pv].items() if k!=pv)
 cert=clean(cert)
 for ep in EP:
  for hi in range(len(tk)):
   val=sum(v*cert.get(k,F(0)) for k,v in bj.get((ep,hi),{}).items())
   for r in set(ep):
    rest=list(ep);rest.remove(r)
    val+=sum(v*cert.get((0,rest[0],*ij),F(0)) for ij,v in dac[r,hi].items())
   assert val==bfunc.get((ep,hi),F(0))
 ck('joint_B_rowspace_original7952_columns',True)
 joint={'status':'annihilates_complete_one_field_W0_EW_Euler_and_J_kernel','columns':jexamined,'rank':len(jbasis),'rowspace_certificate':[[list(k),str(v)] for k,v in sorted(cert.items())],'scope':'Only pure sqrt2 B with W slot0; no full-family exclusion.'}
# Explicit C witness discovered by an exact combined EE-Euler/J solve.
# Discovery prefix counts are provenance, not a rank certificate; acceptance
# below replays the saved positive witness directly on original ambient rows.
assert not joint['remaining_ambient_J']
ccoeff=[[[0,0,0],137,'-2'],[[0,0,4],176,'1'],[[0,0,4],178,'-1']]
cd=[{tr:{} for tr in triples} for _ in range(2)]
for tr,hi,v in ccoeff:
 for ids in set(permutations(tr)):
  for a,va in covs[ids[0]].items():
   for b,vb in covs[ids[1]].items():
    for c,vc in covs[ids[2]].items():
     if a<=b<=c:cd[1][a,b,c]=add((1,cd[1][a,b,c]),(F(v)*va*vb*vc,tk[hi]))
bc=[{tr:add((1,jdlt[ip][tr]),(1,cd[ip][tr])) for tr in triples} for ip in range(2)]
for ip in range(2):
 for a,b in receivers:
  hz=[bc[ip][tuple(sorted((a,b,z)))] for z in range(n)]
  assert all(sum(eta[z]*(hz[z].get((i,z,j),0)+hz[z].get((j,z,i),0)) for z in range(n))==0 for i,j in receivers)
ck('BC_all22050_original_ambient_Euler_entries',True)
for fun in Jfs:
 value=Z
 for (tr,hk),co in fun.items():value=plus(value,mul(co,tuple(bc[ip][tr].get(hk,F(0)) for ip in range(2))))
 assert value==Z
ck('BC_all105_original_curved_J_receivers',True)
ck('BC_original_threeW_change',dual_target(bc)==F(joint['dual_change']))
ctrl('omitted_C_fails_EE_Euler',joint['EE_Euler_nonzero_entries']>0)
lamfix=-vfull/F(joint['dual_change'])
sfixed=[{tr:add((1,Snew[ip][tr]),(lamfix,bc[ip][tr])) for tr in triples} for ip in range(2)]
ck('scaled_short_dual_target_zero',dual_target(sfixed)==0)
for rr,fun in zip(receivers,Jfs):
 value=out[rr]
 for (tr,hk),co in fun.items():
  correction=tuple(polar_delta[ip][tr].get(hk,F(0))+lamfix*bc[ip][tr].get(hk,F(0)) for ip in range(2))
  value=plus(value,mul(co,correction))
 assert value==Z
ck('scaled_cubic_all105_original_curved_J',True)
ck('scaled_cubic_all420_fourW',not all_fourW(sfixed))
ck('scaled_cubic_W3_unchanged',all(evfield(bc[ip],[W[a] for a in tr])=={} for ip in range(2) for tr in combinations_with_replacement(range(7),3)))
ccompletion={'C_coefficients':ccoeff,'field_part':1,'BC_sha256':digest(bc),'dual_change':joint['dual_change'],'scaled_repair_factor':str(lamfix),'repaired_cubic_sha256':digest(sfixed),'scope':'Explicit full homogeneous Euler/J correction; scaled repair of one short three-W dual preserves W3/fourW. Scaled cubic fails complete three-W replay; full correction-family feasibility remains open.'}
# Complete original three-W quotient replay on the newly repaired cubic.
section('bas3={}','three=all_threeW(Snew)')
threefixed=all_threeW(sfixed)
ck('scaled_cubic_all168_threeW_tested',len(threefixed['failed_targets'])<=168)
nextdual=None
if threefixed['failed_targets']:
 wtnew,opnew=threefixed['failed_targets'][0];targetnew=defaultdict(F)
 for ep in EP:
  slots=[7+x for x in wtnew]+list(ep)
  for pos0 in combinations(range(5),2):
   aa=[slots[i] for i in pos0];bb=[slots[i] for i in range(5) if i not in pos0]
   for pa,pb,fac in ([(0,0,1),(1,1,2)] if opnew==0 else [(0,1,1),(1,0,1)]):
    for key,v in pol(eval_L(pa,aa),evfield(sfixed[pb],[vec[a] for a in bb])).items():targetnew[ep,key]-=fac*v
 residue=quotient3(clean(targetnew));obs=min(residue);newdu={obs:F(1)}
 for pivot in sorted(bas3,reverse=True):
  v=-sum(x*newdu.get(k,F(0)) for k,x in bas3[pivot].items() if k!=pivot)
  if v:newdu[pivot]=v
 ck('new_dual_all6272_original_quartic_columns',all(sum(v*raw_Ucol(r,h).get(k,F(0)) for k,v in newdu.items())==0 for r in range(7) for h in hs))
 value=sum(v*targetnew.get(k,F(0)) for k,v in newdu.items())
 ck('new_dual_repaired_target_nonzero',value==residue[obs] and bool(value))
 nextdual={'W_indices':wtnew,'field_part':opnew,'raw_dual':[[list(ep),list(k),str(v)] for (ep,k),v in sorted(newdu.items())],'target_value':str(value),'scope':'Obstructs only this particular scaled cubic, not its full homogeneous correction fiber.'}
print('complete three-W',len(threefixed['failed_targets']),threefixed['residual_entries'],flush=True,file=sys.stderr)
print('joint B discriminator',joint['status'],jexamined,flush=True,file=sys.stderr)
print('B kernel discriminator',bkernel['status'],examined,flush=True,file=sys.stderr)
report={'result_id':'K2414','checks':checks,'controls':controls,'inherited_geometry_checks':len(inherited),'A_projection_sha256':digest(projected),'A_projected_cubic_sha256':digest(SA),'adapted_A_nonzero_hook_entries':sum(sum(len(h) for h in p.values()) for p in adapted_A),'short_dual':r08['three_W_first_obstruction'],'short_dual_projected_target':str(vA),'B_EW_kernel_discriminator':bkernel,'B_EW_J_kernel_discriminator':joint,'C_completion':ccompletion,'repaired_threeW':threefixed,'repaired_threeW_first_obstruction':nextdual,'B_pullback_nonzero':bpull,'A_pullback_nonzero':apull,'scope':'Inherited A feasibility and seven-term full Euler/J correction repairing one short three-W dual; no complete three-W or full-family feasibility/exclusion.'}
deps=sorted(set(deps+['explorations/conditional-build/k2393-coupled-polar-dual-2026-10-31.md','tests/channel-swings/k2405_fifth_euler_compatibility_probe.py','tests/channel-swings/k2408_joint_cubic_compatibility_probe.py','lab/process/k2408-joint-cubic-compatibility.json','explorations/conditional-build/k2411-broader-polar-compatibility-2026-10-31.md']))
report['dependencies']={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps}
p=ROOT/'lab/process/k2414-inherited-polar-fiber.json'
if '--write' in sys.argv:p.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
elif '--verify-only' not in sys.argv:assert json.loads(p.read_text())==report
print(json.dumps({'checks':len(checks),'controls':len(controls),'B_pullback_nonzero':len(bpull),'A_pullback_nonzero':len(apull),'projected_target':str(vA)},sort_keys=True))
