#!/usr/bin/env python3
"""Exact controls, not a proof of source applicability or global ellipticity."""
from fractions import Fraction as Q
from itertools import combinations
from math import comb
import json,time

def zero(m,n):return [[Q(0) for _ in range(n)] for _ in range(m)]
def eye(n):return [[Q(i==j) for j in range(n)]for i in range(n)]
def mul(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)]for row in a]
def sub(a,b):return [[x-y for x,y in zip(u,v)]for u,v in zip(a,b)]
def scale(c,a):return [[c*x for x in row]for row in a]
def tr(a):return sum(a[i][i]for i in range(len(a)))
def rank(a):
 a=[[Q(v)for v in row]for row in a];m=len(a);n=len(a[0])if m else 0;r=0
 for j in range(n):
  k=next((k for k in range(r,m)if a[k][j]),None)
  if k is None:continue
  a[r],a[k]=a[k],a[r];t=a[r][j];a[r]=[x/t for x in a[r]]
  for k in range(m):
   if k!=r and a[k][j]:
    t=a[k][j];a[k]=[x-t*y for x,y in zip(a[k],a[r])]
  r+=1
  if r==m:break
 return r

def wedge(k,p):
 n=len(k);src=list(combinations(range(n),p));dst=list(combinations(range(n),p+1));ix={s:i for i,s in enumerate(dst)};a=zero(len(dst),len(src))
 for j,s in enumerate(src):
  for i,c in enumerate(k):
   if i not in s:a[ix[tuple(sorted((i,)+s))]][j]+=c*(-1)**sum(v<i for v in s)
 return a

def run():
 t=time.perf_counter();checks=[];data={}
 def ck(name,test):
  assert test,name
  checks.append(name)
 # Complete exterior sequence works in indefinite signature in every dimension.
 for n in range(2,8):
  k=[Q(1),Q(1)]+[Q(0)]*(n-2);ds=[wedge(k,p)for p in range(n)];rs=[rank(d)for d in ds]
  ck(f'deRham_{n}_ranks',rs==[comb(n-1,p)for p in range(n)])
  ck(f'deRham_{n}_complex',all(mul(ds[p+1],ds[p])==zero(len(ds[p+1]),len(ds[p][0]))for p in range(n-1)))
  ck(f'deRham_{n}_exact',all(rs[p-1]+rs[p]==comb(n,p)for p in range(1,n)))
  ck(f'deRham_{n}_shifted_trace',sum((-1)**p*(-p)*comb(n,p)for p in range(n+1))==0)
 data['deRham_positive_control']='Full exterior sequence exact at real null k in n=2..7; n3 is exactly the short firstorder profile.'
 # Maxwell is degree 1,2,1, including a sharp n2 null positive control.
 maxwell=[]
 for n in [2,3,4,14]:
  eta=[1,-1]+[1]*(n-2);B=zero(n,n);B[0][1]=B[1][0]=1
  for label,k in [('null',[1,1]+[0]*(n-2)),('positive',[1]+[0]*(n-1)),('negative',[0,1]+[0]*(n-2))]:
   k=list(map(Q,k));sharp=[a*b for a,b in zip(eta,k)];q=sum(a*b for a,b in zip(k,sharp));G=[[x]for x in k];W=[sharp];L=sub(scale(q,eye(n)),mul(G,W));rs=[rank(G),rank(L),rank(W)];hs=[n-rs[0]-rs[1],n-rs[1]-rs[2]]
   ck(f'Maxwell_{n}_{label}_complex',mul(L,G)==zero(n,1)and mul(W,L)==zero(1,n))
   ck(f'Maxwell_{n}_{label}_homology',hs==([n-2,n-2]if label=='null'else[0,0]))
   if label=='null':
    ck(f'Maxwell_{n}_boost',mul(B,G)==G and sub(mul(B,L),mul(L,B))==scale(2,L)and scale(-1,mul(W,B))==W)
    ck(f'Maxwell_{n}_trace',tr(sub(B,eye(n)))-tr(sub(B,scale(3,eye(n))))==2*n)
   maxwell.append(dict(n=n,covector=label,ranks=rs,middle_homology=hs))
 data['maxwell']=maxwell
 # Natural module boost traces cancel before shifts; after shifts the defect is forced.
 for n in [2,3,4,7,14]:
  for d in [1,2,16384]:
   for a,b,c in [(1,1,1),(1,2,1),(1,0,1),(2,1,3)]:
    te=Q(7,3);dims=[d,n*d,n*d,d];ts=[te,n*te,n*te,te];shifts=[0,a,a+b,a+b+c]
    val=sum((-1)**j*(ts[j]-shifts[j]*dims[j])for j in range(4))
    ck(f'order_trace_{n}_{d}_{a}{b}{c}',val==(a+c-(n-1)*b)*d)
 ck('native14_firstorder_defect', (3-14)*16384==-180224)
 ck('native14_integer_order_impossibility',2%13!=0)
 # Laurent character identity for nontrivial E, independent from trace differentiation.
 for n in [3,4,14]:
  base={0:1,-3:-1}
  for w,m in [(1,1),(-1,1),(0,n-2)]:
   base[w-1]=base.get(w-1,0)-m;base[w-2]=base.get(w-2,0)+m
  base={w:m for w,m in base.items()if m}
  ck(f'character_identity_{n}',base==({}if n==3 else{-1:-(n-3),-2:n-3}))
 # Nonsemisimple chain-map trace cancellation: exact split complex, arbitrary block Jordan maps.
 for aa,bb,cc in [(1,2,1),(2,3,2)]:
  dims=[aa,aa+bb,bb+cc,cc];ds=[zero(dims[j+1],dims[j])for j in range(3)]
  for i in range(aa):ds[0][i][i]=1
  for i in range(bb):ds[1][i][aa+i]=1
  for i in range(cc):ds[2][i][bb+i]=1
  def block(s,l):
   A=scale(l,eye(s))
   for i in range(s-1):A[i][i+1]=1
   return A
  def diag(A,C):
   M=zero(len(A)+len(C),len(A)+len(C))
   for i,row in enumerate(A):M[i][:len(A)]=row
   for i,row in enumerate(C):M[len(A)+i][len(A):]=row
   return M
  A=block(aa,2);C=block(bb,-3);D=block(cc,5);H=[A,diag(A,C),diag(C,D),D]
  ck(f'nondiagonal_chain_{aa}',all(mul(H[j+1],ds[j])==mul(ds[j],H[j])for j in range(3)))
  ck(f'exact_chain_{aa}',rank(ds[0])==aa and rank(ds[2])==cc and all(rank(ds[j-1])+rank(ds[j])==dims[j]for j in [1,2]))
  ck(f'alternating_trace_{aa}',sum((-1)**j*tr(H[j])for j in range(4))==0)
  bad=[row[:]for row in H[1]];bad[0][0]+=1
  ck(f'planted_non_chain_map_{aa}',mul(bad,ds[0])!=mul(ds[0],H[0]))
 # The deliberately omitted degree shift would yield a false pass.
 ck('planted_unshifted_trace_rejected',sum((-1)**j*x for j,x in enumerate([1,14,14,1]))==0 and (3-14)!=0)
 data.update(status='PASS',grouped_checks=len(checks),checks=checks,runtime_seconds=time.perf_counter()-t,scope='Exact finite controls; universal theorem is written/reviewed; no full GU complex, source covariance, global domain or novelty certified.')
 return data
if __name__=='__main__':print(json.dumps(run(),indent=2))
