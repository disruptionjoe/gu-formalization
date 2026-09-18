#!/usr/bin/env python3
"""Independent K224 partition, 64-choice, measure and raw-term replay."""
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
from k221_order_six_signed_quadratic_cell_enclosure import signed_quadratic_bounds
from k221_order_six_signed_quadratic_cell_enclosure_probe import raw_point

MANIFEST = ROOT / "lab/process/k224-order-six-second-shell-cost-stress.json"
INPUTS = {"k185": ROOT / "lab/process/k185-order-six-duffy-face-tail-wave.json",
          "k221": ROOT / "lab/process/k221-order-six-signed-quadratic-cell-enclosure.json",
          "k223": ROOT / "lab/process/k223-order-six-anisotropic-first-shell.json"}


def ch(r: Q) -> Q:
    return (r*r+1)/(2*r)


def sh(r: Q) -> Q:
    return (r*r-1)/(2*r)


def main() -> None:
    doc = json.loads(MANIFEST.read_text())
    source = json.loads(INPUTS["k185"].read_text())
    previous = json.loads(INPUTS["k223"].read_text())
    for name, path in INPUTS.items():
        assert hashlib.sha256(path.read_bytes()).hexdigest() == doc["input_sha256"][name]
    assert doc["candidate_count"] == 64 and doc["selected_cell_count"] == 16
    assert [x["first_exceeding_coordinate"] for x in doc["cells"]] == list(range(8))
    coarse_total = [Q(0), Q(0)]
    selected_total = [Q(0), Q(0)]
    weights = Q(0)
    children_bands = []
    for j, record in enumerate(doc["cells"]):
        expected = tuple((Q(1),Q(3)) if k<j else
                         (Q(3),Q(4)) if k==j else
                         (Q(1),Q(4)) for k in range(8))
        coarse = record["coarse"]
        assert tuple(tuple(map(Q,x)) for x in coarse["exp_t_bands"]) == expected
        base_weight = Q(1)
        for a,b in expected:
            base_weight *= sh(b)-sh(a)
        assert Q(coarse["product_sinh_difference"]) == base_weight
        weights += base_weight
        for k in range(2):
            coarse_total[k] += Q(coarse["interval_without_pi8"][k])
        alternatives = record["candidate_absolute_uppers_without_pi8"]
        assert len(alternatives) == 8
        for axis,(a,b) in enumerate(expected):
            cut = (a+b)/2
            pair = [Q(0),Q(0)]
            child_weight = Q(0)
            for half, (left,right) in enumerate(((a,cut),(cut,b))):
                bands = expected[:axis]+((left,right),)+expected[axis+1:]
                low = tuple(ch(x) for x,_ in bands)
                high = tuple(ch(y) for _,y in bands)
                w = base_weight*(sh(right)-sh(left))/(sh(b)-sh(a))
                core = signed_quadratic_bounds(source, low, high)["intersection_core"]
                for k in range(2):
                    pair[k] += SCALE*w*core[k]
                child_weight += w
                if axis == record["selected"]["axis"]:
                    stored = record["selected"]["children"][half]
                    assert tuple(tuple(map(Q,x)) for x in stored["exp_t_bands"]) == bands
                    assert Q(stored["product_sinh_difference"]) == w
                    midpoint = tuple((x+y)/2 for x,y in zip(low,high))
                    raw = SCALE*w*raw_point(source, midpoint)
                    lo,hi = map(Q,stored["interval_without_pi8"])
                    assert lo <= raw <= hi
                    children_bands.append(bands)
            assert child_weight == base_weight
            assert Q(alternatives[axis]) == max(-pair[0],pair[1])
            if axis == record["selected"]["axis"]:
                assert Q(record["selected"]["cut_exp_t"]) == cut
                assert tuple(pair) == tuple(map(Q,record["selected"]["interval_without_pi8"]))
                for k in range(2):
                    selected_total[k] += pair[k]
        assert Q(alternatives[record["selected"]["axis"]]) == min(map(Q,alternatives))
    assert len(children_bands) == 16
    assert weights == sh(Q(4))**8-sh(Q(3))**8 == Q(doc["exact_shell_measure"])
    assert tuple(coarse_total) == tuple(map(Q,doc["coarse"]["interval_without_pi8"]))
    assert tuple(selected_total) == tuple(map(Q,doc["selected"]["interval_without_pi8"]))
    coarse_upper = max(-coarse_total[0],coarse_total[1])/3**8
    selected_upper = max(-selected_total[0],selected_total[1])/3**8
    assert Q(doc["coarse"]["absolute_upper_using_pi_gt_3"]) == coarse_upper
    assert Q(doc["selected"]["absolute_upper_using_pi_gt_3"]) == selected_upper
    assert selected_upper < coarse_upper
    assert Q(2449,1000)**2 < 6 and Q(1415,1000)**2 > 2
    assert 3*(Q(2449,1000)-Q(1415,1000)) > Q(31,10)
    p = Q(31,10)
    coarse_better = max(-coarse_total[0],coarse_total[1])/p**8
    selected_better = max(-selected_total[0],selected_total[1])/p**8
    assert Q(doc["coarse"]["absolute_upper_using_pi_gt_31_over_10"]) == coarse_better
    assert Q(doc["selected"]["absolute_upper_using_pi_gt_31_over_10"]) == selected_better
    first_bound = max(-Q(previous["interval_without_pi8"][0]),
                      Q(previous["interval_without_pi8"][1]))/p**8
    inner_doc = json.loads(INPUTS["k221"].read_text())
    inner = Q(inner_doc["full_inner_comparison"]["absolute_upper_rational_using_pi_gt_3"])
    cube_bound = selected_better+first_bound+inner
    budget = Q(doc["target_absolute_budget"])
    assert coarse_better > budget > cube_bound >= selected_better
    assert Q(doc["selected_upper_to_budget_using_pi_gt_31_over_10"]) == selected_better/budget
    assert Q(doc["combined_inner_first_second_cube_absolute_upper"]) == cube_bound
    assert Q(doc["combined_cube_budget_headroom"]) == budget-cube_bound
    # Interior samples of three bands, including the entire old [0,log(3)] cube.
    for labels in itertools.product((Q(3,2),Q(11,4),Q(15,4)),repeat=8):
        owners = sum(all(a < x < b for (a,b),x in zip(bands,labels))
                     for bands in children_bands)
        assert owners == (0 if all(x<3 for x in labels) else 1)
    # Hostile controls: a duplicated cell destroys measure, and the first
    # displayed alternate is not the minimum at least once.
    assert weights+Q(doc["cells"][0]["selected"]["children"][0]["product_sinh_difference"]) != weights
    assert any(Q(row["candidate_absolute_uppers_without_pi8"][0]) >
               min(map(Q,row["candidate_absolute_uppers_without_pi8"]))
               for row in doc["cells"])
    print("[PASS] independent second-shell 64-axis replay, 3^8 cover, exact measure, 16 raw midpoints")


if __name__ == "__main__":
    main()
