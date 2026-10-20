#!/usr/bin/env sage-python
"""Exact polynomial Dirac observation and compatible constant coefficients."""
import argparse,hashlib,json
from pathlib import Path
from sage.all import QQ,matrix,identity_matrix,diagonal_matrix,block_matrix,block_diagonal_matrix
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1836-k77-differential-dirac-quotient.json'
def mat(x):return matrix(QQ,x.get('rows',16),x.get('columns',16),{(i,j):QQ(v) for i,j,v in x['entries']})
def enc(M):return {'rows':int(M.nrows()),'columns':int(M.ncols()),'entries':[[int(i),int(j),str(v)] for (i,j),v in sorted(M.dict().items())]}
def clifford():
 I=identity_matrix(QQ,2);X=matrix(QQ,[[0,1],[1,0]]);Z=diagonal_matrix(QQ,[1,-1]);E=matrix(QQ,[[0,1],[-1,0]])
 return [X.tensor_product(I),Z.tensor_product(I),E.tensor_product(E)]
def observation_equations(a,d,degree=1):
 rows=[];n=192 if degree else 64
 for i in range(3):
  for j in (range(i,3) if degree else [i]):
   for r in range(4):
    for c in range(16):
     row={}
     pairs=([(i,j)] if i==j else [(i,j),(j,i)]) if degree else [(0,i)]
     for k,l in pairs:
      for h in range(16):
       pos=k*64+r*16+h;row[pos]=row.get(pos,0)+a[l][h,c]
      for h in range(4):
       pos=k*64+h*16+c;row[pos]=row.get(pos,0)-d[l][r,h]/24
     rows.append(row)
 return matrix(QQ,len(rows),n,{(r,c):v for r,row in enumerate(rows) for c,v in row.items()},sparse=True)
def coefficient_space(T,H,skew=False):
 # Unknown C16x16 followed by B4x4; T_i C = B T_i.
 rows=[]
 for M in T:
  for r in range(4):
   for c in range(16):
    row={h*16+c:M[r,h] for h in range(16)}
    for h in range(4):row[256+r*4+h]=-M[h,c]
    rows.append(row)
 if skew:
  for r in range(16):
   for c in range(r,16):
    row={}
    for h in range(16):
     for pos,val in [(h*16+c,H[r,h]),(h*16+r,H[h,c])]:row[pos]=row.get(pos,0)+val
    rows.append(row)
 E=matrix(QQ,len(rows),272,{(r,c):v for r,row in enumerate(rows) for c,v in row.items()},sparse=True)
 return E.right_kernel()
def produce():
 src=json.loads((ROOT/'lab/process/k1832-k77-common-energy-form.json').read_text());d=clifford();checks={};records=[]
 def ck(k,v):checks[k]=bool(v);assert v,k
 ck('target_Clifford',all(d[i]*d[j]+d[j]*d[i]==(2*identity_matrix(QQ,4) if i==j else matrix(QQ,4,4)) for i in range(3) for j in range(3)))
 for ix,blk in enumerate(src['blocks']):
  a=list(map(mat,blk['matrices']));H=mat(blk['H']);Hi=H.inverse();ker=observation_equations(a,d).right_kernel();ck(f'degree1_dimension2_{ix}',ker.dimension()==2)
  ck(f'constant_dimension0_{ix}',observation_equations(a,d,0).right_nullity()==0)
  basis=[[matrix(QQ,4,16,w[i*64:(i+1)*64]) for i in range(3)] for w in ker.basis()];T=basis[0];gram=T[0]*Hi*T[0].transpose();alpha=gram[0,0]
  ck(f'positive_scalar_Gram_{ix}',alpha>0 and all(M*Hi*M.transpose()==alpha*identity_matrix(QQ,4) for M in T))
  ck(f'zero_cross_Gram_{ix}',all(T[i]*Hi*T[j].transpose()+T[j]*Hi*T[i].transpose()==0 for i in range(3) for j in range(i+1,3)))
  Q=[Hi*M.transpose()/alpha for M in T];I=identity_matrix(QQ,16)
  ck(f'lift_axis_{ix}',all(Q[i]*T[i]==576*(I-a[i]*a[i])/575 for i in range(3)))
  ck(f'lift_cross_{ix}',all(Q[i]*T[j]+Q[j]*T[i]==-576*(a[i]*a[j]+a[j]*a[i])/575 for i in range(3) for j in range(i+1,3)))
  ck(f'intertwine_axis_{ix}',all(T[i]*a[i]==d[i]*T[i]/24 and a[i]*Q[i]==Q[i]*d[i]/24 for i in range(3)))
  ck(f'intertwine_cross_{ix}',all(T[i]*a[j]+T[j]*a[i]==(d[i]*T[j]+d[j]*T[i])/24 and a[i]*Q[j]+a[j]*Q[i]==(Q[i]*d[j]+Q[j]*d[i])/24 for i in range(3) for j in range(i+1,3)))
  W=block_matrix([[M] for M in T]);ck(f'stacked_rank12_{ix}',W.rank()==12)
  cspace=coefficient_space(T,H);sk=coefficient_space(T,H,True)
  ck(f'local_coefficient_dimension80_{ix}',cspace.dimension()==80)
  bd=matrix(QQ,[w[256:] for w in cspace.basis()]).rank();skbd=matrix(QQ,[w[256:] for w in sk.basis()]).rank()
  ck(f'all_target_B_available_{ix}',bd==16)
  J=d[0]*d[1]*d[2];ck(f'target_complex_structure_{ix}',J*J==-identity_matrix(QQ,4) and J.transpose()==-J and all(J*M==M*J for M in d))
  # The second solution is the complex multiple of the first, with a rational scale.
  V=matrix(QQ,[sum([M.list() for M in T],[]),sum([(J*M).list() for M in T],[])])
  ck(f'all_nonzero_solutions_complex_multiples_{ix}',V.rank()==2 and V.row_space()==ker)
  ck(f'energy_skew_dimension9_target3_{ix}',sk.dimension()==9 and skbd==3)
  Bs=matrix(QQ,[w[256:] for w in sk.basis()]);bb=[matrix(QQ,4,4,w) for w in Bs.row_space().basis()]
  mass=[B for B in bb if all(B*M+M*B==0 for M in d)]
  central=[B for B in bb if all(B*M==M*B for M in d)]
  ck(f'two_mass_one_central_{ix}',len(mass)==2 and len(central)==1)
  ck(f'quaternion_skew_generators_{ix}',all(B*B==-identity_matrix(QQ,4) for B in bb) and all(bb[i]*bb[j]+bb[j]*bb[i]==0 for i in range(3) for j in range(i+1,3)))
  masspairs=[]
  for B in mass:
   weights=Bs.transpose().solve_right(matrix(QQ,16,1,B.list()).column(0))
   w=sum((weights[j]*sk.basis()[j] for j in range(len(weights))),sk.zero())
   C=matrix(QQ,16,16,w[:256]);ck(f'mass_lift_{ix}_{len(masspairs)}',C.transpose()*H+H*C==0 and all(t*C==B*t for t in T))
   masspairs.append({'C':enc(C),'B':enc(B)})
  records.append({'T':[enc(M) for M in T],'Q':[enc(M) for M in Q],'alpha':str(alpha),'degree1_basis':[[enc(M) for M in x] for x in basis],'mass_lifts':masspairs,'local_C_B_dimension':int(cspace.dimension()),'energy_skew_C_B_dimension':int(sk.dimension()),'energy_skew_target_B_dimension':int(skbd),'energy_skew_basis':[{'C':enc(matrix(QQ,16,16,w[:256])),'B':enc(matrix(QQ,4,4,w[256:]))} for w in sk.basis()]})
 return {'result_id':'K1836','status':'active_research','classification':'INTERNAL_STRUCTURAL_ONLY','target_claim':'NONE-NOT-A-KILL','results':{'slow_Dirac_local_differential_observation':True,'constant_observation_exists':False,'source_owned':False,'inverse_local':False,'per_module_degree1_dimension':2,'full_slow_target_real_dimension':128},'target_D':[enc(M) for M in d],'blocks':records,'checks':checks,'inputs':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1832-k77-common-energy-form.json','lab/process/k1824-k77-joint-observed-symbol-algebra.json']}}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');args=p.parse_args();v=produce()
 if args.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
 else:assert v==json.loads(OUT.read_text()),'certificate drift'
 print('PASS K1836',len(v['checks']),'exact groups',[(b['energy_skew_C_B_dimension'],b['energy_skew_target_B_dimension']) for b in v['blocks']])
