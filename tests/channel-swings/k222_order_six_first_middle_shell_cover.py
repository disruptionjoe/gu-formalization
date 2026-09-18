#!/usr/bin/env python3
"""K222: exact finite first-shell cover from K221 rational cell enclosures."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json

from k221_order_six_signed_quadratic_cell_enclosure import (
    K185, K218, K219, K220, OUT as K221, ROOT, SCALE,
    signed_quadratic_bounds,
)

OUT = ROOT / "lab/process/k222-order-six-first-middle-shell-cover.json"


def cosh(r: Q) -> Q:
    return (r + 1/r)/2


def sinh(r: Q) -> Q:
    return (r - 1/r)/2


def cells(split: bool):
    """First coordinate outside [0,log 2] partitions the first shell."""
    for j in range(8):
        bands = ((Q(2), Q(5, 2)), (Q(5, 2), Q(3))) if split else ((Q(2), Q(3)),)
        for ra, rb in bands:
            lo = tuple(cosh(ra) if k == j else Q(1) for k in range(8))
            hi = tuple(cosh(Q(2)) if k < j else
                       cosh(rb) if k == j else cosh(Q(3)) for k in range(8))
            weight = (sinh(rb)-sinh(ra))*sinh(Q(2))**j*sinh(Q(3))**(7-j)
            yield j, ra, rb, lo, hi, weight


def cover(source: dict, split: bool) -> dict:
    records = []
    total = [Q(0), Q(0)]
    k220_width = Q(0)
    for j, ra, rb, lo, hi, weight in cells(split):
        b = signed_quadratic_bounds(source, lo, hi)
        assert weight > 0
        interval = [SCALE*weight*x for x in b["intersection_core"]]
        for i in range(2):
            total[i] += interval[i]
        k220_width += SCALE*weight*(b["k220_core"][1]-b["k220_core"][0])
        records.append({
            "first_exceeding_coordinate": j,
            "exceeding_exp_t": [str(ra), str(rb)],
            "cosh_lower": [str(x) for x in lo],
            "cosh_upper": [str(x) for x in hi],
            "product_sinh_difference": str(weight),
            "intersection_interval_without_pi8": [str(x) for x in interval],
            "width_to_k220": str((interval[1]-interval[0]) /
                                  (SCALE*weight*(b["k220_core"][1]-b["k220_core"][0]))),
        })
    expected_measure = sinh(Q(3))**8-sinh(Q(2))**8
    assert sum((Q(r["product_sinh_difference"]) for r in records), Q(0)) == expected_measure
    assert len(records) == (16 if split else 8)
    assert total[0] == -total[1] and total[1] > 0
    assert total[1]-total[0] < k220_width
    return {
        "node_count": len(records),
        "exact_shell_measure": str(expected_measure),
        "interval_without_pi8": [str(x) for x in total],
        "absolute_upper_using_pi_gt_3": str(total[1]/3**8),
        "width_to_k220": str((total[1]-total[0])/k220_width),
        "cells": records,
    }


def generate() -> dict:
    source = json.loads(K185.read_text())
    coarse, refined = cover(source, False), cover(source, True)
    inner = Q(json.loads(K221.read_text())["full_inner_comparison"]
              ["absolute_upper_rational_using_pi_gt_3"])
    first_cube = inner + Q(refined["absolute_upper_using_pi_gt_3"])
    assert Q(refined["absolute_upper_using_pi_gt_3"]) < Q(coarse["absolute_upper_using_pi_gt_3"])
    assert Q(refined["absolute_upper_using_pi_gt_3"]) < Q(21, 10**24)
    assert first_cube < Q(208, 10**25)
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {name: hashlib.sha256(path.read_bytes()).hexdigest()
                         for name, path in (("k185", K185), ("k218", K218),
                                            ("k219", K219), ("k220", K220),
                                            ("k221", K221))},
        "object": "K218's original signed eight-auxiliary core, not K216's artificial angular weight",
        "region": "[0,log(3)]^8 minus [0,log(2)]^8 in nonnegative auxiliary t",
        "partition": "Assign each point outside the inner cube to its first coordinate above log(2). Coordinates before it lie in [0,log(2)], that coordinate in [log(2),log(3)], and later coordinates in [0,log(3)]. Boundaries overlap only in measure zero. Optionally split the exceeding coordinate at log(5/2).",
        "exact_cell_rule": "Apply K221 intersection with K220 on every cell, sum interval endpoints with the exact product of sinh upper minus sinh lower. All exp(t) endpoints are rational, so cosh, sinh, the entire prefactor excluding pi^-8, and the resulting interval are rational.",
        "coarse": coarse,
        "refined": refined,
        "inner_plus_refined_first_cube_absolute_upper_using_pi_gt_3": str(first_cube),
        "refined_bound_strictly_sharper": True,
        "interpretation": "One finite adjacent shell is certified by 8 or 16 cells. Triangle composition with K221's disjoint inner cube bounds [0,log(3)]^8, but first-coordinate bisection yields only a modest improvement; this finite sample gives neither an adaptive asymptotic cost nor the complete middle region through K215's 215 log(2). It does not compose coalescent, K185/K188 quotient or K204/K209 common-reference boundaries, nor move source/physics status.",
        "claim_ceiling": "Exact first-shell signed absolute bound using pi>3 and finite 8/16-cell comparison only; no accurate complete order-six prefix or physical result.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K222 exact first-middle-shell 8/16-cell cover")
    print("absolute ceilings:", *(f"{float(Q(result[k]['absolute_upper_using_pi_gt_3'])):.8e}"
                                  for k in ("coarse", "refined")))
