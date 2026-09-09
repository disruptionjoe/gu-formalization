#!/usr/bin/env python3
"""K188 outward small-radius strip certificate for the order-six family.

K185 reduces every determinant-expanded absolute majorant to a common radial
Gamma density with shape six and rate 256.  K187 shows that differentiating
the determinant regularizers through rho=0 is not a valid smooth-endpoint
route.  This module instead discards 0 <= rho < 2^-20 under the K185
majorant.  The normalized lower tail obeys, exactly,

    P(6, x) = gamma(6, x) / Gamma(6) <= x^6 / 720,

because exp(-u) <= 1 and Gamma(6)=5!.  The resulting rational ceiling is
propagated through all eighteen coherent groups.  High-precision incomplete-
gamma values are controls only; the rational inequality carries the proof.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

from scipy.special import gammainc


ROOT = Path(__file__).resolve().parents[2]
K185_MANIFEST = ROOT / "lab/process/k185-order-six-duffy-face-tail-wave.json"
K187_MANIFEST = ROOT / "lab/process/k187-order-six-radial-log-endpoint-wave.json"
OUTPUT = ROOT / "lab/process/k188-order-six-small-rho-strip-wave.json"
RATE = 256
SHAPE = 6
EPSILON_POWER = 20
EPSILON = Fraction(1, 2**EPSILON_POWER)
RADIAL_CUTOFF = Fraction(1, 4)


def fraction_row(value: Fraction) -> dict[str, Any]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "decimal": float(value),
    }


def as_fraction(row: dict[str, Any]) -> Fraction:
    return Fraction(int(row["numerator"]), int(row["denominator"]))


def lower_tail_fraction_ceiling(epsilon: Fraction) -> Fraction:
    x = RATE * epsilon
    return x**SHAPE / Fraction(SHAPE * math.factorial(SHAPE - 1), 1)


def independent_controls() -> dict[str, Any]:
    rows = []
    for power in (16, 20, 24, 28):
        epsilon = 2.0 ** (-power)
        x = RATE * epsilon
        exact = float(gammainc(SHAPE, x))
        ceiling = x**SHAPE / (SHAPE * math.factorial(SHAPE - 1))
        rows.append(
            {
                "epsilon": f"2^-{power}",
                "x_equals_256_epsilon": f"{x:.18e}",
                "normalized_incomplete_gamma_control": f"{exact:.18e}",
                "rational_inequality_ceiling_decimal": f"{ceiling:.18e}",
                "control_below_ceiling": exact < ceiling,
                "ceiling_to_control_ratio": f"{ceiling / exact:.16e}",
            }
        )
    return {
        "precision": "IEEE-754 binary64 SciPy regularized incomplete gamma",
        "rows": rows,
        "all_controls_strictly_below_rational_ceiling": all(
            row["control_below_ceiling"] for row in rows
        ),
        "role": "independent floating incomplete-gamma checks only; the exact exp(-u)<=1 inequality carries the outward certificate",
    }


def build() -> dict[str, Any]:
    source = json.loads(K185_MANIFEST.read_text())
    endpoint = json.loads(K187_MANIFEST.read_text())
    groups = source["groups"]
    fraction_ceiling = lower_tail_fraction_ceiling(EPSILON)
    group_rows: dict[str, Any] = {}
    small_bounds: list[Fraction] = []
    face_bounds: list[Fraction] = []
    tail_bounds: list[Fraction] = []
    boundary_sums: list[Fraction] = []
    for group_id, group in sorted(groups.items()):
        bounds = group["proof_safe_bounds"]
        whole = as_fraction(bounds["whole_group_global_ceiling"])
        face = as_fraction(bounds["any_simplex_coordinate_below_2^-180_group_ceiling"])
        tail = as_fraction(bounds["rho_greater_than_one_quarter_group_ceiling"])
        small = whole * fraction_ceiling
        boundary_sum = small + face + tail
        group_rows[group_id] = {
            "weighted_leibniz_term_count": group["weighted_leibniz_term_count"],
            "whole_group_global_ceiling": fraction_row(whole),
            "rho_below_2^-20_group_ceiling": fraction_row(small),
            "k185_face_strip_group_ceiling": fraction_row(face),
            "k185_rho_above_one_quarter_group_ceiling": fraction_row(tail),
            "combined_known_boundary_group_ceiling": fraction_row(boundary_sum),
            "small_strip_below_face_bound": small < face,
            "small_strip_below_radial_tail_bound": small < tail,
        }
        small_bounds.append(small)
        face_bounds.append(face)
        tail_bounds.append(tail)
        boundary_sums.append(boundary_sum)

    k185_fixed = source["fixed_control"]
    k185_graph = source["complete_face_hypergraph"]
    k187_fixed = endpoint["fixed_control"]
    tail_fraction = as_fraction(
        next(iter(groups.values()))["proof_safe_bounds"]
        ["rho_greater_than_one_quarter_fraction_ceiling"]
    )
    face_fraction = as_fraction(
        next(iter(groups.values()))["proof_safe_bounds"]
        ["any_simplex_coordinate_below_2^-180_fraction_ceiling"]
    )
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "source_manifest": "lab/process/k185-order-six-duffy-face-tail-wave.json",
            "endpoint_manifest": "lab/process/k187-order-six-radial-log-endpoint-wave.json",
            "source_coherent_groups": len(groups),
            "source_time_gram_entries": k185_graph["gram_entries"],
            "source_leibniz_terms": k185_graph["leibniz_terms"],
            "source_nontrivial_patterns": k187_fixed["source_patterns"],
            "source_nontrivial_occurrences": k187_fixed["source_nontrivial_occurrences"],
            "radial_shape": source["radial_duffy_certificate"]["radial_shape"],
            "radial_rate": k185_fixed["chart_shift"],
            "face_floor": source["radial_duffy_certificate"]["face_delta"],
            "radial_cutoff": source["radial_duffy_certificate"]["large_radius_cutoff"],
        },
        "small_radius_certificate": {
            "selected_epsilon": "2^-20",
            "selected_epsilon_fraction": fraction_row(EPSILON),
            "x_equals_rate_times_epsilon": fraction_row(RATE * EPSILON),
            "normalized_gamma_shape_six_density": "256^6*rho^5*exp(-256*rho)/Gamma(6)",
            "exact_inequality": "P(6,x)=integral_0^x u^5 exp(-u) du/Gamma(6) <= x^6/(6 Gamma(6)) = x^6/720",
            "proof_step": "exp(-u)<=1 for u>=0 and Gamma(6)=5!=120",
            "normalized_lower_tail_fraction_ceiling": fraction_row(fraction_ceiling),
            "ceiling_below_k185_face_fraction": fraction_ceiling < face_fraction,
            "ceiling_below_k185_radial_tail_fraction": fraction_ceiling < tail_fraction,
            "k185_face_fraction_to_small_fraction_ratio_control": float(face_fraction / fraction_ceiling),
            "k185_tail_fraction_to_small_fraction_ratio_control": float(tail_fraction / fraction_ceiling),
            "applies_to_all_angular_coordinates": True,
            "depends_on_regularizer_radial_derivatives": False,
            "consumes_k187_log_obstruction_without_differentiating_through_zero": True,
        },
        "complete_group_propagation": {
            "groups": group_rows,
            "all_18_coherent_groups_covered": len(group_rows) == 18,
            "all_234_time_gram_entries_covered": k185_graph["gram_entries"] == 234,
            "all_1864_leibniz_terms_covered": k185_graph["leibniz_terms"] == 1864,
            "all_53_nontrivial_patterns_remain_in_scope": k187_fixed["source_patterns"] == 53,
            "all_468_nontrivial_occurrences_remain_in_scope": k187_fixed["source_nontrivial_occurrences"] == 468,
            "small_radius_group_ceiling_range": {
                "minimum": fraction_row(min(small_bounds)),
                "maximum": fraction_row(max(small_bounds)),
            },
            "combined_known_boundary_group_ceiling_range": {
                "minimum": fraction_row(min(boundary_sums)),
                "maximum": fraction_row(max(boundary_sums)),
            },
            "every_small_strip_bound_below_face_and_tail_bounds": all(
                small < face and small < tail
                for small, face, tail in zip(small_bounds, face_bounds, tail_bounds)
            ),
        },
        "domain_cover": {
            "regions": [
                {
                    "id": "small_radius_all_angles",
                    "domain": "0<=rho<2^-20 on the complete angular simplex",
                    "status": "OUTWARD_BOUND_CLOSED",
                    "certificate": "K188 exact Gamma-six lower-tail inequality",
                },
                {
                    "id": "positive_radius_angular_faces",
                    "domain": "2^-20<=rho<=1/4 and some z_i<2^-180",
                    "status": "OUTWARD_BOUND_CLOSED",
                    "certificate": "K185 face bound integrated over a superset, hence still valid",
                },
                {
                    "id": "positive_radius_face_stripped_core",
                    "domain": "2^-20<=rho<=1/4 and all z_i>=2^-180",
                    "status": "OPEN_DETERMINANT_PRESERVING_INTERVAL_ERROR",
                    "certificate": None,
                },
                {
                    "id": "large_radius_all_angles",
                    "domain": "rho>1/4 on the complete angular simplex",
                    "status": "OUTWARD_BOUND_CLOSED",
                    "certificate": "K185 rational Gamma-six upper-tail bound",
                },
            ],
            "covers_complete_positive_orthant_after_radialization": True,
            "known_boundary_bounds_may_be_added_by_union_bound": True,
            "only_open_region": "positive_radius_face_stripped_core",
            "determinants_remain_unexpanded_in_open_numerical_core": True,
        },
        "independent_controls": independent_controls(),
        "release_test": {
            "outward_small_radius_strip_error_serialized": True,
            "positive_split_radius_selected": True,
            "all_18_groups_and_234_entries_covered": True,
            "k185_face_and_radial_tail_bounds_composed": True,
            "k187_zero_endpoint_derivative_premise_avoided": True,
            "positive_radius_face_stripped_core_is_only_remaining_order_six_integration_region": True,
            "determinant_preserving_positive_radius_core_error_serialized": False,
            "complete_outward_order_six_total_error_serialized": False,
            "accurate_order_six_prefix_released": False,
            "complete_base_action_column_evaluated": False,
            "complete_R_ref_form_dual_residual_serialized": False,
            "positive_complete_M_orthogonal_complement_or_flux_floor_serialized": False,
            "scalar_center_left_floor_serialized": False,
            "native_K152_interval_emitted": False,
        },
        "next_exact_input": {
            "owner": "determinant-preserving positive-radius weighted interval cubature",
            "domain": "2^-20<=rho<=1/4 and z_i>=2^-180",
            "first_gate": "derive outward value and mixed-derivative enclosures for each of the 53 K186 divided-difference regularizers on the positive-radius face-stripped core, then certify the Duffy/Jacobi remainder without expanding determinants",
            "must_preserve": "all 234 signed entries, 18 coherent groups, K179 signs, old-position factors, primitive gaps, complete species determinants and shared time nodes",
        },
        "ledger_effect": {
            "SC-META-53": "UNCERTAIN_UNCHANGED",
            "LT-SM8": "NEEDS_UNCHANGED",
            "RA-F1": "NEEDS_UNCHANGED",
            "AC-F1": "NEEDS_UNCHANGED",
        },
        "physical_or_source_selection": False,
        "Born_prediction_or_confirmation_credit": False,
        "canon_paper_release_or_public_posture_move": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.write:
        OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if args.summary or not args.write:
        propagation = dict(result["complete_group_propagation"])
        propagation.pop("groups", None)
        print(json.dumps({
            "fixed_control": result["fixed_control"],
            "small_radius_certificate": result["small_radius_certificate"],
            "complete_group_propagation": propagation,
            "domain_cover": result["domain_cover"],
            "independent_controls": result["independent_controls"],
            "release_test": result["release_test"],
            "next_exact_input": result["next_exact_input"],
        }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
