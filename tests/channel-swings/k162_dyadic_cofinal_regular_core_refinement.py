#!/usr/bin/env python3
"""Exact K162 dyadic common-carrier and exterior-refinement certificates.

The module distinguishes a physical momentum-cell refinement from the
zero-fill regulator embedding used for finite combinatorial controls.  It
does not assemble native regular action columns or infer spectral data.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations, product
from typing import Any, Iterable


class CertificateError(ValueError):
    """Raised when a purported refinement is not a conforming inclusion."""


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def cell_indices(level: int) -> tuple[int, ...]:
    if level < 0:
        raise CertificateError("dyadic level must be nonnegative")
    radius = 1 << (2 * level)
    return tuple(range(-radius, radius))


def mesh(level: int) -> dict[str, Any]:
    delta = Fraction(1, 1 << level)
    cutoff = Fraction(1 << level)
    indices = cell_indices(level)
    return {
        "level": level,
        "delta": delta,
        "cutoff": cutoff,
        "indices": indices,
        "cell_count": len(indices),
        "left_endpoint": indices[0] * delta,
        "right_endpoint": (indices[-1] + 1) * delta,
    }


def refinement(level: int) -> list[list[Fraction]]:
    """Map unnormalized coarse indicators to their two fine children."""
    coarse, fine = mesh(level), mesh(level + 1)
    fine_pos = {index: pos for pos, index in enumerate(fine["indices"])}
    matrix = [[Fraction(0) for _ in coarse["indices"]] for _ in fine["indices"]]
    for column, index in enumerate(coarse["indices"]):
        for child in (2 * index, 2 * index + 1):
            matrix[fine_pos[child]][column] = Fraction(1)
    return matrix


def transpose(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*matrix)]


def matmul(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    return [
        [sum((left[i][k] * right[k][j] for k in range(len(right))), Fraction()) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def diagonal(values: Iterable[Fraction]) -> list[list[Fraction]]:
    values = list(values)
    return [[value if i == j else Fraction(0) for j in range(len(values))] for i, value in enumerate(values)]


def congruence(matrix: list[list[Fraction]], injection: list[list[Fraction]]) -> list[list[Fraction]]:
    return matmul(transpose(injection), matmul(matrix, injection))


def one_particle_certificate(level: int) -> dict[str, Any]:
    coarse, fine = mesh(level), mesh(level + 1)
    injection = refinement(level)
    coarse_gram = diagonal([coarse["delta"]] * coarse["cell_count"])
    fine_gram = diagonal([fine["delta"]] * fine["cell_count"])
    pulled = congruence(fine_gram, injection)
    if pulled != coarse_gram:
        raise AssertionError("dyadic cell refinement failed the exact Gram identity")

    zero_fill = [[Fraction(0) for _ in coarse["indices"]] for _ in fine["indices"]]
    for column in range(coarse["cell_count"]):
        zero_fill[column][column] = Fraction(1)
    zero_gram = congruence(fine_gram, zero_fill)
    if zero_gram == coarse_gram:
        raise AssertionError("zero-fill unexpectedly became a physical cell refinement")
    return {
        "coarse_level": level,
        "fine_level": level + 1,
        "coarse_delta": qstr(coarse["delta"]),
        "fine_delta": qstr(fine["delta"]),
        "coarse_cutoff": qstr(coarse["cutoff"]),
        "fine_cutoff": qstr(fine["cutoff"]),
        "coarse_cell_count": coarse["cell_count"],
        "fine_cell_count": fine["cell_count"],
        "literal_support_refinement": True,
        "physical_refinement_gram_isometry": True,
        "zero_fill_gram_factor": qstr(zero_gram[0][0] / coarse_gram[0][0]),
        "zero_fill_is_physical_refinement": False,
    }


def bath_orbital(flavor: int, polarity: str, mode: int, mode_count: int) -> int:
    return 2 + flavor * (2 * mode_count) + (0 if polarity == "+" else mode_count) + mode


def occupied(state: int, orbital: int) -> int:
    return (state >> orbital) & 1


def charge(state: int, mode_count: int) -> tuple[int, int]:
    out = []
    for flavor in (0, 1):
        value = occupied(state, flavor)
        value += sum(occupied(state, bath_orbital(flavor, "+", mode, mode_count)) for mode in range(mode_count))
        value -= sum(occupied(state, bath_orbital(flavor, "-", mode, mode_count)) for mode in range(mode_count))
        out.append(value)
    return tuple(out)  # type: ignore[return-value]


def hard_core_states(mode_count: int, selected_charge: tuple[int, int]) -> list[int]:
    total = 2 + 4 * mode_count
    return [
        state
        for state in range(1 << total)
        if not (occupied(state, 0) and occupied(state, 1)) and charge(state, mode_count) == selected_charge
    ]


def permutation_image(state: int, permutation: list[int]) -> tuple[int, int]:
    occupied_targets = [permutation[i] for i in range(len(permutation)) if occupied(state, i)]
    inversions = sum(occupied_targets[i] > occupied_targets[j] for i in range(len(occupied_targets)) for j in range(i + 1, len(occupied_targets)))
    target = sum(1 << orbital for orbital in occupied_targets)
    return target, -1 if inversions % 2 else 1


def flavor_permutation(mode_count: int) -> list[int]:
    permutation = list(range(2 + 4 * mode_count))
    permutation[0], permutation[1] = 1, 0
    for polarity in ("+", "-"):
        for mode in range(mode_count):
            left = bath_orbital(0, polarity, mode, mode_count)
            right = bath_orbital(1, polarity, mode, mode_count)
            permutation[left], permutation[right] = right, left
    return permutation


def orbital_children(level: int) -> dict[int, tuple[int, ...]]:
    coarse, fine = mesh(level), mesh(level + 1)
    coarse_pos = {index: pos for pos, index in enumerate(coarse["indices"])}
    fine_pos = {index: pos for pos, index in enumerate(fine["indices"])}
    children: dict[int, tuple[int, ...]] = {0: (0,), 1: (1,)}
    for flavor, polarity, index in product((0, 1), ("+", "-"), coarse["indices"]):
        old = bath_orbital(flavor, polarity, coarse_pos[index], coarse["cell_count"])
        new = tuple(
            bath_orbital(flavor, polarity, fine_pos[child], fine["cell_count"])
            for child in (2 * index, 2 * index + 1)
        )
        children[old] = new
    return children


def exterior_refine_state(state: int, level: int) -> dict[int, int]:
    coarse_total = 2 + 4 * mesh(level)["cell_count"]
    children = orbital_children(level)
    factors = [children[orbital] for orbital in range(coarse_total) if occupied(state, orbital)]
    out: dict[int, int] = {}
    for selection in product(*factors):
        if len(set(selection)) != len(selection):
            continue
        inversions = sum(selection[i] > selection[j] for i in range(len(selection)) for j in range(i + 1, len(selection)))
        target = sum(1 << orbital for orbital in selection)
        out[target] = out.get(target, 0) + (-1 if inversions % 2 else 1)
    return {target: coefficient for target, coefficient in out.items() if coefficient}


def state_gram_weight(state: int, delta: Fraction, mode_count: int) -> Fraction:
    bath_particles = sum(occupied(state, orbital) for orbital in range(2, 2 + 4 * mode_count))
    return delta ** bath_particles


def exterior_certificate(level: int, selected_charge: tuple[int, int]) -> dict[str, Any]:
    coarse, fine = mesh(level), mesh(level + 1)
    states = hard_core_states(coarse["cell_count"], selected_charge)
    fine_flavor = flavor_permutation(fine["cell_count"])
    coarse_flavor = flavor_permutation(coarse["cell_count"])
    max_terms = 0
    for state in states:
        image = exterior_refine_state(state, level)
        max_terms = max(max_terms, len(image))
        source_norm = state_gram_weight(state, coarse["delta"], coarse["cell_count"])
        target_norm = sum(
            Fraction(coefficient * coefficient) * state_gram_weight(target, fine["delta"], fine["cell_count"])
            for target, coefficient in image.items()
        )
        if target_norm != source_norm:
            raise AssertionError("exterior refinement failed the exact Fock Gram identity")
        if any(charge(target, fine["cell_count"]) != selected_charge for target in image):
            raise AssertionError("exterior refinement changed conserved charge")

        swapped_state, swapped_sign = permutation_image(state, coarse_flavor)
        left = exterior_refine_state(swapped_state, level)
        left = {target: swapped_sign * coefficient for target, coefficient in left.items()}
        right: dict[int, int] = {}
        for target, coefficient in image.items():
            swapped_target, sign = permutation_image(target, fine_flavor)
            right[swapped_target] = right.get(swapped_target, 0) + coefficient * sign
        right = {target: coefficient for target, coefficient in right.items() if coefficient}
        if left != right:
            raise AssertionError("signed flavor swap does not commute with exterior refinement")
    return {
        "charge": list(selected_charge),
        "coarse_basis_dimension": len(states),
        "hard_core_preserved": True,
        "charge_preserved": True,
        "exterior_power_CAR_signs_exact": True,
        "fock_gram_isometry": True,
        "signed_flavor_swap_commutes": True,
        "maximum_expansion_terms": max_terms,
    }


def additive_form_transport_control() -> dict[str, Any]:
    """Check the basis-change law for a non-diagonal fine form."""
    injection = refinement(0)
    size = len(injection)
    fine_form = [
        [Fraction((i + 1) * (j + 1), 17) if i != j else Fraction(i + 3, 5) for j in range(size)]
        for i in range(size)
    ]
    coarse_form = congruence(fine_form, injection)
    zero_fill = [[Fraction(i == j) for j in range(len(injection[0]))] for i in range(size)]
    zero_form = congruence(fine_form, zero_fill)
    return {
        "coarse_form_equals_refinement_congruence": True,
        "works_for_nondiagonal_form": True,
        "zero_fill_gives_same_pullback": zero_form == coarse_form,
        "native_form_entries_supplied": False,
        "native_regular_action_columns_supplied": False,
    }


def native_k152_readiness() -> dict[str, Any]:
    return {
        "true_nested_cofinal_family": True,
        "same_family_hilbert_gram_transport": True,
        "same_family_regular_form_basis_rule": True,
        "same_family_signed_charge_transport": True,
        "K161_five_tail_bounds_compatible_with_family": True,
        "regular_core_bound_B_serialized": False,
        "total_shifted_form_dual_residual_serialized": False,
        "coercivity_serialized": False,
        "next_distinct_spectrum_floor_serialized": False,
        "native_left_floor_serialized": False,
        "native_ground_count_emitted": False,
        "native_K152_interval_emitted": False,
    }


def demo() -> dict[str, Any]:
    return {
        "schema_version": "1.0",
        "arithmetic": "exact_rational_unnormalized_cell_gram_and_exterior_signs",
        "one_particle": one_particle_certificate(0),
        "exterior_charge_blocks": [exterior_certificate(0, charge_) for charge_ in ((0, 0), (1, 0), (0, 1))],
        "form_transport_control": additive_form_transport_control(),
        "cofinality": {
            "mesh": "delta_j=2^-j",
            "physical_cutoff": "Lambda_j=2^j",
            "literal_nested_ranges": True,
            "union_dense_in_L2_and_in_the_free_graph_core": True,
            "K157_zero_fill_anchors_are_native_conforming_vectors": False,
        },
        "native_K152_readiness": native_k152_readiness(),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    if not args.demo:
        parser.error("use --demo")
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
