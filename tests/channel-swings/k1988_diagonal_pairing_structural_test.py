"""Exact full coordinate-diagonal constraint and quantitative mixing certificate."""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,hashlib
from k1976_general_pairing_transport import setup,norm,enc
from k1979_multicoordinate_symmetric_pairing import right
from k1970_weighted_adjoint_mass_completion_probe import transpose
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k1988-diagonal-pairing-structural-test.json'
def inverse(A):
 n=len(A);B=[list(r)+[F(i==j) for j in range(n)] for i,r in enumerate(A)]
 for k in range(n):
  j=next(i for i in range(k,n) if B[i][k]);B[k],B[j]=B[j],B[k];a=B[k][k];B[k]=[x/a for x in B[k]]
  for i in range(n):
   if i!=k and B[i][k]:
    a=B[i][k];B[i]=[x-a*y for x,y in zip(B[i],B[k])]
 return [r[n:] for r in B]
def produce():
 I,V,J,T,inv,O=setup();symbol=set().union(*(set(j) for j in J[:14]));families=[]
 for s in [-1,1]:
  cols=[right({(i,i):F(1)},J,T,O,s) for i in range(128)];slots=sorted(set().union(*(set(c) for c in cols))-symbol);assert len(slots)==128
  A=[[c.get(ij,F(0)) for c in cols] for ij in slots]
  # The actual incidence graph gives32 separate4x4 systems, not a dense rank calculation.
  pending=set(range(128));blocks=[];inverse_rows={}
  while pending:
   variables={min(pending)};rows=set()
   while True:
    nr={i for i,row in enumerate(A) if any(row[j] for j in variables)}
    nv={j for i in nr for j,v in enumerate(A[i]) if v}
    if nv==variables and nr==rows:break
    variables,rows=nv,nr
   assert len(variables)==len(rows)==4
   vs=sorted(variables);rs=sorted(rows);small=[[A[i][j] for j in vs] for i in rs];iv=inverse(small)
   for k,j in enumerate(vs):inverse_rows[j]={rs[l]:v for l,v in enumerate(iv[k]) if v}
   blocks.append(dict(variables=vs,slots=[list(slots[i]) for i in rs],matrix=[[str(v) for v in r] for r in small],inverse=[[str(v) for v in r] for r in iv]));pending-=variables
  for j,r in inverse_rows.items():
   assert [sum(v*A[i][k] for i,v in r.items()) for k in range(128)]==[F(k==j) for k in range(128)]
  ca=max(sum(abs(v) for v in r.values()) for r in inverse_rows.values());bj=sum(norm(transpose(o))*norm(j) for o,j in zip(O,J))+norm(T);der=[norm(j) for j in J[:14]]
  minidentity=max(abs(sum(row)) for row in A)
  families.append(dict(sign=s,unsupported_slots=[list(ij) for ij in slots],blocks=blocks,rank=128,inverse_row_norm=str(ca),zeroth_order_norm_bound=str(bj),derivative_norm_bounds=list(map(str,der)),identity_unsupported_max=str(minidentity),identity_derivative_lower_bound=str(minidentity/sum(der))))
 return dict(result_id='K1988',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',families=families,scope='Every C1 coordinate-diagonal field on the fixed raw128 core solving the unchanged14-coordinate PDE is zero, both signs. Quantitative off-diagonal value/derivative necessity for full fields; no exclusion of general symmetric local solutions or source pairing.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['tests/channel-swings/k1976_general_pairing_transport.py','tests/channel-swings/k1979_multicoordinate_symmetric_pairing.py','lab/process/k1985-symmetric-second-jet-compatibility.json']})
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();r=produce()
 if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text())
 print('PASS K1988',[(x['sign'],len(x['blocks']),x['inverse_row_norm'],x['identity_derivative_lower_bound']) for x in r['families']])
