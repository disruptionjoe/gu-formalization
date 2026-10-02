#!/usr/bin/env python3
"""Hostile mutations for K794."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tests/channel-swings/k794_sc_act_06_released_flat_realization_closure.py"


def load():
    spec = importlib.util.spec_from_file_location("k794", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    base = module.build()
    mutations = [
        lambda p: p.__setitem__("result_id", "K794-MUTANT"),
        lambda p: p.__setitem__("target_claim", "SC-ACT-04"),
        lambda p: p.__setitem__("classification", "CONDITIONAL_COMPARATOR"),
        lambda p: p["composition"].__setitem__("released_independent_first_order_bosonic_rows_beyond_Upsilon", 1),
        lambda p: p["composition"].__setitem__("xi_factors_through_D_Upsilon_on_zero_locus", False),
        lambda p: p["composition"].__setitem__("xi_reduces_connection_kernel", True),
        lambda p: p["composition"].__setitem__("zero_fermion_full_field_extension_reduces_embedded_connection_kernel", True),
        lambda p: p["composition"].__setitem__("distinct_i2b_row_imported_into_first_order_packet", True),
        lambda p: p["composition"].__setitem__("maximal_current_symmetry_grant", 16389),
        lambda p: p["composition"].__setitem__("uniform_persistent_middle_classes", 90123),
        lambda p: p["decision"].__setitem__("K717_is_complete_elliptic_realization_under_released_serialization", True),
        lambda p: p["decision"].__setitem__("K717_direct_released_source_packet_closed", False),
        lambda p: p["decision"].__setitem__("K717_background_is_not_a_solution_of_Upsilon_zero", True),
        lambda p: p["decision"].__setitem__("global_SC_ACT_06_proved_or_refuted", True),
        lambda p: p["decision"].__setitem__("source_claim_status_changes", True),
        lambda p: p["decision"].__setitem__("next_direct_frontier", "none"),
        lambda p: p["decision"].__setitem__("revival_trigger", "none"),
        lambda p: p["protected_effects"].__setitem__("sc_act_06", "REFUTED"),
        lambda p: p["protected_effects"].__setitem__("source_register", "CHANGED"),
        lambda p: p["protected_effects"].__setitem__("physics_ledger", "CHANGED"),
        lambda p: p["protected_effects"].__setitem__("canon", "CHANGED"),
        lambda p: p["protected_effects"].__setitem__("paper_and_public_posture", "CHANGED"),
        lambda p: p["protected_effects"].__setitem__("prediction_confirmation_physical_verdict", "CHANGED"),
        lambda p: p.__setitem__("source_and_ledger_effect", "PROMOTED"),
        lambda p: p.__setitem__("pinned_inputs", {}),
        lambda p: p["composition"].__setitem__("uniform_persistent_middle_classes", 0),
        lambda p: p["composition"].__setitem__("maximal_current_symmetry_grant", 106512),
        lambda p: p["decision"].__setitem__("next_direct_frontier", "another germ only"),
        lambda p: p["decision"].__setitem__("revival_trigger", "additional symmetry"),
        lambda p: p["composition"].__setitem__("xi_factors_through_D_Upsilon_on_zero_locus", 0),
        lambda p: p["decision"].__setitem__("K717_direct_released_source_packet_closed", 0),
        lambda p: p["decision"].__setitem__("source_claim_status_changes", 1),
    ]
    assert len(mutations) == 32
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(base)
        mutate(candidate)
        try:
            module.validate(candidate)
        except (AssertionError, KeyError, ValueError):
            rejected += 1
    assert rejected == len(mutations)
    print(f"K794 probe: {rejected}/{len(mutations)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
