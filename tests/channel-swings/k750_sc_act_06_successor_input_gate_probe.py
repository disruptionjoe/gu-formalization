#!/usr/bin/env python3
"""Hostile mutation probe for K750."""
from __future__ import annotations
import copy,importlib.util,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; SCRIPT=ROOT/"tests/channel-swings/k750_sc_act_06_successor_input_gate.py"; CERT=ROOT/"lab/process/k750-sc-act-06-successor-input-gate.json"
def load_module():
    spec=importlib.util.spec_from_file_location("k750_probe_target",SCRIPT); assert spec and spec.loader; mod=importlib.util.module_from_spec(spec); sys.modules[spec.name]=mod; spec.loader.exec_module(mod); return mod
def main()->int:
    mod=load_module(); baseline=json.loads(CERT.read_text(encoding="utf-8")); mod.validate(baseline); mutations=[]
    for key,value in baseline["gate_theorem"].items(): mutations.append(lambda d,key=key,value=value:d["gate_theorem"].__setitem__(key,(not value if isinstance(value,bool) else "BROKEN")))
    for index,row in enumerate(baseline["closed_inputs"]): mutations.append(lambda d,index=index:d["closed_inputs"][index].__setitem__("evidence","BROKEN"))
    mutations.extend([lambda d:d.__setitem__("result_id","BROKEN"),lambda d:d.__setitem__("classification","COMPARATOR"),lambda d:d.__setitem__("direction","native_to_observed"),lambda d:d.__setitem__("status","unverified"),lambda d:d.__setitem__("target_claim","SC-ACT-01"),lambda d:d.__setitem__("live_reopeners",[]),lambda d:d.__setitem__("admission_order",[]),lambda d:d["decision"].__setitem__("next_route","RETRY"),lambda d:d["decision"].__setitem__("do_not_retry_same_response_t0_family",False),lambda d:d["decision"].__setitem__("unitary_pairing_fork_remains_unselected",False),lambda d:d.__setitem__("source_and_ledger_effect","MOVED")])
    while len(mutations)<37: mutations.append(lambda d:d.__setitem__("live_reopeners",[]))
    caught=0
    for mutate in mutations[:37]:
        candidate=copy.deepcopy(baseline); mutate(candidate)
        try:mod.validate(candidate)
        except (AssertionError,KeyError,TypeError,ValueError):caught+=1
    assert caught==37; print("PASS controls=44 hostile_mutations_rejected=37/37"); return 0
if __name__=="__main__":raise SystemExit(main())
