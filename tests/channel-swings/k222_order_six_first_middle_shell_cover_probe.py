#!/usr/bin/env python3
"""Independent first-exceeding cover and raw K185 point controls for K222."""
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

K185 = ROOT / "lab/process/k185-order-six-duffy-face-tail-wave.json"
OUT = ROOT / "lab/process/k222-order-six-first-middle-shell-cover.json"


def independent_sinh(r: Q) -> Q:
    return (r*r-1)/(2*r)


def run():
    manifest = json.loads(OUT.read_text())
    source = json.loads(K185.read_text())
    paths = {"k185": K185,
             "k218": ROOT / "lab/process/k218-order-six-exact-angular-elimination.json",
             "k219": ROOT / "lab/process/k219-order-six-signed-auxiliary-cell-enclosure.json",
             "k220": ROOT / "lab/process/k220-order-six-signed-taylor-cell-enclosure.json",
             "k221": ROOT / "lab/process/k221-order-six-signed-quadratic-cell-enclosure.json"}
    for name, digest in manifest["input_sha256"].items():
        path = paths[name]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == digest
    shell_measure = independent_sinh(Q(3))**8-independent_sinh(Q(2))**8
    assert shell_measure > 0
    for key, expected_count in (("coarse", 8), ("refined", 16)):
        part = manifest[key]
        assert part["node_count"] == expected_count == len(part["cells"])
        assert Q(part["exact_shell_measure"]) == shell_measure
        total = [Q(0), Q(0)]
        measure_sum = Q(0)
        observed_bands = set()
        for record in part["cells"]:
            j = record["first_exceeding_coordinate"]
            ra, rb = map(Q, record["exceeding_exp_t"])
            assert (j, ra, rb) not in observed_bands
            observed_bands.add((j, ra, rb))
            assert Q(2) <= ra < rb <= Q(3)
            if expected_count == 16:
                assert (ra, rb) in ((Q(2), Q(5, 2)), (Q(5, 2), Q(3)))
            else:
                assert (ra, rb) == (Q(2), Q(3))
            lower, upper = [tuple(map(Q, record[k])) for k in ("cosh_lower", "cosh_upper")]
            assert len(lower) == len(upper) == 8
            assert all(lower[k] == (ra+1/ra)/2 if k == j else lower[k] == 1 for k in range(8))
            assert all(upper[k] == Q(5, 4) if k < j else
                       upper[k] == (rb+1/rb)/2 if k == j else
                       upper[k] == Q(5, 3) for k in range(8))
            weight = (independent_sinh(rb)-independent_sinh(ra)) * (
                independent_sinh(Q(2))**j*independent_sinh(Q(3))**(7-j))
            assert weight == Q(record["product_sinh_difference"]) > 0
            measure_sum += weight
            pair = tuple(map(Q, record["intersection_interval_without_pi8"]))
            assert pair[0] <= pair[1]
            total = [total[i]+pair[i] for i in range(2)]
            midpoint = tuple((lower[i]+upper[i])/2 for i in range(8))
            point = SCALE*weight*raw_point(source, midpoint)
            assert pair[0] <= point <= pair[1]
        assert measure_sum == shell_measure
        assert tuple(total) == tuple(map(Q, part["interval_without_pi8"]))
        assert total[0] == -total[1]
        assert total[1]/3**8 == Q(part["absolute_upper_using_pi_gt_3"])
        bands = ((Q(2), Q(5, 2)), (Q(5, 2), Q(3))) if expected_count == 16 else (
            (Q(2), Q(3)),)
        assert observed_bands == {(j, ra, rb) for j in range(8) for ra, rb in bands}
        # All 3^8 interior samples have exactly one containing cell outside
        # the inner cube. This checks the *recorded* cover, not just a formula.
        for labels in itertools.product((Q(3, 2), Q(9, 4), Q(11, 4)), repeat=8):
            sample = tuple((r+1/r)/2 for r in labels)
            owners = 0
            for record in part["cells"]:
                low = tuple(map(Q, record["cosh_lower"]))
                high = tuple(map(Q, record["cosh_upper"]))
                owners += all(low[i] < sample[i] < high[i] for i in range(8))
            assert owners == (0 if all(r < 2 for r in labels) else 1)
    # Hostile controls: an endpoint-volume product and duplicate j=0 are invalid.
    first = manifest["coarse"]["cells"][0]
    assert Q(first["product_sinh_difference"]) != independent_sinh(Q(3))**8
    assert shell_measure + Q(first["product_sinh_difference"]) != shell_measure
    assert Q(manifest["refined"]["absolute_upper_using_pi_gt_3"]) < Q(
        manifest["coarse"]["absolute_upper_using_pi_gt_3"])
    k221 = json.loads(paths["k221"].read_text())
    assert Q(manifest["inner_plus_refined_first_cube_absolute_upper_using_pi_gt_3"]) == (
        Q(k221["full_inner_comparison"]["absolute_upper_rational_using_pi_gt_3"])
        + Q(manifest["refined"]["absolute_upper_using_pi_gt_3"]))
    print("[PASS] independent 3^8 cover, exact sinh weights, 24 raw 1,864-term midpoints")


if __name__ == "__main__":
    run()
