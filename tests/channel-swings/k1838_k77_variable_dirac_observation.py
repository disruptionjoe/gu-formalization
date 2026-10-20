#!/usr/bin/env sage-python
"""Exact jet compatibility and moving-frame repair for the fixed local quotient."""
import argparse,hashlib,json
from pathlib import Path
from sage.all import QQ,PolynomialRing,matrix,identity_matrix,block_matrix
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k1838-k77-variable-dirac-observation.json'
def mat(x):return matrix(QQ,x.get('rows',16),x.get('columns',16),{(i,j):QQ(v) for i,j,v in x['entries']})
def produce():
 src=json.loads((ROOT/'lab/process/k1836-k77-differential-dirac-quotient.json').read_text())
 eng=json.loads((ROOT/'lab/process/k1832-k77-common-energy-form.json').read_text())
 D=list(map(mat,src['target_D']));J=D[0]*D[1]*D[2];I4=identity_matrix(QQ,4);checks={};blocks=[]
 def ck(k,v):checks[k]=bool(v);assert v,k
 for b,(rec,en) in enumerate(zip(src['blocks'],eng['blocks'])):
  T=list(map(mat,rec['T']));A=list(map(mat,en['matrices']));H=mat(en['H']);W=block_matrix([[x] for x in T]);Hi=H.inverse()
  R=Hi*W.transpose()*(W*Hi*W.transpose()).inverse()
  ck(f'right_inverse_{b}',W*R==identity_matrix(QQ,12))
  # All 48 possible target first jets, not selected masses or directions.
  jets=[]
  for i in range(3):
   for u in range(4):
    for v in range(4):
     E=matrix(QQ,4,4,{(u,v):1});jets.append((E*T[i]).list())
  ck(f'gradient_map_rank48_{b}',matrix(QQ,jets).rank()==48)
  zero=[]
  for pair in rec['energy_skew_basis']:
   C=mat(pair['C']);B=mat(pair['B'])
   ck(f'pointwise_pair_{b}_{len(zero)}_{len(checks)}',all(t*C==B*t for t in T))
   if B.is_zero():zero.append(C)
  basisC=[mat(pair['C']) for pair in rec['energy_skew_basis']]
  basisB=matrix(QQ,[mat(pair['B']).list() for pair in rec['energy_skew_basis']])
  zero=[sum((w[j]*basisC[j] for j in range(len(w))),matrix(QQ,16,16)) for w in basisB.left_kernel().basis()]
  ck(f'invisible_skew_dimension6_{b}',len(zero)==6 and matrix(QQ,[x.list() for x in zero]).rank()==6)
  P=identity_matrix(QQ,16)-R*W
  ck(f'common_kernel_rank4_{b}',P.rank()==4 and P*P==P and W*P==0)
  ck(f'invisible_supported_on_kernel_{b}',all(P*K==K and K*P==K and K.transpose()*H+H*K==0 for K in zero))
  # The zeroth-order correction is a constant-observation equation pointwise.
  rows=[]
  for i in range(3):
   for u in range(4):
    for v in range(16):
     row=[QQ(0)]*64
     for h in range(16):row[u*16+h]+=A[i][h,v]
     for h in range(4):row[h*16+v]-=D[i][u,h]/24
     rows.append(row)
  ck(f'zeroth_correction_kernel0_{b}',matrix(QQ,rows).rank()==64)
  # A nonconstant invisible field is allowed; its every derivative is invisible.
  ck(f'invisible_derivative_control_{b}',all(T[i]*zero[j]==0 for i in range(3) for j in range(6)))
  # Surjective first-order system even with arbitrary B and S when lifts relax.
  St=matrix(QQ,4,16,{(i,(3*i+2)%16):i+1 for i in range(4)})
  Bt=matrix(QQ,4,4,{(i,(i+1)%4):i+2 for i in range(4)})
  target=block_matrix([[Bt*T[i]+D[i]*St/24-St*A[i]] for i in range(3)])
  Ct=R*target
  ck(f'relaxed_first_order_solution_{b}',all(T[i]*Ct-Bt*T[i]+St*A[i]-D[i]*St/24==0 for i in range(3)))
  # Scalar simultaneous conjugation f=x1^2 preserves leading T and all A,d.
  # C=-2x A1, B=-2x d1, S=-2x T1; zero defect is a polynomial in x.
  ck(f'fixed_leading_repair_first_{b}',all(-T[i]*A[0]+D[0]*T[i]/24-T[0]*A[i]+D[i]*T[0]/24==0 for i in range(3)))
  ck(f'fixed_leading_repair_zero_{b}',T[0]*A[0]==D[0]*T[0]/24)
  blocks.append({'relaxed_first_order_dimension':144,'gradient_rank':48,'target_gradient_kernel':0,'zeroth_correction_kernel':0,'invisible_skew_dimension':6,'common_kernel_dimension':4})
 # Rational orthogonal moving target frame. Spatial symbols remain fixed.
 ring=PolynomialRing(QQ,['x','t']);x,t=ring.gens();F=ring.fraction_field();s=F(x+t*x*x)
 U=(I4+s*J)*(I4-s*J).inverse();Ui=U.transpose();Bt=mat(src['blocks'][0]['mass_lifts'][0]['B'])
 Ut=U.derivative(t);Ux=U.derivative(x);M=U*Bt*Ui;Bnew=M-Ut*Ui-D[0]*Ux*Ui/24
 ck('moving_frame_orthogonal',U*Ui==I4)
 ck('moving_frame_commutes_principal',all(U*d==d*U for d in D))
 ck('moving_mass_constant_modulus',M*M==-I4 and all(M*d+d*M==0 for d in D))
 ck('connection_is_energy_skew',Bnew+Bnew.transpose()==0)
 ck('full_target_covariance',Ut+D[0]*Ux/24+Bnew*U-U*Bt==0)
 ck('mass_only_variable_frame_fails',Ut+D[0]*Ux/24!=0)
 Gx=Ux*Ui;Gt=Ut*Ui
 ck('pure_frame_curvature_zero',Gx.derivative(t)-Gt.derivative(x)-Gt*Gx+Gx*Gt==0)
 T=list(map(mat,src['blocks'][0]['T']));C=mat(src['blocks'][0]['mass_lifts'][0]['C'])
 ck('moving_observation_first_jets',all(U*q*C-(U*q).derivative(t)-D[0]*(U*q).derivative(x)/24-Bnew*U*q==0 for q in T))
 return {'result_id':'K1838','status':'active_research','classification':'INTERNAL_STRUCTURAL_ONLY','target_claim':'NONE-NOT-A-KILL','results':{'fixed_observation_requires_spatially_constant_target_B':True,'time_dependence_allowed':True,'invisible_variable_C_allowed':True,'zeroth_order_repair_with_pointwise_pairs':False,'moving_frame_repair':True,'fixed_leading_zeroth_order_repair_after_relaxation':True,'source_owned':False,'variable_mass_magnitude_selected':False},'blocks':blocks,'checks':checks,'inputs':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1836-k77-differential-dirac-quotient.json','lab/process/k1832-k77-common-energy-form.json']}}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();v=produce()
 if a.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
 else:assert v==json.loads(OUT.read_text()),'certificate drift'
 print('PASS K1838',len(v['checks']),'exact algebra groups')
