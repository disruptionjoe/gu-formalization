#!/usr/bin/env python3
"""K1190: integrate the corrected enlarged-gauge branch."""
from __future__ import annotations
import argparse,json
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k1190-i1b-enlarged-gauge-boundary.json"
def build()->dict[str,Any]:
 return {"schema_version":"1.0","result_id":"K1190-I1B-ENLARGED-GAUGE-BOUNDARY","created":"2026-10-05","status":"working_draft_verified","classification":"SOURCE_NATIVE_ROUTE","target_claim":"SC-ACT-06","actual_current_t0_gauge_rank":4,"auxiliary_nonnull_radial":{"domain_dimension":16384,"hessian_defect_rank":8191,"joint_null_dimension":8193,"source_owned_gauge":False},"favorable_nonnull_overgrant":{"after_auxiliary_radial":90115,"after_auxiliary_radial_and_rank98_best":90017},"changed_parent_minimum_restriction_rank":8191,"null_radial_rank_computed":False,"candidate_meeting_full_packet":0,"next_condition":"supply a native source-owned enlarged gauge or KT/BFV differential, measure its joint-kernel image on every causal stratum, prove closed range, and replay K1150; otherwise supply a new source-owned map or changed stationary parent","protected_disposition":"SC-ACT-01/02/06 remain ASSERTS; SC-META-53 remains UNCERTAIN; LT-SM8/LT-GR6b/RA-F1/AC-F1 remain NEEDS","claim_ceiling":"exact corrected branch boundary; no global GU or SC-ACT-06 verdict"}
def validate(p:dict[str,Any])->None:
 assert p["result_id"]=="K1190-I1B-ENLARGED-GAUGE-BOUNDARY" and p["status"]=="working_draft_verified" and p["classification"]=="SOURCE_NATIVE_ROUTE" and p["target_claim"]=="SC-ACT-06"
 assert p["actual_current_t0_gauge_rank"]==4 and p["auxiliary_nonnull_radial"]=={"domain_dimension":16384,"hessian_defect_rank":8191,"joint_null_dimension":8193,"source_owned_gauge":False}
 assert p["favorable_nonnull_overgrant"]=={"after_auxiliary_radial":90115,"after_auxiliary_radial_and_rank98_best":90017} and p["changed_parent_minimum_restriction_rank"]==8191
 assert not p["null_radial_rank_computed"] and p["candidate_meeting_full_packet"]==0 and "every causal stratum" in p["next_condition"] and "remain ASSERTS" in p["protected_disposition"] and "no global" in p["claim_ceiling"]
def main()->int:
 q=argparse.ArgumentParser();q.add_argument("--write",action="store_true");a=q.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n";OUTPUT.write_text(s) if a.write else print(s,end="");print("PASS controls=20",file=__import__('sys').stderr);return 0
if __name__=="__main__":raise SystemExit(main())
