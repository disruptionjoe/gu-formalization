#!/usr/bin/env python3
"""K213: eliminate the Gamma radius in each positive K185 Leibniz term."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import itertools
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / "lab/process"
K185 = P / "k185-order-six-duffy-face-tail-wave.json"
K205 = P / "k205-order-six-radial-normal-form.json"
K204 = P / "k204-order-six-core-moment-defect.json"
OUT = P / "k213-order-six-bessel-laplace-radial-elimination.json"


def all_masks() -> tuple[int, int, int, int]:
    data = json.loads(K185.read_text())
    catalog = data["exact_allocation_certificate"]["allocation_catalog"]
    rows = data["complete_face_hypergraph"]["entries"]
    terms = factors = max_load = 0
    groups = set()
    for row in rows:
        groups.add(row["group_id"])
        for term in row["terms"]:
            masks = tuple(int(x, 16) for x in catalog[term["allocation_id"]]
                          ["support_masks_hex"].split(","))
            assert len(masks) == 8 and all(0 < m < 1 << 14 for m in masks)
            assert term["leibniz_sign"] in (-1, 1)
            max_load = max(max_load, max(sum(bool(m & (1 << i)) for m in masks)
                                         for i in range(14)))
            terms += 1
            factors += len(masks)
    assert len(groups) == 18
    return len(rows), terms, factors, max_load


def box_tail_coefficient(delta: Q) -> Q:
    """Bound on a *single* transformed eight-factor integral beyond [0,T]^8.

    This includes the exact 2^8 Gamma prefactor but not the original
    uniform angular factor 1/pi^8, which is at most one.
    """
    assert delta > 0
    coefficient = Q(2**8 * 256**6 * math.factorial(13), math.factorial(5))
    amgm_denominator = Q((7*256)**2) * Q(28, 3)**12
    # Integral cosh(t)^(-1/2) <= 2 sqrt(2); eight such integrals give 4096.
    # Union over the eight tails and S_j >= delta on the face-stripped core.
    return coefficient * 8 * 4096 / (amgm_denominator * delta**12)


def generate() -> dict:
    old = json.loads(K205.read_text())
    core = json.loads(K204.read_text())["core"]
    assert core["angular_coordinate_lower"] == "1/2^180"
    rows, terms, factors, max_load = all_masks()
    assert (rows, terms, factors, max_load) == (234, 1864, 14912, 7)
    assert old["counts"]["leibniz_terms"] == terms
    delta = Q(1, 2**180)
    bound = box_tail_coefficient(delta)
    # e > 2, so exp(-T/2) < 2^(-T/2) for even T. This is a deliberately
    # coarse *sufficient* core tail certificate, not a node-cost lower bound.
    target = Q(1, 10**21)
    first_even = next(t for t in itertools.count(0, 2) if bound / 2**(t//2) < target)
    assert bound / 2**(first_even//2) < target
    assert bound / 2**((first_even-2)//2) >= target
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {name: hashlib.sha256(path.read_bytes()).hexdigest()
                         for name, path in (("K185", K185), ("K205", K205), ("K204", K204))},
        "counts": {"gram_entries": rows, "leibniz_terms": terms,
                   "factor_occurrences": factors, "max_support_load": max_load},
        "object": "K139/K184 conditional positive Fock model; one K185 signed permutation term at fixed positive interior angular z",
        "source_routing": "SC-ACT-01/02 ASSERTS a distinct source action/equation; SC-META-53 UNCERTAIN and LT-SM8/LT-GR6b/RA-F1/AC-F1 NEEDS are unchanged",
        "identity": "K1(x)=integral_0^infty exp(-x*cosh(t))*cosh(t) dt (x>0); Gamma(6,256) radial expectation of rho^8 product_j[2 K1(rho*S_j)] = (2^8*256^6*13!/5!)*integral_[0,infty)^8 product_j cosh(t_j)/(256+sum_j S_j*cosh(t_j))^14 dt",
        "normalization": "Multiply the identity by the original uniform simplex density 1/pi^8 and each stored Leibniz/coefficient sign before assembling the eighteen signed groups; K202's common product z_i^(-2/3) cancels its residual product z_i^(2/3) exactly. S_j=sum_(i in support_mask_j) z_i>0. The historical isolated residual-weight reading is withdrawn by K217.",
        "proof": "Apply the positive cosh representation eight times; Tonelli for each unsigned term, then integrate rho^13 exp[-rho*(256+sum S_j cosh(t_j))] to 13!/(256+sum S_j cosh(t_j))^14. The finite signed K185 sum is taken only afterwards.",
        "core_tail": {
            "scope": "For each term on K204's z_i>=delta=2^-180 angular core only; no rho<=1/4 restriction is imposed on the identity",
            "inequality": "D^14 >= (7*256)^2*(28/3)^12*product_j(S_j*cosh(t_j))^(3/2), D=256+sum S_j*cosh(t_j)",
            "tail_bound": "Integral outside [0,T]^8 after radial prefactor and with the original angular 1/pi^8<=1 is < C(delta)*exp(-T/2), C(delta)=2^8*256^6*13!/5!*8*4096/((7*256)^2*(28/3)^12*delta^12)",
            "coefficient_exact_rational": str(bound),
            "coarse_binary_exponential": "exp(-T/2)<2^(-T/2) for even positive T because e>2",
            "first_even_T_sufficient_for_per_term_1e_minus_21_under_coarse_bound": first_even,
            "cost_warning": "This huge sufficient T reflects a very loose uniform core bound; it is not a necessary node count, complexity lower bound, or an accurate signed result. Sharper support-aware or signed bounds are required."
        },
        "radial_impact": "Exact analytic exchange of the radial integral for eight auxiliary dimensions; bypasses the K205 Lipschitz/W1 node-count certificate class algebraically, without proving numerical efficiency.",
        "unchanged_complete_rule_error_upper_rational": old["unchanged_complete_rule_error_upper_rational"],
        "claim_ceiling": "Interior termwise identity and finite-box core-tail bound only. No certified eight-dimensional cubature, signed angular/core error, K185/K188 quotient face/tail composition, accurate order-six prefix, action-selected state, physics or source verdict."
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] 1,864 term masks and exact eight-factor radial identity")
    print("[PASS] core-only finite-box tail certificate; coarse T =",
          result["core_tail"]["first_even_T_sufficient_for_per_term_1e_minus_21_under_coarse_bound"])
