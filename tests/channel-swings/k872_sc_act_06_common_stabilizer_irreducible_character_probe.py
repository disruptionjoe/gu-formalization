#!/usr/bin/env python3
"""Hostile mutations for K872."""
from __future__ import annotations
import copy, importlib.util, json
from pathlib import Path
H=Path(__file__).resolve().parent;R=H.parents[1];S=importlib.util.spec_from_file_location("k872",H/"k872_sc_act_06_common_stabilizer_irreducible_character.py");M=importlib.util.module_from_spec(S);assert S.loader;S.loader.exec_module(M)
def main()->int:
 b=json.loads((R/"lab/process/k872-sc-act-06-common-stabilizer-irreducible-character.json").read_text());ms=[lambda p:p.update(classification="CONVENTIONAL_ROUTE"),lambda p:p.update(target_claim="SC-ACT-01"),lambda p:p["reconstruction"].update(root_systems=[]),lambda p:p["reconstruction"].update(method="guess"),lambda p:p["reconstruction"].update(weyl_group_orders={}),lambda p:p["reconstruction"].update(complex_highest_weight_row_count=50),lambda p:p["reconstruction"].update(real_irreducible_type_count=39),lambda p:p["reconstruction"].update(real_tensor_type_count=28),lambda p:p["reconstruction"].update(complex_pair_type_count=10),lambda p:p["reconstruction"].update(real_dimension_check=0),lambda p:p["reconstruction"].update(maximum_real_multiplicity=9),lambda p:p["reconstruction"].update(rows_sha256="bad"),lambda p:p["reconstruction"].update(exact_weight_reconstruction=False),lambda p:p["reconstruction"].update(negative_residual_multiplicity_encountered=True),lambda p:p["decision"].update(common_stabilizer_weight_character_computed=False),lambda p:p["decision"].update(real_irreducible_multiplicities_computed=False),lambda p:p["decision"].update(owned_old_cohomology_module_authenticated=True),lambda p:p["decision"].update(typewise_capacity_decidable_from_current_inputs=True),lambda p:p.update(source_and_ledger_effect="SC-ACT-06_PROVED"),lambda p:p["controls"].update(hostile_mutations_rejected=19)];n=0
 for f in ms:
  p=copy.deepcopy(b);f(p)
  try:M.validate(p)
  except (AssertionError,KeyError,TypeError,ValueError):n+=1
 assert n==len(ms)==20;print(f"K872 hostile mutations rejected: {n}/{len(ms)}");return 0
if __name__=="__main__":raise SystemExit(main())
