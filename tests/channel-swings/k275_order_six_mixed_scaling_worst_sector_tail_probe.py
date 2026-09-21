#!/usr/bin/env python3
"""Independent reverse-allocation replay and hostile controls for K275."""
from __future__ import annotations

from collections import Counter
from fractions import Fraction as Q
import json
from math import factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROCESS = ROOT / "lab/process"
SOURCE = PROCESS / "k185-order-six-duffy-face-tail-wave.json"
RECORD = PROCESS / "k275-order-six-mixed-scaling-worst-sector-tail.json"
AXES = 8
DENOMINATORS = 14
GENERIC = (
    Q(5, 4), Q(17, 8), Q(9, 8), Q(13, 8),
    Q(21, 8), Q(25, 8), Q(29, 8), Q(33, 8),
)


def independent_terms(source: dict):
    catalog = source["exact_allocation_certificate"]["allocation_catalog"]
    for entry in reversed(source["complete_face_hypergraph"]["entries"]):
        outer = entry["coefficient_product"] * (2 if entry["left"] != entry["right"] else 1)
        for term in reversed(entry["terms"]):
            masks = tuple(int(value, 16) for value in
                          catalog[term["allocation_id"]]["support_masks_hex"].split(","))
            yield outer * term["leibniz_sign"], masks


def margin(masks: tuple[int, ...], face: int) -> int:
    touched = 0
    for axis in reversed(range(AXES)):
        if face & (1 << axis):
            touched |= masks[axis]
    return touched.bit_count() - face.bit_count()


def leading(items: list, axis: int) -> Q:
    total = Q(0)
    measure = Q(1)
    for other in reversed(range(AXES)):
        if other != axis:
            measure *= GENERIC[other]
    for weight, masks in reversed(items):
        touched = masks[axis]
        if touched.bit_count() != 2:
            continue
        denominator = Q(1)
        for load_index in reversed(range(DENOMINATORS)):
            if touched & (1 << load_index):
                continue
            load = Q(256)
            for other in reversed(range(AXES)):
                if other != axis and masks[other] & (1 << load_index):
                    load += GENERIC[other]
            denominator *= load
        total += Q(weight, denominator)
    return measure * total


def main() -> None:
    source = json.loads(SOURCE.read_text())
    record = json.loads(RECORD.read_text())
    items = list(independent_terms(source))
    assert len(items) == 1864

    term_hist = Counter()
    singleton_counts = Counter()
    checks = 0
    nonsingleton_min = DENOMINATORS
    for _, masks in items:
        term_min = DENOMINATORS
        for face in reversed(range(1, 1 << AXES)):
            value = margin(masks, face)
            assert value >= 1
            checks += 1
            term_min = min(term_min, value)
            if face.bit_count() >= 2:
                nonsingleton_min = min(nonsingleton_min, value)
        term_hist[term_min] += 1
        for axis in range(2, 8):
            if margin(masks, 1 << axis) == 1:
                singleton_counts[axis] += 1

    exact_checks = 0
    assert checks == record["certificate"]["term_face_checks"] == 475320; exact_checks += 1
    assert {str(k): v for k, v in sorted(term_hist.items())} == record["certificate"]["term_minimum_margin_histogram"]; exact_checks += 1
    assert {str(k): v for k, v in sorted(singleton_counts.items())} == record["certificate"]["worst_singleton_face_term_counts"]; exact_checks += 1
    assert nonsingleton_min == record["certificate"]["minimum_over_nonsingleton_faces"] == 2; exact_checks += 1

    replay_leading = {str(axis): leading(items, axis) for axis in range(2, 8)}
    expected_leading = {
        axis: Q(value) for axis, value in
        record["worst_faces"]["exact_leading_coefficients_without_common_constant_or_pi8"].items()
    }
    assert replay_leading == expected_leading; exact_checks += 1

    coefficient = Q(record["dyadic_tail"]["uniform_coefficient_rational"])
    def bound(m: int) -> Q:
        polynomial = sum((Q(7 * m, 10) ** r / factorial(r) for r in range(8)), Q(0))
        return coefficient * polynomial / 2**m
    assert bound(183) == Q(record["dyadic_tail"]["bound_at_m_183_rational"]); exact_checks += 1
    assert bound(184) == Q(record["dyadic_tail"]["bound_at_m_184_rational"]); exact_checks += 1

    hostile_checks = 0
    assert min(margin(masks, 1 << axis) for _, masks in items for axis in range(2, 8)) == 1; hostile_checks += 1
    assert min(margin(masks, face) for _, masks in items
               for face in range(1, 1 << AXES) if face.bit_count() >= 2) == 2; hostile_checks += 1
    assert any(value < 0 for value in replay_leading.values()) and any(value > 0 for value in replay_leading.values()); hostile_checks += 1
    assert min(margin(masks, 1 << axis) - 1
               for _, masks in items for axis in range(2, 8)) == 0; hostile_checks += 1

    print(f"[PASS] K275 independent reverse replay {exact_checks}/7 exact, {hostile_checks}/4 hostile")


if __name__ == "__main__":
    main()
