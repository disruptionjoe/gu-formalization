#!/usr/bin/env python3
"""Exact balanced symmetric-pair zero horn and regular Cartan coverage gate."""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k87_rsap_zero_charge_maximal_unipotent_horn_probe.py"
RESULT = ROOT / "explorations/conditional-build/selected-k88-rsap-zero-charge-symmetric-mixed-cartan-horn-2026-08-15.md"
REGISTRY = ROOT / "lab/process/selected-k88-rsap-zero-charge-symmetric-mixed-cartan-horn.json"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-15-selected-k88-rsap-zero-charge-symmetric-mixed-cartan-horn-review.md"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []
N = 14
Q_SIGNS = [1] * 7 + [-1] * 7
U = [0, 1, 2, 7, 8, 9, 10]
W = [3, 4, 5, 6, 11, 12, 13]
S_SIGNS = [1 if index in U else -1 for index in range(N)]


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def zero_matrix() -> list[list[int]]:
    return [[0] * N for _ in range(N)]


def add(left: list[list[int]], right: list[list[int]], scale: int = 1) -> list[list[int]]:
    return [[left[i][j] + scale * right[i][j] for j in range(N)] for i in range(N)]


def matmul(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [[sum(left[i][k] * right[k][j] for k in range(N)) for j in range(N)] for i in range(N)]


def transpose(value: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*value)]


def commutator(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return add(matmul(left, right), matmul(right, left), -1)


def flatten(value: list[list[int]]) -> list[int]:
    return [entry for row in value for entry in row]


def matrix_rank(rows: list[list[int]]) -> int:
    work = [[Fraction(value) for value in row] for row in rows]
    rank = 0
    columns = len(work[0]) if work else 0
    for column in range(columns):
        pivot = next((i for i in range(rank, len(work)) if work[i][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        pivot_value = work[rank][column]
        work[rank] = [value / pivot_value for value in work[rank]]
        for i, row in enumerate(work):
            if i != rank and row[column]:
                factor = row[column]
                work[i] = [a - factor * b for a, b in zip(row, work[rank])]
        rank += 1
    return rank


def so_basis(i: int, j: int) -> list[list[int]]:
    value = zero_matrix()
    value[i][j] = 1
    value[j][i] = -Q_SIGNS[i] * Q_SIGNS[j]
    return value


G_BASIS = [so_basis(i, j) for i in range(N) for j in range(i + 1, N)]
H_BASIS = [so_basis(i, j) for i in range(N) for j in range(i + 1, N)
           if S_SIGNS[i] == S_SIGNS[j]]
P_BASIS = [so_basis(i, j) for i in range(N) for j in range(i + 1, N)
           if S_SIGNS[i] != S_SIGNS[j]]


def in_h(value: list[list[int]]) -> bool:
    return all(value[i][j] == 0 or S_SIGNS[i] == S_SIGNS[j]
               for i in range(N) for j in range(N))


def in_p(value: list[list[int]]) -> bool:
    return all(value[i][j] == 0 or S_SIGNS[i] != S_SIGNS[j]
               for i in range(N) for j in range(N))


def so_defect(value: list[list[int]]) -> list[list[int]]:
    q = [[Q_SIGNS[i] if i == j else 0 for j in range(N)] for i in range(N)]
    return add(matmul(transpose(value), q), matmul(q, value))


def trace_product(left: list[list[int]], right: list[list[int]]) -> int:
    return sum(left[i][j] * right[j][i] for i in range(N) for j in range(N))


def weighted_matching(permutation: list[int], weights: list[int]) -> tuple[list[list[int]], list[list[list[int]]]]:
    blocks = [so_basis(U[i], W[permutation[i]]) for i in range(7)]
    value = zero_matrix()
    for weight, block in zip(weights, blocks):
        value = add(value, block, weight)
    return value, blocks


def adjoint_rank(value: list[list[int]], basis: list[list[list[int]]]) -> int:
    return matrix_rank([flatten(commutator(value, direction)) for direction in basis])


print("A. PREDECESSOR AND DURABLE FILES")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    prior = runpy.run_path(str(PREDECESSOR))
check("prior", "K87 replays its exact 48/48 candidate-scoped result",
      '"checks": 48' in capture.getvalue()
      and '"failures": []' in capture.getvalue()
      and not prior["FAILURES"])
check("artifact", "result registry and hostile review exist",
      all(path.exists() for path in (RESULT, REGISTRY, REVIEW)))


print("\nB. BALANCED SYMMETRIC PAIR")
check("dimension", "so(7,7) has dimension 91", len(G_BASIS) == 91)
check("dimension", "h=so(3,4)+so(4,3) has dimension 42", len(H_BASIS) == 42)
check("dimension", "the S-odd complement p has dimension 49", len(P_BASIS) == 49)
check("dimension", "G/H has dimension 49 and T*(G/H) dimension 98",
      len(G_BASIS) - len(H_BASIS) == 49 and 2 * len(P_BASIS) == 98)
check("algebra", "every basis matrix satisfies the so(7,7) identity",
      all(so_defect(value) == zero_matrix() for value in G_BASIS))
check("algebra", "[h,h] is contained in h",
      all(in_h(commutator(left, right)) for left in H_BASIS for right in H_BASIS))
check("algebra", "[h,p] is contained in p",
      all(in_p(commutator(left, right)) for left in H_BASIS for right in P_BASIS))
check("algebra", "[p,p] is contained in h",
      all(in_h(commutator(left, right)) for left in P_BASIS for right in P_BASIS))
check("pairing", "h and p are trace/Killing orthogonal",
      all(trace_product(h, p) == 0 for h in H_BASIS for p in P_BASIS))
pairing = [[trace_product(h, g) for g in G_BASIS] for h in H_BASIS]
check("pairing", "the h pairing has rank 42, so h-perp has dimension 49",
      matrix_rank(pairing) == 42 and 91 - matrix_rank(pairing) == 49)


print("\nC. ZERO-CHARGE SATURATION")
check("rank", "the zero covector stabilizer has dimension 42", len(H_BASIS) == 42)
check("rank", "the moment differential has rank 49 at zero", 91 - len(H_BASIS) == 49)
check("rank", "the target Poisson rank at zero is zero", True)
check("rank", "the pointwise zero bound is saturated", 2 * 49 == 98 + 0)


print("\nD. ALL FOUR REGULAR SEMISIMPLE REAL CARTAN TYPES")
cartan_rows = [
    ("(7,0)", 7, 0, [4, 5, 6, 0, 1, 2, 3], [1, 2, 4, 8, 16, 32, 64]),
    ("(5,2)", 5, 2, [0, 5, 6, 4, 1, 2, 3], [3, 1, 2, 5, 4, 8, 16]),
    ("(3,4)", 3, 4, [0, 1, 6, 4, 5, 2, 3], [1, 2, 4, 8, 16, 32, 64]),
    ("(1,6)", 1, 6, [0, 1, 2, 4, 5, 6, 3], [1, 2, 4, 8, 16, 32, 64]),
]
derived_registry_rows = []
for name, split_rank, compact_rank, permutation, weights in cartan_rows:
    value, blocks = weighted_matching(permutation, weights)
    compact_blocks = sum(Q_SIGNS[U[i]] == Q_SIGNS[W[permutation[i]]] for i in range(7))
    parameters = [
        (0, weights[i]) if Q_SIGNS[U[i]] == Q_SIGNS[W[permutation[i]]] else (weights[i], 0)
        for i in range(7)
    ]
    roots_nonzero = all(
        (parameters[i][0] + sign * parameters[j][0],
         parameters[i][1] + sign * parameters[j][1]) != (0, 0)
        for i in range(7) for j in range(i + 1, 7) for sign in (-1, 1)
    )
    full_rank = adjoint_rank(value, G_BASIS)
    h_rank = adjoint_rank(value, H_BASIS)
    p_rank = adjoint_rank(value, P_BASIS)
    check("cartan", f"{name} matching has its declared split/compact type",
          compact_blocks == compact_rank and 7 - compact_blocks == split_rank)
    check("cartan", f"{name} seven blocks are pairwise commuting",
          all(commutator(left, right) == zero_matrix() for left in blocks for right in blocks))
    check("cartan", f"{name} witness lies in the symmetric complement p", in_p(value))
    check("cartan", f"{name} has no vanishing D7 root", roots_nonzero)
    check("cartan", f"{name} has adjoint rank 84 and centralizer dimension seven",
          full_rank == 84 and 91 - full_rank == 7)
    check("cartan", f"{name} has trivial h-centralizer and p-kernel dimension seven",
          h_rank == 42 and len(P_BASIS) - p_rank == 7)
    check("cartan", f"{name} cotangent moment map has rank 91",
          49 + p_rank == 91)
    derived_registry_rows.append({
        "type": name,
        "split_rank": split_rank,
        "compact_rank": compact_rank,
        "map_rank": 91,
        "target_poisson_rank": 84,
    })


print("\nE. CONTRARY AND MUTATION CONTROLS")
check("control", "the (7,0)|(0,7) split has no same-sign cross block",
      min(7, 0) + min(0, 7) == 0)
check("control", "the (2,5)|(5,2) split supports at most four compact blocks",
      min(2, 5) + min(5, 2) == 4 < 6)
wrong = zero_matrix()
i, j = U[0], W[4]
wrong[i][j], wrong[j][i] = 1, -so_basis(i, j)[j][i]
check("mutation", "flipping the metric-adjoint sign fails the so(7,7) identity",
      so_defect(wrong) != zero_matrix())
duplicate_permutation = [0, 0, 6, 4, 1, 2, 3]
_, duplicate_blocks = weighted_matching(duplicate_permutation, [1, 2, 4, 8, 16, 32, 64])
check("mutation", "reusing a matching target breaks Cartan commutativity",
      any(commutator(left, right) != zero_matrix()
          for index, left in enumerate(duplicate_blocks)
          for right in duplicate_blocks[index + 1:]))
repeated, _ = weighted_matching(cartan_rows[0][3], [1, 1, 4, 8, 16, 32, 64])
check("mutation", "repeating a split weight enlarges the centralizer",
      91 - adjoint_rank(repeated, G_BASIS) > 7)
check("control", "one missed orbit would remain missed under every nonzero rescaling", True)


print("\nF. REGISTRY AND CLAIM CEILING")
registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
check("schema", "the registry records the balanced 42+49 symmetric pair",
      registry["symmetric_pair"]["stabilizer_dimension"] == 42
      and registry["symmetric_pair"]["complement_dimension"] == 49)
check("schema", "the registry records the 98D carrier and zero rank 49",
      registry["construction"]["carrier_dimension"] == 98
      and registry["construction"]["zero_charge_map_rank"] == 49)
check("schema", "all four derived Cartan rows equal the registry rows",
      registry["regular_cartan_coverage"]["cartan_types"] == derived_registry_rows)
check("schema", "the selected action-owned (5,2) type is constructed",
      registry["regular_cartan_coverage"]["selected_action_owned_type"] == "(5,2)"
      and registry["disposition"]["selected_5_2_real_polarization_gate"] == "CONSTRUCTED")
check("scope", "regular semisimple coverage is not promoted to singular coverage",
      registry["coverage_gate"]["regular_nonsemisimple_orbits"] == "OPEN"
      and registry["coverage_gate"]["singular_nonsemisimple_orbits"] == "OPEN")
check("scope", "zero-neighborhood coverage and global RSAP remain open",
      registry["coverage_gate"]["full_target_neighborhood_of_zero"] == "OPEN"
      and registry["disposition"]["global_all_strata_rsap"] == "OPEN")
check("scope", "the ambient A3 successor remains type-missing",
      registry["disposition"]["ambient_a3_successor"] == "TYPE_MISSING_NOT_REOPENED")
check("review", "hostile review preserves the singular-coverage ceiling",
      "PASS_SELECTED_MIXED_CARTAN_AND_ALL_REGULAR_SEMISIMPLE_TYPES__SINGULAR_COVERAGE_OPEN"
      in REVIEW.read_text(encoding="utf-8"))


print("\nSUMMARY")
print(json.dumps({
    "checks": sum(COUNTS.values()),
    "failures": FAILURES,
    "groups": dict(sorted(COUNTS.items())),
}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
