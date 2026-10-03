#!/usr/bin/env python3
"""Hostile mutations for K870."""
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;S=importlib.util.spec_from_file_location("k870",H/"k870_sc_act_06_corrected_isotropy_disposition.py");M=importlib.util.module_from_spec(S);assert S.loader;S.loader.exec_module(M)
def main()->int:
 b=M.build();ms=[lambda p:p.update(classification="CONVENTIONAL_ROUTE"),lambda p:p.update(target_claim="SC-ACT-01"),lambda p:p["compiled_result"].update(dimension_split_survives=False),lambda p:p["compiled_result"].update(radial_dimension=0),lambda p:p["compiled_result"].update(tangential_kernel_dimension=90124),lambda p:p["compiled_result"].update(auxiliary_SO13_kernel_module_retracted=False),lambda p:p["compiled_result"].update(common_stabilizer="SO(13)"),lambda p:p["compiled_result"].update(common_stabilizer_character_known=True),lambda p:p["compiled_result"].update(owned_old_cohomology_module_known=True),lambda p:p["compiled_result"].update(current_flat_exact_admitted=True),lambda p:p["corrected_certificate"].update(row_count=10),lambda p:p["corrected_certificate"].update(satisfied_row_count=4),lambda p:p["corrected_certificate"].update(failed_row_count=7),lambda p:p["corrected_certificate"].update(all_rows_conjunctive=False),lambda p:p["corrected_certificate"].update(current_GU_candidate_admitted=True),lambda p:p["corrected_certificate"].update(failed_SO13_row_cannot_be_counted_as_satisfied=False),lambda p:p["decision"].update(K866_disposition_current=True),lambda p:p["decision"].update(SC_ACT_06_proved_or_refuted=True),lambda p:p.update(source_and_ledger_effect="SC-ACT-06_REFUTED"),lambda p:p["controls"].update(hostile_mutations_rejected=19)];n=0
 for f in ms:
  p=copy.deepcopy(b);f(p)
  try:M.validate(p)
  except (AssertionError,KeyError,TypeError,ValueError):n+=1
 assert n==len(ms)==b["controls"]["hostile_mutations_rejected"];print(f"K870 hostile mutations rejected: {n}/{len(ms)}");return 0
if __name__=="__main__":raise SystemExit(main())
