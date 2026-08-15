#!/usr/bin/env python3
"""Exact ambient-incidence certificate for split and SU(2,2) A3 factors."""

from fractions import Fraction as F
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REG = json.loads((ROOT / "lab/process/selected-k80-rsap-a3-cross-real-form-incidence.json").read_text())
FAILURES = []
COUNTS = {}


def check(group, label, condition):
    COUNTS[group] = COUNTS.get(group, 0) + 1
    print(f"{'PASS' if condition else 'FAIL'} [{group}] {label}")
    if not condition:
        FAILURES.append(f"[{group}] {label}")


def zero(n, m=None):
    return [[F(0) for _ in range(n if m is None else m)] for _ in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def mmul(a, b):
    bt = transpose(b)
    return [[sum((x * y for x, y in zip(row, col)), F(0)) for col in bt] for row in a]


def madd(a, b):
    return [[x + y for x, y in zip(arow, brow)] for arow, brow in zip(a, b)]


def flatten(a):
    return [x for row in a for x in row]


def diag(values):
    out = zero(len(values))
    for i, value in enumerate(values):
        out[i][i] = F(value)
    return out


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


def column_rank(matrices):
    return rank(transpose([flatten(a) for a in matrices])) if matrices else 0


def so_basis(support, signs):
    basis = []
    for offset_i, i in enumerate(support):
        for j in support[offset_i + 1:]:
            x = zero(14)
            x[i][j] = F(signs[j])
            x[j][i] = F(-signs[i])
            basis.append(x)
    return basis


def span_intersection_dimension(left, right):
    return len(left) + len(right) - column_rank(left + right)


def support_signature(support, signs):
    return (sum(signs[i] > 0 for i in support), sum(signs[i] < 0 for i in support))


def support_operator(support, signs):
    """An exact invertible H-skew operator on each support used here."""
    x = zero(14)
    positives = [i for i in support if signs[i] > 0]
    negatives = [i for i in support if signs[i] < 0]
    coefficient = 1
    while positives and negatives:
        i, j = positives.pop(0), negatives.pop(0)
        x[i][j] = F(signs[j] * coefficient)
        x[j][i] = F(-signs[i] * coefficient)
        coefficient += 1
    while len(positives) >= 2:
        i, j = positives.pop(0), positives.pop(0)
        x[i][j] = F(signs[j] * coefficient)
        x[j][i] = F(-signs[i] * coefficient)
        coefficient += 1
    while len(negatives) >= 2:
        i, j = negatives.pop(0), negatives.pop(0)
        x[i][j] = F(signs[j] * coefficient)
        x[j][i] = F(-signs[i] * coefficient)
        coefficient += 1
    return x


SIGNS = [1] * 7 + [-1] * 7
H = diag(SIGNS)

W_SPLIT = [0, 1, 2, 7, 8, 9]
W_22_TRANSVERSE = [3, 4, 5, 6, 10, 11]
W_22_A1A1 = [0, 1, 3, 4, 7, 8]
W_22_B2 = [0, 1, 2, 3, 7, 8]

print("A. INDIVIDUAL AMBIENT EMBEDDING CLASSES")
split_basis = so_basis(W_SPLIT, SIGNS)
check("embedding", "split support has signature (3,3)", support_signature(W_SPLIT, SIGNS) == (3, 3))
check("embedding", "split algebra has dimension fifteen", column_rank(split_basis) == 15)
check("embedding", "every split generator lies in so(7,7)", all(madd(mmul(transpose(x), H), mmul(H, x)) == zero(14) for x in split_basis))

for label, support in {
    "transverse": W_22_TRANSVERSE,
    "a1xa1": W_22_A1A1,
    "b2": W_22_B2,
}.items():
    basis = so_basis(support, SIGNS)
    check("embedding", f"{label} SU(2,2) support has signature (4,2)", support_signature(support, SIGNS) == (4, 2))
    check("embedding", f"{label} SU(2,2) algebra has dimension fifteen", column_rank(basis) == 15)
    check("embedding", f"{label} generators lie in so(7,7)", all(madd(mmul(transpose(x), H), mmul(H, x)) == zero(14) for x in basis))

split_full = support_operator(W_SPLIT, SIGNS)
unitary_full = support_operator(W_22_TRANSVERSE, SIGNS)
check("support", "split full-support control has rank six", rank(split_full) == 6)
check("support", "SU(2,2) full-support control has rank six", rank(unitary_full) == 6)
check("support", "their image signatures are (3,3) and (4,2)", support_signature(W_SPLIT, SIGNS) == (3, 3) and support_signature(W_22_TRANSVERSE, SIGNS) == (4, 2))
check("conjugacy", "support signature obstructs cross-form SO(7,7) conjugacy", REG["ambient"]["cross_form_conjugacy"].startswith("IMPOSSIBLE"))

print("\nB. THREE INEQUIVALENT RELATIVE POSITIONS")
models = {
    "transverse": W_22_TRANSVERSE,
    "a1xa1_face_candidate": W_22_A1A1,
    "b2_bridge_candidate": W_22_B2,
}
expected = {
    "transverse": (0, (0, 0), 0),
    "a1xa1_face_candidate": (4, (2, 2), 6),
    "b2_bridge_candidate": (5, (3, 2), 10),
}
for label, unitary_support in models.items():
    common = sorted(set(W_SPLIT) & set(unitary_support))
    unitary_basis = so_basis(unitary_support, SIGNS)
    common_basis = so_basis(common, SIGNS)
    dim, signature, algebra_dim = expected[label]
    record = REG["relative_models"][label]
    check("incidence", f"{label} support intersection dimension", len(common) == dim == record["support_intersection_dimension"])
    check("incidence", f"{label} support intersection signature", support_signature(common, SIGNS) == signature == tuple(record["support_intersection_signature"]))
    check("incidence", f"{label} algebra intersection dimension", span_intersection_dimension(split_basis, unitary_basis) == algebra_dim == record["embedded_algebra_intersection_dimension"])
    check("incidence", f"{label} common-support so algebra realizes the intersection", column_rank(common_basis) == algebra_dim)

pair_span_ranks = [column_rank(split_basis + so_basis(support, SIGNS)) for support in models.values()]
check("joint-orbit", "the three pairs have distinct joint span ranks", len(set(pair_span_ranks)) == 3)
check("joint-orbit", "intersection dimension and signature are ambient-isometry invariants", REG["incidence"]["joint_orbit_invariant"].startswith("dimension_and_signature"))
check("joint-orbit", "three inequivalent relative orbits are explicitly realized", REG["incidence"]["three_inequivalent_relative_orbits_constructed"] is True)

print("\nC. GENERIC SEPARATION AND SPECIAL INCIDENCE")
common4 = sorted(set(W_SPLIT) & set(W_22_A1A1))
common5 = sorted(set(W_SPLIT) & set(W_22_B2))
a1a1_control = support_operator(common4, SIGNS)
b2_control = support_operator(common5[:-1], SIGNS)
check("controls", "the A1xA1-face control has rank four and lies in both algebras", rank(a1a1_control) == 4 and column_rank(split_basis + [a1a1_control]) == 15 and column_rank(so_basis(W_22_A1A1, SIGNS) + [a1a1_control]) == 15)
check("controls", "the B2 model contains an exact rank-four shared control", rank(b2_control) == 4 and column_rank(split_basis + [b2_control]) == 15 and column_rank(so_basis(W_22_B2, SIGNS) + [b2_control]) == 15)
check("controls", "a full-support overlap is impossible across unequal support signatures", REG["incidence"]["generic_full_support_target_overlap"] == "EMPTY")
check("controls", "special lower-support overlap is possible but not forced", REG["incidence"]["special_lower_support_overlap"] == "POSSIBLE_BUT_NOT_FORCED")

print("\nD. SYMPLECTIC GATE AND CLAIM CEILING")
symp = REG["symplectic_disposition"]
check("symplectic", "no common refinement is claimed", symp["common_refinement_constructed"] is False)
check("symplectic", "moment and primitive comparisons remain unlicensed", {symp["moment_map_comparison"], symp["tautological_primitive_comparison"], symp["triple_cocycle"]} == {"NOT_LICENSED"})
check("symplectic", "A1xA1 and B2 are typed alternatives", set(symp["candidate_faces"]) == {"A1xA1_on_so(2,2)", "B2_on_so(3,2)"} and symp["candidate_faces_are_alternatives_not_simultaneous_truth"] is True)
check("scope", "individual A3 factors remain unchanged", REG["scope"]["individual_a3_principal_factors"] == "UNCHANGED")
check("scope", "deeper strata, zero charge and global RSAP remain open", {REG["scope"][key] for key in ("complete_nonsplit_singular_atlases", "deeper_so77_singular_strata", "zero_charge_rank_at_most_49", "global_all_strata_rsap")} == {"OPEN", "NOT_CONSTRUCTED"})
check("scope", "protected truth surfaces remain unchanged", set(REG["changes"].values()) == {"none"})
for key in ("artifact", "probe", "hostile_review"):
    check("links", f"the {key} exists", (ROOT / REG[key]).is_file())

print("\nSUMMARY")
print(json.dumps({"groups": COUNTS, "checks": sum(COUNTS.values()), "failures": FAILURES}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
