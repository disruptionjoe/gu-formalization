#!/usr/bin/env python3
"""Deterministic replay and hostile mutations for K381."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k381_order_nine_group_interval_evaluator.py")
STORED = ROOT / "lab/process/k381-order-nine-group-interval-evaluator.json"


def load():
    spec = importlib.util.spec_from_file_location("k381_probe_target", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K381 producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    stored = json.loads(STORED.read_text())
    if stored != module.build():
        raise AssertionError("deterministic K381 replay differs")
    value = stored["complete_node_evaluation"]
    checks = [
        stored["fixed_control"]["paths"] == 256,
        stored["fixed_control"]["coherent_groups"] == 20,
        stored["fixed_control"]["upper_triangle_gram_entries"] == 2368,
        stored["fixed_control"]["ordered_quadratic_terms"] == 4480,
        stored["fixed_control"]["maximum_species_determinant_rank"] == 5,
        stored["fixed_control"]["native_prefactor"] == "(2*pi)^-11",
        stored["assembly_contract"]["all_2368_transpose_symmetry_checks_pass"],
        stored["assembly_contract"]["all_4480_ordered_terms_replayed"],
        stored["assembly_contract"]["strictly_positive_individual_gram_entries"] == 2368,
        value["signed_rule_value_is_strictly_positive"],
        0 < float(value["normalized_one_node_rule_lower"]) <= float(value["normalized_one_node_rule_upper"]),
        not stored["decision"]["complete_order_nine_integral_emitted"],
    ]
    if not all(checks):
        raise AssertionError("K381 control failed")
    mutations = [
        lambda p: p["fixed_control"].__setitem__("paths", 255),
        lambda p: p["fixed_control"].__setitem__("coherent_groups", 19),
        lambda p: p["fixed_control"].__setitem__("upper_triangle_gram_entries", 2367),
        lambda p: p["fixed_control"].__setitem__("ordered_quadratic_terms", 4479),
        lambda p: p["fixed_control"].__setitem__("maximum_species_determinant_rank", 4),
        lambda p: p["fixed_control"].__setitem__("native_prefactor", "(2*pi)^-10"),
        lambda p: p["complete_node_evaluation"].__setitem__("signed_rule_value_is_strictly_positive", False),
        lambda p: p["assembly_contract"].__setitem__("all_4480_ordered_terms_replayed", False),
        lambda p: p["assembly_contract"].__setitem__("occurrencewise_absolute_value_used", True),
        lambda p: p["assembly_contract"].__setitem__("order_eight_weight_or_prefactor_reused", True),
        lambda p: p["decision"].__setitem__("complete_order_nine_integral_emitted", True),
        lambda p: p["release_test"].__setitem__("native_K152_interval_emitted", True),
    ]
    rejected = 0
    for mutation in mutations:
        candidate = copy.deepcopy(stored)
        mutation(candidate)
        try:
            module.validate_payload(candidate)
        except AssertionError:
            rejected += 1
    if rejected != len(mutations):
        raise AssertionError("K381 hostile mutation survived")
    print(f"K381 order-nine evaluator probe passed ({sum(checks)}/{len(checks)} controls; {rejected}/{len(mutations)} hostile mutations rejected)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
