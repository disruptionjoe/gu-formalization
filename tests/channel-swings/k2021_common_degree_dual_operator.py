"""Exact full-carrier common density dual and moving-map Green identity.

Sparse rational arithmetic; no floating ranks or source-adjoint identification.
"""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,hashlib,argparse
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k2021-common-degree-dual-operator.json'
def add(*terms):
 z={}
 for c,a in terms:
  for ij,v in a.items():z[ij]=z.get(ij,F(0))+c*v
 return {ij:v for ij,v in z.items() if v}
def mul(a,b):
 rows={}
 for (i,j),v in b.items():rows.setdefault(i,[]).append((j,v))
 z={}
 for (i,k),v in a.items():
  for j,w in rows.get(k,[]):z[i,j]=z.get((i,j),F(0))+v*w
 return {ij:v for ij,v in z.items() if v}
def tr(a):return {(j,i):v for (i,j),v in a.items()}
def eye(n):return {(i,i):F(1) for i in range(n)}
I=eye(128);ETA=[1]*7+[-1]*7
@lru_cache(None)
def gamma(k):
 z={};j=k%7;mask=1<<(6-j)
 for col in range(128):
  s=(-1)**((col>>(7-j)).bit_count())
  if k>=7:s*=1 if col&mask else -1
  z[col^mask,col]=F(s)
 return z
@lru_cache(None)
def blade(ks):
 a=I
 for k in ks:a=mul(a,gamma(k))
 return a
J=blade(tuple(range(14)));B=blade(tuple(range(7,14)));W=add((F(3,2),I),(F(-1,2),J))
def blockdiag(blocks):
 return {(128*b+i,128*b+j):v for b,a in enumerate(blocks) for (i,j),v in a.items()}
H=blockdiag([add((e,B)) for e in ETA]+[B]);JJ=blockdiag([J]*15);II=eye(1920)
@lru_cache(None)
def raw(k):
 z={}
 for r in range(14):
  for c in range(14):
   if r!=k and c not in [r,k]:
    a=mul(blade((r,k,c)),W)
    z.update({(128*r+i,128*c+j):ETA[r]*v for (i,j),v in a.items()})
  if r==k:z.update({(128*r+i,1792+i):F(1) for i in range(128)})
 z.update({(1792+i,128*k+i):F(-ETA[k]) for i in range(128)})
 return z
def data(x):
 q=add((1,gamma(0)),(x,gamma(7)));qi=add((1/(1-x*x),q))
 c=blockdiag([I]*14+[q]);ci=blockdiag([I]*14+[qi]);cp=blockdiag([{}]*14+[gamma(7)])
 return c,ci,cp

def produce():
 checks={};ck=lambda k,v: checks.__setitem__(k,bool(v))
 ck('split_symmetric_involution',tr(B)==B and mul(B,B)==I and not add((1,B),(1,I))=={})
 ck('opposite_half',not add((1,B),(-1,I))=={} and add((1,mul(B,J)),(1,mul(J,B)))=={})
 for i in range(14):
  ck(f'gamma_B_skew_{i}',add((1,mul(tr(gamma(i)),B)),(1,mul(B,gamma(i))))=={})
  for j in range(14):ck(f'Clifford_{i}_{j}',add((1,mul(gamma(i),gamma(j))),(1,mul(gamma(j),gamma(i))),(-2*ETA[i] if i==j else 0,I))=={})
  ck(f'raw_green_{i}',add((1,mul(tr(raw(i)),H)),(1,mul(H,raw(i))))=={})
 samples=[]
 for x in [F(0),F(1,3),F(-2,5),F(3,4)]:
  c,ci,cp=data(x);h=mul(mul(tr(c),H),c);hp=add((2,h),(1,mul(mul(tr(cp),H),c)),(1,mul(mul(tr(c),H),cp)))
  ck(f'inverse_{x}',mul(c,ci)==II and mul(ci,c)==II)
  ck(f'common_symmetric_{x}',h==tr(h))
  ck(f'zero_degree_form_{x}',{(i-1792,j-1792):v for (i,j),v in h.items() if i>=1792}==add((-(1-x*x),B)))
  kk=mul(mul(ci,raw(7)),add((1,cp),(1,c)))
  ts=[]
  for k in range(14):
   a=mul(mul(ci,raw(k)),c);ss=mul(h,a);ts.append(ss)
   ck(f'principal_halves_{x}_{k}',mul(ss,JJ)==mul(JJ,ss))
   ck(f'principal_pairing_{x}_{k}',ss==add((-1,tr(ss))))
  ds=add((2,ts[7]),(1,mul(mul(tr(cp),H),mul(raw(7),c))),(1,mul(mul(tr(c),H),mul(raw(7),cp))))
  t0=mul(h,kk)
  ck(f'full_Green_{x}',add((1,t0),(-1,tr(t0)),(-1,ds))=={})
  ck(f'lower_order_halves_{x}',mul(t0,JJ)==mul(JJ,t0))
  # True fault inputs, evaluated against the same Green equation.
  no_q=mul(mul(tr(c),H),mul(raw(7),c))
  no_density=mul(mul(tr(c),H),mul(raw(7),cp))
  ck(f'omitted_q_derivative_rejected_{x}',bool(add((1,no_q),(-1,tr(no_q)),(-1,ds))))
  ck(f'omitted_density_rejected_{x}',bool(add((1,no_density),(-1,tr(no_density)),(-1,ds))))
  samples.append(dict(x=str(x),q_squared=str(1-x*x),green_entries=len(t0),principal_entries=sum(map(len,ts))))
 # Constant q gamma0: row duals R1=eta B and R0=q^t B, C1=I,C0=q.
 c,ci,_=data(F(0));r=mul(tr(c),H);ck('row_column_common_pairing',mul(r,c)==mul(mul(tr(c),H),c))
 ck('null_covector_singular',mul(add((1,gamma(0)),(1,gamma(7))),add((1,gamma(0)),(1,gamma(7))))=={})
 assert all(checks.values()),[k for k,v in checks.items() if not v]
 inputs=['tests/channel-swings/k1951_coordinated_zero_southeast_principal.py','lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md','explorations/k77-wave2-source-sign-shiab-duality-reconciliation-2026-08-04.md']
 return dict(result_id='K2021',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',checks=checks,samples=samples,carrier_dimension=1920,pairing_inertia=[960,960],scope='Local conditional common density dual and formal adjoint, with arbitrary supplied nowhere-null q and positive density. No source selection, positive physical state, global domain or GU verdict.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs})
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');a=ap.parse_args();z=produce()
 if a.write:OUT.write_text(json.dumps(z,indent=2)+'\n')
 else:assert z==json.loads(OUT.read_text())
 print('PASS K2021',len(z['checks']),'exact identity and fault controls')
