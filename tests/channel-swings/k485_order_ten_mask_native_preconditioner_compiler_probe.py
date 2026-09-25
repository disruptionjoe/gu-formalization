#!/usr/bin/env python3
"""Stored-invariant and optional exhaustive replay probe for K485."""
import argparse, copy, importlib.util, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; PRODUCER=ROOT/"tests/channel-swings/k485_order_ten_mask_native_preconditioner_compiler.py"; STORED=ROOT/"lab/process/k485-order-ten-mask-native-preconditioner-compiler.json"
spec=importlib.util.spec_from_file_location("k485_probe_target",PRODUCER); module=importlib.util.module_from_spec(spec); sys.modules[spec.name]=module; spec.loader.exec_module(module)
def main():
 p=argparse.ArgumentParser(); p.add_argument("--rebuild",action="store_true"); a=p.parse_args(); s=json.loads(STORED.read_text()); module.validate_payload(s)
 checks=[s["fixed_control"]["ordered_descriptors"]==13300,s["fixed_control"]["reachable_face_instances"]==936,s["fixed_control"]["determinant_matrix_face_uses_replayed"]==49544352,len(s["preconditioner_templates"])==60,len(s["confluent_divided_difference_contract"]["templates"])==75,s["template_summary"]["all_strong_duality_checks_pass"],s["template_summary"]["maximum_determinant_rank"]==5,all(s["release_test"].values())]
 if a.rebuild: checks.append(s==module.build())
 if not all(checks): raise AssertionError("K485 control failed")
 mutations=[lambda x:x["fixed_control"].__setitem__("ordered_descriptors",13299),lambda x:x["fixed_control"].__setitem__("reachable_face_instances",0),lambda x:x["template_summary"].__setitem__("all_strong_duality_checks_pass",False),lambda x:x["decision"].__setitem__("complete_face_normal_integrability_emitted",True),lambda x:x["decision"].__setitem__("recursive_numerical_cover_complete",True),lambda x:x["release_test"].__setitem__("all_60_singular_templates_present",False),lambda x:x["release_test"].__setitem__("all_75_confluent_templates_present",False),lambda x:x["release_test"].__setitem__("native_K152_interval_not_emitted",False)]
 rejected=0
 for mutate in mutations:
  c=copy.deepcopy(s); mutate(c)
  try: module.validate_payload(c)
  except AssertionError: rejected+=1
 if rejected!=len(mutations): raise AssertionError(f"K485 hostile rejection failed: {rejected}/{len(mutations)}")
 print(f"K485 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations"); return 0
if __name__=="__main__": raise SystemExit(main())
