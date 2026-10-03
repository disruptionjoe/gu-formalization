#!/usr/bin/env python3
"""Hostile mutations for K886."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tests/channel-swings/k886_sc_act_06_released_repair_disposition.py"


def load():
    spec = importlib.util.spec_from_file_location("k886", SCRIPT)
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
        lambda p: p["released_repair_certificate"].__setitem__("row_count", 6),
        lambda p: p["released_repair_certificate"].__setitem__("satisfied_row_count", 5),
        lambda p: p["released_repair_certificate"].__setitem__("failed_or_open_row_count", 2),
        lambda p: p["released_repair_certificate"].__setitem__("injected_dimension", 90124),
        lambda p: p["released_repair_certificate"].__setitem__("real_irreducible_type_count", 39),
        lambda p: p["released_repair_certificate"].__setitem__("released_factorized_failed_type_count", 39),
        lambda p: p["released_repair_certificate"]["rows"].__setitem__("same-response residual-square quotient capacity zero", False),
        lambda p: p["released_repair_certificate"]["rows"].__setitem__("selected-I1B induced quotient character known", True),
        lambda p: p["corrected_completion_gate"].__setitem__("satisfied_row_count", 6),
        lambda p: p["corrected_completion_gate"].__setitem__("failed_row_count", 5),
        lambda p: p["corrected_completion_gate"].__setitem__("current_GU_candidate_admitted", True),
        lambda p: p["decision"].__setitem__("selected_I1B_route_excluded", True),
        lambda p: p["decision"].__setitem__("future_or_unreleased_action_parent_excluded", True),
        lambda p: p["decision"].__setitem__("complete_flat_packet_repairability_refuted", True),
        lambda p: p["decision"].__setitem__("global_SC_ACT_06_proved_or_refuted", True),
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
    print("K886 probe: 20/20 hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
