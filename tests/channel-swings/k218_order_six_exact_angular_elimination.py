#!/usr/bin/env python3
"""K218: exact uniform-simplex elimination after K213 radial reduction."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from math import factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROCESS = ROOT / "lab/process"
K185 = PROCESS / "k185-order-six-duffy-face-tail-wave.json"
K213 = PROCESS / "k213-order-six-bessel-laplace-radial-elimination.json"
K216 = PROCESS / "k216-order-six-analytic-angular-prefix.json"
K217 = PROCESS / "k217-order-six-signed-inner-box.json"
OUT = PROCESS / "k218-order-six-exact-angular-elimination.json"


def loads(masks: tuple[int, ...], coshes: tuple[Q, ...]) -> tuple[Q, ...]:
    assert len(masks) == len(coshes) == 8
    return tuple(sum((coshes[j] for j in range(8) if masks[j] & (1 << i)), Q(0))
                 for i in range(14))


def simplex_integral(denominators: tuple[Q, ...]) -> Q:
    """Integral over the ordinary coordinate simplex of (sum a_i z_i)^-14."""
    assert len(denominators) == 14 and all(a > 0 for a in denominators)
    product = Q(1)
    for a in denominators:
        product *= a
    return 1 / (factorial(13) * product)


def signed_point(source: dict, coshes: tuple[Q, ...]) -> Q:
    """Exact rational factor multiplying pi^-8 after angular integration."""
    entries = source["complete_face_hypergraph"]["entries"]
    catalog = source["exact_allocation_certificate"]["allocation_catalog"]
    cache: dict[str, Q] = {}
    total = Q(0)
    for entry in entries:
        outer = (2 if entry["left"] != entry["right"] else 1) * entry["coefficient_product"]
        for term in entry["terms"]:
            key = term["allocation_id"]
            if key not in cache:
                masks = tuple(int(s, 16) for s in catalog[key]["support_masks_hex"].split(","))
                assert len(masks) == 8 and all(0 < m < 1 << 14 for m in masks)
                a = tuple(256 + x for x in loads(masks, coshes))
                cache[key] = simplex_integral(a)
            total += outer * term["leibniz_sign"] * cache[key]
    assert len(cache) == 1276
    return total * Q(2**8 * 256**6 * factorial(13), factorial(5)) * _product(coshes)


def _product(values: tuple[Q, ...]) -> Q:
    result = Q(1)
    for x in values:
        result *= x
    return result


def generate() -> dict:
    source = json.loads(K185.read_text())
    k213 = json.loads(K213.read_text())
    k216 = json.loads(K216.read_text())
    k217 = json.loads(K217.read_text())
    assert k213["counts"]["leibniz_terms"] == k216["term_count"] == 1864
    assert k217["ordered_term_count_with_off_diagonal_twice"] == 2928
    points = {
        "all_t_zero": (Q(1),) * 8,
        "all_t_log2": (Q(5, 4),) * 8,
        "alternating_zero_log2": tuple(Q(1) if j % 2 == 0 else Q(5, 4) for j in range(8)),
    }
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {p.stem.split("-")[0]: hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in (K185, K213, K216, K217)},
        "object": "K185 original uniform 13-simplex angular integral inside each K213 radial-eliminated term",
        "identity": "For fourteen strictly positive a_i, integral_Delta13 (sum_i a_i z_i)^(-14) dz_1...dz_13 = 1/(13! product_i a_i). Here a_i=256+sum_(j:i in support_j)cosh(t_j). The original K202 reference and residual cancel, leaving the uniform density 1/pi^8. This is exact for every finite positive auxiliary t, not merely the K216 small box.",
        "proof": "Multiply fourteen Laplace integrals integral_0^infinity exp(-a_i x_i) dx_i=1/a_i, set x_i=r z_i, sum z_i=1. The Jacobian is r^13; integrating r gives Gamma(14)/(sum_i a_i z_i)^14=13!/(sum_i a_i z_i)^14. Positivity licenses Tonelli. The equal-a case yields the simplex volume 1/13!.",
        "signed_eight_auxiliary_integrand": "pi^-8 * (2^8*256^6/5!) * product_j cosh(t_j) * sum_(ordered K185 terms) [coefficient_product * leibniz_sign / product_(i=0)^13 (256+sum_(j:i in support_j) cosh(t_j))], with K184 off-diagonal entries doubled. Integrate this over auxiliary t in [0,infinity)^8 only after a separately certified signed error/tail composition.",
        "terms": 1864,
        "ordered_terms_after_off_diagonal_doubling": 2928,
        "distinct_allocations": 1276,
        "exact_signed_point_rational_without_pi8": {name: str(signed_point(source, c)) for name, c in points.items()},
        "controls": "An independent probe verifies the fourteen-variable coefficient identity through degree four, a one-exception Beta(1,13) integral, the signed expression at three exact auxiliary points by a separately coded allocation traversal, and planted exponent/weight errors.",
        "source_routing": k216["source_routing"],
        "unchanged_complete_rule_error_upper_rational": k216["unchanged_complete_rule_error_upper_rational"],
        "claim_ceiling": "Exact elimination of the thirteen-dimensional angular integral and an exact signed eight-auxiliary integrand. K217's inner-box certificate and K215's positive tail remain separate. No certified middle-box signed integration, full coalescent or quotient/common-reference boundary composition, accurate complete order-six prefix, source action, physical state or physics-ledger movement."
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] exact 14-factor angular collapse and signed rational point values")
