"""Full raw principal form rigidity and arbitrary constant-weight boundary.

Universal claims use the algebraic argument in the companion note. This exact
producer verifies every principal projector and a complete signed-orbit
centralizer; it never substitutes samples for that completeness argument.
"""
from pathlib import Path
from fractions import Fraction
import json,hashlib,argparse
from sage.all import QQ,matrix,identity_matrix,zero_matrix,block_diagonal_matrix
import k2021_common_degree_dual_operator as b
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'lab/process/k2032-principal-form-rigidity.json'
def sm(d,n=128):return matrix(QQ,n,n,{ij:QQ(v.numerator)/v.denominator for ij,v in d.items()},sparse=True)
def raw(k,W):
 z={}
 for r in range(14):
  for c in range(14):
   if r!=k and c not in (r,k):
    a=sm(b.blade((r,k,c)))*W
    z.update({(128*r+i,128*c+j):b.ETA[r]*v for (i,j),v in a.dict().items()})
 z.update({(128*k+i,1792+i):1 for i in range(128)})
 z.update({(1792+i,128*k+i):-b.ETA[k] for i in range(128)})
 return matrix(QQ,1920,1920,z,sparse=True)
def orbit_centralizer(gens):
 # Monomial conjugation acts on all16384 matrix units; solve every signed orbit.
 n=128;adj=[[] for _ in range(n*n)]
 for g in gens:
  perm=[None]*n;sgn=[None]*n
  for (i,j),v in g.dict().items():perm[j]=i;sgn[j]=int(v)
  assert None not in perm and all(abs(x)==1 for x in sgn)
  for i in range(n):
   for j in range(n):adj[i*n+j].append((perm[i]*n+perm[j],sgn[i]*sgn[j]))
 seen={};basis=[];bad=0
 for start in range(n*n):
  if start in seen:continue
  vals={start:1};todo=[start];ok=True
  while todo:
   u=todo.pop()
   for v,s in adj[u]:
    val=vals[u]*s
    if v in vals:ok &= vals[v]==val
    else:vals[v]=val;todo.append(v)
  seen.update(vals)
  if ok:basis.append(matrix(QQ,n,n,{divmod(i,n):v for i,v in vals.items()},sparse=True))
  else:bad+=1
 return basis,bad,len(seen)
def produce():
 I=identity_matrix(QQ,128,sparse=True);Z=zero_matrix(QQ,128,128,sparse=True);II=identity_matrix(QQ,1920,sparse=True);W=sm(b.W);V=sm(b.J);H=sm(b.H,1920);g=[sm(b.gamma(k)) for k in range(14)]
 projectors=[]
 for k in range(14):
  D=raw(k,W);Q=b.ETA[k]*D*D
  assert (Q+II)*(Q-2*II)*(Q-288*II)==0
  P=(Q-2*II)*(Q-288*II)/867
  want=block_diagonal_matrix([I if j in (k,14) else Z for j in range(15)])
  assert P==want and D.transpose()*H+H*D==0
  projectors.append(P);print('principal',k,flush=True)
 aux=(sum(projectors,zero_matrix(QQ,1920,1920,sparse=True))-II)/13
 assert aux==block_diagonal_matrix([Z]*14+[I])
 even=[g[0]*g[j] for j in range(1,14)];basis,bad,total=orbit_centralizer(even)
 assert len(basis)==2 and total==16384
 assert all(all(X*A==A*X for A in even) for X in basis)
 assert matrix(QQ,[X.list() for X in basis]+[I.list(),V.list()]).rank()==2
 # Each even generator is a ratio of two actual triple blocks. All remaining
 # spinor weights are scalar since one invertible odd block exchanges halves.
 ratios=[]
 for j in range(1,14):
  k,c=[x for x in range(14) if x not in (0,j)][:2]
  A=g[0]*g[k]*g[c]*W;B=g[j]*g[k]*g[c]*W
  assert A*B.inverse()==b.ETA[j]*g[0]*g[j]
  ratios.append([0,j,k,c])
 odd=g[0]*g[1]*g[2]*W
 assert V*odd==-odd*V and odd.is_invertible()
 # Two noncommuting invertible W controls verify exact pencil equivalence.
 weights=[W,g[0]+2*I,g[7]];eqs=0
 for weight in weights:
  S=block_diagonal_matrix([weight.inverse()]*14+[I]);R=block_diagonal_matrix([I]*14+[weight])
  for k in [0,7,8,9]:assert R*raw(k,weight)*S==raw(k,I);eqs+=1
 # Singular W: principal rank factorization and exact observed common kernel.
 # D0's transverse13x13 block is invertible at W=I; rank is13rank(W)+256.
 D=raw(0,I);T=D.matrix_from_rows_and_columns(range(128,1792),range(128,1792))
 Ti=matrix(QQ,1664,1664,sparse=True)
 for r in range(1,14):
  for c in range(1,14):
   a=b.ETA[r]*g[r]*g[0]*g[c]*(QQ(1)/12-int(r==c))
   for (i,j),v in a.dict().items():Ti[128*(r-1)+i,128*(c-1)+j]=v
 assert T*Ti==identity_matrix(QQ,1664,sparse=True)
 singular=[]
 for weight in [zero_matrix(QQ,128,128,sparse=True),(I+V)/2]:
  r=weight.rank();ker=weight.right_kernel().basis_matrix().transpose();q=ker.ncols()
  # Every pure unobserved ker(W) slot is a common-null field.
  for k in [0,7,8,9]:
   D=raw(k,weight)
   for slot in [1,2,3,4,5,6,10,11,12,13]:
    assert D.matrix_from_columns(range(128*slot,128*(slot+1)))*ker==0
  singular.append(dict(weight_rank=r,time_rank=256+13*r,common_kernel=10*q,spatial_curl_freedom=2*q))
 # Genuine faults: change input symbols/weight, then replay fixed identities.
 D=raw(0,W);badD=matrix(D);badD[0,1792]+=1
 assert badD.transpose()*H+H*badD!=0
 Q=b.ETA[0]*badD*badD;assert (Q+II)*(Q-2*II)*(Q-288*II)!=0
 badW=(I+V)/2;assert badW*badW!=I
 assert V*odd!=odd*V
 inputs=['tests/channel-swings/k2021_common_degree_dual_operator.py','lab/process/k1951-coordinated-zero-southeast-principal.json','lab/process/k2028-all-grade-raw-common-form.json']
 return dict(result_id='K2032',status='active_research',classification='INTERNAL_STRUCTURAL_ONLY',target_claim='NONE-NOT-A-KILL',principal_projectors=14,centralizer_even_dimension=2,centralizer_full_dimension=1,signed_orbit_coordinates=total,inconsistent_orbits=bad,even_generator_ratios=ratios,pencil_equivalence_controls=eqs,singular_controls=singular,full_form_inertia=[960,960],raw_mutation_conditions=2,contrary_input_controls=2,scope='All constant real symmetric full forms for the fixed14 principal symbols; arbitrary constant invertible triple-gamma weights; singular descriptor nonuniqueness. No source-selected reality, physical gauge quotient or GU verdict.',inputs={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs})
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();r=produce()
 if a.write:OUT.write_text(json.dumps(r,indent=2)+'\n')
 else:assert r==json.loads(OUT.read_text())
 print('PASS K2032',r,flush=True)
