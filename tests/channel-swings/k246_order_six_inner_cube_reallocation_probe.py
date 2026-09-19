#!/usr/bin/env python3
"""Independent raw-orbit, moment, Newton-tail, and budget replay for K246."""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import comb, factorial

from flint import fmpq, fmpq_mpoly_ctx

from k230_order_six_permutation_projection_probe import canonical, raw_entries
from k242_order_six_third_shell_signed_taylor import coefficient_hash
from k243_order_six_budget_composition_q6_method_limit import K224, PI_LOWER
from k244_order_six_exact_corner_shell_ladder import exact_corner, sinh_log
from k246_order_six_inner_cube_reallocation import ORDER, OUT, TAIL_START


def independent_groups(items):
    groups = defaultdict(int)
    for weight, masks in items:
        groups[canonical(masks)] += weight
    return {rows: weight for rows, weight in groups.items() if weight}


def independent_polynomials(groups):
    ring = fmpq_mpoly_ctx.get([f"x{i}" for i in range(8)])
    variables = ring.gens()
    total = [ring.constant(0) for _ in range(ORDER + 1)]
    for rows, weight in groups.items():
        pieces = [ring.constant(1)] + [ring.constant(0) for _ in range(ORDER)]
        for row in rows:
            base = 256 + row.bit_count()
            linear = sum(
                (variables[j] for j in range(8) if row & (1 << j)),
                ring.constant(0),
            )
            quotient = [pieces[0] / base]
            for degree in range(1, ORDER + 1):
                quotient.append((pieces[degree] - linear * quotient[degree - 1]) / base)
            pieces = quotient
        for degree, piece in enumerate(pieces):
            total[degree] += weight * piece
    return total


def add(left, right):
    return [
        (left[i] if i < len(left) else fmpq(0))
        + (right[i] if i < len(right) else fmpq(0))
        for i in range(max(len(left), len(right)))
    ]


def multiply(left, right):
    out = [fmpq(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] += x * y
    return out


def independent_moments(q: int):
    qf = fmpq(q)
    sinh_t = (qf * qf - 1) / (2 * qf)
    cosh_t = (qf * qf + 1) / (2 * qf)
    powers = [[fmpq(0), fmpq(1)], [sinh_t]]
    for n in range(2, ORDER + 2):
        powers.append(add(
            [sinh_t * cosh_t ** (n - 1) / n],
            [(n - 1) * value / n for value in powers[n - 2]],
        ))
    moments = []
    for exponent in range(ORDER + 1):
        value = [fmpq(0)]
        for k in range(exponent + 1):
            scale = fmpq((-1) ** (exponent - k) * comb(exponent, k))
            value = add(value, [scale * x for x in powers[k + 1]])
        moments.append(value)
    return moments


def independent_integral(polynomial, moments):
    out = [fmpq(0)] * 9
    for exponents, coefficient in polynomial.terms():
        value = [fmpq(1)]
        for exponent in exponents:
            value = multiply(value, moments[exponent])
        for power, entry in enumerate(value):
            out[power] += coefficient * entry
    return out


def newton_h(ratios: list[fmpq], degree: int) -> fmpq:
    complete = [fmpq(1)]
    for n in range(1, degree + 1):
        complete.append(sum(
            (sum((ratio ** k for ratio in ratios), fmpq(0)) * complete[n - k]
             for k in range(1, n + 1)),
            fmpq(0),
        ) / n)
    return complete[degree]


def independent_tail(groups, q: int) -> fmpq:
    total = fmpq(0)
    for rows, weight in groups.items():
        base = fmpq(1)
        ratios = []
        for row in rows:
            denominator = 256 + row.bit_count()
            base /= denominator
            ratios.append(exact_corner(q) * row.bit_count() / denominator)
        ratio = max(ratios) * fmpq(TAIL_START + 14, TAIL_START + 1)
        total += abs(weight) * base * newton_h(ratios, TAIL_START) / (1 - ratio)
    return total


def row_value(row) -> fmpq:
    return fmpq(row["numerator"], row["denominator"])


def main() -> None:
    manifest = json.loads(OUT.read_text())
    items = list(raw_entries())
    assert len(items) == 1864
    groups = independent_groups(items)
    assert len(groups) == 307
    polynomials = independent_polynomials(groups)
    for degree, polynomial in enumerate(polynomials):
        assert coefficient_hash(polynomial) == manifest["expansion"]["degree_coefficient_sha256"][str(degree)]

    cube_hashes = manifest["expansion"]["cube_integrated_log_polynomial_sha256"]
    for q in (4, 13, 14, 15):
        moments = independent_moments(q)
        coefficients = [fmpq(0)] * 9
        for polynomial in polynomials:
            values = independent_integral(polynomial, moments)
            for power, value in enumerate(values):
                coefficients[power] += value
        assert sha256(";".join(map(str, coefficients)).encode()).hexdigest() == cube_hashes[str(q)]

    for q, row, shell in (
        (4, manifest["signed_inner_cube"], False),
        (14, manifest["shells"]["14"], True),
        (15, manifest["shells"]["15"], True),
    ):
        core = independent_tail(groups, q)
        assert str(core) == row["exact_core_tail_majorant"]
        measure = (sinh_log(q) ** 8 - sinh_log(q - 1) ** 8
                   if shell else sinh_log(q) ** 8)
        assert str(measure) == row["exact_region_measure"]
        tail = fmpq(2**8 * 256**6, factorial(5)) / PI_LOWER**8 * measure * core
        assert tail == row_value(row["normalized_tail_upper"])
        assert row_value(row["complete_upper"]) > fmpq(row["strict_polynomial_upper"])
        assert row_value(row["complete_lower"]) < fmpq(row["strict_polynomial_lower"])

    # A cube is not a shell: substituting the q=3-to-4 measure would silently
    # drop the inner region. Pointwise equality with an S6 average is never used;
    # only the symmetric-cube integral of the independently rebuilt signed sum is.
    cube_measure = fmpq(manifest["signed_inner_cube"]["exact_region_measure"])
    assert cube_measure == sinh_log(4) ** 8
    assert cube_measure != sinh_log(4) ** 8 - sinh_log(3) ** 8

    budget = manifest["exact_route_budget"]
    remaining = row_value(budget["remaining_after_q14"])
    q15_lower = row_value(budget["q15_complete_lower"])
    assert remaining > 0 and q15_lower > remaining
    assert budget["result"] == "q14_certified__q15_exceeds_reallocated_exact_route_budget"

    old_cube = fmpq(json.loads(K224.read_text())["combined_inner_first_second_cube_absolute_upper"])
    full_budget = row_value(budget["full_absolute_budget"])
    spent = full_budget - remaining
    assert spent + old_cube > full_budget
    assert manifest["route_composition"]["k224_charged_on_k246_route"] is False
    print("[PASS] K246 independent raw-orbit, moment, Newton-tail, and reallocation replay")


if __name__ == "__main__":
    main()
