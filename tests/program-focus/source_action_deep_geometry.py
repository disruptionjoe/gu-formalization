"""Rational Nomizu model of the actual flat-base K95 metric bundle.
Basis: horizontal e0..e3; vertical eta-selfadjoint A4..A13, with tangent U=-2eta A.
No large numerical linear algebra. Root owns serialized execution.
"""
from fractions import Fraction as Q
from itertools import combinations
N=14; eta=[Q(1),Q(1),Q(1),Q(-1)]
def zero(n=4):return [[Q(0) for _ in range(n)] for _ in range(n)]
def eye(n=4):return [[Q(i==j) for j in range(n)] for i in range(n)]
def mm(a,b):return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
def sub(a,b):return [[x-y for x,y in zip(r,s)] for r,s in zip(a,b)]
def comm(a,b):return sub(mm(a,b),mm(b,a))
def trace(a):return sum(a[i][i] for i in range(len(a)))
def diag(v):return [[Q(v[i]) if i==j else Q(0) for j in range(len(v))] for i in range(len(v))]
A=[eye(),diag([1,-1,0,0]),diag([1,1,-2,0]),diag([1,1,1,-3])]
pairs=list(combinations(range(4),2))
for i,j in pairs:
 a=zero();a[i][j]=1;a[j][i]=eta[i]*eta[j];A.append(a)
def vg(a,b):return 4*trace(mm(a,b))-2*trace(a)*trace(b)
d=eta+[vg(a,a) for a in A]
assert d==list(map(Q,[1,1,1,-1,-16,8,24,48,8,8,-8,8,-8,-8]))
assert all(vg(a,b)==0 for i,a in enumerate(A) for j,b in enumerate(A) if i!=j)
def mbracket(i,j):
 if i<4 and j>=4:return {k:-A[j-4][k][i] for k in range(4) if A[j-4][k][i]}
 if i>=4 and j<4:return {k:A[i-4][k][j] for k in range(4) if A[i-4][k][j]}
 return {}
def hbracket(i,j):return comm(A[i-4],A[j-4]) if i>=4 and j>=4 else zero()
def h_action(H,j):
 if j<4:return {k:H[k][j] for k in range(4) if H[k][j]}
 b=comm(H,A[j-4]);return {k+4:vg(b,a)/d[k+4] for k,a in enumerate(A) if vg(b,a)}
Lambda=[[[Q(0) for k in range(N)] for j in range(N)] for i in range(N)]
for i in range(N):
 for j in range(N):
  for k in range(N):
   Lambda[i][j][k]=(mbracket(i,j).get(k,0)*d[k]-mbracket(j,k).get(i,0)*d[i]+mbracket(k,i).get(j,0)*d[j])/(2*d[k])
# Tangent matrices have output row,input column.
L=[[[Lambda[i][j][k] for j in range(N)] for k in range(N)] for i in range(N)]
spin=[]
for i in range(N):
 b={}
 for a in range(N):
  for c in range(a+1,N):
   q=Q(1,2)*d[a]*Lambda[i][c][a]/(d[a]*d[c])
   if q:b[(1<<a)|(1<<c)]=q
 spin.append(b)
def cliff_mul(a,b):
 swaps=sum((b&((1<<i)-1)).bit_count() for i in range(N) if a>>i&1)
 q=Q(-1 if swaps%2 else 1)
 for i in range(N):
  if (a&b)>>i&1:q*=d[i]
 return a^b,q
def cliff_comm(a,b):
 z={}
 for x,v in a.items():
  for y,w in b.items():
   c,s=cliff_mul(x,y);_,t=cliff_mul(y,x);z[c]=z.get(c,0)+v*w*(s-t)
 return {c:v for c,v in z.items() if v}
def curvature(i,j):
 R=comm(L[i],L[j])
 for k,v in mbracket(i,j).items():R=[[a-v*b for a,b in zip(r,s)] for r,s in zip(R,L[k])]
 H=hbracket(i,j)
 for c in range(N):
  for a,v in h_action(H,c).items():R[a][c]-=v
 return R
def curvature_spin(i,j):
 R=curvature(i,j);z={}
 for a in range(N):
  for b in range(a+1,N):
   q=R[a][b]/(2*d[b])
   if q:z[(1<<a)|(1<<b)]=q
 return z
def checks():
 out={}
 def check(k,b):out[k]=bool(b);assert b,k
 check('native_signature_9_5',sum(v>0 for v in d)==9 and sum(v<0 for v in d)==5)
 check('torsion_free',all(Lambda[i][j][k]-Lambda[j][i][k]==mbracket(i,j).get(k,0) for i in range(N) for j in range(N) for k in range(N)))
 check('metric_compatible',all(d[k]*Lambda[i][j][k]+d[j]*Lambda[i][k][j]==0 for i in range(N) for j in range(N) for k in range(N)))
 check('spin_convention',all(cliff_comm(spin[i],{1<<j:Q(1)})=={1<<k:v for k,v in enumerate(Lambda[i][j]) if v} for i in range(N) for j in range(N)))
 Rs={(i,j):curvature(i,j) for i in range(N) for j in range(N)}
 Ric=[[sum(Rs[i,j][i][k] for i in range(N)) for k in range(N)] for j in range(N)]
 expected=[Q(1,4)]*5+[Q(-5,4)]*9
 check('actual_Ricci_blocks',all(Ric[j][k]==(expected[j]*d[j] if j==k else 0) for j in range(N) for k in range(N)))
 check('scalar_minus10',sum(Ric[i][i]/d[i] for i in range(N))==-10)
 check('first_Bianchi',all(Rs[i,j][a][k]+Rs[j,k][a][i]+Rs[k,i][a][j]==0 for i in range(N) for j in range(N) for k in range(N) for a in range(N)))
 check('trace_divergence_minus4',sum(Lambda[i][4][i] for i in range(N))==-4)
 check('trace_normal_parallel_fibre',all(not any(Lambda[i][4]) for i in range(4,N)))
 return {'checks':out,'gram':[str(x) for x in d],'ricci_raised':[str(Ric[i][i]/d[i]) for i in range(N)]}
if __name__=='__main__':
 import json
 print(json.dumps(checks(),indent=2))
