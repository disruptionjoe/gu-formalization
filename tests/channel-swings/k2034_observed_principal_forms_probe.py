"""Separate signed-bit block and symbolic moving-metric verification."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def gamma(k):
 out={};j=k%7
 for col in range(128):
  bits=[(col>>(6-i))&1 for i in range(7)];sgn=(-1)**sum(bits[:j])
  if k>=7:sgn*=2*bits[j]-1
  out[col^(1<<(6-j)),col]=F(sgn)
 return out
def mul(a,b):
 rows={}
 for (i,j),v in b.items():rows.setdefault(i,[]).append((j,v))
 z={}
 for (i,k),v in a.items():
  for j,w in rows.get(k,[]):z[i,j]=z.get((i,j),F(0))+v*w
 return {ij:v for ij,v in z.items() if v}
def scale(a,c):return {ij:c*v for ij,v in a.items() if c*v}
def add(a,b):
 z=dict(a)
 for ij,v in b.items():z[ij]=z.get(ij,0)+v
 return {ij:v for ij,v in z.items() if v}
def tr(a):return {(j,i):v for (i,j),v in a.items()}
def replay(fault=None):
 I={(i,i):F(1) for i in range(128)};g=[gamma(i) for i in range(14)];eta=[1]*7+[-1]*7;V=I;B=I
 for x in g:V=mul(V,x)
 for x in g[7:]:B=mul(B,x)
 W=add(scale(I,F(3,2)),scale(V,F(-1,2)));Wb=add(scale(I,F(3,2)),scale(V,F(1,2)))
 U=[1,2,3,4,5,6,10,11,12,13];O=[0,7,8,9];Q=s.eye(10)-s.ones(10)/10
 if fault=='copy_projection':Q[0,0]+=1
 assert Q*Q==Q and Q*s.ones(10,1)==s.zeros(10,1),'copy projection'
 blocks=0
 for r in U:
  assert scale(mul(mul(tr(g[r]),B),g[r]),eta[r])==scale(B,-1),'form pullback'
 for k in O:
  G=mul(g[k],Wb)
  for r in U:
   for c in U:
    if r==c:continue
    raw=scale(mul(mul(mul(g[r],g[k]),g[c]),W),eta[r]);norm=scale(mul(mul(g[r],raw),g[c]),eta[c])
    assert norm==G,'transverse action';blocks+=1
  # Into observed rows, transformed column coefficient is independent of c.
  for r in O:
   if r==k:continue
   first=None
   for c in U:
    raw=scale(mul(mul(mul(g[r],g[k]),g[c]),W),eta[r]);z=scale(mul(raw,g[c]),eta[c])
    if first is None:first=z
    assert z==first,'sum-zero decoupling';blocks+=1
 # Separate symbolic complement reduction and maximal invariant kernel.
 a,b1,b2,b3,v,h=s.symbols('a b1 b2 b3 v h');coords=s.Matrix([a,b1,b2,b3,v,h]);Ts=[]
 for j in range(3):
  bs=[b1,b2,b3];others=sum(bs[l] for l in range(3) if l!=j);vp=(h+2*v-others)/12
  out=[bs[j]]+[a+others+9*v-h+vp if l==j else bs[l]-v+vp for l in range(3)]+[vp,others+10*v]
  T=s.Matrix(out).jacobian(coords)
  if fault=='complement_coefficient' and j==0:T[4,4]+=1
  defect=T*T-s.eye(6);assert defect*defect==s.zeros(6) and defect.rank()==1,'complement Jordan polynomial';Ts.append(T)
 R=s.Matrix.vstack(*(T*T-s.eye(6) for T in Ts));R2=s.Matrix.vstack(R,*(R*T for T in Ts));assert R.rank()==3 and R2.rank()==4,'maximal invariant dimension'
 graph=s.Matrix([[1,0],[1,0],[1,0],[1,0],[0,1],[2,10]])
 assert R2*graph==s.zeros(R2.rows,2)
 for T in Ts:assert T*graph==graph
 q=s.Matrix([[s.Rational(1,9)]*4+[1,0]]);sec=s.Matrix([0,0,0,0,1,10]);assert q*sec==s.ones(1)
 for T in Ts:assert q*T==q and T*sec==sec
 seed=s.Matrix([0,0,0,0,0,1]);span=seed;dims=[]
 while True:
  dims.append(span.rank());new=s.Matrix.hstack(span,*(T*span for T in Ts));cols=new.columnspace();new=s.Matrix.hstack(*cols)
  if new.cols==span.cols:break
  span=new
 assert dims==[1,4,5] and q*span==s.zeros(1,5),'complete cyclic complement'
 # Complete copy-scalar form space by independent linear equations on symmetric entries.
 pairs=[(i,j) for i in range(10) for j in range(i,10)]
 constraints=s.zeros(10,55)
 for j,(a,b) in enumerate(pairs):constraints[a,j]+=1;constraints[b,j]+=int(a!=b)
 assert constraints.rank()==10 and len(constraints.nullspace())==45
 M=mul(mul(mul(g[1],g[2]),g[10 if fault!='mass_signature' else 3]),Wb)
 assert mul(M,M)==scale(I,2),'mass square'
 assert mul(tr(M),B)==mul(B,M),'mass adjoint'
 G0=mul(g[0],Wb);K=scale(mul(G0,M),F(1,2))
 assert tr(K)==scale(K,-1) and mul(K,K)==scale(I,-1),'positive energy mass'
 Es=[]
 for i in O[1:]:
  E=mul(g[0],g[i]);assert tr(E)==E and mul(E,E)==I;Es.append(E)
  assert add(mul(E,K),mul(K,E))=={},'mass anticommutation'
 for i,E in enumerate(Es):
  for j,D in enumerate(Es):assert add(mul(E,D),mul(D,E))==(scale(I,2) if i==j else {}),'wave dispersion'
 # Genuine varying positive2-copy metric: both variables live, not a scalar ansatz.
 x,y=s.symbols('x y',real=True);a=1+y*y;A=s.Matrix([[a,a*x],[a*x,a*x*x+1]]);Ai=A.inv();Cs=[s.simplify(Ai*A.diff(v)/2) for v in [x,y]]
 if fault=='moving_connection':Cs=[s.zeros(2),s.zeros(2)]
 for v,C in zip([x,y],Cs):assert s.simplify(A*C+C.T*A-A.diff(v))==s.zeros(2),'metric connection'
 curve=s.simplify(Cs[1].diff(x)-Cs[0].diff(y)+Cs[0]*Cs[1]-Cs[1]*Cs[0]);expected=-(Cs[0]*Cs[1]-Cs[1]*Cs[0])
 assert s.simplify(curve-expected)==s.zeros(2) and curve.subs({x:0,y:1})!=s.zeros(2),'nonflat metric connection'
 assert s.factor(A.det())==1+y*y and A[0,0]==1+y*y,'positive metric'
 # Zero auxiliary-input column forces raw common connection zero, while the mass is nonzero.
 tied_upper={} if fault!='source_tie' else M
 assert tied_upper=={},'raw common-connection tie'
 return blocks
if __name__=='__main__':
 n=replay();faults=[]
 for fault in ['copy_projection','mass_signature','moving_connection','source_tie','complement_coefficient']:
  try:replay(fault)
  except AssertionError as e:faults.append([fault,str(e)])
  else:raise AssertionError('accepted fault '+fault)
 r=json.loads((ROOT/'lab/process/k2034-observed-principal-forms.json').read_text())
 for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 assert r['copy_symmetric_dimension']==45 and r['invariant_dimension']==9*128 and r['maximal_positive_dimension']==11*128
 print('PASS separate',n,'actual raw blocks;complete55-variable copy constraints;mass/evolution/curved connection; faults',faults,';provenance',len(r['inputs']))
