#!/usr/bin/env python3
"""Hostile mutations for K792."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tests/channel-swings/k792_sc_act_06_redundant_prolongation_kernel_theorem.py"


def load():
    spec = importlib.util.spec_from_file_location("k792", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    base = module.build()
    mutations = [
        lambda p: p.__setitem__("result_id", "K792-MUTANT"),
        lambda p: p.__setitem__("target_claim", "SC-ACT-04"),
        lambda p: p.__setitem__("classification", "CONDITIONAL_COMPARATOR"),
        lambda p: p["linearization"].__setitem__("background_residual_zero", False),
        lambda p: p["linearization"].__setitem__("identity", "wrong"),
        lambda p: p["linearization"].__setitem__("zero_locus_reduction", "wrong"),
        lambda p: p["linearization"].__setitem__("principal_factorization", "wrong"),
        lambda p: p["linearization"].__setitem__("variation_of_connection_times_background_residual_vanishes", False),
        lambda p: p["linearization"].__setitem__("xi_row_factors_through_direct_response", False),
        lambda p: p["exact_consequence"].__setitem__("connection_domain_dimension", 229375),
        lambda p: p["exact_consequence"].__setitem__("direct_response_rank", 122863),
        lambda p: p["exact_consequence"].__setitem__("direct_response_kernel_dimension", 106511),
        lambda p: p["exact_consequence"].__setitem__("stacked_row_rank", 122865),
        lambda p: p["exact_consequence"].__setitem__("stacked_row_kernel_dimension", 106511),
        lambda p: p["exact_consequence"].__setitem__("all_three_real_nonzero_covector_orbits", False),
        lambda p: p["decision"].__setitem__("xi_can_act_nontrivially_on_a_vector_killed_by_J", True),
        lambda p: p["decision"].__setitem__("xi_supplies_K790_missing_independent_row", True),
        lambda p: p["decision"].__setitem__("discarding_xi_changes_field_kernel", True),
        lambda p: p.__setitem__("source_and_ledger_effect", "PROMOTED"),
        lambda p: p.__setitem__("pinned_inputs", {}),
        lambda p: p["exact_consequence"].__setitem__("direct_response_rank", 229376),
        lambda p: p["exact_consequence"].__setitem__("direct_response_kernel_dimension", 0),
        lambda p: p["exact_consequence"].__setitem__("stacked_row_rank", 0),
        lambda p: p["exact_consequence"].__setitem__("stacked_row_kernel_dimension", 229376),
        lambda p: p["linearization"].__setitem__("background_residual_zero", 0),
        lambda p: p["exact_consequence"].__setitem__("connection_domain_dimension", 229377),
    ]
    assert len(mutations) == 26
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(base)
        mutate(candidate)
        try:
            module.validate(candidate)
        except (AssertionError, KeyError, ValueError):
            rejected += 1
    assert rejected == len(mutations)
    print(f"K792 probe: {rejected}/{len(mutations)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
