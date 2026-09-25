#!/usr/bin/env python3
"""Stored-invariant and optional exhaustive replay probe for K487."""
import argparse, copy, importlib.util, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; PRODUCER=ROOT/"tests/channel-swings/k487_order_ten_face_program_compiler.py"; STORED=ROOT/"lab/process/k487-order-ten-face-program-compiler.json"
spec=importlib.util.spec_from_file_location("k487_probe_target",PRODUCER); module=importlib.util.module_from_spec(spec); sys.modules[spec.name]=module; spec.loader.exec_module(module)
def main():
 p=argparse.ArgumentParser(); p.add_argument("--rebuild",action="store_true"); a=p.parse_args(); s=json.loads(STORED.read_text()); module.validate_payload(s)
 checks=[len(s["face_programs"])==936,s["fixed_control"]["descriptor_face_programs"]==12448800,s["fixed_control"]["determinant_matrix_face_programs"]==49544352,len(s["selected_boundary_or_interior_program_per_hybrid"])==22,[r["axis"] for r in s["positive_interior_fallback_programs"]]==["v10","v11"],set(s["program_summary"]["global_singular_template_histogram"])=={f"S{i:02d}" for i in range(60)},set(s["program_summary"]["global_confluent_template_histogram"])=={f"C{i:02d}" for i in range(75)},s["approach_chart_contract"]["complete_coherent_assembly_required"],not s["approach_chart_contract"]["raw_Bessel_evaluation_at_zero_used"],all(s["release_test"].values())]
 if a.rebuild: checks.append(s==module.build())
 if not all(checks): raise AssertionError("K487 control failed")
 mutations=[lambda x:x["fixed_control"].__setitem__("hybrid_terms",21),lambda x:x["fixed_control"].__setitem__("ordered_descriptors_per_face",13299),lambda x:x["fixed_control"].__setitem__("reachable_face_instances",935),lambda x:x["selected_boundary_or_interior_program_per_hybrid"].pop(),lambda x:x["positive_interior_fallback_programs"].pop(),lambda x:x["release_test"].__setitem__("all_936_face_instances_present",False),lambda x:x["release_test"].__setitem__("all_60_singular_templates_resolved",False),lambda x:x["release_test"].__setitem__("native_K152_interval_not_emitted",False)]
 rejected=0
 for mutate in mutations:
  c=copy.deepcopy(s); mutate(c)
  try: module.validate_payload(c)
  except AssertionError: rejected+=1
 if rejected!=len(mutations): raise AssertionError(f"K487 hostile rejection failed: {rejected}/{len(mutations)}")
 print(f"K487 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations"); return 0
if __name__=="__main__": raise SystemExit(main())
