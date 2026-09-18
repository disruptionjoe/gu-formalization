#!/usr/bin/env python3
"""K233: a certified, fixed-anchor two-exception Taylor radius for K185."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations
import json
from math import prod

from k225_order_six_diagonal_cancellation import K185, ROOT, terms
from k231_order_six_projected_diagonal_jet import OUT as K231, orbit_jet
from k232_order_six_quartic_sos import MANIFEST as K232

OUT = ROOT / "lab/process/k233-order-six-two-exception-local-radius.json"
ANCHOR = (Q(5, 4), Q(17, 8)) + (Q(1),) * 6
PAIRS = tuple(combinations(range(2, 8), 2))


def bound_fifth(items):
    """Exact unsigned bound using h_5(r) <= (sum r)^5 for r >= 0."""
    total = Q()
    for weight, masks in items:
        loads = [256 + sum(ANCHOR[j] for j in range(8) if masks[j] & (1 << i))
                 for i in range(14)]
        q = Q(abs(weight), prod(loads))
        for pair in PAIRS:
            s1 = sum((Q(sum(bool(masks[j] & (1 << i)) for j in pair), loads[i])
                      for i in range(14)), Q())
            total += q * s1**5 / len(PAIRS)
    return total


def generate():
    items = list(terms(json.loads(K185.read_text())))
    assert len(items) == 1864 and len(PAIRS) == 15
    prior = json.loads(K231.read_text())
    assert prior["orbit_direction_controls"]["2"]["degree_four_sign"] == 1
    a = orbit_jet(items, ANCHOR, 2)[4]
    assert a > 0
    b5 = bound_fifth(items)
    radius = a / b5
    assert Q(1, 30000) < radius < Q(1, 25000)
    return {
        "schema_version": "1.0", "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {"k185": sha256(K185.read_bytes()).hexdigest(),
                         "k231": sha256(K231.read_bytes()).hexdigest(),
                         "k232": sha256(K232.read_bytes()).hexdigest()},
        "object": "S6-projected original signed K185/K218 rational-cosh core at fixed (u,v,b)=(5/4,17/8,1) along any two-exception ray c_j=c_k=b+h, other c_2..c_7=b, h>=0",
        "raw_signed_terms": len(items), "projected_pair_count": len(PAIRS),
        "fourth_coefficient_A": str(a), "absolute_fifth_bound_B5": str(b5),
        "certified_radius": str(radius), "radius_decimal": f"{float(radius):.12e}",
        "rational_bracket": ["1/30000", "1/25000"],
        "theorem": "For h>=0 on the stated fixed-anchor two-exception ray, Hbar(h)=A*h^4+R5(h), |R5(h)|<=B5*h^5. K231 proves coefficients 0..3 vanish and K232 gives P(1,1,0,0,0,0)=1. For each raw rational term q(h)=product_i(a_i+n_i*h)^-1, n_i in {0,1,2} and a_i>0, Taylor's integral remainder has |q^(5)(t)|/5! = q(t)*h_5(n_i/(a_i+n_i*t)) <= q(0)*(sum_i n_i/a_i)^5 for t>=0. Sum absolute weighted term bounds, then average over 15 pairs. Hence Hbar(h)>0 for 0<h<A/B5; equality at h=0 is K225. The upper bracket on A/B5 says only this specified sufficient bound stops certifying positivity at 1/25000, not that the core turns negative there.",
        "method_cost_note": "This raw-term sufficient radius is less than 1/25000 cosh units, whereas a third auxiliary shell spans cosh values 1..5. Covering a length-four ray by intervals no wider than this radius would require more than 100000 segments if this same fixed-anchor radius were the only local rule. That conditional count is not a necessary node count, a six-dimensional cover, a signed integral estimate, or a uniform reanchored-cell bound.",
        "claim_ceiling": "Exact fixed-anchor two-exception local positivity radius for one deliberately conservative raw-term absolute fifth-derivative majorant. No global sign of A or Hbar, general six-coordinate cell remainder, third-shell certificate/cost lower bound, K215 prefix, boundary composition, source/physics/ledger/canon change."
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K233 exact local Taylor radius", result["radius_decimal"])
