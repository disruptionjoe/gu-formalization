#!/usr/bin/env python3
"""Independent raw-allocation, compiler, tail and quadrature replay for K264."""
from __future__ import annotations

from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations
import json
from math import comb, factorial

from flint import arb, ctx, fmpq, fmpq_mpoly_ctx

from k225_order_six_diagonal_cancellation import ROOT
from k262_order_six_low_through_three_high_multiplicity_integral import (
    HIGH_Q,
    LOW_Q,
)
from k262_order_six_low_through_three_high_multiplicity_integral_probe import (
    K185,
    K230,
    independent_groups,
    quadrature,
    raw_terms,
)


RECORD = ROOT / "lab/process/k264-order-nine-complete-low-high-union.json"
ORDER = 9


def as_arb(value: Q | fmpq) -> arb:
    if isinstance(value, Q):
        return arb(value.numerator) / value.denominator
    return arb(value)


def cosh_log(q: Q) -> Q:
    return (q + 1 / q) / 2


def sinh_log(q: Q) -> Q:
    return (q - 1 / q) / 2


def center_radius(bounds: tuple[Q, Q]) -> tuple[Q, Q]:
    low, high = (cosh_log(value) for value in bounds)
    return (low + high) / 2, (high - low) / 2


def cosh_power_integrals(bounds: tuple[Q, Q], maximum_power: int) -> list[arb]:
    q_low, q_high = bounds
    c_low, c_high = cosh_log(q_low), cosh_log(q_high)
    s_low, s_high = sinh_log(q_low), sinh_log(q_high)
    values = [
        arb(q_high.numerator).log() - arb(q_high.denominator).log()
        - arb(q_low.numerator).log() + arb(q_low.denominator).log()
    ]
    values.append(as_arb(s_high - s_low))
    for exponent in range(2, maximum_power + 1):
        boundary = (
            s_high * c_high ** (exponent - 1)
            - s_low * c_low ** (exponent - 1)
        ) / exponent
        values.append(
            as_arb(boundary)
            + arb(exponent - 1) / exponent * values[exponent - 2]
        )
    return values


def centered_moments_independent(bounds: tuple[Q, Q], center: Q,
                                 order: int) -> tuple[arb, ...]:
    powers = cosh_power_integrals(bounds, order + 1)
    moments = []
    for exponent in range(order + 1):
        value = arb(0)
        for power in reversed(range(exponent + 1)):
            coefficient = Q(comb(exponent, power)) * (-center) ** (exponent - power)
            value += as_arb(coefficient) * powers[power + 1]
        moments.append(value)
    return tuple(moments)


def complete_homogeneous_reverse(ratios: tuple[Q, ...], degree: int) -> Q:
    coefficients = [Q(1)] + [Q()] * degree
    for ratio in reversed(ratios):
        updated = [Q()] * (degree + 1)
        powers = [ratio ** exponent for exponent in range(degree + 1)]
        for target_degree in range(degree + 1):
            updated[target_degree] = sum(
                (coefficients[prior] * powers[target_degree - prior]
                 for prior in range(target_degree + 1)),
                Q(),
            )
        coefficients = updated
    return coefficients[degree]


def tail_independent(rows: tuple[int, ...], centers: tuple[Q, ...],
                     radii: tuple[Q, ...], tail_start: int) -> Q:
    base_product = Q(1)
    ratios = []
    for row in reversed(rows):
        support = tuple(axis for axis in range(8) if row & (1 << axis))
        base = Q(256) + sum((centers[axis] for axis in support), Q())
        deviation = sum((radii[axis] for axis in support), Q())
        base_product *= base
        ratios.append(deviation / base)
    leading = complete_homogeneous_reverse(tuple(ratios), tail_start)
    ratio_ceiling = max(ratios) * Q(tail_start + 14, tail_start + 1)
    assert ratio_ceiling < 1
    return leading / base_product / (1 - ratio_ceiling)


def coefficient_hash(polynomial) -> str:
    payload = ";".join(
        f"{','.join(map(str, exponents))}:{coefficient}"
        for exponents, coefficient in polynomial.terms()
    )
    return sha256(payload.encode()).hexdigest()


def compile_independent(groups: dict, subset: tuple[int, ...], ring, variables,
                        low_center: Q, low_radius: Q,
                        high_center: Q, high_radius: Q,
                        low_moments: tuple, high_moments: tuple,
                        low_measure: Q, high_measure: Q):
    active = frozenset((1,) + subset)
    centers = tuple(high_center if axis in active else low_center for axis in range(8))
    radii = tuple(high_radius if axis in active else low_radius for axis in range(8))
    moments = tuple(high_moments if axis in active else low_moments for axis in range(8))
    polynomials = [ring.constant(0) for _ in range(ORDER + 1)]
    for rows, weight in reversed(list(groups.items())):
        pieces = [ring.constant(1)] + [ring.constant(0) for _ in range(ORDER)]
        for row in reversed(rows):
            support = tuple(axis for axis in range(8) if row & (1 << axis))
            base = fmpq(256) + sum(
                (fmpq(centers[axis].numerator, centers[axis].denominator)
                 for axis in support),
                fmpq(0),
            )
            linear = sum((variables[axis] for axis in support), ring.constant(0))
            next_pieces = []
            for degree in range(ORDER + 1):
                previous = next_pieces[degree - 1] if degree else ring.constant(0)
                next_pieces.append((pieces[degree] - linear * previous) / base)
            pieces = next_pieces
        for degree, piece in enumerate(pieces):
            polynomials[degree] += weight * piece

    heads = []
    hashes = []
    for polynomial in polynomials:
        hashes.append(coefficient_hash(polynomial))
        value = arb(0)
        for exponents, coefficient in reversed(list(polynomial.terms())):
            term = arb(coefficient)
            for axis in reversed(range(8)):
                term *= moments[axis][exponents[axis]]
            value += term
        heads.append(value)
    tail = sum(
        (Q(abs(weight)) * tail_independent(rows, centers, radii, ORDER + 1)
         for rows, weight in reversed(list(groups.items()))),
        Q(),
    )
    multiplicity = len(subset)
    tail *= high_measure ** (1 + multiplicity) * low_measure ** (7 - multiplicity)
    return hashes, heads, tail


def main() -> None:
    ctx.prec = 256
    source = json.loads(K185.read_text())
    record = json.loads(RECORD.read_text())
    items = list(raw_terms(source))
    groups = independent_groups(items)
    compact = ";".join(
        ",".join(map(str, rows)) + ":" + str(weight)
        for rows, weight in sorted(groups.items())
    )
    digest = sha256(compact.encode()).hexdigest()
    assert len(items) == 1864 and len(groups) == 307
    assert digest == json.loads(K230.read_text())["orbit_coefficient_manifest_sha256"]
    assert digest == record["projection"]["orbit_manifest_sha256"]

    ring = fmpq_mpoly_ctx.get([f"z{axis}" for axis in range(8)])
    variables = ring.gens()
    low_center, low_radius = center_radius(LOW_Q)
    high_center, high_radius = center_radius(HIGH_Q)
    low_moments = centered_moments_independent(LOW_Q, low_center, ORDER)
    high_moments = centered_moments_independent(HIGH_Q, high_center, ORDER)
    low_measure = sinh_log(LOW_Q[1]) - sinh_log(LOW_Q[0])
    high_measure = sinh_log(HIGH_Q[1]) - sinh_log(HIGH_Q[0])
    independent_head = arb(0)
    independent_tail = Q()

    for layer in record["multiplicity_layers"]:
        multiplicity = layer["multiplicity"]
        expected = {
            tuple(box["high_exceptional_axes"]): box
            for box in layer["box_records"]
        }
        layer_head = arb(0)
        layer_tail = Q()
        for subset in combinations(range(2, 8), multiplicity):
            hashes, heads, tail = compile_independent(
                groups, subset, ring, variables,
                low_center, low_radius, high_center, high_radius,
                low_moments, high_moments, low_measure, high_measure,
            )
            prior = expected[subset]
            assert hashes == prior["coefficient_sha256_by_degree"]
            assert tail == Q(prior["raw_absolute_tail_upper"])
            for value, prior_value in zip(heads, prior["raw_head_by_degree"]):
                assert (value - arb(prior_value)).contains(0)
            layer_head += sum(heads, arb(0))
            layer_tail += tail
        assert (layer_head - arb(layer["complete_raw_head"])).contains(0)
        assert layer_tail == Q(layer["complete_raw_absolute_tail_upper"])
        independent_head += layer_head
        independent_tail += layer_tail

    complete = record["complete_union"]
    assert (independent_head - arb(complete["complete_raw_head"])).contains(0)
    assert independent_tail == Q(complete["complete_raw_absolute_tail_upper"])

    q2_by_multiplicity = {}
    q3_by_multiplicity = {}
    absolute_q2 = 0.0
    wrong_q2 = 0.0
    for multiplicity in range(7):
        q2_by_multiplicity[multiplicity], _ = quadrature(groups, multiplicity, 2)
        q3_by_multiplicity[multiplicity], _ = quadrature(groups, multiplicity, 3)
        absolute_piece, _ = quadrature(
            groups, multiplicity, 2, absolute_weights=True
        )
        wrong_piece, _ = quadrature(groups, multiplicity, 2, wrong_measure=True)
        absolute_q2 += absolute_piece
        wrong_q2 += wrong_piece
    q2 = sum(q2_by_multiplicity.values())
    q3 = sum(q3_by_multiplicity.values())
    normalization = float(2**8 * 256**6 / factorial(5)) / float(arb.pi() ** 8)
    normalized_q2 = normalization * q2
    normalized_q3 = normalization * q3
    interval = complete["normalized_integral_interval"]
    lower = float(arb(interval["lower"]).lower())
    upper = float(arb(interval["upper"]).upper())
    assert 0 < lower < normalized_q2 < upper
    assert 0 < lower < normalized_q3 < upper
    assert abs(normalized_q3 - normalized_q2) < abs(normalized_q3) * 2e-4
    assert absolute_q2 > q2 and wrong_q2 != q2
    assert q3 - q3_by_multiplicity[4] < 0 < q3

    declared = record["certificate"]["declared_strict_positive_mass_lower"]
    assert Q(declared["numerator"], declared["denominator"]) == Q(106, 10**22)
    k263 = json.loads((ROOT / "lab/process/k263-order-six-four-high-multiplicity-integral.json").read_text())
    unresolved = k263["zero_through_four_composition"]["normalized_integral_interval"]
    assert arb(unresolved["lower"]) < 0 < arb(unresolved["upper"])

    print("[PASS] K264 reverse orbit manifest", digest)
    print("[PASS] K264 independent exact polynomial, moment and tail replay")
    print("[PASS] K264 q2/q3 complete-union quadratures inside interval")
    print("[PASS] K264 absolute-weight, wrong-measure and m4-deletion controls")
    print("[PASS] K264 order-nine certificate resolves K263 interval ambiguity")


if __name__ == "__main__":
    main()
