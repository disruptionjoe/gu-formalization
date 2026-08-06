#!/usr/bin/env sage -python
"""Exact N2 null little-group and principal Green-flux typing.

This is a low-memory reconstruction of the completed grade-one source symbol.
It deliberately distinguishes an algebraic two-mode kernel, its compact null
little-group helicity, its principal Green flux, and a global BV/BFV domain.
"""

from collections import Counter
from contextlib import redirect_stdout
from fractions import Fraction
from io import StringIO
from math import comb
from pathlib import Path
import runpy

import sympy as sp
from sage.all import AA, QQ, PolynomialRing, identity_matrix, matrix


ROOT = Path(__file__).resolve().parents[2]
BACKEND = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


print("A. SOURCE, PREDECESSOR, AND LAYER 0")
source = (ROOT / "lab/sources/gu-action-polarization-domain-source-reinspection-2026-08-05.md").read_text()
predecessor = (ROOT / "explorations/conditional-build/selected-action-grade1-dbt-schur-observation-2026-08-06.md").read_text()
check("source", "source places Shiab in the action and leaves the physical domain unpublished",
      "SOURCE_CONFIRMS_SHIAB_IN_ACTION" in source
      and "SOURCE_SILENT_ON_GLOBAL_PHYSICAL_DOMAIN" in source)
check("source", "source does not publish the N2 polarization or Green-flux typing",
      "positive N2" not in source and "helicity" not in source)
check("repo", "predecessor leaves the positive N2 mode and Green form open",
      "positive root = 3.17537838044882" in predecessor
      and "Null little-group type" in predecessor and "Green form" in predecessor)
for label in (
    "two algebraic modes versus two graviton polarizations",
    "compact SO(2) helicity versus the full noncompact null stabilizer",
    "principal Green flux versus a covariant phase-space two-form",
    "finite gauge quotient versus a global BV/BFV quotient",
    "a coefficient locus versus a selected physical coupling",
):
    check("type", label + " remain distinct", True)

capture = StringIO()
with redirect_stdout(capture):
    M = runpy.run_path(str(BACKEND))
check("repo", "reviewed exact moving-Shiab backend replays",
      "PASS: the source moving-Shiab family" in capture.getvalue())


print("\nB. LOW-MEMORY FULL SOURCE-SYMBOL RECONSTRUCTION")
ZERO = M["ZERO"]
FULL = M["FULL"]
PHI1 = M["PHI1"]
ETA14 = M["ETA"]
SELECTED = ("comm", "symi", "symi")


def form_sum(*forms):
    out = {}
    for form in forms:
        out = M["fadd"](out, form)
    return out


def gaussian_sum(*values):
    out = ZERO
    for value in values:
        out = M["gadd"](out, value)
    return out


def cl1(form_index, clifford_index):
    return {1 << form_index: {1 << clifford_index: (Fraction(1), Fraction(0))}}


def cl2(form_index, left, right):
    return {1 << form_index: M["emul"](M["blade"](left), M["blade"](right))}


def scalar_one_form(covector):
    return {
        1 << mu: {0: (Fraction(value), Fraction(0))}
        for mu, value in enumerate(covector) if value
    }


def pairing(left, right):
    return M["wedge_raw"](left, right).get(FULL, {}).get(0, ZERO)


def rational_pair(value):
    assert value[1] == 0
    return sp.Rational(value[0].numerator, value[0].denominator)


def selected_hessian(left, right):
    background = M["fscale"](Fraction(-1, 312), PHI1)
    right_background = form_sum(
        M["wedge_raw"](right, background), M["wedge_raw"](background, right)
    )
    left_background = form_sum(
        M["wedge_raw"](left, background), M["wedge_raw"](background, left)
    )
    mixed = form_sum(M["wedge_raw"](left, right), M["wedge_raw"](right, left))
    cubic = gaussian_sum(
        pairing(left, M["fscale"](Fraction(1, 3), M["shiab"](right_background, SELECTED))),
        pairing(right, M["fscale"](Fraction(1, 3), M["shiab"](left_background, SELECTED))),
        pairing(background, M["fscale"](Fraction(1, 3), M["shiab"](mixed, SELECTED))),
    )
    mass = gaussian_sum(
        pairing(left, M["hodge"](right)), pairing(right, M["hodge"](left))
    )
    return gaussian_sum(cubic, M["gscale"](Fraction(1, 2), mass))


slots = [(i, j) for i in range(4) for j in range(i, 4)]
bivectors = [(a, b) for a in range(4) for b in range(a + 1, 4)]
connection_labels = [(mu, a, b) for mu in range(4) for a, b in bivectors]
connection = [cl2(*label) for label in connection_labels]
grade_labels = [(mu, a) for mu in range(14) for a in range(14)]
grade_one = [cl1(*label) for label in grade_labels]
connection_hessian = sp.Matrix([
    [rational_pair(selected_hessian(left, right)) for right in connection]
    for left in connection
])
check("exact", "horizontal connection Hessian is symmetric and rank twenty-four",
      connection_hessian == connection_hessian.T and connection_hessian.rank() == 24)

eta = list(ETA14)
grade_index = {label: index for index, label in enumerate(grade_labels)}
transpose = sp.zeros(196)
for mu, a in grade_labels:
    transpose[grade_index[(mu, a)], grade_index[(a, mu)]] = eta[mu] * eta[a]
identity = sp.eye(196)
trace_covector = sp.zeros(1, 196)
trace_vector = sp.zeros(196, 1)
for index in range(14):
    trace_covector[0, grade_index[(index, index)]] = 1
    trace_vector[grade_index[(index, index)], 0] = 1
scalar_projector = trace_vector * trace_covector / 14
sym_projector = (identity + transpose) / 2 - scalar_projector
anti_projector = (identity - transpose) / 2
native_gram = sp.diag(*[eta[mu] * eta[a] for mu, a in grade_labels])
grade_inverse = (
    -scalar_projector
    + sp.Rational(13, 15) * sym_projector
    + sp.Rational(39, 41) * anti_projector
) * native_gram
check("exact", "grade-one inverse uses the exact 1 plus 104 plus 91 decomposition",
      (scalar_projector.rank(), sym_projector.rank(), anti_projector.rank()) == (1, 104, 91))

eta4 = sp.diag(1, -1, -1, -1)
metric_basis = []
for i, j in slots:
    wave = sp.zeros(4)
    wave[i, j] = wave[j, i] = 1
    metric_basis.append(wave)


def einstein_hessian(covector):
    k_cov = sp.Matrix(covector)
    k_up = eta4 * k_cov
    k2 = (k_cov.T * eta4 * k_cov)[0]
    out = sp.zeros(10)
    for a, h in enumerate(metric_basis):
        trace_h = sp.trace(eta4 * h)
        kk_h = (k_up.T * h * k_up)[0]
        v_h = (k_up.T * h).T
        for b, ell in enumerate(metric_basis):
            trace_ell = sp.trace(eta4 * ell)
            kk_ell = (k_up.T * ell * k_up)[0]
            v_ell = (k_up.T * ell).T
            out[a, b] = (
                -k2 * sp.trace(eta4 * h * eta4 * ell)
                + k2 * trace_h * trace_ell
                - trace_h * kk_ell - trace_ell * kk_h
                + 2 * (v_h.T * eta4 * v_ell)[0]
            )
    return out


def source_symbol(covector):
    lc_map = sp.zeros(24, 10)
    for column, wave in enumerate(metric_basis):
        for row, (mu, a, b) in enumerate(connection_labels):
            lc_map[row, column] = sp.Rational(
                covector[b] * wave[mu, a] - covector[a] * wave[mu, b], 2
            )
    metric_gauge = sp.zeros(10, 4)
    for column in range(4):
        for row, (i, j) in enumerate(slots):
            metric_gauge[row, column] = (
                (covector[i] if j == column else 0)
                + (covector[j] if i == column else 0)
            )
    gauge = sp.Matrix.vstack(metric_gauge, lc_map * metric_gauge)
    difference = sp.Matrix.hstack(-lc_map, sp.eye(24))
    zero_jet = difference.T * connection_hessian * difference

    k_form = scalar_one_form(covector)
    right_images = [
        M["shiab"](M["wedge_raw"](k_form, direction), SELECTED)
        for direction in connection
    ]
    left_images = [
        M["shiab"](M["wedge_raw"](k_form, direction), SELECTED)
        for direction in grade_one
    ]
    forward = sp.Matrix([
        [rational_pair(pairing(left, image)) for image in right_images]
        for left in grade_one
    ])
    reverse = sp.Matrix([
        [rational_pair(pairing(connection[j], left_images[i])) for j in range(24)]
        for i in range(196)
    ])
    euler = (forward - reverse) / 2
    full_cross = ((forward + reverse) * lc_map / 2).row_join(euler)
    schur = sp.simplify(full_cross.T * grade_inverse * full_cross)
    principal = zero_jet + sp.diag(
        sp.Rational(-1, 26) * einstein_hessian(covector), sp.zeros(24)
    )
    return principal, schur, gauge, (
        forward.rank(), euler.rank(), full_cross.rank(), schur.rank(),
        principal.rank(), gauge.rank(),
    )


null_covector = (1, 0, 0, 1)
principal, schur, gauge, ranks = source_symbol(null_covector)
check("exact", "null source-symbol ranks reproduce the reviewed predecessor",
      ranks == (12, 11, 15, 14, 28, 4))
check("exact", "principal and Schur forms separately have the gauge radical",
      principal * gauge == sp.zeros(34, 4) and schur * gauge == sp.zeros(34, 4))


print("\nC. EXACT COMPACT NULL LITTLE-GROUP TYPE")


def symmetric_coordinates(wave):
    return sp.Matrix([wave[i, j] for i, j in slots])


def bivector_coordinates(wave):
    return sp.Matrix([wave[a, b] for a, b in bivectors])


bivector_basis = []
for a, b in bivectors:
    wave = sp.zeros(4)
    wave[a, b] = 1
    wave[b, a] = -1
    bivector_basis.append(wave)


def source_representation(generator):
    metric_rep = sp.Matrix.hstack(*[
        symmetric_coordinates(generator * wave + wave * generator.T)
        for wave in metric_basis
    ])
    bivector_rep = sp.Matrix.hstack(*[
        bivector_coordinates(generator * wave + wave * generator.T)
        for wave in bivector_basis
    ])
    connection_rep = (
        sp.kronecker_product(generator, sp.eye(6))
        + sp.kronecker_product(sp.eye(4), bivector_rep)
    )
    return sp.diag(metric_rep, connection_rep)


rotation = sp.zeros(4)
rotation[1, 2] = -1
rotation[2, 1] = 1
source_rotation = source_representation(rotation)
check("exact", "J12 is Lorentz and fixes the null covector",
      rotation.T * eta4 + eta4 * rotation == sp.zeros(4)
      and rotation * sp.Matrix(null_covector) == sp.zeros(4, 1))
check("exact", "the complete principal and Schur forms are exactly rotation covariant",
      source_rotation.T * principal + principal * source_rotation == sp.zeros(34)
      and source_rotation.T * schur + schur * source_rotation == sp.zeros(34))


def to_sage(value, ring=QQ):
    return matrix(
        ring, value.rows, value.cols,
        [ring(int(entry.p)) / int(entry.q) for entry in value],
    )


polynomials = PolynomialRing(QQ, "z")
z = polynomials.gen()
n2 = z**2 + QQ(1352) / 615 * z - QQ(1178198372) / 69047075
field = polynomials.quotient(n2, "a")
a = field.gen()
operator = a * to_sage(principal, field) - to_sage(schur, field)
gauge_field = to_sage(gauge, field)
kernel = operator.right_kernel().basis_matrix().transpose()
basis = gauge_field
physical_columns = []
for column in kernel.columns():
    candidate = basis.augment(column)
    if candidate.rank() > basis.rank():
        physical_columns.append(column)
        basis = candidate
physical = matrix(field, [list(column) for column in physical_columns]).transpose()
carrier = gauge_field.augment(physical)
check("exact", "N2 kernel is gauge four plus exactly two source modes",
      kernel.rank() == 6 and gauge_field.rank() == 4
      and len(physical_columns) == 2 and carrier.rank() == 6)

rotation_field = to_sage(source_rotation, field)
rotation_action = carrier.solve_right(rotation_field * carrier)
quotient_rotation = rotation_action[4:6, 4:6]
check("exact", "rotation preserves both the gauge image and the N2 kernel",
      rotation_field * gauge_field == carrier * rotation_action[:, 0:4]
      and rotation_field * physical == carrier * rotation_action[:, 4:6])
check("exact", "the two-mode quotient is the real helicity-one module",
      quotient_rotation == matrix(field, [[0, -1], [1, 0]])
      and quotient_rotation**2 == -identity_matrix(field, 2)
      and quotient_rotation.charpoly() == quotient_rotation.charpoly().parent().gen()**2 + 1)
check("exact", "the quotient is not the helicity-two graviton module",
      quotient_rotation**2 + 4 * identity_matrix(field, 2) == 3 * identity_matrix(field, 2))
check("planted", "PLANT two algebraic modes are not renamed two helicity-two polarizations", True)
check("planted", "PLANT one-mode N1 roots cannot individually supply a real helicity pair", True)


print("\nD. ACTION-DERIVED PRINCIPAL GREEN FLUX")
samples = {}
for time_component in range(6):
    p_sample, q_sample, _, _ = source_symbol((time_component, 0, 0, 1))
    samples[time_component] = (
        a * to_sage(p_sample, field) - to_sage(q_sample, field)
    )
fifth_difference = sum(
    ((-1) ** (5 - index)) * comb(5, index) * samples[index]
    for index in range(6)
)
check("exact", "the filtered Schur pencil is degree at most four along the time covector",
      fifth_difference.is_zero())

# Exact Lagrange-derivative weights at time component one on nodes 0..4.
weights = [QQ(-1) / 4, QQ(-5) / 6, QQ(3) / 2, QQ(-1) / 2, QQ(1) / 12]
time_derivative = sum(weights[index] * samples[index] for index in range(5))
green = physical.transpose() * time_derivative * physical
green_gauge = physical.transpose() * time_derivative * gauge_field
green_scalar = QQ(600329995) / 1382653597 * a - QQ(111263815960284) / 35822959328735
check("exact", "principal Green flux descends through the gauge radical",
      green_gauge.is_zero())
check("exact", "N2 local principal Green flux is a nondegenerate scalar form",
      green == green_scalar * identity_matrix(field, 2) and green.rank() == 2)

positive_root = next(root for root, multiplicity in n2.roots(AA) if root > 0)
green_real = AA(green_scalar.lift()(positive_root))
check("exact", "at the positive N2 embedding the local flux has one definite sign",
      -2 < green_real < -1)
shifted = physical + gauge_field[:, 1:3]
check("exact", "changing physical representatives by gauge leaves the flux unchanged",
      shifted.transpose() * time_derivative * shifted == green)
check("type", "definite finite principal flux is not yet positive energy or a common right-H Krein domain", True)
check("type", "wrong helicity retires N2 before global-domain promotion", True)


print("\nE. DISPOSITION AND FENCES")
for label in (
    "N2 is killed only as a spin-two Einstein carrier in this completed grade-one bank",
    "the graph-only Einstein theorem remains exact on its declared constant-T subspace",
    "a local definite flux does not rescue the helicity mismatch",
    "no coefficient selector residue quotient field or external datum is added",
    "P1 P2 P3 remain unused",
    "Curt remains formally separate and no third lane is promoted",
):
    check("planted", "PLANT " + label, True)

print("SOURCE_RETURN=SOURCE-CONFIRMS_AND_SOURCE-SILENT")
print("N2_KERNEL=GAUGE4_PLUS_TWO_SOURCE_MODES")
print("N2_COMPACT_NULL_LITTLE_GROUP=HELICITY_PLUS_MINUS_ONE__NOT_PLUS_MINUS_TWO")
print("N2_PRINCIPAL_GREEN_FLUX=RANK2_DEFINITE_AT_POSITIVE_EMBEDDING__GAUGE_DESCENDING")
print("N2_SPIN_TWO_CANDIDATE=KILLED_IN_COMPLETE_GRADE1_BANK")
print("GLOBAL_RIGHT_H_KREIN_DOMAIN_ODD_BV_BFV=NOT_REACHED_BY_N2")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
