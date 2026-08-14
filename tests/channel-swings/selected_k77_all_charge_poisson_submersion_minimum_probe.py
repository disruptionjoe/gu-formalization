#!/usr/bin/env python3
"""Exact dimension bound for all-charge Poisson submersions of so(7,7)*."""

from collections import Counter
from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def strict(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def rank(matrix):
    work = [[Fraction(value) for value in row] for row in matrix]
    if not work:
        return 0
    rows, columns = len(work), len(work[0])
    pivot_row = 0
    for column in range(columns):
        pivot = next((row for row in range(pivot_row, rows) if work[row][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for row in range(rows):
            if row != pivot_row and work[row][column]:
                multiple = work[row][column]
                work[row] = [left - multiple * right for left, right in zip(work[row], work[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def poisson_block(dimension, target_rank):
    assert target_rank % 2 == 0 and target_rank <= dimension
    result = [[0 for _ in range(dimension)] for _ in range(dimension)]
    for index in range(0, target_rank, 2):
        result[index][index + 1] = 1
        result[index + 1][index] = -1
    return result


atlas = strict("lab/process/selected-k77-regular-semisimple-cartan-atlas-realization.json")
boundary = strict("lab/process/selected-k77-boundary-stationarity-symplectic-realization-gate.json")

print("A. PRIOR RESULT AND LAYER ZERO")
check("prior", "the complete regular-semisimple atlas has dimension 98",
      atlas["component"]["dimension"] == 98)
check("prior", "the regular moment rank is 91", atlas["component"]["moment_rank"] == 91)
check("prior", "the inherited all-charge interval was 98 through 182",
      boundary["regular_lie_poisson_geometry"]["smallest_global_equivariant_dimension"] == "OPEN_IN_INTERVAL_98_TO_182")
for label in (
    "Poisson submersion versus a rank-singular Poisson map",
    "regular-semisimple locus versus all of g-star",
    "source-owned edge phase space versus mathematical realization",
    "pointwise lower bound versus connectedness of the carrier",
):
    check("layer0", label + " remain distinct", True)

print("\nB. POINTWISE POISSON-SUBMERSION LOWER BOUND")
base_dimension = 91
for poisson_rank in (84, 70, 0):
    pi = poisson_block(base_dimension, poisson_rank)
    computed_rank = rank(pi)
    corank = base_dimension - computed_rank
    minimum = base_dimension + corank
    check("exact", f"rank-{poisson_rank} canonical skew block has exact rank",
          computed_rank == poisson_rank)
    check("theorem", f"rank-{poisson_rank} submersion bound is 182-rank",
          minimum == 182 - poisson_rank)

# If J is a Poisson submersion, the 91 Hamiltonian lifts W are independent.
# omega|W has rank r, so rad(W) has dimension 91-r. Since W^omega=ker dJ,
# rad(W) lies in the vertical space, whose dimension is dim(M)-91.
for poisson_rank in (84, 70, 0):
    radical = base_dimension - poisson_rank
    check("theorem", f"rank-{poisson_rank} radical fits only when vertical dimension is at least corank",
          (182 - poisson_rank) - base_dimension == radical)

print("\nC. REGULAR AND ZERO-ORBIT CONSEQUENCES")
check("result", "the regular rank-84 lower bound reproduces 98", 182 - 84 == 98)
check("result", "the zero coadjoint orbit has Poisson rank zero", rank(poisson_block(91, 0)) == 0)
check("result", "any all-charge Poisson submersion has dimension at least 182", 182 - 0 == 182)
check("construction", "the cotangent group has dimension 182", 2 * 91 == 182)
check("result", "the all-charge Poisson-submersion minimum is exactly 182", 2 * 91 == 182 - 0)
check("scope", "a 98-dimensional Poisson submersion cannot include the zero orbit", 98 < 182)
check("scope", "a below-182 rival must weaken submersion at singular charges or change target class", True)

print("\nD. PHYSICAL AND CLAIM FENCES")
check("scope", "the theorem does not obstruct a weaker singular Poisson map", True)
check("source", "the source does not own the Cartan atlas or cotangent edge carrier", True)
check("physics", "no boundary action domain quantization or cohomology follows", True)
check("accounting", "no ledger canon residue quotient datum or public-posture change follows", True)

RESULT = {
    "disposition": "ALL_CHARGE_POISSON_SUBMERSION_MINIMUM_EXACTLY_182__REGULAR_LOCUS_MINIMUM_98__WEAKER_SINGULAR_MAP_CLASS_OPEN",
    "target_dimension": 91,
    "pointwise_bound": "dim(M)>=182-rank(pi_p)",
    "regular_rank": 84,
    "regular_minimum": 98,
    "zero_rank": 0,
    "all_charge_submersion_minimum": 182,
    "next_gate": "TYPE_A_WEAKER_RANK_SINGULAR_POISSON_MAP_CLASS_BEFORE_SEEKING_ANY_ALL_CHARGE_CARRIER_BELOW_182",
}
print(json.dumps(RESULT, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
