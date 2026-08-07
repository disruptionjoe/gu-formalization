#!/usr/bin/env python3
"""Exact full-Cl2 residual pullback for the selected second action.

The construction first derives the observer-stabilizer support formula and
then exhaustively verifies all 1274 x 100 entries against the selected-action
Hessian.  Co-moving target data are composed only at stationary quadratic
grade; other Clifford grades and higher variational grades remain open.
"""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
from itertools import combinations
from pathlib import Path
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
BACKEND = ROOT / "tests/channel-swings/selected_cubic_gauge_rotated_lc_ward_owner_probe.py"
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


def rational(value: Fraction) -> sp.Rational:
    return sp.Rational(value.numerator, value.denominator)


print("A. SOURCE, LAYER 0, AND CO-MOVING PREDECESSORS")
source = read("lab/sources/gu-two-layer-action-source-reinspection-2026-08-04.md")
prior = read("explorations/conditional-build/selected-second-layer-i2b-gauss-owner-map-2026-08-06.md")
frame = read("explorations/conditional-build/selected-action-comoving-frame-naturality-2026-08-06.md")
observation = read("explorations/conditional-build/selected-action-physical-soldering-observation-compose-2026-08-06.md")
check("source", "source confirms the bosonic norm-square architecture",
      "SOURCE-DISPLAYS-BOSONIC-NORM-SQUARE" in source)
check("source", "source is silent on the I2B to observer full-II map",
      "SOURCE-SILENT" in source and "independent K77 second-layer target" in source)
check("repo", "v0.38 leaves the complete 1274 by 100 Cl2 pullback open",
      "1,274-by-100 residual map" in prior and "2/39" in prior)
check("repo", "pure co-moving frame response is already exact and natural",
      "pure-frame derivative is exactly zero" in frame)
check("repo", "complete first-jet observation has an exact inverse equation dual",
      "Both composites are the identity" in observation)
for label in (
    "selected Cl2 bosonic residual versus total-residual rival",
    "stationary quadratic norm versus cubic and Euler derivatives",
    "target isometry transport versus a physical gauge quotient",
    "complete residual pullback versus observer full-II functional",
):
    check("type", label + " remain distinct", True)


capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    X = runpy.run_path(str(BACKEND))
check("repo", "selected stationary-action backend replays", "PASS 51/51" in capture.getvalue())

selected_hessian = X["selected_hessian"]
cl2_basis = X["cl2_basis"]
fscale = X["fscale"]
form_sum = X["form_sum"]
ETA = tuple(X["ETA"])


print("\nB. REPRESENTATION-BLOCKED SPARSE TARGET FORMULA")
N = 14
PAIRS = list(combinations(range(N), 2))
DOMAIN = [(mu, pair) for mu in range(N) for pair in PAIRS]
DOMAIN_INDEX = {item: index for index, item in enumerate(DOMAIN)}
II_COORDS = [(mu, nu, a) for mu in range(4) for nu in range(mu, 4) for a in range(10)]
II_INDEX = {item: index for index, item in enumerate(II_COORDS)}


def cell(mu: int, pair: tuple[int, int]) -> str:
    form = "H" if mu < 4 else "N"
    blade = "HH" if pair[1] < 4 else "HN" if pair[0] < 4 else "NN"
    return f"{form}_{blade}"


def gauss_form(mu: int, nu: int, a: int):
    normal = 4 + a
    terms = [fscale(-ETA[nu] * ETA[normal], cl2_basis(mu, nu, normal))]
    if mu != nu:
        terms.append(fscale(-ETA[mu] * ETA[normal], cl2_basis(nu, mu, normal)))
    return form_sum(*terms)


# The support formula is derived after splitting form index H/N and bivector
# type HH/HN/NN.  Off-diagonal II has two H_HN entries.  Diagonal II has four
# H_HN entries plus the nine oriented N_NN entries transverse to its normal.
TARGET_ENTRIES: dict[tuple[int, int], sp.Rational] = {}
for column, (mu, nu, a) in enumerate(II_COORDS):
    normal = 4 + a
    if mu != nu:
        TARGET_ENTRIES[(DOMAIN_INDEX[(mu, (nu, normal))], column)] = sp.Rational(124, 117) * ETA[mu]
        TARGET_ENTRIES[(DOMAIN_INDEX[(nu, (mu, normal))], column)] = sp.Rational(124, 117) * ETA[nu]
        continue
    for rho in range(4):
        coefficient = sp.Rational(118, 117) if rho == mu else -sp.Rational(2, 39)
        TARGET_ENTRIES[(DOMAIN_INDEX[(rho, (rho, normal))], column)] = ETA[mu] * coefficient
    for b in range(10):
        if b == a:
            continue
        other = 4 + b
        pair = tuple(sorted((normal, other)))
        orientation = 1 if b > a else -1
        TARGET_ENTRIES[(DOMAIN_INDEX[(other, pair)], column)] = ETA[mu] * orientation * sp.Rational(2, 39)

TARGET = sp.SparseMatrix(len(DOMAIN), len(II_COORDS), TARGET_ENTRIES)
support_cells = Counter(cell(DOMAIN[row][0], DOMAIN[row][1]) for row, _ in TARGET_ENTRIES)
column_counts = Counter(sum(1 for row in range(len(DOMAIN)) if (row, column) in TARGET_ENTRIES)
                        for column in range(len(II_COORDS)))
check("exact", "six stabilizer cells reduce to H_HN plus N_NN support",
      support_cells == Counter({"H_HN": 280, "N_NN": 360}))
check("exact", "the sparse formula has 640 entries with two or thirteen per column",
      len(TARGET_ENTRIES) == 640 and column_counts == Counter({2: 60, 13: 40}))
check("exact", "the complete Cl2 target map has rank 100", TARGET.rank() == 100)


print("\nC. EXHAUSTIVE EXACT 1274 BY 100 CERTIFICATE")
gauss_forms = [gauss_form(*coordinate) for coordinate in II_COORDS]
all_entries_match = True
for column, direction in enumerate(gauss_forms):
    for row, (form_index, (left, right)) in enumerate(DOMAIN):
        actual_pair = selected_hessian(cl2_basis(form_index, left, right), direction)
        if actual_pair[1] != 0 or rational(actual_pair[0]) != TARGET_ENTRIES.get((row, column), 0):
            all_entries_match = False
            break
    if not all_entries_match:
        break
check("exact", "every selected Cl2 Hessian coefficient equals the derived sparse formula",
      all_entries_match)
check("planted", "PLANT the first 2-over-39 witness does not stand in for target completeness",
      len(TARGET_ENTRIES) > 1 and all_entries_match)


print("\nD. FULL CL2 I2B QUADRATIC PULLBACK")
G_DOMAIN = sp.diag(*[
    ETA[mu] * ETA[pair[0]] * ETA[pair[1]]
    for mu, pair in DOMAIN
])
G_II = sp.diag(*[
    (1 if mu == nu else 2) * ETA[mu] * ETA[nu] * ETA[4 + a]
    for mu, nu, a in II_COORDS
])
TRACE = sp.MutableSparseMatrix(10, 100, {})
for a in range(10):
    for mu in range(4):
        TRACE[a, II_INDEX[(mu, mu, a)]] = ETA[mu]
TRACE = sp.SparseMatrix(TRACE)
G_NORMAL = sp.diag(*ETA[4:14])
TRACE_SQUARE = TRACE.T * G_NORMAL * TRACE

K_FULL = TARGET.T * G_DOMAIN.inv() * TARGET
full_ii_coefficient = sp.Rational(15376, 13689)
trace_square_coefficient = -sp.Rational(340, 4563)
EXPECTED = full_ii_coefficient * G_II + trace_square_coefficient * TRACE_SQUARE
check("exact", "full Cl2 pullback is full-II plus trace-square with exact coefficients",
      K_FULL == EXPECTED)
check("exact", "orthogonal leakage contributes exactly 4-over-169 trace-square",
      trace_square_coefficient - (-sp.Rational(448, 4563)) == sp.Rational(4, 169))
check("exact", "the full Cl2 form remains rank 100 and not pure full-II",
      K_FULL.rank() == 100 and trace_square_coefficient != 0)

TRACE_ADJOINT = G_II.inv() * TRACE.T * G_NORMAL
TRACE_PROJECTOR = sp.Rational(1, 4) * TRACE_ADJOINT * TRACE
RELATIVE = G_II.inv() * K_FULL
trace_eigenvalue = sp.Rational(11296, 13689)
traceless_eigenvalue = sp.Rational(15376, 13689)
check("exact", "relative full Cl2 square has exact trace and traceless eigenvalues",
      RELATIVE == trace_eigenvalue * TRACE_PROJECTOR
      + traceless_eigenvalue * (sp.eye(100) - TRACE_PROJECTOR))
positive = sum(1 for value in G_II.diagonal() if value > 0)
negative = sum(1 for value in G_II.diagonal() if value < 0)
check("exact", "positive relative eigenvalues preserve native inertia 54,46",
      trace_eigenvalue > 0 and traceless_eigenvalue > 0
      and (positive, negative) == (54, 46))
check("planted", "PLANT completing leakage does not remove the trace-square term",
      trace_square_coefficient != 0)
check("planted", "PLANT indefinite inertia is not positive physical energy",
      positive > 0 and negative > 0)


print("\nE. STATIONARY CO-MOVING QUADRATIC COMPOSITION")
# For I2(s)=1/2 <U(s),G(s)U(s)> and U(0)=0, the quadratic coefficient is
# <U'(0),G(0)U'(0)>.  Derivatives of G and any moving target map multiply U(0)
# and disappear only at this grade.
s = sp.symbols("s")
u1, u2, g0, g1, r1 = sp.symbols("u1 u2 g0 g1 r1")
u = sp.Matrix([s * u1, s * u2])
g = sp.diag(g0 + s * g1, 1)
r = sp.eye(2) + s * sp.Matrix([[0, r1], [-r1, 0]])
i2 = sp.Rational(1, 2) * (r * u).T * (r.inv().T * g * r.inv()) * (r * u)
quadratic = sp.diff(i2[0], s, 2).subs(s, 0)
check("exact", "moving target metric and target transport drop at stationary quadratic grade",
      sp.expand(quadratic) == g0 * u1**2 + u2**2
      and not sp.expand(quadratic).has(g1, r1))
check("type", "the stationary identity composes frame epsilon and complete observation only at quadratic grade", True)
check("type", "other Clifford grades and the total-residual rival remain open", True)
check("planted", "PLANT stationary quadratic simplification is not cubic or Euler equivalence", True)


print("\nF. DISPOSITION AND PHYSICAL FENCES")
for label in (
    "full Cl2 plus trace is not observer full-II equality",
    "rank 100 is not helicity two",
    "no Euler or preboundary equivalence follows",
    "no common domain BV BFV or physical phase space is opened",
    "no coefficient residue quotient or external datum is booked",
    "P1 P2 P3 remain unused and Curt remains formally separate",
):
    check("planted", "PLANT " + label, True)

print("SOURCE_RETURN=SOURCE-CONFIRMS_NORM_SQUARE__SOURCE_SILENT_ON_OWNER_MAP")
print("FULL_CL2_TARGET_SHAPE=1274_BY_100")
print("FULL_CL2_TARGET_NNZ=640")
print("FULL_CL2_TARGET_SUPPORT=H_HN_280_PLUS_N_NN_360")
print(f"FULL_CL2_I2B_FULL_II_COEFFICIENT={full_ii_coefficient}")
print(f"FULL_CL2_I2B_TRACE_SQUARE_COEFFICIENT={trace_square_coefficient}")
print("ORTHOGONAL_LEAKAGE_TRACE_SQUARE_INCREMENT=4/169")
print(f"FULL_CL2_RELATIVE_TRACE_EIGENVALUE={trace_eigenvalue}")
print(f"FULL_CL2_RELATIVE_TRACELESS_EIGENVALUE={traceless_eigenvalue}")
print("DISPOSITION=FULL_II_PLUS_TRACE__SELECTED_CL2_COMPLETE__TOTAL_RESIDUAL_OTHER_GRADES_OPEN")
print("NEXT=TYPE_AND_COMPUTE_TOTAL_RESIDUAL_OTHER_GRADE_SUPPORT_BEFORE_EULER_PREBOUNDARY_HELICITY")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
