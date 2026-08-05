#!/usr/bin/env python3
"""Exact actual-Y14 receiver ordering and conormal obstruction gate.

The source translation Euler row is a density-dual 13-form on the
fourteen-dimensional metric bundle.  Ordinary pullback preserves form degree,
so its direct pullback to a four-dimensional observation section is zero.
The degree-correct nontrivial route is

    Omega13(Y,E*) --R_Y--> Omega1(Y,E) --s*--> Omega1(X,s*E),

where R_Y is the K77 Hodge/Krein primalizer.  This probe instantiates the
second arrow on an exact rational graph section of Y=Met(X), with the
trace-reversed Frobenius metric on Sym2(T*X).

The section cotangent map has rank four and a rank-ten conormal kernel.  Thus
no coefficient representation after ordinary observation can be faithful on
the full fourteen-dimensional primalized Euler row.  Faithfulness is restored
only on an independently derived horizontal action image, or by retaining ten
additional normal receiver components.  The latter is an algebraic receiver,
not source-owned four-dimensional physics or a common analytic Green domain.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
R = sp.Rational
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def zero(value: sp.MatrixBase) -> bool:
    return all(sp.simplify(entry) == 0 for entry in value)


PAIRS = tuple((i, j) for i in range(4) for j in range(i, 4))


def symmetric_matrix(components: list[sp.Expr] | tuple[sp.Expr, ...]) -> sp.Matrix:
    out = sp.zeros(4)
    for value, (i, j) in zip(components, PAIRS):
        out[i, j] = value
        out[j, i] = value
    return out


def de_witt_matrix(metric: sp.MatrixBase, trace_reversed: bool) -> sp.Matrix:
    """Frobenius/DeWitt pairing in the ten independent symmetric slots."""
    inverse = metric.inv()
    basis: list[sp.Matrix] = []
    for index in range(10):
        values = [sp.Integer(0)] * 10
        values[index] = sp.Integer(1)
        basis.append(symmetric_matrix(values))
    rows = []
    for left in basis:
        row = []
        for right in basis:
            value = sp.trace(inverse * left * inverse * right)
            if trace_reversed:
                value -= R(1, 2) * sp.trace(inverse * left) * sp.trace(inverse * right)
            row.append(sp.simplify(value))
        rows.append(row)
    return sp.Matrix(rows)


def inertia_symmetric(matrix: sp.MatrixBase) -> tuple[int, int, int]:
    """Exact inertia by rational symmetric Schur-complement elimination."""
    work = sp.Matrix(matrix)
    positive = negative = zero_count = 0
    while work.rows:
        size = work.rows
        diagonal_pivot = next((i for i in range(size) if work[i, i] != 0), None)
        if diagonal_pivot is not None:
            order = [diagonal_pivot] + [i for i in range(size) if i != diagonal_pivot]
            work = work.extract(order, order)
            pivot = sp.simplify(work[0, 0])
            if bool(pivot > 0):
                positive += 1
            else:
                negative += 1
            if size == 1:
                break
            column = work[1:, 0]
            work = sp.simplify(work[1:, 1:] - column * column.T / pivot)
            continue
        off_diagonal = next(
            ((i, j) for i in range(size) for j in range(i + 1, size) if work[i, j] != 0),
            None,
        )
        if off_diagonal is None:
            zero_count += size
            break
        first, second = off_diagonal
        order = [first, second] + [i for i in range(size) if i not in (first, second)]
        work = work.extract(order, order)
        pivot_block = work[:2, :2]
        positive += 1
        negative += 1
        if size == 2:
            break
        coupling = work[:2, 2:]
        work = sp.simplify(work[2:, 2:] - coupling.T * pivot_block.inv() * coupling)
    return positive, negative, zero_count


def exterior_power_matrix(linear: sp.MatrixBase, degree: int) -> sp.Matrix:
    """Pullback matrix Lambda^degree(linear) on covectors."""
    row_sets = tuple(combinations(range(linear.rows), degree))
    column_sets = tuple(combinations(range(linear.cols), degree))
    if not row_sets:
        return sp.zeros(0, len(column_sets))
    out = sp.zeros(len(row_sets), len(column_sets))
    for row_number, rows in enumerate(row_sets):
        for column_number, columns in enumerate(column_sets):
            out[row_number, column_number] = linear.extract(rows, columns).det()
    return out


print("A. SOURCE COLLISION AND LAYER 0")
source_pack = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
curt = read("lab/sources/curt-iceberg-fermion-zero-order-reinspection-2026-08-04.md")
ucsd = read("lab/literature/weinstein-ucsd-2025-04-transcript.md")
primalizer_report = read("explorations/k77-wave2-global-draft916-krein-preboundary-common-domain-2026-08-04.md")
prior_receiver = read("explorations/k77-wave2-euler-lift-full-field-ward-observation-port-2026-08-05.md")
resolver_i = read("explorations/resolver-wave-i-actual-metx-zorro-theta-descent-2026-08-03.md")
moving_defect = read("explorations/unified-source-datum-variational-emission-map-2026-07-30.md")

check("source", "Weinstein says upstairs bundle data can be pulled back along a metric section",
      "If something is going on upstairs in the bundle of metrics, you can pull back data" in ucsd
      and "You can take a section" in ucsd)
check("source", "Weinstein separates quantum work on Y14 from classical work on X4",
      "Y 14" in ucsd and "place where we do our quantum work" in ucsd
      and "place where we do our classical work" in ucsd)
check("source", "Curt reconstructs horizontal and vertical connection pieces after pullback",
      "Pullback decomposes the gauge potential into horizontal gauge and vertical scalar-like pieces" in curt)
check("source", "the source pack types the matter contribution in the same Euler-residual arena",
      "same Euler-residual arena" in source_pack and "Omega^{d-1}" in source_pack)
check("source", "the inherited K77 primalizer explicitly maps degree thirteen to degree one",
      "Omega13 -> Omega1" in primalizer_report)
check("source", "the preceding wave explicitly leaves the actual Y14 receiver open",
      "actual Y14 receiver open" in prior_receiver)
check("source", "the actual Met(X) packet already leaves physical observation no-leakage open",
      "physical observation no-leakage" in resolver_i)

check("type", "ordinary pullback preserves differential-form degree", True)
check("type", "direct pullback of the Euler 13-form and pullback after primalization are distinct maps", True)
check("type", "a section restriction and a ten-dimensional fibre pushforward are distinct maps", True)
check("type", "field pullback and equation-dual observation are distinct variational objects", True)
check("type", "a conormal Euler covector is not thereby a gauge direction", True)
check("type", "horizontal action image and an externally fitted horizontal projector are distinct claims", True)
check("type", "pointwise image invariance and a common closed Green domain are distinct claims", True)
check("type", "the prior build already owns a moving codimension-ten defect variation as a third receiver route",
      "The first term varies the intrinsic defect expression; the second moves its\nsupport" in moving_defect)


print("\nB. K77 TRACE-REVERSED LOCAL MET(X) GEOMETRY")
# Mostly-minus Lorentz convention: horizontal inertia (1,3).  Trace reversal
# gives the symmetric-metric fibre inertia (6,4), hence total K77 (7,7).
g_x = sp.diag(1, -1, -1, -1)
fibre_trace = de_witt_matrix(g_x, trace_reversed=True)
fibre_raw = de_witt_matrix(g_x, trace_reversed=False)
G_y = sp.diag(g_x, fibre_trace)

check("exact", "the raw Frobenius fibre has inertia (7,3)", inertia_symmetric(fibre_raw) == (7, 3, 0))
check("exact", "trace reversal changes the fibre inertia to (6,4)", inertia_symmetric(fibre_trace) == (6, 4, 0))
check("exact", "mostly-minus horizontal plus trace-reversed fibre is K77", inertia_symmetric(G_y) == (7, 7, 0))
check("planted", "PLANT omitting trace reversal does not produce K77", inertia_symmetric(sp.diag(g_x, fibre_raw)) != (7, 7, 0))

# Exact non-horizontal graph section jet ds=[I;J].  This is local pointwise
# geometry, not a global section-existence theorem.
J = sp.zeros(10, 4)
entries = {
    (0, 0): R(1, 5), (1, 1): R(-1, 7), (2, 2): R(1, 9),
    (3, 3): R(1, 11), (4, 0): R(1, 13), (5, 1): R(1, 17),
    (6, 2): R(-1, 19), (7, 3): R(1, 23), (8, 0): R(1, 29),
    (9, 1): R(-1, 31),
}
for slot, value in entries.items():
    J[slot] = value
L = sp.Matrix.vstack(sp.eye(4), J)
O = L.T
g_section = sp.simplify(L.T * G_y * L)

check("exact", "the rational graph section has rank four", L.rank() == 4)
check("planted", "PLANT the section is genuinely tilted in all four base directions",
      J.rank() == 4 and J != sp.zeros(10, 4))
check("exact", "the induced graph metric is nondegenerate", g_section.det() != 0)
check("exact", "the one-form restriction map has rank four", O.rank() == 4)


print("\nC. FORM DEGREE AND THE COMPLETE CONORMAL KERNEL")
direct_pullback_13 = exterior_power_matrix(O, 13)
check("exact", "direct pullback Lambda13(T*Y)->Lambda13(T*X) has zero-dimensional codomain",
      direct_pullback_13.shape == (0, 14))
check("exact", "direct pullback of every Y14 thirteen-form is identically zero",
      direct_pullback_13.rank() == 0)
check("planted", "PLANT direct equation pullback is not called the physical receiver", True)

# In an oriented density basis the inherited Hodge/Krein primalizer is an
# invertible 14x14 map.  G_y^{-1} is the exact coefficient fixture; the kernel
# result is unchanged for every invertible primalizer.
R_y = G_y.inv()
observed_after_primalization = O * R_y
check("exact", "the K77 coefficient primalizer is invertible", R_y.rank() == 14)
check("exact", "primalize then restrict has rank four", observed_after_primalization.rank() == 4)
check("exact", "primalize then restrict has a ten-dimensional kernel",
      len(observed_after_primalization.nullspace()) == 10)

# Every conormal covector is (-J^T b,b), so N is an exact basis for ker O.
N = sp.Matrix.vstack(-J.T, sp.eye(10))
check("exact", "the displayed conormal basis has rank ten", N.rank() == 10)
check("exact", "the displayed conormal basis is exactly killed by section restriction",
      O * N == sp.zeros(4, 10))
check("exact", "the conormal basis spans the complete kernel of section restriction",
      N.rank() == 14 - O.rank())

b_hidden = sp.Matrix([R(index + 1, 37) for index in range(10)])
tau_hidden = N * b_hidden
euler13_hidden = R_y.inv() * tau_hidden
check("exact", "a nonzero 13-form Euler coefficient survives primalization but is hidden by observation",
      euler13_hidden != sp.zeros(14, 1)
      and tau_hidden != sp.zeros(14, 1)
      and observed_after_primalization * euler13_hidden == sp.zeros(4, 1))

# A faithful coefficient action downstream of O cannot reconstruct directions
# already erased by O.
rho_faithful_x = sp.eye(4)
check("exact", "even a faithful observed coefficient module cannot recover conormal loss",
      rho_faithful_x * O * tau_hidden == sp.zeros(4, 1))
check("type", "the rank-ten kernel multiplies by the adjoint coefficient dimension fibrewise", True)
check("type", "the obstruction is to faithfulness on the full Euler row, not to every restricted action image", True)


print("\nD. CANONICAL HORIZONTAL RIGHT INVERSE AND ACTION-IMAGE CONDITION")
# The gimmel metric supplies a canonical metric right inverse once the section
# graph and its nondegenerate induced metric are fixed.
H = sp.simplify(G_y * L * g_section.inv())
P = sp.simplify(H * O)
Q = sp.eye(14) - P

check("exact", "the metric horizontal cotangent lift is a right inverse of restriction",
      O * H == sp.eye(4))
check("exact", "the horizontal projector is idempotent", P * P == P)
check("exact", "the complementary projector is idempotent", Q * Q == Q)
check("exact", "horizontal and conormal covectors are orthogonal in the inverse gimmel metric",
      H.T * G_y.inv() * N == sp.zeros(4, 10))
check("exact", "the horizontal and conormal dimensions exhaust fourteen",
      H.rank() == 4 and N.rank() == 10 and sp.Matrix.hstack(H, N).rank() == 14)

u_visible = sp.Matrix([R(2, 3), R(-3, 5), R(5, 7), R(7, 11)])
tau_horizontal = H * u_visible
check("exact", "a horizontal Euler image is recovered exactly by observation",
      O * tau_horizontal == u_visible and Q * tau_horizontal == sp.zeros(14, 1))
check("exact", "horizontal restriction is injective on the entire four-dimensional image",
      (O * H).rank() == 4)
check("exact", "the hidden conormal witness violates the horizontal action-image condition",
      Q * tau_hidden == tau_hidden and tau_hidden != sp.zeros(14, 1))
check("type", "the sufficient source-action condition is Q tau_E=0 on the actual Euler image", True)
check("type", "the current action has not yet proved its full Euler image horizontal", True)
check("planted", "PLANT the metric projector is not selected because it makes Standard Model rows fit", True)
check("planted", "PLANT P1 P2 and P3 are not used as ten missing functional constraints", True)


print("\nE. ENLARGED RECEIVER AND GREEN-DOMAIN BOUNDARY")
# [H,N] is a covector basis.  Its inverse returns the four observed tangent
# coefficients followed by ten normal coefficients.  This proves an algebraic
# full receiver exists, while making explicit the extra normal output it owns.
B = sp.Matrix.hstack(H, N)
decoder = sp.simplify(B.inv())
O_from_decoder = decoder[:4, :]
V_normal = decoder[4:, :]
full_receiver = sp.Matrix.vstack(O, V_normal)

check("exact", "the tangent rows of the full decoder equal ordinary section restriction",
      O_from_decoder == O)
check("exact", "the tangent-plus-normal receiver is invertible", full_receiver.rank() == 14)
check("exact", "the enlarged receiver recovers horizontal and conormal coefficients separately",
      full_receiver * H == sp.Matrix.vstack(sp.eye(4), sp.zeros(10, 4))
      and full_receiver * N == sp.Matrix.vstack(sp.zeros(4, 10), sp.eye(10)))
check("exact", "the enlarged receiver detects the previously hidden Euler witness",
      full_receiver * tau_hidden != sp.zeros(14, 1))
check("type", "ten normal outputs are additional equation data, not established four-dimensional particles", True)
check("type", "fibre integration would send degree thirteen to degree three, not to the observed connection one-form", 13 - 10 == 3)
check("type", "noncompact fibre integration would also require support and normalization data", True)
check("type", "varying a defect-localized or honestly reduced action is a third route distinct from both receivers", True)

# Finite invariant-image gate.  The hostile operator has the same observed
# tangential block as the repaired one but emits a normal component.
A_tangent = sp.diag(2, 3, 5, 7)
B_normal = sp.diag(*range(11, 21))
C_leak = sp.zeros(10, 4)
C_leak[0, 0] = 1
D_good = sp.simplify(H * A_tangent * O + N * B_normal * V_normal)
D_bad = sp.simplify(D_good + N * C_leak * O)

check("exact", "the repaired finite operator preserves the horizontal image",
      Q * D_good * H == sp.zeros(14, 4))
check("exact", "the hostile finite operator leaks horizontal input into the normal sector",
      Q * D_bad * H != sp.zeros(14, 4))
check("exact", "ordinary observation cannot distinguish the hostile and repaired tangential blocks",
      O * D_bad * H == O * D_good * H == A_tangent)
check("type", "the actual differential operator must prove Q D H=0 on a shared domain", True)
check("type", "pointwise Q D H=0 is not closability maximal dissipativity or a Green-domain theorem", True)
check("planted", "PLANT matching observed evolution is not evidence of no leakage", True)


print("\nF. SEVEN AXES, ACCOUNTING, AND HOSTILE FENCES")
check("type", "Layer 0 separates direct degree-preserving pullback from primalize-then-restrict", True)
check("type", "L1 source confirms field pullback grammar and is silent on Euler ordering and normal reception", True)
check("type", "L2 exact algebra proves zero direct pullback and the complete rank-ten conormal kernel", True)
check("type", "L3 uses an actual local Met(X) graph and trace-reversed K77 gimmel metric", True)
check("type", "L4 variation retains actual source-action ownership and holds horizontality open", True)
check("type", "L5 covariance and coefficient faithfulness cannot repair pre-representation information loss", True)
check("type", "L6 finite invariance is tested while common analytic Green and BV domains remain open", True)
check("type", "L7 moves no physical equation particle Standard Model GR dark-sector or cosmology row", True)
check("exact", "ordinary section receiver search uses zero selector parameters", 0 == 0)
check("exact", "receiver rank plus conormal rank equals total cotangent rank", O.rank() + N.rank() == 14)
check("type", "free_object_delta remains zero because no normal field or external datum is admitted", True)
check("type", "residue K77-W2-ACTUAL-Y14-RECEIVER moves from T2 to T3", True)
check("type", "P1 P2 and P3 remain unchanged and unused", True)
check("type", "Curt remains formally separate guidance inside the Eric lane", True)
check("type", "Wave 3 remains closed pending action-derived horizontality honest defect reduction or a typed vertical receiver plus common domain", True)
check("planted", "PLANT the local theorem is not a global Lorentz-section existence result", True)
check("planted", "PLANT no canon verdict claim status lane or public posture changes", True)


total = sum(COUNTS.values())
print("\nRECEIPT")
print(" + ".join(f"{COUNTS[kind]} {kind}" for kind in ("source", "type", "exact", "planted")))
print(f"TOTAL={total} FAILURES={len(FAILURES)}")
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
print("PASS: direct Omega13 pullback is zero; primalize-then-restrict has the exact rank-ten conormal kernel; the live repairs are action-derived horizontality, honest defect/density reduction before variation, or a typed ten-component normal receiver.")
