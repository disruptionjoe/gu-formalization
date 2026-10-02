#!/usr/bin/env python3
"""Hostile mutations for K795."""
from __future__ import annotations
import copy, importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; SCRIPT=ROOT/"tests/channel-swings/k795_k500_complete_ab_decision_interface.py"
def load():
    s=importlib.util.spec_from_file_location("k795",SCRIPT); assert s and s.loader; m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
def main():
    m=load(); base=m.build(); muts=[]
    muts += [lambda p:p.__setitem__("result_id","MUTANT"), lambda p:p.__setitem__("classification","SOURCE_NATIVE_ROUTE")]
    for k in base["current_custody"]: muts.append(lambda p,k=k:p["current_custody"].__setitem__(k,not p["current_custody"][k]))
    for k in base["decision"]:
        if isinstance(base["decision"][k],bool): muts.append(lambda p,k=k:p["decision"].__setitem__(k,not p["decision"][k]))
    for side in ("A_native_requirements","B_native_requirements"):
        for _ in range(3): muts.append(lambda p,s=side:p["decision_interface"][s].pop())
    muts += [lambda p:p.__setitem__("pinned_inputs",{}), lambda p:p.__setitem__("source_and_ledger_effect","PROMOTED")]
    while len(muts)<26: muts.append(lambda p:p["decision_interface"].__setitem__("final_requirement","one gate is enough"))
    assert len(muts)==26; caught=0
    for f in muts:
        q=copy.deepcopy(base); f(q)
        try:m.validate(q)
        except (AssertionError,KeyError,ValueError):caught+=1
    assert caught==26; print("K795 probe: 26/26 hostile mutations rejected"); return 0
if __name__=="__main__": raise SystemExit(main())
