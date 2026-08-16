#!/usr/bin/env python3
"""SN-2: exact valuation classifier for a source-native neutral eq. 9.16 pencil.

The declared horn SN2-NEUTRAL-CLOSED supplies an invariant observed-neutral
restriction of the zero-momentum source blocks

                         D = [[A, B], [-C, 0]].

A is the zeta/Omega1-to-zeta/Omega1 block, B and C are the two independent
Omega1/Omega0 cross blocks, and the southeast zero is the displayed source
branch.  This is not a nu_L/nu_R identification, a reality condition, a
standard SO(10) 126 construction, or a selected relative-scale relation.

The arithmetic implementation is dependency-free, but the certificate is
conditional on banked source/K77 receipts and declared horns. It uses exact polynomial arithmetic over
Q.  It checks the scalar Newton polygon, block Schur/Smith equivalence, fixed,
direct, zero, delayed, singular, fractional and Jordan branches, and planted
mutants that defeat common but source-unfaithful shortcuts.
"""

from fractions import Fraction
from itertools import permutations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/active-research/joe-directed/majorana-126-neutrino/sn2-neutral-pencil-valuation-classifier-2026-08-16.md"
SOURCE = ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md"
REGISTER = ROOT / "lab/sources/source-claim-register.yaml"
K77 = ROOT / "explorations/resolver-wave-k77a-real-spinor-observation-atomic-particle-crosswalk-2026-08-04.md"
ROUTING = ROOT / "lab/methods/source-native-comparator-routing.md"
SN1 = ROOT / "lab/active-research/joe-directed/majorana-126-neutrino/sn1-observed-neutrino-mass-pencil-2026-08-16.md"

artifact = ARTIFACT.read_text()
source = SOURCE.read_text()
register = REGISTER.read_text()
k77 = K77.read_text()
routing = ROUTING.read_text()
sn1 = SN1.read_text()
artifact_words = " ".join(artifact.lower().split())
k77_words = " ".join(k77.lower().split())

counts = {"source": 0, "scalar": 0, "block": 0, "branch": 0, "mutant": 0, "ceiling": 0}
failures = []


def check(kind, label, condition):
    counts[kind] += 1
    if condition:
        print(f"PASS [{kind}] {label}")
    else:
        failures.append(label)
        print(f"FAIL [{kind}] {label}")


class Poly:
    """Q[t,lam], represented by {(t_power, lambda_power): coefficient}."""

    def __init__(self, terms=None):
        self.terms = {
            key: Fraction(value)
            for key, value in (terms or {}).items()
            if value
        }

    @staticmethod
    def constant(value):
        return Poly({(0, 0): Fraction(value)})

    @staticmethod
    def monomial(t_power=0, lambda_power=0, coefficient=1):
        return Poly({(t_power, lambda_power): Fraction(coefficient)})

    def __add__(self, other):
        other = as_poly(other)
        result = dict(self.terms)
        for key, value in other.terms.items():
            result[key] = result.get(key, Fraction(0)) + value
            if not result[key]:
                del result[key]
        return Poly(result)

    __radd__ = __add__

    def __neg__(self):
        return Poly({key: -value for key, value in self.terms.items()})

    def __sub__(self, other):
        return self + (-as_poly(other))

    def __rsub__(self, other):
        return as_poly(other) - self

    def __mul__(self, other):
        other = as_poly(other)
        result = {}
        for (ta, la), ca in self.terms.items():
            for (tb, lb), cb in other.terms.items():
                key = (ta + tb, la + lb)
                result[key] = result.get(key, Fraction(0)) + ca * cb
        return Poly(result)

    __rmul__ = __mul__

    def __pow__(self, exponent):
        if exponent < 0:
            raise ValueError("negative polynomial powers are not used")
        result = Poly.constant(1)
        factor = self
        while exponent:
            if exponent & 1:
                result *= factor
            factor *= factor
            exponent //= 2
        return result

    def __eq__(self, other):
        return self.terms == as_poly(other).terms


def as_poly(value):
    return value if isinstance(value, Poly) else Poly.constant(value)


ZERO = Poly.constant(0)
ONE = Poly.constant(1)
T = Poly.monomial(t_power=1)
LAM = Poly.monomial(lambda_power=1)


def determinant(matrix):
    n = len(matrix)
    result = ZERO
    for perm in permutations(range(n)):
        inversions = sum(
            perm[i] > perm[j]
            for i in range(n) for j in range(i + 1, n)
        )
        term = Poly.constant(-1 if inversions % 2 else 1)
        for row, column in enumerate(perm):
            term *= matrix[row][column]
        result += term
    return result


def characteristic(matrix):
    n = len(matrix)
    return determinant([
        [LAM * (1 if i == j else 0) - matrix[i][j] for j in range(n)]
        for i in range(n)
    ])


def valuation(poly):
    poly = as_poly(poly)
    return min((tp for (tp, _lp) in poly.terms), default=None)


def coefficient_valuations(poly):
    grouped = {}
    for (tp, lp), coefficient in poly.terms.items():
        if coefficient:
            grouped.setdefault(lp, []).append(tp)
    return {lp: min(powers) for lp, powers in grouped.items()}


def newton_root_valuations(poly):
    """Negative slopes of the lower Newton hull, repeated by horizontal length."""
    points = sorted(coefficient_valuations(poly).items())
    hull = []
    for point in points:
        hull.append(point)
        while len(hull) >= 3:
            x0, y0 = hull[-3]
            x1, y1 = hull[-2]
            x2, y2 = hull[-1]
            left_slope = Fraction(y1 - y0, x1 - x0)
            right_slope = Fraction(y2 - y1, x2 - x1)
            if left_slope >= right_slope:
                hull.pop(-2)
            else:
                break
    roots = []
    for (x0, y0), (x1, y1) in zip(hull, hull[1:]):
        roots.extend([-Fraction(y1 - y0, x1 - x0)] * (x1 - x0))
    return sorted(roots)


def scalar_pencil(alpha, beta, gamma, a0=1, b0=1, c0=1):
    return [
        [a0 * T**alpha, b0 * T**beta],
        [-c0 * T**gamma, ZERO],
    ]


def block_pencil(A, B, C):
    r = len(A)
    s = len(B[0])
    return [
        list(A[i]) + list(B[i])
        for i in range(r)
    ] + [
        [-entry for entry in C[i]] + [ZERO] * s
        for i in range(s)
    ]


def matrix_mul(left, right):
    return [
        [sum((left[i][k] * right[k][j] for k in range(len(right))), ZERO)
         for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def matrix_eq(left, right):
    return len(left) == len(right) and all(
        left[i][j] == right[i][j]
        for i in range(len(left)) for j in range(len(left[0]))
    )


def rank_fraction(matrix):
    work = [[Fraction(entry) for entry in row] for row in matrix]
    rows, columns = len(work), len(work[0])
    rank = 0
    for column in range(columns):
        pivot = next((row for row in range(rank, rows) if work[row][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        pivot_value = work[rank][column]
        work[rank] = [value / pivot_value for value in work[rank]]
        for row in range(rows):
            if row != rank and work[row][column]:
                multiple = work[row][column]
                work[row] = [a - multiple * b for a, b in zip(work[row], work[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


def eval_t(poly, value=1):
    return sum(coefficient * Fraction(value) ** tp
               for (tp, lp), coefficient in as_poly(poly).terms.items() if lp == 0)


def eval_matrix_t(matrix, value=1):
    return [[eval_t(entry, value) for entry in row] for row in matrix]


print("A. SOURCE-NATIVE CUSTODY")
check("source", "routing method forbids importing the standard 126 route",
      "standard SO(10) `126` VEV" in routing and "does not adjudicate" in routing)
check("source", "equation 9.16 has four distinct barred and unbarred fields",
      "four distinct fields" in source)
check("source", "equation 9.16 exact southeast branch is zero",
      source.count("southeast-zero") >= 4 and "SE=0" in source)
check("source", "the nonzero southeast rival is admitted but unselected",
      "non-trivial map in the lower right quadrant" in source and "neither source supplies a uniqueness theorem" in source)
check("source", "SC-OP-04, SC-OP-05 and SC-GEN-58 are receipted",
      all(claim in register for claim in ("SC-OP-04", "SC-OP-05", "SC-GEN-58")))
check("source", "K77 supplies neutral observed carrier entries",
      "neutrino_left" in (ROOT / "lab/process/resolver-wave-k77a-atomic-particle-crosswalk.json").read_text()
      and "neutrino_right" in (ROOT / "lab/process/resolver-wave-k77a-atomic-particle-crosswalk.json").read_text())
check("source", "K77 neutral support remains kinematic rather than a mass",
      "geometry has only said" in k77_words and "it has not selected the coefficient" in k77_words)
check("source", "SN-1 establishes only the uniform-ray degree-one theorem",
      "D_{\\nu,0}(t)=tD_{\\nu,0}(1)" in sn1 and "independently scaled" in sn1)
check("source", "SN2 declares rather than derives neutral closure",
      "SN2-NEUTRAL-CLOSED" in artifact and "DECLARED CONDITIONAL HORN" in artifact)
check("source", "artifact classifies A/B/C as Omega1/Omega0 blocks",
      "not a `(nu_L,nu_R)` basis" in artifact and "`SOURCE_NATIVE_ROUTE`" in artifact)


print("\nB. EXACT SCALAR NEWTON CLASSIFIER")
for alpha in range(4):
    for beta in range(4):
        for gamma in range(4):
            observed = newton_root_valuations(characteristic(scalar_pencil(alpha, beta, gamma)))
            total = beta + gamma
            expected = (sorted([Fraction(alpha), Fraction(total - alpha)])
                        if 2 * alpha < total
                        else [Fraction(total, 2), Fraction(total, 2)])
            check("scalar", f"Newton slopes a/b/c={alpha}/{beta}/{gamma}", observed == expected)

fixed_t2 = [
    (beta, gamma) for beta in range(1, 5) for gamma in range(1, 5)
    if newton_root_valuations(characteristic(scalar_pencil(0, beta, gamma))) == [Fraction(0), Fraction(2)]
]
check("scalar", "strict bilateral nonnegative-integer t^2 pattern is uniquely (1,1)",
      fixed_t2 == [(1, 1)])
check("scalar", "one-sided 0/2 and 2/0 alternatives have slopes 0 and 2",
      all(newton_root_valuations(characteristic(scalar_pencil(0, b, c))) == [Fraction(0), Fraction(2)]
          for b, c in ((0, 2), (2, 0))))
check("scalar", "direct balanced off-diagonal pencil has two linear roots",
      newton_root_valuations(characteristic([[ZERO, T], [-T, ZERO]])) == [Fraction(1), Fraction(1)])
check("scalar", "unbalanced off-diagonal pencil can have fractional Puiseux slopes",
      newton_root_valuations(characteristic([[ZERO, T], [-(T**2), ZERO]]))
      == [Fraction(3, 2), Fraction(3, 2)])
check("scalar", "scalar protected zero is exactly the product-zero branch",
      characteristic([[T, T], [ZERO, ZERO]]) == LAM * (LAM - T))


print("\nC. EXACT BLOCK SCHUR/SMITH EQUIVALENCE")
A = [[Poly.constant(2), Poly.constant(1)], [Poly.constant(1), Poly.constant(1)]]
Ainv = [[Poly.constant(1), Poly.constant(-1)], [Poly.constant(-1), Poly.constant(2)]]
B0 = [[Poly.constant(1), Poly.constant(2)], [Poly.constant(3), Poly.constant(5)]]
C0 = [[Poly.constant(7), Poly.constant(11)], [Poly.constant(13), Poly.constant(17)]]
B = [[T * entry for entry in row] for row in B0]
C = [[T * entry for entry in row] for row in C0]
D = block_pencil(A, B, C)
I2 = [[ONE, ZERO], [ZERO, ONE]]
Z2 = [[ZERO, ZERO], [ZERO, ZERO]]
CAinv = matrix_mul(C, Ainv)
K = matrix_mul(CAinv, B)
L = [list(I2[0]) + list(Z2[0]), list(I2[1]) + list(Z2[1]),
     list(CAinv[0]) + list(I2[0]), list(CAinv[1]) + list(I2[1])]
minus_Ainv_B = [[-entry for entry in row] for row in matrix_mul(Ainv, B)]
R = [list(I2[0]) + list(minus_Ainv_B[0]), list(I2[1]) + list(minus_Ainv_B[1]),
     list(Z2[0]) + list(I2[0]), list(Z2[1]) + list(I2[1])]
diagonalized = matrix_mul(matrix_mul(L, D), R)
expected_diagonal = block_pencil(A, Z2, Z2)
expected_diagonal[2][2:] = K[0]
expected_diagonal[3][2:] = K[1]
check("block", "exact unimodular elimination gives diag(A, C A^-1 B)",
      matrix_eq(diagonalized, expected_diagonal))
check("block", "B and C leading matrices are independent, not transposes",
      C0 != [list(row) for row in zip(*B0)])
check("block", "independent full-rank composition has t^2 invariant factors",
      all(entry == ZERO or valuation(entry) == 2 for row in K for entry in row)
      and determinant(K) != ZERO and valuation(determinant(K)) == 4)


print("\nD. BLOCK BRANCH FIXTURES")
def diagonal_block_fixture(a_entries, b_entries, c_entries):
    AA = [[a_entries[0], ZERO], [ZERO, a_entries[1]]]
    BB = [[b_entries[0], ZERO], [ZERO, b_entries[1]]]
    CC = [[c_entries[0], ZERO], [ZERO, c_entries[1]]]
    return block_pencil(AA, BB, CC)


fixed = diagonal_block_fixture([2, 3], [T, T], [5*T, 7*T])
check("branch", "fixed-heavy full-composition slopes are 0,0,2,2",
      newton_root_valuations(characteristic(fixed)) == [Fraction(0), Fraction(0), Fraction(2), Fraction(2)])

direct = diagonal_block_fixture([ZERO, ZERO], [T, T], [5*T, 7*T])
check("branch", "direct branch slopes are all linear",
      newton_root_valuations(characteristic(direct)) == [Fraction(1)] * 4)

uniform = diagonal_block_fixture([2*T, 3*T], [T, T], [5*T, 7*T])
check("branch", "uniform A/B/C ray has no hierarchy",
      newton_root_valuations(characteristic(uniform)) == [Fraction(1)] * 4)

rank_one = diagonal_block_fixture([ONE, ONE], [T, T], [T, ZERO])
check("branch", "rank-one composition has one exact zero and one t^2 light mode",
      characteristic(rank_one) == LAM * (LAM - ONE) * (LAM**2 - LAM + T**2))

delayed = diagonal_block_fixture([ONE, ONE], [T, T], [T, T**2])
check("branch", "higher-order fill gives delayed light slopes 2 and 3",
      newton_root_valuations(characteristic(delayed))
      == [Fraction(0), Fraction(0), Fraction(2), Fraction(3)])

singular_A = diagonal_block_fixture([ONE, ZERO], [T, T], [T, T])
check("branch", "singular A mixes fixed-heavy and direct slopes",
      newton_root_valuations(characteristic(singular_A))
      == [Fraction(0), Fraction(1), Fraction(1), Fraction(2)])

P_ann = [[T, ZERO], [ZERO, ZERO]]
C_ann = [[ZERO, ZERO], [ZERO, T]]
annihilating = block_pencil(I2, P_ann, C_ann)
check("branch", "nonzero valuation-one B/C can compose to exact zero",
      matrix_mul(C_ann, P_ann) == Z2 and characteristic(annihilating) == LAM**2 * (LAM - ONE)**2)

N = [[ZERO, ONE], [ZERO, ZERO]]
C_nil = [[T * entry for entry in row] for row in N]
nilpotent = block_pencil(I2, [[T, ZERO], [ZERO, T]], C_nil)
check("branch", "nilpotent composition has algebraic zero multiplicity two",
      characteristic(nilpotent) == LAM**2 * (LAM - ONE)**2)
check("branch", "nilpotent fixture has geometric zero multiplicity one and hence a Jordan chain",
      4 - rank_fraction(eval_matrix_t(nilpotent)) == 1)

wall = scalar_pencil(1, 1, 1, a0=2, b0=1, c0=1)
check("branch", "equality-wall fixture has repeated linear root",
      characteristic(wall) == (LAM - T)**2)
check("branch", "equality-wall repeated root is a nontrivial Jordan block",
      eval_matrix_t(wall) != [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]])


print("\nE. PLANTED MUTANTS")
C_transpose_B = [list(row) for row in zip(*B)]
mutant_transpose = block_pencil(A, B, C_transpose_B)
check("mutant", "silently imposing C=B^T changes the exact pencil",
      characteristic(mutant_transpose) != characteristic(D))
check("mutant", "a southeast zero alone does not force t^2",
      newton_root_valuations(characteristic(uniform)) != [Fraction(0), Fraction(0), Fraction(2), Fraction(2)])
check("mutant", "block valuations alone do not defeat composition cancellation",
      characteristic(annihilating) != characteristic(fixed))

balanced = [[ZERO, T], [-T, ZERO]]
singularly_rescaled = [[ZERO, ONE], [-(T**2), ZERO]]
check("mutant", "singular t-dependent basis rescaling changes entry valuations but not roots",
      characteristic(balanced) == characteristic(singularly_rescaled)
      and newton_root_valuations(characteristic(singularly_rescaled)) == [Fraction(1), Fraction(1)])

observed_cancelled = T - T
check("mutant", "observation can kill a leading coefficient and raise valuation to infinity",
      valuation(T) == 1 and valuation(observed_cancelled) is None)
check("mutant", "Jordan structure is not determined by valuation slopes alone",
      newton_root_valuations(characteristic(wall)) == [Fraction(1), Fraction(1)]
      and wall != [[T, ZERO], [ZERO, T]])


print("\nF. CLAIM CEILING")
for phrase in (
    "relative scales remain declared and unselected",
    "barred and unbarred variables remain independent",
    "not a mass",
    "not a stationary background",
    "not a reality map",
    "not a physical pole",
    "not an empirical neutrino prediction",
):
    check("ceiling", phrase, phrase in artifact_words)
check("ceiling", "artifact carries the mandatory routing notice",
      "GU-COMPARATOR-ROUTING — scope before inference" in artifact)
check("ceiling", "artifact preserves the prospective strength of SC-GEN-58",
      "prospective" in artifact and "does not select" in artifact)


total = sum(counts.values())
print("\nSUMMARY")
print(" + ".join(f"{value} {kind}" for kind, value in counts.items()), "=", total)
if failures:
    print("FAILURES", failures)
    raise SystemExit(1)
print("PASS: under declared SN2-NEUTRAL-CLOSED, the source A/B/C/0 pencil has an exact Newton/Schur/Smith/Jordan valuation classifier; strict bilateral integer t^2 requires the unselected 0/1/1 scale horn plus nondegenerate composition.")
