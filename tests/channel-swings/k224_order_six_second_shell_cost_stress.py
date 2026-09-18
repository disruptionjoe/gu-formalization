#!/usr/bin/env python3
"""K224: exact second-shell K221 enclosure and finite axis-split stress."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json

from k222_order_six_first_middle_shell_cover import (
    K185, K221, ROOT, SCALE, cosh, sinh, signed_quadratic_bounds,
)

K223 = ROOT / "lab/process/k223-order-six-anisotropic-first-shell.json"
OUT = ROOT / "lab/process/k224-order-six-second-shell-cost-stress.json"


def outer_cells():
    """First coordinate beyond log(3), through log(4)."""
    for j in range(8):
        bands = tuple((Q(1), Q(3)) if k < j else
                      (Q(3), Q(4)) if k == j else
                      (Q(1), Q(4)) for k in range(8))
        yield j, bands


def interval(source: dict, bands: tuple) -> tuple[tuple[Q, Q], Q]:
    lower = tuple(cosh(a) for a, _ in bands)
    upper = tuple(cosh(b) for _, b in bands)
    weight = Q(1)
    for a, b in bands:
        weight *= sinh(b)-sinh(a)
    core = signed_quadratic_bounds(source, lower, upper)["intersection_core"]
    return (SCALE*weight*core[0], SCALE*weight*core[1]), weight


def encoded_cell(source: dict, bands: tuple) -> dict:
    pair, weight = interval(source, bands)
    return {"exp_t_bands": [[str(a), str(b)] for a, b in bands],
            "product_sinh_difference": str(weight),
            "interval_without_pi8": [str(x) for x in pair]}


def add(a: tuple[Q, Q], b: tuple[Q, Q]) -> tuple[Q, Q]:
    return a[0]+b[0], a[1]+b[1]


def magnitude(pair: tuple[Q, Q]) -> Q:
    return max(-pair[0], pair[1])


def generate() -> dict:
    source = json.loads(K185.read_text())
    first = json.loads(K223.read_text())
    records = []
    coarse_total = refined_total = (Q(0), Q(0))
    shell_measure = Q(0)
    axes = []
    for j, bands in outer_cells():
        coarse = encoded_cell(source, bands)
        coarse_pair = tuple(map(Q, coarse["interval_without_pi8"]))
        coarse_total = add(coarse_total, coarse_pair)
        alternatives = []
        for axis, (a, b) in enumerate(bands):
            m = (a+b)/2
            left = bands[:axis]+((a, m),)+bands[axis+1:]
            right = bands[:axis]+((m, b),)+bands[axis+1:]
            children = [encoded_cell(source, left), encoded_cell(source, right)]
            pair = add(*(tuple(map(Q, child["interval_without_pi8"]))
                         for child in children))
            assert sum((Q(x["product_sinh_difference"]) for x in children), Q(0)) == Q(coarse["product_sinh_difference"])
            alternatives.append({"axis": axis, "cut_exp_t": str(m),
                                 "absolute_upper_without_pi8": str(magnitude(pair)),
                                 "interval_without_pi8": [str(x) for x in pair],
                                 "children": children})
        chosen = min(alternatives, key=lambda x: (Q(x["absolute_upper_without_pi8"]), x["axis"]))
        refined_total = add(refined_total, tuple(map(Q, chosen["interval_without_pi8"])))
        shell_measure += Q(coarse["product_sinh_difference"])
        axes.append(chosen["axis"])
        records.append({"first_exceeding_coordinate": j, "coarse": coarse,
                        "candidate_absolute_uppers_without_pi8":
                            [x["absolute_upper_without_pi8"] for x in alternatives],
                        "selected": chosen})
    assert shell_measure == sinh(Q(4))**8-sinh(Q(3))**8
    coarse_bound = magnitude(coarse_total)/3**8
    refined_bound = magnitude(refined_total)/3**8
    assert refined_bound < coarse_bound
    # Inscribed regular 12-gon: pi > 12 sin(pi/12)
    # = 3(sqrt(6)-sqrt(2)) > 3(2449/1000-1415/1000) > 31/10.
    assert Q(2449,1000)**2 < 6 and Q(1415,1000)**2 > 2
    assert 3*(Q(2449,1000)-Q(1415,1000)) > Q(31,10)
    better_pi = Q(31,10)
    coarse_better = magnitude(coarse_total)/better_pi**8
    refined_better = magnitude(refined_total)/better_pi**8
    budget = Q(1, 10**21)
    first_bound = Q(first["interval_without_pi8"][1])/better_pi**8
    inner = Q(json.loads(K221.read_text())["full_inner_comparison"]
              ["absolute_upper_rational_using_pi_gt_3"])
    cube_bound = refined_better+first_bound+inner
    assert coarse_better > budget and refined_better < budget
    assert cube_bound < budget
    return {
        "schema_version": "1.0", "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {name: hashlib.sha256(path.read_bytes()).hexdigest()
                         for name, path in (("k185", K185), ("k221", K221),
                                            ("k223", K223))},
        "object": "K218 exact signed eight-auxiliary core on the complete second middle shell",
        "region": "[0,log(4)]^8 minus [0,log(3)]^8",
        "partition": "First coordinate j exceeding log(3): preceding coordinates [0,log(3)], j in [log(3),log(4)], subsequent coordinates [0,log(4)]. Boundaries are measure zero.",
        "candidate_family": "For each of eight first-exceeding cells, test all eight single axis arithmetic midpoint bisections of rational exp(t) bands. Select the smallest exact two-child local absolute K221/K220 upper; tie by lowest axis.",
        "candidate_count": 64, "coarse_cell_count": 8, "selected_cell_count": 16,
        "exact_shell_measure": str(shell_measure), "cells": records,
        "coarse": {"interval_without_pi8": [str(x) for x in coarse_total],
                   "absolute_upper_using_pi_gt_3": str(coarse_bound),
                   "absolute_upper_using_pi_gt_31_over_10": str(coarse_better)},
        "selected": {"axes": axes, "interval_without_pi8": [str(x) for x in refined_total],
                     "absolute_upper_using_pi_gt_3": str(refined_bound),
                     "absolute_upper_using_pi_gt_31_over_10": str(refined_better)},
        "pi_lower_certificate": "Inscribed regular 12-gon: pi>3(sqrt(6)-sqrt(2))>3(2449/1000-1415/1000)>31/10; the squared rational inequalities have the correct signs.",
        "target_absolute_budget": str(budget),
        "coarse_upper_to_budget": str(coarse_bound/budget),
        "selected_upper_to_budget_using_pi_gt_31_over_10": str(refined_better/budget),
        "combined_inner_first_second_cube_absolute_upper": str(cube_bound),
        "combined_cube_budget_headroom": str(budget-cube_bound),
        "claim_ceiling": "The selected 16-cell second shell and combined [0,log(4)]^8 cube meet 10^-21 using pi>31/10; the eight-cell second shell does not certify it with this rational bound. This is a finite enclosure-cost test, not a cover to K215, a necessary node theorem or a complete order-six prefix. No coalescent, quotient, common-reference, source or physics conclusion."
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2)+"\n")
    print("[PASS] K224 exact second-shell 8/16-cell and 64-axis matrix")
    print("axes:", result["selected"]["axes"])
    print("absolute upper (pi>31/10):", f"{float(Q(result['selected']['absolute_upper_using_pi_gt_31_over_10'])):.12e}")
