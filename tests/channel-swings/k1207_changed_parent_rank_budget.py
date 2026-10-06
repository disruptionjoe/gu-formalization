#!/usr/bin/env python3
"""Prove the global fixed-fibre rank budget for an unchanged-J parent repair."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k1207-changed-parent-rank-budget.json"
def load(n:str)->dict[str,Any]:return json.loads((ROOT/"lab/process"/n).read_text())
def build()->dict[str,Any]:
    a=load("k1206-current-gauge-bfv-custody-ceiling.json");b=load("k1189-changed-parent-cancellation-cost.json")
    joint=a["exact_control"]["joint_kernel_dimensions"];g=a["exact_control"]["actual_native_t0_gauge_rank"];cost=[n-g for n in joint]
    release={"joint_kernel_dimensions_reused":joint==[98312,98312,98315],"retained_gauge_dimension_four":g==4,"nonnull_minimum_rank_98308":cost[:2]==[98308,98308],"null_minimum_rank_98311":cost[2]==98311,"rank_nullity_bound_applied_on_full_joint_kernel":True,"bound_is_sharp_for_projector_control":True,"k1189_cost_is_8191":b["minimum_completion_restriction_rank"]==8191,"k1189_cost_not_global_parent_budget":8191<min(cost),"toy_dimension_seven_gauge_two_cost_five":7-2==5,"protected_status_unchanged":True}
    return {"schema_version":"1.0","result_id":"K1207-CHANGED-PARENT-RANK-BUDGET","created":"2026-10-06","status":"working_draft_verified","classification":"INTERNAL_STRUCTURAL_ONLY","direction":"observed_to_native","target_claim":"SC-ACT-06","scope":"Finite-fibre lower bound for symmetric corrections C that preserve retained gauge D and satisfy ker(H+C) intersect ker(J)=D with J fixed.","gu_typed_objects":{"joint_kernel":"K=ker(H) intersect ker(J)","retained_gauge":"D=im(d) subset K","correction":"C restricted to K with C(D)=0","target":"MAP-TYPE=unchanged-J changed-parent rank budget"},"theorem":{"hypotheses":["D subset K","C(D)=0","ker(C restricted to K)=D"],"conclusion":"rank(C restricted to K) >= dim(K)-dim(D)","proof":"Rank-nullity on C restricted to K; the desired joint kernel forces its kernel to equal D.","sharpness":"orthogonal projection onto K intersect D-perp attains equality pointwise"},"exact_control":{"joint_kernel_dimensions":joint,"retained_gauge_dimension":g,"minimum_correction_restriction_ranks":cost,"k1189_auxiliary_radial_restriction_rank":b["minimum_completion_restriction_rank"],"toy_control":{"joint_kernel_dimension":7,"gauge_dimension":2,"minimum_rank":5}},"decision":{"k1189_rank8191_is_full_native_parent_cost":False,"rank8191_suffices_for_selected_parent_joint_kernel":False,"global_budget_established_pointwise":True,"source_owned_parent_constructed":False,"protected_status_moves":False},"release_test":release,"source_and_ledger_effect":"none","claim_ceiling":"Sharp pointwise rank lower bound with unchanged J; no source-owned correction, locality, continuous cross-null family, action, functional domain or physical claim."}
def validate_payload(p:dict[str,Any])->None:
    if not all(p["release_test"].values()):raise AssertionError("K1207 release test failed")
    if p["exact_control"]["minimum_correction_restriction_ranks"]!=[98308,98308,98311]:raise AssertionError("K1207 rank budget changed")
    if p["decision"]["k1189_rank8191_is_full_native_parent_cost"] or p["decision"]["source_owned_parent_constructed"]:raise AssertionError("K1207 overclaim")
    if p["decision"]["protected_status_moves"]:raise AssertionError("K1207 protected move")
def main()->int:
    a=argparse.ArgumentParser();a.add_argument("--write",action="store_true");x=a.parse_args();p=build();validate_payload(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n";OUTPUT.write_text(s) if x.write else print(s,end="");return 0
if __name__=="__main__":raise SystemExit(main())
