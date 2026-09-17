#!/usr/bin/env python3
"""K217: true-measure signed K185 inner box and a K216 normalization audit."""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as Q
import hashlib
from itertools import combinations_with_replacement
import json
from math import comb, factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / "lab/process"
K185 = P / "k185-order-six-duffy-face-tail-wave.json"
K213 = P / "k213-order-six-bessel-laplace-radial-elimination.json"
K215 = P / "k215-order-six-angular-integrated-auxiliary-tail.json"
K216 = P / "k216-order-six-analytic-angular-prefix.json"
OUT = P / "k217-order-six-signed-inner-box.json"
BETA = Q(1)  # original unweighted simplex; K202's common weight cancels its residual
BETA0 = 14 * BETA
QMAX = Q(35, 1024)
ORDER = 3


def add(a: tuple[Q, Q, Q, Q], b: tuple[Q, Q, Q, Q]) -> tuple[Q, Q, Q, Q]:
    return tuple(x + y for x, y in zip(a, b))  # type: ignore[return-value]


def scale(a: tuple[Q, Q, Q, Q], c: Q) -> tuple[Q, Q, Q, Q]:
    return tuple(c * x for x in a)  # type: ignore[return-value]


def mul(a: tuple[Q, Q, Q, Q], b: tuple[Q, Q, Q, Q]) -> tuple[Q, Q, Q, Q]:
    return tuple(sum(a[i] * b[k-i] for i in range(k+1))
                 for k in range(4))  # type: ignore[return-value]


ZERO = (Q(0),) * 4
ONE = (Q(1), Q(0), Q(0), Q(0))
# J_r = integral_0^log(2) cosh(t)^(r+1) dt, a polynomial in h=log(2).
J = ((Q(3, 4), Q(0), Q(0), Q(0)),
     (Q(15, 32), Q(1, 2), Q(0), Q(0)),
     (Q(57, 64), Q(0), Q(0), Q(0)),
     (Q(735, 1024), Q(3, 8), Q(0), Q(0)))


def angular_moment(masks: tuple[int, ...], js: tuple[int, ...]) -> Q:
    """E_Dirichlet product of support sums, n<=3; cycle partitions."""
    n = len(js)
    if not n:
        return Q(1)
    a = [masks[j] for j in js]
    sizes = [x.bit_count() for x in a]
    if n == 1:
        numerator = BETA * sizes[0]
    elif n == 2:
        numerator = BETA**2 * sizes[0] * sizes[1] + BETA * (a[0] & a[1]).bit_count()
    else:
        assert n == 3
        numerator = BETA**3 * sizes[0] * sizes[1] * sizes[2]
        numerator += BETA**2 * (
            (a[0] & a[1]).bit_count() * sizes[2]
            + (a[0] & a[2]).bit_count() * sizes[1]
            + (a[1] & a[2]).bit_count() * sizes[0])
        numerator += 2 * BETA * (a[0] & a[1] & a[2]).bit_count()
    denominator = Q(1)
    for k in range(n):
        denominator *= BETA0 + k
    return numerator / denominator


def integrated_moment(masks: tuple[int, ...], n: int) -> tuple[Q, Q, Q, Q]:
    """Angular E[X^n] then integrate product cosh(t_j) on the full inner box."""
    result = ZERO
    for js in combinations_with_replacement(range(8), n):
        counts = Counter(js)
        multiplicity = factorial(n)
        factor = ONE
        for j in range(8):
            m = counts[j]
            multiplicity //= factorial(m)
            factor = mul(factor, J[m])
        result = add(result, scale(factor, multiplicity * angular_moment(masks, js)))
    return result


def pointwise_cancellation(terms: list[dict], catalog: dict) -> None:
    assert sum(term["leibniz_sign"] for term in terms) == 0
    for j in range(8):
        for i in range(14):
            assert sum(term["leibniz_sign"] * bool(
                int(catalog[term["allocation_id"]]["support_masks_hex"].split(",")[j], 16)
                & (1 << i)) for term in terms) == 0


def generate() -> dict:
    source = json.loads(K185.read_text())
    k213 = json.loads(K213.read_text())
    k215 = json.loads(K215.read_text())
    k216 = json.loads(K216.read_text())
    entries = source["complete_face_hypergraph"]["entries"]
    catalog = source["exact_allocation_certificate"]["allocation_catalog"]
    assert len(entries) == 234 and sum(len(e["terms"]) for e in entries) == 1864
    assert k213["counts"]["leibniz_terms"] == k216["term_count"] == 1864
    assert k215["first_sufficient_universal_whole_sum_dyadic_m"] == 215
    cache: dict[tuple[str, int], tuple[Q, Q, Q, Q]] = {}
    signed = [ZERO for _ in range(ORDER + 1)]
    for entry in entries:
        pointwise_cancellation(entry["terms"], catalog)
        for term in entry["terms"]:
            key = term["allocation_id"]
            masks = tuple(int(x, 16) for x in catalog[key]["support_masks_hex"].split(","))
            assert len(masks) == 8 and all(0 < m < 1 << 14 for m in masks)
            sign = (2 if entry["left"] != entry["right"] else 1) * entry["coefficient_product"] * term["leibniz_sign"]
            for n in range(ORDER + 1):
                cache_key = (key, n)
                if cache_key not in cache:
                    cache[cache_key] = integrated_moment(masks, n)
                signed[n] = add(signed[n], scale(cache[cache_key], sign))
    assert signed[0] == signed[1] == ZERO

    # 1/(256+X)^14 = 256^-14 sum (-1)^n binom(13+n,n)(X/256)^n.
    polynomial = ZERO
    for n in range(ORDER + 1):
        polynomial = add(polynomial, scale(signed[n],
                          Q((-1)**n * comb(13+n, n), 256**n)))
    # Multiplicative exact prefactor omitted from polynomial:
    # (2^8*256^6*13!/5!)/256^14 * B(1,...,1)/pi^8.
    prefactor_rational = Q(2**8 * 256**6 * factorial(13), factorial(5) * 256**14)
    ratio = QMAX * Q(ORDER + 15, ORDER + 2)
    assert ratio < 1
    remainder_relative = Q(comb(ORDER + 14, ORDER + 1)) * QMAX**(ORDER + 1) / (1-ratio)
    # Before signs: original uniform simplex volume=1/13!, pi>3,
    # integral_[0,log 2]^8 product cosh(t_j)=(sinh(log 2))^8=(3/4)^8.
    # Off-diagonal K184 entries count twice, giving 2,928 ordered terms.
    raw_one = prefactor_rational * Q(1, factorial(13)*3**8) * Q(3, 4)**8 * remainder_relative
    ordered_terms = sum(len(e["terms"]) * (2 if e["left"] != e["right"] else 1)
                        for e in entries)
    assert ordered_terms == 2928
    raw_all = ordered_terms * raw_one
    assert raw_all < Q(1, 10**21)
    assert polynomial == ZERO
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {p.stem.split("-")[0]: hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in (K185, K213, K215, K216)},
        "object": "K139/K184 raw signed K185 assembly, auxiliary inner box [0,log(2)]^8, after K213 radial elimination",
        "normalization_correction": "Historical K216's beta_i=5/3 applies to the isolated residual prod z_i^(2/3), not original K185. K202's common Dirichlet(1/3)^14 reference density prod z_i^(-2/3) cancels it; the actual angular measure is uniform Dirichlet(1)^14. K185's varying beta_i=1-alpha_i are AM--GM majorant measures. Current K213/K216 executable artifacts use the corrected uniform raw measure; their earlier weighted identity and raw transfer remain historical only.",
        "identity": "The complete signed inner-box integral equals [2^8*256^6*13!/(5!*256^14*13!*pi^8)] times P(log 2), up to the stated absolute error. P integrates through degree three the binomial expansion in X=sum_j cosh(t_j) S_j(z), with S_j=sum_(i in support_j)z_i, under the ORIGINAL UNIFORM angular measure. Exact coefficient replay gives P=0. Both entry coefficient_product and the off-diagonal factor two and Leibniz signs are included.",
        "proof": "At order n<=3, integrate X^n by uniform Dirichlet(1)^14 cycle-partition moments of eight support sums and elementary J_r=int_0^log(2) cosh(t)^(r+1)dt. Each of 234 entries cancels pointwise at orders zero and one by exact signed support incidence; complete signed auxiliary-integrated orders two and three cancel after the ordered off-diagonal factors. The alternating binomial series has an absolute tail at X/256<=35/1024 bounded by the order-four majorant and a decreasing geometric ratio. Bound every raw term before signed grouping; no cancellation is assumed for the remainder.",
        "entry_count": len(entries), "term_count": 1864,
        "ordered_term_count_with_off_diagonal_twice": ordered_terms,
        "distinct_allocation_moments": len(cache),
        "pointwise_cancellation_orders": [0, 1],
        "signed_integrated_moment_polynomials_n0_to_n3": [[str(x) for x in a] for a in signed],
        "prefactor_rational": str(prefactor_rational),
        "beta_factor": "Gamma(1)^14/Gamma(14)=1/13! (original unweighted simplex)",
        "pi_factor": "pi^-8",
        "signed_inner_box_polynomial_in_log2": [str(x) for x in polynomial],
        "remainder": {
            "q_ceiling": str(QMAX), "order_inclusive": ORDER,
            "relative_binomial_tail_ceiling": str(remainder_relative),
            "one_raw_term_absolute_ceiling": str(raw_one),
            "whole_2928_ordered_term_absolute_ceiling": str(raw_all),
            "normalization": "Raw Bessel/Gamma prefactor and K185 signs, 2,928 ordered terms after off-diagonal doubling, original uniform simplex volume 1/13!, pi>3, exact integral product cosh(t_j)=(3/4)^8."
        },
        "source_routing": k216["source_routing"],
        "unchanged_complete_rule_error_upper_rational": k216["unchanged_complete_rule_error_upper_rational"],
        "claim_ceiling": "The true signed inner-box contribution is bounded in absolute value by the raw whole-sum tail. K213/K216 now have corrected raw normalization, but the middle region through K215's 215 log(2) sufficient cutoff, full signed coalescent cells, K185/K188 quotient and K204/K209 reference boundaries, accurate complete prefix, source action and physical state remain open."
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] exact signed inner-box moment polynomial and raw remainder")
