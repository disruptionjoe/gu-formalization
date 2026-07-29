#!/usr/bin/env python3
r"""
B5 CHIRALITY ORIENTATION AUDIT.

Preregistered in explorations/prereg-b5-chirality-orientation-audit-2026-07-29.md.
Follows explorations/b5-phase-sum-forcing-audit-2026-07-29.md.

The prior run found chirality grading is not blind to six of the ten special
orbits, and was careful to claim only CAPABILITY, never that a forced rule
fires.  This probe closes that gap.

  DISTINGUISHING: the two cells of an orbit carry different labels.  Necessary,
                  fixes nothing.
  ORIENTING:      something canonically says WHICH member takes the + phase.
                  Only an orientation can fix a sign, hence the signed sum.

An orientation exists iff the certified ledger FAILS to be invariant under
global chirality exchange.  If relabelling every E+ <-> E- leaves the cell set,
multiplicity function, slot dimensions, and orbit structure identical, the
labels carry no canonical direction.

CONSTRUCTION FORK (GEOMETER-VS-PHYSICS-OBJECTS.md): program-native throughout.
No positive-Hilbert object used or substituted.

Deterministic, foreground, stdlib only, no writes, no network, no randomness.
EXIT 0 = ran and all controls passed; the PRINTED findings are the result.
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))

import shiab_b5_observer_symbol_multiplicity_matrix as matrix  # noqa: E402
import shiab_b5_krein_mirror_orbit_reduction as reduction  # noqa: E402

FAILURES: list[str] = []


def check(label: str, condition: bool) -> None:
    if condition:
        print(f"PASS: {label}")
    else:
        FAILURES.append(label)
        print(f"FAIL: {label}")


cells = reduction.nonzero_cells()
joint = reduction.joint_orbits(cells)
special = sorted(tuple(sorted(o)) for o in joint if len(o) == 2)

print("=" * 74)
print("B5 CHIRALITY ORIENTATION AUDIT  --  distinguished, or actually oriented?")
print("=" * 74)


def has_chirality(name: str) -> bool:
    return ":E+:" in name or ":E-:" in name


chirality_orbits = [o for o in special if has_chirality(o[0][0])]
x_orbits = [o for o in special if not has_chirality(o[0][0])]

print("\n[P2] reproduce the prior run's orbit identification (kill 3)")
check("six chirality special orbits", len(chirality_orbits) == 6)
check("four X-sector special orbits", len(x_orbits) == 4)

# ------------------------------------------------- P1 global mirror involution
print("\n[P1] global chirality exchange is an involution on the ledger (kill 2)")


def mirror_slot(name: str) -> str:
    return matrix.SLOT_BY_NAME[name].mirror


involutive = all(
    mirror_slot(mirror_slot(s.name)) == s.name for s in matrix.SLOTS
)
check("mirror is an involution on all slots", involutive)

mirrored_cells = {reduction.mirror(c) for c in cells}
check("mirror permutes the certified cell set", mirrored_cells == cells)


# ------------------------------------------- the invariance battery
def dim_of(name: str) -> int:
    return matrix.SLOT_BY_NAME[name].dimension


def mult_of(cell) -> int:
    src, tgt = cell
    return matrix.symbol_multiplicity(
        matrix.TYPES[matrix.SLOT_BY_NAME[src].h_type],
        matrix.TYPES[matrix.SLOT_BY_NAME[tgt].h_type],
    )


def slot_dimension_symmetric() -> bool:
    return all(dim_of(s.name) == dim_of(s.mirror) for s in matrix.SLOTS)


def multiplicity_symmetric() -> bool:
    return all(mult_of(c) == mult_of(reduction.mirror(c)) for c in cells)


def orbit_structure_symmetric() -> bool:
    sizes = sorted(len(o) for o in joint)
    mirrored = sorted(
        len({reduction.mirror(c) for c in o}) for o in joint
    )
    return sizes == mirrored


print("\n[ORIENTATION] does any certified structure BREAK global exchange?")
battery = {
    "slot dimensions": slot_dimension_symmetric(),
    "symbol multiplicities": multiplicity_symmetric(),
    "orbit structure": orbit_structure_symmetric(),
    "cell set": mirrored_cells == cells,
}
breakers = [k for k, sym in battery.items() if not sym]
for label, sym in battery.items():
    state = "SYMMETRIC (orients nothing)" if sym else "BREAKS EXCHANGE (orients)"
    print(f"  {label:24s}: {state}")

# ---------------------------------------------------- N1/N2 planted asymmetry
print("\n[N1/N2] planted asymmetries must be DETECTED (kill 1)")

real_types = dict(matrix.TYPES)
# victim = the SOURCE slot of the first cell of the first chirality orbit
victim_slot = chirality_orbits[0][0][0]
victim = matrix.SLOT_BY_NAME[victim_slot].h_type
victim_dim = matrix.TYPES[victim].dimension
donor = next(
    name for name, t in matrix.TYPES.items() if t.dimension != victim_dim
)
try:
    # break the E+/E- symmetry by giving ONE chirality type a foreign dimension
    matrix.TYPES[victim] = matrix.TYPES[donor]
    planted_dim_detected = not slot_dimension_symmetric()
    planted_mult_detected = not multiplicity_symmetric()
finally:
    matrix.TYPES.clear()
    matrix.TYPES.update(real_types)
print(f"  planted: type {victim} (dim {victim_dim}) -> {donor} "
      f"(dim {real_types[donor].dimension})")

check("planted dimension asymmetry detected", planted_dim_detected)
check("planted multiplicity asymmetry detected", planted_mult_detected)
check("ledger restored after planting", slot_dimension_symmetric())

# ------------------------------------------------------------------- verdict
print("\n" + "=" * 74)
if FAILURES:
    print(f"CONTROLS FAILED: {FAILURES}")
    print("RESULT: VOID -- do not read the findings below as a result.")
    sys.exit(1)

if not breakers:
    verdict = "DISTINGUISHED-NOT-ORIENTED"
elif len(breakers) == len(battery):
    verdict = "ORIENTED"
else:
    verdict = "PARTIALLY-ORIENTED"

print(f"VERDICT: {verdict}")
print("=" * 74)

if verdict == "DISTINGUISHED-NOT-ORIENTED":
    print(
        "\nEvery certified structure is INVARIANT under global chirality\n"
        "exchange.  Chirality separates the two cells of the six E+/E- special\n"
        "orbits but nothing in the ledger picks a DIRECTION, so no sign can be\n"
        "fixed from committed structure.\n"
        "\nCONSEQUENCE: the prior run's 'six addressable' reading is WITHDRAWN\n"
        "as a narrowing.  Those six are addressable only by an external Z/2\n"
        "chirality ORIENTATION -- the same TYPE of datum located-not-forced\n"
        "already says the count requires.  The residual stays at eleven pairs.\n"
        "\nCorroboration, not a new theorem: W201 / located-not-forced type the\n"
        "external datum as needing a K-DEFINITE, NON-chirality re-grading,\n"
        "because chirality eigenspaces are K-null.  This run reaches the same\n"
        "typing from the finite symbol ledger instead of from index theory.\n"
        "\nThe four X-sector orbits remain of an UNCLASSIFIED type: blind to\n"
        "every ledger invariant AND not addressed by the chirality Z/2."
    )
else:
    print(f"\nStructures breaking global exchange: {breakers}")
    print("An orientation is readable; residual narrows below eleven pairs.")

print(
    "\nEARNS: nothing frozen, no phase/orientation/Green-form/domain selected,\n"
    "no operator built, no claim/canon/verdict/count/priority/posture movement."
)
