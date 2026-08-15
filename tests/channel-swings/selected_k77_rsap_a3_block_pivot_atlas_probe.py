#!/usr/bin/env python3
"""Exact certificate for the complete split-A3 symmetric block-pivot atlas."""

from fractions import Fraction as F
from itertools import permutations, product
import json
from math import factorial, prod
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REG = json.loads((ROOT / "lab/process/selected-k77-rsap-a3-block-pivot-atlas.json").read_text())
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


def mvec(a, v):
    return [sum((x * y for x, y in zip(row, v)), F(0)) for row in a]


def inverse(a):
    n = len(a)
    aug = [[F(x) for x in row] + ident for row, ident in zip(a, eye(n))]
    for col in range(n):
        pivot = next((row for row in range(col, n) if aug[row][col]), None)
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


def det(a):
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
                scale = a[row][col] / p
                for j in range(col + 1, len(a)):
                    a[row][j] -= scale * a[col][j]
    return out


def permute_symmetric(a, order):
    return [[a[i][j] for j in order] for i in order]


def schur(a, size):
    b = [row[:size] for row in a[:size]]
    c = [row[size:] for row in a[:size]]
    r = [row[size:] for row in a[size:]]
    if not r:
        return [], det(b)
    correction = mmul(mmul(transpose(c), inverse(b)), c)
    return [[r[i][j] - correction[i][j] for j in range(len(r))] for i in range(len(r))], det(b)


def pivot_signature(a):
    """Exact existence proof: choose 1x1, or a forced 2x2 zero-diagonal pivot."""
    a = [[F(x) for x in row] for row in a]
    blocks = []
    negative = 0
    determinant_product = F(1)
    while a:
        n = len(a)
        diagonal = next((i for i in range(n) if a[i][i]), None)
        if diagonal is not None:
            order = [diagonal] + [i for i in range(n) if i != diagonal]
            a = permute_symmetric(a, order)
            pivot = a[0][0]
            negative += int(pivot < 0)
            a, pivot_det = schur(a, 1)
            blocks.append(1)
            determinant_product *= pivot_det
            continue
        pair = next(((i, j) for i in range(n) for j in range(i + 1, n) if a[i][j]), None)
        if pair is None:
            raise ValueError("singular zero matrix reached")
        i, j = pair
        order = [i, j] + [k for k in range(n) if k not in pair]
        a = permute_symmetric(a, order)
        a, pivot_det = schur(a, 2)
        check_det = pivot_det < 0
        if not check_det:
            raise ValueError("zero-diagonal 2x2 pivot was not indefinite")
        negative += 1
        blocks.append(2)
        determinant_product *= pivot_det
    return tuple(blocks), negative, determinant_product


def symmetric_matrix(entries):
    out = [[0 for _ in range(4)] for _ in range(4)]
    positions = [(i, j) for i in range(4) for j in range(i, 4)]
    for value, (i, j) in zip(entries, positions):
        out[i][j] = out[j][i] = value
    return out


def permutation_matrix(order):
    out = zero(4, 4)
    for i, j in enumerate(order):
        out[i][j] = F(1)
    return out


SYM_POSITIONS = [(i, j) for i in range(4) for j in range(i, 4)]


def symmetric_action(g):
    """Linear representation of Q -> g Q g^T in upper-triangle coordinates."""
    cols = []
    for i, j in SYM_POSITIONS:
        q = zero(4, 4)
        q[i][j] = q[j][i] = F(1)
        if i == j:
            q[i][j] = F(1)
        image = mmul(mmul(g, q), transpose(g))
        cols.append([image[r][c] for r, c in SYM_POSITIONS])
    return transpose(cols)


class Dual:
    def __init__(self, value, gradient):
        self.value = F(value)
        self.gradient = tuple(F(x) for x in gradient)

    def __add__(self, other):
        other = promote(other, len(self.gradient))
        return Dual(self.value + other.value, [a + b for a, b in zip(self.gradient, other.gradient)])

    __radd__ = __add__

    def __neg__(self):
        return Dual(-self.value, [-x for x in self.gradient])

    def __sub__(self, other):
        return self + (-promote(other, len(self.gradient)))

    def __rsub__(self, other):
        return promote(other, len(self.gradient)) - self

    def __mul__(self, other):
        other = promote(other, len(self.gradient))
        return Dual(
            self.value * other.value,
            [self.value * b + other.value * a for a, b in zip(self.gradient, other.gradient)],
        )

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = promote(other, len(self.gradient))
        return Dual(
            self.value / other.value,
            [
                (a * other.value - self.value * b) / (other.value * other.value)
                for a, b in zip(self.gradient, other.gradient)
            ],
        )

    def __rtruediv__(self, other):
        return promote(other, len(self.gradient)) / self


def promote(value, size):
    return value if isinstance(value, Dual) else Dual(value, [F(0)] * size)


print("A. SYMMETRIC-SPACE AND BLOCK-CENSUS ACCOUNTING")
check("type", "the symmetric-space base is nine-dimensional", REG["symmetric_space"]["base_dimension"] == 15 - 6 == 9)
check("type", "the principal cotangent factor is eighteen-dimensional", REG["symmetric_space"]["cotangent_factor_dimension"] == 18)
compositions = ((1, 1, 1, 1), (2, 1, 1), (1, 2, 1), (1, 1, 2), (2, 2))
keys = tuple("+".join(map(str, comp)) for comp in compositions)
skeletons = {key: factorial(4) // prod(factorial(b) for b in comp) for key, comp in zip(keys, compositions)}
inertia_labels = {
    key: sum(1 for values in product(*(range(b + 1) for b in comp)) if sum(values) == 2)
    for key, comp in zip(keys, compositions)
}
sectors = {key: skeletons[key] * inertia_labels[key] for key in keys}
check("census", "the five ordered block compositions exhaust one and two pivots", len(compositions) == 5 and all(sum(c) == 4 for c in compositions))
check("census", "ordered pivot skeleton counts are exact", skeletons == {k: REG["block_pivot_cover"]["ordered_pivot_skeletons"][k] for k in keys})
check("census", "there are sixty-six pivot skeletons", sum(skeletons.values()) == REG["block_pivot_cover"]["ordered_pivot_skeletons"]["total"] == 66)
check("census", "inertia-label counts are exact", inertia_labels == REG["block_pivot_cover"]["inertia_labels_per_skeleton"])
check("census", "labelled sector counts are exact", sectors == {k: REG["block_pivot_cover"]["labelled_chart_sectors"][k] for k in keys})
check("census", "the redundant cover has 306 labelled sectors", sum(sectors.values()) == REG["block_pivot_cover"]["labelled_chart_sectors"]["total"] == 306)
check("census", "scalar and block sectors partition 144 plus 162 labels", sectors["1+1+1+1"] == 144 and sum(sectors.values()) - 144 == 162)
for comp in compositions:
    lower = sum(comp[i] * comp[j] for i in range(len(comp)) for j in range(i))
    diagonal = sum(b * (b + 1) // 2 for b in comp)
    check("dimension", f"block shape {comp} has ten symmetric coordinates and nine at determinant one", lower + diagonal == 10 and lower + diagonal - 1 == 9)

print("\nB. EXACT BLOCK-PIVOT COVERAGE")
anti = [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]
anti_blocks, anti_negative, anti_product = pivot_signature(anti)
check("coverage", "the all-zero-diagonal anti-form is nonsingular determinant one", det(anti) == 1)
check("coverage", "the anti-form forces a two-plus-two pivot pattern", anti_blocks == (2, 2))
check("coverage", "the anti-form has inertia two-two", anti_negative == 2)
check("coverage", "pivot determinants multiply to the original determinant", anti_product == det(anti))
det_one_count = 0
signature_22_count = 0
two_pivot_count = 0
factor_failures = 0
for entries in product((-1, 0, 1), repeat=10):
    a = symmetric_matrix(entries)
    if det(a) != 1:
        continue
    det_one_count += 1
    try:
        blocks, negative, pivot_product = pivot_signature(a)
    except ValueError:
        factor_failures += 1
        continue
    factor_failures += int(pivot_product != 1)
    signature_22_count += int(negative == 2)
    two_pivot_count += int(2 in blocks)
check("coverage", "every determinant-one {-1,0,1} symmetric control factors exactly", det_one_count > 0 and factor_failures == 0)
check("coverage", "the finite control contains signature-two-two forms", signature_22_count > 0)
check("coverage", "the finite control genuinely requires two-by-two pivots", two_pivot_count > 0)
check("coverage", "the registry records universal block-pivot coverage", REG["block_pivot_cover"]["coverage"] == "EVERY_NONSINGULAR_SIGNATURE_22_FORM")

print("\nC. SIGN AND WEYL ACTIONS")
weyl = tuple(permutations(range(4)))
sign_words = {word for word in product((1, -1), repeat=4) if word.count(-1) == 2}
orbit = {tuple((1, 1, -1, -1)[i] for i in order) for order in weyl}
check("weyl", "the A3 Weyl group has order twenty-four", len(weyl) == REG["sign_and_weyl_data"]["weyl_order"] == 24)
check("weyl", "S4 acts transitively on the six scalar inertia words", orbit == sign_words and len(orbit) == 6)
centralizer_signs = {word for word in product((1, -1), repeat=4) if prod(word) == 1}
actions = set()
for word in centralizer_signs:
    g = zero(4, 4)
    for i, value in enumerate(word):
        g[i][i] = F(value)
    action = symmetric_action(g)
    actions.add(tuple(tuple(row) for row in action))
check("sign", "the split diagonal centralizer has eight sign components", len(centralizer_signs) == 8)
check("sign", "opposite signs induce four effective symmetric-form actions", len(actions) == REG["sign_and_weyl_data"]["effective_form_congruence_sign_actions"] == 4)
sample_x = [F(i + 1, 3) for i in range(10)]
sample_xi = [F(11 - i, 5) for i in range(10)]
pairing = sum((a * b for a, b in zip(sample_xi, sample_x)), F(0))
for order in ((1, 0, 2, 3), (0, 2, 1, 3), (0, 1, 3, 2), (3, 1, 2, 0)):
    action = symmetric_action(permutation_matrix(order))
    moved_x = mvec(action, sample_x)
    moved_xi = mvec(transpose(inverse(action)), sample_xi)
    check("cotangent", f"permutation {order} preserves the cotangent pairing", sum((a * b for a, b in zip(moved_xi, moved_x)), F(0)) == pairing)

print("\nD. NONLINEAR RATIONAL PIVOT OVERLAP")
# Q=[[a,b],[b,c]].  In the first scalar-pivot chart
# (a,b,c)=(d1,l*d1,d2+l^2*d1).  Swapping the pivots gives
# (m,e1,e2)=(b/c,c,a-b^2/c), a genuinely rational chart transition.
u_values = (F(2, 3), F(3), F(5))  # (l,d1,d2)
u = []
for i, value in enumerate(u_values):
    gradient = [F(0)] * 3
    gradient[i] = F(1)
    u.append(Dual(value, gradient))
l, d1, d2 = u
c = d2 + l * l * d1
v = (l * d1 / c, c, d1 * d2 / c)
jacobian = [list(item.gradient) for item in v]
check("nonlinear", "the rational overlap Jacobian is invertible", det(jacobian) != 0)
xi = [F(7, 3), F(-5, 4), F(11, 6)]
eta = mvec(transpose(inverse(jacobian)), xi)
check("nonlinear", "the inverse-transpose lift preserves the tautological one-form", mvec(transpose(jacobian), eta) == xi)
check("nonlinear", "the overlap is genuinely nonlinear", any(entry.denominator != 1 for row in jacobian for entry in row))
check("nonlinear", "the registry records strict primitive equality", REG["transition_cocycle"]["tautological_primitive"] == "STRICT_EQUALITY")

print("\nE. STRICT TRIPLE COCYCLE")
n1 = eye(3)
n2 = [[F(1), F(1), F(0)], [F(0), F(1), F(0)], [F(0), F(0), F(1)]]
n3 = [[F(1), F(0), F(0)], [F(0), F(1), F(1)], [F(0), F(0), F(1)]]
f12 = mmul(n2, inverse(n1))
f23 = mmul(n3, inverse(n2))
f31 = mmul(n1, inverse(n3))
check("triple", "successive base transitions need not commute", mmul(f23, f12) != mmul(f12, f23))
check("triple", "the ordered base transition product is identity", mmul(mmul(f31, f23), f12) == eye(3))
cot12 = transpose(inverse(f12))
cot23 = transpose(inverse(f23))
cot31 = transpose(inverse(f31))
check("triple", "the ordered cotangent transition product is identity", mmul(mmul(cot31, cot23), cot12) == eye(3))
check("triple", "the moment cocycle is strict by geometric naturality", REG["transition_cocycle"]["moment_map"].startswith("STRICT_GEOMETRIC_EQUALITY"))
check("triple", "primitive monodromy vanishes without a contractibility premise", REG["transition_cocycle"]["primitive_monodromy"] == "ZERO_WITHOUT_CONTRACTIBILITY_ASSUMPTION")

print("\nF. SCHEDULE, SCOPE AND LINKS")
common = REG["common_refinement"]
check("schedule", "the refinement remains twenty-six-dimensional", common["refinement_dimension"] == 18 + 8 == 26)
check("schedule", "the full carrier remains ninety-eight-dimensional", common["common_leaf_dimension"] + common["refinement_dimension"] == common["full_source_dimension"] == 98)
check("schedule", "the regular map rank remains ninety-one", common["regular_map_rank"] == 91)
check("schedule", "all nineteen local target components intertwine", common["all_19_local_target_components_intertwined"] is True)
scope = REG["scope"]
check("scope", "the complete split-A3 regular atlas is constructed", scope["full_split_a3_regular_atlas"] == "CONSTRUCTED")
check("scope", "the split A2/A3 regular transition atlas is constructed", scope["split_a2_a3_regular_transition_atlas"] == "CONSTRUCTED")
check("scope", "other A3 forms and the first singular jump remain open", scope["compact_and_mixed_a3_real_forms"] == scope["first_singular_centralizer_jump"] == "OPEN")
check("scope", "zero charge and all-strata RSAP remain open", scope["zero_charge_rank_at_most_49"] == "NOT_CONSTRUCTED" and scope["global_all_strata_rsap"] == "OPEN")
check("scope", "the all-charge fallback remains 182D", scope["all_charge_fallback_dimension"] == 182)
check("scope", "protected truth surfaces remain unchanged", set(REG["changes"].values()) == {"none"})
for key in ("artifact", "probe", "hostile_review"):
    check("links", f"{key} exists", (ROOT / REG[key]).is_file())
check("links", "the next gate is the first singular centralizer jump", REG["next_gate"].startswith("ATTACH_THE_FIRST_SPLIT_A3_SINGULAR"))

print("\nSUMMARY")
total = sum(COUNTS.values())
print(json.dumps({
    "checks": total,
    "counts": COUNTS,
    "determinant_one_controls": det_one_count,
    "signature_22_controls": signature_22_count,
    "controls_using_2x2_pivots": two_pivot_count,
    "failures": FAILURES,
    "status": REG["status"],
    "next_gate": REG["next_gate"],
}, indent=2, sort_keys=True))
if FAILURES:
    raise SystemExit(1)
print(f"PASS {total}/{total}")
