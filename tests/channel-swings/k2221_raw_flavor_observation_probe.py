#!/usr/bin/env python3
"""Exact original-row lift, trace compatibility and local observation controls."""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
import argparse,json,hashlib
ROOT=Path(__file__).resolve().parents[2]
import k2206_changed_raw_mass_construction_probe as o
F=o.F; add=o.add; mul=o.mul; scale=o.scale; I=o.ONE; Z=o.ZERO
T=o.blade(o.UN); A=mul(o.G[0],o.J)
C={j:mul(o.G[0],o.G[j]) for j in o.OBS[1:]}
X={j:mul(C[j],T) for j in C}
def comm(a,b):return add(mul(a,b),scale(mul(b,a),-1))
def anti(a,b):return add(mul(a,b),mul(b,a))
def controls(fault=None):
 out={}
 def ck(k,v):out[k]=bool(v)
 ck('T_squared',mul(T,T)==scale(I,-1))
 ck('T_transpose',o.transpose(T)==scale(T,-1))
 ck('T_mass_commutes',comm(T,A)==Z)
 ck('mass_skew',o.transpose(A)==scale(A,-1))
 for j in C:
  ck(f'T_C_{j}',comm(T,C[j])==Z)
  ck(f'X_grade12_{j}',all(m.bit_count()==12 for m in X[j]))
  ck(f'X_skew_{j}',o.transpose(X[j])==scale(X[j],-1))
  ck(f'X_B_self_{j}',o.star(X[j])==X[j])
  ck(f'mass_X_anticommute_{j}',anti(A,X[j])==Z)
  for r in o.UN:
   xx=T if fault=='trace_lift' and j==7 else X[j]
   ck(f'trace_X_{j}_{r}',add(mul(o.star(xx),o.G[r]),mul(o.G[r],xx))==Z)
   ck(f'failed_direct_T_{j}_{r}',add(mul(o.star(T),o.G[r]),mul(o.G[r],T))!=Z)
 # Every connection component, not just the nonzero one.
 omega0=add(scale(A,F(2,3)),*(scale(X[j],v) for j,v in zip(C,[F(3,7),F(-5,11),F(2,13)])))
 defect=add(o.star(omega0),omega0)
 xxsum=add(*(scale(X[j],v) for j,v in zip(C,[F(3,7),F(-5,11),F(2,13)])))
 ck('fixed_B_mass_skew',o.star(A)==scale(A,-1))
 ck('fixed_B_defect',defect==scale(xxsum,2) and defect!=Z)
 ck('independent_lift_blades',len({next(iter(x)) for x in X.values()})==3)
 ck('defect_square_invertible',mul(defect,defect)==scale(I,-4*sum(v*v for v in [F(3,7),F(-5,11),F(2,13)])))
 gg=add(scale(I,F(3,5)),scale(A,F(4,5)));gi=o.star(gg)
 ck('B_unitary_frame',mul(gi,gg)==I)
 changed=add(mul(mul(gi,omega0),gg),A)
 ck('B_frame_defect_covariance',add(o.star(changed),changed)==mul(mul(gi,defect),gg))
 ck('B_frame_no_repair',add(o.star(changed),changed)!=Z)
 for k in range(14):
  om=omega0 if k==0 else Z
  for r in o.UN:ck(f'all14_trace_{k}_{r}',add(mul(o.star(om),o.G[r]),mul(o.G[r],om))==Z)
 tr=[scale(o.G[k],o.ETA[k]) for k in range(14)]+[o.WB]
 inv=o.G+[scale(o.W,F(1,2))]
 for j,xx in X.items():
  nn=xx if fault=='induced_sign' else scale(xx,-1)
  def entry(a,c):
   rr=o.raw(0,a,c,'raw_return_sign' if fault=='return_sign' else None)
   prod=mul(xx,rr) if fault=='coefficient_order' else mul(rr,xx)
   return mul(mul(inv[a],prod),tr[c])
  for c in o.UN[1:]:
   for a in range(15):
    lhs=add(entry(a,c),scale(entry(a,o.UN[0]),-1))
    rhs=scale(mul(mul(o.G[0],o.WB),nn),-int(a==c)+int(a==o.UN[0]))
    ck(f'raw_{j}_{c}_{a}',lhs==rhs)
  # Off-sector lower-return check, where return corruption is visible.
  rr=o.raw(0,14,0,'raw_return_sign' if fault=='return_sign' else None)
  ck(f'original_bottom_{j}',mul(rr,xx)==scale(xx,-1))
 # Rational phase point cos(theta)=3/5, sin(theta)=4/5.
 u=add(scale(I,F(3,5)),scale(T,F(4,5)))
 ut=o.transpose(u); e=scale(add(I,o.G[1]),F(1,2)); p=mul(mul(u,e),ut)
 ck('u_orthogonal',mul(u,ut)==I)
 ck('E_projector',mul(e,e)==e and o.transpose(e)==e)
 ck('P_projector',mul(p,p)==p and o.transpose(p)==p)
 ck('P_rank64_spin',p.get(0,0)*128==64)
 ck('P_mass_commutes',comm(p,A)==Z)
 for j in C:ck(f'P_C_commutes_{j}',comm(p,C[j])==Z)
 dp=comm(T,p)
 ck('P_nonconstant',dp!=Z)
 dp_check=scale(dp,-1) if fault=='projector_derivative' else dp
 ck('parallel_observation',add(scale(mul(C[7],dp_check),-1),comm(X[7],p))==Z)
 ck('omitted_connection_leaks',mul(C[7],dp)!=Z)
 # a8=sin(x7), a7=a9=0 at x=0: f78=1, so the crossed
 # covariant derivatives on a putative parallel P give -[T,P].
 ck('nonflat_integrability_witness',comm(T,e)!=Z)
 # Exact full blade census for the matrices commuting with Cj,A,T.
 # Each Clifford blade is an eigenvector of conjugations, so this exhausts
 # linear constraints; no sampled matrix rank argument is used.
 masks=range(1<<14)
 massive=[mask for mask in masks if not(mask&1) and all(not(mask&(1<<j)) for j in C)]
 with_t=[mask for mask in massive if mask.bit_count()%2==0]
 ck('spin_massive_commutant1024',len(massive)==1024)
 ck('spin_massive_T_commutant512',len(with_t)==512)
 ck('all9_copy_dimensions',len(massive)*81==288**2 and len(with_t)*81==2*144**2)
 return out
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
 checks=controls();assert all(checks.values()),[k for k,v in checks.items() if not v]
 faults={f:[k for k,v in controls(f).items() if not v] for f in ['trace_lift','induced_sign','return_sign','coefficient_order','projector_derivative']};assert all(faults.values())
 deps=['tests/channel-swings/k2206_changed_raw_mass_construction_probe.py','explorations/conditional-build/k2212-mass-connection-algebra-2026-10-28.md','explorations/conditional-build/k2218-local-observation-rigidity-2026-10-28.md','explorations/conditional-build/k2221-raw-flavor-observation-2026-10-28.md']
 report=dict(result_id='K2221',status='conditional_raw_lift_and_parallel_observation_classification',checks=checks,fault_failures=faults,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),evidence_kinds='Universal written Clifford-character, parallel-transport and selfadjoint-domain proofs; exact original-row, trace, projector and faithful blade-census controls. No source physical observation.')
 target=ROOT/'lab/process/k2221-raw-flavor-observation.json'
 if args.write:target.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(target.read_text())==report
 print(json.dumps(dict(result='K2221',controls=len(checks),faults={k:len(v) for k,v in faults.items()})))
if __name__=='__main__':main()
