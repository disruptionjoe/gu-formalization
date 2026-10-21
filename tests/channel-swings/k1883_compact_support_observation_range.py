#!/usr/bin/env python3
"""Actual coefficient certificates for the compact-support range theorem."""
import argparse,hashlib,json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1883-compact-support-observation-range.json'
INPUTS=['lab/process/k1832-k77-common-energy-form.json','lab/process/k1836-k77-differential-dirac-quotient.json','lab/process/k1840-k77-conservative-variable-observation.json']
def mat(v):
 M=s.zeros(v.get('rows',16),v.get('columns',16))
 for i,j,x in v['entries']:M[i,j]=s.Rational(x)
 return M
def enc(M):return {'rows':M.rows,'columns':M.cols,'entries':[[i,j,str(M[i,j])] for i in range(M.rows) for j in range(M.cols) if M[i,j]]}
def produce():
 en,src,old=[json.loads((ROOT/p).read_text()) for p in INPUTS];D=list(map(mat,src['target_D']));checks={};blocks=[]
 def ck(n,v):checks[n]=bool(v);assert v,n
 for idx,(er,sr,kr) in enumerate(zip(en['blocks'],src['blocks'],old['blocks'])):
  T=list(map(mat,sr['T']));S=mat(kr['repairs'][0]['S']);B=mat(kr['repairs'][0]['B']);H=mat(er['H']);Z=s.Matrix.vstack(*T);K=-D[0]*B
  ck('rank12_'+str(idx),Z.rank()==12)
  N=Z.T*(Z*Z.T).inv();ck('right_inverse_'+str(idx),Z*N==s.eye(12))
  ck('K_involution_'+str(idx),K==s.diag(1,-1,-1,1) and K*K==s.eye(4) and K.T==K)
  ck('mass_factorization_'+str(idx),S==24*K*T[0])
  ck('adjoint_dual_'+str(idx),S.T-24*T[0].T*K==s.zeros(16,4))
  ck('stationary_target_dual_'+str(idx),-D[0]*K-B==s.zeros(4))
  ck('complex_rank_defect_'+str(idx),(-24*T[0]+S).rank()==2)
  ck('opposite_complex_defect_'+str(idx),(24*T[0]+S).rank()==2)
  ck('real_frequency_surjectivity_'+str(idx),S.rank()==4)
  ck('no_constant_inverse_'+str(idx),Z.col_join(S).rank()==12)
  # Exact composition at independent exponential-test-field symbols.
  x=s.symbols('x0:3');r=s.symbols('r');L=s.Matrix.hstack(x[0]*s.eye(4)+24*r*K,x[1]*s.eye(4),x[2]*s.eye(4))
  ck('full_operator_reduction_'+str(idx),L*Z==sum((x[i]*T[i] for i in range(3)),s.zeros(4,16))+r*S)
  blocks.append({'K':enc(K),'right_inverse_Z':enc(N),'complex_symbol_rank':2})
 return dict(result_id='K1883',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',blocks=blocks,scope={'compact_range_codimension':4,'all_target_compact_inverse':False,'massive_L2_surjective':True,'massless_Cc_targets_have_L2_lifts_R3':True,'rotating_charges_require_inverse_frame':True,'native_GU':False,'pure_mass_rotating_lift':False},checks=checks,inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in INPUTS})
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();v=produce()
 if a.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
 else:assert v==json.loads(OUT.read_text()),'certificate drift'
 print('PASS K1883',len(v['checks']),'exact matrix groups;',len(v['inputs']),'pins')
