#!/usr/bin/env python3
"""Independent replay and hostile controls for K345."""

from __future__ import annotations

import copy
import importlib.util
import json
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy.special import k1


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k345_order_eight_group_interval_evaluator.py")
STORED = ROOT / "lab/process/k345-order-eight-group-interval-evaluator.json"


def load():
    spec = importlib.util.spec_from_file_location("k345_probe_target", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K345 producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def independent_scipy_value(module):
    """Full ordered replay with distinct double-precision linear algebra."""
    cumulative = {position: (10 - position) / 256 for position in range(1, 10)}
    old_kernel = {position: 2 * k1(value) for position, value in cumulative.items()}
    pair_kernel = {
        (left, right): 2 * k1(cumulative[left] + cumulative[right])
        for left in range(1, 10)
        for right in range(1, 10)
    }

    def occurrences(term):
        result = defaultdict(list)
        for position, species in zip(term["output_variable_provenance"], term["output_letters"], strict=True):
            result[str(species)].append(int(position))
        return dict(sorted(result.items()))

    def gram(left, right):
        value = old_kernel[int(left["old_position"])] * old_kernel[int(right["old_position"])]
        left_occurrences = occurrences(left)
        right_occurrences = occurrences(right)
        for species in left_occurrences:
            matrix = np.array(
                [
                    [pair_kernel[(row, column)] for column in right_occurrences[species]]
                    for row in left_occurrences[species]
                ],
                dtype=float,
            )
            value *= float(np.linalg.det(matrix))
        return value

    groups = defaultdict(list)
    for term in module.K179.coefficient_family():
        if int(term["order"]) == 8:
            groups[(int(term["seed_impurity"]), str(term["output_signature"]))].append(term)
    total = 0.0
    for terms in groups.values():
        for left in terms:
            for right in terms:
                total += (
                    int(left["exact_operator_coefficient"])
                    * int(right["exact_operator_coefficient"])
                    * gram(left, right)
                )
    return total * 256.0**-18 * (2 * np.pi) ** -10


def main() -> int:
    module = load()
    stored = json.loads(STORED.read_text())
    rebuilt = module.build()
    if stored != rebuilt:
        raise AssertionError("deterministic K345 replay differs")
    value = stored["complete_node_evaluation"]
    lower = float(value["normalized_one_node_rule_lower"])
    upper = float(value["normalized_one_node_rule_upper"])
    independent = independent_scipy_value(module)
    checks = [
        stored["fixed_control"]["paths"] == 192,
        stored["fixed_control"]["coherent_groups"] == 23,
        stored["fixed_control"]["upper_triangle_gram_entries"] == 1296,
        stored["fixed_control"]["ordered_quadratic_terms"] == 2400,
        len(stored["coherent_group_values"]) == 23,
        sum(row["upper_triangle_entries"] for row in stored["coherent_group_values"]) == 1296,
        sum(row["ordered_quadratic_terms"] for row in stored["coherent_group_values"]) == 2400,
        3.0e-35 < lower <= upper < 3.2e-35,
        abs(independent / ((lower + upper) / 2) - 1) < 2e-12,
        value["signed_rule_value_is_strictly_positive"],
        stored["assembly_contract"]["all_1296_transpose_symmetry_checks_pass"],
        stored["assembly_contract"]["strictly_positive_individual_gram_entries"] == 1296,
        stored["release_test"]["upper_triangle_equals_full_ordered_replay"],
        not stored["remainder_boundary"]["complete_order_eight_remainder_radius_emitted"],
        not stored["decision"]["complete_order_eight_integral_emitted"],
        not stored["decision"]["native_K152_interval_emitted"],
    ]
    if not all(checks):
        raise AssertionError("K345 control failed")
    mutations = [
        lambda p: p["fixed_control"].__setitem__("paths", 191),
        lambda p: p["fixed_control"].__setitem__("coherent_groups", 22),
        lambda p: p["fixed_control"].__setitem__("upper_triangle_gram_entries", 1295),
        lambda p: p["fixed_control"].__setitem__("ordered_quadratic_terms", 2399),
        lambda p: p["fixed_control"].__setitem__("native_time_node", ["1/255"] * 18),
        lambda p: p["fixed_control"].__setitem__("native_prefactor", "(2*pi)^-9"),
        lambda p: p["complete_node_evaluation"].__setitem__("normalized_one_node_rule_lower", "0"),
        lambda p: p["complete_node_evaluation"].__setitem__("signed_rule_value_is_strictly_positive", False),
        lambda p: p["assembly_contract"].__setitem__("all_1296_upper_triangle_entries_evaluated", False),
        lambda p: p["assembly_contract"].__setitem__("all_2400_ordered_terms_independently_replayed", False),
        lambda p: p["assembly_contract"].__setitem__("all_coefficients_retained", False),
        lambda p: p["assembly_contract"].__setitem__("all_coherent_cross_terms_retained", False),
        lambda p: p["assembly_contract"].__setitem__("occurrencewise_absolute_value_used", True),
        lambda p: p["assembly_contract"].__setitem__("K299_weight_reused", True),
        lambda p: p["remainder_boundary"].__setitem__("global_second_derivative_integrals_computed", True),
        lambda p: p["remainder_boundary"].__setitem__("complete_order_eight_remainder_radius_emitted", True),
        lambda p: p["decision"].__setitem__("normalized_order_eight_one_node_value_emitted", False),
        lambda p: p["decision"].__setitem__("complete_order_eight_integral_emitted", True),
        lambda p: p["decision"].__setitem__("native_K152_interval_emitted", True),
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
        raise AssertionError(f"K345 hostile rejection changed: {rejected}/{len(mutations)}")
    print(f"K345 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
