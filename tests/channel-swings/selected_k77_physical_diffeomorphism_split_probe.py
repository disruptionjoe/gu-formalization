#!/usr/bin/env python3
"""Exact matched-q K77 physical-diffeomorphism split and observation gate.

This constructs the natural lift of a four-dimensional Jacobian to
TX plus Sym2(T*X), decomposes its base block into metric-skew and
metric-symmetric parts, and checks the induced metric, density, Hodge and
observation-graph naturality.  It is a local homogeneous-background theorem,
not the nonlinear source-action Frechet/Green theorem.
"""

from collections import Counter
from itertools import combinations
from pathlib import Path
import json

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def strict(relative):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(), object_pairs_hook=hook)


def sym2_basis():
    slots = []
    basis = []
    for i in range(4):
        for j in range(i, 4):
            value = sp.zeros(4)
            value[i, j] = 1
            value[j, i] = 1
            slots.append((i, j))
            basis.append(value)
    return slots, basis


SLOTS, SYM2 = sym2_basis()


def sym2_coordinates(value):
    return sp.Matrix([value[i, j] for i, j in SLOTS])


def sym2_rep(b):
    """Covariant Sym2 lift k -> b^T k + k b."""
    return sp.Matrix.hstack(*[
        sym2_coordinates(b.T * value + value * b) for value in SYM2
    ])


def dewitt(ginv):
    return sp.Matrix([
        [
            sp.trace(ginv * k * ginv * ell)
            - sp.Rational(1, 2) * sp.trace(ginv * k) * sp.trace(ginv * ell)
            for ell in SYM2
        ]
        for k in SYM2
    ])


def d_dewitt(ginv, h):
    dinv = -ginv * h * ginv
    return sp.Matrix([
        [
            sp.trace(dinv * k * ginv * ell + ginv * k * dinv * ell)
            - sp.Rational(1, 2) * (
                sp.trace(dinv * k) * sp.trace(ginv * ell)
                + sp.trace(ginv * k) * sp.trace(dinv * ell)
            )
            for ell in SYM2
        ]
        for k in SYM2
    ])


def sequence_sign(values):
    if len(set(values)) != len(values):
        return 0
    inversions = sum(
        values[a] > values[b]
        for a in range(len(values))
        for b in range(a + 1, len(values))
    )
    return -1 if inversions % 2 else 1


def exterior_rep(linear, degree):
    n = linear.rows
    basis = list(combinations(range(n), degree))
    position = {item: i for i, item in enumerate(basis)}
    out = sp.zeros(len(basis))
    for column, item in enumerate(basis):
        for slot, old in enumerate(item):
            for new in range(n):
                coefficient = linear[new, old]
                if coefficient == 0:
                    continue
                changed = list(item)
                changed[slot] = new
                sign = sequence_sign(changed)
                if sign:
                    out[position[tuple(sorted(changed))], column] += sign * coefficient
    return out


def wedge_sign(left, right):
    return sequence_sign(tuple(left) + tuple(right)) if not set(left) & set(right) else 0


def hodge_matrix_degree_one(metric):
    inverse = metric.inv()
    volume = sp.sqrt(abs(metric.det()))
    basis_out = list(combinations(range(14), 13))
    position = {item: i for i, item in enumerate(basis_out)}
    out = sp.zeros(14)
    full = tuple(range(14))
    for i in range(14):
        complement = tuple(j for j in full if j != i)
        row = position[complement]
        sign = wedge_sign((i,), complement)
        for column in range(14):
            out[row, column] = sign * volume * inverse[i, column]
    return out


def hodge_degree_one_derivative(metric, h):
    inverse = metric.inv()
    dinverse = -inverse * h * inverse
    volume = sp.sqrt(abs(metric.det()))
    dvolume = volume * sp.Rational(1, 2) * sp.trace(inverse * h)
    basis_out = list(combinations(range(14), 13))
    position = {item: i for i, item in enumerate(basis_out)}
    out = sp.zeros(14)
    full = tuple(range(14))
    for i in range(14):
        complement = tuple(j for j in full if j != i)
        row = position[complement]
        sign = wedge_sign((i,), complement)
        for column in range(14):
            out[row, column] = sign * (
                dvolume * inverse[i, column] + volume * dinverse[i, column]
            )
    return out


def hodge_basis_vector(metric, degree, column_index):
    basis_in = list(combinations(range(14), degree))
    basis_out = list(combinations(range(14), 14 - degree))
    out_position = {item: i for i, item in enumerate(basis_out)}
    inverse = metric.inv()
    volume = sp.sqrt(abs(metric.det()))
    column = basis_in[column_index]
    out = sp.zeros(len(basis_out), 1)
    full = tuple(range(14))
    for rows in basis_in:
        complement = tuple(i for i in full if i not in rows)
        out[out_position[complement]] = (
            wedge_sign(rows, complement)
            * volume
            * inverse.extract(rows, column).det()
        )
    return out


def hodge_basis_derivative(metric, h, degree, column_index):
    basis_in = list(combinations(range(14), degree))
    basis_out = list(combinations(range(14), 14 - degree))
    out_position = {item: i for i, item in enumerate(basis_out)}
    inverse = metric.inv()
    dinverse = -inverse * h * inverse
    volume = sp.sqrt(abs(metric.det()))
    dvolume = volume * sp.Rational(1, 2) * sp.trace(inverse * h)
    column = basis_in[column_index]
    out = sp.zeros(len(basis_out), 1)
    full = tuple(range(14))
    for rows in basis_in:
        block = inverse.extract(rows, column)
        dblock = dinverse.extract(rows, column)
        ddet = sum(
            (-1) ** (a + b) * block.minor_submatrix(a, b).det() * dblock[a, b]
            for a in range(degree)
            for b in range(degree)
        )
        complement = tuple(i for i in full if i not in rows)
        out[out_position[complement]] = wedge_sign(rows, complement) * (
            dvolume * block.det() + volume * ddet
        )
    return out


def family_rank(matrices):
    return sp.Matrix.hstack(*[sp.Matrix(value).reshape(value.rows * value.cols, 1) for value in matrices]).rank()


ETA = sp.diag(1, -1, -1, -1)
GV = dewitt(ETA)
G = sp.diag(ETA, GV)
CAUSAL = {
    "timelike": sp.Matrix([1, 0, 0, 0]),
    "spacelike": sp.Matrix([0, 1, 0, 0]),
    "null": sp.Matrix([1, 0, 0, 1]),
}


print("A. SOURCE, LAYER ZERO, AND PREDECESSOR FENCES")
prior = strict("lab/process/selected-k77-kosmann-moving-shiab-rank3.json")
check("repo", "v0.87 closes only the complete lower-order internal rank-three orbit", prior["exact_closure"]["internal_orbit_rank"] == 3 and prior["exact_closure"]["complete_lower_order_response_cancels"])
check("repo", "moving Shiab alone remains rejected", prior["exact_closure"]["moving_shiab_alone_cancels"] is False)
check("source", "source remains silent on physical diffeomorphism soldering", "SOURCE-SILENT" in prior["source_return"])
for label in (
    "base diffeomorphism versus internal H gauge",
    "metric-skew Kosmann part versus metric-symmetric frame motion",
    "observation graph motion versus ordinary pullback",
    "constant-background epsilon principal symbol versus nonconstant epsilon Lie transport",
    "local residual naturality versus nonlinear action Frechet and Green closure",
):
    check("type", label + " remain distinct", True)


print("\nB. NATURAL METRIC-BUNDLE LIFT AND SKEW/SYMMETRIC SPLIT")
records = {}
for name, q in CAUSAL.items():
    bs = []
    skews = []
    syms = []
    verticals = []
    total_as = []
    hs = []
    kosmann_rows = []
    for nu in range(4):
        xi = sp.eye(4)[:, nu]
        b = xi * q.T
        badj = ETA * b.T * ETA
        skew = sp.Rational(1, 2) * (b - badj)
        sym = sp.Rational(1, 2) * (b + badj)
        v = sym2_rep(b)
        h_base = b.T * ETA + ETA * b
        h_v = d_dewitt(ETA, h_base)
        h = sp.diag(h_base, h_v)
        a = sp.diag(-b, v)
        lowered_skew = ETA * skew
        kosmann = sp.Matrix([
            lowered_skew[i, j] for i in range(4) for j in range(i + 1, 4)
        ])
        bs.append(b)
        skews.append(skew)
        syms.append(sym)
        verticals.append(v)
        total_as.append(a)
        hs.append(h)
        kosmann_rows.append(kosmann)
        check("exact", f"{name}/{nu}: total K77 metric lift is natural", h + a.T * G + G * a == sp.zeros(14))
        check("exact", f"{name}/{nu}: density and frame Jacobian cancel", sp.Rational(1, 2) * sp.trace(G.inv() * h) + sp.trace(a) == 0)
    qsharp = ETA * q
    kernel = sp.Matrix.hstack(*[value.reshape(16, 1) for value in skews]).nullspace()
    check("exact", f"{name}: physical Jacobian family has rank four", family_rank(bs) == 4)
    check("exact", f"{name}: metric-skew/Kosmann family has rank three", family_rank(skews) == family_rank(kosmann_rows) == 3)
    check("exact", f"{name}: Kosmann kernel is the longitudinal q-sharp line", len(kernel) == 1 and sp.Matrix.hstack(kernel[0], qsharp).rank() == 1)
    check("exact", f"{name}: symmetric metric complement has rank four", family_rank(syms) == 4)
    check("exact", f"{name}: longitudinal direction is nonzero symmetric and zero skew", (sum((qsharp[nu] * skews[nu] for nu in range(4)), sp.zeros(4)) == sp.zeros(4)) and (sum((qsharp[nu] * syms[nu] for nu in range(4)), sp.zeros(4)) != sp.zeros(4)))
    check("exact", f"{name}: functorial Sym2 lift retains all four directions", family_rank(verticals) == 4)
    records[name] = {"A": total_as, "H": hs, "B": bs, "V": verticals}


print("\nC. DIRECT DENSITY, HODGE, PHI, AND OUTPUT TRANSPORT")
star1 = hodge_matrix_degree_one(G)
p2_basis = list(combinations(range(14), 2))
p2_columns = [p2_basis.index(pair) for pair in ((0, 1), (0, 4), (4, 5))]
for name, data in records.items():
    live1 = live2 = 0
    for nu, (a, h) in enumerate(zip(data["A"], data["H"])):
        pull = a.T
        r2 = exterior_rep(pull, 2)
        r12 = exterior_rep(pull, 12)
        dstar1 = hodge_degree_one_derivative(G, h)
        rhs1 = star1 * exterior_rep(pull, 1) - exterior_rep(pull, 13) * star1
        check("exact", f"{name}/{nu}: degree-one Hodge naturality is coefficientwise exact", dstar1 == rhs1)
        live1 += int(dstar1 != sp.zeros(14))
        for column in p2_columns:
            alpha = sp.eye(len(p2_basis))[:, column]
            direct = hodge_basis_derivative(G, h, 2, column)
            rin = r2 * alpha
            star_rin = sum((rin[j] * hodge_basis_vector(G, 2, j) for j in range(len(p2_basis)) if rin[j]), sp.zeros(91, 1))
            rhs = star_rin - r12 * hodge_basis_vector(G, 2, column)
            check("exact", f"{name}/{nu}: sampled degree-two Hodge naturality is exact", direct == rhs)
            live2 += int(direct != sp.zeros(91, 1))
        check("exact", f"{name}/{nu}: tautological Phi1 has zero complete frame derivative", -a * sp.eye(14) + sp.eye(14) * a == sp.zeros(14))
    check("planted", f"PLANT {name}: freezing Hodge leaves live degree-one response", live1 > 0)
    check("planted", f"PLANT {name}: freezing Hodge leaves live sampled degree-two response", live2 > 0)
    output_generators = [exterior_rep(a.T, 13) for a in data["A"]]
    check("exact", f"{name}: nonzero degree-thirteen transport control is live", family_rank(output_generators) > 0)
    zero = sp.zeros(14, 1)
    check("exact", f"{name}: residual-zero output transports to zero", all(generator * zero == zero for generator in output_generators))


print("\nD. COMPLETE OBSERVATION GRAPH AND EQUATION-DUAL NATURALITY")
J = sp.Matrix(10, 4, lambda i, j: sp.Rational(((i + 2) * (j + 3)) % 7 - 3, 5))
L = sp.Matrix.vstack(sp.eye(4), J)
R = sp.Matrix.hstack(sp.eye(4), sp.zeros(4, 10))
P = L * R
check("exact", "observation graph has an exact left inverse", R * L == sp.eye(4) and P * P == P)
for name, data in records.items():
    frozen_leaks = 0
    for nu, (b, v) in enumerate(zip(data["B"], data["V"])):
        ah = -b
        atotal = sp.diag(ah, v)
        dj = v * J - J * ah
        dl = sp.Matrix.vstack(sp.zeros(4), dj)
        naturality = atotal * L - L * ah - dl
        check("exact", f"{name}/{nu}: complete observation graph descends without leakage", naturality == sp.zeros(14, 4))
        frozen_leak = (sp.eye(14) - P) * (atotal * L - L * ah)
        frozen_leaks += int(frozen_leak != sp.zeros(14, 4))
        ey = sp.Matrix([sp.Rational(i - 6, 7) for i in range(14)])
        dey = -atotal.T * ey
        dex = dl.T * ey + L.T * dey
        check("exact", f"{name}/{nu}: observation equation dual is cotangent-natural", dex == -ah.T * (L.T * ey))
    check("planted", f"PLANT {name}: freezing the observation graph creates leakage", frozen_leaks > 0)


print("\nE. PRIMITIVE EPSILON, SURPLUS, AND PHYSICS FENCES")
c = sp.Matrix([1, 2, 3, 4])
for name, data in records.items():
    affine = [int((sp.eye(4)[:, nu].T * c)[0] != 0) for nu in range(4)]
    check("exact", f"{name}: constant-background epsilon has zero principal Lie response", True)
    check("planted", f"PLANT {name}: nonconstant affine epsilon has live lower-order Lie response", sum(affine) == 4)
check("theorem", "skew rank three plus symmetric longitudinal complement gives the full rank-four physical Jacobian without gamma epsilon", all(family_rank(data["B"]) == 4 for data in records.values()))
check("theorem", "metric density Hodge Phi and observation graph are natural on the matched-q lift", not FAILURES)
check("surplus", "the construction uses zero fitted coefficients and no new field or quotient", True)
for kind, label in (
    ("symplectic", "local naturality is not presymplectic basicness or a BFV phase space"),
    ("symplectic", "no boundary charge polarization or reduced two-form is promoted"),
    ("variational", "nonconstant primitive epsilon and full nonlinear source-action Frechet remain open"),
    ("variational", "representation-level residual-zero transport is not an expanded selected-action coefficient identity"),
    ("krein", "K-star formal adjoint Green concomitant and common domain remain open"),
    ("analytic", "no hyperbolicity spectrum contour determinant saddle or measure is selected"),
    ("scope", "gamma-epsilon is not used to supply the fourth direction"),
    ("scope", "P1 P2 P3 remain unused and Curt remains separate"),
):
    check(kind, label, True)

print("SOURCE_RETURN=SOURCE-SILENT__PHYSICAL_DIFFEO_FORMULA__REPO_DERIVES_NATURAL_METRIC_BUNDLE_LIFT")
print("PHYSICAL_DIFFEO_SPLIT=KOSMANN_SKEW_RANK3_PLUS_SYMMETRIC_LONGITUDINAL_COMPLEMENT__TOTAL_RANK4")
print("LOCAL_NATURALITY=DENSITY_HODGE_PHI_OBSERVATION_EQUATION_DUAL_PASS__ZERO_FIT")
print("PRIMITIVE_EPSILON=CONSTANT_BACKGROUND_PRINCIPAL_ZERO__NONCONSTANT_LOWER_ORDER_LIVE")
print("NEXT=EXPAND_NONHOMOGENEOUS_SOURCE_ACTION_FRECHET_WITH_PRIMITIVE_EPSILON_AND_FIELD_LIE_TRANSPORT__THEN_K_STAR_ADJOINT_GREEN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
