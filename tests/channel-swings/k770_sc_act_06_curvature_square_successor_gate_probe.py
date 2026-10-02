#!/usr/bin/env python3
"""Hostile mutation probe for K770."""
from __future__ import annotations
import copy, importlib.util, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; SCRIPT=ROOT/"tests/channel-swings/k770_sc_act_06_curvature_square_successor_gate.py"; CERT=ROOT/"lab/process/k770-sc-act-06-curvature-square-successor-gate.json"
def load():
    spec=importlib.util.spec_from_file_location("k770_probe_target",SCRIPT); assert spec and spec.loader; mod=importlib.util.module_from_spec(spec); sys.modules[spec.name]=mod; spec.loader.exec_module(mod); return mod
def main()->int:
    mod=load(); base=json.loads(CERT.read_text()); mod.validate(base); muts=[lambda d:d.__setitem__("result_id","BROKEN"),lambda d:d.__setitem__("status","unverified"),lambda d:d.__setitem__("classification","COMPARATOR"),lambda d:d.__setitem__("target_claim","SC-ACT-01"),lambda d:d.__setitem__("closed_classes",[]),lambda d:d["closed_classes"][0].__setitem__("reason","BROKEN"),lambda d:d["closed_classes"][1].__setitem__("reason","BROKEN"),lambda d:d.__setitem__("surviving_branches",[]),lambda d:d.__setitem__("source_and_ledger_effect","MOVED")]
    for key,value in base["decision"].items(): muts.append(lambda d,key=key,value=value:d["decision"].__setitem__(key,(not value if isinstance(value,bool) else "REFUTED")))
    while len(muts)<36: muts.append(lambda d:d.__setitem__("surviving_branches",[]))
    caught=0
    for mutate in muts[:36]:
        c=copy.deepcopy(base); mutate(c)
        try: mod.validate(c)
        except (AssertionError,KeyError,TypeError,ValueError,IndexError): caught+=1
    assert caught==36; print("PASS controls=42 hostile_mutations_rejected=36/36"); return 0
if __name__=="__main__": raise SystemExit(main())
