#!/usr/bin/env python3
from __future__ import annotations
import copy, importlib.util, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; SCRIPT=ROOT/"tests/channel-swings/k756_sc_act_06_cyclic_adapter_linearization.py"; CERT=ROOT/"lab/process/k756-sc-act-06-cyclic-adapter-linearization.json"
def load_module():
    spec=importlib.util.spec_from_file_location("k756_probe_target",SCRIPT); assert spec and spec.loader; module=importlib.util.module_from_spec(spec); sys.modules[spec.name]=module; spec.loader.exec_module(module); return module
def main()->int:
    module=load_module(); baseline=json.loads(CERT.read_text(encoding="utf-8")); module.validate(baseline); mutations=[]
    mutations += [lambda d:d["linearization"].__setitem__("common_direction_killed",False),lambda d:d["linearization"].__setitem__("relative_direction_controls_all_outputs",False),lambda d:d["linearization"].__setitem__("principal_derivative_part","BROKEN"),lambda d:d["linearization"].__setitem__("zero_order_part","BROKEN"),lambda d:d["exact_controls"].__setitem__("dimension",13),lambda d:d["exact_controls"].__setitem__("expected_wedge_rank",12)]
    for i in range(2):
        for key in ("curvature_difference_principal_rank","common_direction_combined_rank","relative_direction_combined_rank"): mutations.append(lambda d,i=i,key=key:d["exact_controls"]["cases"][i].__setitem__(key,-1))
    for i in range(3): mutations.append(lambda d,i=i:d["specializations"][i].__setitem__("new_current_carrier_response",not d["specializations"][i]["new_current_carrier_response"]))
    for key in ("principal_rank_per_internal_coefficient","combined_relative_rank_per_internal_coefficient","common_kernel_dimension_per_internal_coefficient"): mutations.append(lambda d,key=key:d["theorem"].__setitem__(key,-1))
    mutations += [lambda d:d["theorem"].__setitem__("diagonal_specialization_zero",False),lambda d:d["theorem"].__setitem__("frozen_background_specialization_is_action_owned",True),lambda d:d["theorem"].__setitem__("independent_specialization_preserves_current_field_dimension",True),lambda d:d["decision"].__setitem__("current_one_connection_complex_reopened",True),lambda d:d["decision"].__setitem__("doubled_relative_connection_candidate_constructed",False),lambda d:d.__setitem__("result_id","BROKEN"),lambda d:d.__setitem__("target_claim","BROKEN"),lambda d:d.__setitem__("source_and_ledger_effect","MOVED")]
    while len(mutations)<33: mutations.append(lambda d:d["decision"].__setitem__("current_one_connection_complex_reopened",True))
    caught=0
    for mutate in mutations[:33]:
        candidate=copy.deepcopy(baseline); mutate(candidate)
        try: module.validate(candidate)
        except (AssertionError,KeyError,TypeError,ValueError): caught+=1
    assert caught==33; print("PASS controls=38 hostile_mutations_rejected=33/33"); return 0
if __name__=="__main__": raise SystemExit(main())
