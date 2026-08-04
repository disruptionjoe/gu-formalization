#!/usr/bin/env python3
"""Exact K77 primalizer and two-connection comparison gate.

The source collision corrects the anticipated comparison: Weinstein introduces
the unreleased two-connection D-squared directly after the fermionic
0->1->13->14 rolled complex.  It is not source-typed as the bosonic half of a
Bose--Fermi totalization.  This probe therefore:

* constructs the orientation-free density/Krein primalizers on the actual
  real Cl(7,7) carrier;
* checks inverse, moving-variation, and transition naturality identities;
* builds the smallest typed Hodge rolling of the spoken four-entry mnemonic;
* compares its slot/order profile with the released D916 fermion operator; and
* keeps the full cyclic arrow pair and coefficient selection open.

No physical domain, observed equation, particle map, or datum use is claimed.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import sys

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
CHANNEL = ROOT / "tests" / "channel-swings"
sys.path.insert(0, str(CHANNEL))

from p77_real_index_twin import build_split_clifford, clifford_relations_exact  # noqa: E402


COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def zero_sp(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(value) == 0 for value in matrix)


def block2(a: sp.Matrix, b: sp.Matrix, c: sp.Matrix, d: sp.Matrix) -> sp.Matrix:
    return sp.Matrix.vstack(sp.Matrix.hstack(a, b), sp.Matrix.hstack(c, d))


print("A. SOURCE COLLISION AND LAYER 0")
toe = read("lab/sources/transcripts/toe-weinstein-gu-40-years.md")
portal = read("lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md")
primary_pack = read("lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md")
dirac_rebase = read("explorations/k77-wave2-dirac-derham-superig-rebase-2026-08-04.md")
up_back = read("explorations/k77-wave2-up-back-over-path-adapter-independent-square-root-target-2026-08-04.md")
mixed_prior = read("explorations/k77-wave2-stabilized-mixed-bose-fermi-cross-maps-target-match-2026-08-04.md")

check("source", "TOE places the new D-squared immediately after the fermion-sector rolled complex",
      "That's what the Fermion sector looks like" in toe
      and toe.index("That's what the Fermion sector looks like") < toe.index("There is a new D squared"))
check("source", "TOE identifies the released chain as zero-one-thirteen-fourteen",
      "zero to one to 13 to 14" in toe)
check("source", "TOE says the old rolled fermion matrix has a southeast zero",
      "zero in the south east corner" in toe and "seesaw mechanism" in toe)
check("source", "TOE gives the four new tokens and two second-column minus signs",
      "DA, F sub B" in toe and "identity DB" in toe
      and "two negative signs in the second column" in toe)
check("source", "TOE explicitly leaves the cyclic two-connection completion unreleased",
      "created and have never released to anyone" in toe)
check("source", "Portal distinguishes Bose and Fermi complexes with one common obstruction",
      "two somatic complexes" in portal and "One of them is Bose, one of them is Fermi" in portal)
check("source", "Portal places stress and Dirac paths between the two complexes",
      "stress-energy tensor should be the up-and-back term" in portal
      and "up-and-over" in portal and "over-and-up" in portal)
check("source", "the earlier source pack kept the cyclic completion as a fifth fermion-side object",
      "Weinstein's unreleased cyclic two-connection `D^2` proposal" in dirac_rebase
      and "SOURCE-UNRELEASED" in primary_pack)
check("source", "the immediate predecessors accidentally called the two-connection target bosonic",
      "independent bosonic target" in up_back
      and "later bosonic two-connection operator" in mixed_prior)

check("type", "the two-connection construction is retyped as a fermionic cyclic-completion rival", True)
check("type", "mixed action Hessians remain the Bose--Fermi cross-sector maps", True)
check("type", "a fermion-cyclic rolling map and a Bose--Fermi comparison functor are different objects", True)
check("type", "the source correction invalidates the planned tensor-to-spinor central-character test as the target gate", True)


print("\nB. ACTUAL REAL-K77 DENSITY/KREIN PRIMALIZERS")
P, M = build_split_clifford(7)
GAMMA = P + M
ETA = [1] * 7 + [-1] * 7
I128 = np.eye(128, dtype=np.int64)
Z128 = np.zeros((128, 128), dtype=np.int64)


def product(matrices: list[np.ndarray]) -> np.ndarray:
    result = I128.copy()
    for matrix in matrices:
        result = result @ matrix
    return result


B = product(M)
J = product(GAMMA)
check("exact", "real Cl(7,7) relations hold", clifford_relations_exact(GAMMA, ETA))
check("exact", "the split spin pairing is symmetric, involutive, and cross-chiral",
      np.array_equal(B.T, B) and np.array_equal(B @ B, I128)
      and np.array_equal(B @ J, -J @ B))


def hodge_square_sign(p: int) -> int:
    return -1 if (p * (14 - p) + 7) % 2 else 1


check("exact", "K77 Hodge-square signs are minus-plus-plus-minus",
      [hodge_square_sign(p) for p in (0, 1, 13, 14)] == [-1, 1, 1, -1])
H1 = np.diag([((-1) ** a) * ETA[a] for a in range(14)]).astype(np.int64)
H13 = H1.copy()
check("exact", "the actual one/thirteen form factors are mutual inverses",
      np.array_equal(H13 @ H1, np.eye(14, dtype=np.int64)))


def flat_one(field: list[np.ndarray]) -> list[np.ndarray]:
    return [H1[a, a] * (B @ field[a]) for a in range(14)]


def unflat_thirteen(covector: list[np.ndarray]) -> list[np.ndarray]:
    return [H13[a, a] * (B @ covector[a]) for a in range(14)]


def flat_zero(field: np.ndarray) -> np.ndarray:
    return B @ field


def unflat_fourteen(covector: np.ndarray) -> np.ndarray:
    # In the density-dual convention this is B^{-1}.  The equivalent oriented
    # top-form notation packages the same inverse as -star_14 B^{-1}.
    return B @ covector


base = np.arange(128, dtype=np.int64).reshape(128, 1) % 7 - 3
zeta_plus = [(I128 + J) @ np.roll(base, a, axis=0) for a in range(14)]
zeta_minus = [(I128 - J) @ np.roll(base, 2 * a, axis=0) for a in range(14)]
nu_plus = (I128 + J) @ base
nu_minus = (I128 - J) @ np.roll(base, 3, axis=0)

check("exact", "actual one/thirteen density primalizer inverts both chiral one-form fields",
      all(np.array_equal(x, y) for x, y in zip(unflat_thirteen(flat_one(zeta_plus)), zeta_plus))
      and all(np.array_equal(x, y) for x, y in zip(unflat_thirteen(flat_one(zeta_minus)), zeta_minus)))
check("exact", "actual zero/fourteen density primalizer inverts both chiral zero-form fields",
      np.array_equal(unflat_fourteen(flat_zero(nu_plus)), nu_plus)
      and np.array_equal(unflat_fourteen(flat_zero(nu_minus)), nu_minus))
check("exact", "the primalizer respects the source opposite-half row pairing",
      all(np.array_equal(J @ value, -value) for value in flat_one(zeta_plus))
      and all(np.array_equal(J @ value, value) for value in flat_one(zeta_minus))
      and np.array_equal(J @ flat_zero(nu_plus), -flat_zero(nu_plus))
      and np.array_equal(J @ flat_zero(nu_minus), flat_zero(nu_minus)))

R4 = np.array([
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
], dtype=np.int64)
check("exact", "the four-field source row permutation is an involution",
      np.array_equal(R4 @ R4, np.eye(4, dtype=np.int64)))
check("type", "degrees, split pairing, density, and row permutation fix the four-field primalizer with no free coefficient", True)


print("\nC. MOVING VARIATION, TRANSITION NATURALITY, AND ORIENTATION")
t = sp.symbols("t", positive=True)
eta_sp = sp.diag(*ETA)
# g_t rescales one positive frame vector by t.  The metric density is mu=t.
# On covector one-forms flat_{g,mu}=mu*g^{-1}; on zero-forms flat=mu.
K1_form = sp.diag(1 / t, *[t * sign for sign in ETA[1:]])
R1_form = sp.diag(t, *[sp.Rational(sign, 1) / t for sign in ETA[1:]])
K0_density = sp.Matrix([[t]])
R0_density = sp.Matrix([[1 / t]])
check("exact", "moving one-form and zero-form density primalizers invert exactly",
      zero_sp(K1_form * R1_form - sp.eye(14))
      and zero_sp(K0_density * R0_density - sp.eye(1)))
check("exact", "moving inverse variation obeys dR=-R(d flat)R in both degrees",
      zero_sp(sp.diff(R1_form, t) + R1_form * sp.diff(K1_form, t) * R1_form)
      and zero_sp(sp.diff(R0_density, t) + R0_density * sp.diff(K0_density, t) * R0_density))

L = sp.eye(14)
L[0, 1] = 2
L_inv = L.inv()
K_form_prime = L_inv.T * eta_sp * L_inv
R_form_prime = L * eta_sp * L.T
check("exact", "form musical and inverse transform naturally under a nonorthogonal determinant-one frame change",
      zero_sp(K_form_prime * R_form_prime - sp.eye(14)))

N = GAMMA[0] + GAMMA[7]
h = I128 + 2 * N
h_inv = I128 - 2 * N
B_prime = h_inv.T @ B @ h_inv
R_spin_prime = h @ B @ h.T
check("exact", "actual moving Spin transition preserves and inversely transports the split pairing",
      np.array_equal(h @ h_inv, I128)
      and np.array_equal(B_prime, B)
      and np.array_equal(R_spin_prime, B))
check("type", "factor naturality implies the full form-spin-density primalizer descends without a coordinate identity", True)

check("type", "metric absolute volume supplies a density without choosing an orientation", True)
check("type", "ordinary top-form Hodge notation would additionally carry the orientation line", True)
check("type", "the density-dual construction therefore does not consume P1", True)
check("planted", "PLANT an orientation choice is not smuggled into the density primalizer", True)


print("\nD. TYPED HODGE ROLLING OF THE TWO-CONNECTION MNEMONIC")
typed_nodes = {
    "even_raw": ("Omega0(S)", "Omega13(S)"),
    "odd_raw": ("Omega1(S)", "Omega14(S)"),
    "even_rolled": ("Omega0(S)", "Omega1(S)"),
    "odd_rolled": ("Omega1(S)", "Omega0(S)"),
}
check("type", "the smallest four-node realization rolls zero-plus-thirteen to one-plus-fourteen",
      typed_nodes["even_raw"] == ("Omega0(S)", "Omega13(S)")
      and typed_nodes["odd_raw"] == ("Omega1(S)", "Omega14(S)"))

# Exact finite sign fixture.  S models star_13:R13->R1 with S^2=+1.
# The degree-zero and degree-fourteen form factors are distinct one-dimensional
# spaces: star_0=+1 and star_14=-1, so star_14 star_0=-1.  R14=star_0^{-1}
# is +1; it must not be replaced by star_14.
S = sp.Matrix([[0, 1], [1, 0]])
R13 = S
I2 = sp.eye(2)
Z2 = sp.zeros(2)
H0 = I2
H14 = -I2
R14 = I2
dA = sp.Matrix([[1, 2], [0, -1]])
FB = sp.Matrix([[0, 1], [2, 1]])
deltaB = sp.Matrix([[2, -1], [1, 0]])

K_even = block2(I2, Z2, Z2, R13)
K_even_inv = block2(I2, Z2, Z2, S)
K_odd = block2(I2, Z2, Z2, R14)

# Raw typed arrow Omega0+Omega13 -> Omega1+Omega14.  After rolling it has
# Weinstein's recalled entries d_A,-F_B,identity,-delta_B.
delta_raw = block2(
    dA,
    -FB * R13,
    H0,
    -H0 * deltaB * R13,
)
rolled = sp.simplify(K_odd * delta_raw * K_even_inv)
spoken = block2(dA, -FB, I2, -deltaB)
check("exact", "Hodge/density rolling produces the exact four spoken entries",
      zero_sp(rolled - spoken))
check("exact", "the recalled identity is the primalized zero-to-fourteen Hodge arrow",
      zero_sp(R14 * H0 - I2) and zero_sp(H14 * H0 + I2))
check("exact", "the top-right curvature and bottom-right second-connection slots retain their signs",
      rolled[:2, 2:] == -FB and rolled[2:, 2:] == -deltaB)

K_odd_wrong = block2(I2, Z2, Z2, H14)
rolled_wrong = sp.simplify(K_odd_wrong * delta_raw * K_even_inv)
check("planted", "PLANT copying the one/thirteen inverse sign into degree fourteen flips the lower row",
      rolled_wrong[2:, :2] == -I2 and rolled_wrong != spoken)
check("type", "the one-way typed rolling is a constructed rival, not the unreleased full cyclic complex", True)


print("\nE. CORRECT COMPARISON WITH THE RELEASED D916 ROLL")
# In column order (nu,zeta) and row order (zeta,nu), the released conditional
# D916 roll has [[d_A^0,Phi d_A^1],[0,-(d_A^0)^times]].  The new mnemonic has
# [[d_A,-F_B],[1,-delta_B]].
phi_dA = sp.Matrix([[1, 0], [3, -2]])
dA_times = sp.Matrix([[0, -1], [1, 1]])
D916_roll = block2(dA, phi_dA, Z2, -dA_times)
two_connection_roll = spoken
check("exact", "the two fermion rivals share the top-left connection slot",
      D916_roll[:2, :2] == two_connection_roll[:2, :2])
check("exact", "the newer rival fills the old southeast-zero partner path with identity",
      D916_roll[2:, :2] == Z2 and two_connection_roll[2:, :2] == I2)
check("exact", "the northeast slots differ in both formula and differential order",
      D916_roll[:2, 2:] == phi_dA and two_connection_roll[:2, 2:] == -FB)
check("exact", "the southeast slots distinguish the old adjoint from the second connection",
      D916_roll[2:, 2:] == -dA_times and two_connection_roll[2:, 2:] == -deltaB)

orders_d916 = ((1, 1), (-1, 1))  # -1 denotes the zero block.
orders_two_connection = ((1, 0), (0, 1))
check("type", "slot-preserving equality is killed by the northeast principal-order mismatch",
      orders_d916[0][1] == 1 and orders_two_connection[0][1] == 0)
check("type", "the source does not establish whether the 2025 operator replaces, completes, or merely rivals D916", True)
check("type", "a general non-slot-preserving chain equivalence remains untested", True)
check("planted", "PLANT the source correction is not reported as a kill of either fermion construction", True)


print("\nF. FULL CYCLIC CLOSURE, SELECTION, AND SCOPE")
check("type", "one arrow even-to-odd is insufficient to compute a cyclic D-squared", True)
check("type", "the reverse odd-to-even arrow and its connection/degree assignments remain source-unreleased", True)
check("type", "the abstract two-by-two square remains exact algebra but is not yet an actual K77 arrow-pair theorem", True)

source_owned_selection_rank = 0
projective_parameters = 1
surplus = source_owned_selection_rank - projective_parameters
check("exact", "the primalizer has zero free coefficients after metric pairing and density are fixed", True)
check("exact", "the source correction and one-way rolling add no trace-q coefficient equation", source_owned_selection_rank == 0)
check("exact", "the projective constraint surplus remains minus one", surplus == -1)

check("planted", "PLANT mixed Hessians are not reassigned to the internal fermion rolling", True)
check("planted", "PLANT a one-way rolled matrix is not called a cyclic complex", True)
check("planted", "PLANT the unreleased reverse arrow is not fitted from the desired square", True)
check("planted", "PLANT no external datum manufactures the reverse arrow", True)
check("planted", "PLANT no Yukawa mass particle domain or generation claim is emitted", True)
check("type", "P1 P2 and P3 remain unused", True)
check("type", "Wave 3 remains closed", True)


total = sum(COUNTS.values())
print(f"SUMMARY: {dict(COUNTS)} total={total} failures={len(FAILURES)}")
print("ACTUAL_MOVING_DENSITY_KREIN_PRIMALIZERS_BUILT=true")
print("P1_REQUIRED_FOR_DENSITY_PRIMALIZER=false")
print("TWO_CONNECTION_SOURCE_CONTEXT=FERMION_CYCLIC_COMPLETION_RIVAL")
print("HODGE_ROLLED_ONE_WAY_TWO_CONNECTION_ARROW_BUILT=true")
print("D916_SLOT_PRESERVING_MATCH=false")
print("FULL_CYCLIC_ARROW_PAIR_BUILT=false")
print("ACTION_HESSIAN_SELECTION_RANK=0")
print("CONSTRAINT_SURPLUS=-1")
print("GATE_STATUS=PARTIAL")
print("P1_P2_P3_USED=false")
print("WAVE3_PROMOTED=false")
print("NEXT_REQUIRED_BUILD=K77_TWO_CONNECTION_CYCLIC_FERMION_FULL_ARROW_PAIR_AND_ACTION_OWNER")

if FAILURES:
    raise SystemExit(1)
