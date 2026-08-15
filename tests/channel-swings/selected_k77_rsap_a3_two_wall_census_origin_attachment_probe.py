#!/usr/bin/env python3
"""Exact split-A3 two-wall census and first three-wall origin certificate."""

from fractions import Fraction as F
from itertools import combinations, permutations, product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REG = json.loads((ROOT / "lab/process/selected-k77-rsap-a3-two-wall-census-origin-attachment.json").read_text())
A2 = json.loads((ROOT / "lab/process/selected-k77-rsap-a3-adjacent-a2-two-wall-attachment.json").read_text())
WALLS = json.loads((ROOT / "lab/process/selected-k77-rsap-rank82-wall-family-a2-cocycle-gate.json").read_text())
FAILURES = []
COUNTS = {}


def check(group, label, condition):
    COUNTS[group] = COUNTS.get(group, 0) + 1
    print(f"{'PASS' if condition else 'FAIL'} [{group}] {label}")
    if not condition:
        FAILURES.append(f"[{group}] {label}")


def zero(n, m):
    return [[F(0) for _ in range(m)] for _ in range(n)]


def eye(n):
    out = zero(n, n)
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


def diag(values):
    out = zero(len(values), len(values))
    for i, value in enumerate(values):
        out[i][i] = F(value)
    return out


def unit(i, j, n):
    out = zero(n, n)
    out[i][j] = F(1)
    return out


def bracket(a, b):
    return msub(mmul(a, b), mmul(b, a))


def flatten(a):
    return [x for row in a for x in row]


def column_rank(matrices):
    return rank(transpose([flatten(a) for a in matrices])) if matrices else 0


def block_diag(*blocks):
    size = sum(len(block) for block in blocks)
    out = zero(size, size)
    offset = 0
    for block in blocks:
        for i, row in enumerate(block):
            for j, value in enumerate(row):
                out[offset + i][offset + j] = F(value)
        offset += len(block)
    return out


def permute_symmetric(a, order):
    return [[a[i][j] for j in order] for i in order]


def schur(a, size):
    b = [row[:size] for row in a[:size]]
    c = [row[size:] for row in a[:size]]
    rest = [row[size:] for row in a[size:]]
    if not rest:
        return []
    correction = mmul(mmul(transpose(c), inverse(b)), c)
    return [[rest[i][j] - correction[i][j] for j in range(len(rest))] for i in range(len(rest))]


def inertia(a):
    a = [[F(x) for x in row] for row in a]
    positive = negative = 0
    while a:
        n = len(a)
        pivot = next((i for i in range(n) if a[i][i]), None)
        if pivot is not None:
            order = [pivot] + [i for i in range(n) if i != pivot]
            a = permute_symmetric(a, order)
            positive += int(a[0][0] > 0)
            negative += int(a[0][0] < 0)
            a = schur(a, 1)
            continue
        pair = next(((i, j) for i in range(n) for j in range(i + 1, n) if a[i][j]), None)
        if pair is None:
            raise ValueError("degenerate form")
        order = list(pair) + [i for i in range(n) if i not in pair]
        a = permute_symmetric(a, order)
        positive += 1
        negative += 1
        a = schur(a, 2)
    return positive, negative


def jordan(n, value=0):
    out = diag([value] * n)
    for i in range(n - 1):
        out[i][i + 1] = F(1)
    return out


def reverse(n):
    out = zero(n, n)
    for i in range(n):
        out[i][n - 1 - i] = F(1)
    return out


def sl_basis(n):
    basis = [msub(unit(i, i, n), unit(n - 1, n - 1, n)) for i in range(n - 1)]
    basis += [unit(i, j, n) for i in range(n) for j in range(n) if i != j]
    return basis


print("A. COMPLETE A3 TWO-WALL ROOT AND SIGN CENSUS")
SIG = (1, 1, -1, -1)
edges = tuple(combinations(range(4), 2))
pairs = tuple(combinations(edges, 2))
a2_pairs = [pair for pair in pairs if len(set(pair[0]) & set(pair[1])) == 1]
a1_pairs = [pair for pair in pairs if len(set(pair[0]) & set(pair[1])) == 0]
check("roots", "A3 has six roots up to sign and fifteen unordered pairs", len(edges) == 6 and len(pairs) == 15)
check("roots", "twelve root pairs span A2", len(a2_pairs) == REG["two_wall_census"]["a2_pairs"] == 12)
check("roots", "three root pairs span A1xA1", len(a1_pairs) == REG["two_wall_census"]["a1_squared_pairs"] == 3)


def root_kind(edge, signs):
    return "S" if signs[edge[0]] * signs[edge[1]] == -1 else "C"


typed = {"a2_split_split": 0, "a2_same_opposite": 0, "a1_squared_split_split": 0, "a1_squared_same_same": 0}
for pair in a2_pairs:
    kinds = sorted(root_kind(edge, SIG) for edge in pair)
    typed["a2_split_split" if kinds == ["S", "S"] else "a2_same_opposite"] += 1
for pair in a1_pairs:
    kinds = sorted(root_kind(edge, SIG) for edge in pair)
    typed["a1_squared_split_split" if kinds == ["S", "S"] else "a1_squared_same_same"] += 1
check("signs", "the four typed source-presentation counts are exact", typed == REG["two_wall_census"]["typed_source_presentations"])
check("signs", "no A2 same/same or A1xA1 mixed presentation exists", sum(typed.values()) == 15)
check("scope", "only A2 and A1xA1 are target subsystem orbits", set(REG["two_wall_census"]["target_subsystem_orbits"]) == {"A2", "A1xA1"})
check("scope", "the predecessor built the split/split principal A2 face", A2["scope"]["first_adjacent_split_a2_two_wall_attachment"] == "CONSTRUCTED")
check("scope", "the orthogonal wall-family packet banked every real pairing", set(WALLS["orthogonal_overlaps"]["mixed_real_forms_checked"]) == {"split+split", "split+compact", "compact+split", "compact+compact"})

print("\nB. SAME-SIGN PARTIAL IMAGE AND OPPOSITE-SIGN CONTROL")
H2 = diag((1, -1))
X2 = madd(unit(0, 1, 2), unit(1, 0, 2))
K2 = msub(unit(0, 1, 2), unit(1, 0, 2))
N2 = madd(H2, K2)
same_samples = [madd(scale(a, H2), scale(b, X2)) for a, b in ((1, 0), (0, 1), (2, -3), (0, 0))]
same_dets = [m[0][0] * m[1][1] - m[0][1] * m[1][0] for m in same_samples]
check("partial", "the same-sign annihilator has determinant -(a^2+b^2)", same_dets == [F(-1), F(-1), F(-13), F(0)])
check("partial", "the elliptic control has positive determinant", K2[0][0] * K2[1][1] - K2[0][1] * K2[1][0] == 1)
check("partial", "the nonzero nilpotent control squares to zero", N2 != zero(2, 2) and mmul(N2, N2) == zero(2, 2))
check("partial", "the same-sign sheet is not an RSAP wall chart", REG["same_sign_face"]["local_surjectivity_at_zero"] is False and REG["same_sign_face"]["rsap_wall_chart"] is False)
opposite_controls = [H2, K2, N2]
opposite_dets = [m[0][0] * m[1][1] - m[0][1] * m[1][0] for m in opposite_controls]
check("routing", "the opposite-sign plane contains hyperbolic elliptic and nilpotent controls", opposite_dets == [F(-1), F(1), F(0)])

sign_words = [word for word in product((1, -1), repeat=4) if word.count(1) == 2]
for index, pair in enumerate(a2_pairs):
    routings = [word for word in sign_words if all(root_kind(edge, word) == "S" for edge in pair)]
    check("routing", f"A2 pair {index + 1} has exactly two opposite-sign sheets", len(routings) == 2)
chain = ((0, 1), (1, 2), (2, 3))
alternating = [word for word in sign_words if all(root_kind(edge, word) == "S" for edge in chain)]
check("routing", "the full A3 chain has exactly two alternating sheets", set(alternating) == {(1, -1, 1, -1), (-1, 1, -1, 1)})
check("routing", "the selected origin sheet is alternating", REG["opposite_sign_routing"]["selected_a3_signature"] == [1, -1, 1, -1])

print("\nC. ALL REAL FOUR-DIMENSIONAL JORDAN TYPES HAVE SIGNATURE (2,2) SYMMETRIZERS")
for n, expected in ((1, (1, 0)), (2, (1, 1)), (3, (2, 1)), (4, (2, 2))):
    j = jordan(n)
    r = reverse(n)
    check("real-block", f"size-{n} reverse form symmetrizes the real Jordan block", mmul(transpose(j), r) == mmul(r, j))
    check("real-block", f"size-{n} reverse-form inertia is exact", inertia(r) == expected)

real_partitions = ((4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1))
for partition in real_partitions:
    blocks_a = [jordan(n, i + 1) for i, n in enumerate(partition)]
    a = block_diag(*blocks_a)
    candidates = []
    for signs in product((1, -1), repeat=len(partition)):
        h = block_diag(*(scale(sign, reverse(n)) for sign, n in zip(signs, partition)))
        if inertia(h) == (2, 2) and mmul(transpose(a), h) == mmul(h, a):
            candidates.append(h)
    check("jordan-census", f"real partition {partition} has a signature-(2,2) symmetrizer", bool(candidates))

C = [[F(2), F(-3)], [F(3), F(2)]]
HC = diag((1, -1))
check("complex-block", "one complex pair is self-adjoint for a neutral form", mmul(transpose(C), HC) == mmul(HC, C) and inertia(HC) == (1, 1))
A_C2 = block_diag(C, jordan(2, 5))
H_C2 = block_diag(HC, reverse(2))
check("jordan-census", "complex pair plus real size-two block has signature (2,2)", mmul(transpose(A_C2), H_C2) == mmul(H_C2, A_C2) and inertia(H_C2) == (2, 2))
A_C11 = block_diag(C, [[F(5)]], [[F(7)]])
H_C11 = block_diag(HC, [[F(1)]], [[F(-1)]])
check("jordan-census", "complex pair plus two real lines has signature (2,2)", mmul(transpose(A_C11), H_C11) == mmul(H_C11, A_C11) and inertia(H_C11) == (2, 2))
C2 = [[F(-1), F(-2)], [F(2), F(-1)]]
A_CC = block_diag(C, C2)
H_CC = block_diag(HC, HC)
check("jordan-census", "two complex pairs have signature (2,2)", mmul(transpose(A_CC), H_CC) == mmul(H_CC, A_CC) and inertia(H_CC) == (2, 2))
A_CJ = zero(4, 4)
for i in range(2):
    for j in range(2):
        A_CJ[i][j] = C[i][j]
        A_CJ[i + 2][j + 2] = C[i][j]
        A_CJ[i][j + 2] = eye(2)[i][j]
H_CJ = zero(4, 4)
for i in range(2):
    for j in range(2):
        H_CJ[i][j + 2] = HC[i][j]
        H_CJ[i + 2][j] = HC[i][j]
check("jordan-census", "size-two complex Jordan block has signature (2,2)", mmul(transpose(A_CJ), H_CJ) == mmul(H_CJ, A_CJ) and inertia(H_CJ) == (2, 2))
check("jordan-census", "the registry records all nine configurations", REG["all_jordan_symmetrizer_census"]["configuration_count"] == 9)
check("jordan-census", "the all-Jordan consequence is full split-A3 surjectivity", REG["all_jordan_symmetrizer_census"]["consequence"].endswith("EVERY_REAL_JORDAN_TYPE"))

print("\nD. A3 ORIGIN CENTRALIZERS AND COMPLETE RANK SCHEDULE")
SIG_ALT = (1, -1, 1, -1)
sl4 = sl_basis(4)
m_basis = [msub(unit(i, i, 4), unit(3, 3, 4)) for i in range(3)]
h_basis = []
for i in range(4):
    for j in range(i + 1, 4):
        e = unit(i, j, 4)
        f = unit(j, i, 4)
        if SIG_ALT[i] * SIG_ALT[j] == 1:
            h_basis.append(msub(e, f))
            m_basis.append(madd(e, f))
        else:
            h_basis.append(madd(e, f))
            m_basis.append(msub(e, f))
check("pair", "so(2,2) fixed algebra has dimension six", column_rank(h_basis) == 6)
check("pair", "the moving space has dimension nine", column_rank(m_basis) == 9)
check("pair", "fixed and moving spaces span sl4", column_rank(h_basis + m_basis) == 15)

controls = {
    "regular": (diag((6, 2, -2, -6)), 12, 3, 15, 84, 91),
    "one_wall": (diag((2, 2, 0, -4)), 10, 4, 14, 82, 90),
    "a1_squared": (diag((1, 1, -1, -1)), 8, 5, 13, 80, 89),
    "a2": (diag((1, 1, 1, -3)), 6, 6, 12, 78, 88),
    "origin": (zero(4, 4), 0, 9, 9, 72, 85),
}
for label, (lam, orbit_rank, m_centralizer, factor_rank, target_rank, full_rank) in controls.items():
    ad_all = [bracket(x, lam) for x in sl4]
    ad_m = [bracket(x, lam) for x in m_basis]
    check("centralizer", f"{label} sl4 orbit rank", column_rank(ad_all) == orbit_rank)
    check("centralizer", f"{label} moving centralizer dimension", 9 - column_rank(ad_m) == m_centralizer)
    check("rank", f"{label} principal-factor map rank", 9 + column_rank(ad_m) == factor_rank)
    check("rank", f"{label} full target Poisson rank", 72 + orbit_rank == target_rank)
    check("rank", f"{label} full map rank", 72 + factor_rank + 4 == full_rank)

origin = REG["three_wall_origin"]
check("bound", "the 98D pointwise origin bound is eighty-five", (98 + origin["target_poisson_rank_origin"]) // 2 == 85)
check("bound", "the constructed origin map saturates the pointwise bound", origin["full_map_rank_origin"] == 85)
check("schedule", "the complete target-rank schedule is exact", [origin[k] for k in ("target_poisson_rank_regular", "target_poisson_rank_one_wall", "target_poisson_rank_a1_squared", "target_poisson_rank_a2", "target_poisson_rank_origin")] == [84, 82, 80, 78, 72])
check("schedule", "the complete map-rank schedule is exact", [origin[k] for k in ("full_map_rank_regular", "full_map_rank_one_wall", "full_map_rank_a1_squared", "full_map_rank_a2", "full_map_rank_origin")] == [91, 90, 89, 88, 85])
check("schedule", "the origin fibre dimension is thirteen", 98 - origin["full_map_rank_origin"] == origin["origin_fibre_dimension"] == 13)

print("\nE. FIRST FOUR-CHART ORIGIN COCYCLE")
normalizations = [
    eye(4),
    [[F(1), F(1), F(0), F(0)], [F(0), F(1), F(0), F(0)], [F(0), F(0), F(1), F(0)], [F(0), F(0), F(0), F(1)]],
    [[F(1), F(0), F(0), F(0)], [F(0), F(1), F(1), F(0)], [F(0), F(0), F(1), F(0)], [F(0), F(0), F(0), F(1)]],
    [[F(1), F(0), F(0), F(1)], [F(0), F(1), F(0), F(0)], [F(0), F(0), F(1), F(1)], [F(0), F(0), F(0), F(1)]],
]
transitions = {(j, i): mmul(normalizations[j], inverse(normalizations[i])) for i in range(4) for j in range(4)}
check("cocycle", "successive face transitions are genuinely noncommuting", mmul(transitions[(2, 1)], transitions[(1, 0)]) != mmul(transitions[(1, 0)], transitions[(2, 1)]))
for i, j, k in combinations(range(4), 3):
    base_cycle = mmul(transitions[(i, k)], mmul(transitions[(k, j)], transitions[(j, i)]))
    cot_cycle = mmul(transpose(inverse(transitions[(i, k)])), mmul(transpose(inverse(transitions[(k, j)])), transpose(inverse(transitions[(j, i)]))))
    check("cocycle", f"base triangle {(i, j, k)} closes", base_cycle == eye(4))
    check("cocycle", f"cotangent triangle {(i, j, k)} closes", cot_cycle == eye(4))
xi = [[F(2)], [F(-3)], [F(5)], [F(7)]]
dx = [[F(11)], [F(-13)], [F(17)], [F(19)]]
for label, transition in (("A2-left/A3", transitions[(3, 0)]), ("A2-right/A3", transitions[(3, 1)]), ("A1xA1/A3", transitions[(3, 2)])):
    cot = transpose(inverse(transition))
    check("primitive", f"{label} preserves the tautological pairing", mmul(transpose(mmul(cot, xi)), mmul(transition, dx)) == mmul(transpose(xi), dx))
check("cocycle", "the registry records zero moment defect", REG["cocycle"]["moment_cech_defect"] == "ZERO")
check("cocycle", "the registry records zero primitive defect", REG["cocycle"]["primitive_cech_defect"] == "ZERO")

print("\nF. CLAIM CEILING AND LINKS")
scope = REG["scope"]
check("scope", "all split-A3 two-wall target types are covered", scope["all_split_a3_two_wall_target_types"] == "CLASSIFIED_AND_COVERED")
check("scope", "the same-sign local face is excluded only as an RSAP chart", scope["same_sign_local_face_as_rsap"] == "EXCLUDED")
check("scope", "the first split-A3 origin is constructed", scope["first_split_a3_three_wall_origin"] == "CONSTRUCTED")
check("scope", "remaining nonsemisimple transitions and other A3 forms stay open", scope["remaining_split_a3_nonsemisimple_singular_transition_census"] == scope["other_a3_real_forms"] == "OPEN")
check("scope", "zero charge and all-strata RSAP stay open", scope["zero_charge_rank_at_most_49"] == "NOT_CONSTRUCTED" and scope["global_all_strata_rsap"] == "OPEN")
check("scope", "the all-charge fallback remains 182D", scope["all_charge_fallback_dimension"] == 182)
check("scope", "protected truth surfaces remain unchanged", set(REG["changes"].values()) == {"none"})
for key in ("artifact", "probe", "hostile_review"):
    check("links", f"the {key} exists", (ROOT / REG[key]).is_file())
check("links", "the next gate is the remaining nonsemisimple A3 transition census", REG["next_gate"].startswith("CLASSIFY_AND_GLUE_THE_REMAINING_SPLIT_A3_NONSEMISIMPLE"))

print("\nSUMMARY")
total = sum(COUNTS.values())
print(json.dumps({"checks": total, "counts": COUNTS, "failures": FAILURES, "status": REG["status"], "next_gate": REG["next_gate"]}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {total}/{total}")
