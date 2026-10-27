#!/usr/bin/env python3
"""Exact original-map controls and polynomial elimination in faithful sparse Cl77."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import argparse,hashlib,json
from k2159_commutant_equation_adapters_probe import G,I,ETA,W,N,mm,add,scale,C,R,A,kernel
ROOT=Path(__file__).resolve().parents[2]
def blade(indices):return {sum(1<<i for i in indices):F(1)}
def port(z):return [scale(add(mm(z,g),mm(g,z)),F(1,2)) for g in G]
def comm(a,b):return add(mm(a,b),scale(mm(b,a),-1))
def controls(fault=None,census=False):
 out={};ck=lambda k,v:out.__setitem__(k,bool(v))
 T={j:{} for j in N};T[3]=scale(blade([4,5]),F(2,3));T[8]=scale(blade([0,1,2,7,9]),F(-1,2))
 if fault=='noncommutant':T[3]=G[0]
 ck('declared_noncentral_commutant',all(not comm(t,G[mu]) for t in T.values() for mu in W))
 mixed=add(blade([0,1,3,4,5,6,8]),scale(blade([2,7,3,4,9,10,11]),F(2)),scale(blade([0,2,4,5,8,12,13]),F(-3)))
 # Singular normal5 factor: C=gamma4569(gamma3+gamma8).
 singular=mm(blade([4,5,6,9]),add(G[3],G[8]));singular=mm(blade([0,1]),singular)
 ck('singular_nonzero_r2_control',bool(singular) and not mm(singular,singular))
 fixtures={0:blade([3,4,5,6,8,9,10]),2:mixed,4:blade([0,1,2,7,3,4,5])}
 fixture_extra=[(2,singular)]
 original=True;traces=True;cert=True;normal=True;parity=True;projection=True;smooth=True
 for r,z in list(fixtures.items())+fixture_extra:
  a=port(z)
  if fault=='omit_normal_port':a[3]={}
  normal &= add(*(scale(mm(G[j],a[j]),ETA[j]) for j in N))==scale(z,7-r)
  for j in N:
   zz,v=kernel(T,j)
   if fault=='kernel_shift':v=add(v,T[j])
   e,f=C(a,zz,v,lower_sign=1 if fault=='reverse_sign' else -1)
   rr,rv=R(T,e,f)
   L={mu:add(e[mu],scale(mm(G[mu],f),-1)) for mu in W}
   projection &= all(L[mu]==add(rr[mu],scale(mm(G[mu],rv),-1)) for mu in W)
   for mu in W:
    expected=add(mm(add(scale(mm(G[mu],z),7-r),scale(a[mu],-10-2*r)),T[j]),scale(add(comm(a[mu],G[j]),mm(G[mu],a[j])),ETA[j]))
    original &= L[mu]==expected
   S=add(*(scale(mm(G[mu],L[mu]),ETA[mu]) for mu in W))
   traces &= S==add(scale(mm(z,T[j]),28-14*r-2*r*r),scale(a[j],(2*r+4)*ETA[j]))
   if r==2:
    for mu in W:
     val=add(L[mu],scale(mm(G[mu],S),-F(1,4)),scale(mm(S,G[mu]),-F(7,8)))
     cert &= val==scale(mm(a[j],G[mu]),-8*ETA[j])
   if r in [0,4]:
    for mu in W:
     zt=mm(z,T[j]);aj=a[j]
     if r==0:parity &= not add(mm(zt,G[mu]),mm(G[mu],zt)) and not comm(aj,G[mu])
     else:parity &= not comm(zt,G[mu]) and not add(mm(aj,G[mu]),mm(G[mu],aj))
   H=add(mm(G[0],T[3]),mm(G[7],T[8]))
   for mu in W:
    moved=add(rr[mu],scale(mm(G[mu],H),2 if fault=='moving_upper_coefficient' else 1),scale(mm(G[mu],add(rv,H)),-1))
    smooth &= moved==L[mu]
 ck('original_C_kernel_all_rows_and_slots',original);ck('tangent_trace_identity',traces);ck('r2_elimination_certificate',cert)
 ck('normal_contraction_detects_nonzero_Z',normal);ck('pure_zero_four_parity_split',parity);ck('equation_projection_cancels',projection);ck('moving_terms_cancel_exactly',smooth)
 forced=scale(G[3],-F(1,5));c=comm(forced,G[2]);ck('actual_forced_noncommutant_invertible',mm(c,c)==scale(I,-F(4,25)))
 zero=[{} for _ in G];scalars=[scale(I,F(i+1,3)) if i in W else {} for i in range(14)]
 ck('zero_coefficient_positive_control',all(R(T,*C(zero,*kernel(T,j)))==({i:{} for i in W},{}) for j in N))
 ck('scalar_connection_positive_control',all(R(T,*C(scalars,*kernel(T,j)))==({i:{} for i in W},{}) for j in N))
 if census:
  counts={0:0,2:0,4:0};ok=True
  for r in counts:
   for tw in combinations(W,r):
    for nn in combinations(N,7-r):
     z=blade(tw+nn);a=port(z);counts[r]+=1
     ok &= add(*(scale(mm(G[i],a[i]),ETA[i]) for i in W))==scale(z,r)
     ok &= add(*(scale(mm(G[j],a[j]),ETA[j]) for j in N))==scale(z,7-r)
     for mu in W:
      ok &= add(*(scale(mm(mm(G[i],a[mu]),G[i]),ETA[i]) for i in W))==scale(a[mu],6-2*r)
      for j in N:ok &= comm(a[mu],G[j])==comm(G[mu],a[j])
  ck('all1752_pure_even_port_identities',ok and counts=={0:120,2:1512,4:120})
 return out
FAULTS=['noncommutant','omit_normal_port','kernel_shift','reverse_sign','moving_upper_coefficient']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();base=controls(census=True);assert all(base.values()),[k for k,v in base.items() if not v]
 faults={}
 for f in FAULTS:
  bad=[k for k,v in controls(f).items() if not v];assert bad,('undetected',f);faults[f]=bad
 deps=['explorations/conditional-build/k2161-noncentral-adapter-obstruction-2026-10-27.md','explorations/conditional-build/k2159-commutant-equation-adapters-2026-10-27.md','tests/channel-swings/k2159_commutant_equation_adapters_probe.py','tests/channel-swings/source_native_fermion_transverse_port_probe.py']
 report=dict(result_id='K2161',status='conditional_exact_controls',exact_checks=base,fault_failures=faults,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Written polynomial elimination and parity proofs cover arbitrary pure0,2,4 coefficients and smooth commutant adapters, separately reviewed. Finite census controls algebra; no mixed-degree or full-source exclusion.')
 p=ROOT/'lab/process/k2161-noncentral-adapter-obstruction.json'
 if args.write:p.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(p.read_text())==report,'stored report differs'
 print(json.dumps(dict(result='K2161',exact_checks=len(base),faults=faults)))
if __name__=='__main__':main()
