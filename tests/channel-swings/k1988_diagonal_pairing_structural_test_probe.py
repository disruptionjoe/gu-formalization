"""Separate raw contraction and inverse verification; no import of K1988 producer."""
from pathlib import Path
from fractions import Fraction as F
import json,copy
from k1976_general_pairing_transport import setup
from k1970_weighted_adjoint_mass_completion_probe import product,transpose,plus
ROOT=Path(__file__).resolve().parents[2]
def check(d):
 I,V,J,T,inv,O=setup();allowed=set().union(*(set(j) for j in J[:14]));checks=0
 for f in d['families']:
  sign=f['sign'];seen=set();ca=F(0)
  for b in f['blocks']:
   variables=b['variables'];slots=list(map(tuple,b['slots']));A=[[F(v) for v in row] for row in b['matrix']];B=[[F(v) for v in row] for row in b['inverse']]
   assert not (set(slots)&allowed),'unsupported projection';seen.update(variables)
   for j,var in enumerate(variables):
    Q={(var,var):F(1)};raw={}
    for k in range(14):raw=plus(raw,product(product(transpose(O[k]),Q),J[k]),1 if k<7 else -1)
    raw=plus(raw,product(Q,T),-sign)
    assert [raw.get(ij,F(0)) for ij in slots]==[row[j] for row in A],'raw coefficient';checks+=1
   for i in range(4):
    for j in range(4):assert sum(B[i][k]*A[k][j] for k in range(4))==F(i==j),'inverse identity';checks+=1
   ca=max(ca,max(sum(abs(v) for v in row) for row in B))
  assert seen==set(range(128)) and ca==F(f['inverse_row_norm']),'complete cover'
  rownorm=lambda a:max([sum(abs(v) for (r,c),v in a.items() if r==i) for i in range(128)])
  jnorm=[rownorm(a) for a in J[:14]];rnorm=sum(rownorm(transpose(o))*rownorm(j) for o,j in zip(O,J))+rownorm(T)
  assert jnorm==list(map(F,f['derivative_norm_bounds'])) and rnorm==F(f['zeroth_order_norm_bound']),'norm constants'
  maxraw=max(abs(sum(map(F,r))) for b in f['blocks'] for r in b['matrix'])
  assert maxraw/sum(jnorm)==F(f['identity_derivative_lower_bound']),'derivative bound'
  # Independent positive first-jet controls: allowed off-diagonal mixing really repairs Q=I.
  jets=json.load(open(ROOT/'lab/process/k1979-multicoordinate-symmetric-pairing.json'))['families'];g=next(x for x in jets if x['sign']==sign)
  lhs={}
  for k,h in enumerate(g['identity_first_jets']):lhs=plus(lhs,product({(i,j):F(v) for i,j,v in h},J[k]),1 if k<7 else -1)
  rhs={}
  for k in range(14):rhs=plus(rhs,product(transpose(O[k]),J[k]),1 if k<7 else -1)
  rhs=plus(rhs,T,-sign);assert lhs==rhs,'full positive first-jet contrary control';checks+=1
 return checks
if __name__=='__main__':
 d=json.load(open(ROOT/'lab/process/k1988-diagonal-pairing-structural-test.json'));n=check(d);faults=[]
 for kind in ['coefficient','inverse','projection','norm']:
  bad=copy.deepcopy(d);f=bad['families'][0]
  if kind=='coefficient':f['blocks'][0]['matrix'][0][0]=str(F(f['blocks'][0]['matrix'][0][0])+1)
  if kind=='inverse':f['blocks'][0]['inverse'][0][0]=str(F(f['blocks'][0]['inverse'][0][0])+1)
  if kind=='projection':f['blocks'][0]['slots'][0]=list(next(iter(setup()[2][0])))
  if kind=='norm':f['identity_derivative_lower_bound']='1'
  try:check(bad)
  except AssertionError as e:faults.append((kind,str(e)))
  else:raise AssertionError('undetected '+kind)
 print('PASS K1988 independent',n,'raw/inverse/jet obligations; genuine faults',faults)
