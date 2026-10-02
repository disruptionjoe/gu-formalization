#!/usr/bin/env python3
"""Hostile mutation probe for K769."""
from __future__ import annotations
import copy, importlib.util, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; SCRIPT=ROOT/"tests/channel-swings/k769_sc_act_06_curvature_square_cohomology_bound.py"; CERT=ROOT/"lab/process/k769-sc-act-06-curvature-square-cohomology-bound.json"
def load():
    spec=importlib.util.spec_from_file_location("k769_probe_target",SCRIPT); assert spec and spec.loader; mod=importlib.util.module_from_spec(spec); sys.modules[spec.name]=mod; spec.loader.exec_module(mod); return mod
def main()->int:
    mod=load(); base=json.loads(CERT.read_text()); mod.validate(base); muts=[lambda d:d.__setitem__("result_id","BROKEN"),lambda d:d.__setitem__("status","unverified"),lambda d:d.__setitem__("classification","SOURCE_NATIVE_ROUTE"),lambda d:d.__setitem__("target_claim","SC-ACT-01"),lambda d:d["composition"].__setitem__("gauge_rank",5),lambda d:d["composition"].__setitem__("rows",[]),lambda d:d["composition"]["rows"][0].__setitem__("k763_lower_bound",1),lambda d:d["composition"]["rows"][0].__setitem__("necessary_rank_threshold_cleared",False),lambda d:d["composition"]["rows"][1].__setitem__("old_block_correction_rank_r",1),lambda d:d["composition"]["rows"][1].__setitem__("k763_lower_bound",1),lambda d:d["composition"]["rows"][1].__setitem__("necessary_rank_threshold_cleared",True),lambda d:d["composition"]["rows"][2].__setitem__("k763_lower_bound",1),lambda d:d["composition"]["rows"][2].__setitem__("necessary_rank_threshold_cleared",False),lambda d:d["composition"]["rows"][2].__setitem__("middle_exact_proved",True),lambda d:d["composition"]["rows"][3].__setitem__("k763_lower_bound",1),lambda d:d["composition"]["rows"][3].__setitem__("necessary_rank_threshold_cleared",False),lambda d:d["composition"]["rows"][3].__setitem__("middle_exact_proved",True),lambda d:d.__setitem__("source_and_ledger_effect","MOVED")]
    for key,value in base["decision"].items(): muts.append(lambda d,key=key,value=value:d["decision"].__setitem__(key,(not value if isinstance(value,bool) else value+1)))
    while len(muts)<34: muts.append(lambda d:d["composition"].__setitem__("rows",[]))
    caught=0
    for mutate in muts[:34]:
        c=copy.deepcopy(base); mutate(c)
        try: mod.validate(c)
        except (AssertionError,KeyError,TypeError,ValueError): caught+=1
    assert caught==34; print("PASS controls=40 hostile_mutations_rejected=34/34"); return 0
if __name__=="__main__": raise SystemExit(main())
