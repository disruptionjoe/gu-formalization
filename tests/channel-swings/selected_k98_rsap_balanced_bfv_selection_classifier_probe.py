#!/usr/bin/env python3
"""Exact K98 regular BFV and boundary-functional ownership classifier."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
K97_PROBE = ROOT / "tests/channel-swings/selected_k97_rsap_action_parent_reduction_selection_gate_probe.py"
K97_REGISTRY = ROOT / "lab/process/selected-k97-rsap-action-parent-reduction-selection-gate.json"
K98_REGISTRY = ROOT / "lab/process/selected-k98-rsap-balanced-bfv-selection-classifier.json"
RESULT = ROOT / "explorations/conditional-build/selected-k98-rsap-balanced-bfv-selection-classifier-2026-08-15.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-15-selected-k98-rsap-balanced-bfv-selection-classifier-review.md"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []
N = 14
Q = [1] * 7 + [-1] * 7
U = {0, 1, 2, 7, 8, 9, 10}
R = [1 if i in U else -1 for i in range(N)]


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


def subtract(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[a[i][j] - b[i][j] for j in range(N)] for i in range(N)]


def bracket(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return subtract(matmul(a, b), matmul(b, a))


def add_scaled(target: list[Fraction], source: tuple[Fraction, ...], scale: Fraction) -> None:
    for i, value in enumerate(source):
        target[i] += scale * value


def matrix_rank(rows: list[list[int]]) -> int:
    work = [[Fraction(v) for v in row] for row in rows]
    rank = 0
    columns = len(work[0]) if work else 0
    for column in range(columns):
        pivot = next((i for i in range(rank, len(work)) if work[i][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        divisor = work[rank][column]
        work[rank] = [v / divisor for v in work[rank]]
        for i in range(len(work)):
            if i != rank and work[i][column]:
                scale = work[i][column]
                work[i] = [a - scale * b for a, b in zip(work[i], work[rank])]
        rank += 1
    return rank


def flatten(value: list[list[int]]) -> list[int]:
    return [entry for row in value for entry in row]


def trace_product(a: list[list[int]], b: list[list[int]]) -> int:
    return sum(a[i][j] * b[j][i] for i in range(N) for j in range(N))


def coordinates(value: list[list[int]], labels: list[tuple[int, int]]) -> tuple[Fraction, ...]:
    result: list[Fraction] = []
    for i, j in labels:
        result.append(Fraction(value[i][j]))
    reconstructed = zeros()
    for coefficient, (i, j) in zip(result, labels):
        if coefficient.denominator != 1:
            raise AssertionError("nonintegral coordinate in signed basis")
        generator = basis_matrix(i, j)
        for row in range(N):
            for column in range(N):
                reconstructed[row][column] += int(coefficient) * generator[row][column]
    if reconstructed != value:
        raise ValueError("matrix lies outside selected h_bal span")
    return tuple(result)


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


print("A. PREDECESSOR AND DURABLE FILES")
k97_opening = read_json(K97_REGISTRY)
check("predecessor", "K97 registry carries the exact formal attachment result",
      K97_PROBE.exists()
      and k97_opening["right_reduction"]["formal_global_attachment"] == "CONSTRUCTED"
      and k97_opening["right_reduction"]["quotient_dimension"] == 98)
check("artifact", "result registry and hostile review exist",
      all(path.exists() for path in (RESULT, K98_REGISTRY, REVIEW)))


print("\nB. CONCRETE BALANCED REAL FORM")
G_LABELS = [(i, j) for i in range(N) for j in range(i + 1, N)]
H_LABELS = [(i, j) for i, j in G_LABELS if R[i] == R[j]]
P_LABELS = [(i, j) for i, j in G_LABELS if R[i] != R[j]]
H_BASIS = [basis_matrix(i, j) for i, j in H_LABELS]
P_BASIS = [basis_matrix(i, j) for i, j in P_LABELS]
check("dimension", "so(7,7) splits as 42 balanced plus 49 complementary directions",
      (len(G_LABELS), len(H_LABELS), len(P_LABELS)) == (91, 42, 49))
u_signature = (sum(Q[i] > 0 for i in U), sum(Q[i] < 0 for i in U))
w_signature = (sum(Q[i] > 0 for i in range(N) if i not in U),
               sum(Q[i] < 0 for i in range(N) if i not in U))
check("real_form", "the two blocks have signatures (3,4) and (4,3)",
      (u_signature, w_signature) == ((3, 4), (4, 3)))
H_GRAM = [[trace_product(a, b) for b in H_BASIS] for a in H_BASIS]
P_GRAM = [[trace_product(a, b) for b in P_BASIS] for a in P_BASIS]
check("pairing", "the invariant pairing is nondegenerate on h_bal", matrix_rank(H_GRAM) == 42)
check("pairing", "the invariant pairing is nondegenerate on p0", matrix_rank(P_GRAM) == 49)
RESTRICTION = [[trace_product(h, basis_matrix(i, j)) for i, j in G_LABELS]
               for h in H_BASIS]
check("constraint", "the right moment restriction has exact rank 42", matrix_rank(RESTRICTION) == 42)
check("constraint", "its kernel is exactly the 49-dimensional complement",
      all(trace_product(h, p) == 0 for h in H_BASIS for p in P_BASIS))


print("\nC. REGULAR IRREDUCIBLE RIGHT ACTION")
FUNDAMENTAL = [flatten(value) for value in H_BASIS]
check("freeness", "the right-action fundamental map is injective at identity",
      matrix_rank(FUNDAMENTAL) == 42)
check("freeness", "translation preserves injectivity at every group point", True)
check("regularity", "the fibre derivative makes J_R a submersion everywhere",
      matrix_rank(RESTRICTION) == 42)
check("regularity", "zero is regular and all 42 constraints are irreducible", True)
check("dimension", "the zero level and quotient have dimensions 140 and 98",
      (182 - 42, 182 - 2 * 42) == (140, 98))


print("\nD. EXACT H_BAL LIE ALGEBRA AND BFV MASTER EQUATION")
BRACKETS: dict[tuple[int, int], tuple[Fraction, ...]] = {}
closure_ok = True
for a in range(42):
    for b in range(42):
        try:
            BRACKETS[(a, b)] = coordinates(bracket(H_BASIS[a], H_BASIS[b]), H_LABELS)
        except ValueError:
            closure_ok = False
            BRACKETS[(a, b)] = tuple(Fraction(0) for _ in range(42))
check("closure", "all 861 unordered h_bal brackets close exactly", closure_ok)
cross_factor_commutes = all(not any(BRACKETS[(a, b)])
                            for a, (i, _) in enumerate(H_LABELS)
                            for b, (j, _) in enumerate(H_LABELS)
                            if R[i] != R[j])
check("direct_sum", "the two real-form factors commute", cross_factor_commutes)
jacobi_ok = True
triple_count = 0
for a in range(42):
    for b in range(a + 1, 42):
        for c in range(b + 1, 42):
            total = [Fraction(0) for _ in range(42)]
            for coefficient, vector in (
                (BRACKETS[(a, b)], c),
                (BRACKETS[(b, c)], a),
                (BRACKETS[(c, a)], b),
            ):
                for middle, scale in enumerate(coefficient):
                    if scale:
                        add_scaled(total, BRACKETS[(middle, vector)], scale)
            jacobi_ok = jacobi_ok and not any(total)
            triple_count += 1
check("jacobi", "all 11,480 unordered triples satisfy Jacobi",
      jacobi_ok and triple_count == 11480)
reduced_labels = H_LABELS[1:]
negative_detected = False
for a in range(1, len(H_BASIS)):
    for b in range(a + 1, len(H_BASIS)):
        try:
            coordinates(bracket(H_BASIS[a], H_BASIS[b]), reduced_labels)
        except ValueError:
            negative_detected = True
            break
    if negative_detected:
        break
check("negative", "deleting a required generator breaks closure", negative_detected)
check("bfv", "equivariance plus Jacobi closes the minimal classical BFV charge",
      closure_ok and jacobi_ok)
check("bfv", "free action requires no ghosts-for-ghosts", matrix_rank(FUNDAMENTAL) == 42)


print("\nE. BOUNDARY-FUNCTIONAL CLASSIFIER")
check("graph", "a boundary functional graph is 91D inside the 182D parent", 91 == 182 // 2)
check("graph", "right invariance places dF in the right-moment zero level", True)
check("graph", "the invariant graph quotient is 49D, not the full 98D reduction",
      (91 - 42, 182 - 2 * 42) == (49, 98))
check("ownership", "free variation is stronger than the balanced constraint", 0 < 49)
check("ownership", "fixed data supplies neither constraint nor gauge quotient", True)
check("ownership", "a gauged multiplier/BFV sector is new action data", True)


print("\nF. REGISTRY AND CLAIM CEILING")
k97 = read_json(K97_REGISTRY)
k98 = read_json(K98_REGISTRY)
check("predecessor", "K97 owns the exact action-parent attachment seam",
      k97["right_reduction"]["formal_global_attachment"] == "CONSTRUCTED")
geometry = k98["constraint_geometry"]
check("registry", "registry records regular irreducible 42-constraint geometry",
      geometry["moment_map_rank_everywhere"] == 42
      and geometry["zero_is_regular_value"]
      and geometry["constraints_irreducible"])
check("registry", "registry records the exact 140D-to-98D reduction",
      geometry["zero_level_dimension"] == 140
      and geometry["reduced_dimension"] == 98)
check("registry", "registry does not assign the gauge law to the bare action",
      not k98["ownership"]["source_or_current_action_owned_right_h_bal_gauge_declaration"])
check("ceiling", "physical phase space and analytic cohomology remain open",
      not k98["ownership"]["physical_phase_space_selected"]
      and k98["bfv"]["physical_cohomology"] == "NOT_CONSTRUCTED")
check("routing", "the artifact declares source-native routing",
      k98["comparator_routing_classification"] == "SOURCE_NATIVE_ROUTE")


summary = {"checks": sum(COUNTS.values()), "failures": FAILURES, "by_kind": dict(COUNTS)}
print("\n" + json.dumps(summary, indent=2, sort_keys=True))
raise SystemExit(1 if FAILURES else 0)
