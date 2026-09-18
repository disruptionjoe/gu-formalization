#!/usr/bin/env python3
"""Independent K223 cover/measure/raw-term and selected-axis audit."""
from __future__ import annotations

from fractions import Fraction as Q
import hashlib
import itertools
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from k219_order_six_signed_auxiliary_cell_enclosure import SCALE
from k221_order_six_signed_quadratic_cell_enclosure_probe import raw_point
from k221_order_six_signed_quadratic_cell_enclosure import signed_quadratic_bounds

SOURCE = ROOT / "lab/process/k185-order-six-duffy-face-tail-wave.json"
MANIFEST = ROOT / "lab/process/k223-order-six-anisotropic-first-shell.json"


def sh(r: Q) -> Q:
    return (r*r-1)/(2*r)


def ch(r: Q) -> Q:
    return (r*r+1)/(2*r)


def run() -> None:
    doc = json.loads(MANIFEST.read_text())
    source = json.loads(SOURCE.read_text())
    paths = {"k185": SOURCE,
             "k221": ROOT / "lab/process/k221-order-six-signed-quadratic-cell-enclosure.json",
             "k222": ROOT / "lab/process/k222-order-six-first-middle-shell-cover.json"}
    assert all(hashlib.sha256(paths[k].read_bytes()).hexdigest() == v
               for k, v in doc["input_sha256"].items())
    previous = json.loads(paths["k222"].read_text())
    assert doc["candidate_count"] == 64 and doc["selected_cell_count"] == 16
    assert [r["first_exceeding_coordinate"] for r in doc["cells"]] == list(range(8))
    total = [Q(0), Q(0)]
    weight_sum = Q(0)
    children = []
    for record in doc["cells"]:
        j = record["first_exceeding_coordinate"]
        axes = record["candidate_absolute_uppers_without_pi8"]
        assert len(axes) == 8
        old = previous["coarse"]["cells"][j]
        low = tuple(map(Q, old["cosh_lower"]))
        high = tuple(map(Q, old["cosh_upper"]))
        original_weight = Q(old["product_sinh_difference"])
        for axis, value in enumerate(axes):
            a,b = ((Q(1),Q(2)) if axis < j else
                   (Q(2),Q(3)) if axis == j else (Q(1),Q(3)))
            m = (a+b)/2
            c = ch(m)
            halves = ((low, tuple(c if k==axis else high[k] for k in range(8)),
                       original_weight*(sh(m)-sh(a))/(sh(b)-sh(a))),
                      (tuple(c if k==axis else low[k] for k in range(8)), high,
                       original_weight*(sh(b)-sh(m))/(sh(b)-sh(a))))
            pair = [Q(0), Q(0)]
            for lower, upper, w in halves:
                bnd = signed_quadratic_bounds(source, lower, upper)["intersection_core"]
                for k in range(2):
                    pair[k] += SCALE*w*bnd[k]
            assert Q(value) == max(-pair[0], pair[1])
            if axis == record["selected"]["axis"]:
                assert record["selected"]["cut_exp_t"] == str(m)
                assert tuple(pair) == tuple(map(Q,record["selected"]["interval_without_pi8"]))
                for stored, (lower, upper, w) in zip(record["selected"]["children"], halves):
                    assert tuple(map(Q,stored["cosh_lower"])) == lower
                    assert tuple(map(Q,stored["cosh_upper"])) == upper
                    assert Q(stored["product_sinh_difference"]) == w
                    midpoint = tuple((lower[k]+upper[k])/2 for k in range(8))
                    raw = SCALE*w*raw_point(source, midpoint)
                    lo,hi = map(Q,stored["interval_without_pi8"])
                    assert lo <= raw <= hi
                    children.append((lower,upper))
                    weight_sum += w
        assert Q(axes[record["selected"]["axis"]]) == min(map(Q,axes))
        for k in range(2):
            total[k] += Q(record["selected"]["interval_without_pi8"][k])
    assert len(children) == 16
    assert weight_sum == sh(Q(3))**8-sh(Q(2))**8 == Q(doc["exact_shell_measure"])
    assert tuple(total) == tuple(map(Q,doc["interval_without_pi8"]))
    assert Q(doc["absolute_upper_using_pi_gt_3"]) == max(-total[0],total[1])/3**8
    assert Q(doc["absolute_upper_using_pi_gt_3"]) < Q(previous["refined"]["absolute_upper_using_pi_gt_3"])
    for labels in itertools.product((Q(3,2),Q(9,4),Q(11,4)),repeat=8):
        point=tuple(ch(x) for x in labels)
        count=sum(all(lo[k]<point[k]<hi[k] for k in range(8)) for lo,hi in children)
        assert count == (0 if all(x<2 for x in labels) else 1)
    # Hostile controls: wrong optimizing direction and duplicated child lose equality.
    assert Q(doc["cells"][0]["candidate_absolute_uppers_without_pi8"][0]) > min(
        map(Q,doc["cells"][0]["candidate_absolute_uppers_without_pi8"]))
    assert weight_sum+Q(doc["cells"][0]["selected"]["children"][0]["product_sinh_difference"]) != weight_sum
    print("[PASS] independent 64-axis replay, 3^8 cover, exact measures and 16 raw signed midpoints")


if __name__ == "__main__":
    run()
