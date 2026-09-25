#!/usr/bin/env python3
from __future__ import annotations
import copy, importlib.util
from pathlib import Path
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("k504",HERE/"k504_k500_finite_car_lower_envelope_obstruction.py")
K=importlib.util.module_from_spec(spec);spec.loader.exec_module(K)
def checks(p):
 c=p["exact_control"];d=p["decision"]
 return [p["result_id"]=="K504-K500-FINITE-CAR-LOWER-ENVELOPE-OBSTRUCTION",p["classification"]=="INTERNAL_STRUCTURAL_ONLY",c["levels_one_through_three_not_rank_forced_zero"] is True,c["level_four_forced_zero"] is True,c["alternating_words"][3]["species_occupancies"]==[2,2],d["fixed_finite_K162_approximant_can_prove_uniform_positive_all_level_envelope"] is False,d["finite_prefix_values_retracted"] is False,d["continuum_words_proved_zero"] is False,d["complete_K500_uniform_leakage_emitted"] is False,p["source_and_ledger_effect"]=="none"]
def selftest():
 p=K.build();caught=0
 muts=[lambda q:q["exact_control"].__setitem__("level_four_forced_zero",False),lambda q:q["decision"].__setitem__("fixed_finite_K162_approximant_can_prove_uniform_positive_all_level_envelope",True),lambda q:q["decision"].__setitem__("finite_prefix_values_retracted",True),lambda q:q["decision"].__setitem__("continuum_words_proved_zero",True),lambda q:q["decision"].__setitem__("complete_K500_uniform_leakage_emitted",True),lambda q:q.__setitem__("source_and_ledger_effect","moved")]
 for m in muts:
  z=copy.deepcopy(p);m(z);caught+=int(not all(checks(z)))
 return caught==len(muts),caught,len(muts)
if __name__=="__main__":
 p=K.build();c=checks(p);h,n,t=selftest();print(f"K504 controls: {sum(c)}/{len(c)}; hostile: {'PASS' if h else 'FAIL'} {n}/{t}");raise SystemExit(0 if all(c) and h else 1)
