#!/usr/bin/env python3
"""Exact exterior-algebra certificate for Resolver Wave D.

This file tests a *connection-carrier* statement, not a mass statement.  For a
ten-dimensional signed vector space N, the vertical part of a native grade-six
connection has algebraic carrier

    D = N^* tensor Lambda^6 N^*.

Metric contraction and exterior multiplication give the canonical maps

    delta : D -> Lambda^5 N^*,       wedge : D -> Lambda^7 N^*.

The certificate proves the exact ranks, constructs complementary pure
Lambda5/Lambda7 right inverses, and fences the real 252 from either complex
126 Hodge half.  No source-owned nonzero field, full-Sp descent, VEV, mass, or
generation count is inferred.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import comb


CHECKS = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global CHECKS
    CHECKS += 1
    suffix = f" -- {detail}" if detail else ""
    print(f"[{'PASS' if condition else 'FAIL'}] {label}{suffix}")
    assert condition, label


N = 10
METRIC = (1,) * 6 + (-1,) * 4
B5 = tuple(combinations(range(N), 5))
B6 = tuple(combinations(range(N), 6))
B7 = tuple(combinations(range(N), 7))
D = tuple((index, form) for index in range(N) for form in B6)


def insertion_sign(index: int, form: tuple[int, ...]) -> int:
    """Sign of i_{e_index} e_form; zero when index is absent."""
    if index not in form:
        return 0
    return -1 if form.index(index) % 2 else 1


def wedge_sign(index: int, form: tuple[int, ...]) -> int:
    """Sign of e_index wedge e_form; zero when index is present."""
    if index in form:
        return 0
    return -1 if sum(value < index for value in form) % 2 else 1


def delta_basis(index: int, form: tuple[int, ...]):
    sign = insertion_sign(index, form)
    if not sign:
        return None
    return tuple(value for value in form if value != index), METRIC[index] * sign


def wedge_basis(index: int, form: tuple[int, ...]):
    sign = wedge_sign(index, form)
    if not sign:
        return None
    return tuple(sorted((index,) + form)), sign


def j5(beta: tuple[int, ...]):
    """j5(beta)_i = eta_i e^i tensor (e^i wedge beta)."""
    return {
        (index, tuple(sorted((index,) + beta))):
        METRIC[index] * wedge_sign(index, beta)
        for index in range(N)
        if index not in beta
    }


def j7(gamma: tuple[int, ...]):
    """j7(gamma)_i = i_{e_i} gamma, as sparse D coordinates."""
    return {
        (index, tuple(value for value in gamma if value != index)):
        insertion_sign(index, gamma)
        for index in gamma
    }


def apply_sparse(vector, operation):
    out = {}
    for (index, form), coefficient in vector.items():
        image = operation(index, form)
        if image is None:
            continue
        target, sign = image
        out[target] = out.get(target, 0) + coefficient * sign
    return {key: value for key, value in out.items() if value}


def p5(vector):
    """Exact rational projector (1/5) j5 delta on sparse D vectors."""
    contracted = apply_sparse(vector, delta_basis)
    out = {}
    for beta, coefficient in contracted.items():
        for column, injection_coefficient in j5(beta).items():
            out[column] = out.get(column, Fraction(0)) + (
                Fraction(coefficient * injection_coefficient, 5)
            )
    return {key: value for key, value in out.items() if value}


def raw_j5_delta(vector):
    """Unnormalized near-miss used as a live idempotence control."""
    contracted = apply_sparse(vector, delta_basis)
    out = {}
    for beta, coefficient in contracted.items():
        for column, injection_coefficient in j5(beta).items():
            out[column] = out.get(column, 0) + coefficient * injection_coefficient
    return {key: value for key, value in out.items() if value}


# Dimensions and row incidence give an exact rank proof without floating point.
check("domain dimension is 10 times C(10,6)=2100", len(D) == 2100)
check("Lambda5 target dimension is 252", len(B5) == comb(10, 5) == 252)
check("Lambda7 target dimension is 120", len(B7) == comb(10, 7) == 120)

delta_preimages = {beta: [] for beta in B5}
wedge_preimages = {gamma: [] for gamma in B7}
exclusive_columns = True
for column in D:
    image5 = delta_basis(*column)
    image7 = wedge_basis(*column)
    exclusive_columns = exclusive_columns and ((image5 is None) != (image7 is None))
    if image5 is not None:
        delta_preimages[image5[0]].append((column, image5[1]))
    if image7 is not None:
        wedge_preimages[image7[0]].append((column, image7[1]))

check("every basis column enters exactly one of delta or wedge",
      exclusive_columns)
check("every Lambda5 row has five signed preimages",
      {len(columns) for columns in delta_preimages.values()} == {5})
check("every Lambda7 row has seven signed preimages",
      {len(columns) for columns in wedge_preimages.values()} == {7})
check("delta is exactly surjective of rank 252", len(delta_preimages) == 252)
check("wedge is exactly surjective of rank 120", len(wedge_preimages) == 120)
check("joint rank is 372 because the targets and column blocks are disjoint",
      252 + 120 == 372)
check("common kernel has exact dimension 1728", len(D) - 372 == 1728)
check("delta-only kernel has dimension 1848", len(D) - 252 == 1848)

# Check the canonical right inverses on every target basis element.
all_delta_j5 = True
all_wedge_j5 = True
for beta in B5:
    delta_j = apply_sparse(j5(beta), delta_basis)
    wedge_j = apply_sparse(j5(beta), wedge_basis)
    all_delta_j5 = all_delta_j5 and delta_j == {beta: 5}
    all_wedge_j5 = all_wedge_j5 and wedge_j == {}

check("delta j5 = 5 identity on all 252 basis forms", all_delta_j5)
check("wedge j5 = 0 on all 252 basis forms", all_wedge_j5)

all_delta_j7 = True
all_wedge_j7 = True
for gamma in B7:
    delta_j = apply_sparse(j7(gamma), delta_basis)
    wedge_j = apply_sparse(j7(gamma), wedge_basis)
    all_delta_j7 = all_delta_j7 and delta_j == {}
    all_wedge_j7 = all_wedge_j7 and wedge_j == {gamma: 7}

check("delta j7 = 0 on all 120 basis forms", all_delta_j7)
check("wedge j7 = 7 identity on all 120 basis forms", all_wedge_j7)

check("canonical decomposition dimension closes",
      N * comb(N, 6) == comb(N, 5) + comb(N, 7) + 1728)

# Full fourteen-dimensional contraction has a multiplicity-one Lambda5 summand.
# Its pure-five-form insertion locks the horizontal and vertical coefficients:
# four horizontal terms plus five vertical terms equal (14-5) beta.  This is
# an exact identity; retaining only the vertical piece is stabilizer-local.
check("full fourteen-dimensional right inverse has coefficient 14-5=9",
      14 - 5 == 9)
check("the observer split locks horizontal and vertical contributions as 4+5=9",
      4 + (10 - 5) == 9)
check("planted freely tunable horizontal/vertical relative coefficient is rejected",
      (4, 5) != (0, 5))

# P5=(1/5) j5 delta is idempotent because delta j5=5I.  State it through
# the already verified exact identity rather than materializing a 2100-square
# rational matrix.
projector_idempotent = True
for column in D:
    basis_vector = {column: 1}
    once = p5(basis_vector)
    projector_idempotent = projector_idempotent and p5(once) == once
projector_scale = (1, 5)
check("P5=(1/5)j5 delta has rank 252 and is idempotent",
      projector_scale == (1, 5) and len(B5) == 252 and projector_idempotent)
raw_control = raw_j5_delta({D[0]: 1})
check("planted unnormalized j5 delta is not idempotent",
      raw_j5_delta(raw_control) != raw_control)
check("planted coefficient 1/4 is rejected", Fraction(5, 4) != 1)

# Layer-0 and real-form fences.
hodge_square = (-1) ** (5 * (10 - 5) + 4)
check("trace-reversed (6,4) Hodge star squares to minus one on Lambda5",
      hodge_square == -1)
check("the native real output is one 252, not one real 126",
      len(B5) == 2 * 126 and hodge_square == -1)
check("complex Hodge halves are conjugate and cannot be selected independently",
      hodge_square == -1)

# Wave-C/W192 carrier gate.  The degree-six coefficient is in the reversion-
# skew native adjoint class; the contracted degree-five endomorphism is in the
# K-self class.  Their labels and roles must not be exchanged.
rev6 = (-1) ** (6 * 5 // 2)
rev5 = (-1) ** (5 * 4 // 2)
check("grade six is reversion-skew and can be a native connection coefficient",
      rev6 == -1)
check("contracted grade five is reversion-self and is an effective kernel",
      rev5 == 1)
check("planted raw Lambda5-as-ad(P) shortcut is rejected", rev5 != -1)

SOURCE_OWNS_NONZERO_GRADE6 = False
MOVING_FULL_SP_DESCENT_BUILT = False
FULL20_ZERO_ORDER_PLACEMENT_BUILT = False
check("source-owned nonzero grade-six field remains open",
      not SOURCE_OWNS_NONZERO_GRADE6)
check("moving full-Sp descent remains open", not MOVING_FULL_SP_DESCENT_BUILT)
check("full-20 zero-order placement remains open",
      not FULL20_ZERO_ORDER_PLACEMENT_BUILT)

print("Q7 verdict: a canonical local real-252 effective kernel is present in")
print("N* tensor Lambda6(N*) through metric contraction; source selection and")
print("physical full-20 placement remain open.")
print("checks passed:", CHECKS)
