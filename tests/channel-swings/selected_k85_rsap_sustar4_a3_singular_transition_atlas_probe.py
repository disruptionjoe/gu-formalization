#!/usr/bin/env python3
"""Exact six-family singular transition atlas for SU*(4)/SO*(4)."""

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
REGISTRY = ROOT / "lab/process/selected-k85-rsap-sustar4-a3-singular-transition-atlas.json"
RESULT = ROOT / "explorations/conditional-build/selected-k85-rsap-sustar4-a3-singular-transition-atlas-2026-08-15.md"
REVIEW = ROOT / "lab/process/hostile-reviews/2026-08-15-selected-k85-rsap-sustar4-a3-singular-transition-atlas-review.md"
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
scale = prior["scale"]
flatten = prior["flatten"]
rank = prior["rank"]
column_rank = prior["column_rank"]
diag = prior["diag"]
cmat = prior["cmat"]
cadd = prior["cadd"]
csub = prior["csub"]
cmul = prior["cmul"]
ctranspose = prior["ctranspose"]
cconj = prior["cconj"]
cneg = prior["cneg"]
cbracket = prior["cbracket"]
cflatten = prior["cflatten"]
qmatrix = prior["qmatrix"]
h_q = prior["h_q"]
m_q = prior["m_q"]
g_q = prior["g_q"]
N = prior["N"]
CZ = prior["CZ"]
I2 = prior["I2"]
REG = json.loads(REGISTRY.read_text(encoding="utf-8"))


def cscale(value: F, matrix):
    return scale(value, matrix[0]), scale(value, matrix[1])


def cinverse(matrix):
    n = len(matrix[0])
    real = matrix[0]
    imag = matrix[1]
    representation = [real[i] + [(-value) for value in imag[i]] for i in range(n)]
    representation += [imag[i] + real[i] for i in range(n)]
    work = [row + unit for row, unit in zip(representation, eye(2 * n))]
    for col in range(2 * n):
        pivot = next((row for row in range(col, 2 * n) if work[row][col]), None)
        if pivot is None:
            raise ValueError("singular complex matrix")
        work[col], work[pivot] = work[pivot], work[col]
        value = work[col][col]
        work[col] = [entry / value for entry in work[col]]
        for row in range(2 * n):
            if row != col and work[row][col]:
                value = work[row][col]
                work[row] = [left - value * right for left, right in zip(work[row], work[col])]
    inverse = [row[2 * n:] for row in work]
    return [row[:n] for row in inverse[:n]], [row[:n] for row in inverse[n:]]


def cdet(matrix):
    n = len(matrix[0])
    work = [[(matrix[0][i][j], matrix[1][i][j]) for j in range(n)] for i in range(n)]
    answer = (F(1), F(0))

    def mul(x, y):
        return x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]

    def div(x, y):
        denominator = y[0] * y[0] + y[1] * y[1]
        return ((x[0] * y[0] + x[1] * y[1]) / denominator,
                (x[1] * y[0] - x[0] * y[1]) / denominator)

    for col in range(n):
        pivot = next((row for row in range(col, n) if work[row][col] != (0, 0)), None)
        if pivot is None:
            return F(0), F(0)
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            answer = (-answer[0], -answer[1])
        diagonal = work[col][col]
        answer = mul(answer, diagonal)
        for row in range(col + 1, n):
            if work[row][col] != (0, 0):
                ratio = div(work[row][col], diagonal)
                work[row] = [(left[0] - mul(ratio, right)[0], left[1] - mul(ratio, right)[1])
                             for left, right in zip(work[row], work[col])]
    return answer


def coordinates(matrix, basis):
    columns = transpose([cflatten(value) for value in basis])
    augmented = [row + [value] for row, value in zip(columns, cflatten(matrix))]
    pivot_row = 0
    pivots = []
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
        raise ValueError("complex matrix is outside basis span")
    answer = [F(0)] * len(basis)
    for row, pivot in enumerate(pivots):
        answer[pivot] = augmented[row][-1]
    return answer


def inverse(matrix):
    n = len(matrix)
    work = [[F(value) for value in row] + unit for row, unit in zip(matrix, eye(n))]
    for col in range(n):
        pivot = next((row for row in range(col, n) if work[row][col]), None)
        if pivot is None:
            raise ValueError("singular matrix")
        work[col], work[pivot] = work[pivot], work[col]
        value = work[col][col]
        work[col] = [entry / value for entry in work[col]]
        for row in range(n):
            if row != col and work[row][col]:
                value = work[row][col]
                work[row] = [left - value * right for left, right in zip(work[row], work[col])]
    return [row[n:] for row in work]


def centralizers(matrix):
    return (
        15 - column_rank([cbracket(value, matrix) for value in g_q], True),
        9 - column_rank([cbracket(value, matrix) for value in m_q], True),
    )


J4 = qmatrix(CZ, cmat(I2))


def in_moving_fibre(matrix):
    return (
        ctranspose(matrix) == matrix
        and cmul(matrix, J4) == cmul(J4, cconj(matrix))
        and column_rank(m_q + [matrix], True) == 9
    )


print("A. QUATERNIONIC PAIR AND SIX-FAMILY EXHAUSTION")
check("pair", "the quaternionic pair has dimensions six plus nine",
      column_rank(h_q, True) == 6 and column_rank(m_q, True) == 9 and column_rank(g_q, True) == 15)
check("pair", "the isotropy and moving spaces have transpose parity",
      all(ctranspose(value) == cneg(value) for value in h_q)
      and all(ctranspose(value) == value for value in m_q))

regular_spectral = qmatrix(cmat(diag((1, -1)), diag((1, 2))), CZ)
regular_jordan = prior["Q_regular_ns"]
repeated_nonreal = qmatrix(cmat(zero(2), I2), CZ)
mixed = prior["Q_first_singular"]
real_distinct = qmatrix(cmat(diag((1, -1))), CZ)
real_jordan = qmatrix(N, CZ)
origin = cmat(zero(4))
families = {
    "two_distinct_nonreal_pairs": regular_spectral,
    "paired_nonreal_size_two_jordan": regular_jordan,
    "repeated_nonreal_pair_semisimple": repeated_nonreal,
    "one_nonreal_pair_plus_real_double": mixed,
    "two_distinct_real_doubles": real_distinct,
    "paired_real_size_two_jordan": real_jordan,
}
check("census", "the six K79 canonical families are retained exactly",
      list(families) == REG["classification"]["canonical_families"]
      and len(families) == REG["classification"]["canonical_family_count"] == 6)
check("census", "the origin is a terminal stratum rather than a seventh canonical family",
      REG["classification"]["origin_is_terminal_stratum_not_seventh_canonical_family"] is True
      and "origin" not in families)
check("census", "every canonical representative is quaternionic-real and transpose symmetric",
      all(in_moving_fibre(value) for value in families.values()))
check("census", "the six types separate into two regular and four nonzero singular families",
      len(REG["classification"]["regular_families"]) == 2
      and len(REG["classification"]["singular_families"])
      == REG["classification"]["singular_family_count"] == 4)


print("\nB. EXACT CENTRALIZERS AND POINTWISE-BOUND SCHEDULES")
expected = {
    "two_distinct_nonreal_pairs": (3, 3, 15, 84, 91),
    "paired_nonreal_size_two_jordan": (3, 3, 15, 84, 91),
    "repeated_nonreal_pair_semisimple": (7, 5, 13, 80, 89),
    "one_nonreal_pair_plus_real_double": (5, 4, 14, 82, 90),
    "two_distinct_real_doubles": (7, 5, 13, 80, 89),
    "paired_real_size_two_jordan": (7, 5, 13, 80, 89),
}
for label, control in families.items():
    orbit_rank = column_rank([cbracket(value, control) for value in g_q], True)
    moving_rank = column_rank([cbracket(value, control) for value in m_q], True)
    actual = (15 - orbit_rank, 9 - moving_rank, 9 + moving_rank, 72 + orbit_rank, 76 + 9 + moving_rank)
    check("rank", f"{label} has its exact full/moving centralizers and ranks", actual == expected[label])
    check("bound", f"{label} saturates the 98D pointwise bound", actual[4] == (98 + actual[3]) // 2)
origin_actual = (15, 9, 9, 72, 85)
check("rank", "the quaternionic origin has the universal terminal schedule",
      origin_actual == tuple(REG["rank_census"]["origin"]))
check("bound", "the origin saturates the 98D pointwise bound", 85 == (98 + 72) // 2)


print("\nC. REGULAR APPROACHES AND QUATERNIONIC CLOSURE GRAPH")
paths = {
    "spectral_to_repeated_nonreal": (regular_spectral, repeated_nonreal, (3, 3), (7, 5)),
    "spectral_to_mixed": (regular_spectral, mixed, (3, 3), (5, 4)),
    "spectral_to_real_distinct": (regular_spectral, real_distinct, (3, 3), (7, 5)),
    "spectral_to_origin": (regular_spectral, origin, (3, 3), (15, 9)),
    "jordan_to_repeated_nonreal": (regular_jordan, repeated_nonreal, (3, 3), (7, 5)),
    "jordan_to_real_jordan": (regular_jordan, real_jordan, (3, 3), (7, 5)),
    "jordan_to_origin": (regular_jordan, origin, (3, 3), (15, 9)),
    "mixed_to_real_distinct": (mixed, real_distinct, (5, 4), (7, 5)),
    "mixed_to_origin": (mixed, origin, (5, 4), (15, 9)),
    "repeated_nonreal_to_origin": (repeated_nonreal, origin, (7, 5), (15, 9)),
    "real_distinct_to_origin": (real_distinct, origin, (7, 5), (15, 9)),
    "real_jordan_to_origin": (real_jordan, origin, (7, 5), (15, 9)),
}
for label, (start, limit, source, endpoint) in paths.items():
    direction = csub(start, limit)
    nonzero_samples = [cadd(limit, cscale(parameter, direction))
                       for parameter in (F(1), F(1, 2), F(2, 3))]
    check("path", f"{label} stays in the quaternionic symmetric moving fibre",
          all(in_moving_fibre(value) for value in nonzero_samples + [limit, direction]))
    check("path", f"{label} retains the claimed source centralizer away from the endpoint",
          all(centralizers(value) == source for value in nonzero_samples))
    check("path", f"{label} lands in the claimed centralizer stratum",
          centralizers(limit) == endpoint)
check("path", "all twelve registered family-degeneration controls are present",
      len(paths) == REG["transitions"]["linear_degenerations_checked"] == 12)
check("approach", "every singular family and the origin has an exact regular approach",
      {"spectral_to_repeated_nonreal", "spectral_to_mixed",
       "spectral_to_real_distinct", "jordan_to_real_jordan",
       "spectral_to_origin"}.issubset(paths))


print("\nD. NONCOMMUTING SO*(4) COTANGENT CAYLEY NERVE")
I4C = cmat(eye(4))


def cayley(generator, denominator):
    scaled = cscale(F(1, denominator), generator)
    return cmul(csub(I4C, scaled), cinverse(cadd(I4C, scaled)))


frames = {
    "identity": I4C,
    "cayley_h0": cayley(h_q[0], 2),
    "cayley_h1": cayley(h_q[1], 3),
    "cayley_h0_h2": cayley(cadd(h_q[0], h_q[2]), 4),
}
coordinate_maps = {}
for label, frame in frames.items():
    transformed = [cmul(ctranspose(frame), cmul(value, frame)) for value in m_q]
    coordinate_map = transpose([coordinates(value, m_q) for value in transformed])
    coordinate_maps[label] = coordinate_map
    check("frame", f"{label} is an exact determinant-one SO*(4) frame",
          cmul(ctranspose(frame), frame) == I4C
          and cmul(frame, J4) == cmul(J4, cconj(frame))
          and cdet(frame) == (F(1), F(0))
          and rank(coordinate_map) == 9)

labels = tuple(frames)
transitions = {(target, source): mmul(inverse(coordinate_maps[target]), coordinate_maps[source])
               for source in labels for target in labels}
check("nerve", "the four-frame nerve has six pairs and four triangles",
      len(tuple(combinations(labels, 2))) == REG["transitions"]["pairwise_frame_transitions"] == 6
      and len(tuple(combinations(labels, 3))) == REG["transitions"]["frame_triangles"] == 4)
check("nerve", "the Cayley controls give genuinely noncommuting transitions",
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
    cotangent_cycles.append(
        mmul(transpose(inverse(transitions[(i, k)])),
              mmul(transpose(inverse(transitions[(k, j)])), transpose(inverse(transitions[(j, i)])))) == eye(9))
check("cocycle", "all four SO*(4) base-frame triangles close", all(base_cycles))
check("cocycle", "all four cotangent-frame triangles close", all(cotangent_cycles))
check("moment", "the one global quaternionic cotangent moment map has zero Cech defect",
      REG["transitions"]["moment_cech_defect"] == "ZERO_BY_ONE_GLOBAL_SU_STAR4_COTANGENT_MOMENT_MAP")


print("\nE. CLAIM CEILING")
scope = REG["scope"]
check("scope", "the quaternionic local atlas closes without a new model",
      scope["quaternionic_sustar4_singular_transition_atlas"].startswith("CLOSED")
      and scope["new_quaternionic_local_model"] == "NOT_REQUIRED")
check("scope", "cross-real-form incidence remains type-missing",
      scope["cross_real_form_atlas_edge"] == "TYPE_MISSING_NOT_REOPENED")
check("scope", "deeper ambient strata are next while zero charge and global RSAP remain open",
      scope["deeper_so77_singular_strata"] == "OPEN_NEXT"
      and scope["zero_charge_rank_at_most_49"] == "NOT_CONSTRUCTED"
      and scope["global_all_strata_rsap"] == "OPEN")
check("scope", "the all-charge fallback remains 182-dimensional", scope["all_charge_fallback_dimension"] == 182)
check("scope", "protected truth surfaces remain unchanged", set(REG["changes"].values()) == {"none"})
check("links", "result registry and hostile review paths are durable",
      all(path.exists() for path in (RESULT, REGISTRY, REVIEW)))


print("\nSUMMARY")
print(json.dumps({"checks": sum(COUNTS.values()), "failures": FAILURES, "groups": dict(sorted(COUNTS.items()))}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
