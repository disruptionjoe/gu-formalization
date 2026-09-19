#!/usr/bin/env python3
"""Independent raw-allocation replay of K258's adjacent-box bundle."""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction as Q
import hashlib
import json
from math import factorial
from pathlib import Path

from flint import arb, ctx, fmpq


ROOT = Path(__file__).resolve().parents[2]
K185 = ROOT / "lab/process/k185-order-six-duffy-face-tail-wave.json"
K247 = ROOT / "lab/process/k247-order-six-cumulative-q15-boundary.json"
RECORD = ROOT / "lab/process/k258-order-six-adjacent-box-bundle.json"
PAIRS = ((2, 7), (2, 6), (2, 4), (5, 7), (5, 6), (4, 5), (3, 5), (2, 5))
HOSTILE_ADDITION = (4, 7)
Q_LO, Q_HI, STEP = Q(1792), Q(2304), Q(32)
INACTIVE_HI = Q(13, 5)
MASS_FLOOR = Q(151, 10**22)


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
        total += positive_weight / product - negative_weight / product
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


def main() -> None:
    ctx.prec = 256
    source = json.loads(K185.read_text())
    record = json.loads(RECORD.read_text())
    items = list(raw_terms(source))
    assert len(items) == 1864
    grouped = {pair: groups(items, pair) for pair in PAIRS}
    hostile = groups(items, HOSTILE_ADDITION)

    recorded_pairs = {tuple(row) for row in record["bundle"]["selected_exceptional_pairs"]}
    assert recorded_pairs == set(PAIRS)
    assert Q_LO > INACTIVE_HI
    for left, right in PAIRS:
        assert 2 <= left < right <= 7
    assert len(set(PAIRS)) == 8

    inactive_box = I(c(Q(1)), c(INACTIVE_HI))
    inactive_measure = s(INACTIVE_HI) ** 5
    q_cells = [(Q_LO + i * STEP, Q_LO + (i + 1) * STEP) for i in range(16)]
    c_cells = [I(c(lo), c(hi)) for lo, hi in q_cells]
    measures = [s(hi) - s(lo) for lo, hi in q_cells]

    negative = 0
    hostile_failure = False
    total_mass = arb(0)
    replay_hash = hashlib.sha256()
    component_negative = {pair: 0 for pair in PAIRS}
    component_positive = {pair: 0 for pair in PAIRS}
    for i in range(15, -1, -1):
        for j in range(15, -1, -1):
            for k in range(15, -1, -1):
                boxes = (c_cells[i], c_cells[j], c_cells[k])
                bundle = arb(0)
                for pair in PAIRS:
                    value = evaluate(grouped[pair], boxes, inactive_box)
                    component_negative[pair] += int(value.upper() < 0)
                    component_positive[pair] += int(value.lower() > 0)
                    bundle += value
                assert bundle.upper() < 0
                negative += 1
                hostile_bundle = bundle + evaluate(hostile, boxes, inactive_box)
                hostile_failure |= hostile_bundle.upper() >= 0
                measure = measures[i] * measures[j] * measures[k] * inactive_measure
                total_mass += (-arb(bundle.upper())) * A(measure)
                replay_hash.update(f"{i},{j},{k}:{bundle.lower()}:{bundle.upper()}\n".encode())

    norm = fmpq(2**8 * 256**6, factorial(5)) * fmpq(7, 22) ** 8
    normalized = arb(norm) * arb(total_mass.lower())
    assert negative == 4096 and normalized > A(MASS_FLOOR)
    assert hostile_failure
    assert record["interval_atlas"]["strictly_negative_bundle_cells"] == negative
    assert replay_hash.hexdigest() != record["interval_atlas"]["cell_bounds_sha256"]

    component_rows = {
        tuple(row["exceptional_pair"]): row
        for row in record["bundle"]["component_boxes"]
    }
    for pair in PAIRS:
        assert component_rows[pair]["strictly_negative_cells"] == component_negative[pair]
        assert component_rows[pair]["strictly_positive_cells"] == component_positive[pair]

    center_high = c(Q(2048))
    center_low = c(Q(2))
    signed_sum = Q(0)
    absolute_sum = Q(0)
    for pair in PAIRS:
        coordinates = tuple(
            center_high if axis in (1,) + pair else center_low
            for axis in range(8)
        )
        signed_sum += exact_core(items, coordinates)
        absolute_sum += exact_core(items, coordinates, absolute_weights=True)
    assert signed_sum < 0 and absolute_sum > 0

    floor_row = record["integration"]["declared_strict_bundle_negative_mass_lower"]
    assert Q(floor_row["numerator"], floor_row["denominator"]) == MASS_FLOOR
    prefix = json.loads(K247.read_text())["certificate"]["complete_upper"]
    prefix_upper = Q(prefix["numerator"], prefix["denominator"])
    assert MASS_FLOOR > prefix_upper
    print("[PASS] K258 independent reverse bundle atlas", negative)
    print("[PASS] K258 exact center, disjointness, hostile addition and K247 composition")


if __name__ == "__main__":
    main()
