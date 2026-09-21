#!/usr/bin/env python3
"""Independent reverse-order replay of K272's held-out S6 orbit."""
from __future__ import annotations

from fractions import Fraction as Q
from hashlib import sha256
import json
import sys

from flint import arb, ctx, fmpq, fmpq_mpoly_ctx

from k225_order_six_diagonal_cancellation import ROOT
from k262_order_six_low_through_three_high_multiplicity_integral_probe import (
    K185,
    independent_groups,
    raw_terms,
)
from k265_order_nine_complete_binary_low_high_union_probe import (
    centered_moments_independent,
    center_radius,
    sinh_log,
    tail_independent,
)
from k267_order_nine_exchangeable_axis_middle_collar import BOUNDS, status_specs

sys.set_int_max_str_digits(0)

RECORD = ROOT / "lab/process/k272-k267-s6-invariant-moment-compression-pilot.json"
K230 = ROOT / "lab/process/k230-order-six-permutation-projection.json"
ORDER = 9
FIXED_STATUS = ("high", "high")


def mapping(rep_status, box_status):
    result = [0, 1] + [None] * 6
    for label in ("low", "high", "middle"):
        left = [a for a in range(2, 8) if rep_status[a] == label]
        right = [a for a in range(2, 8) if box_status[a] == label]
        for a, b in zip(left, right):
            result[a] = b
    assert sorted(result) == list(range(8))
    return tuple(result)


def replay_held_out(groups, geometry):
    specs = list(reversed(list(status_specs(FIXED_STATUS, 5))))
    rep_status = list(status_specs(FIXED_STATUS, 5))[0][2]
    ring = fmpq_mpoly_ctx.get([f"v{a}" for a in range(8)])
    variables = ring.gens()
    aggregates = [dict() for _ in range(ORDER + 1)]
    total_tail = Q()
    enumerated_monomials = 0
    permutations = []
    for _, _, status in specs:
        centers = tuple(geometry[name]["center"] for name in status)
        radii = tuple(geometry[name]["radius"] for name in status)
        polynomials = [ring.constant(0) for _ in range(ORDER + 1)]
        for rows, weight in reversed(list(groups.items())):
            pieces = [ring.constant(1)] + [ring.constant(0) for _ in range(ORDER)]
            for row in reversed(rows):
                support = tuple(a for a in range(8) if row & (1 << a))
                base = fmpq(256) + sum(
                    (fmpq(centers[a].numerator, centers[a].denominator) for a in support),
                    fmpq(0),
                )
                linear = sum((variables[a] for a in support), ring.constant(0))
                nxt = []
                for degree in range(ORDER + 1):
                    previous = nxt[degree - 1] if degree else ring.constant(0)
                    nxt.append((pieces[degree] - linear * previous) / base)
                pieces = nxt
            for degree, piece in enumerate(pieces):
                polynomials[degree] += weight * piece
        permutation = mapping(rep_status, status)
        permutations.append(permutation)
        for degree, polynomial in enumerate(polynomials):
            terms = list(reversed(list(polynomial.terms())))
            enumerated_monomials += len(terms)
            for exponents, coefficient in terms:
                pulled = tuple(exponents[permutation[a]] for a in range(8))
                aggregates[degree][pulled] = aggregates[degree].get(pulled, fmpq(0)) + coefficient
        box_tail = sum(
            (Q(abs(weight)) * tail_independent(rows, centers, radii, ORDER + 1)
             for rows, weight in reversed(list(groups.items()))),
            Q(),
        )
        for name in status:
            box_tail *= geometry[name]["measure"]
        total_tail += box_tail
    for degree in range(ORDER + 1):
        aggregates[degree] = {k: v for k, v in aggregates[degree].items() if v}
    moments = tuple(geometry[name]["moments"] for name in rep_status)
    heads = []
    for level in aggregates:
        value = arb(0)
        for exponents, coefficient in reversed(sorted(level.items())):
            term = arb(coefficient)
            for axis in reversed(range(8)):
                term *= moments[axis][exponents[axis]]
            value += term
        heads.append(value)
    payload = [
        [[*(int(e) for e in exponents), str(coefficient)] for exponents, coefficient in sorted(level.items())]
        for level in aggregates
    ]
    digest = sha256(json.dumps(payload, separators=(",", ":")).encode()).hexdigest()
    return heads, total_tail, digest, enumerated_monomials, sum(map(len, aggregates)), permutations


def main():
    ctx.prec = 256
    record = json.loads(RECORD.read_text())
    held = next(layer for layer in record["layers"] if layer["role"] == "held_out")
    source = json.loads(K185.read_text())
    groups = independent_groups(list(raw_terms(source)))
    projection = json.loads(K230.read_text())
    assert len(groups) == projection["retained_orbits"] == 307
    geometry = {}
    for name, bounds in BOUNDS.items():
        center, radius = center_radius(bounds)
        geometry[name] = {
            "center": center,
            "radius": radius,
            "moments": centered_moments_independent(bounds, center, ORDER),
            "measure": sinh_log(bounds[1]) - sinh_log(bounds[0]),
        }
    heads, tail, digest, enum_count, aggregate_count, permutations = replay_held_out(groups, geometry)
    exact = 0
    for value, expected in zip(heads, held["raw_head_by_degree"]):
        assert (value - arb(expected)).contains(0); exact += 1
    assert tail == Q(held["raw_absolute_tail_upper"]); exact += 1
    assert digest == held["aggregate_coefficient_sha256"]; exact += 1
    assert enum_count == held["cost"]["enumerated_moment_monomial_evaluations"]; exact += 1
    assert aggregate_count == held["cost"]["compressed_moment_monomial_evaluations"]; exact += 1
    assert {tuple(p) for p in permutations} == {tuple(p) for p in held["representative_to_box_permutations"]}; exact += 1

    hostile = 0
    assert digest != next(layer for layer in record["layers"] if layer["role"] == "pilot")["aggregate_coefficient_sha256"]; hostile += 1
    assert aggregate_count < enum_count; hostile += 1
    assert held["cost"]["compressed_box_recurrence_updates"] == held["cost"]["enumerated_box_recurrence_updates"]; hostile += 1
    assert held["cost"]["compressed_tail_orbit_evaluations"] == held["cost"]["enumerated_tail_orbit_evaluations"]; hostile += 1
    assert held["cost"]["naive_reynolds_recurrence_updates"] > held["cost"]["compressed_box_recurrence_updates"]; hostile += 1
    assert record["cost_conclusion"]["result"] == "reject_as_total_algebraic_speedup"; hostile += 1
    print(f"[PASS] K272 probe exact {exact}/15 hostile {hostile}/6")


if __name__ == "__main__":
    main()
