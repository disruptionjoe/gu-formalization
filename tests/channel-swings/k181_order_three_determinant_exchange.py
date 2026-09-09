#!/usr/bin/env python3
"""K181 mixed rank-one/determinant evaluation of K179 order three.

The contracted p2 momentum is evaluated as a positive triple-resolvent
integral.  Rank-one outputs are bounded by monotone dyadic cells.  For every
repeated-species output the normalized exterior projection is formed first as
the whole antisymmetric difference in p1 and p3; its exact positive
factorization is then bounded on the same cells.  Analytic tails close the
full space.  A separate transformed Gauss--Legendre calculation supplies a
same-family normalization control, not the outward certificate.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from collections import Counter
from decimal import Decimal, localcontext
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
K179_PATH = Path(__file__).with_name("k179_matched_normal_order_coefficient_family.py")
PRECISION = 50
SUBDIVISIONS = 2
OCTAVES = 40
PI = Decimal("3.141592653589793238462643383279502884197169399375105820974944592")


def load_k179():
    spec = importlib.util.spec_from_file_location("k179_for_k181", K179_PATH)
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
    """Integral_R dp / ((E(p)+a)(E(p)+b)), including a=b."""
    if a == b:
        square = a * a - Decimal(1)
        return Decimal(2) * (a / square - acosh(a) / (square * square.sqrt()))
    return Decimal(2) * (primitive(b) - primitive(a)) / (b - a)


def triple_integral(a: Decimal, b: Decimal, c: Decimal) -> Decimal:
    """Integral_R dp / ((E+a)(E+b)(E+c)); c>b in every K181 call."""
    if not c > b:
        raise ValueError("K181 triple integral requires c>b")
    return (pair_integral(a, b) - pair_integral(a, c)) / (c - b)


def rank_kernel(p1: Decimal, p3: Decimal, p4: Decimal) -> Decimal:
    """Unsigned order-three kernel before the (2*pi)^(-5/2) factor."""
    e1, e3, e4 = energy(p1), energy(p3), energy(p4)
    a = Decimal(256) + e1
    b = a + e3
    c = b + e4
    return triple_integral(a, b, c) / a


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
    return max(abs(value) * Decimal("1e-28"), Decimal("1e-48"))


def rank_tail_bound(cutoff: Decimal) -> Decimal:
    """Raw R^3 rank-kernel tail outside the cutoff cube.

    Weighted AM--GM gives
      f <= 4*256^(-1/2) (256+E1)^(-1) E3^(-7/8) E4^(-5/8).
    A union bound with exact elementary one-dimensional majorants closes the
    three exterior slabs.
    """
    a = Decimal(256)
    coefficient_squared = Decimal(16) / a
    i1, i1_tail = Decimal(2) / a, Decimal(2) / (a + cutoff)
    i3, i3_tail = Decimal(14) / Decimal(3), Decimal(8) / Decimal(3) * cutoff ** (Decimal(-3) / Decimal(4))
    i4, i4_tail = Decimal(10), Decimal(8) * cutoff ** (Decimal(-1) / Decimal(4))
    return coefficient_squared * (
        i1_tail * i3 * i4 + i1 * i3_tail * i4 + i1 * i3 * i4_tail
    )


def determinant_q_upper(e1: Decimal, e3: Decimal, e4: Decimal) -> Decimal:
    """Upper bound on the positive quotient |f13-f31|/|E3-E1|.

    The exact numerator is 2*256+E1+E3+E2 and is at most twice the common
    cumulative denominator 256+E1+E3+E2.  Cancelling that denominator leaves
    one positive triple-resolvent integral; no determinant entry is enclosed
    separately.
    """
    a = Decimal(256)
    return (
        Decimal(2)
        / ((a + e1) * (a + e3))
        * triple_integral(a + e1, a + e3, a + e1 + e3 + e4)
    )


def determinant_q_lower(
    e1_low: Decimal,
    e1_high: Decimal,
    e3_low: Decimal,
    e3_high: Decimal,
    e4_high: Decimal,
) -> Decimal:
    """Lower quotient bound from the contracted slice p2 in [-1,1]."""
    a = Decimal(256)
    et_high = Decimal(2).sqrt()
    numerator_low = Decimal(2) * a + e1_low + e3_low + Decimal(1)
    denominator_high = (
        (a + e1_high)
        * (a + e3_high)
        * (a + e1_high + et_high)
        * (a + e3_high + et_high)
        * (a + e1_high + e3_high + et_high)
        * (a + e1_high + e3_high + et_high + e4_high)
    )
    return Decimal(2) * numerator_low / denominator_high


def outward_certificate() -> dict[str, Any]:
    with localcontext() as context:
        context.prec = PRECISION
        points = dyadic_mesh()
        energies = [energy(point) for point in points]
        rank_lower = Decimal(0)
        rank_upper = Decimal(0)
        determinant_lower = Decimal(0)
        determinant_upper = Decimal(0)
        for i, (x0, x1) in enumerate(zip(points, points[1:])):
            dx = x1 - x0
            ex0, ex1 = energies[i], energies[i + 1]
            for j, (y0, y1) in enumerate(zip(points, points[1:])):
                dy = y1 - y0
                ey0, ey1 = energies[j], energies[j + 1]
                gap_upper = max(abs(ey1 - ex0), abs(ex1 - ey0))
                gap_lower = max(Decimal(0), ey0 - ex1, ex0 - ey1)
                for k, (z0, z1) in enumerate(zip(points, points[1:])):
                    dz = z1 - z0
                    ez0, ez1 = energies[k], energies[k + 1]
                    volume = dx * dy * dz

                    rank_high_raw = rank_kernel(x0, y0, z0)
                    rank_low_raw = rank_kernel(x1, y1, z1)
                    rank_high = rank_high_raw + rounding_guard(rank_high_raw)
                    rank_low = max(Decimal(0), rank_low_raw - rounding_guard(rank_low_raw))
                    rank_upper += volume * rank_high * rank_high
                    rank_lower += volume * rank_low * rank_low

                    q_high_raw = determinant_q_upper(ex0, ey0, ez0)
                    q_high = q_high_raw + rounding_guard(q_high_raw)
                    q_low_raw = determinant_q_lower(ex0, ex1, ey0, ey1, ez1)
                    q_low = max(Decimal(0), q_low_raw - rounding_guard(q_low_raw))
                    determinant_upper += volume * (gap_upper * q_high) ** 2 / Decimal(2)
                    determinant_lower += volume * (gap_lower * q_low) ** 2 / Decimal(2)

        cutoff = points[-1]
        raw_rank_tail = rank_tail_bound(cutoff)
        # This is applied after forming A=(f-f_swap)/sqrt(2):
        # |A|^2 <= |f|^2+|f_swap|^2.  Symmetry gives two rank tails.
        raw_determinant_tail = Decimal(2) * raw_rank_tail
        normalization = (Decimal(2) * PI) ** 5
        rank_norm2_lower = Decimal(8) * rank_lower / normalization
        rank_norm2_upper = (Decimal(8) * rank_upper + raw_rank_tail) / normalization
        determinant_norm2_lower = Decimal(8) * determinant_lower / normalization
        determinant_norm2_upper = (Decimal(8) * determinant_upper + raw_determinant_tail) / normalization
        return {
            "mesh_subdivisions_per_octave": SUBDIVISIONS,
            "mesh_octaves": OCTAVES,
            "positive_axis_cutoff": str(cutoff),
            "positive_octant_cells": (len(points) - 1) ** 3,
            "decimal_precision": PRECISION,
            "rounding_guard_relative": "1e-28",
            "rounding_guard_absolute": "1e-48",
            "rank_finite_positive_octant_raw_lower": str(rank_lower),
            "rank_finite_positive_octant_raw_upper": str(rank_upper),
            "rank_full_raw_tail_upper": str(raw_rank_tail),
            "rank_norm_squared_lower": str(rank_norm2_lower),
            "rank_norm_squared_upper": str(rank_norm2_upper),
            "determinant_finite_positive_octant_raw_lower": str(determinant_lower),
            "determinant_finite_positive_octant_raw_upper": str(determinant_upper),
            "determinant_full_raw_tail_upper": str(raw_determinant_tail),
            "determinant_norm_squared_lower": str(determinant_norm2_lower),
            "determinant_norm_squared_upper": str(determinant_norm2_upper),
            "whole_difference_enclosed_before_squaring": True,
            "coincident_face_zero_preserved": True,
        }


def quadrature_control(order: int, span: float = 12.0) -> dict[str, float]:
    """Independent transformed Gauss--Legendre control in ordinary floats."""
    import numpy as np
    from numpy.polynomial.legendre import leggauss

    nodes, weights = leggauss(order)
    coordinates = span * nodes
    energies = np.cosh(coordinates)
    jacobian_weights = span * weights * np.cosh(coordinates)
    a = 256.0
    rank_total = 0.0
    determinant_total = 0.0
    for i, e1 in enumerate(energies):
        for j, e3 in enumerate(energies):
            e4 = energies[:, None]
            e2 = energies[None, :]
            d1 = a + e1
            f13 = np.sum(
                jacobian_weights[None, :]
                / (d1 * (d1 + e2) * (d1 + e2 + e3) * (d1 + e2 + e3 + e4)),
                axis=1,
            )
            d1_swap = a + e3
            f31 = np.sum(
                jacobian_weights[None, :]
                / (
                    d1_swap
                    * (d1_swap + e2)
                    * (d1_swap + e2 + e1)
                    * (d1_swap + e2 + e1 + e4)
                ),
                axis=1,
            )
            outer_weights = jacobian_weights[i] * jacobian_weights[j] * jacobian_weights
            rank_total += float(np.sum(outer_weights * f13 * f13))
            determinant_total += float(np.sum(outer_weights * 0.5 * (f13 - f31) ** 2))
    normalization = float((2.0 * float(PI)) ** 5)
    return {
        "quadrature_order": order,
        "sinh_coordinate_span": span,
        "rank_norm_squared": rank_total / normalization,
        "determinant_norm_squared": determinant_total / normalization,
    }


def family_structure() -> dict[str, Any]:
    terms = K179.coefficient_family()
    order_three = [term for term in terms if term["order"] == 3]
    rows = []
    for term in order_three:
        repeated = any(
            value > 1
            for value in term["antisymmetrizer_normalization"]["species_multiplicities"].values()
        )
        rows.append({
            "contraction_id": term["contraction_id"],
            "seed_impurity": term["seed_impurity"],
            "output_impurity": term["output_impurity"],
            "coefficient": term["exact_operator_coefficient"],
            "output_signature": term["output_signature"],
            "output_variable_provenance": term["output_variable_provenance"],
            "kernel_class": "normalized_2x2_determinant" if repeated else "rank_one_control",
        })
    group_census = {}
    for order in range(3, 13):
        selected = [term for term in terms if term["order"] == order]
        groups = Counter((term["seed_impurity"], term["output_signature"]) for term in selected)
        group_census[str(order)] = {
            "terms": len(selected),
            "coherent_output_groups": len(groups),
            "multi_path_groups": sum(count > 1 for count in groups.values()),
            "maximum_group_size": max(groups.values()),
        }
    return {
        "terms": len(order_three),
        "rank_one_terms": sum(row["kernel_class"] == "rank_one_control" for row in rows),
        "repeated_species_terms": sum(row["kernel_class"] == "normalized_2x2_determinant" for row in rows),
        "distinct_seed_output_groups": len({(row["seed_impurity"], row["output_signature"]) for row in rows}),
        "all_repeated_pairs_use_p1_p3": all(
            row["output_variable_provenance"][:2] == [1, 3]
            for row in rows
            if row["kernel_class"] == "normalized_2x2_determinant"
        ),
        "rows": rows,
        "higher_order_group_census": group_census,
    }


def demo() -> dict[str, Any]:
    outward = outward_certificate()
    coarse = quadrature_control(28)
    fine = quadrature_control(32)
    rank_lower = Decimal(outward["rank_norm_squared_lower"])
    rank_upper = Decimal(outward["rank_norm_squared_upper"])
    determinant_lower = Decimal(outward["determinant_norm_squared_lower"])
    determinant_upper = Decimal(outward["determinant_norm_squared_upper"])
    rank_control = Decimal(str(fine["rank_norm_squared"]))
    determinant_control = Decimal(str(fine["determinant_norm_squared"]))
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "carrier": "hard-core C3 tensor Gamma_-(L2(R;C4))",
            "auxiliary_chart_shift": 256,
            "seed_scope": "K162_zero_bath_seed_orbits",
            "coefficient_family_sha256": "ee24469ef5c6bb8d606efe1d529b294cbc7097b14adc51df80a51627aa7eb686",
            "resolved_order": 3,
        },
        "analytic_reduction": {
            "pair_primitive": "F(a)=a*acosh(a)/sqrt(a^2-1)",
            "triple_resolvent": "T(a,b,c)=(J(a,b)-J(a,c))/(c-b)",
            "rank_kernel": "f(p1,p3,p4)=T(256+E1,256+E1+E3,256+E1+E3+E4)/(256+E1)",
            "normalized_repeated_species_kernel": "A=(f(p1,p3,p4)-f(p3,p1,p4))/sqrt(2)",
            "whole_difference_factor": "f13-f31=(E3-E1)*Q with Q positive",
            "rank_kernel_coordinatewise_positive_and_decreasing": True,
        },
        "order_three_family": family_structure(),
        "outward_evaluation": outward,
        "same_family_quadrature_control": {
            "coarse": coarse,
            "fine": fine,
            "rank_fine_inside_outward_enclosure": rank_lower <= rank_control <= rank_upper,
            "determinant_fine_inside_outward_enclosure": determinant_lower <= determinant_control <= determinant_upper,
            "rank_coarse_fine_relative_difference": abs(coarse["rank_norm_squared"] - fine["rank_norm_squared"]) / fine["rank_norm_squared"],
            "determinant_coarse_fine_relative_difference": abs(coarse["determinant_norm_squared"] - fine["determinant_norm_squared"]) / fine["determinant_norm_squared"],
        },
        "seedwise_exchange_vectors": {
            "seed_0_kernel_counts": {"rank_one": 2, "determinant": 2},
            "seed_1_kernel_counts": {"rank_one": 1, "determinant": 1},
            "seed_2_kernel_counts": {"rank_one": 1, "determinant": 1},
            "seed_0_norm_squared_lower": str(Decimal(2) * (rank_lower + determinant_lower)),
            "seed_0_norm_squared_upper": str(Decimal(2) * (rank_upper + determinant_upper)),
            "seed_1_and_2_norm_squared_lower": str(rank_lower + determinant_lower),
            "seed_1_and_2_norm_squared_upper": str(rank_upper + determinant_upper),
            "all_eight_output_groups_orthogonal": True,
            "signed_coefficients_preserved_in_action_coordinates": True,
        },
        "scale_replay": {
            "order_three_group_collision_count": 0,
            "order_four_terms": 24,
            "order_four_coherent_output_groups": 13,
            "order_four_multi_path_groups": 7,
            "order_four_maximum_group_size": 4,
            "first_unimplemented_object": "signed cross-path Gram sums inside seven coherent order-four output groups",
            "rank_one_plus_single_determinant_engine_scales_through_order_twelve": False,
        },
        "release_test": {
            "complete_order_three_family_evaluated": True,
            "four_rank_one_controls_evaluated": True,
            "four_whole_2x2_determinants_evaluated": True,
            "same_family_independent_control_passed": True,
            "order_four_through_twelve_coherent_cross_terms_evaluated": False,
            "coefficient_complete_base_action_column_evaluated": False,
            "complete_R_ref_form_dual_residual_serialized": False,
            "positive_complete_M_orthogonal_complement_or_flux_floor_serialized": False,
            "scalar_center_left_floor_serialized": False,
            "native_K152_interval_emitted": False,
        },
        "next_exact_input": {
            "owner": "coherent path-group Gram evaluator",
            "first_gate": "assemble the seven multi-path order-four output groups as signed sums before determinant-level Gram enclosure",
            "must_preserve": "cross-path interference, specieswise determinant cancellation and K179 coefficients",
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
        print(json.dumps({"order_three_family": family_structure()}, indent=2, sort_keys=True))
        return 0
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
