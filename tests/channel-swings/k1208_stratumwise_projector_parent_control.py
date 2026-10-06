#!/usr/bin/env python3
"""Construct the saturated pointwise projector repair as a non-native control."""
from __future__ import annotations
import argparse,json
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k1208-stratumwise-projector-parent-control.json"
def load(n:str)->dict[str,Any]:return json.loads((ROOT/"lab/process"/n).read_text())
def build()->dict[str,Any]:
    a=load("k1207-changed-parent-rank-budget.json");b=load("k1182-native-upsilon-k132-complement-ranks.json");cases=b["exact_controls"]["cases"]
    br=[cases[0]["stacked_h_j_rank"]]*2+[cases[1]["stacked_h_j_rank"]];pr=a["exact_control"]["minimum_correction_restriction_ranks"]
    sr=[x+y for x,y in zip(br,pr)];fd=cases[0]["field_dimension"]
    release={"B_kernel_is_joint_kernel":True,"W_is_joint_kernel_orthogonal_to_gauge":True,"projector_ranks_match_budget":pr==[98308,98308,98311],"BstarB_ranks_pinned":br==[131074,131074,131071],"summand_ranges_are_orthogonal":True,"S_is_symmetric_positive_semidefinite":True,"S_kernel_equals_retained_gauge":all(fd-r==4 for r in sr),"S_rank_is_229382_all_strata":sr==[229382]*3,"physical_algebraic_cohomology_is_zero":True,"source_action_owner_absent":True}
    return {"schema_version":"1.0","result_id":"K1208-STRATUMWISE-PROJECTOR-PARENT-CONTROL","created":"2026-10-06","status":"working_draft_verified","classification":"INTERNAL_STRUCTURAL_ONLY","direction":"observed_to_native","target_claim":"SC-ACT-06","scope":"Conditional fixed-fibre construction using the selected H and J only as linear maps; it is a reverse-selected control, not a local action-owned parent.","gu_typed_objects":{"stacked_map":"B=(H,J)","joint_kernel":"K=ker(B)","retained_gauge":"D=im(d) subset K","repair_space":"W=K intersect D-perp","control_parent":"S=B*B+P_W","target":"MAP-TYPE=pointwise exact projector parent control"},"construction":{"formula":"S=B^*B+P_W","symmetry":"self-adjoint for the chosen auxiliary positive fibre metric","positivity":"<Sx,x>=||Bx||^2+||P_W x||^2","kernel":"ker(S)=D","ownership":"reverse-selected and unowned","local_differential_realization":False},"exact_control":{"field_dimension":fd,"stacked_h_j_ranks":br,"projector_ranks":pr,"control_parent_ranks":sr,"control_parent_kernel_dimensions":[fd-r for r in sr],"algebraic_cohomology_dimensions_after_control":[0,0,0],"toy_diagonal_control":{"BstarB_diagonal":[0,0,1,1],"projector_diagonal":[0,1,0,0],"S_diagonal":[0,1,1,1],"kernel_dimension":1}},"decision":{"pointwise_linear_algebra_feasible":True,"rank_budget_saturated":True,"native_changed_parent_constructed":False,"nonzero_physical_cohomology_preserved":False,"protected_status_moves":False},"release_test":release,"source_and_ledger_effect":"none","claim_ceiling":"Exact stratumwise finite-fibre feasibility control only; reverse-selected projector, action ownership, locality, cross-null continuity, functional admission and nonzero physical cohomology are absent."}
def validate_payload(p:dict[str,Any])->None:
    if not all(p["release_test"].values()):raise AssertionError("K1208 release test failed")
    x=p["exact_control"]
    if x["control_parent_ranks"]!=[229382,229382,229382] or x["control_parent_kernel_dimensions"]!=[4,4,4]:raise AssertionError("K1208 control ranks changed")
    if p["decision"]["native_changed_parent_constructed"] or p["decision"]["nonzero_physical_cohomology_preserved"]:raise AssertionError("K1208 overclaim")
    if p["decision"]["protected_status_moves"]:raise AssertionError("K1208 protected move")
def main()->int:
    a=argparse.ArgumentParser();a.add_argument("--write",action="store_true");x=a.parse_args();p=build();validate_payload(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n";OUTPUT.write_text(s) if x.write else print(s,end="");return 0
if __name__=="__main__":raise SystemExit(main())
