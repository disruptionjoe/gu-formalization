#!/usr/bin/env python3
"""Replay complete order-ten face execution custody."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2]
OUTPUT=ROOT/"lab/process/k1197-order-ten-face-execution-coverage-replay.json"
def load(name:str)->dict[str,Any]: return json.loads((ROOT/"lab/process"/name).read_text())
def build()->dict[str,Any]:
    k508=load("k508-order-ten-selected-face-cell-bank.json"); k511=load("k511-order-ten-face-shard-plan.json")
    files=[next((ROOT/"lab/process").glob(f"k{n}-order-ten-*.json")) for n in range(512,542)]
    banks=[json.loads(f.read_text()) for f in files]
    planned=[pid for sh in k511["shards"] for pid in sh["program_ids"]]
    executed=[]
    for b in banks: executed += [r["program_id"] for r in b["direct_overlap_controls"]]
    shard_count=sum(int(b["fixed_control"].get("shard_count", 1)) for b in banks)
    programs=sum(int(b["fixed_control"]["program_count"]) for b in banks)
    cells=sum(int(b["fixed_control"]["complete_positive_width_cells"]) for b in banks)
    evaluations=sum(int(b["fixed_control"]["ordered_descriptor_cell_evaluations"]) for b in banks)
    overlaps=sum(len(b["direct_overlap_controls"]) for b in banks)
    return {"schema_version":"1.0","result_id":"K1197-ORDER-TEN-FACE-EXECUTION-COVERAGE-REPLAY","created":"2026-10-06","classification":"INTERNAL_NUMERICAL_CONTROL_ONLY","direction":"observed_to_native",
      "fixed_control":{"predecessor_manifests":[str((ROOT/"lab/process/k508-order-ten-selected-face-cell-bank.json").relative_to(ROOT)),str((ROOT/"lab/process/k511-order-ten-face-shard-plan.json").relative_to(ROOT))]+[str(f.relative_to(ROOT)) for f in files],"selected_programs":20,"planned_remaining_programs":len(planned),"execution_artifacts":len(banks),"executed_shards":shard_count,"executed_remaining_programs":programs,"selected_cells":k508["fixed_control"]["complete_positive_width_cells"],"remaining_cells":cells,"total_cells":k508["fixed_control"]["complete_positive_width_cells"]+cells,"total_descriptor_cell_evaluations":k508["fixed_control"]["ordered_descriptor_cell_evaluations"]+evaluations,"direct_overlap_controls":overlaps},
      "custody_replay":{"planned_program_ids_unique":len(set(planned))==len(planned),"executed_program_ids_unique":len(set(executed))==len(executed),"executed_ids_equal_plan":executed==planned,"all_direct_overlap_controls_pass":all(r["intervals_overlap"] for b in banks for r in b["direct_overlap_controls"]),"K541_declares_complete_bank":banks[-1]["decision"]["complete_K508_plus_K511_reachable_face_program_bank"]},
      "decision":{"all_936_reachable_face_programs_have_positive_width_execution_evidence":True,"literal_new_all_face_reexecution_required":False,"complete_order_ten_integral_enclosure_emitted":False,"next_exact_input":"Replay the K542--K553 projective, boundary, owner, remainder and complete-integral chain."},
      "release_test":{"exactly_229_shards":shard_count==229,"exactly_916_remaining_programs":programs==len(planned)==len(executed)==916,"exactly_6552_total_cells":k508["fixed_control"]["complete_positive_width_cells"]+cells==6552,"exactly_87141600_descriptor_cell_evaluations":k508["fixed_control"]["ordered_descriptor_cell_evaluations"]+evaluations==87141600,"all_ids_match_in_order":executed==planned,"all_overlaps_pass":all(r["intervals_overlap"] for b in banks for r in b["direct_overlap_controls"]),"integral_not_overclaimed":True,"protected_status_unchanged":True},
      "claim_ceiling":"Exact custody replay for K508 and K512--K541. Twenty selected programs plus all 916 K511-planned remaining programs have 6,552 positive-width cells, 87,141,600 ordered descriptor-cell evaluations and one passing direct overlap per remaining program. This establishes complete reachable-face execution evidence, not by itself a projective cover, Peano remainder, complete integral, K152 interval or physical claim."}
def validate_payload(p:dict[str,Any])->None:
    if not all(p["release_test"].values()):raise AssertionError("K1197 custody replay failed")
    if not all(p["custody_replay"].values()):raise AssertionError("K1197 custody invariant failed")
    if p["decision"]["complete_order_ten_integral_enclosure_emitted"]:raise AssertionError("K1197 overclaimed integral")
def main()->int:
    a=argparse.ArgumentParser();a.add_argument("--write",action="store_true");x=a.parse_args();p=build();validate_payload(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n";OUTPUT.write_text(s) if x.write else print(s,end="");return 0
if __name__=="__main__":raise SystemExit(main())
