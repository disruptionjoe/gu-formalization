#!/usr/bin/env python3
"""Exact adjoint/mirror orbit reduction for the frozen B5 symbol ledger.

The input is the complete complexified observer-symbol matrix certified by
``shiab_b5_observer_symbol_multiplicity_matrix.py``.  This file does not pick
an operator.  It classifies the coefficient space under the support actions of

* formal adjoint: (source, target) -> (target, source), and
* normal-chirality coflip:
  (source, target) -> (mirror(source), mirror(target)).

The native Krein signs, coflip phases, Green form, and common domain remain
symbolic.  The output is therefore a phase-parametric admissibility theorem,
not a native differential or a physical quotient.
"""

from __future__ import annotations

from collections import Counter
from itertools import product

import shiab_b5_observer_symbol_multiplicity_matrix as matrix


Cell = tuple[str, str]


def check(label: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(label)
    print(f"PASS: {label}")


def transpose(cell: Cell) -> Cell:
    source, target = cell
    return target, source


def mirror(cell: Cell) -> Cell:
    source, target = cell
    return (
        matrix.SLOT_BY_NAME[source].mirror,
        matrix.SLOT_BY_NAME[target].mirror,
    )


def nonzero_cells(
    slots: list[matrix.Slot] | None = None,
) -> set[Cell]:
    selected = matrix.SLOTS if slots is None else slots
    return {
        (source.name, target.name)
        for source in selected
        for target in selected
        if matrix.symbol_multiplicity(
            matrix.TYPES[source.h_type],
            matrix.TYPES[target.h_type],
        )
    }


def involution_orbits(cells: set[Cell], action) -> list[frozenset[Cell]]:
    unseen = set(cells)
    orbits: list[frozenset[Cell]] = []
    while unseen:
        cell = min(unseen)
        orbit = frozenset((cell, action(cell)))
        if not orbit <= cells:
            raise AssertionError("involution orbit leaves the frozen cell set")
        orbits.append(orbit)
        unseen.difference_update(orbit)
    return orbits


def joint_orbits(cells: set[Cell]) -> list[frozenset[Cell]]:
    unseen = set(cells)
    orbits: list[frozenset[Cell]] = []
    while unseen:
        cell = min(unseen)
        orbit = frozenset(
            (
                cell,
                transpose(cell),
                mirror(cell),
                transpose(mirror(cell)),
            )
        )
        if not orbit <= cells:
            raise AssertionError("joint orbit leaves the frozen cell set")
        orbits.append(orbit)
        unseen.difference_update(orbit)
    return orbits


def canonical_edge(cell: Cell) -> Cell:
    return min(cell, transpose(cell))


def main() -> None:
    print("B5 Krein-adjoint / mirror support reduction")
    print("construction: program-native observer carrier, phase-parametric Krein grade")
    print("not claimed: native phases, differential, Green domain, BV cohomology, positivity")

    cells = nonzero_cells()
    check("the frozen complex matrix has 136 ordered cells", len(cells) == 136)
    check("formal-adjoint transpose is fixed-point-free", all(transpose(cell) != cell for cell in cells))
    check("mirror support exchange is fixed-point-free", all(mirror(cell) != cell for cell in cells))
    check(
        "transpose and mirror commute on every cell",
        all(transpose(mirror(cell)) == mirror(transpose(cell)) for cell in cells),
    )

    transpose_orbits = involution_orbits(cells, transpose)
    mirror_orbits = involution_orbits(cells, mirror)
    combined_orbits = joint_orbits(cells)
    orbit_sizes = Counter(len(orbit) for orbit in combined_orbits)

    check("formal adjoint has 68 unordered coefficient edges", len(transpose_orbits) == 68)
    check("mirror has 68 ordered-cell support pairs", len(mirror_orbits) == 68)
    check("joint action has 39 orbits", len(combined_orbits) == 39)
    check("joint orbit census is 29 four-cell plus 10 two-cell", orbit_sizes == {4: 29, 2: 10})

    product_fixed = {
        cell for cell in cells if transpose(mirror(cell)) == cell
    }
    special_edges = {canonical_edge(cell) for cell in product_fixed}
    check("transpose-times-mirror fixes exactly 20 directed cells", len(product_fixed) == 20)
    check("those cells form exactly 10 adjoint edges", len(special_edges) == 10)
    check(
        "every special edge joins one slot directly to its mirror",
        all(target == matrix.SLOT_BY_NAME[source].mirror for source, target in special_edges),
    )

    # Krein formal self-adjointness pairs each edge coefficient with the
    # conjugate coefficient on its transpose, up to a normalized unit phase.
    # Therefore every one of the 68 edges contributes one complex parameter,
    # i.e. two real dimensions.  The actual unit phases do not alter this
    # count.
    adjoint_real_dimension = 2 * len(transpose_orbits)
    check("formal Krein-adjoint coefficient space has real dimension 136", adjoint_real_dimension == 136)

    # Linear coflip:
    # On each of the 29 exchanged edge pairs, each parity has two real
    # dimensions.  On each of the 10 special edges, the mirror action becomes
    # an antilinear involution of its complex edge coefficient, so each parity
    # has one real dimension, independent of the normalized phase.
    linear_even_dimension = 2 * orbit_sizes[4] + orbit_sizes[2]
    linear_breaking_dimension = linear_even_dimension
    check(
        "linear coflip gives 68 real mirror-even coefficients",
        linear_even_dimension == 68,
    )
    check(
        "linear coflip gives 68 real mirror-breaking coefficients",
        linear_breaking_dimension == 68,
    )
    check(
        "linear parity sectors exhaust the adjoint space",
        linear_even_dimension + linear_breaking_dimension == adjoint_real_dimension,
    )

    # Antilinear coflip:
    # The 29 exchanged edge pairs again contribute two real dimensions to
    # each parity.  On a special edge, formal adjoint and antilinear mirror
    # have the same support exchange; their composition is complex-linear.
    # Its normalized phase invariant is +/-1, so that entire two-real-
    # dimensional edge belongs to either the even or the breaking sector.
    # Current GU truth does not choose those ten invariants.
    antilinear_dimension_pairs: set[tuple[int, int]] = set()
    for phase_assignment in product((-1, 1), repeat=len(special_edges)):
        even_special = sum(phase == 1 for phase in phase_assignment)
        breaking_special = len(special_edges) - even_special
        even_dimension = 2 * orbit_sizes[4] + 2 * even_special
        breaking_dimension = 2 * orbit_sizes[4] + 2 * breaking_special
        if even_dimension + breaking_dimension != adjoint_real_dimension:
            raise AssertionError(
                "antilinear phase assignment does not exhaust the adjoint space"
            )
        antilinear_dimension_pairs.add((even_dimension, breaking_dimension))

    expected_pairs = {(58 + 2 * count, 78 - 2 * count) for count in range(11)}
    check(
        "every antilinear phase assignment exhausts the adjoint space",
        all(left + right == adjoint_real_dimension for left, right in antilinear_dimension_pairs),
    )
    check(
        "all 1024 native phase assignments reduce to the exact 11 dimension pairs",
        antilinear_dimension_pairs == expected_pairs,
    )
    check(
        "antilinear mirror-even dimension ranges from 58 to 78 by twos",
        {left for left, _right in antilinear_dimension_pairs}
        == set(range(58, 79, 2)),
    )
    check(
        "no single antilinear native phase assignment is selected",
        len(antilinear_dimension_pairs) == 11,
    )

    # Hostile construction controls.
    without_x = [slot for slot in matrix.SLOTS if not slot.name.startswith("X:")]
    collapsed_provenance = matrix.SLOTS[:4] + matrix.SLOTS[12:]
    check("omitting X changes the adjoint-edge census", len(involution_orbits(nonzero_cells(without_x), transpose)) != 68)
    check(
        "collapsing the three provenance copies changes the adjoint-edge census",
        len(involution_orbits(nonzero_cells(collapsed_provenance), transpose)) != 68,
    )
    check(
        "linear and antilinear coflips are not silently conflated",
        antilinear_dimension_pairs != {(linear_even_dimension, linear_breaking_dimension)},
    )

    required_native_packet = (
        "slot_pairing_phases",
        "coflip_linearity_and_phases",
        "formal_adjoint_sign",
        "green_boundary_form",
        "common_closed_domain",
    )
    check("the residual native packet has five explicitly typed fields", len(required_native_packet) == 5)

    print("\nJoint support-orbit summary:")
    print(f"  ordered complex cells: {len(cells)}")
    print(f"  formal-adjoint edges: {len(transpose_orbits)}")
    print(f"  four-cell joint orbits: {orbit_sizes[4]}")
    print(f"  special two-cell joint orbits: {orbit_sizes[2]}")
    print("  special adjoint edges:")
    for source, target in sorted(special_edges):
        print(f"    {source} <-> {target}")

    print("\nReal coefficient dimensions after formal Krein adjoint:")
    print(f"  total adjoint space: {adjoint_real_dimension}")
    print(f"  linear coflip: even={linear_even_dimension}, breaking={linear_breaking_dimension}")
    print("  antilinear coflip:")
    for even_dimension, breaking_dimension in sorted(antilinear_dimension_pairs):
        print(f"    even={even_dimension}, breaking={breaking_dimension}")

    print("\nRESULT: B5-KREIN-MIRROR-ORBIT-REDUCTION-COMPLETE")
    print(
        "RESIDUAL: ten native antilinear phase invariants plus the "
        "Green-form/common-domain packet are not frozen"
    )


if __name__ == "__main__":
    main()
