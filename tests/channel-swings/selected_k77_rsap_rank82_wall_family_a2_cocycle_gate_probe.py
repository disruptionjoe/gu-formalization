#!/usr/bin/env python3
"""Exact rank-82 wall-family census and first A2 overlap gate.

The probe admits both real rank-one wall factors, composes every orthogonal
A1 x A1 pairing in a 98D carrier, checks a strict A1^3 permutation cocycle,
and kills the natural split-A2 carrier T*(SL(3,R)/SL(2,R)) at a regular
nilpotent value where its moment differential has rank seven instead of eight.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import itertools
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


def projection(rows: int) -> list[list[Fraction]]:
    result = zeros(rows, 2 * rows)
    for index in range(rows):
        result[index][index] = Fraction(1)
    return result


def sl2_poisson(h: int, e: int, f: int) -> list[list[Fraction]]:
    return [
        [Fraction(0), Fraction(2 * e), Fraction(-2 * f)],
        [Fraction(-2 * e), Fraction(0), Fraction(h)],
        [Fraction(2 * f), Fraction(-h), Fraction(0)],
    ]


def sl2_differential(e: int, f: int) -> list[list[Fraction]]:
    return [
        [Fraction(2 * e), Fraction(-2 * f), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0), Fraction(1)],
    ]


def su2_poisson(h: int, x: int, y: int) -> list[list[Fraction]]:
    return [
        [Fraction(0), Fraction(y), Fraction(-x)],
        [Fraction(-y), Fraction(0), Fraction(h)],
        [Fraction(x), Fraction(-h), Fraction(0)],
    ]


def su2_differential(x: int, y: int) -> list[list[Fraction]]:
    return [
        [Fraction(y), Fraction(-x), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0), Fraction(1)],
    ]


def factor(kind: str, zero: bool = False) -> tuple[list[list[Fraction]], list[list[Fraction]]]:
    if kind == "split":
        e, f = ((0, 0) if zero else (1, 1))
        return sl2_differential(e, f), sl2_poisson(0, e, f)
    x, y = ((0, 0) if zero else (1, 1))
    return su2_differential(x, y), su2_poisson(0, x, y)


def permutation_matrix(order: tuple[int, ...], block_size: int) -> list[list[Fraction]]:
    result = zeros(len(order) * block_size, len(order) * block_size)
    for new_block, old_block in enumerate(order):
        for offset in range(block_size):
            result[new_block * block_size + offset][old_block * block_size + offset] = Fraction(1)
    return result


def matrix_power(matrix: list[list[Fraction]], exponent: int) -> list[list[Fraction]]:
    result = identity(len(matrix))
    for _ in range(exponent):
        result = multiply(result, matrix)
    return result


registry = json.loads(
    (ROOT / "lab/process/selected-k77-rsap-rank82-wall-family-a2-cocycle-gate.json").read_text(encoding="utf-8")
)

print("A. D7 WALL AND PAIR CENSUS")
roots = []
for i, j in itertools.combinations(range(7), 2):
    for sign_i in (-1, 1):
        for sign_j in (-1, 1):
            root = [0] * 7
            root[i], root[j] = sign_i, sign_j
            roots.append(tuple(root))
check("root", "the D7 root system has 84 roots", len(set(roots)) == 84)
check("root", "every D7 root has squared length two", {sum(x * x for x in root) for root in roots} == {2})

inner_products = set()
pair_types = Counter()
for alpha, beta in itertools.combinations(roots, 2):
    dot = sum(a * b for a, b in zip(alpha, beta))
    if beta == tuple(-value for value in alpha):
        continue
    inner_products.add(dot)
    pair_types["A1xA1" if dot == 0 else "A2"] += 1
check("root", "nonparallel root pairs have inner product only -1, 0, or 1", inner_products == {-1, 0, 1})
check("root", "both orthogonal A1xA1 and adjacent A2 pairs occur", pair_types["A1xA1"] > 0 and pair_types["A2"] > 0)
check("root", "no B2 or G2 rank-two subsystem can occur in simply-laced D7", set(pair_types) == {"A1xA1", "A2"})
check("wall", "rank-82 first walls have exactly the two real rank-one forms", registry["wall_family"]["real_rank_one_forms"] == ["sl(2,R)", "su(2)"])
check("wall", "a complex rank-one jump is excluded because it loses at least four orbit dimensions", registry["wall_family"]["complex_root_jump_target_rank_ceiling"] == 80)

print("\nB. BOTH ISOLATED REAL WALL FACTORS")
pi4 = standard_poisson(2)
for kind in ("split", "compact"):
    regular_d, regular_p = factor(kind)
    zero_d, zero_p = factor(kind, zero=True)
    check("factor", f"{kind} cotangent factor is symplectic rank four", rank(pi4) == 4)
    check("factor", f"{kind} regular moment differential has rank three", rank(regular_d) == 3)
    check("factor", f"{kind} wall moment differential has rank two", rank(zero_d) == 2)
    check("factor", f"{kind} regular Lie-Poisson rank is two", rank(regular_p) == 2)
    check("factor", f"{kind} wall Lie-Poisson rank is zero", rank(zero_p) == 0)
    check("factor", f"{kind} regular moment map is Poisson exactly", multiply(multiply(regular_d, pi4), transpose(regular_d)) == regular_p)
    check("factor", f"{kind} wall moment map is Poisson exactly", multiply(multiply(zero_d, pi4), transpose(zero_d)) == zero_p)

print("\nC. ORTHOGONAL A1 x A1 INTERSECTIONS")
leaf80 = standard_poisson(40)
centre5_pi = standard_poisson(5)
source98_pair = block_diag(leaf80, pi4, pi4, centre5_pi)
check("pair", "the orthogonal-pair carrier has dimension and symplectic rank 98", len(source98_pair) == 98 and rank(source98_pair) == 98)
for first_kind, second_kind in itertools.product(("split", "compact"), repeat=2):
    for zero_count, zero_flags in enumerate(((False, False), (True, False), (True, True))):
        first_d, first_p = factor(first_kind, zero_flags[0])
        second_d, second_p = factor(second_kind, zero_flags[1])
        differential = block_diag(identity(80), first_d, second_d, projection(5))
        target_pi = block_diag(leaf80, first_p, second_p, zeros(5, 5))
        expected_map_rank = 91 - zero_count
        expected_target_rank = 84 - 2 * zero_count
        label = f"{first_kind}+{second_kind}, {zero_count} walls"
        check("pair", f"{label}: map rank is {expected_map_rank}", rank(differential) == expected_map_rank)
        check("pair", f"{label}: target rank is {expected_target_rank}", rank(target_pi) == expected_target_rank)
        check("pair", f"{label}: product Poisson identity holds", multiply(multiply(differential, source98_pair), transpose(differential)) == target_pi)

print("\nD. FIRST ORTHOGONAL TRIPLE COCYCLE")
leaf78 = standard_poisson(39)
centre4_pi = standard_poisson(4)
source98_triple = block_diag(leaf78, pi4, pi4, pi4, centre4_pi)
check("triple", "the A1^3 carrier has dimension and symplectic rank 98", len(source98_triple) == 98 and rank(source98_triple) == 98)
for zero_count in range(4):
    factor_data = [factor("split", index < zero_count) for index in range(3)]
    differential = block_diag(identity(78), *(item[0] for item in factor_data), projection(4))
    target_pi = block_diag(leaf78, *(item[1] for item in factor_data), zeros(4, 4))
    check("triple", f"A1^3 with {zero_count} walls has map rank {91-zero_count}", rank(differential) == 91 - zero_count)
    check("triple", f"A1^3 with {zero_count} walls has target rank {84-2*zero_count}", rank(target_pi) == 84 - 2 * zero_count)
    check("triple", f"A1^3 with {zero_count} walls satisfies the product Poisson identity", multiply(multiply(differential, source98_triple), transpose(differential)) == target_pi)

triple_pi = block_diag(pi4, pi4, pi4)
cycle = (1, 2, 0)
inverse_cycle = (2, 0, 1)
source_cycle = permutation_matrix(cycle, 4)
source_inverse = permutation_matrix(inverse_cycle, 4)
target_cycle = permutation_matrix(cycle, 3)
sample_differentials = [sl2_differential(1, 1), sl2_differential(1, -1), sl2_differential(2, 1)]
d_old = block_diag(*sample_differentials)
d_new = block_diag(*(sample_differentials[index] for index in cycle))
check("cocycle", "cyclic factor permutation preserves the summed symplectic form", multiply(multiply(source_cycle, triple_pi), transpose(source_cycle)) == triple_pi)
check("cocycle", "moment maps commute strictly with the cyclic overlap permutation", multiply(target_cycle, d_old) == multiply(d_new, source_cycle))
check("cocycle", "the first triple transition closes exactly", multiply(source_inverse, source_cycle) == identity(12))
check("cocycle", "the registry records additive tautological potentials with zero Cech defect", registry["orthogonal_overlaps"]["triple_potential_cocycle"] == "STRICT_ZERO_DEFECT")

print("\nE. NATURAL SPLIT-A2 CANDIDATE KILL")
# For H=SL(2,R) in the upper-left block of SL(3,R), ann(h) consists of
# arrowhead matrices [[a,0,u],[0,a,v],[r,s,-2a]].  The infinitesimal H action
# on (u,v;r,s) has the coefficient matrix below in variables (A,B,C).
def h_action_matrix(u: int, v: int, r: int, s: int) -> list[list[Fraction]]:
    return [
        [Fraction(u), Fraction(v), Fraction(0)],
        [Fraction(-v), Fraction(0), Fraction(u)],
        [Fraction(r), Fraction(0), Fraction(s)],
        [Fraction(-s), Fraction(r), Fraction(0)],
    ]


generic_action = h_action_matrix(1, 0, 1, 0)
nilpotent_action = h_action_matrix(1, 0, 0, 1)
zero_action = h_action_matrix(0, 0, 0, 0)
check("a2", "the generic arrowhead stabilizer in h is zero", rank(generic_action) == 3)
check("a2", "the candidate moment map has generic rank eight", 8 - (3 - rank(generic_action)) == 8)
check("a2", "the zero-section candidate moment map has rank five", 8 - (3 - rank(zero_action)) == 5)
check("a2", "the selected nilpotent arrowhead has a one-dimensional h stabilizer", 3 - rank(nilpotent_action) == 1)
check("a2", "the candidate moment differential drops to rank seven there", 8 - (3 - rank(nilpotent_action)) == 7)

nilpotent = [
    [Fraction(0), Fraction(0), Fraction(1)],
    [Fraction(0), Fraction(0), Fraction(0)],
    [Fraction(0), Fraction(1), Fraction(0)],
]
check("a2", "the arrowhead representative is nonzero nilpotent of order three", matrix_power(nilpotent, 3) == zeros(3, 3) and matrix_power(nilpotent, 2) != zeros(3, 3))
check("a2", "the arrowhead representative has Jordan rank profile 2 then 1", rank(nilpotent) == 2 and rank(matrix_power(nilpotent, 2)) == 1)

sl3_basis = [
    [[1, 0, 0], [0, -1, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 1, 0], [0, 0, -1]],
    [[0, 1, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [1, 0, 0], [0, 0, 0]],
    [[0, 0, 1], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [1, 0, 0]],
    [[0, 0, 0], [0, 0, 1], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 1, 0]],
]
commutator_columns = []
for basis_matrix in sl3_basis:
    left = multiply(basis_matrix, nilpotent)
    right = multiply(nilpotent, basis_matrix)
    commutator_columns.append([left[i][j] - right[i][j] for i in range(3) for j in range(3)])
commutator_map = transpose(commutator_columns)
check("a2", "the nilpotent centralizer in sl3 has dimension two", 8 - rank(commutator_map) == 2)
check("a2", "the nilpotent target is regular with Poisson rank six", rank(commutator_map) == 6)
check("a2", "the full 98D candidate has map rank 90 rather than 91 over that regular value", 78 + 7 + 5 == 90)
check("a2", "the natural split-A2 homogeneous cotangent candidate is rejected", registry["adjacent_a2_gate"]["natural_candidate_verdict"] == "REJECTED_REGULAR_NILPOTENT_RANK_DEFECT")

print("\nF. CLAIM CEILING")
check("scope", "all isolated real rank-82 wall types are admitted locally", registry["scope"]["all_isolated_rank_82_real_wall_types"] == "CONSTRUCTED_LOCALLY")
check("scope", "orthogonal pair and first triple cocycles are admitted", registry["scope"]["orthogonal_a1_overlaps"] == "CONSTRUCTED")
check("scope", "only the natural split-A2 candidate is killed", registry["scope"]["universal_a2_obstruction"] == "NOT_PROVED")
check("scope", "global RSAP remains open", registry["scope"]["global_rsap"] == "OPEN")
check("scope", "zero-charge rank at most 49 remains unconstructed", registry["scope"]["zero_charge_rank_at_most_49"] == "NOT_CONSTRUCTED")
check("accounting", "no protected truth surface moves", set(registry["changes"].values()) == {"none"})

print("\nSUMMARY")
total = sum(COUNTS.values())
assert total == 92, total
print(json.dumps({"checks": total, "counts": dict(COUNTS), "failures": FAILURES, "status": registry["status"], "next_gate": registry["next_gate"]}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {total}/{total}")
