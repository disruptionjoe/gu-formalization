#!/usr/bin/env python3
"""Independent raw-allocation and Newton-tail replay for K242."""
from __future__ import annotations

from collections import defaultdict
import json
from math import factorial

from flint import fmpq, fmpq_mpoly_ctx

from k225_order_six_diagonal_cancellation import K185, terms
from k242_order_six_third_shell_signed_taylor import (
    HEADROOM, ORDER, OUT, PI_LOWER, POLYNOMIAL_UPPER, TAIL_START,
    coefficient_hash, integrate_polynomial, log_polynomial_hash,
    moment_polynomials, orbit_groups, row_masks,
)


def raw_polynomials(items):
    """Aggregate original allocation functions, without S6 orbit projection."""
    allocations = defaultdict(int)
    for weight, masks in items:
        allocations[row_masks(masks)] += weight
    allocations = {rows: weight for rows, weight in allocations.items() if weight}
    assert len(allocations) == 1276
    ring = fmpq_mpoly_ctx.get([f"x{i}" for i in range(8)])
    variables = ring.gens()
    total = [ring.constant(0) for _ in range(ORDER + 1)]
    for rows, weight in allocations.items():
        pieces = [ring.constant(1)] + [ring.constant(0) for _ in range(ORDER)]
        for row in rows:
            base = 256 + row.bit_count()
            linear = sum((variables[j] for j in range(8) if row & (1 << j)),
                         ring.constant(0))
            divided = [pieces[0] / base]
            for degree in range(1, ORDER + 1):
                divided.append((pieces[degree] - linear*divided[degree-1]) / base)
            pieces = divided
        for degree, piece in enumerate(pieces):
            total[degree] += weight*piece
    return total


def newton_h10(ratios):
    complete = [fmpq(1)]
    for n in range(1, TAIL_START + 1):
        complete.append(sum((sum((ratio**k for ratio in ratios), fmpq(0))
                             * complete[n-k] for k in range(1, n+1)), fmpq(0))/n)
    return complete[TAIL_START]


def alternate_tail(groups, start: int):
    total = fmpq(0)
    for rows, weight in groups.items():
        base_value = fmpq(1)
        ratios = []
        for row in rows:
            base = 256 + row.bit_count()
            base_value /= base
            ratios.append(fmpq(4*row.bit_count(), base))
        complete = [fmpq(1)]
        for n in range(1, start + 1):
            complete.append(sum((sum((ratio**k for ratio in ratios), fmpq(0))
                                 * complete[n-k] for k in range(1, n+1)), fmpq(0))/n)
        ratio = max(ratios) * fmpq(start + 14, start + 1)
        total += abs(weight)*base_value*complete[start]/(1-ratio)
    return total


def main():
    manifest = json.loads(OUT.read_text())
    items = list(terms(json.loads(K185.read_text())))
    raw = raw_polynomials(items)
    moments = {q: moment_polynomials(q) for q in (4, 5)}
    cube = {q: [fmpq(0)]*9 for q in (4, 5)}
    for degree, polynomial in enumerate(raw):
        for q in (4, 5):
            values = integrate_polynomial(polynomial, moments[q])
            for power, value in enumerate(values):
                cube[q][power] += value
        # Pointwise raw polynomials need not equal the orbit representative;
        # their symmetric-cube moment functionals agree degree by degree.
    for q in (4, 5):
        assert log_polynomial_hash(cube[q]) == manifest["expansion"]["cube_integrated_log_polynomial_sha256"][str(q)]

    groups = orbit_groups(items)
    for rows in list(groups)[:12]:
        ratios = [fmpq(4*row.bit_count(), 256+row.bit_count()) for row in rows]
        assert newton_h10(ratios) > 0
    tail_core = alternate_tail(groups, TAIL_START)
    assert str(tail_core) == manifest["all_higher_degree_tail"]["exact_core_majorant"]
    measure = fmpq(manifest["all_higher_degree_tail"]["exact_shell_measure"])
    scale = fmpq(2**8*256**6, factorial(5))/PI_LOWER**8*measure
    tail = scale*tail_core
    assert str(tail) == manifest["all_higher_degree_tail"]["normalized_upper"]
    assert POLYNOMIAL_UPPER + tail < HEADROOM

    # Hostile controls: stopping the tail at degree nine is not sufficient;
    # neither a raw sign mutation nor uniform-dt moments reproduce the record.
    degree_nine_tail = scale*alternate_tail(groups, ORDER)
    assert degree_nine_tail > HEADROOM
    mutated = raw[4] + next(iter(raw[4].terms()))[1]
    assert coefficient_hash(mutated) != coefficient_hash(raw[4])
    assert moment_polynomials(5)[0] == [fmpq(12, 5)]  # product-cosh measure
    assert moment_polynomials(5)[0] != [fmpq(1)]      # hostile uniform-dt unit
    assert manifest["complete_third_shell"]["result"] == "passes_budget"
    print("[PASS] K242 independent raw allocation integration and Newton tail replay")


if __name__ == "__main__":
    main()
