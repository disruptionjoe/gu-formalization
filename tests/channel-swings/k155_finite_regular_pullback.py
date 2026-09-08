#!/usr/bin/env python3
"""Exact finite K139 pullbacks and signed-cycle route discriminators.

This module works on K151's finite canonical charge blocks.  It proves an
algebraic identity and finite Neumann error bound.  It deliberately does not
claim the common-carrier coefficient/graph convergence needed to identify the
native continuum regular representative.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from collections import deque
from fractions import Fraction
from itertools import product
from pathlib import Path
from typing import Any, Sequence


def _load_k151():
    path = Path(__file__).with_name("k151_native_charge_block_assembler.py")
    spec = importlib.util.spec_from_file_location("k151_native_charge_block_runtime", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load exact K151 assembler at {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_K151 = _load_k151()
Matrix = _K151.Matrix
State = _K151.State
apply_word = _K151.apply_word
bath_orbital = _K151.bath_orbital
basis = _K151.basis
charge_block = _K151.charge_block
flavor_swap_matrix = _K151.flavor_swap_matrix
matmul = _K151.matmul
occupied = _K151.occupied
q = _K151.q
qstr = _K151.qstr
state_label = _K151.state_label
transpose = _K151.transpose


class CertificateError(ValueError):
    """Raised when exact finite data do not certify the requested result."""


def zero(rows: int, columns: int) -> Matrix:
    return [[Fraction(0) for _ in range(columns)] for _ in range(rows)]


def identity(size: int) -> Matrix:
    return [[Fraction(i == j) for j in range(size)] for i in range(size)]


def add(*matrices: Matrix) -> Matrix:
    if not matrices or not matrices[0]:
        raise CertificateError("matrix sum requires nonempty matrices")
    rows, columns = len(matrices[0]), len(matrices[0][0])
    if any(len(m) != rows or any(len(row) != columns for row in m) for m in matrices):
        raise CertificateError("matrix sum has incompatible shapes")
    return [
        [sum((m[i][j] for m in matrices), Fraction(0)) for j in range(columns)]
        for i in range(rows)
    ]


def scale(value: Fraction, matrix: Matrix) -> Matrix:
    return [[value * entry for entry in row] for row in matrix]


def diagonal(values: Sequence[Fraction]) -> Matrix:
    return [[value if i == j else Fraction(0) for j in range(len(values))] for i, value in enumerate(values)]


def inverse(matrix: Matrix) -> Matrix:
    """Exact Gauss--Jordan inverse."""
    if not matrix or any(len(row) != len(matrix) for row in matrix):
        raise CertificateError("inverse requires a nonempty square matrix")
    size = len(matrix)
    work = [row[:] + unit[:] for row, unit in zip(matrix, identity(size), strict=True)]
    for column in range(size):
        pivot = next((row for row in range(column, size) if work[row][column]), None)
        if pivot is None:
            raise CertificateError("boundary chart is singular")
        work[column], work[pivot] = work[pivot], work[column]
        pivot_value = work[column][column]
        work[column] = [value / pivot_value for value in work[column]]
        for row in range(size):
            if row == column or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [left - factor * right for left, right in zip(work[row], work[column], strict=True)]
    return [row[size:] for row in work]


def matrix_power(matrix: Matrix, exponent: int) -> Matrix:
    if exponent < 0:
        raise CertificateError("matrix exponent must be nonnegative")
    result = identity(len(matrix))
    base = matrix
    power = exponent
    while power:
        if power & 1:
            result = matmul(result, base)
        base = matmul(base, base)
        power //= 2
    return result


def induced_one_norm(matrix: Matrix) -> Fraction:
    return max(sum((abs(matrix[i][j]) for i in range(len(matrix))), Fraction(0)) for j in range(len(matrix[0])))


def induced_infinity_norm(matrix: Matrix) -> Fraction:
    return max(sum((abs(value) for value in row), Fraction(0)) for row in matrix)


def charge_components(
    energies: Sequence[int | str | Fraction],
    couplings: Sequence[int | str | Fraction],
    charge: tuple[int, int],
) -> tuple[list[State], Matrix, Matrix, Matrix]:
    """Return the exact finite ``H0, C, C*`` block in K151's order.

    ``C=d* a_+ + a_- d`` and ``C*`` contains the two adjoint words.  Each
    projected word preserves the hard-core carrier and the selected charge.
    """
    if len(energies) != len(couplings) or not energies:
        raise CertificateError("energies and couplings must have the same nonzero length")
    eps = [q(value) for value in energies]
    gs = [q(value) for value in couplings]
    if any(value <= 0 for value in eps):
        raise CertificateError("finite-mode free energies must be positive")
    mode_count = len(eps)
    states = basis(mode_count, charge, hard_core=True)
    index = {state: position for position, state in enumerate(states)}
    free = zero(len(states), len(states))
    annihilation_half = zero(len(states), len(states))
    creation_half = zero(len(states), len(states))

    for column, state in enumerate(states):
        free[column][column] = sum(
            (
                eps[mode] * occupied(state, bath_orbital(flavor, polarity, mode, mode_count))
                for flavor, polarity, mode in product((0, 1), ("+", "-"), range(mode_count))
            ),
            Fraction(0),
        )
        for flavor in (0, 1):
            for mode, coupling in enumerate(gs):
                plus = bath_orbital(flavor, "+", mode, mode_count)
                minus = bath_orbital(flavor, "-", mode, mode_count)
                halves = (
                    (annihilation_half, ((flavor, True), (plus, False))),
                    (annihilation_half, ((minus, False), (flavor, False))),
                    (creation_half, ((plus, True), (flavor, False))),
                    (creation_half, ((flavor, True), (minus, True))),
                )
                for target_matrix, word in halves:
                    result = apply_word(state, word)
                    if result is None:
                        continue
                    target, sign = result
                    if occupied(target, 0) and occupied(target, 1):
                        continue
                    row = index.get(target)
                    if row is None:
                        raise AssertionError("boundary half left the charge block")
                    target_matrix[row][column] += coupling * sign
    if transpose(annihilation_half) != creation_half:
        raise AssertionError("separated boundary halves are not exact adjoints")
    return states, free, annihilation_half, creation_half


def matched_endpoint_counterterm(
    states: Sequence[State],
    energies: Sequence[int | str | Fraction],
    couplings: Sequence[int | str | Fraction],
    auxiliary_shift: int | str | Fraction,
    finite_boundary_scalar: int | str | Fraction = 0,
) -> Matrix:
    """Two-edge equal-coupling endpoint subtraction on the native C3 carrier."""
    eps = [q(value) for value in energies]
    gs = [q(value) for value in couplings]
    lam = q(auxiliary_shift)
    if lam <= 0:
        raise CertificateError("auxiliary shift must be positive")
    if len(eps) != len(gs):
        raise CertificateError("counterterm inputs have incompatible lengths")
    coefficient = sum((g * g / (energy + lam) for energy, g in zip(eps, gs, strict=True)), Fraction(0))
    boundary = q(finite_boundary_scalar)
    # D=2|0><0|+|1><1|+|2><2| for the two equal signed edges.
    values = [boundary + coefficient * (1 if occupied(state, 0) or occupied(state, 1) else 2) for state in states]
    return diagonal(values)


def regular_pullback(
    energies: Sequence[int | str | Fraction],
    couplings: Sequence[int | str | Fraction],
    charge: tuple[int, int],
    auxiliary_shift: int | str | Fraction,
    finite_boundary_scalar: int | str | Fraction = 0,
) -> dict[str, Any]:
    states, free, c, cstar = charge_components(energies, couplings, charge)
    lam = q(auxiliary_shift)
    if lam <= 0:
        raise CertificateError("auxiliary shift must be positive")
    unit = identity(len(states))
    shifted_free = add(free, scale(lam, unit))
    shifted_inverse = diagonal([Fraction(1, 1) / shifted_free[i][i] for i in range(len(states))])
    g = scale(Fraction(-1), matmul(shifted_inverse, cstar))
    u = add(unit, scale(Fraction(-1), g))
    u_inverse = inverse(u)
    endpoint = matched_endpoint_counterterm(states, energies, couplings, lam, finite_boundary_scalar)
    h = add(free, c, cstar, endpoint)
    direct = matmul(transpose(u_inverse), matmul(h, u_inverse))
    regular_core = add(endpoint, scale(-lam, unit), scale(Fraction(-1), matmul(transpose(g), matmul(shifted_free, g))))
    expanded = add(shifted_free, matmul(transpose(u_inverse), matmul(regular_core, u_inverse)))
    if direct != expanded or matmul(transpose(u), matmul(direct, u)) != h:
        raise AssertionError("exact regular pullback identities failed")
    return {
        "states": states,
        "auxiliary_shift": lam,
        "free": free,
        "shifted_free": shifted_free,
        "C": c,
        "Cstar": cstar,
        "endpoint": endpoint,
        "H": h,
        "G": g,
        "U": u,
        "U_inverse": u_inverse,
        "regular_core": regular_core,
        "R": direct,
    }


def neumann_regular_tail_bound(packet: dict[str, Any], word_order: int) -> dict[str, Fraction]:
    if word_order < 0:
        raise CertificateError("word order must be nonnegative")
    g, w, exact = packet["G"], packet["regular_core"], packet["R"]
    q_one, q_inf = induced_one_norm(g), induced_infinity_norm(g)
    if q_one >= 1 or q_inf >= 1:
        raise CertificateError("finite one/infinity norm contractions are both required")
    partial = zero(len(g), len(g))
    for exponent in range(word_order + 1):
        partial = add(partial, matrix_power(g, exponent))
    approximation = add(
        packet["shifted_free"],
        matmul(transpose(partial), matmul(w, partial)),
    )
    tail_one = q_one ** (word_order + 1) / (1 - q_one)
    tail_inf = q_inf ** (word_order + 1) / (1 - q_inf)
    bound = induced_infinity_norm(w) * (
        tail_one / (1 - q_inf) + tail_inf / (1 - q_one)
    )
    actual = induced_infinity_norm(add(exact, scale(Fraction(-1), approximation)))
    if actual > bound:
        raise AssertionError("certified Neumann bound does not dominate the exact error")
    return {
        "one_norm_contraction": q_one,
        "infinity_norm_contraction": q_inf,
        "one_norm_inverse_tail": tail_one,
        "infinity_norm_inverse_tail": tail_inf,
        "regular_matrix_error_upper": bound,
        "regular_matrix_error_actual": actual,
    }


def signed_components(matrix: Matrix) -> list[tuple[int, int, Fraction]]:
    return [
        (i, j, matrix[i][j])
        for i in range(len(matrix))
        for j in range(i)
        if matrix[i][j]
    ]


def stoquastic_gauge_certificate(matrix: Matrix) -> dict[str, Any]:
    """Decide diagonal +/-1 gauge stoquasticity and return a conflict cycle."""
    if not matrix or any(len(row) != len(matrix) for row in matrix):
        raise CertificateError("stoquasticity requires a nonempty square matrix")
    if matrix != transpose(matrix):
        raise CertificateError("stoquasticity requires a symmetric matrix")
    adjacency: list[list[tuple[int, int, Fraction]]] = [[] for _ in matrix]
    for left, right, value in signed_components(matrix):
        required_product = -1 if value > 0 else 1
        adjacency[left].append((right, required_product, value))
        adjacency[right].append((left, required_product, value))
    seen: set[int] = set()
    components = 0
    for root in range(len(matrix)):
        if root in seen:
            continue
        components += 1
        seen.add(root)
        queue: deque[int] = deque([root])
        while queue:
            here = queue.popleft()
            for there, _, _ in adjacency[here]:
                if there not in seen:
                    seen.add(there)
                    queue.append(there)
    signs: list[int | None] = [None] * len(matrix)
    parent: list[int | None] = [None] * len(matrix)
    conflict: tuple[int, int, Fraction] | None = None
    for root in range(len(matrix)):
        if signs[root] is not None:
            continue
        signs[root] = 1
        queue: deque[int] = deque([root])
        while queue and conflict is None:
            here = queue.popleft()
            for there, required, value in sorted(adjacency[here]):
                expected = signs[here] * required
                if signs[there] is None:
                    signs[there] = expected
                    parent[there] = here
                    queue.append(there)
                elif signs[there] != expected:
                    conflict = (here, there, value)
                    break
        if conflict is not None:
            break
    if conflict is None:
        gauge = [int(value) for value in signs]
        transformed = [
            [Fraction(gauge[i] * gauge[j]) * matrix[i][j] for j in range(len(matrix))]
            for i in range(len(matrix))
        ]
        if any(transformed[i][j] > 0 for i in range(len(matrix)) for j in range(i)):
            raise AssertionError("reported gauge does not make off-diagonals nonpositive")
        return {"stoquastic_diagonal_sign_gauge_exists": True, "components": components, "gauge": gauge, "cycle": None}

    left, right, _ = conflict
    left_path: list[int] = []
    cursor: int | None = left
    while cursor is not None:
        left_path.append(cursor)
        cursor = parent[cursor]
    right_path: list[int] = []
    cursor = right
    while cursor is not None:
        right_path.append(cursor)
        cursor = parent[cursor]
    left_ancestors = set(left_path)
    common = next(vertex for vertex in right_path if vertex in left_ancestors)
    cycle = left_path[: left_path.index(common) + 1] + list(reversed(right_path[: right_path.index(common)]))
    edge_values = [matrix[cycle[(i + 1) % len(cycle)]][cycle[i]] for i in range(len(cycle))]
    sign_product = product_sign(edge_values)
    if sign_product == (-1) ** len(cycle):
        raise AssertionError("reported cycle is not sign-frustrated")
    return {
        "stoquastic_diagonal_sign_gauge_exists": False,
        "components": components,
        "gauge": None,
        "cycle": cycle,
        "cycle_edge_values": edge_values,
        "cycle_sign_product": sign_product,
        "stoquastic_required_sign_product": (-1) ** len(cycle),
    }


def product_sign(values: Sequence[Fraction]) -> int:
    result = 1
    for value in values:
        if not value:
            raise CertificateError("cycle edges must be nonzero")
        result *= 1 if value > 0 else -1
    return result


def flavor_covariant(
    energies: Sequence[int | str | Fraction],
    couplings: Sequence[int | str | Fraction],
    charge: tuple[int, int],
    auxiliary_shift: int | str | Fraction,
) -> bool:
    source = regular_pullback(energies, couplings, charge, auxiliary_shift)
    target_charge = (charge[1], charge[0])
    target = regular_pullback(energies, couplings, target_charge, auxiliary_shift)
    swap = flavor_swap_matrix(source["states"], target["states"], len(energies))
    return matmul(target["R"], swap) == matmul(swap, source["R"]) and matmul(transpose(swap), swap) == identity(len(source["states"]))


def demo() -> dict[str, Any]:
    energies = ["5/4", "3/2"]
    couplings = ["1", "1"]
    pullback = regular_pullback(energies, couplings, (0, 0), 256)
    tail = neumann_regular_tail_bound(pullback, 3)
    interaction = add(pullback["C"], pullback["Cstar"])
    sign = stoquastic_gauge_certificate(interaction)
    return {
        "schema_version": "1.0",
        "arithmetic": "exact_rational_finite_regulator",
        "charge": [0, 0],
        "mode_count": 2,
        "basis_dimension": len(pullback["states"]),
        "exact_pullback_identity": True,
        "exact_expanded_regular_identity": True,
        "finite_neumann_tail": {key: qstr(value) for key, value in tail.items()},
        "flavor_swap_intertwines_regular_pullback": flavor_covariant(energies, couplings, (1, 0), 256),
        "interaction_graph_components": sign["components"],
        "stoquastic_diagonal_sign_gauge_exists": sign["stoquastic_diagonal_sign_gauge_exists"],
        "frustrated_cycle_length": len(sign["cycle"]),
        "frustrated_cycle_states": [state_label(pullback["states"][vertex], 2) for vertex in sign["cycle"]],
        "frustrated_cycle_edge_values": [qstr(value) for value in sign["cycle_edge_values"]],
        "frustrated_cycle_sign_product": sign["cycle_sign_product"],
        "continuum_R256_identified": False,
        "native_ground_count_certified": False,
        "standard_occupation_basis_Perron_Frobenius_route_available": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true", required=True)
    parser.parse_args()
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
