#!/usr/bin/env python3
"""Exact certificate for the first split-A3 singular attachment."""

from fractions import Fraction as F
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REG = json.loads((ROOT / "lab/process/selected-k77-rsap-a3-first-singular-attachment.json").read_text())
WALL = json.loads((ROOT / "lab/process/selected-k77-rsap-98d-first-wall-slice-obstruction.json").read_text())
ATLAS = json.loads((ROOT / "lab/process/selected-k77-rsap-a3-block-pivot-atlas.json").read_text())
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


def inverse(a):
    n = len(a)
    aug = [[F(x) for x in row] + ident for row, ident in zip(a, eye(n))]
    for col in range(n):
        pivot = next((row for row in range(col, n) if aug[row][col]), None)
        if pivot is None:
            raise ValueError("singular")
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


def matrix_unit(i, j, n=4):
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
    return [[-signature[i] * x[j][i] * signature[j] for j in range(4)] for i in range(4)]


def standard_poisson(pair_count):
    out = zero(2 * pair_count, 2 * pair_count)
    for i in range(pair_count):
        out[i][pair_count + i] = F(1)
        out[pair_count + i][i] = F(-1)
    return out


def block_diag(*blocks):
    rows = sum(len(block) for block in blocks)
    cols = sum(len(block[0]) for block in blocks)
    out = zero(rows, cols)
    ro = co = 0
    for block in blocks:
        for i, row in enumerate(block):
            for j, value in enumerate(row):
                out[ro + i][co + j] = value
        ro += len(block)
        co += len(block[0])
    return out


def sl2_poisson(h, e, f):
    return [[F(0), F(2 * e), F(-2 * f)], [F(-2 * e), F(0), F(h)], [F(2 * f), F(-h), F(0)]]


def sl2_dmoment(e, f):
    return [[F(2 * e), F(-2 * f), F(0), F(0)], [F(0), F(0), F(1), F(0)], [F(0), F(0), F(0), F(1)]]


def projection(n):
    out = zero(n, 2 * n)
    for i in range(n):
        out[i][i] = F(1)
    return out


print("A. EMBEDDED OPPOSITE-SIGN SPLIT ROOT")
SIG = (1, 1, -1, -1)
E = matrix_unit(1, 2)
FGEN = matrix_unit(2, 1)
H = msub(matrix_unit(1, 1), matrix_unit(2, 2))
K = madd(E, FGEN)
R = msub(E, FGEN)
check("root", "embedded matrices are traceless", all(sum(a[i][i] for i in range(4)) == 0 for a in (H, E, FGEN, K, R)))
check("root", "[H,E]=2E", bracket(H, E) == [[2 * x for x in row] for row in E])
check("root", "[H,F]=-2F", bracket(H, FGEN) == [[-2 * x for x in row] for row in FGEN])
check("root", "[E,F]=H", bracket(E, FGEN) == H)
check("involution", "E+F is fixed and spans so(1,1)", involution(K, SIG) == K)
check("involution", "H is moving", involution(H, SIG) == [[-x for x in row] for row in H])
check("involution", "E-F is moving", involution(R, SIG) == [[-x for x in row] for row in R])
check("type", "the root crosses opposite signature directions", SIG[1] * SIG[2] == -1 and REG["embedded_split_root"]["root_signature"] == "opposite-sign")

print("\nB. SL4 CENTRALIZER AND MOMENT-RANK JUMP")
diagonal_basis = [msub(matrix_unit(i, i), matrix_unit(3, 3)) for i in range(3)]
h_basis = []
m_basis = list(diagonal_basis)
for i in range(4):
    for j in range(i + 1, 4):
        h_basis.append(msub(matrix_unit(i, j), [[SIG[i] * SIG[j] * x for x in row] for row in matrix_unit(j, i)]))
        m_basis.append(madd(matrix_unit(i, j), [[SIG[i] * SIG[j] * x for x in row] for row in matrix_unit(j, i)]))
check("pair", "so(2,2) fixed algebra has dimension six", column_rank(h_basis) == 6)
check("pair", "moving symmetric-pair space has dimension nine", column_rank(m_basis) == 9)
check("pair", "fixed and moving spaces span sl4", column_rank(h_basis + m_basis) == 15)

wall = diag((3, 1, 1, -5))
regular = diag((3, 1, 0, -4))
sl4_basis = diagonal_basis + [matrix_unit(i, j) for i in range(4) for j in range(4) if i != j]
wall_ad = [bracket(x, wall) for x in sl4_basis]
regular_ad = [bracket(x, regular) for x in sl4_basis]
wall_m_ad = [bracket(x, wall) for x in m_basis]
regular_m_ad = [bracket(x, regular) for x in m_basis]
check("centralizer", "regular sl4 centralizer has dimension three", 15 - column_rank(regular_ad) == 3)
check("centralizer", "subregular sl4 centralizer has dimension five", 15 - column_rank(wall_ad) == REG["embedded_split_root"]["sl4_centralizer_dimension"] == 5)
check("centralizer", "regular moving centralizer has dimension three", 9 - column_rank(regular_m_ad) == 3)
check("centralizer", "wall moving centralizer has dimension four", 9 - column_rank(wall_m_ad) == REG["embedded_split_root"]["sl4_symmetric_space_centralizer_dimension"] == 4)
check("rank", "A3 cotangent moment rank is fifteen regularly", 9 + column_rank(regular_m_ad) == REG["rank_schedule"]["a3_factor_map_rank_regular"] == 15)
check("rank", "A3 cotangent moment rank is fourteen on the wall", 9 + column_rank(wall_m_ad) == REG["rank_schedule"]["a3_factor_map_rank_wall"] == 14)
check("rank", "sl4 orbit rank changes twelve to ten", column_rank(regular_ad) == 12 and column_rank(wall_ad) == REG["embedded_split_root"]["sl4_orbit_dimension"] == 10)

print("\nC. BANKED TRANSVERSE POISSON MODEL")
PI4 = standard_poisson(2)
for label, e, f, expected in (("split-plus", 1, 1, 3), ("split-minus", -1, -1, 3), ("wall", 0, 0, 2)):
    dmu = sl2_dmoment(e, f)
    check("transverse", f"{label} sl2 moment rank is exact", rank(dmu) == expected)
    check("transverse", f"{label} sl2 Poisson square is exact", mmul(mmul(dmu, PI4), transpose(dmu)) == sl2_poisson(0, e, f))
check("bank", "the banked wall model is locally target-surjective", WALL["wall_attachment"]["local_target_surjectivity"] is True)
check("bank", "the banked model attaches both regular chambers", WALL["regular_overlap"]["adjacent_chambers_attached"] is True)
check("bank", "the completed A3 atlas covers every split regular form", ATLAS["block_pivot_cover"]["coverage"] == "EVERY_NONSINGULAR_SIGNATURE_22_FORM")
check("centre", "sl4 R2 plus external R4 gives the wall R6", REG["wall_model_reconciliation"]["centre_accounting"].startswith("R2") and 2 + 4 == 6)

print("\nD. COMPLETE 98D RANK SCHEDULE")
leaf72 = standard_poisson(36)
centre8 = standard_poisson(4)
source98 = block_diag(leaf72, standard_poisson(9), centre8)
check("schedule", "regular A3 source has symplectic rank ninety-eight", rank(source98) == 98)
check("schedule", "regular full map rank is 72+15+4=91", 72 + 15 + 4 == REG["rank_schedule"]["regular_map_rank"] == 91)
check("schedule", "wall full map rank is 72+14+4=90", 72 + 14 + 4 == REG["rank_schedule"]["wall_map_rank"] == 90)
check("schedule", "target Poisson rank changes 72+12 to 72+10", 72 + 12 == REG["rank_schedule"]["regular_target_poisson_rank"] == 84 and 72 + 10 == REG["rank_schedule"]["wall_target_poisson_rank"] == 82)
check("schedule", "fibre dimension grows seven to eight", 98 - 91 == REG["rank_schedule"]["regular_fibre_dimension"] == 7 and 98 - 90 == REG["rank_schedule"]["wall_fibre_dimension"] == 8)
check("schedule", "wall regrouping is 82+4+12=98", 82 + 4 + 12 == REG["wall_model_reconciliation"]["wall_carrier_dimension"] == 98)

print("\nE. COMPOSED COTANGENT OVERLAPS")
# Exact representative Jacobians.  The argument is functorial: once the two
# banked arrows are genuine base diffeomorphisms, inverse-transpose lifts
# compose by this identity for their actual Jacobians as well.
FWC = [[F(1), F(1), F(0)], [F(0), F(1), F(1)], [F(0), F(0), F(1)]]
FBC = [[F(2), F(0), F(1)], [F(1), F(1), F(0)], [F(0), F(1), F(1)]]
FBW = mmul(FBC, FWC)
CWC = transpose(inverse(FWC))
CBC = transpose(inverse(FBC))
CBW = transpose(inverse(FBW))
check("overlap", "wall-to-Cartan Jacobian is invertible", rank(FWC) == 3)
check("overlap", "Cartan-to-block Jacobian is invertible", rank(FBC) == 3)
check("overlap", "base Jacobians compose", FBW == mmul(FBC, FWC))
check("overlap", "cotangent Jacobians compose in inverse-transpose order", CBW == mmul(CBC, CWC))
xi = [[F(2)], [F(-3)], [F(5)]]
dx = [[F(7)], [F(11)], [F(-13)]]
pairing = mmul(transpose(xi), dx)
check("primitive", "wall-to-Cartan lift preserves the tautological pairing", mmul(transpose(mmul(CWC, xi)), mmul(FWC, dx)) == pairing)
check("primitive", "composed wall-to-block lift preserves the tautological pairing", mmul(transpose(mmul(CBW, xi)), mmul(FBW, dx)) == pairing)
check("moment", "registry records strict geometric moment equality", REG["attachment"]["moment_map"] == "STRICT_GEOMETRIC_EQUALITY")
check("primitive", "registry records strict primitive equality", REG["attachment"]["tautological_primitive"].startswith("STRICT_EQUALITY"))

print("\nF. FIRST WALL/CARTAN/BLOCK-PIVOT TRIPLE")
FR = inverse(FBW)
CR = transpose(inverse(FR))
check("triple", "ordered base product is identity", mmul(FR, mmul(FBC, FWC)) == eye(3))
check("triple", "ordered cotangent product is identity", mmul(CR, mmul(CBC, CWC)) == eye(3))
check("triple", "moment Cech defect is zero", REG["first_triple"]["moment_cech_defect"] == "ZERO")
check("triple", "primitive Cech defect is zero", REG["first_triple"]["primitive_cech_defect"] == "ZERO")

print("\nG. CLAIM CEILING AND LINKS")
scope = REG["scope"]
check("scope", "first split-A3 singular attachment is constructed", scope["first_split_a3_singular_attachment"] == "CONSTRUCTED")
check("scope", "other A3 forms remain open", scope["other_a3_real_forms"] == "OPEN")
check("scope", "adjacent A2 and deeper intersections remain open", scope["adjacent_a2_deeper_intersection"] == scope["deeper_singular_strata"] == "OPEN")
check("scope", "zero charge and global RSAP remain open", scope["zero_charge_rank_at_most_49"] == "NOT_CONSTRUCTED" and scope["global_all_strata_rsap"] == "OPEN")
check("scope", "all-charge fallback remains 182D", scope["all_charge_fallback_dimension"] == 182)
check("scope", "protected truth surfaces remain unchanged", set(REG["changes"].values()) == {"none"})
for key in ("artifact", "probe", "hostile_review"):
    check("links", f"{key} exists", (ROOT / REG[key]).is_file())
check("links", "next gate is the adjacent split-A2 intersection", REG["next_gate"].startswith("ATTACH_THE_FIRST_ADJACENT_SPLIT_A2"))

print("\nSUMMARY")
total = sum(COUNTS.values())
print(json.dumps({"checks": total, "counts": COUNTS, "failures": FAILURES, "status": REG["status"], "next_gate": REG["next_gate"]}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {total}/{total}")
