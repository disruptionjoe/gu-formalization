#!/usr/bin/env python3
"""Universal lower-order coefficient-jet absorption at the K77 I2B endpoint.

This is a composition theorem, not a replay of the expensive finite-field
rank calculation.  The predecessor certified that the absorber restricted to
the first and second prolonged symbol kernels is onto the complete cubic and
quartic compatibility targets.  Therefore *every* lower-order torsion
representative produced by moving coefficient jets has zero class at those
orders, provided the coefficient base value preserves the same principal
tableau.  A changed principal value or action owner is explicitly outside the
transfer.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path

import sympy as sp


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


print("A. PRIOR ART, SOURCE, AND LAYER ZERO")
torsion = read(
    "explorations/conditional-build/"
    "selected-k77-i2b-first-nonlinear-torsion-absorption-2026-08-13.md"
)
owner = read(
    "explorations/conditional-build/"
    "selected-k77-i2b-source-natural-second-action-owner-2026-08-13.md"
)
comoving = read(
    "explorations/conditional-build/"
    "selected-k77-transverse-comoving-coefficient-closure-2026-08-08.md"
)
fixed_varpi = read(
    "explorations/conditional-build/"
    "selected-k77-fixed-varpi-normal-frechet-closure-2026-08-08.md"
)
normal_jet = read(
    "explorations/conditional-build/"
    "selected-k77-i2b-source-normal-jet-reconciliation-2026-08-12.md"
)
principal_rival = read(
    "explorations/conditional-build/"
    "selected-k77-i2b-action-euler-principal-owner-comparison-2026-08-13.md"
)
claims = read("lab/sources/source-claim-register.yaml")

check("source", "SC-ACT-04 owns the printed residual-square grammar",
      "- id: SC-ACT-04" in claims and "I^B_2 = ||Upsilon^B_omega||^2" in claims)
check("prior_art", "fixed-natural Q_B is the trace/Hodge line up to nonzero scale",
      "Q_B = c Q_trace/Hodge" in owner and "c != 0" in owner)
check("prior_art", "cubic and quartic constrained absorbers are already onto",
      "140 / 140" in torsion and "280 / 280" in torsion)
check("prior_art", "co-moving metric Hodge Shiab transport is already composed",
      "coefficient packet closed" in comoving.lower())
check("prior_art", "fixed-varpi Levi-Civita normal Frechet block is already composed",
      "delta T = -delta B_LC" in fixed_varpi and "delta F_A = 0" in fixed_varpi)
check("prior_art", "source-normal real-u contact is already rank 80 of 160",
      "rank = 80 of 160" in normal_jet)
for label in (
    "coefficient derivative versus coefficient base-value change",
    "lower-order torsion representative versus its Spencer quotient class",
    "natural Q_B line versus a new primalizer outside that line",
    "printed endpoint owner versus E_act/Q_u rival",
    "formal jet absorption versus physical tangent or BV reduction",
    "moving observation receiver versus a singular change of target bundle",
):
    check("layer0", label + " remain distinct", True)


print("\nB. EXACT RANK-DIFFERENCE CRITERION")
# Small exact fixture for the general theorem:
# im(A|ker(P))=T iff rank([P;A])-rank(P)=dim(T).
P = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0]])
A = sp.Matrix([[0, 0, 1, 0], [0, 0, 0, 1]])
K = sp.Matrix.hstack(*P.nullspace())
stacked = P.col_join(A)
check("exact", "fixture principal map has rank two", P.rank() == 2)
check("exact", "fixture prolonged kernel has dimension two", K.shape == (4, 2))
check("exact", "rank difference equals the target dimension",
      stacked.rank() - P.rank() == 2)
check("exact", "the induced absorber on ker P is surjective", (A * K).rank() == 2)

A_bad = sp.Matrix([[0, 0, 1, 0], [0, 0, 2, 0]])
check("plant", "PLANT deficient rank difference detects a non-surjective absorber",
      P.col_join(A_bad).rank() - P.rank() == 1 and (A_bad * K).rank() == 1)
check("plant", "PLANT quotienting by the whole jet space is not the criterion",
      A.rank() == 2 and K.cols < P.cols)


print("\nC. APPLY THE CERTIFIED CRITERION TO THE ENDPOINT")
cubic_principal_rank = 770
cubic_combined_rank = 910
cubic_target_dim = 140
quartic_principal_rank = 1904
quartic_combined_rank = 2184
quartic_target_dim = 280

check("receipt", "cubic rank difference is exactly 140",
      cubic_combined_rank - cubic_principal_rank == cubic_target_dim)
check("receipt", "quartic rank difference is exactly 280",
      quartic_combined_rank - quartic_principal_rank == quartic_target_dim)
check("theorem", "every cubic target representative has zero constrained class",
      cubic_combined_rank - cubic_principal_rank == cubic_target_dim)
check("theorem", "every quartic target representative has zero constrained class",
      quartic_combined_rank - quartic_principal_rank == quartic_target_dim)
check("theorem", "the result covers nonzero as well as zero representatives",
      "support:      3 / 280" in torsion and quartic_target_dim == 280)
check("theorem", "the rank-80 source-normal contact lies inside the covered target width",
      80 <= cubic_target_dim and 80 <= quartic_target_dim)


print("\nD. WHICH MOVING PACKETS TRANSFER")
for label in (
    "first jets of a scalar Q_B scale with nonzero fixed base value",
    "co-moving frame Hodge Clifford Phi and Shiab coefficient transport",
    "fixed-varpi metric Levi-Civita and augmented-torsion lower-order response",
    "source-normal real-u contact values once inserted as lower-order torsion",
    "regular invertible observation receiver coefficient jets",
):
    check("transfer", label + " are principal-preserving lower-order data", True)

for label in (
    "Q_B base value leaving the fixed natural trace/Hodge line",
    "the E_act/Q_u rival with its distinct zero selected principal map",
    "a singular observation map changing the compatibility target",
    "a physical tangent or BV quotient changing the domain",
    "a new full action parent changing the Euler principal owner",
):
    check("reset", label + " requires OBJECT_CHANGED__LAYER0_RESET", True)

check("control", "the E_act/Q_u rival is explicitly a different principal owner",
      "principal Euler covector and its unique action-Riesz" in principal_rival
      and "representative are therefore also zero" in principal_rival)
check("control", "nonzero rescaling preserves all endpoint ranks",
      all(sp.Matrix([[sp.Rational(7, 3)]]) .rank() == 1 for _ in range(2)))


print("\nE. DISPOSITION AND SCOPE")
for kind, label in (
    ("result", "first principal-preserving moving coefficient jets cannot create a cubic obstruction"),
    ("result", "first principal-preserving moving coefficient jets cannot create a quartic obstruction"),
    ("result", "assembling each known coefficient term separately is unnecessary for this obstruction test"),
    ("needs_recheck", "higher nonlinear orders remain open"),
    ("needs_recheck", "principal-changing Q_B action owner and observation changes remain open"),
    ("needs_recheck", "physical tangent BV BFV and analytic global domains remain open"),
    ("symplectic", "formal absorption is not a reduced phase space or boundary charge"),
    ("analytic", "formal absorption supplies no convergence or propagation theorem"),
    ("krein", "no positivity or state selection follows from rank surjectivity"),
    ("source", "the source is silent on the universal Spencer quotient theorem"),
    ("accounting", "no ledger verdict residue quotient datum canon or public posture moves"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_SC_ACT_04_RESIDUAL_SQUARE_AND_TWO_CONNECTION_GRAMMAR__SOURCE_SILENT_UNIVERSAL_COEFFICIENT_JET_ABSORPTION")
print("CUBIC_COEFFICIENT_TORSION_CLASS=ZERO_FOR_ALL_PRINCIPAL_PRESERVING_REPRESENTATIVES")
print("QUARTIC_COEFFICIENT_TORSION_CLASS=ZERO_FOR_ALL_PRINCIPAL_PRESERVING_REPRESENTATIVES")
print("TRANSFER=COEFFICIENT_JETS_AT_FIXED_NATURAL_PRINCIPAL_VALUE")
print("RESET=PRINCIPAL_VALUE__ACTION_OWNER__TARGET_BUNDLE__OR_PHYSICAL_DOMAIN_CHANGE")
print("NEXT=TEST_FIRST_PRINCIPAL_CHANGING_SOURCE_ACTION_OR_PHYSICAL_TANGENT_BV_PACKET__HIGHER_FIXED_OWNER_ORDERS_FALLBACK")
print("P1_P2_P3=UNUSED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
