"""Full fourteen-direction grade-one connection on the fixed K1951 raw core."""
import argparse,json,hashlib
from pathlib import Path
from sage.all import QQ,GF,matrix,identity_matrix,zero_matrix,block_matrix,prod
from k1953_spin_connection_stable_mass import setup
from k1951_coordinated_zero_southeast_principal import raw
from k1836_k77_differential_dirac_quotient import enc,mat
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1957-full-direction-grade-one.json'

def assemble():
 g,As,J,L,C,H=setup();_,_,_,D=raw();I=identity_matrix(QQ,128,sparse=True);Z=zero_matrix(QQ,128,128,sparse=True);eta=[1]*7+[-1]*7;omega=prod(g);Wi=(I+omega)/2+(I-omega)/4
 blocks=[[Z]*15 for _ in range(15)];blocks[0][14]=-I;blocks[14][0]=I
 for r in range(1,14):
  for c in range(1,14):blocks[r][c]=Wi*eta[r]*g[r]*g[0]*g[c]*(QQ(1)/12-(r==c))
 Di=block_matrix(QQ,blocks,sparse=True);assert Di*D(0)==identity_matrix(QQ,1920,sparse=True),'time inverse'
 cols=[];outs=[]
 for k in range(14):
  A=Di*D(k)
  for a in range(14):
   V=A*identity_matrix(QQ,15,sparse=True).tensor_product(g[a])*J;M=L*V
   cols.append({128*i+j:v for (i,j),v in (V-J*M).dict().items()});outs.append(M)
  print('assembled direction',k,flush=True)
 keys=sorted(set().union(*(set(c) for c in cols)));idx={k:i for i,k in enumerate(keys)}
 T=matrix(QQ,len(keys),196,{(idx[k],j):v for j,col in enumerate(cols) for k,v in col.items()},sparse=True)
 return T,keys,outs,C,H,J,D(0)

def produce():
 T,keys,outs,C,H,J,D0=assemble();piv=list(T.change_ring(GF(101)).transpose().pivots());B=T.matrix_from_rows(piv);K=B.right_kernel().basis_matrix()
 assert T*K.transpose()==0,'full exact leakage kernel';assert K.rank()+B.rank()==196,'complete exact rank'
 images=[sum((x*o for x,o in zip(row,outs)),zero_matrix(QQ,128,128,sparse=True)) for row in K.rows()]
 O=matrix(QQ,[M.list() for M in images]).transpose() if images else matrix(QQ,16384,0)
 F=matrix(QQ,[sum([(M*c+c*M).list() for c in C],[])+(H*M+M.transpose()*H).list() for M in images]).transpose() if images else matrix(QQ,65536,0)
 mass=F.right_kernel().basis_matrix();massimgs=[sum((x*M for x,M in zip(row,images)),zero_matrix(QQ,128,128,sparse=True)) for row in mass.rows()]
 imrank=matrix(QQ,[M.list() for M in massimgs]).rank() if massimgs else 0
 cols=list(B.pivots());minor=B.matrix_from_columns(cols);inv=minor.inverse();assert inv*minor==identity_matrix(QQ,len(piv))
 aux=(D0*J).matrix_from_rows(list(range(1792,1920)));auxinv=aux.inverse();assert auxinv*aux==identity_matrix(QQ,128),'full14 auxiliary range complements core'
 norm=max(sum(abs(x) for x in row) for row in inv.rows())
 return dict(auxiliary_complement_inverse=enc(auxinv),arbitrary_auxiliary_parameter_count=14*128*128,inverse_infinity_norm=str(norm),result_id='K1957',rank=len(piv),parameter_count=196,kernel=enc(K),selected_rows=[keys[i] for i in piv],selected_columns=cols,inverse=enc(inv),induced_image_rank=O.rank(),mass_parameter_kernel=enc(mass),mass_image_rank=imrank,inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1951-coordinated-zero-southeast-principal.json','lab/process/k1955-grade-one-connection.json']})
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();r=produce()
 if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text()),'report identity'
 print('PASS', {k:r[k] for k in ['rank','parameter_count','induced_image_rank','mass_image_rank']},flush=True)
