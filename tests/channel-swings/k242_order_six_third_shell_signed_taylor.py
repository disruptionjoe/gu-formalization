#!/usr/bin/env python3
"""K242: exact signed degree-nine Taylor integral and rigorous shell tail."""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import comb, factorial

from flint import arb, ctx, fmpq, fmpq_mpoly_ctx

from k225_order_six_diagonal_cancellation import K185, ROOT, terms
from k230_order_six_permutation_projection import (
    OUT as K230, orbit_key, row_masks,
)

OUT = ROOT / "lab/process/k242-order-six-third-shell-signed-taylor.json"
K218 = ROOT / "lab/process/k218-order-six-exact-angular-elimination.json"
K241 = ROOT / "lab/process/k241-order-six-quartic-coefficient-atlas.json"
ORDER = 9
TAIL_START = ORDER + 1
HEADROOM = fmpq(17933, 10**26)
PI_LOWER = fmpq(31, 10)
POLYNOMIAL_LOWER = fmpq(9935, 10**31)
POLYNOMIAL_UPPER = fmpq(9937, 10**31)
ctx.prec = 256


def orbit_groups(items):
    groups = defaultdict(int)
    for weight, masks in items:
        groups[orbit_key(row_masks(masks))] += weight
    return {rows: weight for rows, weight in groups.items() if weight}


def taylor_polynomials(groups, order: int = ORDER):
    """Signed homogeneous Taylor polynomials at c=(1,...,1)."""
    ring = fmpq_mpoly_ctx.get([f"x{i}" for i in range(8)])
    variables = ring.gens()
    total = [ring.constant(0) for _ in range(order + 1)]
    for rows, weight in groups.items():
        pieces = [ring.constant(1)] + [ring.constant(0) for _ in range(order)]
        for row in rows:
            base = 256 + row.bit_count()
            linear = sum((variables[j] for j in range(8) if row & (1 << j)),
                         ring.constant(0))
            divided = [pieces[0] / base]
            for degree in range(1, order + 1):
                divided.append((pieces[degree] - linear * divided[degree-1]) / base)
            pieces = divided
        for degree, piece in enumerate(pieces):
            total[degree] += weight * piece
    return total


def add(left, right):
    return [(left[i] if i < len(left) else fmpq(0))
            + (right[i] if i < len(right) else fmpq(0))
            for i in range(max(len(left), len(right)))]


def multiply(left, right):
    out = [fmpq(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i+j] += x*y
    return out


def moment_polynomials(q: int, order: int = ORDER):
    """mu_e=int cosh(t)(cosh(t)-1)^e dt as a+b*log(q)."""
    qf = fmpq(q)
    sinh_t = (qf*qf - 1) / (2*qf)
    cosh_t = (qf*qf + 1) / (2*qf)
    powers = [[fmpq(0), fmpq(1)], [sinh_t]]
    for n in range(2, order + 2):
        boundary = [sinh_t * cosh_t**(n-1) / n]
        recurrence = [(n-1) * value / n for value in powers[n-2]]
        powers.append(add(boundary, recurrence))
    moments = []
    for exponent in range(order + 1):
        value = [fmpq(0)]
        for k in range(exponent + 1):
            coefficient = fmpq((-1)**(exponent-k) * comb(exponent, k))
            value = add(value, [coefficient*x for x in powers[k+1]])
        moments.append(value)
    return moments


def integrate_polynomial(polynomial, moments):
    out = [fmpq(0)] * 9
    cache = {}
    for exponents, coefficient in polynomial.terms():
        if exponents not in cache:
            value = [fmpq(1)]
            for exponent in exponents:
                value = multiply(value, moments[exponent])
            cache[exponents] = value
        for power, value in enumerate(cache[exponents]):
            out[power] += coefficient * value
    return out


def coefficient_hash(polynomial) -> str:
    payload = ";".join(
        f"{','.join(map(str, exponents))}:{coefficient}"
        for exponents, coefficient in polynomial.terms())
    return sha256(payload.encode()).hexdigest()


def log_polynomial_hash(coefficients) -> str:
    return sha256(";".join(map(str, coefficients)).encode()).hexdigest()


def evaluate_log_polynomial(coefficients, q: int):
    log_q = arb(q).log()
    return sum((arb(str(value)) * log_q**power
                for power, value in enumerate(coefficients)), arb(0))


def complete_homogeneous_ten(ratios):
    coefficients = [fmpq(1)] + [fmpq(0)] * TAIL_START
    for ratio in ratios:
        updated = [fmpq(0)] * (TAIL_START + 1)
        power = fmpq(1)
        for k in range(TAIL_START + 1):
            for degree in range(TAIL_START + 1 - k):
                updated[k+degree] += coefficients[degree] * power
            power *= ratio
        coefficients = updated
    return coefficients[TAIL_START]


def tail_majorant(groups):
    """Uniform all-degree >=10 orbit bound on [1,5]^8."""
    total = fmpq(0)
    for rows, weight in groups.items():
        base_value = fmpq(1)
        ratios = []
        for row in rows:
            base = 256 + row.bit_count()
            base_value /= base
            ratios.append(fmpq(4 * row.bit_count(), base))
        h10 = complete_homogeneous_ten(ratios)
        ratio_ceiling = max(ratios) * fmpq(TAIL_START + 14, TAIL_START + 1)
        assert ratio_ceiling < 1
        total += abs(weight) * base_value * h10 / (1-ratio_ceiling)
    return total


def generate():
    items = list(terms(json.loads(K185.read_text())))
    assert len(items) == 1864
    groups = orbit_groups(items)
    assert len(groups) == 307
    polynomials = taylor_polynomials(groups)
    moments = {q: moment_polynomials(q) for q in (4, 5)}
    by_degree = {q: [] for q in (4, 5)}
    for degree, polynomial in enumerate(polynomials):
        for q in (4, 5):
            by_degree[q].append(integrate_polynomial(polynomial, moments[q]))
    # K231's fourth-order onset appears after the symmetric cube functional,
    # even though one orbit representative is not itself S6 invariant.
    assert all(all(value == 0 for value in by_degree[q][degree])
               for q in (4, 5) for degree in range(4))
    cube_total = {q: [sum((by_degree[q][degree][power]
                           for degree in range(ORDER + 1)), fmpq(0))
                       for power in range(9)] for q in (4, 5)}
    cube_values = {q: evaluate_log_polynomial(cube_total[q], q) for q in (4, 5)}
    normalization = arb(2**8 * 256**6) / factorial(5) / arb.pi()**8
    polynomial_shell = normalization * (cube_values[5] - cube_values[4])
    assert polynomial_shell > arb(str(POLYNOMIAL_LOWER))
    assert polynomial_shell < arb(str(POLYNOMIAL_UPPER))

    shell_measure = fmpq(12, 5)**8 - fmpq(15, 8)**8
    tail_core = tail_majorant(groups)
    tail_upper = (fmpq(2**8 * 256**6, factorial(5)) / PI_LOWER**8
                  * shell_measure * tail_core)
    complete_upper = POLYNOMIAL_UPPER + tail_upper
    assert complete_upper < HEADROOM

    prior = json.loads(K230.read_text())
    compact = ";".join(
        ",".join(map(str, rows)) + ":" + str(weight)
        for rows, weight in sorted(groups.items()))
    assert sha256(compact.encode()).hexdigest() == prior["orbit_coefficient_manifest_sha256"]
    degree_records = []
    for degree, polynomial in enumerate(polynomials):
        shell_degree = normalization * (
            evaluate_log_polynomial(by_degree[5][degree], 5)
            - evaluate_log_polynomial(by_degree[4][degree], 4))
        degree_records.append({
            "degree": degree,
            "monomials": len(list(polynomial.terms())),
            "coefficient_sha256": coefficient_hash(polynomial),
            "integrated_shell_arb": str(shell_degree),
        })
    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "input_sha256": {path.stem.split("-")[0]: sha256(path.read_bytes()).hexdigest()
                         for path in (K185, K218, K230, K241)},
        "object": "Complete original K185/K218 signed rational-cosh core on [0,log(5)]^8 minus [0,log(4)]^8",
        "scope": "Internal order-six finite-prefix integration algebra; not a source-selected action, physical state, quotient, spectrum or observable",
        "expansion": {
            "anchor_c": [1] * 8,
            "total_degree_inclusive": ORDER,
            "raw_signed_terms": len(items),
            "retained_s6_orbits": len(groups),
            "orbit_manifest_sha256": prior["orbit_coefficient_manifest_sha256"],
            "degrees": degree_records,
            "cube_integrated_log_polynomial_sha256": {
                str(q): log_polynomial_hash(cube_total[q]) for q in (4, 5)},
            "theorem": "Expand every retained K230 denominator orbit at c=(1,...,1) in x_j=c_j-1 through total degree nine. On each symmetric cube its orbit representative has the same integral as its S6 average. The K218 measure gives mu_e(q)=int_0^log(q) cosh(t)(cosh(t)-1)^e dt, obtained exactly as a rational affine polynomial in log(q) from the standard cosh-power recurrence. Product moments therefore integrate every signed multivariate coefficient exactly before any absolute value.",
        },
        "signed_polynomial_shell": {
            "arb_256_bit": str(polynomial_shell),
            "strict_rational_lower": str(POLYNOMIAL_LOWER),
            "strict_rational_upper": str(POLYNOMIAL_UPPER),
        },
        "all_higher_degree_tail": {
            "starts_at_total_degree": TAIL_START,
            "exact_core_majorant": str(tail_core),
            "exact_shell_measure": str(shell_measure),
            "pi_lower": str(PI_LOWER),
            "normalized_upper": str(tail_upper),
            "normalized_upper_decimal": f"{float(Q(str(tail_upper))):.12e}",
            "proof": "For one orbit at x_j in [0,4], write r_i=(sum_j m_ij x_j)/(256+row_popcount_i). Its reciprocal product has alternating homogeneous coefficients q0*h_n(r). Monotonicity bounds h_10 at x=(4,...,4). For n>=10, h_(n+1)/h_n is at most r_max*(n+14)/(n+1), hence at most r_max*24/11<1. The geometric continuation h_10/(1-r_max*24/11), summed with absolute retained-orbit coefficients, covers every degree ten and higher. Multiplication by the exact shell measure and pi>31/10 completes the integral bound.",
        },
        "complete_third_shell": {
            "headroom": str(HEADROOM),
            "absolute_upper": str(complete_upper),
            "absolute_upper_decimal": f"{float(Q(str(complete_upper))):.12e}",
            "fraction_of_headroom": f"{float(Q(str(complete_upper/HEADROOM))):.12e}",
            "result": "passes_budget",
            "interpretation": "The exact signed degree-zero-through-nine polynomial plus the absolute all-higher-degree tail encloses the complete K218 third shell. K241's quartic is included in degree four and is not added again.",
        },
        "controls": "The independent probe reconstructs the degree-nine cube integrals from all 1,276 raw allocation functions without K230 orbit projection, replays h_10 by Newton power sums rather than factor convolution, and rejects omitted degree ten, a sign mutation and a wrong measure normalization.",
        "source_routing": "SC-ACT-01/02 ASSERTS; SC-META-53 UNCERTAIN; LT-GR6b/LT-SM8 NEEDS. No source or physics-ledger row moves.",
        "claim_ceiling": "Rigorous complete third-shell signed integral enclosure below K224's residual allocation only. No complete K215 finite prefix, separate quotient/coalescent/common-reference boundary composition, source action/state/domain, physics verdict, canon, paper or public-posture change.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    result = generate()
    if args.write:
        OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("[PASS] K242 exact signed degree-nine shell", result["signed_polynomial_shell"]["arb_256_bit"])
    print("[PASS] K242 complete third-shell upper", result["complete_third_shell"]["absolute_upper_decimal"], result["complete_third_shell"]["fraction_of_headroom"])
