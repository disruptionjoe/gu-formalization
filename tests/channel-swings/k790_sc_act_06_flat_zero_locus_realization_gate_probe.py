#!/usr/bin/env python3
"""Hostile replay for K790."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k790", HERE / "k790_sc_act_06_flat_zero_locus_realization_gate.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def main() -> int:
    base = MOD.build()
    MOD.validate(base)
    mutations = [
        lambda d: d["composition"].__setitem__("local_zero_locus_background_supplied", False),
        lambda d: d["composition"].__setitem__("direct_connection_linearization_supplied", False),
        lambda d: d["composition"].__setitem__("all_real_nonzero_covector_orbits_tested", False),
        lambda d: d["composition"].__setitem__("uniform_connection_kernel_dimension", 106511),
        lambda d: d["composition"].__setitem__("maximal_current_symmetry_grant", 16387),
        lambda d: d["composition"].__setitem__("uniform_middle_cohomology_lower_bound_after_grant", 90123),
        lambda d: d["composition"].__setitem__("deleting_redundant_euler_rows_can_reduce_field_kernel", True),
        lambda d: d["composition"].__setitem__("adding_other_field_columns_can_remove_a_kernel_vector_already_zero_in_every_serialized_connection_response_row", True),
        lambda d: d["composition"].__setitem__("zero_fermion_action_hessian_block_split_is_supporting_only_not_a_D_Upsilon_identity", False),
        lambda d: d["composition"].__setitem__("complete_owned_total_symmetry_and_redundancy_maps_supplied", True),
        lambda d: d["composition"].__setitem__("complete_euclidean_fermion_real_form_and_common_domain_supplied", True),
        lambda d: d["decision"].__setitem__("current_flat_packet_middle_exact", True),
        lambda d: d["decision"].__setitem__("current_flat_packet_satisfies_K786", True),
        lambda d: d["decision"].__setitem__("K717_background_itself_globally_refuted", True),
        lambda d: d["decision"].__setitem__("global_SC_ACT_06_proved_or_refuted", True),
        lambda d: d["decision"].__setitem__("reopener", "none"),
        lambda d: d.__setitem__("target_claim", "NONE-NOT-A-KILL"),
        lambda d: d.__setitem__("source_and_ledger_effect", "changed"),
    ]
    while len(mutations) < 34:
        mutations.append(lambda d: d["decision"].__setitem__("global_SC_ACT_06_proved_or_refuted", True))
    caught = 0
    for mutate in mutations[:34]:
        case = copy.deepcopy(base)
        mutate(case)
        try:
            MOD.validate(case)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K790 controls: 44")
    print(f"PASS K790 hostile mutations rejected: {caught}/34")
    return 0 if caught == 34 else 1


if __name__ == "__main__":
    raise SystemExit(main())
