#!/usr/bin/env python3
"""Integrate K356's canonical equal-normal cells with K353 powers.

This is a one-dimensional radial control on each equal-allocation normal chart.
It uses unit projective angular density and therefore does not cover a full
codimension-c normal cone.  Face rows overlap and are never summed into a
hybrid Peano integral.
"""

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
K356 = ROOT / "lab/process/k356-order-eight-preconditioned-face-cell-bank.json"
OUTPUT = ROOT / "lab/process/k357-order-eight-near-face-strip-integration.json"

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
        raise AssertionError("nonintegrable K357 normal power")
    return (right ** (exponent + 1) - left ** (exponent + 1)) / (exponent + 1)


def build() -> dict[str, Any]:
    k356 = json.loads(K356.read_text())
    if not k356["decision"]["K352_preconditioned_positive_width_face_cells_released"]:
        raise AssertionError("K356 face cells unavailable")
    expected_cells = [[Fraction(a), Fraction(b)] for a, b in k356["fixed_control"]["normal_cells"]]
    if expected_cells[0][0] != Fraction(1, 4096) or expected_cells[-1][1] != Fraction(1, 1024):
        raise AssertionError("K356 near-face strip changed")
    for left_row, right_row in zip(expected_cells, expected_cells[1:], strict=False):
        if left_row[1] != right_row[0]:
            raise AssertionError("K356 normal cells do not form a contiguous partition")

    rows = []
    by_axis: dict[str, list[arb]] = defaultdict(list)
    active_count = 0
    for face in k356["face_cell_bank"]:
        codimension = int(face["codimension"])
        singular_power = int(face["maximum_second_singular_power"])
        active = bool(face["active_peano_axis_zeroed"])
        exponent = codimension - 1 - singular_power + (2 if active else 0)
        if exponent != int(face["minimum_face_normal_power"]):
            raise AssertionError("K357 failed to replay K353 normal exponent")
        peano_coefficient = Fraction(1, 2 * codimension * codimension) if active else Fraction(1, 2 * 256 * 256)
        cell_rows = []
        face_total = arb(0)
        for stored, (left, right) in zip(face["cells"], expected_cells, strict=True):
            if [Fraction(value) for value in stored["normal_interval"]] != [left, right]:
                raise AssertionError("K356 face cell partition changed")
            normal_mass = power_integral(left, right, exponent)
            scaled_upper = arb(stored["rho_to_K353_second_singular_power_abs_upper"])
            contribution = scaled_upper * arb(q(peano_coefficient * normal_mass))
            if not math.isfinite(float(contribution.upper())) or contribution.upper() <= 0:
                raise AssertionError("K357 non-finite strip contribution")
            face_total += contribution
            cell_rows.append({
                "normal_interval": stored["normal_interval"],
                "normal_width": stored["normal_width"],
                "K353_normal_power": exponent,
                "exact_normal_power_mass": q(normal_mass),
                "K349_peano_coefficient": q(peano_coefficient),
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
            "K353_normal_power": exponent,
            "cells": cell_rows,
            "complete_equal_normal_strip_abs_upper": upper(face_total),
        })
        by_axis[face["axis"]].append(face_total)
        active_count += int(active)

    axis_order = [f"s{index}" for index in range(1, 10)] + [f"v{index}" for index in range(1, 10)]
    axis_summary = []
    for axis in axis_order:
        values = by_axis.get(axis, [])
        axis_summary.append({
            "axis": axis,
            "reachable_face_count": len(values),
            "maximum_single_face_equal_normal_strip_abs_upper": upper(max(values, key=lambda item: item.upper())) if values else None,
            "overlap_counted_sum_diagnostic_abs_upper": upper(sum(values, arb(0))) if values else None,
            "overlap_counted_sum_is_not_a_hybrid_integral": True,
        })

    total_width = sum((right - left for left, right in expected_cells), Fraction(0))
    return {
        "schema_version": "1.0",
        "result_id": "K357-ORDER-EIGHT-NEAR-FACE-STRIP-INTEGRATION",
        "created": "2026-09-23",
        "classification": "INTERNAL_NUMERICAL_CONTROL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifest": "lab/process/k356-order-eight-preconditioned-face-cell-bank.json",
            "K356_complete_bank_sha256": k356["bank_summary"]["complete_bank_sha256"],
            "reachable_face_programs": len(rows),
            "cells_per_face": len(expected_cells),
            "integrated_face_cells": len(rows) * len(expected_cells),
            "normal_strip": [q(expected_cells[0][0]), q(expected_cells[-1][1])],
            "exact_partition_width": q(total_width),
            "active_peano_face_count": active_count,
            "arb_decimal_digits": 180,
            "threads": 1,
        },
        "integration_contract": {
            "K356_scaled_second_upper_used": True,
            "K353_face_normal_jacobian_power_used": True,
            "K349_quadratic_peano_factor_used": True,
            "active_zeroed_axis_factor_is_rho_squared_over_2c_squared": True,
            "nonzeroed_active_axis_factor_is_1_over_2_times_256_squared": True,
            "seven_cells_pairwise_disjoint_up_to_boundaries": True,
            "seven_cells_exactly_partition_declared_strip": True,
            "unit_projective_angular_density_only": True,
            "equal_normal_strip_is_not_full_projective_normal_cone": True,
            "face_rows_overlap_and_are_not_summed_into_hybrid_integrals": True,
        },
        "face_strip_bank": rows,
        "hybrid_summary": axis_summary,
        "strip_summary": {
            "all_517_face_strips_integrated": len(rows) == 517,
            "all_3619_cell_contributions_finite_positive": all(
                math.isfinite(float(cell["integrated_abs_upper"])) and float(cell["integrated_abs_upper"]) > 0
                for row in rows for cell in row["cells"]
            ),
            "global_minimum_K353_normal_power": min(row["K353_normal_power"] for row in rows),
            "hybrids_with_reachable_faces": sum(row["reachable_face_count"] > 0 for row in axis_summary),
            "hybrids_without_reachable_faces": [row["axis"] for row in axis_summary if row["reachable_face_count"] == 0],
            "complete_strip_bank_sha256": digest(rows),
        },
        "decision": {
            "all_equal_normal_near_face_strips_integrated": True,
            "wide_unsplit_cells_rejected_by_K356_quality_control": True,
            "full_projective_normal_cone_complete": False,
            "recursive_positive_interior_cover_complete": False,
            "analytic_radial_tails_complete": False,
            "complete_hybrid_integrals_emitted": False,
            "next_exact_input": "construct an exact normal-projective partition around every codimension-two-through-eighteen face, then join these stable radial cells to recursive positive-interior cells and analytic radial tails",
        },
        "release_test": {
            "exactly_517_face_strip_rows_present": len(rows) == 517,
            "exactly_3619_integrated_cells_present": sum(len(row["cells"]) for row in rows) == 3619,
            "declared_strip_exactly_partitioned": total_width == Fraction(3, 4096),
            "all_contributions_finite_positive": all(
                math.isfinite(float(cell["integrated_abs_upper"])) and float(cell["integrated_abs_upper"]) > 0
                for row in rows for cell in row["cells"]
            ),
            "K353_global_minimum_power_replayed": min(row["K353_normal_power"] for row in rows) == 0,
            "exactly_16_hybrids_have_reachable_faces": sum(row["reachable_face_count"] > 0 for row in axis_summary) == 16,
            "v8_v9_have_no_invented_faces": [row["axis"] for row in axis_summary if row["reachable_face_count"] == 0] == ["v8", "v9"],
            "full_normal_cone_not_overclaimed": True,
            "complete_order_eight_remainder_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k356["ledger_effect"],
        "source_routing": k356["source_routing"],
        "claim_ceiling": "Exact integration of K356's seven-cell canonical equal-normal chart on rho in [1/4096,1/1024] for every one of the 517 reachable faces. Each contribution uses K353's exact face-normal power and K349's appropriate quadratic Peano coefficient; the cells are pairwise disjoint up to boundaries and have exact total width 3/4096. The calculation uses unit projective angular density, and distinct face rows overlap, so neither the face-row sums nor hybrid diagnostics are full normal-cone or K348 hybrid integrals. The missing normal-projective cover, origin rho<1/4096, positive interior, analytic tails, complete order-eight remainder/integral, action column, R_ref, K152 interval, source/ledger move, canon, paper, public and physical posture remain open.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["reachable_face_programs"], fixed["cells_per_face"], fixed["integrated_face_cells"], fixed["exact_partition_width"]) != (517, 7, 3619, "3/4096"):
        raise AssertionError("K357 fixed census changed")
    rows = payload["face_strip_bank"]
    if len(rows) != 517 or any(len(row["cells"]) != 7 or row["K353_normal_power"] < 0 for row in rows):
        raise AssertionError("K357 face-strip bank changed")
    contract = payload["integration_contract"]
    required = (
        "K356_scaled_second_upper_used", "K353_face_normal_jacobian_power_used",
        "K349_quadratic_peano_factor_used", "seven_cells_pairwise_disjoint_up_to_boundaries",
        "seven_cells_exactly_partition_declared_strip", "unit_projective_angular_density_only",
        "equal_normal_strip_is_not_full_projective_normal_cone",
        "face_rows_overlap_and_are_not_summed_into_hybrid_integrals",
    )
    if not all(contract[key] for key in required):
        raise AssertionError("K357 integration contract changed")
    decision = payload["decision"]
    if not decision["all_equal_normal_near_face_strips_integrated"]:
        raise AssertionError("K357 strip release lost")
    if any(decision[key] for key in ("full_projective_normal_cone_complete", "recursive_positive_interior_cover_complete", "analytic_radial_tails_complete", "complete_hybrid_integrals_emitted")):
        raise AssertionError("K357 overclaimed whole-domain closure")
    if not all(payload["release_test"].values()):
        raise AssertionError("K357 release test failed")


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
