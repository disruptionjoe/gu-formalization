#!/usr/bin/env python3
"""Hostile mutations for K858."""
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
H=Path(__file__).resolve().parent;S=importlib.util.spec_from_file_location("k858",H/"k858_sc_act_06_topological_repair_disposition.py");M=importlib.util.module_from_spec(S);assert S.loader;S.loader.exec_module(M)
def main()->int:
 b=M.build();ms=[lambda p:p.update(classification="CONVENTIONAL_ROUTE"),lambda p:p.update(target_claim="SC-ACT-01"),lambda p:p["compiled_result"].update(euclidean_covector_dimension=13),lambda p:p["compiled_result"].update(unit_cosphere="S^12"),lambda p:p["compiled_result"].update(stable_triviality_threshold=13),lambda p:p["compiled_result"].update(current_middle_cohomology_lower_bound=90123),lambda p:p["compiled_result"].update(threshold_margin=0),lambda p:p["compiled_result"].update(conditional_bundle_trivial=False),lambda p:p["compiled_result"].update(pure_topological_obstruction_after_bundle_hypotheses=True),lambda p:p["compiled_result"].update(source_or_action_ownership_supplied=True),lambda p:p["compiled_result"].update(complete_constant_rank_current_bundle_supplied=True),lambda p:p["compiled_result"].update(current_flat_exact_admitted=True),lambda p:p["hypothesis_firewall"].update(required_before_topology_applies=[]),lambda p:p["hypothesis_firewall"].update(abstract_frame_is_not_an_owner=False),lambda p:p["hypothesis_firewall"].update(lower_bound_is_not_bundle_rank=False),lambda p:p["decision"].update(pure_topological_nonexistence_route_closed_conditionally=False),lambda p:p["decision"].update(ownership_and_complete_family_are_now_the_decisive_gates=False),lambda p:p["decision"].update(current_flat_packet_repaired=True),lambda p:p.update(source_and_ledger_effect="SC-ACT-06_PROVED"),lambda p:p["controls"].update(hostile_mutations_rejected=19)];r=0
 for m in ms:
  p=copy.deepcopy(b);m(p)
  try:M.validate(p)
  except AssertionError:r+=1
 assert r==len(ms)==b["controls"]["hostile_mutations_rejected"];print(f"K858 hostile mutations rejected: {r}/{len(ms)}");return 0
if __name__=="__main__":raise SystemExit(main())
