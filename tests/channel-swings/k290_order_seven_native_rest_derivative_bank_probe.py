#!/usr/bin/env python3
"""Independent replay and hostile controls for K290."""

from __future__ import annotations

import copy
import itertools
import json
import math
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k290-order-seven-native-rest-derivative-bank.json"
K288 = ROOT / "lab/process/k288-order-seven-native-occurrence-measure.json"
getcontext().prec = 80


def d(value: Any) -> Decimal:
    return Decimal(str(value))


def product_replay(factors: list[list[Decimal]], order: int) -> Decimal:
    total = Decimal(0)
    for assignment in itertools.product(range(len(factors)), repeat=order):
        counts = [assignment.count(slot) for slot in range(len(factors))]
        term = Decimal(1)
        for factor, count in zip(factors, counts):
            term *= factor[count]
        total += term
    return total


def check(payload: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    fixed = payload.get("fixed_control", {})
    release = payload.get("release_test", {})
    endpoint = payload.get("endpoint_theorem", {})
    bank = payload.get("derivative_bank", {})
    groups = payload.get("coherent_group_bank", [])
    if fixed.get("occurrences") != 24 or not release.get("all_24_occurrences_replayed"):
        failures.append("occurrence_census")
    if fixed.get("maximum_shape_derivative_order") != 4:
        failures.append("derivative_order")
    if not endpoint.get("all_orders_finite") or "m^m" not in endpoint.get("homogeneous_maximum", ""):
        failures.append("endpoint_theorem")
    if len(groups) != 4 or any(row.get("records") != 6 for row in groups):
        failures.append("group_census")
    source = json.loads(K288.read_text())
    source_groups: dict[str, list[int]] = {}
    for row in source["coherent_gram_measure"]["size_four_occurrences"]:
        source_groups.setdefault(row["group_id"], []).append(row["signed_occurrence_weight"])
    if {row["group_id"]: row["signed_weights"] for row in groups} != source_groups:
        failures.append("group_weights")
    factor_map = bank.get("factor_componentwise_mixed_derivative_abs_upper", {})
    names = [
        "native_exponential",
        "projective_product",
        "common_size_four_cauchy_determinant",
        "companion_size_three_bessel_determinant",
        "left_endpoint_safe_old_kernel_piece",
        "right_endpoint_safe_old_kernel_piece",
    ]
    if set(factor_map) != set(names):
        failures.append("factor_inventory")
    else:
        factors = [[d(value) for value in factor_map[name]] for name in names]
        scalar = d(bank["constant_scalar_upper"]["x15_prefactor_upper"])
        stored = [d(value) for value in bank["single_occurrence_rest_componentwise_mixed_derivative_abs_upper"]]
        for order in range(5):
            replay = scalar * product_replay(factors, order)
            if replay > stored[order] * Decimal("1.00000000000002"):
                failures.append(f"product_rule_{order}")
    assignments = bank.get("labelled_product_assignments", {})
    if assignments != {str(order): 6**order for order in range(5)}:
        failures.append("labelled_assignments")
    if payload.get("factorization", {}).get("common_factor_excluded") != "K284/K286 size-four regularizer R4":
        failures.append("factor_boundary")
    ceiling = payload.get("claim_ceiling", "")
    if "No composed native interior remainder" not in ceiling or release.get("native_weighted_interior_remainder_serialized"):
        failures.append("claim_ceiling")
    return failures


def mutate(payload: dict[str, Any], name: str) -> dict[str, Any]:
    result = copy.deepcopy(payload)
    if name == "occurrences":
        result["fixed_control"]["occurrences"] = 23
    elif name == "order":
        result["fixed_control"]["maximum_shape_derivative_order"] = 3
    elif name == "endpoint":
        result["endpoint_theorem"]["all_orders_finite"] = False
    elif name == "groups":
        result["coherent_group_bank"].pop()
    elif name == "weights":
        result["coherent_group_bank"][0]["signed_weights"][1] = -1
    elif name == "factor":
        del result["derivative_bank"]["factor_componentwise_mixed_derivative_abs_upper"]["right_endpoint_safe_old_kernel_piece"]
    elif name == "assignments":
        result["derivative_bank"]["labelled_product_assignments"]["4"] -= 1
    elif name == "ceiling":
        result["release_test"]["native_weighted_interior_remainder_serialized"] = True
    return result


def main() -> int:
    payload = json.loads(MANIFEST.read_text())
    base = check(payload)
    if base:
        raise AssertionError(base)
    mutations = ("occurrences", "order", "endpoint", "groups", "weights", "factor", "assignments", "ceiling")
    rejected = {name: bool(check(mutate(payload, name))) for name in mutations}
    if not all(rejected.values()):
        raise AssertionError(rejected)
    print(json.dumps({"checks_passed": 8, "hostile_mutations_rejected": rejected}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
