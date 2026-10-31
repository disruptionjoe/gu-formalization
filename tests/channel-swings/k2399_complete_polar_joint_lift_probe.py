"""K2399 exact certificate replay; no large joint search or scratch files needed."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from itertools import combinations,combinations_with_replacement,permutations
import argparse,json,hashlib,sys
parser=argparse.ArgumentParser();parser.add_argument('--root',type=Path);parser.add_argument('--certificate',type=Path);parser.add_argument('--write',action='store_true');args=parser.parse_args()
root=args.root or Path(__file__).resolve().parents[2]
p96=root/'tests/channel-swings/k2396_full_polar_coupled_repair_probe.py';code=p96.read_text()
# Reconstruct and verify the inherited anchor and all pinned predecessors.
# Stop before its write block; --write here may only update K2399's report.
env={'__file__':str(p96),'__name__':'k2399_anchor_replay'}
exec(compile(code[:code.index("if '--write' in sys.argv:")],str(p96),'exec'),env)
globals().update({k:v for k,v in env.items() if not k.startswith('__')})
print('K2396 inherited anchor replay passed',flush=True)
ROOT=root;newpath=args.certificate or ROOT/'lab/process/k2399-complete-polar-joint-lift.json';new=json.loads(newpath.read_text())
for dep,digest_expected in new['dependencies'].items():
 if hashlib.sha256((ROOT/dep).read_bytes()).hexdigest()!=digest_expected:raise AssertionError('dependency_'+dep)
deltas=decode_tensor(new['ambient_delta']);deltas=[{t:part.get(t,{}) for t in triples} for part in deltas]
# Reconstruct saved25 raw A/B coefficients plus exact C coefficients. This
# removes the search matrix, chosen right inverses and private caches from acceptance.
betas=[{q:F(1)/W[r][q]} for r,(p,q) in enumerate(pairs)];covs=alphas+betas
pars=[[],[]]
for typ,a,b,hi,ip,v in new['raw_joint_solution']:
 if typ=='A':pp=w2[a];t=(b,7+pp[0],7+pp[1])
 elif typ=='B':ep=EP[b];t=(ep[0],ep[1],7+a)
 else:raise AssertionError('unknown coefficient kind')
 pars[ip].append((t,hi,F(v)))
for ip,part in enumerate(new['C_coefficients']):
 pars[ip].extend((tuple(t),hi,F(v)) for t,hi,v in part)
rebuilt=[]
for ip in range(2):
 ff={t:{} for t in triples}
 for t,hi,v in pars[ip]:
  for perm in set(permutations(t)):
   for a,va in covs[perm[0]].items():
    for b,vb in covs[perm[1]].items():
     for c,vc in covs[perm[2]].items():
      if a<=b<=c:ff[a,b,c]=add((1,ff[a,b,c]),(v*va*vb*vc,tk[hi]))
 rebuilt.append(ff)
if rebuilt!=deltas:raise AssertionError('raw_coefficients_reconstruct_ambient_delta')
expected2=new['two_W_next']

newchecks={}
def nc(name,value):
 newchecks[name]=bool(value)
 if not value:raise AssertionError(name)
for ip,part in enumerate(deltas):
 for t,h in part.items():
  nc('hook_antisymmetry_'+str(ip),all(h.get((i,j,k),0)+h.get((i,k,j),0)==0 for i,j,k in h))
  nc('hook_cyclic_'+str(ip),all(h.get((i,j,k),0)+h.get((j,k,i),0)+h.get((k,i,j),0)==0 for i,j,k in h))
  nc('hook_trace_'+str(ip),all(sum(eta[i]*h.get((i,i,a),0) for i in range(n))==0 for a in range(n)))
 nc('all11025_Euler_'+str(ip),all(sum(eta[z]*(part[tuple(sorted((a,b,z)))].get((i,z,j),0)+part[tuple(sorted((a,b,z)))].get((j,z,i),0)) for z in range(n))==0 for a,b in receivers for i,j in receivers))
 nc('full_pointwise_polar_'+str(ip),all(not pol(h,k) for h in part.values() for k in K))
 nc('W3_fixed_'+str(ip),all(not evfield(part,[W[a] for a in t]) for t in ws))
Sfinal=[{t:add((1,Snew[ip][t]),(1,deltas[ip][t])) for t in triples} for ip in range(2)]
sw=[{t:evfield(part,[W[a] for a in t]) for t in ws} for part in Sfinal]
swu=[{(t,u):evfield(part,[W[t[0]],W[t[1]],{u:F(1)}]) for t in w2 for u in range(n)} for part in Sfinal]
def final_fourW_target(quad,op,sc3,sc2):
 out=defaultdict(F)
 for u in range(n):
  for aa in range(4):
   st=tuple(quad[j] for j in range(4) if j!=aa)
   for pa,pb,fac in ([(0,0,1),(1,1,2)] if op==0 else [(0,1,1),(1,0,1)]):
    for key,v in pol(sc3[pa][st],lwu[pb][quad[aa],u]).items():out[u,key]-=fac*v
  for pos in combinations(range(4),2):
   lt=tuple(quad[j] for j in pos);st=tuple(quad[j] for j in range(4) if j not in pos)
   for pa,pb,fac in ([(0,0,1),(1,1,2)] if op==0 else [(0,1,1),(1,0,1)]):
    for key,v in pol(sc2[pa][st,u],lw[pb][lt]).items():out[u,key]-=fac*v
 return clean(out)
def all_fourW(tensor_parts):
 local3=[{t:evfield(part,[W[a] for a in t]) for t in ws} for part in tensor_parts]
 local2=[{(t,u):evfield(part,[W[t[0]],W[t[1]],{u:F(1)}]) for t in w2 for u in range(n)} for part in tensor_parts]
 return [[list(q),ip] for q in combinations_with_replacement(range(7),4) for ip in range(2) if quotient(final_fourW_target(q,ip,local3,local2))]
nc('complete420_fourW_targets',not all_fourW(Sfinal))
nc('same_fourW_checker_original13_failures',len(all_fourW(S))==13)
nc('same_fourW_checker_anchor0_failures',not all_fourW(Snew))
final3=all_threeW(Sfinal)
nc('complete168_threeW_targets',not final3['failed_targets'])
# Changed actual ambient coefficient, while checker and target remain fixed.
mut=[{t:dict(h) for t,h in part.items()} for part in deltas];tt=next(t for t,h in mut[0].items() if h);mut[0][tt]=add((1,mut[0][tt]),(1,hs[0]))
nc('changed_ambient_coefficient_fails_Euler',any(sum(eta[z]*(mut[0][tuple(sorted((a,b,z)))].get((i,z,j),0)+mut[0][tuple(sorted((a,b,z)))].get((j,z,i),0)) for z in range(n)) for a,b in receivers for i,j in receivers))
# Change actual final tensors, and run the same sector checkers unchanged.
mut4=[{t:add((1,Sfinal[ip][t]),(-1,Delta[ip][t])) for t in triples} for ip in range(2)]
nc('changed_actual_final_tensor_fails_fourW',bool(all_fourW(mut4)))
mut3=[{t:add((1,Sfinal[ip][t]),(-1,deltas[ip][t])) for t in triples} for ip in range(2)]
nc('changed_actual_final_tensor_fails_threeW',bool(all_threeW(mut3)['failed_targets']))
enc=[[[list(t),[[list(k),str(v)] for k,v in sorted(h.items())]] for t,h in sorted(part.items()) if h] for part in Sfinal]
final_digest=hashlib.sha256(json.dumps(enc,sort_keys=True,separators=(',',':')).encode()).hexdigest()
verification={'checks':newchecks,'four_W_field_targets':420,'three_W_field_targets':168,'three_W_replay':final3,'ambient_delta_entries':[sum(map(len,p.values())) for p in deltas]}

"""Complete next two-W quartic image and actual repaired tensor targets."""
ET=list(combinations_with_replacement(range(7),3))
def raw2col(ep,h):
 out=defaultdict(F)
 for e in range(7):
  et=tuple(sorted((*ep,e)));mult=et.count(e)
  for k,v in pol(h,KE[e]).items():out[et,k]+=mult*v
 return clean(out)
def annihilates_twoW(dd):
 for ep in EP:
  for h in hs:
   column=raw2col(ep,h)
   if sum(v*column.get(k,F(0)) for k,v in dd.items())!=0:return False
 return True
bas2={};rec2={}
for ei,ep in enumerate(EP):
 for hi,h in enumerate(hs):
  cc=raw2col(ep,h);hist={}
  while cc:
   k=min(cc);v=cc[k]
   if k not in bas2:bas2[k]={j:x/v for j,x in cc.items()};rec2[k]=((ep,hi),v,hist);break
   hist[k]=v
   for j,x in bas2[k].items():
    z=cc.get(j,F(0))-v*x
    if z:cc[j]=z
    elif j in cc:del cc[j]
 if ei%4==0:print('twoW full map pair',ei,'rank',len(bas2),flush=True)
cacheL2={};cacheS2={}
def getL2(ip,aa):
 tag=(ip,*sorted(aa))
 if tag not in cacheL2:cacheL2[tag]=eval_L(ip,aa)
 return cacheL2[tag]
def getS2(ip,aa,parts):
 tag=(id(parts),ip,*sorted(aa))
 if tag not in cacheS2:cacheS2[tag]=evfield(parts[ip],[vec[a] for a in aa])
 return cacheS2[tag]
def target2(wp,op,parts):
 out=defaultdict(F)
 for et in ET:
  slots=[7+x for x in wp]+list(et)
  for pos in combinations(range(5),2):
   aa=[slots[i] for i in pos];bb=[slots[i] for i in range(5) if i not in pos]
   for pa,pb,fac in ([(0,0,1),(1,1,2)] if op==0 else [(0,1,1),(1,0,1)]):
    for k,v in pol(getL2(pa,aa),getS2(pb,bb,parts)).items():out[et,k]-=fac*v
 return clean(out)
failed2=[];first2=None;rescount2=0
for wp in EP:
 for op in range(2):
  raw=target2(wp,op,Sfinal);cc=dict(raw);res={}
  while cc:
   k=min(cc);v=cc[k]
   if k not in bas2:res[k]=v;del cc[k];continue
   for j,x in bas2[k].items():
    z=cc.get(j,F(0))-v*x
    if z:cc[j]=z
    elif j in cc:del cc[j]
  if res:
   failed2.append([list(wp),op]);rescount2+=len(res)
   if first2 is None:
    obs=min(res);dual2={obs:F(1)}
    for k in sorted(bas2,reverse=True):
     v=-sum(x*dual2.get(j,F(0)) for j,x in bas2[k].items() if j!=k)
     if v:dual2[k]=v
    nc('twoW_dual_all25088_original_quartic_generators',annihilates_twoW(dual2))
    vv=sum(v*raw.get(k,F(0)) for k,v in dual2.items());nc('twoW_dual_nonzero_actual_target',vv==res[obs] and vv!=0)
    first2={'W_pair':list(wp),'field_part':op,'dual':[[list(et),list(k),str(v)] for (et,k),v in sorted(dual2.items())],'value':str(vv)}
next2={'full_map_columns':25088,'full_map_rank':len(bas2),'full_field_targets':56,'failed_targets':failed2,'residual_entries':rescount2,'first_obstruction':first2,'scope':'Complete necessary two-W fifth-algebraic test of this constructed cubic only; other A/B/C choices remain open.'}
print('TWO-W NEXT','rank',len(bas2),'failures',len(failed2),'dual entries',len(first2['dual']) if first2 else 0,flush=True)
new['two_W_next']=next2

nc('stored_twoW_certificate_recomputed',next2==expected2)
nc('final_tensor_digest',final_digest==new['repaired_tensor_sha256'])
nc('raw25_coefficients_reconstruct_actual_delta',rebuilt==deltas and len(new['raw_joint_solution'])==25)
# Portable positive C-kernel continuation: reconstruct, never rerun its search.
ce=new['C_kernel_escape'];ci=ce['input_part'];scaleC=F(ce['scale'])
cd=[{t:{} for t in triples} for _ in range(2)]
for et0,hi,v0 in ce['witness']:
 et=tuple(et0);v=F(v0)
 for perm in set(permutations(et)):
  for a,va in alphas[perm[0]].items():
   for b,vb in alphas[perm[1]].items():
    for c,vc in alphas[perm[2]].items():
     if a<=b<=c:cd[ci][a,b,c]=add((1,cd[ci][a,b,c]),(scaleC*v*va*vb*vc,tk[hi]))
cd_stored=decode_tensor(ce['ambient_delta']);cd_stored=[{t:part.get(t,{}) for t in triples} for part in cd_stored]
nc('C_escape_coefficients_reconstruct_ambient',cd==cd_stored)
nc('C_escape_full_Euler',all(sum(eta[z]*(part[tuple(sorted((a,b,z)))].get((i,z,j),0)+part[tuple(sorted((a,b,z)))].get((j,z,i),0)) for z in range(n))==0 for part in cd for a,b in receivers for i,j in receivers))
nc('C_escape_hook',all(all(h.get((i,j,k),0)+h.get((i,k,j),0)==0 and h.get((i,j,k),0)+h.get((j,k,i),0)+h.get((k,i,j),0)==0 for i,j,k in h) and all(sum(eta[i]*h.get((i,i,a),0) for i in range(n))==0 for a in range(n)) for part in cd for h in part.values()))
nc('C_escape_polar',all(not pol(h,k) for part in cd for h in part.values() for k in K))
nc('C_escape_zero_oneW',all(not evfield(part,[e1,e2,w]) for part in cd for e1 in vec for e2 in vec for w in W))
Sc=[{t:add((1,Sfinal[ip][t]),(1,cd[ip][t])) for t in triples} for ip in range(2)]
obsC=next2['first_obstruction'];wpc=tuple(obsC['W_pair']);opc=obsC['field_part'];duc={(tuple(et),tuple(k)):F(v) for et,k,v in obsC['dual']}
rawc=target2(wpc,opc,Sc)
nc('C_escape_actual_twoW_dual_cancels',sum(v*rawc.get(k,F(0)) for k,v in duc.items())==0)
nc('C_escape_scale_and_dual_change',scaleC*F(ce['dual_change'])==-F(obsC['value']))
nc('C_escape_all420_fourW_preserved',not all_fourW(Sc))
nc('C_escape_all168_threeW_preserved',not all_threeW(Sc)['failed_targets'])
def replay_twoW(parts):
 bad=[];nr=0
 for wp0 in EP:
  for op0 in range(2):
   cc=target2(wp0,op0,parts);rr={}
   while cc:
    k=min(cc);v=cc[k]
    if k not in bas2:rr[k]=v;del cc[k];continue
    for j,x in bas2[k].items():
     z=cc.get(j,F(0))-v*x
     if z:cc[j]=z
     elif j in cc:del cc[j]
   if rr:bad.append([list(wp0),op0]);nr+=len(rr)
 return {'failed_targets':bad,'residual_entries':nr}
nc('C_escape_complete56_replay',replay_twoW(Sc)==ce['twoW_replay'])

print('C escape original tensor replay passed',flush=True)
# Whole fixed-A/B C-family obstruction lifted to original receivers.
co=new['fixed_A_B_C_obstruction'];crd={}
for sc,t,ip,k,v in co['raw_dual']:
 crd[sc,tuple(t),ip,(tuple(k[0]),tuple(k[1])) if sc==1 else tuple(k)]=F(v)
for wp,op in {(t,ip) for (sc,t,ip,k) in crd if sc==1}:
 dd={k:v for (sc,t,ip,k),v in crd.items() if (sc,t,ip)==(1,wp,op)}
 nc('C_family_dual_all25088_original_quartic_generators',annihilates_twoW(dd))
recs=list(combinations_with_replacement(range(n),2))
def c_contract(h,a):return clean({ij:sum(eta[m]*v*(h.get((ij[0],m,ij[1]),0)+h.get((ij[1],m,ij[0]),0)) for m,v in a.items()) for ij in recs})
ca={(r,hi):c_contract(h,a) for r,a in enumerate(alphas) for hi,h in enumerate(tk)}
cf=defaultdict(F)
for (sc,t,op,key),ev in crd.items():
 if sc==0:
  for r in range(7):
   et=tuple(sorted((*t,r)))
   for hi in range(284):cf[et,op,hi]+=ev*ca[r,hi].get(key,F(0))
 else:
  et,pk=key
  for ip in range(2):
   lp=op if ip==0 else 1-op;fac=2 if ip==1 and op==0 else 1
   for hi,h in enumerate(tk):cf[et,ip,hi]-=ev*fac*pol(h,lw[lp][t]).get(pk,F(0))
nc('C_family_dual_all47712_original_realified_C_generators',not clean(cf))
def C_affine_contraction(parts):
 out=F(0)
 for wp,op in {(t,ip) for (sc,t,ip,k) in crd if sc==1}:
  raw=target2(wp,op,parts)
  out-=sum(v*raw.get(k,F(0)) for (sc,t,ip,k),v in crd.items() if (sc,t,ip)==(1,wp,op))
 return out
cvalue=C_affine_contraction(Sfinal)
nc('C_family_dual_nonzero_actual_affine_target',cvalue==F(co['target_contraction']) and cvalue!=0)
nc('C_family_dual_unchanged_by_C_escape',C_affine_contraction(Sc)==cvalue)
# Corrupt an actual original dual coefficient, then execute the identical
# original-generator predicate. This is not a changed expected value/check.
mutated=False
for (sc,wp,op,key),value in crd.items():
 if sc!=1:continue
 if not any(raw2col(ep,h).get(key,F(0)) for ep in EP for h in hs):continue
 dd={k:v for (s,t,ip,k),v in crd.items() if (s,t,ip)==(1,wp,op)}
 dd[key]+=1
 nc('changed_original_C_dual_rejected_by_same_generator_check',not annihilates_twoW(dd))
 mutated=True;break
nc('C_dual_coefficient_mutation_executed',mutated)
co['verification']={'original_raw_entries':len(crd),'Euler_multiplier_entries':sum(sc==0 for sc,t,ip,k in crd),'C_field_coordinates':23856,'C_Euler_kernel_field_coordinates':20945,'target_contraction':str(cvalue),'scope':'Complete C-only exclusion at constructed fixed A/B and W3; arbitrary simultaneous A/B/C changes remain open.'}

new['verification']=verification
if args.write:newpath.write_text(json.dumps(new,indent=2,sort_keys=True)+'\n')
print(json.dumps(new,sort_keys=True))
