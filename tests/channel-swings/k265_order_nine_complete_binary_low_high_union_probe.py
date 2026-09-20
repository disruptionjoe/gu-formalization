#!/usr/bin/env python3
"""Independent replay and hostile controls for the complete K265 binary union."""
from __future__ import annotations

from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations, product
import json
from math import comb, factorial

from flint import arb, ctx, fmpq, fmpq_mpoly_ctx
import numpy as np

from k225_order_six_diagonal_cancellation import ROOT
from k262_order_six_low_through_three_high_multiplicity_integral import (
    HIGH_Q,
    LOW_Q,
)
from k262_order_six_low_through_three_high_multiplicity_integral_probe import (
    K185,
    K230,
    independent_groups,
    raw_terms,
)


RECORD = ROOT / "lab/process/k265-order-nine-complete-binary-low-high-union.json"
K264 = ROOT / "lab/process/k264-order-nine-complete-low-high-union.json"
ORDER = 9
NORMALIZATION_SERIALIZATION_SLACK = Q(1, 10**86)


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


def compile_independent(groups: dict, fixed_status: tuple[int, int],
                        subset: tuple[int, ...], ring, variables,
                        low_center: Q, low_radius: Q,
                        high_center: Q, high_radius: Q,
                        low_moments: tuple, high_moments: tuple,
                        low_measure: Q, high_measure: Q):
    active = frozenset(
        axis for axis, is_high in enumerate(fixed_status) if is_high
    ) | frozenset(subset)
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
    high_count = sum(fixed_status) + len(subset)
    tail *= high_measure ** high_count * low_measure ** (8 - high_count)
    return hashes, heads, tail


def normalized_interval_independent(head: arb, tail: Q) -> tuple[arb, arb]:
    raw_lower = head.lower() - as_arb(tail)
    raw_upper = head.upper() + as_arb(tail)
    normalization_lower = fmpq(2**8 * 256**6, factorial(5)) * fmpq(7, 22) ** 8
    normalization_upper = fmpq(2**8 * 256**6, factorial(5)) * fmpq(10, 31) ** 8
    lower_scale = normalization_upper if raw_lower < 0 else normalization_lower
    upper_scale = normalization_upper if raw_upper > 0 else normalization_lower
    return arb(lower_scale) * raw_lower, arb(upper_scale) * raw_upper


def quadrature_fixed(groups: dict, fixed_status: tuple[int, int], order: int,
                     absolute_weights: bool = False,
                     wrong_measure: bool = False) -> float:
    if order == 2:
        nodes = np.array([-1 / np.sqrt(3), 1 / np.sqrt(3)])
        weights = np.ones(2)
    elif order == 3:
        nodes = np.array([-np.sqrt(3 / 5), 0.0, np.sqrt(3 / 5)])
        weights = np.array([5 / 9, 8 / 9, 5 / 9])
    else:
        raise ValueError(order)
    rows = np.array([
        [[(row >> axis) & 1 for axis in range(8)] for row in key]
        for key in groups
    ], dtype=np.float64)
    signed_weights = np.array([
        abs(weight) if absolute_weights else weight for weight in groups.values()
    ], dtype=np.float64)
    low_y = tuple(map(float, map(sinh_log, LOW_Q)))
    high_y = tuple(map(float, map(sinh_log, HIGH_Q)))
    total = 0.0
    for status in product((0, 1), repeat=6):
        active = frozenset(
            axis for axis, is_high in enumerate(fixed_status + status) if is_high
        )
        axis_nodes = []
        axis_weights = []
        for axis in range(8):
            lo, hi = high_y if axis in active else low_y
            axis_nodes.append((lo + hi) / 2 + (hi - lo) / 2 * nodes)
            axis_weights.append((hi - lo) / 2 * weights)
        for indices in product(range(order), repeat=8):
            y = np.array([axis_nodes[axis][indices[axis]] for axis in range(8)])
            c = np.sqrt(1 + y * y)
            denominators = 256.0 + np.einsum("gka,a->gk", rows, c)
            value = np.sum(signed_weights / np.prod(denominators, axis=1))
            measure = np.prod([axis_weights[axis][indices[axis]] for axis in range(8)])
            if wrong_measure:
                measure /= np.prod(c)
            total += measure * value
    return total


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
    fixed_status_by_name = {
        "low_low": (0, 0), "high_low": (1, 0), "high_high": (1, 1)
    }
    for block in record["new_fixed_status_blocks"]:
        fixed_status = fixed_status_by_name[block["block"]]
        block_head = arb(0)
        block_tail = Q()
        for layer in block["multiplicity_layers"]:
            multiplicity = layer["multiplicity"]
            expected = {
                tuple(box["high_exceptional_axes"]): box
                for box in layer["box_records"]
            }
            layer_head = arb(0)
            layer_tail = Q()
            for subset in combinations(range(2, 8), multiplicity):
                hashes, heads, tail = compile_independent(
                    groups, fixed_status, subset, ring, variables,
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
            block_head += layer_head
            block_tail += layer_tail
        assert (block_head - arb(block["complete_raw_head"])).contains(0)
        assert block_tail == Q(block["complete_raw_absolute_tail_upper"])
        block_lower, block_upper = normalized_interval_independent(
            arb(block["complete_raw_head"]), block_tail
        )
        interval = block["normalized_integral_interval"]
        assert abs(block_lower - arb(interval["lower"])) < as_arb(
            NORMALIZATION_SERIALIZATION_SLACK
        )
        assert abs(block_upper - arb(interval["upper"])) < as_arb(
            NORMALIZATION_SERIALIZATION_SLACK
        )
        assert block_lower > 0
        independent_head += block_head
        independent_tail += block_tail

    k264 = json.loads(K264.read_text())
    k264_complete = k264["complete_union"]
    independent_head += arb(k264_complete["complete_raw_head"])
    independent_tail += Q(k264_complete["complete_raw_absolute_tail_upper"])
    complete = record["complete_binary_union"]
    assert (independent_head - arb(complete["complete_raw_head"])).contains(0)
    assert independent_tail == Q(complete["complete_raw_absolute_tail_upper"])
    independent_lower, independent_upper = normalized_interval_independent(
        arb(complete["complete_raw_head"]), independent_tail
    )
    interval = complete["normalized_integral_interval"]
    assert abs(independent_lower - arb(interval["lower"])) < as_arb(
        NORMALIZATION_SERIALIZATION_SLACK
    )
    assert abs(independent_upper - arb(interval["upper"])) < as_arb(
        NORMALIZATION_SERIALIZATION_SLACK
    )

    all_fixed_status = {
        "low_low": (0, 0), "low_high": (0, 1),
        "high_low": (1, 0), "high_high": (1, 1),
    }
    q2_by_block = {
        name: quadrature_fixed(groups, status, 2)
        for name, status in all_fixed_status.items()
    }
    q3_by_block = {
        name: quadrature_fixed(groups, status, 3)
        for name, status in all_fixed_status.items()
    }
    q2 = sum(q2_by_block.values())
    q3 = sum(q3_by_block.values())
    normalization = float(2**8 * 256**6 / factorial(5)) / float(arb.pi() ** 8)
    normalized_q2 = normalization * q2
    normalized_q3 = normalization * q3
    interval = complete["normalized_integral_interval"]
    lower = float(arb(interval["lower"]).lower())
    upper = float(arb(interval["upper"]).upper())
    assert 0 < lower < normalized_q2 < upper
    assert 0 < lower < normalized_q3 < upper
    # The dominant high/high block has a measured q2/q3 gap of 3.10e-4.
    assert abs(normalized_q3 - normalized_q2) < abs(normalized_q3) * 4e-4
    absolute_q2 = quadrature_fixed(groups, (1, 1), 2, absolute_weights=True)
    wrong_q2 = quadrature_fixed(groups, (1, 1), 2, wrong_measure=True)
    assert absolute_q2 > q2_by_block["high_high"]
    assert wrong_q2 != q2_by_block["high_high"]
    assert q3 - q3_by_block["high_high"] > 0
    assert q3_by_block["high_high"] > 10 * sum(
        value for name, value in q3_by_block.items() if name != "high_high"
    )

    declared = record["certificate"]["declared_strict_positive_mass_lower"]
    declared_lower = Q(declared["numerator"], declared["denominator"])
    assert declared_lower == Q(6, 10**18)
    assert independent_lower > as_arb(declared_lower)

    print("[PASS] K265 reverse orbit manifest", digest)
    print("[PASS] K265 independent exact polynomial, moment, tail and normalization replay")
    print("[PASS] K265 q2/q3 four-block complete-union quadratures inside interval")
    print("[PASS] K265 absolute-weight, wrong-measure and block-deletion controls")
    print("[PASS] K265 complete binary-union lower bound", float(independent_lower.lower()))


if __name__ == "__main__":
    main()
