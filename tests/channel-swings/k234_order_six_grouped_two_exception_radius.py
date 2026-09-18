#!/usr/bin/env python3
"""K234: exact signed fifth jet and grouped sixth remainder on K233's ray."""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations
import json

from k225_order_six_diagonal_cancellation import K185, ROOT, terms
from k233_order_six_two_exception_local_radius import ANCHOR, OUT as K233

OUT = ROOT / "lab/process/k234-order-six-grouped-two-exception-radius.json"
PAIRS = tuple(combinations(range(2, 8), 2))


def normalized_groups(items):
    """Combine proportional rational functions *before* taking absolute values."""
    groups = defaultdict(Q)
    for weight, masks in items:
        for pair in PAIRS:
            loads = [(256 + sum(ANCHOR[j] for j in range(8)
                             if masks[j] & (1 << i)),
                      sum(bool(masks[j] & (1 << i)) for j in pair))
                     for i in range(14)]
            # a+n*h = n*(h+a/n) for n>0; n=0 is a constant factor.
            signature = tuple(sorted(a/n for a, n in loads if n))
            factor = Q(weight, len(PAIRS))
            for a, n in loads:
                factor /= n if n else a
            groups[signature] += factor
    return groups


def positive_coefficients(signature, degree):
    """Coefficients of product (1+h/a)^-1, with alternating signs omitted."""
    coefficients = [Q(1)] + [Q()] * degree
    value = Q(1)
    for a in signature:
        value /= a
        inverse = 1/a
        coefficients = [sum((coefficients[k-j]*inverse**j
                             for j in range(k+1)), Q())
                        for k in range(degree+1)]
    return value, coefficients


def generate():
    items = list(terms(json.loads(K185.read_text())))
    assert len(items) == 1864 and len(PAIRS) == 15
    groups = normalized_groups(items)
    nonzero = [(signature, weight) for signature, weight in groups.items() if weight]
    assert len(groups) == 576 and len(nonzero) == 398
    c5 = b6 = Q()
    for signature, weight in nonzero:
        at_zero, coefficients = positive_coefficients(signature, 6)
        c5 -= weight * at_zero * coefficients[5]
        b6 += abs(weight) * at_zero * coefficients[6]
    prior = json.loads(K233.read_text())
    a = Q(prior["fourth_coefficient_A"])
    assert c5 < 0 and b6 > 0 and a + c5 - b6 > 0
    # Since c5<0 and b6>0, the lower polynomial decreases on [0,1].
    return {
        "schema_version": "1.0", "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {"k185": sha256(K185.read_bytes()).hexdigest(),
                         "k233": sha256(K233.read_bytes()).hexdigest()},
        "object": "S6-projected original signed K185/K218 rational-cosh core at fixed (u,v,b)=(5/4,17/8,1) on any two-exception ray c_j=c_k=b+h, other c_2..c_7=b, h>=0",
        "raw_signed_terms": len(items), "projected_pair_count": len(PAIRS),
        "normalized_denominator_groups": len(groups),
        "nonzero_group_coefficients": len(nonzero),
        "fourth_coefficient_A": str(a), "signed_fifth_coefficient_C5": str(c5),
        "grouped_sixth_bound_B6": str(b6),
        "unit_interval_lower_at_one": str(a+c5-b6),
        "decimal_controls": {"A": f"{float(a):.12e}",
                             "C5": f"{float(c5):.12e}",
                             "B6": f"{float(b6):.12e}",
                             "lower_at_one": f"{float(a+c5-b6):.12e}"},
        "theorem": "For every h>=0 on the fixed ray, Hbar(h)=A*h^4+C5*h^5+R6(h), |R6(h)|<=B6*h^6. The exact K231 low-jet identities and K233 A apply. Average over all 15 coordinate pairs, then combine identical functions after writing every positive a+n*h with n>0 as n*(h+a/n) and n=0 as a constant. There are 576 normalized signatures, 398 with nonzero exact rational aggregate coefficients. For a group w*product_i(h+d_i)^-1, all d_i>0, |q^(6)(t)|/6! = |w|*product_i(t+d_i)^-1*h_6(1/(t+d_i)) is coordinatewise decreasing for t>=0. Thus B6 is the sum of each grouped unsigned sixth coefficient at zero, an all-h Taylor remainder bound. The exact signed C5 is negative, B6 positive, and A+C5-B6>0. Hence Hbar(h)>0 for 0<h<=1 because A+C5*h-B6*h^2 is decreasing there. This does not assert a sign after h=1 or away from the stated ray.",
        "method_cost_note": "The fixed-anchor certified radius grows from K233's <1/25000 to at least one cosh unit. This rebuts only that raw-term majorant's pessimism along this ray; it is not a six-dimensional reanchored cover, signed integral, evaluation count or global cost theorem.",
        "claim_ceiling": "Exact fixed-anchor projected two-exception positivity through h=1 under grouped signed Taylor algebra. No other anchor, direction, variable A interval, six-coordinate cell, third-shell signed integral, K215 prefix, quotient/boundary composition, source/physics/ledger/canon change."
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K234 grouped sixth remainder and unit-ray positivity",
          result["decimal_controls"])
