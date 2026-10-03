#!/usr/bin/env python3
"""Hostile mutations for K880."""
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];SCRIPT=ROOT/"tests/channel-swings/k880_sc_act_06_redundant_target_quotient.py"
def load():s=importlib.util.spec_from_file_location("k880",SCRIPT);assert s and s.loader;m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def main()->int:
 m=load();b=m.build();fs=[lambda p:p.__setitem__("target_claim","SC-ACT-05"),lambda p:p.__setitem__("classification","CONDITIONAL_COMPARATOR"),lambda p:p.__setitem__("pinned_inputs",{}),lambda p:p["target_quotient_theorem"].__setitem__("background_residual_zero",False),lambda p:p["target_quotient_theorem"].__setitem__("linearized_xi_factors_through_direct_response",False),lambda p:p["target_quotient_theorem"].__setitem__("stacked_row_rank_equals_direct_response_rank",False),lambda p:p["target_quotient_theorem"].__setitem__("stacked_kernel_equals_direct_kernel",False),lambda p:p["target_quotient_theorem"].__setitem__("induced_xi_map_on_old_quotient_is_zero",False),lambda p:p["target_quotient_theorem"].__setitem__("xi_is_not_an_independent_repair_target",False),lambda p:p["typewise_target_capacity"].__setitem__("row_count",39),lambda p:p["typewise_target_capacity"].__setitem__("known_row_count",39),lambda p:p["typewise_target_capacity"].__setitem__("all_xi_b_rho_zero",False),lambda p:p["typewise_target_capacity"]["rows"][0].__setitem__("xi_target_multiplicity_b_rho",1),lambda p:p["typewise_target_capacity"]["rows"][0].__setitem__("xi_induced_map_on_old_quotient_zero",False),lambda p:p["decision"].__setitem__("redundant_xi_row_reduces_the_injected_submodule",True),lambda p:p["decision"].__setitem__("xi_supplies_typewise_repair_capacity",True),lambda p:p["decision"].__setitem__("complete_independent_target_carrier_computed",True),lambda p:p.__setitem__("source_and_ledger_effect","PROMOTED"),lambda p:p["controls"].__setitem__("controls_passed",39),lambda p:p["controls"].__setitem__("hostile_mutations_rejected",19)];n=0
 for f in fs:
  q=copy.deepcopy(b);f(q)
  try:m.validate(q)
  except (AssertionError,KeyError,ValueError):n+=1
 assert n==len(fs)==20;print("K880 probe: 20/20 hostile mutations rejected");return 0
if __name__=="__main__":raise SystemExit(main())
