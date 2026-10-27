#!/usr/bin/env python3
"""Reconstruct principal/coefficient maps in faithful exact sparse Cl(7,7)."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
from source_native_fermion_transverse_port_probe import add,scale,mul
ROOT=Path(__file__).resolve().parents[2]
ETA=[1]*7+[-1]*7;W=[0,1,2,7];N=[i for i in range(14) if i not in W]
G=[{1<<i:F(1)} for i in range(14)];I={0:F(1)};Z={sum(1<<i for i in [0,1,3,4,5,6,8]):F(1)};Q=[3,4,5,6,8]
def mm(a,b):return mul(a,b,ETA)
def tr(z,inds):return add(*(scale(mm(G[i],z[i]),ETA[i]) for i in inds))
def dot(T,z):return add(*(mm(T[j],z[j]) for j in N))
def D(z,v,k,inds):
 s=add(*(scale(G[i],ETA[i]*k.get(i,0)) for i in inds));t=tr(z,inds)
 return {i:add(mm(s,z[i]),scale(t,-k.get(i,0)),scale(v,k.get(i,0))) for i in inds},add(*(scale(z[i],-ETA[i]*k.get(i,0)) for i in inds))
def A(T,z,v,c=2):
 f=dot(T,z);return {i:add(z[i],mm(G[i],f)) for i in W},add(v,scale(tr(z,N),-1),scale(f,c))
def R(T,e,v,sign=-1):
 f=dot(T,e);return {i:add(e[i],scale(mm(G[i],f),sign)) for i in W},add(v,scale(f,sign))
def kernel(T,j):
 z={i:(I if i==j else {}) for i in N};z.update({i:scale(mm(G[i],T[j]),-1) for i in W});return z,add(scale(G[j],ETA[j]),scale(T[j],-2))
def C(a,z,v,lower_sign=-1):
 e={i:add(*(scale(mm(G[l],add(mm(a[l],z[i]),scale(mm(a[i],z[l]),-1))),ETA[l]) for l in range(14)),mm(a[i],v)) for i in range(14)}
 return e,add(*(scale(mm(a[l],z[l]),lower_sign*ETA[l]) for l in range(14)))
def port():return [scale(add(mm(Z,g),mm(g,Z)),F(1,2)) for g in G]
def controls(fault=None,census=False):
 out={};ck=lambda k,v:out.__setitem__(k,bool(v));c=1 if fault=='shift_coefficient' else 2;rsign=1 if fault=='equation_sign' else -1
 # Two noncentral commuting blocks, including the all-tangent/odd-normal sector.
 T={j:{} for j in N};T[3]={((1<<4)|(1<<5)):F(2,3)};T[8]={sum(1<<i for i in [0,1,2,7,9]):F(-1,2)}
 if fault=='noncommutant':T[3]=G[0]
 ok=True
 for mu in W:
  for col in range(15):
   z={i:(I if i==col else {}) for i in range(14)};v=I if col==14 else {}
   az,av=A(T,z,v,c);lhs=D(az,av,{mu:1},W);e,ev=D(z,v,{mu:1},range(14));rhs=R(T,e,ev,rsign)
   ok &= lhs==rhs
 ck('all_tangent_all_field_blocks_noncentral',ok)
 ck('all_kernel_columns',all(A(T,*kernel(T,j),c)==({i:{} for i in W},{}) for j in N))
 # Section on all five observed blocks.
 section=True
 for col in W+[14]:
  z={i:(I if i==col else {}) for i in range(14)};v=I if col==14 else {}
  section &= A(T,z,v,c)==({i:z[i] for i in W},v)
 ck('right_inverse_all_observed_blocks',section)
 a=[(scale(I,F(i+1,3)) if i in W else {}) for i in range(14)]
 ck('complete_scalar_connection_positive_control',all(R(T,*C(a,*kernel(T,j),lower_sign=1 if fault=='lower_row_sign' else -1),rsign)==({i:{} for i in W},{}) for j in N))
 aa=port();scalar_fixtures=[{j:F(j-5,7) for j in N},{j:F(int(j==9)) for j in N},{j:F(0) for j in N}]
 reduced=True;grades=True;remaining=True;gradeone=True
 for ts in scalar_fixtures:
  TT={j:scale(I,ts[j]) for j in N};b=add(*(scale(G[j],ts[j]) for j in Q))
  for j in N:
   z,v=kernel(TT,j);e,ev=C(aa,z,v);rr,rv=R(TT,e,ev)
   f=scale(I,ts[j]);fq=scale(I,ts[j] if j in Q else 0);chi=scale(G[j],ETA[j]) if j in Q else {}
   expected=scale(mm(mm(G[2],Z),add(mm(b,f),scale(mm(b,chi),-1),fq)),2)
   reduced &= rr[2]==expected
   inside=add(mm(b,f),scale(mm(b,chi),-1),fq)
   gradeone &= {m:v for m,v in inside.items() if m.bit_count()==1}==mm(b,f)
   grades &= all(mask.bit_count() in range(4,9) for val in rr.values() for mask in val)
   if all(ts[q]==0 for q in Q) and j not in Q:
    remaining &= rr[0]==scale(mm(aa[0],f),-14)
 ck('original_full_coefficient_reduced_identity_all_normal_slots',reduced)
 ck('remaining_scalar_coefficients_minus14',remaining)
 ck('scalar_grade_one_forcing_bt_j',gradeone)
 ck('moving_scalar_grade_separation',grades)
 zero={j:{} for j in N};res,_=R(zero,*C(aa,*kernel(zero,3)))
 ck('zero_parameter_invertible_leak',mm(res[0],res[0])==scale(I,-4))
 ck('zero_parameter_empty_tangent_row',not res[2] and not res[7])
 # Product-rule term independently formed by differentiating A in a normal column.
 moving=True
 dT={mu:{j:{} for j in N} for mu in W};dT[0][3]=mm(G[4],G[5]);dT[7][3]=I
 H=add(*(scale(mm(G[mu],dT[mu][3]),ETA[mu]) for mu in W));terms=[]
 for mu in W:
  f=dT[mu][3];dz={i:mm(G[i],f) for i in W};dv=scale(f,2);terms.append(D(dz,dv,{mu:1},W))
 total=({i:add(*(t[0][i] for t in terms)) for i in W},add(*(t[1] for t in terms)))
 expected=({i:scale(mm(G[i],H),-1) for i in W},scale(H,-1))
 if fault=='omit_moving_derivative':total=({i:{} for i in W},{})
 ck('moving_product_rule_exact',total==expected and bool(H))
 # Commutant parameters actually require left/right order: T8 and gamma3 do not commute.
 ck('noncentral_order_control',bool(add(mm(T[8],G[3]),scale(mm(G[3],T[8]),-1))))
 if census:
  actual=[];expected=[]
  for mask in range(1<<14):
   b={mask:F(1)}
   if all(mm(b,G[mu])==mm(G[mu],b) for mu in W):actual.append(mask)
   w=sum((mask>>i)&1 for i in W);n=sum((mask>>i)&1 for i in N)
   if (w==0 and n%2==0) or (w==4 and n%2==1):expected.append(mask)
  ck('complete_16384_blade_commutant_census',actual==expected and len(actual)==1024)
 return out
FAULTS=['shift_coefficient','equation_sign','noncommutant','omit_moving_derivative','lower_row_sign']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args();base=controls(census=True)
 assert all(base.values()),[k for k,v in base.items() if not v]
 faults={}
 for f in FAULTS:
  bad=[k for k,v in controls(f).items() if not v];assert bad,('undetected',f);faults[f]=bad
 deps=['explorations/conditional-build/k2159-commutant-equation-adapters-2026-10-27.md','explorations/conditional-build/k2157-normal-trace-equation-adapter-2026-10-27.md','tests/channel-swings/source_native_fermion_transverse_port_probe.py']
 report=dict(result_id='K2159',status='conditional_exact_controls',exact_checks=base,fault_failures=faults,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Written commutant classification, all-scalar coefficient contradiction and moving grade obstruction separately reviewed. Rational fixtures verify reductions, not universal parameter exhaustion. No full source/physical quotient.')
 p=ROOT/'lab/process/k2159-commutant-equation-adapters.json'
 if args.write:p.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(p.read_text())==report,'stored report differs'
 print(json.dumps(dict(result='K2159',exact_checks=len(base),faults=faults)))
if __name__=='__main__':main()
