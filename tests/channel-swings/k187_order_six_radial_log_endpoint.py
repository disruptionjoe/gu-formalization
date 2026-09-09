#!/usr/bin/env python3
"""K187 exact radial-log obstruction for the K186 Bessel regularizers.

For a fixed positive angular point write T=rho*t and U=rho*u.  The convergent
integer-order expansion used independently in K186 gives

  rho * 2 K1(rho*a)
    = 2/a + rho^2*a*log(rho)
      + rho^2*a*(log(a/2)+gamma-1/2) + O(rho^4 log(rho)).

Consequently the regularizer has

  R_m(rho*t,rho*u)
    = 1 + rho^2*(c_m(t,u) log(rho)+d_m(t,u))
      + O(rho^4 log(rho)^2),

where c_m is the exact directional derivative of det(A+epsilon*B)/det(A)
at epsilon zero, A_ij=2/(t_i+u_j), B_ij=t_i+u_j.  A nonzero c_m makes the
second radial derivative logarithmically unbounded at rho=0.  This module
censuses that coefficient exactly on one admissible rational angular profile
for all 53 K186 patterns.  It refutes the proposed *uniform ordinary smooth*
Jacobi endpoint remainder; it does not refute log-aware or split-domain
certification and does not provide an all-angular sign theorem for c_m.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K186_SOLVER = Path(__file__).with_name("k186_order_six_bessel_vandermonde.py")
K186_MANIFEST = ROOT / "lab/process/k186-order-six-bessel-vandermonde-wave.json"
OUTPUT = ROOT / "lab/process/k187-order-six-radial-log-endpoint-wave.json"
PROFILE_DENOMINATOR = 14
CONTROL_POWERS = (20, 40, 80)


def load_k186():
    spec = importlib.util.spec_from_file_location("k186_for_k187", K186_SOLVER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {K186_SOLVER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K186 = load_k186()


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    return K186.determinant(matrix)


def minor(matrix: list[list[Fraction]], row: int, column: int) -> list[list[Fraction]]:
    return [
        values[:column] + values[column + 1 :]
        for index, values in enumerate(matrix)
        if index != row
    ]


def cumulative_times(positions: list[int], primitives: list[Fraction]) -> list[Fraction]:
    return [sum(primitives[position - 1 :], Fraction(0)) for position in positions]


def exact_log_coefficient(record: dict[str, Any]) -> Fraction:
    """Return D det_A[B]/det(A) exactly on the equal 14-simplex profile."""

    primitives = [Fraction(1, PROFILE_DENOMINATOR)] * 14
    times = cumulative_times(record["left_canonical_positions"], primitives[:7])
    other_times = cumulative_times(record["right_canonical_positions"], primitives[7:])
    cauchy = [[Fraction(2, 1) / (left + right) for right in other_times] for left in times]
    perturbation = [[left + right for right in other_times] for left in times]
    derivative = sum(
        Fraction((-1) ** (row + column), 1)
        * determinant(minor(cauchy, row, column))
        * perturbation[row][column]
        for row in range(len(cauchy))
        for column in range(len(cauchy))
    )
    return derivative / determinant(cauchy)


def fraction_row(value: Fraction) -> dict[str, Any]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "decimal": float(value),
    }


def pattern_occurrences(manifest: dict[str, Any]) -> Counter[str]:
    result: Counter[str] = Counter()
    for entry in manifest["complete_factorization_inventory"]["entries"]:
        for factor in entry["species_factors"]:
            if factor["size"] > 1:
                result[K186.pattern_key(factor)] += 1
    return result


def asymptotic_controls(patterns: dict[str, dict[str, Any]], coefficients: dict[str, Fraction]) -> dict[str, Any]:
    rows = []
    maxima: dict[int, Decimal] = {}
    for power in CONTROL_POWERS:
        precision = 120 + 2 * power
        errors = []
        for pattern_id, record in patterns.items():
            with localcontext() as context:
                context.prec = precision
                rho = Decimal(2) ** (-power)
                primitives = [rho / Decimal(PROFILE_DENOMINATOR)] * 14
                times = K186.times_for(record["left_canonical_positions"], primitives[:7])
                other_times = K186.times_for(record["right_canonical_positions"], primitives[7:])
                regularizer = K186.divided_difference_regularizer(times, other_times, precision)
                quotient = (regularizer - 1) / (rho * rho * rho.ln())
                exact = Decimal(coefficients[pattern_id].numerator) / Decimal(
                    coefficients[pattern_id].denominator
                )
                error = abs(quotient - exact)
                errors.append(error)
                rows.append(
                    {
                        "pattern_id": pattern_id,
                        "rho": f"2^-{power}",
                        "precision_decimal_digits": precision,
                        "scaled_log_quotient": format(quotient, ".22E"),
                        "absolute_error_from_exact_coefficient": format(error, ".12E"),
                    }
                )
        maxima[power] = max(errors)
    return {
        "rows": rows,
        "max_absolute_error_by_radius": {
            f"2^-{power}": format(maxima[power], ".12E") for power in CONTROL_POWERS
        },
        "error_strictly_decreases_at_each_radius": all(
            maxima[right] < maxima[left]
            for left, right in zip(CONTROL_POWERS, CONTROL_POWERS[1:])
        ),
        "role": "high-precision convergent-series/divided-difference asymptotic control; not outward interval arithmetic",
    }


def build() -> dict[str, Any]:
    source = json.loads(K186_MANIFEST.read_text())
    patterns = source["unique_patterns"]
    occurrences = pattern_occurrences(source)
    coefficients = {pattern_id: exact_log_coefficient(record) for pattern_id, record in patterns.items()}
    coefficient_rows = {
        pattern_id: {
            "size": patterns[pattern_id]["size"],
            "occurrences": occurrences[pattern_id],
            "equal_angular_profile_coefficient": fraction_row(value),
        }
        for pattern_id, value in coefficients.items()
    }
    histogram = Counter(f"{value.numerator}/{value.denominator}" for value in coefficients.values())
    controls = asymptotic_controls(patterns, coefficients)
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "source_manifest": "lab/process/k186-order-six-bessel-vandermonde-wave.json",
            "source_patterns": len(patterns),
            "source_nontrivial_occurrences": sum(occurrences.values()),
            "source_time_gram_entries": source["fixed_control"]["source_entries"],
            "angular_profile": "all fourteen primitive coordinates equal 1/14",
            "angular_profile_inside_face_stripped_core": Fraction(1, PROFILE_DENOMINATOR)
            >= Fraction(1, 2**180),
        },
        "radial_log_certificate": {
            "scaled_kernel_expansion": "rho*2*K1(rho*a)=2/a+rho^2*a*log(rho)+rho^2*a*(log(a/2)+gamma-1/2)+O(rho^4*log(rho))",
            "cauchy_matrix": "A_ij=2/(t_i+u_j)",
            "log_perturbation_matrix": "B_ij=t_i+u_j",
            "coefficient_formula": "c_m(t,u)=Ddet_A[B]/det(A)=sum_ij cofactor_ij(A) B_ij/det(A)",
            "regularizer_expansion": "R_m(rho*t,rho*u)=1+rho^2*(c_m(t,u)*log(rho)+d_m(t,u))+O(rho^4*log(rho)^2)",
            "second_derivative_consequence": "d_rho^2 R_m=c_m(t,u)*(2*log(rho)+3)+2*d_m(t,u)+o(1), hence unbounded below when c_m>0",
            "proof_scope": "exact at the declared rational angular profile for every K186 pattern; one nonzero profile already refutes a uniform bounded second-radial-derivative claim on the whole compact core",
            "all_53_profile_coefficients_exact": len(coefficients) == 53,
            "all_53_profile_coefficients_positive": all(value > 0 for value in coefficients.values()),
            "distinct_exact_coefficients": len(set(coefficients.values())),
            "coefficient_range": {
                "minimum": fraction_row(min(coefficients.values())),
                "maximum": fraction_row(max(coefficients.values())),
            },
            "coefficient_histogram": dict(sorted(histogram.items())),
            "patterns": coefficient_rows,
        },
        "coalescent_face_audit": {
            "k186_time_coalescence_extension_preserved": True,
            "radial_endpoint_is_a_distinct_boundary": True,
            "reason": "Newton row/column divided differences remove time-collision Vandermonde zeros, but they do not remove the integer-order Bessel rho^2 log(rho) term",
            "all_angular_coefficient_sign_claimed": False,
            "uniform_mixed_duffy_derivative_enclosure_claimed": False,
        },
        "independent_controls": controls,
        "release_test": {
            "all_53_factor_patterns_censused": len(coefficients) == 53,
            "all_468_nontrivial_occurrences_propagated": sum(occurrences.values()) == 468,
            "all_234_time_gram_entries_remain_in_scope": source["fixed_control"]["source_entries"] == 234,
            "nonzero_rho_squared_log_rho_coefficient_proved": any(value != 0 for value in coefficients.values()),
            "bounded_second_radial_derivative_on_zero_inclusive_core": False,
            "ordinary_smooth_endpoint_jacobi_remainder_applicable": False,
            "k186_continuity_and_positive_coalescent_extension_preserved": True,
            "outward_log_aware_or_split_domain_total_error_serialized": False,
            "accurate_order_six_prefix_released": False,
            "complete_base_action_column_evaluated": False,
            "complete_R_ref_form_dual_residual_serialized": False,
            "positive_complete_M_orthogonal_complement_or_flux_floor_serialized": False,
            "scalar_center_left_floor_serialized": False,
            "native_K152_interval_emitted": False,
        },
        "replacement_route": {
            "retired_route": "ordinary bounded-C2-or-higher Jacobi remainder across rho=0",
            "next_exact_input": "subtract the explicit rho^2 log(rho) endpoint term with an outward remainder or split at a proved small rho epsilon; then use log-weight-aware quadrature or interval cubature on epsilon<=rho<=1/4 and combine with K185 face/tail bounds",
            "must_preserve": "all 234 signed entries, 53 regularizer patterns, old-position factors, primitive gap sums, complete determinants and shared time nodes",
            "release_condition": "one outward total error covering the small-rho endpoint, face strips, compact interior and rho>1/4 tail",
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
        certificate = dict(result["radial_log_certificate"])
        certificate.pop("patterns", None)
        print(
            json.dumps(
                {
                    "classification": result["classification"],
                    "fixed_control": result["fixed_control"],
                    "radial_log_certificate": certificate,
                    "independent_controls": {
                        key: value
                        for key, value in result["independent_controls"].items()
                        if key != "rows"
                    },
                    "release_test": result["release_test"],
                    "replacement_route": result["replacement_route"],
                },
                indent=2,
                sort_keys=True,
            )
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
