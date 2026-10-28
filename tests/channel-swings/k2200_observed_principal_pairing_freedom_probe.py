#!/usr/bin/env python3
"""Exact controls for complete observed principal-pairing theorem.
Use --write to refresh the hash-bound native report.
"""
from fractions import Fraction as F
from itertools import product
from math import gcd,comb
from functools import reduce
import json,argparse,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
ETA=(1,)*7+(-1,)*7
OBS=(0,7,8,9);UN=tuple(i for i in range(14) if i not in OBS)
FULL=(1<<14)-1;ONE={0:F(1)};ZERO={}
def add(*xs):
 r={}
 for x in xs:
  for m,c in x.items():r[m]=r.get(m,0)+c
 return {m:c for m,c in r.items() if c}
def scale(x,c):return {m:v*c for m,v in x.items() if v*c}
def neg(x):return scale(x,-1)
def mm(x,y):
 r={}
 for a,c in x.items():
  for b,d in y.items():
   s=1
   for i in range(14):
    if a>>i&1:
     if (b&((1<<i)-1)).bit_count()%2:s=-s
     if b>>i&1:s*=ETA[i]
   r[a^b]=r.get(a^b,0)+s*c*d
 return {m:c for m,c in r.items() if c}
def star(x):return {m:c*(-1)**(m.bit_count()*(m.bit_count()+1)//2) for m,c in x.items()}
def blade(xs):
 r=ONE
 for i in xs:r=mm(r,{1<<i:F(1)})
 return r
G=[{1<<i:F(1)} for i in range(14)]
J=blade(range(14));W=scale(add(scale(ONE,3),neg(J)),F(1,2));WB=scale(add(scale(ONE,3),J),F(1,2))
GM=[mm(G[k],WB) for k in range(14)]
def raw(k,a,c):
 if a<14 and c<14 and len({a,k,c})==3:return scale(mm(blade((a,k,c)),W),ETA[a])
 if a==k and c==14:return ONE
 if a==14 and c==k:return scale(ONE,-ETA[k])
 return ZERO
def scalar(k,fault=None):
 a=[[F(0) for _ in range(15)] for _ in range(15)]
 for i in range(14):
  if i!=k:
   for j in range(14):
    if j!=i and j!=k:a[i][j]=F(1)
 a[k][14]=F(1);a[14][k]=F(1 if fault=='return_sign' else -1,2)
 return a
def eye():return [[F(int(i==j)) for j in range(15)] for i in range(15)]
def ma(a,b):return [[a[i][j]+b[i][j] for j in range(15)] for i in range(15)]
def ms(a,c):return [[v*c for v in row] for row in a]
def mt(a):return list(map(list,zip(*a)))
def mx(a,b):return [[sum(a[i][k]*b[k][j] for k in range(15)) for j in range(15)] for i in range(15)]
def mv(a,v):return [sum(a[i][k]*v[k] for k in range(15)) for i in range(15)]
ID=eye();FF=[[F((2 if i==14 else -1)*int(i==j)) for j in range(15)] for i in range(15)]
def algebra_controls(fault=None):
 cs={};ck=lambda k,v:cs.__setitem__(k,bool(v))
 matrices=[scalar(k,fault) for k in OBS]
 tr=[scale(G[a],ETA[a]) for a in range(14)]+[WB]
 ti=G+[scale(W,F(1,2))]
 for a in range(15):
  ck('coordinate_inverse_'+str(a),mm(tr[a],ti[a])==ONE and mm(ti[a],tr[a])==ONE)
  ck('normalized_form_'+str(a),scale(mm(star(tr[a]),tr[a]),ETA[a] if a<14 else 1)==scale(ONE,-1 if a<14 else 2))
 for k,M in zip(OBS,matrices):
  for a in range(15):
   for c in range(15):ck(f'raw_normalization_{k}_{a}_{c}',mm(mm(ti[a],raw(k,a,c)),tr[c])==scale(GM[k],M[a][c]))
  ck('scalar_F_adjoint_'+str(k),mx(mt(M),FF)==mx(FF,M))
  sq=mx(M,M);proj=ms(mx(ma(sq,ms(ID,-144)),ma(sq,ms(ID,-1))),F(4,866 if fault=='projector_denominator' else 867))
  want=[[F(int(i==j and i in(k,14))) for j in range(15)] for i in range(15)]
  ck('spectral_plane_'+str(k),proj==want)
  ck('scalar_spectral_polynomial_'+str(k),mx(mx(ma(M,ms(ID,-12)),ma(M,ID)),ma(sq,ms(ID,F(1,2))))==ms(ID,0))
  for l,L in zip(OBS,matrices):
   if l!=k:ck(f'other_symbol_exits_plane_{k}_{l}',all(L[a][c]==0 for a in(k,14) for c in(k,14)))
 pv=[[F(int(a==c))-F(1,10) if a in UN and c in UN else F(0) for c in range(15)] for a in range(15)]
 ck('V_rank9_trace',sum(pv[a][a] for a in range(15))==9)
 ck('V_projector',mx(pv,pv)==pv)
 ck('V_F_orthogonal',mx(mt(pv),FF)==mx(FF,pv))
 ck('V_joint_minus1',all(mx(M,pv)==ms(pv,-1) and mx(pv,M)==ms(pv,-1) for M in matrices))
 def e(i):return [F(int(j==i)) for j in range(15)]
 ck('auxiliary_cyclic_observed',all(mv(M,e(14))==e(k) for k,M in zip(OBS,matrices)))
 n=[mv(matrices[1],e(0))[a]-e(8)[a]-e(9)[a] for a in range(15)]
 ck('auxiliary_cyclic_normal_sum',n==[F(int(a in UN)) for a in range(15)])
 ck('plane_intersection_auxiliary',set.intersection(*(set((k,14)) for k in OBS))=={14})
 for k in OBS:
  ck('Gamma_B_skew_'+str(k),star(GM[k])==neg(GM[k]))
  for l in OBS:ck(f'Gamma_clifford_{k}_{l}',add(mm(GM[k],GM[l]),mm(GM[l],GM[k]))==scale(ONE,4*ETA[k]*int(k==l)))
 # Exact parity census over ALL16384 original basis blades.
 count={x:0 for x in product((1,-1),repeat=4)};central=[]
 for m in range(1<<14):
  r=m.bit_count();char=tuple((-1)**(r-((m>>k)&1)) for k in OBS)
  count[char]+=1
  if all(v==1 for v in char[:3 if fault=='omit_fourth_character' else 4]):central.append(m)
 ck('all16_character_dimensions',set(count.values())=={1024})
 ck('centralizer_dimension1024',len(central)==1024)
 selfadj=skew=0;commutes=True;adjoints=True
 for m in central:
  r=m.bit_count();z={m:F(1)} if r%2==0 else mm({m:F(1)},WB)
  sig=(-1)**(r*(r+(3 if fault=='adjoint_degree' else 1))//2)
  selfadj+=sig==1;skew+=sig==-1
  commutes &= all(mm(z,GM[k])==mm(GM[k],z) for k in OBS)
  adjoints &=star(z)==scale(z,sig)
 ck('every_adapted_centralizer_blade',commutes);ck('every_adapted_adjoint_sign',adjoints)
 ck('adjoint_dimensions496_528',(selfadj,skew)==(496,528))
 ck('binomial_selfadjoint_count',sum(comb(10,r) for r in(0,4,8,3,7))==496)
 ck('full_bilinear_dimension',82*1024==83968)
 ck('full_symmetric_dimension',46*496+36*528==41824)
 ck('full_antisymmetric_dimension',46*528+36*496==42144)
 z=blade((1,2,3,4));xx=add(scale(ONE,2),z);xi=scale(add(scale(ONE,2),neg(z)),F(1,3))
 ck('noncopy_witness_selfadjoint',star(z)==z)
 ck('noncopy_witness_involution',mm(z,z)==ONE)
 ck('noncopy_witness_compatible',all(mm(z,GM[k])==mm(GM[k],z) for k in OBS))
 ck('noncopy_witness_inverse',mm(xx,xi)==ONE and mm(xi,xx)==ONE)
 ck('noncopy_witness_trace_balance',mm(mm(G[1],z),G[1])==neg(z))
 ck('degenerate_rank_and_inertia',9*64+6*128==1344 and 1344//2==672)
 ck('antiisometry_gamma0',star(GM[0])==neg(GM[0]) and mm(GM[0],GM[0])==scale(ONE,2))
 chars=[tuple(1 if k==l else -1 for l in OBS) for k in OBS]
 ck('four_derivative_characters_distinct',len(set(chars))==4)
 for k in OBS:
  ck('actual_derivative_character_'+str(k),all(mm(GM[k],GM[l])==scale(mm(GM[l],GM[k]),1 if k==l else -1) for l in OBS))
 return cs
# Independent exact integer elimination of L M=epsilon M^T L with L^T=sign L.
def norm(r):
 r={k:v for k,v in r.items() if v}
 if not r:return r
 g=reduce(gcd,map(abs,r.values()));g*=1 if r[min(r)]>0 else -1
 return {k:v//g for k,v in r.items()}
def eliminate(signs,sym):
 pairs=[(i,j) for i in range(15) for j in range(i if sym==1 else i+1,15)];lookup={p:q for q,p in enumerate(pairs)}
 def term(i,j):return (lookup.get((i,j)),1) if i<=j else (lookup.get((j,i)),sym)
 piv={}
 for k,eps in zip(OBS,signs):
  M=[[int(2*v) for v in row] for row in scalar(k)]
  for i in range(15):
   for j in range(15):
    r={}
    for t in range(15):
     if M[t][j]:
      q,s=term(i,t)
      if q is not None:r[q]=r.get(q,0)+s*M[t][j]
     if M[t][i]:
      q,s=term(t,j)
      if q is not None:r[q]=r.get(q,0)-eps*s*M[t][i]
    r=norm(r)
    while r:
     p=min(r)
     if p not in piv:piv[p]=r;break
     old=piv[p];a=r[p];b=old[p]
     r=norm({q:b*r.get(q,0)-a*old.get(q,0) for q in r.keys()|old.keys()})
 return len(pairs)-len(piv)
def main():
 parser=argparse.ArgumentParser();parser.add_argument("--write",action="store_true");args=parser.parse_args()
 cs=algebra_controls();assert all(cs.values()),[k for k,v in cs.items() if not v]
 rows=[]
 for chars in product((1,-1),repeat=4):
  dims=(eliminate(chars,1),eliminate(chars,-1));expect=(46,36) if all(x==1 for x in chars) else (0,0)
  assert dims==expect,(chars,dims);rows.append(dict(character=list(chars),scalar_symmetric=dims[0],scalar_skew=dims[1]))
 faults={}
 for f in('return_sign','projector_denominator','omit_fourth_character','adjoint_degree'):
  bad=[k for k,v in algebra_controls(f).items() if not v];assert bad,('undetected',f);faults[f]=dict(count=len(bad),examples=bad[:3])
 deps=['explorations/conditional-build/k2200-observed-principal-pairing-freedom-2026-10-28.md','explorations/conditional-build/k2021-common-degree-dual-operator-2026-10-24.md','explorations/conditional-build/k2034-observed-principal-forms-2026-10-24.md','explorations/conditional-build/k2199-degree-dual-construction-boundary-2026-10-28.md']
 report=dict(result_id='K2200',status='conditional_complete_observed_pairing_classification',checks=cs,character_systems=rows,fault_failures=faults,dimensions=dict(bilinear=83968,symmetric=41824,antisymmetric=42144),dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),evidence_kinds='Universal all-character scalar-intertwiner proof, original raw-block reconstruction, complete adapted-blade census, independent exact scalar elimination and genuine mutations. No physical pairing selection or positive evolution conclusion.')
 dst=ROOT/'lab/process/k2200-observed-principal-pairing-freedom.json'
 if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(dst.read_text())==report
 print(json.dumps(dict(result='K2200',controls=len(cs),scalar_systems=2*len(rows),faults=len(faults))))
if __name__=='__main__':main()
