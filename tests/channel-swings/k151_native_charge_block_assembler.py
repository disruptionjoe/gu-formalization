#!/usr/bin/env python3
"""Exact finite-mode charge blocks for the K148 native hard-core corner.

The finite matrices are regulator controls and conforming form-core data.  The
module also exposes the ultraviolet discriminator that prevents their finite
off-diagonal norms from being passed to K150 as a continuum-uniform bound.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import product
from typing import Iterable, Sequence


State = int
Matrix = list[list[Fraction]]


def q(value: int | str | Fraction) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    return Fraction(value)


def occupied(state: State, orbital: int) -> int:
    return (state >> orbital) & 1


def apply_car(state: State, orbital: int, create: bool) -> tuple[State, int] | None:
    """Apply a canonical CAR generator in the global orbital ordering."""
    here = occupied(state, orbital)
    if here == int(create):
        return None
    sign = -1 if (state & ((1 << orbital) - 1)).bit_count() % 2 else 1
    return state ^ (1 << orbital), sign


def apply_word(
    state: State, operators_left_to_right: Sequence[tuple[int, bool]]
) -> tuple[State, int] | None:
    coefficient = 1
    current = state
    for orbital, create in reversed(operators_left_to_right):
        result = apply_car(current, orbital, create)
        if result is None:
            return None
        current, sign = result
        coefficient *= sign
    return current, coefficient


def bath_orbital(flavor: int, polarity: str, mode: int, mode_count: int) -> int:
    if flavor not in (0, 1) or polarity not in ("+", "-"):
        raise ValueError("invalid flavor or polarity")
    species = 2 * flavor + (polarity == "-")
    return 2 + species * mode_count + mode


def is_hard_core(state: State) -> bool:
    return not (occupied(state, 0) and occupied(state, 1))


def charges(state: State, mode_count: int) -> tuple[int, int]:
    out = []
    for flavor in (0, 1):
        particles = sum(
            occupied(state, bath_orbital(flavor, "+", mode, mode_count))
            for mode in range(mode_count)
        )
        holes = sum(
            occupied(state, bath_orbital(flavor, "-", mode, mode_count))
            for mode in range(mode_count)
        )
        out.append(occupied(state, flavor) + particles - holes)
    return out[0], out[1]


def basis(mode_count: int, charge: tuple[int, int], hard_core: bool = True) -> list[State]:
    if mode_count <= 0:
        raise ValueError("mode_count must be positive")
    orbitals = 2 + 4 * mode_count
    return [
        state
        for state in range(1 << orbitals)
        if (not hard_core or is_hard_core(state)) and charges(state, mode_count) == charge
    ]


def state_label(state: State, mode_count: int) -> str:
    impurity = "0"
    if occupied(state, 0):
        impurity = "1"
    elif occupied(state, 1):
        impurity = "2"
    bath = []
    for flavor, polarity, mode in product((0, 1), ("+", "-"), range(mode_count)):
        if occupied(state, bath_orbital(flavor, polarity, mode, mode_count)):
            bath.append(f"{flavor + 1}{polarity}:{mode}")
    return f"|{impurity};{','.join(bath) or '-'}>"


def _add(matrix: Matrix, row: int, column: int, value: Fraction) -> None:
    matrix[row][column] += value


def charge_block(
    energies: Sequence[int | str | Fraction],
    couplings: Sequence[int | str | Fraction],
    charge: tuple[int, int],
    *,
    hard_core: bool = True,
    penalty: int | str | Fraction = 0,
) -> tuple[list[State], Matrix]:
    """Build the exact K146/K148 signed finite-mode block.

    Global orbital order is ``d1,d2,(1,+),(1,-),(2,+),(2,-)`` with modes
    increasing inside each bath species.  The interaction is

      d_i^* a_i+ + a_i+^* d_i + d_i^* a_i-^* + a_i- d_i.

    Restricting away double impurity occupation gives K148's native C3
    carrier.  Allowing it and adding ``penalty*n1*n2`` gives K149's auxiliary
    finite-U control.
    """
    if len(energies) != len(couplings) or not energies:
        raise ValueError("energies and couplings must have the same nonzero length")
    eps = [q(value) for value in energies]
    gs = [q(value) for value in couplings]
    if any(value <= 0 for value in eps):
        raise ValueError("finite-mode free energies must be positive")
    mode_count = len(eps)
    states = basis(mode_count, charge, hard_core=hard_core)
    index = {state: position for position, state in enumerate(states)}
    matrix = [[Fraction(0) for _ in states] for _ in states]
    penalty_q = q(penalty)

    for column, state in enumerate(states):
        free = Fraction(0)
        for flavor, polarity, mode in product((0, 1), ("+", "-"), range(mode_count)):
            free += eps[mode] * occupied(
                state, bath_orbital(flavor, polarity, mode, mode_count)
            )
        if occupied(state, 0) and occupied(state, 1):
            free += penalty_q
        _add(matrix, column, column, free)

        for flavor in (0, 1):
            for mode, coupling in enumerate(gs):
                plus = bath_orbital(flavor, "+", mode, mode_count)
                minus = bath_orbital(flavor, "-", mode, mode_count)
                words = (
                    ((flavor, True), (plus, False)),
                    ((plus, True), (flavor, False)),
                    ((flavor, True), (minus, True)),
                    ((minus, False), (flavor, False)),
                )
                for word in words:
                    result = apply_word(state, word)
                    if result is None:
                        continue
                    target, sign = result
                    if hard_core and not is_hard_core(target):
                        continue
                    row = index.get(target)
                    if row is None:
                        raise AssertionError("interaction left the fixed charge sector")
                    _add(matrix, row, column, coupling * sign)

    if any(matrix[i][j] != matrix[j][i] for i in range(len(states)) for j in range(len(states))):
        raise AssertionError("assembled Hamiltonian is not exactly symmetric")
    return states, matrix


def induced_permutation_sign(state: State, orbital_map: Sequence[int]) -> int:
    images = [orbital_map[i] for i in range(len(orbital_map)) if occupied(state, i)]
    inversions = sum(images[i] > images[j] for i in range(len(images)) for j in range(i + 1, len(images)))
    return -1 if inversions % 2 else 1


def flavor_swap(state: State, mode_count: int) -> tuple[State, int]:
    orbitals = 2 + 4 * mode_count
    mapping = list(range(orbitals))
    mapping[0], mapping[1] = 1, 0
    for polarity in ("+", "-"):
        for mode in range(mode_count):
            left = bath_orbital(0, polarity, mode, mode_count)
            right = bath_orbital(1, polarity, mode, mode_count)
            mapping[left], mapping[right] = right, left
    target = sum(1 << mapping[i] for i in range(orbitals) if occupied(state, i))
    return target, induced_permutation_sign(state, mapping)


def flavor_swap_matrix(source: Sequence[State], target: Sequence[State], mode_count: int) -> Matrix:
    target_index = {state: position for position, state in enumerate(target)}
    result = [[Fraction(0) for _ in source] for _ in target]
    for column, state in enumerate(source):
        mapped, sign = flavor_swap(state, mode_count)
        if mapped not in target_index:
            raise ValueError("target basis is not the swapped charge sector")
        result[target_index[mapped]][column] = Fraction(sign)
    return result


def transpose(matrix: Matrix) -> Matrix:
    return [list(row) for row in zip(*matrix)]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    if not left or not right or len(left[0]) != len(right):
        raise ValueError("incompatible matrix sizes")
    return [
        [sum((left[i][k] * right[k][j] for k in range(len(right))), Fraction(0)) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def flavor_intertwines(
    energies: Sequence[int | str | Fraction],
    couplings: Sequence[int | str | Fraction],
    charge: tuple[int, int],
) -> bool:
    source, h_source = charge_block(energies, couplings, charge)
    target_charge = charge[1], charge[0]
    target, h_target = charge_block(energies, couplings, target_charge)
    unitary = flavor_swap_matrix(source, target, len(energies))
    return matmul(h_target, unitary) == matmul(unitary, h_source) and matmul(
        transpose(unitary), unitary
    ) == [[Fraction(i == j) for j in range(len(source))] for i in range(len(source))]


def particle_hole_complement_preserves_native(state: State) -> bool:
    """Tempting two-flavor impurity complement fails already on the vacuum."""
    complemented = state ^ 0b11
    return is_hard_core(complemented)


def point_tail_norm_sq(couplings: Iterable[int | str | Fraction]) -> Fraction:
    """Vacuum-to-one-particle norm square of an omitted bare point tail."""
    return sum((q(value) ** 2 for value in couplings), Fraction(0))


def resolvent_dressed_tail_norm_sq(
    energies: Iterable[int | str | Fraction],
    couplings: Iterable[int | str | Fraction],
    shift: int | str | Fraction,
) -> Fraction:
    lam = q(shift)
    if lam <= 0:
        raise ValueError("resolvent shift must be positive")
    return sum(
        (q(g) / (q(energy) + lam)) ** 2
        for energy, g in zip(energies, couplings, strict=True)
    )


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def demo() -> dict:
    energies = ["5/4"]
    couplings = ["1"]
    charge = (0, 0)
    states, matrix = charge_block(energies, couplings, charge)
    return {
        "schema_version": "1.0",
        "arithmetic": "exact_rational",
        "mode_count": len(energies),
        "charge": list(charge),
        "basis_dimension": len(states),
        "basis": [state_label(state, len(energies)) for state in states],
        "matrix": [[qstr(value) for value in row] for row in matrix],
        "flavor_swap_intertwines": flavor_intertwines(energies, couplings, charge),
        "bare_point_tail_norm_sq_first_8": qstr(point_tail_norm_sq([1] * 8)),
        "bare_point_tail_uniformly_bounded": False,
        "resolvent_dressed_first_8_finite": True,
        "finite_matrix_is_native_continuum_spectrum": False,
        "k150_raw_bounded_block_hypothesis_certified": False,
        "next_lower_certificate": "form_level_Lehmann--Goerisch_or_penalty_form_bound",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true", required=True)
    parser.parse_args()
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
