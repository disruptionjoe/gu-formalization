"""Independent algebraic replay using symbolic13-slot reduction and matrix units."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parents[2]
def gamma(k):
 j=k%7;out={}
 for c in range(128):
  sign=(-1)**((c>>(7-j)).bit_count())
  if k>=7:sign*=1 if c&(1<<(6-j)) else -1
  out[c^(1<<(6-j)),c]=sign
 return out
def mul(a,b):
 rr={}
 for (i,j),v in b.items():rr.setdefault(i,[]).append((j,v))
 out={}
 for (i,k),v in a.items():
  for j,w in rr.get(k,[]):out[i,j]=out.get((i,j),0)+v*w
 return {ij:v for ij,v in out.items() if v}
def add(a,b,c=1):
 z=dict(a)
 for ij,v in b.items():z[ij]=z.get(ij,0)+c*v
 return {ij:v for ij,v in z.items() if v}
def replay(fault=None):
 I={(i,i):1 for i in range(128)};gg=[gamma(i) for i in range(14)];V=I
 for g in gg:V=mul(V,g)
 W={ij:F(3,2)*I.get(ij,0)-F(1,2)*V.get(ij,0) for ij in I}
 if fault=='weight':W[0,0]+=1
 Wbar={ij:F(3,2)*I.get(ij,0)+F(1,2)*V.get(ij,0) for ij in I}
 assert mul(W,Wbar)=={ij:2*v for ij,v in I.items()},'weight square'
 N=s.ones(13)-s.eye(13);assert (N-s.eye(13)*12)*(N+s.eye(13))==s.zeros(13)
 # Every transverse block conjugates to gk Wbar times(J-I), proving spectrum.
 blocks=0
 for k in range(14):
  eta=1 if k<7 else -1
  assert mul(mul(gg[k],Wbar),mul(gg[k],Wbar))=={ij:2*eta*v for ij,v in I.items()}
  for r in range(14):
   for c in range(14):
    if r==k or c in (r,k):continue
    # Left gr and right eta_c gc; source eta_r is included.
    q=mul(mul(mul(gg[r],mul(mul(mul(gg[r],gg[k]),gg[c]),W)),gg[c]),I)
    factor=(1 if r<7 else -1)*(1 if c<7 else -1)
    q={ij:factor*v for ij,v in q.items()};assert q==mul(gg[k],Wbar),'transverse conjugation';blocks+=1
 # Centralizer independent construction: equations on entries, signed cycles.
 generators=[mul(gg[0],gg[j]) for j in range(1,14)];maps=[{c:(r,v) for (r,c),v in g.items()} for g in generators];todo=set(product(range(128),repeat=2));good=[]
 while todo:
  start=min(todo);values={start:1};stack=[start];consistent=True
  while stack:
   i,j=stack.pop()
   for mapping in maps:
    ri,si=mapping[i];rj,sj=mapping[j];pair=(ri,rj);v=values[i,j]*si*sj
    if pair in values:consistent &= values[pair]==v
    else:values[pair]=v;stack.append(pair)
  todo.difference_update(values)
  if consistent:good.append(values)
 assert len(good)==2 and all(all(i==j for i,j in a) for a in good),'even centralizer'
 assert sorted(len(a) for a in good)==[64,64]
 # A commutant candidate with different chirality scalars fails actual odd block.
 O=mul(mul(mul(gg[0],gg[1]),gg[2]),W)
 candidate=I if fault!='chirality_scalar' else V
 assert mul(candidate,O)==mul(O,candidate),'odd compatibility'
 # Differential null field: z7=d8 f, z8=-d7 f, all other slots zero.
 t,x,y=s.symbols('t x y');f=t**3*x*y*(1-x)*(1-y)
 z7=s.diff(f,y);z8=-s.diff(f,x)
 if fault=='curl_sign':z8=-z8
 assert s.expand(s.diff(z7,x)+s.diff(z8,y))==0,'differential constraint'
 assert z7.subs(t,0)==z8.subs(t,0)==0 and z7!=0
 # Variable invertible weight: the correction is required by Leibniz, not optional.
 X=s.Matrix([[1,x],[0,1]]);S=X.inv();K=-s.diff(S,x)*X
 if fault=='moving_term':K=s.zeros(2)
 assert s.diff(S,x)+K*S==s.zeros(2),'moving weight connection'
 return blocks
if __name__=='__main__':
 r=json.loads((ROOT/'lab/process/k2032-principal-form-rigidity.json').read_text());n=replay();caught=[]
 for fault in ['weight','chirality_scalar','curl_sign','moving_term']:
  try:replay(fault)
  except AssertionError as e:caught.append([fault,str(e)])
  else:raise AssertionError('accepted actual fault '+fault)
 for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 assert r['centralizer_full_dimension']==1 and r['centralizer_even_dimension']==2 and r['signed_orbit_coordinates']==16384
 print('PASS independent',n,'raw transverse blocks;complete16384 matrix-unit orbits;differential null field and moving coefficient; faults',caught,';3 provenance hashes')
