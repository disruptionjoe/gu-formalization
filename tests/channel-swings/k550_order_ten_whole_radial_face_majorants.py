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
K409 = ROOT / "lab/process/k409-order-ten-positive-peano-contract.json"
K413 = ROOT / "lab/process/k413-order-ten-mask-native-preconditioner-compiler.json"
K414 = ROOT / "lab/process/k414-order-ten-face-normal-integrability-atlas.json"
K415 = ROOT / "lab/process/k415-order-ten-face-program-compiler.json"
K545 = ROOT / "lab/process/k545-order-ten-global-face-neighborhood-ownership.json"
K547 = ROOT / "lab/process/k547-order-ten-zero-safe-scaled-derivative-bank.json"
K549 = ROOT / "lab/process/k549-order-ten-zero-inclusive-determinant-envelope.json"
K413_PRODUCER = HERE / "k413_order_ten_mask_native_preconditioner_compiler.py"
OUTPUT = ROOT / "lab/process/k550-order-ten-whole-radial-face-majorants.json"
SHIFT = 256


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K413_BACKEND = load_module(K413_PRODUCER, "k413_for_k550")


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
    k409 = json.loads(K409.read_text())
    k413 = json.loads(K413.read_text())
    k414 = json.loads(K414.read_text())
    k415 = json.loads(K415.read_text())
    k545 = json.loads(K545.read_text())
    k547 = json.loads(K547.read_text())
    k549 = json.loads(K549.read_text())
    primitive = [Fraction(row["global_scaled_upper"]) for row in k547["scaled_bessel_contract"]["global_rows"]]
    determinant_rows = k549["determinant_envelope_bank"]
    determinant_maxima: dict[int, list[Fraction]] = {}
    for rank in range(1, 6):
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
    descriptors = K413_BACKEND.ordered_descriptors()
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

    k414_map = {
        (row["axis"], tuple(row["zeroed_axes"])): row
        for row in k414["face_normal_atlas"]
    }
    face_rows = []
    axis_histogram: Counter[str] = Counter()
    for program in k415["face_programs"]:
        key = (program["axis"], tuple(program["zeroed_axes"]))
        face = k414_map[key]
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
            raise AssertionError("K550 tangential axis census became negative")
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
            "K414_radial_power": radial_power,
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
        "result_id": "K550-ORDER-TEN-WHOLE-RADIAL-FACE-MAJORANTS",
        "created": "2026-09-27",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K409, K413, K414, K415, K545, K547, K549)],
            "global_determinant_envelopes_loaded": len(determinant_rows),
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
            "all_13300_ordered_descriptors_assembled": len(descriptors) == 13300,
            "all_28_coherent_groups_retained_before_final_sum": len({row["group_id"] for row in descriptors}) == 28,
        },
        "descriptor_majorant_bank": descriptor_rows,
        "whole_radial_face_bank": face_rows,
        "whole_radial_contract": {
            "normal_coordinates": "rho=sum of the selected face-normal raw times with exact simplex angular mass 1/(c-1)!",
            "radial_rule": "K414 supplies rho^p with p>=0; combined Laguerre/Peano weight supplies exp(-256*rho), so the exact mass is p!/256^(p+1)",
            "active_peano_rule": "for t<=1/256 use K_256(t)<=t^2/2 and exp(256t)<3; for t>=1/256 use K_256(t)=exp(-256t)/256^2<=t^2 exp(-256t)",
            "inactive_peano_rule": "integrate the exact K409 kernel mass 1/(2*256^3)",
            "nested_transition_rule": "apply the worst exact K549/K547 rank-compatible transition constant at most c-1 times; this is deliberately coarse but finite",
            "every_face_row_is_finite": True,
            "face_rows_overlap_and_must_not_be_summed_as_hybrid_integrals": True,
            "K545_disjoint_owner_stitching_still_required": True,
        },
        "majorant_summary": {
            "face_program_histogram_by_axis": dict(axis_histogram),
            "minimum_radial_power": min(row["K414_radial_power"] for row in face_rows),
            "maximum_radial_power": max(row["K414_radial_power"] for row in face_rows),
            "all_face_rows_finite_positive_rationals": all(Fraction(row["exact_whole_radial_abs_upper"]) > 0 for row in face_rows),
            "v10_v11_have_no_face_rows": axis_histogram["v10"] == 0 and axis_histogram["v11"] == 0,
        },
        "decision": {
            "whole_radial_majorant_emitted_for_every_K414_face_program": True,
            "compact_and_analytic_tail_primitives_composed": True,
            "uniform_face_program_integrand_majorants_complete": True,
            "K545_disjoint_recursive_owner_cover_complete": False,
            "complete_hybrid_integrals_emitted": False,
            "complete_order_ten_remainder_emitted": False,
            "next_exact_input": "stitch these finite face rows to K545's unique owners and a recursive positive-interior cell cover without double counting, then sum each of the twenty-two K409 hybrids",
        },
        "release_test": {
            "all_10958_global_determinant_envelopes_loaded": len(determinant_rows) == 10958,
            "all_13300_ordered_descriptors_assembled": len(descriptors) == 13300,
            "exactly_28_coherent_groups_retained": len({row["group_id"] for row in descriptors}) == 28,
            "exactly_936_face_programs_majorized": len(face_rows) == 936,
            "all_K414_radial_powers_nonnegative": all(row["K414_radial_power"] >= 0 for row in face_rows),
            "maximum_transition_depth_is_21": max(row["maximum_nested_transition_depth"] for row in face_rows) == 21,
            "all_face_rows_finite_positive": all(Fraction(row["exact_whole_radial_abs_upper"]) > 0 for row in face_rows),
            "overlapping_face_rows_not_summed": True,
            "recursive_owner_cover_not_overclaimed": True,
            "complete_order_ten_remainder_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k547["ledger_effect"],
        "source_routing": k547["source_routing"],
        "claim_ceiling": "Exact rational finite whole-radial absolute majorants for all 936 K414/K415 face programs, obtained from all 10,958 K549 global determinant envelopes while retaining all 13,300 ordered descriptors and 28 coherent groups and integrating K414's nonnegative normal powers under the exact K409 Laguerre/Peano measures. The rows deliberately overlap and are not summed into hybrids; K545 disjoint owner stitching, recursive positive-interior cells, all twenty-two complete K409 hybrid integrals, the order-ten remainder/integral, action column, R_ref, K152, source/ledger move, canon, paper, public and physical posture remain open.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["global_determinant_envelopes_loaded"], fixed["ordered_descriptors"], fixed["face_programs"], fixed["hybrid_axes"], fixed["maximum_nested_transition_depth"], fixed["shift"]) != (10958, 13300, 936, 20, 21, 256):
        raise AssertionError("K550 fixed census changed")
    coherent = payload["complete_coherent_majorant"]
    if not coherent["all_13300_ordered_descriptors_assembled"] or not coherent["all_28_coherent_groups_retained_before_final_sum"]:
        raise AssertionError("K550 coherent assembly changed")
    rows = payload["whole_radial_face_bank"]
    if len(rows) != 936 or any(row["K414_radial_power"] < 0 or Fraction(row["exact_whole_radial_abs_upper"]) <= 0 for row in rows):
        raise AssertionError("K550 face bank changed")
    contract = payload["whole_radial_contract"]
    if not contract["every_face_row_is_finite"] or not contract["face_rows_overlap_and_must_not_be_summed_as_hybrid_integrals"] or not contract["K545_disjoint_owner_stitching_still_required"]:
        raise AssertionError("K550 overlap boundary changed")
    decision = payload["decision"]
    if not decision["whole_radial_majorant_emitted_for_every_K414_face_program"] or decision["K545_disjoint_recursive_owner_cover_complete"] or decision["complete_hybrid_integrals_emitted"] or decision["complete_order_ten_remainder_emitted"]:
        raise AssertionError("K550 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K550 release test failed")


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
