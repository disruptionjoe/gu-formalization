#!/usr/bin/env python3
"""Probe and hostile mutations for K510."""
from __future__ import annotations
import copy, importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location("k510",H/"k510_k500_selected_path_rate_discriminator.py")
K=importlib.util.module_from_spec(s);s.loader.exec_module(K)
def checks(p):
 c=p["exact_controls"];d=p["decision"];t=p["rate_theorem"]
 return [p["result_id"]=="K510-K500-SELECTED-PATH-RATE-DISCRIMINATOR",c["row_count"]==26,c["all_paths_nonzero"] is True,c["sample_ratios_strictly_increase_by_level"] is True,t["ratio_diverges"] is True,"not asserted" in t["template_status"],d["K507_native_positivity_retracted"] is False,d["simplex_volume_only_selected_path_certificate_sufficient_for_K500"] is False,d["determinant_aware_or_direct_variance_work_required"] is True,d["uniform_all_level_native_path_lower_emitted"] is False,d["complete_K500_uniform_leakage_emitted"] is False,p["source_and_ledger_effect"]=="none"]
def main():
 p=K.build();ok=checks(p);n=0
 for f in [lambda q:q["exact_controls"].__setitem__("all_paths_nonzero",False),lambda q:q["rate_theorem"].__setitem__("ratio_diverges",False),lambda q:q["decision"].__setitem__("K507_native_positivity_retracted",True),lambda q:q["decision"].__setitem__("simplex_volume_only_selected_path_certificate_sufficient_for_K500",True),lambda q:q["decision"].__setitem__("uniform_all_level_native_path_lower_emitted",True),lambda q:q["decision"].__setitem__("complete_K500_uniform_leakage_emitted",True)]:
  h=copy.deepcopy(p);f(h)
  try:K.validate(h)
  except AssertionError:n+=1
 print(f"K510 controls: {sum(ok)}/{len(ok)}; hostile: {n}/6")
 return 0 if all(ok) and n==6 else 1
if __name__=="__main__":raise SystemExit(main())
