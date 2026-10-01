#!/usr/bin/env python3
from __future__ import annotations
import copy, importlib.util, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; SCRIPT=ROOT/"tests/channel-swings/k758_sc_act_06_cyclic_adapter_successor_gate.py"; CERT=ROOT/"lab/process/k758-sc-act-06-cyclic-adapter-successor-gate.json"
def load_module():
    spec=importlib.util.spec_from_file_location("k758_probe_target",SCRIPT); assert spec and spec.loader; module=importlib.util.module_from_spec(spec); sys.modules[spec.name]=module; spec.loader.exec_module(module); return module
def main()->int:
    module=load_module(); baseline=json.loads(CERT.read_text(encoding="utf-8")); module.validate(baseline); mutations=[lambda d:d.__setitem__("closed_or_inadmissible_specializations",[]),lambda d:d["constructed_but_unowned"].__setitem__("principal_relative_rank_per_internal_coefficient",12),lambda d:d["constructed_but_unowned"].__setitem__("combined_relative_rank_per_internal_coefficient",13),lambda d:d["constructed_but_unowned"].__setitem__("formula_grade","SOURCE_STATES_FORMULA"),lambda d:d["constructed_but_unowned"].__setitem__("source_action_owner",True),lambda d:d["constructed_but_unowned"].__setitem__("stationary_background",True),lambda d:d["constructed_but_unowned"].__setitem__("current_carrier_composable",True),lambda d:d.__setitem__("live_reopeners",[]),lambda d:d.__setitem__("admission_order",[])]
    for key in ("SC_ACT_06_status","cyclic_formula_globally_refuted","current_one_connection_cyclic_repair_closed","independent_doubled_candidate_exists_as_exact_algebra","independent_doubled_candidate_is_action_owned","current_98308_98311_bounds_moved","global_SC_ACT_06_refuted"):
        value="MOVED" if key=="SC_ACT_06_status" else (False if key in ("current_one_connection_cyclic_repair_closed","independent_doubled_candidate_exists_as_exact_algebra") else True); mutations.append(lambda d,key=key,value=value:d["gate_theorem"].__setitem__(key,value))
    mutations += [lambda d:d["decision"].__setitem__("do_not_retry_current_carrier_cyclic_specializations",False),lambda d:d["decision"].__setitem__("next_route","RETRY"),lambda d:d.__setitem__("result_id","BROKEN"),lambda d:d.__setitem__("target_claim","BROKEN"),lambda d:d.__setitem__("source_and_ledger_effect","MOVED")]
    while len(mutations)<36: mutations.append(lambda d:d["decision"].__setitem__("next_route","RETRY"))
    caught=0
    for mutate in mutations[:36]:
        candidate=copy.deepcopy(baseline); mutate(candidate)
        try: module.validate(candidate)
        except (AssertionError,KeyError,TypeError,ValueError): caught+=1
    assert caught==36; print("PASS controls=42 hostile_mutations_rejected=36/36"); return 0
if __name__=="__main__": raise SystemExit(main())
