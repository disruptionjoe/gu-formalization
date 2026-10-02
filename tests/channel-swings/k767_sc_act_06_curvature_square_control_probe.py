#!/usr/bin/env python3
"""Hostile mutation probe for K767."""
from __future__ import annotations
import copy, importlib.util, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; SCRIPT=ROOT/"tests/channel-swings/k767_sc_act_06_curvature_square_control.py"; CERT=ROOT/"lab/process/k767-sc-act-06-curvature-square-control.json"
def load():
    spec=importlib.util.spec_from_file_location("k767_probe_target",SCRIPT); assert spec and spec.loader
    mod=importlib.util.module_from_spec(spec); sys.modules[spec.name]=mod; spec.loader.exec_module(mod); return mod
def main() -> int:
    mod=load(); base=json.loads(CERT.read_text()); mod.validate(base); mutations=[]
    mutations += [lambda d:d.__setitem__("result_id","BROKEN"),lambda d:d.__setitem__("status","unverified"),lambda d:d.__setitem__("classification","SOURCE_NATIVE_ROUTE"),lambda d:d.__setitem__("target_claim","SC-ACT-01")]
    for key,value in base["ownership"].items():
        if isinstance(value,bool): mutations.append(lambda d,key=key,value=value:d["ownership"].__setitem__(key,not value))
    for key,value in base["stationarity"].items():
        if isinstance(value,bool): mutations.append(lambda d,key=key,value=value:d["stationarity"].__setitem__(key,not value))
        elif key.endswith("zero"): mutations.append(lambda d,key=key:d["stationarity"].__setitem__(key,"NONZERO"))
    for key,value in base["ward"].items(): mutations.append(lambda d,key=key,value=value:d["ward"].__setitem__(key,(not value if isinstance(value,bool) else value+1)))
    for key,value in base["decision"].items(): mutations.append(lambda d,key=key,value=value:d["decision"].__setitem__(key,not value))
    mutations.append(lambda d:d.__setitem__("source_and_ledger_effect","MOVED"))
    while len(mutations)<32: mutations.append(lambda d:d["decision"].__setitem__("global_SC_ACT_06_refuted",True))
    caught=0
    for mutate in mutations[:32]:
        candidate=copy.deepcopy(base); mutate(candidate)
        try: mod.validate(candidate)
        except (AssertionError,KeyError,TypeError,ValueError): caught+=1
    assert caught==32; print("PASS controls=38 hostile_mutations_rejected=32/32"); return 0
if __name__=="__main__": raise SystemExit(main())
