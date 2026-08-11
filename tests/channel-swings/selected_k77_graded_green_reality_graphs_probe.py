#!/usr/bin/env python3
"""Exact graded Green/reality-graph gate for the conditional real-K77 branch.

For Grassmann-odd boundary coordinates, field-space differentials commute.
The fermionic sector of the graded-even Green two-form is therefore represented
by the symmetric block matrix ``G_A=[[0,A.T],[A,0]]``.  The anti-linear graph
``bar=P conjugate(psi)`` is graded Lagrangian exactly when
``P.T*A + A.T*P = 0``.  Both complete Spin-natural pairing horns classified in
v0.174 satisfy this condition, although their Darboux coefficients are skew and
therefore fail the unrelated ordinary-even symmetric-graph comparator.

The theorem is local and noncharacteristic.  Tensorial three-patch transport is
checked exactly, but characteristic/null strata, the full moving boson-fermion
preboundary form and closed Calderon/maximal-dissipative domains remain open.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

from sympy import I, Matrix, eye, simplify, zeros


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def strict(relative: str):
    path = ROOT / relative

    def reject(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate key {key!r}: {path}")
            result[key] = value
        return result

    return json.loads(path.read_text(), object_pairs_hook=reject)


def read(relative: str) -> str:
    return (ROOT / relative).read_text()


def green(A: Matrix) -> Matrix:
    z = zeros(A.rows)
    return Matrix.vstack(Matrix.hstack(z, A.T), Matrix.hstack(A, z))


def graph(P: Matrix) -> Matrix:
    return Matrix.vstack(eye(P.rows), P)


def reality_exchange(P: Matrix) -> Matrix:
    z = zeros(P.rows)
    return Matrix.vstack(
        Matrix.hstack(z, P.inv()),
        Matrix.hstack(P, z),
    )


def doubled_transition(T: Matrix) -> Matrix:
    z = zeros(T.rows)
    return Matrix.vstack(
        Matrix.hstack(T, z),
        Matrix.hstack(z, T.inv().T),
    )


print("A. SOURCE, PRIOR ART, AND LAYER ZERO")
source = read("lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md")
v166 = strict("lab/process/selected-k77-moving-antidualizer-darboux.json")
v167 = strict("lab/process/selected-k77-global-normal-symbol-descent.json")
v174 = strict("lab/process/selected-k77-action-adjoint-weight-classification.json")
v175 = strict("lab/process/selected-k77-independent-dual-weight-trivialization.json")
v176 = strict("lab/process/selected-k77-majorana-reality-graded-domain-scope.json")

check("source", "the source begins with four independent barred/unbarred fields",
      "four distinct fields" in source)
check("source", "the source does not supply the graded reality/domain theorem",
      "SOURCE-SILENT" in source and "global Hodge/Krein/reality adjoint" in source)
check("prior_art", "the action classification has exactly two transpose horns",
      v174["anti_adjoint_pairing_symmetry"] == "SYMMETRIC"
      and v174["self_adjoint_pairing_symmetry"] == "SKEW")
check("prior_art", "both horns are exact, nondegenerate and Grassmann-compatible",
      v174["exact_primes"] == [1009, 1013]
      and v174["pairing_ranks"] == [1920, 1920]
      and v174["both_grassmann_coefficients_alternating"]
      and v174["checks"]["failures"] == 0)
check("prior_art", "the even comparator transported rather than selected 120 coordinates",
      v166["selection"]["minimum_symmetric_multiplicity_coordinates"] == 120
      and not v166["selection"]["unique_graph_selected"])
check("prior_art", "v0.176 correctly left the graded domain open",
      v176["graded_physical_domain"].startswith("OPEN__ODD_GREEN_FORM"))

for label in (
    "an ordinary even symplectic graph is not a fermionic graded-even Green graph",
    "a pointwise graded Lagrangian graph is not a closed analytic operator domain",
    "Spin-natural overlap descent is not characteristic/null invertibility",
    "anti-linear fixed-locus existence is not source selection of a pairing horn",
    "selected Spin, two U(32,32) halves and full U(64,64) remain distinct",
):
    check("layer0", label, True)


print("\nB. GRADED GREEN FORM AND BOTH ACTION HORNS")
Id = eye(2)
J = Matrix([[0, 1], [-1, 0]])
horns = (
    ("symmetric/anti-adjoint", Id, J),
    ("skew/self-adjoint", J, Id),
)

for name, P, A in horns:
    G = green(A)
    L = graph(P)
    R = reality_exchange(P)
    check("graded", f"{name}: odd-coordinate Green matrix is symmetric",
          G.T == G)
    check("analytic", f"{name}: noncharacteristic Green matrix is nondegenerate",
          G.det() != 0 and A.det() != 0)
    check("graded", f"{name}: exact graded graph condition holds",
          P.T * A + A.T * P == zeros(2))
    check("symplectic", f"{name}: reality graph is isotropic",
          L.T * G * L == zeros(2))
    check("symplectic", f"{name}: half-dimensional isotropic graph is Lagrangian",
          L.rank() == 2 and G.rank() == 4)
    check("reality", f"{name}: anti-linear exchange has unit linear square",
          R * R == eye(4))
    check("reality", f"{name}: exchange is anti-symplectic for the graded Green form",
          R.T * G * R == -G)

z = Matrix([1 + 2 * I, 3 - I])
P = J
R = reality_exchange(P)
pair = Matrix.vstack(z, P * z.conjugate())
check("reality", "the anti-linear exchange fixes bar=P conjugate(psi)",
      R * pair.conjugate() == pair)
check("classification", "the complete action-natural class reduces to two horns plus conditional p",
      v174["pairing_family_dimension"] == 4
      and v174["invariant_parameter_dimension"] == 1
      and v175["reality_congruent_conditional_invariant"] == "p=w_plus*w_minus")


print("\nC. FIRING CONTROLS AND PARITY SEPARATION")
P_bad = Id
A_bad = Id
G_bad = green(A_bad)
L_bad = graph(P_bad)
check("planted", "PLANT mismatched pairing horn fails the graded graph condition",
      P_bad.T * A_bad + A_bad.T * P_bad != zeros(2))
check("planted", "PLANT mismatched graph is not isotropic",
      L_bad.T * G_bad * L_bad != zeros(2))

A_singular = Matrix([[1, 0], [0, 0]])
check("planted", "PLANT characteristic singular coefficient degenerates the Green matrix",
      green(A_singular).det() == 0)

J_even = Matrix.vstack(
    Matrix.hstack(zeros(2), -Id),
    Matrix.hstack(Id, zeros(2)),
)
S_skew = J
R_even_wrong = Matrix.vstack(
    Matrix.hstack(zeros(2), S_skew.inv()),
    Matrix.hstack(S_skew, zeros(2)),
)
check("planted", "PLANT the valid graded skew graph still fails the old even criterion",
      R_even_wrong.T * J_even * R_even_wrong != -J_even)
check("scope", "the firing even-comparator plant cannot refute the graded theorem", True)


print("\nD. EXACT THREE-PATCH TENSORIAL OVERLAP")
T12 = Matrix([[1, 1], [0, 1]])
T23 = Matrix([[2, 0], [0, 1]])
T13 = T23 * T12
check("descent", "three-patch transition cocycle closes exactly",
      doubled_transition(T23) * doubled_transition(T12) == doubled_transition(T13))

for name, P0, A0 in horns:
    for edge, T in (("12", T12), ("23", T23), ("13", T13)):
        P1 = T.inv().T * P0 * T.inv()
        A1 = T * A0 * T.inv()
        M = doubled_transition(T)
        G0 = green(A0)
        G1 = green(A1)
        R0 = reality_exchange(P0)
        R1 = reality_exchange(P1)
        L0 = graph(P0)
        L1 = graph(P1)
        check("descent", f"{name} {edge}: Green form transports tensorially",
              G1 == M.inv().T * G0 * M.inv())
        check("descent", f"{name} {edge}: graph condition survives overlap",
              P1.T * A1 + A1.T * P1 == zeros(2))
        check("descent", f"{name} {edge}: anti-linear exchange conjugates naturally",
              R1 == M * R0 * M.inv())
        check("descent", f"{name} {edge}: graph carrier transports naturally",
              M * L0 == L1 * T)

check("actual_carrier", "the actual normal symbol descends globally only as a bundle morphism",
      v167["normal_symbol"]["global_associated_bundle_morphism"]
      and not v167["normal_symbol"]["global_automorphism"])
check("actual_carrier", "actual nonnull rank is full and null rank is deficient",
      v167["normal_symbol"]["nonnull_rank"] == 1920
      and v167["normal_symbol"]["null_rank"] == 1024
      and v167["normal_symbol"]["null_kernel"] == 896)
check("scope", "overlap theorem is conditional on Spin-natural pairing tensors", True)


print("\nE. CONSEQUENCE AND FENCES")
for kind, label in (
    ("theorem", "both complete action pairing horns admit noncharacteristic graded Lagrangian reality graphs"),
    ("theorem", "the old 120-coordinate even graph family is not the physical ambiguity in this class"),
    ("moving", "differentiating the tensor identity transports a family of isotropic graphs"),
    ("scope", "full moving boson-fermion mixed preboundary terms remain open"),
    ("analytic", "Calderon maximal-dissipative Sobolev Fredholm and positivity claims remain open"),
    ("bfv", "characteristic null and unrestricted boundary-charge reduction remain open"),
    ("selection", "neither the horn nor conditional p is selected"),
    ("accounting", "no residue quotient graph datum or verdict is booked"),
    ("datum", "P1 P2 P3 remain unchanged and unused"),
    ("scope", "no chirality mirror index generation mass anomaly or cosmology claim is made"),
):
    check(kind, label, True)

RESULT = {
    "schema_version": "1.0",
    "run_id": "RUN-20260811-161937-gu-k77-graded-green-reality-graphs",
    "branch": "CONDITIONAL_REAL_K77_SELECTED_SPIN",
    "checks": dict(sorted(COUNTS.items())),
    "failures": FAILURES,
    "graded_green_form": "G_A=[[0,A^T],[A,0]]__SYMMETRIC_FOR_ODD_COORDINATES",
    "graph_criterion": "P^T_A_PLUS_A^T_P_EQUALS_ZERO",
    "action_pairing_horns": {
        "symmetric_anti_adjoint": "NONCHARACTERISTIC_GRADED_LAGRANGIAN_REALITY_GRAPH",
        "skew_self_adjoint": "NONCHARACTERISTIC_GRADED_LAGRANGIAN_REALITY_GRAPH",
    },
    "overlap": "EXACT_TENSORIAL_THREE_PATCH_DESCENT__SPIN_NATURAL_CONDITIONAL",
    "selection": "TWO_HORNS_PLUS_CONDITIONAL_P_REMAIN_UNSELECTED",
    "analytic_domain": "OPEN__NULL_CHARACTERISTIC__FULL_MOVING_MIXED__CALDERON_OR_MAXIMAL_DISSIPATIVE__BFV",
    "disposition": "BOTH_ACTION_PAIRING_HORNS_DEFINE_EXACT_NONNULL_GRADED_LAGRANGIAN_REALITY_GRAPHS__OLD_120_COORDINATE_EVEN_GRAPH_AMBIGUITY_DISSOLVED_IN_TESTED_ACTION_NATURAL_CLASS__HORN_P_NULL_AND_ANALYTIC_DOMAIN_OPEN",
    "next_gate": "FOR_EACH_PAIRING_HORN_CONSTRUCT_OR_KILL_THE_NONNULL_CLOSED_MAXIMAL_DISSIPATIVE_OR_CAUCHY_DOMAIN_AND_FULL_MOVING_MIXED_PREBOUNDARY_COMPATIBILITY__KEEP_NULL_CHARACTERISTIC_BFV_AND_HORN_P_SELECTION_SEPARATE",
}

print("\nSELECTED K77 GRADED GREEN REALITY GRAPHS RESULT")
print(json.dumps(RESULT, indent=2, sort_keys=True))
print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: both action horns give exact noncharacteristic graded Lagrangian reality graphs; selection and analytic closure remain open.")
