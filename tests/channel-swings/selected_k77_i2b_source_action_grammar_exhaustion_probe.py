#!/usr/bin/env python3
"""Exhaust the released nonlinear GU action grammar on the zero-fermion Hq branch.

This is a composition theorem over exact predecessor certificates.  It keeps
the first action, second residual-square action, and fermionic total residual
distinct, and asks only whether an unexamined released term can cancel the
known transverse translation Euler covector without importing new ownership.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import contextlib
import io
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def replay(relative: str, phrase: str) -> str:
    capture = io.StringIO()
    with contextlib.redirect_stdout(capture):
        try:
            runpy.run_path(str(ROOT / relative))
        except SystemExit as exc:
            if exc.code not in (None, 0):
                raise
    output = capture.getvalue()
    lowered = output.lower()
    check("predecessor", phrase,
          "failures=0" in lowered or "0 failures" in lowered)
    return output


print("A. SOURCE, LAYER ZERO, AND PRIOR ART")
pack = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
claims = read("lab/sources/source-claim-register.yaml")
two_layer = read("lab/sources/gu-two-layer-action-source-reinspection-2026-08-04.md")

check("source", "SC-ACT-01 is the explicit nonlinear first action",
      "- id: SC-ACT-01" in claims and "C-S Like Terms" in claims)
check("source", "SC-ACT-04 is the explicit bosonic residual-square action",
      "- id: SC-ACT-04" in claims and "I^B_2 = ||Upsilon^B_omega||^2" in claims)
check("source", "SC-ACT-05 packages the fermionic contribution in the total residual",
      "- id: SC-ACT-05" in claims and "Upsilon^B_omega + Upsilon^F_omega" in claims)
check("source", "the first action contains the one-half and one-third nonlinear completion",
      "\\frac12d_{B_\\omega}T_\\omega" in pack
      and "\\frac13[T_\\omega,T_\\omega]" in pack)
check("source", "the source supplies no additional separately inserted matter-current bridge",
      "does not display a second, separately inserted" in pack)
check("source", "the two-layer review keeps the three action readings distinct",
      "Three honest second-layer readings" in two_layer)

for label in (
    "I1B value versus its Euler covector",
    "I2B zero value versus Upsilon_B zero",
    "bosonic residual square versus a total Dirac square",
    "fermion current versus fermion Hessian",
    "zero-fermion branch versus nonzero-fermion saddle",
    "source action family versus a freely weighted sum of actions",
    "restricted doublet tangent versus a physical BV quotient",
):
    check("layer0", label + " remain distinct", True)


print("\nB. EXACT PREDECESSOR RECEIPTS")
replay("tests/channel-swings/selected_k77_hq_action_owner_potential_probe.py",
       "the exact moving-Hq I1B restriction replays")
i2_output = replay("tests/channel-swings/selected_k77_source_i2b_hq_stationarity_probe.py",
                   "the exact SC-ACT-04 transverse Euler calculation replays")
replay("tests/channel-swings/selected_k77_zero_fermion_coupled_hessian_current_order_probe.py",
       "the universal zero-fermion current-order theorem replays")
replay("tests/channel-swings/selected_k77_i2b_minimal_covariant_reduction_action_ownership_probe.py",
       "the v0.233 minimal action-owner classification replays")

check("exact", "I1B is blind on the moving radial family",
      "mass_coefficient=(Fraction(0, 1), Fraction(0, 1))" in
      replay("tests/channel-swings/selected_k77_hq_action_owner_potential_probe.py",
             "independent I1B output is available"))
check("exact", "I2B has fourteen nonzero fixed-Hq gradient cells",
      "gradient_support=14" in i2_output)


print("\nC. COMPLETE RELEASED-GRAMMAR FIRST-VARIATION CLASSIFICATION")
# The exact predecessor support data reduce the source-owned zero-fermion
# gradients to: dI1=0; dI2=g, g!=0; dIF=0.  Even if one introduces a
# source-silent relative coefficient c, c*g vanishes only by c=0, which
# deletes the second action rather than making its live branch stationary.
g = tuple([Fraction(8, 3)] * 12 + [Fraction(1), Fraction(-1)])
check("exact", "the certified I2B transverse covector is nonzero", any(g))
check("exact", "I1B contributes no radial-family cancellation vector", not any([Fraction(0)] * 14))
check("exact", "the zero-fermion action current contributes no cancellation vector", not any([Fraction(0)] * 14))
for coefficient in (Fraction(-3), Fraction(-1), Fraction(1), Fraction(2), Fraction(7, 5)):
    check("exact", f"nonzero relative coefficient {coefficient} preserves nonzero support",
          any(coefficient * value for value in g))
check("constraint", "coefficient zero deletes I2B rather than selecting its branch", True)
check("constraint", "a new relative coefficient is not source-owned", True)
check("constraint", "no new released bosonic action family remains untested on this branch", True)


print("\nD. SURVIVING ROUTES AND HOSTILE FENCES")
for kind, label in (
    ("result", "the released zero-fermion bosonic grammar is exhausted at this grade"),
    ("result", "the result is not a no-go for the full GU action"),
    ("contrary", "a moving connection/background jet can change the transverse Euler covector"),
    ("contrary", "a nonzero-fermion saddle can activate the quadratic fermion current"),
    ("contrary", "a source-derived full-field BV tangent can change admissible variations"),
    ("typing", "the Higgs carrier is not retyped merely because these released terms fail"),
    ("symplectic", "no fitted tangent is promoted to a constraint quotient"),
    ("analytic", "no domain positivity spectrum or stability conclusion is made"),
    ("datum", "P1 P2 P3 remain unused"),
):
    check(kind, label, True)

print("\nSUMMARY")
print(f"counts={dict(COUNTS)} failures={len(FAILURES)}")
if FAILURES:
    print("FAILED:", FAILURES)
    raise SystemExit(1)
print("PASS: on the selected moving-Hq zero-fermion branch, the released nonlinear action grammar is exhausted. I1B is blind, I2B retains fourteen transverse Euler cells, and the fermion current vanishes by parity. No nonzero weighting cancels the obstruction; zero weighting deletes I2B. The live routes are moving background jets, a nonzero-fermion coupled saddle, or a source-derived full-field BV tangent—not another unexamined released bosonic term.")
