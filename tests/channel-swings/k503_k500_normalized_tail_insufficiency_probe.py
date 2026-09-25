#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k503",H/"k503_k500_normalized_tail_insufficiency.py");K=importlib.util.module_from_spec(s);s.loader.exec_module(K)
def checks(p):
 c=p["exact_control"];d=p["decision"];t=p["theorem"]
 return [p["result_id"]=="K503-K500-NORMALIZED-TAIL-INSUFFICIENCY",p["classification"]=="INTERNAL_STRUCTURAL_ONLY",c["all_absolute_bounds_saturated"] is True,c["all_word_norm_upper_bounds_hold"] is True,c["sample_normalized_leakage_strictly_grows"] is True,c["abstract_sequence_unbounded"] is True,c["native_K162_counterexample"] is False,"unbounded" in t["normalized_leakage"],d["K175_K496_absolute_tails_sufficient_for_K500_leakage"] is False,d["existing_native_tail_results_retracted"] is False,d["complete_uniform_leakage_emitted"] is False,p["source_and_ledger_effect"]=="none"]
def selftest():
 p=K.build();n=0
 for m in [lambda q:q["exact_control"].__setitem__("all_absolute_bounds_saturated",False),lambda q:q["exact_control"].__setitem__("sample_normalized_leakage_strictly_grows",False),lambda q:q["exact_control"].__setitem__("native_K162_counterexample",True),lambda q:q["decision"].__setitem__("K175_K496_absolute_tails_sufficient_for_K500_leakage",True),lambda q:q["decision"].__setitem__("existing_native_tail_results_retracted",True),lambda q:q["decision"].__setitem__("complete_uniform_leakage_emitted",True),lambda q:q.__setitem__("source_and_ledger_effect","moved")]:
  z=copy.deepcopy(p);m(z);n+=int(not all(checks(z)))
 return n==7
if __name__=="__main__":
 p=K.build();c=checks(p);h=selftest();print(f"K503 controls: {sum(c)}/{len(c)}; hostile: {'PASS 7/7' if h else 'FAIL'}");raise SystemExit(0 if all(c) and h else 1)
