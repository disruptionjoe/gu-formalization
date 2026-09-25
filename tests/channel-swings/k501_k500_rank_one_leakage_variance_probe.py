#!/usr/bin/env python3
from __future__ import annotations
import copy, importlib.util
from fractions import Fraction
from pathlib import Path
H=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location("k501",H/"k501_k500_rank_one_leakage_variance.py");K=importlib.util.module_from_spec(s);s.loader.exec_module(K)
def checks(p):
 c=p["exact_control"];d=p["decision"];t=p["theorem"]
 return [p["result_id"]=="K501-K500-RANK-ONE-LEAKAGE-VARIANCE",p["classification"]=="INTERNAL_STRUCTURAL_ONLY",Fraction(c["leakage_square_direct"])==Fraction(36,25),c["weighted_variance"]==c["leakage_square_direct"],c["shifted_leakage_square"]==c["leakage_square_direct"],c["constant_multiplier_variance"]=="0","weighted variance" in t["multiplier_specialization"],d["K500_leakage_reduced_to_one_vector_variance_per_level"] is True,d["full_level_matrix_required"] is False,d["native_all_level_variances_evaluated"] is False,p["source_and_ledger_effect"]=="none"]
def selftest():
 p=K.build();n=0
 for m in [lambda q:q["exact_control"].__setitem__("weighted_variance","0"),lambda q:q["exact_control"].__setitem__("shifted_leakage_square","0"),lambda q:q["exact_control"].__setitem__("constant_multiplier_variance","1"),lambda q:q["decision"].__setitem__("full_level_matrix_required",True),lambda q:q["decision"].__setitem__("native_all_level_variances_evaluated",True),lambda q:q.__setitem__("source_and_ledger_effect","moved")]:
  z=copy.deepcopy(p);m(z);n+=int(not all(checks(z)))
 return n==6
if __name__=="__main__":
 p=K.build();c=checks(p);h=selftest();print(f"K501 controls: {sum(c)}/{len(c)}; hostile: {'PASS 6/6' if h else 'FAIL'}");raise SystemExit(0 if all(c) and h else 1)
