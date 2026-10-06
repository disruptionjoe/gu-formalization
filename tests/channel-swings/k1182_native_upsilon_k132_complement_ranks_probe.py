#!/usr/bin/env python3
"""Hostile mutation probe for K1182."""
from __future__ import annotations
import copy, importlib.util, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; SCRIPT=ROOT/"tests/channel-swings/k1182_native_upsilon_k132_complement_ranks.py"; CERT=ROOT/"lab/process/k1182-native-upsilon-k132-complement-ranks.json"
def load():
    s=importlib.util.spec_from_file_location("k1182_probe_target",SCRIPT); assert s and s.loader; m=importlib.util.module_from_spec(s); sys.modules[s.name]=m; s.loader.exec_module(m); return m
def main()->int:
    m=load(); p=json.loads(CERT.read_text()); m.validate(p); rejected=0
    paths=[("result_id",), ("classification",), ("target_claim",), ("decision","first_measured_source_owned_k132_carrier_map"), ("decision","sufficient_radical_capture"), ("decision","protected_verdict_change")]
    for path in paths:
        bad=copy.deepcopy(p); c=bad
        for k in path[:-1]: c=c[k]
        c[path[-1]] = (not c[path[-1]]) if isinstance(c[path[-1]],bool) else "BROKEN"
        try:m.validate(bad)
        except (AssertionError,KeyError):rejected+=1
    for i in (0,1):
        for key in ("hessian_rank","stacked_h_j_rank","rank_j_on_ker_h","physical_candidate_residual_after_gauge"):
            bad=copy.deepcopy(p); bad["exact_controls"]["cases"][i][key]+=1
            try:m.validate(bad)
            except (AssertionError,KeyError):rejected+=1
    assert rejected==14; print("PASS controls=18 hostile_mutations_rejected=14/14"); return 0
if __name__=="__main__": raise SystemExit(main())
