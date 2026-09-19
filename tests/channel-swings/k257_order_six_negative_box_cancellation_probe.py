#!/usr/bin/env python3
"""Independent reverse-order replay for K257's negative box certificate."""
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
RECORD = ROOT / "lab/process/k257-order-six-negative-box-cancellation.json"
ACTIVE_AXES = (5, 3, 1)  # deliberately reversed from the producer
INACTIVE_AXES = tuple(axis for axis in range(7, -1, -1) if axis not in ACTIVE_AXES)
Q_LO, Q_HI, STEP = Q(1792), Q(2304), Q(32)
INACTIVE_HI = Q(13, 5)
MASS_FLOOR = Q(226, 10**22)


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


def groups(items):
    result = defaultdict(lambda: [0, 0])
    for weight, supports in items:
        factors = []
        for row in range(13, -1, -1):
            active_mask = sum(
                1 << local
                for local, axis in enumerate(ACTIVE_AXES)
                if supports[axis] & (1 << row)
            )
            inactive_count = sum(
                1 for axis in INACTIVE_AXES if supports[axis] & (1 << row)
            )
            factors.append((active_mask, inactive_count))
        slot = result[tuple(sorted(factors, reverse=True))]
        slot[0 if weight > 0 else 1] += abs(weight)
    return {
        key: (positive, negative)
        for key, (positive, negative) in result.items()
        if positive or negative
    }


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


def main() -> None:
    ctx.prec = 256
    source = json.loads(K185.read_text())
    record = json.loads(RECORD.read_text())
    items = list(raw_terms(source))
    grouped = groups(items)
    assert len(items) == 1864 and len(grouped) == 318

    inactive_box = I(c(Q(1)), c(INACTIVE_HI))
    inactive_measure = s(INACTIVE_HI) ** 5
    q_cells = [(Q_LO + i * STEP, Q_LO + (i + 1) * STEP) for i in range(16)]
    c_cells = [I(c(lo), c(hi)) for lo, hi in q_cells]
    measures = [s(hi) - s(lo) for lo, hi in q_cells]

    total = arb(0)
    negative = 0
    replay_hash = hashlib.sha256()
    for i in range(15, -1, -1):
        for j in range(15, -1, -1):
            for k in range(15, -1, -1):
                value = evaluate(grouped, (c_cells[i], c_cells[j], c_cells[k]), inactive_box)
                assert value.upper() < 0
                negative += 1
                measure = measures[i] * measures[j] * measures[k] * inactive_measure
                total += (-arb(value.upper())) * A(measure)
                replay_hash.update(f"{i},{j},{k}:{value.lower()}:{value.upper()}\n".encode())

    norm = fmpq(2**8 * 256**6, factorial(5)) * fmpq(7, 22) ** 8
    normalized = arb(norm) * arb(total.lower())
    assert negative == 4096
    assert normalized > A(MASS_FLOOR)
    assert record["interval_atlas"]["strictly_negative_cells"] == negative
    assert Q(
        record["integration"]["declared_strict_negative_mass_lower"]["numerator"],
        record["integration"]["declared_strict_negative_mass_lower"]["denominator"],
    ) == MASS_FLOOR

    # Exact point controls do not use interval grouping.  The signed center is
    # negative while removing the original signs makes it positive.
    center_c = c(Q(2048))
    inactive_c = c(Q(2))
    coordinates = tuple(
        center_c if axis in ACTIVE_AXES else inactive_c for axis in range(8)
    )
    assert exact_core(items, coordinates) < 0
    assert exact_core(items, coordinates, absolute_weights=True) > 0

    k247 = json.loads(K247.read_text())
    upper = k247["certificate"]["complete_upper"]
    prefix_upper = Q(upper["numerator"], upper["denominator"])
    assert Q_LO > 15 and MASS_FLOOR > prefix_upper
    assert record["composition"]["strict_negative_excess_over_k247_upper"]["numerator"] > 0
    assert replay_hash.hexdigest() != record["interval_atlas"]["cell_bounds_sha256"]
    print("[PASS] K257 independent reverse atlas", negative)
    print("[PASS] K257 exact signed/absolute center and K247-upper composition")


if __name__ == "__main__":
    main()
