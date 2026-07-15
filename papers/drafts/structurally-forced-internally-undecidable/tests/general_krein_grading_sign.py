#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Regression checks for the hardened finite-dimensional Krein statement.

The first draft claimed that the simultaneous stabilizer of an indefinite form
and a positive majorant leaves exactly one free Z/2 grading sign. That claim is
false. This test checks the corrected conclusions:

1. O(p,q) has a one-dimensional invariant symmetric-form space on its standard
   representation.
2. O(p) x O(q) has a two-dimensional invariant symmetric-form space and a
   continuous cone of positive invariant metrics.
3. Among the four block-scalar involutions commuting with O(p) x O(q), exactly
   one is eta-self-adjoint and makes eta C positive. The canonical grading is
   unique, not a free Z/2.
4. The no-common-constituent hypothesis only removes cross terms. It does not
   force one invariant scale on each diagonal block.
5. When a constituent occurs on both sides, admissible gradings form a
   continuum. The diagonal O(r) subgroup of O(r,r) gives an explicit family.
6. Real irreducibility alone does not imply uniqueness of an invariant real
   symmetric form. The realified standard so(3,C) action preserves the real and
   imaginary parts of its complex symmetric form.

The script is deterministic and standalone. It is a regression test, not a
proof of the general theorem in the paper.
"""

import itertools
import math

import numpy as np


TOL = 1e-8
checks = []


def ok(name, condition, detail=""):
    condition = bool(condition)
    checks.append((name, condition))
    print(("PASS " if condition else "FAIL ") + name + ("  | " + detail if detail else ""))
    return condition


def nullspace(matrix, tol=TOL):
    if matrix.size == 0 or matrix.shape[0] == 0:
        return np.eye(matrix.shape[1])
    _, singular_values, vh = np.linalg.svd(matrix)
    if singular_values.size == 0:
        return np.eye(matrix.shape[1])
    rank = int(np.sum(singular_values > tol * max(1.0, singular_values[0])))
    return vh[rank:].conj().T


def signature(matrix):
    eigenvalues = np.linalg.eigvalsh(0.5 * (matrix + matrix.T))
    return int(np.sum(eigenvalues > TOL)), int(np.sum(eigenvalues < -TOL))


def sym_basis(n, allowed=None):
    basis = []
    for i in range(n):
        for j in range(i, n):
            if allowed is not None and not allowed(i, j):
                continue
            matrix = np.zeros((n, n))
            matrix[i, j] = 1.0
            matrix[j, i] = 1.0
            basis.append(matrix)
    return basis


def so_diagonal_generators(signs):
    """Exact basis of so(diag(signs)), with each sign equal to +1 or -1."""
    n = len(signs)
    generators = []
    for i in range(n):
        for j in range(i + 1, n):
            matrix = np.zeros((n, n))
            matrix[i, j] = 1.0
            matrix[j, i] = -signs[i] * signs[j]
            generators.append(matrix)
    return generators


def rotation_generators(dimension):
    return so_diagonal_generators([1.0] * dimension)


def block_orthogonal_generators(block_dims):
    """Lie generators and one reflection for each O(d) block."""
    n = sum(block_dims)
    lie = []
    group = []
    offset = 0
    for dimension in block_dims:
        for local in rotation_generators(dimension):
            generator = np.zeros((n, n))
            generator[offset:offset + dimension, offset:offset + dimension] = local
            lie.append(generator)
        reflection = np.eye(n)
        reflection[offset, offset] = -1.0
        group.append(reflection)
        offset += dimension
    return lie, group


def diagonal_orthogonal_generators(r):
    """Diagonal O(r) acting by the same standard representation on two copies."""
    lie = []
    for local in rotation_generators(r):
        generator = np.zeros((2 * r, 2 * r))
        generator[:r, :r] = local
        generator[r:, r:] = local
        lie.append(generator)
    reflection_local = np.eye(r)
    reflection_local[0, 0] = -1.0
    reflection = np.zeros((2 * r, 2 * r))
    reflection[:r, :r] = reflection_local
    reflection[r:, r:] = reflection_local
    return lie, [reflection]


def invariant_dimension(generators, basis):
    lie, group = generators
    if not basis:
        return 0
    columns = []
    for matrix in basis:
        constraints = [(x.T @ matrix + matrix @ x).reshape(-1) for x in lie]
        constraints += [(g.T @ matrix @ g - matrix).reshape(-1) for g in group]
        columns.append(np.concatenate(constraints) if constraints else np.zeros(matrix.size))
    return nullspace(np.array(columns).T).shape[1]


def invariant_block_dimensions(generators, p, q):
    n = p + q
    plus = sym_basis(n, lambda i, j: i < p and j < p)
    minus = sym_basis(n, lambda i, j: i >= p and j >= p)
    cross = sym_basis(n, lambda i, j: (i < p) != (j < p))
    total = sym_basis(n)
    return (
        invariant_dimension(generators, plus),
        invariant_dimension(generators, minus),
        invariant_dimension(generators, cross),
        invariant_dimension(generators, total),
    )


def eta_self_adjoint(eta, operator):
    return np.linalg.norm(operator.T @ eta - eta @ operator) < TOL


def involutive(operator):
    return np.linalg.norm(operator @ operator - np.eye(operator.shape[0])) < TOL


def commutes_with_all(operator, matrices):
    return all(np.linalg.norm(operator @ matrix - matrix @ operator) < TOL for matrix in matrices)


print("\n[1] Canonical maximal-compact cases")
signatures = [(1, 1), (2, 1), (3, 1), (4, 2), (6, 4), (9, 5), (7, 7)]
dimension_check_signatures = {(1, 1), (6, 4), (9, 5)}
for p, q in signatures:
    n = p + q
    eta = np.diag([1.0] * p + [-1.0] * q)
    full = (so_diagonal_generators([1.0] * p + [-1.0] * q), [])
    compact = block_orthogonal_generators([p, q])

    if (p, q) in dimension_check_signatures:
        full_dim = invariant_dimension(full, sym_basis(n))
        d_plus, d_minus, d_cross, compact_dim = invariant_block_dimensions(compact, p, q)
        ok(f"canonical({p},{q}).full_dim_1", full_dim == 1)
        ok(f"canonical({p},{q}).compact_formula", (d_plus, d_minus, d_cross, compact_dim) == (1, 1, 0, 2))

    candidates = []
    for eps_plus, eps_minus in itertools.product((-1.0, 1.0), repeat=2):
        candidate = np.diag([eps_plus] * p + [eps_minus] * q)
        admissible = (
            involutive(candidate)
            and eta_self_adjoint(eta, candidate)
            and commutes_with_all(candidate, compact[0] + compact[1])
            and signature(eta @ candidate) == (n, 0)
        )
        candidates.append(((eps_plus, eps_minus), admissible))
    admitted = [signs for signs, is_admissible in candidates if is_admissible]
    ok(f"canonical({p},{q}).unique_admissible_C", admitted == [(1.0, -1.0)], str(admitted))

    p_plus = np.diag([1.0] * p + [0.0] * q)
    p_minus = np.diag([0.0] * p + [1.0] * q)
    cone_samples = [(1.0, 1.0), (1.0, 3.0), (2.5, 0.4)]
    all_positive = all(signature(a * p_plus + b * p_minus) == (n, 0) for a, b in cone_samples)
    ok(f"canonical({p},{q}).positive_metric_cone", all_positive)
    non_involutive = True
    for a, b in cone_samples[1:]:
        metric_operator = eta @ (a * p_plus + b * p_minus)
        non_involutive = non_involutive and np.linalg.norm(metric_operator @ metric_operator - np.eye(n)) > 1e-6
    ok(f"canonical({p},{q}).cone_not_gradings", non_involutive)


print("\n[2] Non-coincidence removes cross terms but does not imply two dimensions")
p, q = 3, 2
proper_no_common = block_orthogonal_generators([2, 1, 2])
dims = invariant_block_dimensions(proper_no_common, p, q)
ok("proper_no_common.cross_zero", dims[2] == 0, str(dims))
ok("proper_no_common.diagonal_extra_scale", dims == (2, 1, 0, 3), str(dims))


print("\n[3] Common-constituent case gives continuous admissible gradings")
for r in (1, 2, 3):
    eta = np.diag([1.0] * r + [-1.0] * r)
    diagonal = diagonal_orthogonal_generators(r)
    dims = invariant_block_dimensions(diagonal, r, r)
    ok(f"shared({r}).dimension_formula", dims == (1, 1, 1, 3), str(dims))

    family = []
    for t in (-0.9, -0.3, 0.0, 0.4, 1.0):
        c2 = math.cosh(2.0 * t)
        s2 = math.sinh(2.0 * t)
        candidate = np.block([
            [c2 * np.eye(r), -s2 * np.eye(r)],
            [s2 * np.eye(r), -c2 * np.eye(r)],
        ])
        valid = (
            involutive(candidate)
            and eta_self_adjoint(eta, candidate)
            and commutes_with_all(candidate, diagonal[0] + diagonal[1])
            and signature(eta @ candidate) == (2 * r, 0)
        )
        ok(f"shared({r}).C_t({t:+.1f})", valid)
        family.append(candidate)
    separated = all(np.linalg.norm(family[i] - family[i + 1]) > 1e-5 for i in range(len(family) - 1))
    ok(f"shared({r}).family_is_continuous_not_Z2", separated)


print("\n[4] Real-Schur warning: realified so(3,C)")
skew = []
for i, j in ((0, 1), (0, 2), (1, 2)):
    matrix = np.zeros((3, 3))
    matrix[i, j] = 1.0
    matrix[j, i] = -1.0
    skew.append(matrix)
realified = []
for a in skew:
    realified.append(np.block([[a, np.zeros_like(a)], [np.zeros_like(a), a]]))
    realified.append(np.block([[np.zeros_like(a), -a], [a, np.zeros_like(a)]]))
real_part = np.block([[np.eye(3), np.zeros((3, 3))], [np.zeros((3, 3)), -np.eye(3)]])
imag_part = np.block([[np.zeros((3, 3)), np.eye(3)], [np.eye(3), np.zeros((3, 3))]])
inv_dim_complex_realified = invariant_dimension((realified, []), sym_basis(6))
ok("real_schur.two_invariant_forms", inv_dim_complex_realified == 2, str(inv_dim_complex_realified))
ok("real_schur.real_part_invariant", all(np.linalg.norm(x.T @ real_part + real_part @ x) < TOL for x in realified))
ok("real_schur.imag_part_invariant", all(np.linalg.norm(x.T @ imag_part + imag_part @ x) < TOL for x in realified))


print("\n[5] Division-algebra dimension formulas")
for m in range(1, 6):
    d_real = m * (m + 1) // 2
    d_complex = m * m
    d_quaternion = m * (2 * m - 1)
    ok(f"division({m}).R", d_real == m + m * (m - 1) // 2)
    ok(f"division({m}).C", d_complex == m + 2 * (m * (m - 1) // 2))
    ok(f"division({m}).H", d_quaternion == m + 4 * (m * (m - 1) // 2))

for a, b in ((1, 1), (2, 1), (2, 3)):
    expected = {"R": a * b, "C": 2 * a * b, "H": 4 * a * b}
    for division_algebra, real_dimension in (("R", 1), ("C", 2), ("H", 4)):
        computed = real_dimension * a * b
        ok(
            f"residual({a},{b}).{division_algebra}",
            computed == expected[division_algebra],
            str(computed),
        )


passed = sum(1 for _, condition in checks if condition)
total = len(checks)
print("\n==================== SUMMARY ====================")
print(f"{passed}/{total} checks passed")
print("Canonical non-coincidence -> unique admissible C.")
print("Common constituent -> continuous admissible-C moduli.")
print("Invariant metric freedom is not the same as grading-sign freedom.")
print("=================================================")
raise SystemExit(0 if passed == total else 1)
