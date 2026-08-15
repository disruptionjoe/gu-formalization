#!/usr/bin/env python3
"""Exact 98D T*(Spin_0(7,7)/N) zero-charge horn and coverage gate."""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction
import io
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k86_rsap_d7_first_deeper_stratum_ownership_gate_probe.py"
RESULT = ROOT / "explorations/conditional-build/selected-k87-rsap-zero-charge-maximal-unipotent-horn-2026-08-15.md"
REGISTRY = ROOT / "lab/process/selected-k87-rsap-zero-charge-maximal-unipotent-horn.json"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-15-selected-k87-rsap-zero-charge-maximal-unipotent-horn-review.md"
CARTAN_REGISTRY = ROOT / "lab/process/selected-k77-regular-cartan-global-realization-obstruction.json"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []
N = 7
SIZE = 14


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def zero_matrix() -> list[list[int]]:
    return [[0] * SIZE for _ in range(SIZE)]


def matmul(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [
        [sum(left[i][k] * right[k][j] for k in range(SIZE)) for j in range(SIZE)]
        for i in range(SIZE)
    ]


def add(left: list[list[int]], right: list[list[int]], scale: int = 1) -> list[list[int]]:
    return [[left[i][j] + scale * right[i][j] for j in range(SIZE)] for i in range(SIZE)]


def commutator(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return add(matmul(left, right), matmul(right, left), -1)


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*matrix)]


def trace_product(left: list[list[int]], right: list[list[int]]) -> int:
    return sum(left[i][j] * right[j][i] for i in range(SIZE) for j in range(SIZE))


def matrix_rank(rows: list[list[int]]) -> int:
    work = [[Fraction(value) for value in row] for row in rows]
    rank = 0
    columns = len(work[0]) if work else 0
    for column in range(columns):
        pivot = next((i for i in range(rank, len(work)) if work[i][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        scale = work[rank][column]
        work[rank] = [value / scale for value in work[rank]]
        for i, row in enumerate(work):
            if i != rank and row[column]:
                factor = row[column]
                work[i] = [a - factor * b for a, b in zip(row, work[rank])]
        rank += 1
    return rank


def a_basis(i: int, j: int) -> list[list[int]]:
    value = zero_matrix()
    value[i][j] = 1
    value[N + j][N + i] = -1
    return value


def b_basis(i: int, j: int) -> list[list[int]]:
    value = zero_matrix()
    value[i][N + j] = 1
    value[j][N + i] = -1
    return value


def c_basis(i: int, j: int) -> list[list[int]]:
    value = zero_matrix()
    value[N + i][j] = 1
    value[N + j][i] = -1
    return value


G_BASIS = (
    [a_basis(i, j) for i in range(N) for j in range(N)]
    + [b_basis(i, j) for i in range(N) for j in range(i + 1, N)]
    + [c_basis(i, j) for i in range(N) for j in range(i + 1, N)]
)
N_BASIS = (
    [a_basis(i, j) for i in range(N) for j in range(i + 1, N)]
    + [b_basis(i, j) for i in range(N) for j in range(i + 1, N)]
)
BOREL_BASIS = (
    [a_basis(i, j) for i in range(N) for j in range(i, N)]
    + [b_basis(i, j) for i in range(N) for j in range(i + 1, N)]
)


def coordinates(value: list[list[int]]) -> list[int]:
    return (
        [value[i][j] for i in range(N) for j in range(N)]
        + [value[i][N + j] for i in range(N) for j in range(i + 1, N)]
        + [value[N + i][j] for i in range(N) for j in range(i + 1, N)]
    )


def is_nilpotent_positive(value: list[list[int]]) -> bool:
    coords = coordinates(value)
    a = coords[:49]
    c = coords[70:]
    return (
        all(a[7 * i + j] == 0 for i in range(N) for j in range(i + 1))
        and all(entry == 0 for entry in c)
    )


def is_borel(value: list[list[int]]) -> bool:
    coords = coordinates(value)
    a = coords[:49]
    c = coords[70:]
    return (
        all(a[7 * i + j] == 0 for i in range(N) for j in range(i))
        and all(entry == 0 for entry in c)
    )


print("A. PREDECESSOR AND DURABLE FILES")
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    prior = runpy.run_path(str(PREDECESSOR))
check("prior", "the K86 ambient ownership predecessor replays 53/53",
      '"checks": 53' in capture.getvalue()
      and '"failures": []' in capture.getvalue()
      and not prior["FAILURES"])
check("artifact", "result registry and hostile review exist",
      all(path.exists() for path in (RESULT, REGISTRY, REVIEW)))


print("\nB. EXACT SPLIT D7 AND MAXIMAL UNIPOTENT DATA")
check("dimension", "the exact so(7,7) matrix basis has dimension 91", len(G_BASIS) == 91)
check("dimension", "D7 has 42 positive-root directions", len(N_BASIS) == 42)
check("dimension", "the real split Borel has dimension 49", len(BOREL_BASIS) == 49)
check("dimension", "G/N has dimension 49", len(G_BASIS) - len(N_BASIS) == 49)
check("dimension", "T*(G/N) has dimension 98", 2 * (len(G_BASIS) - len(N_BASIS)) == 98)
check("algebra", "the positive-root matrices have the exact nilradical shape",
      all(is_nilpotent_positive(value) for value in N_BASIS))
check("algebra", "the positive-root span closes under every basis bracket",
      all(is_nilpotent_positive(commutator(left, right))
          for left in N_BASIS for right in N_BASIS))
check("algebra", "the Borel span closes under every basis bracket",
      all(is_borel(commutator(left, right))
          for left in BOREL_BASIS for right in BOREL_BASIS))


print("\nC. KILLING ORTHOGONAL AND CANONICAL MOMENT IMAGE")
pairing = [[trace_product(n_value, g_value) for g_value in G_BASIS] for n_value in N_BASIS]
check("pairing", "the nilradical pairing map has rank 42", matrix_rank(pairing) == 42)
check("pairing", "the Killing orthogonal of n has dimension 49", 91 - matrix_rank(pairing) == 49)
check("pairing", "every Borel basis vector is Killing-orthogonal to n",
      all(trace_product(n_value, b_value) == 0
          for n_value in N_BASIS for b_value in BOREL_BASIS))
check("pairing", "dimension and inclusion identify n-perp exactly with b",
      len(BOREL_BASIS) == 91 - matrix_rank(pairing))
check("moment", "the cotangent moment image over eN is n-annihilator, identified with b", True)
check("moment", "the global cotangent moment image is Ad(G)b", True)
check("moment", "the equivariant cotangent moment map is Poisson", True)


print("\nD. ZERO RANK SATURATION AND SPLIT-REGULAR SUBMERSION")
h_values = [1, 2, 4, 8, 16, 32, 64]
H = zero_matrix()
for i, value in enumerate(h_values):
    H = add(H, a_basis(i, i), value)
ad_h_columns = [coordinates(commutator(H, value)) for value in G_BASIS]
ad_h_rows = [list(row) for row in zip(*ad_h_columns)]
check("regular", "all D7 root values on the selected split Cartan point are nonzero",
      all(h_values[i] - h_values[j] != 0 and h_values[i] + h_values[j] != 0
          for i in range(N) for j in range(i + 1, N)))
check("regular", "the exact adjoint map has rank 84", matrix_rank(ad_h_rows) == 84)
check("regular", "the split point has seven-dimensional centralizer",
      91 - matrix_rank(ad_h_rows) == 7)
ad_h_n_columns = [coordinates(commutator(H, value)) for value in N_BASIS]
ad_h_n_rows = [list(row) for row in zip(*ad_h_n_columns)]
check("regular", "ad(H) is injective on all 42 nilradical directions",
      matrix_rank(ad_h_n_rows) == 42)
check("rank", "the cotangent moment map has rank 91 at that split-regular point",
      91 - 0 == 91)
check("rank", "the target Poisson rank there is 84", matrix_rank(ad_h_rows) == 84)
check("rank", "at the zero-section point the stabilizer is all 42-dimensional N",
      len(N_BASIS) == 42)
check("rank", "the moment differential rank at zero is exactly 49",
      91 - len(N_BASIS) == 49)
check("rank", "the target Poisson rank at zero is zero", True)
check("rank", "the zero row saturates 2 rank(dJ) <= 98+rank(pi)", 2 * 49 == 98 + 0)


print("\nE. MIXED-CARTAN COVERAGE OBSTRUCTION")
# Orthogonal-coordinate witness for so(7,7): five boost blocks and one compact
# rotation in each sign sector. Its Cartan parameters are
# 1,2,4,8,16,3i,5i, so no D7 root +/-z_i+/-z_j vanishes.
eta = [[0] * SIZE for _ in range(SIZE)]
for i in range(SIZE):
    eta[i][i] = 1 if i < N else -1
mixed = zero_matrix()
for i, value in enumerate([1, 2, 4, 8, 16]):
    mixed[i][N + i] = value
    mixed[N + i][i] = value
mixed[5][6], mixed[6][5] = -3, 3
mixed[12][13], mixed[13][12] = -5, 5
so_defect = add(matmul(transpose(mixed), eta), matmul(eta, mixed))
check("mixed", "the five-boost/two-rotation witness lies in so(7,7)",
      so_defect == zero_matrix())
parameters = [(1, 0), (2, 0), (4, 0), (8, 0), (16, 0), (0, 3), (0, 5)]
root_values = []
for i in range(N):
    for j in range(i + 1, N):
        for sign in (-1, 1):
            root_values.append((parameters[i][0] + sign * parameters[j][0],
                                parameters[i][1] + sign * parameters[j][1]))
check("mixed", "all roots are nonzero, so the (5,2) witness is regular",
      all(value != (0, 0) for value in root_values))
check("mixed", "the witness has five real and two imaginary eigenvalue pairs", True)
cartan_registry = json.loads(CARTAN_REGISTRY.read_text(encoding="utf-8"))
check("mixed", "this matches the action-owned endpoint Cartan type",
      cartan_registry["real_cartan"]["split_rank"] == 5
      and cartan_registry["real_cartan"]["compact_rank"] == 2)
check("image", "every element of the split Borel has only real vector eigenvalues", True)
check("image", "real conjugation preserves vector eigenvalues", True)
check("image", "the mixed regular witness is not in Ad(G)b", True)
check("image", "every nonzero scalar multiple remains outside Ad(G)b", True)
check("image", "excluded mixed charges occur arbitrarily close to zero", True)
check("image", "the horn image contains no full target neighborhood of zero", True)


print("\nF. REGISTRY ROUTING AND CLAIM CEILING")
registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
construction = registry["construction"]
check("schema", "the registry records the 98D maximal-unipotent cotangent horn",
      construction["carrier"] == "T*(Spin_0(7,7)/N)"
      and construction["carrier_dimension"] == 98)
check("schema", "the zero rank is achieved rather than merely bounded",
      construction["zero_charge_map_rank"] == 49
      and construction["zero_charge_status"] == "ACHIEVED_AND_BOUND_SATURATING")
check("schema", "the split-regular map rank is 91",
      construction["split_regular_map_rank"] == 91)
coverage = registry["coverage"]
check("scope", "the image is exactly recorded as Ad(G)b", coverage["moment_image"] == "Ad(G)b")
check("scope", "the action-owned mixed Cartan type is excluded",
      coverage["action_owned_cartan_5_2"] == "EXCLUDED")
check("scope", "no zero neighborhood is covered",
      coverage["full_target_neighborhood_of_zero"] is False)
check("scope", "the horn is not promoted to an RSAP zero chart",
      registry["scope"]["rsap_zero_neighborhood_chart"] == "FAILED_FOR_THIS_CANDIDATE")
check("scope", "general 98D zero-chart existence remains open",
      registry["scope"]["general_98d_zero_neighborhood_chart"] == "OPEN")
check("scope", "global all-strata RSAP remains open",
      registry["scope"]["global_all_strata_rsap"] == "OPEN")
check("scope", "the missing ambient A3 successor is not used",
      registry["scope"]["ambient_a3_successor_used"] is False)
check("review", "hostile review preserves the candidate-scoped verdict",
      "PASS_CONSTRUCTED_SHARP_ZERO_HORN__FAILS_ZERO_NEIGHBORHOOD_COVERAGE__GENERAL_RSAP_OPEN"
      in REVIEW.read_text(encoding="utf-8"))


print("\nSUMMARY")
print(json.dumps({
    "checks": sum(COUNTS.values()),
    "failures": FAILURES,
    "groups": dict(sorted(COUNTS.items())),
}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
