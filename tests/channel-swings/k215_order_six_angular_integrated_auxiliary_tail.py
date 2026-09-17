#!/usr/bin/env python3
"""K215: rational full-simplex integral of K214's positive auxiliary tail."""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / "lab/process"
INPUTS = {name: P / f"{name}-order-six-{suffix}.json" for name, suffix in (
    ("k185", "duffy-face-tail-wave"),
    ("k213", "bessel-laplace-radial-elimination"),
    ("k214", "support-aware-auxiliary-tail"),
)}
OUT = P / "k215-order-six-angular-integrated-auxiliary-tail.json"
N = 14
FACTORS = 8
POWER = Q(1, 4)
TERM_BUDGET = Q(1, 10**21)
GROUP_BUDGET = Q(1, 10**21)


def gamma_ceiling(beta: Q) -> Q:
    """Gamma(beta)<1/beta+3/8 for 0<beta<=1."""
    assert 0 < beta <= 1
    return 1 / beta + Q(3, 8)


def sinh_dyadic(m: int) -> Q:
    assert m >= 1
    return Q(2**m - Q(1, 2**m), 2)


def cutoff(coefficient: Q, target: Q) -> int:
    """Test coefficient*(256/sinh(m log 2))^(1/4)<target exactly."""
    assert coefficient > 0 and target > 0
    m = 1
    while coefficient**4 * Q(256, sinh_dyadic(m)) >= target**4:
        m += 1
    assert m == 1 or coefficient**4 * Q(256, sinh_dyadic(m - 1)) >= target**4
    return m


def coefficient(loads: tuple[Q, ...], masks: tuple[int, ...]) -> Q:
    assert len(loads) == N and len(masks) == FACTORS
    assert sum(loads) == FACTORS and max(loads) <= Q(2, 3)
    beta = tuple(1 - a for a in loads)
    base = [gamma_ceiling(b) for b in beta]
    product = Q(1)
    for b in base:
        product *= b
    total = Q(0)
    for mask in masks:
        assert 0 < mask < 1 << N
        # S_j >= z_i for each supported i. Select the smallest rigorous
        # Gamma-product ceiling, never an angular sample or a new allocation.
        ratio = min(gamma_ceiling(beta[i] - POWER) / base[i]
                    for i in range(N) if mask & (1 << i))
        total += product * ratio
    # Raw time integral: Gamma(6)/256^6, (2*pi)^-8 and K214's 2^8.
    # pi>3, C_w<=1, Gamma(6-1/4)=Gamma(23/4)>28.
    return Q(120, 3**8 * 256**6 * 28) * total


def generate() -> dict:
    k185 = json.loads(INPUTS["k185"].read_text())
    k213 = json.loads(INPUTS["k213"].read_text())
    k214 = json.loads(INPUTS["k214"].read_text())
    catalog = k185["exact_allocation_certificate"]["allocation_catalog"]
    entries = k185["complete_face_hypergraph"]["entries"]
    assert k213["counts"]["leibniz_terms"] == 1864
    assert k214["barycenter_diagnostic"]["terms"] == 1864
    assert all(v["maximum_load"] in ("4/7", "7/12", "3/5", "5/8", "2/3")
               for v in catalog.values())
    universal = Q(120 * FACTORS, 3**8 * 256**6 * 28) * Q(99, 8) * Q(27, 8)**13
    assert cutoff(universal, TERM_BUDGET) == 172
    hist = Counter()
    cache: dict[str, Q] = {}
    count = 0
    largest = Q(0)
    for row in entries:
        for term in row["terms"]:
            key = term["allocation_id"]
            if key not in cache:
                alloc = catalog[key]
                loads = tuple(Q(x) for x in alloc["loads"].split(","))
                masks = tuple(int(x, 16) for x in alloc["support_masks_hex"].split(","))
                cache[key] = coefficient(loads, masks)
                assert cache[key] <= universal
            bound = cache[key]
            largest = max(largest, bound)
            hist[cutoff(bound, TERM_BUDGET)] += 1
            count += 1
    assert count == 1864 and sum(hist.values()) == count
    # The absolute sum of 1,864 positive term tails is bounded even when
    # the complete signed group assembly is not numerically integrated.
    total_m = cutoff(universal * count, GROUP_BUDGET)
    assert total_m < 443
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {k: hashlib.sha256(v.read_bytes()).hexdigest() for k, v in INPUTS.items()},
        "object": "K139/K184 raw unnormalized time-Gram integral, each positive K185 Leibniz term",
        "theorem": "For T=m log 2, m>=1, the full-simplex integral of the K214 unsigned auxiliary tail is strictly below B_a*(256/sinh(T))^(1/4). B_a is an exact rational K185 allocation coefficient computed by this script; it is independent of the 2^-180 core floor.",
        "proof": "K214 bounds one coordinate tail by (2^8/product S_j)*(256/(256+S_j sinh T))^6. Since (1+x)^-6<=x^-1/4 for x>0, allocate the extra S_j^-1/4 to any supported z_i^-1/4. K185 AM--GM majorizes 1/product S by C_w product z_i^-alpha_i, with C_w<=1, sum alpha=8 and alpha_i<=2/3. Each shifted beta_i=1-alpha_i-1/4>=1/12. The simplex integral is product Gamma(beta_k-shift)/Gamma(23/4). Gamma(beta)<1/beta+3/8, Gamma(23/4)>28 and pi>3 yield B_a. The raw Gamma(6,256) normalization contributes 120/256^6; the original (2*pi)^-8 cancels K214's 2^8. No signed cancellation is used.",
        "normalization": "B_a = 120/(3^8*256^6*28) * sum_(j=1)^8 min_(i in support_j) product_(k=1)^14 [1/(beta_k-(1/4)1_(k=i))+3/8]",
        "elementary_gamma_lower": "Gamma(23/4)=(19*15*11*7*3/4^5)Gamma(3/4); Gamma(3/4)>4/(3e)>4/9 since e<3, hence Gamma(23/4)>28.",
        "universal_rational_coefficient": str(universal),
        "universal_per_term_target": "1/10^21",
        "first_sufficient_universal_per_term_dyadic_m": cutoff(universal, TERM_BUDGET),
        "mask_count": count,
        "unique_allocations": len(cache),
        "mask_specific_first_m_histogram": {str(k): hist[k] for k in sorted(hist)},
        "mask_specific_worst_first_m": max(hist),
        "whole_unsigned_1864_term_budget": "1/10^21",
        "first_sufficient_universal_whole_sum_dyadic_m": total_m,
        "comparison": "K214's 443 is sufficient per term pointwise on its angular core, whereas these are integrated full-simplex raw-time absolute-tail bounds; their targets and normalization differ. Neither is a necessary node cutoff.",
        "unchanged_complete_rule_error_upper_rational": k214["unchanged_complete_rule_error_upper_rational"],
        "source_routing": k214["source_routing"],
        "claim_ceiling": "Full angular integration of a positive auxiliary-box tail, including a conservative 1,864-term absolute sum. No finite-box prefix cubature, complete signed angular cell error, K185/K188 versus K204/K209 boundary composition, accurate order-six prefix, action-selected physical state or source verdict."
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] 1,864 angular-integrated term tails and rational dyadic cutoffs")
    print("[PASS] universal per-term m =", result["first_sufficient_universal_per_term_dyadic_m"])
    print("[PASS] universal whole-sum m =", result["first_sufficient_universal_whole_sum_dyadic_m"])
