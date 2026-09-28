#!/usr/bin/env python3
"""Assemble coherent higher-order derivatives and integrate every K561 face."""

from __future__ import annotations

import argparse
import hashlib
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
K378 = ROOT / "lab/process/k378-rank-six-global-scaled-bessel-bank.json"
K558 = ROOT / "lab/process/k558-orders-eleven-twelve-positive-peano-contract.json"
K559 = ROOT / "lab/process/k559-orders-eleven-twelve-hybrid-face-atlas.json"
K561 = ROOT / "lab/process/k561-orders-eleven-twelve-face-normal-integrability-atlas.json"
K562 = ROOT / "lab/process/k562-orders-eleven-twelve-global-determinant-envelopes.json"
K560_PRODUCER = HERE / "k560_orders_eleven_twelve_rank_six_mask_native_preconditioner.py"
OUTPUT = ROOT / "lab/process/k563-orders-eleven-twelve-whole-radial-face-majorants.json"
SHIFT = 256
EXPECTED = {11: (25200, 24, 1198), 12: (69552, 33, 1535)}


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K560_BACKEND = load_module(K560_PRODUCER, "k560_for_k563")


def q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def multiply_taylor(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    result = [Fraction(), Fraction(), Fraction()]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= 2:
                result[i + j] += a * b
    return result


def descriptor_digest(rows: list[dict[str, Any]]) -> str:
    h = hashlib.sha256()
    for row in rows:
        h.update(json.dumps(row, sort_keys=True, separators=(",", ":")).encode())
        h.update(b"\n")
    return "sha256:" + h.hexdigest()


def build() -> dict[str, Any]:
    k378 = json.loads(K378.read_text())
    k558 = json.loads(K558.read_text())
    k559 = json.loads(K559.read_text())
    k561 = json.loads(K561.read_text())
    k562 = json.loads(K562.read_text())
    primitive = [Fraction(row["global_scaled_upper"]) for row in k378["global_scaled_bessel_bank"]["rows"]]
    determinant_rows = k562["determinant_envelope_bank"]
    determinant_maxima = {
        rank: [
            max(Fraction(env["exact_rational_abs_upper"]) for row in determinant_rows if row["rank"] == rank for env in row["derivative_envelopes"] if env["derivative_order"] == order)
            for order in range(3)
        ]
        for rank in range(1, 7)
    }
    transition_constant = max(Fraction(env["exact_rational_abs_upper"]) for row in determinant_rows for env in row["derivative_envelopes"])
    old_taylor = [primitive[order] / math.factorial(order) for order in range(3)]
    face_power = {
        (int(order_row["order"]), face["axis"], tuple(face["zeroed_axes"])): int(face["minimum_certified_second_derivative_face_normal_power"])
        for order_row in k561["order_atlases"] for face in order_row["face_normal_atlas"]
    }
    order_contracts = {int(row["order"]): row for row in k558["order_contracts"]}
    order_face_atlases = {int(row["order"]): row for row in k559["order_atlases"]}
    order_results = []
    combined_descriptor_rows = []
    combined_face_rows = []
    for order in (11, 12):
        descriptors = K560_BACKEND.ordered_descriptors(order)
        complete_taylor = [Fraction(), Fraction(), Fraction()]
        factor_histogram: Counter[int] = Counter()
        rank_pattern_histogram: Counter[str] = Counter()
        descriptor_rows = []
        for descriptor in descriptors:
            polynomial = [Fraction(1), Fraction(), Fraction()]
            polynomial = multiply_taylor(polynomial, old_taylor)
            polynomial = multiply_taylor(polynomial, old_taylor)
            ranks = []
            for matrix in descriptor["species_matrices"]:
                rank = int(matrix["rank"])
                ranks.append(rank)
                polynomial = multiply_taylor(polynomial, [determinant_maxima[rank][index] / math.factorial(index) for index in range(3)])
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
                "normalized_second_abs_upper": q(2 * polynomial[2]),
            })
        complete_second = 2 * complete_taylor[2]
        face_rows = []
        for hybrid in order_face_atlases[order]["hybrid_face_atlas"]:
            moving_dimension = len(hybrid["moving_axes"])
            preceding_count = len(order_contracts[order]["fixed_control"]["native_axes"]) - moving_dimension
            for face_kind, faces in hybrid["faces"].items():
                for face in faces:
                    mask = tuple(face["zeroed_axes"])
                    codimension = int(face["codimension"])
                    radial_power = face_power[(order, hybrid["axis"], mask)]
                    active = bool(face["active_peano_axis_zeroed"])
                    angular_mass = Fraction(1, math.factorial(codimension - 1))
                    radial_mass = Fraction(math.factorial(radial_power), SHIFT ** (radial_power + 1))
                    if active:
                        peano_factor = Fraction(3, 2)
                        exponential_tangential_axes = moving_dimension - codimension
                        peano_rule = "K_256(t)*exp(-256*sum_other)<=3*t^2*exp(-256*rho)/2"
                    else:
                        peano_factor = Fraction(1, 2 * SHIFT**3)
                        exponential_tangential_axes = moving_dimension - codimension - 1
                        peano_rule = "integral K_256(t)dt=1/(2*256^3)"
                    if exponential_tangential_axes < 0:
                        raise AssertionError("K563 tangential axis census became negative")
                    upper = (
                        complete_second * transition_constant ** (codimension - 1) * angular_mass * radial_mass * peano_factor
                        * Fraction(1, SHIFT**exponential_tangential_axes) * Fraction(1, SHIFT**preceding_count)
                    )
                    face_rows.append({
                        "program_id": f"order{order}:{hybrid['axis']}:{face_kind}:{','.join(mask)}",
                        "order": order,
                        "axis": hybrid["axis"],
                        "face_kind": face_kind,
                        "zeroed_axes": list(mask),
                        "codimension": codimension,
                        "moving_dimension": moving_dimension,
                        "preceding_node_axes": preceding_count,
                        "active_peano_axis_zeroed": active,
                        "K561_radial_power": radial_power,
                        "maximum_nested_transition_depth": codimension - 1,
                        "exact_projective_simplex_mass": q(angular_mass),
                        "exact_radial_gamma_mass": q(radial_mass),
                        "peano_measure_rule": peano_rule,
                        "exponential_tangential_axes": exponential_tangential_axes,
                        "exact_whole_radial_abs_upper": q(upper),
                    })
        expected_descriptors, expected_groups, expected_faces = EXPECTED[order]
        if (len(descriptors), len({row["group_id"] for row in descriptors}), len(face_rows)) != EXPECTED[order]:
            raise AssertionError(f"K563 order-{order} census changed")
        order_results.append({
            "order": order,
            "coherent_majorant": {
                "ordered_descriptors": len(descriptors),
                "coherent_groups": expected_groups,
                "descriptor_majorant_stream_sha256": descriptor_digest(descriptor_rows),
                "factor_count_histogram": {str(key): factor_histogram[key] for key in sorted(factor_histogram)},
                "species_rank_pattern_histogram": dict(sorted(rank_pattern_histogram.items())),
                "normalized_complete_value_first_second_taylor_uppers": [q(value) for value in complete_taylor],
                "normalized_complete_second_derivative_abs_upper": q(complete_second),
            },
            "whole_radial_face_bank": face_rows,
            "order_summary": {
                "all_ordered_descriptors_assembled": len(descriptors) == expected_descriptors,
                "all_coherent_groups_retained": len({row["group_id"] for row in descriptors}) == expected_groups,
                "all_reachable_faces_majorized": len(face_rows) == expected_faces,
                "minimum_radial_power": min(row["K561_radial_power"] for row in face_rows),
                "maximum_radial_power": max(row["K561_radial_power"] for row in face_rows),
                "all_face_rows_finite_positive_rationals": all(Fraction(row["exact_whole_radial_abs_upper"]) > 0 for row in face_rows),
            },
        })
        combined_descriptor_rows.extend(descriptor_rows)
        combined_face_rows.extend(face_rows)
    return {
        "schema_version": "1.0",
        "result_id": "K563-ORDERS-ELEVEN-TWELVE-WHOLE-RADIAL-FACE-MAJORANTS",
        "created": "2026-09-28",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "predecessor_manifests": [str(path.relative_to(ROOT)) for path in (K378, K558, K559, K561, K562)],
            "orders": [11, 12],
            "global_determinant_envelopes_loaded": len(determinant_rows),
            "combined_ordered_descriptors": len(combined_descriptor_rows),
            "combined_coherent_groups": sum(row["coherent_majorant"]["coherent_groups"] for row in order_results),
            "combined_face_programs": len(combined_face_rows),
            "shift": SHIFT,
        },
        "shared_majorant_contract": {
            "old_kernel_taylor_uppers": [q(value) for value in old_taylor],
            "determinant_derivative_uppers_by_rank": {str(rank): [q(value) for value in values] for rank, values in determinant_maxima.items()},
            "transition_constant": q(transition_constant),
            "normal_coordinates": "rho is the sum of selected face-normal raw times with exact simplex mass 1/(c-1)!",
            "radial_rule": "K561 supplies rho^p with p>=0 and the K558 weight supplies exp(-256*rho), giving exact mass p!/256^(p+1)",
            "face_rows_overlap_and_must_not_be_summed_as_hybrid_integrals": True,
            "symbolic_disjoint_owner_stitching_still_required": True,
            "raw_Bessel_evaluation_at_zero_used": False,
        },
        "order_majorants": order_results,
        "majorant_summary": {
            "combined_descriptor_stream_sha256": descriptor_digest(combined_descriptor_rows),
            "all_2733_face_rows_finite_positive": len(combined_face_rows) == 2733 and all(Fraction(row["exact_whole_radial_abs_upper"]) > 0 for row in combined_face_rows),
            "global_minimum_radial_power": min(row["K561_radial_power"] for row in combined_face_rows),
            "maximum_transition_depth": max(row["maximum_nested_transition_depth"] for row in combined_face_rows),
        },
        "decision": {
            "whole_radial_majorant_emitted_for_every_K561_face": True,
            "compact_and_analytic_tail_primitives_composed": True,
            "uniform_face_integrand_majorants_complete": True,
            "disjoint_recursive_owner_cover_complete": False,
            "complete_hybrid_integrals_emitted": False,
            "next_exact_input": "compile exact symbolic first-match face owners, charge each owner union once, and bound every positive interior before summing the fifty K558 hybrids",
        },
        "release_test": {
            "all_3540_global_determinant_envelopes_loaded": len(determinant_rows) == 3540,
            "all_94752_ordered_descriptors_assembled": len(combined_descriptor_rows) == 94752,
            "exactly_57_coherent_groups_retained": sum(row["coherent_majorant"]["coherent_groups"] for row in order_results) == 57,
            "exactly_2733_face_programs_majorized": len(combined_face_rows) == 2733,
            "all_K561_radial_powers_nonnegative": all(row["K561_radial_power"] >= 0 for row in combined_face_rows),
            "all_face_rows_finite_positive": all(Fraction(row["exact_whole_radial_abs_upper"]) > 0 for row in combined_face_rows),
            "overlapping_face_rows_not_summed": True,
            "recursive_owner_cover_not_overclaimed": True,
            "complete_remainders_not_overclaimed": True,
            "native_K152_interval_not_emitted": True,
        },
        "ledger_effect": k562["ledger_effect"],
        "source_routing": k562["source_routing"],
        "claim_ceiling": "Exact rational finite whole-radial absolute majorants for all 2,733 K561 face instances, obtained from all 3,540 K562 coefficient envelopes while retaining all 94,752 ordered descriptors and 57 coherent groups across separate order-eleven/twelve domains. The rows overlap and are not summed into hybrids; symbolic disjoint ownership, recursive positive interiors, complete remainders/integrals, base action, R_ref, K152, source/ledger movement, canon, paper, public, novelty and physical claims remain open.",
    }


def validate_payload(payload: dict[str, Any]) -> None:
    fixed = payload["fixed_control"]
    if (fixed["global_determinant_envelopes_loaded"], fixed["combined_ordered_descriptors"], fixed["combined_coherent_groups"], fixed["combined_face_programs"], fixed["shift"]) != (3540, 94752, 57, 2733, 256):
        raise AssertionError("K563 fixed census changed")
    faces = [face for row in payload["order_majorants"] for face in row["whole_radial_face_bank"]]
    if len(faces) != 2733 or any(face["K561_radial_power"] < 0 or Fraction(face["exact_whole_radial_abs_upper"]) <= 0 for face in faces):
        raise AssertionError("K563 face bank changed")
    contract = payload["shared_majorant_contract"]
    if not contract["face_rows_overlap_and_must_not_be_summed_as_hybrid_integrals"] or not contract["symbolic_disjoint_owner_stitching_still_required"] or contract["raw_Bessel_evaluation_at_zero_used"]:
        raise AssertionError("K563 overlap boundary changed")
    decision = payload["decision"]
    if not decision["whole_radial_majorant_emitted_for_every_K561_face"] or decision["disjoint_recursive_owner_cover_complete"] or decision["complete_hybrid_integrals_emitted"]:
        raise AssertionError("K563 decision boundary changed")
    if not all(payload["release_test"].values()):
        raise AssertionError("K563 release test failed")


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
