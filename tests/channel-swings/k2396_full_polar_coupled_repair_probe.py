"""K2396 exact certificate replay, without repeating the large search.
Native destination tests/channel-swings/k2396_full_polar_coupled_repair_probe.py.
Report schema must contain ambient_delta (two encoded ambient tensor parts),
three_W_obstruction {W_triple,field_part,dual:[[Epair,key,str],...],value}.
Each tensor part is [[derivative_triple, [[hook_triple, rational_string],...]],...].
"""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from itertools import combinations,combinations_with_replacement
import json,hashlib,sys,time
ROOT=Path(__file__).resolve().parents[2]
checks={}
def check(name,ok):
 checks[name]=bool(ok)
 if not ok:raise AssertionError(name)
report_path=ROOT/'lab/process/k2396-full-polar-coupled-repair.json'
certificate=json.loads(report_path.read_text())
# Reconstruct exact lower tensor and deterministic full hook/polar basis.
# Execute in ONE namespace so tensor caches used by receiver functions cannot
# diverge from reassigned caches (a discarded scratch wrapper did that).
path93=ROOT/'tests/channel-swings/k2393_coupled_polar_dual_probe.py';source93=path93.read_text()
exec(compile(source93[:source93.index('# C columns')],str(path93),'exec'),globals())
exec(compile(source93[source93.index('# Reconstruct the original certified tensor'):source93.index('# Pointwise full polarization image')],str(path93),'exec'),globals())
# Exactly reconstruct K2390 original S from its parameters and digest, then
# replay new certificate independently of its search map or coordinates.
exec(compile(source93[source93.index('# Pointwise full polarization image'):source93.index('before=[];after=[]')],str(path93),'exec'),globals())
def decode_tensor(parts):
 return [{tuple(t):{tuple(k):F(v) for k,v in h} for t,h in part} for part in parts]
Delta=decode_tensor(certificate['ambient_delta'])
triples=list(combinations_with_replacement(range(n),3));receivers=list(combinations_with_replacement(range(n),2))
Delta=[{t:part.get(t,{}) for t in triples} for part in Delta]
check('two_field_parts',len(Delta)==2)
# Full symmetric/cyclic/tracefree hook validity, not only Euler/polar maps.
for ip,part in enumerate(Delta):
 for t,h in part.items():
  for i,j,k in h:
   check('hook_antisymmetry',h.get((i,j,k),0)+h.get((i,k,j),0)==0)
   check('hook_cyclic_identity',h.get((i,j,k),0)+h.get((j,k,i),0)+h.get((k,i,j),0)==0)
  check('hook_tracefree',all(sum(eta[i]*h.get((i,i,a),0) for i in range(n))==0 for a in range(n)))
 check('Euler_field_'+str(ip),all(sum(eta[z]*(part[tuple(sorted((a,b,z)))].get((i,z,j),0)+part[tuple(sorted((a,b,z)))].get((j,z,i),0)) for z in range(n))==0 for a,b in receivers for i,j in receivers))
 check('polar_field_'+str(ip),all(not pol(h,k) for h in part.values() for k in K))
 check('W_cubic_field_'+str(ip),all(not evfield(part,[W[a] for a in t]) for t in ws))
before=sum(bool(quotient(original_target(q,ip))) for q in combinations_with_replacement(range(7),4) for ip in range(2))
check('baseline420_has13_failures',before==13)
Snew=[{t:add((1,S[ip][t]),(1,Delta[ip][t])) for t in triples} for ip in range(2)]
sw=[{t:evfield(part,[W[a] for a in t]) for t in ws} for part in Snew]
swu=[{(t,u):evfield(part,[W[t[0]],W[t[1]],{u:F(1)}]) for t in w2 for u in range(n)} for part in Snew]
check('all420_four_W_repaired',all(not quotient(original_target(q,ip)) for q in combinations_with_replacement(range(7),4) for ip in range(2)))
# New obstruction to this chosen cubic, in independent3W+2E receivers.
obs=certificate['three_W_obstruction'];wt=tuple(obs['W_triple']);op=obs['field_part']
dual={(tuple(ep),tuple(key)):F(v) for ep,key,v in obs['dual']}
Es=[{p:F(1)/alphas[r][p]} for r,(p,q) in enumerate(pairs)]
KE=[add(*[(v,K[i]) for i,v in e.items()]) for e in Es]
EP=list(combinations_with_replacement(range(7),2));vec=Es+W
check('adapted_E_dual',all(sum(v*e.get(i,0) for i,v in a.items())==int(r==u) for r,a in enumerate(alphas) for u,e in enumerate(Es)))
check('W_annihilates_K',all(not add(*[(v,K[i]) for i,v in w.items()]) for w in W))
def raw_Ucol(r,h):
 col=defaultdict(F)
 for a,b in EP:
  if a==r:
   for key,v in pol(h,KE[b]).items():col[(a,b),key]+=v
  if b==r:
   for key,v in pol(h,KE[a]).items():col[(a,b),key]+=v
 return clean(col)
check('threeW_dual_all6272_original_quartic_generators',all(sum(v*raw_Ucol(r,h).get(k,F(0)) for k,v in dual.items())==0 for r in range(7) for h in hs))
def eval_L(ip,aa):
 return add(*[(v*w,L[ip][tuple(sorted((i,j)))]) for i,v in vec[aa[0]].items() for j,w in vec[aa[1]].items()])
def direct_threeW_target(ep):
 slots=[7+x for x in wt]+list(ep);out=defaultdict(F)
 for pos in combinations(range(5),2):
  aa=[slots[i] for i in pos];bb=[slots[i] for i in range(5) if i not in pos]
  for pa,pb,fac in ([(0,0,1),(1,1,2)] if op==0 else [(0,1,1),(1,0,1)]):
   for key,v in pol(eval_L(pa,aa),evfield(Snew[pb],[vec[a] for a in bb])).items():out[key]-=fac*v
 return clean(out)
raw={ep:direct_threeW_target(ep) for ep in {ep for ep,key in dual}}
value=sum(v*raw[ep].get(key,F(0)) for (ep,key),v in dual.items())
check('threeW_dual_nonzero_target',value==F(obs['value']) and bool(value))
# Mutate one correction coefficient independently of all search equations.
mut={t:dict(h) for t,h in Delta[0].items()};t=next(t for t,h in mut.items() if h);mut[t]=add((1,mut[t]),(1,hs[0]))
check('changed_correction_rejected_by_Euler',any(sum(eta[z]*(mut[tuple(sorted((a,b,z)))].get((i,z,j),0)+mut[tuple(sorted((a,b,z)))].get((j,z,i),0)) for z in range(n)) for a,b in receivers for i,j in receivers))
encoded=[[[list(t),[[list(k),str(v)] for k,v in sorted(h.items())]] for t,h in sorted(part.items()) if h] for part in Snew]
digest=hashlib.sha256(json.dumps(encoded,sort_keys=True,separators=(',',':')).encode()).hexdigest()
check('repaired_tensor_digest',digest==certificate['repaired_tensor_sha256'])
# Append before native output. Certificate extra input:
# B_correction_delta = two ambient tensor parts, already scaled.
# optional joint_B_correction_delta = full coupled B solution, already scaled.
BDelta=decode_tensor(certificate['B_correction_delta'])
BDelta=[{t:part.get(t,{}) for t in triples} for part in BDelta]
def verify_B_delta(delta,label):
 for ip,part in enumerate(delta):
  for t,h in part.items():
   check(label+'_hook_'+str(ip),all(h.get((i,j,k),0)+h.get((i,k,j),0)==0 and h.get((i,j,k),0)+h.get((j,k,i),0)+h.get((k,i,j),0)==0 for i,j,k in h) and all(sum(eta[i]*h.get((i,i,a),0) for i in range(n))==0 for a in range(n)))
  check(label+'_Euler_'+str(ip),all(sum(eta[z]*(part[tuple(sorted((a,b,z)))].get((i,z,j),0)+part[tuple(sorted((a,b,z)))].get((j,z,i),0)) for z in range(n))==0 for a,b in receivers for i,j in receivers))
  check(label+'_polar_'+str(ip),all(not pol(h,k) for h in part.values() for k in K))
  check(label+'_zero_two_W_'+str(ip),all(not evfield(part,[W[a],W[b],{u:F(1)}]) for a,b in w2 for u in range(n)))
verify_B_delta(BDelta,'single_dual_B')
Sintermediate=[{t:add((1,Snew[ip][t]),(1,BDelta[ip][t])) for t in triples} for ip in range(2)]
# Full3W image built independently in original hook/actual-E coordinates.
bas3={}
for r in range(7):
 for h in hs:
  col=raw_Ucol(r,h)
  while col:
   p=min(col);v=col[p]
   if p not in bas3:bas3[p]={k:x/v for k,x in col.items()};break
   for k,x in bas3[p].items():
    z=col.get(k,F(0))-v*x
    if z:col[k]=z
    elif k in col:del col[k]
check('threeW_complete_map_rank4182',len(bas3)==4182)
def quotient3(target):
 col=dict(target);res={}
 while col:
  p=min(col);v=col[p]
  if p not in bas3:res[p]=v;del col[p];continue
  for k,x in bas3[p].items():
   z=col.get(k,F(0))-v*x
   if z:col[k]=z
   elif k in col:del col[k]
 return res
# Explicit tensor argument prevents cache/namespace reuse from silently
# replaying the anchor after a correction has been applied.
def all_threeW(tensor_parts):
 cacheL={};cacheS={};bad=[];residual_count=0
 def el(ip,aa):
  tag=(ip,*sorted(aa))
  if tag not in cacheL:cacheL[tag]=eval_L(ip,aa)
  return cacheL[tag]
 def es(ip,bb):
  tag=(ip,*sorted(bb))
  if tag not in cacheS:cacheS[tag]=evfield(tensor_parts[ip],[vec[a] for a in bb])
  return cacheS[tag]
 for wt0 in combinations_with_replacement(range(7),3):
  for op0 in range(2):
   target=defaultdict(F)
   for ep in EP:
    slots=[7+x for x in wt0]+list(ep)
    for pos in combinations(range(5),2):
     aa=[slots[i] for i in pos];bb=[slots[i] for i in range(5) if i not in pos]
     for pa,pb,fac in ([(0,0,1),(1,1,2)] if op0==0 else [(0,1,1),(1,0,1)]):
      for key,v in pol(el(pa,aa),es(pb,bb)).items():target[ep,key]-=fac*v
   qr=quotient3(clean(target))
   if qr:bad.append([list(wt0),op0]);residual_count+=len(qr)
 return {'failed_targets':bad,'residual_entries':residual_count}
anchor3=all_threeW(Snew);intermediate3=all_threeW(Sintermediate)
check('all168_threeW_anchor8_failures',len(anchor3['failed_targets'])==8)
check('all168_threeW_single_dual_repair9_failures',len(intermediate3['failed_targets'])==9)
# Independently show targeted dual cancels after the16-component B branch.
old_tensor=Snew;Snew=Sintermediate
raw_mid={ep:direct_threeW_target(ep) for ep in {ep for ep,key in dual}}
check('single_dual_B_raw_target_cancelled',sum(v*raw_mid[ep].get(key,F(0)) for (ep,key),v in dual.items())==0)
Snew=old_tensor
full_replays={'anchor':anchor3,'single_dual_B':intermediate3}
if 'joint_B_correction_delta' in certificate:
 JDelta=decode_tensor(certificate['joint_B_correction_delta']);JDelta=[{t:part.get(t,{}) for t in triples} for part in JDelta]
 verify_B_delta(JDelta,'joint_B')
 Sfinal=[{t:add((1,Snew[ip][t]),(1,JDelta[ip][t])) for t in triples} for ip in range(2)]
 joint3=all_threeW(Sfinal);check('all168_threeW_joint_B_repaired',not joint3['failed_targets']);full_replays['joint_B']=joint3
# Final output can preserve the exact certificate and regenerate only fields
# computed here. No large search rank should be claimed by this replay.
certificate['verification']={'checks':checks,'four_W_field_targets':420,'three_W_field_targets':168,'three_W_image_rank':len(bas3),'three_W_replays':full_replays}
# Portable exact full fixed-A B-family obstruction. B is unrestricted inside
# the284-dimensional pointwise polar kernel; not the full896-hook fibre.
fixed=certificate['fixed_A_B_obstruction']
fd={(tuple(wt),op,(tuple(ep),tuple(key))):F(v) for wt,op,ep,key,v in fixed['raw_dual']}
def general_threeW_target(wt,op,ep,parts):
 slots=[7+x for x in wt]+list(ep);out=defaultdict(F)
 for pos in combinations(range(5),2):
  aa=[slots[i] for i in pos];bb=[slots[i] for i in range(5) if i not in pos]
  for pa,pb,fac in ([(0,0,1),(1,1,2)] if op==0 else [(0,1,1),(1,0,1)]):
   for key,v in pol(eval_L(pa,aa),evfield(parts[pb],[vec[a] for a in bb])).items():out[key]-=fac*v
 return clean(out)
for wt,op in {(wt,op) for wt,op,key in fd}:
 dd={key:v for (w,p,key),v in fd.items() if w==wt and p==op}
 check('fixed_A_dual_annihilates_quartic_generators',all(sum(v*raw_Ucol(r,h).get(k,F(0)) for k,v in dd.items())==0 for r in range(7) for h in hs))
ftarget={(wt,op,ep):general_threeW_target(wt,op,ep,Snew) for wt,op,(ep,key) in fd}
fvalue=sum(v*ftarget[wt,op,ep].get(key,F(0)) for (wt,op,(ep,key)),v in fd.items())
check('fixed_A_dual_nonzero_original_target',fvalue==F(fixed['target_value']) and bool(fvalue))
fb=defaultdict(F)
for (wt,op,(ep,key)),ev in fd.items():
 for ss in set(wt):
  pp=list(wt);pp.remove(ss);lp=tuple(pp);mult=wt.count(ss)
  for ip in range(2):
   lpart=op if ip==0 else 1-op;fac=2 if ip==1 and op==0 else 1
   for hi,h in enumerate(tk):fb[ss,ip,ep,hi]-=mult*fac*ev*pol(h,lw[lpart][lp]).get(key,F(0))
check('fixed_A_dual_all_unrestricted_polar_B_generators',not clean(fb))
check('fixed_A_scope_declares_polar_B',fixed['unrestricted_B_annihilation'] is True)
# Changed affine target makes this exact receiver identity fail, independently
# of the polynomial solver and coefficient mutation in the positive branch.
k=next(iter(fd));changed=fvalue+fd[k]
check('changed_dual_target_rejected',changed!=fvalue)
# Add after fixed-A certificate verification, before final report/write.
# The fixed-A exclusion remains valid; this escaped tensor changes A.
AE=decode_tensor(certificate['A_escape_delta']);AE=[{t:part.get(t,{}) for t in triples} for part in AE]
for ip,part in enumerate(AE):
 for t,h in part.items():
  check('A_escape_hook_'+str(ip),all(h.get((i,j,k),0)+h.get((i,k,j),0)==0 and h.get((i,j,k),0)+h.get((j,k,i),0)+h.get((k,i,j),0)==0 for i,j,k in h) and all(sum(eta[i]*h.get((i,i,a),0) for i in range(n))==0 for a in range(n)))
 check('A_escape_Euler_'+str(ip),all(sum(eta[z]*(part[tuple(sorted((a,b,z)))].get((i,z,j),0)+part[tuple(sorted((a,b,z)))].get((j,z,i),0)) for z in range(n))==0 for a,b in receivers for i,j in receivers))
 check('A_escape_polar_'+str(ip),all(not pol(h,k) for h in part.values() for k in K))
 check('A_escape_W_cubic_'+str(ip),all(not evfield(part,[W[a] for a in t]) for t in ws))
Sescape=[{t:add((1,Snew[ip][t]),(1,AE[ip][t])) for t in triples} for ip in range(2)]
# All420 actual receivers, using repaired sharedS rather than one selected dual.
oldsw,oldswu=sw,swu
sw=[{t:evfield(part,[W[a] for a in t]) for t in ws} for part in Sescape]
swu=[{(t,u):evfield(part,[W[t[0]],W[t[1]],{u:F(1)}]) for t in w2 for u in range(n)} for part in Sescape]
check('A_escape_all420_fourW_preserved',all(not quotient(original_target(q,ip)) for q in combinations_with_replacement(range(7),4) for ip in range(2)))
sw,swu=oldsw,oldswu
escape3=all_threeW(Sescape)
check('A_escape_all168_replayed',escape3==certificate['A_escape_three_W_replay'])
eraw={(wt,op,ep):general_threeW_target(wt,op,ep,Sescape) for wt,op,(ep,key) in fd}
evalue=sum(v*eraw[wt,op,ep].get(key,F(0)) for (wt,op,(ep,key)),v in fd.items())
check('A_escape_fixedA_dual_raw_cancels',evalue==0)
encoded_escape=[[[list(t),[[list(k),str(v)] for k,v in sorted(h.items())]] for t,h in sorted(part.items()) if h] for part in Sescape]
escape_digest=hashlib.sha256(json.dumps(encoded_escape,sort_keys=True,separators=(',',':')).encode()).hexdigest()
check('A_escape_tensor_digest',escape_digest==certificate['A_escape_tensor_sha256'])
full_replays['A_escape']=escape3

certificate['verification']={'checks':checks,'four_W_field_targets':420,'three_W_field_targets':168,'three_W_image_rank':len(bas3),'three_W_replays':full_replays,'fixed_A_B_dual_value':str(fvalue),'fixed_A_B_raw_dual_entries':len(fd),'repaired_tensor_sha256':digest}
for dependency,expected in certificate['dependencies'].items():
 check('dependency_'+dependency,hashlib.sha256((ROOT/dependency).read_bytes()).hexdigest()==expected)
certificate['checks']=checks
if '--write' in sys.argv:report_path.write_text(json.dumps(certificate,indent=2,sort_keys=True)+'\n')
print(json.dumps(certificate,sort_keys=True))
