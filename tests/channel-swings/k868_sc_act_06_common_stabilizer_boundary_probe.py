#!/usr/bin/env python3
"""Hostile mutations for K868."""
from __future__ import annotations
import copy,importlib.util
from pathlib import Path
HERE=Path(__file__).resolve().parent;S=importlib.util.spec_from_file_location("k868",HERE/"k868_sc_act_06_common_stabilizer_boundary.py");M=importlib.util.module_from_spec(S);assert S.loader;S.loader.exec_module(M)
def main()->int:
    b=M.build(); muts=[
        lambda p:p.update(classification="CONVENTIONAL_ROUTE"),lambda p:p.update(target_claim="SC-ACT-01"),
        lambda p:p["stabilizer_chain"].update(native_group="SO(14)"),lambda p:p["stabilizer_chain"].update(common_q_stabilizer_identity_component="SO(13)"),
        lambda p:p["stabilizer_chain"].update(positive_tangential_dimension=13),lambda p:p["stabilizer_chain"].update(negative_tangential_dimension=0),
        lambda p:p["stabilizer_chain"].update(cross_sign_euclidean_rotation_excluded=False),lambda p:p["stabilizer_chain"].update(compact_semisimple=False),
        lambda p:p["radial_restriction"].update(exterior_dimension_sum=4096),lambda p:p["radial_restriction"].update(dimension_check=8192),
        lambda p:p["radial_restriction"].update(full_real_irreducible_reduction_completed=True),lambda p:p["surviving_response_facts"].update(tangential_kernel_dimension=90124),
        lambda p:p["surviving_response_facts"].update(tangential_kernel_is_common_stabilizer_module=False),lambda p:p["surviving_response_facts"].update(tangential_common_stabilizer_character_computed=True),
        lambda p:p["decision"].update(auxiliary_SO13_is_valid_response_stabilizer=True),lambda p:p["decision"].update(common_compact_stabilizer_authenticated=False),
        lambda p:p["decision"].update(owned_old_symmetry_authenticated=True),lambda p:p["decision"].update(SC_ACT_06_proved_or_refuted=True),
        lambda p:p.update(source_and_ledger_effect="SC-ACT-06_REFUTED"),lambda p:p["controls"].update(hostile_mutations_rejected=19),]
    n=0
    for f in muts:
        p=copy.deepcopy(b);f(p)
        try:M.validate(p)
        except (AssertionError,KeyError,TypeError,ValueError):n+=1
    assert n==len(muts)==b["controls"]["hostile_mutations_rejected"];print(f"K868 hostile mutations rejected: {n}/{len(muts)}");return 0
if __name__=="__main__":raise SystemExit(main())
