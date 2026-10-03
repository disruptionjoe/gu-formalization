#!/usr/bin/env python3
"""Hostile mutations for K882."""
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];SCRIPT=ROOT/"tests/channel-swings/k882_sc_act_06_full_field_obstruction_disposition.py"
def load():s=importlib.util.spec_from_file_location("k882",SCRIPT);assert s and s.loader;m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def main()->int:
 m=load();b=m.build();fs=[lambda p:p.__setitem__("target_claim","SC-ACT-05"),lambda p:p.__setitem__("classification","CONDITIONAL_COMPARATOR"),lambda p:p.__setitem__("pinned_inputs",{}),lambda p:p["obstruction_certificate"].__setitem__("injected_dimension",90124),lambda p:p["obstruction_certificate"].__setitem__("real_irreducible_type_count",39),lambda p:p["obstruction_certificate"].__setitem__("sum_of_multiplicity_lower_bounds",168),lambda p:p["obstruction_certificate"].__setitem__("known_displayed_route_failed_type_count",39),lambda p:p["obstruction_certificate"].__setitem__("all_known_displayed_repairs_fail_on_submodule",False),lambda p:p["obstruction_certificate"]["rows"].__setitem__("complete full-field cohomology character known",True),lambda p:p["corrected_completion_gate"].__setitem__("satisfied_row_count",6),lambda p:p["corrected_completion_gate"].__setitem__("failed_row_count",5),lambda p:p["corrected_completion_gate"].__setitem__("current_GU_candidate_admitted",True),lambda p:p["decision"].__setitem__("complete_full_field_cohomology_computed",True),lambda p:p["decision"].__setitem__("current_flat_packet_repaired",True),lambda p:p["decision"].__setitem__("current_flat_packet_repairability_refuted",True),lambda p:p["decision"].__setitem__("global_SC_ACT_06_proved_or_refuted",True),lambda p:p["decision"].__setitem__("source_claim_status_changes",True),lambda p:p["protected_effects"].__setitem__("sc_act_06","REFUTED"),lambda p:p.__setitem__("source_and_ledger_effect","PROMOTED"),lambda p:p["controls"].__setitem__("hostile_mutations_rejected",19)];n=0
 for f in fs:
  q=copy.deepcopy(b);f(q)
  try:m.validate(q)
  except (AssertionError,KeyError,ValueError):n+=1
 assert n==len(fs)==20;print("K882 probe: 20/20 hostile mutations rejected");return 0
if __name__=="__main__":raise SystemExit(main())
