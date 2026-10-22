"""Exact full-direction bivector leakage, split by disjoint scalar-entry supports."""
import argparse,hashlib,json
from pathlib import Path
from sage.all import QQ,GF,matrix,identity_matrix,zero_matrix,block_matrix,prod
from k1953_spin_connection_stable_mass import setup
from k1951_coordinated_zero_southeast_principal import raw
from k1836_k77_differential_dirac_quotient import enc,mat
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1959-full-direction-even-connection.json'

def assemble():
 g,As,J,L,C,H=setup();_,_,_,D=raw();I=identity_matrix(QQ,128,sparse=True);Z=zero_matrix(QQ,128,128,sparse=True);eta=[1]*7+[-1]*7;om=prod(g);Wi=(I+om)/2+(I-om)/4
 parts=[[Z]*15 for _ in range(15)];parts[0][14]=-I;parts[14][0]=I
 for r in range(1,14):
  for c in range(1,14):parts[r][c]=Wi*eta[r]*g[r]*g[0]*g[c]*(QQ(1)/12-(r==c))
 Di=block_matrix(parts,sparse=True);assert Di*D(0)==identity_matrix(QQ,1920)
 cols=[];labels=[];outs=[]
 for k in range(14):
  A=Di*D(k)
  for a in range(14):
   for b in range(a+1,14):
    V=A*identity_matrix(QQ,15,sparse=True).tensor_product(g[a]*g[b])*J;M=L*V
    cols.append({128*i+j:v for (i,j),v in (V-J*M).dict().items()});outs.append(M);labels.append([k,a,b])
  print('assembled covector',k,flush=True)
 return cols,labels,outs,C,H

def certify(cols,labels,outs,C,H):
 parent=list(range(len(cols)))
 def find(x):
  while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
  return x
 owner={}
 for j,c in enumerate(cols):
  for row in c:
   if row in owner:parent[find(j)]=find(owner[row])
   else:owner[row]=j
 groups={}
 for j in range(len(cols)):groups.setdefault(find(j),[]).append(j)
 cert=[];kernels=[];totalrank=0
 for ids in groups.values():
  keys=sorted(set().union(*(set(cols[j]) for j in ids)))
  T=matrix(QQ,[[cols[j].get(k,0) for j in ids] for k in keys])
  if not keys:T=matrix(QQ,0,len(ids))
  piv=list(T.change_ring(GF(101)).transpose().pivots());B=T.matrix_from_rows(piv);K=B.right_kernel().basis_matrix()
  assert T*K.transpose()==0 and K.rank()+len(piv)==len(ids),'exact kernel upper bound'
  pc=list(B.pivots());inv=B.matrix_from_columns(pc).inverse();assert inv*B.matrix_from_columns(pc)==identity_matrix(QQ,len(piv))
  totalrank+=len(piv)
  for row in K:
   x=[QQ(0)]*len(cols)
   for j,v in zip(ids,row):x[j]=v
   kernels.append(x)
  cert.append(dict(columns=ids,rows=[keys[i] for i in piv],pivot_columns=pc,inverse=enc(inv),kernel=enc(K)))
  print('block',len(ids),'rank',len(piv),flush=True)
 K=matrix(QQ,kernels) if kernels else matrix(QQ,0,len(cols))
 images=[sum((x*M for x,M in zip(row,outs)),zero_matrix(QQ,128,128)) for row in K]
 F=matrix(QQ,[sum([(M*c+c*M).list() for c in C],[])+(H*M+M.transpose()*H).list() for M in images]).transpose() if images else matrix(QQ,65536,0)
 MK=F.right_kernel().basis_matrix();mi=[sum((x*M for x,M in zip(row,images)),zero_matrix(QQ,128,128)) for row in MK]
 return dict(rank=totalrank,blocks=cert,kernel=enc(K),induced_rank=matrix(QQ,[M.list() for M in images]).rank() if images else 0,mass_kernel=enc(MK),mass_image_rank=matrix(QQ,[M.list() for M in mi]).rank() if mi else 0)

def produce():
 cols,labels,outs,C,H=assemble();r=certify(cols,labels,outs,C,H)
 r.update(result_id='K1959',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',labels=labels,parameter_count=len(cols),inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1951-coordinated-zero-southeast-principal.json','lab/process/k1957-full-direction-grade-one.json']})
 return r

def tensor_produce():
 """Changed connection placement: common spinor plus covector-slot action."""
 g,As,J,L,C,H=setup();L=matrix(QQ,L,sparse=True);_,_,_,D=raw();I=identity_matrix(QQ,128,sparse=True);Z=zero_matrix(QQ,128,128,sparse=True);eta=[1]*7+[-1]*7;om=prod(g);Wi=(I+om)/2+(I-om)/4
 parts=[[Z]*15 for _ in range(15)];parts[0][14]=-I;parts[14][0]=I
 for r in range(1,14):
  for c in range(1,14):parts[r][c]=Wi*eta[r]*g[r]*g[0]*g[c]*(QQ(1)/12-(r==c))
 Di=block_matrix(parts,sparse=True);cols=[];outs=[];labels=[];I15=identity_matrix(QQ,15,sparse=True)
 for k in range(14):
  A=Di*D(k);LA=L*A;R=A-J*LA
  for a in range(14):
   for b in range(a+1,14):
    JJ=I15.tensor_product(g[a]*g[b])*J
    JJ[128*a:128*(a+1),:]+=2*eta[a]*J[128*b:128*(b+1),:]
    JJ[128*b:128*(b+1),:]-=2*eta[b]*J[128*a:128*(a+1),:]
    leak=R*JJ;M=LA*JJ
    cols.append({128*i+j:v for (i,j),v in leak.dict().items()});outs.append(M);labels.append([k,a,b])
  print('tensorial covector',k,flush=True)
 r=certify(cols,labels,outs,C,H)
 # A concrete surviving nonmass rotation is checked on the actual matrices.
 j=labels.index([0,1,2]);M=outs[j]
 assert not cols[j] and M*M==-I and H*M+M.transpose()*H==0 and all(M*c==c*M for c in C),'tensorial temporal rotation'
 r['rotation_label']=[0,1,2];r['rotation_matrix']=enc(M)
 return r

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');p.add_argument('--part',choices=['spinor','tensor','all'],default='all');a=p.parse_args()
 saved=json.loads(OUT.read_text()) if OUT.exists() else {}
 r=produce() if a.part in ['spinor','all'] else {k:v for k,v in saved.items() if k!='tensorial'}
 if a.part in ['tensor','all']:r['tensorial']=tensor_produce()
 elif 'tensorial' in saved:r['tensorial']=saved['tensorial']
 if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==saved,'report mismatch'
 print('PASS K1959', {k:r[k] for k in ['rank','parameter_count','induced_rank','mass_image_rank']}, 'tensor', {k:r.get('tensorial',{}).get(k) for k in ['rank','induced_rank','mass_image_rank']},flush=True)
