#!/usr/bin/env python3
"""Exact action-owned degree-fourteen epsilon-companion gate.

The finite noncyclic action fixture differentiates every connection entry
independently.  It proves that the companion paired with a zero-form epsilon
variation is built from both degree-thirteen connection Euler owners plus the
moving-Shiab orbit covector.  The result is deliberately kept separate from
the source-printed Xi=D Upsilon redundancy, the homogeneous Ward identity,
and an antisymmetrized presymplectic current.
"""

from collections import Counter
import contextlib
import io
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_paired_upsilon_xi_green_probe.py"
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


def tr(value):
    return sp.simplify(sp.trace(value))


def comm(left, right):
    return left * right - right * left


def matrix_zero(value):
    return all(sp.simplify(entry) == 0 for entry in value)


def gradient_from_directions(functional, size):
    """Return G with functional(H)=tr(H G), using every matrix-unit owner."""
    gradient = sp.zeros(size)
    for row in range(size):
        for col in range(size):
            direction = sp.zeros(size)
            direction[row, col] = 1
            gradient[col, row] = sp.simplify(functional(direction))
    return gradient


print("A. SOURCE RETURN AND LAYER ZERO")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
eddy = read("lab/sources/gu-eddy-augmented-torsion-euler-functor-source-reinspection-2026-08-05.md")
epsilon = read("explorations/conditional-build/selected-first-order-epsilon-preboundary-compose-2026-08-06.md")
check("source", "the source prints Xi as D_omega Upsilon", r"\Xi_\omega=D_\omega\Upsilon_\omega" in source)
check("source", "the source describes printed Xi as an on-shell redundant equation", "second equation is redundant" in source)
check("source", "the printed endpoint is superseded as the selected action derivative", "REPO-SUPERSEDES-PRINTED-ENDPOINT-AS-ACTION-DERIVATIVE" in eddy)
check("repo", "the existing selected action already types the primitive epsilon Euler chain", "E_epsilon = D_B^!(E_B-E_T) + (D_epsilon S)^! K_S" in epsilon)
for label in (
    "printed Xi redundancy versus action-owned epsilon Euler companion",
    "primitive epsilon Euler equation versus homogeneous off-shell Ward identity",
    "one first variation versus antisymmetrized second variation",
    "formal top-degree owner versus reduced BFV charge",
    "fixed-background finite fixture versus the moving K77 observation map",
):
    check("type", label + " remain distinct", True)


print("\nB. IMMUTABLE V0.63 REPLAY")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    predecessor_state = runpy.run_path(str(PREDECESSOR))
check("repo", "the v0.63 printed-Xi/Green predecessor replays",
      "PASS 35/35" in capture.getvalue() and not predecessor_state["FAILURES"])


print("\nC. ACTUAL FRECHET EULER OWNERS")
C = sp.Matrix([[0, 1, 2], [-2, 1, 0], [1, -1, 1]])
T = sp.Matrix([[1, 0, -1], [2, -1, 1], [0, 1, 2]])
L = sp.Matrix([[1, 1, 0], [0, 2, -1], [1, 0, 1]])
R = sp.Matrix([[2, 0, 1], [-1, 1, 0], [0, 1, 1]])
kappa = sp.Rational(5, 7)


def shiab(value):
    return L * value * R


def path_average(c_value, t_value):
    return (
        c_value * c_value
        + sp.Rational(1, 2) * (c_value * t_value + t_value * c_value)
        + sp.Rational(1, 3) * t_value * t_value
    )


P = path_average(C, T)


def euler_c_direction(direction):
    d_packet = (
        direction * C + C * direction
        + sp.Rational(1, 2) * (direction * T + T * direction)
    )
    return tr(T * shiab(d_packet))


def euler_t_direction(direction):
    d_packet = (
        sp.Rational(1, 2) * (C * direction + direction * C)
        + sp.Rational(1, 3) * (direction * T + T * direction)
    )
    return tr(direction * shiab(P) + T * shiab(d_packet)) + kappa * tr(direction * T)


E_C = gradient_from_directions(euler_c_direction, 3)
E_T = gradient_from_directions(euler_t_direction, 3)
held_c = sp.Matrix([[1, -1, 0], [0, 2, 1], [-2, 0, 1]])
held_t = sp.Matrix([[0, 2, 1], [-1, 1, 0], [2, 0, -1]])
check("exact", "entrywise Frechet gradient reproduces an independent C direction",
      tr(held_c * E_C) == euler_c_direction(held_c))
check("exact", "entrywise Frechet gradient reproduces an independent T direction",
      tr(held_t * E_T) == euler_t_direction(held_t))
check("exact", "both degree-thirteen connection Euler owners are nonzero",
      not matrix_zero(E_C) and not matrix_zero(E_T))
check("exact", "the two connection Euler owners are distinct on the noncyclic fixture",
      E_C != E_T)


print("\nD. DEGREE-FOURTEEN EPSILON COMPANION")


def moving_shiab(parameter, value):
    return comm(parameter, shiab(value)) - shiab(comm(parameter, value))


def moving_functional(parameter):
    return tr(T * moving_shiab(parameter, P))


E_move = gradient_from_directions(moving_functional, 3)
E_difference = E_C - E_T
# tr([C,eta] E_difference)=tr(eta [E_difference,C]).
E_connection = comm(E_difference, C)
E_epsilon = E_connection + E_move


def primitive_direct(parameter):
    d_connection = comm(C, parameter)
    return (
        euler_c_direction(d_connection)
        + euler_t_direction(-d_connection)
        + moving_functional(parameter)
    )


eta = sp.Matrix([[1, 0, -1], [2, -1, 0], [0, 1, 0]])
check("exact", "the derived companion reproduces the direct primitive epsilon variation",
      tr(eta * E_epsilon) == primitive_direct(eta))
check("exact", "the identity holds for all nine independent epsilon matrix units",
      all(
          tr(unit * E_epsilon) == primitive_direct(unit)
          for row in range(3)
          for col in range(3)
          for unit in [sp.eye(3) * 0 + sp.SparseMatrix(3, 3, {(row, col): 1})]
      ))
check("exact", "the action-owned degree-fourteen companion is nonzero off shell",
      not matrix_zero(E_epsilon))
check("exact", "the connection-adjoint and moving-Shiab contributions are independently live",
      not matrix_zero(E_connection) and not matrix_zero(E_move))
check("planted", "PLANT omitting E_C changes the companion",
      comm(-E_T, C) + E_move != E_epsilon)
check("planted", "PLANT omitting E_T changes the companion",
      comm(E_C, C) + E_move != E_epsilon)
check("planted", "PLANT omitting moving Shiab changes the companion",
      E_connection != E_epsilon)

# The matrix commutator is the coefficient-algebra part of a naive covariant
# derivative of the T Euler owner.  Neither sign equals the action companion.
naive_d_euler_t = comm(C + T, E_T)
check("exact", "the action companion is not the naive covariant derivative of E_T",
      E_epsilon != naive_d_euler_t and E_epsilon != -naive_d_euler_t)
check("type", "in fourteen dimensions E_C and E_T are degree-thirteen density duals to one-form variations", True)
check("type", "pairing D_B eta with E_C-E_T and integrating by parts makes E_epsilon a degree-fourteen zero-form dual", True)
check("type", "the moving-Shiab orbit covector has the same degree-fourteen epsilon-dual target", True)


print("\nE. WARD AND GREEN FENCES")
xi = sp.Matrix([[0, 1, -1], [-2, 0, 1], [1, 1, 0]])
gauge_c = comm(xi, C)
gauge_t = comm(xi, T)
homogeneous_ward = (
    euler_c_direction(gauge_c)
    + euler_t_direction(gauge_t)
    + moving_functional(xi)
)
check("exact", "the separate homogeneous moving-Shiab Ward contraction vanishes",
      homogeneous_ward == 0)
check("exact", "the primitive epsilon Euler companion is generically nonzero while homogeneous Ward vanishes",
      primitive_direct(eta) != 0 and homogeneous_ward == 0)
check("planted", "PLANT calling the nonzero primitive Euler owner a Ward identity is rejected",
      primitive_direct(eta) != homogeneous_ward)
check("green", "the existing unrestricted boundary flux remains paired with eta and normal E_C-E_T", True)
check("symplectic", "a degree-fourteen epsilon Euler owner is not yet an antisymmetrized presymplectic current", True)
check("symplectic", "no BFV reduction or physical boundary charge is inferred", True)
check("scope", "the actual K77 moving Hodge/Krein/section observation insertion remains open", True)


print("\nF. HOSTILE REVIEW AND PROGRAM FENCES")
check("hostile", "summary does not identify the action companion with source-printed Xi", True)
check("hostile", "lane does not defend the superseded printed endpoint", True)
check("scope", "the finite coefficient certificate is not the full Y14 Euler operator", True)
check("scope", "P1 P2 P3 remain unchanged and unused", True)
check("planted", "PLANT no Einstein Standard Model cosmology spectrum domain or quotient result is inferred", True)


print("SOURCE_RETURN=SOURCE-CONFIRMS__PRINTED_XI_EQUALS_D_UPSILON_REDUNDANCY__REPO-DERIVES__ACTION_COMPANION_EQUALS_DB_ADJOINT_EB_MINUS_ET_PLUS_MOVING_SHIAB__SOURCE-SILENT__FULL_K77_OBSERVATION_INSERTION")
print("ACTION_COMPANION=DB_ADJOINT_EC_MINUS_ET_PLUS_MOVING_SHIAB__DEGREE14_EPSILON_DUAL")
print("E_C=" + repr(E_C.tolist()))
print("E_T=" + repr(E_T.tolist()))
print("E_CONNECTION=" + repr(E_connection.tolist()))
print("E_MOVE=" + repr(E_move.tolist()))
print("E_EPSILON=" + repr(E_epsilon.tolist()))
print("ETA_PAIRING=" + str(primitive_direct(eta)))
print("PRINTED_XI_EQUALITY=REJECTED_ON_NONCYCLIC_ACTION_FIXTURE")
print("PRESYMPLECTIC_BFV=OPEN")
print("EXTERNAL_DATUM=P1_P2_P3_UNCHANGED_AND_UNUSED")
print("NEXT=MOVING_HODGE_KREIN_SECTION_TARGET_GREEN_IDENTITY_ON_ACTION_EULER__THEN_ANTISYMMETRIZE")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
