#!/usr/bin/env python3
"""Hostile semantic mutations for K843."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

SCRIPT = Path(__file__).with_name("k843_sc_act_06_microlocal_cohomology_obstruction.py")
spec = importlib.util.spec_from_file_location("k843", SCRIPT)
assert spec and spec.loader
k843 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(k843)


def main() -> int:
    base = k843.build()
    mutations = [
        ("classification", "CONVENTIONAL_COMPARATOR"), ("target_claim", "NONE-NOT-A-KILL"),
        ("comparator_routing_notice", "missing"), ("gu_typed_objects.action_owner", "source-action"),
        ("theorem.operator_order", 2), ("theorem.open_covector_cone_required", False),
        ("theorem.constant_symbol_ranks_on_cone_required", False), ("theorem.principal_composition_zero_required", False),
        ("theorem.positive_middle_symbol_cohomology_required", False), ("theorem.field_Hs_growth_exponent", "s-1"),
        ("theorem.equation_Hs_minus_1_growth_exponent", "s"), ("theorem.compact_remainder_Hs_minus_1_growth_exponent", "s"),
        ("theorem.quotient_to_residual_ratio_growth_exponent", 0), ("theorem.local_elliptic_quotient_estimate_holds", True),
        ("theorem.bounded_one_derivative_splitting_follows", True), ("exact_controls.defect_complex.middle_symbol_cohomology_dimension", 0),
        ("exact_controls.exact_complex_control.middle_symbol_cohomology_dimension", 1),
        ("exact_controls.defect_amplitude", [1, 0, 0]), ("decision.local_high_frequency_obstruction_obtained", False),
        ("decision.global_fredholmness_adjudicated_without_a_global_realization", True),
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
            k843.validate(packet)
        except AssertionError:
            rejected += 1
    assert rejected == len(mutations) == base["controls"]["hostile_mutations_rejected"]
    print(f"K843 probe: rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
