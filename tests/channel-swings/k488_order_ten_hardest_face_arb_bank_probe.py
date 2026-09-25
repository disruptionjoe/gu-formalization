#!/usr/bin/env python3
"""Stored-invariant and optional exhaustive Arb replay probe for K488."""
import argparse, copy, importlib.util, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; PRODUCER=ROOT/"tests/channel-swings/k488_order_ten_hardest_face_arb_bank.py"; STORED=ROOT/"lab/process/k488-order-ten-hardest-face-arb-bank.json"
spec=importlib.util.spec_from_file_location("k488_probe_target",PRODUCER); module=importlib.util.module_from_spec(spec); sys.modules[spec.name]=module; spec.loader.exec_module(module)
def main():
 p=argparse.ArgumentParser(); p.add_argument("--rebuild",action="store_true"); a=p.parse_args(); s=json.loads(STORED.read_text()); module.validate_payload(s); rows=s["hardest_face_arb_controls"]
 checks=[len(rows)==22,sum(len(r["controls"]) for r in rows)==66,s["fixed_control"]["ordered_descriptor_control_evaluations"]==877800,all(c["coherent_group_count"]==28 for r in rows for c in r["controls"]),all(float(c["minimum_cumulative_argument_lower"])>0 for r in rows for c in r["controls"]),s["execution_contract"]["all_28_coherent_groups_assembled_before_reported_enclosure"],s["execution_contract"]["controls_are_not_face_intervals"],not s["execution_contract"]["raw_Bessel_evaluation_at_zero_used"],all(s["release_test"].values())]
 if a.rebuild: checks.append(s==module.build())
 if not all(checks): raise AssertionError("K488 control failed")
 mutations=[lambda x:x["fixed_control"].__setitem__("complete_arb_controls",65),lambda x:x["fixed_control"].__setitem__("ordered_descriptor_control_evaluations",877799),lambda x:x["hardest_face_arb_controls"].pop(),lambda x:x["hardest_face_arb_controls"][0]["controls"].pop(),lambda x:x["hardest_face_arb_controls"][0]["controls"][0].__setitem__("coherent_group_count",27),lambda x:x["hardest_face_arb_controls"][0]["controls"][0].__setitem__("minimum_cumulative_argument_lower","0"),lambda x:x["decision"].__setitem__("all_936_faces_numerically_evaluated",True),lambda x:x["decision"].__setitem__("complete_hybrid_integrals_emitted",True),lambda x:x["release_test"].__setitem__("native_K152_interval_not_emitted",False)]
 rejected=0
 for mutate in mutations:
  c=copy.deepcopy(s); mutate(c)
  try: module.validate_payload(c)
  except AssertionError: rejected+=1
 if rejected!=len(mutations): raise AssertionError(f"K488 hostile rejection failed: {rejected}/{len(mutations)}")
 print(f"K488 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations"); return 0
if __name__=="__main__": raise SystemExit(main())
