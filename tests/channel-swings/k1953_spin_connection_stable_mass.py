"""Fixed-background minimal Spin connection versus the K1951 stable mass."""
import sys,json,hashlib,argparse
from pathlib import Path
from sage.all import QQ,matrix,identity_matrix,zero_matrix,block_matrix,GF
from k1951_coordinated_zero_southeast_principal import raw,left
from k1836_k77_differential_dirac_quotient import enc,mat
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k1953-spin-connection-stable-mass.json'
INPUT='lab/process/k1951-coordinated-zero-southeast-principal.json'

def setup():
 rows=json.loads((ROOT/INPUT).read_text())['blocks'];g,As,comps,D=raw();J=matrix(QQ,1920,128,sparse=True)
 for k,r in enumerate(rows):
  js=mat(r['basis'])*mat(r['section'])
  for (i,j),v in js.dict().items():J[r['coordinates'][i],4*k+j]=v
 L=left(J);Cs=[L*A*J for A in As]
 H=block_matrix([[mat(r['quotient_energy']) if k==l else zero_matrix(QQ,4,4) for l in range(32)] for k,r in enumerate(rows)],sparse=True)
 assert L*J==identity_matrix(QQ,128)
 assert all(A*J==J*C and H*C==C.transpose()*H for A,C in zip(As,Cs))
 return g,As,J,L,Cs,H

def constraints(tensorial=False):
 g,As,J,L,Cs,H=setup();cols=[];outs=[];labels=[]
 for k,A in zip([0,7,8,9],[identity_matrix(QQ,1920,sparse=True)]+As):
  for a in range(14):
   for b in range(a+1,14):
    JJ=identity_matrix(QQ,15,sparse=True).tensor_product(g[a]*g[b])*J
    if tensorial:
     eta=[1]*7+[-1]*7
     JJ[128*a:128*(a+1),:]+=2*eta[a]*J[128*b:128*(b+1),:]
     JJ[128*b:128*(b+1),:]-=2*eta[b]*J[128*a:128*(a+1),:]
    V=A*JJ;M=L*V;leak=V-J*M
    vec={i*128+j:v for (i,j),v in leak.dict().items()};off=1920*128
    for c in Cs:
     for (i,j),v in (M*c+c*M).dict().items():vec[off+i*128+j]=v
     off+=128*128
    for (i,j),v in (H*M+M.transpose()*H).dict().items():vec[off+i*128+j]=v
    cols.append(vec);outs.append(M);labels.append([k,a,b])
 keys=sorted(set().union(*(set(x) for x in cols)));inds={v:i for i,v in enumerate(keys)}
 T=matrix(QQ,len(keys),len(cols),{(inds[i],j):v for j,x in enumerate(cols) for i,v in x.items()},sparse=True)
 return T,keys,labels,outs

def tensor_certificate(prior=None):
 T,keys,labels,outs=constraints(True)
 if prior:
  ker=mat(prior['kernel']);rows=[keys.index(k) for k in prior['selected_rows']];cols=prior['selected_columns'];inv=mat(prior['inverse'])
 else:
  ker=T.right_kernel().basis_matrix();free=set(ker.pivots());cols=[i for i in range(364) if i not in free]
  rows=list(T.matrix_from_columns(cols).change_ring(GF(101)).transpose().pivots())
  inv=T.matrix_from_rows_and_columns(rows,cols).inverse()
 assert ker.nrows()==5 and ker.rank()==5 and T*ker.transpose()==0,'complete tensor nullspace upper bound'
 assert len(rows)==len(cols)==359 and inv*T.matrix_from_rows_and_columns(rows,cols)==identity_matrix(QQ,359),'complete tensor rank lower bound'
 images=[sum((v[i]*outs[i] for i in range(364)),zero_matrix(QQ,128,128)) for v in ker.rows()]
 assert all(M==0 for M in images),'every tensor mass solution has zero reduced coefficient'
 # A temporal internal rotation survives: absence of a Dirac mass is not absence of dynamics.
 j=labels.index([0,1,2]);M=outs[j];g,As,J,L,C,H=setup()
 assert all(T[i,j]==0 for i,k in enumerate(keys) if k<1920*128),'rotation preserves stable subspace'
 assert H*M+M.transpose()*H==0 and M*M==-identity_matrix(QQ,128) and all(M*c==c*M for c in C),'conservative internal rotation, not Dirac mass'
 return dict(rank=359,kernel=enc(ker),selected_rows=[keys[i] for i in rows],selected_columns=cols,inverse=enc(inv),mass_image_dimension=0,nonmass_witness=dict(label=[0,1,2],matrix=enc(M)))

def produce():
 T,keys,labels,outs=constraints();cut=1920*128;skew=cut+3*128*128
 leak=T.matrix_from_rows([i for i,k in enumerate(keys) if k<cut]);anti=T.matrix_from_rows([i for i,k in enumerate(keys) if k<skew]);conserve=T.matrix_from_rows([i for i,k in enumerate(keys) if k<cut or k>=skew])
 # A nonsingular leakage minor proves the stronger invariant-subspace exclusion;
 # mass/energy equations are unnecessary once this holds.
 if OUT.exists():
  prior=json.loads(OUT.read_text());piv=[keys.index(k) for k in prior['selected_rows']];minor=leak.matrix_from_rows(piv);inv=mat(prior['inverse'])
 else:
  piv=leak.transpose().pivots();minor=leak.matrix_from_rows(piv);inv=minor.inverse()
 assert len(piv)==364 and inv*minor==identity_matrix(QQ,364),'exact leakage inverse certificate'
 ranks={name:364 for name in ['leakage','leakage_and_anticommutation','leakage_and_energy','all']}
 bound=max(sum(abs(v) for v in row) for row in inv.rows())
 repairs=[dict(class_name=name,parameter_dimension=0,image_dimension=0,kernel=enc(matrix(QQ,0,364)),examples=[]) for name in ['invariant','conservative_invariant']]
 return dict(tensorial=tensor_certificate(json.loads(OUT.read_text()).get('tensorial') if OUT.exists() else None),result_id='K1953',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',labels=labels,ranks=ranks,selected_rows=[keys[i] for i in piv],inverse=enc(inv),inverse_infinity_norm=str(bound),repairs=repairs,inputs={INPUT:hashlib.sha256((ROOT/INPUT).read_bytes()).hexdigest()},scope='Conditional fixed K1951 principal system; common Spin(7,7) connection on spinor slots in four observed directions. No nonzero coefficient in this 364-parameter class preserves the fixed stable subspace, even without energy or mass constraints. No full source/barred-map or physical GU exclusion.')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();v=produce()
 if a.write:OUT.write_text(json.dumps(v,indent=2)+'\n')
 else:assert v==json.loads(OUT.read_text()),'report drift'
 print('PASS K1953 exact ranks',v['ranks'],'repairs',[(r['class_name'],r['parameter_dimension'],r['image_dimension']) for r in v['repairs']],'inverse bound',v['inverse_infinity_norm'])
