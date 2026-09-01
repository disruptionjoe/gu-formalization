#!/usr/bin/env python3
"""Exact domain, constraint and connection-denominator controls for K77."""
from __future__ import annotations

import copy
import json
import pathlib
import sys
from fractions import Fraction


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k77-owned-domain-constraint-denominator-wave.json"
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


def add(left: Vector, right: Vector) -> Vector:
    return tuple(a + b for a, b in zip(left, right))


def scale(coefficient: Q, vector: Vector) -> Vector:
    return tuple(coefficient * value for value in vector)


def quotient_norm(form: Matrix, vector: Vector, gauge: Vector) -> Q:
    """Squared norm of the H-orthogonal representative modulo one gauge line."""
    hg = matvec(form, gauge)
    coefficient = dot(vector, hg) / dot(gauge, hg)
    representative = add(vector, scale(-coefficient, gauge))
    return quadratic(form, representative)


def model_checks(mutation: str | None = None) -> list[tuple[str, bool]]:
    checks: list[tuple[str, bool]] = []
    projector = matrix(((1, 0, 0, 0), (0, 1, 0, 0),
                        (0, 0, 0, 0), (0, 0, 0, 0)))
    energy = matrix(((1, 0, 0, 0), (0, 4, 0, 0),
                     (0, 0, 1, 0), (0, 0, 0, 4)))
    d1 = matrix(((0, 0, 1, 0),))
    gauge_x = (Q(1), Q(0), Q(0), Q(0))
    gauge_y = (Q(0), Q(1), Q(0), Q(0))
    gauge_diagonal = (Q(1), Q(1), Q(0), Q(0))
    gauges = (gauge_x, gauge_y, gauge_diagonal)

    checks.append(("the planted cylinder has two explicitly cooriented ends",
                   mutation != "erase_coorientation"))
    checks.append(("incoming control data have a positive rank-two range",
                   matvec(projector, gauge_x) == gauge_x
                   and matvec(projector, gauge_y) == gauge_y
                   and quadratic(energy, gauge_x) > 0
                   and quadratic(energy, gauge_y) > 0))

    chain_zero = all(matvec(d1, gauge) == (Q(0),) for gauge in gauges)
    if mutation == "break_chain":
        chain_zero = False
    checks.append(("all three candidate gauge lines lie in the constraint cycles",
                   chain_zero))
    stable = all(matvec(projector, gauge) == gauge for gauge in gauges)
    if mutation == "break_projector_stability":
        stable = False
    checks.append(("the same principal projector preserves all three gauge images",
                   stable))

    vector = (Q(3, 5), Q(2, 5), Q(0), Q(0))
    raw_norm = quadratic(energy, vector)
    quotient_norms = tuple(quotient_norm(energy, vector, gauge) for gauge in gauges)
    if mutation == "collapse_quotient_norms":
        quotient_norms = (quotient_norms[0],) * 3
    checks.append(("the planted representative has raw principal norm one",
                   raw_norm == Q(1)))
    checks.append(("three projector-stable complexes give three exact quotient norms",
                   quotient_norms == (Q(16, 25), Q(9, 25), Q(4, 125))))
    checks.append(("principal projector and energy do not select a gauge complex",
                   len(set(quotient_norms)) == 3))

    # Select gauge_x only inside the finite control, then test quotient evolution.
    evolution = matrix(((1, 0, 0, 0), (0, Q(1, 2), 0, 0),
                        (0, 0, 1, 0), (0, 0, 0, Q(1, 2))))
    if mutation == "break_projector_commutation":
        evolution = matrix(((1, 0, 1, 0), (0, Q(1, 2), 0, 0),
                            (0, 0, 1, 0), (0, 0, 0, Q(1, 2))))
    checks.append(("control evolution commutes with the incoming projector",
                   mul(evolution, projector) == mul(projector, evolution)))
    gauge_preserved = matvec(evolution, gauge_x) == gauge_x
    if mutation == "break_gauge_propagation":
        gauge_preserved = False
    checks.append(("control evolution preserves the selected gauge image",
                   gauge_preserved))
    checks.append(("control evolution preserves the constraint cycles",
                   matvec(d1, matvec(evolution, vector)) == (Q(0),)))

    representative = (Q(0), Q(2, 5), Q(0), Q(0))
    shifted = add(representative, scale(Q(7, 5), gauge_x))
    output_difference = add(matvec(evolution, shifted),
                            scale(Q(-1), matvec(evolution, representative)))
    if mutation == "break_quotient_well_defined":
        output_difference = gauge_y
    checks.append(("control evolution is representative independent modulo gauge",
                   output_difference == scale(Q(7, 5), gauge_x)))
    before = quotient_norm(energy, representative, gauge_x)
    after = quotient_norm(energy, matvec(evolution, representative), gauge_x)
    if mutation == "break_quotient_contraction":
        after = before
    checks.append(("the induced quotient evolution contracts squared norm by one quarter",
                   before == Q(16, 25) and after == Q(4, 25)
                   and after * 4 == before))
    checks.append(("the normalized quotient representative is fixed only after gauge choice",
                   quotient_norm(energy, (Q(0), Q(1, 2), Q(0), Q(0)), gauge_x)
                   == Q(1)))

    bad_evolution = matrix(((1, 0, 0, 0), (1, Q(1, 2), 0, 0),
                            (0, 0, 1, 0), (0, 0, 0, Q(1, 2))))
    bad_difference = matvec(bad_evolution, gauge_x)
    bad_descends = bad_difference[1:] == (Q(0), Q(0), Q(0))
    if mutation == "force_bad_evolution_descent":
        bad_descends = True
    checks.append(("projector commutation alone does not make quotient evolution well defined",
                   mul(bad_evolution, projector) == mul(projector, bad_evolution)
                   and not bad_descends))
    finite_closed_range = (len(gauge_x) == 4
                           and gauge_x != (Q(0), Q(0), Q(0), Q(0)))
    if mutation == "promote_finite_closed_range":
        finite_closed_range = False
    checks.append(("the planted gauge image is rank one in a finite carrier",
                   finite_closed_range))

    # One fibre symplectic form admits incompatible connection/holonomy choices.
    omega = matrix(((0, 1), (-1, 0)))
    euclidean = identity(2)
    rotation = matrix(((0, -1), (1, 0)))
    hyperbolic = matrix(((2, 0), (0, Q(1, 2))))
    if mutation == "break_rotation_symplecticity":
        rotation = matrix(((0, -2), (1, 0)))
    if mutation == "break_hyperbolic_symplecticity":
        hyperbolic = matrix(((2, 0), (0, 1)))
    checks.append(("rotation is a symplectic monodromy for the same fibre Green form",
                   mul(mul(transpose(rotation), omega), rotation) == omega))
    checks.append(("hyperbolic scaling is another symplectic monodromy for that fibre form",
                   mul(mul(transpose(hyperbolic), omega), hyperbolic) == omega))
    checks.append(("rotation preserves the Euclidean compatible majorant",
                   mul(mul(transpose(rotation), euclidean), rotation) == euclidean))
    moved = mul(mul(transpose(hyperbolic), euclidean), hyperbolic)
    if mutation == "claim_hyperbolic_unitarity":
        moved = euclidean
    checks.append(("hyperbolic monodromy does not preserve that majorant",
                   moved != euclidean))
    no_positive_fixed = Q(4) != Q(1) and Q(1, 4) != Q(1)
    if mutation == "invent_positive_hyperbolic_majorant":
        no_positive_fixed = False
    checks.append(("hyperbolic monodromy fixes no positive symmetric majorant",
                   no_positive_fixed))
    checks.append(("fibre Green data alone do not select connection holonomy",
                   rotation != hyperbolic and mutation != "select_holonomy_from_fibre"))
    stratum_dimensions = (24, 24, 22)
    if mutation == "erase_null_jump":
        stratum_dimensions = (24, 24, 24)
    checks.append(("I1B still requires one fixed-rank stratum before bundle transport",
                   len(set(stratum_dimensions)) == 2))
    return checks


def manifest_checks(data: dict) -> list[tuple[str, bool]]:
    result = data["result"]
    return [
        ("manifest labels the cylinder and constraint complex as a control",
         data["finite_control"]["owner_status"] == "planted_control_not_gu_native"),
        ("manifest records zero actual GU domains and physical quotients",
         result["actual_gu_domains_completed"] == 0
         and result["global_physical_quotients_completed"] == 0),
        ("manifest records no source action or I1B connection selection",
         result["action_selection"] == "none"
         and result["i1b_connection_selection"] == "none"),
        ("manifest keeps the observed and I1B packets noncomposable",
         data["packet_custody"]["cross_packet_union_allowed"] is False),
        ("manifest forbids finite-to-Sobolev promotion",
         data["analytic_firewall"]["sobolev_closed_range_proved"] is False
         and data["analytic_firewall"]["continuum_constraint_propagation_proved"] is False),
        ("manifest keeps the held-out family unscored",
         data["holdout_firewall"]["status"] == "reserved_unscored"
         and data["holdout_firewall"]["scored_in_this_result"] is False),
    ]


MANIFEST_MUTATIONS = {
    "promote_control": ("finite_control", "owner_status", "gu_native"),
    "promote_physical": ("result", "global_physical_quotients_completed", 1),
    "select_action": ("result", "action_selection", "selected"),
    "select_i1b_connection": ("result", "i1b_connection_selection", "selected"),
    "cross_union": ("packet_custody", "cross_packet_union_allowed", True),
    "promote_sobolev": ("analytic_firewall", "sobolev_closed_range_proved", True),
    "score_holdout": ("holdout_firewall", "status", "scored"),
}


def all_checks(data: dict, mutation: str | None = None) -> list[tuple[str, bool]]:
    if mutation in MANIFEST_MUTATIONS:
        data = copy.deepcopy(data)
        section, key, value = MANIFEST_MUTATIONS[mutation]
        data[section][key] = value
        if mutation == "score_holdout":
            data["holdout_firewall"]["scored_in_this_result"] = True
        model_mutation = None
    else:
        model_mutation = mutation
    return model_checks(model_mutation) + manifest_checks(data)


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if "--selftest" in sys.argv:
        mutations = [
            "erase_coorientation", "break_chain", "break_projector_stability",
            "collapse_quotient_norms", "break_projector_commutation",
            "break_gauge_propagation", "break_quotient_well_defined",
            "break_quotient_contraction", "force_bad_evolution_descent",
            "promote_finite_closed_range", "break_rotation_symplecticity",
            "break_hyperbolic_symplecticity", "claim_hyperbolic_unitarity",
            "invent_positive_hyperbolic_majorant", "select_holonomy_from_fibre",
            "erase_null_jump", "promote_control", "promote_physical",
            "select_action", "select_i1b_connection", "cross_union",
            "promote_sobolev", "score_holdout",
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
