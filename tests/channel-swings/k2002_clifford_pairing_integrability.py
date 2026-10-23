"""Exact covariant differential trace certificate for the fixed raw pairing PDE."""
from fractions import Fraction as F
from pathlib import Path
from itertools import product as cart
import argparse,json,hashlib
import sympy as sp
from k1976_general_pairing_transport import setup,enc
from k1979_multicoordinate_symmetric_pairing import right
from k1970_weighted_adjoint_mass_completion_probe import product,plus,transpose
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k2002-clifford-pairing-integrability.json'
GROUPS=[[0],list(range(1,7)),[7,8,9],[10,11,12,13]]
REP=[0,1,7,10]
WEIGHTS=[F(1),F(-4,9),F(1),F(-4,9)]
def gammas():
 out=[]
 for k in range(14):
  g={}
  for j in range(128):
   bit=1<<(6-k%7);v=(-1)**((j>>(7-k%7)).bit_count())
   if k>=7:v*=1 if j&bit else -1
   g[j^bit,j]=F(v)
  out.append(g)
 return out

def projection(A,basis):
 return [sum(v*A.get(ij,F(0)) for ij,v in b.items())/128 for b in basis]

def reduced(sign):
 I,V,J,T,inv,O=setup();gam=gammas();X=product(inv,gam[0]);base=[]
 for mask in range(16):
  z=I
  for k in range(4):
   if mask>>k&1:z=product(z,gam[REP[k]])
  base.append(z)
 basis=base+[product(V,z) for z in base]
 symidx=[i for i,b in enumerate(basis) if b==transpose(b)]
 assert len(symidx)==20
 assert [[sum(v*b.get(ij,F(0)) for ij,v in a.items()) for b in basis] for a in basis]==[[F(128*(i==j)) for j in range(32)] for i in range(32)]
 cols=[]
 for k,a in enumerate(WEIGHTS):cols.append([projection({ij:a*v for ij,v in product(basis[z],gam[REP[k]]).items()},basis) for z in symidx])
 const=[projection({ij:-v for ij,v in product(right(basis[z],J,T,O,sign),X).items()},basis) for z in symidx]
 # Invariance is verified in every raw entry, not inferred from projections.
 for z in range(32):
  q=product(right(basis[z],J,T,O,sign),X);cs=projection(q,basis);back={}
  for c,b in zip(cs,basis):back=plus(back,b,c)
  assert q==back
 for k in range(14):
  a=F(1) if k in GROUPS[0]+GROUPS[2] else F(-4,9)
  assert product(J[k],X)=={ij:(1 if k<7 else -1)*a*v for ij,v in gam[k].items()}
 assert product(T,X)==plus({ij:-F(3,4)*v for ij,v in I.items()},V,-F(5,4))
 return basis,symidx,cols,const,X

def certificate(sign,degree):
 basis,sy,cols,const,X=reduced(sign);cand=[]
 for r in range(32):
  for ex in cart(range(degree+1),repeat=4):
   if sum(ex)<=degree and all(ex[k]%2==((r%16)>>k&1) for k in range(1,4)):cand.append((r,ex))
 rows={}
 for z in range(len(sy)):
  for c,(r,ex) in enumerate(cand):
   for value,shift in [(const[z][r],None)]+[(cols[k][z][r],k) for k in range(4)]:
    if not value:continue
    xp=list(ex)
    if shift is not None:xp[shift]+=1
    key=(z,tuple(xp));rows.setdefault(key,{})[c]=sp.Rational(value)
 keys=sorted(rows);ri={k:i for i,k in enumerate(keys)}
 A=sp.MutableSparseMatrix(len(keys),len(cand),{(ri[k],c):v for k,row in rows.items() for c,v in row.items()});b=sp.zeros(len(keys),1);b[ri[(0,(0,0,0,0))]]=1
 try:sol,pars=A.gauss_jordan_solve(b)
 except ValueError:return None
 sol=sol.subs({v:0 for v in pars});assert A*sol==b
 terms=[[r,list(ex),str(sol[c])] for c,(r,ex) in enumerate(cand) if sol[c]]
 return dict(sign=sign,degree=degree,equations=A.rows,unknowns=A.cols,terms=terms,symmetric_basis_indices=sy)

def produce():
 families=[]
 for sign in [-1,1]:
  assert certificate(sign,2) is None
  c=certificate(sign,4);assert c and len(c['terms'])==112;families.append(c)
 inputs=['tests/channel-swings/k1976_general_pairing_transport.py','tests/channel-swings/k1979_multicoordinate_symmetric_pairing.py','lab/process/k1951-coordinated-zero-southeast-principal.json','lab/process/k1967-paired-raw-coefficient-observation.json']
 return dict(result_id='K2002',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',scope='Every real symmetric distributional solution of the unchanged raw pairing PDE on any open set has trace zero. Hence nonzero PSD/NSD solutions and local definite pairings are excluded, both signs. No source-selected pairing or GU verdict.',groups=GROUPS,representatives=REP,weights=list(map(str,WEIGHTS)),basis='ordered products gamma0,gamma1,gamma7,gamma10 for masks0..15, then V times those; gamma0 fixed in covariant lift',right_transform='X=J0^-1 gamma0; Jk X=eta_k a_k gamma_k; T X=-(3I+5V)/4',families=families,inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs})
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();r=produce()
 if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text())
 print('PASS K2002: two degree4 trace certificates,318 equations/280 unknowns/112 terms each; degree2 covariant ansatz inconsistent')
