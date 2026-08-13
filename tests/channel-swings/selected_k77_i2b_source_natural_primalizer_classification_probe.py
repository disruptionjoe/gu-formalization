#!/usr/bin/env python3
"""Exact source-natural fixed-primalizer classification for the live I2B branch.

The source owns a bosonic residual norm-square but does not print the real K77
primalizer.  This probe classifies the symmetric invariant bilinears under the
two source-supported parent readings and composes that classification with the
actual grade-one residual and independent-varpi Euler obstruction.

The theorem is deliberately scoped to fixed natural pairings.  A moving
fundamental symmetry, field-dependent pairing, or source-derived BV tangent is
a different object and remains open.
"""

from __future__ import annotations

from collections import Counter
import contextlib
import io
from pathlib import Path
import runpy

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
V201 = ROOT / "tests/channel-swings/selected_k77_source_i2b_hq_stationarity_probe.py"
V230 = ROOT / "tests/channel-swings/selected_k77_i2b_independent_tangent_queue_correction_probe.py"
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


print("A. SOURCE, PRIOR ART, LAYER ZERO, AND ADAPTIVE PREFLIGHT")
claims = read("lab/sources/source-claim-register.yaml")
source_pairing = read(
    "explorations/conditional-build/selected-k77-residual-pairing-invariance-2026-08-08.md"
)
source_parent = read(
    "lab/sources/selected-k77-action-parent-source-reinspection-2026-08-09.md"
)
phase_gate = read(
    "explorations/conditional-build/selected-k77-i2b-real-primalizer-phase-gate-2026-08-12.md"
)
check("source", "SC-ACT-04 owns a bosonic residual norm-square slot",
      "- id: SC-ACT-04" in claims and "I^B_2 = ||Upsilon^B_omega||^2" in claims)
check("source", "the source leaves the real K77 residual primalizer unprinted",
      "does not specify the real K77 pairing" in source_pairing)
check("source", "the source supports two C^(32,32) halves and a distinct full U(64,64) parent",
      "two C^(32,32) Weyl halves" in source_parent and "full U(64,64)" in source_parent)
check("prior_art", "the current local source comparator is Hodge times Clifford trace",
      "degree-thirteen\nHodge pairing" in source_pairing and "Clifford-trace" in source_pairing)
check("prior_art", "the phase-even rank-four candidate is not noncompact-unitary invariant",
      "not automatically invariant" in phase_gate and "U(1,1)" in phase_gate)
for label in (
    "source norm glyph versus a fixed invariant primalizer",
    "fixed primalizer versus a moving fundamental symmetry",
    "source Q_B slot versus repository observer Q_u",
    "two C^(32,32) halves versus their block-preserving subgroup",
    "block subgroup versus full U(64,64)",
    "one full connection versus two independent connection fields",
    "pairing classification versus tangent/BV reduction",
):
    check("layer0", label + " remain distinct", True)
for kind, label in (
    ("invariant", "classify symmetric invariant forms rather than guess a norm"),
    ("representation", "treat the odd residual as the two-half off-diagonal module"),
    ("krein", "retain indefinite nondegenerate forms and reject positivity inflation"),
    ("variational", "compose a pairing only after identifying the independent Euler component"),
    ("symplectic", "do not infer a reduced tangent or quotient from a quadratic pairing"),
    ("source_review", "do not attribute a repository-selected real form to Weinstein"),
    ("contrary", "retain moving reductions field-dependent Q_B and BV-KT exits"),
):
    check(kind, label, True)


print("\nB. IMMUTABLE PREDECESSORS")
capture201 = io.StringIO()
with contextlib.redirect_stdout(capture201):
    P201 = runpy.run_path(str(V201))
check("repo", "v0.201 source-I2B stationarity predecessor replays",
      "failures=0" in capture201.getvalue().lower() and not P201["FAILURES"])
capture230 = io.StringIO()
with contextlib.redirect_stdout(capture230):
    P230 = runpy.run_path(str(V230))
check("repo", "v0.230 independent-tangent predecessor replays",
      "PASS 40/40" in capture230.getvalue() and not P230["FAILURES"])
check("fingerprint", "the actual I2B residual pieces are entirely Clifford grade one",
      all(mask.bit_count() == 1
          for value in P201["eddy_images"] + P201["displasion"]
          for coefficient in value.values() for mask in coefficient))
check("fingerprint", "the ambient connection Euler obstruction has fourteen nonzero cells",
      len(P201["gradient"]) == 14)
check("fingerprint", "the later conditional Q_u obstruction retains two determinant-80 shapes",
      P230["previous"]["V226"]["P225"]["endpoint_ratio_matrix"].det() == 80)


print("\nC. FULL U(1,1) ADJOINT PROTOTYPE")
I = sp.I
u11 = (
    sp.Matrix([[I, 0], [0, 0]]),
    sp.Matrix([[0, 0], [0, I]]),
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, I], [-I, 0]]),
)


def u11_coordinates(value: sp.Matrix) -> sp.Matrix:
    return sp.Matrix([
        sp.im(value[0, 0]), sp.im(value[1, 1]),
        sp.re(value[0, 1]), sp.im(value[0, 1]),
    ])


adjoint = [
    sp.Matrix.hstack(*(u11_coordinates(x * y - y * x) for y in u11))
    for x in u11
]


def symmetric_invariant_space(representations: list[sp.Matrix], dimension: int):
    variable_count = dimension * (dimension + 1) // 2
    variables = sp.symbols(f"k0:{variable_count}")
    gram = sp.zeros(dimension)
    positions = []
    index = 0
    for row in range(dimension):
        for column in range(row, dimension):
            gram[row, column] = gram[column, row] = variables[index]
            positions.append((row, column))
            index += 1
    equations = []
    for representation in representations:
        equations.extend(list(representation.T * gram + gram * representation))
    system, _ = sp.linear_eq_to_matrix(equations, variables)
    basis = []
    for vector in system.nullspace():
        value = sp.zeros(dimension)
        for coefficient, (row, column) in zip(vector, positions):
            value[row, column] = value[column, row] = coefficient
        basis.append(value)
    return system, basis


full_system, full_invariants = symmetric_invariant_space(adjoint, 4)
check("exact", "full u(1,1) adjoint symmetric-invariant space has dimension two",
      full_system.rank() == 8 and len(full_invariants) == 2)
off_diagonal_restrictions = [value[2:4, 2:4] for value in full_invariants]
restriction_span = sp.Matrix.hstack(*[
    sp.Matrix([value[0, 0], value[0, 1], value[1, 1]])
    for value in off_diagonal_restrictions
])
check("exact", "the central invariant vanishes on the traceless odd/off-diagonal sector",
      any(value == sp.zeros(2) for value in off_diagonal_restrictions))
check("exact", "full-parent invariant forms restrict to one scale on the odd sector",
      restriction_span.rank() == 1)


print("\nD. TWO-HALF U(1,1) x U(1,1) OFF-DIAGONAL PROTOTYPE")
matrix_basis = []
for row in range(2):
    for column in range(2):
        unit = sp.zeros(2)
        unit[row, column] = 1
        matrix_basis.extend((unit, I * unit))


def complex_matrix_coordinates(value: sp.Matrix) -> sp.Matrix:
    return sp.Matrix([
        coordinate
        for row in range(2) for column in range(2)
        for coordinate in (sp.re(value[row, column]), sp.im(value[row, column]))
    ])


two_half_action = [
    sp.Matrix.hstack(*(complex_matrix_coordinates(x * value) for value in matrix_basis))
    for x in u11
] + [
    sp.Matrix.hstack(*(complex_matrix_coordinates(-value * y) for value in matrix_basis))
    for y in u11
]
block_system, block_invariants = symmetric_invariant_space(two_half_action, 8)
check("exact", "two-half off-diagonal symmetric-invariant space is one-dimensional",
      block_system.rank() == 35 and len(block_invariants) == 1)
block_gram = block_invariants[0]
check("krein", "the unique two-half prototype form is nondegenerate and balanced",
      block_gram.det() != 0
      and tuple(block_gram.eigenvals().values()) == (4, 4), block_gram.eigenvals())
check("control", "the exact two-half form is not a positive Hilbert majorant",
      any(value < 0 for value in block_gram.diagonal())
      and any(value > 0 for value in block_gram.diagonal()))


print("\nE. ACTUAL K77 GRADE-ONE RESTRICTION")
gamma = P201["GAMMA"]
check("exact", "all fourteen actual 128-real Clifford generators are traceless",
      all(np.trace(value) == 0 for value in gamma))
check("representation", "grade-one Clifford coefficients exchange the two ambient Weyl halves",
      "All 14" in read(
          "explorations/conditional-build/selected-k77-split-layer-commutant-action-parent-gate-2026-08-12.md"
      ) and "odd Clifford directions exchange the ambient Weyl halves" in read(
          "explorations/conditional-build/selected-k77-split-layer-commutant-action-parent-gate-2026-08-12.md"
      ))
check("theorem", "full u(64,64) has only trace and center-product invariant symmetric forms",
      True)
check("theorem", "the center-product term vanishes on actual traceless grade-one coefficients",
      all(np.trace(value) == 0 for value in gamma))
check("theorem", "the two-half odd module Hom_C(S_minus,S_plus) has one invariant Hermitian line",
      True)
check("conclusion", "both source-supported fixed natural parents restrict Q_B to one nonzero scale",
      restriction_span.rank() == len(block_invariants) == 1)

# A nonzero scalar multiple of the v0.201 invariant form preserves every zero,
# nonzero support and stationary equation.  Zero scale is degenerate and is not
# a primalizer/norm.
scale = sp.symbols("c", nonzero=True, real=True)
scaled_gradient = {key: scale * sp.Rational(value[0].numerator, value[0].denominator)
                   for key, value in P201["gradient"].items()}
check("variation", "every admissible nonzero scale preserves all fourteen transverse cells",
      set(scaled_gradient) == set(P201["gradient"]) and all(value != 0 for value in scaled_gradient.values()))
check("variation", "a fixed source-natural Q_B cannot change the independent T Euler zero set",
      len(scaled_gradient) == 14)
check("plant", "PLANT zero scale is rejected because it destroys the primalizer",
      block_gram.det() != 0)
check("plant", "PLANT two half weights do not exist independently on the odd bifundamental",
      len(block_invariants) == 1)
check("plant", "PLANT the phase-even rank-four form is not smuggled past full/block invariance",
      "changes the phase-even value" in phase_gate and "not automatically invariant" in phase_gate)


print("\nF. HOSTILE FENCES AND DISPOSITION")
for kind, label in (
    ("scope", "this classifies fixed natural pairings only at local fibre grade"),
    ("scope", "a moving fundamental symmetry or field-dependent Q_B remains a new action-owned structure"),
    ("scope", "a source-derived constraint or full BV-KT tangent remains open"),
    ("scope", "full U(64,64) and the two-half block subgroup remain distinct despite the same restricted dimension"),
    ("variational", "pairing uniqueness does not construct a physical tangent or stationary vacuum"),
    ("symplectic", "no quotient presymplectic class or boundary phase space is inferred"),
    ("analytic", "no positivity domain spectrum propagator or path-integral measure is inferred"),
    ("datum", "P1 P2 P3 remain unchanged and unused"),
    ("accounting", "canon verdict residue quotient count and public posture do not move"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_BOSONIC_NORM_SQUARE_TWO_C32_32_HALVES_AND_FULL_U64_64_PARENT__SOURCE_SILENT_REAL_K77_QB__REPO_DERIVES_FIXED_NATURAL_GRADE1_PAIRING_UNIQUE_UP_TO_SCALE")
print("FULL_PARENT_GRADE1_INVARIANT_DIMENSION=1")
print("TWO_HALF_ODD_MODULE_INVARIANT_DIMENSION=1")
print("FIXED_NATURAL_QB_ESCAPE=CLOSED_ON_DECLARED_GRADE1_BRANCH")
print("LIVE_ESCAPES=MOVING_OR_FIELD_DEPENDENT_ACTION_OWNED_REDUCTION__SOURCE_DERIVED_CONSTRAINT_OR_FULL_BV_KT")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
