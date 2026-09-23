#!/usr/bin/env python3
"""Compose global determinant primitives into finite whole-radial face rows."""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
K348 = ROOT / "lab/process/k348-order-eight-positive-peano-contract.json"
K352 = ROOT / "lab/process/k352-order-eight-mask-native-preconditioner-compiler.json"
K353 = ROOT / "lab/process/k353-order-eight-face-normal-integrability-atlas.json"
K354 = ROOT / "lab/process/k354-order-eight-face-program-compiler.json"
K363 = ROOT / "lab/process/k363-order-eight-global-face-neighborhood-ownership.json"
K366 = ROOT / "lab/process/k366-order-eight-bivariate-determinant-newton-fronts.json"
K368 = ROOT / "lab/process/k368-order-eight-global-scaled-bessel-envelope.json"
K367_PRODUCER = HERE / "k367_order_eight_zero_inclusive_determinant_envelope.py"
K352_PRODUCER = HERE / "k352_order_eight_mask_native_preconditioner_compiler.py"
OUTPUT = ROOT / "lab/process/k369-order-eight-whole-radial-face-majorants.json"
SHIFT = 256


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K367_BACKEND = load_module(K367_PRODUCER, "k367_for_k369")
K352_BACKEND = load_module(K352_PRODUCER, "k352_for_k369")


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def multiply_taylor(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    result = [Fraction(), Fraction(), Fraction()]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= 2:
                result[i + j] += a * b
    return result


def build() -> dict[str, Any]:
    k348 = json.loads(K348.read_text())
    k352 = json.loads(K352.read_text())
    k353 = json.loads(K353.read_text())
    k354 = json.loads(K354.read_text())
    k363 = json.loads(K363.read_text())
    k366 = json.loads(K366.read_text())
    k368 = json.loads(K368.read_text())
    primitive = [Fraction(row["global_scaled_upper"]) for row in k368["global_scaled_bessel_bank"]["rows"]]
    determinant_rows = K367_BACKEND.compile_envelopes(primitive, k352, k366)
    determinant_maxima: dict[int, list[Fraction]] = {}
    for rank in range(1, 5):
        determinant_maxima[rank] = [
            max(
                Fraction(env["exact_rational_abs_upper"])
                for row in determinant_rows if row["rank"] == rank
                for env in row["derivative_envelopes"] if env["derivative_order"] == order
            )
            for order in range(3)
        ]
    transition_constant = max(Fraction(env["exact_rational_abs_upper"]) for row in determinant_rows for env in row["derivative_envelopes"])

    old_taylor = [primitive[order] / math.factorial(order) for order in range(3)]
    descriptors = K352_BACKEND.ordered_descriptors()
    descriptor_rows = []
    complete_taylor = [Fraction(), Fraction(), Fraction()]
    factor_histogram: Counter[int] = Counter()
    rank_pattern_histogram: Counter[str] = Counter()
    for descriptor in descriptors:
        polynomial = [Fraction(1), Fraction(), Fraction()]
        polynomial = multiply_taylor(polynomial, old_taylor)
        polynomial = multiply_taylor(polynomial, old_taylor)
        ranks = []
        for matrix in descriptor["species_matrices"]:
            rank = int(matrix["rank"])
            ranks.append(rank)
            determinant_taylor = [determinant_maxima[rank][order] / math.factorial(order) for order in range(3)]
            polynomial = multiply_taylor(polynomial, determinant_taylor)
        coefficient = abs(int(descriptor["coefficient_product"]))
        polynomial = [coefficient * value for value in polynomial]
        complete_taylor = [left + right for left, right in zip(complete_taylor, polynomial, strict=True)]
        factor_count = 2 + len(ranks)
        factor_histogram[factor_count] += 1
        rank_pattern_histogram[",".join(str(value) for value in sorted(ranks))] += 1
        descriptor_rows.append({
            "group_id": descriptor["group_id"],
            "left": descriptor["left"],
            "right": descriptor["right"],
            "species_ranks": ranks,
            "factor_count": factor_count,
            "normalized_second_abs_upper": q(2 * polynomial[2]),
        })
    complete_second = 2 * complete_taylor[2]

    k353_map = {
        (row["axis"], tuple(row["zeroed_axes"])): row
        for row in k353["face_normal_atlas"]
    }
    face_rows = []
    axis_histogram: Counter[str] = Counter()
    for program in k354["face_programs"]:
        key = (program["axis"], tuple(program["zeroed_axes"]))
        face = k353_map[key]
        codimension = int(program["codimension"])
        radial_power = int(face["minimum_second_derivative_face_normal_power"])
        moving_dimension = len(program["moving_axes"])
        preceding_count = len(program["preceding_axes_fixed_at_node"])
        active = bool(program["active_peano_axis_zeroed"])
        angular_mass = Fraction(1, math.factorial(codimension - 1))
        radial_mass = Fraction(math.factorial(radial_power), SHIFT ** (radial_power + 1))
        if active:
            peano_factor = Fraction(3, 2)
            exponential_tangential_axes = moving_dimension - codimension
            peano_measure = "K_256(t)*exp(-256*sum_other)<=3*t^2*exp(-256*rho)/2"
        else:
            peano_factor = Fraction(1, 2 * SHIFT**3)
            exponential_tangential_axes = moving_dimension - codimension - 1
            peano_measure = "integral K_256(t)dt=1/(2*256^3)"
        if exponential_tangential_axes < 0:
            raise AssertionError("K369 tangential axis census became negative")
        tangential_mass = Fraction(1, SHIFT**exponential_tangential_axes)
        preceding_weight = Fraction(1, SHIFT**preceding_count)
        transition_depth = codimension - 1
        upper = (
            complete_second
            * transition_constant**transition_depth
            * angular_mass
            * radial_mass
            * peano_factor
            * tangential_mass
            * preceding_weight
        )
        face_rows.append({
            "program_id": program["program_id"],
            "axis": program["axis"],
            "face_kind": program["face_kind"],
            "codimension": codimension,
            "moving_dimension": moving_dimension,
            "preceding_node_axes": preceding_count,
            "active_peano_axis_zeroed": active,
            "K353_radial_power": radial_power,
            "maximum_nested_transition_depth": transition_depth,
            "exact_projective_simplex_mass": q(angular_mass),
            "exact_radial_gamma_mass": q(radial_mass),
            "peano_measure_rule": peano_measure,
            "exponential_tangential_axes": exponential_tangential_axes,
            "exact_whole_radial_abs_upper": q(upper),
        })
        axis_histogram[program["axis"]] += 1

    return {
        "schema_version": "1.0",
        "result_id": "K369-ORDER-EIGHT-WHOLE-RADIAL-FACE-MAJORANTS",
        "created": "2026-09-23",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K348, K352, K353, K354, K363, K366, K368)],
            "global_determinant_envelopes_recomputed": len(determinant_rows),
            "ordered_descriptors": len(descriptors),
            "face_programs": len(face_rows),
            "hybrid_axes": len(axis_histogram),
            "maximum_nested_transition_depth": max(row["maximum_nested_transition_depth"] for row in face_rows),
            "shift": SHIFT,
        },
        "complete_coherent_majorant": {
            "old_kernel_taylor_uppers": [q(value) for value in old_taylor],
            "determinant_derivative_uppers_by_rank": {str(rank): [q(value) for value in values] for rank, values in determinant_maxima.items()},
            "transition_constant": q(transition_constant),
            "factor_count_histogram": {str(key): factor_histogram[key] for key in sorted(factor_histogram)},
            "species_rank_pattern_histogram": dict(sorted(rank_pattern_histogram.items())),
            "normalized_complete_value_first_second_taylor_uppers": [q(value) for value in complete_taylor],
            "normalized_complete_second_derivative_abs_upper": q(complete_second),
            "all_2400_ordered_descriptors_assembled": len(descriptors) == 2400,
            "all_23_coherent_groups_retained_before_final_sum": len({row["group_id"] for row in descriptors}) == 23,
        },
        "descriptor_majorant_bank": descriptor_rows,
        "whole_radial_face_bank": face_rows,
        "whole_radial_contract": {
            "normal_coordinates": "rho=sum of the selected face-normal raw times with exact simplex angular mass 1/(c-1)!",
            "radial_rule": "K353 supplies rho^p with p>=0; combined Laguerre/Peano weight supplies exp(-256*rho), so the exact mass is p!/256^(p+1)",
            "active_peano_rule": "for t<=1/256 use K_256(t)<=t^2/2 and exp(256t)<3; for t>=1/256 use K_256(t)=exp(-256t)/256^2<=t^2 exp(-256t)",
            "inactive_peano_rule": "integrate the exact K348 kernel mass 1/(2*256^3)",
            "nested_transition_rule": "apply the worst exact K367/K368 rank-compatible transition constant at most c-1 times; this is deliberately coarse but finite",
            "every_face_row_is_finite": True,
            "face_rows_overlap_and_must_not_be_summed_as_hybrid_integrals": True,
            "K363_disjoint_owner_stitching_still_required": True,
        },
        "majorant_summary": {
            "face_program_histogram_by_axis": dict(axis_histogram),
            "minimum_radial_power": min(row["K353_radial_power"] for row in face_rows),
            "maximum_radial_power": max(row["K353_radial_power"] for row in face_rows),
            "all_face_rows_finite_positive_rationals": all(Fraction(row["exact_whole_radial_abs_upper"]) > 0 for row in face_rows),
            "v8_v9_have_no_face_rows": axis_histogram["v8"] == 0 and axis_histogram["v9"] == 0,
        },
        "decision": {
            "whole_radial_majorant_emitted_for_every_K353_face_program": True,
            "compact_and_analytic_tail_primitives_composed": True,
            "uniform_face_program_integrand_majorants_complete": True,
            "K363_disjoint_recursive_owner_cover_complete": False,
            "complete_hybrid_integrals_emitted": False,
            "complete_order_eight_remainder_emitted": False,
            "next_exact_input": "stitch these finite face rows to K363's unique owners and a recursive positive-interior cell cover without double counting, then sum each of the eighteen K348 hybrids",
        },
        "release_test": {
            "all_global_determinant_envelopes_recomputed": len(determinant_rows) > 0,
            "all_2400_ordered_descriptors_assembled": len(descriptors) == 2400,
            "exactly_23_coherent_groups_retained": len({row["group_id"] for row in descriptors}) == 23,
            "exactly_517_face_programs_majorized": len(face_rows) == 517,
            "all_K353_radial_powers_nonnegative": all(row["K353_radial_power"] >= 0 for row in face_rows),
            "maximum_transition_depth_is_17": max(row["maximum_nested_transition_depth"] for row in face_rows) == 17,
            "all_face_rows_finite_positive": all(Fraction(row["exact_whole_radial_abs_upper"]) > 0 for row in face_rows),
            "overlapping_face_rows_not_summed": True,
            "recursive_owner_cover_not_overclaimed": True,
            "complete_order_eight_remainder_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k368["ledger_effect"],
        "source_routing": k368["source_routing"],
        "claim_ceiling": "Exact rational finite whole-radial absolute majorants for all 517 K353 face programs, obtained by recomputing every K367 determinant envelope with K368's global primitive bounds, retaining all 2,400 ordered descriptors and 23 coherent groups, and integrating K353's nonnegative normal powers under the exact K348 Laguerre/Peano measures. The rows deliberately overlap and are not summed into hybrids; K363 disjoint owner stitching, recursive positive-interior cells, all eighteen complete K348 hybrid integrals, the order-eight remainder/integral, action column, R_ref, K152, source/ledger move, canon, paper, public and physical posture remain open.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["ordered_descriptors"], fixed["face_programs"], fixed["hybrid_axes"], fixed["maximum_nested_transition_depth"], fixed["shift"]) != (2400, 517, 16, 17, 256):
        raise AssertionError("K369 fixed census changed")
    coherent = payload["complete_coherent_majorant"]
    if not coherent["all_2400_ordered_descriptors_assembled"] or not coherent["all_23_coherent_groups_retained_before_final_sum"]:
        raise AssertionError("K369 coherent assembly changed")
    rows = payload["whole_radial_face_bank"]
    if len(rows) != 517 or any(row["K353_radial_power"] < 0 or Fraction(row["exact_whole_radial_abs_upper"]) <= 0 for row in rows):
        raise AssertionError("K369 face bank changed")
    contract = payload["whole_radial_contract"]
    if not contract["every_face_row_is_finite"] or not contract["face_rows_overlap_and_must_not_be_summed_as_hybrid_integrals"] or not contract["K363_disjoint_owner_stitching_still_required"]:
        raise AssertionError("K369 overlap boundary changed")
    decision = payload["decision"]
    if not decision["whole_radial_majorant_emitted_for_every_K353_face_program"] or decision["K363_disjoint_recursive_owner_cover_complete"] or decision["complete_hybrid_integrals_emitted"] or decision["complete_order_eight_remainder_emitted"]:
        raise AssertionError("K369 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K369 release test failed")


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
