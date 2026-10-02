#!/usr/bin/env python3
"""Hostile mutations for K791."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tests/channel-swings/k791_sc_act_06_released_first_order_row_inventory.py"


def load():
    spec = importlib.util.spec_from_file_location("k791", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    base = module.build()
    mutations = []
    for key in base["source_witnesses"]:
        mutations.append(lambda p, k=key: p["source_witnesses"].__setitem__(k, False))
    for key in base["typing"]:
        mutations.append(lambda p, k=key: p["typing"].__setitem__(k, False))
    mutations += [
        lambda p: p.__setitem__("result_id", "K791-MUTANT"),
        lambda p: p.__setitem__("target_claim", "SC-ACT-01"),
        lambda p: p.__setitem__("classification", "CONVENTIONAL_COMPARATOR"),
        lambda p: p["inventory"]["first_order_bosonic_residual_rows"].append("invented row"),
        lambda p: p["inventory"]["first_order_fermion_rows"].clear(),
        lambda p: p["inventory"].__setitem__("redundant_rows", []),
        lambda p: p["inventory"]["distinct_second_action_rows"].clear(),
        lambda p: p["inventory"]["field_columns_not_equation_rows"].remove("metric g"),
        lambda p: p["inventory"]["field_columns_not_equation_rows"].remove("source epsilon"),
        lambda p: p["inventory"]["field_columns_not_equation_rows"].remove("connection varpi"),
        lambda p: p["inventory"]["field_columns_not_equation_rows"].remove("fermions"),
        lambda p: p["inventory"]["additional_released_first_order_bosonic_row_independent_of_Upsilon"].append("invented"),
        lambda p: p["decision"].__setitem__("released_independent_first_order_bosonic_row_count_beyond_Upsilon", 1),
        lambda p: p["decision"].__setitem__("only_displayed_extra_bosonic_equation_is_declared_redundant", False),
        lambda p: p["decision"].__setitem__("source_inventory_supplies_K790_missing_independent_row", True),
        lambda p: p.__setitem__("source_and_ledger_effect", "PROMOTED"),
        lambda p: p.__setitem__("pinned_inputs", {}),
        lambda p: p["inventory"].__setitem__("first_order_bosonic_residual_rows", []),
        lambda p: p["inventory"].__setitem__("first_order_fermion_rows", ["one"]),
    ]
    assert len(mutations) == 28
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(base)
        mutate(candidate)
        try:
            module.validate(candidate)
        except (AssertionError, KeyError, ValueError):
            rejected += 1
    assert rejected == len(mutations)
    print(f"K791 probe: {rejected}/{len(mutations)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
