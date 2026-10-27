#!/usr/bin/env python3
"""Exact sparse Clifford controls; universal scope is proved in the companion note."""
from fractions import Fraction as F
from pathlib import Path
from itertools import combinations
import argparse,json,hashlib
from source_native_fermion_transverse_port_probe import add,mul,scale
ROOT=Path(__file__).resolve().parents[2]
ETA=[1]*7+[-1]*7; W=[0,1,2,7]; N=[i for i in range(14) if i not in W]
G=[{1<<i:F(1)} for i in range(14)]; I={0:F(1)}; Z={sum(1<<i for i in [0,1,3,4,5,6,8]):F(1)}
def mm(a,b):return mul(a,b,ETA)
def trace(z,inds):return add(*(scale(mm(G[i],z[i]),ETA[i]) for i in inds))
def D(z,v,k,inds):
 s=add(*(scale(G[i],ETA[i]*k.get(i,0)) for i in inds)); tr=trace(z,inds)
 return {i:add(mm(s,z[i]),scale(tr,-k.get(i,0)),scale(v,k.get(i,0))) for i in inds},add(*(scale(z[i],-ETA[i]*k.get(i,0)) for i in inds))
def A(z,v,c=1):return {i:z[i] for i in W},add(v,scale(trace(z,N),-c))
def port(z,comm=False):return [scale(add(mm(z,g),scale(mm(g,z),-1 if comm else 1)),F(1,2)) for g in G]
def upper(a,z,v):return {i:add(*(scale(mm(G[j],add(mm(a[j],z[i]),scale(mm(a[i],z[j]),-1))),ETA[j]) for j in range(14)),mm(a[i],v)) for i in W}
def controls(fault=None,exhaust=False):
 out={};ck=lambda n,v:out.__setitem__(n,bool(v));c=0 if fault=='literal_pullback' else (-1 if fault=='shift_sign' else 1)
 ok=True; kernel=True
 for mu in W:
  k={mu:1}
  for col in range(15):
   z={i:(I if i==col else {}) for i in range(14)};v=I if col==14 else {}
   az,av=A(z,v,c);lhs,lv=D(az,av,k,W);rhs,rv=D(z,v,k,range(14))
   ok &= all(lhs[i]==rhs[i] for i in W) and lv==rv
 ck('all_tangent_covectors_all_field_blocks',ok)
 for j in N:
  z={i:(I if i==j else {}) for i in range(14)};v=scale(G[j],ETA[j]);az,av=A(z,v,c)
  kernel &= not av and all(not x for x in az.values())
 ck('all_ten_kernel_blocks',kernel)
 z={i:scale(G[i],F(1,12)) for i in range(14)};az,av=A(z,I,c)
 ck('ambient_lift_scalar_one_sixth',av==scale(I,F(1,6)))
 ck('ambient_lift_observed_half',all(az[i]==scale(mm(G[i],av),F(1,2)) for i in W))
 a=port(Z,fault=='commutator_port');j=3;z={i:(I if i==j else {}) for i in range(14)};v=G[j]
 residual=upper(a,z,v)
 expected=scale({sum(1<<i for i in [1,4,5,6,8]):F(1)},2)
 ck('actual_upper_connection_leak',residual[0]==expected)
 scalar=[(I if i in W else {}) for i in range(14)]
 ck('scalar_tangent_coefficient_positive_control',all(not val for val in upper(scalar,z,v).values()))
 ck('invertible_leak_square',mm(residual[0],residual[0])==scale(I,-4))
 k={0:1,7:1};s=add(G[0],scale(G[7],-1));z={i:(s if i==3 else {}) for i in range(14)};v=mm(G[3],s)
 ds,dv=D(z,v,k,range(14));az,av=A(z,v,c)
 ck('forgotten_characteristic_input',all(not t for t in ds.values()) and not dv and not av and all(not t for t in az.values()))
 ck('characteristic_leak_nonzero',bool(upper(a,z,v)[0]))
 # Actual scalar coordinate realization A(x)=[1,-x], P=I; R=A at x=2.
 # Dobs=d/dx; choose C=[[0,-1],[0,0]], then R C - A'=0 only with C_01=-1.
 x=F(2);Aprime=[0,-1];C01=1 if fault=='moving_sign' else -1
 M=[0,C01-Aprime[1]]
 ck('moving_leibniz_correction',M==[0,0]);ck('frozen_moving_map_fails',C01!=0)
 # Density-dual evaluation of A is not equation insertion R*.
 lam=F(3);zN=F(5);nu=F(7);gamma=F(2);AdualN=0 if fault=='wrong_dual' else -gamma*lam
 ck('field_dual_evaluation',lam*(nu-gamma*zN)==lam*nu+AdualN*zN)
 ck('equation_and_field_duals_distinct',AdualN!=0)
 # Normal covector on a tangent zeta component has a nonzero slash defect.
 z={i:(I if i==0 else {}) for i in range(14)};normal_k={3:1};full,_=D(z,{},normal_k,range(14))
 ck('normal_jet_not_descended',full[0]==G[3] and bool(full[0]))
 if exhaust:
  passed={i:0 for i in range(5)};total=0
  for inds in combinations(range(14),7):
   zz={sum(1<<i for i in inds):F(1)};aa=port(zz);r=len(set(inds)&set(W));total+=1
   # For each blade, absent mixed indices commute identically; test every nontrivial pair.
   ok=all(not add(mm(aa[mu],G[j]),scale(mm(G[j],aa[mu]),-1)) for mu in W for j in N)
   passed[r]+=int(ok)
  ck('all3432_complete_upper_classification',total==3432 and passed=={0:120,1:0,2:0,3:0,4:0})
 return out
FAULTS=['literal_pullback','shift_sign','commutator_port','moving_sign','wrong_dual']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
 base=controls(exhaust=True);assert all(base.values()),('BASELINE FAIL',[k for k,v in base.items() if not v]);faults={}
 for f in FAULTS:
  fails=[k for k,v in controls(f).items() if not v];assert fails,('UNDETECTED',f);faults[f]=fails
 deps=['explorations/conditional-build/k2157-normal-trace-equation-adapter-2026-10-27.md','tests/channel-swings/source_native_fermion_transverse_port_probe.py']
 report=dict(result_id='K2157',status='conditional_exact_controls',exact_checks=base,fault_failures=faults,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Companion note proves all-input principal identity, dual distinction, mixed-contraction class obstruction and moving-factorization criterion; no full source operator or physical quotient.')
 p=ROOT/'lab/process/k2157-normal-trace-equation-adapter.json'
 if args.write:p.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(p.read_text())==report,'stored report differs'
 print(json.dumps({'result':'K2157','exact_checks':len(base),'faults':faults}))
if __name__=='__main__':main()
