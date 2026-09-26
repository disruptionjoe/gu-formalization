#!/usr/bin/env python3
"""Probe and hostile mutations for K511."""
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k511",H/"k511_order_ten_face_shard_plan.py");K=importlib.util.module_from_spec(s);s.loader.exec_module(K)
def main():
 p=K.build();f=p["fixed_control"];c=p["partition_contract"];d=p["decision"]
 checks=[p["result_id"]=="K511-ORDER-TEN-FACE-SHARD-PLAN",f["remaining_programs"]==916,f["shard_count"]==229,f["last_shard_size"]==4,len(p["shards"])==229,all(s["program_count"]==4 for s in p["shards"]),c["remaining_programs_present_exactly_once"],c["union_with_K508_is_all_936"],c["no_overlap_with_K508"],d["remaining_face_work_now_has_exact_shards"],d["all_916_remaining_faces_executed"] is False,p["source_and_ledger_effect"]=="none"]
 n=0
 for m in [lambda q:q["fixed_control"].__setitem__("remaining_programs",915),lambda q:q["partition_contract"].__setitem__("remaining_programs_present_exactly_once",False),lambda q:q["partition_contract"].__setitem__("union_with_K508_is_all_936",False),lambda q:q["partition_contract"].__setitem__("no_overlap_with_K508",False),lambda q:q["decision"].__setitem__("all_916_remaining_faces_executed",True)]:
  h=copy.deepcopy(p);m(h)
  try:K.validate(h)
  except AssertionError:n+=1
 print(f"K511 controls: {sum(checks)}/{len(checks)}; hostile: {n}/5");return 0 if all(checks) and n==5 else 1
if __name__=="__main__":raise SystemExit(main())
