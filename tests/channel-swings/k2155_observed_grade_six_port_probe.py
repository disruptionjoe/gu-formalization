#!/usr/bin/env python3
"""Exact Cl77 observation controls; written proof establishes completeness/rank."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
import argparse,hashlib,json
import numpy as np
from source_native_fermion_transverse_port_probe import add,mul,scale
ROOT=Path(__file__).resolve().parents[2]
ETA=[1]*7+[-1]*7;W=[0,1,2,7];G=[{1<<i:F(1)} for i in range(14)]
Z={sum(1<<i for i in [0,1,3,4,5,6,8]):F(1)}
OLD={(1<<7)-1:F(1)}
FAULTS=['ambient_denominator','old_coefficient','commutator_port','wrong_trace_direction','unrestricted_inputs','observed_lift','wrong_pairing']
def port(z,comm=False):return [scale(add(mul(z,g,ETA),scale(mul(g,z,ETA),-1 if comm else 1)),F(1,2)) for g in G]
def slash(k):return add(*(scale(G[i],ETA[i]*k.get(i,0)) for i in W))
def response(z,k,den=4,comm=False):
 a=port(z,comm);s=slash(k);tr=add(*(scale(mul(G[i],a[i],ETA),ETA[i]) for i in W));d=add(*(scale(a[i],ETA[i]*k.get(i,0)) for i in W));return add(d,scale(mul(s,tr,ETA),-F(1,den)))
def matrices():
 gs=[]
 for j in range(7):
  cr=np.zeros((128,128),dtype=np.int64);an=cr.copy()
  for n in range(128):
   sign=(-1)**((n&((1<<j)-1)).bit_count())
   if n&(1<<j):an[n^(1<<j),n]=sign
   else:cr[n^(1<<j),n]=sign
  gs.append(cr+an)
  gs.append(cr-an)
 return gs[::2]+gs[1::2]
def product(gs,indices):
 a=np.eye(128,dtype=np.int64)
 for i in indices:a=a@gs[i]
 return a
def controls(fault=None,exhaust=False):
 out={};check=lambda n,v:out.__setitem__(n,bool(v));k={0:1,7:1};s=slash(k)
 chosen=OLD if fault=='old_coefficient' else Z;den=14 if fault=='ambient_denominator' else 4;comm=fault=='commutator_port'
 a=port(chosen,comm);tr=add(*(scale(mul(G[i],a[i],ETA),ETA[i]) for i in W))
 check('new_tangent_trace',tr==scale(Z,2));fr=response(chosen,k,den,comm)
 check('massless_descent',not (fr if fault=='unrestricted_inputs' else mul(fr,s,ETA)))
 check('old_observation_failure',bool(mul(response(OLD,k),s,ETA)))
 check('null_slash_square',not mul(s,s,ETA));check('invisible_component2',not a[2] and not k.get(2,0))
 check('invertible_component1',mul(a[1],a[1],ETA)=={0:F(1)})
 check('r0_zero_port',all(not port({sum(1<<i for i in [3,4,5,6,8,9,10]):F(1)})[i] for i in W))
 z4={sum(1<<i for i in [0,1,2,7,3,4,5]):F(1)}
 check('r4_pure_trace',all(port(z4)[i]==mul(G[i],z4,ETA) for i in W))
 lift=F(1,2) if fault=='observed_lift' else F(1,12)
 zeta={i:scale(mul(G[i],s,ETA),lift) for i in W}
 gamma_zeta=add(*(scale(mul(G[i],zeta[i],ETA),ETA[i]) for i in W))
 residual={i:add(mul(s,zeta[i],ETA),scale(gamma_zeta,-k.get(i,0)),scale(s,k.get(i,0))) for i in W}
 check('literal_coupled_lift_residual',all(residual[i]==scale(s,F(5,6)*k.get(i,0)) for i in W))
 check('literal_coupled_lower_row',not add(*(scale(zeta[i],-ETA[i]*k.get(i,0)) for i in W)))
 gs=matrices();I=np.eye(128,dtype=np.int64);B=product(gs,range(7,14));J=product(gs,range(14));q=8 if fault=='wrong_trace_direction' else 9
 K=B@gs[q];az=product(gs,[0,1,3,4,5,6,8]);ams=[(az@g+g@az)//2 for g in gs]
 if fault=='wrong_pairing':K=B
 check('real_clifford_relations',all(np.array_equal(gs[i]@gs[j]+gs[j]@gs[i],2*ETA[i]*I if i==j else 0*I) for i in range(14) for j in range(i,14)))
 check('B_symmetric_involution',np.array_equal(B.T,B) and np.array_equal(B@B,I))
 check('B_gamma_skew',all(not np.any(g.T@B+B@g) for g in gs))
 check('J_half_isotropy',not np.any((I+J).T@B@(I+J)) and not np.any((I-J).T@B@(I-J)))
 check('Hq_Hermitian_involution',np.array_equal(K.T,-K) and np.array_equal(K@K,-I))
 check('Hq_half_signatures',not np.any(K@J-J@K) and np.trace(K)==0 and np.trace(J@K)==0 and np.trace(J)==0)
 check('Hq_tangent_selfadjoint',all(not np.any(gs[i].T@K-K@gs[i]) for i in W))
 check('whole_port_Hq_skew',all(not np.any(A.T@K+K@A) for A in ams))
 check('whole_port_J_even',all(not np.any(A@J-J@A) for A in ams))
 K8=B@gs[8];A=ams[0]
 check('q8_same_real_failure',bool(np.any(A.T@K8+K8@A)))
 check('q8_observed_imaginary_repair',not np.any(-A.T@K8+K8@A))
 check('q8_uniform_ambient_phase_fails',bool(np.any(-ams[8].T@K8+K8@ams[8])))
 sm=gs[0]-gs[7];partner=(gs[0]+gs[7]);check('null_rank_half_identity',not np.any(sm@sm) and np.array_equal(sm@partner+partner@sm,4*I))
 if exhaust:
  counts={i:0 for i in range(5)};passes={i:0 for i in range(5)};traces=True;residual_identity=True
  nulls=[{i:1,7:sgn} for i in [0,1,2] for sgn in [-1,1]]
  for inds in combinations(range(14),7):
   z={sum(1<<i for i in inds):F(1)};r=len(set(inds)&set(W));counts[r]+=1;ap=port(z)
   traces &= add(*(scale(mul(G[i],ap[i],ETA),ETA[i]) for i in W))==scale(z,r)
   ok=True
   for kk in nulls:
    ss=slash(kk);actual=mul(response(z,kk),ss,ETA);expected=scale(mul(mul(ss,z,ETA),ss,ETA),F(2-r,4));residual_identity &=actual==expected;ok &=not actual
   passes[r]+=int(ok)
  check('all3432_trace_identities',traces and sum(counts.values())==3432)
  check('all3432_sandwich_identities',residual_identity)
  check('basis_classification',counts=={0:120,1:840,2:1512,3:840,4:120} and passes=={0:120,1:0,2:1512,3:0,4:120})
 return out

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--write',action='store_true');args=ap.parse_args()
 base=controls(exhaust=True);bad=[k for k,v in base.items() if not v];assert not bad,('BASELINE FAIL',bad)
 faults={}
 for f in FAULTS:
  bad=[k for k,v in controls(f).items() if not v];assert bad,('UNDETECTED',f);faults[f]=bad
 deps=['explorations/conditional-build/k2155-observed-grade-six-port-2026-10-27.md','tests/channel-swings/source_native_fermion_transverse_port_probe.py']
 report=dict(result_id='K2155',status='conditional_exact_controls',exact_checks=base,fault_failures=faults,dependency_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in deps},probe_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),universal_evidence='Written normal-grade/null-span classification, radical proof and injective-functional witness; finite basis identities and exact integer matrix controls independently checked. No physical quotient or complete operator descent.')
 p=ROOT/'lab/process/k2155-observed-grade-six-port.json'
 if args.write:p.write_text(json.dumps(report,indent=2)+'\n')
 else:assert json.loads(p.read_text())==report,'stored report differs'
 print(json.dumps({'result':'K2155','checks':len(base),'faults':len(faults),'basis_blades':3432}))
if __name__=='__main__':main()
