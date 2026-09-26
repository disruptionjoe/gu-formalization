#!/usr/bin/env python3
"""K511 deterministic partition of K508's remaining order-ten faces."""
from __future__ import annotations
import argparse,hashlib,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
K487=ROOT/"lab/process/k487-order-ten-face-program-compiler.json"
K508=ROOT/"lab/process/k508-order-ten-selected-face-cell-bank.json"
OUTPUT=ROOT/"lab/process/k511-order-ten-face-shard-plan.json"
SHARD_SIZE=4
def digest(x):return "sha256:"+hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def build():
 k487=json.loads(K487.read_text());k508=json.loads(K508.read_text())
 selected={r["program_id"] for r in k508["selected_face_cell_bank"]}
 remaining=[r for r in k487["face_programs"] if r["program_id"] not in selected]
 remaining.sort(key=lambda r:(hashlib.sha256(r["program_id"].encode()).hexdigest(),r["program_id"]))
 shards=[]
 for i in range(0,len(remaining),SHARD_SIZE):
  rows=remaining[i:i+SHARD_SIZE]
  shards.append({"shard_id":f"order10-face-{i//SHARD_SIZE:03d}","program_ids":[r["program_id"] for r in rows],"axes":sorted({r["axis"] for r in rows}),"codimensions":dict(sorted(Counter(str(r["codimension"]) for r in rows).items())),"program_count":len(rows),"program_digest":digest([r["program_id"] for r in rows])})
 flat=[p for s in shards for p in s["program_ids"]]
 return {"schema_version":"1.0","result_id":"K511-ORDER-TEN-FACE-SHARD-PLAN","created":"2026-09-25","classification":"INTERNAL_NUMERICAL_CONTROL_ONLY","direction":"observed_to_native","fixed_control":{"K487_program_bank_sha256":k487["program_summary"]["complete_program_bank_sha256"],"K508_selected_bank_sha256":k508["bank_summary"]["complete_selected_bank_sha256"],"reachable_face_programs":936,"already_executed_programs":len(selected),"remaining_programs":len(remaining),"shard_size":SHARD_SIZE,"shard_count":len(shards),"last_shard_size":len(shards[-1]["program_ids"]),"normal_cells_per_program":7,"ordered_descriptors_per_cell":13300,"coherent_groups_per_cell":28,"arb_decimal_digits":180,"threads":1},"partition_contract":{"sort_key":"sha256(program_id), then program_id","selected_programs_excluded_exactly_once":True,"remaining_programs_present_exactly_once":len(flat)==len(set(flat))==916,"union_with_K508_is_all_936":len(set(flat)|selected)==936,"no_overlap_with_K508":not(set(flat)&selected),"shards_are_resumable_and_order_independent":True,"plan_digest":digest(shards)},"shards":shards,"decision":{"remaining_face_work_now_has_exact_shards":True,"representative_shard_to_execute":"order10-face-000","all_916_remaining_faces_executed":False,"full_projective_normal_cone_complete":False,"complete_hybrid_integrals_emitted":False},"source_and_ledger_effect":"none","claim_ceiling":"A deterministic no-duplication/no-omission execution partition for the 916 K487 face programs not covered by K508. It is a resource and provenance interface, not numerical face evidence, a projective/interior/tail cover, K457 value, K152 interval, or source/physical result."}
def validate(p):
 f=p["fixed_control"];c=p["partition_contract"]
 if (f["remaining_programs"],f["shard_size"],f["shard_count"],f["last_shard_size"])!=(916,4,229,4):raise AssertionError("K511 census changed")
 if not all(c[k] for k in ("selected_programs_excluded_exactly_once","remaining_programs_present_exactly_once","union_with_K508_is_all_936","no_overlap_with_K508")):raise AssertionError("K511 partition failed")
 if p["decision"]["all_916_remaining_faces_executed"]:raise AssertionError("K511 overclaimed execution")
def main():
 a=argparse.ArgumentParser();a.add_argument("--write",action="store_true");x=a.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n";OUTPUT.write_text(s) if x.write else print(s,end="");return 0
if __name__=="__main__":raise SystemExit(main())
