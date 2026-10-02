#!/usr/bin/env python3
"""Hostile semantic mutations for K844."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

SCRIPT = Path(__file__).with_name("k844_sc_act_06_flat_symbol_sobolev_obstruction.py")
spec = importlib.util.spec_from_file_location("k844", SCRIPT)
assert spec and spec.loader
k844 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(k844)


def main() -> int:
    base = k844.build()
    mutations = [
        ("classification", "INTERNAL_STRUCTURAL_ONLY"), ("target_claim", "NONE-NOT-A-KILL"),
        ("gu_typed_objects.action_owner", "repository-construction"), ("hypothesis_match.local_coordinate_ball_supplied", False),
        ("hypothesis_match.global_torus_or_compact_realization_assumed", True), ("hypothesis_match.open_covector_cone", "native_null"),
        ("hypothesis_match.open_cone_available", False), ("hypothesis_match.connection_symbol_rank_on_cone", 122865),
        ("hypothesis_match.connection_symbol_kernel_on_cone", 106511), ("hypothesis_match.overgranted_symmetry_rank", 16387),
        ("hypothesis_match.middle_symbol_cohomology_lower_bound", 0), ("hypothesis_match.principal_composition_zero_under_grant", False),
        ("hypothesis_match.actual_owned_symmetry_is_no_larger_than_grant", False),
        ("microlocal_consequence.oscillatory_compactly_supported_sequence_exists", False),
        ("microlocal_consequence.quotient_Hs_to_residual_Hs_minus_1_ratio_unbounded", False),
        ("microlocal_consequence.local_first_order_elliptic_quotient_estimate_holds", True),
        ("microlocal_consequence.bounded_one_derivative_right_inverse_on_current_quotient_follows", True),
        ("microlocal_consequence.current_flat_symbol_complex_is_middle_elliptic", True),
        ("microlocal_consequence.global_fredholm_cohomology_dimension_computed", True),
        ("decision.current_flat_realization_crosses_K842_bounded_or_tame_splitting_row", True),
        ("decision.K717_background_globally_refuted", True), ("decision.global_SC_ACT_06_proved_or_refuted", True),
    ]
    rejected = 0
    for path, value in mutations:
        packet = copy.deepcopy(base)
        cursor = packet
        parts = path.split(".")
        for key in parts[:-1]:
            cursor = cursor[key]
        cursor[parts[-1]] = value
        try:
            k844.validate(packet)
        except AssertionError:
            rejected += 1
    assert rejected == len(mutations) == base["controls"]["hostile_mutations_rejected"]
    print(f"K844 probe: rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
