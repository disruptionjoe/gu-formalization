#!/usr/bin/env python3
"""Stored-invariant and optional exhaustive replay probe for K486."""
import argparse, copy, importlib.util, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; PRODUCER=ROOT/"tests/channel-swings/k486_order_ten_face_normal_integrability_atlas.py"; STORED=ROOT/"lab/process/k486-order-ten-face-normal-integrability-atlas.json"
spec=importlib.util.spec_from_file_location("k486_probe_target",PRODUCER); module=importlib.util.module_from_spec(spec); sys.modules[spec.name]=module; spec.loader.exec_module(module)
def main():
 p=argparse.ArgumentParser(); p.add_argument("--rebuild",action="store_true"); a=p.parse_args(); s=json.loads(STORED.read_text()); module.validate_payload(s)
 checks=[s["fixed_control"]["hybrid_terms"]==22,s["fixed_control"]["ordered_descriptors_per_face"]==13300,s["fixed_control"]["reachable_face_instances"]==936,s["fixed_control"]["descriptor_face_replays"]==12448800,len(s["face_normal_atlas"])==936,s["atlas_summary"]["all_faces_locally_integrable"],s["atlas_summary"]["global_minimum_face_normal_power"]==0,all(s["release_test"].values())]
 if a.rebuild: checks.append(s==module.build())
 if not all(checks): raise AssertionError("K486 control failed")
 mutations=[lambda x:x["fixed_control"].__setitem__("hybrid_terms",21),lambda x:x["fixed_control"].__setitem__("ordered_descriptors_per_face",13299),lambda x:x["fixed_control"].__setitem__("reachable_face_instances",935),lambda x:x["atlas_summary"].__setitem__("all_faces_locally_integrable",False),lambda x:x["decision"].__setitem__("complete_reachable_face_normal_integrability_closed",False),lambda x:x["decision"].__setitem__("complete_hybrid_integrals_emitted",True),lambda x:x["release_test"].__setitem__("all_936_faces_present",False),lambda x:x["release_test"].__setitem__("native_K152_interval_not_emitted",False)]
 rejected=0
 for mutate in mutations:
  c=copy.deepcopy(s); mutate(c)
  try: module.validate_payload(c)
  except AssertionError: rejected+=1
 if rejected!=len(mutations): raise AssertionError(f"K486 hostile rejection failed: {rejected}/{len(mutations)}")
 print(f"K486 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations"); return 0
if __name__=="__main__": raise SystemExit(main())
