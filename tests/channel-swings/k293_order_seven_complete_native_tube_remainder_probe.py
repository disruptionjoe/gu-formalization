#!/usr/bin/env python3
"""Independent exact replay and hostile controls for K293."""

from __future__ import annotations

import copy
import json
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k293-order-seven-complete-native-tube-remainder.json"
K291 = ROOT / "lab/process/k291-order-seven-native-interior-remainder.json"
K292 = ROOT / "lab/process/k292-order-seven-disjoint-native-tube-atlas.json"
getcontext().prec = 110


def d(value: Any) -> Decimal:
    if isinstance(value, str) and "/" in value:
        q = Fraction(value)
        return Decimal(q.numerator) / Decimal(q.denominator)
    return Decimal(str(value))


def close(a: Decimal, b: Decimal) -> bool:
    return abs(a - b) <= max(abs(a), abs(b), Decimal(1)) * Decimal("1e-90")


def check(payload: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    k291 = json.loads(K291.read_text())
    k292 = json.loads(K292.read_text())
    m4 = d(k291["native_density_remainder"]["complete_four_group_fourth_shape_derivative_abs_upper"])
    h = d(k292["fixed_control"]["transverse_shape_radius"])
    start_norm = Decimal(6) * h**4 * m4 / Decimal(270)
    start = d(k292["strata"]["start_box"]["exact_native_volume"]) * start_norm
    stored_start = payload.get("start_box", {})
    if stored_start.get("free_shape_axes") != 6 or not close(start, d(stored_start.get("native_shape_integral_remainder_abs_upper", "NaN"))):
        failures.append("start_box")
    faces = payload.get("swept_faces", [])
    if len(faces) != 6:
        failures.append("face_census")
        return failures
    face_norm = Decimal(5) * h**4 * m4 / Decimal(270)
    swept = Decimal(0)
    for stored, source in zip(faces, k292["strata"]["swept_faces"]):
        expected = d(source["exact_native_volume"]) * face_norm
        swept += expected
        if stored.get("free_shape_axes") != 5 or stored.get("native_jacobian") != source["native_jacobian"]:
            failures.append("face_scope")
        if not close(expected, d(stored.get("native_shape_integral_remainder_abs_upper", "NaN"))):
            failures.append("face_remainder")
    result = payload.get("complete_native_tube_remainder", {})
    total = start + swept
    if not close(swept, d(result.get("swept_faces_contribution", "NaN"))):
        failures.append("swept_total")
    if not close(total, d(result.get("native_shape_integral_abs_upper", "NaN"))):
        failures.append("shape_total")
    full = Decimal(1) / Decimal(256) * total
    if not close(full, d(result.get("x_y_u_z_integrated_abs_upper", "NaN"))):
        failures.append("x_width")
    if not result.get("complete_k284_interior_tube_serialized") or result.get("radial_or_projective_exterior_serialized"):
        failures.append("scope")
    if "no radial/projective exterior bound" not in payload.get("claim_ceiling", ""):
        failures.append("claim_ceiling")
    return failures


def mutate(payload: dict[str, Any], name: str) -> dict[str, Any]:
    result = copy.deepcopy(payload)
    if name == "face": result["swept_faces"].pop()
    elif name == "start_axes": result["start_box"]["free_shape_axes"] = 5
    elif name == "face_axes": result["swept_faces"][0]["free_shape_axes"] = 6
    elif name == "jacobian": result["swept_faces"][0]["native_jacobian"] = "1/1"
    elif name == "face_value": result["swept_faces"][0]["native_shape_integral_remainder_abs_upper"] = "0"
    elif name == "swept_total": result["complete_native_tube_remainder"]["swept_faces_contribution"] = "0"
    elif name == "x_width": result["complete_native_tube_remainder"]["x_y_u_z_integrated_abs_upper"] = "0"
    elif name == "scope": result["complete_native_tube_remainder"]["radial_or_projective_exterior_serialized"] = True
    elif name == "ceiling": result["claim_ceiling"] = "Complete native action column."
    return result


def main() -> int:
    payload = json.loads(MANIFEST.read_text())
    baseline = check(payload)
    if baseline:
        raise AssertionError(baseline)
    names = ("face", "start_axes", "face_axes", "jacobian", "face_value", "swept_total", "x_width", "scope", "ceiling")
    rejected = {name: bool(check(mutate(payload, name))) for name in names}
    if not all(rejected.values()):
        raise AssertionError(rejected)
    print(json.dumps({"checks_passed": 9, "hostile_mutations_rejected": rejected}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
