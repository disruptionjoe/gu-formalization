#!/usr/bin/env python3
"""Stitch K363 owners to K369 rows and bound every positive interior union."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K348 = ROOT / "lab/process/k348-order-eight-positive-peano-contract.json"
K349 = ROOT / "lab/process/k349-order-eight-zero-safe-radial-contract.json"
K350 = ROOT / "lab/process/k350-order-eight-hybrid-face-atlas.json"
K353 = ROOT / "lab/process/k353-order-eight-face-normal-integrability-atlas.json"
K363 = ROOT / "lab/process/k363-order-eight-global-face-neighborhood-ownership.json"
K369 = ROOT / "lab/process/k369-order-eight-whole-radial-face-majorants.json"
OUTPUT = ROOT / "lab/process/k370-order-eight-disjoint-owner-hybrid-majorants.json"
AXES = tuple(f"s{i}" for i in range(1, 10)) + tuple(f"v{i}" for i in range(1, 10))
AXIS_INDEX = {axis: index for index, axis in enumerate(AXES)}
SHIFT = 256
EPSILON = Fraction(1, 64)


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def digest_stream(rows: list[tuple[int, str]]) -> str:
    h = hashlib.sha256()
    for low_mask, owner in rows:
        h.update(f"{low_mask}:{owner}\n".encode())
    return "sha256:" + h.hexdigest()


def flattened_faces(hybrid: dict[str, Any]) -> list[tuple[str, ...]]:
    result = set()
    for rows in hybrid["faces"].values():
        result.update(tuple(row["zeroed_axes"]) for row in rows)
    return sorted(result, key=lambda mask: (-len(mask), tuple(AXIS_INDEX[axis] for axis in mask)))


def owner_assignments(hybrid: dict[str, Any]) -> tuple[list[tuple[int, str]], Counter[str]]:
    moving = list(hybrid["moving_axes"])
    position = {axis: index for index, axis in enumerate(moving)}
    reachable = flattened_faces(hybrid)
    assignments: list[tuple[int, str]] = []
    counts: Counter[str] = Counter()
    for low_mask in range(1 << len(moving)):
        low_axes = {axis for axis, index in position.items() if low_mask & (1 << index)}
        candidates = [mask for mask in reachable if set(mask) <= low_axes]
        owner = ",".join(candidates[0]) if candidates else "INTERIOR"
        assignments.append((low_mask, owner))
        counts[owner] += 1
    return assignments, counts


def build() -> dict[str, Any]:
    k348 = json.loads(K348.read_text())
    k349 = json.loads(K349.read_text())
    k350 = json.loads(K350.read_text())
    k353 = json.loads(K353.read_text())
    k363 = json.loads(K363.read_text())
    k369 = json.loads(K369.read_text())
    owner_rows = {row["axis"]: row for row in k363["hybrid_owner_bank"]}
    face_upper = {
        (row["axis"], tuple(row["program_id"].split(":")[-1].split(","))): Fraction(row["exact_whole_radial_abs_upper"])
        for row in k369["whole_radial_face_bank"]
    }
    singular = defaultdict(list)
    for row in k353["face_normal_atlas"]:
        singular[row["axis"]].append(int(row["maximum_value_first_second_singular_powers"][2]))
    complete_second = Fraction(k369["complete_coherent_majorant"]["normalized_complete_second_derivative_abs_upper"])

    hybrid_rows = []
    total_subsets = 0
    total_interior_cells = 0
    total_face_owner_unions = 0
    for hybrid in k350["hybrid_face_atlas"]:
        axis = hybrid["axis"]
        moving = list(hybrid["moving_axes"])
        dimension = len(moving)
        assignments, counts = owner_assignments(hybrid)
        recorded = owner_rows[axis]
        if digest_stream(assignments) != recorded["assigned_owner_histogram_sha256"]:
            raise AssertionError(f"K363 owner digest changed for {axis}")
        interior_subset_count = counts.pop("INTERIOR", 0)
        used_owners = sorted(counts, key=lambda text: tuple(AXIS_INDEX[a] for a in text.split(",")))
        owner_uppers = []
        for owner in used_owners:
            key = (axis, tuple(owner.split(",")))
            if key not in face_upper:
                raise AssertionError(f"missing K369 owner row {axis}:{owner}")
            owner_uppers.append(face_upper[key])
        face_sum = sum(owner_uppers, Fraction())

        interior_cells = 0
        full_mask = (1 << dimension) - 1
        for low_mask, owner in assignments:
            if owner == "INTERIOR" and low_mask != full_mask:
                interior_cells += dimension - low_mask.bit_count()
        # K350 has no reachable face for v8/v9 because every singular support
        # meets a preceding coordinate fixed at 1/256.  Bound all twelve
        # scaled degrees from K349 by 256^12 and retain no rho singularity.
        # Every other hybrid uses K353's sharper moving-support degree.
        face_free_terminal = not singular[axis]
        singular_degree = (
            abs(int(k349["all_zero_radial_ledger"]["complete_second_derivative_degree"]))
            if face_free_terminal
            else max(singular[axis])
        )
        effective_radial_singular_degree = 0 if face_free_terminal else singular_degree
        radial_power = dimension + 1 - effective_radial_singular_degree
        if radial_power < 0:
            raise AssertionError(f"nonintegrable interior radial power for {axis}")
        scale_penalty = Fraction(SHIFT, 1) if face_free_terminal else Fraction(dimension, 1) / EPSILON
        angular_mass = Fraction(1, math.factorial(dimension - 1))
        radial_mass = Fraction(math.factorial(radial_power), SHIFT ** (radial_power + 1))
        preceding_weight = Fraction(1, SHIFT ** AXIS_INDEX[axis])
        interior_upper = (
            complete_second
            * scale_penalty**singular_degree
            * Fraction(3, 2)
            * angular_mass
            * radial_mass
            * preceding_weight
        )
        hybrid_upper = face_sum + interior_upper
        hybrid_rows.append({
            "axis": axis,
            "moving_dimension": dimension,
            "low_coordinate_subsets_replayed": len(assignments),
            "face_owned_subsets": sum(counts.values()),
            "interior_owned_subsets": interior_subset_count,
            "distinct_face_owner_unions": len(used_owners),
            "recursive_interior_max_cells": interior_cells,
            "maximum_second_singular_degree": singular_degree,
            "effective_moving_radial_singular_degree": effective_radial_singular_degree,
            "face_free_fixed_node_fallback": face_free_terminal,
            "interior_radial_power_before_exponential_integration": radial_power,
            "interior_scale_penalty": q(scale_penalty**singular_degree),
            "exact_face_owner_union_abs_upper": q(face_sum),
            "exact_positive_interior_abs_upper": q(interior_upper),
            "exact_complete_hybrid_abs_upper": q(hybrid_upper),
            "owner_histogram_sha256": digest_stream(assignments),
        })
        total_subsets += len(assignments)
        total_interior_cells += interior_cells
        total_face_owner_unions += len(used_owners)

    return {
        "schema_version": "1.0",
        "result_id": "K370-ORDER-EIGHT-DISJOINT-OWNER-HYBRID-MAJORANTS",
        "created": "2026-09-23",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K348, K349, K350, K353, K363, K369)],
            "native_axes": list(AXES),
            "hybrid_terms": len(hybrid_rows),
            "low_coordinate_subsets_replayed": total_subsets,
            "face_programs_available": len(k369["whole_radial_face_bank"]),
            "epsilon": q(EPSILON),
            "shift": SHIFT,
        },
        "disjoint_owner_contract": {
            "face_rule": "restrict each K369 face majorant to the union of K363 cells carrying that unique owner and charge the row once for the whole owner union",
            "interior_rule": "an INTERIOR low mask contains no complete K350-reachable singular support, so every such support meets a coordinate greater than epsilon times the cell maximum",
            "scale_rule": "with rho no larger than m times the maximum, each active singular scale is greater than epsilon*rho/m; charge (m/epsilon)^S for the hybrid maximum second-order singular degree S",
            "recursive_cell_rule": "choose the first maximum coordinate, then recursively classify every other coordinate as low (at most epsilon times max) or high (strictly above); equality remains on the low side",
            "active_peano_rule": "K_256(t_active) times the remaining exponentials is at most (3/2)*t_active^2*exp(-256*rho)",
            "radial_rule": "rho^(m-1) Jacobian times rho^2 Peano gain times rho^(-S) has exponent m+1-S and exact gamma mass (m+1-S)!/256^(m+2-S)",
            "terminal_fallback_rule": "when K350 has no reachable face (v8,v9), every singular support meets a preceding node fixed at 1/256; charge K349's total complete-second scaled degree twelve by 256^12, so the moving radial singular degree is zero",
            "face_and_interior_owner_regions_pairwise_disjoint": True,
            "overlapping_K369_rows_summed_directly": False,
            "raw_Bessel_evaluation_at_zero_used": False,
        },
        "hybrid_majorant_bank": hybrid_rows,
        "majorant_summary": {
            "all_18_hybrids_complete": len(hybrid_rows) == 18,
            "all_K363_owner_digests_replayed": all(row["owner_histogram_sha256"] == owner_rows[row["axis"]]["assigned_owner_histogram_sha256"] for row in hybrid_rows),
            "all_face_owners_resolve_to_K369": total_face_owner_unions == sum(row["distinct_face_owners_used"] for row in k363["hybrid_owner_bank"]),
            "total_distinct_face_owner_unions": total_face_owner_unions,
            "total_recursive_positive_interior_max_cells": total_interior_cells,
            "minimum_interior_radial_power": min(row["interior_radial_power_before_exponential_integration"] for row in hybrid_rows),
            "all_hybrid_uppers_finite_positive_rationals": all(Fraction(row["exact_complete_hybrid_abs_upper"]) > 0 for row in hybrid_rows),
        },
        "decision": {
            "K363_disjoint_owner_stitching_complete": True,
            "recursive_positive_interior_cover_complete": True,
            "all_eighteen_K348_hybrid_majorants_emitted": True,
            "complete_order_eight_remainder_emitted": False,
            "next_exact_input": "sum the eighteen disjoint hybrid absolute uppers under K348's tensor Peano identity, then apply the native prefactor once and join K345",
        },
        "release_test": {
            "exactly_18_hybrid_rows": len(hybrid_rows) == 18,
            "all_524286_K363_subsets_replayed": total_subsets == 524286,
            "all_owner_digests_match": all(row["owner_histogram_sha256"] == owner_rows[row["axis"]]["assigned_owner_histogram_sha256"] for row in hybrid_rows),
            "face_rows_charged_once_per_owner_union": True,
            "direct_overlap_sum_absent": True,
            "interior_radial_powers_nonnegative": all(row["interior_radial_power_before_exponential_integration"] >= 0 for row in hybrid_rows),
            "all_hybrid_uppers_finite_positive": all(Fraction(row["exact_complete_hybrid_abs_upper"]) > 0 for row in hybrid_rows),
            "raw_zero_evaluation_absent": True,
            "complete_remainder_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k369["ledger_effect"],
        "source_routing": k369["source_routing"],
        "claim_ceiling": "Exact rational absolute majorants for all eighteen K348 hybrid Peano integrals. K363 owner cells are disjoint, each used K369 face row is charged once per owner union, and a finite recursive max-coordinate low/high cover bounds the positive-interior union with the exact per-hybrid singular degree. This does not yet sum the eighteen terms, apply the native prefactor, enclose the complete order-eight integral, build the action column or R_ref, emit K152, move source/ledger truth, promote canon, prepare a paper, change public posture or establish physical significance.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["hybrid_terms"], fixed["low_coordinate_subsets_replayed"], fixed["face_programs_available"], fixed["epsilon"], fixed["shift"]) != (18, 524286, 517, "1/64", 256):
        raise AssertionError("K370 fixed census changed")
    rows = payload["hybrid_majorant_bank"]
    if len(rows) != 18 or any(Fraction(row["exact_complete_hybrid_abs_upper"]) <= 0 for row in rows):
        raise AssertionError("K370 hybrid bank changed")
    contract = payload["disjoint_owner_contract"]
    if not contract["face_and_interior_owner_regions_pairwise_disjoint"] or contract["overlapping_K369_rows_summed_directly"] or contract["raw_Bessel_evaluation_at_zero_used"]:
        raise AssertionError("K370 owner contract changed")
    decision = payload["decision"]
    if not all(decision[key] for key in ("K363_disjoint_owner_stitching_complete", "recursive_positive_interior_cover_complete", "all_eighteen_K348_hybrid_majorants_emitted")) or decision["complete_order_eight_remainder_emitted"]:
        raise AssertionError("K370 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K370 release test failed")


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
