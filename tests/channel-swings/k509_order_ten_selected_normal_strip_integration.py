#!/usr/bin/env python3
"""Integrate K508's selected equal-normal order-ten interval cells."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
K508 = ROOT / "lab/process/k508-order-ten-selected-face-cell-bank.json"
OUTPUT = ROOT / "lab/process/k509-order-ten-selected-normal-strip-integration.json"

ctx.dps = 180
ctx.threads = 1


def digest(payload: Any) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def upper(value: arb) -> str:
    return repr(math.nextafter(float(abs(value).upper()), math.inf))


def power_integral(left: Fraction, right: Fraction, exponent: int) -> Fraction:
    if exponent <= -1:
        raise AssertionError("nonintegrable K509 normal power")
    return (right ** (exponent + 1) - left ** (exponent + 1)) / (exponent + 1)


def build() -> dict[str, Any]:
    k508 = json.loads(K508.read_text())
    if not k508["decision"]["K485_preconditioned_selected_positive_width_face_cells_released"]:
        raise AssertionError("K508 selected face cells unavailable")
    intervals = [[Fraction(a), Fraction(b)] for a, b in k508["fixed_control"]["normal_cells"]]
    if intervals[0][0] != Fraction(1, 4096) or intervals[-1][1] != Fraction(1, 1024):
        raise AssertionError("K509 selected strip changed")
    for left, right in zip(intervals, intervals[1:], strict=False):
        if left[1] != right[0]:
            raise AssertionError("K508 cells do not form a contiguous partition")

    rows = []
    by_axis: dict[str, list[arb]] = defaultdict(list)
    active_count = 0
    for face in k508["selected_face_cell_bank"]:
        codimension = int(face["codimension"])
        singular_power = int(face["maximum_second_singular_power"])
        active = bool(face["active_peano_axis_zeroed"])
        exponent = codimension - 1 - singular_power + (2 if active else 0)
        if exponent != int(face["minimum_face_normal_power"]):
            raise AssertionError("K509 failed to replay K486 normal exponent")
        peano_coefficient = Fraction(1, 2 * codimension * codimension) if active else Fraction(1, 2 * 256 * 256)
        cell_rows = []
        face_total = arb(0)
        for stored, (left, right) in zip(face["cells"], intervals, strict=True):
            if [Fraction(value) for value in stored["normal_interval"]] != [left, right]:
                raise AssertionError("K508 interval partition changed")
            mass = power_integral(left, right, exponent)
            scaled_upper = arb(stored["rho_to_K486_second_singular_power_abs_upper"])
            contribution = scaled_upper * arb(q(peano_coefficient * mass))
            if not math.isfinite(float(contribution.upper())) or contribution.upper() <= 0:
                raise AssertionError("K509 non-finite strip contribution")
            face_total += contribution
            cell_rows.append({
                "normal_interval": stored["normal_interval"],
                "normal_width": stored["normal_width"],
                "K486_normal_power": exponent,
                "exact_normal_power_mass": q(mass),
                "K410_peano_coefficient": q(peano_coefficient),
                "integrated_abs_upper": upper(contribution),
            })
        rows.append({
            "program_id": face["program_id"],
            "axis": face["axis"],
            "face_kind": face["face_kind"],
            "zeroed_axes": face["zeroed_axes"],
            "codimension": codimension,
            "active_peano_axis_zeroed": active,
            "maximum_second_singular_power": singular_power,
            "K486_normal_power": exponent,
            "cells": cell_rows,
            "complete_selected_equal_normal_strip_abs_upper": upper(face_total),
        })
        by_axis[face["axis"]].append(face_total)
        active_count += int(active)

    axis_order = [f"s{index}" for index in range(1, 12)] + [f"v{index}" for index in range(1, 12)]
    summaries = []
    for axis in axis_order:
        values = by_axis.get(axis, [])
        summaries.append({
            "axis": axis,
            "selected_face_count": len(values),
            "selected_face_equal_normal_strip_abs_upper": upper(values[0]) if values else None,
            "selected_row_is_not_a_hybrid_integral": True,
        })

    width = sum((right - left for left, right in intervals), Fraction())
    return {
        "schema_version": "1.0",
        "result_id": "K509-ORDER-TEN-SELECTED-NORMAL-STRIP-INTEGRATION",
        "created": "2026-09-25",
        "classification": "INTERNAL_NUMERICAL_CONTROL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifest": "lab/process/k508-order-ten-selected-face-cell-bank.json",
            "K508_complete_selected_bank_sha256": k508["bank_summary"]["complete_selected_bank_sha256"],
            "selected_reachable_face_programs": len(rows),
            "cells_per_selected_face": len(intervals),
            "integrated_selected_face_cells": len(rows) * len(intervals),
            "normal_strip": [q(intervals[0][0]), q(intervals[-1][1])],
            "exact_partition_width": q(width),
            "active_peano_face_count": active_count,
            "arb_decimal_digits": 180,
            "threads": 1,
        },
        "integration_contract": {
            "K508_scaled_second_upper_used": True,
            "K486_face_normal_jacobian_power_used": True,
            "K410_quadratic_peano_factor_used": True,
            "active_zeroed_axis_factor_is_rho_squared_over_2c_squared": True,
            "nonzeroed_active_axis_factor_is_1_over_2_times_256_squared": True,
            "seven_cells_pairwise_disjoint_up_to_boundaries": True,
            "seven_cells_exactly_partition_declared_strip": True,
            "unit_projective_angular_density_only": True,
            "selected_equal_normal_strip_is_not_full_projective_normal_cone": True,
            "selected_face_rows_are_not_complete_hybrid_integrals": True,
        },
        "selected_face_strip_bank": rows,
        "hybrid_summary": summaries,
        "strip_summary": {
            "all_20_selected_face_strips_integrated": len(rows) == 20,
            "all_140_cell_contributions_finite_positive": all(math.isfinite(float(cell["integrated_abs_upper"])) and float(cell["integrated_abs_upper"]) > 0 for row in rows for cell in row["cells"]),
            "minimum_selected_K486_normal_power": min(row["K486_normal_power"] for row in rows),
            "selected_hybrids_with_reachable_faces": sum(row["selected_face_count"] > 0 for row in summaries),
            "selected_hybrids_without_reachable_faces": [row["axis"] for row in summaries if row["selected_face_count"] == 0],
            "complete_selected_strip_bank_sha256": digest(rows),
        },
        "decision": {
            "all_selected_equal_normal_near_face_strips_integrated": True,
            "remaining_916_faces_integrated": False,
            "full_projective_normal_cone_complete": False,
            "recursive_positive_interior_cover_complete": False,
            "analytic_radial_tails_complete": False,
            "complete_hybrid_integrals_emitted": False,
            "next_exact_input": "Execute the remaining all-face bank under a measured resource plan, then construct the normal-projective partition and join it to recursive positive-interior cells and analytic tails.",
        },
        "release_test": {
            "exactly_20_selected_face_strip_rows_present": len(rows) == 20,
            "exactly_140_integrated_cells_present": sum(len(row["cells"]) for row in rows) == 140,
            "declared_strip_exactly_partitioned": width == Fraction(3, 4096),
            "all_contributions_finite_positive": all(math.isfinite(float(cell["integrated_abs_upper"])) and float(cell["integrated_abs_upper"]) > 0 for row in rows for cell in row["cells"]),
            "all_selected_normal_powers_integrable": min(row["K486_normal_power"] for row in rows) >= 0,
            "exactly_20_hybrids_have_selected_reachable_faces": sum(row["selected_face_count"] > 0 for row in summaries) == 20,
            "v10_v11_have_no_invented_faces": [row["axis"] for row in summaries if row["selected_face_count"] == 0] == ["v10", "v11"],
            "all_face_cover_not_overclaimed": True,
            "full_normal_cone_not_overclaimed": True,
            "complete_order_ten_remainder_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k508["ledger_effect"],
        "source_routing": k508["source_routing"],
        "claim_ceiling": "Exact outward integration of K508's seven-cell equal-normal chart on rho in [1/4096,1/1024] for the twenty K487 selected reachable-face programs. Each contribution uses K486's face-normal power and K410's quadratic Peano coefficient. This is selected-program backend evidence only: 916 reachable faces, the normal-projective cover, origin rho<1/4096, positive interior, analytic tails, complete order-ten remainder/integral, K457 value, K152 interval, source/ledger move, canon, paper, public and physical posture remain open.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["selected_reachable_face_programs"], fixed["cells_per_selected_face"], fixed["integrated_selected_face_cells"], fixed["exact_partition_width"]) != (20, 7, 140, "3/4096"):
        raise AssertionError("K509 fixed census changed")
    rows = payload["selected_face_strip_bank"]
    if len(rows) != 20 or any(len(row["cells"]) != 7 or row["K486_normal_power"] < 0 for row in rows):
        raise AssertionError("K509 selected strip bank changed")
    if not payload["decision"]["all_selected_equal_normal_near_face_strips_integrated"] or payload["decision"]["remaining_916_faces_integrated"]:
        raise AssertionError("K509 selected/all-face boundary changed")
    if any(payload["decision"][key] for key in ("full_projective_normal_cone_complete", "recursive_positive_interior_cover_complete", "analytic_radial_tails_complete", "complete_hybrid_integrals_emitted")):
        raise AssertionError("K509 overclaimed whole-domain closure")
    if not all(payload["release_test"].values()):
        raise AssertionError("K509 release test failed")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    payload = build()
    validate_payload(payload)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.write:
        OUTPUT.write_text(rendered)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
