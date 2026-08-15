#!/usr/bin/env python3
"""Exact K100 balanced order-parameter construction and owner census."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import contextlib
import io
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
K99_PROBE = ROOT / "tests/channel-swings/selected_k99_rsap_balanced_multiplier_owner_exhaustion_probe.py"
K100_REGISTRY = ROOT / "lab/process/selected-k100-rsap-balanced-order-parameter-owner-census.json"
RESULT = ROOT / "explorations/conditional-build/selected-k100-rsap-balanced-order-parameter-owner-census-2026-08-15.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-15-selected-k100-rsap-balanced-order-parameter-owner-census-review.md"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []
N = 14
Q = [1] * 7 + [-1] * 7
PRIME = 1_000_003


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


def zero(n: int) -> list[list[int]]:
    return [[0] * n for _ in range(n)]


def identity(n: int) -> list[list[int]]:
    return [[int(i == j) for j in range(n)] for i in range(n)]


def basis_matrix(i: int, j: int, form: list[int]) -> list[list[int]]:
    value = zero(len(form))
    value[i][j] = 1
    value[j][i] = -form[i] * form[j]
    return value


def so_basis(form: list[int]) -> list[list[list[int]]]:
    return [basis_matrix(i, j, form)
            for i in range(len(form)) for j in range(i + 1, len(form))]


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def subtract(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def bracket(a, b):
    return subtract(matmul(a, b), matmul(b, a))


def transpose(a):
    return [list(row) for row in zip(*a)]


def flatten(a):
    return [value for row in a for value in row]


def matrix_rank(rows) -> int:
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


def commutant_rows(generators, n: int):
    rows = []
    for generator in generators:
        for i in range(n):
            for j in range(n):
                row = {}
                for k in range(n):
                    if generator[i][k]:
                        key = k * n + j
                        row[key] = row.get(key, 0) + generator[i][k]
                    if generator[k][j]:
                        key = i * n + k
                        row[key] = row.get(key, 0) - generator[k][j]
                if any(row.values()):
                    rows.append(row)
    return rows


def modular_sparse_rank(rows) -> int:
    pivots = {}
    for source in rows:
        row = {key: value % PRIME for key, value in source.items() if value % PRIME}
        while row:
            pivot = min(row)
            if pivot not in pivots:
                inverse = pow(row[pivot], PRIME - 2, PRIME)
                row = {key: (value * inverse) % PRIME
                       for key, value in row.items() if (value * inverse) % PRIME}
                pivots[pivot] = row
                break
            factor = row[pivot]
            for key, value in pivots[pivot].items():
                new = (row.get(key, 0) - factor * value) % PRIME
                if new:
                    row[key] = new
                elif key in row:
                    del row[key]
    return len(pivots)


def diagonal_involution(plus: set[int]) -> list[list[int]]:
    return [[(1 if i in plus else -1) if i == j else 0 for j in range(N)]
            for i in range(N)]


def signature(indices: set[int]) -> tuple[int, int]:
    return (sum(Q[index] == 1 for index in indices),
            sum(Q[index] == -1 for index in indices))


def trace(a) -> Fraction:
    return sum(a[i][i] for i in range(len(a)))


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


print("A. PREDECESSOR AND DURABLE FILES")
replay = io.StringIO()
replay_code = None
with contextlib.redirect_stdout(replay):
    try:
        runpy.run_path(str(K99_PROBE), run_name="__main__")
    except SystemExit as error:
        replay_code = error.code
check("predecessor", "K99 multiplier-owner certificate replays cleanly",
      replay_code == 0 and '"failures": []' in replay.getvalue())
check("artifact", "result registry and hostile review exist",
      all(path.exists() for path in (RESULT, K100_REGISTRY, REVIEW)))


print("\nB. ALL REAL SIGNATURE TYPES OF SEVEN-PLUS-SEVEN INVOLUTIONS")
orbit_rows = []
all_spectral_equal = True
all_stabilizers = True
for a in range(8):
    plus = set(range(a)) | set(range(7, 7 + (7 - a)))
    involution = diagonal_involution(plus)
    powers = []
    power = identity(N)
    for exponent in range(1, 15):
        power = matmul(power, involution)
        powers.append(trace(power))
    stabilizer = sum(1 for i in range(N) for j in range(i + 1, N)
                     if (i in plus) == (j in plus))
    orbit_rows.append((signature(plus), signature(set(range(N)) - plus),
                       trace(involution), tuple(powers), stabilizer))
    all_spectral_equal = all_spectral_equal and tuple(powers) == tuple(
        0 if exponent % 2 else 14 for exponent in range(1, 15))
    all_stabilizers = all_stabilizers and stabilizer == 42
check("orbit", "all eight real signature allocations are enumerated", len(orbit_rows) == 8)
check("orbit", "the allocations are (a,7-a)|(7-a,a)",
      all(row[0] == (a, 7 - a) and row[1] == (7 - a, a)
          for a, row in enumerate(orbit_rows)))
check("spectrum", "all eight types have identical traces through degree 14",
      all_spectral_equal)
check("dimension", "every type has stabilizer 42 and orbit dimension 49",
      all_stabilizers and 91 - 42 == 49)
check("balanced", "the unordered balanced type is exactly a=3 or a=4",
      orbit_rows[3][:2] == ((3, 4), (4, 3))
      and orbit_rows[4][:2] == ((4, 3), (3, 4)))


print("\nC. EPSILON DRESSING AND PHYSICAL-SPLIT CONTROL")
FULL = so_basis(Q)
balanced_plus = set(range(3)) | set(range(7, 11))
R0 = diagonal_involution(balanced_plus)
derivative = [flatten(bracket(generator, R0)) for generator in FULL]
check("dressing", "delta R=[eta,R] has rank 49", matrix_rank(derivative) == 49)
check("dressing", "its kernel has dimension 42", 91 - matrix_rank(derivative) == 42)
check("dressing", "the kernel generators are exactly the balanced stabilizer",
      sum(all(value == 0 for value in column) for column in derivative) == 42)
linearized_tangent_ok = all(
    add(matmul(column_matrix, R0), matmul(R0, column_matrix)) == zero(N)
    for column_matrix in (bracket(generator, R0) for generator in FULL))
check("dressing", "every moving-orbit tangent preserves R^2=1 to first order",
      linearized_tangent_ok)
physical_plus = {0, 7, 8, 9}
R_physical = diagonal_involution(physical_plus)
check("control", "the physical involution has signature (1,3)|(6,4) and trace -6",
      signature(physical_plus) == (1, 3)
      and signature(set(range(N)) - physical_plus) == (6, 4)
      and trace(R_physical) == -6)
check("control", "conjugation cannot turn physical multiplicities 4|10 into 7|7",
      (len(physical_plus), N - len(physical_plus)) == (4, 10)
      and trace(R_physical) != trace(R0))


print("\nD. GLOBAL CHARGE-ONLY EQUIVARIANCE OBSTRUCTION")
ambient_rank_mod = modular_sparse_rank(commutant_rows(FULL, N))
check("commutant", "the exact ambient commutant has codimension 195",
      ambient_rank_mod == 195)
check("commutant", "identity supplies the one-dimensional exact kernel",
      all(bracket(identity(N), generator) == zero(N) for generator in FULL)
      and N * N - ambient_rank_mod == 1)
check("zero", "a scalar involution has trace plus or minus 14, never zero",
      {trace(identity(N)), trace([[-value for value in row] for row in identity(N)])}
      == {14, -14})
check("zero", "an adjoint-equivariant charge-only map cannot be balanced at zero",
      ambient_rank_mod == 195 and trace(R0) == 0)


print("\nE. SOURCE-PHYSICAL LORENTZ COMMUTANT")
ETA = [1, -1, -1, -1]
LORENTZ = so_basis(ETA)
PAIRS = [(i, j) for i in range(4) for j in range(i, 4)]
REPRESENTATION = []
for generator in LORENTZ:
    representation = zero(N)
    for i in range(4):
        for j in range(4):
            representation[i][j] = generator[i][j]
    for column, (u, v) in enumerate(PAIRS):
        symmetric = zero(4)
        symmetric[u][v] = 1
        symmetric[v][u] = 1
        transformed = [[sum(generator[i][k] * symmetric[k][j]
                            + symmetric[i][k] * generator[j][k]
                            for k in range(4))
                        for j in range(4)] for i in range(4)]
        for row, (i, j) in enumerate(PAIRS):
            representation[4 + row][4 + column] = transformed[i][j]
    REPRESENTATION.append(representation)
lorentz_rank_mod = modular_sparse_rank(commutant_rows(REPRESENTATION, N))
check("commutant", "the full physical 14D Lorentz commutant has dimension three",
      N * N - lorentz_rank_mod == 3)

P_BASE = [[Fraction(int(i == j and i < 4)) for j in range(N)] for i in range(N)]
P_SYM = [[Fraction(int(i == j and i >= 4)) for j in range(N)] for i in range(N)]
metric_vector = [Fraction(ETA[i] if i == j else 0) for i, j in PAIRS]
trace_functional = [Fraction(ETA[i] if i == j else 0) for i, j in PAIRS]
P_TRACE = [[Fraction(0) for _ in range(N)] for _ in range(N)]
for i in range(10):
    for j in range(10):
        P_TRACE[4 + i][4 + j] = metric_vector[i] * trace_functional[j] / 4
P_TRACELESS = subtract(P_SYM, P_TRACE)
projectors = (P_BASE, P_TRACE, P_TRACELESS)
check("projector", "base trace and traceless projectors commute with Lorentz",
      all(bracket(projector, generator) == zero(N)
          for projector in projectors for generator in REPRESENTATION))
check("projector", "the three projectors are orthogonal and sum to identity",
      add(add(P_BASE, P_TRACE), P_TRACELESS) == identity(N)
      and all(matmul(projectors[i], projectors[j]) == zero(N)
              for i in range(3) for j in range(3) if i != j))
check("projector", "their ranks are exactly 4,1,9",
      tuple(matrix_rank(projector) for projector in projectors) == (4, 1, 9)
      and tuple(trace(projector) for projector in projectors) == (4, 1, 9))
subset_dimensions = sorted({sum(size for bit, size in zip(mask, (4, 1, 9)) if bit)
                            for mask in ((a, b, c) for a in (0, 1)
                                         for b in (0, 1) for c in (0, 1))})
check("obstruction", "Lorentz-equivariant involution eigenspaces have only block-subset dimensions",
      subset_dimensions == [0, 1, 4, 5, 9, 10, 13, 14])
check("obstruction", "no Lorentz-natural homogeneous seven-plane exists",
      7 not in subset_dimensions)


print("\nF. REGISTRY, CLAIM CEILING AND SUCCESSOR")
k100 = read_json(K100_REGISTRY)
check("registry", "registry records eight real orbit types and balanced a=3/4",
      k100["balanced_involution_orbits"]["real_orbit_types"] == 8
      and k100["balanced_involution_orbits"]["balanced_unordered_type"] == "a=3_or_4")
check("registry", "epsilon reuses existing continuous coordinates but not the seed",
      k100["epsilon_dressing"]["new_continuous_local_field_components"] == 0
      and "R0" in k100["epsilon_dressing"]["required_external_input"])
check("ceiling", "nonhomogeneous curvature and unreleased action routes remain open",
      k100["claim_ceiling"]["nonhomogeneous_curvature_selector"] == "OPEN"
      and k100["claim_ceiling"]["unreleased_action_term"] == "OPEN")
check("ceiling", "physical phase-space selection remains open",
      k100["claim_ceiling"]["physical_phase_space_selection"] == "OPEN")
check("successor", "next gate is the actual projected dressed-connection variational role",
      k100["disposition"]["next_gate"].startswith(
          "WITH_CONDITIONAL_BALANCED_R0_PROJECT_DRESSED_B_EPSILON"))
check("routing", "the result remains source-native and changes no ledger",
      k100["comparator_routing_classification"] == "SOURCE_NATIVE_ROUTE"
      and k100["disposition"]["ledger_change"] == "none")


summary = {"checks": sum(COUNTS.values()), "failures": FAILURES,
           "by_kind": dict(COUNTS)}
print("\n" + json.dumps(summary, indent=2, sort_keys=True))
raise SystemExit(1 if FAILURES else 0)
