#!/usr/bin/env python3
"""Independent raw-allocation, tail, quadrature and domain controls for K262."""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations, permutations, product
import json
from pathlib import Path

from flint import arb, ctx
import numpy as np


ROOT = Path(__file__).resolve().parents[2]
K185 = ROOT / "lab/process/k185-order-six-duffy-face-tail-wave.json"
K230 = ROOT / "lab/process/k230-order-six-permutation-projection.json"
K247 = ROOT / "lab/process/k247-order-six-cumulative-q15-boundary.json"
K261 = ROOT / "lab/process/k261-order-six-all-pair-box-taylor-integral.json"
RECORD = ROOT / "lab/process/k262-order-six-low-through-three-high-multiplicity-integral.json"
LOW_Q = (Q(1), Q(13, 5))
HIGH_Q = (Q(1792), Q(2304))
LAYER_ORDERS = {0: 4, 1: 4, 3: 6}


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


def term_tail(rows, centers, radii, tail_start):
    base_product = Q(1)
    ratios = []
    for row in reversed(rows):
        support = [axis for axis in range(8) if row & (1 << axis)]
        base = Q(256) + sum((centers[axis] for axis in support), Q())
        deviation = sum((radii[axis] for axis in support), Q())
        base_product *= base
        ratios.append(deviation / base)
    ratio = max(ratios) * Q(tail_start + 14, tail_start + 1)
    assert ratio < 1
    return complete_homogeneous(ratios, tail_start) / base_product / (1 - ratio)


def subsets(multiplicity):
    return tuple(reversed(tuple(combinations(range(2, 8), multiplicity))))


def exact_degree_zero(groups, multiplicity):
    low_center, _ = center_radius(LOW_Q)
    high_center, _ = center_radius(HIGH_Q)
    low_measure = sinh_log(LOW_Q[1]) - sinh_log(LOW_Q[0])
    high_measure = sinh_log(HIGH_Q[1]) - sinh_log(HIGH_Q[0])
    measure = high_measure ** (1 + multiplicity) * low_measure ** (7 - multiplicity)
    total = Q()
    for subset in subsets(multiplicity):
        active = frozenset((1,) + subset)
        centers = tuple(high_center if axis in active else low_center for axis in range(8))
        for rows, weight in groups.items():
            denominator = Q(1)
            for row in rows:
                denominator *= Q(256) + sum(
                    (centers[axis] for axis in range(8) if row & (1 << axis)), Q()
                )
            total += Q(weight) / denominator * measure
    return total


def replay_tail(groups, multiplicity, order):
    low_center, low_radius = center_radius(LOW_Q)
    high_center, high_radius = center_radius(HIGH_Q)
    low_measure = sinh_log(LOW_Q[1]) - sinh_log(LOW_Q[0])
    high_measure = sinh_log(HIGH_Q[1]) - sinh_log(HIGH_Q[0])
    measure = high_measure ** (1 + multiplicity) * low_measure ** (7 - multiplicity)
    total = Q()
    for subset in subsets(multiplicity):
        active = frozenset((1,) + subset)
        centers = tuple(high_center if axis in active else low_center for axis in range(8))
        radii = tuple(high_radius if axis in active else low_radius for axis in range(8))
        subtotal = Q()
        for rows, weight in groups.items():
            subtotal += abs(weight) * term_tail(rows, centers, radii, order + 1)
        total += measure * subtotal
    return total


def quadrature(groups, multiplicity, order, absolute_weights=False, wrong_measure=False):
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
    box_totals = {}
    for subset in subsets(multiplicity):
        active = frozenset((1,) + subset)
        axis_nodes = []
        axis_weights = []
        for axis in range(8):
            lo, hi = high_y if axis in active else low_y
            axis_nodes.append((lo + hi) / 2 + (hi - lo) / 2 * nodes)
            axis_weights.append((hi - lo) / 2 * weights)
        box_total = 0.0
        for indices in product(range(order), repeat=8):
            y = np.array([axis_nodes[axis][indices[axis]] for axis in range(8)])
            c = np.sqrt(1 + y * y)
            denominators = 256.0 + np.einsum("gka,a->gk", rows, c)
            value = np.sum(signed_weights / np.prod(denominators, axis=1))
            measure = np.prod([axis_weights[axis][indices[axis]] for axis in range(8)])
            if wrong_measure:
                measure /= np.prod(c)
            box_total += measure * value
        box_totals[subset] = box_total
        total += box_total
    return total, box_totals


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

    layer_rows = {row["multiplicity"]: row for row in record["new_multiplicity_layers"]}
    for multiplicity, order in LAYER_ORDERS.items():
        layer = layer_rows[multiplicity]
        degree_zero = exact_degree_zero(groups, multiplicity)
        recorded_zero = arb(layer["complete_raw_head_by_degree"][0])
        assert recorded_zero.contains(arb(degree_zero.numerator) / degree_zero.denominator)
        tail = replay_tail(groups, multiplicity, order)
        assert str(tail) == layer["complete_raw_absolute_tail_upper"]
        q2, _ = quadrature(groups, multiplicity, 2)
        q3, boxes3 = quadrature(groups, multiplicity, 3)
        interval = layer["complete_raw_integral_interval"]
        assert float(arb(interval["lower"]).lower()) < q2 < float(arb(interval["upper"]).upper())
        assert float(arb(interval["lower"]).lower()) < q3 < float(arb(interval["upper"]).upper())
        assert abs(q3 - q2) < max(1e-35, abs(q3) * 2e-4)
        if multiplicity == 3:
            assert q2 > 0 and q3 > 0
            values = tuple(boxes3.values())
            assert max(values) - min(values) > 1e-34
            dominant = max(boxes3, key=lambda subset: abs(boxes3[subset]))
            assert abs(q3 - boxes3[dominant]) > 1e-33

    absolute, _ = quadrature(groups, 3, 2, absolute_weights=True)
    wrong, _ = quadrature(groups, 3, 2, wrong_measure=True)
    signed, _ = quadrature(groups, 3, 2)
    assert absolute > 0 and wrong != signed

    new_upper = record["certificate"]["declared_new_layers_absolute_upper"]
    enlarged = record["certificate"]["declared_enlarged_union_negative_mass_lower"]
    excess = record["composition"]["declared_negative_excess_over_k247_upper"]
    assert Q(new_upper["numerator"], new_upper["denominator"]) == Q(244, 10**22)
    assert Q(enlarged["numerator"], enlarged["denominator"]) == Q(186, 10**22)
    assert Q(excess["numerator"], excess["denominator"]) == Q(172, 10**22)
    k261_lower = json.loads(K261.read_text())["certificate"]["declared_strict_negative_mass_lower"]
    prefix = json.loads(K247.read_text())["certificate"]["complete_upper"]
    exact_margin = (
        Q(k261_lower["numerator"], k261_lower["denominator"])
        - Q(new_upper["numerator"], new_upper["denominator"])
        - Q(prefix["numerator"], prefix["denominator"])
    )
    assert exact_margin > Q(excess["numerator"], excess["denominator"])

    print("[PASS] K262 reverse orbit manifest", digest)
    print("[PASS] K262 exact degree-zero and complete-tail replay for multiplicities 0,1,3")
    print("[PASS] K262 independent q2/q3 layer controls")
    print("[PASS] K262 absolute-weight, wrong-measure, deletion and non-invariant-box controls")
    print("[PASS] K262 K261/K247 composition", float(exact_margin))


if __name__ == "__main__":
    main()
