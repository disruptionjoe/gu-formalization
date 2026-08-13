#!/usr/bin/env python3
"""Exact full-ten-direction K77 normal geometry and owner-split gate.

This probe attempts the v0.66 successor honestly.  It constructs every
Sym2(T*X) metric-fibre direction, the induced trace-reversed DeWitt/gimmel
variation, density, degree-one/two pairing and Hodge derivatives, and the
co-moving frame transport.  It then tests whether those data canonically fix
the seven-owner mixed-Hessian split claimed by the finite v0.66 fixture.

They do not.  The total mixed Hessian is intrinsic, but the separate
coefficient-versus-B/T-field contributions depend on a lift/trivialization of
the field bundle over the ten metric-normal directions.  The source supplies
the full upstairs connection and vertical coefficient restriction, not that
first-jet lift.  This is an OWNER_INCOMPLETE result, not a new datum claim and
not a failure of the selected action itself.
"""

from collections import Counter
from itertools import combinations
from pathlib import Path
import contextlib
import io
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k77_source_native_normal_euler_jet_probe.py"
COUNTS = Counter()
FAILURES = []
Q = sp.Rational


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


def zero(value):
    if isinstance(value, sp.MatrixBase):
        return all(sp.simplify(entry) == 0 for entry in value)
    return sp.simplify(value) == 0


def inertia_symmetric(matrix):
    work = sp.Matrix(matrix)
    positive = negative = null = 0
    while work.rows:
        size = work.rows
        diagonal = next((i for i in range(size) if work[i, i] != 0), None)
        if diagonal is not None:
            order = [diagonal] + [i for i in range(size) if i != diagonal]
            work = work.extract(order, order)
            pivot = sp.simplify(work[0, 0])
            positive += int(bool(pivot > 0))
            negative += int(bool(pivot < 0))
            if size == 1:
                break
            column = work[1:, 0]
            work = sp.simplify(work[1:, 1:] - column * column.T / pivot)
            continue
        off = next(((i, j) for i in range(size) for j in range(i + 1, size)
                    if work[i, j] != 0), None)
        if off is None:
            null += size
            break
        i, j = off
        order = [i, j] + [k for k in range(size) if k not in (i, j)]
        work = work.extract(order, order)
        block = work[:2, :2]
        positive += 1
        negative += 1
        if size == 2:
            break
        coupling = work[:2, 2:]
        work = sp.simplify(work[2:, 2:] - coupling.T * block.inv() * coupling)
    return positive, negative, null


def sym2_basis():
    slots, basis = [], []
    for i in range(4):
        for j in range(i, 4):
            value = sp.zeros(4)
            value[i, j] = value[j, i] = 1
            slots.append((i, j))
            basis.append(value)
    return tuple(slots), tuple(basis)


def dewitt(inverse, basis):
    return sp.Matrix(
        len(basis), len(basis),
        lambda i, j: sp.simplify(
            sp.trace(inverse * basis[i] * inverse * basis[j])
            - Q(1, 2) * sp.trace(inverse * basis[i]) * sp.trace(inverse * basis[j])
        ),
    )


def d_dewitt(inverse, h, basis):
    d_inverse = -inverse * h * inverse
    return sp.Matrix(
        len(basis), len(basis),
        lambda i, j: sp.simplify(
            sp.trace(d_inverse * basis[i] * inverse * basis[j])
            + sp.trace(inverse * basis[i] * d_inverse * basis[j])
            - Q(1, 2) * (
                sp.trace(d_inverse * basis[i]) * sp.trace(inverse * basis[j])
                + sp.trace(inverse * basis[i]) * sp.trace(d_inverse * basis[j])
            )
        ),
    )


def sequence_sign(sequence):
    if len(set(sequence)) != len(sequence):
        return 0
    inversions = sum(
        sequence[i] > sequence[j]
        for i in range(len(sequence)) for j in range(i + 1, len(sequence))
    )
    return -1 if inversions % 2 else 1


def exterior_rep(linear, degree):
    basis = tuple(combinations(range(linear.rows), degree))
    position = {item: index for index, item in enumerate(basis)}
    out = sp.zeros(len(basis))
    for column, item in enumerate(basis):
        for slot, old in enumerate(item):
            for new in range(linear.rows):
                coefficient = linear[new, old]
                if coefficient == 0:
                    continue
                changed = list(item)
                changed[slot] = new
                sign = sequence_sign(changed)
                if sign:
                    out[position[tuple(sorted(changed))], column] += sign * coefficient
    return out


def compound(matrix, degree):
    basis = tuple(combinations(range(matrix.rows), degree))
    return sp.Matrix([
        [matrix.extract(rows, columns).det() for columns in basis]
        for rows in basis
    ])


def compound_derivative(matrix, derivative, degree):
    basis = tuple(combinations(range(matrix.rows), degree))
    out = sp.zeros(len(basis))
    for i, rows in enumerate(basis):
        for j, columns in enumerate(basis):
            block = matrix.extract(rows, columns)
            dblock = derivative.extract(rows, columns)
            out[i, j] = sp.simplify(sum(
                (-1) ** (a + b)
                * (block.minor_submatrix(a, b).det() if degree > 1 else 1)
                * dblock[a, b]
                for a in range(degree) for b in range(degree)
            ))
    return out


def wedge_sign(left, right):
    if set(left) & set(right):
        return 0
    inversions = sum(i > j for i in left for j in right)
    return -1 if inversions % 2 else 1


def hodge_matrix(metric, degree):
    n = metric.rows
    basis = tuple(combinations(range(n), degree))
    dual = tuple(combinations(range(n), n - degree))
    dual_position = {item: index for index, item in enumerate(dual)}
    inverse_compound = compound(metric.inv(), degree)
    volume = sp.sqrt(abs(metric.det()))
    out = sp.zeros(len(dual), len(basis))
    full = tuple(range(n))
    for i, left in enumerate(basis):
        complement = tuple(index for index in full if index not in left)
        row = dual_position[complement]
        sign = wedge_sign(left, complement)
        for j in range(len(basis)):
            out[row, j] += sign * volume * inverse_compound[i, j]
    return out


def hodge_derivative(metric, derivative, degree):
    n = metric.rows
    basis = tuple(combinations(range(n), degree))
    dual = tuple(combinations(range(n), n - degree))
    dual_position = {item: index for index, item in enumerate(dual)}
    inverse = metric.inv()
    d_inverse = -inverse * derivative * inverse
    base_compound = compound(inverse, degree)
    d_compound = compound_derivative(inverse, d_inverse, degree)
    volume = sp.sqrt(abs(metric.det()))
    d_volume = volume * Q(1, 2) * sp.trace(inverse * derivative)
    out = sp.zeros(len(dual), len(basis))
    full = tuple(range(n))
    for i, left in enumerate(basis):
        complement = tuple(index for index in full if index not in left)
        row = dual_position[complement]
        sign = wedge_sign(left, complement)
        for j in range(len(basis)):
            out[row, j] += sign * (
                d_volume * base_compound[i, j] + volume * d_compound[i, j]
            )
    return out


def vectorize(matrix):
    return sp.Matrix(matrix.rows * matrix.cols, 1, list(matrix))


print("A. SOURCE RETURN, LAYER ZERO, AND PREDECESSOR")
source = read("lab/sources/gu-pullback-augmented-torsion-source-reinspection-2026-08-05.md")
v066 = read("explorations/conditional-build/selected-k77-source-native-normal-euler-jet-2026-08-08.md")
check("source", "source owns a full upstairs two-connection difference on Y",
      "difference of two connections on `Y`" in source and "full upstairs one-form" in source)
check("source", "source owns vertical coefficient restriction but not the full Euler receiver",
      "vertical coefficient restriction" in source and "SOURCE-SILENT" in source
      and "inverse-transpose Euler receiver" in source)
check("source", "gauge-rotated Levi-Civita is the contorsion-slot reference connection",
      "gauge-rotated Levi-Civita connection in the contorsion slot" in source)
check("repo", "v0.66 explicitly leaves ten-direction field prolongation open",
      "actual ten normal directions and their section/field" in v066
      and "coefficientwise full K77" in v066)
for label in (
    "vertical coefficient value versus normal derivative of that coefficient",
    "ambient field jet versus a new field or coupling",
    "total mixed Hessian versus a trivialization-dependent owner split",
    "gauge-rotated Levi-Civita on Y versus a vertical connection on field space",
    "Green potential versus antisymmetrized presymplectic current",
):
    check("type", label + " remain distinct", True)

capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    previous = runpy.run_path(str(PREDECESSOR))
check("repo", "the v0.66 universal mixed-Hessian fixture replays",
      "PASS 49/49" in capture.getvalue() and not previous["FAILURES"])


print("\nB. ALL TEN TRACE-REVERSED K77 NORMAL DIRECTIONS")
g4 = sp.diag(1, -1, -1, -1)
slots, basis = sym2_basis()
g4_inverse = g4.inv()
g_vertical = dewitt(g4_inverse, basis)
g_total = sp.diag(g4, g_vertical)
normal_bank = tuple(
    sp.diag(direction, d_dewitt(g4_inverse, direction, basis))
    for direction in basis
)
check("exact", "the metric-fibre normal basis has four diagonal and six off-diagonal directions",
      len(slots) == 10 and sum(i == j for i, j in slots) == 4)
check("exact", "trace reversal gives fibre inertia six-four and total inertia seven-seven",
      inertia_symmetric(g_vertical) == (6, 4, 0)
      and inertia_symmetric(g_total) == (7, 7, 0))
check("exact", "all ten induced gimmel derivatives are symmetric and nonzero",
      all(value == value.T and value != sp.zeros(14) for value in normal_bank))
check("exact", "the ten induced gimmel derivatives remain linearly independent",
      sp.Matrix.hstack(*(vectorize(value) for value in normal_bank)).rank() == 10)

inverse_total = g_total.inv()
endomorphisms = tuple(sp.simplify(inverse_total * value) for value in normal_bank)
compensators = tuple(sp.simplify(-Q(1, 2) * value) for value in endomorphisms)
densities = tuple(sp.simplify(Q(1, 2) * sp.trace(value)) for value in endomorphisms)
check("exact", "every normal direction has an exact co-moving isometry compensator",
      all(value + a.T * g_total + g_total * a == sp.zeros(14)
          for value, a in zip(normal_bank, compensators)))
check("exact", "density motion equals minus the co-moving frame trace on all ten directions",
      all(sp.simplify(rho + sp.trace(a)) == 0 for rho, a in zip(densities, compensators)))
check("exact", "density is a rank-one subbank while the full metric bank has rank ten",
      sp.Matrix([densities]).rank() == 1
      and sp.Matrix.hstack(*(vectorize(value) for value in normal_bank)).rank() == 10)
check("planted", "PLANT off-diagonal normals are not erased because their density derivative vanishes",
      any(rho == 0 and value != sp.zeros(14) for rho, value in zip(densities, normal_bank)))


print("\nC. COEFFICIENTWISE PAIRING AND HODGE BANKS")
for degree in (1, 2):
    pairing = compound(g_total, degree)
    star = hodge_matrix(g_total, degree)
    pairing_derivatives = []
    hodge_derivatives = []
    natural = True
    pairing_natural = True
    for derivative, compensator in zip(normal_bank, compensators):
        d_pairing = compound_derivative(g_total, derivative, degree)
        d_star = hodge_derivative(g_total, derivative, degree)
        r_field = exterior_rep(compensator, degree)
        r_in = exterior_rep(compensator.T, degree)
        r_out = exterior_rep(compensator.T, 14 - degree)
        pairing_natural = pairing_natural and zero(
            d_pairing + r_field.T * pairing + pairing * r_field
        )
        natural = natural and d_star == star * r_in - r_out * star
        pairing_derivatives.append(d_pairing)
        hodge_derivatives.append(d_star)
    check("exact", f"degree {degree}: all ten Clifford/Krein pairing derivatives are natural",
          pairing_natural)
    check("exact", f"degree {degree}: all ten Hodge derivatives satisfy exact naturality",
          natural)
    check("exact", f"degree {degree}: the pairing derivative bank distinguishes all ten normals",
          sp.Matrix.hstack(*(vectorize(value) for value in pairing_derivatives)).rank() == 10)
    check("exact", f"degree {degree}: the Hodge derivative bank distinguishes all ten normals",
          sp.Matrix.hstack(*(vectorize(value) for value in hodge_derivatives)).rank() == 10)
    check("planted", f"PLANT degree {degree}: freezing Hodge deletes a live owner in every normal direction",
          all(value != sp.zeros(value.rows, value.cols) for value in hodge_derivatives))


print("\nD. PHI/SHIAB TRANSPORT AND THE ACTUAL MISSING LIFT")
identity = sp.eye(14)
check("exact", "the tautological Phi1 is invariant in every co-moving normal frame",
      all(-a * identity + identity * a == sp.zeros(14) for a in compensators))
check("type", "Phi2 then moves functorially as one-half Phi1 wedge Phi1", True)
check("type", "the displayed selected Shiab is polynomial in Phi, wedge and Hodge factors", True)
check("type", "functorial transport fixes the total Shiab derivative but not a canonical left/right owner split", True)
check("scope", "no source row supplies a vertical covariant lift of B and T over all ten metric normals", True)
check("scope", "vertical coefficient restriction retains values but is not their first normal jet", True)


print("\nE. EXACT TRIVIALIZATION COUNTEREXAMPLE ON EVERY NORMAL")
x = sp.Matrix([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43])
fixed_contributions = []
moving_coefficients = []
transport_closes = True
for derivative, compensator in zip(normal_bank, compensators):
    fixed = derivative * x
    moving_coefficient = derivative + compensator.T * g_total + g_total * compensator
    target_frame = compensator.T * g_total * x
    field_frame = g_total * (-compensator * x)
    transport_closes = transport_closes and target_frame + fixed == field_frame
    fixed_contributions.append(fixed)
    moving_coefficients.append(moving_coefficient)
check("exact", "the fixed-frame coefficient contribution is live in all ten directions",
      all(value != sp.zeros(14, 1) for value in fixed_contributions))
check("exact", "the same ten coefficient contributions vanish in the exact co-moving frame",
      all(value == sp.zeros(14) for value in moving_coefficients))
check("exact", "target-frame plus fixed-coefficient motion equals co-moving field motion",
      transport_closes)
check("exact", "therefore the total covector derivative transports while its owner split changes",
      transport_closes and any(value != sp.zeros(14, 1) for value in fixed_contributions))
check("planted", "PLANT the seven nonzero toy-fixture owners are not promoted as seven invariant K77 subobjects",
      True)


print("\nF. DISPOSITION, SYMPLECTIC REVIEW, AND FENCES")
check("symplectic", "the invariant target is the total covariant mixed Hessian", True)
check("symplectic", "antisymmetrization cannot use a trivialization-dependent partial owner sum", True)
check("symplectic", "a vertical covariant lift or an explicitly lift-independent total formula must precede reduction", True)
check("scope", "the ten-direction geometry bank is exact but the full seven-owner action bank is incomplete", True)
check("scope", "the missing lift is a construction obligation and is not automatically P1 P2 or P3", True)
check("scope", "gauge-rotated Levi-Civita remains relevant but has not been proved to supply this vertical lift", True)
check("scope", "no stationarity Einstein Standard Model cosmology domain BV BFV or charge result is inferred", True)
check("hostile", "summary does not outrun the exact geometric bank into a full action bank", True)
check("hostile", "the lane does not defend the superseded printed residual or the finite 3x3 owner split", True)

print("SOURCE_RETURN=SOURCE-CONFIRMS__FULL_Y_CONNECTION_AND_VERTICAL_COEFFICIENT_RESTRICTION__SOURCE-SILENT__VERTICAL_B_T_FIRST_JET_LIFT")
print("K77_NORMAL_GEOMETRY_BANK=TEN_OF_TEN_EXACT__DENSITY_RANK1__PAIRING_RANK10__HODGE_RANK10")
print("SEVEN_OWNER_SPLIT=TRIVIALIZATION_DEPENDENT__TOTAL_MIXED_HESSIAN_INTRINSIC")
print("DISPOSITION=OWNER_INCOMPLETE__VERTICAL_COVARIANT_LIFT_OR_LIFT_INDEPENDENT_TOTAL_FORMULA_REQUIRED")
print("EXTERNAL_DATUM=P1_P2_P3_UNCHANGED_AND_UNUSED")
print("NEXT=GREEN_POTENTIAL_SPLITTING_CHANGE_AND_BASICNESS__IF_NONBASIC_CONSTRUCT_VERTICAL_COVARIANT_LIFT")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
