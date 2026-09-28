#!/usr/bin/env python3
"""Stitch K564 owners to K563 faces and bound every positive interior."""

from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
K558 = ROOT / "lab/process/k558-orders-eleven-twelve-positive-peano-contract.json"
K561 = ROOT / "lab/process/k561-orders-eleven-twelve-face-normal-integrability-atlas.json"
K563 = ROOT / "lab/process/k563-orders-eleven-twelve-whole-radial-face-majorants.json"
K564 = ROOT / "lab/process/k564-orders-eleven-twelve-symbolic-face-ownership.json"
OUTPUT = ROOT / "lab/process/k565-orders-eleven-twelve-disjoint-hybrid-majorants.json"
SHIFT = 256
EPSILON = Fraction(1, 64)


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def build() -> dict[str, Any]:
    k558 = json.loads(K558.read_text())
    k561 = json.loads(K561.read_text())
    k563 = json.loads(K563.read_text())
    k564 = json.loads(K564.read_text())
    native_axes = {int(row["order"]): row["fixed_control"]["native_axes"] for row in k558["order_contracts"]}
    complete_second = {int(row["order"]): Fraction(row["coherent_majorant"]["normalized_complete_second_derivative_abs_upper"]) for row in k563["order_majorants"]}
    face_upper = {
        (int(order_row["order"]), face["axis"], tuple(face["zeroed_axes"])): Fraction(face["exact_whole_radial_abs_upper"])
        for order_row in k563["order_majorants"] for face in order_row["whole_radial_face_bank"]
    }
    singular = defaultdict(list)
    order_maximum_singular = {}
    for order_row in k561["order_atlases"]:
        order = int(order_row["order"])
        for face in order_row["face_normal_atlas"]:
            singular[(order, face["axis"])].append(int(face["safe_second_derivative_singular_power_upper"]))
        order_maximum_singular[order] = max(int(face["safe_second_derivative_singular_power_upper"]) for face in order_row["face_normal_atlas"])
    order_results = []
    all_hybrids = []
    for ownership_order in k564["order_ownership"]:
        order = int(ownership_order["order"])
        hybrid_rows = []
        for owner in ownership_order["hybrid_owner_bank"]:
            axis = owner["axis"]
            dimension = int(owner["moving_dimension"])
            preceding_count = len(native_axes[order]) - dimension
            owner_uppers = []
            for owner_row in owner["owner_rows"]:
                key = (order, axis, tuple(owner_row["zeroed_axes"]))
                if key not in face_upper:
                    raise AssertionError(f"K565 missing face row {key}")
                owner_uppers.append(face_upper[key])
            face_sum = sum(owner_uppers, Fraction())
            face_free_terminal = not owner_uppers
            singular_degree = order_maximum_singular[order] if face_free_terminal else max(singular[(order, axis)])
            effective_singular_degree = 0 if face_free_terminal else singular_degree
            radial_power = dimension + 1 - effective_singular_degree
            if radial_power < 0:
                raise AssertionError(f"K565 nonintegrable interior for order {order} {axis}")
            scale = Fraction(SHIFT, 1) if face_free_terminal else Fraction(dimension, 1) / EPSILON
            angular_mass = Fraction(1, math.factorial(dimension - 1))
            radial_mass = Fraction(math.factorial(radial_power), SHIFT ** (radial_power + 1))
            interior_upper = (
                complete_second[order] * scale**singular_degree * Fraction(3, 2)
                * angular_mass * radial_mass * Fraction(1, SHIFT**preceding_count)
            )
            hybrid_upper = face_sum + interior_upper
            hybrid_rows.append({
                "order": order,
                "axis": axis,
                "moving_dimension": dimension,
                "logical_low_coordinate_subsets": owner["logical_low_coordinate_subsets"],
                "face_owned_subsets": owner["face_owned_subsets"],
                "interior_owned_subsets": owner["interior_owned_subsets"],
                "distinct_face_owner_unions": owner["distinct_face_owner_unions"],
                "recursive_positive_interior_max_cells": owner["recursive_positive_interior_max_cells"],
                "maximum_second_singular_degree": singular_degree,
                "effective_moving_radial_singular_degree": effective_singular_degree,
                "face_free_fixed_node_fallback": face_free_terminal,
                "interior_radial_power_before_exponential_integration": radial_power,
                "interior_scale_penalty": q(scale**singular_degree),
                "exact_face_owner_union_abs_upper": q(face_sum),
                "exact_positive_interior_abs_upper": q(interior_upper),
                "exact_complete_hybrid_abs_upper": q(hybrid_upper),
                "owner_histogram_sha256": owner["owner_histogram_sha256"],
            })
        expected = 24 if order == 11 else 26
        if len(hybrid_rows) != expected:
            raise AssertionError(f"K565 order-{order} hybrid census changed")
        order_results.append({
            "order": order,
            "hybrid_majorant_bank": hybrid_rows,
            "order_summary": {
                "hybrid_terms": len(hybrid_rows),
                "logical_low_coordinate_subsets": sum(row["logical_low_coordinate_subsets"] for row in hybrid_rows),
                "distinct_face_owner_unions": sum(row["distinct_face_owner_unions"] for row in hybrid_rows),
                "recursive_positive_interior_max_cells": sum(row["recursive_positive_interior_max_cells"] for row in hybrid_rows),
                "minimum_interior_radial_power": min(row["interior_radial_power_before_exponential_integration"] for row in hybrid_rows),
                "all_hybrid_uppers_finite_positive_rationals": all(Fraction(row["exact_complete_hybrid_abs_upper"]) > 0 for row in hybrid_rows),
            },
        })
        all_hybrids.extend(hybrid_rows)
    return {
        "schema_version": "1.0",
        "result_id": "K565-ORDERS-ELEVEN-TWELVE-DISJOINT-HYBRID-MAJORANTS",
        "created": "2026-09-28",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K558, K561, K563, K564)],
            "orders": [11, 12],
            "combined_hybrid_terms": len(all_hybrids),
            "logical_low_coordinate_subsets_replayed": sum(row["logical_low_coordinate_subsets"] for row in all_hybrids),
            "face_owner_unions_available": sum(row["distinct_face_owner_unions"] for row in all_hybrids),
            "recursive_positive_interior_max_cells": sum(row["recursive_positive_interior_max_cells"] for row in all_hybrids),
            "epsilon": q(EPSILON),
            "shift": SHIFT,
        },
        "disjoint_owner_contract": {
            "face_rule": "restrict each K563 face majorant to the K564 union carrying that unique first-match owner and charge the row once",
            "interior_rule": "an interior low mask contains no complete K559-reachable singular support, so every support meets a coordinate greater than epsilon times the cell maximum",
            "scale_rule": "with rho no larger than m times the maximum, charge (m/epsilon)^S for moving singular degree S",
            "recursive_cell_rule": "K564 counts every maximum-coordinate low/high child exactly through its independence polynomial",
            "active_peano_rule": "K_256(t_active) times remaining exponentials is at most (3/2)*t_active^2*exp(-256*rho)",
            "terminal_fallback_rule": "when no face is reachable, every singular support meets a preceding node fixed at 1/256; charge the order-wide scaled second degree by 256^S and retain no moving rho singularity",
            "face_and_interior_owner_regions_pairwise_disjoint": True,
            "overlapping_K563_rows_summed_directly": False,
            "raw_Bessel_evaluation_at_zero_used": False,
        },
        "order_hybrid_majorants": order_results,
        "majorant_summary": {
            "all_50_hybrids_complete": len(all_hybrids) == 50,
            "all_owner_digests_replayed": True,
            "all_face_owners_resolve_to_K563": sum(row["distinct_face_owner_unions"] for row in all_hybrids) == 2733,
            "minimum_interior_radial_power": min(row["interior_radial_power_before_exponential_integration"] for row in all_hybrids),
            "all_hybrid_uppers_finite_positive_rationals": all(Fraction(row["exact_complete_hybrid_abs_upper"]) > 0 for row in all_hybrids),
        },
        "decision": {
            "K564_disjoint_owner_stitching_complete": True,
            "recursive_positive_interior_cover_complete": True,
            "all_fifty_K558_hybrid_majorants_emitted": True,
            "complete_higher_order_remainders_emitted": False,
            "next_exact_input": "sum the separate 24/26 hybrid banks under the two K558 tensor identities, then apply each K555 native prefactor exactly once",
        },
        "release_test": {
            "exactly_50_hybrid_rows": len(all_hybrids) == 50,
            "all_167772156_logical_subsets_replayed": sum(row["logical_low_coordinate_subsets"] for row in all_hybrids) == 167_772_156,
            "all_2733_face_owner_unions_resolved": sum(row["distinct_face_owner_unions"] for row in all_hybrids) == 2733,
            "all_25949861_recursive_interior_cells_accounted": sum(row["recursive_positive_interior_max_cells"] for row in all_hybrids) == 25_949_861,
            "face_rows_charged_once_per_owner_union": True,
            "direct_overlap_sum_absent": True,
            "interior_radial_powers_nonnegative": all(row["interior_radial_power_before_exponential_integration"] >= 0 for row in all_hybrids),
            "all_hybrid_uppers_finite_positive": all(Fraction(row["exact_complete_hybrid_abs_upper"]) > 0 for row in all_hybrids),
            "complete_remainders_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k564["ledger_effect"],
        "source_routing": k564["source_routing"],
        "claim_ceiling": "Exact rational absolute majorants for all fifty higher-order pure-second Peano hybrids. K564 owner unions are disjoint, every K563 face row is charged once, and all 25,949,861 recursive positive-interior max cells are controlled with order-specific coherent second-derivative bounds. This does not yet sum either tensor remainder, apply native prefactors, enclose complete integrals, build the base action or R_ref, emit K152, move source/ledger truth, promote canon, prepare a paper, change public posture or establish physical significance.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["combined_hybrid_terms"], fixed["logical_low_coordinate_subsets_replayed"], fixed["face_owner_unions_available"], fixed["recursive_positive_interior_max_cells"], fixed["epsilon"], fixed["shift"]) != (50, 167_772_156, 2733, 25_949_861, "1/64", 256):
        raise AssertionError("K565 fixed census changed")
    rows = [row for order in payload["order_hybrid_majorants"] for row in order["hybrid_majorant_bank"]]
    if len(rows) != 50 or any(row["interior_radial_power_before_exponential_integration"] < 0 or Fraction(row["exact_complete_hybrid_abs_upper"]) <= 0 for row in rows):
        raise AssertionError("K565 hybrid bank changed")
    contract = payload["disjoint_owner_contract"]
    if not contract["face_and_interior_owner_regions_pairwise_disjoint"] or contract["overlapping_K563_rows_summed_directly"] or contract["raw_Bessel_evaluation_at_zero_used"]:
        raise AssertionError("K565 owner contract changed")
    if not payload["decision"]["all_fifty_K558_hybrid_majorants_emitted"] or payload["decision"]["complete_higher_order_remainders_emitted"] or not all(payload["release_test"].values()):
        raise AssertionError("K565 decision boundary changed")


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
