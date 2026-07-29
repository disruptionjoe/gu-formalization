#!/usr/bin/env python3
r"""Can the written W131 differential normalize transport on all 20 B5 slots?

Layer 0 is load-bearing.  The two objects are:

* W131:
      D_RS = Pi_RS c(nabla) Pi_RS + m^2 Pi_RS
  on ``ker Gamma`` only.
* independent B5:
  a first-order middle complex on the complete observer ledger
      S + im Gamma + ker Gamma
  whose 20 irreducible slots include all eight summands of X.

They share an RS principal-symbol block, but they are not the same operator.
This probe gives W131 the strongest possible advantage: every observer-natural
principal-symbol cell whose source and target both lie in ``ker Gamma`` is
treated as nonzero.  That is an optimistic envelope, not a claim about the
actual coefficient table.  Any exact W131 symbol can impose no more
slot-diagonal phase relations than this envelope.

The probe then:

1. computes the exact full and W131-envelope support graphs;
2. enumerates all mirror-pair sign returns and asks which commute with each
   graph;
3. plants a noncentral return that intertwines even the optimistic W131
   envelope;
4. verifies that a coefficient-complete full B5 graph would force centrality;
   and
5. computes the minimum number of formal-adjoint/mirror support orbits that
   must be added to the W131 envelope merely to connect all 20 slots.

This is a transport-normalization obstruction for the written suboperator, not
a no-go for an explicitly extended B5 differential.  It uses exact finite
graph arithmetic, performs no fit, writes nothing, and needs no network.
"""

from __future__ import annotations

from itertools import combinations, product
import os
import sys


HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))

import shiab_b5_krein_mirror_orbit_reduction as reduction  # noqa: E402
import shiab_b5_observer_symbol_multiplicity_matrix as matrix  # noqa: E402


FAILURES: list[str] = []


def check(label: str, condition: bool, detail: str = "") -> None:
    status = "PASS" if condition else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"{status}: {label}{suffix}")
    if not condition:
        FAILURES.append(label)


def connected_components(
    slot_names: set[str], cells: set[tuple[str, str]]
) -> list[frozenset[str]]:
    adjacency = {name: set() for name in slot_names}
    for source, target in cells:
        if source in adjacency and target in adjacency:
            adjacency[source].add(target)
            adjacency[target].add(source)

    unseen = set(slot_names)
    components: list[frozenset[str]] = []
    while unseen:
        seed = min(unseen)
        stack = [seed]
        component = {seed}
        unseen.remove(seed)
        while stack:
            current = stack.pop()
            for neighbour in adjacency[current]:
                if neighbour in unseen:
                    unseen.remove(neighbour)
                    component.add(neighbour)
                    stack.append(neighbour)
        components.append(frozenset(component))
    return sorted(components, key=lambda component: (len(component), sorted(component)))


def is_connected(slot_names: set[str], cells: set[tuple[str, str]]) -> bool:
    return len(connected_components(slot_names, cells)) == 1


def mirror_pairs() -> list[tuple[str, str]]:
    return sorted(
        {
            tuple(sorted((slot.name, slot.mirror)))
            for slot in matrix.SLOTS
        }
    )


def phase_return(
    signs: tuple[int, ...], pairs: list[tuple[str, str]]
) -> dict[str, int]:
    phases: dict[str, int] = {}
    for sign, pair in zip(signs, pairs):
        for slot_name in pair:
            phases[slot_name] = sign
    return phases


def intertwines(
    phases: dict[str, int], cells: set[tuple[str, str]]
) -> bool:
    """A slot-diagonal return commutes with every declared nonzero block."""
    return all(phases[source] == phases[target] for source, target in cells)


def is_central(phases: dict[str, int]) -> bool:
    return len(set(phases.values())) == 1


print("=" * 94)
print("L0. W131 projected RS operator versus the complete B5 middle-complex ledger")
print("=" * 94)

all_slots = {slot.name for slot in matrix.SLOTS}
w131_slots = {
    slot.name
    for slot in matrix.SLOTS
    if slot.name.startswith("kerGamma:") or slot.name.startswith("X:")
}
omitted_slots = all_slots - w131_slots

full_cells = reduction.nonzero_cells()
w131_envelope_cells = {
    cell
    for cell in full_cells
    if cell[0] in w131_slots and cell[1] in w131_slots
}

full_dimension = sum(slot.dimension for slot in matrix.SLOTS)
w131_dimension = sum(
    slot.dimension for slot in matrix.SLOTS if slot.name in w131_slots
)

check(
    "the complete B5 ledger is S + imGamma + kerGamma: 20 slots, dimension 1920",
    len(all_slots) == 20 and full_dimension == 1920,
)
check(
    "W131 acts on kerGamma only: 12 slots, dimension 1664",
    len(w131_slots) == 12 and w131_dimension == 1664,
)
check(
    "the eight absent slots are exactly the S and imGamma provenance sectors",
    len(omitted_slots) == 8
    and all(
        name.startswith("S:") or name.startswith("imGamma:")
        for name in omitted_slots
    ),
)
check(
    "Layer-0 verdict: W131 is a proper suboperator, not the complete B5 differential",
    w131_slots < all_slots,
    f"missing dimension {full_dimension - w131_dimension}",
)


print("\n" + "=" * 94)
print("P1. Optimistic W131 envelope: strongest phase constraints it could impose")
print("=" * 94)

w131_components = connected_components(w131_slots, w131_envelope_cells)
all_components_under_w131 = connected_components(all_slots, w131_envelope_cells)

check(
    "the full observer-symbol class has 136 ordered cells",
    len(full_cells) == 136,
)
check(
    "the optimistic W131-only envelope has 40 ordered cells",
    len(w131_envelope_cells) == 40,
)
check(
    "the optimistic W131 envelope connects all 12 of its own slots",
    len(w131_components) == 1 and len(w131_components[0]) == 12,
)
check(
    "on the full ledger it leaves the eight omitted slots as isolated components",
    sorted(len(component) for component in all_components_under_w131)
    == [1] * 8 + [12],
)

pairs = mirror_pairs()
all_returns = [
    phase_return(signs, pairs)
    for signs in product((-1, 1), repeat=len(pairs))
]
w131_admissible = [
    phases
    for phases in all_returns
    if intertwines(phases, w131_envelope_cells)
]
full_admissible = [
    phases
    for phases in all_returns
    if intertwines(phases, full_cells)
]

# Quotient by the common global sign.  Each class has exactly two members.
w131_relative_classes = len(w131_admissible) // 2
full_relative_classes = len(full_admissible) // 2

check(
    "the mirror ledger has ten sign pairs before differential constraints",
    len(pairs) == 10 and len(all_returns) == 2**10,
)
check(
    "even the optimistic W131 envelope leaves 2^4 relative sign classes",
    w131_relative_classes == 2**4,
    (
        f"{len(w131_admissible)} absolute assignments, "
        f"{w131_relative_classes} modulo global sign"
    ),
)
check(
    "a coefficient-complete full B5 graph would force one central class",
    full_relative_classes == 1
    and all(is_central(phases) for phases in full_admissible),
    f"{len(full_admissible)} absolute assignments",
)

# Plant a return that is uniform on the complete W131 carrier but flips one
# entirely absent mirror pair.  It therefore commutes with every possible
# W131-envelope block while remaining visibly noncentral on the B5 ledger.
planted_noncentral = {name: 1 for name in all_slots}
absent_pair = next(
    pair for pair in pairs if set(pair) <= omitted_slots
)
for slot_name in absent_pair:
    planted_noncentral[slot_name] = -1

check(
    "planted noncentral return intertwines even the maximal W131 envelope",
    intertwines(planted_noncentral, w131_envelope_cells),
)
check(
    "strict centrality catches the planted return",
    not is_central(planted_noncentral),
    f"flipped absent pair {absent_pair}",
)
check(
    "the complete graph rejects the same planted return",
    not intertwines(planted_noncentral, full_cells),
)


print("\n" + "=" * 94)
print("P2. Smallest support packet that could make full normalization decidable")
print("=" * 94)

joint_orbits = reduction.joint_orbits(full_cells)
bridge_candidates = [
    orbit for orbit in joint_orbits if not set(orbit) <= w131_envelope_cells
]

minimal_bridge_orbits: tuple[frozenset[tuple[str, str]], ...] | None = None
for orbit_count in range(1, len(pairs) + 1):
    for candidate_tuple in combinations(bridge_candidates, orbit_count):
        augmented_cells = set(w131_envelope_cells)
        for orbit in candidate_tuple:
            augmented_cells.update(orbit)
        if is_connected(all_slots, augmented_cells):
            minimal_bridge_orbits = candidate_tuple
            break
    if minimal_bridge_orbits is not None:
        break

check(
    "the full 20-slot support graph is connected (positive-power control)",
    is_connected(all_slots, full_cells),
)
check(
    "at least four formal-adjoint/mirror symbol orbits must supplement W131",
    minimal_bridge_orbits is not None and len(minimal_bridge_orbits) == 4,
    (
        "none found"
        if minimal_bridge_orbits is None
        else f"minimum {len(minimal_bridge_orbits)}"
    ),
)

print("\nOne lexicographically first minimum connectivity skeleton")
print("(support target only; it is NOT a selected/source-owned differential):")
if minimal_bridge_orbits is not None:
    for index, orbit in enumerate(minimal_bridge_orbits, start=1):
        print(f"  orbit {index}:")
        for source, target in sorted(orbit):
            print(f"    {source} -> {target}")


print("\n" + "=" * 94)
if FAILURES:
    print(f"CONTROLS FAILED: {FAILURES}")
    print("RESULT: VOID")
    raise SystemExit(1)

print("RESULT: B5-NORMALIZED-TRANSPORT-NOT-DETERMINED-BY-W131-DIFFERENTIAL")
print(
    "\nL0.  The projected W131 Rarita--Schwinger operator is a proper "
    "suboperator on\n"
    "ker Gamma (12 slots / 1664 dimensions), while B5 asks for a middle "
    "complex on\n"
    "S + im Gamma + ker Gamma (20 slots / 1920 dimensions).  Shared RS "
    "notation does\n"
    "not identify those objects.\n"
    "\nBEST-CASE KILL.  Even if every one of the 40 allowed W131-carrier "
    "symbol\n"
    "cells were nonzero, four relative binary endpoint phases would remain "
    "on the\n"
    "absent S/imGamma sectors.  A planted noncentral return intertwines that "
    "maximal\n"
    "envelope.  Therefore the written differential cannot normalize the "
    "20-slot\n"
    "transport or prove the P1/P2 one-bit weld.\n"
    "\nCONSTRUCTION TARGET.  The complete 136-cell class is connected and "
    "would force\n"
    "a central slot-diagonal return if a written differential actually "
    "realized a\n"
    "connected nonzero coefficient graph.  Starting from W131, the support "
    "lower\n"
    "bound is four additional formal-adjoint/mirror symbol orbits connecting "
    "the\n"
    "S and imGamma provenance slots to the RS/X core.  Their coefficients, "
    "nilpotent/\n"
    "acyclic arrangement, normalized Krein adjoint, Green form, and common "
    "domain\n"
    "remain to be constructed; selecting the displayed skeleton is not a "
    "solution."
)
