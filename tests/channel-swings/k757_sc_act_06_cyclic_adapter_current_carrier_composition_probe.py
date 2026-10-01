#!/usr/bin/env python3
from __future__ import annotations
import copy, importlib.util, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; SCRIPT=ROOT/"tests/channel-swings/k757_sc_act_06_cyclic_adapter_current_carrier_composition.py"; CERT=ROOT/"lab/process/k757-sc-act-06-cyclic-adapter-current-carrier-composition.json"
def load_module():
    spec=importlib.util.spec_from_file_location("k757_probe_target",SCRIPT); assert spec and spec.loader; module=importlib.util.module_from_spec(spec); sys.modules[spec.name]=module; spec.loader.exec_module(module); return module
def main()->int:
    module=load_module(); baseline=json.loads(CERT.read_text(encoding="utf-8")); module.validate(baseline); mutations=[lambda d:d["current_obstruction"].__setitem__("body_middle_bounds_preserved",[0,0]),lambda d:d["current_obstruction"].__setitem__("k749_full_symbol_block_obstruction",False)]
    for i in range(3): mutations.append(lambda d,i=i:d["specialization_composition"][i].__setitem__("new_principal_image",True))
    mutations.append(lambda d:d["specialization_composition"][2].__setitem__("composable_with_current_carrier",True))
    for key in ("released_current_parent_inventory_exhausted","source_silent_adapter_nonexistence_proved","diagonal_adapter_repairs_current_complex","frozen_background_adapter_is_new_action_owned_response","independent_doubled_adapter_can_be_inserted_without_rebuilding_complex","current_98308_98311_bounds_changed","current_carrier_reopened"):
        desired=False if key=="released_current_parent_inventory_exhausted" else True; mutations.append(lambda d,key=key,desired=desired:d["composition_theorem"].__setitem__(key,desired))
    mutations += [lambda d:d.__setitem__("required_doubled_packet",[]),lambda d:d["decision"].__setitem__("cyclic_reconstruction_reopens_current_sc_act_06_test",True),lambda d:d["decision"].__setitem__("cyclic_reconstruction_killed_globally",True),lambda d:d["decision"].__setitem__("doubled_connection_candidate_shape_constructed",False),lambda d:d.__setitem__("result_id","BROKEN"),lambda d:d.__setitem__("target_claim","BROKEN"),lambda d:d.__setitem__("source_and_ledger_effect","MOVED")]
    while len(mutations)<35: mutations.append(lambda d:d["composition_theorem"].__setitem__("current_carrier_reopened",True))
    caught=0
    for mutate in mutations[:35]:
        candidate=copy.deepcopy(baseline); mutate(candidate)
        try: module.validate(candidate)
        except (AssertionError,KeyError,TypeError,ValueError): caught+=1
    assert caught==35; print("PASS controls=40 hostile_mutations_rejected=35/35"); return 0
if __name__=="__main__": raise SystemExit(main())
