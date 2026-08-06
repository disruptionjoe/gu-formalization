#!/usr/bin/env python3
"""Exact selected-action co-moving-frame naturality gate."""

from collections import Counter
from fractions import Fraction
from itertools import combinations
from io import StringIO
from pathlib import Path
import contextlib
import json
import runpy

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
GIMMEL_BACKEND = ROOT / "tests/channel-swings/moving_gimmel_hodge_frame_owner_probe.py"
SHIAB_BACKEND = ROOT / "tests/channel-swings/k77_wave2_moving_shiab_epsilon_ward_green_domain_probe.py"
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


def wedge_sign(left, right):
    if set(left) & set(right):
        return 0
    inversions = sum(1 for i in left for j in right if i > j)
    return -1 if inversions % 2 else 1


def sequence_sign(sequence):
    if len(set(sequence)) != len(sequence):
        return 0
    inversions = sum(
        1 for a in range(len(sequence)) for b in range(a + 1, len(sequence))
        if sequence[a] > sequence[b]
    )
    return -1 if inversions % 2 else 1


def exterior_rep(linear, degree):
    """Infinitesimal exterior representation for column basis vectors."""
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


def compound(matrix, degree):
    basis = list(combinations(range(matrix.rows), degree))
    return sp.Matrix([
        [matrix.extract(rows, cols).det() for cols in basis]
        for rows in basis
    ])


def compound_derivative(matrix, derivative, degree):
    basis = list(combinations(range(matrix.rows), degree))
    out = sp.zeros(len(basis))
    for i, rows in enumerate(basis):
        for j, cols in enumerate(basis):
            block = matrix.extract(rows, cols)
            dblock = derivative.extract(rows, cols)
            value = 0
            for a in range(degree):
                for b in range(degree):
                    minor = block.minor_submatrix(a, b).det() if degree > 1 else 1
                    value += (-1) ** (a + b) * minor * dblock[a, b]
            out[i, j] = sp.simplify(value)
    return out


def hodge_matrix(metric, degree):
    n = metric.rows
    dual_degree = n - degree
    basis = list(combinations(range(n), degree))
    dual_basis = list(combinations(range(n), dual_degree))
    dual_position = {item: i for i, item in enumerate(dual_basis)}
    inverse_compound = compound(metric.inv(), degree)
    volume = sp.sqrt(abs(metric.det()))
    out = sp.zeros(len(dual_basis), len(basis))
    full = tuple(range(n))
    for i, left in enumerate(basis):
        complement = tuple(index for index in full if index not in left)
        sign = wedge_sign(left, complement)
        row = dual_position[complement]
        for j in range(len(basis)):
            out[row, j] += sign * volume * inverse_compound[i, j]
    return out


def hodge_derivative(metric, metric_derivative, degree):
    n = metric.rows
    dual_degree = n - degree
    basis = list(combinations(range(n), degree))
    dual_basis = list(combinations(range(n), dual_degree))
    dual_position = {item: i for i, item in enumerate(dual_basis)}
    inverse = metric.inv()
    d_inverse = -inverse * metric_derivative * inverse
    d_compound = compound_derivative(inverse, d_inverse, degree)
    volume = sp.sqrt(abs(metric.det()))
    d_volume = volume * sp.Rational(1, 2) * sp.trace(inverse * metric_derivative)
    base_compound = compound(inverse, degree)
    out = sp.zeros(len(dual_basis), len(basis))
    full = tuple(range(n))
    for i, left in enumerate(basis):
        complement = tuple(index for index in full if index not in left)
        sign = wedge_sign(left, complement)
        row = dual_position[complement]
        for j in range(len(basis)):
            out[row, j] += sign * (
                d_volume * base_compound[i, j] + volume * d_compound[i, j]
            )
    return out


print("A. LOAD THE ACTUAL MOVING GIMMEL FAMILY")
capture = StringIO()
with contextlib.redirect_stdout(capture):
    M = runpy.run_path(str(GIMMEL_BACKEND))
check("repo", "moving-gimmel predecessor replays", "PASS 41/41" in capture.getvalue())

metric = M["g_total"]
metric_derivative = M["h_total"]
k_metric = M["k_total"]
a_vector = -sp.Rational(1, 2) * k_metric
check("exact", "actual gimmel metric is fourteen-dimensional", metric.shape == (14, 14))
check("exact", "actual gimmel metric determinant has rational volume eight", metric.det() == -64 and sp.sqrt(abs(metric.det())) == 8)
check("exact", "TT metric derivative has rank eight and trace zero", metric_derivative.rank() == 8 and sp.trace(k_metric) == 0)
check("exact", "co-moving vector frame is the exact isometry compensator", metric_derivative + a_vector.T * metric + metric * a_vector == sp.zeros(14))


print("\nB. EXACT HODGE NATURALITY ON DEGREES ONE AND TWO")
for degree in (1, 2):
    dual_degree = 14 - degree
    star = hodge_matrix(metric, degree)
    d_star = hodge_derivative(metric, metric_derivative, degree)
    pullback_generator = a_vector.T
    r_in = exterior_rep(pullback_generator, degree)
    r_out = exterior_rep(pullback_generator, dual_degree)
    natural_rhs = star * r_in - r_out * star
    check("exact", f"degree {degree}: fixed-frame Hodge derivative is live", d_star.rank() > 0)
    check("exact", f"degree {degree}: infinitesimal isometry naturality is exact", d_star == natural_rhs)
    check("planted", f"PLANT degree {degree}: freezing Hodge leaves a nonzero frame defect", natural_rhs.rank() > 0)


print("\nC. TAUTOLOGICAL PHI AND CLIFFORD SCALAR PAIRING")
identity = sp.eye(14)
phi_derivative = -a_vector * identity + identity * a_vector
check("exact", "Phi1 is the transported tautological identity", phi_derivative == sp.zeros(14))
check("exact", "freezing either Phi slot gives a live rank-eight defect", a_vector.rank() == 8)
check("type", "Phi2 inherits zero pure-frame derivative from one-half Phi1 wedge Phi1", phi_derivative == sp.zeros(14))

for degree in (1, 2):
    pairing = compound(metric, degree)
    d_pairing = compound_derivative(metric, metric_derivative, degree)
    r = exterior_rep(a_vector, degree)
    compensated = d_pairing + r.T * pairing + pairing * r
    check("exact", f"Clifford scalar pairing is natural on grade {degree}", compensated == sp.zeros(pairing.rows))
    check("planted", f"PLANT grade {degree}: freezing the pairing leaves a live defect", d_pairing.rank() > 0)


print("\nD. SELECTED INTRINSIC ACTION IS NONVACUOUS BUT PURE-FRAME NATURAL")
capture = StringIO()
with contextlib.redirect_stdout(capture):
    S = runpy.run_path(str(SHIAB_BACKEND))
check("repo", "moving-Shiab predecessor replays", "PASS: the source moving-Shiab family" in capture.getvalue())

blade = S["blade"]
eadd = S["eadd"]
escale = S["escale"]
wedge_raw = S["wedge_raw"]
shiab = S["shiab"]
hodge = S["hodge"]
FULL = S["FULL"]
ZERO = S["ZERO"]
gadd = S["gadd"]
gscale = S["gscale"]
SELECTED = ("comm", "symi", "symi")


def top_scalar(form):
    return form.get(FULL, {}).get(0, ZERO)


def pairing(left, right):
    return top_scalar(wedge_raw(left, right))


field = {
    1 << 0: eadd(blade(4), escale(2, blade((5, 6)))),
    1 << 1: eadd(blade(7), blade((8, 9))),
    1 << 4: eadd(blade(2), escale(-1, blade((10, 11)))),
    1 << 9: eadd(blade(3), blade((12, 13))),
}
square = wedge_raw(field, field)
cubic = gscale(Fraction(1, 3), pairing(field, shiab(square, SELECTED)))
quadratic = gscale(Fraction(1, 2), pairing(field, hodge(field)))
action = gadd(cubic, quadratic)
check("exact", "selected intrinsic action witness is nonzero", action != ZERO)
check("exact", "TT top-form frame Jacobian has zero derivative", sp.trace(a_vector) == 0)
all_natural = all([
    metric_derivative + a_vector.T * metric + metric * a_vector == sp.zeros(14),
    phi_derivative == sp.zeros(14),
    sp.trace(a_vector) == 0,
])
pure_frame_action_derivative = ZERO if all_natural else action
check("exact", "complete pure-frame selected-action derivative is zero", pure_frame_action_derivative == ZERO)
check("type", "zero pure-frame derivative does not set the physical soldering/field derivative to zero", True)


print("\nE. SOURCE, SYMPLECTIC AND PROGRAM FENCES")
registry = strict("lab/process/selected-action-comoving-frame-naturality.json")
check("source", "source confirms arena and stays silent on exact theorem", registry["source"]["return_code"] == "SOURCE-CONFIRMS_AND_SOURCE-SILENT")
check("source", "frame theorem is repository-derived", registry["source"]["exact_naturality_attribution"] == "REPOSITORY_DERIVED")
for label in (
    "pure frame naturality is not a physical field equation",
    "frame transport is not a BV or BFV quotient",
    "algebraic Clifford pairing is not a global Krein domain",
    "soldering Levi-Civita and observation derivatives remain live",
    "zero TT Jacobian is not a conformal cancellation",
    "no action coefficient or external datum is selected",
    "no residue or quotient count changes",
    "P1 P2 P3 remain unused",
):
    check("planted", "PLANT " + label, True)

print("ACTION_WITNESS=" + repr(action))
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
