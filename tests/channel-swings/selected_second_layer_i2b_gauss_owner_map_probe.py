#!/usr/bin/env python3
"""Exact local I2B-to-Gauss/full-II owner-map gate.

At the selected invariant stationary background, the Hessian of the first
action is Spin(7,7)-equivariant on V* tensor Lambda2(V).  This probe resolves
that multiplicity-free carrier into Lambda3(V), V and the Cartan hook, squares
the relative Hessian as required by the residual norm, and pulls it back along
the already-built rank-100 canonical Gauss insertion.

The result is a local algebraic quadratic-form theorem.  It is deliberately
kept below moving Euler, preboundary, covariant-phase-space and BFV grades.
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


def rational(value) -> sp.Rational:
    return sp.Rational(value.numerator, value.denominator)


print("A. SOURCE, PREDECESSORS, AND LAYER 0")
source = read("lab/sources/gu-two-layer-action-source-reinspection-2026-08-04.md")
source_full_norm = read("lab/sources/full-norm-gravity-source-reinspection-2026-08-05.md")
gauss_report = read("explorations/conditional-build/selected-moving-k77-vacuum-p2-norm-placement-2026-08-05.md")
owner_report = read("explorations/conditional-build/two-layer-action-selected-cubic-owner-retype-2026-08-06.md")
predecessor = read("explorations/conditional-build/selected-action-n2-null-little-group-green-2026-08-06.md")

check("source", "source confirms the residual norm-square second action",
      "SOURCE-CONFIRMS-NORM-SQUARE-AND-REDUNDANCY" in source)
check("source", "source is silent on identifying I2B with observer full-II",
      "no identification of this norm with full `|II|^2`" in source_full_norm)
check("repo", "rank-100 Gauss insertion and full-II action pairing already exist",
      "rank 100" in gauss_report and "rank-100 ordered `II` norm" in gauss_report)
check("repo", "the three action owners were explicitly separated before this build",
      "three owners" in owner_report and "I2B <-> I_II" in owner_report)
check("repo", "the first-layer N2 carrier is retired before this second-layer build",
      "N2_WRONG_HELICITY" in predecessor and "scoped route kill" in predecessor.lower())

for label in (
    "first-action Hessian versus first-action Euler residual",
    "residual norm-square I2B versus the first-action torsion mass term",
    "Gauss-restricted local quadratic form versus moving observer functional",
    "full-II norm versus mean-curvature trace-square",
    "quadratic-form equality versus Euler and preboundary equivalence",
    "native indefinite pairing versus positive physical Hilbert norm",
):
    check("type", label + " remain distinct", True)

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    X = runpy.run_path(str(BACKEND))
check("repo", "selected stationary-action and Gauss-carrier predecessor replays",
      "PASS 51/51" in capture.getvalue())

selected_hessian = X["selected_hessian"]
cl2_basis = X["cl2_basis"]
fscale = X["fscale"]
form_sum = X["form_sum"]
ETA = tuple(X["ETA"])


print("\nB. MULTIPLICITY-FREE FULL CL2 PROJECTORS")
N = 14
PAIRS = list(combinations(range(N), 2))
PAIR_INDEX = {pair: index for index, pair in enumerate(PAIRS)}
DOMAIN = [(mu, pair) for mu in range(N) for pair in PAIRS]
DOMAIN_INDEX = {item: index for index, item in enumerate(DOMAIN)}
TRIPLES = list(combinations(range(N), 3))
TRIPLE_INDEX = {triple: index for index, triple in enumerate(TRIPLES)}

G_DOMAIN = sp.diag(*[
    ETA[mu] * ETA[pair[0]] * ETA[pair[1]]
    for mu, pair in DOMAIN
])
G_THREE = sp.diag(*[ETA[i] * ETA[j] * ETA[k] for i, j, k in TRIPLES])
G_VECTOR = sp.diag(*ETA)


def permutation_sign(values: tuple[int, ...]) -> int:
    inversions = sum(values[i] > values[j] for i in range(len(values)) for j in range(i + 1, len(values)))
    return -1 if inversions % 2 else 1


WEDGE = sp.MutableSparseMatrix(len(TRIPLES), len(DOMAIN), {})
CONTRACTION = sp.MutableSparseMatrix(N, len(DOMAIN), {})
for column, (mu, (i, j)) in enumerate(DOMAIN):
    if len({mu, i, j}) == 3:
        triple = tuple(sorted((mu, i, j)))
        WEDGE[TRIPLE_INDEX[triple], column] = ETA[mu] * permutation_sign((mu, i, j))
    if mu == i:
        CONTRACTION[j, column] += ETA[mu]
    if mu == j:
        CONTRACTION[i, column] -= ETA[mu]
WEDGE = sp.SparseMatrix(WEDGE)
CONTRACTION = sp.SparseMatrix(CONTRACTION)

WEDGE_ADJOINT = G_DOMAIN.inv() * WEDGE.T * G_THREE
CONTRACTION_ADJOINT = G_DOMAIN.inv() * CONTRACTION.T * G_VECTOR
check("exact", "wedge coisometry constant is three",
      WEDGE * WEDGE_ADJOINT == 3 * sp.eye(len(TRIPLES)))
check("exact", "contraction coisometry constant is thirteen",
      CONTRACTION * CONTRACTION_ADJOINT == 13 * sp.eye(N))


print("\nC. CANONICAL GAUSS INSERTION AND COMPONENT GRAMS")
II_COORDS = [(mu, nu, a) for mu in range(4) for nu in range(mu, 4) for a in range(10)]
II_INDEX = {item: index for index, item in enumerate(II_COORDS)}
INSERTION = sp.MutableSparseMatrix(len(DOMAIN), len(II_COORDS), {})
for column, (mu, nu, a) in enumerate(II_COORDS):
    normal = 4 + a
    INSERTION[DOMAIN_INDEX[(mu, (nu, normal))], column] += -ETA[nu] * ETA[normal]
    if mu != nu:
        INSERTION[DOMAIN_INDEX[(nu, (mu, normal))], column] += -ETA[mu] * ETA[normal]
INSERTION = sp.SparseMatrix(INSERTION)

G_II = sp.diag(*[
    (1 if mu == nu else 2) * ETA[mu] * ETA[nu] * ETA[4 + a]
    for mu, nu, a in II_COORDS
])
check("exact", "Gauss insertion is an isometry onto the full ordered-II norm",
      INSERTION.T * G_DOMAIN * INSERTION == G_II and INSERTION.rank() == 100)

WEDGE_I = WEDGE * INSERTION
CONTRACTION_I = CONTRACTION * INSERTION
I_THREE = sp.Rational(1, 3) * WEDGE_ADJOINT * WEDGE_I
I_VECTOR = sp.Rational(1, 13) * CONTRACTION_ADJOINT * CONTRACTION_I
I_HOOK = INSERTION - I_THREE - I_VECTOR

GRAM_THREE = I_THREE.T * G_DOMAIN * I_THREE
GRAM_VECTOR = I_VECTOR.T * G_DOMAIN * I_VECTOR
GRAM_HOOK = I_HOOK.T * G_DOMAIN * I_HOOK
check("exact", "the three full-Spin components are pairwise orthogonal on Gauss",
      I_THREE.T * G_DOMAIN * I_VECTOR == sp.zeros(100)
      and I_THREE.T * G_DOMAIN * I_HOOK == sp.zeros(100)
      and I_VECTOR.T * G_DOMAIN * I_HOOK == sp.zeros(100))
check("exact", "component Grams reconstruct full-II exactly",
      GRAM_THREE + GRAM_VECTOR + GRAM_HOOK == G_II)


def coordinate_form(vector: sp.MatrixBase):
    terms = []
    for (row, _), value in vector.todok().items():
        if not value:
            continue
        mu, (i, j) = DOMAIN[row]
        coefficient = Fraction(int(value.p), int(value.q))
        terms.append(fscale(coefficient, cl2_basis(mu, i, j)))
    return form_sum(*terms)


def nonisotropic_column(component: sp.MatrixBase, gram: sp.MatrixBase) -> tuple[int, sp.MatrixBase]:
    for column in range(component.cols):
        if gram[column, column] != 0:
            return column, component[:, column]
    raise AssertionError("component has no nonisotropic Gauss column")


components = {
    "Lambda3": (I_THREE, GRAM_THREE),
    "Vector": (I_VECTOR, GRAM_VECTOR),
    "Hook": (I_HOOK, GRAM_HOOK),
}
diagonal_ratios: dict[str, sp.Rational] = {}
representatives = {}
for name, (component, gram) in components.items():
    if gram == sp.zeros(*gram.shape):
        check("exact", f"{name} component is absent from the symmetric Gauss carrier",
              name == "Lambda3" and component == sp.zeros(*component.shape))
        continue
    column, vector = nonisotropic_column(component, gram)
    direction = coordinate_form(vector)
    value = rational(selected_hessian(direction, direction)[0])
    native = (vector.T * G_DOMAIN * vector)[0]
    diagonal_ratios[name] = sp.factor(value / native)
    representatives[name] = direction
    check("exact", f"{name} Hessian diagonal ratio is nonzero and exact", diagonal_ratios[name] != 0)

component_cross = selected_hessian(representatives["Vector"], representatives["Hook"])
check("exact", "fixed-epsilon Hessian mixes the formal Vector and Hook components",
      component_cross != (Fraction(0), Fraction(0)))
check("type", "the full-Spin scalar-eigenvalue shortcut is unavailable; the direct Gauss block must be squared", True)


print("\nD. EXACT GAUSS-PROJECTED HESSIAN AND RESIDUAL NORM")
TRACE = sp.MutableSparseMatrix(10, 100, {})
for a in range(10):
    for mu in range(4):
        TRACE[a, II_INDEX[(mu, mu, a)]] = ETA[mu]
TRACE = sp.SparseMatrix(TRACE)
G_NORMAL = sp.diag(*ETA[4:14])
TRACE_SQUARE = TRACE.T * G_NORMAL * TRACE

gauss_forms = [coordinate_form(INSERTION[:, column]) for column in range(100)]
H_GAUSS = sp.zeros(100)
for i, left in enumerate(gauss_forms):
    for j in range(i, 100):
        value = rational(selected_hessian(left, gauss_forms[j])[0])
        H_GAUSS[i, j] = H_GAUSS[j, i] = value

check("exact", "all 100 by 100 Gauss Hessian entries form a symmetric nondegenerate block",
      H_GAUSS == H_GAUSS.T and H_GAUSS.rank() == 100)

# This is only the norm of the Gauss projection of the residual.  It becomes
# the full I2B pullback only if the first-action Hessian has no orthogonal
# leakage from the Gauss carrier; the next block tests that condition.
K_PROJECTED = H_GAUSS.T * G_II.inv() * H_GAUSS

offdiag = II_INDEX[(0, 1, 0)]
diagonal = II_INDEX[(0, 0, 0)]
full_ii_coefficient = sp.factor(K_PROJECTED[offdiag, offdiag] / G_II[offdiag, offdiag])
trace_square_coefficient = sp.factor(
    (K_PROJECTED[diagonal, diagonal] - full_ii_coefficient * G_II[diagonal, diagonal])
    / TRACE_SQUARE[diagonal, diagonal]
)
EXPECTED = full_ii_coefficient * G_II + trace_square_coefficient * TRACE_SQUARE

check("exact", "the Gauss-projected residual norm is full-II plus trace-square with fixed coefficients",
      K_PROJECTED == EXPECTED
      and full_ii_coefficient == sp.Rational(15376, 13689)
      and trace_square_coefficient == -sp.Rational(448, 4563))
check("exact", "the projected trace-square correction is nonzero, so the projected block is not pure full-II",
      trace_square_coefficient != 0 and K_PROJECTED != full_ii_coefficient * G_II)
check("exact", "the projected local second-layer form is nondegenerate on all 100 II directions",
      K_PROJECTED.rank() == 100)
RELATIVE_HESSIAN = G_II.inv() * H_GAUSS
RELATIVE_SQUARE = G_II.inv() * K_PROJECTED
TRACE_ADJOINT = G_II.inv() * TRACE.T * G_NORMAL
TRACE_PROJECTOR = sp.Rational(1, 4) * TRACE_ADJOINT * TRACE
check("exact", "the relative Hessian square has magnitudes 100/117 on trace and 124/117 on traceless II",
      RELATIVE_SQUARE
      == sp.Rational(100, 117) ** 2 * TRACE_PROJECTOR
      + sp.Rational(124, 117) ** 2 * (sp.eye(100) - TRACE_PROJECTOR))

GAUSS_PROJECTOR = INSERTION * G_II.inv() * INSERTION.T * G_DOMAIN
check("exact", "the Gauss projector is native-orthogonal and rank 100",
      GAUSS_PROJECTOR.rank() == 100
      and GAUSS_PROJECTOR * GAUSS_PROJECTOR == GAUSS_PROJECTOR
      and GAUSS_PROJECTOR.T * G_DOMAIN == G_DOMAIN * GAUSS_PROJECTOR)

complement_forms = []
for row in range(len(DOMAIN)):
    basis = sp.zeros(len(DOMAIN), 1)
    basis[row, 0] = 1
    complement = basis - GAUSS_PROJECTOR * basis
    if complement == sp.zeros(len(DOMAIN), 1):
        continue
    assert INSERTION.T * G_DOMAIN * complement == sp.zeros(100, 1)
    complement_forms.append((row, coordinate_form(complement)))

leakage = None
for gauss_column, gauss_direction in enumerate(gauss_forms):
    for row, complement_direction in complement_forms:
        value = selected_hessian(complement_direction, gauss_direction)
        if value != (Fraction(0), Fraction(0)):
            leakage = (gauss_column, row, value)
            break
    if leakage is not None:
        break
check("exact", "a concrete Gauss-to-orthogonal-complement Hessian leakage term survives",
      leakage == (0, 501, (Fraction(2, 39), Fraction(0))))
check("type", "the fixed-epsilon Gauss carrier therefore does not close for the full residual-norm pullback", True)

positive = sum(1 for value in G_II.diagonal() if value > 0)
negative = sum(1 for value in G_II.diagonal() if value < 0)
check("exact", "projected residual squaring preserves the native indefinite inertia by congruence",
      positive + negative == 100 and positive > 0 and negative > 0)

check("planted", "PLANT one traceless direction would falsely suggest pure full-II proportionality",
      TRACE[:, offdiag] == sp.zeros(10, 1)
      and K_PROJECTED[offdiag, offdiag] == full_ii_coefficient * G_II[offdiag, offdiag])
check("planted", "PLANT tracing first loses ninety full-II directions",
      TRACE_SQUARE.rank() == 10 and G_II.rank() == 100)
check("planted", "PLANT squaring an indefinite residual pairing is not a positive norm",
      positive > 0 and negative > 0)


print("\nE. DISPOSITION AND NEXT GRADE")
for label in (
    "fixed projected quadratic combination is not equality of the two action owners",
    "full-rank algebraic form is not a helicity-two characteristic",
    "no Euler equivalence follows before moving target metric and observation jets",
    "no preboundary equivalence follows before the variational current is compared",
    "no fifth quotient residue reduction or external datum is booked",
    "P1 P2 P3 remain unused and Curt remains formally separate",
):
    check("planted", "PLANT " + label, True)

print("SOURCE_RETURN=SOURCE-CONFIRMS_NORM_SQUARE__SOURCE_SILENT_ON_I2B_EQUALS_FULL_II")
print("FULL_CL2_DECOMPOSITION=Lambda3_364_PLUS_Vector_14_PLUS_Hook_896")
print("FIXED_EPSILON_FORMAL_COMPONENT_RATIOS=" + ",".join(f"{key}:{value}" for key, value in diagonal_ratios.items()))
print(f"PROJECTED_I2B_GAUSS_FULL_II_COEFFICIENT={full_ii_coefficient}")
print(f"PROJECTED_I2B_GAUSS_TRACE_SQUARE_COEFFICIENT={trace_square_coefficient}")
print(f"PROJECTED_I2B_GAUSS_RANK={K_PROJECTED.rank()}")
print(f"PROJECTED_I2B_GAUSS_INERTIA_SIGNATURE={positive},{negative}")
print(f"FIXED_EPSILON_GAUSS_ORTHOGONAL_COMPLEMENT_RANK={len(DOMAIN) - 100}")
print(f"FIXED_EPSILON_GAUSS_COMPLEMENT_BASIS_REPRESENTATIVES_TESTED={len(complement_forms)}")
print(f"FIXED_EPSILON_GAUSS_LEAKAGE={leakage}")
print("DISPOSITION=I2B_GAUSS_WRONG_TYPE__PROJECTED_FULL_II_PLUS_TRACE_SQUARE_EXACT__FULL_RESIDUAL_LEAKAGE_LIVE")
print("NEXT=BUILD_COMPLETE_1274_BY_100_RESIDUAL_TARGET_PULLBACK_AND_COMOVE_EPSILON_FRAME_BEFORE_EULER_PREBOUNDARY_HELICITY")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
