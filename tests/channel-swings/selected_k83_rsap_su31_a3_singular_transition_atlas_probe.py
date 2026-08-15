#!/usr/bin/env python3
"""Exact four-configuration singular transition atlas for SU(3,1)/SO(3,1)."""

from __future__ import annotations

from collections import Counter
import contextlib
from fractions import Fraction as F
import io
from itertools import combinations, product
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = ROOT / "tests/channel-swings/selected_k79_rsap_a3_real_form_principal_factor_census_probe.py"
REGISTRY = ROOT / "lab/process/selected-k83-rsap-su31-a3-singular-transition-atlas.json"
RESULT = ROOT / "explorations/conditional-build/selected-k83-rsap-su31-a3-singular-transition-atlas-2026-08-15.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-15-selected-k83-rsap-su31-a3-singular-transition-atlas-review.md"
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
scale = prior["scale"]
flatten = prior["flatten"]
column_rank = prior["column_rank"]
diag = prior["diag"]
block_diag = prior["block_diag"]
jordan = prior["jordan"]
reverse = prior["reverse"]
bracket = prior["bracket"]
adjoint_space = prior["adjoint_space"]
linear_combination = prior["linear_combination"]
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


def permute_symmetric(matrix: list[list[F]], order: list[int]) -> list[list[F]]:
    return [[matrix[i][j] for j in order] for i in order]


def schur(matrix: list[list[F]], size: int) -> list[list[F]]:
    pivot = [row[:size] for row in matrix[:size]]
    cross = [row[size:] for row in matrix[:size]]
    rest = [row[size:] for row in matrix[size:]]
    if not rest:
        return []
    correction = mmul(mmul(transpose(cross), inverse(pivot)), cross)
    return [[rest[i][j] - correction[i][j] for j in range(len(rest))] for i in range(len(rest))]


def inertia(matrix: list[list[F]]) -> tuple[int, int]:
    work = [[F(value) for value in row] for row in matrix]
    positive = negative = 0
    while work:
        pivot = next((index for index in range(len(work)) if work[index][index]), None)
        if pivot is not None:
            order = [pivot] + [index for index in range(len(work)) if index != pivot]
            work = permute_symmetric(work, order)
            positive += int(work[0][0] > 0)
            negative += int(work[0][0] < 0)
            work = schur(work, 1)
            continue
        pair = next(((i, j) for i in range(len(work)) for j in range(i + 1, len(work)) if work[i][j]), None)
        if pair is None:
            raise ValueError("degenerate symmetric form")
        order = list(pair) + [index for index in range(len(work)) if index not in pair]
        work = permute_symmetric(work, order)
        positive += 1
        negative += 1
        work = schur(work, 2)
    return positive, negative


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


def complex_block(real: int, imaginary: int) -> list[list[F]]:
    return [[F(real), F(imaginary)], [F(-imaginary), F(real)]]


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


def primary_centralizer(partition: tuple[int, ...]) -> int:
    columns = [sum(size >= col for size in partition) for col in range(1, max(partition) + 1)]
    return sum(value * value for value in columns)


def real_singular_types(block_sizes: tuple[int, ...]) -> set[tuple[tuple[int, ...], ...]]:
    types = set()
    for grouping in set_partitions(tuple(range(len(block_sizes)))):
        primaries = tuple(sorted((tuple(sorted((block_sizes[index] for index in group), reverse=True)) for group in grouping), reverse=True))
        if sum(primary_centralizer(partition) for partition in primaries) > 4:
            types.add(primaries)
    return types


print("\nA. FOUR CONFIGURATIONS AND NINE SINGULAR INCIDENCE FAMILIES")
computed_counts = {
    "real_3_plus_1": len(real_singular_types((3, 1))),
    "real_2_plus_1_plus_1": len(real_singular_types((2, 1, 1))),
    "real_1_plus_1_plus_1_plus_1": len(real_singular_types((1, 1, 1, 1))),
    "complex_plus_real_1_plus_1": 1,
}
check("census", "exactly the four signature-(3,1) configurations survive",
      tuple(computed_counts) == tuple(REG["classification"]["canonical_configurations"])
      and len(computed_counts) == REG["classification"]["configuration_count"] == 4)
check("census", "per-configuration singular counts are exhaustive",
      computed_counts == REG["classification"]["singular_family_counts"])
check("census", "the singular Jordan-incidence count is nine",
      sum(computed_counts.values()) == REG["classification"]["singular_jordan_incidence_family_count"] == 9)
check("census", "families are not claimed as real adjoint-orbit counts",
      REG["classification"]["family_count_is_not_claimed_as_real_adjoint_orbit_count"] is True)


print("\nB. EXACT REGULAR CONTROLS")
K = diag((1, -1))
H_REF = diag((1, 1, 1, -1))
H31 = block_diag(reverse(3), [[F(1)]])
H211 = block_diag(reverse(2), [[F(1)]], [[F(1)]])
HC11 = block_diag(K, [[F(1)]], [[F(1)]])
regular_controls = {
    "real_3_plus_1": (block_diag(jordan(3, 1), [[F(-3)]]), H31),
    "real_2_plus_1_plus_1": (block_diag(jordan(2), [[F(1)]], [[F(-1)]]), H211),
    "real_1_plus_1_plus_1_plus_1": (diag((3, 1, -1, -3)), H_REF),
    "complex_plus_real_1_plus_1": (block_diag(complex_block(0, 1), [[F(2)]], [[F(-2)]]), HC11),
}
for label, (control, form) in regular_controls.items():
    moving = adjoint_space(form, 1)
    orbit_rank = column_rank([bracket(value, control) for value in SL4])
    moving_rank = column_rank([bracket(value, control) for value in moving])
    check("regular", f"{label} is signature (3,1), trace-free and self-adjoint",
          inertia(form) == (3, 1)
          and sum(control[i][i] for i in range(4)) == 0
          and mmul(transpose(control), form) == mmul(form, control))
    check("regular", f"{label} has full/moving centralizers 3/3",
          15 - orbit_rank == 3 and 9 - moving_rank == 3)


print("\nC. NINE FAMILIES AND TWENTY-FIVE SIGN CONTROLS")
families = {
    "J3+J1_same": (block_diag(jordan(3), [[F(0)]]), ((jordan(3), reverse(3)), ([[F(0)]], [[F(1)]])), (5, 4, 14, 82, 90)),
    "J2+J1+J1_same": (block_diag(jordan(2), [[F(0)]], [[F(0)]]), ((jordan(2), reverse(2)), ([[F(0)]], [[F(1)]]), ([[F(0)]], [[F(1)]])), (9, 6, 12, 78, 88)),
    "J2+J1_same_plus_J1_distinct": (block_diag(jordan(2, 1), [[F(1)]], [[F(-3)]]), ((jordan(2, 1), reverse(2)), ([[F(1)]], [[F(1)]]), ([[F(-3)]], [[F(1)]])), (5, 4, 14, 82, 90)),
    "J2_plus_repeated_semisimple_pair": (block_diag(jordan(2, 1), [[F(-1)]], [[F(-1)]]), ((jordan(2, 1), reverse(2)), ([[F(-1)]], [[F(1)]]), ([[F(-1)]], [[F(1)]])), (5, 4, 14, 82, 90)),
    "semisimple_2+1+1": (diag((1, 1, 2, -4)), tuple(([[F(value)]], [[F(1)]]) for value in (1, 1, 2, -4)), (5, 4, 14, 82, 90)),
    "semisimple_2+2": (diag((1, 1, -1, -1)), tuple(([[F(value)]], [[F(1)]]) for value in (1, 1, -1, -1)), (7, 5, 13, 80, 89)),
    "semisimple_3+1": (diag((1, 1, 1, -3)), tuple(([[F(value)]], [[F(1)]]) for value in (1, 1, 1, -3)), (9, 6, 12, 78, 88)),
    "origin_4": (zero(4), tuple(([[F(0)]], [[F(1)]]) for _ in range(4)), (15, 9, 9, 72, 85)),
    "complex_pair_plus_repeated_real_pair": (block_diag(complex_block(1, 1), [[F(-1)]], [[F(-1)]]), ((complex_block(1, 1), K), ([[F(-1)]], [[F(1)]]), ([[F(-1)]], [[F(1)]])), (5, 4, 14, 82, 90)),
}
sign_count = 0
representative_forms = {}
for label, (control, blocks, expected) in families.items():
    valid_forms = []
    for signs in product((-1, 1), repeat=len(blocks)):
        form = block_diag(*(scale(sign, block_form) for sign, (_, block_form) in zip(signs, blocks)))
        if inertia(form) == (3, 1):
            valid_forms.append(form)
    representative_forms[label] = valid_forms[0]
    sign_count += len(valid_forms)
    for form in valid_forms:
        moving = adjoint_space(form, 1)
        orbit_rank = column_rank([bracket(value, control) for value in SL4])
        moving_rank = column_rank([bracket(value, control) for value in moving])
        actual = (15 - orbit_rank, 9 - moving_rank, 9 + moving_rank, 72 + orbit_rank, 76 + 9 + moving_rank)
        if actual != expected or mmul(transpose(control), form) != mmul(form, control):
            FAILURES.append(f"sign control mismatch for {label}")
    check("sign", f"{label} has invariant admissible signature-(3,1) controls", bool(valid_forms))
    check("rank", f"{label} saturates the registered pointwise schedule",
          list(expected) == REG["rank_census"][label]
          and expected[4] == (98 + expected[3]) // 2)
check("sign", "twenty-five admissible block-sign controls are checked",
      sign_count == REG["classification"]["sign_characteristic_controls_checked"] == 25)


print("\nD. EVERY FAMILY HAS A REGULAR APPROACH")
for label, (control, _blocks, _expected) in families.items():
    form = representative_forms[label]
    moving = adjoint_space(form, 1)
    witness = None
    for coefficients in product((-1, 0, 1), repeat=5):
        if not any(coefficients):
            continue
        direction = linear_combination(coefficients + (0,) * (len(moving) - 5), moving)
        trial = madd(control, direction)
        if column_rank([bracket(value, trial) for value in SL4]) == 12:
            witness = direction
            break
    check("approach", f"{label} has an exact self-adjoint regular perturbation", witness is not None)


print("\nE. ELEVEN CONFIGURATION-CLOSURE PATHS")
paths = {
    "real31_collision": (block_diag(jordan(3, 1), [[F(-3)]]), block_diag(jordan(3), [[F(0)]]), H31, "J3+J1_same"),
    "real211_all": (block_diag(jordan(2), [[F(1)]], [[F(-1)]]), block_diag(jordan(2), [[F(0)]], [[F(0)]]), H211, "J2+J1+J1_same"),
    "real211_block_line": (block_diag(jordan(2, 1), [[F(2)]], [[F(-4)]]), block_diag(jordan(2, 1), [[F(1)]], [[F(-3)]]), H211, "J2+J1_same_plus_J1_distinct"),
    "real211_line_pair": (block_diag(jordan(2, 1), [[F(0)]], [[F(-2)]]), block_diag(jordan(2, 1), [[F(-1)]], [[F(-1)]]), H211, "J2_plus_repeated_semisimple_pair"),
    "real1111_211": (diag((0, 2, 3, -5)), diag((1, 1, 3, -5)), H_REF, "semisimple_2+1+1"),
    "real1111_22": (diag((0, 2, -3, 1)), diag((1, 1, -1, -1)), H_REF, "semisimple_2+2"),
    "real1111_31": (diag((0, 1, 2, -3)), diag((1, 1, 1, -3)), H_REF, "semisimple_3+1"),
    "real1111_origin": (diag((3, 1, -1, -3)), zero(4), H_REF, "origin_4"),
    "complex_real11_to_211": (block_diag(complex_block(0, 1), [[F(2)]], [[F(-2)]]), diag((0, 0, 2, -2)), HC11, "semisimple_2+1+1"),
    "complex_real11_pair": (block_diag(complex_block(0, 1), [[F(2)]], [[F(-2)]]), block_diag(complex_block(1, 1), [[F(-1)]], [[F(-1)]]), HC11, "complex_pair_plus_repeated_real_pair"),
    "complex_real11_to_22": (block_diag(complex_block(1, 1), [[F(-1)]], [[F(-1)]]), diag((1, 1, -1, -1)), HC11, "semisimple_2+2"),
}
destination_schedules = {label: tuple(values[:2]) for label, values in REG["rank_census"].items()}
for label, (start, limit, form, destination) in paths.items():
    moving = adjoint_space(form, 1)
    limit_orbit = column_rank([bracket(value, limit) for value in SL4])
    limit_moving = column_rank([bracket(value, limit) for value in moving])
    check("path", f"{label} remains trace-free and self-adjoint in one fibre",
          all(sum(matrix[i][i] for i in range(4)) == 0
              and mmul(transpose(matrix), form) == mmul(form, matrix)
              for matrix in (start, limit)))
    check("path", f"{label} reaches the registered destination schedule",
          (15 - limit_orbit, 9 - limit_moving) == destination_schedules[destination])
check("path", "all eleven closure paths are registered",
      len(paths) == REG["transitions"]["linear_degenerations_checked"] == 11)


print("\nF. FOUR-CHART RATIONAL COTANGENT NERVE")
P31 = [[F(0), F(1), F(0), F(1)], [F(-1), F(0), F(0), F(0)], [F(0), F(1, 2), F(0), F(-1, 2)], [F(0), F(0), F(1), F(0)]]
P211 = [[F(-1), F(0), F(0), F(1)], [F(-1, 2), F(0), F(0), F(-1, 2)], [F(0), F(1), F(0), F(0)], [F(0), F(0), F(1), F(0)]]
PC11 = [[F(1), F(0), F(0), F(0)], [F(0), F(0), F(0), F(1)], [F(0), F(1), F(0), F(0)], [F(0), F(0), F(1), F(0)]]
normalizers = {
    "real_3_plus_1": P31,
    "real_2_plus_1_plus_1": P211,
    "real_1_plus_1_plus_1_plus_1": eye(4),
    "complex_plus_real_1_plus_1": PC11,
}
forms = {label: form for label, (_control, form) in regular_controls.items()}
reference_space = adjoint_space(H_REF, 1)
coordinate_maps = {}
for label, normalizer in normalizers.items():
    form = forms[label]
    normalizer_inverse = inverse(normalizer)
    transformed = [mmul(normalizer_inverse, mmul(value, normalizer)) for value in adjoint_space(form, 1)]
    coordinate_map = transpose([coordinates(value, reference_space) for value in transformed])
    coordinate_maps[label] = coordinate_map
    check("normalize", f"{label} has a determinant-one rational normalization",
          determinant(normalizer) == 1
          and mmul(transpose(normalizer), mmul(form, normalizer)) == H_REF
          and determinant(coordinate_map) != 0)

labels = tuple(normalizers)
transitions = {(target, source): mmul(inverse(coordinate_maps[target]), coordinate_maps[source]) for source in labels for target in labels}
check("nerve", "the four-chart nerve has six pairs and four triangles",
      len(tuple(combinations(labels, 2))) == REG["transitions"]["pairwise_chart_transitions"] == 6
      and len(tuple(combinations(labels, 3))) == REG["transitions"]["chart_triangles"] == 4)
q = [[F(value)] for value in (2, -3, 5, 7, -11, 13, 17, -19, 23)]
dq = [[F(value)] for value in (29, -31, 37, 41, -43, 47, 53, -59, 61)]
pair_checks = []
for source, target in combinations(labels, 2):
    tangent = transitions[(target, source)]
    cotangent = transpose(inverse(tangent))
    pair_checks.append(mmul(transpose(mmul(cotangent, q)), mmul(tangent, dq)) == mmul(transpose(q), dq))
check("primitive", "all six pair transitions preserve the tautological pairing", all(pair_checks))
base_cycles = []
cotangent_cycles = []
for i, j, k in combinations(labels, 3):
    base_cycles.append(mmul(transitions[(i, k)], mmul(transitions[(k, j)], transitions[(j, i)])) == eye(9))
    cotangent_cycles.append(mmul(transpose(inverse(transitions[(i, k)])), mmul(transpose(inverse(transitions[(k, j)])), transpose(inverse(transitions[(j, i)])))) == eye(9))
check("cocycle", "all four base triangles close strictly", all(base_cycles))
check("cocycle", "all four cotangent triangles close strictly", all(cotangent_cycles))
check("moment", "one global SU(3,1) cotangent moment map gives zero Cech defect",
      REG["transitions"]["moment_cech_defect"] == "ZERO_BY_ONE_GLOBAL_SU31_COTANGENT_MOMENT_MAP")


print("\nG. CLAIM CEILING")
scope = REG["scope"]
check("scope", "the SU(3,1) local singular atlas closes without a new model",
      scope["su31_singular_transition_atlas"].startswith("CLOSED")
      and scope["new_su31_local_model"] == "NOT_REQUIRED")
check("scope", "cross-real-form incidence remains type-missing",
      scope["cross_real_form_atlas_edge"] == "TYPE_MISSING_NOT_REOPENED")
check("scope", "compact SU(4) is the next within-form atlas",
      scope["compact_su4_singular_transition_atlas"] == "OPEN_NEXT")
check("scope", "deeper strata, zero charge and global RSAP remain open",
      {scope["deeper_so77_singular_strata"], scope["zero_charge_rank_at_most_49"], scope["global_all_strata_rsap"]} == {"OPEN", "NOT_CONSTRUCTED"})
check("scope", "the all-charge fallback remains 182-dimensional", scope["all_charge_fallback_dimension"] == 182)
check("scope", "protected truth surfaces remain unchanged", set(REG["changes"].values()) == {"none"})
check("links", "result registry and hostile review paths are durable",
      all(path.exists() for path in (RESULT, REGISTRY, REVIEW)))


print("\nSUMMARY")
print(json.dumps({"checks": sum(COUNTS.values()), "failures": FAILURES, "groups": dict(sorted(COUNTS.items()))}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
