#!/usr/bin/env python3
"""Hostile mutations for K873."""
from __future__ import annotations
import copy, importlib.util, json
from pathlib import Path
H=Path(__file__).resolve().parent;R=H.parents[1];S=importlib.util.spec_from_file_location("k873",H/"k873_sc_act_06_owned_symmetry_custody.py");M=importlib.util.module_from_spec(S);assert S.loader;S.loader.exec_module(M)
def main()->int:
 b=json.loads((R/"lab/process/k873-sc-act-06-owned-symmetry-custody.json").read_text());ms=[lambda p:p.update(classification="CONVENTIONAL_ROUTE"),lambda p:p.update(target_claim="SC-ACT-01"),lambda p:p["source_custody"].update(displayed_C0="unknown"),lambda p:p["source_custody"].update(source_gauge_group="SO(13)"),lambda p:p["source_custody"].update(real_parameter_dimension=0),lambda p:p["source_custody"].update(principal_map_is_owned=False),lambda p:p["source_custody"].update(complete_displayed_complex_stabilized=True),lambda p:p["source_custody"].update(caveat_empor_remains_load_bearing=False),lambda p:p["owned_image"].update(map_injective=False),lambda p:p["owned_image"].update(composition_zero_on_flat_zero_locus=False),lambda p:p["owned_image"].update(image_dimension=0),lambda p:p["owned_image"].update(common_stabilizer="SO(13)"),lambda p:p["owned_tangential_quotient"].update(quotient_dimension=90124),lambda p:p["owned_tangential_quotient"].update(real_irreducible_type_count=39),lambda p:p["owned_tangential_quotient"].update(authenticated_at_principal_connection_symbol_scope=False),lambda p:p["decision"].update(K789_q_lambda_remains_merely_unowned_candidate=True),lambda p:p["decision"].update(owned_principal_internal_gauge_image_authenticated=False),lambda p:p["decision"].update(source_displayed_complete_complex_promoted=True),lambda p:p.update(source_and_ledger_effect="SC-ACT-06_PROVED"),lambda p:p["controls"].update(hostile_mutations_rejected=19)];n=0
 for f in ms:
  p=copy.deepcopy(b);f(p)
  try:M.validate(p)
  except (AssertionError,KeyError,TypeError,ValueError):n+=1
 assert n==len(ms)==20;print(f"K873 hostile mutations rejected: {n}/{len(ms)}");return 0
if __name__=="__main__":raise SystemExit(main())
