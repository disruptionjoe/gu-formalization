#!/usr/bin/env python3
"""K247: degree-21 cumulative q<=15 signed boundary."""
from __future__ import annotations

import argparse, json
from fractions import Fraction as Q
from hashlib import sha256
from math import factorial
from flint import arb, ctx, fmpq
from k242_order_six_third_shell_signed_taylor import (
    K185, ROOT, coefficient_hash, evaluate_log_polynomial, integrate_polynomial,
    log_polynomial_hash, moment_polynomials, orbit_groups, taylor_polynomials, terms,
)
from k243_order_six_budget_composition_q6_method_limit import PI_LOWER
from k244_order_six_exact_corner_shell_ladder import complete_homogeneous, exact_corner, sinh_log
from k246_order_six_inner_cube_reallocation import OUT as K246

OUT = ROOT / "lab/process/k247-order-six-cumulative-q15-boundary.json"
ORDER, TAIL_START, QMAX = 21, 22, 15
LOWER, UPPER = fmpq(13419, 10**25), fmpq(13420, 10**25)
ctx.prec = 256

def row(v):
    q = Q(str(v)); return {"numerator": q.numerator, "denominator": q.denominator, "decimal": f"{float(q):.12e}"}

def tail_majorant(groups):
    x = exact_corner(QMAX); total = fmpq(0); maximum = fmpq(0)
    for rows, weight in groups.items():
        base = fmpq(1); ratios = []
        for mask in rows:
            d = 256 + mask.bit_count(); base /= d; ratios.append(x * mask.bit_count() / d)
        ratio = max(ratios) * fmpq(TAIL_START + 14, TAIL_START + 1)
        assert ratio < 1; maximum = max(maximum, ratio)
        total += abs(weight) * base * complete_homogeneous(ratios, TAIL_START) / (1 - ratio)
    return total, maximum

def generate():
    groups = orbit_groups(list(terms(json.loads(K185.read_text()))))
    assert len(groups) == 307
    polynomials = taylor_polynomials(groups, ORDER)
    moments = moment_polynomials(QMAX, ORDER); coefficients = [fmpq(0)] * 9
    for polynomial in polynomials:
        for power, value in enumerate(integrate_polynomial(polynomial, moments)):
            coefficients[power] += value
    norm = arb(2**8 * 256**6) / factorial(5) / arb.pi()**8
    polynomial = norm * evaluate_log_polynomial(coefficients, QMAX)
    assert polynomial > arb(str(LOWER)) and polynomial < arb(str(UPPER))
    core_tail, ratio = tail_majorant(groups)
    tail = fmpq(2**8 * 256**6, factorial(5)) / PI_LOWER**8 * sinh_log(QMAX)**8 * core_tail
    complete_lower, complete_upper = LOWER - tail, UPPER + tail
    budget = fmpq(1, 10**21)
    assert complete_lower > budget
    return {
      "schema_version":"1.0", "classification":"INTERNAL_STRUCTURAL_ONLY",
      "input_sha256":{"k185":sha256(K185.read_bytes()).hexdigest(),"k246":sha256(K246.read_bytes()).hexdigest()},
      "object":"complete cumulative signed K218 cube q<=15 at total degree 21",
      "scope":"exact K213/K218 internal order-six cumulative prefix; not a full-error or source/physics verdict",
      "expansion":{"order":ORDER,"tail_start":TAIL_START,"raw_terms":1864,"orbits":307,
        "degree_sha256":{str(i):coefficient_hash(p) for i,p in enumerate(polynomials)},
        "integrated_log_polynomial_sha256":log_polynomial_hash(coefficients)},
      "certificate":{"region":"q<=15","exact_x_max":str(exact_corner(QMAX)),
        "signed_order_0_through_21_arb":str(polynomial),"strict_polynomial_lower":str(LOWER),"strict_polynomial_upper":str(UPPER),
        "exact_core_tail_majorant":str(core_tail),"maximum_geometric_ratio":str(ratio),"exact_measure":str(sinh_log(QMAX)**8),
        "normalized_tail_upper":row(tail),"complete_lower":row(complete_lower),"complete_upper":row(complete_upper)},
      "decision":{"target":row(budget),"complete_lower_exceeds_target":True,
        "lower_to_target":f"{float(Q(str(complete_lower/budget))):.12e}",
        "result":"cumulative_q15_prefix_exceeds_target__farther_signed_cancellation_unresolved"},
      "controls":"Independent raw-orbit, moment, coefficient-hash and Newton h22 replay; hostile omitted-tail and full-error-globalization checks.",
      "source_routing":"SC-ACT-01/02 ASSERTS; SC-META-53 UNCERTAIN; LT-GR6b/LT-SM8 NEEDS. No source or ledger row moves.",
      "claim_ceiling":"The complete cumulative q<=15 signed prefix exceeds 1e-21. Farther shells may cancel; no full-error lower bound, K215 impossibility, pointwise sign, physics, canon, paper, or public-posture change."
    }

if __name__ == "__main__":
    p=argparse.ArgumentParser(); p.add_argument('--write',action='store_true'); a=p.parse_args(); r=generate()
    if a.write: OUT.write_text(json.dumps(r,indent=2)+"\n")
    print('[PASS] K247 cumulative q15 lower',r['certificate']['complete_lower']['decimal'])
