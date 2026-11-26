"""Exact native-symbol controls for the full-frozen nonlocal completion.

The written proof owns exponentials, two-sided Sobolev bounds and closed range.
No transfer to the variable-coefficient physical domain is asserted.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse,json
import source_action_deep_geometry as g
from source_action_deep_algebra import add,scale
from source_action_physical_probe import mul,gamma,contraction
from source_action_slice_completion_probe import (zero,vadd,vscale,column,covector,norm,sigma,inverse,readout,inject)

def connection_lower(i,v):
 z,nu=v
 return ([add(mul(g.spin[i],z[a]),*(scale(-g.Lambda[i][a][b],z[b])for b in range(14)))for a in range(14)],mul(g.spin[i],nu))

def reference_lower(v):
 return vadd(*(sigma(covector(i),connection_lower(i,v))for i in range(14)))

def displacement_lower(T,v):
 z,nu=v;sl=contraction(T,range(14))
 out=[add(mul(sl,z[a]),*(scale(-1/g.d[b],mul(gamma(b),mul(T[a],z[b])))for b in range(14)),mul(T[a],nu))for a in range(14)]
 return out,add(*(scale(1/g.d[a],mul(T[a],z[a]))for a in range(14)),scale(-Q(1,2),mul(sl,nu)))

def run():
 checks=0;z=covector(8);w=covector(4)
 assert norm(z)==Q(1,8) and norm(w)==-Q(1,16);checks+=1
 # Rational points on R^2=1+|eta|^2; no numerical square roots.
 examples=[([0,0,0,0],Q(1)),([2,2,0,0],Q(3)),([0,0,0,Q(3,4)],Q(5,4)),([2,0,0,2],Q(3))]
 rows=[]
 for eta,R in examples:
  eta=list(map(Q,eta));assert R*R==1+sum(e*e for e in eta);checks+=1
  xi=eta+[Q(0)]*10;xi[4]=8*R
  om2=8*(4*R*R-sum(eta[i]*eta[i]/g.d[i]for i in range(4)))
  assert om2>=24*R*R;checks+=1
  def K(v):return vscale(-1,inverse(z,sigma(xi,v)))
  for j in range(15):
   v=column(j);assert K(K(v))==vscale(om2,v);checks+=1
   assert vadd(sigma(z,K(v)),sigma(xi,v))==zero();checks+=1
  rows.append({'eta':list(map(str,eta)),'normal_frequency':str(8*R),'omega_squared':str(om2)})
 for j in range(5):
  expected=[{}for _ in range(5)];expected[j]={0:Q(1)}
  assert readout(inject(j))==expected;checks+=1
 # All constant lower matrices are covered by Az L=-C0. Replay actual
 # reference plus the two rational stationary centers as native controls;
 # the universal proof, not center substitution, covers the exact roots.
 data=json.loads((Path(__file__).resolve().parents[2]/'lab/process/source-action-deep-coefficients.json').read_text())
 for root in data['certified_roots']:
  T=[{}for _ in range(14)]
  for coeff,basis in zip(map(Q,root['coordinates']),data['basis']):
   for e,c,val in basis:
    a=int(e).bit_length()-1;T[a]=add(T[a],{int(c):coeff*Q(val)})
  for j in range(15):
   v=column(j);cv=vadd(reference_lower(v),displacement_lower(T,v));lv=vscale(-1,inverse(z,cv))
   assert vadd(sigma(z,lv),cv)==zero();checks+=1
  assert any(vadd(reference_lower(column(j)),displacement_lower(T,column(j)))!=zero()for j in range(15));checks+=1
 # Mutation: omitting the negative-normal injection destroys the uniform
 # real-normal spectrum for a spacelike observed frequency.
 xi=covector(0);assert -norm(xi)/norm(z)<0;checks+=1
 return {'controls':checks,'full_operator_columns':15,'complex_carrier_rank':1920,'literal_observed_rank':640,'normal_positive_index':8,'normal_negative_index':4,'frequency_controls':rows,'lower_terms':'actual reference plus both rational stationary centers checked; theorem applies to every constant lower matrix','scope':'exact full-frozen completion; norm/closed-range/PsiDO results have separate written proofs; no variable physical-domain transfer'}

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path);a=p.parse_args();s=json.dumps(run(),indent=2)+'\n'
 if a.output:a.output.write_text(s)
 else:print(s)
