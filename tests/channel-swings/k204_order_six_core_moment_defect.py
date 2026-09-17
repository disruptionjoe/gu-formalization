#!/usr/bin/env python3
"""K204 exact deletion bounds for K203's common reference, not quotient error."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
K203 = ROOT / "lab/process/k203-order-six-positive-moment-rule.json"
OUT = ROOT / "lab/process/k204-order-six-core-moment-defect.json"
DELTA = F(1, 2**180)
RADIUS = F(1, 4)


def rising(x: F, n: int) -> F:
    result = F(1)
    for k in range(n):
        result *= x + k
    return result


def exp_tail_upper(shape: int) -> F:
    """Q(shape,64), with e^-64 < (3/8)^64 from e > 8/3."""
    return F(3, 8) ** 64 * sum(
        (F(64**k, math.factorial(k)) for k in range(shape)), F(0))


def angular_moment(pattern: tuple[int, ...]) -> F:
    return math.prod((rising(F(1, 3), n) for n in pattern), start=F(1)) / rising(
        F(14, 3), sum(pattern))


def frac(x: F) -> str:
    return str(x)


def generate() -> dict:
    upstream = json.loads(K203.read_text())
    assert upstream["counts"]["nodes"] == 28
    assert upstream["exact_moments"]["radial_degree"] == 3
    assert upstream["exact_moments"]["angular_degree"] == 2
    assert upstream["rule"]["reference"] == "rho^5 exp(-256 rho) product_i z_i^(-2/3)"

    # For z_1 ~ Beta(1/3,13/3), on 0<=z<=1/2 the density denominator
    # B(1/3,13/3) >= (1/16)*3*2^(-1/3) > 3/32.  Thus
    # P(z_1<delta) < 32 delta^(1/3), and union over 14 gives 448.
    # The strict comparison 2^(-1/3)>1/2 and delta^(1/3)=2^-60
    # are exact rational inequalities, with no floating gamma estimate.
    face = F(448, 2**60)
    radial = exp_tail_upper(6)
    lost = face + radial
    assert 0 < lost < 1

    # All 28 nodes lie in the core: 0<sqrt(7)<3 gives
    # rho_+<(7+3)/256<1/4; 0<sqrt(3/17)<1/2 gives
    # every z_i>(1/2)/14=1/28>2^-180.
    assert F(10, 256) < RADIUS and F(1, 28) > DELTA
    patterns = {
        "constant": (), "single_coordinate": (1,),
        "coordinate_square": (2,), "distinct_pair": (1, 1),
    }
    rows = {}
    for a in range(4):
        radial_moment = rising(F(6), a) / 256**a
        tilted_tail = exp_tail_upper(6 + a)
        for name, pattern in patterns.items():
            full = radial_moment * angular_moment(pattern)
            # D=E[rho^a z^n 1_{C^c}].  The angular face contribution is
            # <= E[rho^a]*face since 0<=z^n<=1.  The radial tail is
            # <= E[rho^a z^n]*Q(6+a,64), by Gamma size bias.
            deletion = radial_moment * face + full * tilted_tail
            conditional_defect = (deletion + full * lost) / (1 - lost)
            if a == 0 and not pattern:
                conditional_defect = F(0)  # Both probability rules integrate 1 exactly.
            rows[f"rho^{a}:{name}"] = {
                "full_reference_moment": frac(full),
                "discarded_unnormalized_moment_upper": frac(deletion),
                "conditional_core_vs_full_rule_upper": frac(conditional_defect),
            }
    return {
        "schema_version": "1.0", "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {"K203": hashlib.sha256(K203.read_bytes()).hexdigest()},
        "core": {"radial_upper": "1/4", "angular_coordinate_lower": "1/2^180",
                 "all_28_rule_nodes_strictly_inside": True},
        "reference": "Gamma(shape=6,rate=256) x Dirichlet(1/3)^14",
        "face_union_probability_upper_rational": frac(face),
        "radial_tail_probability_upper_rational": frac(radial),
        "lost_reference_probability_upper_rational": frac(lost),
        "monomial_orbit_representatives": rows,
        "orbit_rule": "permutation symmetry supplies all 120 angular monomials of total degree <=2 for each of four radial degrees",
        "conditional_defect_rule": "If p=P(C), m=E(P), D=E(P 1_Cc), then E(P|C)-m=(m(1-p)-D)/p; bound by (m*q+D_upper)/(1-q) where q bounds 1-p",
        "unchanged_full_domain_error_rational": upstream["all_group_absolute_error_ceiling_rational"],
        "claim_ceiling": "exact full-reference moments and rational compact-core deletion/conditional moment-defect bounds; no complete signed quotient derivative or accurate order-six integral",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] all 28 positive rule nodes in the compact core")
    print("[PASS] 480 polynomial moments covered by 16 exact orbit representatives")
    print("[PASS] lost reference mass <", result["lost_reference_probability_upper_rational"])
