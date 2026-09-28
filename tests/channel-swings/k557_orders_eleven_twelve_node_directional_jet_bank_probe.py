#!/usr/bin/env python3
"""Deterministic replay and hostile controls for K557."""

from __future__ import annotations

import copy
import importlib.util
import itertools
import json
from collections import defaultdict
from functools import lru_cache
from pathlib import Path

from flint import arb


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k557_orders_eleven_twelve_node_directional_jet_bank.py")
STORED = ROOT / "lab/process/k557-orders-eleven-twelve-node-directional-jet-bank.json"


def load():
    spec = importlib.util.spec_from_file_location("k557_probe_target", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K557 producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def raw_complete_value(module, order: int, raw: list[arb]) -> arb:
    side = order + 1
    cumulative_s = {position: sum(raw[position - 1 : side], arb(0)) for position in range(1, side + 1)}
    cumulative_v = {position: sum(raw[side + position - 1 :], arb(0)) for position in range(1, side + 1)}

    @lru_cache(maxsize=None)
    def kernel(side_name: str, position: int) -> arb:
        argument = cumulative_s[position] if side_name == "s" else cumulative_v[position]
        return 2 * argument.bessel_k(1)

    @lru_cache(maxsize=None)
    def entry(row: int, column: int) -> arb:
        return 2 * (cumulative_s[row] + cumulative_v[column]).bessel_k(1)

    @lru_cache(maxsize=None)
    def determinant(rows: tuple[int, ...], columns: tuple[int, ...]):
        total = arb(0)
        for permutation in itertools.permutations(range(len(rows))):
            inversions = sum(
                permutation[left] > permutation[right]
                for left in range(len(permutation))
                for right in range(left + 1, len(permutation))
            )
            term = arb(-1 if inversions % 2 else 1)
            for row, column in enumerate(permutation):
                term *= entry(rows[row], columns[column])
            total += term
        return total

    def gram(left, right):
        value = kernel("s", int(left["old_position"]))
        value *= kernel("v", int(right["old_position"]))
        left_occurrences = module.K556_MODULE.occurrences(left)
        right_occurrences = module.K556_MODULE.occurrences(right)
        for species in left_occurrences:
            value *= determinant(tuple(left_occurrences[species]), tuple(right_occurrences[species]))
        return value

    total = arb(0)
    groups = defaultdict(list)
    for term in module.K556_MODULE.K179.coefficient_family():
        if int(term["order"]) == order:
            groups[(int(term["seed_impurity"]), str(term["output_signature"]))].append(term)
    for terms in groups.values():
        for left in terms:
            for right in terms:
                total += int(left["exact_operator_coefficient"]) * int(right["exact_operator_coefficient"]) * gram(left, right)
    return total


def main() -> int:
    module = load()
    stored = json.loads(STORED.read_text())
    if stored != module.build():
        raise AssertionError("deterministic K557 replay differs")
    rows = {row["order"]: row for row in stored["order_banks"]}
    independent_checks = []
    independent_rows = []
    h = arb("1e-8")
    for order in (11, 12):
        side = order + 1
        axes = [f"s{i}" for i in range(1, side + 1)] + [f"v{i}" for i in range(1, side + 1)]
        stored_axes = {row["axis"]: row for row in rows[order]["axis_node_jets"]}
        raw = [arb(1) / 256 for _ in axes]
        center = raw_complete_value(module, order, raw)
        for axis in (f"s1", f"s{(side + 1)//2}", f"v{side}"):
            index = axes.index(axis)
            plus = list(raw)
            minus = list(raw)
            plus[index] += h
            minus[index] -= h
            plus_value = raw_complete_value(module, order, plus)
            minus_value = raw_complete_value(module, order, minus)
            first = (plus_value - minus_value) / (2 * h)
            second = (plus_value - 2 * center + minus_value) / (h * h)
            stored_first = (arb(stored_axes[axis]["raw_first_derivative_lower"]) + arb(stored_axes[axis]["raw_first_derivative_upper"])) / 2
            stored_second = (arb(stored_axes[axis]["raw_second_derivative_lower"]) + arb(stored_axes[axis]["raw_second_derivative_upper"])) / 2
            first_relative = abs(float((first / stored_first - 1).mid()))
            second_relative = abs(float((second / stored_second - 1).mid()))
            independent_checks.extend((first_relative < 2e-9, second_relative < 2e-8))
            independent_rows.append((order, axis, first_relative, second_relative))
    checks = [
        list(rows) == [11, 12],
        len(rows[11]["axis_node_jets"]) == 24,
        len(rows[12]["axis_node_jets"]) == 26,
        stored["fixed_control"]["combined_axis_entry_evaluations"] == 2413152,
        all(row["bank_summary"]["all_axis_jets_finite"] for row in rows.values()),
        all(row["bank_summary"]["complete_value_coefficient_replays_K555"] for row in rows.values()),
        all(row["bank_summary"]["local_node_jets_are_not_global_derivative_bounds"] for row in rows.values()),
        not stored["decision"]["global_second_derivative_integrals_computed"],
        not stored["decision"]["complete_order_eleven_integral_emitted"],
        not stored["decision"]["complete_order_twelve_integral_emitted"],
        all(independent_checks),
    ]
    if not all(checks):
        raise AssertionError(f"K557 control failed; independent relative errors={independent_rows}")
    mutations = [
        lambda p: p["fixed_control"].__setitem__("combined_paths", 1791),
        lambda p: p["fixed_control"].__setitem__("combined_groups", 56),
        lambda p: p["fixed_control"].__setitem__("combined_symmetric_node_entries", 48271),
        lambda p: p["fixed_control"].__setitem__("combined_ordered_directional_entries", 94751),
        lambda p: p["fixed_control"].__setitem__("combined_native_axes", 49),
        lambda p: p["fixed_control"].__setitem__("combined_axis_entry_evaluations", 2413151),
        lambda p: p["order_banks"].pop(),
        lambda p: p["order_banks"][0]["fixed_control"].__setitem__("native_raw_time_node", "1/255"),
        lambda p: p["order_banks"][0]["axis_node_jets"].pop(),
        lambda p: p["order_banks"][1]["bank_summary"].__setitem__("all_axis_jets_finite", False),
        lambda p: p["order_banks"][1]["bank_summary"].__setitem__("complete_value_coefficient_replays_K555", False),
        lambda p: p["order_banks"][0]["bank_summary"].__setitem__("local_node_jets_are_not_global_derivative_bounds", False),
        lambda p: p["order_banks"][0]["bank_summary"].__setitem__("global_second_derivative_integrals_computed", True),
        lambda p: p["decision"].__setitem__("complete_first_second_node_jets_evaluated", False),
        lambda p: p["decision"].__setitem__("complete_order_eleven_integral_emitted", True),
        lambda p: p["decision"].__setitem__("complete_order_twelve_integral_emitted", True),
        lambda p: p["decision"].__setitem__("native_K152_interval_emitted", True),
        lambda p: p["release_test"].__setitem__("global_remainders_not_overclaimed", False),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(stored)
        mutate(candidate)
        try:
            module.validate_payload(candidate)
        except AssertionError:
            rejected += 1
    if rejected != len(mutations):
        raise AssertionError(f"K557 hostile rejection changed: {rejected}/{len(mutations)}")
    print(f"K557 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
