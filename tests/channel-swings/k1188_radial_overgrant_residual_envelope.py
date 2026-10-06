#!/usr/bin/env python3
"""K1188: strongest nonnull residual under an auxiliary radial over-grant."""
from __future__ import annotations
import argparse,json
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k1188-radial-overgrant-residual-envelope.json"
def residual(base:int,*independent_ranks:int)->int:return base-sum(independent_ranks)
def build()->dict[str,Any]:
 base=98308;radial=8193;prior=98;after=residual(base,radial)
 return {"schema_version":"1.0","result_id":"K1188-RADIAL-OVERGRANT-RESIDUAL-ENVELOPE","created":"2026-10-05","status":"working_draft_verified","classification":"CONDITIONAL_RESULT","target_claim":"SC-ACT-06","current_nonnull_residual_after_h_j_and_actual_gauge":base,"actual_current_gauge_rank":4,"auxiliary_radial_joint_null_grant":radial,"residual_after_radial_overgrant":after,"rank98_grant":prior,"residual_after_radial_plus_rank98":{"best_independent_placement":residual(after,prior),"worst_complete_overlap":after},"nonnull_only":True,"full_packet_candidate_after_overgrant":False,"ownership":{"radial_joint_nullspace":"corrected auxiliary connection-only slice","rank98_channel":"favorable unowned transport grant"},"claim_ceiling":"nonnull dimension-only stress test; neither auxiliary grant is source-owned gauge or a functional complex"}
def validate(p:dict[str,Any])->None:
 assert p["result_id"]=="K1188-RADIAL-OVERGRANT-RESIDUAL-ENVELOPE" and p["classification"]=="CONDITIONAL_RESULT" and p["target_claim"]=="SC-ACT-06"
 assert p["current_nonnull_residual_after_h_j_and_actual_gauge"]==98308 and p["actual_current_gauge_rank"]==4 and p["auxiliary_radial_joint_null_grant"]==8193
 assert p["residual_after_radial_overgrant"]==90115==residual(98308,8193) and p["rank98_grant"]==98
 assert p["residual_after_radial_plus_rank98"]=={"best_independent_placement":90017,"worst_complete_overlap":90115}
 assert p["nonnull_only"] and not p["full_packet_candidate_after_overgrant"] and "auxiliary" in p["ownership"]["radial_joint_nullspace"] and "unowned" in p["ownership"]["rank98_channel"] and "nonnull" in p["claim_ceiling"]
def main()->int:
 q=argparse.ArgumentParser();q.add_argument("--write",action="store_true");a=q.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n";OUTPUT.write_text(s) if a.write else print(s,end="");print("PASS controls=18",file=__import__('sys').stderr);return 0
if __name__=="__main__":raise SystemExit(main())
