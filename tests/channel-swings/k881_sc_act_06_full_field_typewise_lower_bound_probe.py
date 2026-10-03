#!/usr/bin/env python3
"""Hostile mutations for K881."""
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];SCRIPT=ROOT/"tests/channel-swings/k881_sc_act_06_full_field_typewise_lower_bound.py"
def load():s=importlib.util.spec_from_file_location("k881",SCRIPT);assert s and s.loader;m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def main()->int:
 m=load();b=m.build();fs=[lambda p:p.__setitem__("target_claim","SC-ACT-05"),lambda p:p.__setitem__("classification","CONDITIONAL_COMPARATOR"),lambda p:p.__setitem__("pinned_inputs",{}),lambda p:p["equivariant_transfer"].__setitem__("common_stabilizer","SO(13)"),lambda p:p["equivariant_transfer"].__setitem__("injection_is_equivariant",False),lambda p:p["equivariant_transfer"].__setitem__("real_irreducible_type_count",39),lambda p:p["equivariant_transfer"].__setitem__("injected_dimension_check",90124),lambda p:p["equivariant_transfer"].__setitem__("sum_of_multiplicity_lower_bounds",168),lambda p:p["equivariant_transfer"].__setitem__("complete_full_field_character_computed",True),lambda p:p["typewise_lower_bounds"].__setitem__("row_count",39),lambda p:p["typewise_lower_bounds"].__setitem__("failed_known_route_row_count",39),lambda p:p["typewise_lower_bounds"]["rows"][0].__setitem__("displayed_mixed_domain_multiplicity",1),lambda p:p["typewise_lower_bounds"]["rows"][0].__setitem__("redundant_xi_target_multiplicity",1),lambda p:p["typewise_lower_bounds"]["rows"][0].__setitem__("remaining_typewise_deficit_lower_bound",0),lambda p:p["typewise_lower_bounds"]["rows"][0].__setitem__("complete_full_field_multiplicity_known",True),lambda p:p["decision"].__setitem__("displayed_mixed_plus_xi_routes_repair_the_injected_submodule",True),lambda p:p["decision"].__setitem__("complete_flat_packet_repairability_refuted",True),lambda p:p["decision"].__setitem__("SC_ACT_06_proved_or_refuted",True),lambda p:p.__setitem__("source_and_ledger_effect","PROMOTED"),lambda p:p["controls"].__setitem__("hostile_mutations_rejected",19)];n=0
 for f in fs:
  q=copy.deepcopy(b);f(q)
  try:m.validate(q)
  except (AssertionError,KeyError,ValueError):n+=1
 assert n==len(fs)==20;print("K881 probe: 20/20 hostile mutations rejected");return 0
if __name__=="__main__":raise SystemExit(main())
