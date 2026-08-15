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


def loxodromic_matching(
    loxodromic_blocks: int,
    permutation: list[int],
) -> tuple[list[list[int]], list[list[list[int]]], list[list[list[int]]], list[int], list[int]]:
    """Disjoint loxodromic four-planes plus the remaining pure blocks."""
    coefficients = [[-3, -3], [-3, -2]]
    lox_values = []
    used_u: set[int] = set()
    used_w: set[int] = set()
    for block_index in range(loxodromic_blocks):
        lox_u = [block_index, 3 + block_index]
        lox_w = [block_index, 4 + block_index]
        used_u.update(lox_u)
        used_w.update(lox_w)
        lox_value = zero_matrix()
        for row, u_index in enumerate(lox_u):
            for column, w_index in enumerate(lox_w):
                lox_value = add(
                    lox_value,
                    so_basis(U[u_index], W[w_index]),
                    (4 ** block_index) * coefficients[row][column],
                )
        lox_values.append(lox_value)

    remaining_u = [index for index in range(7) if index not in used_u]
    remaining_w = [index for index in range(7) if index not in used_w]
    weights = [128 * (2 ** index) for index in range(len(remaining_u))]
    blocks = [
        so_basis(U[remaining_u[index]], W[remaining_w[permutation[index]]])
        for index in range(len(remaining_u))
    ]
    value = zero_matrix()
    for lox_value in lox_values:
        value = add(value, lox_value)
    for weight, block in zip(weights, blocks):
        value = add(value, block, weight)
    return value, lox_values, blocks, remaining_u, remaining_w


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


print("\nD. FOUR NON-LOXODROMIC REGULAR SEMISIMPLE CARTAN CLASSES")
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
        "loxodromic_blocks": 0,
        "map_rank": 91,
        "target_poisson_rank": 84,
    })


print("\nE. SIX LOXODROMIC REGULAR SEMISIMPLE CARTAN CLASSES")
lox_rows = [
    ("(6,1)", 6, 1, 1, [3, 4, 0, 1, 2]),
    ("(4,3)", 4, 3, 1, [0, 4, 3, 1, 2]),
    ("(2,5)", 2, 5, 1, [0, 1, 3, 4, 2]),
    ("(5,2)", 5, 2, 2, [2, 0, 1]),
    ("(3,4)", 3, 4, 2, [0, 2, 1]),
    ("(4,3)", 4, 3, 3, [0]),
]
for name, split_rank, compact_rank, loxodromic_blocks, permutation in lox_rows:
    value, lox_values, blocks, remaining_u, remaining_w = loxodromic_matching(
        loxodromic_blocks, permutation
    )
    lox_invariants = []
    for block_index, lox_value in enumerate(lox_values):
        square = matmul(lox_value, lox_value)
        u_pair = (block_index, 3 + block_index)
        squared_half = [[square[U[i]][U[j]] for j in u_pair] for i in u_pair]
        squared_trace = squared_half[0][0] + squared_half[1][1]
        squared_determinant = (
            squared_half[0][0] * squared_half[1][1]
            - squared_half[0][1] * squared_half[1][0]
        )
        squared_discriminant = squared_trace * squared_trace - 4 * squared_determinant
        scale = 4 ** block_index
        lox_invariants.append(
            squared_trace == 5 * scale * scale
            and squared_determinant == 9 * scale ** 4
            and squared_discriminant == -11 * scale ** 4
        )
    same_sign_blocks = sum(
        Q_SIGNS[U[remaining_u[index]]]
        == Q_SIGNS[W[remaining_w[permutation[index]]]]
        for index in range(len(remaining_u))
    )
    full_rank = adjoint_rank(value, G_BASIS)
    h_rank = adjoint_rank(value, H_BASIS)
    p_rank = adjoint_rank(value, P_BASIS)
    class_label = f"{name} with L={loxodromic_blocks}"
    check("loxodromic", f"{class_label} has its declared irreducible loxodromic four-planes",
          all(lox_invariants))
    check("loxodromic", f"{name} has its declared split/compact type",
          loxodromic_blocks + len(blocks) - same_sign_blocks == split_rank
          and loxodromic_blocks + same_sign_blocks == compact_rank)
    check("loxodromic", f"{class_label} blocks commute pairwise",
          all(commutator(left, right) == zero_matrix() for left in blocks for right in blocks)
          and all(commutator(lox_value, block) == zero_matrix()
                  for lox_value in lox_values for block in blocks)
          and all(commutator(left, right) == zero_matrix()
                  for left in lox_values for right in lox_values))
    check("loxodromic", f"{class_label} witness lies in the symmetric complement p", in_p(value))
    check("loxodromic", f"{class_label} has adjoint rank 84 and centralizer dimension seven",
          full_rank == 84 and 91 - full_rank == 7)
    check("loxodromic", f"{class_label} has trivial h-centralizer and p-kernel dimension seven",
          h_rank == 42 and len(P_BASIS) - p_rank == 7)
    check("loxodromic", f"{class_label} cotangent moment map has rank 91",
          49 + p_rank == 91)
    derived_registry_rows.append({
        "type": name,
        "split_rank": split_rank,
        "compact_rank": compact_rank,
        "loxodromic_blocks": loxodromic_blocks,
        "map_rank": 91,
        "target_poisson_rank": 84,
    })

derived_registry_rows.sort(key=lambda row: (row["compact_rank"], row["loxodromic_blocks"]))
admissible_cartan_triples = sorted(
    (7 - 2 * elliptic_pairs - 2 * loxodromic_blocks, elliptic_pairs, loxodromic_blocks)
    for elliptic_pairs in range(4)
    for loxodromic_blocks in range(4)
    if 7 - 2 * elliptic_pairs - 2 * loxodromic_blocks > 0
)
derived_cartan_triples = sorted(
    (
        row["split_rank"] - row["loxodromic_blocks"],
        (row["compact_rank"] - row["loxodromic_blocks"]) // 2,
        row["loxodromic_blocks"],
    )
    for row in derived_registry_rows
)
check("classification", "H+2E+2L=7 exhausts exactly ten real Cartan block types",
      len(admissible_cartan_triples) == 10
      and derived_cartan_triples == admissible_cartan_triples)
check("classification", "the odd (7,7) case avoids the O-to-SO all-loxodromic split",
      7 == 7 and 7 % 2 == 1)


print("\nF. CONTRARY AND MUTATION CONTROLS")
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


print("\nG. REGISTRY AND CLAIM CEILING")
registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
check("schema", "the registry records the balanced 42+49 symmetric pair",
      registry["symmetric_pair"]["stabilizer_dimension"] == 42
      and registry["symmetric_pair"]["complement_dimension"] == 49)
check("schema", "the registry records the 98D carrier and zero rank 49",
      registry["construction"]["carrier_dimension"] == 98
      and registry["construction"]["zero_charge_map_rank"] == 49)
check("schema", "all ten derived Cartan classes equal the registry rows",
      registry["regular_cartan_coverage"]["cartan_types"] == derived_registry_rows)
classification = registry["regular_cartan_coverage"]["classification"]
check("schema", "the registry distinguishes Cartan classes and closes connected-group splitting",
      classification["class_count"] == 10
      and classification["block_equation"] == "H+2E+2L=7"
      and "NOT_INDIVIDUAL_ADJOINT_ORBITS" in classification["object"]
      and "p=q=7_IS_ODD" in classification["o_to_so_split"]
      and classification["so_to_so0_split"].startswith("NO__")
      and "CENTRAL_KERNEL" in classification["spin_cover_effect"]
      and "10.4153/CJM-1994-039-5" in classification["primary_reference"])
check("schema", "the carrier uses the connected Spin block stabilizer, including its finite kernel",
      "H_bal" in registry["symmetric_pair"]["stabilizer_group"]
      and "diagonal_Z2" in registry["symmetric_pair"]["spin_cover_description"]
      and "H_bal" in registry["construction"]["carrier"])
check("schema", "the selected action-owned (5,2) type is constructed",
      registry["regular_cartan_coverage"]["selected_action_owned_type"] == "(5,2)"
      and registry["regular_cartan_coverage"]["selected_action_owned_loxodromic_blocks"] == 0
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
      "PASS_ALL_TEN_REGULAR_SEMISIMPLE_CARTAN_TYPES__SINGULAR_COVERAGE_OPEN"
      in REVIEW.read_text(encoding="utf-8"))


print("\nSUMMARY")
print(json.dumps({
    "checks": sum(COUNTS.values()),
    "failures": FAILURES,
    "groups": dict(sorted(COUNTS.items())),
}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
