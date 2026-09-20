#!/usr/bin/env python3
"""K262: certify the zero-through-three high-multiplicity K218 union.

The six exceptional axes 2..7 are exchangeable.  For multiplicities zero,
one, and three this producer integrates the exact K230 orbit representation on
the complete S6-invariant union.  Multiplicities zero and one use a signed
degree-four head; multiplicity three uses degree six.  All omitted degrees are
bounded by a complete-homogeneous geometric tail.  K261 supplies the disjoint
exact-two layer.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations, combinations_with_replacement
import json
from math import comb, factorial

from flint import arb, ctx, fmpq

from k225_order_six_diagonal_cancellation import K185, ROOT, terms
from k242_order_six_third_shell_signed_taylor import orbit_groups


K218 = ROOT / "lab/process/k218-order-six-exact-angular-elimination.json"
K230 = ROOT / "lab/process/k230-order-six-permutation-projection.json"
K247 = ROOT / "lab/process/k247-order-six-cumulative-q15-boundary.json"
K261 = ROOT / "lab/process/k261-order-six-all-pair-box-taylor-integral.json"
OUT = ROOT / "lab/process/k262-order-six-low-through-three-high-multiplicity-integral.json"

LOW_Q = (Q(1), Q(13, 5))
HIGH_Q = (Q(1792), Q(2304))
LAYER_ORDERS = {0: 4, 1: 4, 3: 6}
NEW_LAYERS_UPPER = Q(244, 10**22)  # 2.44e-20
ENLARGED_UNION_NEGATIVE_LOWER = Q(186, 10**22)  # 1.86e-20
PREFIX_COMPOSITION_NEGATIVE_LOWER = Q(172, 10**22)  # 1.72e-20
PI_LOWER = Q(31, 10)
PI_UPPER = Q(22, 7)
PRECISION = 256
ZERO_EXPONENT = (0,) * 8


def rational_row(value: Q) -> dict:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "decimal": f"{float(value):.12e}",
    }


def as_arb(value: Q | fmpq) -> arb:
    if isinstance(value, Q):
        return arb(value.numerator) / value.denominator
    return arb(value)


def cosh_log(q: Q) -> Q:
    return (q + 1 / q) / 2


def sinh_log(q: Q) -> Q:
    return (q - 1 / q) / 2


def box_center_and_radius(bounds: tuple[Q, Q]) -> tuple[Q, Q]:
    lo, hi = (cosh_log(value) for value in bounds)
    return (lo + hi) / 2, (hi - lo) / 2


def cosh_power_integrals(bounds: tuple[Q, Q], maximum_power: int) -> list[arb]:
    q_lo, q_hi = bounds
    c_lo, c_hi = cosh_log(q_lo), cosh_log(q_hi)
    s_lo, s_hi = sinh_log(q_lo), sinh_log(q_hi)
    values = [arb(q_hi.numerator).log() - arb(q_hi.denominator).log()
              - arb(q_lo.numerator).log() + arb(q_lo.denominator).log()]
    values.append(as_arb(s_hi - s_lo))
    for n in range(2, maximum_power + 1):
        boundary = (s_hi * c_hi ** (n - 1) - s_lo * c_lo ** (n - 1)) / n
        values.append(as_arb(boundary) + arb(n - 1) / n * values[n - 2])
    return values


def centered_moments(bounds: tuple[Q, Q], center: Q, order: int) -> tuple[arb, ...]:
    powers = cosh_power_integrals(bounds, order + 1)
    result = []
    for exponent in range(order + 1):
        value = arb(0)
        for k in range(exponent + 1):
            coefficient = Q(comb(exponent, k)) * (-center) ** (exponent - k)
            value += as_arb(coefficient) * powers[k + 1]
        result.append(value)
    return tuple(result)


def add_exponents(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a + b for a, b in zip(left, right))


def multiply_polynomials(left: list[dict], right: list[dict], order: int) -> list[dict]:
    result = [{} for _ in range(order + 1)]
    for left_degree, left_terms in enumerate(left):
        for right_degree, right_terms in enumerate(right):
            degree = left_degree + right_degree
            if degree > order:
                continue
            target = result[degree]
            for left_exp, left_value in left_terms.items():
                for right_exp, right_value in right_terms.items():
                    exponent = add_exponents(left_exp, right_exp)
                    target[exponent] = target.get(exponent, arb(0)) + left_value * right_value
    return result


def multinomial(exponents: tuple[int, ...]) -> int:
    value = factorial(sum(exponents))
    for exponent in exponents:
        value //= factorial(exponent)
    return value


def reciprocal_factor_polynomial(row: int, centers: tuple[Q, ...], order: int) -> list[dict]:
    support = tuple(axis for axis in range(8) if row & (1 << axis))
    base = Q(256) + sum((centers[axis] for axis in support), Q())
    result = []
    for degree in range(order + 1):
        terms_by_exponent = {}
        for selection in combinations_with_replacement(support, degree):
            exponents = [0] * 8
            for axis in selection:
                exponents[axis] += 1
            exponent = tuple(exponents)
            coefficient = Q((-1) ** degree * multinomial(exponent), 1) / base ** (degree + 1)
            terms_by_exponent[exponent] = as_arb(coefficient)
        result.append(terms_by_exponent)
    return result


def integrate_polynomial(polynomial: list[dict], moments: tuple[tuple[arb, ...], ...]) -> list[arb]:
    by_degree = []
    for terms_by_exponent in polynomial:
        value = arb(0)
        for exponents, coefficient in terms_by_exponent.items():
            term = coefficient
            for axis, exponent in enumerate(exponents):
                term *= moments[axis][exponent]
            value += term
        by_degree.append(value)
    return by_degree


def complete_homogeneous(ratios: tuple[Q, ...], degree: int) -> Q:
    coefficients = [Q(1)] + [Q()] * degree
    for ratio in ratios:
        updated = [Q()] * (degree + 1)
        power = Q(1)
        for k in range(degree + 1):
            for prior_degree in range(degree + 1 - k):
                updated[k + prior_degree] += coefficients[prior_degree] * power
            power *= ratio
        coefficients = updated
    return coefficients[degree]


def rational_tail(rows: tuple[int, ...], centers: tuple[Q, ...], radii: tuple[Q, ...],
                  tail_start: int) -> Q:
    base_product = Q(1)
    ratios = []
    for row in rows:
        support = tuple(axis for axis in range(8) if row & (1 << axis))
        base = Q(256) + sum((centers[axis] for axis in support), Q())
        deviation = sum((radii[axis] for axis in support), Q())
        base_product *= base
        ratios.append(deviation / base)
    h_start = complete_homogeneous(tuple(ratios), tail_start)
    ratio_ceiling = max(ratios) * Q(tail_start + 14, tail_start + 1)
    assert ratio_ceiling < 1
    return h_start / base_product / (1 - ratio_ceiling)


def layer_digest(records: list[dict]) -> str:
    return sha256(json.dumps(records, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def generate_layer(groups: dict, multiplicity: int, order: int,
                   normalization_lower: fmpq, normalization_upper: fmpq) -> dict:
    low_center, low_radius = box_center_and_radius(LOW_Q)
    high_center, high_radius = box_center_and_radius(HIGH_Q)
    low_moments = centered_moments(LOW_Q, low_center, order)
    high_moments = centered_moments(HIGH_Q, high_center, order)
    low_measure = sinh_log(LOW_Q[1]) - sinh_log(LOW_Q[0])
    high_measure = sinh_log(HIGH_Q[1]) - sinh_log(HIGH_Q[0])
    complete_head = [arb(0) for _ in range(order + 1)]
    complete_tail = Q()
    records = []
    for subset in combinations(range(2, 8), multiplicity):
        active = frozenset((1,) + subset)
        centers = tuple(high_center if axis in active else low_center for axis in range(8))
        radii = tuple(high_radius if axis in active else low_radius for axis in range(8))
        moments = tuple(high_moments if axis in active else low_moments for axis in range(8))
        factor_cache = {
            row: reciprocal_factor_polynomial(row, centers, order)
            for row in range(256)
        }
        box_head = [arb(0) for _ in range(order + 1)]
        box_tail = Q()
        for rows, weight in groups.items():
            polynomial = [{ZERO_EXPONENT: arb(1)}] + [{} for _ in range(order)]
            for row in rows:
                polynomial = multiply_polynomials(polynomial, factor_cache[row], order)
            integrated = integrate_polynomial(polynomial, moments)
            for degree, value in enumerate(integrated):
                box_head[degree] += weight * value
            box_tail += abs(weight) * rational_tail(rows, centers, radii, order + 1)
        box_measure = high_measure ** (1 + multiplicity) * low_measure ** (7 - multiplicity)
        box_tail *= box_measure
        for degree, value in enumerate(box_head):
            complete_head[degree] += value
        complete_tail += box_tail
        records.append({
            "high_exceptional_axes": list(subset),
            "raw_head_by_degree": [str(value) for value in box_head],
            "raw_absolute_tail_upper": str(box_tail),
        })
    raw_head = sum(complete_head, arb(0))
    raw_lower = raw_head.lower() - as_arb(complete_tail)
    raw_upper = raw_head.upper() + as_arb(complete_tail)
    normalized_head_lower_scale = arb(normalization_lower) * raw_head
    normalized_head_upper_scale = arb(normalization_upper) * raw_head
    normalized_tail = arb(normalization_upper) * as_arb(complete_tail)
    normalized_lower = (
        arb(normalization_lower) * raw_lower
        if raw_lower >= 0 else arb(normalization_upper) * raw_lower
    )
    normalized_upper = (
        arb(normalization_upper) * raw_upper
        if raw_upper >= 0 else arb(normalization_lower) * raw_upper
    )
    absolute_upper = max(-normalized_lower.lower(), normalized_upper.upper())
    return {
        "multiplicity": multiplicity,
        "boxes": len(records),
        "total_degree_inclusive": order,
        "tail_starts_at_degree": order + 1,
        "box_records": records,
        "box_record_sha256": layer_digest(records),
        "complete_raw_head_by_degree": [str(value) for value in complete_head],
        "complete_raw_head": str(raw_head),
        "complete_raw_absolute_tail_upper": str(complete_tail),
        "complete_raw_integral_interval": {"lower": str(raw_lower), "upper": str(raw_upper)},
        "normalized_signed_head_at_lower_normalization": str(normalized_head_lower_scale),
        "normalized_signed_head_at_upper_normalization": str(normalized_head_upper_scale),
        "normalized_absolute_tail_upper": str(normalized_tail),
        "normalized_integral_interval": {"lower": str(normalized_lower), "upper": str(normalized_upper)},
        "normalized_absolute_integral_upper": str(absolute_upper),
    }


def generate() -> dict:
    ctx.prec = PRECISION
    source = json.loads(K185.read_text())
    items = list(terms(source))
    groups = orbit_groups(items)
    assert len(items) == 1864 and len(groups) == 307
    projection = json.loads(K230.read_text())
    compact = ";".join(
        ",".join(map(str, rows)) + ":" + str(weight)
        for rows, weight in sorted(groups.items())
    )
    assert sha256(compact.encode()).hexdigest() == projection["orbit_coefficient_manifest_sha256"]

    normalization_lower = fmpq(2**8 * 256**6, factorial(5)) * fmpq(7, 22) ** 8
    normalization_upper = fmpq(2**8 * 256**6, factorial(5)) * fmpq(10, 31) ** 8
    layers = [generate_layer(groups, multiplicity, order, normalization_lower, normalization_upper)
              for multiplicity, order in LAYER_ORDERS.items()]
    by_multiplicity = {row["multiplicity"]: row for row in layers}
    m3_lower = arb(by_multiplicity[3]["normalized_integral_interval"]["lower"])
    assert m3_lower > 0
    new_upper = sum((arb(by_multiplicity[m]["normalized_absolute_integral_upper"])
                     for m in (0, 1, 3)), arb(0))
    assert new_upper < as_arb(NEW_LAYERS_UPPER)

    k261 = json.loads(K261.read_text())
    k261_declared = k261["certificate"]["declared_strict_negative_mass_lower"]
    k261_lower = Q(k261_declared["numerator"], k261_declared["denominator"])
    enlarged_lower = k261_lower - NEW_LAYERS_UPPER
    assert enlarged_lower == ENLARGED_UNION_NEGATIVE_LOWER
    prefix = json.loads(K247.read_text())["certificate"]["complete_upper"]
    prefix_upper = Q(prefix["numerator"], prefix["denominator"])
    composition_margin = enlarged_lower - prefix_upper
    assert composition_margin > PREFIX_COMPOSITION_NEGATIVE_LOWER

    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "conditional_internal_structure_not_forward_physics_credit",
        "input_sha256": {
            path.stem.split("-")[0]: sha256(path.read_bytes()).hexdigest()
            for path in (K185, K218, K230, K247, K261)
        },
        "object": (
            "The exact K218 signed integral on the 42-box S6-invariant disjoint union "
            "with fixed high axis 1, fixed low axis 0, and zero through three high "
            "exceptional coordinates among axes 2..7"
        ),
        "domain": {
            "fixed_high_axis": 1,
            "fixed_low_axis": 0,
            "exceptional_axes": list(range(2, 8)),
            "included_high_multiplicities": [0, 1, 2, 3],
            "high_q_interval": list(map(str, HIGH_Q)),
            "low_q_interval": list(map(str, LOW_Q)),
            "boxes": sum(comb(6, multiplicity) for multiplicity in range(4)),
            "pairwise_disjoint": True,
            "s6_invariant_union": True,
            "exact_two_layer_ref": "lab/process/k261-order-six-all-pair-box-taylor-integral.json",
        },
        "projection": {
            "raw_signed_terms": len(items),
            "retained_exact_s6_orbits": len(groups),
            "orbit_manifest_sha256": projection["orbit_coefficient_manifest_sha256"],
            "rule": (
                "K230 proves integral equality on every S6-invariant domain. Each complete "
                "multiplicity union is invariant; unequal functions outside one exact orbit "
                "identity are never netted."
            ),
        },
        "new_multiplicity_layers": layers,
        "certificate": {
            "normalization_lower_using_pi_less_than_22_over_7": str(normalization_lower),
            "normalization_upper_using_pi_greater_than_31_over_10": str(normalization_upper),
            "normalization_direction_rule": (
                "Negative-mass lower bounds use pi<22/7. Positive and absolute upper "
                "bounds, tail uppers, and negative lower endpoints use pi>31/10."
            ),
            "computed_new_layers_absolute_upper": str(new_upper),
            "declared_new_layers_absolute_upper": rational_row(NEW_LAYERS_UPPER),
            "k261_exact_two_negative_mass_lower": rational_row(k261_lower),
            "declared_enlarged_union_negative_mass_lower": rational_row(enlarged_lower),
            "result": "strictly_negative_complete_zero_through_three_high_multiplicity_union",
        },
        "composition": {
            "k247_complete_positive_prefix_upper": rational_row(prefix_upper),
            "computed_negative_excess_over_k247_upper": rational_row(composition_margin),
            "declared_negative_excess_over_k247_upper": rational_row(PREFIX_COMPOSITION_NEGATIVE_LOWER),
            "result": (
                "the exact 42-box multiplicity-zero-through-three union and the disjoint "
                "K247 q<=15 prefix have strictly negative combined integral"
            ),
        },
        "controls": (
            "An independent reverse-order raw-allocation probe reconstructs the orbit manifest, "
            "exact degree-zero heads and complete tails, checks two- and three-point product "
            "quadratures, and applies absolute-weight, wrong-measure, multiplicity-deletion and "
            "non-invariant-single-box controls."
        ),
        "source_routing": (
            "SC-ACT-01/02 ASSERTS and SC-META-53 UNCERTAIN remain unchanged; "
            "LT-GR6b/LT-SM8/RA-F1/AC-F1 remain NEEDS."
        ),
        "decision": (
            "K261's negative exact-two layer dominates the complete adjacent zero-, one-, and "
            "three-high layers. The remaining multiplicity-four-through-six complement needs a "
            "new global sign balance because the multiplicity-four signed head is already positive "
            "and larger than K261's conservative negative lower."
        ),
        "claim_ceiling": (
            "Exact sign and negative-mass lower bound only on the declared 42-box union, plus its "
            "K247 composition. No multiplicity-four-through-six complement, full-K218 sign, "
            "complete original order-six error, K215 impossibility, source/ledger/canon/paper/"
            "public-posture change, or physical-positivity conclusion."
        ),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K262", result["certificate"]["result"])
    print("[PASS] K262 new layers upper", result["certificate"]["declared_new_layers_absolute_upper"]["decimal"])
    print("[PASS] K262 enlarged negative lower", result["certificate"]["declared_enlarged_union_negative_mass_lower"]["decimal"])
    print("[PASS] K262 K247 excess", result["composition"]["declared_negative_excess_over_k247_upper"]["decimal"])
