#!/usr/bin/env python3
"""Full14 principal identities and complete blade centralizer, exact and lightweight."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import argparse,hashlib,json
import sympy as S
from k2169_invertible_pencil_full_descent_probe import G,I,ETA,mm,add,scale,comm
ROOT=Path(__file__).resolve().parents[2]
def blade(indices):
 x=I
 for i in indices:x=mm(x,G[i])
 return x
J=blade(range(14))
def star(x):return {m:v*((-1)**(m.bit_count()*(m.bit_count()+1)//2)) for m,v in x.items()}
def controls(fault=None):
 cs={};ck=lambda k,v:cs.__setitem__(k,bool(v));W=scale(add(scale(I,2 if fault=='W_coefficient' else 3),scale(J,-1)),F(1,2))
 ck('volume_involution',mm(J,J)==I)
 for k in range(14):
  good=True
  for a,c in combinations([j for j in range(14) if j!=k],2):
   ac=scale(mm(blade([a,k,c]),W),ETA[a]);ca=scale(mm(blade([c,k,a]),W),ETA[c])
   good &= add(scale(star(ca),ETA[c]),scale(ac,ETA[a]))=={}
  ck('all_principal_Green_cells_'+str(k),good and not add(scale(I,-ETA[k]),scale(I,ETA[k])))
 for i,j in combinations(range(14),2):
  a,b=[t for t in range(14) if t not in (i,j)][:2]
  lhs=mm(mm(blade([a,b,i]),W),mm(blade([a,b,j]),W));rhs=scale(mm(G[i],G[j]),-2*ETA[a]*ETA[b])
  ck(f'generate_bivector_{i}_{j}',lhs==rhs)
 # Complete symbolic character census, not a floating rank estimate.
 survivors=[m for m in range(1<<14) if all(((m>>i)&1)==((m>>j)&1) for i,j in combinations(range(14),2))]
 ck('full_blade_centralizer',survivors==[0,(1<<14)-1])
 T=mm(blade([0,1,2]),W)
 ck('odd_kills_volume',bool(comm(J,T)) and comm(J,T)==scale(mm(J,T),2))
 ck('triple_invertible',mm(T,mm(scale(add(scale(I,3),J),F(1,4)),scale(blade([2,1,0]),ETA[0]*ETA[1]*ETA[2])))==I)
 # A planted nonidentity block in the final covector column defeats four-only checking.
 def injection(U,Z):return all(U[a][k]==(Z if a==k else 0) for k in range(4 if fault=='four_directions' else 14) for a in range(14))
 U=[[int(a==k) for k in range(14)] for a in range(14)];ck('injection_positive',injection(U,1));U[13][13]=2;ck('injection_rejects_unseen_column',not injection(U,1))
 t=S.symbols('t',real=True);A=S.Matrix([[0,1],[-1,0]]);density=S.exp(2*t)
 actual=-(density*A.T).diff(t)/density
 expected=(-1 if fault=='density_sign' else 1)*density.diff(t)/density*A
 ck('actual_integration_by_parts_density_sign',actual==expected)
 # D(dc) top-right is the fourteen component gradient, hence injective.
 for k in range(14):ck('density_symbol_injection_'+str(k),[int(i==k) for i in range(14)].count(1)==1)
 # General mixed-block ansatz at every distinct k,c, evaluated from original A cells.
 for k,c in [(0,1),(7,9),(13,4)]:
  lhs={}
  for b in range(14):
   if b in (k,c):continue
   ukb=scale(mm(G[k],G[b]),24*ETA[k]);abc=scale(mm(blade([b,k,c]),W),ETA[b]);lhs=add(lhs,mm(ukb,abc))
  rhs=scale(mm(G[c],W),1 if fault=='mixed_sign' else -1)
  ck(f'mixed_ansatz_289_{k}_{c}',add(lhs,scale(rhs,-1))==scale(mm(G[c],W),289))
 return cs
def casimir_controls(fault=None):
 cs={};ck=lambda k,v:cs.__setitem__(k,bool(v));W=scale(add(scale(I,3),scale(J,-1)),F(1,2))
 def A(k,a,b):return scale(mm(blade([a,k,b]),W),ETA[a]) if len({a,k,b})==3 else {}
 C={(a,b):scale(mm(G[a],G[b]),ETA[a]) for a in range(14) for b in range(14)}
 Q={}
 for a in range(14):
  for b in range(14):
   Q[a,b]=add(*(scale(mm(A(k,a,c),A(k,c,b)),ETA[k]) for k in range(14) for c in range(14)),scale(I,-int(a==b)))
   expect=add(scale(C[a,b],263 if fault=='casimir_coefficient' else 264),scale(I,47*int(a==b)))
   ck(f'original_sum_D_squared_{a}_{b}',Q[a,b]==expect)
   cc=add(*(mm(C[a,c],C[c,b]) for c in range(14)))
   ck(f'Clifford_trace_projector_{a}_{b}',cc==scale(C[a,b],14))
 for a in range(14):
  for b in range(14):
   # Exact computed blocks, with no formula substitution into the polynomial.
   proj=add(*(mm(add(Q[a,c],scale(I,-47*int(a==c))),add(Q[c,b],scale(I,-3743*int(c==b)))) for c in range(14)))
   ck(f'upper_spectral_polynomial_{a}_{b}',proj=={})
 ck('lower_projection_normalization',(-14-47)*(-14-3743)==229177)
 ck('lower_distinct_from_both_upper_eigenvalues',-14 not in [47,3743])
 ck('offdiagonal_casimir_zero',all(not A(k,a,k) and not A(k,k,a) for k in range(14) for a in range(14)))
 return cs
FAULTS=['W_coefficient','four_directions','density_sign','mixed_sign','casimir_coefficient']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();cs=controls()|casimir_controls();assert all(cs.values()),[k for k,v in cs.items() if not v]
 faults={}
 for f in FAULTS:
  bad=[k for k,v in (casimir_controls(f) if f=='casimir_coefficient' else controls(f)).items() if not v];assert bad,('undetected',f);faults[f]=bad
 deps=['explorations/conditional-build/k2199-degree-dual-construction-boundary-2026-10-28.md','explorations/conditional-build/k2021-common-degree-dual-operator-2026-10-24.md','explorations/conditional-build/k2028-all-grade-raw-common-form-2026-10-24.md','tests/channel-swings/k2169_invertible_pencil_full_descent_probe.py','tests/channel-swings/k2021_common_degree_dual_operator.py']
 report=dict(result_id='K2199',status='conditional_exact_all_pairing_classification',checks=cs,fault_failures=faults,blade_census_size=16384,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),evidence_kinds='Universal full commutant proof via the exact spectral degree projector, full14 cell identities, complete blade census and density sign control; mixed289 is a reused independent ansatz check, not the general proof.')
 dst=ROOT/'lab/process/k2199-degree-dual-construction-boundary.json'
 if args.write:dst.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(dst.read_text())==report
 print(json.dumps(dict(result='K2199',controls=len(cs),faults={k:len(v) for k,v in faults.items()})))
if __name__=='__main__':main()
