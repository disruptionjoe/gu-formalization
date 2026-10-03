#!/usr/bin/env python3
"""Hostile mutations for K885."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tests/channel-swings/k885_sc_act_06_released_action_parent_quotient_inventory.py"


def load():
    spec = importlib.util.spec_from_file_location("k885", SCRIPT)
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
        lambda p: p["inventory_summary"].__setitem__("released_parent_row_count", 3),
        lambda p: p["inventory_summary"].__setitem__("closed_zero_capacity_parent_count", 1),
        lambda p: p["inventory_summary"].__setitem__("open_independent_parent_count", 0),
        lambda p: p["inventory_summary"].__setitem__("unowned_unbuilt_parent_count", 0),
        lambda p: p["inventory_summary"].__setitem__("released_independent_first_order_row_beyond_Upsilon", 1),
        lambda p: p["inventory_summary"].__setitem__("all_40_types_uncovered_by_closed_factorized_parents", False),
        lambda p: p["released_parent_inventory"][0].__setitem__("quotient_disposition", "closed_zero_quotient_capacity"),
        lambda p: p["released_parent_inventory"][1].__setitem__("induced_rank_on_injected_submodule", 1),
        lambda p: p["released_parent_inventory"][2].__setitem__("induced_rank_on_injected_submodule", 1),
        lambda p: p["released_parent_inventory"][3].__setitem__("quotient_disposition", "open_independent_map"),
        lambda p: p["decision"].__setitem__("selected_I1B_repair_capacity_closed", True),
        lambda p: p["decision"].__setitem__("source_silent_path_adapter_promoted", True),
        lambda p: p["decision"].__setitem__("absence_of_future_or_unreleased_parent_proved", True),
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
    print("K885 probe: 20/20 hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
