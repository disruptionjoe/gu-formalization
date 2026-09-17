#!/usr/bin/env python3
"""K214: support-dependent finite-box tail after K213's radial elimination."""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / "lab/process"
K185 = P / "k185-order-six-duffy-face-tail-wave.json"
K204 = P / "k204-order-six-core-moment-defect.json"
K213 = P / "k213-order-six-bessel-laplace-radial-elimination.json"
OUT = P / "k214-order-six-support-aware-auxiliary-tail.json"
TARGET = Q(1, 10**21)


def sinh_dyadic(m: int) -> Q:
    """sinh(m log 2), exact and independent of floating point."""
    assert m >= 0
    return Q(2**m - Q(1, 2**m), 2)


def tail_bound(supports: tuple[Q, ...], m: int) -> Q:
    """Unsigned eight-factor bound, before the angular z^(2/3)/pi^8 <= 1."""
    assert len(supports) == 8 and all(s > 0 for s in supports)
    product = Q(1)
    for s in supports:
        product *= s
    u = sinh_dyadic(m)
    return Q(2**8, product) * sum((Q(256, 256 + s*u))**6 for s in supports)


def first_dyadic_cutoff(supports: tuple[Q, ...], target: Q = TARGET) -> int:
    assert target > 0
    m = 0
    while tail_bound(supports, m) >= target:
        m += 1
    assert m == 0 or tail_bound(supports, m-1) >= target
    return m


def generate() -> dict:
    prior = json.loads(K213.read_text())
    core = json.loads(K204.read_text())["core"]
    assert core["angular_coordinate_lower"] == "1/2^180"
    assert prior["counts"]["leibniz_terms"] == 1864
    k185 = json.loads(K185.read_text())
    catalog = k185["exact_allocation_certificate"]["allocation_catalog"]
    entries = k185["complete_face_hypergraph"]["entries"]
    delta = Q(1, 2**180)
    # Each nonempty support S_j >= delta on K204's compact angular core.
    uniform = (delta,)*8
    uniform_m = first_dyadic_cutoff(uniform)
    assert uniform_m == 443
    histogram: Counter[int] = Counter()
    count = 0
    min_s = Q(1)
    for row in entries:
        for term in row["terms"]:
            masks = tuple(int(x, 16) for x in catalog[term["allocation_id"]]
                          ["support_masks_hex"].split(","))
            assert len(masks) == 8 and all(0 < mask < 1 << 14 for mask in masks)
            # z_i=1/14 is a diagnostic point, not a global angular bound.
            supports = tuple(Q(mask.bit_count(), 14) for mask in masks)
            min_s = min(min_s, *supports)
            histogram[first_dyadic_cutoff(supports)] += 1
            count += 1
    assert count == 1864 and sum(histogram.values()) == count
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {key: hashlib.sha256(path.read_bytes()).hexdigest()
                         for key, path in (("K185", K185), ("K204", K204), ("K213", K213))},
        "object": "K139/K184 conditional Fock model; one unsigned K185 term at positive angular interior",
        "theorem": "For S_j>0 and T>=0, the K213 eight-auxiliary integral outside [0,T]^8, including its exact Gamma/Bessel prefactor but before z_i^(2/3)/pi^8, is at most (2^8/product_j S_j)*sum_j[256/(256+S_j*sinh(T))]^6.",
        "proof": "Union-bound the eight coordinate tails. For the seven other factors use 0<x K1(x)<=1 (derivative (x K1(x))'=-x K0(x)<0, limit 1 at zero). Tonelli integrates the Gamma(6,256) density times rho^8/rho^7 and the remaining cosh kernel: 2^8*6*256^6/(product_(k!=j) S_k)*integral_T^infty cosh(t)/(256+S_j*cosh(t))^7 dt. With u=sinh(t), cosh(t)>=u>=0, the last integral is at most 1/[6*S_j*(256+S_j*sinh(T))^6]. Sum over j. Nonnegative termwise tails precede the signed determinant sum.",
        "uniform_core": {
            "angular_coordinate_lower": "1/2^180",
            "inequality": "Each support S_j>=delta; the term bound is <=8*2^8/delta^8*(256/(256+delta*sinh(T)))^6, before the angular factor which is <=1.",
            "target_per_unsigned_term": "1/10^21",
            "dyadic_T_definition": "T=m*log(2), sinh(T)=(2^m-2^-m)/2 exactly",
            "first_integer_m_sufficient_under_this_uniform_bound": uniform_m,
            "previous_integer_m_fails_this_uniform_bound": uniform_m-1,
            "comparison": "K213's distinct loose AM--GM certificate required even T=4534; neither cutoff is necessary for the actual tail or a node-cost lower bound."
        },
        "barycenter_diagnostic": {
            "z": "each of 14 coordinates equals 1/14 (not a uniform core result)",
            "terms": count,
            "minimum_support": str(min_s),
            "first_m_histogram": {str(k): histogram[k] for k in sorted(histogram)},
            "worst_first_m": max(histogram)
        },
        "source_routing": prior["source_routing"],
        "unchanged_complete_rule_error_upper_rational": prior["unchanged_complete_rule_error_upper_rational"],
        "claim_ceiling": "A sharper support-aware positive core auxiliary tail only. No certified eight-dimensional cubature, signed angular cell enclosure, quotient-face/common-reference boundary composition, accurate order-six prefix, physical state, or source verdict."
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] support-dependent tail, all 1,864 K185 term masks")
    print("[PASS] exact rational uniform dyadic m =",
          result["uniform_core"]["first_integer_m_sufficient_under_this_uniform_bound"])
    print("[PASS] barycenter worst dyadic m =",
          result["barycenter_diagnostic"]["worst_first_m"])
