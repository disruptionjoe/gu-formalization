"""Exact full grade-one plus grade-thirteen upper-core coefficient census."""
from pathlib import Path
import json,hashlib,argparse
from sage.all import QQ,matrix,identity_matrix,zero_matrix,block_matrix,block_diagonal_matrix
from k1967_paired_raw_coefficient_observation import setup,upper_column,certify
from k1836_k77_differential_dirac_quotient import enc,mat
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k2024-full-odd-connection-compatibility.json'
def produce():
 g,volume,eta,J,C,energy,DJ,Fi,Ti,apply=setup()
 I=identity_matrix(QQ,128,sparse=True);Z=zero_matrix(QQ,128,128,sparse=True)
 labels=[];cols=[];images=[]
 for k in range(14):
  for a in range(14):
   for dual in (0,1):
    col,M,_=upper_column(k,g[a]*(volume if dual else I),J,DJ,Fi,apply)
    labels.append([k,a,dual]);cols.append(col);images.append(M)
  print('built392 row',k,flush=True)
 cert=certify(cols);K=mat(cert['kernel']);print('upper rank/kernel',cert['rank'],K.nrows(),flush=True)
 assert K.ncols()==392
 B=g[7]
 for j in range(8,14):B=B*g[j]
 hs=[eta[a]*B for a in range(14)];defects=[];conserve=[];masses=[]
 for idx,row in enumerate(K):
  om=[sum((row[j]*g[a]*(volume if dual else I) for j,(kk,a,dual) in enumerate(labels) if kk==k),Z) for k in range(14)]
  W=(3*I-volume)/2
  total=[sum((g[k]*g[c]*W*om[k] for k in range(14) if om[k]),Z) for c in range(14)]
  top=[[Z if a==c else eta[a]*g[a]*(total[c]-g[a]*g[c]*W*om[a]-eta[c]*W*om[c]) for c in range(14)]+[om[a]] for a in range(14)]
  dd={}
  for a in range(14):
   for c in range(14):
    for (r,s),v in (hs[a]*top[a][c]-top[c][a].transpose()*hs[c]).dict().items():dd[(a*128+r)*1792+c*128+s]=v
  defects.append(dd);M=sum((x*m for x,m in zip(row,images)),Z);masses.append(M)
  conserve.append({r*128+s:v for (r,s),v in (energy*M+M.transpose()*energy).dict().items()})
  print('full upper defect',idx,len(dd),'conservation',len(conserve[-1]),flush=True)
 common=certify(defects)
 combined=certify([{**d,**{1792**2+k:v for k,v in c.items()}} for d,c in zip(defects,conserve)])
 joint=mat(combined['kernel']);jointparams=joint*K
 induced=[sum((x*m for x,m in zip(row,masses)),Z) for row in joint]
 return dict(result_id='K2024',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',labels=labels,upper=cert,upper_common_form=common,joint_common_form_and_energy=combined,joint_coefficients=enc(jointparams),joint_induced=[enc(m) for m in induced],broader_repair=broader_repair(),scope='All392 real grade1 and grade13 coefficients on fixed raw principal/core and fixed H, upper invariance and inherited positive energy; other grades, forms, cores and source selection unclassified.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1951-coordinated-zero-southeast-principal.json','lab/process/k1967-paired-raw-coefficient-observation.json','lab/process/k2021-common-degree-dual-operator.json','lab/process/k2022-degree-dual-dynamics-boundary.json']})
def broader_repair():
 from random import Random
 g,v,eta,js,C,P,djs,Fi,Ti,_=setup()
 I=identity_matrix(QQ,128,sparse=True);Jc=block_matrix(QQ,[[a] for a in js],sparse=True);DJ=block_matrix(QQ,[[a] for a in djs],sparse=True)
 assert all(c.transpose()==c for c in C)
 assert all(C[i]*C[j]+C[j]*C[i]==(2*I if i==j else zero_matrix(QQ,128,128)) for i in range(3) for j in range(3))
 B=g[7]
 for k in range(8,14):B=B*g[k]
 H=block_diagonal_matrix([eta[k]*B for k in range(14)]+[B],sparse=True)
 S=Jc.transpose()*H*DJ
 assert S.transpose()==-S and all(S*c==c*S for c in C) and (S*S).is_diagonal()
 freq=[-(S*S)[i,i] for i in range(128)];N=zero_matrix(QQ,128,128,sparse=True);rng=Random(20241024);terms=[]
 for step in range(512):
  i,j=sorted(rng.sample(range(128),2))
  if freq[i]!=freq[j]:continue
  X=zero_matrix(QQ,128,128,sparse=True);X[i,j]=1;X[j,i]=-1
  for c in C:X=(X-c*X*c)/2
  X=(X-S*X*S/freq[i])/2
  if not X:continue
  terms.append([i,j]);N+=X
  if len(terms)%8==0 and N.rank()==128:break
 assert N.rank()==128 and N.transpose()==-N and N*S==S*N and all(N*c+c*N==0 for c in C)
 O=zero_matrix(QQ,128,1920,sparse=True);O[:,1792:]=Fi
 assert O*Jc==I
 Y=H*DJ*N;Z=Jc.transpose()*Y;assert Z==Z.transpose()
 L=Y*O+O.transpose()*Y.transpose()-O.transpose()*Z*O;K=H*L
 assert H*K==K.transpose()*H and K*Jc==DJ*N
 inv=N.inverse();gap=1/sum(x*x for x in inv.dict().values())
 assert gap>0
 # A second completion keeps the source candidate's southeast zero.
 X=Jc[:1792,:];F=Jc[1792:,:];Y1=Y[:1792,:];Y2=Y[1792:,:]
 Ox=zero_matrix(QQ,128,1792,sparse=True);Ox[:,:128]=Ti;assert Ox*X==I
 Bs=Ox.transpose()*Y2.transpose();Z1=Y1-Bs*F;T=X.transpose()*Z1;assert T==T.transpose()
 As=Z1*Ox+Ox.transpose()*Z1.transpose()-Ox.transpose()*T*Ox
 L0=block_matrix(QQ,[[As,Bs],[Bs.transpose(),zero_matrix(QQ,128,128,sparse=True)]],sparse=True)
 K0=H*L0
 assert H*K0==K0.transpose()*H and K0*Jc==DJ*N and not K0[1792:,1792:]
 assert (K-K0)*Jc==zero_matrix(QQ,1920,128)
 tie=[];W=(3*I-v)/2
 for full in [K,K0]:
  oms=[full[128*a:128*(a+1),1792:] for a in range(14)]
  totals=[sum((g[k]*g[c]*W*oms[k] for k in range(14)),zero_matrix(QQ,128,128,sparse=True)) for c in range(14)]
  entries=0;first=None
  for a in range(14):
   for c in range(14):
    expected=zero_matrix(QQ,128,128,sparse=True) if a==c else eta[a]*g[a]*(totals[c]-g[a]*g[c]*W*oms[a]-eta[c]*W*oms[c])
    defect=full[128*a:128*(a+1),128*c:128*(c+1)]-expected
    entries+=len(defect.dict())
    if first is None and defect:
     (ii,jj),val=sorted(defect.dict().items())[0];first=[128*a+ii,128*c+jj,str(val)]
  assert entries>0;tie.append(dict(entries=entries,witness=first))
 se=K[1792:,1792:]
 return dict(S=enc(S),seed=20241024,projected_terms=terms,M=enc(N),rank=128,gap_squared_lower=str(gap),inverse_frobenius_squared=str(1/gap),raw_connection_tie_defects=tie,full_K=enc(K),zero_southeast_K=enc(K0),zero_southeast_entries=len(K0.dict()),southeast_rank=se.rank(),southeast_entries=len(se.dict()),full_entries=len(K.dict()),upper_left_entries=len(K[:1792,:1792].dict()),scope='New unrestricted zeroth-order block completion, not a common grade1/13 connection or source-selected mass. H-self-adjoint full operator with inherited positive invariant128 massive core; full carrier remains Jordan-defective.')

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();r=produce()
 if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text())
 print('PASS K2024',r['upper']['rank'],r['upper_common_form']['rank'],r['joint_common_form_and_energy']['rank'],flush=True)
