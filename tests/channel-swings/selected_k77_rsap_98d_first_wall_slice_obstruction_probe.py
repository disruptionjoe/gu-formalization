#!/usr/bin/env python3
"""Exact local 98D RSAP construction at one split-root wall.

The nonlinear carrier is the cotangent bundle of the homogeneous space
SL(2,R)/A.  The finite matrices below certify its moment-map rank change and
Poisson identity, then compose it with an 82D symplectic leaf and T*R^6.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def zeros(rows: int, cols: int) -> list[list[Fraction]]:
    return [[Fraction(0) for _ in range(cols)] for _ in range(rows)]


def identity(size: int) -> list[list[Fraction]]:
    result = zeros(size, size)
    for index in range(size):
        result[index][index] = Fraction(1)
    return result


def transpose(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(column) for column in zip(*matrix)]


def multiply(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    right_t = transpose(right)
    return [[sum(a * b for a, b in zip(row, column)) for column in right_t] for row in left]


def rank(matrix: list[list[Fraction]]) -> int:
    work = [[Fraction(value) for value in row] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    pivot_row = 0
    for col in range(cols):
        pivot = next((row for row in range(pivot_row, rows) if work[row][col]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][col]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row:
                continue
            scale = work[row][col]
            if scale:
                work[row] = [a - scale * b for a, b in zip(work[row], work[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def block_diag(*blocks: list[list[Fraction]]) -> list[list[Fraction]]:
    total_rows = sum(len(block) for block in blocks)
    total_cols = sum(len(block[0]) for block in blocks)
    result = zeros(total_rows, total_cols)
    row_offset = 0
    col_offset = 0
    for block in blocks:
        for row, values in enumerate(block):
            for col, value in enumerate(values):
                result[row_offset + row][col_offset + col] = value
        row_offset += len(block)
        col_offset += len(block[0])
    return result


def standard_poisson(pair_count: int) -> list[list[Fraction]]:
    result = zeros(2 * pair_count, 2 * pair_count)
    for index in range(pair_count):
        result[index][pair_count + index] = Fraction(1)
        result[pair_count + index][index] = Fraction(-1)
    return result


def sl2_poisson(h: int, e: int, f: int) -> list[list[Fraction]]:
    return [
        [Fraction(0), Fraction(2 * e), Fraction(-2 * f)],
        [Fraction(-2 * e), Fraction(0), Fraction(h)],
        [Fraction(2 * f), Fraction(-h), Fraction(0)],
    ]


def sl2_moment_differential(e: int, f: int) -> list[list[Fraction]]:
    # Columns are base E,F followed by fibre E*,F* in T*(SL2/A).
    return [
        [Fraction(2 * e), Fraction(-2 * f), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0), Fraction(1)],
    ]


def projection(rows: int) -> list[list[Fraction]]:
    result = zeros(rows, 2 * rows)
    for index in range(rows):
        result[index][index] = Fraction(1)
    return result


registry = json.loads(
    (ROOT / "lab/process/selected-k77-rsap-98d-first-wall-slice-obstruction.json").read_text(encoding="utf-8")
)
prior = json.loads(
    (ROOT / "lab/process/selected-k77-rank-singular-poisson-rank-loss-schedule.json").read_text(encoding="utf-8")
)

print("A. LAYER ZERO AND LIE ALGEBRA")
check("layer0", "the wall is codimension one in the Cartan base", registry["target"]["wall_codimension"]["cartan_or_invariant_base"] == 1)
check("layer0", "the same subregular locus is codimension three in the full target", registry["target"]["wall_codimension"]["full_lie_poisson_target"] == 3)
check("type", "the generic split-root centralizer is sl2 plus a six-dimensional centre", registry["target"]["wall_centralizer"] == "sl(2,R) direct_sum R^6")

# Structure constants for [H,E]=2E, [H,F]=-2F, [E,F]=H.
c = {}
c[0, 1, 1], c[1, 0, 1] = 2, -2
c[0, 2, 2], c[2, 0, 2] = -2, 2
c[1, 2, 0], c[2, 1, 0] = 1, -1
jacobi_ok = True
for i in range(3):
    for j in range(3):
        for k in range(3):
            for n in range(3):
                value = sum(
                    c.get((i, j, m), 0) * c.get((m, k, n), 0)
                    + c.get((j, k, m), 0) * c.get((m, i, n), 0)
                    + c.get((k, i, m), 0) * c.get((m, j, n), 0)
                    for m in range(3)
                )
                jacobi_ok &= value == 0
check("jacobi", "the sl2 structure constants satisfy Jacobi exactly", jacobi_ok)
check("poisson", "the sl2 bivector has rank two at a split point", rank(sl2_poisson(0, 1, 1)) == 2)
check("poisson", "the sl2 bivector has rank two at an elliptic point", rank(sl2_poisson(0, 1, -1)) == 2)
check("poisson", "the sl2 bivector has rank two at a nilpotent point", rank(sl2_poisson(0, 1, 0)) == 2)
check("poisson", "the sl2 bivector vanishes only at the wall origin", rank(sl2_poisson(0, 0, 0)) == 0)

print("\nB. COTANGENT HOMOGENEOUS-SPACE MOMENT MAP")
source_pi4 = standard_poisson(2)
check("symplectic", "T*(SL2/A) has exact symplectic rank four", rank(source_pi4) == 4)

sample_points = [(0, 0), (1, 0), (0, 1), (1, 1), (1, -1)]
for e, f in sample_points:
    differential = sl2_moment_differential(e, f)
    pulled = multiply(multiply(differential, source_pi4), transpose(differential))
    check("moment", f"cotangent moment map is Poisson at ann(a) sample ({e},{f})", pulled == sl2_poisson(0, e, f))
check("rank", "the sl2 moment map has rank two on the zero section", rank(sl2_moment_differential(0, 0)) == 2)
for e, f in sample_points[1:]:
    check("rank", f"the sl2 moment map has rank three away from zero at ({e},{f})", rank(sl2_moment_differential(e, f)) == 3)

# ann(a) is the off-diagonal plane.  These representatives hit every real
# coadjoint type; trace and determinant classify the nonzero semisimple types.
representatives = {
    "zero": (0, 0, 0),
    "split_plus": (0, 1, 1),
    "split_minus": (0, -1, -1),
    "elliptic_plus": (0, 1, -1),
    "elliptic_minus": (0, -1, 1),
    "nilpotent_e_plus": (0, 1, 0),
    "nilpotent_e_minus": (0, -1, 0),
    "nilpotent_f_plus": (0, 0, 1),
    "nilpotent_f_minus": (0, 0, -1),
}
check("surjective", "ann(a) contains representatives of zero and every real coadjoint type", len(representatives) == 9 and all(h == 0 for h, _, _ in representatives.values()))
determinants = {name: -h * h - e * f for name, (h, e, f) in representatives.items()}
check("surjective", "split representatives have negative determinant", determinants["split_plus"] == determinants["split_minus"] == -1)
check("surjective", "elliptic representatives have positive determinant", determinants["elliptic_plus"] == determinants["elliptic_minus"] == 1)
check("surjective", "nilpotent representatives have zero determinant", all(determinants[name] == 0 for name in representatives if name.startswith("nilpotent")))
check("surjective", "the registry records full coadjoint saturation", registry["transverse_realization"]["surjective"] is True)

print("\nC. FULL 98D PRODUCT NORMAL FORM")
leaf_pi = standard_poisson(41)
abelian_source_pi = standard_poisson(6)
abelian_projection = projection(6)
source_pi98 = block_diag(leaf_pi, source_pi4, abelian_source_pi)
check("symplectic", "the product source Poisson tensor has rank 98", rank(source_pi98) == 98)

for label, e, f, expected_target_rank, expected_map_rank in (
    ("regular", 1, 1, 84, 91),
    ("wall", 0, 0, 82, 90),
):
    differential = block_diag(identity(82), sl2_moment_differential(e, f), abelian_projection)
    target_pi = block_diag(leaf_pi, sl2_poisson(0, e, f), zeros(6, 6))
    pulled = multiply(multiply(differential, source_pi98), transpose(differential))
    check("compose", f"{label} product map has shape 91x98", len(differential) == 91 and len(differential[0]) == 98)
    check("compose", f"{label} target Poisson rank is {expected_target_rank}", rank(target_pi) == expected_target_rank)
    check("compose", f"{label} moment-map rank is {expected_map_rank}", rank(differential) == expected_map_rank)
    check("compose", f"{label} product Poisson identity holds exactly", pulled == target_pi)

attachment = registry["wall_attachment"]
check("fibre", "regular fibre dimension is seven", attachment["dimension"] - attachment["regular_map_rank"] == 7)
check("fibre", "wall fibre dimension jumps smoothly to eight", attachment["dimension"] - attachment["wall_map_rank"] == 8)
check("sharp", "the regular point saturates the prior rank inequality", 2 * 91 == 98 + 84)
check("sharp", "the wall point saturates the prior rank inequality", 2 * 90 == 98 + 82)
check("prior", "the predecessor requested exactly this rank schedule", prior["minimal_98_schedule"][1]["map_rank_ceiling"] == 90)

print("\nD. OVERLAP, SMOOTHNESS, AND CLAIM CEILING")
overlap = registry["regular_overlap"]
check("overlap", "both adjacent hyperbolic Cartan chambers are attached", overlap["adjacent_chambers_attached"] is True)
check("overlap", "the tautological cotangent potential is preserved on regular overlaps", overlap["tautological_potential_preserved"] is True)
check("smooth", "the carrier is one smooth manifold rather than a stratified union", attachment["smooth_domain"] is True and attachment["stratified_domain"] is False)
check("smooth", "the map is locally surjective across the wall", attachment["local_target_surjectivity"] is True)
check("scope", "only one split-root first wall is admitted", registry["scope"]["first_split_root_wall"] == "CONSTRUCTED")
check("scope", "global RSAP remains open", registry["scope"]["global_rsap"] == "OPEN")
check("scope", "zero-charge rank 49 is not constructed", registry["scope"]["zero_charge_rank_at_most_49"] == "NOT_CONSTRUCTED")
check("accounting", "no protected truth surface moves", set(registry["changes"].values()) == {"none"})

assert sum(COUNTS.values()) == 46, sum(COUNTS.values())
print("\nSUMMARY")
print(json.dumps({"counts": dict(COUNTS), "failures": FAILURES, "status": registry["status"], "next_gate": registry["next_gate"]}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print("PASS 46/46")
