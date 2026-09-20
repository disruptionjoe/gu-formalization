#!/usr/bin/env python3
"""K261: certify the complete fifteen-pair-box integral by a signed Taylor head.

The all-pair domain is S6 invariant.  K230 therefore permits exact orbit
cancellation before integration.  On each of the fifteen boxes this producer
reanchors every retained rational denominator function at the exact low/high
box centers, integrates the complete signed total-degree-four head against
exact product-cosh moments, and bounds every degree five and higher by one
positive complete-homogeneous tail.
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
K260 = ROOT / "lab/process/k260-order-six-integrated-pair-box-certificate.json"
OUT = ROOT / "lab/process/k261-order-six-all-pair-box-taylor-integral.json"

ORDER = 4
TAIL_START = ORDER + 1
LOW_Q = (Q(1), Q(13, 5))
HIGH_Q = (Q(1792), Q(2304))
ALL_PAIRS = tuple(combinations(range(2, 8), 2))
NEGATIVE_MASS_LOWER = Q(43, 10**21)  # 4.3e-20
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
    """Return integral cosh(t)^n dt for n=0..maximum_power."""
    q_lo, q_hi = bounds
    c_lo, c_hi = cosh_log(q_lo), cosh_log(q_hi)
    s_lo, s_hi = sinh_log(q_lo), sinh_log(q_hi)
    values = [arb(Q(q_hi / q_lo).numerator).log() - arb(Q(q_hi / q_lo).denominator).log()]
    values.append(as_arb(s_hi - s_lo))
    for n in range(2, maximum_power + 1):
        boundary = (s_hi * c_hi ** (n - 1) - s_lo * c_lo ** (n - 1)) / n
        values.append(as_arb(boundary) + arb(n - 1) / n * values[n - 2])
    return values


def centered_product_cosh_moments(bounds: tuple[Q, Q], center: Q) -> list[arb]:
    """Return integral cosh(t)(cosh(t)-center)^e dt, e=0..ORDER."""
    powers = cosh_power_integrals(bounds, ORDER + 1)
    result = []
    for exponent in range(ORDER + 1):
        value = arb(0)
        for k in range(exponent + 1):
            coefficient = Q(comb(exponent, k)) * (-center) ** (exponent - k)
            value += as_arb(coefficient) * powers[k + 1]
        result.append(value)
    return result


def add_exponents(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a + b for a, b in zip(left, right))


def multiply_polynomials(left: list[dict], right: list[dict]) -> list[dict]:
    result = [{} for _ in range(ORDER + 1)]
    for left_degree, left_terms in enumerate(left):
        for right_degree, right_terms in enumerate(right):
            degree = left_degree + right_degree
            if degree > ORDER:
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


def reciprocal_factor_polynomial(row: int, centers: tuple[Q, ...]) -> list[dict]:
    support = tuple(axis for axis in range(8) if row & (1 << axis))
    base = Q(256) + sum((centers[axis] for axis in support), Q())
    result = []
    for degree in range(ORDER + 1):
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


def rational_tail(rows: tuple[int, ...], centers: tuple[Q, ...], radii: tuple[Q, ...]) -> Q:
    base_product = Q(1)
    ratios = []
    for row in rows:
        support = tuple(axis for axis in range(8) if row & (1 << axis))
        base = Q(256) + sum((centers[axis] for axis in support), Q())
        deviation = sum((radii[axis] for axis in support), Q())
        base_product *= base
        ratios.append(deviation / base)
    h_start = complete_homogeneous(tuple(ratios), TAIL_START)
    ratio_ceiling = max(ratios) * Q(TAIL_START + 14, TAIL_START + 1)
    assert ratio_ceiling < 1
    return h_start / base_product / (1 - ratio_ceiling)


def polynomial_digest(rows: list[dict]) -> str:
    payload = []
    for pair_row in rows:
        payload.append({
            "pair": pair_row["exceptional_pair"],
            "degree_head": pair_row["integrated_head_by_degree"],
            "tail": pair_row["raw_absolute_tail_upper"],
        })
    return sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def generate() -> dict:
    ctx.prec = PRECISION
    source = json.loads(K185.read_text())
    items = list(terms(source))
    groups = orbit_groups(items)
    assert len(items) == 1864 and len(groups) == 307 and len(ALL_PAIRS) == 15

    prior_projection = json.loads(K230.read_text())
    compact = ";".join(
        ",".join(map(str, rows)) + ":" + str(weight)
        for rows, weight in sorted(groups.items())
    )
    assert sha256(compact.encode()).hexdigest() == prior_projection["orbit_coefficient_manifest_sha256"]

    low_center, low_radius = box_center_and_radius(LOW_Q)
    high_center, high_radius = box_center_and_radius(HIGH_Q)
    low_moments = tuple(centered_product_cosh_moments(LOW_Q, low_center))
    high_moments = tuple(centered_product_cosh_moments(HIGH_Q, high_center))
    low_measure = sinh_log(LOW_Q[1]) - sinh_log(LOW_Q[0])
    high_measure = sinh_log(HIGH_Q[1]) - sinh_log(HIGH_Q[0])

    complete_head = [arb(0) for _ in range(ORDER + 1)]
    complete_tail = Q()
    pair_rows = []
    for pair in ALL_PAIRS:
        active = frozenset((1,) + pair)
        centers = tuple(high_center if axis in active else low_center for axis in range(8))
        radii = tuple(high_radius if axis in active else low_radius for axis in range(8))
        moments = tuple(high_moments if axis in active else low_moments for axis in range(8))
        factor_cache = {
            row: reciprocal_factor_polynomial(row, centers)
            for row in range(256)
        }
        pair_head = [arb(0) for _ in range(ORDER + 1)]
        pair_tail = Q()
        for rows, weight in groups.items():
            polynomial = [{ZERO_EXPONENT: arb(1)}] + [{} for _ in range(ORDER)]
            for row in rows:
                polynomial = multiply_polynomials(polynomial, factor_cache[row])
            integrated = integrate_polynomial(polynomial, moments)
            for degree, value in enumerate(integrated):
                pair_head[degree] += weight * value
            pair_tail += abs(weight) * rational_tail(rows, centers, radii)

        box_measure = high_measure ** 3 * low_measure ** 5
        pair_tail *= box_measure
        for degree, value in enumerate(pair_head):
            complete_head[degree] += value
        complete_tail += pair_tail
        pair_rows.append({
            "exceptional_pair": list(pair),
            "integrated_head_by_degree": [str(value) for value in pair_head],
            "raw_absolute_tail_upper": str(pair_tail),
        })

    raw_head = sum(complete_head, arb(0))
    raw_upper = raw_head.upper() + as_arb(complete_tail)
    raw_lower = raw_head.lower() - as_arb(complete_tail)
    assert raw_upper < 0 and raw_lower < raw_upper

    normalization_lower = fmpq(2**8 * 256**6, factorial(5)) * fmpq(7, 22) ** 8
    normalized_head = arb(normalization_lower) * raw_head
    normalized_tail = arb(normalization_lower) * as_arb(complete_tail)
    normalized_negative_mass = -arb(normalization_lower) * raw_upper
    assert normalized_negative_mass > as_arb(NEGATIVE_MASS_LOWER)

    prefix = json.loads(K247.read_text())["certificate"]["complete_upper"]
    prefix_upper = Q(prefix["numerator"], prefix["denominator"])
    cancellation_margin = NEGATIVE_MASS_LOWER - prefix_upper
    assert cancellation_margin > 0

    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "conditional_internal_structure_not_forward_physics_credit",
        "input_sha256": {
            path.stem.split("-")[0]: sha256(path.read_bytes()).hexdigest()
            for path in (K185, K218, K230, K247, K260)
        },
        "object": (
            "The exact K218 signed integral on the S6-invariant disjoint union of all fifteen "
            "K259/K260 exceptional-pair boxes, including product-cosh measure and pi^-8 normalization"
        ),
        "domain": {
            "fixed_high_axis": 1,
            "exceptional_pairs": [list(pair) for pair in ALL_PAIRS],
            "high_q_interval": list(map(str, HIGH_Q)),
            "low_q_interval": list(map(str, LOW_Q)),
            "boxes": len(ALL_PAIRS),
            "pairwise_disjoint": True,
            "s6_invariant_union": True,
        },
        "projection": {
            "raw_signed_terms": len(items),
            "retained_exact_s6_orbits": len(groups),
            "orbit_manifest_sha256": prior_projection["orbit_coefficient_manifest_sha256"],
            "rule": (
                "K230 proves integral equality on every S6-invariant domain. Exact orbit-coefficient "
                "cancellation is therefore applied before integration; unequal functions outside one "
                "exact orbit identity are never netted."
            ),
        },
        "reanchored_integral": {
            "precision_bits": PRECISION,
            "total_degree_inclusive": ORDER,
            "tail_starts_at_degree": TAIL_START,
            "low_c_center": str(low_center),
            "high_c_center": str(high_center),
            "pair_records": pair_rows,
            "pair_record_sha256": polynomial_digest(pair_rows),
            "complete_raw_head_by_degree": [str(value) for value in complete_head],
            "complete_raw_head": str(raw_head),
            "complete_raw_absolute_tail_upper": str(complete_tail),
            "complete_raw_integral_interval": {"lower": str(raw_lower), "upper": str(raw_upper)},
            "proof": (
                "For each exact denominator product, write every affine factor as b_i+L_i and "
                "expand product_i(b_i+L_i)^-1 through total degree four. Signed coefficients are "
                "summed and integrated first. The y=sinh(t) change gives dy=cosh(t)dt; centered "
                "moments follow exactly from the cosh-power recurrence at rational q endpoints. "
                "For degree at least five, h_5 of the positive factor ratios and the bound "
                "h_(n+1)/h_n <= r_max(n+14)/(n+1) give one convergent geometric tail."
            ),
        },
        "certificate": {
            "normalization_lower_using_pi_less_than_22_over_7": str(normalization_lower),
            "normalized_signed_head": str(normalized_head),
            "normalized_absolute_tail_upper": str(normalized_tail),
            "computed_normalized_negative_mass_lower": str(normalized_negative_mass.lower()),
            "declared_strict_negative_mass_lower": rational_row(NEGATIVE_MASS_LOWER),
            "result": "strictly_negative_complete_fifteen_box_union",
        },
        "composition": {
            "k247_complete_positive_prefix_upper": rational_row(prefix_upper),
            "strict_negative_excess_over_k247_upper": rational_row(cancellation_margin),
            "result": (
                "the exact all-fifteen pair-box union has more certified negative mass than the "
                "complete positive K247 q<=15 prefix; their disjoint union is strictly negative"
            ),
        },
        "controls": (
            "An independent reverse-order raw-allocation probe reconstructs the K230 orbit manifest, "
            "checks two- and three-point product quadratures against the certified sign and scale, "
            "replays the complete-homogeneous tail formula, and applies absolute-weight, omitted-tail, "
            "wrong-measure and pair-deletion hostile controls."
        ),
        "source_routing": (
            "SC-ACT-01/02 ASSERTS and SC-META-53 UNCERTAIN remain unchanged; "
            "LT-GR6b/LT-SM8/RA-F1/AC-F1 remain NEEDS."
        ),
        "decision": (
            "K260's ten-box ceiling is entirely an enclosure artifact: exact S6 orbit cancellation "
            "plus a signed reanchored moment integral certifies the complete fifteen-box union negative. "
            "The next question is control of genuinely new complement outside this union."
        ),
        "claim_ceiling": (
            "Exact sign and negative-mass lower bound only on the declared fifteen-box union, plus "
            "its K247 composition. No remaining-complement or full-K218 sign, complete original "
            "order-six error, K215 impossibility, source/ledger/canon/paper/public-posture change, "
            "or physical-positivity conclusion."
        ),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K261 all-fifteen result", result["certificate"]["result"])
    print("[PASS] K261 negative mass lower", result["certificate"]["declared_strict_negative_mass_lower"]["decimal"])
    print("[PASS] K261 tail", result["certificate"]["normalized_absolute_tail_upper"])
