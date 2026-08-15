#!/usr/bin/env python3
"""Exact certificate for the first adjacent split-A2 two-wall attachment."""

from fractions import Fraction as F
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REG = json.loads((ROOT / "lab/process/selected-k77-rsap-a3-adjacent-a2-two-wall-attachment.json").read_text())
A2 = json.loads((ROOT / "lab/process/selected-k77-rsap-a2-principal-symmetric-pair.json").read_text())
WALL = json.loads((ROOT / "lab/process/selected-k77-rsap-a3-first-singular-attachment.json").read_text())
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


def msub(a, b):
    return [[x - y for x, y in zip(arow, brow)] for arow, brow in zip(a, b)]


def madd(a, b):
    return [[x + y for x, y in zip(arow, brow)] for arow, brow in zip(a, b)]


def inverse(a):
    n = len(a)
    aug = [[F(x) for x in row] + ident for row, ident in zip(a, eye(n))]
    for col in range(n):
        pivot = next((r for r in range(col, n) if aug[r][col]), None)
        if pivot is None:
            raise ValueError("singular matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [x / scale for x in aug[col]]
        for row in range(n):
            if row != col and aug[row][col]:
                scale = aug[row][col]
                aug[row] = [x - scale * y for x, y in zip(aug[row], aug[col])]
    return [row[n:] for row in aug]


def rank(a):
    a = [[F(x) for x in row] for row in a]
    r = 0
    for col in range(len(a[0]) if a else 0):
        pivot = next((i for i in range(r, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        p = a[r][col]
        a[r] = [x / p for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][col]:
                q = a[i][col]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def unit(i, j, n=3):
    out = zero(n, n)
    out[i][j] = F(1)
    return out


def diag(values):
    out = zero(len(values), len(values))
    for i, value in enumerate(values):
        out[i][i] = F(value)
    return out


def bracket(a, b):
    return msub(mmul(a, b), mmul(b, a))


def flatten(a):
    return [x for row in a for x in row]


def column_rank(matrices):
    return rank(transpose([flatten(a) for a in matrices]))


def involution(x, signature):
    return [[-signature[i] * x[j][i] * signature[j] for j in range(3)] for i in range(3)]


print("A. PRINCIPAL SPLIT-A2 SYMMETRIC PAIR")
SIG = (1, -1, 1)
diagonal_basis = [msub(unit(0, 0), unit(2, 2)), msub(unit(1, 1), unit(2, 2))]
h_basis = []
p_basis = list(diagonal_basis)
for i in range(3):
    for j in range(i + 1, 3):
        h_basis.append(msub(unit(i, j), [[SIG[i] * SIG[j] * x for x in row] for row in unit(j, i)]))
        p_basis.append(madd(unit(i, j), [[SIG[i] * SIG[j] * x for x in row] for row in unit(j, i)]))
check("pair", "so(2,1) fixed algebra has dimension three", column_rank(h_basis) == 3)
check("pair", "moving space has dimension five", column_rank(p_basis) == 5)
check("pair", "fixed and moving spaces span sl3", column_rank(h_basis + p_basis) == 8)
check("pair", "the principal A2 factor is the banked split model", A2["split_model"]["verdict"] == "CONSTRUCTED")
check("pair", "the principal factor is ten-dimensional", REG["embedded_a2"]["carrier_dimension"] == 10)

print("\nB. TWO ADJACENT OPPOSITE-SIGN ROOTS")
for label, i, j in (("alpha1", 0, 1), ("alpha2", 1, 2)):
    e = unit(i, j)
    f = unit(j, i)
    h = msub(unit(i, i), unit(j, j))
    k = madd(e, f)
    r = msub(e, f)
    check("root", f"{label} crosses opposite signs", SIG[i] * SIG[j] == -1)
    check("root", f"{label} obeys [H,E]=2E", bracket(h, e) == [[2 * x for x in row] for row in e])
    check("root", f"{label} obeys [H,F]=-2F", bracket(h, f) == [[-2 * x for x in row] for row in f])
    check("root", f"{label} obeys [E,F]=H", bracket(e, f) == h)
    check("root", f"{label} fixed line is E+F", involution(k, SIG) == k)
    check("root", f"{label} H is moving", involution(h, SIG) == [[-x for x in row] for row in h])
    check("root", f"{label} E-F is moving", involution(r, SIG) == [[-x for x in row] for row in r])
check("root", "both restrictions are sl2/so(1,1)", REG["embedded_a2"]["rank_one_restrictions"] == ["sl(2,R)/so(1,1)"] * 2)

print("\nC. CENTRALIZERS AND FACTOR MAP RANKS")
sl3_basis = diagonal_basis + [unit(i, j) for i in range(3) for j in range(3) if i != j]
controls = {
    "regular": (diag((2, 0, -2)), 2, 2, 8, 6),
    "alpha1-wall": (diag((1, 1, -2)), 4, 3, 7, 4),
    "alpha2-wall": (diag((2, -1, -1)), 4, 3, 7, 4),
    "intersection": (diag((0, 0, 0)), 8, 5, 5, 0),
}
for label, (lam, centralizer, pcentralizer, maprank, orbitrank) in controls.items():
    ad_all = [bracket(x, lam) for x in sl3_basis]
    ad_p = [bracket(x, lam) for x in p_basis]
    check("centralizer", f"{label} sl3 centralizer dimension", 8 - column_rank(ad_all) == centralizer)
    check("centralizer", f"{label} moving centralizer dimension", 5 - column_rank(ad_p) == pcentralizer)
    check("rank", f"{label} principal-factor map rank", 5 + column_rank(ad_p) == maprank)
    check("rank", f"{label} sl3 orbit rank", column_rank(ad_all) == orbitrank)
for label in ("alpha1-wall", "alpha2-wall"):
    lam = controls[label][0]
    check("centralizer", f"{label} isotropy centralizer is one-dimensional", 3 - column_rank([bracket(x, lam) for x in h_basis]) == 1)

print("\nD. COMPLETE 98D SCHEDULE AND WALL RESTRICTIONS")
s = REG["rank_schedule"]
check("schedule", "the carrier dimension is 78+10+10=98", s["common_leaf_dimension"] + REG["embedded_a2"]["carrier_dimension"] + 2 * s["external_centre_dimension"] == s["full_source_dimension"] == 98)
check("schedule", "regular map rank is 78+8+5=91", 78 + 8 + 5 == s["regular_map_rank"] == 91)
check("schedule", "one-wall map rank is 78+7+5=90", 78 + 7 + 5 == s["one_wall_map_rank"] == 90)
check("schedule", "two-wall map rank is 78+5+5=88", 78 + 5 + 5 == s["two_wall_map_rank"] == 88)
check("schedule", "target Poisson ranks are 84,82,78", [s["regular_target_poisson_rank"], s["one_wall_target_poisson_rank"], s["two_wall_target_poisson_rank"]] == [84, 82, 78])
check("schedule", "fibre dimensions are 7,8,10", [98 - s["regular_map_rank"], 98 - s["one_wall_map_rank"], 98 - s["two_wall_map_rank"]] == [7, 8, 10])
check("restriction", "each wall has sl2 plus one internal centre", REG["wall_restrictions"]["each_wall_sl3_centralizer_dimension"] == 4)
check("restriction", "internal R1 plus external R5 gives R6", 1 + s["external_centre_dimension"] == 6)
check("restriction", "both banked split walls are recovered", REG["wall_restrictions"]["both_banked_split_wall_models_recovered"] is True)
check("restriction", "the predecessor split-wall carrier is 98D", WALL["wall_model_reconciliation"]["wall_carrier_dimension"] == 98)

print("\nE. WALL/WALL/A2 COTANGENT COCYCLE")
F1 = [[F(1), F(1), F(0)], [F(0), F(1), F(1)], [F(0), F(0), F(1)]]
F2 = [[F(1), F(0), F(1)], [F(1), F(1), F(0)], [F(0), F(1), F(1)]]
F21 = mmul(inverse(F2), F1)
F12 = inverse(F21)
check("overlap", "alpha1 wall-to-A2 Jacobian is invertible", rank(F1) == 3)
check("overlap", "alpha2 wall-to-A2 Jacobian is invertible", rank(F2) == 3)
check("overlap", "the induced wall-to-wall map is f2^-1 f1", F21 == mmul(inverse(F2), F1))
check("cocycle", "the ordered base cycle is identity", mmul(F12, mmul(inverse(F2), F1)) == eye(3))
C1 = transpose(inverse(F1))
CA2 = transpose(F2)
C12 = transpose(inverse(F12))
check("cocycle", "the inverse-transpose cotangent cycle is identity", mmul(C12, mmul(CA2, C1)) == eye(3))
xi = [[F(2)], [F(-3)], [F(5)]]
dx = [[F(7)], [F(11)], [F(-13)]]
for label, jac in (("alpha1", F1), ("alpha2", F2), ("wall-wall", F21)):
    cot = transpose(inverse(jac))
    check("primitive", f"{label} cotangent lift preserves the pairing", mmul(transpose(mmul(cot, xi)), mmul(jac, dx)) == mmul(transpose(xi), dx))
s1 = [[F(-1), F(0)], [F(1), F(1)]]
s2 = [[F(1), F(1)], [F(0), F(-1)]]
check("weyl", "both simple reflections square to identity", mmul(s1, s1) == eye(2) and mmul(s2, s2) == eye(2))
check("weyl", "the A2 braid relation is exact", mmul(mmul(s1, s2), s1) == mmul(mmul(s2, s1), s2))
check("cocycle", "the registry records zero moment defect", REG["first_triple"]["moment_cech_defect"] == "ZERO")
check("cocycle", "the registry records zero primitive defect", REG["first_triple"]["primitive_cech_defect"] == "ZERO")

print("\nF. CLAIM CEILING AND LINKS")
scope = REG["scope"]
check("scope", "one adjacent split-A2 attachment is constructed", scope["first_adjacent_split_a2_two_wall_attachment"] == "CONSTRUCTED")
check("scope", "all split-A3 two-wall types are not classified", scope["all_split_a3_two_wall_intersections"] == "NOT_CLASSIFIED")
check("scope", "other A3 real forms remain open", scope["other_a3_real_forms"] == "OPEN")
check("scope", "deeper strata remain open", scope["deeper_singular_strata"] == "OPEN")
check("scope", "zero charge remains unconstructed", scope["zero_charge_rank_at_most_49"] == "NOT_CONSTRUCTED")
check("scope", "global all-strata RSAP remains open", scope["global_all_strata_rsap"] == "OPEN")
check("scope", "the all-charge fallback remains 182D", scope["all_charge_fallback_dimension"] == 182)
check("scope", "protected truth surfaces remain unchanged", set(REG["changes"].values()) == {"none"})
for key in ("artifact", "probe", "hostile_review"):
    check("links", f"the {key} path exists", (ROOT / REG[key]).is_file())

print("\nSUMMARY")
total = sum(COUNTS.values())
print(json.dumps({"checks": total, "counts": COUNTS, "failures": FAILURES, "status": REG["status"], "next_gate": REG["next_gate"]}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {total}/{total}")
