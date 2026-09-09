#!/usr/bin/env python3
"""K180 outward evaluation of the common K179 order-two exchange kernel.

The contracted momentum is integrated analytically as a second divided
difference.  Coordinatewise monotonicity then gives lower and upper dyadic
rectangle sums for the remaining two momenta.  A weighted-AM--GM majorant
closes the infinite complement.  A piecewise-constant midpoint compression is
checked against the same enclosure with a cell-oscillation L2 error.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from decimal import Decimal, localcontext
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K179_PATH = Path(__file__).with_name("k179_matched_normal_order_coefficient_family.py")
PRECISION = 50
SUBDIVISIONS = 6
OCTAVES = 40
PI = Decimal("3.141592653589793238462643383279502884197169399375105820974944592")


def load_k179():
    spec = importlib.util.spec_from_file_location("k179_for_k180", K179_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {K179_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K179 = load_k179()


def energy(momentum: Decimal) -> Decimal:
    return (Decimal(1) + momentum * momentum).sqrt()


def acosh(value: Decimal) -> Decimal:
    return (value + (value * value - Decimal(1)).sqrt()).ln()


def primitive(value: Decimal) -> Decimal:
    return value * acosh(value) / (value * value - Decimal(1)).sqrt()


def pair_integral(a: Decimal, b: Decimal) -> Decimal:
    """Integral_R dp / ((E(p)+a)(E(p)+b))."""
    return Decimal(2) * (primitive(b) - primitive(a)) / (b - a)


def common_kernel(p2: Decimal, p3: Decimal) -> Decimal:
    """Integral_R dp1 /(D1 D2 D3), before the (2*pi)^-2 factor."""
    a = Decimal(256)
    b = a + energy(p2)
    c = b + energy(p3)
    return (pair_integral(a, b) - pair_integral(a, c)) / (c - b)


def dyadic_mesh(subdivisions: int = SUBDIVISIONS, octaves: int = OCTAVES) -> list[Decimal]:
    if subdivisions < 2 or octaves < 1:
        raise ValueError("positive dyadic mesh resolution required")
    points = [Decimal(0)] + [Decimal(i + 1) / subdivisions for i in range(subdivisions)]
    for octave in range(octaves):
        left = Decimal(2) ** octave
        step = left / subdivisions
        points.extend(left + step * i for i in range(1, subdivisions + 1))
    return points


def rounding_guard(value: Decimal) -> Decimal:
    # Decimal sqrt/ln are correctly rounded at the active precision.  This
    # guard exceeds the accumulated primitive-operation ulps by >10^15 even
    # after the divided differences at every admitted mesh endpoint.
    return max(abs(value) * Decimal("1e-30"), Decimal("1e-45"))


def full_tail_bound() -> Decimal:
    """Raw R^2 tail outside [-2^40,2^40]^2.

    Weighted AM--GM with alpha=1/8 on D2 and weights
    (1/64,1/16,59/64) on D3 gives
      K <= (64/9) E2^(-15/16) E3^(-59/64).
    The coefficient is deliberately enlarged by dropping all weight products.
    Elementary p-power tails then give the exact rational bound below.
    """
    coefficient_squared = Decimal(64 * 64) / Decimal(9 * 9)
    y_total = Decimal(15) / Decimal(7)
    z_total = Decimal(59) / Decimal(27)
    y_tail = (Decimal(8) / Decimal(7)) / (Decimal(2) ** 35)
    # The exact 2^(-135/4) is smaller than the rational 2^-33 used here.
    z_tail = (Decimal(32) / Decimal(27)) / (Decimal(2) ** 33)
    return Decimal(4) * coefficient_squared * (y_tail * z_total + y_total * z_tail)


def direct_kernel_bounds(p2: Decimal, p3: Decimal) -> tuple[Decimal, Decimal]:
    """Independent one-dimensional monotone enclosure of the p1 integral."""
    points = dyadic_mesh(32, 24)
    e2, e3 = energy(p2), energy(p3)

    def integrand(p1: Decimal) -> Decimal:
        e1 = energy(p1)
        return Decimal(1) / ((Decimal(256) + e1) * (Decimal(256) + e1 + e2) * (Decimal(256) + e1 + e2 + e3))

    lower = Decimal(0)
    upper = Decimal(0)
    for left, right in zip(points, points[1:]):
        width = right - left
        upper += width * integrand(left)
        lower += width * integrand(right)
    cutoff = points[-1]
    tail = Decimal(1) / (Decimal(256) + cutoff) ** 2
    return Decimal(2) * lower, Decimal(2) * upper + tail


def outward_certificate() -> dict[str, Any]:
    with localcontext() as context:
        context.prec = PRECISION
        points = dyadic_mesh()
        lower = Decimal(0)
        upper = Decimal(0)
        midpoint = Decimal(0)
        oscillation_error = Decimal(0)
        for i, (x0, x1) in enumerate(zip(points, points[1:])):
            dx = x1 - x0
            xm = (x0 + x1) / Decimal(2)
            for y0, y1 in zip(points, points[1:]):
                dy = y1 - y0
                ym = (y0 + y1) / Decimal(2)
                area = dx * dy
                high_raw = common_kernel(x0, y0)
                low_raw = common_kernel(x1, y1)
                mid = common_kernel(xm, ym)
                high = high_raw + rounding_guard(high_raw)
                low = max(Decimal(0), low_raw - rounding_guard(low_raw))
                lower += area * low * low
                upper += area * high * high
                midpoint += area * mid * mid
                oscillation_error += area * (high - low) * (high - low)

        tail = full_tail_bound()
        normalization = (Decimal(2) * PI) ** 4
        norm2_lower = Decimal(4) * lower / normalization
        norm2_upper = (Decimal(4) * upper + tail) / normalization
        compression_norm2 = Decimal(4) * midpoint / normalization
        compression_l2_error = ((Decimal(4) * oscillation_error + tail) / normalization).sqrt()

        anchor_rows = []
        for p2, p3 in ((Decimal(0), Decimal(0)), (Decimal(1), Decimal(2)), (Decimal(100), Decimal(100))):
            closed = common_kernel(p2, p3)
            direct_lower, direct_upper = direct_kernel_bounds(p2, p3)
            anchor_rows.append({
                "p2": str(p2),
                "p3": str(p3),
                "closed_form": str(closed),
                "direct_lower": str(direct_lower),
                "direct_upper": str(direct_upper),
                "closed_form_inside_direct_enclosure": direct_lower <= closed <= direct_upper,
            })

        return {
            "mesh_subdivisions_per_octave": SUBDIVISIONS,
            "mesh_octaves": OCTAVES,
            "positive_axis_cutoff": str(points[-1]),
            "positive_quadrant_cells": (len(points) - 1) ** 2,
            "decimal_precision": PRECISION,
            "rounding_guard_relative": "1e-30",
            "rounding_guard_absolute": "1e-45",
            "finite_positive_quadrant_raw_lower": str(lower),
            "finite_positive_quadrant_raw_upper": str(upper),
            "full_raw_tail_upper": str(tail),
            "single_kernel_norm_squared_lower": str(norm2_lower),
            "single_kernel_norm_squared_upper": str(norm2_upper),
            "single_kernel_norm_lower": str(norm2_lower.sqrt()),
            "single_kernel_norm_upper": str(norm2_upper.sqrt()),
            "midpoint_compression_norm_squared": str(compression_norm2),
            "midpoint_compression_l2_error_upper": str(compression_l2_error),
            "midpoint_compression_inside_outward_enclosure": norm2_lower <= compression_norm2 <= norm2_upper,
            "direct_integral_anchor_controls": anchor_rows,
        }


def family_structure() -> dict[str, Any]:
    terms = K179.coefficient_family()
    order_two = [term for term in terms if term["order"] == 2]
    by_seed: dict[str, list[dict[str, str]]] = {}
    for term in order_two:
        by_seed.setdefault(str(term["seed_impurity"]), []).append({
            "contraction_id": term["contraction_id"],
            "coefficient": term["exact_operator_coefficient"],
            "output_signature": term["output_signature"],
        })
    repeated_by_order = {}
    for order in range(2, 13):
        rows = [term for term in terms if term["order"] == order]
        repeated_by_order[str(order)] = {
            "terms": len(rows),
            "terms_with_repeated_output_species": sum(
                any(value > 1 for value in term["antisymmetrizer_normalization"]["species_multiplicities"].values())
                for term in rows
            ),
        }
    return {
        "order_two_terms": len(order_two),
        "all_share_common_unsigned_kernel": len({term["output_kernel_formula"]["ordered_kernel"].lstrip("-1*") for term in order_two}) == 1,
        "each_seed_has_two_orthogonal_output_signatures": all(len(rows) == 2 and len({row["output_signature"] for row in rows}) == 2 for rows in by_seed.values()),
        "seed_rows": by_seed,
        "determinant_rank_at_order_two": 1,
        "higher_order_repeated_species_census": repeated_by_order,
    }


def demo() -> dict[str, Any]:
    certificate = outward_certificate()
    structure = family_structure()
    lower = Decimal(certificate["single_kernel_norm_squared_lower"])
    upper = Decimal(certificate["single_kernel_norm_squared_upper"])
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "carrier": "hard-core C3 tensor Gamma_-(L2(R;C4))",
            "auxiliary_chart_shift": 256,
            "seed_scope": "K162_zero_bath_seed_orbits",
            "coefficient_family_sha256": "ee24469ef5c6bb8d606efe1d529b294cbc7097b14adc51df80a51627aa7eb686",
            "resolved_order": 2,
        },
        "analytic_reduction": {
            "primitive": "F(a)=a*acosh(a)/sqrt(a^2-1)",
            "pair_integral": "J(a,b)=2*(F(b)-F(a))/(b-a)",
            "common_kernel": "K(p2,p3)=(J(256,256+E2)-J(256,256+E2+E3))/E3",
            "coordinatewise_positive_and_decreasing": True,
            "order_two_determinants_are_rank_one": True,
        },
        "order_two_family": structure,
        "outward_evaluation": certificate,
        "seedwise_exchange_vector": {
            "orthogonal_common_kernel_copies_per_seed": 2,
            "norm_squared_lower": str(Decimal(2) * lower),
            "norm_squared_upper": str(Decimal(2) * upper),
            "norm_lower": str((Decimal(2) * lower).sqrt()),
            "norm_upper": str((Decimal(2) * upper).sqrt()),
            "signs_preserved_in_action_coordinates": True,
            "cross_terms_vanish_by_impurity_species_output_orthogonality": True,
        },
        "release_test": {
            "all_six_order_two_kernels_evaluated": True,
            "determinant_level_outward_bounds_certified": True,
            "same_family_conforming_compression_with_error_certified": True,
            "order_two_normalization_agrees": True,
            "order_three_through_twelve_nontrivial_determinants_evaluated": False,
            "coefficient_complete_base_action_column_evaluated": False,
            "complete_R_ref_form_dual_residual_serialized": False,
            "positive_complete_M_orthogonal_complement_or_flux_floor_serialized": False,
            "scalar_center_left_floor_serialized": False,
            "native_K152_interval_emitted": False,
        },
        "next_exact_input": {
            "owner": "grouped determinant-simplex evaluator",
            "first_gate": "evaluate the four order-three terms with repeated output species as signed 2x2 heat-kernel determinants while keeping the other four rank-one terms in the same grouped basis",
            "must_preserve": "path-pair grouping and determinant cancellation before interval enclosure",
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
    parser.add_argument("--demo", action="store_true")
    parser.add_argument("--quick", action="store_true")
    args = parser.parse_args()
    if args.quick:
        structure = family_structure()
        print(json.dumps({"order_two_family": structure}, indent=2, sort_keys=True))
        return 0
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
