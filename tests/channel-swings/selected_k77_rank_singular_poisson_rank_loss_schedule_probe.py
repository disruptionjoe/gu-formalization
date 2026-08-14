#!/usr/bin/env python3
"""Exact pointwise rank schedule for the selected-K77 RSAP target."""

from collections import Counter
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


def rank(matrix):
    work = [[int(value) for value in row] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    pivot_row = 0
    for col in range(cols):
        pivot = next((row for row in range(pivot_row, rows) if work[row][col]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][col]
        for row in range(rows):
            if row == pivot_row or not work[row][col]:
                continue
            factor = work[row][col]
            work[row] = [pivot_value * a - factor * b for a, b in zip(work[row], work[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def restricted_symplectic_matrix(m, s, r):
    """Choose r/2 full pairs and s-r unpaired q-vectors in R^m."""
    n = m // 2
    pairs = r // 2
    isotropic = s - r
    indices = []
    for index in range(pairs):
        indices.extend([index, n + index])
    indices.extend(range(pairs, pairs + isotropic))
    matrix = []
    for left in indices:
        row = []
        for right in indices:
            if left < n and right == n + left:
                row.append(1)
            elif left >= n and right == left - n:
                row.append(-1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix


registry = json.loads((ROOT / "lab/process/selected-k77-rank-singular-poisson-rank-loss-schedule.json").read_text(encoding="utf-8"))
prior = json.loads((ROOT / "lab/process/selected-k77-rank-singular-poisson-map-target.json").read_text(encoding="utf-8"))

print("A. POINTWISE THEOREM")
theorem = registry["pointwise_theorem"]
check("type", "map rank and target Poisson rank remain distinct", theorem["map_rank_symbol"] == "s" and theorem["target_poisson_rank_symbol"] == "r")
check("theorem", "the radical inequality is recorded", theorem["inequality"] == "2*s <= m+r")
check("theorem", "the exact ceiling is recorded", theorem["ceiling"] == "s <= floor((m+r)/2)")
check("prior", "the map remains the typed RSAP class", prior["target"]["id"] == registry["map"]["id"] == "RSAP")

print("\nB. MINIMAL 98-DIMENSIONAL SCHEDULE")
expected = [(84, 91, 0), (82, 90, 1), (0, 49, 42)]
actual = [(row["poisson_rank"], row["map_rank_ceiling"], row["forced_rank_deficit"]) for row in registry["minimal_98_schedule"]]
check("exact", "the three-row schedule is exact", actual == expected)
for target_rank, ceiling, deficit in expected:
    check("arithmetic", f"ceiling at target rank {target_rank}", ceiling == (98 + target_rank) // 2)
    check("arithmetic", f"deficit at target rank {target_rank}", deficit == 91 - ceiling)
check("wall", "minimal carrier loses at least one rank at first wall", expected[1][2] == 1)
check("zero", "minimal carrier rank is at most 49 at zero", expected[2][1] == 49)

print("\nC. ALL BELOW-182 DIMENSIONS")
even_dimensions = list(range(98, 182, 2))
first_wall_deficits = {m: max(0, 91 - (m + 82) // 2) for m in even_dimensions}
zero_deficits = {m: 91 - m // 2 for m in even_dimensions}
check("control", "only m=98 is forced to lose rank at the first rank-82 wall", [m for m, value in first_wall_deficits.items() if value > 0] == [98])
check("theorem", "every below-182 even dimension loses rank at zero", all(value > 0 for value in zero_deficits.values()))
check("boundary", "m=180 still loses one rank at zero", zero_deficits[180] == 1)
check("boundary", "m=182 is the first dimension with no forced zero deficit", 91 - 182 // 2 == 0)
check("scope", "registry refuses universal first-wall loss", registry["all_below_182"]["first_wall_loss_forced"] is False)
check("scope", "registry records universal zero-charge loss", registry["all_below_182"]["zero_charge_loss_forced"] is True)

print("\nD. TANGENT-SPACE SHARPNESS")
for m, s, target_rank in registry["tangent_sharpness"]["saturating_triples"]:
    matrix = restricted_symplectic_matrix(m, s, target_rank)
    check("construct", f"constructed span has dimension {s}", len(matrix) == s and all(len(row) == s for row in matrix))
    check("construct", f"restricted rank is exactly {target_rank}", rank(matrix) == target_rank)
    check("construct", f"triple ({m},{s},{target_rank}) saturates", 2 * s == m + target_rank)
check("scope", "tangent sharpness is not a global map", registry["tangent_sharpness"]["global_map_constructed"] is False)

print("\nE. NEXT GATE AND ACCOUNTING")
check("next", "next gate requests the 91-to-90 wall normal form", "MAP_RANK_91_TO_90" in registry["next_gate"])
check("next", "next gate requests target rank 84-to-82", "TARGET_RANK_84_TO_82" in registry["next_gate"])
check("scope", "global existence remains open", registry["claim_ceiling"].startswith("NO_GLOBAL_RSAP_EXISTENCE"))
check("accounting", "no protected truth surface moves", set(registry["changes"].values()) == {"none"})

print(json.dumps({"counts": dict(COUNTS), "failures": FAILURES, "status": registry["status"], "next_gate": registry["next_gate"]}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
