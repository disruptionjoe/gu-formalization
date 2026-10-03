#!/usr/bin/env python3
"""Hostile mutations for K871 without recomputing the exact character."""
from __future__ import annotations
import copy, importlib.util, json
from pathlib import Path
H=Path(__file__).resolve().parent;R=H.parents[1];S=importlib.util.spec_from_file_location("k871",H/"k871_sc_act_06_common_stabilizer_weight_character.py");M=importlib.util.module_from_spec(S);assert S.loader;S.loader.exec_module(M)
def main()->int:
 b=json.loads((R/"lab/process/k871-sc-act-06-common-stabilizer-weight-character.json").read_text());ms=[lambda p:p.update(classification="CONVENTIONAL_ROUTE"),lambda p:p.update(target_claim="SC-ACT-01"),lambda p:p["torus_model"].update(group="SO(13)"),lambda p:p["torus_model"].update(positive_planes=[]),lambda p:p["torus_model"].update(negative_zero_weight_direction=12),lambda p:p["torus_model"].update(fixed_base_covector=1),lambda p:p["torus_model"].update(exact_field="float64"),lambda p:p["exact_character"].update(clifford_weight_vectors=0),lambda p:p["exact_character"].update(tangential_weight_vectors=12),lambda p:p["exact_character"].update(domain_dimension=0),lambda p:p["exact_character"].update(image_dimension=0),lambda p:p["exact_character"].update(kernel_dimension=90127),lambda p:p["exact_character"].update(nonzero_kernel_weight_count=0),lambda p:p["exact_character"].update(zero_weight_kernel_multiplicity=0),lambda p:p["exact_character"].update(weight_rows_sha256="bad"),lambda p:p["exact_character"].update(sign_inversion_symmetric=False),lambda p:p["decision"].update(common_stabilizer_weight_character_computed=False),lambda p:p["decision"].update(real_irreducible_reconstruction_completed=True),lambda p:p.update(source_and_ledger_effect="SC-ACT-06_PROVED"),lambda p:p["controls"].update(hostile_mutations_rejected=19)];n=0
 for f in ms:
  p=copy.deepcopy(b);f(p)
  try:M.validate(p)
  except (AssertionError,KeyError,TypeError,ValueError):n+=1
 assert n==len(ms)==20;print(f"K871 hostile mutations rejected: {n}/{len(ms)}");return 0
if __name__=="__main__":raise SystemExit(main())
