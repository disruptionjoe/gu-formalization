#!/usr/bin/env python3
"""Hostile mutations for K876."""
from __future__ import annotations
import copy,importlib.util,json
from pathlib import Path
H=Path(__file__).resolve().parent;R=H.parents[1];S=importlib.util.spec_from_file_location("k876",H/"k876_sc_act_06_zero_fermion_gauge_block_custody.py");M=importlib.util.module_from_spec(S);assert S.loader;S.loader.exec_module(M)
def main()->int:
 b=json.loads((R/"lab/process/k876-sc-act-06-zero-fermion-gauge-block-custody.json").read_text());ms=[lambda p:p.update(classification="CONVENTIONAL_ROUTE"),lambda p:p.update(target_claim="SC-ACT-01"),lambda p:p["background"].update(germ="K718"),lambda p:p["background"].update(all_fermions_zero=False),lambda p:p["background"].update(common_stabilizer="SO(13)"),lambda p:p["infinitesimal_action"].update(connection_image_dimension=16388),lambda p:p["infinitesimal_action"].update(connection_image_equals_radial_kernel_summand=False),lambda p:p["infinitesimal_action"].update(fermion_image_dimension_at_zero_background=1),lambda p:p["infinitesimal_action"].update(extra_mixed_gauge_image_in_tangential_quotient=1),lambda p:p["infinitesimal_action"].update(owned_tangential_quotient_dimension=90124),lambda p:p["custody"].update(principal_internal_gauge_image_owned=False),lambda p:p["custody"].update(fermionic_gauge_tangent_zero_at_K717=False),lambda p:p["custody"].update(new_source_owned_predecessor_into_old_tangential_H_found=True),lambda p:p["custody"].update(complete_diffeomorphism_metric_epsilon_symmetry_complex_owned=True),lambda p:p["custody"].update(caveated_full_complex_promoted=True),lambda p:p["decision"].update(mixed_repair_domain_multiplicity_is_zero_on_K717=False),lambda p:p["decision"].update(owned_radial_image_reused_not_double_counted=False),lambda p:p["decision"].update(complete_full_field_symmetry_image_authenticated=True),lambda p:p.update(source_and_ledger_effect="SC-ACT-06_PROVED"),lambda p:p["controls"].update(hostile_mutations_rejected=19)];n=0
 for f in ms:
  p=copy.deepcopy(b);f(p)
  try:M.validate(p)
  except (AssertionError,KeyError,TypeError,ValueError):n+=1
 assert n==len(ms)==20;print(f"K876 hostile mutations rejected: {n}/{len(ms)}");return 0
if __name__=="__main__":raise SystemExit(main())
