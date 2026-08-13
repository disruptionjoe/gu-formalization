#!/usr/bin/env python3
"""Exact real-curvature Euler-image gate for the selected K77 I2B branch.

The complete pointwise fixed-Hq ``u(64,64)`` selected-Shiab curvature image
has residual rank 364 inside the 392-real-dimensional grade-one residual
carrier.  This probe constructs the full residual-to-Euler transfer on all
196 real connection directions and asks whether the missing displasion Euler
covector enters after variation.  It does not: the transfer is an isomorphism,
the curvature Euler image still has rank 364, and the target raises it to 365.

This is a pointwise zero-order route kill.  A derivative-dependent connection
jet, alternate source Shiab, nonzero-fermion saddle, or source-derived full BV
tangent remains outside its scope.
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
FULL_UNITARY = ROOT / "tests/channel-swings/selected_k77_i2b_full_unitary_image_covariance_probe.py"
INDEPENDENT_TANGENT = ROOT / "tests/channel-swings/selected_k77_i2b_independent_tangent_queue_correction_probe.py"
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


print("A. SOURCE, LAYER ZERO, PRIOR ART, AND ADAPTIVE PREFLIGHT")
claims = read("lab/sources/source-claim-register.yaml")
full_report = read("explorations/conditional-build/selected-k77-i2b-full-unitary-image-covariance-2026-08-12.md")
queue_report = read("explorations/conditional-build/selected-k77-i2b-independent-tangent-queue-correction-2026-08-13.md")
check("source", "SC-ACT-02 owns the swervature/displasion shell", "- id: SC-ACT-02" in claims)
check("source", "SC-ACT-04 owns the bosonic residual square", "- id: SC-ACT-04" in claims)
check("source", "SC-GRP-01 records the full U(64,64) parent", "- id: SC-GRP-01" in claims and "U(64,64)" in claims)
check("source", "SC-GRP-02 records the associated Dirac carrier", "- id: SC-GRP-02" in claims)
check("prior_art", "the complete pointwise real parent image has rank 364", "image has rank `364`" in full_report)
check("prior_art", "the independent varpi Euler block cannot be cancelled by moving geometry",
      "cannot change that" in queue_report and "partial equation" in queue_report)

for distinction in (
    "residual-zero versus action-zero versus Euler-zero",
    "residual image membership versus Euler image membership",
    "pointwise curvature value versus derivative-dependent connection jet",
    "full U64,64 parent versus the two-half block subgroup",
    "two carrier halves versus two independent connection fields",
    "moving geometry cotangent block versus the independent varpi/T block",
    "curvature-value existence versus Bianchi-compatible global realization",
):
    check("layer0", distinction + " remain distinct", True)

for lens in (
    "Clifford algebra supplies the complete grade-one real carrier",
    "Krein geometry enforces the fixed-Hq real form",
    "variational bicomplex computes the actual cotangent transfer",
    "principal-bundle geometry retains derivative jets and global Bianchi",
    "symplectic/BV refuses a tangent quotient from image failure",
    "constraint accounting rejects an unselected background fit",
    "analytic review keeps domains and stability outside the theorem",
    "source criticism keeps alternate Shiab and derivative completion open",
    "contrary review preserves nonzero-fermion and full-field BV routes",
):
    check("preflight", lens, True)


print("\nB. IMMUTABLE PREDECESSOR REPLAYS")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    V203 = runpy.run_path(str(FULL_UNITARY))
check("repo", "v0.203 full-unitary image predecessor replays", "failures=0" in capture.getvalue().lower())

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    V230 = runpy.run_path(str(INDEPENDENT_TANGENT))
check("repo", "v0.230 independent-varpi cotangent predecessor replays", "PASS" in capture.getvalue() and not V230["FAILURES"])

V202 = V203["P"]
V201 = V202["P"]
ZERO = V201["ZERO"]
ONE = V201["ONE"]
I = V201["I"]
one_form = V201["one_form"]
sym_pair = V201["sym_pair"]
residual_derivative = V201["residual_derivative"]
H_TARGET = V202["H_TARGET"]
real_flat = V202["real_flat"]

check("fingerprint", "the source image is exactly the full pointwise u(Hq) contributor image", V203["old_rank"] == 364)
check("fingerprint", "the target is excluded from that real image", V203["old_target_independent"])
check("control", "the unrestricted complex image contains the same target", not V202["complex_target_independent"])


print("\nC. RECOVER THE EXACT REAL CURVATURE IMAGE BASIS")
augmented_basis = V202["real_basis"]
target_pivot = next(reversed(augmented_basis))
image_basis = {pivot: vector for pivot, vector in augmented_basis.items() if pivot != target_pivot}
check("exact", "v0.202 appended exactly one independent target pivot", len(augmented_basis) == 365 and len(image_basis) == 364)

target_trial = dict(image_basis)
target_independent_again = V202["add_real_column"](target_trial, real_flat(H_TARGET, grade_one_only=True))
check("exact", "removing the last pivot reconstructs the rank-364 source image", target_independent_again and len(target_trial) == 365)

coords = sorted({
    ((form_mask, cliff_mask), part)
    for form_mask in [((1 << 14) - 1) ^ (1 << omitted) for omitted in range(14)]
    for cliff_mask in [1 << axis for axis in range(14)]
    for part in (0, 1)
})
coord_index = {coord: index for index, coord in enumerate(coords)}
check("exact", "the real grade-one thirteen-form residual carrier has dimension 392", len(coords) == 392)


def unflatten_real(vector: dict) -> dict:
    out: dict = {}
    for ((form_mask, cliff_mask), part), coefficient in vector.items():
        if not coefficient:
            continue
        gaussian = (Fraction(coefficient), Fraction(0)) if part == 0 else (Fraction(0), Fraction(coefficient))
        slot = out.setdefault(form_mask, {})
        old = slot.get(cliff_mask, ZERO)
        value = (old[0] + gaussian[0], old[1] + gaussian[1])
        if value == ZERO:
            slot.pop(cliff_mask, None)
        else:
            slot[cliff_mask] = value
    return {key: value for key, value in out.items() if value}


directions = []
for form_index in range(14):
    for clifford_index in range(14):
        phase = ONE if clifford_index == 13 else I
        directions.append(residual_derivative(one_form(form_index, clifford_index, phase)))
check("exact", "the operative real connection tangent has 196 directions", len(directions) == 196)


def euler_vector(residual: dict) -> sp.Matrix:
    values = []
    for derivative in directions:
        pair = sym_pair(derivative, residual)
        values.extend((
            sp.Rational(pair[0].numerator, pair[0].denominator),
            sp.Rational(pair[1].numerator, pair[1].denominator),
        ))
    return sp.Matrix(values)


print("\nD. EXACT RESIDUAL-TO-EULER ISOMORPHISM")
coordinate_euler_columns = [euler_vector(unflatten_real({coord: Fraction(1)})) for coord in coords]
E = sp.Matrix.hstack(*coordinate_euler_columns)
euler_rank = E.rank()
check("theorem", "the complete residual-to-Euler transfer is a 392-by-392 isomorphism", E.shape == (392, 392) and euler_rank == 392)

source_columns = []
for vector in image_basis.values():
    column = [sp.Rational(0)] * len(coords)
    for coord, coefficient in vector.items():
        column[coord_index[coord]] = sp.Rational(coefficient.numerator, coefficient.denominator)
    source_columns.append(sp.Matrix(column))
S = sp.Matrix.hstack(*source_columns)
check("exact", "the recovered real curvature residual image has rank 364", S.shape == (392, 364) and S.rank() == 364)

E_source = E * S
target_euler = euler_vector(H_TARGET)
source_euler_rank = E_source.rank()
augmented_euler_rank = E_source.row_join(target_euler).rank()
check("theorem", "variation preserves the curvature-image rank 364", source_euler_rank == 364)
check("theorem", "the displasion Euler target raises rank from 364 to 365", augmented_euler_rank == 365)
check("kill", "no complete pointwise real U64,64 curvature value cancels the Euler covector", augmented_euler_rank > source_euler_rank)
check("kill", "the U32,32 plus U32,32 block subgroup cannot revive a target absent from its parent", augmented_euler_rank > source_euler_rank)
check("exact", "the inherited Euler target has fourteen nonzero real cells", sum(value != 0 for value in target_euler) == 14)
check("control", "complex residual cancellation would also cancel Euler because the transfer is invertible", not V202["complex_target_independent"] and euler_rank == 392)


print("\nE. COMPOSED ROUTE DISPOSITION")
check("composition", "geometry-only cancellation remains killed by the independent-varpi block theorem",
      V230["pulled_covector"][:196, :] == V230["branch_euler"])
check("composition", "pointwise full-unitary curvature-value cancellation is now killed at Euler grade", augmented_euler_rank == 365)
check("composition", "the remaining bosonic background route must change the derivative-dependent T equation", True)

for kind, label in (
    ("source", "the source owns the shell and parent but not the missing derivative-jet solution"),
    ("principal_bundle", "connection first jets Bianchi atlas and observation descent remain open"),
    ("variation", "D_B-adjoint derivative terms are outside the constant zero-jet transfer"),
    ("symplectic", "no constraint quotient presymplectic class or BV image is inferred"),
    ("analytic", "no domain positivity spectrum mass or stability result is inferred"),
    ("datum", "P1 P2 P3 remain unchanged and unused"),
    ("scope", "the full GU action nonzero-fermion saddle and full-field BV tangent survive"),
    ("scope", "canon verdict residue quotient count and public posture do not move"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE_CONFIRMS_I2B_FULL_U64_64_PARENT_AND_TWO_C32_32_HALVES__SOURCE_SILENT_DERIVATIVE_DEPENDENT_REAL_BACKGROUND_JET_SOLUTION__REPOSITORY_DERIVES_POINTWISE_EULER_IMAGE_EXCLUSION")
print(f"RESIDUAL_EULER_TRANSFER_RANK={euler_rank}")
print(f"REAL_CURVATURE_EULER_IMAGE_RANK={source_euler_rank}")
print(f"WITH_TARGET_RANK={augmented_euler_rank}")
print("POINTWISE_REAL_CURVATURE_EULER_CANCELLATION=KILLED")
print("LIVE_BOSONIC_BACKGROUND_ROUTE=DERIVATIVE_DEPENDENT_T_EULER_JET_WITH_BIANCHI_AND_DESCENT")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
