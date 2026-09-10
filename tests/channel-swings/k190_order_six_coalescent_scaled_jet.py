#!/usr/bin/env python3
"""K190 cancellation-preserving coalescent jets for K186 regularizers.

The K186 regularizer is

    R_m(T,U) = det[2 K_1(T_i+U_j)] / det[2/(T_i+U_j)].

At complete row/column coalescence the mixed divided differences are a Hankel
matrix of derivatives.  Writing q(x)=x K_1(x) and a_n=x^n q^(n)(x) cancels
every negative power of x algebraically before Arb evaluation.  This module
serializes the exact size-two and size-three normal forms, a directed-Arb
dyadic spine, and all-pattern high-precision near-collision controls.

It does not enclose finite nonzero gaps or a Duffy/Jacobi cubature remainder.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
from decimal import Decimal, localcontext
from pathlib import Path
from typing import Any

import mpmath as mp
from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
K186_PATH = ROOT / "tests/channel-swings/k186_order_six_bessel_vandermonde.py"
K186_MANIFEST = ROOT / "lab/process/k186-order-six-bessel-vandermonde-wave.json"
K189_MANIFEST = ROOT / "lab/process/k189-order-six-arb-core-jet-envelope-wave.json"
OUTPUT = ROOT / "lab/process/k190-order-six-coalescent-scaled-jet-wave.json"
ARB_DIGITS = 200
DECIMAL_DIGITS = 260
DYADIC_POWERS = tuple(range(2, 201))
NEAR_COLLISION_POWERS = (10, 24)


ctx.dps = ARB_DIGITS
ctx.threads = 1
mp.mp.dps = DECIMAL_DIGITS


def load_k186():
    spec = importlib.util.spec_from_file_location("k186", K186_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K186 solver")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K186 = load_k186()


def determinant(matrix: list[list[arb]]) -> arb:
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if len(matrix) == 3:
        return (
            matrix[0][0]
            * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
            - matrix[0][1]
            * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
            + matrix[0][2]
            * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
        )
    raise ValueError("K190 admits only size-two and size-three determinants")


def f_derivative(order: int, x: arb) -> arb:
    """Exact Bessel-recurrence enclosure of d^order(2 K_1)/dx^order."""

    total = arb(0)
    for index in range(order + 1):
        bessel_order = abs(1 - order + 2 * index)
        total += math.comb(order, index) * x.bessel_k(bessel_order)
    sign = -1 if order % 2 else 1
    return sign * (arb(2) ** (1 - order)) * total


def scaled_q_jets(x: arb) -> tuple[arb, arb, arb, arb, arb]:
    """Return a_n=x^n q^(n)(x), n=0..4, without singular subtraction."""

    q = x * x.bessel_k(1)
    k0 = x.bessel_k(0)
    x2 = x * x
    x4 = x2 * x2
    return (
        q,
        -x2 * k0,
        x2 * (q - k0),
        x2 * q - x4 * k0,
        (x4 - x2) * q - 2 * x4 * k0,
    )


def regularizer_from_scaled_jets(size: int, jets: tuple[Any, ...]):
    q, a1, a2, a3, a4 = jets
    if size == 2:
        return q * q + q * a2 - a1 * a1
    if size == 3:
        return (
            q**3
            + 3 * q * q * a2
            - 3 * q * a1 * a1
            + q * q * a3
            - 3 * q * a1 * a2
            + 2 * a1**3
            + (q * q * a4 - 4 * q * a1 * a3 + 3 * q * a2 * a2) / 4
            + (
                q * a2 * a4
                - q * a3 * a3
                - a1 * a1 * a4
                + 2 * a1 * a2 * a3
                - a2**3
            )
            / 4
        )
    raise ValueError("K190 admits only sizes two and three")


def regularizer_from_confluent_hankel(size: int, x: arb) -> arb:
    matrix = [
        [
            f_derivative(row + column, x)
            / (math.factorial(row) * math.factorial(column))
            for column in range(size)
        ]
        for row in range(size)
    ]
    return x ** (size * size) * determinant(matrix) / (arb(2) ** size)


def arb_row(power: int) -> dict[str, Any]:
    x = arb(2) ** (-power)
    jets = scaled_q_jets(x)
    r2 = regularizer_from_scaled_jets(2, jets)
    r3 = regularizer_from_scaled_jets(3, jets)
    raw2 = regularizer_from_confluent_hankel(2, x)
    raw3 = regularizer_from_confluent_hankel(3, x)
    if not raw2.overlaps(r2) or not raw3.overlaps(r3):
        raise AssertionError(f"confluent identity lost overlap at 2^-{power}")
    if not r2.lower() > 0 or not r3.lower() > 0:
        raise AssertionError(f"positive coalescent spine lost at 2^-{power}")
    return {
        "x": f"2^-{power}",
        "scaled_jets": {str(index): str(value) for index, value in enumerate(jets)},
        "R2": str(r2),
        "R3": str(r3),
        "R2_midpoint": float(r2.mid()),
        "R3_midpoint": float(r3.mid()),
        "R2_radius": float(r2.rad()),
        "R3_radius": float(r3.rad()),
        "raw_hankel_overlaps_scaled_R2": True,
        "raw_hankel_overlaps_scaled_R3": True,
        "scaled_width_gain_R2": float(raw2.rad() / r2.rad()),
        "scaled_width_gain_R3": float(raw3.rad() / r3.rad()),
    }


def mpmath_scaled_regularizer(size: int, x_text: str) -> mp.mpf:
    x = mp.mpf(x_text)
    q = x * mp.besselk(1, x)
    k0 = mp.besselk(0, x)
    x2 = x * x
    x4 = x2 * x2
    jets = (q, -x2 * k0, x2 * (q - k0), x2 * q - x4 * k0, (x4 - x2) * q - 2 * x4 * k0)
    return regularizer_from_scaled_jets(size, jets)


def near_collision_controls(patterns: dict[str, dict[str, Any]]) -> dict[str, Any]:
    rows = []
    for pattern_index, (pattern_id, record) in enumerate(sorted(patterns.items())):
        size = int(record["size"])
        x_text = f"0.{(pattern_index % 19) + 2:02d}"
        x = Decimal(x_text)
        left_base = x * Decimal(2) / 5
        right_base = x * Decimal(3) / 5
        reference = mpmath_scaled_regularizer(size, x_text)
        errors = []
        values = []
        for gap_power in NEAR_COLLISION_POWERS:
            with localcontext() as context:
                context.prec = DECIMAL_DIGITS + 40
                epsilon = Decimal(10) ** (-gap_power)
                left = [
                    left_base + Decimal(size - 1 - index) * epsilon
                    for index in range(size)
                ]
                right = [
                    right_base + Decimal(size - 1 - index) * epsilon
                    for index in range(size)
                ]
            value = K186.divided_difference_regularizer(
                left, right, DECIMAL_DIGITS
            )
            relative = abs(mp.mpf(str(value)) - reference) / abs(reference)
            errors.append(float(relative))
            values.append(format(value, ".24E"))
        if errors[-1] >= 1e-20:
            raise AssertionError(f"near-collision control too wide for {pattern_id}")
        rows.append(
            {
                "pattern_id": pattern_id,
                "size": size,
                "left_canonical_positions": record["left_canonical_positions"],
                "right_canonical_positions": record["right_canonical_positions"],
                "coalescent_x": x_text,
                "gap_powers": list(NEAR_COLLISION_POWERS),
                "values": values,
                "relative_errors_to_scaled_jet_limit": errors,
                "finest_gap_relative_error_below_1e_minus_20": True,
            }
        )
    return {
        "patterns": rows,
        "tested_patterns": len(rows),
        "gap_powers": list(NEAR_COLLISION_POWERS),
        "maximum_finest_gap_relative_error": max(
            row["relative_errors_to_scaled_jet_limit"][-1] for row in rows
        ),
        "all_finest_gap_errors_below_1e_minus_20": True,
        "role": "independent high-precision finite-gap convergence controls; not outward finite-gap intervals",
    }


def build() -> dict[str, Any]:
    source = json.loads(K186_MANIFEST.read_text())
    predecessor = json.loads(K189_MANIFEST.read_text())
    patterns = source["unique_patterns"]
    dyadic = [arb_row(power) for power in DYADIC_POWERS]
    near = near_collision_controls(patterns)
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "source_manifest": "lab/process/k186-order-six-bessel-vandermonde-wave.json",
            "predecessor_manifest": "lab/process/k189-order-six-arb-core-jet-envelope-wave.json",
            "domain": predecessor["fixed_control"]["domain"],
            "coalescent_argument_range": "2^-200<=x<=1/4",
            "source_patterns": len(patterns),
            "source_nontrivial_occurrences": predecessor["fixed_control"]["source_nontrivial_occurrences"],
            "source_time_gram_entries": predecessor["fixed_control"]["source_time_gram_entries"],
            "source_coherent_groups": predecessor["fixed_control"]["source_coherent_groups"],
        },
        "exact_normal_form": {
            "kernel": "q(x)=x*K1(x)",
            "scaled_jets": "a_n=x^n*q^(n)(x), n=0..4, with a_0=q",
            "coalescent_hankel": "R_m(x)=x^(m^2)*det[(2*K1)^(i+j)(x)/(i!*j!)]_(i,j=0..m-1)/2^m",
            "R2": "q^2+q*a2-a1^2",
            "R3": "q^3+3*q^2*a2-3*q*a1^2+q^2*a3-3*q*a1*a2+2*a1^3+(q^2*a4-4*q*a1*a3+3*q*a2^2)/4+(q*a2*a4-q*a3^2-a1^2*a4+2*a1*a2*a3-a2^3)/4",
            "jet_identities": {
                "a0": "x*K1(x)",
                "a1": "-x^2*K0(x)",
                "a2": "x^2*(q(x)-K0(x))",
                "a3": "x^2*q(x)-x^4*K0(x)",
                "a4": "(x^4-x^2)*q(x)-2*x^4*K0(x)",
            },
            "negative_powers_cancel_before_evaluation": True,
            "maximum_derivative_order": 4,
        },
        "arb_certificate": {
            "python_flint_decimal_digits": ARB_DIGITS,
            "threads": 1,
            "dyadic_rows": dyadic,
            "tested_radii": len(dyadic),
            "all_raw_hankel_balls_overlap_scaled_balls": True,
            "all_scaled_R2_and_R3_balls_strictly_positive": True,
            "R2_midpoint_range": [
                min(row["R2_midpoint"] for row in dyadic),
                max(row["R2_midpoint"] for row in dyadic),
            ],
            "R3_midpoint_range": [
                min(row["R3_midpoint"] for row in dyadic),
                max(row["R3_midpoint"] for row in dyadic),
            ],
            "minimum_width_gain_R2": min(row["scaled_width_gain_R2"] for row in dyadic),
            "minimum_width_gain_R3": min(row["scaled_width_gain_R3"] for row in dyadic),
        },
        "independent_controls": {
            "all_pattern_near_collision": near,
            "symbolic_polynomial_identity_checked_by_probe": True,
        },
        "decision": {
            "coalescent_singularity_is_numerically_resolved": True,
            "scaled_q_jets_are_selected_core_coordinates": True,
            "entrywise_scaled_kernel_boxes_are_sufficient": False,
            "finite_gap_outward_coverage_is_complete": False,
            "next_exact_input": "derive bivariate confluent divided-difference Taylor enclosures for the scaled q-jet normal forms on dyadic radial strata and gap-ratio boxes; bound the finite-gap defect from the coalescent spine before composing the Duffy/Jacobi chain rule",
            "must_preserve": "all 234 signed entries, 18 coherent groups, 53 patterns, 468 nontrivial occurrences, primitive gaps, old-position factors, complete determinants and shared time nodes",
        },
        "release_test": {
            "exact_R2_scaled_jet_normal_form_banked": True,
            "exact_R3_scaled_jet_normal_form_banked": True,
            "directed_arb_dyadic_coalescent_spine_banked": True,
            "all_53_patterns_replayed_near_collision": near["tested_patterns"] == 53,
            "all_468_occurrences_remain_in_scope": predecessor["fixed_control"]["source_nontrivial_occurrences"] == 468,
            "finite_gap_regularizer_interval_serialized": False,
            "duffy_jacobi_chain_rule_envelopes_serialized": False,
            "determinant_preserving_positive_radius_core_error_serialized": False,
            "complete_outward_order_six_total_error_serialized": False,
            "accurate_order_six_prefix_released": False,
            "complete_base_action_column_evaluated": False,
            "complete_R_ref_form_dual_residual_serialized": False,
            "positive_complete_M_orthogonal_complement_or_flux_floor_serialized": False,
            "scalar_center_left_floor_serialized": False,
            "native_K152_interval_emitted": False,
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


def summary(result: dict[str, Any]) -> dict[str, Any]:
    return {
        "fixed_control": result["fixed_control"],
        "exact_normal_form": result["exact_normal_form"],
        "arb_certificate": {
            key: value
            for key, value in result["arb_certificate"].items()
            if key != "dyadic_rows"
        },
        "independent_controls": {
            "tested_patterns": result["independent_controls"]["all_pattern_near_collision"]["tested_patterns"],
            "maximum_finest_gap_relative_error": result["independent_controls"]["all_pattern_near_collision"]["maximum_finest_gap_relative_error"],
            "all_finest_gap_errors_below_1e_minus_20": result["independent_controls"]["all_pattern_near_collision"]["all_finest_gap_errors_below_1e_minus_20"],
        },
        "decision": result["decision"],
        "release_test": result["release_test"],
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
        print(json.dumps(summary(result), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
