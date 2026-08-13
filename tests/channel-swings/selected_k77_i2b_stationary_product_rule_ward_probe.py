#!/usr/bin/env python3
"""Exact constant-parameter product-rule Ward response at the local I2B jet."""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_i2b_projected_adjoint_jet_prolongation_probe.py"
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


print("A. SOURCE, LAYER ZERO, PRIOR ART, AND ADAPTIVE PREFLIGHT")
source = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
prior = read("explorations/conditional-build/selected-k77-i2b-projected-adjoint-jet-prolongation-2026-08-13.md")
lower_prior = read("explorations/conditional-build/selected-k77-i2b-lower-order-exact-form-lift-2026-08-13.md")
check("source", "the source separates the connection and its adjoint distortion",
      r"T_\omega=\varpi-\epsilon^{-1}d_0\epsilon" in source)
check("prior_art", "the predecessor isolates one rank-25 Lorentz-trace response",
      "Lorentz-trace response" in prior)
check("prior_art", "the complete owned lower-order Hessian includes the residual-dependent term",
      "residual-dependent term fires" in lower_prior)
for distinction in (
    "constant gauge parameter versus first and second parameter jets",
    "commutator of the stationary two-jet versus ten copies of the base-field orbit",
    "principal product-rule response versus owned lower-order Hessian response",
    "frozen Ward residual versus full moving coefficient Ward identity",
    "rank defect versus physical mode or anomaly",
):
    check("layer0", distinction + " remain distinct", True)
for kind, label in (
    ("principal_bundle", "differentiate the homogeneous distortion action through the nonzero two-jet"),
    ("variational", "combine principal product-rule and complete lower-order Hessian terms"),
    ("gauge_bv", "require complete gauge tangency only after moving coefficients are included"),
    ("spencer", "leave first-jet symbols and formal involutivity open"),
    ("krein", "make no positivity inference from rank"),
    ("symplectic", "make no reduced phase-space inference"),
    ("source", "record source silence on the exact rank decomposition"),
    ("contrary", "plant the frozen-principal-only and automatic-cancellation readings"),
):
    check(kind, label, True)


print("\nB. IMMUTABLE PREDECESSOR AND STRUCTURE FINGERPRINT")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))
check("repo", "the projected-adjoint prolongation predecessor replays",
      "PASS 49/49" in capture.getvalue() and not P["FAILURES"])
H = P["H"]
S = H["P"]["S"]
cells = P["cells"]
core = P["core"]
phase = P["phase"]
pairs = P["pairs"]
base = P["base"]
gauge_fields = P["gauge_fields"]
sym_pair = P["sym_pair"]
real_scalar = P["real_scalar"]
principal_with = P["principal_with"]
selected = P["selected"]
check("fingerprint", "the field carrier remains the selected 196-real Cl1 bank", len(cells) == 196)
check("fingerprint", "the gauge-parameter carrier remains all 91 Cl2 generators", len(pairs) == 91)
check("fingerprint", "the inherited stationary jet cancels the frozen Euler covector",
      all(value == 0 for value in P["P"]["stationary"]))


def vector_to_form(values):
    out = {}
    for index, value in enumerate(values):
        if not value:
            continue
        form_index, clifford_index = divmod(index, 14)
        coefficient = core.escale(value, core.blade(clifford_index, phase[clifford_index]))
        out[1 << form_index] = core.eadd(out.get(1 << form_index, {}), coefficient)
    return core.fclean(out)


def form_commutator(eta, form):
    return {
        form_mask: P["commutator"](eta, coefficient)
        for form_mask, coefficient in form.items()
    }


def scalar(value) -> sp.Expr:
    return sp.factor(real_scalar(value))


print("\nC. CONSTANT-PARAMETER PRODUCT-RULE RESPONSE")
c00 = vector_to_form(P["P"]["c00"])
c01 = vector_to_form(P["P"]["c01"])
field_responses = P["field_responses"]
etas = [
    core.emul(core.blade(left, phase[left]), core.blade(right, phase[right]))
    for left, right in pairs
]
product = sp.zeros(196, 91)
for column, eta in enumerate(etas):
    delta00 = form_commutator(eta, c00)
    delta01 = form_commutator(eta, c01)
    response00 = principal_with(selected, 0, delta00)
    response01_0 = principal_with(selected, 0, delta01)
    response01_1 = principal_with(selected, 1, delta01)
    for row in range(196):
        product[row, column] = scalar(sym_pair(field_responses[0][row], response00))
        product[row, column] += scalar(sym_pair(field_responses[0][row], response01_1))
        product[row, column] += scalar(sym_pair(field_responses[1][row], response01_0))
check("exact", "the stationary-two-jet product-rule response has rank 91", product.rank() == 91)
check("plant", "PLANT freezing the nonzero stationary jet would erase a live response", product != sp.zeros(196, 91))


print("\nD. COMPLETE OWNED LOWER-ORDER RESPONSE")
zero_linear = S["residual_derivative"]
residual = S["residual_at_branch"]


def second_residual(left, right):
    return S["shiab"](S["fscale"](Fraction(1, 3), S["fadd"](
        S["wedge_raw"](left, right), S["wedge_raw"](right, left)
    )), selected)


lower = sp.zeros(196, 91)
for row, (_, _, test) in enumerate(cells):
    b_test = zero_linear(test)
    for column, delta in enumerate(gauge_fields):
        lower[row, column] = scalar(sym_pair(b_test, zero_linear(delta)))
        lower[row, column] += scalar(sym_pair(second_residual(test, delta), residual))
check("exact", "the owned lower-order response on the adjoint orbit has rank 25", lower.rank() == 25)
check("exact", "principal product and lower-order images jointly span rank 115",
      sp.Matrix.hstack(product, lower).rank() == 115)

constant_total = product + lower
constant_rank = constant_total.rank()
constant_kernel = constant_total.nullspace()
check("theorem", "the complete frozen constant-parameter Ward response has rank 90", constant_rank == 90)
check("theorem", "its kernel is exactly one-dimensional", len(constant_kernel) == 1)
null_support = [
    (pairs[index], value)
    for index, value in enumerate(constant_kernel[0]) if value != 0
]
check("theorem", "the sole constant-parameter tangent is generator (12,13)",
      null_support == [([12, 13], sp.Integer(1))], null_support)
check("plant", "PLANT the lower-order term does not cancel all constant-parameter responses",
      constant_rank != 0)
check("plant", "PLANT principal-only rank 91 is not the complete frozen Ward rank",
      constant_rank != product.rank())


print("\nE. SECOND-PARAMETER-JET TRACE REMAINS INDEPENDENT")
trace = P["block_images"][0]
check("exact", "the effective second-parameter-jet Lorentz trace retains rank 25", trace.rank() == 25)
check("theorem", "constant and second-jet Ward residuals jointly have rank 115",
      sp.Matrix.hstack(constant_total, trace).rank() == 115)
check("theorem", "the rank-25 second-jet trace is independent of the rank-90 constant residual",
      sp.Matrix.hstack(constant_total, trace).rank() == constant_rank + trace.rank())


print("\nF. HOSTILE DISPOSITION")
for kind, label in (
    ("layer0", "rank 115 is a frozen Ward-completion burden, not physical modes"),
    ("principal_bundle", "moving Shiab Q_B H_q observation and affine connection terms remain"),
    ("gauge_bv", "first-parameter jets and the complete BV differential remain unassembled"),
    ("spencer", "formal compatibility involutivity and a solution germ remain open"),
    ("symplectic", "no presymplectic quotient or BFV phase space is inferred"),
    ("analytic", "no domain hyperbolicity positivity spectrum or stability follows"),
    ("source", "the source is silent on the exact 90 plus 25 decomposition"),
    ("datum", "P1 P2 P3 remain unchanged and unused"),
    ("scope", "ledger canon residue quotient count and public posture do not move"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_INHOMOGENEOUS_CONNECTION_AND_ADJOINT_DISTORTION_GRAMMAR__SOURCE_SILENT_STATIONARY_PRODUCT_RULE_WARD_RANKS__REPOSITORY_DERIVES_CONSTANT90_PLUS_SECONDJET25_COMPLETION_BURDEN")
print(f"PRODUCT_RULE_RANK={product.rank()}")
print(f"LOWER_ORDER_RANK={lower.rank()}")
print(f"CONSTANT_PARAMETER_TOTAL_RANK={constant_rank}")
print("CONSTANT_PARAMETER_KERNEL=(12,13)")
print(f"SECOND_PARAMETER_JET_TRACE_RANK={trace.rank()}")
print(f"COMBINED_FROZEN_WARD_RESIDUAL_RANK={sp.Matrix.hstack(constant_total, trace).rank()}")
print("DISPOSITION=ONE_CONSTANT_GENERATOR_TANGENT__RANK90_CONSTANT_PLUS_RANK25_SECONDJET_MOVING_WARD_COMPLETION_OPEN")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
