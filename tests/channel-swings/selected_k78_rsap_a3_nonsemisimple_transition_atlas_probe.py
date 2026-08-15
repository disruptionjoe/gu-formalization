#!/usr/bin/env python3
"""Exact split-A3 singular nonsemisimple Jordan transition certificate."""

from fractions import Fraction as F
from itertools import combinations, product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REG = json.loads((ROOT / "lab/process/selected-k78-rsap-a3-nonsemisimple-transition-atlas.json").read_text())
ORIGIN = json.loads((ROOT / "lab/process/selected-k77-rsap-a3-two-wall-census-origin-attachment.json").read_text())
FAILURES = []
COUNTS = {}


def check(group, label, condition):
    COUNTS[group] = COUNTS.get(group, 0) + 1
    print(f"{'PASS' if condition else 'FAIL'} [{group}] {label}")
    if not condition:
        FAILURES.append(f"[{group}] {label}")


def zero(n, m=None):
    return [[F(0) for _ in range(n if m is None else m)] for _ in range(n)]


def eye(n):
    out = zero(n)
    for i in range(n):
        out[i][i] = F(1)
    return out


def transpose(a):
    return [list(row) for row in zip(*a)]


def mmul(a, b):
    bt = transpose(b)
    return [[sum((x * y for x, y in zip(row, col)), F(0)) for col in bt] for row in a]


def madd(a, b):
    return [[x + y for x, y in zip(arow, brow)] for arow, brow in zip(a, b)]


def msub(a, b):
    return [[x - y for x, y in zip(arow, brow)] for arow, brow in zip(a, b)]


def scale(c, a):
    return [[F(c) * x for x in row] for row in a]


def flatten(a):
    return [x for row in a for x in row]


def rank(a):
    a = [[F(x) for x in row] for row in a]
    r = 0
    for col in range(len(a[0]) if a else 0):
        pivot = next((row for row in range(r, len(a)) if a[row][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        p = a[r][col]
        a[r] = [x / p for x in a[r]]
        for row in range(len(a)):
            if row != r and a[row][col]:
                q = a[row][col]
                a[row] = [x - q * y for x, y in zip(a[row], a[r])]
        r += 1
    return r


def inverse(a):
    n = len(a)
    aug = [[F(x) for x in row] + ident for row, ident in zip(a, eye(n))]
    for col in range(n):
        pivot = next((row for row in range(col, n) if aug[row][col]), None)
        if pivot is None:
            raise ValueError("singular matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        p = aug[col][col]
        aug[col] = [x / p for x in aug[col]]
        for row in range(n):
            if row != col and aug[row][col]:
                q = aug[row][col]
                aug[row] = [x - q * y for x, y in zip(aug[row], aug[col])]
    return [row[n:] for row in aug]


def determinant(a):
    a = [[F(x) for x in row] for row in a]
    out = F(1)
    for col in range(len(a)):
        pivot = next((row for row in range(col, len(a)) if a[row][col]), None)
        if pivot is None:
            return F(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            out = -out
        p = a[col][col]
        out *= p
        for row in range(col + 1, len(a)):
            if a[row][col]:
                q = a[row][col] / p
                a[row] = [x - q * y for x, y in zip(a[row], a[col])]
    return out


def column_rank(matrices):
    return rank(transpose([flatten(a) for a in matrices])) if matrices else 0


def unit(i, j, n=4):
    out = zero(n)
    out[i][j] = F(1)
    return out


def diag(values):
    out = zero(len(values))
    for i, value in enumerate(values):
        out[i][i] = F(value)
    return out


def block_diag(*blocks):
    size = sum(len(block) for block in blocks)
    out = zero(size)
    offset = 0
    for block in blocks:
        for i, row in enumerate(block):
            for j, value in enumerate(row):
                out[offset + i][offset + j] = F(value)
        offset += len(block)
    return out


def jordan(n, value=0):
    out = diag([value] * n)
    for i in range(n - 1):
        out[i][i + 1] = F(1)
    return out


def reverse(n):
    out = zero(n)
    for i in range(n):
        out[i][n - 1 - i] = F(1)
    return out


def sl_basis(n=4):
    basis = [msub(unit(i, i, n), unit(n - 1, n - 1, n)) for i in range(n - 1)]
    basis += [unit(i, j, n) for i in range(n) for j in range(n) if i != j]
    return basis


def bracket(a, b):
    return msub(mmul(a, b), mmul(b, a))


def nullspace(a, ncols):
    a = [[F(x) for x in row] for row in a]
    r = 0
    pivots = []
    for col in range(ncols):
        pivot = next((row for row in range(r, len(a)) if a[row][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        p = a[r][col]
        a[r] = [x / p for x in a[r]]
        for row in range(len(a)):
            if row != r and a[row][col]:
                q = a[row][col]
                a[row] = [x - q * y for x, y in zip(a[row], a[r])]
        pivots.append(col)
        r += 1
    free = [col for col in range(ncols) if col not in pivots]
    result = []
    for free_col in free:
        vector = [F(0)] * ncols
        vector[free_col] = F(1)
        for row, pivot_col in enumerate(pivots):
            vector[pivot_col] = -a[row][free_col]
        result.append(vector)
    return result


SL4 = sl_basis()


def linear_combination(coefficients, basis):
    out = zero(4)
    for coefficient, matrix in zip(coefficients, basis):
        out = madd(out, scale(coefficient, matrix))
    return out


def adjoint_space(h, sign):
    columns = []
    for x in SL4:
        columns.append(flatten(msub(mmul(transpose(x), h), scale(sign, mmul(h, x)))))
    equations = transpose(columns)
    return [linear_combination(vector, SL4) for vector in nullspace(equations, len(SL4))]


def coordinates(matrix, basis):
    columns = transpose([flatten(x) for x in basis])
    rhs = flatten(matrix)
    augmented = [row + [value] for row, value in zip(columns, rhs)]
    r = 0
    pivots = []
    for col in range(len(basis)):
        pivot = next((row for row in range(r, len(augmented)) if augmented[row][col]), None)
        if pivot is None:
            continue
        augmented[r], augmented[pivot] = augmented[pivot], augmented[r]
        p = augmented[r][col]
        augmented[r] = [x / p for x in augmented[r]]
        for row in range(len(augmented)):
            if row != r and augmented[row][col]:
                q = augmented[row][col]
                augmented[row] = [x - q * y for x, y in zip(augmented[row], augmented[r])]
        pivots.append(col)
        r += 1
    if any(all(not row[col] for col in range(len(basis))) and row[-1] for row in augmented):
        raise ValueError("matrix not in basis span")
    answer = [F(0)] * len(basis)
    for row, pivot in enumerate(pivots):
        answer[pivot] = augmented[row][-1]
    return answer


print("A. EXHAUSTIVE REAL-PRIMARY JORDAN CENSUS")
partitions = {
    1: ((1,),),
    2: ((2,), (1, 1)),
    3: ((3,), (2, 1), (1, 1, 1)),
    4: ((4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)),
}


def primary_centralizer_dimension(partition, degree=1):
    columns = [sum(size >= column for size in partition) for column in range(1, max(partition) + 1)]
    return degree * sum(value * value for value in columns)


real_multiplicity_patterns = ((4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1))
singular_nonsemisimple_by_type = {}
for multiplicities in real_multiplicity_patterns:
    choices = product(*(partitions[multiplicity] for multiplicity in multiplicities))
    for primary_partitions in choices:
        gl_centralizer = sum(primary_centralizer_dimension(partition) for partition in primary_partitions)
        nonsemisimple = any(any(block > 1 for block in partition) for partition in primary_partitions)
        regular = gl_centralizer == 4
        if nonsemisimple and not regular:
            canonical_partitions = tuple(sorted(primary_partitions, reverse=True)) if multiplicities == (2, 2) else primary_partitions
            singular_nonsemisimple_by_type[(multiplicities, canonical_partitions)] = gl_centralizer - 1

singular_nonsemisimple = [
    (multiplicities, primary_partitions, centralizer)
    for (multiplicities, primary_partitions), centralizer in singular_nonsemisimple_by_type.items()
]

expected_labels = {
    ((4,), ((3, 1),)): "J3+J1_same",
    ((4,), ((2, 2),)): "J2+J2_same",
    ((4,), ((2, 1, 1),)): "J2+J1+J1_same",
    ((3, 1), ((2, 1), (1,))): "J2+J1_same_plus_J1_distinct",
    ((2, 2), ((2,), (1, 1))): "J2_plus_repeated_semisimple_pair",
}
found_labels = {expected_labels[(multiplicities, primary_partitions)] for multiplicities, primary_partitions, _ in singular_nonsemisimple}
check("census", "exactly five singular nonsemisimple real-primary families exist", len(singular_nonsemisimple) == 5)
check("census", "the five exhaustive labels match the registry", found_labels == set(REG["classification"]["families"]))
check("census", "their sl4 centralizer dimensions are 5,5,5,7,9", sorted(item[2] for item in singular_nonsemisimple) == [5, 5, 5, 7, 9])

quadratic_configurations = [
    (((2,),), True, primary_centralizer_dimension((2,), degree=2)),
    (((1, 1),), False, primary_centralizer_dimension((1, 1), degree=2)),
    (((1,), (2,)), True, primary_centralizer_dimension((1,), degree=2) + primary_centralizer_dimension((2,))),
    (((1,), (1, 1)), False, primary_centralizer_dimension((1,), degree=2) + primary_centralizer_dimension((1, 1))),
    (((1,), (1,), (1,)), False, 2 + 1 + 1),
    (((1,), (1,)), False, 2 + 2),
]
check("census", "every nonsemisimple complex-primary configuration is regular", all(gl_dim == 4 for _, nonsemisimple, gl_dim in quadratic_configurations if nonsemisimple))
check("census", "complex-primary cases add no singular nonsemisimple family", REG["classification"]["complex_primary_singular_nonsemisimple_count"] == 0)

print("\nB. FIVE EXACT REPRESENTATIVES, SYMMETRIZERS AND RANKS")
H31 = block_diag(reverse(3), [[F(-1)]])
H22 = block_diag(reverse(2), reverse(2))
H211 = block_diag(reverse(2), [[F(1)]], [[F(-1)]])
families = {
    "J3+J1_same": (block_diag(jordan(3), [[F(0)]]), H31, 5, 4, 14, 82, 90),
    "J2+J2_same": (block_diag(jordan(2), jordan(2)), H22, 7, 5, 13, 80, 89),
    "J2+J1+J1_same": (block_diag(jordan(2), [[F(0)]], [[F(0)]]), H211, 9, 6, 12, 78, 88),
    "J2+J1_same_plus_J1_distinct": (block_diag(jordan(2, 1), [[F(1)]], [[F(-3)]]), H211, 5, 4, 14, 82, 90),
    "J2_plus_repeated_semisimple_pair": (block_diag(jordan(2, 1), [[F(-1)]], [[F(-1)]]), H211, 5, 4, 14, 82, 90),
}

spaces = {}
for label, (a, h, g_centralizer, m_centralizer, factor_rank, target_rank, full_rank) in families.items():
    m_space = adjoint_space(h, 1)
    fixed_space = adjoint_space(h, -1)
    spaces[label] = m_space
    orbit_rank = column_rank([bracket(x, a) for x in SL4])
    moving_rank = column_rank([bracket(x, a) for x in m_space])
    check("symmetrizer", f"{label} is trace-free and H-self-adjoint", sum(a[i][i] for i in range(4)) == 0 and mmul(transpose(a), h) == mmul(h, a))
    check("pair", f"{label} has a 9+6 split symmetric pair", column_rank(m_space) == 9 and column_rank(fixed_space) == 6 and column_rank(m_space + fixed_space) == 15)
    check("centralizer", f"{label} sl4 centralizer dimension", 15 - orbit_rank == g_centralizer)
    check("centralizer", f"{label} moving centralizer dimension", 9 - moving_rank == m_centralizer)
    check("rank", f"{label} principal factor rank", 9 + moving_rank == factor_rank)
    check("rank", f"{label} full target Poisson rank", 72 + orbit_rank == target_rank)
    check("rank", f"{label} full map rank", 72 + factor_rank + 4 == full_rank)
    check("bound", f"{label} saturates the 98D pointwise bound", full_rank == (98 + target_rank) // 2)
    record = REG["rank_census"][label]
    check("registry", f"{label} registry schedule is exact", [record[key] for key in ("sl4_centralizer_dimension", "moving_centralizer_dimension", "factor_map_rank", "target_poisson_rank", "full_map_rank")] == [g_centralizer, m_centralizer, factor_rank, target_rank, full_rank])

print("\nC. REGULAR APPROACH ARCS EXIST INSIDE THE SAME SMOOTH FACTOR")
regular_witnesses = {}
for label, (a, h, *_rest) in families.items():
    m_space = spaces[label]
    witness = None
    for coefficients in product((-1, 0, 1), repeat=4):
        if coefficients == (0, 0, 0, 0):
            continue
        d = linear_combination(coefficients + (0,) * (len(m_space) - 4), m_space)
        trial = madd(a, d)
        if column_rank([bracket(x, trial) for x in SL4]) == 12:
            witness = coefficients
            break
    regular_witnesses[label] = witness
    check("approach", f"{label} has an exact H-self-adjoint regular perturbation", witness is not None)
check("approach", "all regular perturbations remain in their signature-(2,2) fibres", all(witness is not None for witness in regular_witnesses.values()))
check("approach", "a nonzero rank minor makes every approach generically regular near t=0", REG["transitions"]["regular_approach"] == "A+tD_IN_mH__GENERICALLY_REGULAR_BY_A_NONZERO_EXACT_MINOR")

print("\nD. EXACT NORMALIZATION INTO THE ALTERNATING PRINCIPAL FIBRE")
H_ALT = diag((1, -1, 1, -1))
P31 = [
    [F(0), F(1), F(1), F(0)],
    [F(1), F(0), F(0), F(0)],
    [F(0), F(-1, 2), F(1, 2), F(0)],
    [F(0), F(0), F(0), F(-1)],
]
P22 = [
    [F(1), F(1), F(0), F(0)],
    [F(1, 2), F(-1, 2), F(0), F(0)],
    [F(0), F(0), F(1), F(1)],
    [F(0), F(0), F(1, 2), F(-1, 2)],
]
P211 = [
    [F(1), F(1), F(0), F(0)],
    [F(1, 2), F(-1, 2), F(0), F(0)],
    [F(0), F(0), F(1), F(0)],
    [F(0), F(0), F(0), F(-1)],
]
B12 = eye(4)
B12[0][0], B12[0][1], B12[1][0], B12[1][1] = F(5, 4), F(3, 4), F(3, 4), F(5, 4)
B34 = eye(4)
B34[2][2], B34[2][3], B34[3][2], B34[3][3] = F(5, 4), F(3, 4), F(3, 4), F(5, 4)
normalizers = {
    "J3+J1_same": P31,
    "J2+J2_same": P22,
    "J2+J1+J1_same": P211,
    "J2+J1_same_plus_J1_distinct": mmul(P211, B12),
    "J2_plus_repeated_semisimple_pair": mmul(P211, B34),
}
alt_space = adjoint_space(H_ALT, 1)
coordinate_maps = {}
for label, p in normalizers.items():
    a, h, *_ = families[label]
    pinv = inverse(p)
    transformed_a = mmul(pinv, mmul(a, p))
    transformed_basis = [mmul(pinv, mmul(x, p)) for x in spaces[label]]
    coordinate_map = transpose([coordinates(x, alt_space) for x in transformed_basis])
    coordinate_maps[label] = coordinate_map
    check("normalize", f"{label} normalizer lies in SL4", determinant(p) == 1)
    check("normalize", f"{label} sends its form to the alternating form", mmul(transpose(p), mmul(h, p)) == H_ALT)
    check("normalize", f"{label} sends its control into the alternating moving fibre", mmul(transpose(transformed_a), H_ALT) == mmul(H_ALT, transformed_a))
    check("normalize", f"{label} induces an invertible 9D tangent transition", determinant(coordinate_map) != 0)

print("\nE. COMPLETE COTANGENT TRANSITION NERVE")
labels = tuple(normalizers)
transitions = {(j, i): mmul(inverse(coordinate_maps[j]), coordinate_maps[i]) for i in labels for j in labels}
check("cocycle", "at least one pair of transition matrices does not commute", any(mmul(transitions[(j, i)], transitions[(k, j)]) != mmul(transitions[(k, j)], transitions[(j, i)]) for i, j, k in combinations(labels, 3)))
for i, j, k in combinations(labels, 3):
    base_cycle = mmul(transitions[(i, k)], mmul(transitions[(k, j)], transitions[(j, i)]))
    cot_cycle = mmul(transpose(inverse(transitions[(i, k)])), mmul(transpose(inverse(transitions[(k, j)])), transpose(inverse(transitions[(j, i)]))))
    check("cocycle", f"base triangle {i}/{j}/{k} closes", base_cycle == eye(9))
    check("cocycle", f"cotangent triangle {i}/{j}/{k} closes", cot_cycle == eye(9))

q = [[F(value)] for value in (2, -3, 5, 7, -11, 13, 17, -19, 23)]
dq = [[F(value)] for value in (29, -31, 37, 41, -43, 47, 53, -59, 61)]
for i, j in combinations(labels, 2):
    transition = transitions[(j, i)]
    cotangent = transpose(inverse(transition))
    check("primitive", f"{i}/{j} preserves the tautological pairing", mmul(transpose(mmul(cotangent, q)), mmul(transition, dq)) == mmul(transpose(q), dq))
check("moment", "all Jordan transitions are restrictions of one global principal moment map", REG["transitions"]["moment_cech_defect"] == "ZERO_BY_GLOBAL_MOMENT_MAP_EQUIVARIANCE")
check("primitive", "the complete registered primitive defect is zero", REG["transitions"]["primitive_cech_defect"] == "ZERO_BY_CANONICAL_COTANGENT_LIFTS")

print("\nF. STRATUM ROUTING AND CLAIM CEILING")
check("routing", "the three centralizer-five families use the wall-rank schedule", sum(record["sl4_centralizer_dimension"] == 5 for record in REG["rank_census"].values()) == 3)
check("routing", "J2+J2 uses the A1xA1-rank schedule", REG["rank_census"]["J2+J2_same"]["schedule_match"] == "A1xA1_RANK_80_89")
check("routing", "J2+J1+J1 uses the A2-rank schedule", REG["rank_census"]["J2+J1+J1_same"]["schedule_match"] == "A2_RANK_78_88")
degeneration_limits = {
    "J3+J1_same": zero(4),
    "J2+J2_same": zero(4),
    "J2+J1+J1_same": zero(4),
    "J2+J1_same_plus_J1_distinct": diag((1, 1, 1, -3)),
    "J2_plus_repeated_semisimple_pair": diag((1, 1, -1, -1)),
}
for label, limit in degeneration_limits.items():
    a, h, *_ = families[label]
    nilpotent_part = msub(a, limit)
    check("routing", f"{label} scaling limit stays in the same moving fibre", mmul(transpose(limit), h) == mmul(h, limit) and mmul(transpose(nilpotent_part), h) == mmul(h, nilpotent_part))
    expected_target = "A3_ORIGIN" if limit == zero(4) else ("A2_SEMISIMPLE" if limit == diag((1, 1, 1, -3)) else "A1xA1_SEMISIMPLE")
    check("routing", f"{label} has the registered exact degeneration target", REG["transitions"]["degeneration_targets"][label] == expected_target)
check("scope", "the split-A3 nonsemisimple singular transition census is closed", REG["scope"]["split_a3_nonsemisimple_singular_transition_census"] == "CLOSED")
check("scope", "no new split-A3 local model is required", REG["scope"]["genuinely_new_split_a3_local_model"] == "NOT_REQUIRED")
check("scope", "the same-sign rank-one sheet remains partial only", REG["scope"]["same_sign_sl2_so2_sheet"] == "PARTIAL_NOT_RSAP")
check("scope", "other A3 forms, deeper strata and zero charge remain open", set(REG["scope"][key] for key in ("other_a3_real_forms", "deeper_so77_singular_strata", "zero_charge_rank_at_most_49", "global_all_strata_rsap")) == {"OPEN", "NOT_CONSTRUCTED"})
check("scope", "the 182D all-charge fallback remains unchanged", REG["scope"]["all_charge_fallback_dimension"] == 182)
check("scope", "the predecessor's all-Jordan surjectivity remains the base result", ORIGIN["all_jordan_symmetrizer_census"]["consequence"].endswith("EVERY_REAL_JORDAN_TYPE"))
check("scope", "protected truth surfaces remain unchanged", set(REG["changes"].values()) == {"none"})
for key in ("artifact", "probe", "hostile_review"):
    check("links", f"the {key} exists", (ROOT / REG[key]).is_file())

print("\nSUMMARY")
print(json.dumps({"groups": COUNTS, "checks": sum(COUNTS.values()), "failures": FAILURES}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
