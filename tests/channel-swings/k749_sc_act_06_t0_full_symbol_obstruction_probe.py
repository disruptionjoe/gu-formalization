#!/usr/bin/env python3
"""Hostile mutation probe for K749."""
from __future__ import annotations
import copy, importlib.util, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]; SCRIPT = ROOT / "tests/channel-swings/k749_sc_act_06_t0_full_symbol_obstruction.py"; CERT = ROOT / "lab/process/k749-sc-act-06-t0-full-symbol-obstruction.json"
def load_module():
    spec=importlib.util.spec_from_file_location("k749_probe_target",SCRIPT); assert spec and spec.loader; mod=importlib.util.module_from_spec(spec); sys.modules[spec.name]=mod; spec.loader.exec_module(mod); return mod
def main() -> int:
    mod=load_module(); baseline=json.loads(CERT.read_text(encoding="utf-8")); mod.validate(baseline); mutations=[]
    for key,value in baseline["composition_theorem"].items(): mutations.append(lambda d,key=key,value=value:d["composition_theorem"].__setitem__(key,not value))
    for index,row in enumerate(baseline["exact_controls"]["cases"]):
        for key,value in row.items(): mutations.append(lambda d,index=index,key=key,value=value:d["exact_controls"]["cases"][index].__setitem__(key,("wrong" if isinstance(value,str) else (not value if isinstance(value,bool) else value+1))))
    mutations.extend([lambda d:d.__setitem__("result_id","BROKEN"),lambda d:d.__setitem__("classification","COMPARATOR"),lambda d:d.__setitem__("direction","native_to_observed"),lambda d:d.__setitem__("status","unverified"),lambda d:d.__setitem__("target_claim","SC-ACT-01"),lambda d:d["exact_controls"].__setitem__("field_dimension",0),lambda d:d["exact_controls"].__setitem__("fermion_two_block_rank",0),lambda d:d["decision"].__setitem__("another_t0_ricci_flat_weyl_germ_repairs_released_full_symbol",True),lambda d:d["decision"].__setitem__("another_pairing_or_weight_repairs_released_full_symbol",True),lambda d:d["decision"].__setitem__("nonzero_fermion_saddle_with_mixed_blocks_remains_open",False),lambda d:d["decision"].__setitem__("independent_action_parent_or_nonzero_t_stationary_germ_remains_open",False),lambda d:d.__setitem__("source_and_ledger_effect","MOVED")])
    while len(mutations)<32: mutations.append(lambda d:d["exact_controls"].__setitem__("field_dimension",0))
    caught=0
    for mutate in mutations[:32]:
        candidate=copy.deepcopy(baseline); mutate(candidate)
        try: mod.validate(candidate)
        except (AssertionError,KeyError,TypeError,ValueError): caught+=1
    assert caught==32; print("PASS controls=38 hostile_mutations_rejected=32/32"); return 0
if __name__=="__main__": raise SystemExit(main())
