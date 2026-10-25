"""Independent signed-bit raw-action and finite-field completeness replay."""
from pathlib import Path
import json,time,hashlib
import numpy as np
from sage.all import QQ,matrix,GF,identity_matrix,zero_matrix,block_diagonal_matrix
from k2034_observed_principal_forms_probe import gamma
from k1836_k77_differential_dirac_quotient import mat
def mat(x):return matrix(QQ,x['rows'],x['columns'],{(i,j):QQ(v) for i,j,v in x['entries']},sparse=True)
ROOT=Path(__file__).resolve().parents[2]

def ranks():
 n=128;ix=np.arange(n);I=(0,np.ones(n,dtype=np.int64))
 def mono(d):
  fs={i^j for i,j in d};assert len(fs)==1;f=fs.pop();a=np.array([int(d.get((i,i^f),0)) for i in range(n)],dtype=np.int64);assert all(a[i]==d.get((i,i^f),0) for i in range(n));return f,a
 def mul(a,c):return a[0]^c[0],a[1]*c[1][ix^a[0]]
 def add(terms):
  fs={t[0] for t in terms};assert len(fs)==1,fs
  return terms[0][0],sum((t[1] for t in terms),np.zeros(n,dtype=np.int64))
 def sc(v,t):return t[0],v*t[1]
 def tr(t):return t[0],t[1][ix^t[0]]
 g=list(map(lambda k:mono(gamma(k)),range(14)));V=I;B=I
 for z in g:V=mul(V,z)
 for z in g[7:]:B=mul(B,z)
 W2=(0,3-V[1]);Wb2=(0,3+V[1]);eta=[1]*7+[-1]*7
 G=[I]
 for m in range(1,16384):k=m.bit_length()-1;G.append(mul(G[m^(1<<k)],g[k]))
 r=json.loads((ROOT/'lab/process/k2028-all-grade-raw-common-form.json').read_text())
 def col(mask,y,s,imag):
  om=[sc(eta[k]*y[k],mul(Wb2,mul(g[k],G[mask]))) for k in range(14)]
  out=[]
  for a in range(14):
   terms=[mul(om[a],Wb2)]
   for k in range(14):
    if a!=s and k not in (a,s):terms.append(sc(eta[a]*eta[s],mul(mul(mul(mul(mul(g[a],g[k]),g[s]),W2),om[k]),g[s])))
   out.append(add(terms))
  bottom=sc(-2 if imag else 2,mul(mul(mul(B,tr(om[s])),B),g[s]))
  # Independently invert D0 by summing its thirteen normalized transverse equations.
  ts=[mul(mul(g[0],g[k]),out[k]) for k in range(1,14)];total=add(ts)
  results=[add([mul(W2,add([total,sc(-12,ts[k-1])])),sc(48,mul(g[0],bottom))]) for k in (7,8,9)]
  us=add([ts[k-1] for k in [1,2,3,4,5,6,10,11,12,13]])
  results.append(add([sc(12,mul(W2,out[0])),sc(96,mul(g[0],bottom)),sc(-1,mul(W2,add([sc(10,total),sc(-12,us)])))]))
  return tuple(z[0] for z in results),np.concatenate([z[1] for z in results]).tolist()
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
   T=matrix(GF(103),[c[2] for c in cs]).transpose();rr=list(T.transpose().pivots());K=T.right_kernel().basis_matrix();assert T*K.transpose()==0
   # Refine survivors using all10 independent transverse inputs and common observed t input later.
   ks=[K.nrows()]
   for s in [2,3,4,5,6,10,11,12,13]:
    if not K.nrows():break
    T2=matrix(GF(103),[col(m,y,s,imag)[1] for m,y,_ in cs]).transpose()
    reduced=T2*K.transpose();K=reduced.right_kernel().basis_matrix()*K;ks.append(K.nrows())
   # finite-field rank gives a lower bound on rational rank.
   records.append(dict(key=list(key),dimension=K.nrows(),first_rank=len(rr),dims=ks))
  allres['imaginary' if imag else 'real']=records
  print('TOTAL',imag,sum(x['dimension'] for x in records),'secs',time.time()-start,flush=True)

 return allres
def multiply(*xs):
 a=xs[0]
 for c in xs[1:]:
  columns={}
  for (i,k),v in a.dict().items():columns.setdefault(k,[]).append((i,v))
  entries={}
  for (k,j),w in c.dict().items():
   for i,v in columns.get(k,[]):entries[i,j]=entries.get((i,j),0)+v*w
  a=matrix(QQ,a.nrows(),c.ncols(),{k:v for k,v in entries.items() if v},sparse=True)
 return a
def full_replay(r):
 g=[matrix(QQ,128,128,{ij:QQ(v.numerator)/v.denominator for ij,v in gamma(k).items()},sparse=True) for k in range(14)];I=identity_matrix(QQ,128,sparse=True);V=I;B=I
 for x in g:V=V*x
 for x in g[7:]:B=B*x
 W=(3*I-V)/2;Wb=(3*I+V)/2;eta=[1]*7+[-1]*7;O=[0,7,8,9];U=[k for k in range(14) if k not in O]
 E=[]
 for k in range(14):
  z=zero_matrix(QQ,128,1408,sparse=True);j=0 if k in O else 1+U.index(k);z[:,128*j:128*(j+1)]=eta[k]*g[k];E.append(z)
 z=zero_matrix(QQ,128,1408,sparse=True)
 for j in range(11):z[:,128*j:128*(j+1)]=(2 if j==0 else 1)*Wb
 E.append(z)
 def derivative(k,fields):
  terms=[multiply(g[c],W,fields[c]) for c in range(14)];total=sum(terms,zero_matrix(QQ,128,fields[0].ncols(),sparse=True))
  return [fields[14] if a==k else eta[a]*multiply(g[a],g[k],total-terms[a]-terms[k]) for a in range(14)]+[-eta[k]*fields[k]]
 DE=derivative(0,E);counts={}
 for kind,v in r['full'].items():
  en=[];invariant=[]
  for j,(o,n) in enumerate(zip(v['omegas'],v['images'])):
   oms=list(map(mat,o));N=mat(n);out=[zero_matrix(QQ,128,1408,sparse=True) for _ in range(15)]
   for k,om in enumerate(oms):
    if not om:continue
    fields=[multiply(om,x) for x in E];part=derivative(k,fields)
    for a in range(14):out[a]+=part[a]
    out[14]+=(1 if kind=='real' else -1)*eta[k]*multiply(B,om.transpose(),B,E[k])
   good=all(x==multiply(y,N) for x,y in zip(out,DE));invariant.append(good)
   if kind=='real':assert not good,'real observed-input obstruction'
   else:assert good,'all full graph columns'
   en.append(N+N.transpose() if kind=='real' else N-N.transpose())
  if kind=='imaginary':
   ks=mat(v['positive_kernel']);assert ks.nrows()==13 and ks.rank()==13
   for row in ks:
    out={}
    for c,x in zip(row,en):
     if c:
      for key,v0 in x.dict().items():out[key]=out.get(key,0)+c*v0
    assert not any(out.values())
   assert any(en),'strict energy restriction'
  counts[kind]=sum(invariant)
  print('separate raw full',kind,counts[kind],flush=True)
 # Explicit same-H completion of the free mass on all11 copies.
 ext=r['massive_extension'];M=mat(ext['mass']);K=mat(ext['coefficient']);N=block_diagonal_matrix([M]*11);H=block_diagonal_matrix([eta[k]*B for k in range(14)]+[B]);EE=matrix(QQ,1920,1408,{(128*k+i,j):v for k,x in enumerate(E) for (i,j),v in x.dict().items()},sparse=True);DDE=matrix(QQ,1920,1408,{(128*k+i,j):v for k,x in enumerate(DE) for (i,j),v in x.dict().items()},sparse=True)
 assert multiply(H,K)==multiply(K.transpose(),H) and multiply(K,EE)==multiply(DDE,N),'mass extension'
 assert M.transpose()==-M and M*M==-I,'stable mass'
 for k in O[1:]:assert M*(g[0]*g[k])+(g[0]*g[k])*M==0,'mass Clifford relation'
 assert K[1792:,1792:]==0,'zero southeast'
 # Actual matrix faults following the full clean baseline.
 bad=matrix(K);bad[0,0]+=1
 assert multiply(bad,EE)!=multiply(DDE,N),'planted coefficient defect'
 wrong=g[0]*g[1]*g[2]*g[3];assert wrong*wrong==I and wrong.transpose()==wrong,'wrong signature instability'
 badN=matrix(N);badN[0,0]+=1
 assert multiply(K,EE)!=multiply(DDE,badN) and badN+badN.transpose()!=0,'planted energy defect'
 broken=matrix(EE);broken[1792,0]+=1
 assert multiply(K,broken)!=multiply(DDE,N),'planted graph defect'
 return counts
if __name__=='__main__':
 r=json.loads((ROOT/'lab/process/k2036-maximal-graph-raw-couplings.json').read_text())
 for path,digest in r['inputs'].items():assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,'input provenance'
 rr=ranks()
 assert sum(x['dimension'] for x in rr['real'])==1 and sum(x['dimension'] for x in rr['imaginary'])==14
 for kind,groups in rr.items():
  stored={tuple(x['key']):x for x in r['transverse'][kind]}
  for gr in groups:
   s=stored[tuple(gr['key'])];assert gr['dimension']==s['remaining']['rows'] and gr['first_rank']==s['first_rank']
 print('BASELINE ranks pass; full',full_replay(r));print('PASS K2036 separate complete raw action,mod103 rank and4 actual faults')
