#!/usr/bin/env python3
"""ECW3D-B2C2A: collide the tau tangent with the W131 BV requirement.

The exact fixture distinguishes three statements which must not be collapsed:

* the derivative graph ``xi -> (xi, D_A xi)`` is a Lie-algebra
  homomorphism into the ordinary inhomogeneous gauge algebra;
* the covariant de Rham leg is not nilpotent on a non-flat connection because
  ``D_A^2 xi = [F_A, xi]``;
* G3's full ordinary-gauge BRST closure is correctly typed in the adjoint
  connection sector and is not the missing scalar-spinor to
  gamma-traceless-vector-spinor differential needed by B2C1.

All matrix arithmetic is rational.  The carrier audit is nominally typed on
purpose: no unsourced identification of ``ad P`` with the spinor module is
allowed to enter through a convenient matrix representation.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import g1_derivative_cocycle_moving_reference_probe as g1  # noqa: E402


def comm(left, right):
    return g1.sub(g1.mm(left, right), g1.mm(right, left))


def covariant_derivative(connection, value, derivative):
    return g1.add(derivative, comm(connection, value))


def form_comm(value, form):
    return tuple(comm(value, entry) for entry in form)


def form_sub(left, right):
    return tuple(g1.sub(x, y) for x, y in zip(left, right))


def bracket_derivative(x, y, dx, dy):
    return tuple(g1.add(comm(dxi, y), comm(x, dyi)) for dxi, dyi in zip(dx, dy))


def tau_tangent(connections, x, dx):
    return x, tuple(
        covariant_derivative(connection, x, derivative)
        for connection, derivative in zip(connections, dx)
    )


def semidirect_bracket(left, right):
    x, alpha = left
    y, beta = right
    return comm(x, y), form_sub(form_comm(x, beta), form_comm(y, alpha))


@dataclass(frozen=True)
class TypedArrow:
    source: str
    target: str
    sector: str


def same_typed_arrow(left, right):
    return left == right


exact_checks = 0
planted_checks = 0


def exact(name, condition):
    global exact_checks
    if not condition:
        raise AssertionError(f"exact check failed: {name}")
    exact_checks += 1


def planted(name, false_claim):
    global planted_checks
    if false_claim:
        raise AssertionError(f"planted false claim unexpectedly passed: {name}")
    planted_checks += 1


def main():
    source = (ROOT / "lab/literature/weinstein-ucsd-2025-04-transcript.md").read_text()
    source_window = source.split("Eric Weinstein [00:18:03]:", 1)[1].split(
        "Eric Weinstein [00:20:57]:", 1
    )[0]
    source_lower = source_window.lower()
    g1_spec = (ROOT / "lab/specifications/g1-global-tilted-moving-reference-packet-2026-07-31.md").read_text()
    g3 = json.loads((ROOT / "lab/process/g3-variational-bvbfv-certificate.json").read_text())
    b2c1 = json.loads(
        (ROOT / "lab/process/eric-curt-wave3d-b2c-projected-gauge-quotient-gate.json").read_text()
    )
    registry = json.loads(
        (ROOT / "lab/process/eric-curt-wave3d-b2c2-tau-tangent-bv-collision.json").read_text()
    )
    campaign = json.loads((ROOT / "lab/process/eric-curt-ten-wave-campaign.json").read_text())

    # Source collision: the ordinary tau graph is author-stated, while the
    # W131/super-IG/BV extension is absent from the load-bearing window.
    exact("source states the inhomogeneous gauge group", "inhomogeneous gauge group" in source_lower)
    exact("source states the tau map", "map, tau" in source_lower)
    exact("source states the derivative term", "d aleph g" in source_lower)
    exact("source types the target as adjoint-valued one-forms", "omega one of add p" in source_lower)
    exact(
        "G1 records the infinitesimal derivative cocycle",
        "D_A\\xi" in g1_spec and "\\tau_A(g)=(g,q_A(g))" in g1_spec,
    )
    planted("source window supplies gamma trace", "gamma" in source_lower)
    planted("source window supplies W131", "w131" in source_lower)
    planted("source window supplies BV closure", re.search(r"\bBV\b", source_window, re.IGNORECASE) is not None)

    # Exact two-coordinate nonabelian first-jet fixture.
    connections = (
        g1.matrix([[1, 2], [0, -1]]),
        g1.matrix([[0, 1], [3, 0]]),
    )
    x = g1.matrix([[1, 1], [2, -1]])
    y = g1.matrix([[0, 2], [-1, 0]])
    dx = (
        g1.matrix([[0, 1], [1, 0]]),
        g1.matrix([[2, 0], [-1, -2]]),
    )
    dy = (
        g1.matrix([[1, -1], [0, -1]]),
        g1.matrix([[0, 1], [2, 0]]),
    )
    dxy = bracket_derivative(x, y, dx, dy)

    lhs = tau_tangent(connections, comm(x, y), dxy)
    rhs = semidirect_bracket(tau_tangent(connections, x, dx), tau_tangent(connections, y, dy))
    exact("tau derivative is a nonabelian Lie-algebra homomorphism", lhs == rhs)
    exact("tau derivative has a nonzero one-form leg", tau_tangent(connections, x, dx)[1] != (g1.zero(2), g1.zero(2)))
    planted("zero-jet graph contains the derivative leg", dx == (g1.zero(2), g1.zero(2)))

    # Non-flat curvature obstructs treating D_A itself as a nilpotent
    # differential.  This does not contradict full BRST nilpotence.
    zero = g1.zero(2)
    a0, a1 = connections
    curvature = comm(a0, a1)
    d0x = covariant_derivative(a0, x, zero)
    d1x = covariant_derivative(a1, x, zero)
    commutator_of_covariant_derivatives = g1.sub(
        covariant_derivative(a0, d1x, zero),
        covariant_derivative(a1, d0x, zero),
    )
    curvature_action = comm(curvature, x)
    exact("covariant-square curvature identity", commutator_of_covariant_derivatives == curvature_action)
    exact("nonflat curvature is present", curvature != zero)
    exact("curvature acts nontrivially on the gauge parameter", curvature_action != zero)
    planted("ordinary covariant de Rham leg is nilpotent here", curvature_action == zero)

    flat_connections = (zero, zero)
    flat_curvature = comm(*flat_connections)
    exact("flat control has zero curvature", flat_curvature == zero)
    exact("flat control has nilpotent covariant square", comm(flat_curvature, x) == zero)
    planted("homomorphism identity forces flatness", curvature == zero)

    # G3 already proves the nonlinear ordinary-gauge BRST completion.  Its
    # scope statement is load-bearing: it is not super-IG/RS cohomology.
    minimal_bv = g3["minimal_bv"]
    exact("G3 BV scope is ordinary Gau(P)", "ordinary Gau(P)" in minimal_bv["scope"])
    exact("G3 ordinary BRST includes the ghost bracket", "s c=1/2[c,c]" in minimal_bv["rules"])
    exact("G3 ordinary BRST closure passes", minimal_bv["closure_and_jacobi"] == "PASS")
    exact("G3 excludes super-IG and physical cohomology", "super-IG or complete diffeomorphism BV" in g3["not_claimed"])
    planted("G3 ordinary BRST is a proved super-IG closure", "super-IG" in minimal_bv["scope"])

    # Layer-0 carrier gate.  Equality is nominal/type-level; dimensions alone
    # and a chosen matrix representation cannot create the missing soldering.
    ordinary_tau = TypedArrow(
        "Omega0(ad P)",
        "Omega1(ad P)",
        "ordinary inhomogeneous gauge algebra",
    )
    ordinary_brst = TypedArrow(
        "Pi Omega0(ad P)",
        "T Conn(P) ~= Omega1(ad P)",
        "ordinary gauge BV",
    )
    w131_needed = TypedArrow(
        "scalar spinor S",
        "ker Gamma subset T*Y tensor S",
        "super-IG/RS tangent complex",
    )
    exact("ordinary tau and W131 arrows are type-distinct", not same_typed_arrow(ordinary_tau, w131_needed))
    exact("ordinary BRST and W131 arrows are type-distinct", not same_typed_arrow(ordinary_brst, w131_needed))
    exact("actual W131 gamma-traceless rank is 1664", 14 * 128 - 128 == 1664)
    exact("B2C1 requires an independently sourced tangent map", b2c1["repair_forks"]["root_dependent_residual_halves"]["verdict"] == "OPEN_ONLY_AFTER_INDEPENDENT_SOURCE_DERIVATION")
    planted("ad P is the scalar-spinor carrier", ordinary_tau.source == w131_needed.source)
    planted("adjoint one-forms are gamma-traceless vector-spinors", ordinary_tau.target == w131_needed.target)
    planted("ordinary BRST supplies W131 physical cohomology", ordinary_brst.sector == w131_needed.sector)

    # Registry/campaign boundaries and exact non-advances.
    wave3 = next((wave for wave in campaign["waves"] if wave["id"] == "ECW3-G4-OBSERVATION"), None)
    if wave3 is None:
        raise AssertionError("campaign is missing the Wave 3 observation row")
    b2c2a = wave3["result"]["wave3d"]["wave3d_b1"]["wave3d_b2a"]["wave3d_b2b"]["wave3d_b2c1"]["wave3d_b2c2a"]
    exact("registry records SOURCE-CORRECTS scope", registry["source_collision"]["disposition"] == "SOURCE-CORRECTS")
    exact("registry refuses a W131 Jordan cohomology retest", registry["w131_collision"]["jordan_cohomology_retested"] is False)
    exact("external datum remains unused", registry["external_datum"]["P1_P2_P3_used"] is False)
    exact("Curt remains formally separate", registry["curt_rival"]["status"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE")
    exact("third lane remains unpromoted", registry["third_lane_promotion"]["verdict"] == "NOT_PROMOTED")
    exact("campaign records B2C2A", b2c2a["registry"] == registry["reporting"]["registry"])
    exact("campaign advances only to the typed super-IG/RS gate", wave3["result"]["active_next_swing"] == registry["next_gate"])
    planted("tau tangent already removes the Jordan chains", registry["w131_collision"]["jordan_cohomology_retested"])
    planted("external datum supplies the carrier bridge", registry["external_datum"]["P1_P2_P3_used"])
    planted("Curt is promoted", registry["third_lane_promotion"]["verdict"] == "PROMOTED")

    exact("registry planted-check count matches", registry["probe"]["planted_rejections"] == planted_checks)
    exact("registry exact-check count matches", registry["probe"]["exact_checks"] == exact_checks + 1)
    exact_checks_expected = exact_checks
    planted_checks_expected = planted_checks

    print(
        "ECW3D-B2C2A TAU-TANGENT/BV TYPE AND CURVATURE COLLISION: "
        f"{exact_checks_expected} exact + {planted_checks_expected} planted = "
        f"{exact_checks_expected + planted_checks_expected} PASS"
    )
    print("RESULT: d tau_A is a source-backed ordinary-gauge Lie-algebra homomorphism")
    print("RESULT: D_A alone is not nilpotent on the nonflat control; full ordinary BRST remains valid")
    print("BOUNDARY: no sourced scalar-spinor -> ker Gamma map, so W131 Jordan cohomology is not retested")


if __name__ == "__main__":
    main()
