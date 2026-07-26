#!/usr/bin/env python3
"""Target-blind provenance-multiplicity stress test for the B5 symbol class.

This extends the frozen complexified observer-symbol census without choosing a
native phase, differential, Green form, domain, or physical quotient.  It asks
only whether the algebraic principal-symbol class itself singles out the three
expanded provenance copies.  It does not: the same declared construction is
well-defined for 1, 2, 3, and 4 copies, and its coefficient census varies by a
uniform quadratic law.
"""

from __future__ import annotations

import shiab_b5_observer_symbol_multiplicity_matrix as matrix


def check(label: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(label)
    print(f"PASS: {label}")


def slots_for_provenance_multiplicity(count: int):
    """Rebuild the frozen ledger with `count` labeled E+/E- provenance copies."""
    if count < 1:
        raise ValueError("a carrier must retain at least one provenance copy")
    slots = []
    for copy in range(count):
        for template in matrix.SLOTS[:4]:
            slots.append((f"P{copy}:{template.name}", template.h_type))
    slots.extend((slot.name, slot.h_type) for slot in matrix.SLOTS[12:])
    return slots


def ordered_symbol_cell_count(count: int) -> int:
    slots = slots_for_provenance_multiplicity(count)
    return sum(
        matrix.symbol_multiplicity(matrix.TYPES[source], matrix.TYPES[target])
        for _source_name, source in slots
        for _target_name, target in slots
    )


def main() -> None:
    print("B5 target-blind provenance-multiplicity stress certificate")
    print("construction: frozen complexified observer-symbol class")
    print("not claimed: native selector, source action, physical chirality, or count")

    counts = {copies: ordered_symbol_cell_count(copies) for copies in range(1, 5)}
    check("one through four provenance-copy ledgers remain explicitly typed", counts.keys() == {1, 2, 3, 4})
    check("the frozen three-copy ledger reproduces 136 ordered cells", counts[3] == 136)
    check("the target-blind census is 40, 80, 136, 208", counts == {1: 40, 2: 80, 3: 136, 4: 208})
    check(
        "the exact coefficient law is 8 n^2 + 16 n + 16",
        all(total == 8 * copies * copies + 16 * copies + 16 for copies, total in counts.items()),
    )
    check(
        "no unique algebraic event occurs at three copies",
        [counts[n + 1] - counts[n] for n in range(1, 4)] == [40, 56, 72],
    )
    check(
        "changing provenance multiplicity changes the census rather than being silently quotiented",
        len(set(counts.values())) == 4,
    )


if __name__ == "__main__":
    main()
