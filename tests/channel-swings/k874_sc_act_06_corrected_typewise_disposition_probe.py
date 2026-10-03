#!/usr/bin/env python3
"""Hostile mutations for K874."""
from __future__ import annotations
import copy, importlib.util, json
from pathlib import Path
H=Path(__file__).resolve().parent;R=H.parents[1];S=importlib.util.spec_from_file_location("k874",H/"k874_sc_act_06_corrected_typewise_disposition.py");M=importlib.util.module_from_spec(S);assert S.loader;S.loader.exec_module(M)
def main()->int:
 b=json.loads((R/"lab/process/k874-sc-act-06-corrected-typewise-disposition.json").read_text());ms=[lambda p:p.update(classification="CONVENTIONAL_ROUTE"),lambda p:p.update(target_claim="SC-ACT-01"),lambda p:p["compiled_result"].update(owned_tangential_quotient_dimension=90124),lambda p:p["compiled_result"].update(real_irreducible_type_count=39),lambda p:p["compiled_result"].update(maximum_old_multiplicity=9),lambda p:p["compiled_result"].update(owned_repair_modules_known=True),lambda p:p["compiled_result"].update(current_flat_exact_admitted=True),lambda p:p["typewise_obligations"].update(row_count=39),lambda p:p["typewise_obligations"].update(known_h_row_count=39),lambda p:p["typewise_obligations"].update(known_repair_capacity_row_count=40),lambda p:p["typewise_obligations"].update(all_current_rows_decidable=True),lambda p:p["corrected_certificate"].update(row_count=10),lambda p:p["corrected_certificate"].update(satisfied_row_count=6),lambda p:p["corrected_certificate"].update(failed_row_count=5),lambda p:p["corrected_certificate"].update(all_rows_conjunctive=False),lambda p:p["corrected_certificate"].update(current_GU_candidate_admitted=True),lambda p:p["decision"].update(owned_principal_quotient_character_closed=False),lambda p:p["decision"].update(current_flat_packet_repaired=True),lambda p:p.update(source_and_ledger_effect="SC-ACT-06_PROVED"),lambda p:p["controls"].update(hostile_mutations_rejected=19)];n=0
 for f in ms:
  p=copy.deepcopy(b);f(p)
  try:M.validate(p)
  except (AssertionError,KeyError,TypeError,ValueError):n+=1
 assert n==len(ms)==20;print(f"K874 hostile mutations rejected: {n}/{len(ms)}");return 0
if __name__=="__main__":raise SystemExit(main())
