#!/usr/bin/env python3
r"""
W132 / H69 -- the graded optical theorem on the physical subspace (the W48 gate question).

Question: the Krein-graded optical theorem weights odd-ghost cuts negatively (W48/W120/W124, the
"leak"). Does that violate PHYSICAL-subspace unitarity, i.e. probability conservation for in/out
states in the positive-norm sector?

Three parts, each with positive and negative controls:

  Part 1 (EXACT, finite-dimensional Krein algebra):
    For any eta-pseudo-unitary S (S^dag eta S = eta, eta = P+ - P-), the physical-subspace
    S-matrix A = P+ S P+ satisfies the EXACT identity
        A^dag A = P+  +  B^dag B,        B = P- S P+.
    So S restricted to the positive subspace is an EXPANSION: physical-channel probabilities from
    a physical in-state sum to 1 + sum_odd |S_fi|^2 >= 1, with equality iff the ghost sector
    decouples (B = 0). Verified to machine precision on random pseudo-unitary S.

  Part 2 (EXACT, the C-metric escape):
    A constructed S that is eta-pseudo-unitary with B != 0 (naive physical-subspace probability
    excess) yet EXACTLY unitary w.r.t. the positive metric eta_+ = e^{-Q} = eta C (C^2 = 1):
    the PRESERVED-IN-C-METRIC sense demonstrated concretely, coexisting with the naive violation.

  Part 3 (TOY-CHECKED, the W120/W124 QFT toy):
    chi chi -> chi chi through the dressed fourth-order (split) propagator
    D(s) = (1/M^2)[1/s - 1/(s - M^2)], massless matter, graviton-sector bubble cuts with
    weights (1/2, -1, 1/2) on (gg, g+ghost, ghost+ghost) forced by the split (Krein signs times
    identical-particle factors). Elastic partial-wave bound |S_J|^2 = |1 + 2ia|^2 <= 1 computed
    explicitly at several s: SATISFIED for M^2 < s < 2M^2, VIOLATED for all s > 2M^2 with the
    maximal deficit -1/4 (units of rho_00) at the two-ghost threshold s = 4M^2 and the -M^4/s^2
    tail. The ghost-free-sector (multichannel) deficit is negative for ALL s > M^2 and tends to
    -1/2: the row-level violation is not confined to any window. Controls: the normal-sign
    theory saturates the standard optical theorem and satisfies the bound everywhere; the
    Lee-Wick/removal prescription (ghost cuts zero, per W120/W124) preserves the bound;
    flipping the ghost residue removes the violation (it genuinely tracks the Krein sign).

Convention: all Part-3 statements are sign/ratio statements in a fixed positive normalization
(units M = 1; partial wave a = T/(32 pi); Im b_ab = rho_ab/(16 pi), rho_ab = sqrt(lambda(s,a,b))/s;
bubble symmetry factor 1/2 for identical loop fields). The elastic-cut identity Im a_el = |a_tree|^2
is verified in-test (PC0) so the normalization is internally consistent, not assumed.

Reproducible: python tests/W132_graded_optical_theorem_physical_subspace.py   (exit 0 iff all pass)
No canon / RESEARCH-STATUS / claim-status / verdict file touched. Exploration-grade. H59 stays OPEN
here; status changes go through the runbook only.
"""
from __future__ import annotations

import math
import sys

import numpy as np
from scipy.linalg import expm

TOL = 1e-11
results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


# ----------------------------------------------------------------------------------------------
# Part 1 -- exact Krein algebra: A^dag A = P+ + B^dag B
# ----------------------------------------------------------------------------------------------
print("\n== Part 1: exact physical-subspace identity for pseudo-unitary S ==")
rng = np.random.default_rng(20260714)
n, npos = 6, 4
eta = np.diag([1.0] * npos + [-1.0] * (n - npos))
Pp = np.diag([1.0] * npos + [0.0] * (n - npos))

# Random eta-pseudo-Hermitian generator H (eta H eta = H^dag), S = exp(iH) is eta-pseudo-unitary.
G = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
H = 0.5 * (G + eta @ G.conj().T @ eta)
S = expm(1j * H)

check("S1 pseudo-unitarity S^dag eta S = eta", np.max(np.abs(S.conj().T @ eta @ S - eta)) < TOL,
      f"max dev {np.max(np.abs(S.conj().T @ eta @ S - eta)):.2e}")

A = Pp @ S @ Pp
B = (np.eye(n) - Pp) @ S @ Pp
lhs = A.conj().T @ A
rhs = Pp + B.conj().T @ B
check("S2 exact identity A^dag A = P+ + B^dag B", np.max(np.abs(lhs - rhs)) < TOL,
      f"max dev {np.max(np.abs(lhs - rhs)):.2e}")

row_phys = np.array([np.sum(np.abs(S[:npos, i]) ** 2) for i in range(npos)])
row_odd = np.array([np.sum(np.abs(S[npos:, i]) ** 2) for i in range(npos)])
check("S3 physical row sums = 1 + odd-channel sum (> 1, B != 0)",
      np.allclose(row_phys, 1.0 + row_odd, atol=1e-10) and np.all(row_phys > 1.0 + 1e-6),
      f"row_phys - 1 = {np.array2string(row_phys - 1.0, precision=3)}")

# Control: block-diagonal (ghost-decoupled) S -> equality, probability conserved on the subspace.
h_bd = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
h_bd = 0.5 * (h_bd + h_bd.conj().T)
h_bd[:npos, npos:] = 0.0
h_bd[npos:, :npos] = 0.0
S_bd = expm(1j * h_bd)
row_bd = np.array([np.sum(np.abs(S_bd[:npos, i]) ** 2) for i in range(npos)])
check("S4 control: decoupled sector (B = 0) -> physical rows sum to exactly 1",
      np.allclose(row_bd, 1.0, atol=1e-10), f"max |row-1| {np.max(np.abs(row_bd-1)):.2e}")

# ----------------------------------------------------------------------------------------------
# Part 2 -- the C-metric escape: same S, naive violation + exact eta_+ unitarity
# ----------------------------------------------------------------------------------------------
print("\n== Part 2: C-metric (PT/Krein) escape demonstrated exactly ==")
# Q Hermitian and eta-odd (eta Q eta = -Q): block off-diagonal.
q = rng.normal(size=(npos, n - npos))
Q = np.zeros((n, n))
Q[:npos, npos:] = q
Q[npos:, :npos] = q.T
C = expm(Q) @ eta
eta_plus = eta @ C  # = e^{-Q}, positive
check("C1 C^2 = 1 and eta_+ = eta C = e^{-Q} positive-definite",
      np.max(np.abs(C @ C - np.eye(n))) < TOL and np.min(np.linalg.eigvalsh(0.5*(eta_plus+eta_plus.T))) > 0,
      f"|C^2-1| {np.max(np.abs(C @ C - np.eye(n))):.2e}, min eig eta_+ {np.min(np.linalg.eigvalsh(0.5*(eta_plus+eta_plus.T))):.3f}")

# S_C = e^{Q/2} e^{ih} e^{-Q/2} with h Hermitian, [h, eta] = 0: pseudo-unitary w.r.t. BOTH eta
# and eta_+ (i.e. [S_C, C] = 0), with B != 0 (ghost channels open).
hb = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
hb = 0.5 * (hb + hb.conj().T)
hb[:npos, npos:] = 0.0
hb[npos:, :npos] = 0.0
Eh = expm(Q / 2)
S_C = Eh @ expm(1j * hb) @ np.linalg.inv(Eh)

dev_eta = np.max(np.abs(S_C.conj().T @ eta @ S_C - eta))
dev_plus = np.max(np.abs(S_C.conj().T @ eta_plus @ S_C - eta_plus))
B_C = (np.eye(n) - Pp) @ S_C @ Pp
rowC = np.array([np.sum(np.abs(S_C[:npos, i]) ** 2) for i in range(npos)])
check("C2 S_C is eta-pseudo-unitary with open ghost channels (B != 0)",
      dev_eta < 1e-9 and np.max(np.abs(B_C)) > 1e-3,
      f"pseudo-unit dev {dev_eta:.2e}, max|B| {np.max(np.abs(B_C)):.3f}")
check("C3 naive physical-subspace violation: some physical row sum > 1",
      np.max(rowC) > 1.0 + 1e-6, f"max physical row sum {np.max(rowC):.6f}")
check("C4 SAME S_C exactly unitary in the C-metric: S^dag eta_+ S = eta_+",
      dev_plus < 1e-9, f"dev {dev_plus:.2e}")

# ----------------------------------------------------------------------------------------------
# Part 3 -- the QFT toy: partial-wave bound at several s
# ----------------------------------------------------------------------------------------------
print("\n== Part 3: partial-wave unitarity bound in the W120/W124 toy ==")
M2 = 1.0  # ghost mass^2, units M = 1


def rho(s: float, a: float, b: float) -> float:
    lam = (s - (math.sqrt(a) + math.sqrt(b)) ** 2) * (s - (math.sqrt(a) - math.sqrt(b)) ** 2)
    return math.sqrt(lam) / s if s > (math.sqrt(a) + math.sqrt(b)) ** 2 else 0.0


def F_graded(s: float) -> float:
    """Graviton-sector signed cut sum (elastic-bound deficit shape), weights (1/2, -1, 1/2)."""
    return 0.5 * rho(s, 0, 0) - rho(s, 0, M2) + 0.5 * rho(s, M2, M2)


def F_normal(s: float) -> float:
    return 0.5 * rho(s, 0, 0) + rho(s, 0, M2) + 0.5 * rho(s, M2, M2)


def F_removal(s: float) -> float:
    """Lee-Wick/removal: every ghost-containing cut is zero (W120 L2, W124 Stage A/B)."""
    return 0.5 * rho(s, 0, 0)


def G_ghostfree(s: float) -> float:
    """Deficit against the ghost-free physical sector (all matched physical cuts removed)."""
    return -rho(s, 0, M2) + 0.5 * rho(s, M2, M2)


def D(s: float) -> float:
    return -1.0 / (s * (s - M2))


# PC0: normalization consistency -- elastic chi chi cut equals |a_tree|^2 exactly.
g = 1.0
s0 = 3.0
a_tree = g * g * D(s0) / (32 * math.pi)
im_a_elastic_cut = (g ** 4) * D(s0) ** 2 * rho(s0, 0, 0) / (32 * math.pi) ** 2  # (g^2/2) bubble, Im b = rho/16pi
check("PC0 elastic-cut identity Im a_el = |a_tree|^2 (normalization two-route)",
      abs(im_a_elastic_cut - a_tree ** 2) < 1e-15, f"dev {abs(im_a_elastic_cut - a_tree**2):.2e}")

# P1: positive control -- normal-sign theory satisfies the bound at all sampled s.
S_SAMPLES = [1.5, 2.5, 3.0, 4.0, 5.0, 8.0, 20.0]
check("P1 positive control: normal theory F_normal(s) > 0 at all sampled s (bound satisfied)",
      all(F_normal(s) > 0 for s in S_SAMPLES),
      "standard optical theorem: all cuts positive, |S_J| <= 1")

# P2: graded deficit shape F(s) against closed forms; sign flip at exactly s* = 2 M^2.
expected = {1.5: 1/6, 2.5: -0.1, 3.0: -1/6, 4.0: -0.25,
            5.0: 0.5 - 0.8 + 0.5 * math.sqrt(0.2), 8.0: 0.5 - 0.875 + 0.5 * math.sqrt(0.5),
            20.0: 0.5 - 0.95 + 0.5 * math.sqrt(0.8)}
ok = all(abs(F_graded(s) - v) < 1e-12 for s, v in expected.items())
check("P2a graded deficit F(s) matches closed forms at 7 sampled s", ok,
      "F: " + ", ".join(f"s={s}: {F_graded(s):+.4f}" for s in S_SAMPLES))
check("P2b sign structure: F > 0 on (M^2, 2M^2), F = 0 at s = 2M^2, F < 0 for all s > 2M^2",
      F_graded(1.5) > 0 and abs(F_graded(2.0)) < 1e-14 and all(F_graded(s) < 0 for s in [2.01, 2.5, 3, 4, 6, 10, 50, 500]),
      f"crossover s* = 2 M^2 exactly; F(2.0) = {F_graded(2.0):.1e}")
check("P2c maximal elastic violation at the two-ghost threshold s = 4M^2, F = -1/4",
      abs(F_graded(4.0) + 0.25) < 1e-14 and all(F_graded(s) > F_graded(4.0) for s in [3.0, 3.5, 3.9, 4.1, 4.5, 5.0]),
      f"F(4) = {F_graded(4.0):+.4f}")

# P3: |S_J|^2 explicitly. |S_J|^2 - 1 = -4 (Im a - |a_tree|^2) = -4 * Im a_grav,
# Im a_grav = g^2 lam^2 D^2 F(s) / (512 pi^2)   (bubble 1/2 folded into F's weights).
lam = 5.0
gg = 5.0
print("      s/M^2    F(s)        |S_J|^2 - 1 (g=lam=5)")
sj = {}
for s in S_SAMPLES:
    im_a_grav = (gg ** 2) * (lam ** 2) * D(s) ** 2 * F_graded(s) / (512 * math.pi ** 2)
    sj[s] = -4 * im_a_grav
    print(f"      {s:5.1f}   {F_graded(s):+8.5f}    {sj[s]:+.3e}")
check("P3 elastic partial-wave bound |S_J| <= 1: HOLDS at s=1.5M^2, VIOLATED at every s > 2M^2",
      sj[1.5] < 0 and all(sj[s] > 0 for s in [2.5, 3.0, 4.0, 5.0, 8.0, 20.0]),
      f"|S_J|^2-1 at s=4M^2: {sj[4.0]:+.3e} > 0")

# P4: ghost-free-sector (multichannel) deficit: negative for ALL s > M^2, tends to -1/2.
check("P4 ghost-free-sector deficit G(s) < 0 for all s > M^2; G -> -1/2 as s -> inf",
      all(G_ghostfree(s) < 0 for s in [1.1, 1.5, 2.0, 3.0, 4.0, 8.0, 100.0]) and abs(G_ghostfree(1e8) + 0.5) < 1e-7,
      "G: " + ", ".join(f"s={s}: {G_ghostfree(s):+.3f}" for s in [1.5, 4.0, 8.0, 100.0]))

# P5: asymptotic tail of the elastic deficit: F(s) -> -M^4/s^2 (fit the power).
s_hi = [200.0, 400.0, 800.0, 1600.0]
logs = [math.log(-F_graded(s)) for s in s_hi]
slope = (logs[-1] - logs[0]) / (math.log(s_hi[-1]) - math.log(s_hi[0]))
check("P5 tail exponent: F ~ -M^4/s^2 (fitted slope ~ -2, coefficient ~ 1)",
      abs(slope + 2.0) < 0.02 and abs(-F_graded(1600.0) * 1600.0 ** 2 - 1.0) < 0.02,
      f"slope {slope:.4f}, coeff {-F_graded(1600.0)*1600.0**2:.4f}")

# P6: removal control (Lee-Wick, W120/W124: ghost cuts identically zero): bound preserved.
check("P6 removal control: F_removal(s) = +1/2 > 0 everywhere (Cutkosky et al. structure)",
      all(abs(F_removal(s) - 0.5) < 1e-15 for s in S_SAMPLES),
      "physical-subspace unitarity preserved by REMOVAL, not by grading")

# N1: flip the ghost residue to +1 -> weights (1/2, +1, 1/2) -> no violation anywhere.
check("N1 negative control: residue-flipped theory has positive deficit at all sampled s",
      all(F_normal(s) > 0 for s in S_SAMPLES + [2.01, 4.0, 100.0]),
      "the violation genuinely tracks the Krein sign of the odd cut")

# ----------------------------------------------------------------------------------------------
n_pass = sum(1 for _, p, _ in results if p)
print(f"\nW132: {n_pass}/{len(results)} checks passed.")
if n_pass != len(results):
    sys.exit(1)
print("VERDICT (this test's scope): physical-subspace unitarity on the free positive subspace is")
print("VIOLATED (exact expansion identity; elastic bound fails for all s > 2M^2, row level for all")
print("s > M^2); it is PRESERVED only in the C-metric (full-Krein, positive non-local inner")
print("product) sense, demonstrated exactly in Part 2. H59 remains OPEN; no status change here.")
sys.exit(0)
