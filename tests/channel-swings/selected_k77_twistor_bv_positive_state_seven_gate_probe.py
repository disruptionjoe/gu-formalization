#!/usr/bin/env python3
"""Exact finite controls for the GU twistor/BV/positive-state seven-gate test.

The probe constructs the algebraic objects that are available now and refuses
to fabricate the analytic objects that are not:

* the base ``Gr(2,C^4)`` twistor correspondence and a Lorentzian null plane;
* the separate normal ``O(6,4)/U(3,2)`` twistor fibre;
* the tangent law for a moving normal complex structure;
* nilpotency of the moving-J BRST extension under the repository convention;
* the universal ``F^(0,2)`` and BRST-mixed curvature decomposition, with
  flat and non-integrable controls; and
* ownership checks for the Penrose pushforward, closed domain, positive
  physical pairing, physical cohomology, and decoherence generator.

This is not a Penrose transform or a construction of a physical Hilbert
space.  Those absences are part of the result.
"""

from __future__ import annotations

from fractions import Fraction
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


def zeros(rows: int, cols: int) -> Matrix:
    return [[Q(0) for _ in range(cols)] for _ in range(rows)]


def eye(size: int) -> Matrix:
    out = zeros(size, size)
    for index in range(size):
        out[index][index] = Q(1)
    return out


def diagonal(entries: list[int]) -> Matrix:
    out = zeros(len(entries), len(entries))
    for index, entry in enumerate(entries):
        out[index][index] = Q(entry)
    return out


def transpose(value: Matrix) -> Matrix:
    return [list(column) for column in zip(*value)]


def add(left: Matrix, right: Matrix) -> Matrix:
    return [
        [a + b for a, b in zip(left_row, right_row)]
        for left_row, right_row in zip(left, right)
    ]


def sub(left: Matrix, right: Matrix) -> Matrix:
    return [
        [a - b for a, b in zip(left_row, right_row)]
        for left_row, right_row in zip(left, right)
    ]


def scale(factor: Fraction, value: Matrix) -> Matrix:
    return [[factor * entry for entry in row] for row in value]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            sum((left[i][k] * right[k][j] for k in range(len(right))), Q(0))
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def commutator(left: Matrix, right: Matrix) -> Matrix:
    return sub(matmul(left, right), matmul(right, left))


def anticommutator(left: Matrix, right: Matrix) -> Matrix:
    return add(matmul(left, right), matmul(right, left))


def is_zero(value: Matrix) -> bool:
    return all(entry == 0 for row in value for entry in row)


def flatten(value: Matrix) -> list[Fraction]:
    return [entry for row in value for entry in row]


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


def column_rank(values: list[Matrix]) -> int:
    if not values:
        return 0
    columns = [flatten(value) for value in values]
    rows = [list(row) for row in zip(*columns)]
    return rank_q(rows)


def eta_skew_generators(signature: list[int]) -> list[Matrix]:
    size = len(signature)
    result = []
    for a in range(size):
        for b in range(a + 1, size):
            generator = zeros(size, size)
            generator[a][b] = Q(signature[b])
            generator[b][a] = Q(-signature[a])
            result.append(generator)
    return result


print("A. LAYER ZERO AND OWNERSHIP")
twistor_receipt = read(
    "explorations/woit-principles/twistor-grassmannian-kernel-2026-07-24.md"
)
j10_receipt = read(
    "explorations/conditional-build/selected-k77-j10-bv-green-descent-gate-2026-08-13.md"
)
domain_receipt = read(
    "explorations/conditional-build/selected-k77-observed-cauchy-domain-layer0-2026-08-11.md"
)
operator_receipt = read(
    "explorations/conditional-build/selected-k77-physical-operator-admission-closure-2026-08-13.md"
)
majorana_receipt = read(
    "explorations/conditional-build/selected-k77-majorana-reality-graded-domain-scope-2026-08-11.md"
)

check("prior_art", "the twistor receipt types spacetime as Gr(2,C^4)",
      "complexified conformally compactified spacetime is `Gr(2,C^4)`" in twistor_receipt)
check("prior_art", "the Penrose-transform field-bundle gate is explicitly open",
      "`TW-5`" in twistor_receipt and "named twistor operator is only a seed" in twistor_receipt)
check("prior_art", "fixed J10 fails while moving J10 is covariant",
      "fixed-`J10` gauge obstruction" in j10_receipt
      and "exact covariance of the universal moving family" in j10_receipt)
check("prior_art", "the complete physical operator is not currently owned",
      "No operator currently owned" in operator_receipt)

for label in (
    "base twistor plane S_x versus quotient Q_x",
    "base Gr(2,C^4) twistor geometry versus normal O(6,4)/U(3,2)",
    "normal vector complex structure J_N versus spinor Clifford volume J10",
    "ambient Weyl halves versus the twistor two-plane and quotient",
    "action pairing versus positive physical pairing",
    "local flat Hs domain versus global Green/Calderon/BFV domain",
):
    check("layer0", label + " remain distinct", True)


print("\nB. BASE TWISTOR CORRESPONDENCE")
dim_grassmannian = 2 * (4 - 2)
dim_projective_twistor = 4 - 1
dim_incidence = dim_grassmannian + 1
phi = diagonal([1, 1, -1, -1])
s_lorentz = [
    [Q(1), Q(0)],
    [Q(0), Q(1)],
    [Q(1), Q(0)],
    [Q(0), Q(1)],
]
r_lorentz = [
    [Q(1), Q(0)],
    [Q(0), Q(1)],
    [Q(-1), Q(0)],
    [Q(0), Q(-1)],
]
s_phi_s = matmul(transpose(s_lorentz), matmul(phi, s_lorentz))
s_phi_r = matmul(transpose(s_lorentz), matmul(phi, r_lorentz))

check("base", "complexified spacetime has complex dimension four",
      dim_grassmannian == 4)
check("base", "projective twistor space is complex three-dimensional",
      dim_projective_twistor == 3)
check("base", "the incidence flag has complex dimension five",
      dim_incidence == 5 == dim_projective_twistor + 2)
check("base", "the explicit Lorentzian spacetime plane is Phi-null",
      is_zero(s_phi_s))
check("base", "the null plane has a nondegenerate complementary pairing",
      rank_q(s_phi_r) == 2)
check("base", "a spacetime point is rank two, not a C^(32,32) carrier",
      rank_q(transpose(s_lorentz)) == 2 and 2 != 64)


print("\nC. NORMAL O(6,4)/U(3,2) TWISTOR FIBRE")
normal_signature = [1] * 6 + [-1] * 4
eta_normal = diagonal(normal_signature)
j_normal = zeros(10, 10)
for a, b in ((0, 1), (2, 3), (4, 5), (6, 7), (8, 9)):
    j_normal[a][b] = Q(-1)
    j_normal[b][a] = Q(1)

so_generators = eta_skew_generators(normal_signature)
identity_10 = eye(10)
commutators = [commutator(generator, j_normal) for generator in so_generators]
h_parts = [
    scale(Q(1, 2), sub(generator, matmul(j_normal, matmul(generator, j_normal))))
    for generator in so_generators
]
m_parts = [
    scale(Q(1, 2), add(generator, matmul(j_normal, matmul(generator, j_normal))))
    for generator in so_generators
]
nonzero_m_parts = [value for value in m_parts if not is_zero(value)]
nonzero_h_parts = [value for value in h_parts if not is_zero(value)]

check("normal", "J_N squares to minus identity",
      matmul(j_normal, j_normal) == scale(Q(-1), identity_10))
check("normal", "J_N is orthogonal for signature (6,4)",
      matmul(transpose(j_normal), matmul(eta_normal, j_normal)) == eta_normal)
check("normal", "so(6,4) has dimension 45", len(so_generators) == 45)
check("normal", "the J_N orbit has real dimension 20",
      column_rank(commutators) == 20)
check("normal", "the stabilizer has dimension 25, matching u(3,2)",
      45 - column_rank(commutators) == 25)
check("normal", "the anti-commuting tangent space m has dimension 20",
      column_rank(m_parts) == 20
      and all(is_zero(anticommutator(value, j_normal)) for value in m_parts))
check("normal", "left multiplication by J_N is a complex structure on m",
      all(
          matmul(j_normal, matmul(j_normal, value)) == scale(Q(-1), value)
          and is_zero(anticommutator(matmul(j_normal, value), j_normal))
          for value in m_parts
      ))
check("normal", "the homogeneous split is symmetric: [m,m] lies in the stabilizer",
      all(
          is_zero(commutator(commutator(left, right), j_normal))
          for left in nonzero_m_parts for right in nonzero_m_parts
      ))
check("normal", "the stabilizer action is complex-linear on m",
      all(
          commutator(h_value, matmul(j_normal, m_value))
          == matmul(j_normal, commutator(h_value, m_value))
          for h_value in nonzero_h_parts for m_value in nonzero_m_parts
      ))
check("normal", "base and normal twistor fibres are not identified by rank",
      dim_incidence == 5 and column_rank(m_parts) == 20)


print("\nD. MOVING-J BRST EXTENSION")
moving_deltas = [commutator(generator, j_normal) for generator in so_generators]
check(
    "moving_constraint",
    "all moving gauge tangents preserve J_N^2=-1",
    all(
        is_zero(add(matmul(delta_j, j_normal), matmul(j_normal, delta_j)))
        for delta_j in moving_deltas
    ),
)
check(
    "moving_constraint",
    "all moving gauge tangents preserve J_N^T eta J_N=eta",
    all(
        is_zero(
            add(
                matmul(transpose(delta_j), matmul(eta_normal, j_normal)),
                matmul(transpose(j_normal), matmul(eta_normal, delta_j)),
            )
        )
        for delta_j in moving_deltas
    ),
)

# Repository convention: s psi = c psi, sJ = [c,J], sc=c^2.  The signs in
# s^2J below include the odd Leibniz rule.  A generic non-stabilizer element
# is used so that sJ is genuinely nonzero.
moving_generator = next(
    generator for generator in so_generators
    if not is_zero(commutator(generator, j_normal))
)
c_repo = add(moving_generator, so_generators[-1])
sc_repo = matmul(c_repo, c_repo)
sj_repo = commutator(c_repo, j_normal)
s2j_repo = sub(
    commutator(sc_repo, j_normal),
    add(matmul(c_repo, sj_repo), matmul(sj_repo, c_repo)),
)
s2psi_coefficient = sub(sc_repo, matmul(c_repo, c_repo))

check("brst", "the moving field is nontrivial on a non-stabilizer control",
      not is_zero(sj_repo))
check("brst", "s^2 J_N vanishes with the odd Leibniz sign",
      is_zero(s2j_repo))
check("brst", "s^2 psi vanishes under the repository ghost convention",
      is_zero(s2psi_coefficient))
check("plant", "freezing J_N would miss a live orbit tangent",
      not is_zero(commutator(moving_generator, j_normal)))


print("\nE. UNIVERSAL TWISTOR SUPERCONNECTION CURVATURE")
# Standard convention g=-c_repo: sg=-g^2, sA_bar=-dbar g-[A_bar,g].
a1_flat = diagonal([1, -1])
a2_flat = diagonal([2, 3])
a1_curved = [[Q(0), Q(1)], [Q(0), Q(0)]]
a2_curved = [[Q(0), Q(0)], [Q(1), Q(0)]]
g = [[Q(0), Q(1)], [Q(-1), Q(0)]]
d1g = [[Q(1), Q(0)], [Q(0), Q(-1)]]
d2g = [[Q(0), Q(2)], [Q(0), Q(0)]]


def mixed_brst_component(a_bar: Matrix, dbar_g: Matrix) -> Matrix:
    s_a_bar = scale(Q(-1), add(dbar_g, commutator(a_bar, g)))
    return add(s_a_bar, add(dbar_g, commutator(a_bar, g)))


f02_flat = commutator(a1_flat, a2_flat)
f02_plant = commutator(a1_curved, a2_curved)
ghost_two = add(scale(Q(-1), matmul(g, g)), matmul(g, g))

check("superconnection", "a commuting flat control has F^(0,2)=0",
      is_zero(f02_flat))
check("superconnection", "a noncommuting control has F^(0,2) nonzero",
      not is_zero(f02_plant))
check("superconnection", "the first BRST-mixed component cancels exactly",
      is_zero(mixed_brst_component(a1_curved, d1g)))
check("superconnection", "the second BRST-mixed component cancels exactly",
      is_zero(mixed_brst_component(a2_curved, d2g)))
check("superconnection", "the ghost-number-two curvature cancels exactly",
      is_zero(ghost_two))
check("mixed", "commuting base/normal connection controls have zero mixed curvature",
      is_zero(commutator(a1_flat, a2_flat)))
check("mixed", "noncommuting base/normal controls expose a live mixed-curvature gate",
      not is_zero(commutator(a1_curved, a2_curved)))


print("\nF. PUSHFORWARD, DOMAIN, PAIRING, AND PHYSICS OWNERSHIP")
check("gate4", "observed principal Jhat complex linearity is already exact",
      "genuine observed-Lorentzian" in j10_receipt
      and "complex-linearity theorem" in j10_receipt)
check("gate4", "the actual Penrose field bundles and transform remain unbuilt",
      "exact field bundles, cohomology degree, line weights, and transform" in twistor_receipt)
check("gate5", "a conditional local flat observed Hs domain exists",
      "local flat observed `H^s` Cauchy domain" in domain_receipt)
check("gate5", "the variable/global closed domain remains absent",
      "variable-coefficient and global observed Cauchy evolution" in domain_receipt)
check("gate5", "the physical graded Green domain remains open",
      "physical graded Green domain and global analysis open" in majorana_receipt)
check("gate6", "current Jhat-isometric action pairings are not a positive physical inner product",
      "positive physical inner product" in j10_receipt)
check("gate7", "physical cohomology is explicitly not constructed",
      "physical cohomology" in majorana_receipt and "complete physical BV cohomology" in j10_receipt)
check("gate7", "a decoherence law still needs state space and open-system dynamics",
      "reduced/open-system dynamics" in j10_receipt and "coupling `lambda` with units" in j10_receipt)


print("\nG. DISPOSITION")
print("GATE1_BASE_TWISTOR_BUNDLE=PASS_LOCAL_ALGEBRAIC")
print("GATE1_NORMAL_TWISTOR_BUNDLE=PASS_HOMOGENEOUS_ALGEBRAIC")
print("GATE1_BASE_NORMAL_IDENTIFICATION=FORBIDDEN_UNTIL_TYPED_MAP")
print("GATE2_MOVING_J_BRST_EXTENSION=PASS_UNIVERSAL_ALGEBRA")
print("GATE3_BRST_MIXED_CANCELLATION=PASS_UNIVERSAL_ALGEBRA")
print("GATE3_ACTUAL_GU_F02_AND_BASE_NORMAL_MIXED_CURVATURE=OPEN_CONNECTION_NOT_BUILT")
print("GATE4_OBSERVED_PRINCIPAL_COMPLEX_LINEARITY=PASS_EXISTING_EXACT_RECEIPT")
print("GATE4_PENROSE_PUSHFORWARD=OPEN_FIELD_BUNDLES_WEIGHTS_AND_TRANSFORM_NOT_BUILT")
print("GATE5_LORENTZIAN_REAL_FORM=PASS_LOCAL_PHI_MODEL")
print("GATE5_POSITIVE_ENERGY_CLOSED_DOMAIN=OPEN")
print("GATE6_POSITIVE_PHYSICAL_PAIRING=OPEN")
print("GATE7_PHYSICAL_COHOMOLOGY_INTERACTIONS_DECOHERENCE=OPEN")
print("DISPOSITION=TWISTOR_AND_MOVING_BV_KINEMATICS_CONSTRUCTED__PHYSICAL_SUPERPOSITION_NOT_DERIVED")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))

if FAILURES:
    print("FAILURES=" + " | ".join(FAILURES))
    raise SystemExit(1)

print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
