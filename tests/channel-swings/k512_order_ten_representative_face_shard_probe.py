#!/usr/bin/env python3
"""Probe and hostile mutations for stored K512."""
from __future__ import annotations
import copy,importlib.util,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];H=Path(__file__).resolve().parent;OUT=ROOT/"lab/process/k512-order-ten-representative-face-shard.json"
s=importlib.util.spec_from_file_location("k512",H/"k512_order_ten_representative_face_shard.py");K=importlib.util.module_from_spec(s);s.loader.exec_module(K)
def main():
 p=json.loads(OUT.read_text());f=p["fixed_control"];b=p["bank_summary"];d=p["decision"]
 checks=[p["result_id"]=="K512-ORDER-TEN-REPRESENTATIVE-FACE-SHARD",f["shard_id"]=="order10-face-000",f["program_count"]==4,f["complete_positive_width_cells"]==28,f["ordered_descriptor_cell_evaluations"]==372400,b["all_four_programs_executed"],b["all_28_cells_finite"],b["every_cell_has_positive_argument_floor"],b["all_four_direct_overlaps_pass"],d["representative_shard_released"],d["unexecuted_remaining_face_programs"]==912,d["all_916_remaining_faces_executed"] is False,p["measurement"]["wall_seconds_observed"]>0,p["source_and_ledger_effect"]=="none"]
 n=0
 for m in [lambda q:q["fixed_control"].__setitem__("complete_positive_width_cells",27),lambda q:q["bank_summary"].__setitem__("all_28_cells_finite",False),lambda q:q["bank_summary"].__setitem__("every_cell_has_positive_argument_floor",False),lambda q:q["decision"].__setitem__("representative_shard_released",False),lambda q:q["decision"].__setitem__("all_916_remaining_faces_executed",True),lambda q:q["decision"].__setitem__("full_projective_normal_cone_complete",True)]:
  h=copy.deepcopy(p);m(h)
  try:K.validate(h)
  except AssertionError:n+=1
 print(f"K512 controls: {sum(checks)}/{len(checks)}; hostile: {n}/6");return 0 if all(checks) and n==6 else 1
if __name__=="__main__":raise SystemExit(main())
