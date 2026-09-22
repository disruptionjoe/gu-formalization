#!/usr/bin/env python3
"""Independent replay and hostile controls for K291."""

from __future__ import annotations

import copy
import json
import math
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k291-order-seven-native-interior-remainder.json"
K284 = ROOT / "lab/process/k284-order-seven-transverse-shape-atlas.json"
K286 = ROOT / "lab/process/k286-order-seven-mixed-shape-derivative-bank.json"
K290 = ROOT / "lab/process/k290-order-seven-native-rest-derivative-bank.json"
getcontext().prec = 100


def d(value: Any) -> Decimal:
    return Decimal(str(value))


def close(left: Decimal, right: Decimal) -> bool:
    return abs(left - right) <= max(abs(left), abs(right), Decimal(1)) * Decimal("1e-70")


def check(payload: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    k284 = json.loads(K284.read_text())
    k286 = json.loads(K286.read_text())
    k290 = json.loads(K290.read_text())
    regularizer = [d(k284["transverse_shape_atlas"]["maximum_R_upper"])] + [
        d(k286["mixed_shape_derivative_bank"]["global_componentwise_mixed_derivative_abs_upper"][str(order)])
        for order in range(1, 5)
    ]
    rows = payload.get("coherent_group_composition", [])
    if len(rows) != 4:
        failures.append("group_count")
        return failures
    total = Decimal(0)
    for stored, source in zip(rows, k290["coherent_group_bank"]):
        rest = [d(value) for value in source["componentwise_mixed_derivative_abs_upper"]]
        contributions = [Decimal(math.comb(4, split)) * regularizer[split] * rest[4 - split] for split in range(5)]
        fourth = sum(contributions)
        if not close(fourth, d(stored["complete_fourth_shape_derivative_abs_upper"])):
            failures.append("product_rule")
        if stored.get("dominant_product_rule_split") != max(range(5), key=lambda index: contributions[index]):
            failures.append("dominant_split")
        total += fourth
    remainder = payload.get("native_density_remainder", {})
    if not close(total, d(remainder.get("complete_four_group_fourth_shape_derivative_abs_upper", "NaN"))):
        failures.append("total_fourth")
    radius = Fraction(k284["fixed_control"]["transverse_shape_radius"])
    h = Decimal(radius.numerator) / Decimal(radius.denominator)
    tensor = Decimal(6) * h**4 * total / Decimal(270)
    if not close(tensor, d(remainder.get("six_axis_normalized_shape_average_abs_upper", "NaN"))):
        failures.append("tensor_remainder")
    volume = (Decimal(2) * h) ** 6
    if not close(volume, d(remainder.get("single_shape_box_volume", "NaN"))):
        failures.append("shape_volume")
    if remainder.get("complete_native_tube_integral_emitted") is not False:
        failures.append("tube_scope")
    release = payload.get("release_test", {})
    if not release.get("native_density_included") or release.get("disjoint_native_tube_atlas_serialized"):
        failures.append("release_scope")
    if "No disjoint native tube integral" not in payload.get("claim_ceiling", ""):
        failures.append("claim_ceiling")
    return failures


def mutate(payload: dict[str, Any], name: str) -> dict[str, Any]:
    result = copy.deepcopy(payload)
    if name == "groups":
        result["coherent_group_composition"].pop()
    elif name == "product":
        result["coherent_group_composition"][0]["complete_fourth_shape_derivative_abs_upper"] = "0"
    elif name == "split":
        result["coherent_group_composition"][0]["dominant_product_rule_split"] = 4
    elif name == "total":
        result["native_density_remainder"]["complete_four_group_fourth_shape_derivative_abs_upper"] = "0"
    elif name == "tensor":
        result["native_density_remainder"]["six_axis_normalized_shape_average_abs_upper"] = "0"
    elif name == "volume":
        result["native_density_remainder"]["single_shape_box_volume"] = "1"
    elif name == "tube":
        result["native_density_remainder"]["complete_native_tube_integral_emitted"] = True
    elif name == "ceiling":
        result["claim_ceiling"] = "Complete native action column."
    return result


def main() -> int:
    payload = json.loads(MANIFEST.read_text())
    base = check(payload)
    if base:
        raise AssertionError(base)
    mutations = ("groups", "product", "split", "total", "tensor", "volume", "tube", "ceiling")
    rejected = {name: bool(check(mutate(payload, name))) for name in mutations}
    if not all(rejected.values()):
        raise AssertionError(rejected)
    print(json.dumps({"checks_passed": 7, "hostile_mutations_rejected": rejected}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
