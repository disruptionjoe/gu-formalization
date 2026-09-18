#!/usr/bin/env python3
"""K221: signed center Hessian and rigorous cubic cell remainder for K218."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json

from k220_order_six_signed_taylor_cell_enclosure import (
    K185, K217, K218, K219, OUT as K220, ROOT, SCALE,
    allocation_coefficients, signed_taylor_bounds, term_data,
)

OUT = ROOT / "lab/process/k221-order-six-signed-quadratic-cell-enclosure.json"


def signed_quadratic_bounds(source: dict, low: tuple[Q, ...],
                            high: tuple[Q, ...]) -> dict:
    """Exact second jet; bound |D^3 H[h,h,h]| for |h_j|<=r_j.

    For d_i=sum_j m_ji h_j and a_i>0, the magnitude of a reciprocal
    product's third directional derivative is bounded by
    q[(sum |d_i|/a_i)^3 + 3(sum |d_i|/a_i)(sum |d_i|^2/a_i^2)
      + 2 sum |d_i|^3/a_i^3]. All its positive factors decrease when
    loads increase, so the lower corner controls the entire segment.
    """
    first = signed_taylor_bounds(source, low, high)
    midpoint, radius = first["center"], first["radius"]
    coefficients = allocation_coefficients(source)
    catalog = source["exact_allocation_certificate"]["allocation_catalog"]
    hessian = [[Q(0) for _ in range(8)] for _ in range(8)]
    third_sixth = Q(0)
    for key, w in coefficients.items():
        masks = tuple(int(v, 16) for v in catalog[key]["support_masks_hex"].split(","))
        q_mid, slopes, loads = term_data(masks, midpoint)
        for j in range(8):
            for k in range(j, 8):
                shared = sum((Q(1, loads[i]**2) for i in range(14)
                              if masks[j] & (1 << i) and masks[k] & (1 << i)), Q(0))
                hessian[j][k] += w*q_mid*(slopes[j]*slopes[k] + shared)
        q_low, _, loads_low = term_data(masks, low)
        directional = [sum((radius[j] for j in range(8)
                            if masks[j] & (1 << i)), Q(0))/loads_low[i]
                       for i in range(14)]
        s1 = sum(directional, Q(0))
        s2 = sum((v*v for v in directional), Q(0))
        s3 = sum((v*v*v for v in directional), Q(0))
        third_sixth += abs(w)*q_low*(s1**3 + 3*s1*s2 + 2*s3)/6
    for j in range(8):
        for k in range(j):
            hessian[j][k] = hessian[k][j]
    quadratic_radius = sum((abs(hessian[j][k])*radius[j]*radius[k]
                            for j in range(8) for k in range(8)), Q(0))/2
    radius_total = first["linear_radius"] + quadratic_radius + third_sixth
    raw = (first["center_core"]-radius_total,
           first["center_core"]+radius_total)
    old = first["intersection_core"]
    intersected = (max(raw[0], old[0]), min(raw[1], old[1]))
    assert intersected[0] <= intersected[1]
    return {"center": midpoint, "radius": radius,
            "center_core": first["center_core"], "signed_gradient": first["signed_gradient"],
            "signed_hessian": tuple(tuple(row) for row in hessian),
            "linear_radius": first["linear_radius"],
            "quadratic_radius": quadratic_radius, "cubic_remainder": third_sixth,
            "quadratic_core": raw, "k220_core": old, "intersection_core": intersected}


def pilot(source: dict, prior: dict, key: str) -> dict:
    cell = prior["pilot_cells"][key]
    low = tuple(Q(x) for x in cell["cosh_lower"])
    high = tuple(Q(x) for x in cell["cosh_upper"])
    measure = Q(cell["exact_product_cosh_measure"])
    b = signed_quadratic_bounds(source, low, high)
    def integral(pair: tuple[Q, Q]) -> list[str]:
        return [str(SCALE*measure*v) for v in pair]
    old_width = b["k220_core"][1]-b["k220_core"][0]
    new_width = b["intersection_core"][1]-b["intersection_core"][0]
    assert new_width < old_width
    return {"cosh_lower": cell["cosh_lower"], "cosh_upper": cell["cosh_upper"],
            "exact_product_cosh_measure": str(measure),
            "center_core": str(b["center_core"]),
            "signed_gradient": [str(x) for x in b["signed_gradient"]],
            "signed_hessian": [[str(x) for x in row] for row in b["signed_hessian"]],
            "linear_radius": str(b["linear_radius"]),
            "quadratic_radius": str(b["quadratic_radius"]),
            "cubic_remainder": str(b["cubic_remainder"]),
            "quadratic_integral_interval_without_pi8": integral(b["quadratic_core"]),
            "intersection_integral_interval_without_pi8": integral(b["intersection_core"]),
            "intersection_width_to_k220_width": str(new_width/old_width),
            "interval_decimal_without_pi8":
                [f"{float(SCALE*measure*v):.8e}" for v in b["intersection_core"]]}


def generate() -> dict:
    source = json.loads(K185.read_text())
    prior = json.loads(K220.read_text())
    cells = {key: pilot(source, prior, key) for key in
             ("small_inner", "k219_inner", "alternating_shifted")}
    full = cells["k219_inner"]
    assert all(Q(v) == 0 for v in full["signed_gradient"])
    upper = Q(full["intersection_integral_interval_without_pi8"][1])/3**8
    assert upper == -Q(full["intersection_integral_interval_without_pi8"][0])/3**8
    k220_upper = Q(prior["full_inner_comparison"]["absolute_upper_rational_using_pi_gt_3"])
    assert upper < k220_upper
    return {
        "schema_version": "1.0", "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {name: hashlib.sha256(path.read_bytes()).hexdigest()
                         for name, path in (("k185", K185), ("k217", K217),
                                            ("k218", K218), ("k219", K219),
                                            ("k220", K220))},
        "object": prior["object"],
        "theorem": "For H(c)=sum_A w_A prod_i a_Ai(c)^-1, retain exact signed midpoint value, gradient and Hessian. On a rectangular nonnegative cosh cell with center m, radii r and lower corner low, the exact Hessian entry is sum_A w_A q_A(m)[L_Aj(m)L_Ak(m)+sum_i m_Aji m_Aki/a_Ai(m)^2]. Its quadratic contribution has absolute radius one-half sum_jk r_j r_k |H_jk(m)|. Put u_Ai=sum_j r_j m_Aji/a_Ai(low); the third-order Taylor remainder is at most one-sixth sum_A |w_A|q_A(low)[(sum_i u_Ai)^3+3(sum_i u_Ai)(sum_i u_Ai^2)+2sum_i u_Ai^3]. Intersect the resulting interval with K220, multiply by exact positive product-cosh cell measure and 2^8*256^6/(5! pi^8).",
        "pilot_cells": cells,
        "full_inner_comparison": {
            "pi_lower_bound": 3,
            "absolute_upper_rational_using_pi_gt_3": str(upper),
            "k220_absolute_upper_rational": str(k220_upper), "strictly_sharper": True},
        "interpretation": "The signed second jet and rigorous cubic remainder narrow K220's three local pilot intervals. The full [0,log(2)]^8 inner-box absolute ceiling improves; no adaptive middle-box cover, node-cost theorem, complete signed prefix, coalescent/quotient/reference composition or physical result follows.",
        "source_routing": prior["source_routing"],
        "unchanged_complete_rule_error_upper_rational": prior["unchanged_complete_rule_error_upper_rational"],
        "claim_ceiling": "Exact local signed quadratic Taylor enclosure and inner-box improvement only; no whole-box or source/physics verdict.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K221 signed Hessian and cubic-remainder rational cells")
    print("width ratios:", ", ".join(f"{float(Q(c['intersection_width_to_k220_width'])):.8g}"
                                   for c in result["pilot_cells"].values()))
