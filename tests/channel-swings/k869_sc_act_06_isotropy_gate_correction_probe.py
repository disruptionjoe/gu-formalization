#!/usr/bin/env python3
"""Hostile mutations for K869."""
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;S=importlib.util.spec_from_file_location("k869",H/"k869_sc_act_06_isotropy_gate_correction.py");M=importlib.util.module_from_spec(S);assert S.loader;S.loader.exec_module(M)
def main()->int:
 b=M.build();ms=[lambda p:p.update(classification="CONVENTIONAL_ROUTE"),lambda p:p.update(target_claim="SC-ACT-01"),lambda p:p["surviving_results"].update(K860_abstract_G_over_H_theorem=False),lambda p:p["surviving_results"].update(K865_abstract_typewise_capacity_theorem=False),lambda p:p["surviving_results"].update(K863_radial_dimension=0),lambda p:p["surviving_results"].update(K863_tangential_kernel_dimension=90124),lambda p:p["surviving_results"].update(K864_conditional_quotient_dimension=90124),lambda p:p["corrected_results"].update(K863_tangential_kernel_is_SO13_module=True),lambda p:p["corrected_results"].update(K863_radial_formula_is_full_kernel_SO13_decomposition=True),lambda p:p["corrected_results"].update(K864_conditional_quotient_is_SO13_module=True),lambda p:p["corrected_results"].update(K866_four_SO13_rows_established=True),lambda p:p["corrected_results"].update(K860_SO14_homogeneous_application_to_current_packet=True),lambda p:p["corrected_results"].update(K865_SO13_multiplicity_test_currently_applicable=True),lambda p:p["corrected_results"].update(replacement_group="SO(13)"),lambda p:p["corrected_results"].update(replacement_character_known=True),lambda p:p["decision"].update(old_SO13_multiplicity_frontier_retired=False),lambda p:p["decision"].update(owned_old_cohomology_module_known=True),lambda p:p["decision"].update(SC_ACT_06_proved_or_refuted=True),lambda p:p.update(source_and_ledger_effect="SC-ACT-06_REFUTED"),lambda p:p["controls"].update(hostile_mutations_rejected=19)];n=0
 for f in ms:
  p=copy.deepcopy(b);f(p)
  try:M.validate(p)
  except (AssertionError,KeyError,TypeError,ValueError):n+=1
 assert n==len(ms)==b["controls"]["hostile_mutations_rejected"];print(f"K869 hostile mutations rejected: {n}/{len(ms)}");return 0
if __name__=="__main__":raise SystemExit(main())
