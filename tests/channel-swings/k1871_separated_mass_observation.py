#!/usr/bin/env sage-python
"""Separated-axis exact conservative repairs and their nonlinear compatibility."""
import argparse,hashlib,json
from pathlib import Path
from sage.all import QQ,matrix,vector,identity_matrix
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1871-separated-mass-observation.json'
def mat(x):return matrix(QQ,x.get('rows',16),x.get('columns',16),{(i,j):QQ(v) for i,j,v in x['entries']})
def enc(M):return {'rows':int(M.nrows()),'columns':int(M.ncols()),'entries':[[int(i),int(j),str(v)] for (i,j),v in sorted(M.dict().items())]}
def produce():
 src=json.loads((ROOT/'lab/process/k1836-k77-differential-dirac-quotient.json').read_text());eng=json.loads((ROOT/'lab/process/k1832-k77-common-energy-form.json').read_text());old=json.loads((ROOT/'lab/process/k1840-k77-conservative-variable-observation.json').read_text())
 D=list(map(mat,src['target_D']));d=[x/24 for x in D];B=[mat(v['B']) for v in old['blocks'][0]['repairs']];I=identity_matrix(QQ,4);checks={};blocks=[]
 def ck(k,v):checks[k]=bool(v);assert v,k
 for ix,(rec,en,kr) in enumerate(zip(src['blocks'],eng['blocks'],old['blocks'])):
  T=list(map(mat,rec['T']));A=list(map(mat,en['matrices']));H=mat(en['H']);Hi=H.inverse();K=mat(kr['full_conservative_kernel']);alpha=QQ(rec['alpha']);CB=[]
  for i in range(16):
   for j in range(i+1,16):CB.append(Hi*matrix(QQ,16,16,{(i,j):1,(j,i):-1}))
  proj=matrix(QQ,[list(w[120:]) for w in K.rows()]).transpose()
  ck(f'fixed_BS_freedom6_{ix}',proj.right_kernel().dimension()==6)
  for z in proj.right_kernel().basis():
   w=z*K;C=sum((w[j]*CB[j] for j in range(120)),matrix(QQ,16))
   ck(f'invisible_{ix}_{len(checks)}',all(t*C==0 for t in T))
  repairs={};data=[]
  for axis in range(3):
   for a in range(2):
    S=-24*D[axis]*B[a]*T[axis];bv=[B[a][i,j] for i in range(4) for j in range(i+1,4)]
    w=proj.solve_right(vector(QQ,bv+S.list()))*K;C=sum((w[j]*CB[j] for j in range(120)),matrix(QQ,16));repairs[axis,a]=(C,S)
    ck(f'conservation_{ix}_{axis}_{a}',H*C+C.transpose()*H==0)
    ck(f'first_order_{ix}_{axis}_{a}',all(T[i]*C-B[a]*T[i]+S*A[i]-d[i]*S==0 for i in range(3)))
    ck(f'derivative_{ix}_{axis}_{a}',T[axis]*C==d[axis]*S)
    ck(f'self_quadratic_{ix}_{axis}_{a}',S*C==B[a]*S)
    ck(f'gram_first_{ix}_{axis}_{a}',all(T[i]*Hi*S.transpose()==S*Hi*T[i].transpose() for i in range(3)))
    ck(f'gram_derivative_{ix}_{axis}_{a}',T[axis]*Hi*S.transpose()==-24*alpha*D[axis]*B[a])
    ck(f'gram_potential_{ix}_{axis}_{a}',S*Hi*S.transpose()==576*alpha*I)
    data.append({'axis':axis,'mass':a,'C':enc(C),'S':enc(S)})
  residuals=[]
  for j in range(3):
   for l in range(j+1,3):
    Rs=[]
    for a in range(2):
     for b in range(2):
      C,S=repairs[j,a];Cp,Sp=repairs[l,b];R=S*Cp+Sp*C-B[a]*Sp-B[b]*S
      ck(f'cross_{ix}_{j}_{l}_{a}_{b}',R.rank()==(4 if a==b else 0))
      if a==b:Rs.append(R)
      else:ck(f'cross_gram_{ix}_{j}_{l}_{a}_{b}',S*Hi*Sp.transpose()+Sp*Hi*S.transpose()==0)
    ck(f'dot_product_law_{ix}_{j}_{l}',Rs[0]==Rs[1])
    G=[]
    for a in range(2):
     Sa=repairs[j,a][1];Sb=repairs[l,a][1];G.append(Sa*Hi*Sb.transpose()+Sb*Hi*Sa.transpose())
    ck(f'cross_gram_dot_law_{ix}_{j}_{l}',G[0]==G[1])
    residuals.append({'axes':[j,l],'R':enc(Rs[0])})
  # Orthogonally rotated mass axes must preserve both nonlinear and Gram cancellation.
  for c,s in [(QQ(3)/5,QQ(4)/5),(QQ(5)/13,QQ(12)/13)]:
   C=c*repairs[0,0][0]+s*repairs[0,1][0];S=c*repairs[0,0][1]+s*repairs[0,1][1]
   Cp=-s*repairs[1,0][0]+c*repairs[1,1][0];Sp=-s*repairs[1,0][1]+c*repairs[1,1][1]
   Ba=c*B[0]+s*B[1];Bb=-s*B[0]+c*B[1]
   ck(f'rotated_pair_{ix}_{c}',S*Cp+Sp*C==Ba*Sp+Bb*S and S*Hi*Sp.transpose()+Sp*Hi*S.transpose()==0)
  blocks.append({'repairs':data,'cross_residuals':residuals,'fixed_BS_invisible_dimension':6})
 K1=D[0]*B[0];K2=D[1]*B[1]
 ck('commuting_wall_involutions',K1*K2==K2*K1 and K1*K1==I and K2*K2==I)
 sectors=[]
 for e1 in [-1,1]:
  for e2 in [-1,1]:
   P=(I+e1*K1)*(I+e2*K2)/4
   ck(f'line_sector_{e1}_{e2}',P*P==P and P.rank()==1 and D[2]*P==-e1*e2*P)
   sectors.append({'orientations':[e1,e2],'P':enc(P),'D3_eigenvalue':-e1*e2})
 return {'result_id':'K1871','status':'active_research','classification':'INTERNAL_STRUCTURAL_ONLY','target_claim':'NONE-NOT-A-KILL','results':{'separated_orthogonal_mass_profiles':True,'same_mass_arbitrary_separated_profiles':False,'three_nonzero_pairwise_orthogonal_masses':False,'general_44_class_solved':False,'source_owned':False,'physical_chiral_count':False,'double_wall_zero_modes_in_observation_range':False,'shift_beyond_wall_height_gaps_target':True},'blocks':blocks,'line_sectors':sectors,'line_budget':{'B':'((b+1/2)*J-1)/alpha','error_squared':'b-(b*b-b/2)*J','large_budget_alpha_B_error_squared_limit':'pi/4','B_J_b':'1','B_J_const':'1/2','B_constant':'-1','error_b':'1','error_b2J':'-1','error_bJ':'1/2'},'checks':checks,'inputs':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1832-k77-common-energy-form.json','lab/process/k1836-k77-differential-dirac-quotient.json','lab/process/k1840-k77-conservative-variable-observation.json']}}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();v=produce()
 if a.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
 else:assert v==json.loads(OUT.read_text()),'certificate drift'
 print('PASS K1871',len(v['checks']),'exact matrix groups;',len(v['inputs']),'dependency pins')
