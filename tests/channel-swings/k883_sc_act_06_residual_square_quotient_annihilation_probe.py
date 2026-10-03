#!/usr/bin/env python3
"""Hostile mutations for K883."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tests/channel-swings/k883_sc_act_06_residual_square_quotient_annihilation.py"


def load():
    spec = importlib.util.spec_from_file_location("k883", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    base = module.build()
    mutations = [
        lambda p: p.__setitem__("target_claim", "SC-ACT-05"),
        lambda p: p.__setitem__("classification", "CONDITIONAL_COMPARATOR"),
        lambda p: p.__setitem__("pinned_inputs", {}),
        lambda p: p["annihilation_theorem"].__setitem__("factorization", "H_Q=QJ"),
        lambda p: p["annihilation_theorem"].__setitem__("old_cocycle_condition", "J h!=0"),
        lambda p: p["annihilation_theorem"].__setitem__("descends_to_old_cohomology", False),
        lambda p: p["annihilation_theorem"].__setitem__("induced_quotient_map_is_zero", False),
        lambda p: p["annihilation_theorem"].__setitem__("induced_quotient_rank", 1),
        lambda p: p["annihilation_theorem"].__setitem__("uniform_for_every_admissible_pairing_and_weight", False),
        lambda p: p["annihilation_theorem"].__setitem__("zero_map_is_SO6xSO7_equivariant", False),
        lambda p: p["annihilation_theorem"].__setitem__("injected_submodule_dimension", 90124),
        lambda p: p["annihilation_theorem"].__setitem__("complete_full_field_complement_tested", True),
        lambda p: p["repair_consequence"].__setitem__("raw_rank_is_repair_capacity", True),
        lambda p: p["repair_consequence"].__setitem__("same_response_residual_square_repairs_injected_submodule", True),
        lambda p: p["repair_consequence"].__setitem__("selected_I1B_induced_map_computed", True),
        lambda p: p["repair_consequence"].__setitem__("genuinely_independent_response_excluded", True),
        lambda p: p["decision"].__setitem__("complete_flat_packet_repairability_refuted", True),
        lambda p: p["decision"].__setitem__("SC_ACT_06_proved_or_refuted", True),
        lambda p: p.__setitem__("source_and_ledger_effect", "PROMOTED"),
        lambda p: p["controls"].__setitem__("hostile_mutations_rejected", 19),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(base)
        mutate(candidate)
        try:
            module.validate(candidate)
        except (AssertionError, KeyError, ValueError):
            rejected += 1
    assert rejected == len(mutations) == 20
    print("K883 probe: 20/20 hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
