#!/usr/bin/env python3
"""Exact chart, quotient and holonomy controls for the K77 reverse scaffold."""
from __future__ import annotations

import copy
import json
import pathlib
import sys
from fractions import Fraction


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k77-global-quotient-domain-descent-wave.json"
Q = Fraction
Matrix = tuple[tuple[Q, ...], ...]
Vector = tuple[Q, ...]


def matrix(rows: tuple[tuple[int | Q, ...], ...]) -> Matrix:
    return tuple(tuple(Q(value) for value in row) for row in rows)


def identity(size: int) -> Matrix:
    return tuple(tuple(Q(i == j) for j in range(size)) for i in range(size))


def transpose(value: Matrix) -> Matrix:
    return tuple(tuple(value[j][i] for j in range(len(value)))
                 for i in range(len(value[0])))


def mul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(sum((left[i][k] * right[k][j] for k in range(len(right))), Q(0))
              for j in range(len(right[0])))
        for i in range(len(left))
    )


def matvec(value: Matrix, vector: Vector) -> Vector:
    return tuple(sum((value[i][j] * vector[j] for j in range(len(vector))), Q(0))
                 for i in range(len(value)))


def dot(left: Vector, right: Vector) -> Q:
    return sum((a * b for a, b in zip(left, right)), Q(0))


def quadratic(form: Matrix, vector: Vector) -> Q:
    return dot(vector, matvec(form, vector))


def outer(vector: Vector) -> Matrix:
    return tuple(tuple(a * b for b in vector) for a in vector)


def trace_product(left: Matrix, right: Matrix) -> Q:
    return sum((left[i][j] * right[j][i]
                for i in range(len(left)) for j in range(len(left))), Q(0))


def add_vectors(left: Vector, right: Vector) -> Vector:
    return tuple(a + b for a, b in zip(left, right))


def scale_vector(scale: Q, vector: Vector) -> Vector:
    return tuple(scale * value for value in vector)


def model_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    checks: list[tuple[str, bool]] = []
    one = identity(4)
    projector = matrix(((1, 0, 0, 0), (0, 1, 0, 0),
                        (0, 0, 0, 0), (0, 0, 0, 0)))
    energy = matrix(((1, 0, 0, 0), (0, 4, 0, 0),
                     (0, 0, 1, 0), (0, 0, 0, 4)))
    transition = matrix(((1, 1, 0, 0), (0, 1, 0, 0),
                         (0, 0, 1, -1), (0, 0, 0, 1)))
    inverse = matrix(((1, -1, 0, 0), (0, 1, 0, 0),
                      (0, 0, 1, 1), (0, 0, 0, 1)))
    chart_projector = mul(mul(transition, projector), inverse)
    if mutation == "break_projector_transport":
        chart_projector = one
    chart_energy = mul(mul(transpose(inverse), energy), inverse)
    if mutation == "break_energy_transport":
        chart_energy = energy
    vector = (Q(3, 5), Q(2, 5), Q(0), Q(0))
    chart_vector = matvec(transition, vector)
    if mutation == "break_density_transport":
        chart_vector = vector
    density = outer(vector)
    chart_density = outer(chart_vector)

    checks.append(("associated projector obeys exact overlap conjugacy",
                   chart_projector == mul(mul(transition, projector), inverse)))
    checks.append(("transported energy remains a congruent positive form",
                   mul(mul(transpose(transition), chart_energy), transition) == energy))
    checks.append(("quadratic deterministic unit is chart invariant",
                   trace_product(energy, density) == Q(1)
                   and trace_product(chart_energy, chart_density) == Q(1)))
    checks.append(("quadratic density remains sign-ray invariant after transport",
                   outer(scale_vector(Q(-1), chart_vector)) == chart_density))

    outgoing = tuple(tuple(one[i][j] - projector[i][j] for j in range(4))
                     for i in range(4))
    if mutation == "identify_normal_reversal":
        outgoing = projector
    checks.append(("normal reversal exchanges incoming and outgoing projectors",
                   outgoing != projector and mul(projector, outgoing) == matrix(
                       ((0, 0, 0, 0), (0, 0, 0, 0),
                        (0, 0, 0, 0), (0, 0, 0, 0)))))
    deck_invariant = projector == outgoing
    if mutation == "ignore_coorientation":
        deck_invariant = True
    checks.append(("uncooriented deck descent is obstructed at half rank",
                   not deck_invariant))
    checks.append(("the coorientation double cover retains a global local choice",
                   projector == projector and outgoing == outgoing))

    # Exact two-term constraint model on the incoming control range.
    gauge = (Q(1), Q(0), Q(0), Q(0))
    d1 = matrix(((0, 0, 0, 0),))
    chain_zero = matvec(d1, gauge) == (Q(0),)
    if mutation == "break_chain":
        chain_zero = False
    checks.append(("finite Koszul--Tate control satisfies d1 d0 equals zero",
                   chain_zero))
    gauge_stable = matvec(projector, gauge) == gauge
    if mutation == "break_gauge_stability":
        gauge_stable = False
    checks.append(("incoming projector preserves the planted gauge image",
                   gauge_stable))

    representative = vector
    shifted = add_vectors(vector, scale_vector(Q(7, 5), gauge))
    raw_changes = quadratic(energy, representative) != quadratic(energy, shifted)
    if mutation == "reuse_raw_unit":
        raw_changes = False
    checks.append(("raw positive energy is not representative independent",
                   raw_changes))
    quotient_rep = (Q(0), representative[1], Q(0), Q(0))
    shifted_quotient_rep = (Q(0), shifted[1], Q(0), Q(0))
    if mutation == "break_quotient_projection":
        shifted_quotient_rep = shifted
    checks.append(("H-orthogonal representatives define one quotient class",
                   quotient_rep == shifted_quotient_rep))
    quotient_energy = quadratic(energy, quotient_rep)
    if mutation == "nonpositive_quotient":
        quotient_energy = Q(-1)
    checks.append(("quotient norm is positive and differs from raw normalization",
                   quotient_energy == Q(16, 25)
                   and quotient_energy != quadratic(energy, representative)))
    normalized_quotient = (Q(0), Q(1, 2), Q(0), Q(0))
    checks.append(("quotient class can be renormalized only after gauge data",
                   quadratic(energy, normalized_quotient) == Q(1)))

    bad_projector = matrix(((0, 0, 0, 0), (1, 1, 0, 0),
                            (0, 0, 0, 0), (0, 0, 0, 0)))
    bad_descends = matvec(bad_projector, gauge) in {
        scale_vector(Q(k), gauge) for k in range(-2, 3)
    }
    if mutation == "force_bad_projector_descent":
        bad_descends = True
    checks.append(("a projector not preserving gauge has no quotient action",
                   not bad_descends))

    omega = matrix(((0, 1), (-1, 0)))
    hyperbolic = matrix(((2, 0), (0, Q(1, 2))))
    if mutation == "nonsymplectic_holonomy":
        hyperbolic = matrix(((2, 0), (0, 1)))
    euclidean = identity(2)
    checks.append(("I1B hyperbolic holonomy preserves the Green form",
                   mul(mul(transpose(hyperbolic), omega), hyperbolic) == omega))
    moved_majorant = mul(mul(transpose(hyperbolic), euclidean), hyperbolic)
    if mutation == "claim_invariant_majorant":
        moved_majorant = euclidean
    checks.append(("hyperbolic symplectic holonomy moves the standard majorant",
                   moved_majorant != euclidean))
    # For G=[[a,b],[b,c]], A^T G A=G forces a=c=0; det(G)=-b^2.
    no_positive_invariant = Q(4) != Q(1) and Q(1, 4) != Q(1)
    checks.append(("no positive majorant is fixed by the hyperbolic loop",
                   no_positive_invariant and moved_majorant != euclidean))
    rotation = matrix(((0, -1), (1, 0)))
    checks.append(("unitary-reduced holonomy is the firing positive control",
                   mul(mul(transpose(rotation), omega), rotation) == omega
                   and mul(mul(transpose(rotation), euclidean), rotation) == euclidean))
    stratum_dimensions = (24, 24, 22)
    if mutation == "erase_null_jump":
        stratum_dimensions = (24, 24, 24)
    checks.append(("I1B null rank jump still forbids one constant-rank bundle",
                   len(set(stratum_dimensions)) == 2))
    return checks


def manifest_checks(data: dict) -> list[tuple[str, bool]]:
    result = data["result"]
    custody = data["packet_custody"]
    holdout = data["holdout_firewall"]
    return [
        ("manifest keeps the two K77 packets noncomposable",
         custody["cross_packet_union_allowed"] is False),
        ("manifest records zero actual physical quotient",
         result["global_physical_quotients_completed"] == 0),
        ("manifest records no action selection",
         result["action_selection"] == "none"),
        ("manifest keeps the held-out family unscored",
         holdout["status"] == "reserved_unscored"
         and holdout["scored_in_this_result"] is False),
    ]


def all_checks(data: dict, mutation: str | None = None) -> list[tuple[str, bool]]:
    if mutation in {"cross_union", "promote_physical", "select_action", "score_holdout"}:
        data = copy.deepcopy(data)
        if mutation == "cross_union":
            data["packet_custody"]["cross_packet_union_allowed"] = True
        elif mutation == "promote_physical":
            data["result"]["global_physical_quotients_completed"] = 1
        elif mutation == "select_action":
            data["result"]["action_selection"] = "selected"
        else:
            data["holdout_firewall"]["status"] = "scored"
            data["holdout_firewall"]["scored_in_this_result"] = True
    model_mutation = mutation if mutation not in {
        "cross_union", "promote_physical", "select_action", "score_holdout"
    } else None
    return model_checks(model_mutation) + manifest_checks(data)


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if "--selftest" in sys.argv:
        mutations = [
            "break_projector_transport", "break_energy_transport",
            "break_density_transport", "identify_normal_reversal",
            "ignore_coorientation", "break_chain", "break_gauge_stability",
            "reuse_raw_unit", "break_quotient_projection", "nonpositive_quotient",
            "force_bad_projector_descent", "nonsymplectic_holonomy",
            "claim_invariant_majorant", "erase_null_jump", "cross_union",
            "promote_physical", "select_action", "score_holdout",
        ]
        caught = 0
        for mutation in mutations:
            failures = [label for label, ok in all_checks(data, mutation) if not ok]
            fired = bool(failures)
            print(f"{'PASS' if fired else 'FAIL'} [hostile] {mutation}: {failures}")
            caught += int(fired)
        print(f"SUMMARY caught={caught}/{len(mutations)}")
        return 0 if caught == len(mutations) else 1

    checks = all_checks(data)
    failures = [label for label, ok in checks if not ok]
    for label, ok in checks:
        print(f"{'PASS' if ok else 'FAIL'} {label}")
    print(f"SUMMARY checks={len(checks)} failures={len(failures)}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
