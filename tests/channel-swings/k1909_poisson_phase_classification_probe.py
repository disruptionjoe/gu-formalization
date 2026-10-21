"""Independent Fraction polynomial arithmetic and exact elimination; no producer import."""
from pathlib import Path
from fractions import Fraction as F
from copy import deepcopy
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
ZERO=(F(0),F(0));ONE=(F(1),F(0))
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def neg(a):return(-a[0],-a[1])
def mul(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conj(a):return(a[0],-a[1])
def read(v):
 z=s.sympify(v);return F(str(s.re(z))),F(str(s.im(z)))
def pa(a,b):
 out=dict(a)
 for k,v in b.items():out[k]=add(out.get(k,ZERO),v)
 return {k:v for k,v in out.items() if v!=ZERO}
def pm(a,b):
 out={}
 for ka,va in a.items():
  for kb,vb in b.items():
   k=tuple(x+y for x,y in zip(ka,kb));out[k]=add(out.get(k,ZERO),mul(va,vb))
 return {k:v for k,v in out.items() if v!=ZERO}
def const(v):return {(0,0,0):v}
def cp(axis,sign):
 e1=tuple(1 if i==axis else 0 for i in range(3));e2=tuple(2 if i==axis else 0 for i in range(3));return {(0,0,0):ONE,e1:(F(0),F(2*sign)),e2:(F(-1),F(0))}
def check(d,flip_c=False):
 count=0
 def ck(ok,label):
  nonlocal count
  assert ok,label
  count+=1
 W=[[read(v) for v in row] for row in d['W']];G=[[F(v) for v in row] for row in d['G']]
 ck(all(W[i][j]==conj(W[j][i]) for i in range(4) for j in range(4)),'Hermitian input')
 ck(all(sum(v[0] for v in row)==0 and sum(v[1] for v in row)==0 for row in W),'row-sum tangent')
 dens=[{(0,0,0):ONE,tuple(2 if k==i else 0 for k in range(3)):ONE} for i in range(3)]+[const(ONE)]
 p={}
 for j in range(4):
  for k in range(4):
   term=const(W[j][k])
   for h in range(4):
    term=pm(term,cp(h,-1) if j!=k and h==j and h<3 else cp(h,1) if j!=k and h==k and h<3 else dens[h] if h not in [j,k] or j==k else const(ONE))
   p=pa(p,term)
 mons=[(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,1,1)];gp={}
 for i in range(7):
  for j in range(7):gp=pa(gp,{tuple(a+b for a,b in zip(mons[i],mons[j])):(G[i][j],F(0))})
 ck(p==gp,'independent cleared polynomial identity')
 R=deepcopy(G);piv=[]
 for k in range(7):
  pivot=R[k][k];ck(pivot>0,'rational Schur pivot');piv.append(str(pivot))
  for i in range(k+1,7):
   for j in range(k+1,7):R[i][j]-=R[i][k]*R[k][j]/pivot
 ck(piv==d['LDL_pivots'],'reported rational pivots')
 # Direct trace from explicit correlation entries, separate from V*V construction.
 a=1/s.sqrt(2);ii=-s.I if flip_c else s.I
 C=s.Matrix([[1,0,a,a],[0,1,a,ii*a],[a,a,1,(1+ii)/2],[a,-ii*a,(1-ii)/2,1]])
 WW=s.Matrix([[s.Rational(v[0].numerator,v[0].denominator)+s.I*s.Rational(v[1].numerator,v[1].denominator) for v in row] for row in W])
 ck(s.simplify(s.trace(WW*C)-(s.Rational(1777,1000)-159*s.sqrt(2)/125))==0,'independent signed derivative')
 ck(d['interval']=='0<t<1/55' and d['output_trace_distance_lower']=='1/176000','report limits')
 ck(d['dependency_sha256']==hashlib.sha256((ROOT/'explorations/conditional-build/k1908-quantum-markov-phase-noise-2026-10-21.md').read_bytes()).hexdigest(),'dependency pin')
 # All-chart positive controls including omitted half-angle points, not used as universal proof.
 for z in [s.ones(4,1),s.Matrix([-1,1,-1,1]),s.Matrix([s.I,-s.I,-1,1])]:ck(s.simplify((z.conjugate().T*WW*z)[0])>=0,'phase control')
 return count
if __name__=='__main__':
 data=json.loads((ROOT/'lab/process/k1909-poisson-phase-classification.json').read_text());print('BASELINE',check(data),'exact/control/report/pin checks')
 faults=[]
 for name in ['witness','Gram','correlation','report','pin']:
  d=deepcopy(data)
  if name=='witness':d['W'][0][0]='0'
  if name=='Gram':d['G'][0][0]='0'
  if name=='report':d['interval']='all t>0'
  if name=='pin':d['dependency_sha256']='0'*64
  try:check(d,flip_c=name=='correlation')
  except AssertionError as exc:print('CAUGHT',name,str(exc));faults.append(name)
  else:raise AssertionError('undetected '+name)
 assert len(faults)==5
 print('PASS 3 mathematical-input, 1 report and 1 pin faults; no crash catches')
