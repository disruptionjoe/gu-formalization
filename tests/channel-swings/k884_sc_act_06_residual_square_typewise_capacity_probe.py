#!/usr/bin/env python3
"""Hostile mutations for K884."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tests/channel-swings/k884_sc_act_06_residual_square_typewise_capacity.py"


def load():
    spec = importlib.util.spec_from_file_location("k884", SCRIPT)
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
        lambda p: p["typewise_capacity"].__setitem__("common_stabilizer", "SO(13)"),
        lambda p: p["typewise_capacity"].__setitem__("row_count", 39),
        lambda p: p["typewise_capacity"].__setitem__("failed_released_factorized_row_count", 39),
        lambda p: p["typewise_capacity"].__setitem__("sum_of_injected_multiplicity_lower_bounds", 168),
        lambda p: p["typewise_capacity"].__setitem__("dimension_of_injected_lower_bound", 90124),
        lambda p: p["typewise_capacity"].__setitem__("all_same_response_capacities_zero", False),
        lambda p: p["typewise_capacity"]["rows"][0].__setitem__("displayed_mixed_capacity", 1),
        lambda p: p["typewise_capacity"]["rows"][0].__setitem__("redundant_xi_capacity", 1),
        lambda p: p["typewise_capacity"]["rows"][0].__setitem__("same_response_residual_square_capacity", 1),
        lambda p: p["typewise_capacity"]["rows"][0].__setitem__("total_released_factorized_capacity", 1),
        lambda p: p["typewise_capacity"]["rows"][0].__setitem__("remaining_deficit_lower_bound", 0),
        lambda p: p["decision"].__setitem__("released_factorized_routes_cover_any_injected_type", True),
        lambda p: p["decision"].__setitem__("selected_I1B_typewise_capacity_known", True),
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
    print("K884 probe: 20/20 hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
