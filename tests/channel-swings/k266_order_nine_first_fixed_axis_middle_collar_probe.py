#!/usr/bin/env python3
"""Independent replay and hostile controls for K266's middle collar."""
from __future__ import annotations

from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations, product
import json
from math import factorial
import sys

from flint import arb, ctx, fmpq, fmpq_mpoly_ctx
import numpy as np

from k225_order_six_diagonal_cancellation import ROOT
from k262_order_six_low_through_three_high_multiplicity_integral import HIGH_Q, LOW_Q
from k262_order_six_low_through_three_high_multiplicity_integral_probe import (
    K185,
    K230,
    independent_groups,
    raw_terms,
)
from k265_order_nine_complete_binary_low_high_union_probe import (
    as_arb,
    centered_moments_independent,
    center_radius,
    coefficient_hash,
    normalized_interval_independent,
    sinh_log,
    tail_independent,
)
from k266_order_nine_first_fixed_axis_middle_collar import BLOCKS, MIDDLE_Q

sys.set_int_max_str_digits(0)


RECORD = ROOT / "lab/process/k266-order-nine-first-fixed-axis-middle-collar.json"
ORDER = 9
BOUNDS = {"low": LOW_Q, "middle": MIDDLE_Q, "high": HIGH_Q}
NORMALIZATION_SERIALIZATION_SLACK = Q(1, 10**86)


def compile_independent(groups: dict, fixed_status: tuple[str, str],
                        high_subset: tuple[int, ...], ring, variables,
                        geometry: dict[str, dict]):
    status = list(fixed_status) + ["low"] * 6
    for axis in high_subset:
        status[axis] = "high"
    centers = tuple(geometry[name]["center"] for name in status)
    radii = tuple(geometry[name]["radius"] for name in status)
    moments = tuple(geometry[name]["moments"] for name in status)
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
    for name in status:
        tail *= geometry[name]["measure"]
    return hashes, heads, tail


def quadrature_box(groups: dict, status: tuple[str, ...], order: int,
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
    y_bounds = {
        name: tuple(map(float, map(sinh_log, bounds)))
        for name, bounds in BOUNDS.items()
    }
    axis_nodes = []
    axis_weights = []
    for name in status:
        lo, hi = y_bounds[name]
        axis_nodes.append((lo + hi) / 2 + (hi - lo) / 2 * nodes)
        axis_weights.append((hi - lo) / 2 * weights)
    total = 0.0
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


def quadrature_block(groups: dict, fixed_status: tuple[str, str],
                     multiplicities, order: int,
                     absolute_weights: bool = False,
                     wrong_measure: bool = False) -> float:
    total = 0.0
    for multiplicity in multiplicities:
        for subset in combinations(range(2, 8), multiplicity):
            status = list(fixed_status) + ["low"] * 6
            for axis in subset:
                status[axis] = "high"
            total += quadrature_box(
                groups, tuple(status), order, absolute_weights, wrong_measure
            )
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
    geometry = {}
    for name, bounds in BOUNDS.items():
        center, radius = center_radius(bounds)
        geometry[name] = {
            "center": center,
            "radius": radius,
            "moments": centered_moments_independent(bounds, center, ORDER),
            "measure": sinh_log(bounds[1]) - sinh_log(bounds[0]),
        }

    independent_head = arb(0)
    independent_tail = Q()
    block_specs = {name: (fixed, multiplicities) for name, fixed, multiplicities in BLOCKS}
    for block in record["fixed_axis_middle_blocks"]:
        fixed_status, multiplicities = block_specs[block["block"]]
        block_head = arb(0)
        block_tail = Q()
        for layer in block["multiplicity_layers"]:
            multiplicity = layer["high_multiplicity"]
            assert multiplicity in multiplicities
            expected = {
                tuple(box["high_exceptional_axes"]): box
                for box in layer["box_records"]
            }
            layer_head = arb(0)
            layer_tail = Q()
            for subset in reversed(list(combinations(range(2, 8), multiplicity))):
                hashes, heads, tail = compile_independent(
                    groups, fixed_status, subset, ring, variables, geometry
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
        block_lower, block_upper = normalized_interval_independent(block_head, block_tail)
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

    complete = record["complete_collar"]
    assert (independent_head - arb(complete["complete_raw_head"])).contains(0)
    assert independent_tail == Q(complete["complete_raw_absolute_tail_upper"])
    independent_lower, independent_upper = normalized_interval_independent(
        independent_head, independent_tail
    )
    interval = complete["normalized_integral_interval"]
    assert abs(independent_lower - arb(interval["lower"])) < as_arb(
        NORMALIZATION_SERIALIZATION_SLACK
    )
    assert abs(independent_upper - arb(interval["upper"])) < as_arb(
        NORMALIZATION_SERIALIZATION_SLACK
    )

    q2_by_block = {
        name: quadrature_block(groups, fixed, multiplicities, 2)
        for name, fixed, multiplicities in BLOCKS
    }
    q3_by_block = {
        name: quadrature_block(groups, fixed, multiplicities, 3)
        for name, fixed, multiplicities in BLOCKS
    }
    normalization = float(2**8 * 256**6 / factorial(5)) / float(arb.pi() ** 8)
    normalized_q2 = normalization * sum(q2_by_block.values())
    normalized_q3 = normalization * sum(q3_by_block.values())
    lower = float(arb(interval["lower"]).lower())
    upper = float(arb(interval["upper"]).upper())
    assert 0 < lower < normalized_q2 < upper
    assert 0 < lower < normalized_q3 < upper
    assert abs(normalized_q3 - normalized_q2) < abs(normalized_q3) * 2e-3

    dominant_name = "axis1_middle_axis0_high"
    dominant = next(row for row in BLOCKS if row[0] == dominant_name)
    absolute_q2 = quadrature_block(
        groups, dominant[1], dominant[2], 2, absolute_weights=True
    )
    wrong_q2 = quadrature_block(
        groups, dominant[1], dominant[2], 2, wrong_measure=True
    )
    assert absolute_q2 > q2_by_block[dominant_name]
    assert wrong_q2 != q2_by_block[dominant_name]
    q3_remainder = sum(
        value for name, value in q3_by_block.items() if name != dominant_name
    )
    assert q3_remainder > 0
    assert q3_by_block[dominant_name] > 4 * q3_remainder

    declared = record["certificate"]["declared_strict_positive_mass_lower"]
    declared_lower = Q(declared["numerator"], declared["denominator"])
    assert declared_lower == Q(1, 10**18)
    assert independent_lower > as_arb(declared_lower)
    assert record["domain"]["boxes"] == 254
    assert record["domain"]["disjoint_from_k247_interior"]
    assert record["domain"]["disjoint_from_k265_interior"]

    print("[PASS] K266 reverse orbit manifest", digest)
    print("[PASS] K266 independent 254-box polynomial, moment, tail and normalization replay")
    print("[PASS] K266 q2/q3 four-block collar quadratures inside interval")
    print("[PASS] K266 absolute-weight, wrong-measure and dominant-block deletion controls")
    print("[PASS] K266 complete collar lower bound", float(independent_lower.lower()))


if __name__ == "__main__":
    main()
