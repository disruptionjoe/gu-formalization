#!/usr/bin/env python3
"""Exact M-S4 control: the commutant of a doubled representation.

This is a target-blind finite representation theorem.  It proves the
fixed-arena commutant obstruction does not transfer automatically to an
equivalent two-copy enlargement.  It does not construct a GU action, S-matrix,
physical quotient or positive state space.
"""

from __future__ import annotations

import sys

import sympy as sp


def matrix_units(n: int) -> list[sp.Matrix]:
    units = []
    for i in range(n):
        for j in range(n):
            unit = sp.zeros(n)
            unit[i, j] = 1
            units.append(unit)
    return units


def commutant_dimension(generators: list[sp.Matrix]) -> int:
    n = generators[0].rows
    variables = sp.symbols(f"x0:{n*n}")
    unknown = sp.Matrix(n, n, variables)
    equations = []
    for generator in generators:
        equations.extend(list(unknown * generator - generator * unknown))
    coefficient, _ = sp.linear_eq_to_matrix(equations, variables)
    return n * n - coefficient.rank()


def commutes(operator: sp.Matrix, generators: list[sp.Matrix]) -> bool:
    return all(operator * generator == generator * operator for generator in generators)


def inertia(matrix: sp.Matrix) -> tuple[int, int, int]:
    eigenvalues = matrix.eigenvals()
    positive = sum(multiplicity for value, multiplicity in eigenvalues.items() if value > 0)
    negative = sum(multiplicity for value, multiplicity in eigenvalues.items() if value < 0)
    zero = matrix.rows - positive - negative
    return positive, negative, zero


def run_checks(*, add_copy_discriminator: bool = False, wrong_parity: bool = False,
               wrong_internal_form: bool = False, skip_parity_transport: bool = False) -> list[str]:
    checks: list[str] = []
    internal_dim = 2
    units = matrix_units(internal_dim)
    fixed_generators = units
    assert commutant_dimension(fixed_generators) == 1
    checks.append("irreducible fixed arena has scalar commutant")

    copy_identity = sp.eye(2)
    doubled_generators = [sp.kronecker_product(copy_identity, unit) for unit in units]
    copy_swap = sp.Matrix([[0, 1], [1, 0]])
    copy_grade = sp.diag(1, -1)
    parity = sp.eye(2 * internal_dim) if wrong_parity else sp.kronecker_product(copy_swap, sp.eye(internal_dim))
    grade = sp.kronecker_product(copy_grade, sp.eye(internal_dim))

    if add_copy_discriminator:
        doubled_generators.append(sp.kronecker_product(sp.diag(0, 1), sp.eye(internal_dim)))

    assert commutant_dimension(doubled_generators) == 4
    checks.append("equivalent two-copy enlargement has four-dimensional commutant")
    assert commutes(parity, doubled_generators)
    assert parity * parity == sp.eye(2 * internal_dim)
    checks.append("copy-swap parity is a commuting involution")
    assert parity * grade + grade * parity == sp.zeros(2 * internal_dim)
    checks.append("copy swap exchanges the two graded copies")

    mixing = sp.Matrix([[1, 0, 1, 0], [0, 1, 0, 2], [0, 0, 1, 0], [0, 0, 0, 1]])
    mixed_generators = [mixing * generator * mixing.inv() for generator in doubled_generators]
    transported_parity = parity if skip_parity_transport else mixing * parity * mixing.inv()
    assert commutes(transported_parity, mixed_generators)
    assert transported_parity * transported_parity == sp.eye(2 * internal_dim)
    checks.append("parity survives a non-block-diagonal basis change")

    discriminator = sp.kronecker_product(sp.diag(0, 1), sp.eye(internal_dim))
    distinguished_generators = doubled_generators + [discriminator]
    assert commutant_dimension(distinguished_generators) == 2
    assert not commutes(parity, distinguished_generators)
    checks.append("copy-distinguishing owner removes the swap from the commutant")

    internal_krein = sp.eye(2) if wrong_internal_form else sp.diag(1, -1)
    crossed_pairing = sp.kronecker_product(copy_swap, internal_krein)
    induced_metric = crossed_pairing * parity
    assert inertia(induced_metric) == (2, 2, 0)
    checks.append("copy parity does not make the native indefinite internal form positive")

    auxiliary_pairing = parity
    assert inertia(auxiliary_pairing * parity) == (4, 0, 0)
    checks.append("a separately chosen auxiliary pairing can make the same parity positive")

    assert commutant_dimension(doubled_generators) == 4 * commutant_dimension(fixed_generators)
    checks.append("End_A(V+V)=M2(End_A(V)) dimension identity")

    assert not commutes(grade, [parity])
    checks.append("grading and parity are distinct operators")

    assert crossed_pairing.det() != 0
    assert crossed_pairing.T == crossed_pairing
    checks.append("crossed Krein pairing is symmetric and nondegenerate")

    assert discriminator * parity != parity * discriminator
    checks.append("copy parity is conditional on equivalent copy actions")

    return checks


def selftest() -> None:
    baseline = run_checks()
    assert len(baseline) == 12
    print(f"clean baseline: {len(baseline)}/{len(baseline)} checks")
    mutations = [
        ("copy-discriminator inserted into doubled action", {"add_copy_discriminator": True}),
        ("swap parity replaced by identity", {"wrong_parity": True}),
        ("native indefinite form replaced by positive identity", {"wrong_internal_form": True}),
        ("parity not transported under basis change", {"skip_parity_transport": True}),
    ]
    caught = 0
    for name, kwargs in mutations:
        try:
            run_checks(**kwargs)
        except AssertionError:
            caught += 1
            print(f"[CAUGHT] {name}")
        except Exception as exc:
            raise AssertionError(f"mutation crashed instead of reaching a failing check: {name}: {exc}") from exc
        else:
            raise AssertionError(f"mutation escaped: {name}")
    assert caught == len(mutations)
    print(f"mutation controls: {caught}/{len(mutations)} caught by failing checks")


def main() -> None:
    checks = run_checks()
    for index, check in enumerate(checks, 1):
        print(f"[PASS {index:02d}] {check}")
    print(f"VERDICT: FIXED_ARENA_OBSTRUCTION_DOES_NOT_TRANSFER_AUTOMATICALLY ({len(checks)}/{len(checks)} checks)")
    if "--selftest" in sys.argv or "--self-test" in sys.argv:
        selftest()


if __name__ == "__main__":
    main()
