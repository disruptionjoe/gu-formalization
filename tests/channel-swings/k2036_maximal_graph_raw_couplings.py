"""Complete fixed common-form coefficient classification on the maximal1408 graph.

Real and imaginary coefficient classes are kept distinct. K2028 supplies the
complete common-form bases; this file recomputes all graph constraints exactly.
"""
from pathlib import Path
import json,hashlib,argparse,time
import numpy as np
from sage.all import QQ,GF,matrix,identity_matrix,zero_matrix,block_diagonal_matrix,lcm
import k2021_common_degree_dual_operator as b
from k2032_principal_form_rigidity import sm,raw
from k1836_k77_differential_dirac_quotient import mat,enc
def mat(x):return matrix(QQ,x['rows'],x['columns'],{(i,j):QQ(v) for i,j,v in x['entries']},sparse=True)
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2036-maximal-graph-raw-couplings.json'

def mm(*xs):
 a=xs[0]
 for c in xs[1:]:
  rows={}
  for (i,j),v in c.dict().items():rows.setdefault(i,[]).append((j,v))
  out={}
  for (i,k),v in a.dict().items():
   for j,w in rows.get(k,[]):out[i,j]=out.get((i,j),0)+v*w
  a=matrix(QQ,a.nrows(),c.ncols(),{k:v for k,v in out.items() if v},sparse=True)
 return a

def graph():
 I=identity_matrix(QQ,128,sparse=True);g=[sm(b.gamma(k)) for k in range(14)];W=sm(b.W);Wb=3*I-W;O=[0,7,8,9];U=[k for k in range(14) if k not in O]
 # Normalize all one-form coordinates zeta_r=eta_r gr u_r.
 E=matrix(QQ,1920,1408,sparse=True)
 for r in range(14):
  j=0 if r in O else 1+U.index(r)
  E[128*r:128*(r+1),128*j:128*(j+1)]=b.ETA[r]*g[r]
 for j in range(11):E[1792:1920,128*j:128*(j+1)]=(2 if j==0 else 1)*Wb
 D=raw(0,W);DE=mm(D,E)
 # annihilator with sparse natural graph constraints and explicit D0 inverse.
 L=matrix(QQ,512,1920,sparse=True)
 for j,r in enumerate(O[1:]):L[128*j:128*(j+1),128*r:128*(r+1)]=g[r];L[128*j:128*(j+1),:128]=-g[0]
 L[384:512,1792:1920]=Wb.inverse();L[384:512,:128]=-2*g[0]
 for r in U:L[384:512,128*r:128*(r+1)]=-g[r]
 assert mm(L,E)==0
 Di=D.inverse();F=mm(L,Di);assert mm(F,DE)==0

 return E,D,Di,F

def transverse_constraints(ann):
 n=128;ix=np.arange(n);I=(0,np.ones(n,dtype=np.int64))
 def mono(d):
  fs={i^j for i,j in d};assert len(fs)==1;f=fs.pop();a=np.array([int(d.get((i,i^f),0)) for i in range(n)],dtype=np.int64);assert all(a[i]==d.get((i,i^f),0) for i in range(n));return f,a
 def mul(a,c):return a[0]^c[0],a[1]*c[1][ix^a[0]]
 def add(terms):
  fs={t[0] for t in terms};assert len(fs)==1,fs
  return terms[0][0],sum((t[1] for t in terms),np.zeros(n,dtype=np.int64))
 def sc(v,t):return t[0],v*t[1]
 def tr(t):return t[0],t[1][ix^t[0]]
 g=list(map(lambda k:mono(b.gamma(k)),range(14)));V=mono(b.J);B=mono(b.B);W2=(0,3-V[1]);Wb2=(0,3+V[1]);eta=b.ETA
 F={}
 for j in range(4):
  for r0 in range(15):
   M=24*ann[128*j:128*(j+1),128*r0:128*(r0+1)]
   if M:F[j,r0]=mono(M.dict())
 G=[I]
 for m in range(1,16384):k=m.bit_length()-1;G.append(mul(G[m^(1<<k)],g[k]))
 r=json.loads((ROOT/'lab/process/k2028-all-grade-raw-common-form.json').read_text())
 def col(mask,y,s,imag):
  om=[sc(eta[k]*y[k],mul(Wb2,mul(g[k],G[mask]))) for k in range(14)] #4Omega
  ts=[mul(mul(mul(g[k],g[s]),W2),mul(om[k],g[s])) for k in range(14)]
  total=add(ts)
  out=[]
  for a in range(14):
   z=mul(om[a],Wb2)
   if a!=s:z=add([z,sc(eta[a]*eta[s],mul(g[a],add([total,sc(-1,ts[a]),sc(-1,ts[s])])) )])
   out.append(z) #8 K E
  out.append(sc(-2 if imag else 2,mul(mul(mul(B,tr(om[s])),B),g[s])))
  result=[add([mul(F[j,a],out[a]) for a in range(15) if (j,a) in F]) for j in range(4)]
  return tuple(z[0] for z in result),np.concatenate([z[1] for z in result]).tolist()
 allres={};start=time.time()
 for imag,data in [(False,r),(True,r['complex_hermitian_branch'])]:
  groups={}
  for gr in data['groups']:
   for mask,y in gr['labels']:
    key,v=col(mask,y,1,imag);groups.setdefault(key,[]).append((mask,y,v))
  print('built',imag,len(groups),sum(map(len,groups.values())),flush=True)
  # Disjointness of equation coordinates between groups checked explicitly.
  seen=set()
  for key in groups:
   coords={(j,f) for j,f in enumerate(key)};assert not coords&seen;seen|=coords
  records=[]
  for key,cs in groups.items():
   T=matrix(QQ,[c[2] for c in cs]).transpose();rr=list(T.change_ring(GF(101)).transpose().pivots());small=T.matrix_from_rows(rr);K=small.right_kernel().basis_matrix();assert T*K.transpose()==0
   # Refine survivors using all10 independent transverse inputs and common observed t input later.
   ks=[K.nrows()]
   for s in [2,3,4,5,6,10,11,12,13]:
    if not K.nrows():break
    T2=matrix(QQ,[col(m,y,s,imag)[1] for m,y,_ in cs]).transpose()
    reduced=T2*K.transpose();K=reduced.right_kernel().basis_matrix()*K;ks.append(K.nrows())
   # Full exact residual is tested at every refinement.
   from k1836_k77_differential_dirac_quotient import enc
   records.append(dict(key=list(key),labels=[[m,y] for m,y,_ in cs],first_rows=rr,first_rank=len(rr),remaining=enc(K),dims=ks))
  allres['imaginary' if imag else 'real']=records
  print('TOTAL',imag,sum(x['remaining']['rows'] for x in records),'secs',time.time()-start,flush=True)

 return allres

def full_constraints(E,D,Di,rs):
 I=identity_matrix(QQ,128,sparse=True);g=[sm(b.gamma(k)) for k in range(14)];W=sm(b.W);Wb=3*I-W;O=[0,7,8,9];U=[k for k in range(14) if k not in O]
 DE=mm(D,E);B=sm(b.B);H=sm(b.H,1920)
 R=matrix(QQ,1408,1920,sparse=True)
 for j,r in enumerate([0]+U):R[128*j:128*(j+1),128*r:128*(r+1)]=g[r]
 assert mm(R,E)==identity_matrix(QQ,1408,sparse=True)
 ans={}
 for kind,groups in rs.items():
  labels=[];defects=[];energies=[];images=[];omlist=[]
  for rec in groups:
   for coeff in mat(rec['remaining']):
    oms=[sum((q*Wb*b.ETA[k]*g[k]*sm(b.blade(tuple(i for i in range(14) if mask>>i&1)))*y[k]/2 for q,(mask,y) in zip(coeff,rec['labels']) if q and y[k]),zero_matrix(QQ,128,128,sparse=True)) for k in range(14)]
    K=matrix(QQ,1920,1920,sparse=True)
    for k,om in enumerate(oms):
     if not om:continue
     K+=mm(raw(k,W),block_diagonal_matrix([om]*15))
    for k,om in enumerate(oms):K[1792:1920,128*k:128*(k+1)]=(1 if kind=='real' else -1)*b.ETA[k]*B*om.transpose()*B
    assert mm(H,K)==(mm(K.transpose(),H) if kind=='real' else -mm(K.transpose(),H))
    image=mm(Di,K,E);N=mm(R,image);df=image-mm(E,N)
    ef=N+N.transpose() if kind=='real' else N-N.transpose()
    labels.append([[int(j),str(x)] for j,x in enumerate(coeff) if x]);omlist.append([enc(a) for a in oms]);images.append(enc(N));defects.append(df.dict());energies.append(ef.dict())
    print('full',kind,len(labels),'invariance',len(df.dict()),'energy',len(ef.dict()),flush=True)
  def kernel(ds):
   keys=sorted(set().union(*(d.keys() for d in ds)));T=matrix(QQ,[[d.get(k,0) for d in ds] for k in keys]) if keys else matrix(QQ,0,len(ds));return T.right_kernel().basis_matrix(),T.rank()
  Ki,ri=kernel(defects);Ke,re=kernel([{**{('i',*k):v for k,v in d.items()},**{('e',*k):v for k,v in e.items()}} for d,e in zip(defects,energies)])
  ans[kind]=dict(invariance_dimension=Ki.nrows(),positive_dimension=Ke.nrows(),invariance_kernel=enc(Ki),positive_kernel=enc(Ke),images=images,omegas=omlist)
  print('FINAL',kind,'invariant',Ki.nrows(),'positive',Ke.nrows(),flush=True)

 return ans

def massive_extension(E,D):
 I=identity_matrix(QQ,128,sparse=True);g=[sm(b.gamma(k)) for k in range(14)];H=sm(b.H,1920);U=[1,2,3,4,5,6,10,11,12,13]
 R=matrix(QQ,1408,1920,sparse=True)
 for j,r in enumerate([0]+U):R[128*j:128*(j+1),128*r:128*(r+1)]=g[r]
 M=g[0]*g[1]*g[2]*g[10];N=block_diagonal_matrix([M]*11);Y=mm(H,D,E,N);S=mm(E.transpose(),Y)
 assert S==S.transpose()
 if True:
  K=mm(H,mm(Y,R)+mm(R.transpose(),Y.transpose())-mm(R.transpose(),S,R))
  assert mm(H,H)==identity_matrix(QQ,1920,sparse=True)
  assert mm(H,K)==mm(K.transpose(),H) and mm(K,E)==mm(D,E,N)
  print('repair entries',len(K.dict()),'se',len(K[1792:,1792:].dict()),flush=True)

 return dict(mass=enc(M),coefficient=enc(K),southeast_zero=not bool(K[1792:,1792:]),dimension=1408)

def combine(row,matrices):
 out={}
 for c,M in zip(row,matrices):
  if c:
   for k,v in M.dict().items():out[k]=out.get(k,0)+c*v
 return matrix(QQ,matrices[0].nrows(),matrices[0].ncols(),{k:v for k,v in out.items() if v},sparse=True)

def produce():
 E,D,Di,F=graph();r=transverse_constraints(F);a=full_constraints(E,D,Di,r)
 assert a['real']['invariance_dimension']==a['real']['positive_dimension']==0
 assert a['imaginary']['invariance_dimension']==14 and a['imaginary']['positive_dimension']==13
 Ns=[mat(x) for x in a['imaginary']['images']];pk=mat(a['imaginary']['positive_kernel']);basis=[combine(row,Ns) for row in pk];g=[sm(b.gamma(k)) for k in range(14)];targets=[block_diagonal_matrix([identity_matrix(QQ,128,sparse=True)]*11)]+[block_diagonal_matrix([g[0]*g[k]]*11) for k in (7,8,9)]
 # Four nonzero basis matrices are proportional to I,C7,C8,C9; other nine vanish.
 nonzero=[N for N in basis if N];assert len(nonzero)==4
 coordinates=[]
 for N in nonzero:
  found=[]
  for j,T in enumerate(targets):
   i0,j0=next(iter(T.dict()));c=N[i0,j0]/T[i0,j0]
   if c and N.dict()=={ij:c*v for ij,v in T.dict().items()}:found.append((j,str(c)))
  assert len(found)==1;coordinates+=found
 assert {j for j,c in coordinates}==set(range(4))
 extension=massive_extension(E,D)
 for kind,groups in r.items():
  for gr in groups:gr.pop('labels')
 refs=['lab/process/k2028-all-grade-raw-common-form.json','lab/process/k2034-observed-principal-forms.json','tests/channel-swings/k2021_common_degree_dual_operator.py']
 return dict(result_id='K2036',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',transverse=r,full=a,image_coordinates=coordinates,image_dimension=4,invisible_dimension=9,massive_extension=extension,inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in refs},scope='Fixed raw common H,zero southeast and maximal1408 observed graph;real invariance zero;imaginary invariance14 and fixed positive energy13. No physical selection or GU verdict.')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');args=p.parse_args();r=produce()
 if args.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text())
 print('PASS K2036 full coefficient classification',flush=True)
