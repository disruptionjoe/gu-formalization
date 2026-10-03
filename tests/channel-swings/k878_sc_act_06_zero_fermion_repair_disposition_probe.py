#!/usr/bin/env python3
"""Hostile mutations for K878."""
from __future__ import annotations
import copy,importlib.util,json
from pathlib import Path
H=Path(__file__).resolve().parent;R=H.parents[1];S=importlib.util.spec_from_file_location("k878",H/"k878_sc_act_06_zero_fermion_repair_disposition.py");M=importlib.util.module_from_spec(S);assert S.loader;S.loader.exec_module(M)
def main()->int:
 b=json.loads((R/"lab/process/k878-sc-act-06-zero-fermion-repair-disposition.json").read_text());ms=[lambda p:p.update(classification="CONVENTIONAL_ROUTE"),lambda p:p.update(target_claim="SC-ACT-01"),lambda p:p["mixed_route_certificate"].update(old_quotient_dimension=90124),lambda p:p["mixed_route_certificate"].update(real_irreducible_type_count=39),lambda p:p["mixed_route_certificate"].update(mixed_domain_rank=1),lambda p:p["mixed_route_certificate"].update(mixed_target_rank=1),lambda p:p["mixed_route_certificate"].update(typewise_rows_tested=39),lambda p:p["mixed_route_certificate"].update(typewise_rows_satisfied=1),lambda p:p["mixed_route_certificate"].update(typewise_rows_failed=39),lambda p:p["mixed_route_certificate"].update(source_displayed_mixed_route_closed=False),lambda p:p["corrected_full_field_certificate"].update(row_count=10),lambda p:p["corrected_full_field_certificate"].update(satisfied_row_count=6),lambda p:p["corrected_full_field_certificate"].update(failed_row_count=5),lambda p:p["corrected_full_field_certificate"].update(current_GU_candidate_admitted=True),lambda p:p["corrected_full_field_certificate"].update(source_action_owned_total_repair_multiplicities_known=True),lambda p:p["decision"].update(source_displayed_mixed_stabilization_route_refuted_on_K717=False),lambda p:p["decision"].update(current_flat_packet_repairability_refuted=True),lambda p:p["decision"].update(SC_ACT_06_proved_or_refuted=True),lambda p:p.update(source_and_ledger_effect="SC-ACT-06_REFUTED"),lambda p:p["controls"].update(hostile_mutations_rejected=19)];n=0
 for f in ms:
  p=copy.deepcopy(b);f(p)
  try:M.validate(p)
  except (AssertionError,KeyError,TypeError,ValueError):n+=1
 assert n==len(ms)==20;print(f"K878 hostile mutations rejected: {n}/{len(ms)}");return 0
if __name__=="__main__":raise SystemExit(main())
