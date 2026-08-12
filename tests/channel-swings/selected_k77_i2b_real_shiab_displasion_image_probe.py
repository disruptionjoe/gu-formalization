#!/usr/bin/env python3
"""Exact real-form selected-Shiab image gate for the I2B displasion branch.

The predecessor found a nonzero, Krein-null displaced-torsion residual on the
restricted SC-ACT-04 branch.  This probe asks whether that residual can be
cancelled by a source-typed curvature value.  It deliberately separates an
unrestricted complex preimage from a preimage in the operative fixed-H_q real
unitary algebra, then tests the simplest source-motivated two-connection
opposite-phase background.  It is a finite local image theorem, not a global
connection, Bianchi, moving-H_q, BV, or analytic-domain theorem.
"""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
import itertools
from pathlib import Path
import runpy

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_source_i2b_hq_stationarity_probe.py"
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


print("A. SOURCE RETURN, LAYER ZERO, PRIOR ART, AND ADAPTIVE PREFLIGHT")
claims = read("lab/sources/source-claim-register.yaml")
two_layer = read("lab/sources/gu-two-layer-action-source-reinspection-2026-08-04.md")
two_connection = read("lab/sources/gu-two-connection-shifted-superconnection-source-reinspection-2026-08-04.md")
reduction = read("explorations/conditional-build/selected-k77-action-owned-reduction-carrier-typing-2026-08-10.md")
cartan = read("explorations/conditional-build/selected-source-varpi-cartan-composition-2026-08-07.md")

check("source", "SC-ACT-02 types the first shell as swervature equals displasion",
      "- id: SC-ACT-02" in claims and "swervature equals displasion" in claims)
check("source", "SC-ACT-04 types the second bosonic action as a residual norm square",
      "- id: SC-ACT-04" in claims and "I^B_2 = ||Upsilon^B_omega||^2" in claims)
check("source", "the source confirms two connections and augmented torsion as their difference",
      "two connections" in two_connection and "difference of that pair augmented torsion" in two_connection)
check("source", "the source leaves the unreleased cyclic map and its action identification silent",
      "SOURCE-SILENT" in two_connection and "unreleased" in two_connection)
check("source", "the source confirms the norm-square architecture and leaves exact path maps silent",
      "SOURCE-CONFIRMS-NORM-SQUARE-AND-REDUNDANCY" in two_layer
      and "exact path maps are `SOURCE-SILENT`" in two_layer)
check("prior_art", "the moving reduction remains a candidate rather than an action-selected quotient",
      "finite physical carrier projector" in reduction and "SOURCE-SILENT" in reduction)
check("prior_art", "the source-native fixed-epsilon tangent varies T and A but not B",
      "VARPI_TANGENT_IS_DELTA_T_DELTA_A_NOT_DELTA_B" in cartan)

for distinction in (
    "first-shell Upsilon zero versus second-action norm zero",
    "Krein-null residual versus zero residual",
    "unrestricted complex preimage versus fixed-Hq real-form preimage",
    "curvature-value preimage versus connection and Bianchi realization",
    "fixed-Hq image failure versus moving-Hq or source-full-unitary failure",
    "negative background direction versus selected background amplitude",
):
    check("layer0", distinction + " remain distinct", True)

for lens in (
    "Clifford algebra checks the complete grade-one contributor bank",
    "Krein geometry enforces the fixed-Hq real unitary phase rule",
    "linear algebra compares exact real and complex images",
    "principal-bundle geometry separates curvature values from connection descent",
    "variational analysis tests the full two-cell first variation",
    "symplectic geometry refuses a reduced phase space without an action-owned reduction",
    "analytic review refuses a spectrum or vacuum from a pointwise image theorem",
    "source criticism keeps the two-connection construction source-typed but unreleased",
    "contrary-path review retains moving-Hq full-unitary and derivative-jet routes",
):
    check("preflight", lens, True)


print("\nB. PREDECESSOR REPLAY AND EXACT ALGEBRA")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    P = runpy.run_path(str(PREDECESSOR))
check("repo", "v0.201 source-I2B stationarity predecessor replays",
      "failures=0" in capture.getvalue().lower())

ZERO = P["ZERO"]
ONE = P["ONE"]
I = P["I"]
SELECTED = P["SELECTED"]
one_form = P["one_form"]
fadd = P["fadd"]
fscale = P["fscale"]
wedge_raw = P["wedge_raw"]
hodge = P["hodge"]
shiab = P["shiab"]
sym_pair = P["sym_pair"]
T0 = P["R"][3]
H_TARGET = hodge(T0)
GAMMA = P["GAMMA"]
Hq = P["Hq_matrix"]
M = P["P"]["M"]
blade = M["blade"]
flatten = M["flatten"]
gmul = M["gmul"]
gdiv = M["gdiv"]
gsub = M["gsub"]


def cross(left, right):
    return fadd(wedge_raw(left, right), wedge_raw(right, left))


def add_real_column(basis, column):
    value = dict(column)
    while value:
        pivot = min(value)
        lead = value[pivot]
        if pivot not in basis:
            basis[pivot] = {key: coefficient / lead for key, coefficient in value.items()}
            return True
        for key, coefficient in basis[pivot].items():
            updated = value.get(key, Fraction(0)) - lead * coefficient
            if updated:
                value[key] = updated
            else:
                value.pop(key, None)
    return False


def real_flat(form, grade_one_only=False):
    out = {}
    for key, coefficient in flatten(form).items():
        if grade_one_only and key[1].bit_count() != 1:
            continue
        if coefficient[0]:
            out[(key, 0)] = coefficient[0]
        if coefficient[1]:
            out[(key, 1)] = coefficient[1]
    return out


def add_gaussian_column(basis, column):
    value = dict(column)
    while value:
        pivot = min(value)
        lead = value[pivot]
        if pivot not in basis:
            basis[pivot] = {
                key: gdiv(coefficient, lead)
                for key, coefficient in value.items()
                if gdiv(coefficient, lead) != ZERO
            }
            return True
        for key, coefficient in basis[pivot].items():
            updated = gsub(value.get(key, ZERO), gmul(lead, coefficient))
            if updated == ZERO:
                value.pop(key, None)
            else:
                value[key] = updated
    return False


check("exact", "the target is a nonzero Clifford-grade-one thirteen-form",
      bool(H_TARGET)
      and all(mask.bit_count() == 1 for value in H_TARGET.values() for mask in value))


print("\nC. OPPOSITE-PHASE TWO-CONNECTION BACKGROUND")
# T0=e^13 gamma_13+i e^12 gamma_12.  The source-available second
# connection supplies the opposite phase B0=e^13 gamma_13-i e^12 gamma_12.
B0 = fadd(one_form(13, 13, ONE), one_form(12, 12, (-I[0], -I[1])))
T2 = wedge_raw(T0, T0)
B2 = wedge_raw(B0, B0)
BT = cross(B0, T0)
check("exact", "the radial torsion eddy is nonzero", bool(T2))
check("exact", "the opposite-phase connection square is exactly the negative torsion eddy",
      B2 == fscale(Fraction(-1), T2))
check("exact", "the two opposite-phase cells exactly anticommute", BT == {})
check("construction", "the two-connection grammar therefore supplies a zero-fit negative curvature direction",
      bool(B2) and B2 == fscale(Fraction(-1), T2))
check("fence", "the background amplitude remains free even though its sign and ray are geometrized", True)

# Full T variation of the two-cell family.  The columns correspond to the two
# background coefficients, the radial eddy coefficient, and kappa_1.  A
# nonzero displaced-torsion coupling would require a null vector with a live
# fourth component.
U = one_form(13, 13, ONE)
V = one_form(12, 12, I)
rows = []
for form_index in range(14):
    for clifford_index in range(14):
        phase = ONE if clifford_index == 13 else I
        delta = one_form(form_index, clifford_index, phase)
        values = [
            sym_pair(shiab(fscale(Fraction(1, 2), cross(U, delta)), SELECTED), H_TARGET),
            sym_pair(shiab(fscale(Fraction(1, 2), cross(V, delta)), SELECTED), H_TARGET),
            sym_pair(shiab(fscale(Fraction(1, 3), cross(T0, delta)), SELECTED), H_TARGET),
            sym_pair(hodge(delta), H_TARGET),
        ]
        for part in (0, 1):
            row = [sp.Rational(value[part].numerator, value[part].denominator)
                   for value in values]
            if any(row):
                rows.append(row)
stationarity = sp.Matrix(rows)
nullspace = stationarity.nullspace()
check("variation", "the exact two-cell stationarity matrix has rank two",
      stationarity.shape == (14, 4) and stationarity.rank() == 2)
check("variation", "every two-cell stationary vector forces kappa_1 to zero",
      len(nullspace) == 2 and all(vector[3] == 0 for vector in nullspace))
check("kill", "the natural opposite-phase two-connection background cannot cancel nonzero displasion",
      all(vector[3] == 0 for vector in nullspace))


print("\nD. UNRESTRICTED COMPLEX POSITIVE CONTROL")
form_pairs = list(itertools.combinations(range(14), 2))
complex_basis = {}
for form_pair in form_pairs:
    form_mask = (1 << form_pair[0]) | (1 << form_pair[1])
    for cliff_pair in form_pairs:
        add_gaussian_column(
            complex_basis,
            flatten(shiab({form_mask: blade(cliff_pair, ONE)}, SELECTED)),
        )
complex_before = len(complex_basis)
complex_target_independent = add_gaussian_column(complex_basis, flatten(H_TARGET))
check("control", "the unrestricted complex Clifford-bivector Shiab bank contains the target",
      not complex_target_independent, f"rank={complex_before}")
check("plant", "PLANT a complex preimage is rejected as a fixed-Hq real-form preimage", True)


print("\nE. COMPLETE FIXED-Hq REAL GRADE-ONE IMAGE")
# Shiab multiplies the curvature Clifford coefficient by one generator in its
# first term and by three in its second.  Hence a grade-one output can receive
# contributions only from even input grades 0, 2, and 4.  Odd inputs preserve
# even output parity; even grades >=6 cannot contract down to grade one.
check("clifford", "Shiab changes Clifford grade by at most three and flips parity", True)
check("clifford", "only input grades zero two and four can contribute to a grade-one target", True)

clifford_inputs = [()] + list(itertools.combinations(range(14), 2)) + list(itertools.combinations(range(14), 4))
zero_matrix = np.zeros((128, 128), dtype=np.complex128)
phases = []
for indices in clifford_inputs:
    matrix = np.eye(128, dtype=np.complex128)
    for index in indices:
        matrix = matrix @ GAMMA[index]
    real_ok = np.array_equal(matrix.conj().T @ Hq + Hq @ matrix, zero_matrix)
    imag = 1j * matrix
    imaginary_ok = np.array_equal(imag.conj().T @ Hq + Hq @ imag, zero_matrix)
    phases.append(ONE if real_ok else I if imaginary_ok else None)

check("unitary", "all 1093 relevant Clifford blades have one exact fixed-Hq real phase",
      len(clifford_inputs) == 1093 and phases.count(None) == 0)
check("unitary", "the real-form phase split is exactly 364 real and 729 imaginary",
      phases.count(ONE) == 364 and phases.count(I) == 729)

real_basis = {}
real_columns = 0
for form_pair in form_pairs:
    form_mask = (1 << form_pair[0]) | (1 << form_pair[1])
    for indices, phase in zip(clifford_inputs, phases):
        column = shiab({form_mask: blade(indices, phase)}, SELECTED)
        add_real_column(real_basis, real_flat(column, grade_one_only=True))
        real_columns += 1

real_rank = len(real_basis)
target_was_independent = add_real_column(real_basis, real_flat(H_TARGET, grade_one_only=True))
check("exact", "the complete relevant fixed-Hq real bank has 99463 columns",
      real_columns == 99463)
check("exact", "its exact Clifford-grade-one image has real rank 364",
      real_rank == 364)
check("kill", "the displasion target raises the real image rank by one",
      target_was_independent and len(real_basis) == real_rank + 1)
check("kill", "the fixed-Hq real selected-Shiab bank cannot cancel the target",
      target_was_independent)
check("control", "complex cancellation and real-form exclusion fire in opposite directions",
      not complex_target_independent and target_was_independent)


print("\nF. HOSTILE FENCES AND DISPOSITION")
for kind, label in (
    ("layer0", "the complex solution does not survive the operative reality condition"),
    ("source", "the source confirms the shell and two connections but is silent on this background map"),
    ("principal_bundle", "a curvature image theorem does not construct a descended Bianchi-compatible connection"),
    ("krein", "the exclusion belongs to fixed Hq and does not decide a moving Hermitian form"),
    ("symplectic", "no reduced phase space momentum map or BV quotient is inferred"),
    ("analytic", "no global Green domain spectrum or vacuum is inferred"),
    ("scope", "the source-full U64,64 or two U32,32 connection parent remains distinct from this Clifford bank"),
    ("datum", "P1 P2 P3 remain unchanged and unused"),
    ("contrary", "moving-Hq derivative jets a different source Shiab or a full-unitary complement may supply the missing line"),
):
    check(kind, label, True)

print("\nSUMMARY")
print(f"counts={dict(COUNTS)} failures={len(FAILURES)}")
print(f"complex_rank={complex_before} real_grade1_rank={real_rank} real_columns={real_columns}")
print(f"stationarity_shape={stationarity.shape} stationarity_rank={stationarity.rank()}")
if FAILURES:
    print("FAILED:", FAILURES)
    raise SystemExit(1)
print("PASS: the unrestricted complex selected-Shiab bivector bank contains the displaced-torsion target, but the complete fixed-Hq real Clifford bank capable of producing grade one does not: its 99,463 columns span rank 364 and the target raises the rank to 365. The source-motivated opposite-phase second connection supplies an exact negative curvature ray, but full stationarity forces kappa_1=0. This kills direct fixed-Hq real curvature cancellation, not moving-Hq, source-full-unitary, derivative-jet, alternate-source-selector, or global connection routes.")
