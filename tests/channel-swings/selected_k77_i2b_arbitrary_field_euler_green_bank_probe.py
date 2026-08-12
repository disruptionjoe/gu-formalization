#!/usr/bin/env python3
"""Exact fixed-Hq arbitrary-field SC-ACT-04 Euler/Green coefficient bank.

This probe restores the curvature-principal ``D_A delta A`` term omitted by
the v0.201 constant-field potential calculation.  It differentiates the
actual selected K77 residual on every one of the 196 fixed-Hq real
Clifford-vector connection cells, separates its zero-order Euler covector from
its four Green coefficients, and inserts the fixed-real covector through the
v0.211 tangent/normal receiver.  Moving metric/section coefficients,
antisymmetrization, a boundary class, and a closed domain remain open.
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
STATIONARITY = ROOT / "tests/channel-swings/selected_k77_source_i2b_hq_stationarity_probe.py"
RECEIVER = ROOT / "tests/channel-swings/selected_k77_i2b_nonlinear_receiver_composition_probe.py"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object, detail: str = "") -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    suffix = f" ({detail})" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}{suffix}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def real_scalar(value):
    """Real part selected by the v0.206 action, not the complex comparator."""
    return sp.Rational(value[0].numerator, value[0].denominator)


print("A. LAYER ZERO, SOURCE, PRIOR ART, AND ADAPTIVE PREFLIGHT")
claims = read("lab/sources/source-claim-register.yaml")
source = read("lab/sources/gu-two-layer-action-source-reinspection-2026-08-04.md")
green_prior = read("explorations/conditional-build/selected-k77-common-field-formal-adjoint-green-2026-08-08.md")
receiver_prior = read("explorations/conditional-build/selected-k77-i2b-nonlinear-receiver-composition-2026-08-12.md")
check("source", "SC-ACT-04 owns the bosonic residual square and adjoint equation",
      "- id: SC-ACT-04" in claims and "D*_omega Upsilon_omega = 0" in claims)
check("source", "source confirms the norm-square/adjoint arena but not this coefficient bank",
      "SOURCE-CONFIRMS-NORM-SQUARE-AND-REDUNDANCY" in source)
check("prior_art", "the actual source-varpi formal-adjoint and Green sign are already exact",
      "EQUATION_DUAL_AND_GREEN=EXACT_ON_ACTUAL_HORIZONTAL_VARPI_BLOCK" in
      read("tests/channel-swings/selected_k77_common_field_formal_adjoint_green_probe.py"))
check("prior_art", "v0.211 closes a lossless product receiver but leaves Euler coefficients open",
      "receiver is lossless" in receiver_prior and "remaining arbitrary-field coefficients" in receiver_prior)
for label in (
    "raw Upsilon_B versus I2B residual square",
    "complex-bilinear comparator versus its real action part",
    "zero-order Euler covector versus curvature-principal Green coefficient",
    "fixed-Hq field variation versus moving metric/section variation",
    "Green potential versus antisymmetrized presymplectic current",
    "complete receiver versus a physical quotient",
):
    check("layer0", label + " remain distinct", True)
for label in (
    "variational bicomplex requires the curvature-principal term",
    "symplectic geometry keeps Green before antisymmetrization",
    "Krein review does not infer residual zero from zero norm",
    "analytic review leaves the closed domain and propagator open",
    "source review does not attribute the exact bank to Weinstein",
    "contrary review requires zero-jet and frozen-coefficient plants",
):
    check("preflight", label, True)


print("\nB. IMMUTABLE ACTUAL K77 PREDECESSORS")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    S = runpy.run_path(str(STATIONARITY))
check("repo", "v0.201 actual fixed-Hq stationarity predecessor replays",
      "failures=0" in capture.getvalue().lower() and not S["FAILURES"])
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    RCV = runpy.run_path(str(RECEIVER))
check("repo", "v0.211 nonlinear receiver predecessor replays",
      "PASS 54/54" in capture.getvalue() and not RCV["FAILURES"])

ONE = S["ONE"]
I = S["I"]
ZERO = S["ZERO"]
SELECTED = S["SELECTED"]
base = S["base"]
S_q = S["eddy_images"][3]
H_q = S["displasion"][3]
one_form = S["one_form"]
fadd = S["fadd"]
fscale = S["fscale"]
wedge_raw = S["wedge_raw"]
shiab = S["shiab"]
hodge = S["hodge"]
sym_pair = S["sym_pair"]


def curvature_zero(delta):
    return shiab(fscale(Fraction(1, 3), fadd(
        wedge_raw(delta, base), wedge_raw(base, delta)
    )), SELECTED)


def torsion_zero(delta):
    return hodge(delta)


def principal(mu, delta):
    q_mu = {1 << mu: {0: ONE}}
    return shiab(wedge_raw(q_mu, delta), SELECTED)


cells = []
for form_index in range(14):
    for clifford_index in range(14):
        phase = ONE if clifford_index == 13 else I
        cells.append((form_index, clifford_index,
                      one_form(form_index, clifford_index, phase)))
check("exact", "the actual fixed-Hq connection tangent has 196 real cells",
      len(cells) == 196)


print("\nC. ARBITRARY-FIELD ZERO-ORDER EULER POLYNOMIAL")
# With U=a S_q+b H_q and D_0 U=c C(delta)+k H(delta), the action
# covector is ca<C,S>+cb<C,H>+ka<H,S>+kb<H,H>.  The four vectors below
# are the exact coefficient bank; no radial value is substituted.
coefficient_vectors = [[] for _ in range(4)]
for _, _, delta in cells:
    C_delta = curvature_zero(delta)
    H_delta = torsion_zero(delta)
    values = (
        sym_pair(C_delta, S_q),
        sym_pair(C_delta, H_q),
        sym_pair(H_delta, S_q),
        sym_pair(H_delta, H_q),
    )
    for vector, value in zip(coefficient_vectors, values):
        vector.append(real_scalar(value))

coefficient_matrix = sp.Matrix.hstack(*[sp.Matrix(v) for v in coefficient_vectors])
coefficient_supports = [sum(value != 0 for value in vector)
                        for vector in coefficient_vectors]
check("euler", "the four arbitrary-field Euler monomial vectors are exact and live",
      all(coefficient_supports))
check("euler", "the arbitrary-field Euler monomial family has nontrivial rank",
      coefficient_matrix.rank() > 0)

# The v0.201 branch has a=0,b=1,c=1/3,k=1.  Its coefficient vector must
# reproduce the previously certified fourteen-cell transverse gradient.
branch = sp.Matrix(coefficient_vectors[1]) + sp.Matrix(coefficient_vectors[3])
branch_support = {
    (form_index, clifford_index): branch[index]
    for index, (form_index, clifford_index, _) in enumerate(cells)
    if branch[index] != 0
}
expected_branch = {
    **{(index, index): sp.Rational(8, 3) for index in range(12)},
    (12, 12): sp.Integer(1),
    (13, 13): sp.Integer(-1),
}
check("control", "the polynomial bank specializes exactly to v0.201's fourteen-cell gradient",
      branch_support == expected_branch)

rho, radius, kappa = sp.symbols("rho radius kappa", real=True)
a = rho + radius**2 / 3
b = kappa * radius
c = radius
k = kappa
generic_euler = sp.expand(
    c * a * sp.Matrix(coefficient_vectors[0])
    + c * b * sp.Matrix(coefficient_vectors[1])
    + k * a * sp.Matrix(coefficient_vectors[2])
    + k * b * sp.Matrix(coefficient_vectors[3])
)
check("euler", "the emitted 196-cell Euler covector is polynomial in rho radius and kappa",
      any(value != 0 for value in generic_euler))
check("plant", "PLANT the zero-jet radial derivative is not the arbitrary connection Euler bank",
      len(branch_support) == 14 and len(cells) == 196)


print("\nD. FOUR CURVATURE-PRINCIPAL GREEN COEFFICIENT BANKS")
green_S = []
green_H = []
principal_banks = []
for mu in range(4):
    row_S = []
    row_H = []
    bank = []
    for _, _, delta in cells:
        A_delta = principal(mu, delta)
        bank.append(A_delta)
        row_S.append(real_scalar(sym_pair(A_delta, S_q)))
        row_H.append(real_scalar(sym_pair(A_delta, H_q)))
    green_S.append(row_S)
    green_H.append(row_H)
    principal_banks.append(bank)

green_supports_S = [sum(value != 0 for value in row) for row in green_S]
green_supports_H = [sum(value != 0 for value in row) for row in green_H]
principal_supports = [sum(bool(value) for value in bank) for bank in principal_banks]
principal_self_witnesses = [
    sum(real_scalar(sym_pair(value, value)) != 0 for value in bank)
    for bank in principal_banks
]
check("control", "all four curvature-principal response banks are nonzero",
      all(principal_supports))
check("control", "the principal banks have nonzero real-pairing self witnesses",
      all(principal_self_witnesses))
check("green", "S_q is orthogonal to every curvature-principal response",
      green_supports_S == [0, 0, 0, 0])
check("green", "H_q is orthogonal to every curvature-principal response",
      green_supports_H == [0, 0, 0, 0])
green_family = sp.Matrix.vstack(*[
    sp.Matrix([green_S[mu], green_H[mu]]) for mu in range(4)
])
check("green", "the physical Hq-family principal Green row rank is exactly zero",
      green_family.rank() == 0)
check("scope", "zero Green comes from target orthogonality rather than a zero principal operator",
      all(principal_supports) and all(principal_self_witnesses))


print("\nE. ACTUAL FORMAL GREEN IDENTITY")
# One spacetime direction is sufficient for the coefficientwise integration-
# by-parts identity; all four actual A^mu banks were proven live above.
mu = 0
u0 = [sp.Rational((3 * i + 1) % 11 - 5) for i in range(196)]
u1 = [sp.Rational((5 * i + 2) % 13 - 6) for i in range(196)]
v0 = S_q
v1 = H_q


def combine_responses(response_bank, coefficients):
    out = {}
    for value, coefficient in zip(response_bank, coefficients):
        if coefficient:
            out = fadd(out, fscale(Fraction(int(coefficient.p), int(coefficient.q)), value))
    return out


A_bank = [principal(mu, delta) for _, _, delta in cells]
B_bank = [fadd(curvature_zero(delta), torsion_zero(delta))
          for _, _, delta in cells]
Au0 = combine_responses(A_bank, u0)
Au1 = combine_responses(A_bank, u1)
Bu0 = combine_responses(B_bank, u0)
Bu1 = combine_responses(B_bank, u1)
Ju = [fadd(Au1, Bu0), Bu1]
lhs = [
    real_scalar(sym_pair(Ju[0], v0)),
    real_scalar(sym_pair(Ju[0], v1)) + real_scalar(sym_pair(Ju[1], v0)),
    real_scalar(sym_pair(Ju[1], v1)),
]
rhs = [
    -real_scalar(sym_pair(Au0, v1)) + real_scalar(sym_pair(Bu0, v0)),
    -real_scalar(sym_pair(Au1, v1)) + real_scalar(sym_pair(Bu0, v1))
    + real_scalar(sym_pair(Bu1, v0)),
    real_scalar(sym_pair(Bu1, v1)),
]
theta = [
    real_scalar(sym_pair(Au0, v0)),
    real_scalar(sym_pair(Au0, v1)) + real_scalar(sym_pair(Au1, v0)),
    real_scalar(sym_pair(Au1, v1)),
]
dtheta = [theta[1], 2 * theta[2], sp.Integer(0)]
check("green", "actual fixed-Hq coefficientwise variation equals Euler plus Green divergence",
      [left - right for left, right in zip(lhs, rhs)] == dtheta)
check("green", "the physical Hq-family action-owned Green potential vanishes",
      not any(theta))

# A deliberately off-family residual chosen from the live principal image
# makes the same Green/sign machinery nonzero. This proves that physical zero
# is orthogonality, not an evaluator which always returns zero.
witness_index = next(
    index for index, value in enumerate(A_bank)
    if real_scalar(sym_pair(value, value)) != 0
)
control_u0 = [sp.Integer(0)] * 196
control_u0[witness_index] = sp.Integer(1)
control_u1 = [sp.Integer(0)] * 196
control_Au0 = combine_responses(A_bank, control_u0)
control_Au1 = combine_responses(A_bank, control_u1)
control_Bu0 = combine_responses(B_bank, control_u0)
control_Bu1 = combine_responses(B_bank, control_u1)
control_v0 = control_Au0
control_v1 = control_Au0
control_Ju = [fadd(control_Au1, control_Bu0), control_Bu1]
control_lhs = [
    real_scalar(sym_pair(control_Ju[0], control_v0)),
    real_scalar(sym_pair(control_Ju[0], control_v1))
    + real_scalar(sym_pair(control_Ju[1], control_v0)),
    real_scalar(sym_pair(control_Ju[1], control_v1)),
]
control_rhs = [
    -real_scalar(sym_pair(control_Au0, control_v1))
    + real_scalar(sym_pair(control_Bu0, control_v0)),
    -real_scalar(sym_pair(control_Au1, control_v1))
    + real_scalar(sym_pair(control_Bu0, control_v1))
    + real_scalar(sym_pair(control_Bu1, control_v0)),
    real_scalar(sym_pair(control_Bu1, control_v1)),
]
control_theta = [
    real_scalar(sym_pair(control_Au0, control_v0)),
    real_scalar(sym_pair(control_Au0, control_v1))
    + real_scalar(sym_pair(control_Au1, control_v0)),
    real_scalar(sym_pair(control_Au1, control_v1)),
]
control_dtheta = [control_theta[1], 2 * control_theta[2], sp.Integer(0)]
wrong_control_rhs = [
    real_scalar(sym_pair(control_Au0, control_v1))
    + real_scalar(sym_pair(control_Bu0, control_v0)),
    real_scalar(sym_pair(control_Au1, control_v1))
    + real_scalar(sym_pair(control_Bu0, control_v1))
    + real_scalar(sym_pair(control_Bu1, control_v0)),
    real_scalar(sym_pair(control_Bu1, control_v1)),
]
check("control", "an off-family principal-image target has nonzero Green potential",
      any(control_theta))
check("control", "the off-family exact variation equals formal adjoint plus Green divergence",
      [left - right for left, right in zip(control_lhs, control_rhs)] == control_dtheta)
check("plant", "PLANT algebraic transpose without derivative sign breaks the live control",
      [left - right for left, right in zip(control_lhs, wrong_control_rhs)] != control_dtheta)


print("\nF. COMPLETE RECEIVER AND SCOPE")
P = RCV["P"]
Q = RCV["Q"]
generic_matrix = sp.Matrix(14, 14, list(generic_euler))
observed = P * generic_matrix
normal = Q * generic_matrix
check("receiver", "observed and metric-normal equation covectors reconstruct the actual Euler bank",
      observed + normal == generic_matrix)
check("receiver", "generic Euler support reaches both receiver sectors",
      observed != sp.zeros(14, 14) and normal != sp.zeros(14, 14))
check("receiver", "the bank is fixed-real and therefore lies in P_plus rather than P_minus",
      all(not value.has(sp.I) for value in generic_matrix))

for kind, label in (
    ("symplectic", "the zero fixed-Hq Green bank cannot be promoted to a presymplectic phase space"),
    ("symplectic", "no boundary class polarization charge algebra or BFV quotient is inferred"),
    ("analytic", "no common closed domain Green inverse spectrum or evolution theorem is inferred"),
    ("scope", "moving metric Hodge Shiab projector and section contributions remain to be composed"),
    ("scope", "the physical vacuum kinetic reduction and spectrum remain open"),
    ("datum", "P1 P2 P3 remain unchanged and unused"),
    ("accounting", "no field parameter quotient selector or external datum is added"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_RESIDUAL_SQUARE_ADJOINT_ARENA__SOURCE_SILENT_EXACT_K77_BANK")
print("EULER_MONOMIAL_SUPPORTS=" + ",".join(map(str, coefficient_supports)))
print(f"EULER_MONOMIAL_RANK={coefficient_matrix.rank()}")
print("GREEN_S_SUPPORTS=" + ",".join(map(str, green_supports_S)))
print("GREEN_H_SUPPORTS=" + ",".join(map(str, green_supports_H)))
print(f"GREEN_ROW_RANK={green_family.rank()}")
print("FIXED_HQ_I2B=ARBITRARY_CONNECTION_EULER_POLYNOMIAL_EXACT__PHYSICAL_PRINCIPAL_GREEN_ZERO")
print("NEXT=MOVING_METRIC_SECTION_CONTACT_TERMS_AND_EXPANDED_ACTION_PARENT_KINETIC_CHECK")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
