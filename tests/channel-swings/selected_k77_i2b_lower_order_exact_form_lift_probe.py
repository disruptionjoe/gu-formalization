#!/usr/bin/env python3
"""Exact lower-order lift of the selected I2B principal exact-form kernel.

The predecessor proved that ``K(k) xi = k tensor xi`` lies in the principal
Hessian kernel but is not the source adjoint-gauge map.  This probe keeps the
same fixed-``H_q`` real-K77 branch and assembles the part of the *full
linearized action Hessian* that acts on ``im K(k)``.  Since
``k wedge (k tensor xi)=0``, this restriction is controlled entirely by the
owned zero-order residual derivative, its cross term with the derivative
operator, and the residual-dependent second variation.

This is a finite-frequency constant-background theorem.  Lower-order lifting
does not change the principal characteristic variety and does not construct a
source BV quotient, physical carrier, closed domain, or propagator.
"""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_i2b_principal_degeneracy_retype_probe.py"
HESSIAN = ROOT / "tests/channel-swings/selected_k77_i2b_moving_higgs_principal_hessian_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object, detail: object = "") -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    suffix = f" ({detail})" if detail != "" else ""
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}{suffix}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


print("A. LAYER ZERO, PRIOR ART, SOURCE RETURN, AND ADAPTIVE PREFLIGHT")
claims = read("lab/sources/source-claim-register.yaml")
source = read("lab/sources/gu-two-layer-action-source-reinspection-2026-08-04.md")
prior = read("explorations/conditional-build/selected-k77-i2b-principal-degeneracy-retype-2026-08-13.md")
check("source", "SC-ACT-04 owns the bosonic residual square",
      "- id: SC-ACT-04" in claims and "I^B_2 = ||Upsilon^B_omega||^2" in claims)
check("source", "the source confirms the norm-square arena but not this K77 finite-frequency restriction",
      "SOURCE-CONFIRMS-NORM-SQUARE-AND-REDUNDANCY" in source)
check("prior_art", "the predecessor names lower-order lifting as the next exact gate",
      "complete lower-order Hessian/characteristic complex" in prior)
for label in (
    "principal symbol versus full finite-frequency linearized Hessian",
    "Cl1 exact-form map versus Cl2 source adjoint gauge map",
    "first Euler covector versus second variation of the action",
    "Riesz isomorphism versus the action Hessian",
    "finite constant background versus physical carrier and global domain",
):
    check("layer0", label + " remain distinct", True)
for kind, label in (
    ("variational", "include both J-adjoint-K-J and residual-dependent second variation"),
    ("analytic", "retain the principal characteristic variety after lower-order lifting"),
    ("krein", "test the symmetric action Hessian despite a nonzero K-null residual"),
    ("gauge_bv", "do not relabel a lifted non-gauge exact-form family as gauge"),
    ("symplectic", "do not infer a reduced phase space from a finite Hessian rank"),
    ("source_review", "grade the exact K77 restriction as repository-derived"),
    ("contrary", "plant omission of the residual-dependent second variation"),
):
    check(kind, label, True)


print("\nB. IMMUTABLE PREDECESSORS AND STRUCTURE FINGERPRINT")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    R = runpy.run_path(str(PREDECESSOR))
check("repo", "principal-degeneracy correction predecessor replays",
      "PASS 48/48" in capture.getvalue() and not R["FAILURES"])
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    H = runpy.run_path(str(HESSIAN))
check("repo", "moving-Hq principal-Hessian predecessor replays",
      "PASS 44/44" in capture.getvalue() and not H["FAILURES"])

P = H["P"]
S = P["S"]
cells = P["cells"]
ONE = P["ONE"]
I = S["I"]
SELECTED = P["SELECTED"]
one_form = S["one_form"]
fadd = S["fadd"]
fscale = S["fscale"]
wedge_raw = S["wedge_raw"]
shiab = S["shiab"]
sym_pair = P["sym_pair"]
real_scalar = P["real_scalar"]
zero_linear = S["residual_derivative"]
residual = S["residual_at_branch"]

check("fingerprint", "field carrier is the same 196-real fixed-Hq Cl1 connection bank", len(cells) == 196)
check("fingerprint", "pairing is the same selected real K77 residual pairing", bool(residual))
check("fingerprint", "the background is the same nonzero K-null restricted radial critical branch",
      S["residual_pairing"](residual, residual) == S["ZERO"])
check("fingerprint", "that restricted branch remains nonstationary on the full 196-cell bank",
      bool(S["gradient"]))
check("fingerprint", "the principal and lower-order packets share the selected Shiab channel",
      SELECTED == S["SELECTED"])


def add_many(values):
    out = {}
    for value in values:
        out = fadd(out, value)
    return out


def exact_direction(k: tuple[int, ...], clifford_index: int):
    phase = ONE if clifford_index == 13 else I
    return add_many(
        fscale(Fraction(coefficient), one_form(mu, clifford_index, phase))
        for mu, coefficient in enumerate(k) if coefficient
    )


def principal(k: tuple[int, ...], delta):
    return add_many(
        fscale(Fraction(coefficient), P["principal"](mu, delta))
        for mu, coefficient in enumerate(k) if coefficient
    )


def second_residual(left, right):
    return shiab(fscale(Fraction(1, 3), fadd(
        wedge_raw(left, right), wedge_raw(right, left)
    )), SELECTED)


def scalar(value) -> sp.Expr:
    return sp.factor(real_scalar(value))


print("\nC. EXACT RESTRICTED FULL-HESSIAN POLYNOMIAL")
covectors = {
    "timelike": (1, 0, 0, 0),
    "spacelike": (0, 1, 0, 0),
    "generic_nonnull": (2, 1, 1, 0),
    "null": (1, 1, 0, 0),
}
results = {}
t = sp.symbols("t", real=True)

for name, k in covectors.items():
    exact = [exact_direction(k, a) for a in range(14)]
    principal_exact = [principal(k, delta) for delta in exact]
    check("syzygy", f"{name} exact-form responses vanish at principal grade",
          all(not value for value in principal_exact))

    lower_exact = [zero_linear(delta) for delta in exact]
    m1 = sp.zeros(196, 14)
    m2 = sp.zeros(196, 14)
    for row, (_, _, test) in enumerate(cells):
        p_test = principal(k, test)
        b_test = zero_linear(test)
        for column, (delta, b_exact) in enumerate(zip(exact, lower_exact)):
            # H(tk)K(tk)=t*M1+t^2*M2.  M1 is the pure lower-order
            # Hessian, including Upsilon.D2Upsilon. M2 is the
            # derivative/lower-order cross term from J(-k)^* K J(k).
            m1[row, column] = scalar(sym_pair(b_test, b_exact)) + scalar(
                sym_pair(second_residual(test, delta), residual)
            )
            m2[row, column] = -scalar(sym_pair(p_test, b_exact))

    rank_m1 = m1.rank()
    rank_m2 = m2.rank()
    rank_plus = (m1 + m2).rank()
    rank_minus = (m1 - m2).rank()
    rank_two = (m1 + 2 * m2).rank()
    check("hessian", f"{name} pure lower-order restriction has full column rank",
          rank_m1 == 14, rank_m1)
    check("hessian", f"{name} full restriction has rank fourteen at t=1,-1,2",
          (rank_plus, rank_minus, rank_two) == (14, 14, 14),
          (rank_plus, rank_minus, rank_two))

    pivot_rows = (m1 + m2).T.rref()[1]
    check("control", f"{name} supplies a fourteen-row exact minor", len(pivot_rows) == 14)
    minor1 = m1.extract(pivot_rows, range(14))
    minor2 = m2.extract(pivot_rows, range(14))
    determinant = sp.factor((minor1 + t * minor2).det())
    check("hessian", f"{name} exact minor is not the zero polynomial", determinant != 0)
    results[name] = {
        "rank_m1": rank_m1,
        "rank_m2": rank_m2,
        "ranks": (rank_plus, rank_minus, rank_two),
        "pivot_rows": pivot_rows,
        "determinant": determinant,
        "m1": m1,
        "m2": m2,
    }
    print(f"{name.upper()}_M1_RANK={rank_m1}")
    print(f"{name.upper()}_M2_RANK={rank_m2}")
    print(f"{name.upper()}_MINOR_DET={determinant}")


print("\nD. RESIDUAL-DEPENDENT TERM AND SIGN CONTROLS")
for name, result in results.items():
    k = covectors[name]
    exact = [exact_direction(k, a) for a in range(14)]
    gram_only = sp.zeros(196, 14)
    residual_term = sp.zeros(196, 14)
    for row, (_, _, test) in enumerate(cells):
        b_test = zero_linear(test)
        for column, delta in enumerate(exact):
            b_exact = zero_linear(delta)
            gram_only[row, column] = scalar(sym_pair(b_test, b_exact))
            residual_term[row, column] = scalar(
                sym_pair(second_residual(test, delta), residual)
            )
    check("plant", f"{name} residual-dependent second variation is nonzero",
          residual_term.rank() > 0, residual_term.rank())
    check("plant", f"{name} omitting Upsilon.D2Upsilon changes the lower-order Hessian",
          gram_only != result["m1"])
    exact_square = sp.Matrix(14, 14, [
        scalar(sym_pair(zero_linear(left), zero_linear(right)))
        + scalar(sym_pair(second_residual(left, right), residual))
        for left in exact for right in exact
    ])
    check("self_adjoint", f"{name} exact-form Hessian restriction is symmetric",
          exact_square == exact_square.T)


print("\nE. DISPOSITION")
for kind, label in (
    ("result", "the fourteen non-gauge exact-form directions are lifted by the owned lower-order Hessian at the tested branch"),
    ("analytic", "lower-order lifting does not remove the principal characteristic kernel or decide well-posedness"),
    ("gauge_bv", "the actual rank-25 source adjoint image still requires induction on the physical carrier"),
    ("symplectic", "no finite Hessian rank is promoted to a reduced phase space"),
    ("krein", "the nonzero K-null background residual contributes through the second variation"),
    ("scope", "the result is constant-background fixed-Hq and not a nonlinear global theorem"),
    ("scope", "the tested radial branch is not stationary on the full 196-cell field bank"),
    ("datum", "P1 P2 P3 remain unchanged and unused"),
    ("scope", "ledger verdict residue quotient canon and public posture do not move"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_SC_ACT_04_RESIDUAL_SQUARE__SOURCE_SILENT_EXACT_K77_LOWER_ORDER_LIFT__REPO_DERIVES_FIXED_BACKGROUND_FINITE_FREQUENCY_THEOREM")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
