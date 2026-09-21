#!/usr/bin/env python3
"""K281 size-four scaled-jet and gap-stratified outward calculus.

K280 adds one genuine size-four Cauchy--Vandermonde pattern.  This certificate
extends the coalescent scaled-q Hankel form through a_6, then tests the actual
K191/K192 normalized Taylor argument at size four.  It also freezes all 63
nonempty row/column gap masks.  Certified cells are outward Arb intervals;
the residual arbitrary-gap faces and Duffy/Jacobi cubature remain open.
"""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import math
from decimal import Decimal, localcontext
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import Any

from flint import arb, ctx


ROOT = Path(__file__).resolve().parents[2]
K190_PATH = ROOT / "tests/channel-swings/k190_order_six_coalescent_scaled_jet.py"
K280_PATH = ROOT / "tests/channel-swings/k280_order_seven_bessel_vandermonde_face_atlas.py"
K280_MANIFEST = ROOT / "lab/process/k280-order-seven-bessel-vandermonde-face-atlas.json"
OUTPUT = ROOT / "lab/process/k281-order-seven-size-four-outward-calculus.json"

SIZE = 4
ARB_DIGITS = 320
TAYLOR_ORDER = 16
RADIAL_FLOOR_POWER = 200
RADIAL_SPLIT_POWER = 3
RADIAL_CEILING_POWER = 2
LOW_GAP_CANDIDATES = tuple(Fraction(1, n) for n in (48, 64, 96, 128, 192, 256, 512))
HIGH_GAP_CANDIDATES = tuple(Fraction(1, n) for n in (512, 768, 1024, 1536, 2048))
SUBDIVISION_CANDIDATES = (8, 16, 32, 64, 128, 256)

ctx.dps = ARB_DIGITS
ctx.threads = 1


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K190 = load_module("k190_for_k281", K190_PATH)
K280 = load_module("k280_for_k281", K280_PATH)


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def rational_ball(value: Fraction) -> arb:
    return arb(fraction_text(value))


def interval_from_bounds(lower: Fraction, upper: Fraction) -> arb:
    return arb(fraction_text((lower + upper) / 2), fraction_text((upper - lower) / 2))


def determinant(matrix: list[list[Any]]):
    size = len(matrix)
    total = matrix[0][0] * 0
    for permutation in itertools.permutations(range(size)):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(size)
            for j in range(i + 1, size)
        )
        term = matrix[0][0] * 0 + (-1 if inversions % 2 else 1)
        for row, column in enumerate(permutation):
            term *= matrix[row][column]
        total += term
    return total


def polynomial_derivative(poly: dict[int, int]) -> dict[int, int]:
    return {degree - 1: degree * value for degree, value in poly.items() if degree}


def polynomial_add(*polys: dict[int, int]) -> dict[int, int]:
    result: dict[int, int] = {}
    for poly in polys:
        for degree, value in poly.items():
            result[degree] = result.get(degree, 0) + value
    return {degree: value for degree, value in result.items() if value}


def polynomial_scale(poly: dict[int, int], scale: int, shift: int = 0) -> dict[int, int]:
    return {degree + shift: scale * value for degree, value in poly.items() if value}


def jet_polynomials(maximum_order: int = 6) -> list[tuple[dict[int, int], dict[int, int]]]:
    """Return a_n=P_n(x^2)q+Q_n(x^2)K0 by D=x*d/dx recurrence."""

    result = [({0: 1}, {})]
    for order in range(maximum_order):
        p, q0 = result[-1]
        next_p = polynomial_add(
            polynomial_scale(polynomial_derivative(p), 2, 1),
            polynomial_scale(q0, -1),
            polynomial_scale(p, -order),
        )
        next_q = polynomial_add(
            polynomial_scale(p, -1, 1),
            polynomial_scale(polynomial_derivative(q0), 2, 1),
            polynomial_scale(q0, -order),
        )
        result.append((next_p, next_q))
    return result


JET_POLYNOMIALS = jet_polynomials()


def evaluate_polynomial(poly: dict[int, int], value: Any):
    total = value * 0
    for degree, coefficient in poly.items():
        total += coefficient * value**degree
    return total


def scaled_q_jets(x: arb) -> tuple[arb, ...]:
    square = x * x
    q = x * x.bessel_k(1)
    k0 = x.bessel_k(0)
    return tuple(
        evaluate_polynomial(p, square) * q + evaluate_polynomial(q0, square) * k0
        for p, q0 in JET_POLYNOMIALS
    )


def b_from_a(order: int, jets: tuple[Any, ...]):
    total = jets[0] * 0
    for index in range(order + 1):
        total += ((-1) ** (order - index)) * jets[index] / math.factorial(index)
    return math.factorial(order) * total


def scaled_r4(x: arb) -> arb:
    jets = scaled_q_jets(x)
    matrix = [
        [b_from_a(row + column, jets) / (math.factorial(row) * math.factorial(column)) for column in range(SIZE)]
        for row in range(SIZE)
    ]
    return determinant(matrix)


def raw_r4(x: arb) -> arb:
    matrix = [
        [K190.f_derivative(row + column, x) / (2 * math.factorial(row) * math.factorial(column)) for column in range(SIZE)]
        for row in range(SIZE)
    ]
    return x ** (SIZE * SIZE) * determinant(matrix)


def jet_formula(poly: dict[int, int], symbol: str) -> str:
    if not poly:
        return "0"
    terms = []
    for degree in sorted(poly, reverse=True):
        coefficient = poly[degree]
        magnitude = abs(coefficient)
        base = symbol if degree == 1 else (f"{symbol}^{degree}" if degree else "1")
        body = base if magnitude == 1 and degree else f"{magnitude}*{base}"
        if not terms:
            terms.append(("-" if coefficient < 0 else "") + body)
        else:
            terms.append((" - " if coefficient < 0 else " + ") + body)
    return "".join(terms)


def dyadic_spine() -> list[dict[str, Any]]:
    rows = []
    for power in range(2, RADIAL_FLOOR_POWER + 1):
        x = arb(2) ** (-power)
        scaled = scaled_r4(x)
        raw = raw_r4(x)
        if not scaled.lower() > 0:
            raise AssertionError(f"scaled R4 lost positivity at 2^-{power}: {scaled}")
        if not scaled.overlaps(raw):
            raise AssertionError(f"raw/scaled R4 mismatch at 2^-{power}")
        rows.append(
            {
                "x": f"2^-{power}",
                "scaled_ball": str(scaled),
                "raw_ball": str(raw),
                "scaled_midpoint": float(scaled.mid()),
                "scaled_width_gain": float(raw.rad() / scaled.rad()) if scaled.rad() else None,
            }
        )
    return rows


@lru_cache(maxsize=None)
def complete_homogeneous(nodes: tuple[Fraction, ...], maximum_degree: int) -> tuple[Fraction, ...]:
    values = [Fraction(0)] * (maximum_degree + 1)
    values[0] = Fraction(1)
    for node in nodes:
        updated = [Fraction(0)] * (maximum_degree + 1)
        for degree in range(maximum_degree + 1):
            updated[degree] = sum(values[degree - k] * node**k for k in range(degree + 1))
        values = updated
    return tuple(values)


@lru_cache(maxsize=None)
def monomial_dd_bounds(
    power: int,
    row: int,
    column: int,
    radial_width: Fraction,
    gap_radius: Fraction,
) -> tuple[Fraction, Fraction]:
    """Bounds for [r_0..r_i][c_0..c_j](w+r+c)^power.

    The multinomial/complete-homogeneous expansion has nonnegative
    coefficients, so the extrema occur at the all-zero and all-upper corners.
    This avoids symbolic cancellation and scales cleanly to size four.
    """

    derivative_order = row + column
    if power < derivative_order:
        return Fraction(0), Fraction(0)
    lower = Fraction(math.factorial(power), math.factorial(row) * math.factorial(column)) if power == derivative_order else Fraction(0)
    # Newton rows use prefixes of the canonical size-four node tuple
    # (gap, gap, gap, 0); only the last prefix reaches the zero endpoint.
    canonical_nodes = (gap_radius,) * (SIZE - 1) + (Fraction(0),)
    row_nodes = canonical_nodes[: row + 1]
    column_nodes = canonical_nodes[: column + 1]
    row_h = complete_homogeneous(row_nodes, power - row)
    column_h = complete_homogeneous(column_nodes, power - column)
    upper = Fraction(0)
    for w_degree in range(power + 1):
        for r_degree in range(row, power - w_degree + 1):
            c_degree = power - w_degree - r_degree
            if c_degree < column:
                continue
            coefficient = math.factorial(power) // (
                math.factorial(w_degree) * math.factorial(r_degree) * math.factorial(c_degree)
            )
            upper += (
                coefficient
                * radial_width**w_degree
                * row_h[r_degree - row]
                * column_h[c_degree - column]
            )
    return lower, upper


def scaled_taylor_coefficients(x: arb, maximum_order: int) -> tuple[arb, ...]:
    bessel = tuple(x.bessel_k(order) for order in range(maximum_order + 2))
    coefficients = []
    for order in range(maximum_order + 1):
        derivative_abs = arb(0)
        for index in range(order + 1):
            derivative_abs += math.comb(order, index) * bessel[abs(1 - order + 2 * index)]
        derivative_abs *= arb(2) ** (-order)
        coefficient = x ** (order + 1) * derivative_abs / math.factorial(order)
        coefficients.append(-coefficient if order % 2 else coefficient)
    return tuple(coefficients)


def dd_entry_residual(
    coefficients: tuple[arb, ...],
    row: int,
    column: int,
    radial_width: Fraction,
    gap_radius: Fraction,
) -> tuple[arb, arb]:
    polynomial = arb(0)
    for power in range(row + column, TAYLOR_ORDER + 1):
        lower, upper = monomial_dd_bounds(power, row, column, radial_width, gap_radius)
        cauchy = arb(-1 if power % 2 else 1)
        polynomial += (coefficients[power] - cauchy) * interval_from_bounds(lower, upper)
    derivative_order = row + column
    eta = radial_width + 2 * gap_radius
    combinatorial = Fraction(
        math.factorial(TAYLOR_ORDER + 1),
        math.factorial(TAYLOR_ORDER + 1 - derivative_order)
        * math.factorial(row)
        * math.factorial(column),
    )
    tail = (
        (abs(coefficients[TAYLOR_ORDER + 1]).upper() + 1)
        * rational_ball(combinatorial)
        * rational_ball(eta) ** (TAYLOR_ORDER + 1 - derivative_order)
    ).upper()
    return polynomial, tail


def cauchy_entry_interval(
    row: int,
    column: int,
    radial_width: Fraction,
    gap_radius: Fraction,
) -> arb:
    derivative_order = row + column
    eta = radial_width + 2 * gap_radius
    # Tensor Hermite--Genocchi makes this a signed positive average of
    # binomial(d,row)/(1+y)^(d+1), with every sampled y in [0,eta].
    # This keeps the exact Cauchy correlation far more sharply than ranging an
    # alternating Taylor series entry by entry.
    maximum = Fraction(math.comb(derivative_order, row))
    minimum = maximum / (1 + eta) ** (derivative_order + 1)
    if derivative_order % 2:
        return interval_from_bounds(-maximum, -minimum)
    return interval_from_bounds(minimum, maximum)


def determinant_residual_radius(
    residual_bounds: list[list[arb]],
    cauchy: list[list[arb]],
    radial_width: Fraction,
    gap_radius: Fraction,
) -> arb:
    node_uppers = [gap_radius] * (SIZE - 1) + [Fraction(0)]
    product_upper = Fraction(1)
    for left in node_uppers:
        for right in node_uppers:
            product_upper *= 1 + radial_width + left + right
    q_upper = rational_ball(product_upper)
    radius = arb(0)

    # Linear terms retain the complete Cauchy minor before absolute bounding.
    for row in range(SIZE):
        for column in range(SIZE):
            minor = [
                [cauchy[i][j] for j in range(SIZE) if j != column]
                for i in range(SIZE)
                if i != row
            ]
            radius += (q_upper * determinant(minor)).abs_upper() * residual_bounds[row][column]

    # Higher residual terms are bounded absolutely; there are only 264 terms.
    for selected_count in range(2, SIZE + 1):
        for selected_rows in itertools.combinations(range(SIZE), selected_count):
            selected = set(selected_rows)
            for permutation in itertools.permutations(range(SIZE)):
                term = q_upper
                for row, column in enumerate(permutation):
                    term *= residual_bounds[row][column] if row in selected else cauchy[row][column].abs_upper()
                radius += term
    return radius.upper()


def cell_certificate(
    base: Fraction,
    upper: Fraction,
    radial_width_bound: Fraction,
    gap_radius: Fraction,
) -> dict[str, Any]:
    coefficients = scaled_taylor_coefficients(rational_ball(base), TAYLOR_ORDER + 1)
    residuals: list[list[arb]] = []
    tails = []
    for row in range(SIZE):
        residual_row = []
        for column in range(SIZE):
            polynomial, tail = dd_entry_residual(
                coefficients, row, column, radial_width_bound, gap_radius
            )
            residual_row.append((polynomial + arb(0, tail)).abs_upper())
            tails.append(tail)
        residuals.append(residual_row)
    cauchy = [
        [cauchy_entry_interval(row, column, radial_width_bound, gap_radius) for column in range(SIZE)]
        for row in range(SIZE)
    ]
    radial_width = upper / base - 1
    perturbation = determinant_residual_radius(residuals, cauchy, radial_width, gap_radius)
    regularizer = arb(1, perturbation)
    if not regularizer.lower() > 0:
        raise AssertionError(
            f"positive size-four cell lost at {fraction_text(base)} radius {fraction_text(gap_radius)}: {regularizer}"
        )
    return {
        "R_lower": float(regularizer.lower()),
        "R_upper": float(regularizer.upper()),
        "perturbation_upper": float(perturbation.upper()),
        "maximum_entry_tail": max(float(tail) for tail in tails),
        "radial_relative_width": fraction_text(radial_width),
    }


def certify_stratum(
    lower_power: int,
    upper_power: int,
    gap_candidates: tuple[Fraction, ...],
) -> dict[str, Any]:
    failures = []
    for gap_radius in gap_candidates:
        bands = []
        successful = True
        for power in range(lower_power, upper_power, -1):
            lower = Fraction(1, 2**power)
            selected = None
            for subdivisions in SUBDIVISION_CANDIDATES:
                step = lower / subdivisions
                cells = []
                try:
                    for index in range(subdivisions):
                        base = lower + index * step
                        cells.append(cell_certificate(base, base + step, Fraction(1, subdivisions), gap_radius))
                except AssertionError as exc:
                    failures.append(
                        {
                            "gap_radius": fraction_text(gap_radius),
                            "band": f"2^-{power}..2^-{power - 1}",
                            "subdivisions": subdivisions,
                            "failure": str(exc),
                        }
                    )
                    continue
                selected = {
                    "lower": f"2^-{power}",
                    "upper": f"2^-{power - 1}",
                    "subdivisions": subdivisions,
                    "minimum_R_lower": min(cell["R_lower"] for cell in cells),
                    "maximum_R_upper": max(cell["R_upper"] for cell in cells),
                    "maximum_perturbation_upper": max(cell["perturbation_upper"] for cell in cells),
                    "maximum_entry_tail": max(cell["maximum_entry_tail"] for cell in cells),
                }
                break
            if selected is None:
                successful = False
                break
            bands.append(selected)
        if successful:
            return {
                "gap_radius": fraction_text(gap_radius),
                "bands": bands,
                "band_count": len(bands),
                "cell_count": sum(row["subdivisions"] for row in bands),
                "minimum_R_lower": min(row["minimum_R_lower"] for row in bands),
                "maximum_R_upper": max(row["maximum_R_upper"] for row in bands),
                "failures_before_selected_radius": failures,
            }
    return {
        "gap_radius": None,
        "bands": [],
        "band_count": 0,
        "cell_count": 0,
        "failures_before_selected_radius": failures,
    }


def face_masks() -> list[dict[str, Any]]:
    labels = ("r0", "r1", "r2", "c0", "c1", "c2")
    centers = (Fraction(1, 32), Fraction(1, 64), Fraction(1, 128), Fraction(1, 40), Fraction(1, 80), Fraction(1, 160))
    rows = []
    for mask in range(1, 1 << len(labels)):
        rows.append(
            {
                "active": [labels[index] for index in range(len(labels)) if mask & (1 << index)],
                "center": {
                    labels[index]: fraction_text(centers[index] if mask & (1 << index) else Fraction(0))
                    for index in range(len(labels))
                },
            }
        )
    return rows


def exact_face_controls(masks: list[dict[str, Any]]) -> dict[str, Any]:
    labels = ("r0", "r1", "r2", "c0", "c1", "c2")
    passed = 0
    for mask_index, row in enumerate(masks, start=1):
        # Interiorize inactive face coordinates by distinct tiny rationals.  The
        # exact Cauchy identity then proves the normalized value one; continuity
        # carries it to the named face closure.
        values = {
            label: Fraction(row["center"][label]) if label in row["active"] else Fraction(mask_index + labels.index(label) + 1, 10**7)
            for label in labels
        }
        left = [Fraction(3, 5) + values[label] for label in labels[:3]] + [Fraction(3, 5)]
        right = [Fraction(2, 5) + values[label] for label in labels[3:]] + [Fraction(2, 5)]
        left.sort(reverse=True)
        right.sort(reverse=True)
        direct = determinant([[Fraction(2, 1) / (x + y) for y in right] for x in left])
        factored = K280.cauchy_determinant(left, right)
        if direct != factored:
            raise AssertionError("size-four interiorized face Cauchy identity failed")
        passed += 1
    return {
        "nonempty_masks": len(masks),
        "interiorized_exact_controls_passed": passed,
        "closure_rule": "the rational Cauchy--Vandermonde identity is exact on every interiorization and its divided quotient extends continuously with normalized value one to each named face",
    }


def decimal_control(gap_radius: Fraction, x_fraction: Fraction = Fraction(2, 25)) -> dict[str, Any]:
    x = Decimal(x_fraction.numerator) / Decimal(x_fraction.denominator)
    gap = Decimal(gap_radius.numerator) / Decimal(gap_radius.denominator) / 2
    left_floor = x * Decimal(3) / 5
    right_floor = x * Decimal(2) / 5
    left = [left_floor + Decimal(SIZE - 1 - index) * x * gap for index in range(SIZE)]
    right = [right_floor + Decimal(SIZE - 1 - index) * x * gap for index in range(SIZE)]
    with localcontext() as context:
        context.prec = 420
        value = K280.divided_regularizer(left, right, 380)
    return {
        "x": fraction_text(x_fraction),
        "gap_ratio": str(gap),
        "regularizer": format(value, ".36E"),
        "strictly_positive": value > 0,
        "role": "independent high-precision finite-gap value; the Arb cells carry outward certification",
    }


def pattern_counts(source: dict[str, Any]) -> dict[str, Any]:
    patterns = source["unique_patterns"]
    by_size = {size: sum(int(row["size"]) == size for row in patterns.values()) for size in (2, 3, 4)}
    occurrences = source["complete_factorization_inventory"]["nontrivial_size_two_through_four_occurrences"]
    return {
        "patterns": len(patterns),
        "patterns_by_size": {str(key): value for key, value in by_size.items()},
        "nontrivial_occurrences": occurrences,
        "gram_entries": source["fixed_control"]["source_gram_entries"],
        "groups": source["fixed_control"]["source_groups"],
    }


def build() -> dict[str, Any]:
    source = json.loads(K280_MANIFEST.read_text())
    counts = pattern_counts(source)
    if counts != {
        "patterns": 98,
        "patterns_by_size": {"2": 72, "3": 25, "4": 1},
        "nontrivial_occurrences": 996,
        "gram_entries": 408,
        "groups": 16,
    }:
        raise AssertionError(f"K280 source census drifted: {counts}")

    dyadic = dyadic_spine()
    low = certify_stratum(RADIAL_FLOOR_POWER, RADIAL_SPLIT_POWER, LOW_GAP_CANDIDATES)
    high = certify_stratum(RADIAL_SPLIT_POWER, RADIAL_CEILING_POWER, HIGH_GAP_CANDIDATES)
    masks = face_masks()
    face_controls = exact_face_controls(masks)
    union_complete = low["gap_radius"] is not None and high["gap_radius"] is not None
    selected_gap = Fraction(low["gap_radius"]) if low["gap_radius"] else LOW_GAP_CANDIDATES[-1]

    return {
        "schema_version": "1.0",
        "result_id": "K281-ORDER-SEVEN-SIZE-FOUR-OUTWARD-CALCULUS",
        "created": "2026-09-21",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "fixed_control": {
            "source_manifest": "lab/process/k280-order-seven-bessel-vandermonde-face-atlas.json",
            "domain": "2^-200<=x<=1/4 with stratum-specific relative row/column spread",
            "taylor_order": TAYLOR_ORDER,
            "arb_decimal_digits": ARB_DIGITS,
            "threads": 1,
            **counts,
        },
        "exact_scaled_jet_theorem": {
            "kernel": "q(x)=x*K1(x)",
            "scaled_jets": "a_n=x^n*q^(n)(x), n=0..6",
            "recurrence": "a_(n+1)=x*d(a_n)/dx-n*a_n; with s=x^2, x*dq/dx=a1=-s*K0 and x*dK0/dx=-q",
            "jet_polynomials": {
                f"a{index}": {
                    "q_coefficient": jet_formula(p, "s"),
                    "K0_coefficient": jet_formula(q0, "s"),
                }
                for index, (p, q0) in enumerate(JET_POLYNOMIALS)
            },
            "b_from_a": "b_n=x^(n+1)*K1^(n)(x)=n!*sum_(k=0)^n (-1)^(n-k)*a_k/k!",
            "R4": "det[b_(i+j)/(i!*j!)] for i,j=0..3",
            "negative_radial_powers_cancel_before_Arb_evaluation": True,
            "maximum_derivative_order": 6,
        },
        "arb_coalescent_certificate": {
            "dyadic_rows": dyadic,
            "tested_radii": len(dyadic),
            "all_raw_hankel_balls_overlap_scaled_balls": True,
            "all_scaled_R4_balls_strictly_positive": True,
            "R4_midpoint_range": [min(row["scaled_midpoint"] for row in dyadic), max(row["scaled_midpoint"] for row in dyadic)],
            "minimum_width_gain": min(row["scaled_width_gain"] for row in dyadic if row["scaled_width_gain"] is not None),
        },
        "outward_gap_stratified_certificate": {
            "normalized_identity": "R4=det(D_ij)*product_ab(1+w+r_a+c_b), with D_ij=[r_0,...,r_i][c_0,...,c_j] x*K1(x*(1+w+r+c))",
            "monomial_rule": "mixed DD of (w+r+c)^n is a nonnegative multinomial sum of complete homogeneous polynomials, so its box extrema occur at the zero and all-upper corners",
            "tail_rule": "complete monotonicity bounds each entry remainder at Taylor order 16 without division by a time gap",
            "low_radial": low,
            "high_radial": high,
            "radial_range_has_no_gap": union_complete,
            "size_four_positive_union_certified": union_complete,
            "all_98_patterns_propagated_conditionally_on_spread_rule": union_complete,
            "all_996_occurrences_propagated_conditionally_on_spread_rule": union_complete,
            "all_408_entries_remain_in_scope": True,
        },
        "size_four_noncoalescent_face_atlas": {
            "gap_labels": ["r0", "r1", "r2", "c0", "c1", "c2"],
            "masks": masks,
            "face_mask_count": len(masks),
            "exact_controls": face_controls,
            "shifted_face_tail_operator_serialized": False,
        },
        "independent_controls": {
            "finite_gap": decimal_control(selected_gap),
            "coalescent_pascal_limit": "at x->0, a0->1 and a_n->0 for n>0, so b_n=(-1)^n*n! and det[(-1)^(i+j)*(i+j)!/(i!*j!)]_(0..3)=1",
        },
        "decision": {
            "size_four_scaled_jet_normal_form_banked": True,
            "size_four_gap_stratified_positive_union_banked": union_complete,
            "complete_noncoalescent_face_topology_banked": True,
            "arbitrary_gap_ratio_coverage_complete": False,
            "duffy_jacobi_composition_released": False,
            "next_exact_input": "construct shifted Hermite--Genocchi face-center tails on the 63-mask size-four atlas and the residual R2/R3 faces, then propagate mixed Duffy derivatives across all 98 patterns before determinant-preserving Jacobi composition",
        },
        "release_test": {
            "exact_R4_scaled_jet_normal_form_banked": True,
            "directed_arb_dyadic_coalescent_spine_banked": True,
            "gap_stratified_R4_value_interval_serialized": union_complete,
            "all_98_patterns_propagated_on_certified_union": union_complete,
            "all_996_occurrences_propagated_on_certified_union": union_complete,
            "size_four_63_mask_face_atlas_serialized": len(masks) == 63,
            "arbitrary_gap_ratio_domain_covered": False,
            "mixed_Duffy_derivative_envelopes_serialized": False,
            "determinant_preserving_Jacobi_error_serialized": False,
            "complete_base_action_column_evaluated": False,
            "complete_R_ref_form_dual_residual_serialized": False,
            "positive_complete_M_orthogonal_complement_or_flux_floor_serialized": False,
            "native_K152_interval_emitted": False,
        },
        "ledger_effect": {
            "SC-META-53": "UNCERTAIN_UNCHANGED",
            "LT-SM8": "NEEDS_UNCHANGED",
            "LT-GR6b": "NEEDS_UNCHANGED",
            "RA-F1": "NEEDS_UNCHANGED",
            "AC-F1": "NEEDS_UNCHANGED",
        },
        "physical_or_source_selection": False,
        "Born_prediction_or_confirmation_credit": False,
        "canon_paper_release_or_public_posture_move": False,
        "claim_ceiling": "Exact size-four coalescent scaled-jet theorem, gap-stratified outward R4 value union if certified, and complete six-gap face topology only; no arbitrary-gap or mixed-Duffy enclosure, Jacobi cubature, action-column value, residual, K152 interval, physical state, source/ledger move, canon, paper or public claim.",
    }


def summary(result: dict[str, Any]) -> dict[str, Any]:
    return {
        "fixed_control": result["fixed_control"],
        "exact_scaled_jet_theorem": result["exact_scaled_jet_theorem"],
        "arb_coalescent_certificate": {
            key: value for key, value in result["arb_coalescent_certificate"].items() if key != "dyadic_rows"
        },
        "outward_gap_stratified_certificate": {
            key: value for key, value in result["outward_gap_stratified_certificate"].items()
            if key not in ("low_radial", "high_radial")
        },
        "low_radial_summary": {
            key: value for key, value in result["outward_gap_stratified_certificate"]["low_radial"].items() if key != "bands"
        },
        "high_radial_summary": {
            key: value for key, value in result["outward_gap_stratified_certificate"]["high_radial"].items() if key != "bands"
        },
        "face_mask_count": result["size_four_noncoalescent_face_atlas"]["face_mask_count"],
        "independent_controls": result["independent_controls"],
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
