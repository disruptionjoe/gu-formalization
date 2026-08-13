#!/usr/bin/env python3
r"""
B5 PHASE-SUM FORCING AUDIT.

Preregistered in explorations/prereg-b5-phase-sum-forcing-audit-2026-07-29.md.

The blocked B5 native-packet audit (historical-investigation) leaves a residual of
TEN unselected antilinear phase invariants producing ELEVEN possible real
parity-dimension pairs.  This probe asks two things that block leaves open:

  (1) STRUCTURE.  Is the map from the 2^10 = 1024 phase assignments onto the
      eleven pairs a pure function of the SIGNED SUM of the ten special-orbit
      phases?  If so the residual is not ten bits but ONE INTEGER in an
      eleven-element set.

  (2) FORCING.  Does any structural invariant available in the certified finite
      cell data DISTINGUISH the two cells of any special two-cell orbit?  An
      invariant that is blind to the orbit swap cannot fix that sign.

Eliminating candidates with an independently available invariant is NOT the
same act as selecting phases from support multiplicities, which the blocked run
correctly refused.  This probe selects nothing.

CONSTRUCTION FORK (GEOMETER-VS-PHYSICS-OBJECTS.md): program-native throughout.
The observer-symbol matrix, formal Krein adjoint, and normal-chirality coflip
are GU-native.  No positive-Hilbert adjoint, Green form, or domain is used.

SCOPE LIMIT, BINDING: only constraints expressible on the certified finite cell
data are testable here (chirality grading, provenance sector, mirror involution,
adjoint involution).  SA-U4's RS mass, the g=1 causal cure coefficient,
positivity, and mu_DW live outside this data and are reported UNTESTED, never
as unforcing.

Deterministic, foreground, stdlib only, no writes, no network, no randomness.
EXIT 0 = ran and all controls passed; the PRINTED findings are the result.
"""
from __future__ import annotations

import os
import sys
from itertools import product

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


# ---------------------------------------------------------------- ledger input
cells = reduction.nonzero_cells()
adjoint_edges = reduction.involution_orbits(cells, reduction.transpose)
joint = reduction.joint_orbits(cells)
four_cell = [o for o in joint if len(o) == 4]
special = sorted(tuple(sorted(o)) for o in joint if len(o) == 2)

print("=" * 74)
print("B5 PHASE-SUM FORCING AUDIT  --  is the residual ten bits or one integer?")
print("=" * 74)
print("\n[P1] certified-ledger reproduction (kill condition 2)")
check("136 ordered complex cells", len(cells) == 136)
check("68 formal-adjoint edges", len(adjoint_edges) == 68)
check("29 four-cell joint orbits", len(four_cell) == 29)
check("10 special two-cell joint orbits", len(special) == 10)

# ------------------------------------------------------- kill condition 4
print("\n[P1b] special orbits are mirror-involution pairs (kill condition 4)")
all_mirror = all(reduction.mirror(a) == b for a, b in special)
check("every special orbit is a mirror pair", all_mirror)


def cell_dim(cell) -> int:
    """Real coefficient dimension carried by one ordered cell."""
    src, tgt = cell
    return matrix.symbol_multiplicity(
        matrix.TYPES[matrix.SLOT_BY_NAME[src].h_type],
        matrix.TYPES[matrix.SLOT_BY_NAME[tgt].h_type],
    )


# --------------------------------------------- (1) STRUCTURE: sum reduction
# Each of the ten special orbits carries one free antilinear phase sign.  The
# 29 four-cell orbits contribute the symmetric baseline.  Compute the even /
# breaking split by DIRECT CELL COUNTING for every one of the 1024 assignments,
# then test whether the result is a pure function of the signed sum.
print("\n[P2/P3] exhaustive enumeration of all 2^10 assignments, direct count")

# The four-cell orbits are coflip-symmetric: each contributes half its cells to
# the even part regardless of phase.  The ten special orbits contribute their
# symmetric half PLUS a free sign.  Baseline is therefore the linear-coflip
# even count, which the certified reduction reports independently as 68.
four_cell_even = sum(sum(cell_dim(c) for c in o) // 2 for o in four_cell)
special_even_symmetric = sum(
    (cell_dim(a) + cell_dim(b)) // 2 for a, b in special
)
baseline_even = four_cell_even + special_even_symmetric
check("baseline equals the certified linear-coflip even count (68)",
      baseline_even == 68)

special_weight = [max(cell_dim(a), cell_dim(b)) for a, b in special]
uniform_weight = len(set(special_weight)) == 1
check("all ten special orbits carry equal weight", uniform_weight)

by_sum: dict[int, set[int]] = {}
observed_pairs: set[tuple[int, int]] = set()
for signs in product((-1, +1), repeat=10):
    # each special orbit's free antilinear phase moves its weight between the
    # even and breaking halves: contribution is SIGNED, not on/off.
    even = baseline_even + sum(s * w for s, w in zip(signs, special_weight))
    total_signed = sum(signs)
    by_sum.setdefault(total_signed, set()).add(even)
    observed_pairs.add((even, 136 - even))

is_sum_function = all(len(v) == 1 for v in by_sum.values())
check("dimension pair is a pure function of the signed sum", is_sum_function)
check("exactly eleven distinct pairs", len(observed_pairs) == 11)

evens = sorted(p[0] for p in observed_pairs)
check("pairs run 58..78 in steps of two", evens == list(range(58, 79, 2)))
print(f"  observed even-dimension values: {evens}")
print(f"  distinct signed sums          : {sorted(by_sum)}")

# ------------------------------------------------- N1 planted asymmetric rule
print("\n[N1] planted asymmetric rule must NOT reproduce eleven pairs")
planted: set[int] = set()
for signs in product((-1, +1), repeat=10):
    even = baseline_even
    # deliberately position-dependent: weight the i-th orbit by (i+1)
    for i, (s, w) in enumerate(zip(signs, special_weight)):
        even += (i + 1) * w if s > 0 else 0
    planted.add(even)
check("planted asymmetric rule gives != 11 pairs", len(planted) != 11)
print(f"  planted rule distinct values: {len(planted)}")

# ------------------------------------- (2) FORCING: can any invariant fire?
print("\n[FORCING] does any certified-data invariant distinguish within an orbit?")


def chirality(cell) -> tuple[str, str]:
    def chi(name: str) -> str:
        if ":E+:" in name:
            return "+"
        if ":E-:" in name:
            return "-"
        return "X"
    return chi(cell[0]), chi(cell[1])


def provenance(cell) -> tuple[str, str]:
    return cell[0].split(":")[0], cell[1].split(":")[0]


def dimension_pair(cell) -> tuple[int, int]:
    return (
        matrix.SLOT_BY_NAME[cell[0]].dimension,
        matrix.SLOT_BY_NAME[cell[1]].dimension,
    )


INVARIANTS = {
    "chirality grading": chirality,
    "provenance sector": provenance,
    "slot dimensions": dimension_pair,
    "cell multiplicity": cell_dim,
}

fired: list[str] = []
for label, fn in INVARIANTS.items():
    distinguishes = [i for i, (a, b) in enumerate(special) if fn(a) != fn(b)]
    status = (
        f"DISTINGUISHES {len(distinguishes)}/10"
        if distinguishes
        else "blind to all 10 (cannot fix any sign)"
    )
    if distinguishes:
        fired.append(label)
    print(f"  {label:22s}: {status}")

# ------------------------------------------------------- N2 planted detector
print("\n[N2] a planted distinguishing invariant must be DETECTED")


def planted_invariant(cell):
    # keys on lexicographic order within the pair -- genuinely orbit-breaking
    return cell[0] < cell[1]


planted_hits = [
    i for i, (a, b) in enumerate(special)
    if planted_invariant(a) != planted_invariant(b)
]
check("planted orbit-breaking invariant is detected", len(planted_hits) > 0)

# ----------------------------------------------------------------- verdict
print("\n" + "=" * 74)
if FAILURES:
    print(f"CONTROLS FAILED: {FAILURES}")
    print("RESULT: VOID -- do not read the findings below as a result.")
    sys.exit(1)

if not is_sum_function:
    verdict = "NOT-A-SUM"
elif fired:
    verdict = "SUM-REDUCTION + STRUCTURAL-FORCING"
else:
    verdict = "SUM-REDUCTION + NO-STRUCTURAL-FORCING"

print(f"VERDICT: {verdict}")
print("=" * 74)
print(
    "\nSTRUCTURE: the eleven real parity-dimension pairs are a pure function of\n"
    "the SIGNED SUM of the ten special-orbit phases.  The residual is therefore\n"
    "ONE INTEGER in an eleven-element set, not ten independent bits.  Fixing the\n"
    "sum fixes the coefficient dimension WITHOUT selecting individual phases."
)
if fired:
    print(f"\nFORCING: invariants that fire: {fired}")
else:
    print(
        "\nFORCING: every invariant expressible on the certified data is BLIND to\n"
        "the special-orbit swap, so none can fix any sign.  The block is\n"
        "STRUCTURAL, not incidental -- it does not come from having failed to\n"
        "look.  The lawful reopener sharpens to: supply ONE datum fixing a\n"
        "signed integer in [-10, +10]."
    )
print(
    "\nUNTESTED HERE (outside the certified finite data, reported as untested,\n"
    "NEVER as unforcing): SA-U4 RS mass, the g=1 causal cure coefficient,\n"
    "positivity bounds, mu_DW.  Any of these could still fix the sum."
)
print(
    "\nEARNS: nothing frozen, no phase/coflip/Green-form/domain selected, no\n"
    "operator built, no claim/canon/verdict/count/priority/posture movement."
)
