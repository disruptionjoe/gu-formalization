"""Complete real raw coefficient obstruction by Clifford sectors and exact minors."""
import numpy as np
import json,time,argparse,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/"lab/process/k2028-all-grade-raw-common-form.json"
from sage.all import QQ,matrix,GF,identity_matrix
from k1967_paired_raw_coefficient_observation import setup
from k1836_k77_differential_dirac_quotient import enc
def produce(imaginary=False):
 start=time.time();g,v,eta,js,C,P,djs,Fi,Ti,_=setup();n=128;idx=np.arange(n)
 def mono(M,scale=1):
  d=M.dict();fs={int(i)^int(j) for i,j in d};assert len(fs)==1
  f=fs.pop();a=np.array([int(M[i,i^f]*scale) for i in range(n)],dtype=np.int64)
  assert all(QQ(int(a[i]))==M[i,i^f]*scale for i in range(n));return f,a
 def mul(A,B):return A[0]^B[0],A[1]*B[1][idx^A[0]]
 def trans(A):return A[0],A[1][idx^A[0]]
 def add(As):
  f=As[0][0];assert all(A[0]==f for A in As);return f,sum((A[1] for A in As),np.zeros(n,dtype=np.int64))
 gs=list(map(mono,g));vs=mono(v);assert vs[0]==0
 J=[mono(a*Fi,44) for a in js];DJ=[mono(a*Fi,44) for a in djs];B=mono(g[7]*g[8]*g[9]*g[10]*g[11]*g[12]*g[13]);ws=3+vs[1]
 G=[(0,np.ones(n,dtype=np.int64))]
 for m in range(1,1<<14):
  k=m.bit_length()-1;G.append(mul(G[m^(1<<k)],gs[k]))
 ys={}
 for r in range(15):
  sign=(-1)**(r*(r+1)//2);rows=[[int(k not in (a,c)) for k in range(14)] for a in range(14) for c in range(a+1,14) if sign*(-1)**(int(a<r)+int(c<r))==(1 if imaginary else -1)]
  T=matrix(QQ,rows,ncols=14);K=T.right_kernel().basis_matrix();ys[r]=[[int(x*row.denominator()) for x in row] for row in K]
 groups={};labels=[]
 for m,X in enumerate(G):
  bits=[i for i in range(14) if m>>i&1];other=[i for i in range(14) if not m>>i&1];perm=bits+other
  for y0 in ys[len(bits)]:
   y=[0]*14
   for i,k in enumerate(perm):y[k]=y0[i]
   A=[(z[0],eta[k]*y[k]*z[1]) for k in range(14) for z in [mul(gs[k],X)]]
   Om=[(a[0],ws*a[1]) for a in A] # 4 times Omega
   T=[add([mul(mul(gs[c],A[k]),J[c]) for c in range(14)]) for k in range(14)]
   outs=[]
   for a in range(14):
    terms=[]
    for k in range(14):
     if k==a:continue
     U=T[k][1]-mul(mul(gs[a],A[k]),J[a])[1]-mul(mul(gs[k],A[k]),J[k])[1]
     terms.append(mul(gs[k],(T[k][0],U)))
    z=mul(gs[a],add(terms));om=Om[a]
    assert z[0]==om[0]
    outs.append((z[0],4*eta[a]*z[1]+44*om[1])) # 176 times upper KJ
   M=outs[0];defect=[]
   for a in range(14):
    dm=mul(DJ[a],M);assert outs[a][0]==dm[0];defect.extend((44*outs[a][1]-dm[1]).tolist())
   mt=trans(M);assert mt[0]==M[0];defect.extend((M[1]+(-1 if imaginary else 1)*mt[1]).tolist())
   # Full H-adjoint bottom is eta_c B Omega_c^T B. Both sides denominator7744.
   low=add([mul(mul(mul(B,trans(Om[c])),B),J[c]) for c in range(14) if eta[c]==1]+[(z[0],-z[1]) for c in range(14) if eta[c]==-1 for z in [mul(mul(mul(B,trans(Om[c])),B),J[c])]])
   dm=mul(DJ[14],M);assert low[0]==dm[0];lower=((-1 if imaginary else 1)*44*low[1]-dm[1]).tolist()
   groups.setdefault(M[0],[]).append((m,y,defect,lower,M[1].tolist()))
  if m%2048==0:print('columns',m,'seconds',round(time.time()-start,1),flush=True)
 print('built',sum(map(len,groups.values())),len(groups),flush=True)
 res=[]
 for f,cs in sorted(groups.items()):
  T=matrix(QQ,[c[2] for c in cs]).transpose();pivs=list(T.change_ring(GF(101)).transpose().pivots());small=T.matrix_from_rows(pivs);K=small.right_kernel().basis_matrix();assert T*K.transpose()==0 and len(pivs)+K.nrows()==len(cs)
  L=matrix(QQ,[c[3] for c in cs]).transpose();LK=(L*K.transpose());K2=LK.right_kernel().basis_matrix()*K
  U=T[:-128,:];uk=U.right_kernel().basis_matrix();urank=U.ncols()-uk.nrows()
  print('group',f,len(cs),'upper',uk.nrows(),'joint',K.nrows(),flush=True)
  fullupper=(L*uk.transpose()).right_kernel().basis_matrix()*uk;fullupperdim=fullupper.nrows()
  pc=list(small.pivots());minor=small.matrix_from_columns(pc);assert minor.nrows()==minor.ncols();det=int(minor.change_ring(GF(101)).determinant());assert det
  res.append(dict(flip=f,labels=[[c[0],c[1]] for c in cs],rank=len(pivs),upper_rank=urank,upper_kernel=enc(uk),full_upper_dimension=fullupperdim,pivots=pivs,pivot_columns=pc,minor_det_mod101=det,kernel=enc(K),full_kernel=enc(K2),mass_rank=(matrix(QQ,[c[4] for c in cs]).transpose()*K2.transpose()).rank()))
 if imaginary:
  from k1836_k77_differential_dirac_quotient import mat
  bases=[];coordinates=[];Id=identity_matrix(QQ,128,sparse=True)
  target=matrix(QQ,[a.list() for a in [Id]+C]).transpose()
  for rec in res:
   f=rec['flip'];cs=groups[f]
   for row in mat(rec['full_kernel']):
    vals=[sum(coef*QQ(cs[j][4][i])/176 for j,coef in enumerate(row)) for i in range(128)]
    M0=matrix(QQ,128,128,{(i,i^f):v for i,v in enumerate(vals) if v},sparse=True)
    M=Fi*M0*js[14];assert P*M==M.transpose()*P
    coord=target.solve_right(matrix(QQ,1,128**2,M.list()).transpose().column(0));assert target*coord==matrix(QQ,1,128**2,M.list()).transpose().column(0)
    bases.append(enc(M));coordinates.append(list(map(str,coord)))
  assert len(bases)==13 and matrix(QQ,coordinates).rank()==4
  return dict(common_form_dimension=sum(len(x['labels']) for x in res),grade_kernels={str(r):ys[r] for r in ys},groups=res,joint_dimension=sum(x['kernel']['rows'] for x in res),full_dimension=sum(x['full_kernel']['rows'] for x in res),induced_basis=bases,image_coordinates=coordinates,image_rank=4,invisible_dimension=9,scope='Pure imaginary coefficients with Hermitian H-adjoint and positive-core conditions; changed real-structure branch, not source-selected.')
 # The unique upper survivor and the allowed southeast-block repair.
 rec=next(x for x in res if x['upper_kernel']['rows']);from k1836_k77_differential_dirac_quotient import mat
 coeff=mat(rec['upper_kernel'])[0];Id=identity_matrix(QQ,128,sparse=True);Zero=matrix(QQ,128,128,sparse=True)
 omats=[sum((coef*(3*Id+v)*eta[k]*y[k]*g[k]/4 for coef,(mask,y) in zip(coeff,rec['labels']) if coef and mask==0),Zero) for k in range(14)]
 assert all(mask==0 for coef,(mask,y) in zip(coeff,rec['labels']) if coef)
 # setup returned the original raw action as the last entry.
 apply=setup()[-1];raw=[sum((apply(k,[om*x for x in js])[a] for k,om in enumerate(omats)),Zero) for a in range(14)]
 M=Fi*raw[0];Bb=g[7]
 for k in range(8,14):Bb=Bb*g[k]
 bottom=sum((eta[k]*Bb*omats[k].transpose()*Bb*js[k] for k in range(14)),Zero)
 se=(djs[14]*M-bottom)*Fi;assert Bb*se==se.transpose()*Bb
 energy=P*M+M.transpose()*P;ld=bottom-djs[14]*M
 survivor=dict(M=enc(M),southeast_repair=enc(se),energy_defect=enc(energy),lower_defect=enc(ld),energy_rank=energy.rank(),lower_rank=ld.rank(),southeast_rank=se.rank())
 inputs=['lab/process/k1951-coordinated-zero-southeast-principal.json','lab/process/k2021-common-degree-dual-operator.json','lab/process/k2026-compatible-mass-moduli.json']
 return dict(result_id='K2028',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',coefficient_variables=14*16384,common_form_dimension=8388,grade_kernels={str(r):ys[r] for r in ys},survivor=survivor,groups=res,upper_dimension=sum(len(x['labels'])-x['upper_rank'] for x in res),full_upper_dimension=sum(x['full_upper_dimension'] for x in res),joint_dimension=0,scope='All real128-by128 connection coefficients in the fixed raw upper contraction, fixed H and invariant128 core with P=8I. No complex-coefficient, changed-form, changed-core or GU-wide conclusion.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs})

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();r=produce();r['complex_hermitian_branch']=produce(True)
 if args.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text())
 print('PASS K2028 common',r['common_form_dimension'],'upper',r['upper_dimension'],'joint',r['joint_dimension'],flush=True)
