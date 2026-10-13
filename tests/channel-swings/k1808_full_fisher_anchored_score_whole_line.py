#!/usr/bin/env python3
"""K1808 analytic tails for the slab-two anchored-score witness."""
from __future__ import annotations

import importlib.util
import json
import sys
from fractions import Fraction as F
from pathlib import Path

from flint import arb

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1808-full-fisher-anchored-score-whole-line.json"
K1807 = ROOT / "lab/process/k1807-full-fisher-anchored-score-compact-taylor.json"
BASE = ROOT / "tests/channel-swings/k1786_full_fisher_whole_line_tail_jet.py"
SPEC = importlib.util.spec_from_file_location("k1786_for_k1808", BASE)
m = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = m
SPEC.loader.exec_module(m)
k = m.k

T_LO = F(56314519603, 1099511627776)
T_HI = F(887855469, 17179869184)
Z_LO = F(589, 1024)
Z_HI = F(1185, 2048)
ANCHOR_T = T_HI
ANCHOR_Z = F(576161143609, 10**12)
THRESHOLD = F(31835729061, 200000000000000000)


def fixed_anchor_score_square_majorant():
    t0, z0 = k.J(k.aq(ANCHOR_T)), k.J(k.aq(ANCHOR_Z))
    p0, a0, b0, v0 = k.channel(t0, z0)
    ra0, rb0, rt0 = a0.sqrt(), b0.sqrt(), t0.sqrt()
    ca0, cb0 = rt0 * ra0 / v0, rt0 * rb0 / v0
    wa0 = p0 * (-t0 * a0 / (2 * v0)).exp()
    wb0 = (1 - p0) * (-t0 * b0 / (2 * v0)).exp()
    denominator0 = m.exponential_basis(wa0, ca0) + m.exponential_basis(wb0, cb0)
    numerator0 = m.exponential_basis(wa0 * ra0, ca0) + m.exponential_basis(wb0 * rb0, cb0)
    residual0 = numerator0 + (m.constant_jet(rt0) * denominator0).times_x()
    denominator0_floor = m.lower((wa0 + wb0).v)
    reciprocal0 = m.reciprocal_majorant(denominator0, denominator0_floor)
    score0 = m.constant_jet(rt0 / v0) * residual0 * reciprocal0
    return score0 * score0, denominator0_floor


def b_tail_bound():
    t = k.J.var(k.ball(T_LO, T_HI), 0)
    z = k.J.var(k.ball(Z_LO, Z_HI), 1)
    p, a, b, v = k.channel(t, z)
    ra, rb, rt, rv = a.sqrt(), b.sqrt(), t.sqrt(), v.sqrt()
    ca, cb = rt * ra / v, rt * rb / v
    wa = p * (-t * a / (2 * v)).exp()
    wb = (1 - p) * (-t * b / (2 * v)).exp()
    denominator = m.exponential_basis(wa, ca) + m.exponential_basis(wb, cb)
    gaussian_rate_jet = k.J(1) / (2 * v)
    gaussian = m.gaussian_majorant(gaussian_rate_jet)
    score0_square, denominator0_floor = fixed_anchor_score_square_majorant()
    prefactor = m.constant_jet(k.J(1) / (rv * k.J((2 * arb.pi()).sqrt())))
    integrand = prefactor * gaussian * denominator * score0_square
    gaussian_rate = m.lower(gaussian_rate_jet.v)
    linear_rate = max(m.upper(ca.v), m.upper(cb.v),
                      m.upper((k.J(k.aq(ANCHOR_T)).sqrt()
                               * (k.J(1) - k.J(k.aq(ANCHOR_Z))).sqrt()
                               / (k.J(1) - k.J(k.aq(ANCHOR_T)))).v),
                      m.upper((k.J(k.aq(ANCHOR_T)).sqrt()
                               * (k.J(1) + (k.J(2) - k.J(k.aq(F(1, 1024)))
                                           / k.J(k.aq(ANCHOR_T))**2)
                                 / k.J(k.aq(ANCHOR_Z))).sqrt()
                               / (k.J(1) - k.J(k.aq(ANCHOR_T)))).v))
    bound = m.integrate_terms(integrand.v, gaussian_rate, linear_rate)
    return bound, denominator0_floor, gaussian_rate, linear_rate, len(integrand.v)


def compute():
    m.CENTER_T = (T_LO + T_HI) / 2
    m.CENTER_Z = (Z_LO + Z_HI) / 2
    m.RADIUS_T = (T_HI - T_LO) / 2
    m.RADIUS_Z = (Z_HI - Z_LO) / 2
    j_tail = arb(m.compute()["absolute_two_tail_bounds"]["value"])
    b_tail, d0_floor, gaussian_rate, linear_rate, term_count = b_tail_bound()
    a_tail = (j_tail * b_tail).sqrt()
    compact = json.loads(K1807.read_text())["certificate"]["compact_bounds"]
    compact_margin = arb(compact["cross_margin_lower"])
    a_cap = arb("2e-7")
    perturbation = 2 * a_cap * a_tail + a_tail**2 + k.aq(THRESHOLD) * b_tail
    whole_margin = arb(compact_margin.lower()) - arb(perturbation.upper())
    return {
        "rectangle": {"t": [str(T_LO), str(T_HI)], "z": [str(Z_LO), str(Z_HI)]},
        "tail_start": "11",
        "anchor_denominator_floor": k.enc(d0_floor),
        "gaussian_rate_floor": k.enc(gaussian_rate),
        "linear_exponent_ceiling": k.enc(linear_rate),
        "b_tail_term_count": term_count,
        "absolute_two_tail_bounds": {
            "J": k.enc(j_tail),
            "B": k.enc(b_tail),
            "A_by_cauchy": k.enc(a_tail),
        },
        "compact_cross_margin_lower": compact["cross_margin_lower"],
        "tail_perturbation_upper": k.enc(perturbation),
        "whole_line_cross_margin_lower": k.enc(whole_margin),
        "whole_line_cross_margin_positive": bool(whole_margin > 0),
    }


def validate(data, got=None):
    got = compute() if got is None else got
    cert = data["certificate"]
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1808"),
        ("inputs", data["inputs"] == ["K1786", "K1806", "K1807"]),
        ("rectangle", cert["rectangle"] == got["rectangle"]),
        ("tail start", cert["tail_start"] == "11"),
        ("anchor denominator", arb(cert["anchor_denominator_floor"]) > 0),
        ("gaussian rate", arb(cert["gaussian_rate_floor"]) > 0),
        ("term count", cert["b_tail_term_count"] == got["b_tail_term_count"]),
    ]
    for key, value in got["absolute_two_tail_bounds"].items():
        checks.append((f"tail {key}", arb(cert["absolute_two_tail_bounds"][key]).contains(arb(value))))
    checks += [
        ("perturbation", arb(cert["tail_perturbation_upper"]).contains(arb(got["tail_perturbation_upper"]))),
        ("positive whole margin", arb(cert["whole_line_cross_margin_lower"]) > 0),
        ("whole line certified", data["decision"]["complete_slab_two_whole_line_witness_certified"]),
        ("global open", not data["decision"]["global_optimizer_proved"]),
    ]
    return checks


def main():
    if not ARTIFACT.exists() or "--print" in __import__("sys").argv:
        print(json.dumps(compute(), indent=2))
        return
    checks = validate(json.loads(ARTIFACT.read_text()))
    for index, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {index:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
