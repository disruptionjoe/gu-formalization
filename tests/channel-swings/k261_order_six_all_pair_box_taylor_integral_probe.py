#!/usr/bin/env python3
"""Independent raw-allocation, tail and quadrature controls for K261."""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations, product
import json
from math import factorial
from pathlib import Path

from flint import arb, ctx
import numpy as np


ROOT = Path(__file__).resolve().parents[2]
K185 = ROOT / "lab/process/k185-order-six-duffy-face-tail-wave.json"
K230 = ROOT / "lab/process/k230-order-six-permutation-projection.json"
RECORD = ROOT / "lab/process/k261-order-six-all-pair-box-taylor-integral.json"
LOW_Q = (Q(1), Q(13, 5))
HIGH_Q = (Q(1792), Q(2304))
PAIRS = tuple(reversed(tuple(combinations(range(2, 8), 2))))
TAIL_START = 5


def raw_terms(source: dict):
    catalog = source["exact_allocation_certificate"]["allocation_catalog"]
    for entry in reversed(source["complete_face_hypergraph"]["entries"]):
        outer = entry["coefficient_product"] * (2 if entry["left"] != entry["right"] else 1)
        for term in reversed(entry["terms"]):
            supports = tuple(
                int(value, 16)
                for value in catalog[term["allocation_id"]]["support_masks_hex"].split(",")
            )
            yield outer * term["leibniz_sign"], supports


def row_masks(masks):
    return tuple(
        sum(((mask >> source_row) & 1) << axis for axis, mask in enumerate(masks))
        for source_row in range(14)
    )


def transform(rows, permutation):
    return tuple(sorted(
        (row & 3) | sum(
            ((row >> (position + 2)) & 1) << (permutation[position] + 2)
            for position in range(6)
        )
        for row in rows
    ))


def orbit_key(rows):
    # Generate permutations locally rather than importing the producer's orbit map.
    from itertools import permutations
    return min(transform(rows, permutation) for permutation in permutations(range(6)))


def independent_groups(items):
    groups = defaultdict(int)
    for weight, masks in items:
        groups[orbit_key(row_masks(masks))] += weight
    return {rows: weight for rows, weight in groups.items() if weight}


def cosh_log(q: Q) -> Q:
    return (q + 1 / q) / 2


def sinh_log(q: Q) -> Q:
    return (q - 1 / q) / 2


def center_radius(bounds):
    lo, hi = map(cosh_log, bounds)
    return (lo + hi) / 2, (hi - lo) / 2


def complete_homogeneous(ratios, degree):
    coefficients = [Q(1)] + [Q()] * degree
    for ratio in reversed(ratios):
        updated = [Q()] * (degree + 1)
        power = Q(1)
        for k in range(degree + 1):
            for prior in range(degree + 1 - k):
                updated[k + prior] += coefficients[prior] * power
            power *= ratio
        coefficients = updated
    return coefficients[degree]


def term_tail(rows, centers, radii):
    bases = []
    ratios = []
    for row in reversed(rows):
        support = [axis for axis in range(8) if row & (1 << axis)]
        base = Q(256) + sum((centers[axis] for axis in support), Q())
        deviation = sum((radii[axis] for axis in support), Q())
        bases.append(base)
        ratios.append(deviation / base)
    ratio = max(ratios) * Q(TAIL_START + 14, TAIL_START + 1)
    assert ratio < 1
    return complete_homogeneous(ratios, TAIL_START) / np.prod(bases, dtype=object) / (1 - ratio)


def exact_degree_zero(groups):
    low_center, _ = center_radius(LOW_Q)
    high_center, _ = center_radius(HIGH_Q)
    low_measure = sinh_log(LOW_Q[1]) - sinh_log(LOW_Q[0])
    high_measure = sinh_log(HIGH_Q[1]) - sinh_log(HIGH_Q[0])
    measure = high_measure ** 3 * low_measure ** 5
    total = Q()
    for pair in PAIRS:
        active = frozenset((1,) + pair)
        centers = tuple(high_center if axis in active else low_center for axis in range(8))
        for rows, weight in groups.items():
            denominator = Q(1)
            for row in rows:
                denominator *= Q(256) + sum(
                    (centers[axis] for axis in range(8) if row & (1 << axis)), Q()
                )
            total += Q(weight) / denominator * measure
    return total


def replay_tail(groups):
    low_center, low_radius = center_radius(LOW_Q)
    high_center, high_radius = center_radius(HIGH_Q)
    low_measure = sinh_log(LOW_Q[1]) - sinh_log(LOW_Q[0])
    high_measure = sinh_log(HIGH_Q[1]) - sinh_log(HIGH_Q[0])
    measure = high_measure ** 3 * low_measure ** 5
    total = Q()
    for pair in PAIRS:
        active = frozenset((1,) + pair)
        centers = tuple(high_center if axis in active else low_center for axis in range(8))
        radii = tuple(high_radius if axis in active else low_radius for axis in range(8))
        total += measure * sum(
            (abs(weight) * term_tail(rows, centers, radii) for rows, weight in groups.items()), Q()
        )
    return total


def quadrature(groups, order, absolute_weights=False, wrong_measure=False):
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
    pair_totals = {}
    for pair in PAIRS:
        active = frozenset((1,) + pair)
        axis_nodes = []
        axis_weights = []
        for axis in range(8):
            lo, hi = high_y if axis in active else low_y
            axis_nodes.append((lo + hi) / 2 + (hi - lo) / 2 * nodes)
            axis_weights.append((hi - lo) / 2 * weights)
        pair_total = 0.0
        for indices in product(range(order), repeat=8):
            y = np.array([axis_nodes[axis][indices[axis]] for axis in range(8)])
            c = np.sqrt(1 + y * y)
            denominators = 256.0 + np.einsum("gka,a->gk", rows, c)
            value = np.sum(signed_weights / np.prod(denominators, axis=1))
            measure = np.prod([axis_weights[axis][indices[axis]] for axis in range(8)])
            if wrong_measure:
                measure /= np.prod(c)
            pair_total += measure * value
        pair_totals[pair] = pair_total
        total += pair_total
    return total, pair_totals


def main():
    ctx.prec = 256
    source = json.loads(K185.read_text())
    record = json.loads(RECORD.read_text())
    items = list(raw_terms(source))
    groups = independent_groups(items)
    assert len(items) == 1864 and len(groups) == 307

    compact = ";".join(
        ",".join(map(str, rows)) + ":" + str(weight)
        for rows, weight in sorted(groups.items())
    )
    digest = sha256(compact.encode()).hexdigest()
    assert digest == json.loads(K230.read_text())["orbit_coefficient_manifest_sha256"]
    assert digest == record["projection"]["orbit_manifest_sha256"]

    degree_zero = exact_degree_zero(groups)
    recorded_degree_zero = arb(record["reanchored_integral"]["complete_raw_head_by_degree"][0])
    assert recorded_degree_zero.contains(arb(degree_zero.numerator) / degree_zero.denominator)

    tail = replay_tail(groups)
    assert str(tail) == record["reanchored_integral"]["complete_raw_absolute_tail_upper"]
    assert tail > 0

    q2, pair2 = quadrature(groups, 2)
    q3, pair3 = quadrature(groups, 3)
    raw_interval = record["reanchored_integral"]["complete_raw_integral_interval"]
    assert float(arb(raw_interval["lower"]).lower()) < q2 < float(arb(raw_interval["upper"]).upper())
    assert float(arb(raw_interval["lower"]).lower()) < q3 < float(arb(raw_interval["upper"]).upper())
    assert abs(q3 - q2) < 6e-35 and q2 < 0 and q3 < 0

    absolute, _ = quadrature(groups, 2, absolute_weights=True)
    wrong, _ = quadrature(groups, 2, wrong_measure=True)
    assert absolute > 0 and wrong != q2
    dominant_pair = max(pair3, key=lambda pair: abs(pair3[pair]))
    assert dominant_pair == (6, 7)
    assert abs(q3 - pair3[dominant_pair]) > 1e-33

    declared = record["certificate"]["declared_strict_negative_mass_lower"]
    assert Q(declared["numerator"], declared["denominator"]) == Q(43, 10**21)
    print("[PASS] K261 reverse orbit and exact degree-zero replay", digest)
    print("[PASS] K261 exact tail replay", str(tail))
    print("[PASS] K261 independent q2/q3 controls", q2, q3)
    print("[PASS] K261 absolute-weight, wrong-measure and pair-deletion controls")


if __name__ == "__main__":
    main()
