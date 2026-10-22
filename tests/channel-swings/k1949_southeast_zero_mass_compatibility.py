"""Exact lower-order southeast-zero repair and two-input obstruction."""
import argparse, hashlib, json
from pathlib import Path
from sage.all import QQ,matrix,vector,identity_matrix,PolynomialRing,block_matrix
from k1836_k77_differential_dirac_quotient import mat,enc,clifford
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1949-southeast-zero-mass-compatibility.json'
INPUTS=['lab/process/k1945-energy-compatible-raw-columns.json','lab/process/k1947-minimal-raw-input-support.json','lab/process/k1840-k77-conservative-variable-observation.json','lab/process/k1832-k77-common-energy-form.json']
def polyenc(p):return [[list(e),str(c)] for e,c in sorted(p.dict().items())]
def produce():
 r,k,m,en=[json.loads((ROOT/p).read_text()) for p in INPUTS];checks={};rows=[];d=[x/24 for x in clifford()]
 def ck(key,b):checks[key]=bool(b);assert b,key
 Traw=mat(r['Traw']);ck('nonzero_SE_principal_invertible',Traw.rank()==128)
 for typ in range(4):
  b=next(x for x in r['blocks'] if x['type']==typ);ix=r['blocks'].index(b);F=mat(b['basis']);H=mat(b['H']);ts=list(map(mat,b['T']));A=list(map(mat,en['blocks'][typ]['matrices']));outrows=[x for x in b['coordinates'] if x<128]
  Rall=mat(r['R'])[:,16*ix:16*(ix+1)];R=Rall.matrix_from_rows(outrows)
  ck(f'raw_return_output_permutation_{typ}',Rall.matrix_from_rows([i for i in range(128) if i not in outrows])==0)
  E=matrix(QQ,20,4,{(i+16,i):1 for i in range(4)});V=F.solve_right(E);K=mat(k['blocks'][typ]['invisible_kernel']);U=R*K;W=K.transpose()*H*V
  ck(f'pure_auxiliary_{typ}',F*V==E)
  for j in range(3):ck(f'zero_SE_principal_surgery_leak_rank4_{typ}_{j}',(mat(b['Q'])*A[j]).rank()==4)
  ck(f'full_invisible_SE_map_injective_{typ}',U.rank()==4 and W.rank()==4)
  repaired=[]
  for a,z in enumerate(m['blocks'][typ]['repairs']):
   C,B,S=map(mat,[z['C'],z['B'],z['S']]);Z=-U.inverse()*R*C*V*W.inverse();Cp=C+K*Z*K.transpose()*H
   ck(f'repair_skew_{typ}_{a}',Z+Z.transpose()==0 and H*Cp+Cp.transpose()*H==0)
   ck(f'zero_raw_SE_{typ}_{a}',R*Cp*V==0)
   ck(f'exact_first_order_{typ}_{a}',all(ts[i]*Cp-B*ts[i]+S*A[i]-d[i]*S==0 for i in range(3)))
   ck(f'exact_profile_{typ}_{a}',ts[0]*Cp==d[0]*S and S*Cp==B*S)
   ck(f'observation_unchanged_{typ}_{a}',all(t*(Cp-C)==0 for t in ts) and S*(Cp-C)==0)
   factors=[]
   for mask in [23,27,29,30]:
    ids=[j for j,c in enumerate(b['coordinates']) if mask&(1<<(c//128))];Q=F.matrix_from_rows(ids);fac=Cp*Q.inverse();ck(f'raw_factor_{typ}_{a}_{mask}',fac*Q==Cp)
    factors.append({'mask':mask,'factor':enc(fac)})
   repaired.append({'C':enc(Cp),'Z':enc(Z),'factors':factors})
  S1,S2=[mat(z['S']) for z in m['blocks'][typ]['repairs']];B1,B2=[mat(z['B']) for z in m['blocks'][typ]['repairs']];C1,C2=[mat(z['C']) for z in repaired]
  ck(f'cross_profile_{typ}',S1*C2+S2*C1==B1*S2+B2*S1)
  rec=next(x for x in k['constant_mass_free_observation']['rows'] if x['type']==typ and x['slots']==[0,4]);Q=mat(rec['input_basis']);N=H.inverse()*Q.transpose();cb=[]
  for i in range(Q.nrows()):
   for j in range(i+1,Q.nrows()):
    z=matrix(QQ,Q.nrows(),Q.nrows());z[i,j]=1;z[j,i]=-1;cb.append(N*z*Q)
  oldker=mat(rec['kernel']);cs=[sum((v[j]*cb[j] for j in range(len(cb))),matrix(QQ,16,16)) for v in oldker.rows()];se=matrix(QQ,[(R*c*V).list() for c in cs]).transpose();ker=se.right_kernel().basis_matrix()*oldker
  ck(f'five_dimensional_SE0_{typ}',ker.nrows()==5 and ker.rank()==5)
  PR=PolynomialRing(QQ,5,'w');ww=PR.gens();pars=vector(PR,ww)*ker
  C=sum((pars[j]*cb[j] for j in range(len(cb))),matrix(PR,16,16));S=matrix(PR,4,16,pars[len(cb):len(cb)+64]);B=pars[-2]*B1+pars[-1]*B2
  ck(f'polynomial_first_order_{typ}',all(ts[i]*C-B*ts[i]+S*A[i]-d[i]*S==0 for i in range(3)) and R*C*V==0)
  res=(S*C-B*S).list();mons=sorted({e for p in res for e in p.dict()});coef=matrix(QQ,[[p.dict().get(e,0) for e in mons] for p in res]);ids=list(coef.transpose().pivots());eqs=[res[j] for j in ids]
  qm=[ww[i]*ww[j] for i in range(5) for j in range(i,5)];products=[h*p for p in eqs for h in qm];mass=(pars[-2]**2+pars[-1]**2)**2;allmons=sorted({e for p in products+[mass] for e in p.dict()});equations=matrix(QQ,[[p.dict().get(e,0) for p in products] for e in allmons]);sol=equations.solve_right(vector(QQ,[mass.dict().get(e,0) for e in allmons]));mult=[sum(sol[15*i+j]*qm[j] for j in range(15)) for i in range(len(eqs))]
  ck(f'exact_mass_fourth_power_identity_{typ}',sum(a*b for a,b in zip(mult,eqs))==mass and mass!=0)
  rows.append({'type':typ,'raw_return':enc(R),'auxiliary_inclusion':enc(V),'invisible_carrier':enc(K),'repairs':repaired,'two_slot_zero_SE':{'kernel':enc(ker),'residual_indices':ids,'multipliers':list(map(polyenc,mult)),'mass_fourth_power':polyenc(mass)}})
 # Every physical copy has the verified local type and disjoint raw coordinate labels.
 time_sets=[];aux_sets=[]
 for ix,b in enumerate(r['blocks']):
  rec=rows[b['type']];rep=next(x for x in r['blocks'] if x['type']==b['type']);outrows=[x for x in b['coordinates'] if x<128];auxrows=[x-512 for x in b['coordinates'] if x>=512]
  ck(f'actual_global_copy_{ix}',b['basis']==rep['basis'] and b['H']==rep['H'] and b['T']==rep['T'] and mat(r['R']).matrix_from_rows(outrows)[:,16*ix:16*(ix+1)]==mat(rec['raw_return']))
  time_sets+=outrows;aux_sets+=auxrows
 ck('global_permutations_cover128',sorted(time_sets)==list(range(128))==sorted(aux_sets))
 return {'result_id':'K1949','status':'active_research','classification':'INTERNAL_STRUCTURAL_ONLY','target_claim':'NONE-NOT-A-KILL','blocks':rows,'principal_scope':'Only the added zeroth-order SE coefficient vanishes. Fixed principal Traw is invertible and cannot equal the displayed source SE-zero operator.','results':{'unique_fixed_observation_zero_SE_repair_all32':True,'same_universal_profiles_and_domains':True,'minimal_raw_input_slots':4,'constant_single_copy_two_slot_nonzero_mass_with_zero_SE':False,'cross_copy_free_observation_exclusion':False,'source_barred_pairing_identified':False},'checks':checks,'inputs':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in INPUTS}}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();v=produce()
 if a.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
 else:assert v==json.loads(OUT.read_text()),'certificate drift'
 print('PASS K1949',len(v['checks']),'exact controls')
