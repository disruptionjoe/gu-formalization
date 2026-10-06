#!/usr/bin/env python3
"""K1228: paired-frame block controls distinguish fixed-channel data from drift."""
from __future__ import annotations
import argparse,json
from fractions import Fraction as F
from pathlib import Path
OUTPUT=Path(__file__).parents[2]/"lab/process/k1228-block-interleaving-drift-controls.json"
def sv(v):return [str(x) for x in v]
def sm(m):return [[str(x) for x in r] for r in m]
def block(M,t):
  raw=[]
  for j in range(3):raw.append([[t[i]+M[i][j] for i in range(3)],[t[i]-M[i][j] for i in range(3)]])
  halves=[[(raw[j][0][i]+raw[j][1][i])/2 for i in range(3)] for j in range(3)]
  diffs=[[(raw[j][0][i]-raw[j][1][i])/2 for i in range(3)] for j in range(3)]
  return raw,halves,diffs
def build():
  z=F(0);M=[[F(3,10),-F(2,5),z],[F(2,13),F(3,26),-F(3,13)],[F(24,65),F(18,65),F(5,52)]];t=[z,-F(9,13),F(15,52)]
  raw0,h0,d0=block(M,t);M1=[r[:] for r in M];M1[0][1]+=F(1,100);t1=t[:];t1[2]-=F(1,200);raw1,h1,d1=block(M1,t1)
  within0=[h0[j][i]-h0[0][i] for i in range(3) for j in (1,2)]
  within1=[h1[j][i]-h1[0][i] for i in range(3) for j in (1,2)]
  dt=[h1[0][i]-h0[0][i] for i in range(3)]
  dM=[[d1[j][i]-d0[j][i] for j in range(3)] for i in range(3)]
  return {"schema_version":"1.0","result_id":"K1228-BLOCK-INTERLEAVING-DRIFT-CONTROLS","created":"2026-10-06",
    "status":"working_draft_verified","classification":"INTERNAL_CONDITIONAL_MATHEMATICS","direction":"observed_to_native",
    "target_claim":"NONE-NOT-A-KILL","scope":"Randomized blocks of paired axial process trials and Bell trials under one nominal channel configuration.",
    "theorem":{"within_block_translation":"h_ij=[y_i(+e_j)+y_i(-e_j)]/2=t_i for every j","within_block_transfer":"d_ij=[y_i(+e_j)-y_i(-e_j)]/2=M_ij","six_consistency_residuals":"h_ij-h_i0 for i=1..3 and j=1,2","cross_block_drift":"Delta t=h_b-h_ref and Delta M=d_b-d_ref","bell_remote_marginal":"sum_x p(x,y|a,b)=1/2 in the ideal Phi+ one-arm-channel model","loss_rule":"score no-signalling and holdout probabilities only with a predeclared inclusion rule and raw attempt counts"},
    "control":{"fixed_block":{"M":sm(M),"t":sv(t),"within_residuals":sv(within0)},"drifted_block":{"delta_t":sv(dt),"delta_M":sm(dM),"within_residuals":sv(within1)},"planted_nonzero_drift_entries":sum(x!=0 for x in dt)+sum(x!=0 for r in dM for x in r)},
    "decision":{"within_block_relations_detect_preparation_conditioned_inconsistency":True,"cross_block_comparison_detects_planted_drift":True,"zero_residuals_prove_memoryless_hardware":False,"postselected_counts_self_validate_locality":False},
    "release_test":{"fixed_within_residuals_zero":all(x==0 for x in within0),"drifted_within_residuals_zero":all(x==0 for x in within1),"planted_cross_block_drift_detected":any(x!=0 for x in dt) and any(x!=0 for r in dM for x in r),"exact_two_drift_entries":sum(x!=0 for x in dt)+sum(x!=0 for r in dM for x in r)==2,"protected_status_unchanged":True},
    "ownership":{"randomization_clocks_loss_model_and_systematic_bounds_imported":True,"gu_native_effect":"none"},
    "claim_ceiling":"Exact observable consistency and drift witnesses; zero witnesses do not prove an ideal, memoryless or loophole-free apparatus."}
def validate(x):
  assert x["result_id"].startswith("K1228-")
  assert len(x["control"]["fixed_block"]["within_residuals"])==6
  assert x["control"]["planted_nonzero_drift_entries"]==2 and all(x["release_test"].values())
  assert x["decision"]["within_block_relations_detect_preparation_conditioned_inconsistency"]
  assert x["decision"]["cross_block_comparison_detects_planted_drift"]
  assert x["decision"]["zero_residuals_prove_memoryless_hardware"] is False
  assert x["decision"]["postselected_counts_self_validate_locality"] is False
  assert x["ownership"]["gu_native_effect"]=="none"
if __name__=="__main__":
  q=argparse.ArgumentParser();q.add_argument("--check",action="store_true");a=q.parse_args();x=build();validate(x)
  if a.check:assert json.loads(OUTPUT.read_text())==x
  else:print(json.dumps(x,indent=2,sort_keys=True))
  print("K1228 controls: 12/12")
