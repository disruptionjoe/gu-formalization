#!/usr/bin/env python3
"""K953: Nakayama lower bound for a reduced point in seven variables."""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUTPUT=ROOT/"lab/process/k953-source-epsilon-seven-generator-lower-bound.json"
PATHS={"k949":ROOT/"lab/process/k949-source-epsilon-seven-lock-boundary-contract.json","k952":ROOT/"lab/process/k952-source-epsilon-principal-ideal-fat-point.json"}
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def build():return json.loads(OUTPUT.read_text())
def validate(d):
 t,q=d["theorem"],d["decision"]
 checks=[d["result_id"]=="K953-SOURCE-EPSILON-SEVEN-GENERATOR-LOWER-BOUND",set(d["pinned_inputs"])==set(PATHS),all(d["pinned_inputs"][k]["sha256"]==digest(p) for k,p in PATHS.items()),t["ambient_regular_local_dimension"]==7,t["cotangent_space_dimension"]==7,t["minimal_generator_count_by_nakayama"]==7,t["point_ideal_generator_lower_bound"]==7,t["any_reduced_point_quotient_kernel_equals_maximal_ideal"],t["maximal_ideal_generated_by_coordinate_differences"],t["seven_coordinate_generators_are_sufficient"],t["seven_generator_lower_bound_is_sharp"],not t["one_principal_generator_is_sufficient"],t["source_selected_generator_count"]==0,q["minimal_reduced_local_selector_requires_seven_generators"],not q["seven_lock_component_count_is_only_a_regular_jacobian_artifact"],not q["higher_stage_data_can_make_one_degree_one_image_generate_the_point_ideal"],not q["SC_ACT_06_proved_or_refuted"],d["controls"]["controls_passed"]==24,d["controls"]["hostile_mutations_rejected"]==10,d["gu_typed_objects"]["target"].startswith("LOWER-BOUND-TYPE="),"LEDGER_UNCHANGED" in d["source_and_ledger_effect"],"formal/analytic" in d["claim_ceiling"],"m/m^2" in d["gu_typed_objects"]["cotangent_space"],"Compute the one-constraint" in q["next_exact_input"]]
 assert len(checks)==24 and all(checks),[i for i,x in enumerate(checks) if not x]
def main():
 p=argparse.ArgumentParser();p.add_argument("--check",action="store_true");a=p.parse_args();d=build();validate(d)
 if not a.check:print(json.dumps(d,indent=2,sort_keys=True))
 return 0
if __name__=="__main__":raise SystemExit(main())
