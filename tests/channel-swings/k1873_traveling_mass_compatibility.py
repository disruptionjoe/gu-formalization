#!/usr/bin/env sage-python
"""Polynomial dual certificates for every nonzero traveling speed."""
import argparse,hashlib,json
from pathlib import Path
from sage.all import QQ,PolynomialRing,matrix,vector,lcm
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1873-traveling-mass-compatibility.json'
def mat(x):return matrix(QQ,x.get('rows',16),x.get('columns',16),{(i,j):QQ(v) for i,j,v in x['entries']})
def encvec(v):return [str(x) for x in v]
def produce():
 s=json.loads((ROOT/'lab/process/k1836-k77-differential-dirac-quotient.json').read_text());e=json.loads((ROOT/'lab/process/k1832-k77-common-energy-form.json').read_text());old=json.loads((ROOT/'lab/process/k1840-k77-conservative-variable-observation.json').read_text());D=list(map(mat,s['target_D']));d=[x/24 for x in D];Bs=[mat(q['B']) for q in old['blocks'][0]['repairs']];R=PolynomialRing(QQ,'v');v=R.gen();F=R.fraction_field();blocks=[];checks={}
 def ck(k,x):checks[k]=bool(x);assert x,k
 for ix,(sr,er,kr) in enumerate(zip(s['blocks'],e['blocks'],old['blocks'])):
  T=list(map(mat,sr['T']));A=list(map(mat,er['matrices']));H=mat(er['H']);Hi=H.inverse();K=mat(kr['full_conservative_kernel']);CB=[Hi*matrix(QQ,16,16,{(i,j):1,(j,i):-1}) for i in range(16) for j in range(i+1,16)];Cs=[];Ss=[]
  for j,w in enumerate(K.rows()):
   C=sum((w[t]*CB[t] for t in range(120)),matrix(QQ,16));S=matrix(QQ,4,16,list(w[126:]));B=matrix(QQ,4);z=0
   for a in range(4):
    for b in range(a+1,4):B[a,b]=w[120+z];B[b,a]=-w[120+z];z+=1
   ck(f'bank_first_order_{ix}_{j}',all(T[i]*C-B*T[i]+S*A[i]-d[i]*S==0 for i in range(3)) and H*C+C.transpose()*H==0)
   Cs.append(C);Ss.append(S)
  M=matrix(F,[list(w[120:126])+list((T[0]*C-d[0]*S+v*S).list()) for w,C,S in zip(K.rows(),Cs,Ss)]).transpose()
  rhs=matrix(F,[[B[i,j] for i in range(4) for j in range(i+1,4)]+[0]*64 for B in Bs]).transpose();N=M.transpose().right_kernel().basis_matrix();Nr=matrix(F,list(reversed(M.rows()))).transpose().right_kernel().basis_matrix();N=N.stack(matrix(F,[list(reversed(row)) for row in Nr.rows()]));V=N*rhs;witnesses=[]
  ck(f'generic_mass_obstruction_rank_{ix}',V.rank()==2)
  for a in range(2):
   target=vector(F,[int(i==a) for i in range(2)])
   candidates=[row for row in N.rows() if (row*rhs)[1-a]==0 and (row*rhs)[a]!=0]
   w=vector(R,[0]*70);den=R(0)
   for row in candidates:
    mult=lcm([x.denominator() for x in row]);wr=vector(R,[R(x*mult) for x in row]);qr=R((row*rhs)[a]*mult)
    g,c1,c2=den.xgcd(qr);w=c1*w+c2*wr;den=g
    if all(p.monic() in [v,v-1,v+1] for p,n in den.factor()):break
   ck(f'generic_annihilator_{ix}_{a}',den!=0 and w*M==0 and w*rhs==den*target)
   factors=[[str(p.monic()),int(n)] for p,n in den.factor()]
   ck(f'only_exceptional_speeds_{ix}_{a}',all(p.monic() in [v,v-1,v+1] for p,n in den.factor()))
   witnesses.append({'mass':a,'polynomial_coefficients':[[str(c) for c in x.list()] for x in w],'rhs_polynomial':[str(c) for c in den.list()],'factors':factors})
  special=[]
  for speed in [-1,1]:
   Mv=matrix(QQ,[[x(v=speed) for x in row] for row in M.rows()]);Nv=Mv.transpose().right_kernel().basis_matrix();Rv=matrix(QQ,rhs);Vv=Nv*Rv;ck(f'exception_mass_rank_{ix}_{speed}',Vv.rank()==2)
   for a in range(2):
    target=vector(QQ,[int(i==a) for i in range(2)]);lam=Vv.transpose().solve_right(target)*Nv;ck(f'exception_annihilator_{ix}_{speed}_{a}',lam*Mv==0 and lam*Rv==target);special.append({'speed':speed,'mass':a,'witness':encvec(lam)})
  # The obstruction is not a blanket no-mass statement: static repairs solve both levels.
  for a,rep in enumerate(kr['repairs']):
   C=mat(rep['C']);S=mat(rep['S']);ck(f'static_positive_{ix}_{a}',T[0]*C==d[0]*S and S*C==Bs[a]*S)
  blocks.append({'generic':witnesses,'exceptional':special,'generic_rank':int(M.rank())});print('block',ix,'certified',flush=True)
 return {'result_id':'K1873','status':'active_research','classification':'INTERNAL_STRUCTURAL_ONLY','target_claim':'NONE-NOT-A-KILL','scope':{'coordinate_axis':0,'fixed_principal_symbols':True,'fixed_positive_pairings':True,'constant_triple_times_arbitrary_profile':True,'nonzero_speed_mass_plane_solution':False,'constant_mass_allowed':True,'all_variable_coefficient_solutions_excluded':False,'source_GU_verdict':False},'blocks':blocks,'checks':checks,'inputs':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1832-k77-common-energy-form.json','lab/process/k1836-k77-differential-dirac-quotient.json','lab/process/k1840-k77-conservative-variable-observation.json']}}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();z=produce()
 if a.write:OUT.write_text(json.dumps(z,indent=2)+'\n')
 else:assert z==json.loads(OUT.read_text()),'certificate drift'
 print('PASS K1873',len(z['checks']),'exact matrix/polynomial groups;',len(z['inputs']),'pins')
