#!/usr/bin/env python3
"""Independent controls and hostile mutations for K577."""

from __future__ import annotations

import copy
import importlib.util
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k577_probe_target", HERE / "k577_k152_high_order_coherent_group_target_atlas.py")
K577 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(K577)


def checks(payload: dict) -> list[bool]:
    fixed = payload["fixed_control"]
    orders = payload["order_targets"]
    return [
        payload["result_id"] == "K577-K152-HIGH-ORDER-COHERENT-GROUP-TARGET-ATLAS",
        fixed["orders"] == [8, 9, 10, 11, 12],
        fixed["resolved_vectors"] == 2720,
        fixed["coherent_groups"] == 128,
        fixed["upper_triangle_gram_entries"] == 58826,
        len(orders) == 5,
        [row["coherent_groups"] for row in orders] == [23, 20, 28, 24, 33],
        all(row["one_node_rule_is_below_order_target"] for row in orders),
        all(row["current_complete_integral_upper_exceeds_order_target"] for row in orders),
        sum(Fraction(row["sufficient_order_upper_target_exact"]) for row in orders) == Fraction(payload["target_identity"]["aggregate_high_order_allowance_exact"]),
        payload["target_identity"]["allocation_is_sufficient_not_necessary"] is True,
        payload["certificate_contract"]["retain_every_off_diagonal_cross_term"] is True,
        payload["certificate_contract"]["node_value_may_seed_but_not_replace_complete_integral"] is True,
        payload["decision"]["complete_high_order_enclosure_emitted"] is False,
        payload["decision"]["native_K152_interval_emitted"] is False,
        payload["source_and_ledger_effect"] == "none",
    ]


def main() -> int:
    payload = K577.build()
    controls = checks(payload)
    mutations = [
        lambda p: p["fixed_control"].__setitem__("resolved_vectors", 2719),
        lambda p: p["fixed_control"].__setitem__("coherent_groups", 127),
        lambda p: p["fixed_control"].__setitem__("upper_triangle_gram_entries", 58825),
        lambda p: p["order_targets"][0].__setitem__("sufficient_order_upper_target_exact", "1"),
        lambda p: p["order_targets"][0]["group_targets"][0].__setitem__("sufficient_complete_integral_upper_target_exact", "0"),
        lambda p: p["order_targets"][0].__setitem__("one_node_rule_is_below_order_target", False),
        lambda p: p["order_targets"][0].__setitem__("current_complete_integral_upper_exceeds_order_target", False),
        lambda p: p["certificate_contract"].__setitem__("retain_every_off_diagonal_cross_term", False),
        lambda p: p["certificate_contract"].__setitem__("node_value_may_seed_but_not_replace_complete_integral", False),
        lambda p: p["decision"].__setitem__("complete_high_order_enclosure_emitted", True),
        lambda p: p["decision"].__setitem__("native_K152_interval_emitted", True),
    ]
    rejected = 0
    for mutate in mutations:
        hostile = copy.deepcopy(payload)
        mutate(hostile)
        try:
            K577.validate(hostile)
        except AssertionError:
            rejected += 1
    print(f"K577 controls: {sum(controls)}/{len(controls)}; hostile: {rejected}/{len(mutations)}")
    return 0 if all(controls) and rejected == len(mutations) else 1


if __name__ == "__main__":
    raise SystemExit(main())
