"""Exact coupled symmetric second jets on the fixed K1979 pairing equation."""
from fractions import Fraction as F
from pathlib import Path
from collections import Counter,defaultdict
import json,hashlib,argparse
from k1976_general_pairing_transport import setup,norm
from k1979_multicoordinate_symmetric_pairing import right
from k1970_weighted_adjoint_mass_completion_probe import plus,product,transpose
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'lab/process/k1985-symmetric-second-jet-compatibility.json'

def construct():
 I,V,J,T,inv,O=setup();N=128;size=14*N*N
 maps=[{i:(j,v*(1 if k<7 else -1)) for (i,j),v in g.items()} for k,g in enumerate(J[:14])]
 def edges(k,l,i,j):
  z=[]
  for a,b in ([(l,k)] if k==l else [(l,k),(k,l)]):
   c,v=maps[b][j];z.append(((a*N+i)*N+c,v))
   if i!=j:
    c,v=maps[b][i];z.append(((a*N+j)*N+c,v))
  return z
 parent=list(range(size))
 def find(x):
  while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
  return x
 for k in range(14):
  for l in range(k,14):
   for i in range(N):
    for j in range(i,N):
     z=edges(k,l,i,j);a=find(z[0][0])
     for x,v in z[1:]:parent[find(x)]=a
 comp=[find(i) for i in range(size)]
 old=json.loads((ROOT/'lab/process/k1979-multicoordinate-symmetric-pairing.json').read_text())['families'];rhs=[]
 for f in old:
  q={}
  for k,h in enumerate(f['identity_first_jets']):
   for (i,j),v in right({(a,b):F(c) for a,b,c in h},J,T,O,f['sign']).items():q[(k*N+i)*N+j]=v
  rhs.append(q)
 needed={comp[k] for q in rhs for k in q};rows={i:{} for i in range(size) if comp[i] in needed};variables=[]
 for k in range(14):
  for l in range(k,14):
   for i in range(N):
    for j in range(i,N):
     z=edges(k,l,i,j)
     if z[0][0] not in rows:continue
     ix=len(variables);variables.append((k,l,i,j))
     assert all(comp[a]==comp[z[0][0]] for a,v in z)
     for a,v in z:rows[a][ix]=v
 piv={};eqrhs={}
 for ri,rr in rows.items():
  d=rr.copy();b=[q.get(ri,F(0)) for q in rhs]
  while d:
   k=min(d)
   if k not in piv:
    a=d[k];piv[k]={j:v/a for j,v in d.items()};eqrhs[k]=[v/a for v in b];break
   a=d[k]
   for j,v in piv[k].items():
    x=d.get(j,F(0))-a*v
    if x:d[j]=x
    else:d.pop(j,None)
   b=[x-a*y for x,y in zip(b,eqrhs[k])]
  else:assert not any(b),'incompatible second jet'
 sol=[{},{}]
 for k in sorted(piv,reverse=True):
  for n in range(2):
   v=eqrhs[k][n]-sum(a*sol[n].get(j,F(0)) for j,a in piv[k].items() if j!=k)
   if v:sol[n][k]=v
 for ri,rr in rows.items():
  for n in range(2):assert sum(v*sol[n].get(j,F(0)) for j,v in rr.items())==rhs[n].get(ri,F(0))
 families=[]
 for n,f in enumerate(old):
  H=[{(i,j):F(v) for i,j,v in h} for h in f['identity_first_jets']];S=defaultdict(dict)
  for vi,v in sol[n].items():
   k,l,i,j=variables[vi];S[k,l][i,j]=v;S[k,l][j,i]=v
  A=sum(norm(h) for h in H);B=sum((F(1,2) if k==l else 1)*norm(s) for (k,l),s in S.items());radius=1/(4*(1+A+B))
  C=sum((F(1,2) if k==l else 1)*norm(right(s,J,T,O,f['sign'])) for (k,l),s in S.items())
  assert radius*A+radius**2*B<F(1,2) and C>0
  Z=[{(i,j):F(v) for i,j,v in z} for z in f['cokernel']]
  for k in range(14):
   lhs={}
   for l in range(14):lhs=plus(lhs,product(S.get(tuple(sorted((k,l))),{}),J[l]),1 if l<7 else -1)
   assert lhs==right(H[k],J,T,O,f['sign'])
  for k in range(14):
   for l in range(k,14):
    rr=right(S.get((k,l),{}),J,T,O,f['sign'])
    assert all(not sum(v*rr.get(ij,F(0)) for ij,v in z.items()) for z in Z)
  families.append(dict(sign=f['sign'],second_jets=[[*variables[j],str(v)] for j,v in sorted(sol[n].items())],linear_norm_bound=str(A),quadratic_norm_bound=str(B),positive_cube_radius=str(radius),quadratic_residual_bound=str(C),differentiated_value_constraints=210))
 return dict(result_id='K1985',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',component_sizes={str(k):v for k,v in Counter(Counter(comp).values()).items()},selected_rows=len(rows),selected_columns=len(variables),selected_rank=len(piv),families=families,scope='Exact mixed symmetric second derivatives of the stored K1979 identity-value first jets, both signs. Positive quadratic Taylor field solves the PDE through linear order; nonzero quadratic defect remains. Necessary second-differentiated value constraints pass; no third-jet, analytic field, source pairing or global existence claim.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['lab/process/k1979-multicoordinate-symmetric-pairing.json','tests/channel-swings/k1976_general_pairing_transport.py','tests/channel-swings/k1979_multicoordinate_symmetric_pairing.py']})
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();r=construct()
 if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text())
 print('PASS K1985 exact selected symbol rank',r['selected_rank'],'and both coupled second jets')
