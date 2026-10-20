#!/usr/bin/env sage-python
"""Conservative full observation class and exact one-coordinate mass repairs."""
import argparse, hashlib, json
from pathlib import Path
from sage.all import QQ, matrix, identity_matrix, vector
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k1840-k77-conservative-variable-observation.json'
def mat(x):
 return matrix(QQ,x.get('rows',16),x.get('columns',16),{(i,j):QQ(v) for i,j,v in x['entries']})
def enc(M):
 return {'rows':int(M.nrows()),'columns':int(M.ncols()),'entries':[[int(i),int(j),str(v)] for (i,j),v in sorted(M.dict().items())]}
def spaces(T,A,d,H):
 Hi=H.inverse();CB=[];BB=[];SB=[]
 for i in range(16):
  for j in range(i+1,16):CB.append(Hi*matrix(QQ,16,16,{(i,j):1,(j,i):-1}))
 for i in range(4):
  for j in range(i+1,4):BB.append(matrix(QQ,4,4,{(i,j):1,(j,i):-1}))
 for i in range(4):
  for j in range(16):SB.append(matrix(QQ,4,16,{(i,j):1}))
 cols=[sum([(t*C).list() for t in T],[]) for C in CB]
 cols += [sum([(-B*t).list() for t in T],[]) for B in BB]
 cols += [sum([(S*A[i]-d[i]*S).list() for i in range(3)],[]) for S in SB]
 E=matrix(QQ,cols).transpose();K=E.right_kernel()
 def decode(w):
  C=sum((w[j]*CB[j] for j in range(120)),matrix(QQ,16))
  B=sum((w[120+j]*BB[j] for j in range(6)),matrix(QQ,4))
  return C,B,matrix(QQ,4,16,w[126:])
 return E,K,decode,CB

def produce():
 src=json.loads((ROOT/'lab/process/k1836-k77-differential-dirac-quotient.json').read_text())
 eng=json.loads((ROOT/'lab/process/k1832-k77-common-energy-form.json').read_text())
 D=list(map(mat,src['target_D']));d=[v/24 for v in D];J=D[0]*D[1]*D[2];I4=identity_matrix(QQ,4)
 checks={};blocks=[]
 def ck(k,v):checks[k]=bool(v);assert v,k
 masses=[mat(p['B']) for p in src['blocks'][0]['mass_lifts']]
 ck('mass_plane_Clifford',all(B*B==-I4 and B.transpose()==-B and all(B*z+z*B==0 for z in D) for B in masses) and masses[0]*masses[1]+masses[1]*masses[0]==0)
 for ix,(rec,en) in enumerate(zip(src['blocks'],eng['blocks'])):
  T=list(map(mat,rec['T']));A=list(map(mat,en['matrices']));H=mat(en['H']);Hi=H.inverse();alpha=QQ(rec['alpha'])
  E,K,decode,CB=spaces(T,A,d,H);triples=[decode(w) for w in K.basis()]
  ck(f'full_rank146_nullity44_{ix}',E.rank()==146 and K.dimension()==44)
  ck(f'complete_target_skew_image6_{ix}',matrix(QQ,[B.list() for C,B,S in triples]).rank()==6)
  ck(f'correction_image35_{ix}',matrix(QQ,[S.list() for C,B,S in triples]).rank()==35)
  # Independent arbitrary profiles in x1 share one observation and fixed energies.
  repairs=[]
  for n,B in enumerate(masses):
   F=D[0]*B;S=-24*F*T[0]
   rhs=vector(QQ,sum([(B*T[i]+d[i]*S-S*A[i]).list() for i in range(3)],[]))
   w=E[:,:120].solve_right(rhs);C=sum((w[j]*CB[j] for j in range(120)),matrix(QQ,16))
   ck(f'repair_first_order_{ix}_{n}',all(T[i]*C-B*T[i]+S*A[i]-d[i]*S==0 for i in range(3)))
   ck(f'repair_derivative_{ix}_{n}',T[0]*C==d[0]*S)
   ck(f'repair_nonlinear_{ix}_{n}',S*C==B*S)
   ck(f'repair_positive_energy_{ix}_{n}',H*C+C.transpose()*H==0 and B+B.transpose()==0)
   ck(f'zeroth_rank4_{ix}_{n}',S.rank()==4)
   ck(f'gram_first_order_zero_{ix}_{n}',all(T[i]*Hi*S.transpose()-S*Hi*T[i].transpose()==0 for i in range(3)))
   ck(f'gram_derivative_{ix}_{n}',T[0]*Hi*S.transpose()==-24*alpha*F)
   ck(f'gram_potential_{ix}_{n}',S*Hi*S.transpose()==576*alpha*I4)
   repairs.append({'B':enc(B),'C':enc(C),'S':enc(S)})
  C1,C2=[mat(v['C']) for v in repairs];B1,B2=masses;S1,S2=[mat(v['S']) for v in repairs]
  ck(f'cross_profile_nonlinear_{ix}',S1*C2+S2*C1==B1*S2+B2*S1)
  ck(f'cross_profile_gram_{ix}',S1*Hi*S2.transpose()+S2*Hi*S1.transpose()==0)
  # Arbitrary two-coordinate dependence with the SAME factorized triple.
  maps=matrix(QQ,[sum([(T[i]*C-d[i]*S).list() for i in [0,1]],[]) for C,B,S in triples]).transpose()
  km=maps.right_kernel();rest=[decode(sum((v[j]*K.basis()[j] for j in range(len(v))),K.zero())) for v in km.basis()]
  ck(f'two_axis_factorized_kernel6_{ix}',km.dimension()==6 and all(B==0 and S==0 and all(t*C==0 for t in T) for C,B,S in rest))
  # Natural U(1) connection subclass is rigid, but not the full44 space.
  Js=mat(en['J'])
  if T[0]*Js==-J*T[0]:Js=-Js
  ck(f'complex_intertwiner_{ix}',all(T[i]*Js==J*T[i] and Js*A[i]==A[i]*Js for i in range(3)))
  cur=[T[i]*Js for i in range(3)]+[(T[i]*A[j]-d[i]*T[j])*Js for i in range(3) for j in range(i+1,3)]
  grad=[B*T[i] for B in masses for i in range(3)]
  ck(f'connection_curvature_mass_gradient_rank12_{ix}',matrix(QQ,[v.list() for v in cur+grad]).rank()==12)
  blocks.append({'full_conservative_kernel':enc(K.basis_matrix()),'full_dimension':44,'target_image_dimension':6,'S_image_dimension':35,'repairs':repairs,'two_axis_factorized_dimension':6,'connection_defect_rank':12})
 Kwall=D[0]*masses[0];P=(I4+Kwall)/2
 ck('wall_projector_rank2',Kwall.transpose()==Kwall and Kwall*Kwall==I4 and P*P==P and P.rank()==2)
 ck('wall_tangential_invariance',all(z*P==P*z for z in D[1:]+[masses[1]]))
 ck('wall_second_mass_gap',masses[1]*masses[1]==-I4 and all(masses[1]*z+z*masses[1]==0 for z in D[1:]))
 ck('wall_normal_factorization',D[0]*Kwall==masses[0])
 return {'result_id':'K1840','status':'active_research','classification':'INTERNAL_STRUCTURAL_ONLY','target_claim':'NONE-NOT-A-KILL','results':{'full_conservative_pointwise_dimension':44,'arbitrary_static_one_coordinate_two_mass_profiles':True,'fixed_positive_energies':True,'two_coordinate_factorized_nonzero_mass':False,'normal_target_zero_modes_observed_in_L2':False,'nonzero_wall_spectral_lift':True,'second_mass_gaps_wall':True,'constant_second_mass_gives_global_L2_right_inverse':True,'source_owned':False,'general_nonlinear_class_solved':False},'blocks':blocks,'checks':checks,'inputs':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1832-k77-common-energy-form.json','lab/process/k1836-k77-differential-dirac-quotient.json']}}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');args=p.parse_args();v=produce()
 if args.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
 else:assert v==json.loads(OUT.read_text()),'certificate drift'
 print('PASS K1840',len(v['checks']),'exact algebra groups')
