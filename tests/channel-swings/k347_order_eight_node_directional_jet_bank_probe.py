#!/usr/bin/env python3
"""Deterministic replay and independent finite-difference controls for K347."""

from __future__ import annotations

import copy
import importlib.util
import itertools
import json
from collections import defaultdict
from pathlib import Path

from flint import arb


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k347_order_eight_node_directional_jet_bank.py")
STORED = ROOT / "lab/process/k347-order-eight-node-directional-jet-bank.json"


def load():
    spec = importlib.util.spec_from_file_location("k347_probe_target", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K347 producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def raw_complete_value(module, raw: list[arb]) -> arb:
    cumulative_s = {position: sum(raw[position - 1 : 9], arb(0)) for position in range(1, 10)}
    cumulative_v = {position: sum(raw[9 + position - 1 :], arb(0)) for position in range(1, 10)}

    def determinant(matrix):
        total = arb(0)
        for permutation in itertools.permutations(range(len(matrix))):
            inversions = sum(
                permutation[left] > permutation[right]
                for left in range(len(permutation))
                for right in range(left + 1, len(permutation))
            )
            term = arb(-1 if inversions % 2 else 1)
            for row, column in enumerate(permutation):
                term *= matrix[row][column]
            total += term
        return total

    def gram(left, right):
        value = 2 * cumulative_s[int(left["old_position"])].bessel_k(1)
        value *= 2 * cumulative_v[int(right["old_position"])].bessel_k(1)
        left_occurrences = module.K346_MODULE.occurrences(left)
        right_occurrences = module.K346_MODULE.occurrences(right)
        for species in left_occurrences:
            matrix = [
                [2 * (cumulative_s[row] + cumulative_v[column]).bessel_k(1) for column in right_occurrences[species]]
                for row in left_occurrences[species]
            ]
            value *= determinant(matrix)
        return value

    total = arb(0)
    groups = defaultdict(list)
    for term in module.K179.coefficient_family():
        if int(term["order"]) == 8:
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
        raise AssertionError("deterministic K347 replay differs")
    rows = {row["axis"]: row for row in stored["axis_node_jets"]}
    raw = [arb(1) / 256 for _ in range(18)]
    h = arb("1e-8")
    independent_checks = []
    independent_rows = []
    for axis in ["s1", "s5", "s9", "v1", "v5", "v9"]:
        index = module.AXES.index(axis)
        plus = list(raw)
        minus = list(raw)
        plus[index] += h
        minus[index] -= h
        center_value = raw_complete_value(module, raw)
        plus_value = raw_complete_value(module, plus)
        minus_value = raw_complete_value(module, minus)
        first = (plus_value - minus_value) / (2 * h)
        second = (plus_value - 2 * center_value + minus_value) / (h * h)
        stored_first = (arb(rows[axis]["raw_first_derivative_lower"]) + arb(rows[axis]["raw_first_derivative_upper"])) / 2
        stored_second = (arb(rows[axis]["raw_second_derivative_lower"]) + arb(rows[axis]["raw_second_derivative_upper"])) / 2
        first_relative = abs(float((first / stored_first - 1).mid()))
        second_relative = abs(float((second / stored_second - 1).mid()))
        independent_checks.append(first_relative < 2e-9)
        independent_checks.append(second_relative < 2e-8)
        independent_rows.append((axis, first_relative, second_relative))
    checks = [
        len(rows) == 18,
        stored["fixed_control"]["axis_entry_evaluations"] == 43200,
        stored["bank_summary"]["all_axis_jets_finite"],
        stored["bank_summary"]["complete_value_coefficient_replays_K345"],
        stored["bank_summary"]["local_node_jets_are_not_global_derivative_bounds"],
        not stored["bank_summary"]["global_second_derivative_integrals_computed"],
        not stored["bank_summary"]["complete_order_eight_remainder_emitted"],
        all(independent_checks),
    ]
    if not all(checks):
        raise AssertionError(f"K347 control failed; independent relative errors={independent_rows}")
    mutations = [
        lambda p: p["fixed_control"].__setitem__("native_axes", p["fixed_control"]["native_axes"][:-1]),
        lambda p: p["fixed_control"].__setitem__("native_raw_time_node", "1/255"),
        lambda p: p["fixed_control"].__setitem__("paths", 191),
        lambda p: p["fixed_control"].__setitem__("coherent_groups", 22),
        lambda p: p["fixed_control"].__setitem__("symmetric_node_upper_triangle_entries", 1295),
        lambda p: p["fixed_control"].__setitem__("ordered_directional_entries_per_axis", 2399),
        lambda p: p["fixed_control"].__setitem__("axis_entry_evaluations", 43199),
        lambda p: p["axis_node_jets"].pop(),
        lambda p: p["bank_summary"].__setitem__("all_axis_jets_finite", False),
        lambda p: p["bank_summary"].__setitem__("complete_value_coefficient_replays_K345", False),
        lambda p: p["bank_summary"].__setitem__("local_node_jets_are_not_global_derivative_bounds", False),
        lambda p: p["bank_summary"].__setitem__("global_second_derivative_integrals_computed", True),
        lambda p: p["bank_summary"].__setitem__("complete_order_eight_remainder_emitted", True),
        lambda p: p["release_test"].__setitem__("all_18_axes_evaluated", False),
        lambda p: p["release_test"].__setitem__("global_remainder_not_overclaimed", False),
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
        raise AssertionError(f"K347 hostile rejection changed: {rejected}/{len(mutations)}")
    print(f"K347 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
