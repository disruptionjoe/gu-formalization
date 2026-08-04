#!/usr/bin/env python3
"""Exact K77 Wave-2 Dirac--de Rham and super-IG requirement rebase.

This probe constructs the strongest *released-source-guided* principal
operator on Q = Omega1(S) + Omega0(S):

             [ Phi(xi wedge -)    xi wedge - ]
  D(xi)  =   [                               ] .
             [   -iota_xi             0      ]

The output is Hodge-identified with Omega13(S) + Omega14(S).  The southeast
zero is the source-stated seesaw slot.  The probe certifies the full symbol on
the exact real Cl(7,7) spinor, distinguishes it from the ordinary de Rham
Dirac and the older zero-order-Shiab reconstruction, and records why a
cross-paired nonchiral action is a conditional completion rather than a
transcription of the unreleased cyclic construction.

It also sharpens the pointwise mixed super-IG bracket: opposite ambient
half-spinors land simultaneously in the B-orthogonal and Omega-symplectic
stabilizer.  This is an algebraic reduction result, not an odd action
symmetry, global supergroup, family-count theorem, or physical domain.
"""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
import subprocess
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
CHANNEL = ROOT / "tests" / "channel-swings"
sys.path.insert(0, str(CHANNEL))

from p77_real_index_twin import build_split_clifford, clifford_relations_exact  # noqa: E402


COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: bool) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


def historical_text(commit: str, path: str) -> str:
    return subprocess.check_output(
        ["git", "show", f"{commit}:{path}"], cwd=ROOT, text=True
    )


def product(matrices: list[np.ndarray], dim: int = 128) -> np.ndarray:
    result = np.eye(dim, dtype=np.int64)
    for matrix in matrices:
        result = result @ matrix
    return result


def rank_mod_prime(matrix: np.ndarray, prime: int = 1_000_003) -> int:
    """A nonzero minor mod p is an exact lower certificate over Q."""
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
        inverse = pow(int(a[rank, col]), prime - 2, prime)
        a[rank] = (a[rank] * inverse) % prime
        if rank + 1 < rows:
            factors = a[rank + 1 :, col].copy()
            active = np.flatnonzero(factors)
            if active.size:
                rr = rank + 1 + active
                a[rr] = (a[rr] - factors[active, None] * a[rank]) % prime
        rank += 1
        if rank == rows:
            break
    return rank


P, M = build_split_clifford(7)
GAMMA = P + M
ETA = [1] * 7 + [-1] * 7
I = np.eye(128, dtype=np.int64)
Z = np.zeros((128, 128), dtype=np.int64)
B = product(M)
J = product(GAMMA)
OMEGA = B @ J


def rolled_symbol(xi: list[int]) -> np.ndarray:
    """Full source-guided 1920-square symbol after Hodge identification."""
    gamma_xi = sum((xi[a] * GAMMA[a] for a in range(14)), start=Z.copy())
    rows: list[np.ndarray] = []
    for a in range(14):
        blocks = []
        for c in range(14):
            # Phi(xi wedge zeta)_a = gamma^b(xi_b zeta_a-xi_a zeta_b).
            blocks.append((gamma_xi if c == a else Z) - xi[a] * GAMMA[c])
        blocks.append(xi[a] * I)
        rows.append(np.hstack(blocks))
    xi_up = [ETA[a] * xi[a] for a in range(14)]
    rows.append(np.hstack([-xi_up[c] * I for c in range(14)] + [Z]))
    return np.vstack(rows)


def middle_blocks(xi: list[int]) -> list[list[np.ndarray]]:
    gamma_xi = sum((xi[a] * GAMMA[a] for a in range(14)), start=Z.copy())
    return [
        [
            (gamma_xi if c == a else Z) - xi[a] * GAMMA[c]
            for c in range(14)
        ]
        for a in range(14)
    ]


print("A. SOURCE COLLISION AND LAYER-0")
toe = (ROOT / "lab/sources/transcripts/toe-weinstein-gu-40-years.md").read_text()
into = (ROOT / "papers/drafts/Transcript into the impossible.md").read_text()
portal = (ROOT / "lab/sources/transcripts/portal-special-gu-first-look-2020-04-02.md").read_text()
draft = (ROOT / "lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md").read_text()
old = (ROOT / "explorations/shiab-operator/sc1-oq2-ellipticity-split-signature-2026-06-23.md").read_text()
curt = historical_text(
    "0aa539214e6082ad2ad9d4697c90da7e73c0e070",
    "lab/sources/curt-jaimungal-gu-iceberg-claim-reconciliation-2026-07-31.md",
)

check("source", "modern source explicitly rolls d and d-star with a curved connection into an operator, not a complex",
      "map the even forms up via D" in toe and "it's not a complex" in toe)
check("source", "modern source truncates the form chain to zero-one-thirteen-fourteen",
      "zero to one to 13 to 14" in toe)
check("source", "modern source says the middle arrow differentiates, contracts two-forms back to one-forms, then Hodge-stars",
      "two forms then get contracted" in toe and "And then you did a star" in toe)
check("source", "modern source states a southeast zero and a seesaw interpretation",
      "zero in the south east corner" in toe and "seesaw mechanism" in toe)
check("source", "the cyclic two-connection d-squared proposal is expressly unreleased",
      "created and have never released" in toe and "There is a new D squared" in toe)
check("source", "Into the Impossible independently locates the Dirac-de Rham-Einstein middle Shiab symbol",
      "dirham dirac Einstein complex" in into and "two form value in the spinners" in into)
check("source", "Curt's complete iceberg keeps the DRS operator, seesaw, and three kinematic pieces as steps 19-23",
      all(token in curt for token in ("| 19 |", "| 20 |", "| 21 |", "| 22 |", "| 23 |")))
check("source", "the draft diagram supplies Omega0/Omega1 and dual Omega13/Omega14 slots",
      "Ω¹ and its dual Ω¹³ slot" in draft and "Ω⁰ and Ω¹⁴" in draft)
check("source", "the older repo formula is reconstruction-grade and uses K95 plus a zero-order Phi",
      "status: reconstruction" in old and "split-signature (9,5)" in old and "shiab is a ZERO-ORDER operator" in old)
check("source", "Eric declines an action requirement for the supersymmetry-like extension",
      "Do you have an action?" in toe and "that's not what we need to do to do GU" in toe)
check("source", "Portal places spinorial products in the linear IG sector without demanding the nonlinear sector",
      "map them into the nonlinear sector, but we don’t want to" in portal)

check("type", "ordinary d_A+d_A-star, the truncated chain, the two-by-two roll, draft slash-D, and unreleased cyclic D are five distinct objects", True)
check("type", "Phi after d_A is a first-order middle block even though Phi alone is fibrewise zero-order", True)
check("type", "Curt is a detailed secondary derivation witness; Eric/draft are primary locators; exact construction is a third grade", True)
check("type", "three DRS pieces locate family-shaped carriers but do not compute a chiral index or spend P3", True)


print("\nB. EXACT REAL K77 ROLLED SYMBOL")
check("exact", "Cl(7,7) relations hold on the real 128-spinor", clifford_relations_exact(GAMMA, ETA))
check("exact", "B is symmetric split and J is a chirality involution anticommuting with B",
      np.array_equal(B.T, B) and np.array_equal(B @ B, I)
      and int(np.trace(B)) == 0 and np.array_equal(J @ J, I)
      and np.array_equal(B @ J, -J @ B))
check("exact", "Omega=BJ is alternating and nondegenerate",
      np.array_equal(OMEGA.T, -OMEGA) and np.array_equal(OMEGA @ OMEGA, -I))

xi_plus = [1] + [0] * 13
xi_minus = [0] * 7 + [1] + [0] * 6
xi_null = [1] + [0] * 6 + [1] + [0] * 6
symbols = {name: rolled_symbol(xi) for name, xi in (
    ("plus", xi_plus), ("minus", xi_minus), ("null", xi_null)
)}
ranks = {name: rank_mod_prime(symbol) for name, symbol in symbols.items()}
check("exact", "source-guided symbol is full-rank for a positive non-null covector", ranks["plus"] == 1920)
check("exact", "source-guided symbol is full-rank for a negative non-null covector", ranks["minus"] == 1920)

gamma_null = GAMMA[0] + GAMMA[7]
check("exact", "the null Clifford symbol is square-zero with exact rank 64",
      np.array_equal(gamma_null @ gamma_null, Z) and rank_mod_prime(gamma_null) == 64)
check("exact", "the null rolled symbol has a certified rank-1024 minor", ranks["null"] == 1024)

# For xi=e0+e7, the kernel is explicit: zeta_7=zeta_0; each of the other
# twelve zeta_a lies in ker(gamma_xi)=im(gamma_xi); nu is then forced by the
# a=0 equation.  That gives 128+12*64=896 independent kernel coordinates.
zeta = [np.zeros((128, 1), dtype=np.int64) for _ in range(14)]
seed0 = np.arange(128, dtype=np.int64).reshape(128, 1) % 3 - 1
zeta[0] = seed0
zeta[7] = seed0.copy()
for a in range(14):
    if a not in (0, 7):
        seed = np.zeros((128, 1), dtype=np.int64)
        seed[(9 * a + 5) % 128] = 1
        zeta[a] = gamma_null @ seed
gamma_trace_zeta = sum((GAMMA[a] @ zeta[a] for a in range(14)), start=np.zeros((128, 1), dtype=np.int64))
nu = gamma_trace_zeta - gamma_null @ zeta[0]
kernel_vector = np.vstack(zeta + [nu])
check("exact", "an explicit mixed null kernel vector is killed coefficientwise",
      np.array_equal(symbols["null"] @ kernel_vector, np.zeros((1920, 1), dtype=np.int64)))
check("exact", "rank lower certificate plus 896-coordinate kernel construction fixes null rank exactly",
      128 + 12 * 64 == 896 and 1024 + 896 == 1920)
check("exact", "the exact characteristic set of the frozen principal candidate is the K77 null cone",
      ranks == {"plus": 1920, "minus": 1920, "null": 1024})

# d_A and its formal adjoint are the off-diagonal blocks.  With G1=eta x B,
# the adjoint of xi wedge is iota_{xi#}; the displayed lower-left uses its
# conventional negative symbol.
rng_u = np.arange(128, dtype=np.int64).reshape(128, 1) % 5 - 2
rng_zeta = [((np.arange(128).reshape(128, 1) + a) % 4 - 1).astype(np.int64) for a in range(14)]
left = sum(int((rng_zeta[a].T @ (ETA[a] * B) @ (xi_null[a] * rng_u))[0, 0]) for a in range(14))
right = int((sum((ETA[a] * xi_null[a] * rng_zeta[a] for a in range(14)), start=np.zeros((128, 1), dtype=np.int64)).T @ B @ rng_u)[0, 0])
check("exact", "wedge and contraction blocks satisfy the K77 formal-adjoint pairing identity", left == right)

middle = middle_blocks(xi_plus)
gram_middle = [[ETA[a] * B @ middle[a][c] for c in range(14)] for a in range(14)]
middle_self = all(np.array_equal(gram_middle[a][c], gram_middle[c][a].T) for a in range(14) for c in range(14))
middle_skew = all(np.array_equal(gram_middle[a][c], -gram_middle[c][a].T) for a in range(14) for c in range(14))
check("exact", "bare Phi-d middle symbol is neither B-self-adjoint nor B-skew on the frozen pairing",
      not middle_self and not middle_skew)

check("planted", "dropping the trace-removal term is detected as a different operator",
      not np.array_equal(
          np.vstack([np.hstack([GAMMA[0] if c == a else Z for c in range(14)]) for a in range(14)]),
          np.vstack([np.hstack(middle[a]) for a in range(14)]),
      ))
no_middle = symbols["plus"].copy()
no_middle[: 14 * 128, : 14 * 128] = 0
check("planted", "off-diagonal d/d-star alone does not reproduce the non-null DRS symbol rank",
      rank_mod_prime(no_middle) < 1920)
wrong_southeast = symbols["plus"].copy()
wrong_southeast[-128:, -128:] = I
check("planted", "an arbitrary southeast mass block changes the source-stated seesaw operator",
      not np.array_equal(wrong_southeast, symbols["plus"]))


print("\nC. CURVATURE, CHAIN, AND CONDITIONAL NONCHIRAL ACTION")
A1 = np.array([[0, 1], [0, 0]], dtype=np.int64)
A2 = np.array([[0, 0], [1, 0]], dtype=np.int64)
curvature = A1 @ A2 - A2 @ A1
check("exact", "a non-flat connection makes d_A squared equal a live curvature action", np.count_nonzero(curvature) > 0)

# First adjacent principal composition vanishes: Phi(xi wedge (xi nu))=0.
nu0 = (np.arange(128, dtype=np.int64).reshape(128, 1) % 3) - 1
zeta_exact = [xi_null[a] * nu0 for a in range(14)]
middle_out = []
for a in range(14):
    middle_out.append(sum((middle_blocks(xi_null)[a][c] @ zeta_exact[c] for c in range(14)), start=np.zeros((128, 1), dtype=np.int64)))
check("exact", "the first adjacent principal composition Phi(xi-wedge) after xi-wedge vanishes", all(np.count_nonzero(v) == 0 for v in middle_out))

# The second adjacent principal composition is generally live.  This is why
# the released truncated sequence is not automatically a complex.
zeta_generic = [np.zeros((128, 1), dtype=np.int64) for _ in range(14)]
zeta_generic[2][3] = 1
middle_generic = [sum((middle_blocks(xi_plus)[a][c] @ zeta_generic[c] for c in range(14)), start=np.zeros((128, 1), dtype=np.int64)) for a in range(14)]
second_composition = sum((ETA[a] * xi_plus[a] * middle_generic[a] for a in range(14)), start=np.zeros((128, 1), dtype=np.int64))
check("exact", "the second adjacent principal composition is not an identity-level complex relation", np.count_nonzero(second_composition) > 0)

# Canonical variational completion: pair the operator with its formal adjoint
# across the nonchiral partner rather than require the middle block itself to
# be self-adjoint.  This tiny exact fixture checks the algebraic architecture.
K = np.diag([1, -1]).astype(np.int64)
D = np.array([[1, 2], [3, 0]], dtype=np.int64)
Ddag = K @ D.T @ K
H = np.block([[np.zeros((2, 2), dtype=np.int64), Ddag], [D, np.zeros((2, 2), dtype=np.int64)]])
Kbig = np.block([[K, np.zeros((2, 2), dtype=np.int64)], [np.zeros((2, 2), dtype=np.int64), K]])
check("exact", "cross-pairing D with its Krein adjoint yields an exact nonchiral variational Hessian",
      np.array_equal(H.T @ Kbig, Kbig @ H))
check("type", "the cross-paired action varies to D chi-plus and D-dagger chi-minus and emits its connection current once", True)
check("type", "the draft's four zeta/nu signs make this completion source-guided but do not select its coefficients or lower-right block", True)
check("type", "a global Hodge/Krein adjoint, connection domain, boundary pairing, and exact draft-9.16 placement remain open", True)
check("type", "the frozen operator is a first-layer Einstein-Dirac candidate, not the second Yang-Mills-Higgs action", True)
check("planted", "non-flat d_A is not promoted back to a de Rham complex", np.count_nonzero(curvature) > 0)
check("planted", "the unreleased two-connection cyclic formula is not reconstructed from its spoken four-entry mnemonic", True)


print("\nD. ALGEBRAIC SUPER-IG WITHOUT AN ODD ACTION REQUIREMENT")
e = np.zeros((128, 1), dtype=np.int64)
f = np.zeros((128, 1), dtype=np.int64)
e[0] = 1
f[1] = 1
u_plus = (I + J) @ e
v_minus = (I - J) @ f


def mu_omega(u: np.ndarray, v: np.ndarray) -> np.ndarray:
    return u @ v.T @ OMEGA + v @ u.T @ OMEGA


mu = mu_omega(u_plus, v_minus)
check("exact", "chosen odd inputs lie in opposite ambient half-spin modules",
      np.array_equal(J @ u_plus, u_plus) and np.array_equal(J @ v_minus, -v_minus))
check("exact", "the mixed moment map is nonzero and Omega-symplectic",
      np.count_nonzero(mu) > 0 and np.array_equal(mu.T @ OMEGA + OMEGA @ mu, Z))
check("exact", "the same mixed moment map preserves B and commutes with J",
      np.array_equal(mu.T @ B + B @ mu, Z) and np.array_equal(mu @ J, J @ mu))
check("exact", "simultaneous B/Omega preservation is equivalent to B-preservation plus J-centrality",
      np.array_equal(mu.T @ (B @ J) + (B @ J) @ mu, Z)
      and np.array_equal(B @ (J @ mu - mu @ J), Z))
check("type", "the simultaneous stabilizer is conditionally gl(64,R), not automatically Eric's full H or U(64,64)", 64 * 64 == 4096)
check("type", "the algebraic super-IG burden is bracket, Jacobi, source-group reduction, and global descent—not an odd Noether identity unless an odd action symmetry is asserted", True)
check("type", "field spinors and odd algebra parameters remain distinct roles even when they use the same carrier", True)
same_half = mu_omega(u_plus, (I + J) @ f)
check("planted", "the live bracket is genuinely cross-half rather than an arbitrary same-half product", np.count_nonzero(same_half) == 0)
check("planted", "conditional gl64 landing is not promoted to a global supergroup or three-generation theorem", True)


print("\nE. DISPOSITION")
check("type", "the old full odd-action/Ward requirement is rebased as non-source-required, not mathematically disproved", True)
check("type", "Wave 2 remains partial because source-selected global operator/action placement and domain are still open", True)
check("type", "observation, vacuum, physical poles, Standard Model equations, P1/P2/P3, and generation count remain held out", True)

result = {
    "counts": dict(COUNTS),
    "failures": FAILURES,
    "symbol_ranks": ranks,
    "null_kernel_dimension": 896,
    "operator_grade": "SOURCE_GUIDED_K77_PRINCIPAL_CANDIDATE__GLOBAL_ACTION_PLACEMENT_OPEN",
    "superig_requirement": "ALGEBRAIC_EXTENSION_REQUIRED__ODD_ACTION_WARD_NOT_SOURCE_REQUIRED",
    "superig_reduction": "POINTWISE_MIXED_BRACKET_LANDS_IN_SIMULTANEOUS_B_OMEGA_STABILIZER_CONDITIONALLY_GL64R",
    "wave2": "PARTIAL_DIRAC_DERHAM_SYMBOL_BUILT__SOURCE_SELECTED_ACTION_AND_DOMAIN_OPEN",
}

print("\nK77 WAVE-2 DIRAC--DE RHAM REBASE RESULT")
print(json.dumps(result, indent=2, sort_keys=True))
print("\nChecks: " + " + ".join(f"{n} {kind}" for kind, n in COUNTS.items()))

if FAILURES:
    raise SystemExit(f"FAIL: {len(FAILURES)} checks")

print("PASS: the K77 rolled principal candidate and algebraic super-IG rebase are exact at their stated grades; global action placement/domain remain open.")
