#!/usr/bin/env python3
"""Hostile mutations for K875."""
from __future__ import annotations
import copy, importlib.util, json
from pathlib import Path
H=Path(__file__).resolve().parent;R=H.parents[1];S=importlib.util.spec_from_file_location("k875",H/"k875_sc_act_06_zero_fermion_mixed_block_vanishing.py");M=importlib.util.module_from_spec(S);assert S.loader;S.loader.exec_module(M)
def main()->int:
 b=json.loads((R/"lab/process/k875-sc-act-06-zero-fermion-mixed-block-vanishing.json").read_text());ms=[lambda p:p.update(classification="CONVENTIONAL_ROUTE"),lambda p:p.update(target_claim="SC-ACT-05"),lambda p:p["background"].update(germ="K718"),lambda p:p["background"].update(all_barred_and_unbarred_background_fermions_zero=False),lambda p:p["background"].update(owned_old_tangential_quotient_dimension=90124),lambda p:p["formal_derivatives"].update(mixed_block_rank_at_zero_fermion=1),lambda p:p["formal_derivatives"].update(every_mixed_term_contains_one_background_fermion=False),lambda p:p["formal_derivatives"].update(fermion_fermion_diagonal_block_forced_zero=True),lambda p:p["theorem"].update(connection_to_fermionic_euler_repair_map_zero=False),lambda p:p["theorem"].update(fermionic_field_to_bosonic_euler_repair_map_zero=False),lambda p:p["theorem"].update(mixed_hessian_reciprocity_preserved=False),lambda p:p["theorem"].update(result_independent_of_F_dimension_and_coefficients=False),lambda p:p["theorem"].update(lower_order_nonmixed_fermion_operator_not_removed=False),lambda p:p["theorem"].update(nonzero_fermion_stationary_germ_covered=True),lambda p:p["theorem"].update(complete_bosonic_full_field_symbol_covered=True),lambda p:p["decision"].update(source_displayed_mixed_blocks_supply_repair_capacity_on_K717=True),lambda p:p["decision"].update(source_displayed_mixed_stabilization_route_closed_on_K717=False),lambda p:p["decision"].update(complete_full_field_repairability_refuted=True),lambda p:p.update(source_and_ledger_effect="SC-ACT-06_REFUTED"),lambda p:p["controls"].update(hostile_mutations_rejected=19)];n=0
 for f in ms:
  p=copy.deepcopy(b);f(p)
  try:M.validate(p)
  except (AssertionError,KeyError,TypeError,ValueError):n+=1
 assert n==len(ms)==20;print(f"K875 hostile mutations rejected: {n}/{len(ms)}");return 0
if __name__=="__main__":raise SystemExit(main())
