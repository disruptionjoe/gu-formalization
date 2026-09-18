#!/usr/bin/env python3
"""K229: finite signed K221 third-shell cost stress, not an integral obstruction."""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as Q

from k224_order_six_second_shell_cost_stress import K185, K223, K221, ROOT, interval, sinh

OUT = ROOT / "lab/process/k229-order-six-third-shell-signed-cost-stress.json"
PI_LOWER = Q(31, 10)


def cells():
    for j in range(8):
        yield j, tuple([(Q(1), Q(4))] * j + [(Q(4), Q(5))] + [(Q(1), Q(5))] * (7-j))


def bound(source, bands):
    pair, measure = interval(source, bands)
    return pair, measure


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def magnitude(pair):
    return max(-pair[0], pair[1])


def generate():
    source = json.loads(K185.read_text())
    coarse_total = selected_total = (Q(0), Q(0))
    total_measure = Q(0)
    records = []
    for j, bands in cells():
        coarse, measure = bound(source, bands)
        coarse_total = add(coarse_total, coarse)
        total_measure += measure
        options = []
        for axis, (a, b) in enumerate(bands):
            cut = (a+b)/2
            left = bands[:axis] + ((a, cut),) + bands[axis+1:]
            right = bands[:axis] + ((cut, b),) + bands[axis+1:]
            pair_l, measure_l = bound(source, left)
            pair_r, measure_r = bound(source, right)
            assert measure_l+measure_r == measure
            combined = add(pair_l, pair_r)
            options.append((magnitude(combined), axis, combined, cut))
        best = min(options)
        selected_total = add(selected_total, best[2])
        records.append({
            "first_exceeding_coordinate": j,
            "coarse_interval_without_pi8": [str(x) for x in coarse],
            "coarse_measure": str(measure),
            "candidate_absolute_uppers_without_pi8": [str(x[0]) for x in options],
            "selected_axis": best[1], "selected_cut_exp_t": str(best[3]),
            "selected_interval_without_pi8": [str(x) for x in best[2]],
        })
    assert total_measure == sinh(Q(5))**8 - sinh(Q(4))**8
    assert magnitude(selected_total) < magnitude(coarse_total)
    first = json.loads(K223.read_text())
    second = json.loads((ROOT / "lab/process/k224-order-six-second-shell-cost-stress.json").read_text())
    assert Q(first["interval_without_pi8"][1]) > 0
    headroom = Q(second["combined_cube_budget_headroom"])
    assert headroom > 0
    selected_upper = magnitude(selected_total)/PI_LOWER**8
    return {
        "schema_version": "1.0", "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {name: hashlib.sha256(path.read_bytes()).hexdigest() for name, path in
                         (("k185", K185), ("k221", K221),
                          ("k224", ROOT / "lab/process/k224-order-six-second-shell-cost-stress.json"))},
        "object": "Original K185/K218 signed 1,864-term rational-cosh core with K221 cell enclosure",
        "region": "[0,log(5)]^8 minus [0,log(4)]^8",
        "partition": "First coordinate j exceeding log(4): earlier coordinates [0,log(4)], j [log(4),log(5)], later coordinates [0,log(5)]; boundaries have zero measure.",
        "candidate_family": "Eight arithmetic midpoint cuts in rational exp(t) bands per coarse cell; choose the smallest two-child exact interval magnitude, ties by axis.",
        "coarse_cell_count": 8, "candidate_count": 64, "selected_cell_count": 16,
        "exact_shell_measure": str(total_measure), "cells": records,
        "coarse_interval_without_pi8": [str(x) for x in coarse_total],
        "selected_interval_without_pi8": [str(x) for x in selected_total],
        "pi_lower_certificate": "K224 inscribed regular 12-gon proves pi>31/10.",
        "coarse_absolute_upper_using_pi_gt_31_over_10": str(magnitude(coarse_total)/PI_LOWER**8),
        "selected_absolute_upper_using_pi_gt_31_over_10": str(selected_upper),
        "remaining_all_farther_allocation": str(headroom),
        "selected_upper_to_remaining_allocation": str(selected_upper/headroom),
        "claim_ceiling": "Finite exact 8/16-cell signed-enclosure cost stress for the complete third shell only. An upper above allocation rejects this chosen certificate, not the signed integral, a finer or reanchored method, a necessary node count, K215, coalescent/quotient/reference composition, source or physics."
    }


if __name__ == "__main__":
    result = generate()
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K229 complete third-shell 8/16-cell signed cost stress")
    print("axes:", [x["selected_axis"] for x in result["cells"]])
    print("selected upper:", float(Q(result["selected_absolute_upper_using_pi_gt_31_over_10"])))
