#!/usr/bin/env python3
"""Independent reverse-order raw-allocation replay of K260."""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction as Q
import hashlib
from itertools import combinations
import json
from math import factorial
from pathlib import Path

from flint import arb, ctx, fmpq


ROOT = Path(__file__).resolve().parents[2]
K185 = ROOT / "lab/process/k185-order-six-duffy-face-tail-wave.json"
K247 = ROOT / "lab/process/k247-order-six-cumulative-q15-boundary.json"
RECORD = ROOT / "lab/process/k260-order-six-integrated-pair-box-certificate.json"
PAIRS = tuple(reversed(tuple(combinations(range(2, 8), 2))))
Q_LO, Q_HI, STEP = Q(1792), Q(2304), Q(32)
INACTIVE_LO, INACTIVE_HI = Q(1), Q(13, 5)


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


def groups(items, pair):
    active_axes = (1,) + pair
    inactive_axes = tuple(axis for axis in range(7, -1, -1) if axis not in active_axes)
    result = defaultdict(lambda: [0, 0])
    for weight, supports in items:
        factors = []
        for row in range(13, -1, -1):
            active_mask = sum(
                1 << local
                for local, axis in enumerate(active_axes)
                if supports[axis] & (1 << row)
            )
            inactive_count = sum(
                1 for axis in inactive_axes if supports[axis] & (1 << row)
            )
            factors.append((active_mask, inactive_count))
        slot = result[tuple(sorted(factors, reverse=True))]
        slot[0 if weight > 0 else 1] += abs(weight)
    return {key: tuple(value) for key, value in result.items() if any(value)}


def A(value: Q) -> arb:
    return arb(value.numerator) / value.denominator


def c(q: Q) -> Q:
    return (q + 1 / q) / 2


def s(q: Q) -> Q:
    return (q - 1 / q) / 2


def I(lo: Q, hi: Q) -> arb:
    alo, ahi = A(lo), A(hi)
    return (alo + ahi) / 2 + arb(0, (ahi - alo) / 2)


def evaluate(grouped, active_boxes, inactive_box):
    total = arb(0)
    for factors, (positive_weight, negative_weight) in reversed(list(grouped.items())):
        product = arb(1)
        for active_mask, inactive_count in reversed(factors):
            denominator = arb(256) + inactive_count * inactive_box
            for local in range(2, -1, -1):
                if active_mask & (1 << local):
                    denominator += active_boxes[local]
            product *= denominator
        reciprocal = 1 / product
        total += positive_weight * reciprocal - negative_weight * reciprocal
    return total


def exact_core(items, coordinates, absolute_weights=False):
    total = Q(0)
    for weight, supports in items:
        product = 1
        for row in range(14):
            product *= 256 + sum(
                coordinates[axis]
                for axis in range(8)
                if supports[axis] & (1 << row)
            )
        total += Q(abs(weight) if absolute_weights else weight, product)
    return total


def pair_text(subset):
    return ";".join(f"{left}-{right}" for left, right in sorted(subset))


def main() -> None:
    ctx.prec = 256
    source = json.loads(K185.read_text())
    record = json.loads(RECORD.read_text())
    items = list(raw_terms(source))
    assert len(items) == 1864 and len(PAIRS) == 15
    grouped = {pair: groups(items, pair) for pair in PAIRS}

    inactive = I(c(INACTIVE_LO), c(INACTIVE_HI))
    inactive_measure = (s(INACTIVE_HI) - s(INACTIVE_LO)) ** 5
    q_cells = [(Q_LO + i * STEP, Q_LO + (i + 1) * STEP) for i in range(16)]
    c_cells = [I(c(lo), c(hi)) for lo, hi in q_cells]
    measures = [s(hi) - s(lo) for lo, hi in q_cells]
    raw_lower = {pair: arb(0) for pair in PAIRS}
    raw_upper = {pair: arb(0) for pair in PAIRS}
    for i in range(15, -1, -1):
        for j in range(15, -1, -1):
            for k in range(15, -1, -1):
                boxes = (c_cells[i], c_cells[j], c_cells[k])
                measure = A(measures[i] * measures[j] * measures[k] * inactive_measure)
                for pair in PAIRS:
                    value = evaluate(grouped[pair], boxes, inactive)
                    raw_lower[pair] += value.lower() * measure
                    raw_upper[pair] += value.upper() * measure

    norm = arb(fmpq(2**8 * 256**6, factorial(5)) * fmpq(7, 22) ** 8)
    lower = {pair: norm * raw_lower[pair] for pair in PAIRS}
    upper = {pair: norm * raw_upper[pair] for pair in PAIRS}

    passing = defaultdict(int)
    failing = defaultdict(int)
    failure_rows = []
    winners = []
    for size in range(15, 9, -1):
        for subset in reversed(list(combinations(tuple(reversed(PAIRS)), size))):
            bound = sum((upper[pair] for pair in subset), arb(0))
            if bound < 0:
                passing[str(size)] += 1
                winners.append((size, tuple(sorted(subset)), bound))
            else:
                failing[str(size)] += 1
                failure_rows.append(f"{size}:{pair_text(subset)}")

    cert = record["integrated_subset_certificate"]
    assert dict(sorted(passing.items(), key=lambda row: int(row[0]))) == {
        key: value for key, value in cert["passing_subsets_by_size"].items() if value
    }
    assert {str(size): failing[str(size)] for size in range(10, 16)} == cert["failing_subsets_by_size"]
    digest = hashlib.sha256(("\n".join(sorted(failure_rows)) + "\n").encode()).hexdigest()
    assert digest == cert["failure_subset_sha256"]
    maximum = max(size for size, _, _ in winners)
    assert maximum == cert["maximum_certifiable_cardinality"] == 10
    recorded = {
        tuple(map(tuple, row["exceptional_pairs"]))
        for row in cert["maximal_subsets"]
    }
    reproduced = {subset for size, subset, _ in winners if size == maximum}
    assert reproduced == recorded

    selected = tuple(map(tuple, record["selected_ten_box_bundle"]["exceptional_pairs"]))
    selected_upper = sum((upper[pair] for pair in selected), arb(0))
    selected_lower = sum((lower[pair] for pair in selected), arb(0))
    assert selected_upper < 0 and selected_lower < selected_upper
    floor_row = record["selected_ten_box_bundle"]["declared_strict_negative_mass_lower"]
    floor = Q(floor_row["numerator"], floor_row["denominator"])
    assert -selected_upper > A(floor)

    center_high, center_low = c(Q(2048)), c(Q(2))
    signed_sum = Q(0)
    absolute_sum = Q(0)
    for pair in selected:
        coordinates = tuple(
            center_high if axis in (1,) + pair else center_low
            for axis in range(8)
        )
        signed_sum += exact_core(items, coordinates)
        absolute_sum += exact_core(items, coordinates, absolute_weights=True)
    assert absolute_sum > 0 and signed_sum != absolute_sum

    prefix = json.loads(K247.read_text())["certificate"]["complete_upper"]
    prefix_upper = Q(prefix["numerator"], prefix["denominator"])
    assert floor > prefix_upper
    assert Q_LO > INACTIVE_HI and len(selected) == 10

    print("[PASS] K260 independent integrated maximum", maximum)
    print("[PASS] K260 reverse failure digest", digest)
    print("[PASS] K260 exact center, mass, disjointness and K247 controls")


if __name__ == "__main__":
    main()
