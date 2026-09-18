#!/usr/bin/env python3
"""K223: exact 64-candidate anisotropic one-bisection first-shell pilot."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json

from k222_order_six_first_middle_shell_cover import (
    K185, K221, OUT as K222, ROOT, SCALE, cells, cosh, sinh,
    signed_quadratic_bounds,
)

OUT = ROOT / "lab/process/k223-order-six-anisotropic-first-shell.json"


def candidate(source: dict, original: tuple, axis: int) -> dict:
    j, _, _, low, high, weight = original
    a, b = ((Q(1), Q(2)) if axis < j else
            (Q(2), Q(3)) if axis == j else (Q(1), Q(3)))
    midpoint_exp = (a + b) / 2
    cut = cosh(midpoint_exp)
    left_upper, right_lower = list(high), list(low)
    left_upper[axis] = right_lower[axis] = cut
    left_weight = weight * (sinh(midpoint_exp)-sinh(a))/(sinh(b)-sinh(a))
    right_weight = weight-left_weight
    assert left_weight > 0 and right_weight > 0
    children = []
    total = [Q(0), Q(0)]
    for lower, upper, measure in ((low, tuple(left_upper), left_weight),
                                  (tuple(right_lower), high, right_weight)):
        pair = signed_quadratic_bounds(source, lower, upper)["intersection_core"]
        scaled = tuple(SCALE*measure*x for x in pair)
        total = [total[k]+scaled[k] for k in range(2)]
        children.append({"cosh_lower": [str(x) for x in lower],
                         "cosh_upper": [str(x) for x in upper],
                         "product_sinh_difference": str(measure),
                         "interval_without_pi8": [str(x) for x in scaled]})
    assert left_weight+right_weight == weight
    return {"axis": axis, "cut_exp_t": str(midpoint_exp),
            "absolute_upper_without_pi8": str(max(-total[0], total[1])),
            "interval_without_pi8": [str(x) for x in total],
            "children": children}


def generate() -> dict:
    source = json.loads(K185.read_text())
    previous = json.loads(K222.read_text())
    records = []
    global_interval = [Q(0), Q(0)]
    all_weight = Q(0)
    for original in cells(False):
        j = original[0]
        candidates = [candidate(source, original, axis) for axis in range(8)]
        best = min(candidates, key=lambda row: (Q(row["absolute_upper_without_pi8"]),
                                                 row["axis"]))
        for k in range(2):
            global_interval[k] += Q(best["interval_without_pi8"][k])
        all_weight += sum((Q(c["product_sinh_difference"])
                           for c in best["children"]), Q(0))
        records.append({"first_exceeding_coordinate": j,
                        "candidate_absolute_uppers_without_pi8":
                            [row["absolute_upper_without_pi8"] for row in candidates],
                        "selected": best})
    assert all_weight == Q(previous["coarse"]["exact_shell_measure"])
    bound = max(-global_interval[0], global_interval[1])/3**8
    prior = Q(previous["refined"]["absolute_upper_using_pi_gt_3"])
    assert bound < prior
    return {
        "schema_version": "1.0", "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {name: hashlib.sha256(path.read_bytes()).hexdigest()
                         for name, path in (("k185", K185), ("k221", K221),
                                            ("k222", K222))},
        "object": "K218's original signed eight-auxiliary core on K222's first middle shell",
        "candidate_family": "For each K222 first-exceeding cell, bisect one of its eight coordinate exp(t) bands [1,2], [2,3] or [1,3] at its rational arithmetic midpoint. Choose the axis minimizing the exact K221/K220-intersected two-child local absolute interval bound; ties go to the lowest axis. Exactly eight alternatives are checked for each of eight disjoint cells, yielding sixteen selected cells.",
        "optimality_scope": "Minimum local absolute bound among these eight prescribed midpoint axes on each of K222's eight cells; no globally optimal cover or asymptotic-cost theorem.",
        "cells": records, "candidate_count": 64, "selected_cell_count": 16,
        "exact_shell_measure": str(all_weight),
        "interval_without_pi8": [str(x) for x in global_interval],
        "absolute_upper_using_pi_gt_3": str(bound),
        "k222_same_count_refined_upper_using_pi_gt_3": str(prior),
        "ratio_to_k222_same_count": str(bound/prior),
        "claim_ceiling": "A strictly sharper finite 16-cell first-shell enclosure than K222, not a cover toward 215 log(2), full quotient/coalescent/reference composition, accurate signed prefix, source/physics or ledger result."
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K223 exact eight-by-eight midpoint-axis matrix")
    print("selected axes:", [cell["selected"]["axis"] for cell in result["cells"]])
    print("absolute ceiling:", f"{float(Q(result['absolute_upper_using_pi_gt_3'])):.12e}")
