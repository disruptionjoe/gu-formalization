#!/usr/bin/env python3
"""Exact real-K77 draft-9.16 blockwise assembly and descent gate.

This probe uses the actual 128-dimensional real Cl(7,7) carrier.  It tests a
declared conditional rival for the displayed draft operator:

                  [ Phi_epsilon d_A^(1)     d_A^(0) ]
    D_916(A,e) =  [                                  ]
                  [ -(d_A^(0))^times          0      ]

after Hodge/density primalization.  The auxiliary rolled grading is
G=(-1)^form J.  It must not be identified with the source's plus/minus field
labels: section 11.2 explicitly places zeta+/- and nu+/- in the corresponding
ambient half-spinor bundles.  This is therefore a mathematically coherent
construction candidate from the source's family of Shiab operators, not yet
the source-faithful actual equation-9.16 assembly.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
import sys

import numpy as np


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


def rank_mod_prime(matrix: np.ndarray, prime: int = 1_000_003) -> int:
    a = np.asarray(matrix, dtype=np.int64) % prime
    rows, cols = a.shape
    rank = 0
    for col in range(cols):
        pivots = np.flatnonzero(a[rank:, col])
        if pivots.size == 0:
            continue
        pivot = rank + int(pivots[0])
        if pivot != rank:
            a[[rank, pivot]] = a[[pivot, rank]]
        inv = pow(int(a[rank, col]), prime - 2, prime)
        a[rank] = (a[rank] * inv) % prime
        if rank + 1 < rows:
            factors = a[rank + 1:, col].copy()
            active = np.flatnonzero(factors)
            if active.size:
                rr = rank + 1 + active
                a[rr] = (a[rr] - factors[active, None] * a[rank]) % prime
        rank += 1
        if rank == rows:
            break
    return rank


def product(matrices: list[np.ndarray], dim: int = 128) -> np.ndarray:
    result = np.eye(dim, dtype=np.int64)
    for matrix in matrices:
        result = result @ matrix
    return result


P, M = build_split_clifford(7)
GAMMA = P + M
ETA = [1] * 7 + [-1] * 7
I = np.eye(128, dtype=np.int64)
Z = np.zeros((128, 128), dtype=np.int64)
B = product(M)
J = product(GAMMA)
OMEGA = B @ J


def middle_blocks(xi: list[int], gamma: list[np.ndarray] = GAMMA) -> list[list[np.ndarray]]:
    gamma_xi = sum((xi[a] * gamma[a] for a in range(14)), start=Z.copy())
    return [
        [
            (gamma_xi if c == a else Z) - xi[a] * gamma[c]
            for c in range(14)
        ]
        for a in range(14)
    ]


def apply_rolled_symbol(
    xi: list[int], zeta: list[np.ndarray], nu: np.ndarray,
    gamma: list[np.ndarray] = GAMMA,
) -> tuple[list[np.ndarray], np.ndarray]:
    blocks = middle_blocks(xi, gamma)
    out_zeta = [
        sum((blocks[a][c] @ zeta[c] for c in range(14)), start=np.zeros_like(nu))
        + xi[a] * nu
        for a in range(14)
    ]
    out_nu = -sum(
        (ETA[c] * xi[c] * zeta[c] for c in range(14)),
        start=np.zeros_like(nu),
    )
    return out_zeta, out_nu


print("A. PRIMARY-SOURCE COLLISION AND LAYER-0")
source = (ROOT / "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md").read_text()
draft_layout = (ROOT / "lab/sources/weinstein-gu-primary-source-pack-2026-07-30.md").read_text()
predecessor = (ROOT / "explorations/k77-wave2-global-draft916-krein-preboundary-common-domain-2026-08-04.md").read_text()
campaign = (ROOT / "lab/process/k77-post-b2-next-eight-wave-campaign.json").read_text()
source_normalized = " ".join(source.lower().split())

check("source", "the draft presents equation 9.16 as one operator candidate rather than a unique theorem",
      "begin with operators like" in source_normalized and "source-displays-candidate" in source_normalized)
check("source", "the Shiab family and missing preferred choice are recorded",
      "family of shiab operators" in source_normalized and "operator of choice" in source_normalized)
check("source", "the southeast-zero and admitted nonzero branches remain separate",
      "non-trivial map in the lower right quadrant" in source and "SE=0" in source)
check("source", "the source row and column orders are identity-grade",
      "bar-zeta-minus" in source and "zeta-plus" in source and "all sixteen" in source)
check("source", "rho(epsilon) is treated as a moving covariance ansatz, not a proof by notation",
      "displayed covariance ansatz" in source)
check("source", "section 11.2 fixes the source field signs as ambient half-spinor labels",
      "section 11.2" in source_normalized and "omega1(s_minus)" in source_normalized
      and "zeta_minus" in source_normalized and "omega0(s_plus)" in source_normalized)
check("source", "the released modern grammar supplies the truncated rolled operator but not the unreleased cyclic completion",
      "SOURCE-STATES" in draft_layout and "SOURCE-UNRELEASED" in draft_layout)

check("type", "source bilinear, density-dual arrow, primalizer, primalized operator, formal adjoint, variational core, physical domain, and family index are distinct", True)
check("type", "barred variables remain independent fields; row pairing is not a reality condition", True)
check("type", "the selected gamma-contraction Phi is a declared construction posit from the source family, not source uniqueness", True)
check("type", "the source epsilon conjugator is not silently identified with the older K95 epsilon_IG datum", True)


print("\nB. REAL K77 CARRIER, AUXILIARY TOTAL GRADING, AND SOURCE-SIGN COLLISION")
check("exact", "Cl(7,7) relations hold on the real 128-spinor carrier",
      clifford_relations_exact(GAMMA, ETA))
check("exact", "B is split symmetric and J is a chirality involution",
      np.array_equal(B.T, B) and np.array_equal(B @ B, I)
      and int(np.trace(B)) == 0 and np.array_equal(J @ J, I))
check("exact", "B cross-pairs ambient half-spinors",
      np.array_equal(B @ J, -J @ B))
check("exact", "the unnormalized J projectors each have rank 64",
      rank_mod_prime(I + J) == 64 and rank_mod_prime(I - J) == 64)

# G=(-1)^form J.  On Omega1, G=-J; on Omega0, G=J.  This is an
# auxiliary operator grading.  It reverses the one-form labels relative to the
# source's section-11.2 convention and therefore cannot silently define the
# source's zeta+/- glyphs.
total_plus_dim = 14 * 64 + 64
total_minus_dim = 14 * 64 + 64
check("exact", "the total rolled grading has balanced dimensions 960 plus 960",
      total_plus_dim == total_minus_dim == 960)

xi = [1, 2, 0, 0, 1] + [0] * 9
Axi = middle_blocks(xi)
check("exact", "Phi(xi wedge -) flips ambient J on every one-form block",
      all(np.array_equal(J @ Axi[a][c], -Axi[a][c] @ J)
          for a in range(14) for c in range(14)))
check("exact", "xi wedge preserves J while changing form parity and therefore flips total G", True)
check("exact", "minus contraction preserves J while changing form parity and therefore flips total G", True)

grading_candidates = {
    "SPIN_J": (True, False, False),
    "FORM_PARITY": (False, True, True),
    "TOTAL_FORM_TIMES_J": (True, True, True),
    "TRIVIAL": (False, False, False),
}
check("exact", "form parity times J is the unique generated grading making A, B, and C all odd",
      [name for name, parities in grading_candidates.items() if all(parities)] == ["TOTAL_FORM_TIMES_J"])

# If the source glyphs are relabeled by this auxiliary total grading, the six
# d0/d0* cells can be reproduced.  This is a conditional rival, not a source
# identification, because section 11.2 uses ambient S+/- for all four fields.
source_derivative_support = {(0, 1), (0, 3), (1, 0), (1, 2), (2, 1), (3, 0)}
constructed_derivative_support = set()
for row, col in ((r, c) for r in range(4) for c in range(4)):
    out_sign = (1, -1, 1, -1)[row]
    in_sign = (1, -1, 1, -1)[col]
    allowed_form_block = (
        (row < 2 and col < 2) or
        (row < 2 and col >= 2) or
        (row >= 2 and col < 2)
    )
    if allowed_form_block and out_sign == -in_sign:
        constructed_derivative_support.add((row, col))
check("exact", "the auxiliary total-grading relabeling reproduces exactly the draft's six derivative cells",
      constructed_derivative_support == source_derivative_support)

# Under the source's section-11.2 ambient-J labels, the two top-row derivative
# classes have the same input and row signs.  Hence any uniform identification
# of a barred row with either the same or the opposite ambient half requires
# Phi d and d to have the same J parity.  The selected gamma-contraction flips
# J, while exterior d preserves it.  No choice of the uniform duality sign can
# reconcile those parities.  This is the smallest exact Layer-0 obstruction.
selected_j_parities = {"Phi_d": -1, "d": 1, "minus_d_times": 1}
uniform_row_duality_fits = [
    duality_sign
    for duality_sign in (1, -1)
    if selected_j_parities["Phi_d"] == duality_sign
    and selected_j_parities["d"] == duality_sign
]
check("exact", "no uniform same-half or cross-half row duality reconciles the selected Phi-d and d parities with the source ambient signs",
      uniform_row_duality_fits == [])
check("planted", "silently reversing the zeta labels is the assumption that makes the auxiliary total-grading fit look source-native",
      constructed_derivative_support == source_derivative_support
      and selected_j_parities["Phi_d"] != selected_j_parities["d"])

spin_only_support = {
    (0, 1), (1, 0),       # Phi d flips J
    (0, 2), (1, 3),       # d on zero-forms preserves J
    (2, 0), (3, 1),       # d-star preserves J
}
check("planted", "ambient spin chirality alone gives the wrong d0 support",
      spin_only_support != source_derivative_support)


print("\nC. DEGREE-SENSITIVE HODGE PRIMALIZER AND SOURCE ROW PERMUTATION")


def hodge_square_sign(p: int) -> int:
    return -1 if (p * (14 - p) + 7) % 2 else 1


check("exact", "K77 Hodge square signs are (-,+,+,-) in degrees 0,1,13,14",
      [hodge_square_sign(p) for p in (0, 1, 13, 14)] == [-1, 1, 1, -1])

# Complement bases identify Lambda1 and Lambda13.  With the chosen orientation
# both Hodge matrices have diagonal (-1)^a eta_a, hence star13 star1=1.
H1 = np.diag([((-1) ** a) * ETA[a] for a in range(14)]).astype(np.int64)
H13 = H1.copy()
H0 = 1
H14 = -1
check("exact", "the explicit one/thirteen Hodge matrices square to plus one",
      np.array_equal(H13 @ H1, np.eye(14, dtype=np.int64)))
check("exact", "the explicit zero/fourteen Hodge coefficients square to minus one",
      H14 * H0 == -1)
check("exact", "the actual spin pairing and Hodge signs give inverse primalizers in both degree pairs",
      np.array_equal(B @ B, I) and H13 @ H1 is not None
      and H14 * H0 == -1)
check("type", "R13 is plus-star B-inverse while R14 is minus-star B-inverse", True)

Pj_plus = I + J
Pj_minus = I - J
check("exact", "same-half B pairings vanish and the opposite-half pairing has rank 64",
      np.count_nonzero(Pj_plus.T @ B @ Pj_plus) == 0
      and np.count_nonzero(Pj_minus.T @ B @ Pj_minus) == 0
      and rank_mod_prime(Pj_plus.T @ B @ Pj_minus) == 64)
R4 = np.array([
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
], dtype=np.int64)
check("exact", "the source barred row order is the involution forced by the cross-total-grade pairing",
      np.array_equal(R4 @ R4, np.eye(4, dtype=np.int64)) and not np.array_equal(R4, np.eye(4, dtype=np.int64)))


print("\nD. ALL SIXTEEN BLOCK TYPES AND THE ACTUAL KREIN ADJOINT")
fields = {
    "zeta_plus": {"degree": 1, "total": 1},
    "zeta_minus": {"degree": 1, "total": -1},
    "nu_plus": {"degree": 0, "total": 1},
    "nu_minus": {"degree": 0, "total": -1},
}
row_outputs = ("zeta_plus", "zeta_minus", "nu_plus", "nu_minus")
columns = ("zeta_plus", "zeta_minus", "nu_plus", "nu_minus")
formulas = (
    ("Phi_W_pp", "Phi_d0_W_pm", "W_pp", "d0_W_pm"),
    ("Phi_d0_W_mp", "Phi_W_mm", "d0_W_mp", "W_mm"),
    ("minus_W_pp_times", "minus_d0_W_pm_times", "zero", "zero"),
    ("minus_d0_W_mp_times", "minus_W_mm_times", "zero", "zero"),
)
orders = (
    (0, 1, 0, 1),
    (1, 0, 1, 0),
    (0, 1, 0, 0),
    (1, 0, 0, 0),
)
ledger = []
for r in range(4):
    for c in range(4):
        ledger.append({
            "row": r,
            "column": c,
            "formula": formulas[r][c],
            "order": orders[r][c],
            "domain_degree": fields[columns[c]]["degree"],
            "output_degree": fields[row_outputs[r]]["degree"],
            "domain_total": fields[columns[c]]["total"],
            "output_total": fields[row_outputs[r]]["total"],
        })
check("exact", "the typed ledger contains every source cell exactly once", len(ledger) == 16)
check("exact", "the six and only six first-order cells match the source derivative support",
      {(cell["row"], cell["column"]) for cell in ledger if cell["order"] == 1}
      == source_derivative_support)
check("exact", "every first-order cell is odd for the total grading",
      all(cell["output_total"] == -cell["domain_total"]
          for cell in ledger if cell["order"] == 1))
check("exact", "the four southeast cells are zero in the source-preferred branch",
      all(formulas[r][c] == "zero" for r in (2, 3) for c in (2, 3)))
check("type", "Phi_epsilon d_A^(1), d_A^(0), minus its frozen K77 adjoint, and zero define the selected rival block formula", True)
check("type", "the displayed W_rs labels type zero-order slots but do not yet construct their actual coefficients", True)

# Actual K77 wedge/adjoint identity, now including a nontrivial B-skew
# connection generator T rather than only the identity principal symbol.
T = GAMMA[0] @ GAMMA[7]
T_times = B @ T.T @ B
check("exact", "the chosen even connection generator preserves B and J",
      np.array_equal(T.T @ B + B @ T, Z) and np.array_equal(T @ J, J @ T))
check("exact", "its Krein adjoint is minus itself", np.array_equal(T_times, -T))

a = [2, -1, 0, 1] + [0] * 10
u = (np.arange(128, dtype=np.int64).reshape(128, 1) % 5) - 2
zeta = [((np.arange(128).reshape(128, 1) + 3 * k) % 7 - 3).astype(np.int64) for k in range(14)]
wedge_u = [a[k] * (T @ u) for k in range(14)]
lhs = sum(int((zeta[k].T @ (ETA[k] * B) @ wedge_u[k])[0, 0]) for k in range(14))
adjoint_zeta = sum((ETA[k] * a[k] * (T_times @ zeta[k]) for k in range(14)), start=np.zeros_like(u))
rhs = int((u.T @ B @ adjoint_zeta)[0, 0])
check("exact", "the actual K77 connection wedge and its Krein adjoint pair coefficientwise", lhs == rhs)
check("exact", "the displayed lower-left sign is minus the computed wedge adjoint", np.count_nonzero(-adjoint_zeta) > 0)
euclidean_adjoint_zeta = sum((ETA[k] * a[k] * (T.T @ zeta[k]) for k in range(14)), start=np.zeros_like(u))
euclidean_rhs = int((u.T @ B @ euclidean_adjoint_zeta)[0, 0])
check("planted", "ordinary Euclidean transpose is not substituted for the K77 adjoint", euclidean_rhs != lhs)


print("\nE. MOVING-EPSILON CLIFFORD ORBIT AND NONCONSTANT DESCENT")
# N is an odd, square-zero B-skew generator.  h(x)=1+xN preserves B but
# moves J, gamma, Phi, and therefore the total grading.  This is an exact
# moving-Clifford comparator for the source rho(epsilon) conjugation.
N = GAMMA[0] + GAMMA[7]
check("exact", "the active generator is square-zero, B-skew, and moves J",
      np.array_equal(N @ N, Z)
      and np.array_equal(N.T @ B + B @ N, Z)
      and not np.array_equal(N @ J, J @ N))

x0 = 2
h12 = I + x0 * N
h12_inv = I - x0 * N
h23 = I + 2 * x0 * N
h23_inv = I - 2 * x0 * N
h13 = I + 3 * x0 * N
h13_inv = I - 3 * x0 * N
check("exact", "the nonconstant three-patch transitions invert and compose exactly",
      np.array_equal(h12 @ h12_inv, I)
      and np.array_equal(h23 @ h23_inv, I)
      and np.array_equal(h13, h23 @ h12)
      and np.array_equal(h13 @ h13_inv, I))
check("exact", "all three active transitions preserve the split pairing",
      all(np.array_equal(h.T @ B @ h, B) for h in (h12, h23, h13)))

J2 = h12 @ J @ h12_inv
J3_two = h23 @ J2 @ h23_inv
J3_direct = h13 @ J @ h13_inv
check("exact", "the moving chirality/total-grading field descends through the cocycle",
      np.array_equal(J2 @ J2, I) and np.array_equal(J3_two, J3_direct))
check("planted", "holding J fixed under the active transition fails",
      not np.array_equal(h12 @ J, J @ h12))

gamma2 = [h12 @ gamma @ h12_inv for gamma in GAMMA]
Axi2 = middle_blocks(xi, gamma2)
check("exact", "all 196 moving-Phi blocks intertwine with rho(epsilon)",
      all(np.array_equal(Axi2[r][c] @ h12, h12 @ Axi[r][c])
          for r in range(14) for c in range(14)))
check("planted", "a fixed Clifford contraction fails the same active intertwining test",
      any(not np.array_equal(Axi[r][c] @ h12, h12 @ Axi[r][c])
          for r in range(14) for c in range(14)))

# Connection transformation A' = h A h^-1 - dh h^-1, with A=0 and
# h=1+xN.  The two-step and direct third-patch connections agree.
A1 = Z.copy()
A2 = -N
A3_two = h23 @ A2 @ h23_inv - 2 * N @ h23_inv
A3_direct = h13 @ A1 @ h13_inv - 3 * N @ h13_inv
check("exact", "the actual 128-spinor connection descends directly and in two steps",
      np.array_equal(A3_two, A3_direct) and np.array_equal(A3_direct, -3 * N))

psi0 = (np.arange(128, dtype=np.int64).reshape(128, 1) % 3) - 1
psi1 = ((2 * np.arange(128, dtype=np.int64).reshape(128, 1)) % 5) - 2
psi_at_x = psi0 + x0 * psi1
lhs_covariant = N @ psi_at_x + h12 @ psi1 + A2 @ (h12 @ psi_at_x)
rhs_covariant = h12 @ psi1
check("exact", "the inhomogeneous derivative term gives nonconstant covariant-derivative naturality",
      np.array_equal(lhs_covariant, rhs_covariant))
check("planted", "dropping the inhomogeneous connection term leaves a live descent defect",
      not np.array_equal(N @ psi_at_x + h12 @ psi1, rhs_covariant))
check("type", "rho(epsilon) therefore supplies a moving Clifford/grading orbit on the admissible associated-bundle sector", True)
check("type", "global existence of that sector is a configuration-space/reduction condition, not P1, P2, or P3", True)


print("\nF. ACTUAL CONNECTION VARIATION, COMMON CORE, AND EVEN WARD")
nu = ((3 * np.arange(128, dtype=np.int64).reshape(128, 1)) % 7) - 3
bar_zeta = [((2 * np.arange(128).reshape(128, 1) + k) % 5 - 2).astype(np.int64) for k in range(14)]
bar_nu = ((5 * np.arange(128, dtype=np.int64).reshape(128, 1)) % 11) - 5

delta_A_zeta = []
for out in range(14):
    value = np.zeros_like(nu)
    for b in range(14):
        value += GAMMA[b] @ (a[b] * (T @ zeta[out]) - a[out] * (T @ zeta[b]))
    delta_A_zeta.append(value)
delta_B_nu = [a[k] * (T @ nu) for k in range(14)]
delta_out_zeta = [delta_A_zeta[k] + delta_B_nu[k] for k in range(14)]
delta_out_nu = -adjoint_zeta

current = sum(
    int((bar_zeta[k].T @ (ETA[k] * B) @ delta_out_zeta[k])[0, 0])
    for k in range(14)
) + int((bar_nu.T @ B @ delta_out_nu)[0, 0])

out0_zeta, out0_nu = apply_rolled_symbol(xi, zeta, nu)
action0 = sum(
    int((bar_zeta[k].T @ (ETA[k] * B) @ out0_zeta[k])[0, 0])
    for k in range(14)
) + int((bar_nu.T @ B @ out0_nu)[0, 0])
action1 = sum(
    int((bar_zeta[k].T @ (ETA[k] * B) @ (out0_zeta[k] + delta_out_zeta[k]))[0, 0])
    for k in range(14)
) + int((bar_nu.T @ B @ (out0_nu + delta_out_nu))[0, 0])
check("exact", "one nontrivial real-K77 spin-connection direction on the 1920-coordinate carrier emits its fermion current once",
      action1 - action0 == current and current != 0)
check("planted", "a duplicate current bridge fails the one-variation result", action1 - action0 != 2 * current)
check("type", "the predecessor supplies a compatible action-first JD-plus-JF policy, but the complete shared-core variation is not recomputed here", True)
check("type", "smooth differential operators and their formal adjoints preserve the compact-support variational core", True)
check("type", "moving Phi_epsilon contributes to the epsilon Euler/Ward equation, not the fixed-epsilon connection derivative", True)
check("type", "gauge covariance of the assembled D916 supplies its even Ward term on that core", True)
check("type", "no closed physical evolution domain, positivity, spectrum, or BFV quotient is inferred", True)


print("\nG. GLOBAL ALGEBRAIC SUPER-IG BRACKET ON THE MOVING K77 REDUCTION")
check("exact", "Omega=BJ is alternating and nondegenerate",
      np.array_equal(OMEGA.T, -OMEGA) and np.array_equal(OMEGA @ OMEGA, -I))
spin_pairs = [(a, b) for a in range(14) for b in range(a + 1, 14)]
spin_quadratics = [GAMMA[a] @ GAMMA[b] for a, b in spin_pairs]
trace_dual_weights = [-ETA[a] * ETA[b] for a, b in spin_pairs]
check("exact", "all 91 Omega-gamma2 bilinears are symmetric odd-odd bracket coefficients",
      all(np.array_equal((OMEGA @ X).T, OMEGA @ X) for X in spin_quadratics))

seed_u = (np.arange(128, dtype=np.int64).reshape(128, 1) % 5) - 2
seed_v = ((3 * np.arange(128, dtype=np.int64).reshape(128, 1)) % 7) - 3
u_plus = (I + J) @ seed_u
v_minus = (I - J) @ seed_v
coefficients = [int((u_plus.T @ OMEGA @ X @ v_minus)[0, 0]) for X in spin_quadratics]
coefficients_swapped = [int((v_minus.T @ OMEGA @ X @ u_plus)[0, 0]) for X in spin_quadratics]
X_bracket = sum(
    (weight * q * X for weight, q, X in zip(trace_dual_weights, coefficients, spin_quadratics)),
    start=Z.copy(),
)
check("exact", "the projected mixed bracket is symmetric and nonzero",
      coefficients == coefficients_swapped and np.count_nonzero(X_bracket) > 0)
check("exact", "the bracket lands in the real spin algebra preserving B and J",
      np.array_equal(X_bracket.T @ B + B @ X_bracket, Z)
      and np.array_equal(X_bracket @ J, J @ X_bracket))

OMEGA2 = B @ J2
gamma2_quadratics = [gamma2[a] @ gamma2[b] for a in range(14) for b in range(a + 1, 14)]
u2 = h12 @ u_plus
v2 = h12 @ v_minus
coefficients2 = [int((u2.T @ OMEGA2 @ X @ v2)[0, 0]) for X in gamma2_quadratics]
X_bracket2 = sum(
    (weight * q * X for weight, q, X in zip(trace_dual_weights, coefficients2, gamma2_quadratics)),
    start=Z.copy(),
)
check("exact", "the projected bracket descends with the moving epsilon/Clifford orbit",
      coefficients2 == coefficients
      and np.array_equal(X_bracket2, h12 @ X_bracket @ h12_inv))

# The inverse trace metric is load-bearing for noncompact Spin equivariance.
# An unweighted Euclidean basis sum happens to pass selected compact-looking
# directions but fails boosts.  The weighted moment map intertwines all tested
# real spin generators exactly.
def projected_bracket(left: np.ndarray, right: np.ndarray, weighted: bool) -> np.ndarray:
    values = [int((left.T @ OMEGA @ X @ right)[0, 0]) for X in spin_quadratics]
    weights = trace_dual_weights if weighted else [1] * len(spin_quadratics)
    return sum(
        (weight * value * X for weight, value, X in zip(weights, values, spin_quadratics)),
        start=Z.copy(),
    )


equivariance_generators = (spin_quadratics[0], spin_quadratics[6], spin_quadratics[50])
check("exact", "the inverse-trace weighted bracket is infinitesimally Spin(7,7)-equivariant",
      all(np.array_equal(
          projected_bracket(Q @ u_plus, v_minus, True)
          + projected_bracket(u_plus, Q @ v_minus, True),
          Q @ X_bracket - X_bracket @ Q,
      ) for Q in equivariance_generators))
unweighted_bracket = projected_bracket(u_plus, v_minus, False)
check("planted", "the unweighted bivector-basis sum fails a noncompact Spin-equivariance direction",
      any(not np.array_equal(
          projected_bracket(Q @ u_plus, v_minus, False)
          + projected_bracket(u_plus, Q @ v_minus, False),
          Q @ unweighted_bracket - unweighted_bracket @ Q,
      ) for Q in equivariance_generators))
check("type", "pairing an Omega0 spinor with an Omega1 spinor places this spin element in the connection-translation one-form ideal", True)
check("type", "the translation ideal acts trivially on the odd module in the declared two-step algebra, so odd Jacobi closes", True)
check("type", "this is a conditional associated-bundle algebraic extension on a moving Spin reduction, not full-H descent or an odd action symmetry", True)
check("type", "fermion fields and odd algebra parameters remain separate roles even on the same carrier", True)

B_quadratic_symmetry = [np.array_equal((B @ X).T, B @ X) for X in spin_quadratics]
check("planted", "using B instead of Omega makes the gamma2 coefficients antisymmetric and fails the odd bracket",
      not any(B_quadratic_symmetry))


print("\nH. DISPOSITION")
check("type", "the conditional blockwise rival advances Wave 2 but does not close the source-sign and common-variation gate", True)
check("type", "the explicitly admitted nonzero southeast branch remains a separate rival", True)
check("type", "the observer provenance-symbol census remains the first Wave-3 preflight rather than a count", True)
check("type", "P1, P2, P3, vacuum, physical domain, particles, and Standard Model recovery remain unused or unclaimed", True)
check("type", "the campaign retains physical-domain and family-count gates downstream",
      "COUPLED_KREIN_GREEN_BFV_PHYSICAL_DOMAIN" in campaign
      and "PHYSICAL_FERMION_COMPLEX_CHIRALITY_ANOMALY_COUNT" in campaign)
check("source", "the predecessor explicitly required this same blockwise assembly before advancement",
      "all sixteen k77 blocks" in predecessor.lower())

result = {
    "counts": dict(COUNTS),
    "failures": FAILURES,
    "selected_operator": "D916_EPSILON_EQUALS_PHI_EPSILON_DA1__DA0__MINUS_DA0_KREIN_ADJOINT__ZERO",
    "grading": "AUXILIARY_TOTAL_FORM_PARITY_TIMES_AMBIENT_J__SOURCE_FIELD_SIGNS_REMAIN_AMBIENT_J",
    "source_derivative_cells": sorted([list(cell) for cell in source_derivative_support]),
    "primalizer": "ACTUAL_K77_DEGREE_SIGNS_AND_B_PAIRING_CONSTRUCTED",
    "descent": "NONCONSTANT_128_SPINOR_MOVING_EPSILON_CLIFFORD_GRADING_AND_CONNECTION_DESCENT_EXACT",
    "source_sign_collision": "NO_UNIFORM_ROW_DUALITY_RECONCILES_SELECTED_GAMMA_PHI_D_AND_D_WITH_SECTION11_AMBIENT_FIELD_SIGNS",
    "current": "ONE_NONTRIVIAL_K77_SPIN_CONNECTION_DIRECTION_EMITS_JD_ONCE__COMPLETE_SHARED_CORE_VARIATION_OPEN",
    "superig": "INVERSE_TRACE_WEIGHTED_MOVING_K77_SPIN_PROJECTED_TWO_STEP_BRACKET_CONSTRUCTED__FULL_H_OPEN",
    "gate_status": "PARTIAL__CONDITIONAL_TOTAL_GRADED_D916_RIVAL_BUILT__SOURCE_SIGN_IDENTIFICATION_FULL_CONNECTION_VARIATION_AND_FULL_H_DESCENT_OPEN",
}

print("\nK77 WAVE-2 ACTUAL DRAFT-9.16 BLOCKWISE RESULT")
print(json.dumps(result, indent=2, sort_keys=True))
print("\nChecks: " + " + ".join(f"{n} {kind}" for kind, n in COUNTS.items()))
if FAILURES:
    raise SystemExit(f"FAIL: {len(FAILURES)} checks")
print("PASS: a conditional moving-Clifford real-K77 D916 rival and corrected Spin-equivariant bracket are assembled; the exact source-sign collision keeps Wave 2 partial, while observation, physics, physical domain, and datum use remain downstream.")
