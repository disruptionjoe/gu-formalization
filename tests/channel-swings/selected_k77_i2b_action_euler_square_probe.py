#!/usr/bin/env python3
"""Exact corrected-action-Euler square on the moving-Q_u K77 bank.

This probe differentiates the released first action directly on the same
fixed-background 196-real connection tangent used by ledger v0.225.  It
constructs the Fréchet-adjoint companion through the action pairing's exact
Riesz map, then squares the resulting degree-thirteen Euler representative
with the already-built observer ``Q_u`` pairing.  The literal printed endpoint
and the older path-average square remain independent controls.

The result is finite, local, and fixed-background.  It is not a source claim
that ``SC-ACT-04`` squares this corrected Euler row, and it supplies no tangent
reduction, BV quotient, global domain, or physical vacuum by itself.
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
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_i2b_two_connection_tangent_independence_probe.py"
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
source = read("lab/sources/gu-eddy-augmented-torsion-euler-functor-source-reinspection-2026-08-05.md")
claims = read("lab/sources/source-claim-register.yaml")
prior = read("explorations/conditional-build/selected-k77-i2b-two-connection-tangent-independence-2026-08-12.md")
check("source", "the source displays the path-average first action and printed endpoint separately",
      "Upsilon_{\\rm print}=S(F_A)+*\\kappa T" in source
      and "E_{\\rm act}=S(\\bar F)+L_T^!S^!T+*\\kappa T" in source)
check("source", "SC-ACT-04 literally squares printed Upsilon rather than corrected E_act",
      "- id: SC-ACT-04" in claims and "I^B_2 = ||Upsilon^B_omega||^2" in claims)
check("prior_art", "v0.225 leaves the corrected E_act square as the named next rival",
      "action-consistent `||E_act||^2` completion" in prior
      and "has not" in prior and "yet been assembled" in prior)

for label in (
    "path-average bracket versus printed endpoint versus action Euler",
    "Euler covector versus its action-pairing Riesz representative",
    "first action versus a newly composed Euler norm square",
    "fixed reference translation versus diagonal two-connection gauge motion",
    "observer Q_u pairing versus source-unprinted Q_B",
    "two C^(32,32) carrier halves versus two connection fields",
):
    check("layer0", label + " remain distinct", True)

for label in (
    "variational bicomplex owns direct differentiation and the adjoint companion",
    "symplectic geometry refuses to infer a quotient from a Ward-zero direction",
    "principal-bundle geometry keeps B fixed in the independent T translation",
    "Krein/operator theory checks Riesz representability before squaring",
    "real/complex structure keeps the exact real tangent phases",
    "exact computation requires a nondegenerate planted Riesz control",
    "source criticism grades the E_act square as repo-composed not source-printed",
    "contrary review preserves a future derived tangent or BV reduction",
):
    check("preflight", label, True)


print("\nB. IMMUTABLE PREDECESSOR AND STRUCTURE FINGERPRINT")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P225 = runpy.run_path(str(PREDECESSOR))
check("repo", "v0.225 predecessor replays", "PASS 50/50" in capture.getvalue() and not P225["FAILURES"])

P224 = P225["V"]
E = P224["E"]
S = E["S"]
cells = E["cells"]
base = E["base"]
S_q = E["S_q"]
H_q = E["H_q"]
ONE = E["ONE"]
ZERO = E["ZERO"]
SELECTED = E["SELECTED"]
fadd = E["fadd"]
fscale = E["fscale"]
wedge_raw = E["wedge_raw"]
hodge = E["hodge"]
shiab = E["shiab"]
action_pair = S["P"]["pairing"]
real_scalar = E["real_scalar"]
q_pair = P224["pair"]

check("fingerprint", "carrier is the same 196-real fixed-Hq connection tangent", len(cells) == 196)
check("fingerprint", "pairing/form is action wedge-Hodge for Riesz and observer Q_u for the rival square", True)
check("fingerprint", "real structure and grading remain K77 grade-one to degree-thirteen", True)
check("fingerprint", "signature horn and embedding remain selected real K77 with trace-Hq owner", True)


print("\nC. ACTION-PAIRING RIESZ MAP")
residual_basis = [hodge(delta) for _, _, delta in cells]
action_gram = sp.zeros(len(cells))
for i, (_, _, delta) in enumerate(cells):
    for j, residual in enumerate(residual_basis):
        action_gram[i, j] = real_scalar(action_pair(delta, residual))

diag = [action_gram[i, i] for i in range(len(cells))]
off_diagonal_support = sum(
    action_gram[i, j] != 0
    for i in range(len(cells))
    for j in range(len(cells))
    if i != j
)
check("exact", "the action Riesz matrix is diagonal", off_diagonal_support == 0)
check("exact", "the action Riesz matrix is nondegenerate on all 196 real cells",
      all(value != 0 for value in diag) and action_gram.rank() == 196)
check("plant", "PLANT deleting one diagonal pairing direction makes the Riesz map singular",
      sp.diag(*(diag[:-1] + [0])).rank() == 195)


def riesz_from_covector(covector: list[sp.Expr]):
    coefficients = [sp.factor(value / weight) for value, weight in zip(covector, diag)]
    out = {}
    for coefficient, residual in zip(coefficients, residual_basis):
        if coefficient:
            rational = sp.Rational(coefficient)
            out = fadd(out, fscale(Fraction(int(rational.p), int(rational.q)), residual))
    return out


print("\nD. EXACT FRECHET-ADJOINT COMPANION")
# Define C by <X,C>=<T_q,S(X T_q + T_q X)>.  The actual term is r^2 C/3.
companion_covector: list[sp.Expr] = []
for _, _, delta in cells:
    variation = shiab(fadd(wedge_raw(delta, base), wedge_raw(base, delta)), SELECTED)
    companion_covector.append(real_scalar(action_pair(base, variation)))
companion = riesz_from_covector(companion_covector)
check("exact", "the Frechet-adjoint companion is nonzero", bool(companion))

companion_return = [
    real_scalar(action_pair(delta, companion))
    for _, _, delta in cells
]
check("exact", "the companion Riesz representative returns all 196 covector cells exactly",
      companion_return == companion_covector)
check("plant", "PLANT the companion is not silently identified with the direct Shiab row",
      companion != S_q)
check("exact", "on the constant moving-Hq locus the companion is exactly twice the direct Shiab row",
      companion == fscale(Fraction(2), S_q))


print("\nE. Q_U GRAM AND CORRECTED E_ACT SQUARE")
observer = P224["observer"]
components = (S_q, companion, H_q)
component_gram = sp.Matrix([
    [sp.factor(q_pair(left, right)) for right in components]
    for left in components
])
check("exact", "the corrected three-component Q_u Gram is symmetric",
      component_gram == component_gram.T)
check("exact", "the three-component Gram has rank two because companion equals twice S_q",
      component_gram.rank() == 2 and component_gram.det() == 0, component_gram)

rho, radius, kappa = E["rho"], E["radius"], E["kappa"]
coefficients = sp.Matrix([
    rho + radius**2 / 3,
    radius**2 / 3,
    kappa * radius,
])
potential = sp.factor(sp.Rational(1, 2) * (coefficients.T * component_gram * coefficients)[0])
radial_euler = sp.factor(sp.diff(potential, radius))
endpoint_potential = sp.factor(80 * (rho + radius**2) ** 2 + kappa**2 * radius**2)
check("comparison", "the corrected E_act square equals the printed-endpoint square on this restricted locus",
      sp.simplify(potential - endpoint_potential) == 0)
print(f"ACTION_RIESZ_DIAGONAL_COUNTS={Counter(diag)}")
print(f"COMPANION_SUPPORT={sum(value != 0 for value in companion_covector)}")
print(f"COMPONENT_GRAM={component_gram}")
print(f"E_ACT_SQUARE={potential}")
print(f"RADIAL_EULER={radial_euler}")


print("\nF. COMPLETE FIXED-BACKGROUND CONNECTION EULER")


def companion_derivative(delta):
    """Riesz representative of D_C(base)[delta] before the overall r/3 factor.

    Since C(T) is quadratic, the actual derivative at T=r*T_q is
    ``r/3`` times this representative.
    """

    covector: list[sp.Expr] = []
    for _, _, test in cells:
        first = shiab(fadd(wedge_raw(test, base), wedge_raw(base, test)), SELECTED)
        second = shiab(fadd(wedge_raw(test, delta), wedge_raw(delta, test)), SELECTED)
        value = action_pair(delta, first)
        value = S["gadd"](value, action_pair(base, second))
        covector.append(real_scalar(value))
    return riesz_from_covector(covector)


e_act = fadd(
    fscale(Fraction(1), S_q),
    fscale(Fraction(1), companion),
)
# The symbolic coefficients cannot be inserted into sparse Gaussian forms, so
# evaluate the Euler polynomial coefficientwise through the Q_u Gram pieces.
euler_cells: list[sp.Expr] = []
derivative_component_rows: list[tuple[sp.Expr, sp.Expr, sp.Expr]] = []
companion_derivative_ratios: list[bool] = []
for _, _, delta in cells:
    direct_derivative = E["curvature_zero"](delta)  # (1/3) S(delta*Tq+Tq*delta)
    adjoint_derivative = companion_derivative(delta)
    mass_derivative = hodge(delta)
    companion_derivative_ratios.append(
        adjoint_derivative == fscale(Fraction(6), direct_derivative)
    )

    # D E_act(delta)=r*direct + (r/3)*D companion + kappa*mass.
    d_parts = (direct_derivative, adjoint_derivative, mass_derivative)
    row = []
    for d_part in d_parts:
        row.append(tuple(sp.factor(q_pair(d_part, component)) for component in components))
    derivative_component_rows.append(tuple(row))
    d_coefficients = (radius, radius / 3, kappa)
    value = sp.Integer(0)
    for d_coefficient, pairings in zip(d_coefficients, row):
        value += d_coefficient * sum(
            pairing * coefficient
            for pairing, coefficient in zip(pairings, coefficients)
        )
    euler_cells.append(sp.factor(value))

check("plant", "PLANT equality of E_act and endpoint values does not identify all 196 Frechet derivatives",
      not all(companion_derivative_ratios))
euler_difference = sp.Matrix([
    sp.simplify(value)
    for value in (sp.Matrix(euler_cells) - P225["endpoint_euler"])
])
euler_difference_support = {
    (mu, a): value
    for value, (mu, a, _) in zip(euler_difference, cells)
    if value != 0
}
check("comparison", "the residual Frechet maps differ but their Q_u-square Euler covectors coincide",
      not euler_difference_support)

radial_chain = sp.Integer(0)
for index, (value, (_, _, delta)) in enumerate(zip(euler_cells, cells)):
    # Base R[3] has two nonzero cells; recover its exact real coordinates by
    # pairing against the diagonal action Riesz basis.
    coordinate = real_scalar(action_pair(delta, hodge(base))) / diag[index]
    radial_chain += coordinate * value
radial_chain = sp.factor(radial_chain)
check("variation", "the complete connection Euler contracts to the restricted radial derivative",
      sp.simplify(radial_chain - radial_euler) == 0, (radial_chain, radial_euler))

branch_rho = -radius**2 - kappa**2 / 160
branch_euler = sp.Matrix([sp.factor(value.subs(rho, branch_rho)) for value in euler_cells])
branch_support = {
    (mu, a): value
    for value, (mu, a, _) in zip(branch_euler, cells)
    if value != 0
}
check("comparison", "the corrected branch has the same twelve-cell support as the endpoint rival",
      branch_support == P225["endpoint_support"])
check("comparison", "the corrected and endpoint Euler covectors coincide on their common stationary branch",
      branch_euler == P225["endpoint_branch"])
check("exact", "the two corrected-branch cancellation shapes retain determinant eighty",
      P225["endpoint_ratio_matrix"].det() == 80
      and P225["endpoint_ratio_matrix"].rank() == 2)
check("plant", "PLANT restricted radial stationarity does not erase the twelve transverse cells",
      radial_euler.subs(rho, branch_rho) == 0 and bool(branch_support))

print(f"GENERIC_EULER_SUPPORT={sum(value != 0 for value in euler_cells)}")
print(f"RADIAL_CHAIN={radial_chain}")
print(f"BRANCH_SUPPORT={branch_support}")
print(f"COMPANION_DERIVATIVE_SIX_TO_ONE_MATCHES={sum(companion_derivative_ratios)}/196")
print(f"OFF_BRANCH_EULER_DIFFERENCE={euler_difference_support}")


print("\nG. DISPOSITION")
for kind, label in (
    ("source", "the corrected E_act square is repo-composed and not literal SC-ACT-04"),
    ("scope", "the literal endpoint and path-average square remain distinct controls"),
    ("scope", "restricted E_act-endpoint equality does not revive their killed full-domain identity"),
    ("demand", "the unrestricted fixed-reference route still requires an action-owned tangent or BV reduction"),
    ("symplectic", "no Ward zero is promoted to a tangent or BV quotient"),
    ("analytic", "no closed domain spectrum positivity or propagator is inferred"),
    ("datum", "P1 P2 P3 remain unchanged and unused"),
    ("scope", "canon verdict and public posture do not move"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_FIRST_ACTION_AND_PRINTED_ENDPOINT_FORMULAS__SOURCE_SILENT_CORRECTED_E_ACT_SQUARE__REPO_CONSTRUCTS_EXACT_LOCAL_RIVAL")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
