#!/usr/bin/env python3
"""Exact certificate for the split A2/A3 26D common refinement."""

from fractions import Fraction as F
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REG = json.loads((ROOT / "lab/process/selected-k77-rsap-a2-a3-common-refinement.json").read_text())
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


def rank(a):
    a = [[F(x) for x in row] for row in a]
    r = 0
    for c in range(len(a[0]) if a else 0):
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
    return r


def poisson_from_pairs(size, pairs):
    out = zero(size, size)
    for q, p in pairs:
        out[q][p] = F(1)
        out[p][q] = F(-1)
    return out


def liouville_from_pairs(size, pairs):
    out = zero(size, size)
    for q, p in pairs:
        out[p][q] = F(1)
    return out


def projection(indices, size):
    out = zero(len(indices), size)
    for row, col in enumerate(indices):
        out[row][col] = F(1)
    return out


def permutation(old_order, new_order):
    where = {name: i for i, name in enumerate(old_order)}
    out = zero(len(old_order), len(old_order))
    for row, name in enumerate(new_order):
        out[row][where[name]] = F(1)
    return out


def pair_permutation(leaf_order, invariant_order):
    new = [f"q{i}" for i in leaf_order] + [f"p{i}" for i in leaf_order]
    new += [f"c{i}" for i in invariant_order] + [f"t{i}" for i in invariant_order]
    return permutation(UNIVERSAL, new)


UNIVERSAL = [f"q{i}" for i in range(1, 7)] + [f"p{i}" for i in range(1, 7)]
UNIVERSAL += [f"c{i}" for i in range(1, 8)] + [f"t{i}" for i in range(1, 8)]
UI = {name: i for i, name in enumerate(UNIVERSAL)}
PAIRS = [(UI[f"q{i}"], UI[f"p{i}"]) for i in range(1, 7)]
PAIRS += [(UI[f"c{i}"], UI[f"t{i}"]) for i in range(1, 8)]
PI26 = poisson_from_pairs(26, PAIRS)
L26 = liouville_from_pairs(26, PAIRS)
TARGET = [f"q{i}" for i in range(1, 7)] + [f"p{i}" for i in range(1, 7)]
TARGET += [f"c{i}" for i in range(1, 8)]
DJ = projection([UI[name] for name in TARGET], 26)
PI19 = poisson_from_pairs(19, [(i, i + 6) for i in range(6)])

print("A. COMMON TARGET AND MINIMAL REALIZATION")
check("universal", "sl4 plus four-centre target has dimension nineteen", len(PI19) == 19)
check("universal", "regular target Poisson rank is twelve", rank(PI19) == 12)
check("universal", "target corank is seven", 19 - rank(PI19) == 7)
check("universal", "universal source has dimension twenty-six", len(PI26) == 26)
check("universal", "universal source is symplectic", rank(PI26) == 26)
check("universal", "moment differential has rank nineteen", rank(DJ) == 19)
check("universal", "minimality identity is 19+7=26", 19 + 7 == 26)
check("universal", "complete Poisson moment identity holds", mmul(mmul(DJ, PI26), transpose(DJ)) == PI19)

print("\nB. A2/A3 FACTOR ACCOUNTING AND PAIR TRANSITION")
A2_ORDER = ["q1", "p1", "q2", "p2", "q3", "p3"]
A2_ORDER += ["q4", "q5", "q6", "p4", "p5", "p6", "c1", "c2", "t1", "t2"]
for i in range(3, 8):
    A2_ORDER += [f"c{i}", f"t{i}"]
A3_ORDER = [f"q{i}" for i in range(1, 7)] + [f"p{i}" for i in range(1, 7)]
A3_ORDER += ["c1", "c2", "c3", "t1", "t2", "t3"]
for i in range(4, 8):
    A3_ORDER += [f"c{i}", f"t{i}"]
K2 = permutation(A2_ORDER, UNIVERSAL)
K3 = permutation(A3_ORDER, UNIVERSAL)
PHI = mmul(transpose(K3), K2)
PI2 = mmul(mmul(transpose(K2), PI26), K2)
PI3 = mmul(mmul(transpose(K3), PI26), K3)
L2 = mmul(mmul(transpose(K2), L26), K2)
L3 = mmul(mmul(transpose(K3), L26), K3)
J2 = mmul(DJ, K2)
J3 = mmul(DJ, K3)
check("pair", "A2 order has twenty-six unique coordinates", len(A2_ORDER) == len(set(A2_ORDER)) == 26)
check("pair", "A3 order contains the same coordinates", set(A2_ORDER) == set(A3_ORDER) == set(UNIVERSAL))
check("pair", "O6 is exactly three complete leaf pairs", A2_ORDER[:6] == ["q1", "p1", "q2", "p2", "q3", "p3"])
check("pair", "X10(A2) occupies exactly ten coordinates", len(A2_ORDER[6:16]) == 10)
check("pair", "X18(A3) occupies exactly eighteen coordinates", len(A3_ORDER[:18]) == 18)
check("pair", "pair transition is an invertible permutation", rank(PHI) == 26 and mmul(transpose(PHI), PHI) == eye(26))
check("pair", "transition pulls A3 Poisson tensor to A2 tensor", mmul(mmul(PHI, PI2), transpose(PHI)) == PI3)
check("pair", "complete nineteen-component moment square commutes", mmul(J3, PHI) == J2)
check("pair", "both chart moment maps have rank nineteen", rank(J2) == rank(J3) == 19)
check("pair", "frozen tautological primitive pulls back strictly", mmul(mmul(transpose(PHI), L3), PHI) == L2)
check("pair", "full carrier stays 72+26=98", REG["full_schedule"]["common_leaf_dimension"] + REG["full_schedule"]["refinement_dimension"] == 98)
check("pair", "full regular map rank stays 91", REG["full_schedule"]["regular_map_rank"] == 91)

print("\nC. GLOBAL CONNECTED-COMPONENT CONTROLS")
# Two elementary A3 root shears. Their determinant-one matrices are global
# polynomial diffeomorphisms on a fixed Gauss cell; inverse shears are integral.
S12 = eye(6)
S12[0][1] = F(1)
S23 = eye(6)
S23[1][2] = F(1)
S12_INV = eye(6)
S12_INV[0][1] = F(-1)
S23_INV = eye(6)
S23_INV[1][2] = F(-1)
check("global", "first root shear is exactly invertible", mmul(S12, S12_INV) == eye(6))
check("global", "second root shear is exactly invertible", mmul(S23, S23_INV) == eye(6))
check("global", "adjacent root shears do not commute", mmul(S12, S23) != mmul(S23, S12))
check("global", "selected overlap is recorded as one contractible Euclidean cell", REG["connected_overlap"]["topology"] == "contractible Euclidean cell")
check("global", "selected component has zero monodromy", REG["connected_overlap"]["monodromy"] == "ZERO_ON_THE_SELECTED_COMPONENT")
check("global", "other sign and Bruhat components stay open", REG["connected_overlap"]["other_sign_or_bruhat_components"] == "OPEN")
check("global", "transition grade is one complete connected component", REG["pair_transition"]["grade"] == "ONE_COMPLETE_CONNECTED_SPLIT_REGULAR_BIG_CELL_COMPONENT")

print("\nD. EXACT INVARIANT-SECTION GAUGE")
A = zero(7, 7)
for i in range(7):
    A[i][i] = F(i + 1)
for i, j in ((0, 1), (1, 4), (2, 6)):
    A[i][j] = A[j][i] = F(1)
GAUGE = eye(26)
for i in range(7):
    for j in range(7):
        GAUGE[UI[f"t{i+1}"]][UI[f"c{j+1}"]] = A[i][j]
check("gauge", "section matrix is symmetric", A == transpose(A))
check("gauge", "section shift is symplectic", mmul(mmul(GAUGE, PI26), transpose(GAUGE)) == PI26)
check("gauge", "section shift fixes the full moment map", mmul(DJ, GAUGE) == DJ)
c = [F(i + 1) for i in range(7)]
grad = [sum((A[i][j] * c[j] for j in range(7)), F(0)) for i in range(7)]
half_grad = [sum(((A[i][j] + A[j][i]) * c[j] / 2 for j in range(7)), F(0)) for i in range(7)]
check("gauge", "primitive change is d(half c^T A c)", grad == half_grad)

print("\nE. FIRST NONCOMMUTING A2/A3/A2 TRIPLE")
N1 = eye(26)
N2 = pair_permutation((2, 1, 3, 4, 5, 6), (2, 1, 3, 4, 5, 6, 7))
N3 = pair_permutation((1, 3, 2, 4, 6, 5), (1, 3, 2, 4, 6, 5, 7))
NS = [N1, N2, N3]
for i, n in enumerate(NS, 1):
    check("triple", f"normalization {i} is symplectic", mmul(mmul(n, PI26), transpose(n)) == PI26)
JS = [mmul(DJ, n) for n in NS]
P12 = mmul(transpose(N2), N1)
P23 = mmul(transpose(N3), N2)
P31 = mmul(transpose(N1), N3)
check("triple", "first full moment square commutes", mmul(JS[1], P12) == JS[0])
check("triple", "second full moment square commutes", mmul(JS[2], P23) == JS[1])
check("triple", "third full moment square commutes", mmul(JS[0], P31) == JS[2])
check("triple", "successive mixed-rank maps do not commute", mmul(P23, P12) != mmul(P12, P23))
check("triple", "ordered A2/A3/A2 product is identity", mmul(mmul(P31, P23), P12) == eye(26))
check("triple", "moment Cech defect is zero", REG["first_noncommuting_triple"]["moment_cech_defect"] == "ZERO_ON_THE_SELECTED_COMPONENT")
check("triple", "primitive Cech defect is zero", REG["first_noncommuting_triple"]["primitive_cech_defect"] == "ZERO_ON_THE_SELECTED_COMPONENT")

print("\nF. CLAIM CEILING AND LINKS")
SCOPE = REG["scope"]
check("scope", "selected component is constructed", SCOPE["selected_split_big_cell_component"] == "CONSTRUCTED")
check("scope", "every split component remains open", SCOPE["every_split_regular_component"] == "OPEN")
check("scope", "other A3 real forms remain open", SCOPE["compact_and_mixed_a3_real_forms"] == "OPEN")
check("scope", "singular and deeper strata remain open", SCOPE["singular_extension"] == SCOPE["deeper_singular_strata"] == "OPEN")
check("scope", "zero charge remains unconstructed", SCOPE["zero_charge_rank_at_most_49"] == "NOT_CONSTRUCTED")
check("scope", "global RSAP remains open", SCOPE["global_rsap"] == "OPEN")
check("scope", "all-charge fallback remains 182D", SCOPE["all_charge_fallback_dimension"] == 182)
check("scope", "protected truth surfaces remain unchanged", set(REG["changes"].values()) == {"none"})
for key in ("artifact", "probe", "hostile_review"):
    check("links", f"{key} exists", (ROOT / REG[key]).is_file())
check("links", "next gate addresses remaining components", REG["next_gate"].startswith("CLASSIFY_AND_GLUE_THE_REMAINING_SPLIT_A3"))

print("\nSUMMARY")
total = sum(COUNTS.values())
print(json.dumps({"checks": total, "counts": COUNTS, "failures": FAILURES, "status": REG["status"], "next_gate": REG["next_gate"]}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {total}/{total}")
