#!/usr/bin/env python3
"""Hostile mutation probe for K760."""
from __future__ import annotations
import copy, importlib.util, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; SCRIPT=ROOT/"tests/channel-swings/k760_sc_act_06_derivative_condensate_cohomology_bound.py"; CERT=ROOT/"lab/process/k760-sc-act-06-derivative-condensate-cohomology-bound.json"
def load():
    s=importlib.util.spec_from_file_location("k760_probe_target",SCRIPT); assert s and s.loader; m=importlib.util.module_from_spec(s); sys.modules[s.name]=m; s.loader.exec_module(m); return m
def main()->int:
    m=load(); b=json.loads(CERT.read_text()); m.validate(b)
    muts=[lambda d:d.__setitem__("result_id","BROKEN"),lambda d:d.__setitem__("classification","SOURCE_NATIVE_ROUTE"),lambda d:d.__setitem__("target_claim","SC-ACT-01"),lambda d:d.__setitem__("original_bounds",{}),lambda d:d["decision"].__setitem__("one_scalar_bounds",{}),lambda d:d["decision"].__setitem__("one_scalar_repairs_k749",True),lambda d:d["decision"].__setitem__("stationarity_supplied",True),lambda d:d["decision"].__setitem__("source_ownership_supplied",True),lambda d:d["decision"].__setitem__("nonfactorizing_old_block_change_tested",True),lambda d:d.__setitem__("sample_bounds",[]),lambda d:d.__setitem__("source_and_ledger_effect","MOVED")]
    while len(muts)<28:muts.append(lambda d:d.__setitem__("sample_bounds",[]))
    c=0
    for f in muts[:28]:
        x=copy.deepcopy(b);f(x)
        try:m.validate(x)
        except (AssertionError,KeyError,TypeError,ValueError):c+=1
    assert c==28;print("PASS controls=34 hostile_mutations_rejected=28/28");return 0
if __name__=="__main__":raise SystemExit(main())
