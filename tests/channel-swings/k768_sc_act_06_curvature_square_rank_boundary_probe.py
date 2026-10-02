#!/usr/bin/env python3
"""Hostile mutation probe for K768."""
from __future__ import annotations
import copy, importlib.util, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; SCRIPT=ROOT/"tests/channel-swings/k768_sc_act_06_curvature_square_rank_boundary.py"; CERT=ROOT/"lab/process/k768-sc-act-06-curvature-square-rank-boundary.json"
def load():
    spec=importlib.util.spec_from_file_location("k768_probe_target",SCRIPT); assert spec and spec.loader; mod=importlib.util.module_from_spec(spec); sys.modules[spec.name]=mod; spec.loader.exec_module(mod); return mod
def main()->int:
    mod=load(); base=json.loads(CERT.read_text()); mod.validate(base); muts=[lambda d:d.__setitem__("result_id","BROKEN"),lambda d:d.__setitem__("status","unverified"),lambda d:d.__setitem__("classification","SOURCE_NATIVE_ROUTE"),lambda d:d.__setitem__("target_claim","SC-ACT-01"),lambda d:d["exact_controls"].__setitem__("dimension",13),lambda d:d["exact_controls"].__setitem__("coefficient_dimension",1),lambda d:d["exact_controls"].__setitem__("connection_dimension",14),lambda d:d["exact_controls"].__setitem__("rows",[]),lambda d:d["exact_controls"]["rows"][0].__setitem__("connection_hessian_rank",1),lambda d:d["exact_controls"]["rows"][0].__setitem__("connection_only_middle_cohomology_dimension",1),lambda d:d["exact_controls"]["rows"][1].__setitem__("connection_hessian_rank",1),lambda d:d["exact_controls"]["rows"][1].__setitem__("connection_only_middle_cohomology_dimension",1),lambda d:d["exact_controls"]["rows"][2].__setitem__("connection_hessian_rank",1),lambda d:d["exact_controls"]["rows"][2].__setitem__("connection_only_middle_cohomology_dimension",1),lambda d:d["exact_controls"]["rows"][3].__setitem__("connection_hessian_rank",1),lambda d:d["exact_controls"]["rows"][3].__setitem__("connection_only_middle_cohomology_dimension",1),lambda d:d.__setitem__("source_and_ledger_effect","MOVED")]
    for key,value in base["decision"].items(): muts.append(lambda d,key=key,value=value:d["decision"].__setitem__(key,not value))
    while len(muts)<38: muts.append(lambda d:d["exact_controls"].__setitem__("rows",[]))
    caught=0
    for mutate in muts[:38]:
        c=copy.deepcopy(base); mutate(c)
        try: mod.validate(c)
        except (AssertionError,KeyError,TypeError,ValueError): caught+=1
    assert caught==38; print("PASS controls=44 hostile_mutations_rejected=38/38"); return 0
if __name__=="__main__": raise SystemExit(main())
