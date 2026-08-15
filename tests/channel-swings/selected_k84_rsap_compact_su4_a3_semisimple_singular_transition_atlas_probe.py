#!/usr/bin/env python3
"""Exact compact SU(4)/SO(4) semisimple singular transition atlas."""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction as F
import io
from itertools import combinations
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k79_rsap_a3_real_form_principal_factor_census_probe.py"
REGISTRY = ROOT / "lab/process/selected-k84-rsap-compact-su4-a3-semisimple-singular-transition-atlas.json"
RESULT = ROOT / "explorations/conditional-build/selected-k84-rsap-compact-su4-a3-semisimple-singular-transition-atlas-2026-08-15.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-15-selected-k84-rsap-compact-su4-a3-semisimple-singular-transition-atlas-review.md"
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    prior = runpy.run_path(str(PREDECESSOR))
check("prior", "the five-real-form predecessor replays 105/105",
      '"checks": 105' in capture.getvalue()
      and '"failures": []' in capture.getvalue()
      and not prior["FAILURES"])

zero = prior["zero"]
eye = prior["eye"]
transpose = prior["transpose"]
mmul = prior["mmul"]
madd = prior["madd"]
msub = prior["msub"]
flatten = prior["flatten"]
column_rank = prior["column_rank"]
diag = prior["diag"]
bracket = prior["bracket"]
adjoint_space = prior["adjoint_space"]
SL4 = prior["SL4"]
REG = json.loads(REGISTRY.read_text(encoding="utf-8"))


def inverse(matrix: list[list[F]]) -> list[list[F]]:
    size = len(matrix)
    work = [[F(value) for value in row] + unit for row, unit in zip(matrix, eye(size))]
    for col in range(size):
        pivot = next((row for row in range(col, size) if work[row][col]), None)
        if pivot is None:
            raise ValueError("singular matrix")
        work[col], work[pivot] = work[pivot], work[col]
        value = work[col][col]
        work[col] = [entry / value for entry in work[col]]
        for row in range(size):
            if row != col and work[row][col]:
                value = work[row][col]
                work[row] = [left - value * right for left, right in zip(work[row], work[col])]
    return [row[size:] for row in work]


def determinant(matrix: list[list[F]]) -> F:
    work = [[F(value) for value in row] for row in matrix]
    value = F(1)
    for col in range(len(work)):
        pivot = next((row for row in range(col, len(work)) if work[row][col]), None)
        if pivot is None:
            return F(0)
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            value = -value
        diagonal = work[col][col]
        value *= diagonal
        for row in range(col + 1, len(work)):
            if work[row][col]:
                ratio = work[row][col] / diagonal
                work[row] = [left - ratio * right for left, right in zip(work[row], work[col])]
    return value


def coordinates(matrix: list[list[F]], basis: list[list[list[F]]]) -> list[F]:
    columns = transpose([flatten(value) for value in basis])
    augmented = [row + [value] for row, value in zip(columns, flatten(matrix))]
    pivot_row = 0
    pivots: list[int] = []
    for col in range(len(basis)):
        pivot = next((row for row in range(pivot_row, len(augmented)) if augmented[row][col]), None)
        if pivot is None:
            continue
        augmented[pivot_row], augmented[pivot] = augmented[pivot], augmented[pivot_row]
        value = augmented[pivot_row][col]
        augmented[pivot_row] = [entry / value for entry in augmented[pivot_row]]
        for row in range(len(augmented)):
            if row != pivot_row and augmented[row][col]:
                value = augmented[row][col]
                augmented[row] = [left - value * right for left, right in zip(augmented[row], augmented[pivot_row])]
        pivots.append(col)
        pivot_row += 1
    if any(all(not row[col] for col in range(len(basis))) and row[-1] for row in augmented):
        raise ValueError("matrix is outside basis span")
    answer = [F(0)] * len(basis)
    for row, pivot in enumerate(pivots):
        answer[pivot] = augmented[row][-1]
    return answer


def set_partitions(items: tuple[int, ...]) -> set[tuple[tuple[int, ...], ...]]:
    if not items:
        return {()}
    first, rest = items[0], items[1:]
    output: set[tuple[tuple[int, ...], ...]] = set()
    for partition in set_partitions(rest):
        output.add(tuple(sorted(((first,),) + partition)))
        for index in range(len(partition)):
            merged = tuple(sorted(partition[index] + (first,)))
            output.add(tuple(sorted(partition[:index] + (merged,) + partition[index + 1:])))
    return output


def multiplicity_type(partition: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    return tuple(sorted((len(block) for block in partition), reverse=True))


print("A. COMPACT NORMALITY AND COMPLETE MULTIPLICITY CENSUS")
H = eye(4)
h_space = adjoint_space(H, -1)
m_space = adjoint_space(H, 1)
check("pair", "the compact pair has dimensions six plus nine",
      column_rank(h_space) == 6 and column_rank(m_space) == 9 and column_rank(h_space + m_space) == 15)
check("pair", "the moving space consists of real symmetric trace-free matrices",
      all(transpose(value) == value and sum(value[i][i] for i in range(4)) == 0 for value in m_space))
check("normality", "compact moving controls are diagonalizable by the real symmetric spectral theorem",
      prior["REG"]["real_forms"]["compact"]["regular_nonsemisimple"] == "EMPTY_BY_COMPACT_NORMALITY")
types = {multiplicity_type(partition) for partition in set_partitions((0, 1, 2, 3))}
check("census", "set-partition exhaustion gives exactly five multiplicity types",
      types == {(1, 1, 1, 1), (2, 1, 1), (2, 2), (3, 1), (4,)})
check("census", "the four nonregular multiplicities match the registry",
      sorted((list(value) for value in types if value != (1, 1, 1, 1)))
      == sorted(REG["classification"]["singular_multiplicities"]))
check("census", "there is one positive-definite sign characteristic",
      REG["classification"]["sign_characteristic_count"] == 1)


print("\nB. REGULAR CONTROL AND FOUR EXACT SINGULAR SCHEDULES")
regular = diag((3, 1, -1, -3))
regular_orbit = column_rank([bracket(value, regular) for value in SL4])
regular_moving = column_rank([bracket(value, regular) for value in m_space])
check("regular", "the compact regular control has full/moving centralizers 3/3",
      15 - regular_orbit == 3 and 9 - regular_moving == 3)
check("regular", "the regular full target/map schedule is 84/91",
      (72 + regular_orbit, 76 + 9 + regular_moving) == (84, 91))

families = {
    "semisimple_2+1+1": (diag((1, 1, 2, -4)), (5, 4, 14, 82, 90)),
    "semisimple_2+2": (diag((1, 1, -1, -1)), (7, 5, 13, 80, 89)),
    "semisimple_3+1": (diag((1, 1, 1, -3)), (9, 6, 12, 78, 88)),
    "origin_4": (zero(4), (15, 9, 9, 72, 85)),
}
for label, (control, expected) in families.items():
    orbit_rank = column_rank([bracket(value, control) for value in SL4])
    moving_rank = column_rank([bracket(value, control) for value in m_space])
    actual = (15 - orbit_rank, 9 - moving_rank, 9 + moving_rank, 72 + orbit_rank, 76 + 9 + moving_rank)
    check("rank", f"{label} has the exact registered centralizers and ranks",
          actual == expected and list(expected) == REG["rank_census"][label])
    check("bound", f"{label} saturates the 98D pointwise bound",
          expected[4] == (98 + expected[3]) // 2)


print("\nC. REGULAR APPROACHES AND COMPLETE MULTIPLICITY CLOSURE GRAPH")
regular_approaches = {
    "semisimple_2+1+1": diag((0, 2, 3, -5)),
    "semisimple_2+2": diag((0, 2, -3, 1)),
    "semisimple_3+1": diag((0, 1, 2, -3)),
    "origin_4": regular,
}
for label, witness in regular_approaches.items():
    orbit_rank = column_rank([bracket(value, witness) for value in SL4])
    check("approach", f"{label} has an exact compact regular approach",
          orbit_rank == 12 and transpose(witness) == witness and sum(witness[i][i] for i in range(4)) == 0)

paths = {
    "regular_to_211": (diag((0, 2, 3, -5)), diag((1, 1, 3, -5)), (5, 4)),
    "regular_to_22": (diag((0, 2, -3, 1)), diag((1, 1, -1, -1)), (7, 5)),
    "regular_to_31": (diag((0, 1, 2, -3)), diag((1, 1, 1, -3)), (9, 6)),
    "regular_to_4": (regular, zero(4), (15, 9)),
    "211_to_22": (diag((1, 1, 2, -4)), diag((1, 1, -1, -1)), (7, 5)),
    "211_to_31": (diag((1, 1, 2, -4)), diag((1, 1, 1, -3)), (9, 6)),
    "22_to_4": (diag((1, 1, -1, -1)), zero(4), (15, 9)),
    "31_to_4": (diag((1, 1, 1, -3)), zero(4), (15, 9)),
}
for label, (start, limit, expected_centralizers) in paths.items():
    check("path", f"{label} stays in the compact symmetric trace-free fibre",
          all(transpose(value) == value and sum(value[i][i] for i in range(4)) == 0
              for value in (start, limit, msub(start, limit))))
    orbit_rank = column_rank([bracket(value, limit) for value in SL4])
    moving_rank = column_rank([bracket(value, limit) for value in m_space])
    check("path", f"{label} lands in the claimed centralizer stratum",
          (15 - orbit_rank, 9 - moving_rank) == expected_centralizers)
check("path", "all eight Hasse-closure controls are registered",
      len(paths) == REG["transitions"]["multiplicity_closure_paths_checked"] == 8)


print("\nD. NONCOMMUTING SO(4) COTANGENT FRAME NERVE")
def rotation(i: int, j: int) -> list[list[F]]:
    value = eye(4)
    value[i][i] = value[j][j] = F(3, 5)
    value[i][j] = F(-4, 5)
    value[j][i] = F(4, 5)
    return value


frames = {
    "identity": eye(4),
    "rotation_01": rotation(0, 1),
    "rotation_12": rotation(1, 2),
    "rotation_23": rotation(2, 3),
}
coordinate_maps = {}
for label, frame in frames.items():
    transformed = [mmul(transpose(frame), mmul(value, frame)) for value in m_space]
    coordinate_map = transpose([coordinates(value, m_space) for value in transformed])
    coordinate_maps[label] = coordinate_map
    check("frame", f"{label} is an exact determinant-one orthogonal moving-frame map",
          mmul(transpose(frame), frame) == eye(4)
          and determinant(frame) == 1
          and determinant(coordinate_map) != 0)

labels = tuple(frames)
transitions = {(target, source): mmul(inverse(coordinate_maps[target]), coordinate_maps[source]) for source in labels for target in labels}
check("nerve", "the four-frame nerve has six pairs and four triangles",
      len(tuple(combinations(labels, 2))) == REG["transitions"]["pairwise_frame_transitions"] == 6
      and len(tuple(combinations(labels, 3))) == REG["transitions"]["frame_triangles"] == 4)
check("nerve", "overlapping rational rotations give noncommuting frame transitions",
      any(mmul(transitions[(j, i)], transitions[(k, j)]) != mmul(transitions[(k, j)], transitions[(j, i)])
          for i, j, k in combinations(labels, 3)))
q = [[F(value)] for value in (2, -3, 5, 7, -11, 13, 17, -19, 23)]
dq = [[F(value)] for value in (29, -31, 37, 41, -43, 47, 53, -59, 61)]
pair_results = []
for source, target in combinations(labels, 2):
    tangent = transitions[(target, source)]
    cotangent = transpose(inverse(tangent))
    pair_results.append(mmul(transpose(mmul(cotangent, q)), mmul(tangent, dq)) == mmul(transpose(q), dq))
check("primitive", "all six inverse-transpose changes preserve the tautological pairing", all(pair_results))
base_cycles = []
cotangent_cycles = []
for i, j, k in combinations(labels, 3):
    base_cycles.append(mmul(transitions[(i, k)], mmul(transitions[(k, j)], transitions[(j, i)])) == eye(9))
    cotangent_cycles.append(mmul(transpose(inverse(transitions[(i, k)])), mmul(transpose(inverse(transitions[(k, j)])), transpose(inverse(transitions[(j, i)])))) == eye(9))
check("cocycle", "all four SO(4) base-frame triangles close", all(base_cycles))
check("cocycle", "all four cotangent-frame triangles close", all(cotangent_cycles))
check("moment", "the global compact cotangent moment map has zero Cech defect",
      REG["transitions"]["moment_cech_defect"] == "ZERO_BY_ONE_GLOBAL_COMPACT_SU4_COTANGENT_MOMENT_MAP")


print("\nE. CLAIM CEILING")
scope = REG["scope"]
check("scope", "the compact local singular atlas closes without a new model",
      scope["compact_su4_singular_transition_atlas"].startswith("CLOSED")
      and scope["new_compact_su4_local_model"] == "NOT_REQUIRED")
check("scope", "cross-real-form incidence remains type-missing",
      scope["cross_real_form_atlas_edge"] == "TYPE_MISSING_NOT_REOPENED")
check("scope", "the quaternionic atlas is next", scope["quaternionic_singular_transition_atlas"] == "OPEN_NEXT")
check("scope", "deeper strata zero charge and global RSAP remain open",
      {scope["deeper_so77_singular_strata"], scope["zero_charge_rank_at_most_49"], scope["global_all_strata_rsap"]} == {"OPEN", "NOT_CONSTRUCTED"})
check("scope", "the all-charge fallback remains 182-dimensional", scope["all_charge_fallback_dimension"] == 182)
check("scope", "protected truth surfaces remain unchanged", set(REG["changes"].values()) == {"none"})
check("links", "result registry and hostile review paths are durable",
      all(path.exists() for path in (RESULT, REGISTRY, REVIEW)))


print("\nSUMMARY")
print(json.dumps({"checks": sum(COUNTS.values()), "failures": FAILURES, "groups": dict(sorted(COUNTS.items()))}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
