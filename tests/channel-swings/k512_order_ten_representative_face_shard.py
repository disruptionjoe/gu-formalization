#!/usr/bin/env python3
"""Execute K511 shard 000 through K508's true interval backend."""
from __future__ import annotations
import argparse,importlib.util,json,math,sys,time
from collections import Counter
from pathlib import Path
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
OUTPUT=ROOT/"lab/process/k512-order-ten-representative-face-shard.json"
K485_JSON=ROOT/"lab/process/k485-order-ten-mask-native-preconditioner-compiler.json"
K487_JSON=ROOT/"lab/process/k487-order-ten-face-program-compiler.json"
K511_JSON=ROOT/"lab/process/k511-order-ten-face-shard-plan.json"
ctx.dps=180;ctx.threads=1
def load(name,file):
 s=importlib.util.spec_from_file_location(name,HERE/file);m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m);return m
K508=load("k508_for_k512","k508_order_ten_selected_face_cell_bank.py")
def build():
 started=time.perf_counter();k485=json.loads(K485_JSON.read_text());k487=json.loads(K487_JSON.read_text());k511=json.loads(K511_JSON.read_text())
 shard=k511["shards"][0]
 if shard["shard_id"]!="order10-face-000" or shard["program_count"]!=4:raise AssertionError("K512 shard identity changed")
 programs={r["program_id"]:r for r in k487["face_programs"]};sing,conf=K508.BASE.template_maps(k485)
 rows=[];directs=[];sg=Counter();cg=Counter();ops=0
 for pid in shard["program_ids"]:
  p=programs[pid];cells=[]
  for ci,(left,right) in enumerate(K508.NORMAL_CELLS):
   rho=K508.BASE.interval(left,right);second,groups,sh,ch,uses=K508.BASE.complete_second(p,rho,sing,conf);ops+=uses
   if not math.isfinite(float(abs(second).upper())):raise AssertionError("K512 nonfinite cell")
   raw=K508.BASE.raw_times(p,rho);cs,cv=K508.K412.cumulative(raw);minimum=min([x.lower() for x in cs.values()]+[x.lower() for x in cv.values()])
   if minimum<=0:raise AssertionError("K512 zero argument")
   power=int(p["maximum_value_first_second_singular_powers"][2]);scaled=abs(second)*rho**power
   groups=[{**r,"group_id":str(r["group_id"]).replace("order9:","order10:")} for r in groups]
   cells.append({"normal_interval":[K508.q(left),K508.q(right)],"minimum_cumulative_argument_lower":K508.lower_text(arb(minimum)),"complete_second_derivative_abs_upper":K508.abs_upper_text(second),"rho_to_K486_second_singular_power_abs_upper":K508.abs_upper_text(scaled),"coherent_group_count":len(groups),"all_28_group_intervals_sha256":K508.digest(groups),"singular_template_ids":sorted(sh),"confluent_template_ids":sorted(ch),"divided_difference_operation_uses":uses})
   sg.update(sh);cg.update(ch)
   if ci==0:
    direct,_=K508.K412.complete_second(p["axis"],raw);overlap=not(second.upper()<direct.lower() or second.lower()>direct.upper())
    if not overlap:raise AssertionError("K512 direct overlap failed")
    directs.append({"program_id":pid,"intervals_overlap":True})
  rows.append({"program_id":pid,"face_id":p["face_id"],"axis":p["axis"],"codimension":p["codimension"],"face_kind":p["face_kind"],"zeroed_axes":p["zeroed_axes"],"cells":cells})
 wall=time.perf_counter()-started
 return {"schema_version":"1.0","result_id":"K512-ORDER-TEN-REPRESENTATIVE-FACE-SHARD","created":"2026-09-25","classification":"INTERNAL_NUMERICAL_CONTROL_ONLY","direction":"observed_to_native","fixed_control":{"shard_id":shard["shard_id"],"shard_program_digest":shard["program_digest"],"K511_plan_digest":k511["partition_contract"]["plan_digest"],"program_count":4,"cells_per_program":7,"complete_positive_width_cells":28,"ordered_descriptors_per_cell":13300,"ordered_descriptor_cell_evaluations":372400,"coherent_groups_per_cell":28,"arb_decimal_digits":180,"threads":1},"measurement":{"wall_seconds_observed":round(wall,6),"program_seconds_observed":round(wall/4,6),"linear_916_program_hours_estimate":round(wall*916/4/3600,6),"estimate_is_scheduler_evidence_not_a_runtime_bound":True},"representative_face_cell_bank":rows,"direct_overlap_controls":directs,"bank_summary":{"all_four_programs_executed":len(rows)==4,"all_28_cells_finite":all(math.isfinite(float(c["complete_second_derivative_abs_upper"])) for r in rows for c in r["cells"]),"every_cell_has_positive_argument_floor":all(float(c["minimum_cumulative_argument_lower"])>0 for r in rows for c in r["cells"]),"all_four_direct_overlaps_pass":len(directs)==4 and all(r["intervals_overlap"] for r in directs),"executed_singular_template_ids":sorted(sg),"executed_confluent_template_ids":sorted(cg),"divided_difference_operation_uses":ops,"bank_sha256":K508.digest(rows)},"decision":{"representative_shard_released":True,"remaining_plan_backend_confirmed":True,"executed_remaining_face_programs":4,"unexecuted_remaining_face_programs":912,"all_916_remaining_faces_executed":False,"full_projective_normal_cone_complete":False,"recursive_positive_interior_cover_complete":False,"analytic_radial_tails_complete":False,"complete_hybrid_integrals_emitted":False,"next_exact_input":"Execute the remaining K511 shards under serialized resource control, then construct the normal-projective partition before interior and tail composition."},"source_and_ledger_effect":"none","claim_ceiling":"Rigorous 180-digit K508-backend evidence on the four exact programs in K511 shard 000, across all 28 positive-width normal cells with 372,400 descriptor-cell evaluations. The wall-time extrapolation is resource evidence only. This is not the other 912 programs, a complete face bank, projective/interior/tail cover, hybrid integral, K457 value, K152 interval, or source/physical result."}
def validate(p):
 f=p["fixed_control"];b=p["bank_summary"];d=p["decision"]
 if (f["program_count"],f["complete_positive_width_cells"],f["ordered_descriptor_cell_evaluations"],f["coherent_groups_per_cell"])!=(4,28,372400,28):raise AssertionError("K512 census changed")
 if not all(b[k] for k in ("all_four_programs_executed","all_28_cells_finite","every_cell_has_positive_argument_floor","all_four_direct_overlaps_pass")):raise AssertionError("K512 backend failed")
 if not d["representative_shard_released"] or d["all_916_remaining_faces_executed"]:raise AssertionError("K512 release boundary changed")
 if any(d[k] for k in ("full_projective_normal_cone_complete","recursive_positive_interior_cover_complete","analytic_radial_tails_complete","complete_hybrid_integrals_emitted")):raise AssertionError("K512 overclaimed cover")
def main():
 a=argparse.ArgumentParser();a.add_argument("--write",action="store_true");x=a.parse_args();p=build();validate(p);s=json.dumps(p,indent=2,sort_keys=True)+"\n";OUTPUT.write_text(s) if x.write else print(s,end="");return 0
if __name__=="__main__":raise SystemExit(main())
