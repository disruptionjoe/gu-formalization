#!/usr/bin/env python3
"""Independent raw-allocation, tail, quadrature and domain controls for K263."""
from __future__ import annotations

from fractions import Fraction as Q
from hashlib import sha256
import json

from flint import arb, ctx

from k262_order_six_low_through_three_high_multiplicity_integral_probe import (
    K185,
    K230,
    exact_degree_zero,
    independent_groups,
    quadrature,
    raw_terms,
    replay_tail,
)
from k225_order_six_diagonal_cancellation import ROOT


RECORD = ROOT / "lab/process/k263-order-six-four-high-multiplicity-integral.json"
MULTIPLICITY = 4
ORDER = 6


def main() -> None:
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

    layer = record["four_high_layer"]
    degree_zero = exact_degree_zero(groups, MULTIPLICITY)
    recorded_zero = arb(layer["complete_raw_head_by_degree"][0])
    assert recorded_zero.contains(arb(degree_zero.numerator) / degree_zero.denominator)
    tail = replay_tail(groups, MULTIPLICITY, ORDER)
    assert str(tail) == layer["complete_raw_absolute_tail_upper"]

    q2, boxes2 = quadrature(groups, MULTIPLICITY, 2)
    q3, boxes3 = quadrature(groups, MULTIPLICITY, 3)
    interval = layer["complete_raw_integral_interval"]
    lower = float(arb(interval["lower"]).lower())
    upper = float(arb(interval["upper"]).upper())
    assert 0 < lower < q2 < upper
    assert 0 < lower < q3 < upper
    assert abs(q3 - q2) < abs(q3) * 2e-4

    absolute, _ = quadrature(groups, MULTIPLICITY, 2, absolute_weights=True)
    wrong, _ = quadrature(groups, MULTIPLICITY, 2, wrong_measure=True)
    assert absolute > q2 > 0 and wrong != q2
    assert abs(q3 - sum(boxes3.values())) < 1e-42
    dropped = q3 - next(iter(boxes3.values()))
    assert dropped < 0 < q3
    single_box = next(iter(boxes2.values()))
    assert single_box != q2 and len(boxes2) == 15

    declared = record["certificate"]["declared_strict_positive_mass_lower"]
    assert Q(declared["numerator"], declared["denominator"]) == Q(42, 10**21)
    composition = record["zero_through_four_composition"]["normalized_integral_interval"]
    assert arb(composition["lower"]) < 0 < arb(composition["upper"])

    print("[PASS] K263 reverse orbit manifest", digest)
    print("[PASS] K263 exact degree-zero and complete-tail replay")
    print("[PASS] K263 independent q2/q3 positive layer controls")
    print("[PASS] K263 absolute-weight, wrong-measure, deletion and single-box controls")
    print("[PASS] K263 zero-through-four composition remains sign-unresolved")


if __name__ == "__main__":
    main()
