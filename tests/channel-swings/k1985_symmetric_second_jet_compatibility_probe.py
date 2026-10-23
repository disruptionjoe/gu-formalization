"""Separate raw-matrix replay of mixed derivatives and their positivity/residual bounds."""
from fractions import Fraction as F
from pathlib import Path
from collections import defaultdict
import json,hashlib
from k1979_multicoordinate_symmetric_pairing_probe import data,decode
from k1967_paired_raw_coefficient_observation_probe import mul,add,tr
ROOT=Path(__file__).resolve().parents[2]
def check(fault=None):
 r=json.loads((ROOT/'lab/process/k1985-symmetric-second-jet-compatibility.json').read_text());prior=json.loads((ROOT/'lab/process/k1979-multicoordinate-symmetric-pairing.json').read_text())['families'];I,V,J,T,O=data();n=0
 if fault=='coefficient':J[3]=add((2,J[3]))
 for f,old in zip(r['families'],prior):
  sign=-f['sign'] if fault=='mass' else f['sign'];H=list(map(decode,old['identity_first_jets']));S=defaultdict(dict)
  for k,l,i,j,v in f['second_jets']:S[k,l][i,j]=F(v);S[k,l][j,i]=F(v)
  if fault=='mixed':S[0,1][0,0]=S[0,1].get((0,0),F(0))+1
  def R(A):return add(*[((1 if k<7 else -1),mul(mul(tr(O[k]),A),J[k])) for k in range(14)],(-sign,mul(A,T)))
  def norm(A):return max(sum(abs(v) for (i,j),v in A.items() if i==row) for row in range(128))
  for k in range(14):
   lhs=add(*[((1 if l<7 else -1),mul(S.get(tuple(sorted((k,l))),{}),J[l])) for l in range(14)])
   assert lhs==R(H[k]),'coupled raw mixed derivative equation';n+=1
  A=sum(norm(h) for h in H);B=sum((F(1,2) if k==l else 1)*norm(s) for (k,l),s in S.items());C=sum((F(1,2) if k==l else 1)*norm(R(s)) for (k,l),s in S.items())
  radius=F(f['positive_cube_radius'])*(10000 if fault=='radius' else 1)
  assert radius*A+radius*radius*B<F(1,2),'positive Taylor neighborhood bound'
  assert [A,B,C]==list(map(F,[f['linear_norm_bound'],f['quadratic_norm_bound'],f['quadratic_residual_bound']])) and C>0
  for k in range(14):
   for l in range(k,14):
    s=S.get((k,l),{});assert s==tr(s);rr=R(s)
    for z in map(decode,old['cokernel']):assert sum(v*rr.get(ij,F(0)) for ij,v in z.items())==0,'second value compatibility';n+=1
  # Direct evaluation of polynomial PDE at an actual rational point, independent of symbol assembly.
  x=[radius*F((-1)**k,k+2) for k in range(14)];field=add((1,I),*[(x[k],h) for k,h in enumerate(H)],*[(x[k]*x[l]*(F(1,2) if k==l else 1),s) for (k,l),s in S.items()]);derivatives=[add((1,H[k]),*[(x[l],S.get(tuple(sorted((k,l))),{})) for l in range(14)]) for k in range(14)]
  actual=add(*[((1 if k<7 else -1),mul(h,J[k])) for k,h in enumerate(derivatives)],(-1,R(field)))
  expected=add(*[(-x[k]*x[l]*(F(1,2) if k==l else 1),R(s)) for (k,l),s in S.items()]);assert actual==expected,'Taylor residual identity';n+=3
 for p,h in r['inputs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 return n
if __name__=='__main__':
 n=check();caught=[]
 for f in ['coefficient','mass','mixed','radius']:
  try:check(f)
  except AssertionError as e:caught.append([f,str(e)])
  else:raise AssertionError('undetected mathematical fault '+f)
 print('PASS K1985 independent',n,'raw obligations;',caught)
