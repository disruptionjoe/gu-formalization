#!/usr/bin/env python3
"""K225: exact common-cosh cancellation and an anisotropy majorant for K218."""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
K185 = ROOT / "lab/process/k185-order-six-duffy-face-tail-wave.json"
K218 = ROOT / "lab/process/k218-order-six-exact-angular-elimination.json"
K224 = ROOT / "lab/process/k224-order-six-second-shell-cost-stress.json"
OUT = ROOT / "lab/process/k225-order-six-diagonal-cancellation.json"


def terms(source: dict):
    catalog = source["exact_allocation_certificate"]["allocation_catalog"]
    for entry in source["complete_face_hypergraph"]["entries"]:
        outer = entry["coefficient_product"] * (2 if entry["left"] != entry["right"] else 1)
        for term in entry["terms"]:
            masks = tuple(int(s, 16) for s in catalog[term["allocation_id"]]["support_masks_hex"].split(","))
            yield outer * term["leibniz_sign"], masks


def signature(masks: tuple[int, ...], free: tuple[int, ...]) -> tuple:
    """The unordered fourteen affine factors after all other c_j equal b."""
    fixed = set(range(8)) - set(free)
    return tuple(sorted((sum(bool(masks[j] & (1 << i)) for j in fixed),
                         tuple(int(bool(masks[j] & (1 << i))) for j in free))
                        for i in range(14)))


def grouping(items: list, free: tuple[int, ...]) -> tuple[int, int]:
    buckets = defaultdict(int)
    for weight, masks in items:
        buckets[signature(masks, free)] += weight
    return len(buckets), sum(value != 0 for value in buckets.values())


def core(items: list, c: tuple[Q, ...]) -> Q:
    total = Q(0)
    for weight, masks in items:
        loads = [256 + sum(c[j] for j, mask in enumerate(masks) if mask & (1 << i))
                 for i in range(14)]
        product = 1
        for load in loads:
            product *= load
        total += Q(weight, product)
    return total


def mixed_majorant(items: list, c: tuple[Q, ...], j: int, k: int) -> Q:
    """Unsigned upper for |d_j d_k H| on coordinates >= c."""
    bound = Q(0)
    for weight, masks in items:
        loads = [256 + sum(c[h] for h, mask in enumerate(masks) if mask & (1 << i))
                 for i in range(14)]
        product = 1
        for load in loads:
            product *= load
        lj = sum((Q(1, loads[i]) for i in range(14) if masks[j] & (1 << i)), Q(0))
        lk = sum((Q(1, loads[i]) for i in range(14) if masks[k] & (1 << i)), Q(0))
        shared = sum((Q(1, loads[i]**2) for i in range(14)
                      if masks[j] & masks[k] & (1 << i)), Q(0))
        bound += Q(abs(weight), product) * (lj * lk + shared)
    return bound


def generate() -> dict:
    source = json.loads(K185.read_text())
    items = list(terms(source))
    assert len(items) == 1864
    strata = {}
    for free in ((0, 1), *((0, 1, j) for j in range(2, 8))):
        count, residual = grouping(items, free)
        assert residual == 0
        strata[",".join(map(str, free))] = {"factor_multisets": count,
                                            "nonzero_coefficient_groups": residual}
    # A contrary mixed point proves this is not a whole-core zero identity.
    c = (Q(5, 4), Q(17, 8), Q(5, 4), Q(1), Q(17, 8), Q(1), Q(1), Q(1))
    value = core(items, c)
    assert value != 0
    anchor = Q(1)
    lower = (c[0], c[1]) + (anchor,) * 6
    bound = sum(((c[j] - anchor) * (c[k] - anchor) * mixed_majorant(items, lower, j, k)
                 for j in range(2, 8) for k in range(j+1, 8)), Q(0))
    assert abs(value) <= bound
    return {
        "schema_version": "1.0", "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {p.stem.split("-")[0]: hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in (K185, K218, K224)},
        "object": "K218 original signed eight-auxiliary rational-cosh core H, excluding the positive product-cosh and pi^-8 factors",
        "raw_signed_terms": len(items), "certified_strata": strata,
        "identity": "For arbitrary u,v,b,x>=1, H(u,v,b,b,b,b,b,b)=0 and H(u,v,b,...,x at any one index 2..7,...,b)=0. For each free set (0,1,j), replace the remaining c coordinates by b. All fourteen affine factors then have the form 256+n_b*b+n_0*u+n_1*v+n_j*x. The K185 signed integer coefficients sum to zero for EACH unordered multiset of fourteen (n_b,n_0,n_1,n_j) factors, not merely at sampled values. The (0,1) case follows likewise.",
        "mixed_derivative_rule": "Fix u,v>=1 and y_2..y_7>=b>=1. H(u,v,y) equals sum over 2<=j<k<=7 of int_b^y_k int_b^y_j d_j d_k H(u,v,y_2..y_(j-1),s_j,b_(j+1)..b_(k-1),s_k,b_(k+1)..b_7) ds_j ds_k. This is two successive finite telescopes and uses the exact zero on every single-exception stratum. Empty/reversed integrals are interpreted with sign when b is not a lower anchor.",
        "majorant_rule": "With b<=min(y_2..y_7), a_Ai(c)=256+sum_j mask_Aji*c_j, q_A=prod_i a_Ai^-1, L_Aj=sum_i mask_Aji/a_Ai and C_Ajk=sum_i mask_Aji*mask_Aki/a_Ai^2, set M_jk(u,v,b)=sum_A |w_A|q_A(u,v,b^6)(L_Aj L_Ak+C_Ajk) at that lower point. Positivity and coordinatewise decrease of every factor imply |H(u,v,y)|<=sum_(2<=j<k<=7)(y_j-b)(y_k-b) M_jk(u,v,b). The exact signed second derivative is sum_A w_A q_A(L_Aj L_Ak+C_Ajk).",
        "mixed_control": {"coshes": [str(x) for x in c], "core_exact": str(value),
                          "majorant_exact": str(bound), "strictly_nonzero": True},
        "claim_ceiling": "An exact original-K185 subspace cancellation and pointwise correlated anisotropy majorant, not an integrated bound, adaptive cell cost, accurate K215 finite prefix, coalescent/quotient/reference composition, source/physics/ledger/canon change or whole-core zero theorem."
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K225 exact common-cosh strata, mixed derivative rule and nonzero control")
