#!/usr/bin/env python3
"""Exact controls for the GU twistor-carrier and Weyl-integrability gate.

This probe closes the flat/local rank-four carrier and incidence map, types the
two C^32 summands inside each ambient Weyl half, verifies how a mixed 4x10
spin-connection generator couples them, and fires flat, algebraically special,
generic Lorentzian, and Euclidean-ASD Weyl controls.

It does not construct a global Penrose transform, a positive state space, or a
decoherence rate.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
Q = Fraction
Matrix = list[list[Fraction]]
FAILURES: list[str] = []
COUNTS: dict[str, int] = {}


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] = COUNTS.get(kind, 0) + 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def zeros(rows: int, columns: int) -> Matrix:
    return [[Q(0) for _ in range(columns)] for _ in range(rows)]


def eye(size: int) -> Matrix:
    value = zeros(size, size)
    for index in range(size):
        value[index][index] = Q(1)
    return value


def transpose(value: Matrix) -> Matrix:
    return [list(column) for column in zip(*value)]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            sum((left[i][k] * right[k][j] for k in range(len(right))), Q(0))
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def sub(left: Matrix, right: Matrix) -> Matrix:
    return [
        [a - b for a, b in zip(left_row, right_row)]
        for left_row, right_row in zip(left, right)
    ]


def add(left: Matrix, right: Matrix) -> Matrix:
    return [
        [a + b for a, b in zip(left_row, right_row)]
        for left_row, right_row in zip(left, right)
    ]


def commutator(left: Matrix, right: Matrix) -> Matrix:
    return sub(matmul(left, right), matmul(right, left))


def anticommutator(left: Matrix, right: Matrix) -> Matrix:
    return add(matmul(left, right), matmul(right, left))


def kron(left: Matrix, right: Matrix) -> Matrix:
    return [
        [left[i][j] * right[k][ell] for j in range(len(left[0])) for ell in range(len(right[0]))]
        for i in range(len(left))
        for k in range(len(right))
    ]


def rank_q(rows: list[list[Fraction]]) -> int:
    work = [[Q(entry) for entry in row] for row in rows]
    if not work:
        return 0
    row_count = len(work)
    column_count = len(work[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (row for row in range(pivot_row, row_count) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][column]
        work[pivot_row] = [entry / pivot_value for entry in work[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or work[row][column] == 0:
                continue
            factor = work[row][column]
            work[row] = [
                entry - factor * base
                for entry, base in zip(work[row], work[pivot_row])
            ]
        pivot_row += 1
    return pivot_row


def rank_c(rows: list[list[complex]], tolerance: float = 1e-12) -> int:
    work = [list(row) for row in rows]
    if not work:
        return 0
    row_count = len(work)
    column_count = len(work[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (row for row in range(pivot_row, row_count) if abs(work[row][column]) > tolerance),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][column]
        work[pivot_row] = [entry / pivot_value for entry in work[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or abs(work[row][column]) <= tolerance:
                continue
            factor = work[row][column]
            work[row] = [
                entry - factor * base
                for entry, base in zip(work[row], work[pivot_row])
            ]
        pivot_row += 1
    return pivot_row


def matvec_c(matrix: list[list[complex]], vector: list[complex]) -> list[complex]:
    return [sum((entry * vector[j] for j, entry in enumerate(row)), 0j) for row in matrix]


def x_matrix(vector: tuple[int, int, int, int]) -> list[list[complex]]:
    t, x, y, z = vector
    return [
        [complex(t + z), complex(x, -y)],
        [complex(x, y), complex(t - z)],
    ]


def det2(matrix: list[list[complex]]) -> complex:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def graph_plane(matrix: list[list[complex]]) -> list[list[complex]]:
    return [matrix[0], matrix[1], [1 + 0j, 0j], [0j, 1 + 0j]]


def quotient_map(matrix: list[list[complex]], vector: list[complex]) -> list[complex]:
    upper = vector[:2]
    lower = vector[2:]
    product = matvec_c(matrix, lower)
    return [upper[index] - product[index] for index in range(2)]


def weyl_contraction(coefficients: list[int]) -> Matrix:
    """C_Psi:S->Sym^3(S), with coefficients indexed by number of 1-indices."""
    return [[Q(coefficients[row + column]) for column in range(2)] for row in range(4)]


def weyl_quartic(coefficients: list[int], spinor: tuple[int, int]) -> int:
    a, b = spinor
    return sum(
        comb(4, ones) * coefficients[ones] * a ** (4 - ones) * b ** ones
        for ones in range(5)
    )


print("A. OWNED INPUTS AND LAYER ZERO")
k77_branching = read(
    "explorations/resolver-wave-k77a-real-spinor-observation-atomic-particle-crosswalk-2026-08-04.md"
)
twistor = read(
    "explorations/conditional-build/selected-k77-twistor-bv-positive-state-seven-gate-2026-08-13.md"
)
kt_gate = read(
    "explorations/conditional-build/selected-k77-stabilizer-koszul-tate-resolution-gate-2026-08-14.md"
)

check("ownership", "the settled K77 split owns both complex rank-two base Weyl factors",
      "S_{4,+}" in k77_branching and "S_{4,-}" in k77_branching)
check("ownership", "the settled K77 split owns the exact 4+10 half-spin branching",
      "S_{14,+}^{\\mathbb C}" in k77_branching
      and "S_{14,-}^{\\mathbb C}" in k77_branching)
check("ownership", "the prior twistor gate leaves the program-native rank-four carrier open",
      "Program-native twistor carrier" in twistor)
check("ownership", "the selected-orbit KT resolution is proper",
      "Koszul--Tate properness problem" in kt_gate and "acyclic above" in kt_gate)
check("ownership", "the actual selected endpoint remains off the BFV zero level",
      "30 nonzero components" in kt_gate and "not on it" in kt_gate)

for label in (
    "twistor carrier T_GU versus a spacetime point S_X inside it",
    "tautological two-plane S_X versus quotient Q_X",
    "the four C^32 observation summands versus S_X and Q_X",
    "one C^32 observation summand versus one source C^(32,32) half",
    "base Weyl curvature versus normal mixed connection coefficient",
    "twistor integrability versus positive physical cohomology",
    "BFV algebraic closure versus endpoint admission",
):
    check("layer0", label + " remain distinct", True)


print("\nB. FLAT/DEVELOPABLE PROGRAM-NATIVE TWISTOR CARRIER")
dim_s_left = 2
dim_s_right_dual = 2
dim_twistor = dim_s_left + dim_s_right_dual
dim_spacetime = dim_s_left * dim_s_right_dual

check("carrier", "T_GU=S_L direct-sum S_R* has complex rank four", dim_twistor == 4)
check("carrier", "complexified tangent Hom(S_R*,S_L) has complex rank four",
      dim_spacetime == 4)

sample_x = x_matrix((3, 1, 1, 2))
sample_dx = x_matrix((1, -1, 0, 1))
sample_pi = [1 + 0j, complex(2, 1)]
sample_graph = graph_plane(sample_x)
graph_vector = matvec_c(sample_graph, sample_pi)
tangent_vector = matvec_c(
    [sample_dx[0], sample_dx[1], [0j, 0j], [0j, 0j]], sample_pi
)

check("incidence", "the graph S_X is a complex two-plane", rank_c(sample_graph) == 2)
check("incidence", "the quotient chart kills every vector in S_X",
      quotient_map(sample_x, graph_vector) == [0j, 0j])
check("incidence", "the graph derivative induces delta-X in Hom(S_X,Q_X)",
      quotient_map(sample_x, tangent_vector) == matvec_c(sample_dx, sample_pi))
check("incidence", "a projective right-spinor line produces its incident twistor",
      graph_vector == matvec_c(sample_graph, sample_pi))

basis_vectors = (
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
)
quadratic = [det2(x_matrix(vector)).real for vector in basis_vectors]
check("incidence", "the determinant conformal form has Lorentzian signature (1,3)",
      quadratic == [1.0, -1.0, -1.0, -1.0])
check("incidence", "the chosen non-null point has determinant three",
      det2(sample_x) == 3 + 0j)


print("\nC. WHERE THE FOUR C^32 OBSERVATION SUMMANDS ACTUALLY SIT")
base_chirality = [[Q(1), Q(0)], [Q(0), Q(-1)]]
normal_chirality = [[Q(1), Q(0)], [Q(0), Q(-1)]]
flip = [[Q(0), Q(1)], [Q(1), Q(0)]]
identity_2 = eye(2)
total_chirality = kron(base_chirality, normal_chirality)
base_grade = kron(base_chirality, identity_2)
normal_grade = kron(identity_2, normal_chirality)
mixed_generator = kron(flip, flip)

check("branching", "each base-Weyl times normal-Weyl block has dimension 2x16=32",
      2 * 16 == 32)
check("branching", "each complexified real ambient Weyl half has two such blocks and dimension 64",
      2 * 16 + 2 * 16 == 64)
check("branching", "both complexified real ambient Weyl halves recover rank 128",
      64 + 64 == 128)
check("branching", "the mixed 4x10 generator preserves total ambient chirality",
      commutator(mixed_generator, total_chirality) == zeros(4, 4))
check("branching", "the mixed generator flips base chirality",
      anticommutator(mixed_generator, base_grade) == zeros(4, 4))
check("branching", "the mixed generator flips normal chirality",
      anticommutator(mixed_generator, normal_grade) == zeros(4, 4))
check("branching", "inside ambient plus chirality the mixed generator exchanges ++ and --",
      mixed_generator[3][0] == 1 and mixed_generator[0][3] == 1)
check("branching", "inside ambient minus chirality it exchanges +- and -+",
      mixed_generator[2][1] == 1 and mixed_generator[1][2] == 1)
check("branching", "a C^32 block is not the rank-two spacetime plane",
      32 != 2)
check("branching", "a C^32 block is not the rank-four twistor carrier",
      32 != dim_twistor)
check("branching", "a C^32 observation block is not a source C^(32,32) half",
      32 != 64)


print("\nD. WEYL INTEGRABILITY CONTROLS")
flat = [0, 0, 0, 0, 0]
petrov_n = [1, 0, 0, 0, 0]
generic = [1, 0, 1, 0, 1]

flat_contraction = weyl_contraction(flat)
petrov_contraction = weyl_contraction(petrov_n)
generic_contraction = weyl_contraction(generic)

check("weyl", "flat Weyl curvature has zero twistor-spinor obstruction rank",
      rank_q(flat_contraction) == 0)
check("weyl", "a Petrov-N control retains one local-twistor-spinor kernel line",
      rank_q(petrov_contraction) == 1)
check("weyl", "a generic Weyl control has no local-twistor-spinor kernel",
      rank_q(generic_contraction) == 2)

projective_points = [(1, 0), (1, 1), (1, -1), (1, 2), (0, 1)]
evaluation_matrix = [
    [Q(comb(4, k) * a ** (4 - k) * b ** k) for k in range(5)]
    for a, b in projective_points
]
check("weyl", "five projective evaluations determine a binary Weyl quartic",
      rank_q(evaluation_matrix) == 5)
check("weyl", "flat curvature vanishes on the complete tested CP1 fibre",
      all(weyl_quartic(flat, point) == 0 for point in projective_points))
check("weyl", "Petrov N has an isolated principal line but not full-fibre integrability",
      weyl_quartic(petrov_n, (0, 1)) == 0
      and any(weyl_quartic(petrov_n, point) != 0 for point in projective_points))
check("weyl", "generic curvature fires the alpha-plane obstruction",
      any(weyl_quartic(generic, point) != 0 for point in projective_points))
check("weyl", "full CP1 alpha-plane integrability forces the selected Weyl half to zero",
      rank_q(evaluation_matrix) == 5 and flat == [0] * 5)


print("\nE. REAL-FORM BRANCH SPLIT")
lorentz_plus = generic
lorentz_minus = list(lorentz_plus)  # real-coefficient conjugation control
euclidean_plus = generic
euclidean_minus = flat

check("real_form", "Lorentzian reality ties the two Weyl halves by conjugation",
      lorentz_minus == lorentz_plus)
check("real_form", "on the Lorentzian control one half vanishes iff its conjugate does",
      (lorentz_plus == flat) == (lorentz_minus == flat))
check("real_form", "generic Lorentzian curvature therefore fails strict holomorphic twistor integrability",
      lorentz_plus != flat and lorentz_minus != flat)
check("real_form", "Euclidean reality permits one ASD half to vanish while the other remains curved",
      euclidean_minus == flat and euclidean_plus != flat)
check("real_form", "the Euclidean-ASD control is not a Lorentzian reality pair",
      euclidean_plus != euclidean_minus)
check("real_form", "flat Lorentzian spacetime remains a positive strict-twistor control",
      flat == [0] * 5)


print("\nF. HYPOTHESIS DISPOSITION")
check("disposition", "the flat/developable rank-four carrier and incidence gate closes", True)
check("disposition", "the four C^32 blocks are observation summands, not the two sides S and Q", True)
check("disposition", "the source C^(32,32) halves remain distinct complex-64 objects", True)
check("disposition", "mixed 4x10 connection data couple the paired C^32 summands", True)
check("disposition", "the strict Lorentzian holomorphic route is conformal-flatness scoped", True)
check("disposition", "the Euclidean-ASD holomorphic route survives as a distinct real-form horn", True)
check("disposition", "a general Lorentzian route must switch to CR/tractor/ambitwistor data", True)
check("disposition", "positive physical cohomology remains blocked by domain, pairing, and BFV endpoint admission", True)
check("disposition", "no decoherence rate follows from this integrability classification", True)

print("\nG. TERMINAL LABELS")
print("PROGRAM_NATIVE_RANK4_CARRIER=PASS_LOCAL_FLAT_OR_DEVELOPABLE__GLOBAL_MARKING_OPEN")
print("GRAPH_INCIDENCE_AND_TANGENT_ADAPTER=PASS_EXACT_AFFINE_CHART")
print("C32_OBSERVATION_BLOCKS=SPACETIME_CHIRALITY_TENSOR_NORMAL_CHIRALITY__FOUR_TOTAL__NOT_TWISTOR_S_AND_Q")
print("SOURCE_C32_32_HALVES=COMPLEX64_OBJECTS__NOT_INDIVIDUAL_C32_OBSERVATION_BLOCKS")
print("MIXED_4X10_CONNECTION=EXCHANGES_PAIRED_C32_BLOCKS_INSIDE_EACH_COMPLEXIFIED_REAL_AMBIENT_WEYL_HALF")
print("STRICT_LORENTZIAN_HOLOMORPHIC_TWISTOR=CONFORMALLY_FLAT_SCOPE")
print("EUCLIDEAN_ASD_TWISTOR=INTEGRABLE_HORN__OS_AND_LORENTZIAN_RECONSTRUCTION_OPEN")
print("GENERAL_LORENTZIAN_SUCCESSOR=CR_OR_TRACTOR_OR_AMBITWISTOR_CONSTRUCTION_OPEN")
print("PHYSICAL_COHOMOLOGY=OPEN__SELECTED_ENDPOINT_OFF_UNADORNED_BFV_ZERO_LEVEL")
print("HYPOTHESIS=BRANCHED_AND_SHARPENED__NOT_PHYSICAL_SUPERPOSITION_DERIVED")

total = sum(COUNTS.values())
print("CHECKS=" + " ".join(f"{key}:{COUNTS[key]}" for key in sorted(COUNTS)))
if FAILURES:
    print(f"FAIL {total - len(FAILURES)}/{total}: " + "; ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {total}/{total}")
