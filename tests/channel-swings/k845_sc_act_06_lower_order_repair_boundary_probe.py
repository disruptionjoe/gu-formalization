#!/usr/bin/env python3
"""Hostile semantic mutations for K845."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

SCRIPT = Path(__file__).with_name("k845_sc_act_06_lower_order_repair_boundary.py")
spec = importlib.util.spec_from_file_location("k845", SCRIPT)
assert spec and spec.loader
k845 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(k845)


def main() -> int:
    base = k845.build()
    mutations = [
        ("classification", "CONVENTIONAL_COMPARATOR"), ("target_claim", "NONE-NOT-A-KILL"),
        ("gu_typed_objects.action_owner", "repository-construction"),
        ("principal_invariance_theorem.zeroth_order_operator_changes_principal_symbol", True),
        ("principal_invariance_theorem.nonlinear_terms_with_same_linearization_change_principal_symbol", True),
        ("principal_invariance_theorem.interior_compactly_supported_quasimodes_are_removed_by_boundary_conditions", True),
        ("principal_invariance_theorem.regular_natural_frame_conjugacy_changes_symbol_cohomology_dimension", True),
        ("principal_invariance_theorem.regular_natural_frame_conjugacy_preserves_rank_and_kernel", False),
        ("principal_invariance_theorem.lower_order_only_repair_restores_local_elliptic_estimate", True),
        ("repair_budget.current_middle_symbol_debt", 0), ("repair_budget.necessary_threshold", "r+s>0"),
        ("repair_budget.threshold_is_sufficient", True), ("repair_budget.changed_principal_response_can_reopen", False),
        ("repair_budget.new_owned_principal_symmetry_can_reopen", False),
        ("repair_budget.genuinely_different_nonconjugate_germ_can_reopen", False),
        ("decision.current_lower_order_or_same_linearization_repair_route_open", True),
        ("decision.principal_reopener_is_exactly_localized", False),
        ("repair_classification.0.disposition", "reopen"), ("repair_classification.3.disposition", "reopen"),
        ("repair_classification.4.disposition", "cannot_repair_K844"), ("claim_ceiling", "Global no-go."),
    ]
    rejected = 0
    for path, value in mutations:
        packet = copy.deepcopy(base)
        cursor = packet
        parts = path.split(".")
        for key in parts[:-1]:
            cursor = cursor[int(key)] if key.isdigit() else cursor[key]
        key = parts[-1]
        if key.isdigit():
            cursor[int(key)] = value
        else:
            cursor[key] = value
        try:
            k845.validate(packet)
        except AssertionError:
            rejected += 1
    assert rejected == len(mutations) == base["controls"]["hostile_mutations_rejected"]
    print(f"K845 probe: rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
