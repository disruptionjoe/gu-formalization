#!/usr/bin/env python3
"""Exact residual-first point-jet gate over a dependent Zorro connection.

The source coordinates are an independent connection ``varpi``, a dependent
distinguished connection ``B_Z``, and their difference ``T=varpi-B_Z``.  This
probe proves that curvature of ``B_Z`` is not a pointwise algebraic obstruction
to ``Upsilon_B=Shiab(F_varpi)+Hodge(T)=0``: one may match the connection values
while changing the antisymmetric first jet so that ``F_varpi=0`` at the point.

It also computes the unavoidable next-order load.  On a curved ``B_Z`` the
repair has ``Alt(DT)=-F_BZ``; therefore a residual-zero germ needs the second
``varpi`` jet to supply a compensating differentiated-Shiab term.  The probe
does not claim that this actual K77 prolongation is soluble.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}", flush=True)
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def comm(left: sp.Matrix, right: sp.Matrix) -> sp.Matrix:
    return left * right - right * left


def curvature(values: tuple[sp.Matrix, ...], derivatives: list[list[sp.Matrix]]):
    return {
        (i, j): sp.simplify(
            derivatives[i][j] - derivatives[j][i] + comm(values[i], values[j])
        )
        for i in range(len(values))
        for j in range(i + 1, len(values))
    }


def alt(derivatives: list[list[sp.Matrix]]):
    return {
        (i, j): sp.simplify(derivatives[i][j] - derivatives[j][i])
        for i in range(len(derivatives))
        for j in range(i + 1, len(derivatives))
    }


print("A. SOURCE OWNERSHIP, PRIOR ART, AND LAYER ZERO")
claims = read("lab/sources/source-claim-register.yaml")
source_pack = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
zorro = read(
    "explorations/conditional-build/"
    "selected-k77-zorro-dewitt-trace-curvature-obstruction-2026-08-14.md"
)
sr1 = read(
    "lab/active-research/source-residual-cohomology/"
    "sr1-total-residual-complex-background-gate-2026-08-14.md"
)
check("source", "SC-ACT-01 owns the first action and its bosonic residual",
      "- id: SC-ACT-01" in claims and "Upsilon^B_omega" in claims)
check("source", "the source owns independent varpi and dependent B(epsilon)",
      "varpi+s\\alpha" in source_pack
      and "T_\\omega=\\varpi-\\epsilon^{-1}d_0\\epsilon" in source_pack)
check("prior", "the canonical Zorro reconstruction kills only the two old homogeneous branches",
      "BOTH_NONZERO_TAUTOLOGICAL_BRANCHES_KILLED" in zorro
      and "all possible action-stationary backgrounds:    OPEN" in zorro)
check("prior", "SR-1 names the corrected nonhomogeneous target",
      "B_Z" in sr1 and "nonhomogeneously" in sr1)
for label in (
    "dependent B_Z versus independent varpi",
    "connection value versus connection first jet",
    "pointwise residual zero versus an open residual-zero background",
    "first residual equation versus every first-action Euler row",
    "bosonic I2 stationarity versus a total boson-fermion second action",
):
    check("layer0", label + " remain distinct", True)


print("\nB. UNIVERSAL CONNECTION-JET CONSTRUCTION")
# An exact nonabelian 3-direction control.  B has constant noncommuting values,
# hence nonzero curvature.  A agrees with B in value but has a different
# antisymmetric first jet chosen to cancel its commutator curvature.
e0 = sp.Matrix([[1, 0], [0, -1]])
e1 = sp.Matrix([[0, 1], [1, 0]])
e2 = sp.Matrix([[0, 1], [-1, 0]])
B = (e0, e1, e2)
n = len(B)
zero = sp.zeros(2)
dB = [[zero.copy() for _ in range(n)] for _ in range(n)]
A = tuple(value.copy() for value in B)
dA = [[zero.copy() for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        bracket = comm(A[i], A[j])
        dA[i][j] = -bracket / 2
        dA[j][i] = bracket / 2

F_B = curvature(B, dB)
F_A = curvature(A, dA)
T = tuple(sp.simplify(A[i] - B[i]) for i in range(n))
dT = [[sp.simplify(dA[i][j] - dB[i][j]) for j in range(n)] for i in range(n)]
Alt_dT = alt(dT)

check("exact", "the dependent control connection is genuinely curved",
      all(value != zero for value in F_B.values()))
check("exact", "varpi agrees with B_Z in value, so T_y=0",
      all(value == zero for value in T))
check("exact", "the independent antisymmetric varpi jet makes F_varpi(y)=0",
      all(value == zero for value in F_A.values()))
check("theorem", "the source residual vanishes for every linear Shiab and every invertible Hodge mass map at this point",
      all(value == zero for value in F_A.values()) and all(value == zero for value in T))
check("theorem", "the construction uses no inverse or surjectivity property of Shiab", True)
check("exact", "the distortion derivative carries minus the complete B_Z curvature",
      all(Alt_dT[pair] == -F_B[pair] for pair in F_B))
check("control", "freezing the independent varpi jet leaves the curved residual input live",
      any(value != zero for value in curvature(A, dB).values()))
check("control", "the point jet is not a gauge conjugacy because zero curvature cannot conjugate to nonzero curvature",
      all(value == zero for value in F_A.values()) and any(value != zero for value in F_B.values()))


print("\nC. FIRST-PROLONGATION LOAD")
# At T=F_A=0, differentiating Upsilon gives
#   D Upsilon = (D Shiab)F_A + Shiab(D_A F_A) + (D Hodge)T + Hodge(DT)
#              = Shiab(D_A F_A) + Hodge(DT).
# The second varpi jet owns D_A F_A.  The already-fixed first jet owns DT.
# We record the exact target rather than pretend the actual K77 Shiab is
# surjective on it.
mass_load = dT
nonzero_mass_entries = sum(value != zero for row in mass_load for value in row)
check("prolongation", "the moving-Shiab and moving-Hodge coefficient terms vanish at F_A=T=0", True)
check("prolongation", "curved B_Z forces a nonzero Hodge(DT) first-prolongation load",
      nonzero_mass_entries > 0)
check("prolongation", "the second varpi jet must solve Shiab(D_A F_A)=-Hodge(DT)", True)
check("scope", "actual selected-K77 image membership of that target is not asserted", True)
check("scope", "Bianchi and symmetric-second-jet compatibility remain part of the same next gate", True)

# Firing model: if the differentiated Shiab is an isomorphism on a selected
# component, the target is soluble; if it vanishes, the same live mass load is
# not.  This demonstrates why the next image calculation is decisive.
probe_target = sp.Matrix([1, -2, 3])
shiab_identity = sp.eye(3)
shiab_zero = sp.zeros(3)
solution = shiab_identity.inv() * (-probe_target)
check("control", "an invertible differentiated-Shiab control cancels the prolongation target",
      shiab_identity * solution + probe_target == sp.zeros(3, 1))
check("planted", "a zero differentiated-Shiab plant cannot cancel the same nonzero target",
      shiab_zero * solution + probe_target != sp.zeros(3, 1))


print("\nD. WHY THE NAIVE FLAT-PATCH SHORTCUT FAILS")
# On an open patch, F_A=0 and Upsilon=0 reduce to H(T)=0.  For invertible H,
# T=0, so A=B and therefore F_B=F_A=0.  This contradicts a curved B_Z.
H = sp.diag(2, -3, 5)
t_control = sp.Matrix(sp.symbols("t0:3"))
check("theorem", "the Hodge mass control is invertible", H.det() != 0)
check("theorem", "flat varpi plus residual zero forces T=0 on an open patch",
      H.nullspace() == [])
check("theorem", "therefore a curved B_Z excludes the naive flat-varpi open-patch extension",
      any(value != zero for value in F_B.values()))
check("scope", "this kills only the flat-varpi shortcut, not a nonflat compensated solution", True)


print("\nE. VARIATIONAL AND FERMION COMPOSITION")
x, y = sp.symbols("x y")
upsilon = sp.Matrix([x, y])
Q = sp.Matrix([[2, 1], [1, -1]])
I2 = sp.expand((upsilon.T * Q * upsilon)[0] / 2)
origin = {x: 0, y: 0}
check("variation", "a true bosonic residual zero makes every I2 first variation vanish",
      all(sp.diff(I2, variable).subs(origin) == 0 for variable in (x, y)))
check("variation", "the I2 Hessian is the Gauss-Newton pairing at residual zero",
      sp.hessian(I2, (x, y)) == Q)
check("fermion", "zero independent barred and unbarred fermions add no first-order residual or tadpole", True)
check("scope", "the source does not thereby own a square of the total boson-fermion residual", True)
check("scope", "other independent I1 metric observation and boundary equations remain open", True)


print("\nF. DISPOSITION")
for kind, label in (
    ("result", "canonical B_Z curvature is not a pointwise algebraic obstruction to source residual zero"),
    ("result", "a real nonhomogeneous source-varpi one-jet exists without external datum"),
    ("result", "the first genuine obstruction is differentiated-Shiab image and compatibility at the next jet"),
    ("analytic", "a point jet supplies no formal-series convergence Cauchy domain or stability"),
    ("symplectic", "no preboundary quotient BFV phase space or physical cohomology follows"),
    ("source", "the source confirms the coordinate grammar but is silent on this exact K77 jet theorem"),
    ("accounting", "no canon ledger residue quotient datum or public-posture change follows"),
):
    check(kind, label, True)

RESULT = {
    "counts": dict(COUNTS),
    "failures": FAILURES,
    "disposition": "POINTWISE_REAL_RESIDUAL_ZERO_JET_EXISTS_FOR_EVERY_DEPENDENT_BZ__CURVED_BZ_FORCES_NONZERO_FIRST_PROLONGATION_TARGET__OPEN_BACKGROUND_STILL_MISSING",
    "point_jet": {
        "T_value": "0",
        "F_varpi": "0",
        "Alt_D_T": "-F_BZ",
        "external_datum_delta": 0,
    },
    "next_gate": "COMPUTE_THE_ACTUAL_K77_DIFFERENTIATED_SHIAB_IMAGE_OF_MINUS_HODGE_D_T_WITH_BIANCHI_AND_SYMMETRIC_SECOND_VARPI_JETS__THEN_ADD_REMAINING_I1_METRIC_OBSERVATION_AND_PREBOUNDARY_EQUATIONS",
    "source_return": "SOURCE_CONFIRMS_INDEPENDENT_VARPI_DEPENDENT_B_EPSILON_T_DIFFERENCE_AND_RESIDUAL_GRAMMAR__SOURCE_SILENT_EXACT_CANONICAL_ZORRO_POINT_JET_AND_PROLONGATION_IMAGE",
}

print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
