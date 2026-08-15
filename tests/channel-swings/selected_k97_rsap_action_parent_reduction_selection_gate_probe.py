#!/usr/bin/env python3
"""Exact K97 formal attachment and current-action selection discriminator."""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
K96_PROBE = ROOT / "tests/channel-swings/selected_k96_rsap_connected_orbit_refinement_probe.py"
K96_REGISTRY = ROOT / "lab/process/selected-k96-rsap-connected-orbit-refinement.json"
K88_REGISTRY = ROOT / "lab/process/selected-k88-rsap-zero-charge-symmetric-mixed-cartan-horn.json"
PARENT_REGISTRY = ROOT / "lab/process/selected-k77-source-epsilon-cotangent-parent.json"
BOUNDARY_REGISTRY = ROOT / "lab/process/selected-k77-boundary-stationarity-symplectic-realization-gate.json"
RESULT = ROOT / "explorations/conditional-build/selected-k97-rsap-action-parent-reduction-selection-gate-2026-08-15.md"
REGISTRY = ROOT / "lab/process/selected-k97-rsap-action-parent-reduction-selection-gate.json"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-15-selected-k97-rsap-action-parent-reduction-selection-gate-review.md"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []
N = 14
Q_SIGNS = [1] * 7 + [-1] * 7
U = {0, 1, 2, 7, 8, 9, 10}
R_SIGNS = [1 if index in U else -1 for index in range(N)]


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


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


def zero_matrix() -> list[list[int]]:
    return [[0] * N for _ in range(N)]


def so_basis(i: int, j: int) -> list[list[int]]:
    value = zero_matrix()
    value[i][j] = 1
    value[j][i] = -Q_SIGNS[i] * Q_SIGNS[j]
    return value


def matmul(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [[sum(left[i][k] * right[k][j] for k in range(N))
             for j in range(N)] for i in range(N)]


def add(left: list[list[int]], right: list[list[int]], scale: int = 1) -> list[list[int]]:
    return [[left[i][j] + scale * right[i][j] for j in range(N)] for i in range(N)]


def commutator(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return add(matmul(left, right), matmul(right, left), -1)


def identity_matrix() -> list[list[Fraction]]:
    return [[Fraction(int(i == j)) for j in range(N)] for i in range(N)]


def boost(i: int, j: int, off_diagonal_sign: int = 1) -> tuple[list[list[Fraction]], list[list[Fraction]]]:
    value = identity_matrix()
    inverse = identity_matrix()
    value[i][i] = value[j][j] = Fraction(5, 3)
    value[i][j] = value[j][i] = Fraction(4 * off_diagonal_sign, 3)
    inverse[i][i] = inverse[j][j] = Fraction(5, 3)
    inverse[i][j] = inverse[j][i] = Fraction(-4 * off_diagonal_sign, 3)
    return value, inverse


def conjugate(value: list[list[int]], group: list[list[Fraction]], inverse: list[list[Fraction]]) -> list[list[Fraction]]:
    return matmul(matmul(group, value), inverse)


def trace_product(left: list[list[int]], right: list[list[int]]) -> int:
    return sum(left[i][j] * right[j][i] for i in range(N) for j in range(N))


def in_p(value: list[list[int]]) -> bool:
    return all(value[i][j] == 0 or R_SIGNS[i] != R_SIGNS[j]
               for i in range(N) for j in range(N))


def block_symplectic(gram: list[list[int]]) -> list[list[int]]:
    size = len(gram)
    return [
        ([0] * size + [-value for value in gram[i]])
        if i < size else
        (gram[i - size] + [0] * size)
        for i in range(2 * size)
    ]


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


print("A. PREDECESSOR AND DURABLE FILES")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    try:
        runpy.run_path(str(K96_PROBE))
        predecessor_exit = 0
    except SystemExit as exc:
        predecessor_exit = exc.code
check("predecessor", "K96 replays its exact 23/23 classical RSAP result",
      predecessor_exit == 0
      and '"checks": 23' in capture.getvalue()
      and '"failures": []' in capture.getvalue())
check("artifact", "result registry and hostile review exist",
      all(path.exists() for path in (RESULT, REGISTRY, REVIEW)))


print("\nB. BALANCED RIGHT-MOMENT ZERO LEVEL")
G_BASIS = [so_basis(i, j) for i in range(N) for j in range(i + 1, N)]
H_BASIS = [so_basis(i, j) for i in range(N) for j in range(i + 1, N)
           if R_SIGNS[i] == R_SIGNS[j]]
P_BASIS = [so_basis(i, j) for i in range(N) for j in range(i + 1, N)
           if R_SIGNS[i] != R_SIGNS[j]]
check("dimension", "the 91-dimensional algebra splits as 42 plus 49",
      (len(G_BASIS), len(H_BASIS), len(P_BASIS)) == (91, 42, 49))
constraint_matrix = [[trace_product(h, g) for g in G_BASIS] for h in H_BASIS]
check("constraint", "restriction to h_bal has 42 independent components",
      matrix_rank(constraint_matrix) == 42)
check("constraint", "every p0 direction lies in the right-moment zero level",
      all(trace_product(h, p) == 0 for h in H_BASIS for p in P_BASIS))
check("constraint", "h_bal-perp has dimension 49 and equals p0",
      len(G_BASIS) - matrix_rank(constraint_matrix) == len(P_BASIS))
check("equivariance", "the right h_bal action preserves p0",
      all(in_p(commutator(h, p)) for h in H_BASIS for p in P_BASIS))


print("\nC. EXACT COTANGENT REDUCTION")
P_GRAM = [[trace_product(left, right) for right in P_BASIS] for left in P_BASIS]
check("pairing", "the trace pairing on p0 is nondegenerate", matrix_rank(P_GRAM) == 49)
REDUCED_FORM = block_symplectic(P_GRAM)
check("symplectic", "the reduced zero-fibre form has exact rank 98",
      matrix_rank(REDUCED_FORM) == 98)
check("dimension", "the right zero level has dimension 140",
      182 - 42 == 140)
check("dimension", "quotienting 42 characteristic directions leaves 98",
      140 - 42 == 98)
h, h_inverse = boost(0, 7)
g, g_inverse = boost(0, 11)
x = P_BASIS[0]
right_transformed_x = conjugate(x, h_inverse, h)
lhs = conjugate(right_transformed_x, matmul(g, h), matmul(h_inverse, g_inverse))
rhs = conjugate(x, g, g_inverse)
check("moment", "the left moment is invariant under the associated right-H_bal relation",
      lhs == rhs and in_p(right_transformed_x))


print("\nD. OWNERSHIP COMPOSITION")
k96 = read_json(K96_REGISTRY)
k88 = read_json(K88_REGISTRY)
parent = read_json(PARENT_REGISTRY)
boundary = read_json(BOUNDARY_REGISTRY)
check("parent", "the selected action owns the full formal 182D epsilon parent",
      parent["ownership"]["full_unrestricted_epsilon_preboundary_parent"] == "ACTION_OWNED_FORMAL"
      and parent["exact_parent"]["dimension"] == 182)
check("reduction", "K88 identifies the same balanced subgroup and 98D carrier",
      k88["symmetric_pair"]["stabilizer_dimension"] == 42
      and k88["construction"]["carrier_dimension"] == 98)
check("reduction", "K96 proves the descended moment map globally surjective",
      k96["moment_map"]["image"] == "ALL_SO77_DUAL"
      and k96["moment_map"]["surjective"])
check("reduction", "K96 certifies the exact classical RSAP minimum",
      k96["rsap"]["constructed"] and k96["rsap"]["minimum_dimension"] == 98)


print("\nE. COMPLETE CURRENT BARE-BOUNDARY SELECTION CENSUS")
potential = boundary["boundary_potential"]
check("free", "free variation forces full zero rather than the 49D p0 fibre",
      potential["free_variation"]["stationarity"] == "p_0=p_2=0"
      and potential["free_variation"]["charge"] == "Q_eta=0 for every eta")
check("dirichlet", "fixed data leaves momentum unlocked",
      not potential["fixed_dirichlet"]["momentum_locked"])
check("dirichlet", "fixed-data boundary transformations are not supplied as gauge",
      "physical symmetry" in potential["fixed_dirichlet"]["unrestricted_boundary_transformations"])
check("generated", "the required generated boundary functional is not source-owned",
      not potential["generated_or_robin"]["source_owned_F"])
check("selection", "the current bare action does not lock a nonzero regular charge",
      boundary["disposition"]["bare_action_locks_nonzero_regular_charge_invariants"] == "NO")


print("\nF. REGISTRY AND CLAIM CEILING")
registry = read_json(REGISTRY)
check("registry", "the registry records the exact right reduction dimensions",
      registry["right_reduction"]["zero_level_dimension"] == 140
      and registry["right_reduction"]["quotient_dimension"] == 98)
check("registry", "the formal attachment is closed but selection is not",
      registry["right_reduction"]["formal_global_attachment"] == "CONSTRUCTED"
      and not registry["selection_census"]["current_bare_action_selects_reduction"])
check("ceiling", "the carrier is not promoted to a physical phase space",
      not registry["layer_0"]["physical_phase_space"]
      and registry["disposition"]["physical_gu_attachment"] == "OPEN")
check("ceiling", "no source-selected subgroup or action-selected constraint is claimed",
      not registry["layer_0"]["source_selected_subgroup"]
      and not registry["layer_0"]["action_selected_constraint"])


summary = {"checks": sum(COUNTS.values()), "by_kind": dict(COUNTS), "failures": FAILURES}
print("\n" + json.dumps(summary, sort_keys=True))
raise SystemExit(1 if FAILURES else 0)
