#!/usr/bin/env python3
"""
W188: exact non-vacuity audit for the boundary-selection story.

This is deliberately a dependency/identifiability test, not a dynamics model.  It asks whether
today's live GU boundary candidates are one independent selector or several, and whether the
current package passes a strong anti-epicycle contract.

The columns are the most conservative independent coordinates visible in W150/W173/W177/W180/
W183/W184/W186.  Two umbrella phrases are split because today's constructions do not supply a
relation between their parts:

  reservoir datum  -> reservoir Krein type + source/kinematic coupling ratio
  generation datum -> K-class carrier + count selector
  section/source    -> observer section + source/cure declaration

The ghost-parity/S-matrix coordinate is kept separate because W184 proves that a Cartan grading is
not a dynamical superselection rule.  mu_DW is a further continuous scale coordinate.

Run:  python -u tests/W188_boundary_selection_nonvacuity.py
Dependencies: Python standard library only.
"""

from fractions import Fraction


CHECKS = []


def check(name, passed, detail=""):
    passed = bool(passed)
    CHECKS.append(passed)
    suffix = f" -- {detail}" if detail else ""
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}{suffix}")


def exact_rank(matrix):
    """Gaussian-elimination rank over Q, plus pivot columns."""
    if not matrix:
        return 0, ()
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError("ragged matrix")
    a = [[Fraction(value) for value in row] for row in matrix]
    row = 0
    pivots = []
    for col in range(width):
        pivot = next((r for r in range(row, len(a)) if a[r][col] != 0), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        scale = a[row][col]
        a[row] = [value / scale for value in a[row]]
        for r in range(len(a)):
            if r == row or a[r][col] == 0:
                continue
            factor = a[r][col]
            a[r] = [x - factor * y for x, y in zip(a[r], a[row])]
        pivots.append(col)
        row += 1
        if row == len(a):
            break
    return row, tuple(pivots)


def dependency_matrix(outcomes, columns):
    return [[int(column in outcome["deps"]) for column in columns] for outcome in outcomes]


def submatrix(matrix, columns):
    return [[row[column] for column in columns] for row in matrix]


def strict_surplus(matrix):
    """Relations among outputs minus independent boundary freedoms added."""
    rank, _ = exact_rank(matrix)
    relations = len(matrix) - rank
    return relations - rank, relations, rank


COLUMNS = (
    "reservoir_krein_type",
    "eta_coupling_ratio",
    "ghost_parity_dynamics",
    "generation_kclass",
    "generation_count_selector",
    "mu_DW_scale",
    "observer_section",
    "source_cure_choice",
)


# `risky_cross=True` means the row is a frozen, potentially falsifying relation spanning at least
# two named sectors.  It does not mean the relation has already been derived in full GU QFT.
OUTCOMES = (
    {
        "name": "positive_total_C_metric",
        "sectors": ("quantum", "source"),
        "deps": ("reservoir_krein_type", "eta_coupling_ratio"),
        "risky_cross": True,
    },
    {
        "name": "reduced_ghost_pole_sheet",
        "sectors": ("quantum",),
        "deps": ("reservoir_krein_type", "eta_coupling_ratio", "ghost_parity_dynamics"),
        "risky_cross": False,
    },
    {
        "name": "ghost_to_two_gravitons_allowed",
        "sectors": ("quantum",),
        "deps": ("ghost_parity_dynamics",),
        "risky_cross": False,
    },
    {
        "name": "law_shadow_scalar_sign",
        "sectors": ("quantum", "gravity"),
        "deps": ("ghost_parity_dynamics",),
        "risky_cross": True,
    },
    {
        "name": "C2_mirror_demotion",
        "sectors": ("matter",),
        "deps": ("source_cure_choice",),
        "risky_cross": False,
    },
    {
        "name": "index_changing_RS_carrier",
        "sectors": ("matter",),
        "deps": ("generation_kclass",),
        "risky_cross": False,
    },
    {
        "name": "realized_generation_count",
        "sectors": ("matter",),
        "deps": ("generation_kclass", "generation_count_selector"),
        "risky_cross": False,
    },
    {
        "name": "RS_causal_cure_branch",
        "sectors": ("matter", "source"),
        "deps": ("generation_kclass", "source_cure_choice"),
        "risky_cross": True,
    },
    {
        "name": "PPN_Yukawa_range",
        "sectors": ("gravity",),
        "deps": ("mu_DW_scale",),
        "risky_cross": False,
    },
    {
        "name": "GW_dispersion_threshold",
        "sectors": ("gravity", "quantum"),
        "deps": ("mu_DW_scale",),
        "risky_cross": True,
    },
    {
        "name": "observer_shadow_pullback",
        "sectors": ("observer",),
        "deps": ("observer_section",),
        "risky_cross": False,
    },
    {
        "name": "overlap_and_operator_gluing",
        "sectors": ("observer",),
        "deps": ("observer_section",),
        "risky_cross": False,
    },
    {
        "name": "matter_connection_current_normalization",
        "sectors": ("matter", "source"),
        "deps": ("eta_coupling_ratio", "source_cure_choice"),
        "risky_cross": True,
    },
    {
        "name": "dark_energy_source_amplitude",
        "sectors": ("cosmology", "source"),
        "deps": ("eta_coupling_ratio", "mu_DW_scale", "source_cure_choice"),
        "risky_cross": True,
    },
    {
        "name": "reservoir_flux_type",
        "sectors": ("quantum", "source"),
        "deps": ("reservoir_krein_type", "source_cure_choice"),
        "risky_cross": True,
    },
    {
        "name": "section_source_transduction",
        "sectors": ("observer", "source"),
        "deps": ("observer_section", "source_cure_choice"),
        "risky_cross": True,
    },
)


# None of these values has been frozen source-first in the cited live chain.  Some have a lean or
# a constrained candidate family; that is not the same as pre-comparison freezing.
FROZEN_SOURCE_FIRST = {column: False for column in COLUMNS}


MATRIX = dependency_matrix(OUTCOMES, COLUMNS)


print("=" * 78)
print("PC -- exact-rank and non-vacuity controls")
print("=" * 78)

identity = [[int(i == j) for j in range(len(COLUMNS))] for i in range(len(COLUMNS))]
identity_rank, identity_pivots = exact_rank(identity)
check("PC1 identity has full exact rank", identity_rank == len(COLUMNS),
      f"rank={identity_rank}, pivots={identity_pivots}")

one_latent = [[1] for _ in OUTCOMES]
one_surplus, one_relations, one_rank = strict_surplus(one_latent)
check("PC2 a genuine one-latent source is rank one", one_rank == 1,
      f"rank={one_rank}")
check("PC3 one frozen selector reused over 16 outputs is compressive",
      one_surplus > 0, f"relations={one_relations}, freedoms=1, surplus={one_surplus}")

identity_surplus, identity_relations, _ = strict_surplus(identity)
check("NC1 independent one-output knobs fail anti-epicycle compression",
      identity_surplus < 0,
      f"relations={identity_relations}, freedoms={len(COLUMNS)}, surplus={identity_surplus}")

duplicate = [row + [row[0]] for row in MATRIX]
live_rank, live_pivots = exact_rank(MATRIX)
duplicate_rank, _ = exact_rank(duplicate)
check("NC2 relabeling one selector does not increase rank", duplicate_rank == live_rank,
      f"live={live_rank}, duplicated-label={duplicate_rank}")


print("\n" + "=" * 78)
print("A -- live-coordinate identifiability")
print("=" * 78)

check("A1 the live dependency matrix has eight identifiable coordinates",
      live_rank == len(COLUMNS), f"shape={len(MATRIX)}x{len(COLUMNS)}, rank={live_rank}")
check("A2 every live coordinate is a pivot in exact elimination",
      live_pivots == tuple(range(len(COLUMNS))), f"pivots={live_pivots}")
check("A3 today's alleged one boundary datum is not rank one", live_rank > 1,
      f"rank={live_rank}")

GROUPS = {
    "reservoir sign + eta ratio": (0, 1),
    "ghost parity dynamics": (2,),
    "generation K-class + count": (3, 4),
    "mu_DW scale": (5,),
    "observer section + source/cure": (6, 7),
}

expected_group_ranks = {
    "reservoir sign + eta ratio": 2,
    "ghost parity dynamics": 1,
    "generation K-class + count": 2,
    "mu_DW scale": 1,
    "observer section + source/cure": 2,
}

for name, indexes in GROUPS.items():
    group_rank, _ = exact_rank(submatrix(MATRIX, indexes))
    check(f"A-group {name}", group_rank == expected_group_ranks[name],
          f"rank={group_rank}")

check("A4 the three umbrella phrases each hide two coordinates",
      all(expected_group_ranks[name] == 2 for name in (
          "reservoir sign + eta ratio",
          "generation K-class + count",
          "observer section + source/cure",
      )))


print("\n" + "=" * 78)
print("B -- strong anti-epicycle contract")
print("=" * 78)

live_surplus, live_relations, _ = strict_surplus(MATRIX)
check("B1 live package is at best break-even, not strictly compressive",
      live_surplus == 0,
      f"outputs={len(OUTCOMES)}, relations={live_relations}, freedoms={live_rank}, surplus={live_surplus}")
check("B2 no live boundary value is frozen source-first",
      not any(FROZEN_SOURCE_FIRST.values()))

datum_results = {}
for column in COLUMNS:
    touched = [outcome for outcome in OUTCOMES if column in outcome["deps"]]
    sectors = sorted({sector for outcome in touched for sector in outcome["sectors"]})
    reused = len(sectors) >= 2
    # One coordinate adds one freedom.  Three or more locked output contracts imply more than one
    # relation and therefore eliminate more output freedom than the coordinate adds.
    eliminates_more = len(touched) >= 3
    risky_cross = any(outcome["risky_cross"] and len(outcome["sectors"]) >= 2
                      for outcome in touched)
    frozen = FROZEN_SOURCE_FIRST[column]
    passes = frozen and reused and eliminates_more and risky_cross
    datum_results[column] = {
        "frozen": frozen,
        "reused": reused,
        "eliminates_more": eliminates_more,
        "risky_cross": risky_cross,
        "passes": passes,
    }
    print(
        f"  {column:28s} frozen={int(frozen)} reuse={int(reused)} "
        f"compression={int(eliminates_more)} risky_cross={int(risky_cross)} "
        f"sectors={','.join(sectors)} consequences={len(touched)}"
    )

check("B3 generation count selector is not cross-sector reused",
      not datum_results["generation_count_selector"]["reused"])
check("B4 generation count selector adds as much freedom as it removes",
      not datum_results["generation_count_selector"]["eliminates_more"])
check("B5 generation count selector emits no risky cross-sector prediction",
      not datum_results["generation_count_selector"]["risky_cross"])
check("B6 no current datum passes all four strong gates",
      not any(result["passes"] for result in datum_results.values()))


print("\n" + "=" * 78)
print("C -- collapse requirement and falsifier")
print("=" * 78)

relations_needed_for_one = live_rank - 1
check("C1 a genuine one-coordinate source action must add seven independent relations",
      relations_needed_for_one == 7,
      f"current_rank={live_rank}, target_rank=1, relations_needed={relations_needed_for_one}")

# A concrete collapse control: all eight named coordinates are functions of one latent selector z.
# Its Jacobian has one column and therefore rank one.  The actual source action must earn an
# equivalent collapse without fitting the observed outputs.
collapse_control = [[1] for _ in COLUMNS]
collapse_rank, _ = exact_rank(collapse_control)
check("C2 explicit one-latent collapse control reaches rank one", collapse_rank == 1)

print("\n" + "=" * 78)
print("VERDICT")
print("=" * 78)
print(
    "TODAY: NOT ONE DATUM.  The conservative live ledger has exact rank 8: five umbrella "
    "families, with reservoir, generation, and section/source each splitting into two independent "
    "coordinates.  The 16-output contract is only break-even (surplus 0), no value was frozen "
    "source-first, and the observed generation count remains a pure selector with no cross-sector "
    "risk.  A future source action can still make the story non-vacuous, but it must derive at least "
    "seven independent relations before comparison and then survive a cross-sector prediction with "
    "the selector held fixed."
)

passed = sum(CHECKS)
total = len(CHECKS)
print(f"\nRESULT: {passed}/{total} checks passed")
raise SystemExit(0 if passed == total else 1)
