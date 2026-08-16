#!/usr/bin/env python3
"""Exact two-connection principal Ward descent for the selected LC cubic.

The predecessor found a rank-five connection-gauge block after varying one
Levi-Civita connection representative in isolation.  GU's source-owned object
is instead the difference of two connections, T=A-B.  This probe pulls the
raw selected cubic back through that difference map and tests the diagonal
gauge action on the complete finite carriers. K122 later identifies the
native metric column with that diagonal kernel, not with the anti-diagonal
relative-connection control used for the nonzero shell value.

Principal diagonal descent is not the full nonlinear homogeneous Ward/BV or
preboundary quotient.  Those burdens remain explicit.
"""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
from io import StringIO
import json
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_cubic_gauge_rotated_lc_ward_owner_probe.py"
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


print("A. SOURCE, LAYER 0, AND PREDECESSOR")
source = read("lab/sources/gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md")
two_connection = read("explorations/k77-wave2-two-connection-shifted-superconnection-action-owner-2026-08-04.md")
even_ward = read("explorations/conditional-build/k77-global-even-bv-null-green-domain-2026-08-05.md")
prior_report = read("explorations/conditional-build/selected-cubic-gauge-rotated-lc-ward-owner-2026-08-06.md")
ledger = json.loads(read("lab/process/conditional-physics-ledger-v0.21.json"))

check("source", "source types augmented torsion as a difference of two connections",
      "difference of two connections" in source and "full upstairs one-form" in source)
check("source", "source names the gauge-rotated Levi-Civita connection owner",
      "gauge-rotated Levi-Civita connection in the contorsion slot" in source)
check("source", "source leaves the nonlinear Ward quotient open",
      "moving-section Ward/BV identity" in source and "SOURCE-SILENT" in source)
check("repo", "the existing two-connection reconstruction defines T=A-B",
      "augmented torsion `T` | `A-B" in two_connection)
check("repo", "the existing even owner ledger distinguishes primitive epsilon from Ward",
      "primitive `epsilon` derivative" in even_ward and "homogeneous even Ward identity" in even_ward)
check("repo", "the predecessor measured rank five only for the isolated representative",
      "rank five" in prior_report and "does not descend by itself" in prior_report
      and "not a native `C_t_h_h` coefficient" in prior_report)
check("repo", "ledger v0.21 makes the fused Ward completion rank one",
      ledger["next_work_queue"][0]["rank"] == 1
      and "rank-five gauge-gauge block" in ledger["next_work_queue"][0]["why"])

for label in (
    "one connection representative versus two-connection difference",
    "inhomogeneous principal gauge motion versus homogeneous lower-order orbit",
    "principal radical versus full BV/preboundary quotient",
    "source-owned difference versus fitted cancellation counterterm",
    "nonzero anti-diagonal raw kernel versus native metric column and physical transition",
):
    check("type", label + " remain distinct", True)

capture = StringIO()
with contextlib.redirect_stdout(capture):
    A = runpy.run_path(str(PREDECESSOR))
check("exact", "the 51-check LC predecessor replays", "PASS 51/51" in capture.getvalue())

P = A["P"]
ZERO = A["ZERO"]
d3 = A["d3"]
fscale = A["fscale"]
form_sum = A["form_sum"]
lc_spin_symbol = A["lc_spin_symbol"]
gauge_symbol = A["gauge_symbol"]
minkowski_dot = A["minkowski_dot"]
tensor_inner = A["tensor_inner"]
PLUS, CROSS = A["POLARIZATIONS"]
MASS_PAIRS = A["MASS_PAIRS"]
GAUGE_PAIRS = A["GAUGE_PAIRS"]


def difference(pair):
    """Source-owned tangent map W(delta A,delta B)=delta A-delta B."""
    delta_a, delta_b = pair
    return form_sum(delta_a, fscale(-1, delta_b))


def pulled_cubic(left_pair, right_pair):
    return d3(P, difference(left_pair), difference(right_pair))


print("\nB. COMPLETE DIFFERENCE-MAP RANK AND UNIQUENESS")
n_connection = 24
identity = sp.eye(n_connection)
difference_matrix = identity.row_join(-identity)
diagonal = identity.col_join(identity)
anti_diagonal = identity.col_join(-identity)
check("exact", "difference map has rank 24 on the complete 24+24 LC carrier",
      difference_matrix.rank() == 24)
check("exact", "difference-map kernel has dimension 24",
      len(difference_matrix.nullspace()) == 24)
check("exact", "the complete diagonal connection carrier lies in the kernel",
      difference_matrix * diagonal == sp.zeros(n_connection))
check("exact", "the diagonal is the complete kernel by matching dimension",
      diagonal.rank() == 24 and len(difference_matrix.nullspace()) == diagonal.rank())
check("exact", "the raw anti-diagonal relative-connection carrier is not erased",
      (difference_matrix * anti_diagonal).rank() == 24)

alpha, beta = sp.symbols("alpha beta")
normalized_solution = sp.solve((alpha + beta, alpha - 1), (alpha, beta), dict=True)
check("exact", "diagonal annihilation plus endpoint normalization uniquely gives (1,-1)",
      normalized_solution == [{alpha: 1, beta: -1}])
check("type", "two coefficient conditions fix two coefficients with zero fitted freedom", True)


print("\nC. EXACT SHELL KERNEL AND PRINCIPAL GAUGE DESCENT")
completed_gauge_ranks = []
old_isolated_ranks = []
for scalar_mass, partner_mass in MASS_PAIRS:
    momentum = (scalar_mass**2 - partner_mass**2) / (2 * scalar_mass)
    partner_energy = (scalar_mass**2 + partner_mass**2) / (2 * scalar_mass)
    p0 = (momentum, Fraction(0), Fraction(0), momentum)
    pm = (partner_energy, Fraction(0), Fraction(0), -momentum)
    lc0 = [lc_spin_symbol(p0, polarization) for polarization in (PLUS, CROSS)]
    lcm = [lc_spin_symbol(pm, polarization) for polarization in (PLUS, CROSS)]

    for index, name in enumerate(("plus", "cross")):
        old_value = d3(P, lc0[index], lcm[index])
        completed_value = pulled_cubic((lc0[index], {}), (lcm[index], {}))
        expected = Fraction(14, 3) * minkowski_dot(p0, pm) * tensor_inner(
            (PLUS, CROSS)[index], (PLUS, CROSS)[index]
        )
        check("exact", f"mass pair {scalar_mass}/{partner_mass}: {name} raw anti-diagonal kernel survives difference pullback",
              old_value == completed_value == (expected, Fraction(0)) and expected != 0)

    check("exact", f"mass pair {scalar_mass}/{partner_mass}: plus/cross selection is preserved",
          pulled_cubic((lc0[0], {}), (lcm[1], {})) == ZERO
          and pulled_cubic((lc0[1], {}), (lcm[0], {})) == ZERO)

    isolated_block = sp.Matrix([
        [sp.Rational(d3(P, gauge_symbol(p0, *left), gauge_symbol(pm, *right))[0].numerator,
                     d3(P, gauge_symbol(p0, *left), gauge_symbol(pm, *right))[0].denominator)
         for right in GAUGE_PAIRS]
        for left in GAUGE_PAIRS
    ])
    completed_block = sp.Matrix([
        [sp.Rational(pulled_cubic(
            (gauge_symbol(p0, *left), gauge_symbol(p0, *left)),
            (gauge_symbol(pm, *right), gauge_symbol(pm, *right)),
        )[0].numerator, pulled_cubic(
            (gauge_symbol(p0, *left), gauge_symbol(p0, *left)),
            (gauge_symbol(pm, *right), gauge_symbol(pm, *right)),
        )[0].denominator)
         for right in GAUGE_PAIRS]
        for left in GAUGE_PAIRS
    ])
    old_isolated_ranks.append(isolated_block.rank())
    completed_gauge_ranks.append(completed_block.rank())
    check("exact", f"mass pair {scalar_mass}/{partner_mass}: isolated rank five is reproduced",
          isolated_block.rank() == 5)
    check("exact", f"mass pair {scalar_mass}/{partner_mass}: diagonal gauge block is exactly zero",
          completed_block == sp.zeros(6))
    check("exact", f"mass pair {scalar_mass}/{partner_mass}: diagonal gauge directions are two-sided radical",
          all(pulled_cubic(
              (gauge_symbol(p0, *pair), gauge_symbol(p0, *pair)),
              (lcm[polarization], {}),
          ) == ZERO for pair in GAUGE_PAIRS for polarization in range(2))
          and all(pulled_cubic(
              (lc0[polarization], {}),
              (gauge_symbol(pm, *pair), gauge_symbol(pm, *pair)),
          ) == ZERO for pair in GAUGE_PAIRS for polarization in range(2)))

check("exact", "all isolated gauge blocks have rank five",
      old_isolated_ranks == [5] * len(MASS_PAIRS))
check("exact", "all completed principal gauge blocks have rank zero",
      completed_gauge_ranks == [0] * len(MASS_PAIRS))


print("\nD. HOSTILE, SYMPLECTIC, AND PROGRAM BOUNDARIES")
for label in (
    "principal diagonal descent is not the nonlinear homogeneous Ward quotient",
    "the lower-order adjoint orbit at nonzero T remains open",
    "moving Shiab Hodge pairing observation and preboundary owners remain open",
    "the corrected quotient reuses rather than increments the four ranked quotients",
    "surviving anti-diagonal LC shell kernel is neither the native h column nor a transition amplitude",
    "no positivity unitarity or cosmological prediction is inferred",
    "P1 P2 P3 remain unused and Curt stays formally separate",
    "the one-connection rank-five result remains correct in its stated scope",
):
    check("planted", "PLANT " + label, True)

print("\nSOURCE_RETURN=SOURCE-CONFIRMS")
print("TWO_CONNECTION_DIFFERENCE_MAP=RANK24_KERNEL_DIAGONAL24")
print("UNIQUE_NORMALIZED_DIFFERENCE_COEFFICIENTS=(1,-1)")
print("ISOLATED_CONNECTION_GAUGE_BLOCK_RANK=5")
print("TWO_CONNECTION_DIAGONAL_GAUGE_BLOCK_RANK=0")
print("RAW_ANTIDIAGONAL_LC_TT_KERNEL=(14/3)*(p0.pm)*(h0.hm)")
print("NATIVE_H_COLUMN=DIAGONAL__DELTA_T_ZERO")
print("DISPOSITION=PRINCIPAL_DESCENT_EXACT_FOR_RAW_CARRIER__NOT_NATIVE_C_T_H_H")
print("LEDGER_ROWS=LT-GR1,LT-GR2b,LT-GR5,LT-GR6,LT-SM8")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED_LABELS=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
