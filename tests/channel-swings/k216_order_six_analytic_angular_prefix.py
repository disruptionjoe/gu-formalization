#!/usr/bin/env python3
"""K216: exact angular elimination and a certified local auxiliary prefix."""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as Q
import hashlib
import json
from math import comb, factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROCESS = ROOT / "lab/process"
K185 = PROCESS / "k185-order-six-duffy-face-tail-wave.json"
K213 = PROCESS / "k213-order-six-bessel-laplace-radial-elimination.json"
K215 = PROCESS / "k215-order-six-angular-integrated-auxiliary-tail.json"
OUT = PROCESS / "k216-order-six-analytic-angular-prefix.json"
BETA = Q(5, 3)
BETA_TOTAL = 14 * BETA
ORDER = 20
BOX_COSH = Q(5, 4)  # cosh(log 2)


def support_loads(masks: tuple[int, ...]) -> tuple[int, ...]:
    assert len(masks) == 8 and all(0 < m < 1 << 14 for m in masks)
    return tuple(sum(bool(mask & (1 << i)) for mask in masks)
                 for i in range(14))


def series_coefficients(loads: tuple[Q, ...], order: int) -> list[Q]:
    """Normalized E[(1-U)^-14] coefficients, U=sum z_i a_i.

    The exact Dirichlet(5/3,...,5/3) moments are encoded by the product
    generating function; no numerical angular quadrature enters this step.
    """
    assert len(loads) == 14 and all(x >= 0 for x in loads)
    high = max(loads)
    denom = 256 + high
    a = [(high - x) / denom for x in loads]
    powers = [sum(x**k for x in a) for k in range(1, order + 1)]
    c = [Q(1)]
    for n in range(1, order + 1):
        c.append(BETA * sum(powers[k-1] * c[n-k]
                            for k in range(1, n + 1)) / n)
    result = [Q(1)]
    numerator = denominator = Q(1)
    for n in range(1, order + 1):
        numerator *= 13 + n
        denominator *= BETA_TOTAL + n - 1
        result.append(numerator * c[n] / denominator)
    return result


def relative_remainder(q: Q, order: int) -> Q:
    """Positive binomial majorant with decreasing post-order ratios."""
    ratio = q * Q(order + 15, order + 2)
    assert ratio < 1
    return Q(comb(order + 14, order + 1)) * q**(order + 1) / (1 - ratio)


def generate() -> dict:
    source = json.loads(K185.read_text())
    k213 = json.loads(K213.read_text())
    k215 = json.loads(K215.read_text())
    catalog = source["exact_allocation_certificate"]["allocation_catalog"]
    histogram: Counter[str] = Counter()
    unique: set[str] = set()
    example: tuple[int, ...] | None = None
    for entry in source["complete_face_hypergraph"]["entries"]:
        for term in entry["terms"]:
            key = term["allocation_id"]
            unique.add(key)
            masks = tuple(int(x, 16) for x in
                          catalog[key]["support_masks_hex"].split(","))
            loads = support_loads(masks)
            histogram[f"{min(loads)}..{max(loads)}"] += 1
            if example is None:
                example = loads
    assert histogram == {"1..7": 1864} and len(unique) == 1276
    assert k213["counts"]["leibniz_terms"] == k215["mask_count"] == 1864
    assert example is not None

    # For t_j in [0,log 2], 1 <= L_i <= 7*cosh(log 2)=35/4.
    q = (7 * BOX_COSH - 1) / (256 + 7 * BOX_COSH)
    assert q == Q(31, 1059)
    remainder = relative_remainder(q, ORDER)
    assert remainder < Q(1, 10**21)
    # Bound the raw angular integral by volume(Delta_13)/pi^8:
    # product z_i^(2/3)<=1, pi>3, log(2)<1 and cosh(t_j)<=5/4.
    raw_term_bound = (Q(2**8 * 256**6 * factorial(13), factorial(5))
                      * Q(1, factorial(13) * 3**8)
                      * BOX_COSH**8 / 256**14 * remainder)
    assert 1864 * raw_term_bound < Q(1, 10**21)

    # At the K215 full box the same *uniform geometric remainder test* fails
    # at order 20; this does not prove that adaptive series or cubature fail.
    m = k215["first_sufficient_universal_whole_sum_dyadic_m"]
    c = Q(2**m + Q(1, 2**m), 2)
    large_q = (7*c - 1) / (256 + 7*c)
    assert large_q * Q(ORDER + 15, ORDER + 2) > 1
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {p.stem.split("-")[0]: hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in (K185, K213, K215)},
        "object": "K139/K184 raw unnormalized K213 term after radial elimination; angular simplex at fixed positive auxiliary t",
        "identity": "Let L_i=sum_(j:i in support_j) cosh(t_j), M=256+max_i L_i, a_i=(max L-L_i)/M, beta_i=5/3, beta_0=70/3. The angular integral of product_i z_i^(2/3)/(256+sum_i z_i L_i)^14 equals B(beta)/M^14 times sum_(n>=0) (14)_n/(beta_0)_n c_n, where c_0=1 and n c_n=(5/3) sum_(k=1)^n (sum_i a_i^k)c_(n-k). B(beta)=Gamma(5/3)^14/Gamma(70/3). Multiply by K213's 2^8*256^6*13!/5! and product cosh(t_j)/pi^8 before the signed K185 assembly.",
        "proof": "Dirichlet(5/3)^14 moments give E[U^n]=n!c_n/(70/3)_n for U=sum_i z_i a_i. Since 0<=U<=q<1, the positive binomial series for (1-U)^-14 converges uniformly on a finite auxiliary box. The coefficients follow by logarithmically differentiating product_i(1-a_i x)^(-5/3). For n>=N+1, the binomial-majorant ratio is at most q*(N+15)/(N+2), so its geometric tail bounds the angular truncation.",
        "all_mask_support_loads": dict(histogram),
        "term_count": 1864,
        "unique_allocations": len(unique),
        "small_box": {
            "auxiliary_domain": "[0,log(2)]^8",
            "maximum_cosh": "5/4",
            "q_ceiling": str(q),
            "series_order_inclusive": ORDER,
            "relative_to_B_over_M14_remainder_ceiling": str(remainder),
            "raw_term_absolute_error_ceiling": str(raw_term_bound),
            "whole_unsigned_1864_term_absolute_error_ceiling": str(1864 * raw_term_bound),
            "normalization": "Original raw K213 term, including angular product z_i^(2/3)/pi^8 and radial-elimination prefactor; bound uses pi>3, simplex volume 1/13!, log(2)<1."
        },
        "large_box": {
            "k215_whole_unsigned_tail_dyadic_m": m,
            "uniform_q_at_that_box": str(large_q),
            "order_20_geometric_ratio_exceeds_one": True,
            "scope": "This simple global binomial/geometric certificate does not close the large-box prefix at order 20; adaptive localization or a different route may. No complexity lower bound."
        },
        "example_loads_at_all_t_zero": list(example),
        "example_normalized_coefficients_at_all_t_zero": [str(x) for x in series_coefficients(tuple(Q(x) for x in example), 4)],
        "source_routing": k213["source_routing"],
        "unchanged_complete_rule_error_upper_rational": k215["unchanged_complete_rule_error_upper_rational"],
        "claim_ceiling": "Exact full-angular elimination and certified angular-series truncation on a small auxiliary box only. No certified eight-dimensional integration over K215's complete finite box, signed full-rule error, quotient/common-reference boundary composition, accurate order-six prefix, source action or physical state."
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] 1,864 support masks, exact angular series and small-box bound")
