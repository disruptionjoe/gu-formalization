#!/usr/bin/env python3
"""Exact shiab/B5 observer-subgroup symbol matrix for the frozen independent ledger.

This computes

    m_ij = dim Hom_H(V_14 tensor W_i, W_j)

for every explicitly labeled irreducible slot in

    3 E_+ + 3 E_- + X,

where H_C = Spin(4,C) x Spin(10,C).  The three provenance copies are never
identified.  X is expanded into its eight irreducible summands.  This is an
algebraic principal-symbol census, not a lower-order operator, BV cohomology,
positive-Hilbert quotient, or native source-action claim.

The D5 calculation uses exact Racah-Speiser decomposition for tensoring by the
minuscule vector 10.  The Spin(4) calculation uses exact SU(2) Clebsch-Gordan
rules.  No numerical library or target value is used.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from math import prod


# D5 weights use doubled orthonormal coordinates.
N = 5
RHO2 = tuple(2 * (N - 1 - i) for i in range(N))
POSITIVE_ROOTS = []
for i, j in combinations(range(N), 2):
    minus = [0] * N
    minus[i], minus[j] = 1, -1
    plus = [0] * N
    plus[i], plus[j] = 1, 1
    POSITIVE_ROOTS.extend((tuple(minus), tuple(plus)))

F_PLUS = (1, 1, 1, 1, 1)
F_MINUS = (1, 1, 1, 1, -1)
T_PLUS = (3, 1, 1, 1, 1)   # omega_1 + omega_5, dimension 144
T_MINUS = (3, 1, 1, 1, -1) # omega_1 + omega_4, dimension 144bar

VECTOR_WEIGHTS = []
for axis in range(N):
    for sign in (-2, 2):
        weight = [0] * N
        weight[axis] = sign
        VECTOR_WEIGHTS.append(tuple(weight))


def dot(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return sum(a * b for a, b in zip(left, right))


def reflect_to_dominant(weight: tuple[int, ...]) -> tuple[tuple[int, ...] | None, int]:
    """Return the regular dominant Weyl translate and its determinant."""
    magnitudes = [abs(value) for value in weight]
    if 0 in magnitudes or len(set(magnitudes)) != N:
        return None, 0

    order = sorted(range(N), key=lambda index: -magnitudes[index])
    dominant = [magnitudes[index] for index in order]
    if sum(value < 0 for value in weight) % 2:
        dominant[-1] *= -1

    inversions = sum(
        order[i] > order[j] for i in range(N) for j in range(i + 1, N)
    )
    permutation_sign = -1 if inversions % 2 else 1
    sign_product = 1
    for position, source in enumerate(order):
        sign_product *= (
            1 if (dominant[position] > 0) == (weight[source] > 0) else -1
        )
    return tuple(dominant), permutation_sign * sign_product


def vector_tensor_decomposition(
    highest_weight: tuple[int, ...],
) -> dict[tuple[int, ...], int]:
    """Decompose the D5 irrep of highest_weight tensor the vector 10."""
    result: dict[tuple[int, ...], int] = {}
    for vector_weight in VECTOR_WEIGHTS:
        shifted = tuple(
            highest_weight[i] + RHO2[i] + vector_weight[i] for i in range(N)
        )
        dominant, sign = reflect_to_dominant(shifted)
        if dominant is None:
            continue
        output = tuple(dominant[i] - RHO2[i] for i in range(N))
        result[output] = result.get(output, 0) + sign
    return {weight: multiplicity for weight, multiplicity in result.items() if multiplicity}


def weyl_dimension(highest_weight: tuple[int, ...]) -> int:
    shifted = tuple(highest_weight[i] + RHO2[i] for i in range(N))
    numerator = prod(dot(shifted, root) for root in POSITIVE_ROOTS)
    denominator = prod(dot(RHO2, root) for root in POSITIVE_ROOTS)
    assert numerator % denominator == 0
    return numerator // denominator


def su2_vector_targets(dimension: int) -> tuple[int, ...]:
    """Irrep dimensions in 2 tensor dimension."""
    return (dimension + 1,) if dimension == 1 else (dimension + 1, dimension - 1)


@dataclass(frozen=True)
class HType:
    name: str
    left_dim: int
    right_dim: int
    d5_weight: tuple[int, ...]
    mirror: str

    @property
    def dimension(self) -> int:
        return self.left_dim * self.right_dim * weyl_dimension(self.d5_weight)


TYPES = {
    # The four irreducible pieces of E_+ and E_-.
    "Lp": HType("Lp", 2, 1, F_PLUS, "Lm"),
    "Rm": HType("Rm", 1, 2, F_MINUS, "Rp"),
    "Lm": HType("Lm", 2, 1, F_MINUS, "Lp"),
    "Rp": HType("Rp", 1, 2, F_PLUS, "Rm"),
    # X from the two chiral Rarita-Schwinger modules.
    "X32p": HType("X32p", 3, 2, F_PLUS, "X32m"),
    "X23m": HType("X23m", 2, 3, F_MINUS, "X23p"),
    "X2Tp": HType("X2Tp", 2, 1, T_PLUS, "X2Tm"),
    "X1Tm": HType("X1Tm", 1, 2, T_MINUS, "X1Tp"),
    "X32m": HType("X32m", 3, 2, F_MINUS, "X32p"),
    "X23p": HType("X23p", 2, 3, F_PLUS, "X23m"),
    "X2Tm": HType("X2Tm", 2, 1, T_MINUS, "X2Tp"),
    "X1Tp": HType("X1Tp", 1, 2, T_PLUS, "X1Tm"),
}


@dataclass(frozen=True)
class Slot:
    name: str
    h_type: str
    mirror: str

    @property
    def dimension(self) -> int:
        return TYPES[self.h_type].dimension


SLOTS: list[Slot] = []
for provenance in ("S", "imGamma", "kerGamma"):
    SLOTS.extend(
        [
            Slot(f"{provenance}:E+:L16+", "Lp", f"{provenance}:E-:L16-"),
            Slot(f"{provenance}:E+:R16-", "Rm", f"{provenance}:E-:R16+"),
            Slot(f"{provenance}:E-:L16-", "Lm", f"{provenance}:E+:L16+"),
            Slot(f"{provenance}:E-:R16+", "Rp", f"{provenance}:E+:R16-"),
        ]
    )

for type_name in (
    "X32p",
    "X23m",
    "X2Tp",
    "X1Tm",
    "X32m",
    "X23p",
    "X2Tm",
    "X1Tp",
):
    mirror_type = TYPES[type_name].mirror
    SLOTS.append(Slot(f"X:{type_name}", type_name, f"X:{mirror_type}"))

SLOT_BY_NAME = {slot.name: slot for slot in SLOTS}


def symbol_multiplicity(source: HType, target: HType) -> int:
    """Multiplicity from V_14 = (2,2,1) + (1,1,10)."""
    base_part = int(
        source.d5_weight == target.d5_weight
        and target.left_dim in su2_vector_targets(source.left_dim)
        and target.right_dim in su2_vector_targets(source.right_dim)
    )
    fiber_part = int(
        source.left_dim == target.left_dim
        and source.right_dim == target.right_dim
    ) * vector_tensor_decomposition(source.d5_weight).get(target.d5_weight, 0)
    return base_part + fiber_part


def check(label: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(label)
    print(f"PASS: {label}")


def main() -> None:
    print("B5 observer-subgroup symbol multiplicity certificate")
    print("construction: program-native H_C observer branching; complexified algebraic grade")
    print("not claimed: native differential, lower-order terms, domain, BV cohomology, positivity")

    # Exact D5 anchors and dimension closures.
    d5_decompositions = {
        "10x16+": vector_tensor_decomposition(F_PLUS),
        "10x16-": vector_tensor_decomposition(F_MINUS),
        "10x144+": vector_tensor_decomposition(T_PLUS),
        "10x144-": vector_tensor_decomposition(T_MINUS),
    }
    check("dim Spin(10) 16+ = dim 16- = 16", weyl_dimension(F_PLUS) == weyl_dimension(F_MINUS) == 16)
    check("dim Spin(10) 144+ = dim 144- = 144", weyl_dimension(T_PLUS) == weyl_dimension(T_MINUS) == 144)
    check(
        "10 tensor 16+ = 144+ + 16- exactly",
        d5_decompositions["10x16+"] == {T_PLUS: 1, F_MINUS: 1},
    )
    check(
        "10 tensor 16- = 144- + 16+ exactly",
        d5_decompositions["10x16-"] == {T_MINUS: 1, F_PLUS: 1},
    )
    for name, source in (("10x144+", T_PLUS), ("10x144-", T_MINUS)):
        decomposition = d5_decompositions[name]
        check(
            f"{name} exact dimension closure",
            sum(multiplicity * weyl_dimension(weight) for weight, multiplicity in decomposition.items())
            == 10 * weyl_dimension(source),
        )

    # Carrier ledger controls.
    x_slots = [slot for slot in SLOTS if slot.name.startswith("X:")]
    provenance_slots = [slot for slot in SLOTS if not slot.name.startswith("X:")]
    check("all 20 labeled irreducible slots are explicit", len(SLOTS) == 20)
    check("three provenance copies remain expanded", len(provenance_slots) == 12)
    check("X has eight irreducible slots", len(x_slots) == 8)
    check("dim X = 1536", sum(slot.dimension for slot in x_slots) == 1536)
    check(
        "full S + imGamma + kerGamma ledger dimension = 1920",
        sum(slot.dimension for slot in SLOTS) == 1920,
    )
    check(
        "omitting X fails the frozen ledger",
        sum(slot.dimension for slot in provenance_slots) == 384,
    )
    check(
        "collapsing provenance copies fails the frozen ledger",
        sum(slot.dimension for slot in provenance_slots[:4]) + 1536 == 1664,
    )
    check("beta is not mistyped as a carrier/principal-symbol slot", all("beta" not in slot.name for slot in SLOTS))

    # Full matrix, with all provenance coefficient cells expanded.
    matrix: dict[tuple[str, str], int] = {}
    for source_slot in SLOTS:
        for target_slot in SLOTS:
            matrix[(source_slot.name, target_slot.name)] = symbol_multiplicity(
                TYPES[source_slot.h_type], TYPES[target_slot.h_type]
            )

    check("every matrix entry is 0 or 1", set(matrix.values()) <= {0, 1})
    check(
        "V self-duality makes the labeled matrix symmetric",
        all(matrix[(left.name, right.name)] == matrix[(right.name, left.name)] for left in SLOTS for right in SLOTS),
    )
    check(
        "mirror exchange preserves every matrix entry",
        all(
            matrix[(left.name, right.name)]
            == matrix[(left.mirror, right.mirror)]
            for left in SLOTS
            for right in SLOTS
        ),
    )

    basis_cells = [
        (source, target, basis)
        for (source, target), multiplicity in matrix.items()
        for basis in range(multiplicity)
    ]
    unseen = set(basis_cells)
    mirror_orbits: list[tuple[tuple[str, str, int], ...]] = []
    while unseen:
        cell = min(unseen)
        source, target, basis = cell
        mirror_cell = (
            SLOT_BY_NAME[source].mirror,
            SLOT_BY_NAME[target].mirror,
            basis,
        )
        orbit = tuple(sorted({cell, mirror_cell}))
        mirror_orbits.append(orbit)
        unseen.difference_update(orbit)

    check("mirror action has no fixed labeled basis cell", all(len(orbit) == 2 for orbit in mirror_orbits))
    check("mirror orbits exhaust the full basis", 2 * len(mirror_orbits) == len(basis_cells))

    # Reduced type matrix is an independently inspectable digest of the full
    # provenance-expanded matrix.
    type_names = list(TYPES)
    type_matrix = {
        (source, target): symbol_multiplicity(TYPES[source], TYPES[target])
        for source in type_names
        for target in type_names
    }
    check(
        "each labeled cell is the declared type-cell pullback",
        all(
            matrix[(left.name, right.name)]
            == type_matrix[(left.h_type, right.h_type)]
            for left in SLOTS
            for right in SLOTS
        ),
    )

    print("\nType order:")
    print("  " + " ".join(f"{name:>5}" for name in type_names))
    print("\n12 x 12 irreducible-type multiplicity matrix:")
    print("      " + " ".join(f"{name:>5}" for name in type_names))
    for source in type_names:
        row = " ".join(f"{type_matrix[(source, target)]:5d}" for target in type_names)
        print(f"{source:>5} {row}")

    print("\nFull labeled-ledger summary:")
    print(f"  slots: {len(SLOTS)}")
    print(f"  ordered basis cells: {len(basis_cells)}")
    print(f"  mirror-paired ordered-cell orbits: {len(mirror_orbits)}")
    print(f"  unordered adjoint edge count: {len(basis_cells) // 2}")
    print("\nNonzero labeled ordered cells:")
    for source, target, _basis in basis_cells:
        print(f"  {source} -> {target}")

    print("\nRESULT: B5-COMPLEX-OBSERVER-SYMBOL-MATRIX-COMPLETE")
    print("RESIDUAL: native real/Krein adjoint phases and operator-domain data are not frozen")


if __name__ == "__main__":
    main()
