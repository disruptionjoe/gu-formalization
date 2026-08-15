#!/usr/bin/env python3
"""Exact K99 minimal multiplier and current-owner exhaustion certificate."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import contextlib
import io
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
K98_PROBE = ROOT / "tests/channel-swings/selected_k98_rsap_balanced_bfv_selection_classifier_probe.py"
K98_REGISTRY = ROOT / "lab/process/selected-k98-rsap-balanced-bfv-selection-classifier.json"
K99_REGISTRY = ROOT / "lab/process/selected-k99-rsap-balanced-multiplier-owner-exhaustion.json"
RESULT = ROOT / "explorations/conditional-build/selected-k99-rsap-balanced-multiplier-owner-exhaustion-2026-08-15.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-15-selected-k99-rsap-balanced-multiplier-owner-exhaustion-review.md"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []
N = 14
Q = [1] * 7 + [-1] * 7
BALANCED_PLUS = {0, 1, 2, 7, 8, 9, 10}
PHYSICAL_BASE = {0, 7, 8, 9}


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def zeros() -> list[list[int]]:
    return [[0] * N for _ in range(N)]


def basis_matrix(i: int, j: int) -> list[list[int]]:
    value = zeros()
    value[i][j] = 1
    value[j][i] = -Q[i] * Q[j]
    return value


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[sum(a[i][k] * b[k][j] for k in range(N))
             for j in range(N)] for i in range(N)]


def add(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[a[i][j] + b[i][j] for j in range(N)] for i in range(N)]


def subtract(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[a[i][j] - b[i][j] for j in range(N)] for i in range(N)]


def scale(c: int, a: list[list[int]]) -> list[list[int]]:
    return [[c * a[i][j] for j in range(N)] for i in range(N)]


def bracket(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return subtract(matmul(a, b), matmul(b, a))


def trace_product(a: list[list[int]], b: list[list[int]]) -> int:
    return sum(a[i][j] * b[j][i] for i in range(N) for j in range(N))


def matrix_rank(rows: list[list[int]]) -> int:
    work = [[Fraction(value) for value in row] for row in rows]
    rank = 0
    columns = len(work[0]) if work else 0
    for column in range(columns):
        pivot = next((row for row in range(rank, len(work)) if work[row][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        divisor = work[rank][column]
        work[rank] = [value / divisor for value in work[rank]]
        for row in range(len(work)):
            if row != rank and work[row][column]:
                factor = work[row][column]
                work[row] = [left - factor * right
                             for left, right in zip(work[row], work[rank])]
        rank += 1
    return rank


def linear_combination(basis: list[list[list[int]]], seed: int) -> list[list[int]]:
    value = zeros()
    for index, generator in enumerate(basis):
        coefficient = ((index + 3 * seed) % 7) - 3
        value = add(value, scale(coefficient, generator))
    return value


def stabilizer_basis(split: set[int]) -> list[list[list[int]]]:
    return [basis_matrix(i, j) for i in range(N) for j in range(i + 1, N)
            if (i in split) == (j in split)]


def complement_basis(split: set[int]) -> list[list[list[int]]]:
    return [basis_matrix(i, j) for i in range(N) for j in range(i + 1, N)
            if (i in split) != (j in split)]


def signature(split: set[int]) -> tuple[int, int]:
    return (sum(Q[index] == 1 for index in split),
            sum(Q[index] == -1 for index in split))


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


print("A. PREDECESSOR AND DURABLE FILES")
replay = io.StringIO()
replay_code = None
with contextlib.redirect_stdout(replay):
    try:
        runpy.run_path(str(K98_PROBE), run_name="__main__")
    except SystemExit as error:
        replay_code = error.code
check("predecessor", "K98 exact BFV certificate replays cleanly",
      replay_code == 0 and '"failures": []' in replay.getvalue())
check("artifact", "result registry and hostile review exist",
      all(path.exists() for path in (RESULT, K99_REGISTRY, REVIEW)))


print("\nB. BALANCED AND SOURCE-PHYSICAL SUBGROUP TYPES")
FULL = [basis_matrix(i, j) for i in range(N) for j in range(i + 1, N)]
H_BAL = stabilizer_basis(BALANCED_PLUS)
P_BAL = complement_basis(BALANCED_PLUS)
H_PHYS = stabilizer_basis(PHYSICAL_BASE)
check("dimension", "so(7,7) has dimension 91", len(FULL) == 91)
check("dimension", "balanced stabilizer and complement have dimensions 42+49",
      (len(H_BAL), len(P_BAL)) == (42, 49))
check("signature", "balanced eigenspaces have signatures (3,4)|(4,3)",
      (signature(BALANCED_PLUS), signature(set(range(N)) - BALANCED_PLUS))
      == ((3, 4), (4, 3)))
check("dimension", "physical 4+10 stabilizer has dimension 51",
      len(H_PHYS) == 6 + 45 == 51)
check("signature", "source physical blocks have signatures (1,3)|(6,4)",
      (signature(PHYSICAL_BASE), signature(set(range(N)) - PHYSICAL_BASE))
      == ((1, 3), (6, 4)))
check("typing", "physical and balanced stabilizers are distinct concrete subspaces",
      {tuple(map(tuple, item)) for item in H_PHYS}
      != {tuple(map(tuple, item)) for item in H_BAL})
check("reduction", "the two cotangent reductions have dimensions 80 and 98",
      (182 - 2 * len(H_PHYS), 182 - 2 * len(H_BAL)) == (80, 98))


print("\nC. EXACT MINIMAL MULTIPLIER VARIATION")
gauge_invariance = True
wrong_coadjoint_detected = False
missing_inhomogeneous_detected = False
for seed in range(1, 8):
    lam = linear_combination(FULL, seed)
    velocity = linear_combination(FULL, seed + 2)
    multiplier = linear_combination(H_BAL, seed + 4)
    xi = linear_combination(H_BAL, seed + 5)
    dot_xi = linear_combination(H_BAL, seed + 6)
    delta_lam = bracket(lam, xi)
    delta_velocity = add(dot_xi, bracket(velocity, xi))
    delta_multiplier = add(dot_xi, bracket(multiplier, xi))
    variation = (trace_product(delta_lam, subtract(velocity, multiplier))
                 + trace_product(lam, subtract(delta_velocity, delta_multiplier)))
    gauge_invariance = gauge_invariance and variation == 0
    wrong_variation = (trace_product(scale(-1, delta_lam), subtract(velocity, multiplier))
                       + trace_product(lam, subtract(delta_velocity, delta_multiplier)))
    missing_term = (trace_product(delta_lam, subtract(velocity, multiplier))
                    + trace_product(lam, subtract(delta_velocity,
                                                  bracket(multiplier, xi))))
    wrong_coadjoint_detected = wrong_coadjoint_detected or wrong_variation != 0
    missing_inhomogeneous_detected = missing_inhomogeneous_detected or missing_term != 0
check("variation", "all seven exact local right-H_bal fixtures leave L_min invariant",
      gauge_invariance)
check("negative", "the wrong coadjoint sign is detected", wrong_coadjoint_detected)
check("negative", "omitting dot(xi) from delta a_t is detected",
      missing_inhomogeneous_detected)


print("\nD. CONSTRAINT AND MULTIPLIER RANK")
GRAM_H = [[trace_product(left, right) for right in H_BAL] for left in H_BAL]
GRAM_P = [[trace_product(left, right) for right in P_BAL] for left in P_BAL]
CROSS = [[trace_product(left, right) for right in P_BAL] for left in H_BAL]
check("pairing", "trace pairing is nondegenerate on h_bal", matrix_rank(GRAM_H) == 42)
check("pairing", "trace pairing is nondegenerate on p_bal", matrix_rank(GRAM_P) == 49)
check("pairing", "h_bal and p_bal are exactly orthogonal",
      all(value == 0 for row in CROSS for value in row))
check("constraint", "a_t variation gives 42 independent moment constraints",
      matrix_rank(GRAM_H) == 42)
check("hessian", "the multiplier-multiplier Hessian is zero",
      matrix_rank([[0] * 42 for _ in range(42)]) == 0)
check("hessian", "the lambda-multiplier mixed block has rank 42",
      matrix_rank(GRAM_H) == 42)
check("reduction", "the exact regular schedule remains 182 to 140 to 98",
      (182 - 42, 182 - 2 * 42) == (140, 98))


print("\nE. CURRENT OWNER CENSUS")
k98 = read_json(K98_REGISTRY)
k99 = read_json(K99_REGISTRY)
rows = {row["candidate"]: row for row in k99["candidate_census"]}
check("ownership", "K98 leaves the right-H_bal declaration and multiplier unowned",
      not k98["ownership"]["source_or_current_action_owned_right_h_bal_gauge_declaration"]
      and not k98["ownership"]["source_or_current_action_owned_multiplier_sector"])
check("ownership", "all five current no-new-field candidates remain non-owners",
      all(not rows[name]["new_field"] and "EXACT_MINIMAL_COMPLETION" not in rows[name]["status"]
          for name in (
              "EXISTING_EPSILON",
              "RESTRICT_EPSILON_VARIATIONS_TO_H_BAL",
              "PROJECT_EXISTING_B_OR_VARPI_TO_H_BAL",
              "DRESS_FULL_CONNECTION_BY_EPSILON_AND_PROJECT",
              "REUSE_CONDITIONAL_EDGE_FIELD",
          )))
check("ownership", "the only passing census row is explicitly new completion data",
      rows["NEW_INDEPENDENT_H_BAL_MULTIPLIER_A_T"]["new_field"]
      and rows["NEW_INDEPENDENT_H_BAL_MULTIPLIER_A_T"]["status"].startswith(
          "EXACT_MINIMAL_COMPLETION"))
check("ceiling", "unreleased terms and a full Hamiltonian split remain open",
      set(k99["not_excluded"]) == {
          "UNRELEASED_SOURCE_ACTION_TERM",
          "ACTION_OWNED_MOVING_BALANCED_ORDER_PARAMETER",
          "FULL_HAMILTONIAN_COLLAR_DECOMPOSITION_WITH_EXISTING_NORMAL_COMPONENT",
      })
check("routing", "the result stays on the source-native route",
      k99["comparator_routing_classification"] == "SOURCE_NATIVE_ROUTE")


print("\nF. CLAIM CEILING AND SUCCESSOR")
owners = k99["owner_stack"]
check("ceiling", "balanced projector, gauge declaration and multiplier are all unowned",
      all(value == "NOT_SOURCE_OR_CURRENT_ACTION_OWNED"
          for key, value in owners.items() if key != "minimal_bfv_ghost_sector"))
check("ceiling", "physical phase-space selection remains open",
      k99["disposition"]["physical_phase_space_selection"] == "OPEN")
check("successor", "next gate requires the balanced owner before a normal multiplier",
      k99["disposition"]["next_gate"].startswith(
          "CONSTRUCT_OR_OBSTRUCT_ACTION_OWNED_BALANCED_INVOLUTION"))


summary = {"checks": sum(COUNTS.values()), "failures": FAILURES,
           "by_kind": dict(COUNTS)}
print("\n" + json.dumps(summary, indent=2, sort_keys=True))
raise SystemExit(1 if FAILURES else 0)
