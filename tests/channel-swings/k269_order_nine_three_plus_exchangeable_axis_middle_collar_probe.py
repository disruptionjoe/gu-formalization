#!/usr/bin/env python3
"""Independent replay and hostile controls for K269."""
from __future__ import annotations

from fractions import Fraction as Q
from hashlib import sha256
import json
from math import factorial

from flint import arb, ctx, fmpq_mpoly_ctx

from k225_order_six_diagonal_cancellation import ROOT
from k262_order_six_low_through_three_high_multiplicity_integral_probe import K185, K230, independent_groups, raw_terms
from k265_order_nine_complete_binary_low_high_union_probe import as_arb, centered_moments_independent, center_radius, normalized_interval_independent, sinh_log
from k267_order_nine_exchangeable_axis_middle_collar_probe import NORMALIZATION_SERIALIZATION_SLACK, compile_independent, quadrature_box
from k269_order_nine_three_plus_exchangeable_axis_middle_collar import BLOCKS, BOUNDS, MIDDLE_COUNTS, ORDER, status_specs

RECORD = ROOT / "lab/process/k269-order-nine-three-plus-exchangeable-axis-middle-collar.json"


def quadrature_stratum(groups, middle_count, order, absolute=False, wrong=False):
    total = 0.0
    for _, fixed in BLOCKS:
        for high_multiplicity in range(7 - middle_count):
            for _, _, status in status_specs(fixed, middle_count, high_multiplicity):
                total += quadrature_box(groups, status, order, absolute, wrong)
    return total


def main() -> None:
    ctx.prec = 256
    record = json.loads(RECORD.read_text())
    items = list(raw_terms(json.loads(K185.read_text())))
    groups = independent_groups(items)
    compact = ";".join(",".join(map(str, r)) + ":" + str(w) for r, w in sorted(groups.items()))
    digest = sha256(compact.encode()).hexdigest()
    assert len(items) == 1864 and len(groups) == 307
    assert digest == json.loads(K230.read_text())["orbit_coefficient_manifest_sha256"] == record["projection"]["orbit_manifest_sha256"]

    ring = fmpq_mpoly_ctx.get([f"z{axis}" for axis in range(8)])
    variables = ring.gens()
    geometry = {}
    for name, bounds in BOUNDS.items():
        center, radius = center_radius(bounds)
        geometry[name] = {"center": center, "radius": radius, "moments": centered_moments_independent(bounds, center, ORDER), "measure": sinh_log(bounds[1]) - sinh_log(bounds[0])}

    total_head = arb(0); total_tail = Q()
    for stratum in reversed(record["middle_count_strata"]):
        middle_count = stratum["middle_axis_count"]
        stratum_head = arb(0); stratum_tail = Q()
        for block in reversed(stratum["fixed_axis_blocks"]):
            fixed = dict(BLOCKS)[block["block"]]
            block_head = arb(0); block_tail = Q()
            for layer in reversed(block["multiplicity_layers"]):
                k = layer["high_exceptional_multiplicity"]
                expected = {(tuple(b["middle_exceptional_axes"]), tuple(b["high_exceptional_axes"])): b for b in layer["box_records"]}
                layer_head = arb(0); layer_tail = Q()
                for mids, highs, status in reversed(list(status_specs(fixed, middle_count, k))):
                    hashes, heads, tail = compile_independent(groups, mids[0], highs, status, ring, variables, geometry)
                    prior = expected[(mids, highs)]
                    assert hashes == prior["coefficient_sha256_by_degree"] and tail == Q(prior["raw_absolute_tail_upper"])
                    for value, old in zip(heads, prior["raw_head_by_degree"]): assert (value - arb(old)).contains(0)
                    layer_head += sum(heads, arb(0)); layer_tail += tail
                assert (layer_head - arb(layer["complete_raw_head"])).contains(0)
                assert layer_tail == Q(layer["complete_raw_absolute_tail_upper"])
                block_head += layer_head; block_tail += layer_tail
            assert (block_head - arb(block["complete_raw_head"])).contains(0)
            assert block_tail == Q(block["complete_raw_absolute_tail_upper"])
            stratum_head += block_head; stratum_tail += block_tail
            print(f"[CHECKPOINT] K269 probe count {middle_count} {block['block']}", flush=True)
        assert (stratum_head - arb(stratum["complete_raw_head"])).contains(0)
        assert stratum_tail == Q(stratum["complete_raw_absolute_tail_upper"])
        total_head += stratum_head; total_tail += stratum_tail

    complete = record["complete_collar"]
    assert (total_head - arb(complete["complete_raw_head"])).contains(0)
    assert total_tail == Q(complete["complete_raw_absolute_tail_upper"])
    lo, hi = normalized_interval_independent(total_head, total_tail)
    interval = complete["normalized_integral_interval"]
    assert abs(lo - arb(interval["lower"])) < as_arb(NORMALIZATION_SERIALIZATION_SLACK)
    assert abs(hi - arb(interval["upper"])) < as_arb(NORMALIZATION_SERIALIZATION_SLACK)

    q2 = {m: quadrature_stratum(groups, m, 2) for m in MIDDLE_COUNTS}
    q3 = {m: quadrature_stratum(groups, m, 3) for m in MIDDLE_COUNTS}
    norm = float(2**8 * 256**6 / factorial(5)) / float(arb.pi() ** 8)
    nq2, nq3 = norm * sum(q2.values()), norm * sum(q3.values())
    assert float(arb(interval["lower"]).lower()) < nq2 < float(arb(interval["upper"]).upper())
    assert float(arb(interval["lower"]).lower()) < nq3 < float(arb(interval["upper"]).upper())
    assert abs(nq3 - nq2) < abs(nq3) * 2e-3
    dominant = 4
    assert quadrature_stratum(groups, dominant, 2, True) > q2[dominant]
    assert quadrature_stratum(groups, dominant, 2, False, True) != q2[dominant]
    assert sum(v for m, v in q3.items() if m != dominant) > 0
    assert record["domain"]["boxes"] == 890
    assert lo > as_arb(Q(1, 10**15))
    print("[PASS] K269 reverse orbit manifest", digest)
    print("[PASS] K269 independent 890-box polynomial, moment, tail and normalization replay")
    print("[PASS] K269 q2/q3 count-stratum quadratures inside interval")
    print("[PASS] K269 hostile controls")


if __name__ == "__main__":
    main()
