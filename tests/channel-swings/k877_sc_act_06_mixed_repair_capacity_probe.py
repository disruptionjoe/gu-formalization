#!/usr/bin/env python3
"""Hostile mutations for K877."""
from __future__ import annotations
import copy,importlib.util,json
from pathlib import Path
H=Path(__file__).resolve().parent;R=H.parents[1];S=importlib.util.spec_from_file_location("k877",H/"k877_sc_act_06_mixed_repair_capacity.py");M=importlib.util.module_from_spec(S);assert S.loader;S.loader.exec_module(M)
def main()->int:
 b=json.loads((R/"lab/process/k877-sc-act-06-mixed-repair-capacity.json").read_text());ms=[lambda p:p.update(classification="CONVENTIONAL_ROUTE"),lambda p:p.update(target_claim="SC-ACT-01"),lambda p:p["typewise_test"].update(group="SO(13)"),lambda p:p["typewise_test"].update(row_count=39),lambda p:p["typewise_test"].update(old_quotient_dimension=90124),lambda p:p["typewise_test"].update(displayed_mixed_repair_domain_dimension=1),lambda p:p["typewise_test"].update(displayed_mixed_repair_target_dimension=1),lambda p:p["typewise_test"].update(decidable_row_count=39),lambda p:p["typewise_test"].update(satisfied_row_count=1),lambda p:p["typewise_test"].update(failed_row_count=39),lambda p:p["typewise_test"].update(total_multiplicity_deficit=172),lambda p:p["theorem"].update(every_old_type_has_positive_multiplicity=False),lambda p:p["theorem"].update(every_displayed_mixed_capacity_is_zero=False),lambda p:p["theorem"].update(displayed_mixed_route_fails_every_type=False),lambda p:p["theorem"].update(mixed_route_cannot_repair_owned_tangential_quotient_on_K717=False),lambda p:p["theorem"].update(complete_full_field_repairability_refuted=True),lambda p:p["decision"].update(source_displayed_Bose_Fermi_stabilization_repair_route="ADMITTED"),lambda p:p["decision"].update(current_flat_packet_repairability_refuted=True),lambda p:p.update(source_and_ledger_effect="SC-ACT-06_REFUTED"),lambda p:p["controls"].update(hostile_mutations_rejected=19)];n=0
 for f in ms:
  p=copy.deepcopy(b);f(p)
  try:M.validate(p)
  except (AssertionError,KeyError,TypeError,ValueError):n+=1
 assert n==len(ms)==20;print(f"K877 hostile mutations rejected: {n}/{len(ms)}");return 0
if __name__=="__main__":raise SystemExit(main())
