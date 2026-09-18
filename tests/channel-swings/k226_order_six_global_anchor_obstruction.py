#!/usr/bin/env python3
"""K226: a certified cost obstruction for K225's fixed b=1 unsigned bound."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json

from k225_order_six_diagonal_cancellation import K185, OUT as K225, terms, mixed_majorant
from k222_order_six_first_middle_shell_cover import ROOT, SCALE, cosh, sinh

K224 = ROOT / "lab/process/k224-order-six-second-shell-cost-stress.json"
OUT = ROOT / "lab/process/k226-order-six-global-anchor-obstruction.json"


def generate() -> dict:
    prior = json.loads(K224.read_text())
    headroom = Q(prior["combined_cube_budget_headroom"])
    assert 0 < headroom < Q(1, 10**21)
    # Integral_0^1 x^4(1-x)^4/(1+x^2) dx = 22/7 - pi > 0.
    # Polynomial quotient: x^6-4x^5+5x^4-4x^2+4, remainder -4.
    quotient_integral = Q(1, 7)-Q(4, 6)+1-Q(4, 3)+4
    assert quotient_integral == Q(22, 7)
    items = list(terms(json.loads(K185.read_text())))
    assert len(items) == 1864
    lower = (cosh(Q(4)), cosh(Q(4))) + (Q(1),)*6
    volume = sinh(Q(4))**6 * (sinh(Q(5))-sinh(Q(4)))**2
    shared = SCALE * (cosh(Q(4))-1)**2 * volume / Q(22, 7)**8
    results = []
    global_sum = Q(0)
    local_sum = Q(0)
    local_lower = (cosh(Q(4)),)*8
    for j in range(2, 8):
        for k in range(j+1, 8):
            m = mixed_majorant(items, lower, j, k)
            global_sum += m
            local_sum += mixed_majorant(items, local_lower, j, k)
            bound_below = shared*m
            assert bound_below > headroom
            results.append({"pair": [j, k], "hessian_majorant_at_lower": str(m),
                            "integral_majorant_strict_lower_rational": str(bound_below),
                            "lower_over_remaining_budget": str(bound_below/headroom)})
    high_cube_volume = (sinh(Q(5))-sinh(Q(4)))**8
    global_cube_upper = SCALE*high_cube_volume*(cosh(Q(5))-1)**2*global_sum/Q(31, 10)**8
    local_cube_upper = SCALE*high_cube_volume*(cosh(Q(5))-cosh(Q(4)))**2*local_sum/Q(31, 10)**8
    assert local_cube_upper < global_cube_upper
    assert local_cube_upper/headroom < Q(1, 400)
    return {
        "schema_version": "1.0", "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {p.stem.split("-")[0]: hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in (K185, K224, K225)},
        "object": "K225 nonnegative fixed global b=1 unsigned pairwise Hessian majorant of the original K218 signed core, with exact outer cosh weight",
        "region": "For each pair 2<=j<k<=7, t_j,t_k in [log(4),log(5)] and all other six t_h in [0,log(4)]; a positive-measure subbox of the third shell [0,log(5)]^8 minus [0,log(4)]^8.",
        "lower_bound_rule": "On each pair subbox, M_jk(c_0,c_1,1^6)>=M_jk(cosh(log4),cosh(log4),1^6), since all reciprocal loads decrease in c_0,c_1. Each (cosh(t_j)-1)(cosh(t_k)-1)>=(cosh(log4)-1)^2. The exact product-cosh measure integrates to sinh(log4)^6*(sinh(log5)-sinh(log4))^2. Multiply by 2^8*256^6/5!, and pi^-8>(7/22)^8. Thus the integral of the ENTIRE nonnegative K225 majorant on the third shell is strictly greater than each listed rational lower bound.",
        "pi_upper_certificate": "Integral_0^1 x^4(1-x)^4/(1+x^2) dx=22/7-pi>0: the polynomial quotient is x^6-4x^5+5x^4-4x^2+4 with remainder -4 and quotient integral 22/7.",
        "remaining_budget_after_k224": str(headroom),
        "pair_count": len(results), "all_pair_lower_bounds_exceed_headroom": True,
        "minimum_ratio_pair": min(results, key=lambda r: Q(r["lower_over_remaining_budget"]))["pair"],
        "minimum_ratio": min((Q(r["lower_over_remaining_budget"]) for r in results), default=Q(0)).__str__(),
        "pairs": results,
        "locally_reanchored_high_cube": {
            "region": "[log(4),log(5)]^8 only",
            "anchor_cosh": str(cosh(Q(4))),
            "weight_integral": str(high_cube_volume),
            "upper_rule": "K225 pairwise majorant with b=cosh(log4) on this cube, all c0,c1 lower-bounded by cosh(log4), all upper c_j by cosh(log5), exact product-cosh measure and pi>31/10 from K224.",
            "local_hessian_sum": str(local_sum),
            "global_hessian_sum": str(global_sum),
            "local_upper_using_pi_gt_31_over_10": str(local_cube_upper),
            "fixed_global_upper_same_cube": str(global_cube_upper),
            "upper_to_headroom": str(local_cube_upper/headroom),
            "improvement_factor": str(global_cube_upper/local_cube_upper)},
        "claim_ceiling": "Every one of fifteen rational subbox witnesses proves the INTEGRAL OF THE FIXED GLOBAL b=1 UNSIGNED K225 MAJORANT exceeds K224's remaining finite-prefix allocation. No partition that only evaluates this same nonnegative majorant can repair its total cost. A separately locally reanchored all-high cube admits a small exact upper, but is only a subset of the third shell. This is NOT a lower bound on the signed integral, not a node-count theorem, and does not certify mixed third-shell cells, K215, coalescent/quotient/reference composition or source/physics conclusions."
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2)+"\n")
    print("[PASS] K226 fifteen exact third-shell global-anchor obstructions")
    print("minimum ratio:", f"{float(Q(result['minimum_ratio'])):.9f}")
