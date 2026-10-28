#!/usr/bin/env python3
"""Exact sparse Clifford closure, original-return transfer and spectral controls."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from itertools import combinations
from fractions import Fraction as F
import json,hashlib,argparse
import sympy as S
import k2206_changed_raw_mass_construction_probe as o
ROOT=Path(__file__).resolve().parents[2]
add,mul,scale=o.add,o.mul,o.scale
G,J,I,Z=o.G,o.J,o.ONE,o.ZERO
O,U=o.OBS,o.UN
B={(a,b):o.blade((a,b)) for a,b in combinations(O,2)}
P={a:mul(G[a],J) for a in O}
Q=o.blade(O);C={a:mul(G[0],G[a]) for a in O[1:]}
def comm(a,b):return add(mul(a,b),scale(mul(b,a),-1))
def rank(xs):
 masks=sorted(set().union(*(set(x) for x in xs)))
 return S.Matrix([[x.get(m,0) for x in xs] for m in masks]).rank()
def controls(fault=None):
 cs={}
 def ck(k,v):cs[k]=bool(v)
 basis=list(B.values())+list(P.values());support=set().union(*(set(x) for x in basis))
 ck('dimension10',rank(basis)==10)
 central=[m for m in range(1<<14) if all((m.bit_count()-((m>>r)&1))%2==0 for r in U)]
 skew_central=[m for m in central if (m.bit_count()*(m.bit_count()+1)//2)%2]
 ck('normal_commutant16',len(central)==16)
 ck('maximal_B_skew_commutant',set(skew_central)==support)
 normal_supports=[set().union(*(set(mul(x,G[r])) for x in basis)) for r in U]
 ck('full14_bottom_intersection_zero',not set.intersection(*normal_supports))
 ck('normal_supports_pairwise_disjoint',all(not (a&b) for a,b in combinations(normal_supports,2)))
 for i,x in enumerate(basis):
  ck('star_'+str(i),o.star(x)==scale(x,-1))
  for r in U:ck(f'normal_{i}_{r}',comm(x,G[r])==Z)
  for j,y in enumerate(basis):ck(f'closure_{i}_{j}',set(comm(x,y))<=support)
 for (a,b),bb in B.items():
  ck(f'PP_{a}_{b}',comm(P[a],P[b])==scale(bb,2 if fault=='curvature_sign' else -2))
  for c in O:ck(f'BP_{a}_{b}_{c}',comm(bb,P[c])==add(scale(P[a],2*o.ETA[b]*int(b==c)),scale(P[b],-2*o.ETA[a]*int(a==c))))
 for j in O[1:]:ck('generated_'+str(j),comm(B[0,j],P[0])==scale(P[j],-2))
 # Check the same original raw lower return, all fifteen output rows on a
 # basis of the sum-zero normal tuples; no independently fitted adjoint.
 def rx(k,a,c,x):
  return mul(x,o.raw(k,a,c)) if fault=='coefficient_order' else mul(o.raw(k,a,c),x)
 tr=[scale(G[k],o.ETA[k]) for k in range(14)]+[o.WB]
 inv=G+[scale(o.W,F(1,2))];images=[];odd=[];even=[]
 for k in O:
  for bi,x in enumerate(basis):
   n=mul(mul(G[0],G[k]),x);images.append(n);(even if bi<6 else odd).append(n)
   for c in U[1:]:
    for a in range(15):
     lhs=add(mul(mul(inv[a],rx(k,a,c,x)),tr[c]),scale(mul(mul(inv[a],rx(k,a,U[0],x)),tr[U[0]]),-1))
     # D0 restricted to V is -gamma0 Wbar; test K=D0*N.
     rhs=scale(mul(mul(G[0],o.WB),n),-int(a==c)+int(a==U[0]))
     ck(f'raw_{k}_{bi}_{c}_{a}',lhs==rhs)
 ck('even_image8',rank(even)==8);ck('odd_image7',rank(odd)==7)
 ck('full_image15',rank(images)==15)
 ck('symmetric_defect10',rank([add(x,o.transpose(x)) for x in images])==10)
 skew=[Q]+[mul(Q,C[j]) for j in O[1:]]+[P[0]]
 ck('conservative_image5',rank(skew)==5 and all(add(x,o.transpose(x))==Z for x in skew))
 # Every symmetric e has only its eta trace; independent symmetric basis.
 for a,b in combinations(O,2):
  n=add(mul(mul(G[0],G[a]),P[b]),mul(mul(G[0],G[b]),P[a]))
  ck(f'symmetric_offdiag_{a}_{b}',n==Z)
 for a in O:ck('diagonal_'+str(a),mul(mul(G[0],G[a]),P[a])==scale(P[0],o.ETA[a]))
 ck('original_bottom_return_off_sector',o.raw(0,14,0)==scale(I,-1) and mul(o.raw(0,14,0),P[0])==scale(P[0],-1))
 ck('flat_mass',mul(mul(G[0],G[0]),P[0])==P[0])
 ck('invisible_curved',add(mul(mul(G[0],G[0]),P[0]),mul(mul(G[0],G[7]),P[7]))==Z and comm(P[0],P[7])!=Z)
 ck('noncovariant_fixed_principal',comm(P[0],C[7])!=Z)
 ck('volume_square',mul(Q,Q)==scale(I,-1))
 ck('mass_square',mul(P[0],P[0])==scale(I,-1))
 ck('mass_volume_anticommute',add(mul(P[0],Q),mul(Q,P[0]))==Z)
 for j in O[1:]:
  ck('Q_C_'+str(j),comm(Q,C[j])==Z)
  ck('P_C_'+str(j),add(mul(P[0],C[j]),mul(C[j],P[0]))==Z)
 # Complex Clifford multiplication represents Hermitian S=-iQ,M=-iP0.
 si=scale(Q,-S.I);mi=scale(P[0],-S.I);cn=C[7];t=mul(si,cn)
 for tau in [-1,1]:
  proj=scale(add(I,scale(t,tau)),F(1,2))
  ck('T_projector_'+str(tau),mul(proj,proj)==proj)
  ck('T_mass_commutes_'+str(tau),comm(t,mi)==Z)
  for r,c,b,m in [(2,3,5,7),(0,0,2,2),(-3,3,5,4)]:
   h=add(scale(cn,r),scale(si,c),scale(t,b),scale(mi,m))
   shifted=add(h,scale(I,-tau*b))
   rhs=((r+tau*c)**2+m*m)*(-1 if fault=='mass_sign' else 1)
   anti=mul(cn,mi)
   ck(f'spectral_pairing_{tau}_{r}_{c}_{b}_{m}',comm(anti,t)==Z and add(mul(anti,add(scale(cn,r+tau*c),scale(mi,m))),mul(add(scale(cn,r+tau*c),scale(mi,m)),anti))==Z and mul(anti,anti)==scale(I,-1))
   ck(f'spectrum_{tau}_{r}_{c}_{b}_{m}',mul(mul(shifted,shifted),proj)==scale(proj,rhs))
 # Actual gap crossing with b>=m, including equality, on the parallel ray.
 for b,m,q in [(5,3,4),(2,2,0)]:
  r=-7+q;tau=1;h=add(scale(cn,r),scale(si,7),scale(t,b),scale(mi,m))
  proj=scale(add(I,t),F(1,2));v=mul(add(h,scale(I,-2*b)),proj)
  ck(f'zero_mode_{b}_{m}',v!=Z and mul(h,v)==Z)
 return cs

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
 cs=controls();assert all(cs.values()),[k for k,v in cs.items() if not v]
 faults={}
 for f in ['curvature_sign','coefficient_order','mass_sign']:
  bad=controls(f);faults[f]=[k for k,v in bad.items() if not v];assert faults[f],f
 deps=['tests/channel-swings/k2206_changed_raw_mass_construction_probe.py','explorations/conditional-build/k2206-changed-raw-mass-construction-2026-10-28.md','explorations/conditional-build/k2209-spin-common-return-2026-10-28.md','explorations/conditional-build/k2212-mass-connection-algebra-2026-10-28.md']
 report=dict(result_id='K2212',status='conditional_exact_connection_closure_and_gap',controls=len(cs),checks=cs,fault_failures=faults,dimensions={'algebra':10,'full14_coefficients':140,'invariant_coefficients':40,'image':15,'kernel':25,'conservative_coefficients':30,'conservative_image':5},gap='max(abs(m)-norm(b),0)',dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),evidence_kinds='Universal Lie/current/spectrum proof plus sparse exact original-row, rank and spectral controls; no physical gauge or action selection.')
 dst=ROOT/'lab/process/k2212-mass-connection-algebra.json'
 if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(dst.read_text())==report,'report drift'
 print(json.dumps({'result':'K2212','controls':len(cs),'faults':{k:len(v) for k,v in faults.items()}}))
if __name__=='__main__':main()
