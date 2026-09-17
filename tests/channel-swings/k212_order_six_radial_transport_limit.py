#!/usr/bin/env python3
"""K212: exact Gamma transport formula and K205 Lipschitz certificate floor."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path

from flint import arb, ctx

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / "lab/process"
K203 = P / "k203-order-six-positive-moment-rule.json"
K205 = P / "k205-order-six-radial-normal-form.json"
OUT = P / "k212-order-six-radial-transport-limit.json"
ctx.dps = 100
ctx.threads = 1


def ar(q: Q) -> arb:
    return arb(q.numerator) / arb(q.denominator)


def gamma_cdf(x: arb, shape: int) -> arb:
    y = 256*x
    return 1 - (-y).exp()*sum((y**k / math.factorial(k) for k in range(shape)), arb(0))


def truncated_first(x: arb) -> arb:
    return arb(6)/256*gamma_cdf(x, 7)


def transport(a: arb, b: arb, p: arb, t: arb) -> arb:
    """Monotone quantile coupling, with F_6(t)=p and a<t<b."""
    return (arb(6)/256 + 2*truncated_first(t)
            - 2*truncated_first(a) - 2*truncated_first(b)
            + a*(2*gamma_cdf(a, 6)-p)
            + b*(2*gamma_cdf(b, 6)-p-1))


def generate() -> dict:
    rule = json.loads(K203.read_text())
    radial = json.loads(K205.read_text())
    assert rule["rule"]["radial_nodes"] == ["(7-sqrt(7))/256", "(7+sqrt(7))/256"]
    assert rule["rule"]["radial_probabilities"] == ["(1+1/sqrt(7))/2", "(1-1/sqrt(7))/2"]
    s = arb(7).sqrt()
    a, b, p = (7-s)/256, (7+s)/256, (1+1/s)/2
    tl = Q("0.0270319788593502346489739")
    tu = Q("0.0270319788593502346489741")
    # Arb inequalities certify the unique quantile, including the radicals.
    assert a < ar(tl) and ar(tu) < b
    assert gamma_cdf(ar(tl), 6).upper() < p.lower()
    assert gamma_cdf(ar(tu), 6).lower() > p.upper()
    wl, wu = Q(5061527065, 10**12), Q(5061527066, 10**12)
    # The explicit formula is monotone in t only at the true quantile; take
    # an interval hull, not an endpoint monotonicity shortcut.
    t = ar(tl).union(ar(tu))
    w = transport(a, b, p, t)
    assert w.lower() > ar(wl) and w.upper() < ar(wu)
    assert wl < wu < Q(7, 512)  # K205's independent-coupling ceiling.
    # Gamma(6,256) has unique density maximum at x=5/256. e^5 exceeds
    # 4000/27 by its first 15 nonnegative Taylor terms, hence fmax < 45.
    exp5_lower = sum((Q(5**k, math.factorial(k)) for k in range(15)), Q(0))
    assert exp5_lower > Q(4000, 27)
    # Every mass-p_i Voronoi cell of a positive N-atom quantizer contributes
    # at least p_i^2/(4 M) to L1 transport when its density is <= M.
    # Cauchy then yields W1 >= 1/(4 M N) > 1/(180 N).
    old = Q(radial["all_groups_radial_only_error_upper_rational"])
    lip = old / Q(7, 512)
    assert lip == Q(7)*sum(Q(v["ordered_support_terms"])
                            for v in radial["groups"].values()) * Q(
                                json.loads((P / "k202-order-six-common-weighted-core.json").read_text())[
                                    "per_support_term_integral_ceiling_rational"])
    threshold = Q(1, 10**21)
    minimum_nodes = lip / (180*threshold)
    result = {
        "schema_version": "1.0", "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {"K203": hashlib.sha256(K203.read_bytes()).hexdigest(),
                         "K205": hashlib.sha256(K205.read_bytes()).hexdigest()},
        "reference": "Gamma(shape=6, rate=256); angular Dirichlet reference held exact",
        "rule": "K203 positive two-node radial Gaussian rule, not its angular replacement",
        "cdf": "F_6(x)=1-exp(-256x)*sum(k=0..5)(256x)^k/k!",
        "truncated_first": "H(x)=(6/256)*F_7(x)",
        "quantile": "unique t in (a,b) with F_6(t)=p; a=(7-sqrt(7))/256, b=(7+sqrt(7))/256, p=(1+1/sqrt(7))/2",
        "quantile_open_rational_interval": [str(tl), str(tu)],
        "w1_formula": "6/256+2H(t)-2H(a)-2H(b)+a*(2F_6(a)-p)+b*(2F_6(b)-p-1)",
        "w1_open_rational_interval": [str(wl), str(wu)],
        "k205_lipschitz_aggregate_rational": str(lip),
        "radial_only_error_open_rational_interval": [str(lip*wl), str(lip*wu)],
        "k205_prior_radial_upper_rational": str(old),
        "density_max": "256*5^5*exp(-5)/5! < 45 (Taylor lower bound for exp(5))",
        "positive_n_atom_w1_floor": "W1(Gamma(6,256),Q_N)>=1/(4*fmax*N)>1/(180*N)",
        "k205_certificate_floor": "L_K205*W1 > L_K205/(180*N), for the unchanged termwise Lipschitz constant L_K205",
        "budget": "1/10^21",
        "necessary_positive_radial_node_count_for_this_certificate": math.floor(minimum_nodes)+1,
        "conditional_total_error_decomposition": "|E_r E_z f-Q_r Q_z f| <= L_K205 W1(E_r,Q_r) + sum_g[B_g(K185/K188 quotient exclusion)+P_g(K204/K209 common-reference polynomial defects)+C_d M_d,g(core signed remainder)]; the second bracket remains uncomputed, and each term requires a compatible core normalization before numerical addition",
        "boundary_composition": "K185/K188 quotient face/tail/small-rho bounds are separate from K204/K209 common-reference deletion and polynomial defects; neither is a signed core-cell derivative enclosure",
        "claim_ceiling": "A lower floor on the worst-case positive-atom K205 Lipschitz certificate, NOT on actual radial or signed error; higher derivatives, signed cancellation, different weights/estimates and angular errors remain open. No source/physics move."
    }
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] exact quantile/W1 expression outward-enclosed")
    print("[PASS] positive N-atom density theorem and K205 certificate floor")
    print("necessary atoms for 1e-21:", result["necessary_positive_radial_node_count_for_this_certificate"])
