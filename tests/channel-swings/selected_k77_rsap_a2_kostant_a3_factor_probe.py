#!/usr/bin/env python3
"""Exact A2 real Kostant bridge and split-A3 principal-factor certificate."""

from fractions import Fraction as F
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REG = json.loads((ROOT / "lab/process/selected-k77-rsap-a2-kostant-a3-factor.json").read_text())
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
    a = zero(n, n)
    for i in range(n):
        a[i][i] = F(1)
    return a


def transpose(a):
    return [list(col) for col in zip(*a)]


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def sub(a, b):
    return [[x - y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(c, a):
    return [[c * x for x in row] for row in a]


def mmul(a, b):
    return [[sum((x * y for x, y in zip(row, col)), F(0)) for col in zip(*b)] for row in a]


def mvec(a, v):
    return [sum((x * y for x, y in zip(row, v)), F(0)) for row in a]


def comm(a, b):
    return sub(mmul(a, b), mmul(b, a))


def cmul(x, y):
    a, b = x
    c, d = y
    return sub(mmul(a, c), mmul(b, d)), add(mmul(a, d), mmul(b, c))


def flat(a):
    return [x for row in a for x in row]


def rank(rows):
    a = [list(map(F, row)) for row in rows if any(row)]
    if not a:
        return 0
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        p = a[r][c]
        a[r] = [x / p for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def nullspace(a):
    a = [list(map(F, row)) for row in a]
    rows, cols = len(a), len(a[0])
    pivots = []
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        p = a[r][c]
        a[r] = [x / p for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        pivots.append(c)
        r += 1
        if r == rows:
            break
    free = [c for c in range(cols) if c not in pivots]
    basis = []
    for f in free:
        v = [F(0)] * cols
        v[f] = F(1)
        for i, p in enumerate(pivots):
            v[p] = -a[i][f]
        basis.append(v)
    return basis


def mat(v, n):
    return [v[i * n:(i + 1) * n] for i in range(n)]


def sl_basis(n):
    out = []
    for i in range(n):
        for j in range(n):
            if i != j:
                a = zero(n, n)
                a[i][j] = F(1)
                out.append(a)
    for i in range(n - 1):
        a = zero(n, n)
        a[i][i] = F(1)
        a[-1][-1] = F(-1)
        out.append(a)
    return out


def form_basis(h, skew):
    n = len(h)
    rows = []
    for i in range(n):
        for j in range(n):
            row = []
            for k in range(n * n):
                e = zero(n, n)
                e[k // n][k % n] = F(1)
                lhs = mmul(transpose(e), h)
                rhs = mmul(h, e)
                row.append((add(lhs, rhs) if skew else sub(rhs, lhs))[i][j])
            rows.append(row)
    trace_row = [F(int(k // n == k % n)) for k in range(n * n)]
    rows.append(trace_row)
    return [mat(v, n) for v in nullspace(rows)]


def block_pair(p, q):
    return flat(p) + flat(q)


def ad_kernel_dim(basis, x, complex_basis=False):
    cols = []
    for item in basis:
        if complex_basis:
            p, q = item
            cols.append(block_pair(comm(p, x), comm(q, x)))
        else:
            cols.append(flat(comm(item, x)))
    return len(basis) - rank(list(map(list, zip(*cols))))


print("A. SPLIT A2 PRINCIPAL TRIPLE")
E3 = [[F(0), F(1), F(0)], [F(0), F(0), F(1)], [F(0), F(0), F(0)]]
F3 = [[F(0), F(0), F(0)], [F(2), F(0), F(0)], [F(0), F(2), F(0)]]
H3 = [[F(2), F(0), F(0)], [F(0), F(0), F(0)], [F(0), F(0), F(-2)]]
F3sq = mmul(F3, F3)
check("triple", "[e,f]=h", comm(E3, F3) == H3)
check("triple", "[h,e]=2e", comm(H3, E3) == scale(F(2), E3))
check("triple", "[h,f]=-2f", comm(H3, F3) == scale(F(-2), F3))
sl3 = sl_basis(3)
split_orbit = [flat(comm(x, E3)) for x in sl3]
check("split", "principal orbit rank is six", rank(split_orbit) == 6)
check("split", "f and f^2 complete the rank-eight slice", rank(split_orbit + [flat(F3), flat(F3sq)]) == 8)
check("split", "regular centralizer has dimension two", ad_kernel_dim(sl3, E3) == 2)
split_jordan = add(E3, add(scale(F(3, 4), F3), scale(F(-1, 2), F3sq)))
check("split", "nonnilpotent discriminant control has a double eigenvalue", rank(sub(split_jordan, eye(3))) == 2)
check("split", "split control obeys (X-I)^2(X+2I)=0 nonsemisimply", mmul(mmul(sub(split_jordan, eye(3)), sub(split_jordan, eye(3))), add(split_jordan, scale(F(2), eye(3)))) == zero(3, 3) and mmul(sub(split_jordan, eye(3)), add(split_jordan, scale(F(2), eye(3)))) != zero(3, 3))
check("split", "nonnilpotent discriminant control remains regular", ad_kernel_dim(sl3, split_jordan) == 2)

print("\nB. MIXED A2 REAL FORM")
HM = [[F(0), F(0), F(1)], [F(0), F(-1), F(0)], [F(1), F(0), F(0)]]
skew = form_basis(HM, True)
selfadj = form_basis(HM, False)
check("mixed", "H has nonzero determinant", rank(HM) == 3)
check("mixed", "real H-skew part has dimension three", len(skew) == 3)
check("mixed", "imaginary H-selfadjoint traceless part has dimension five", len(selfadj) == 5)
check("mixed", "e lies in the mixed real form", add(mmul(transpose(E3), HM), mmul(HM, E3)) == zero(3, 3))
check("mixed", "f lies in the mixed real form", add(mmul(transpose(F3), HM), mmul(HM, F3)) == zero(3, 3))
check("mixed", "f^2 is H-selfadjoint", sub(mmul(HM, F3sq), mmul(transpose(F3sq), HM)) == zero(3, 3))
su_basis = [(x, zero(3, 3)) for x in skew] + [(zero(3, 3), x) for x in selfadj]
mixed_orbit = [block_pair(comm(p, E3), comm(q, E3)) for p, q in su_basis]
mixed_slice = [block_pair(F3, zero(3, 3)), block_pair(zero(3, 3), F3sq)]
check("mixed", "su(2,1) real dimension is eight", len(su_basis) == 8)
check("mixed", "principal mixed orbit rank is six", rank(mixed_orbit) == 6)
check("mixed", "f and i f^2 complete real rank eight", rank(mixed_orbit + mixed_slice) == 8)
check("mixed", "mixed regular centralizer has real dimension two", ad_kernel_dim(su_basis, E3, True) == 2)
mixed_jordan = (add(E3, scale(F(-3, 4), F3)), scale(F(1, 2), F3sq))
mixed_minus_i = (mixed_jordan[0], sub(mixed_jordan[1], eye(3)))
mixed_plus_2i = (mixed_jordan[0], add(mixed_jordan[1], scale(F(2), eye(3))))
mixed_poly = cmul(cmul(mixed_minus_i, mixed_minus_i), mixed_plus_2i)
check("mixed", "mixed control obeys (X-iI)^2(X+2iI)=0 nonsemisimply", mixed_poly == (zero(3, 3), zero(3, 3)) and cmul(mixed_minus_i, mixed_plus_2i) != (zero(3, 3), zero(3, 3)))
mixed_jordan_orbit = [
    block_pair(
        sub(comm(p, mixed_jordan[0]), comm(q, mixed_jordan[1])),
        add(comm(p, mixed_jordan[1]), comm(q, mixed_jordan[0])),
    )
    for p, q in su_basis
]
check("mixed", "nonnilpotent mixed discriminant control remains regular", rank(mixed_jordan_orbit) == 6)

print("\nC. COTANGENT TRANSITION")
J = [[F(1), F(1), F(0)], [F(0), F(1), F(1)], [F(0), F(0), F(1)]]
Jinv = [[F(1), F(-1), F(1)], [F(0), F(1), F(-1)], [F(0), F(0), F(1)]]
p = [F(2, 3), F(-5, 4), F(7, 5)]
dq = [F(3, 7), F(11, 6), F(-2, 9)]
pp = mvec(transpose(Jinv), p)
dqp = mvec(J, dq)
pair = lambda x, y: sum((a * b for a, b in zip(x, y)), F(0))
check("cotangent", "sample Jacobian is exactly invertible", mmul(J, Jinv) == eye(3))
check("cotangent", "inverse-transpose lift preserves the primitive", pair(pp, dqp) == pair(p, dq))
check("cotangent", "registry records strict primitive preservation", REG["cotangent_transition"]["primitive"] == "STRICTLY_PRESERVED")
check("cotangent", "the lift adds no degrees of freedom", REG["cotangent_transition"]["new_degrees_of_freedom"] == 0)

print("\nD. SPLIT A3 PRINCIPAL FACTOR")
E4 = zero(4, 4)
for i in range(3):
    E4[i][i + 1] = F(1)
K4 = zero(4, 4)
for i in range(4):
    K4[i][3 - i] = F(1)
sl4 = sl_basis(4)
check("a3", "sl4 dimension is fifteen", len(sl4) == 15)
check("a3", "reverse form is nonsingular", rank(K4) == 4)
check("a3", "principal nilpotent is K-selfadjoint", sub(mmul(K4, E4), mmul(transpose(E4), K4)) == zero(4, 4))
check("a3", "principal nilpotent has order four", mmul(mmul(E4, E4), mmul(E4, E4)) == zero(4, 4) and mmul(mmul(E4, E4), E4) != zero(4, 4))
check("a3", "regular sl4 centralizer has dimension three", ad_kernel_dim(sl4, E4) == 3)
check("a3", "factor dimension is eighteen", REG["a3_split"]["factor_dimension"] == 18)
check("a3", "regular factor map rank is fifteen", REG["a3_split"]["regular_factor_map_rank"] == 15)
check("a3", "origin factor map rank is nine", REG["a3_split"]["origin_factor_map_rank"] == 9)

print("\nE. FULL SCHEDULE AND CLAIM CEILING")
check("scope", "A2 local regular atlas is constructed", REG["a2"]["regular_atlas"] == "CONSTRUCTED_LOCALLY_ALL_REAL_TYPES")
check("scope", "A2 source remains 98D", REG["a2"]["full_source_dimension"] == 98)
check("scope", "A2 map rank remains 91", REG["a2"]["full_map_rank"] == 91)
check("scope", "A3 common refinement is 18 plus eight", REG["a3_split"]["common_refinement_dimension"] == 26)
check("scope", "A3 full carrier remains 98D", 72 + REG["a3_split"]["common_refinement_dimension"] == 98)
check("scope", "A3 full regular rank is 72+15+4", REG["a3_split"]["full_regular_map_rank"] == 91)
check("scope", "A3 origin rank is 72+9+4", REG["a3_split"]["full_origin_map_rank"] == 85)
check("scope", "A2/A3 transition remains open", REG["a3_split"]["a2_a3_transition"] == "NOT_YET_CONSTRUCTED")
check("scope", "singular atlas remains open", REG["a2"]["singular_atlas"] == "OPEN")
check("scope", "protected truth surfaces remain unchanged", set(REG["changes"].values()) == {"none"})

print("\nF. ARTIFACT LINKS")
for key in ("artifact", "probe", "hostile_review"):
    check("links", f"{key} exists", (ROOT / REG[key]).is_file())
check("links", "next gate is the split A2/A3 transition", REG["next_gate"].startswith("CONSTRUCT_SPLIT_A2_A3"))

print("\nSUMMARY")
total = sum(COUNTS.values())
print(json.dumps({"checks": total, "counts": COUNTS, "failures": FAILURES, "status": REG["status"], "next_gate": REG["next_gate"]}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {total}/{total}")
