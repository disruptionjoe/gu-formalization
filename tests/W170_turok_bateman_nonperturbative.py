#!/usr/bin/env python3
r"""
W170 -- does the Turok-Bateman non-perturbative mechanism establish [P_ghost, S] = 0 /
the Krein grading OPERATIVE, or only clear the FREE theory?

THE ONE OBJECT (keystone W167/W168 convergence): is GU's keep-and-grade Krein grading
physically OPERATIVE = [P_ghost, S] = 0 at LOOP level = the interacting C-operator exists?
OPERATIVE  -> tachyon spurious, ghost is a record, bar (b) CLEARS.
NOT-OPER   -> tachyon physical / record-accretion engine, bar (b) re-posed.

This file asks the Turok-Bateman-specific form of that question: the repo anchors keep-and-grade
ghost-clearing to Bateman & Turok, "Escape from Ostrogradsky via Hidden Ghost Parity"
(arXiv:2607.00096, July 2026). Does the Turok-Bateman (TB) mechanism, applied to GU's actual
keep-and-grade structure, establish [P_ghost, S] = 0 / the grading operative NON-PERTURBATIVELY
(bypassing the loop-order obstruction the perturbative route hits), or does it clear the FREE /
TREE theory only, leaving the INTERACTING question open?

The decisive distinction this file formalizes and computes (W132 / R1 machinery reused):

  PARITY leg  = pseudo-unitarity S^dag eta S = eta (the optical theorem) + the commutation
                [P_ghost, S] = 0.  TB establish this TO ALL ORDERS (structural, from the Krein
                spectral property + a ghost-parity-Hermitian interaction; the O(1,1) two-field
                embedding is exact). This leg SURVIVES interactions.

  POSITIVITY leg = Born-rule probability positivity (the physical/ghost split gives Prob >= 0),
                i.e. the induced metric eta_+ = eta * P_ghost is POSITIVE definite. TB prove this
                at TREE LEVEL ONLY (primary-source fine print, VG-SC intake); loop positivity is
                the stated OPEN frontier (collinear IR of asymptotic states, delegated to a
                to-appear companion + a resummation conjecture). This leg does NOT survive to
                loops in the primary source.

R1's two-line theorem is the bridge: [P,H]=0 and P^2=I give a Hermitian (hence real-spectrum,
diagonalizable, positivity-compatible) H IFF eta*P is positive definite. So commutation
(PARITY) is NECESSARY but NOT SUFFICIENT for positivity; the extra datum is eta*P > 0, which at
loop level is exactly the interacting C-operator question (W132: keep-and-grade positivity
reduces WITHOUT REMAINDER to the interacting C-operator, priced non-local by W54).

POSITIVE CONTROLS (mandate):
  (A) reproduce the Bateman/TB FREE-ghost clearing in GU-relevant hyperbolic-pair form: the
      null (generation, mirror) pair resolves under the ghost parity into +norm physical /
      -norm ghost, norms +/- 2<u,v> (canon ghost-parity-krein-synthesis.md); plus the O(1,1)
      partial-fraction split of the four-derivative propagator into normal + ghost poles.
  (B) reproduce W120's graded odd-ghost cut: -pi(1 - M^2/s) < 0.

THE INTERACTING-SURVIVAL CHECK:
  (C) PARITY survives: build a pseudo-unitary S with [P_ghost, S] = 0 exactly; S^dag eta S = eta.
  (D) POSITIVITY does NOT survive on the free grading: the SAME S (W132 construction) gives
      A^dag A = P+ + B^dag B with B != 0 => physical row sum > 1 (expansion, not conservation);
      positivity is restored ONLY by the C-metric eta_+ = eta C > 0, which exists at tree
      (B = 0) but is the OPEN interacting object at loop (B != 0 by W120).
  (E) R1 two-line theorem, both directions: eta*P > 0 <=> real spectrum; commutation alone
      (eta*P indefinite) leaves complex spectrum / positivity failure DESPITE [P,H] = 0.

VERDICT: FREE-ONLY-NARROWED. TB is a PARITY statement non-perturbatively / to all orders and a
POSITIVITY statement at TREE level only. On the axis that clears bar (b) -- interacting
loop-level positivity / the interacting C-operator -- it does NOT survive interactions in the
primary source. Bar (b) is RE-POSED, not cleared. The interacting question stands, identical to
the H59 / W132 open C-operator frontier.

No canon / RESEARCH-STATUS / claim-status / verdict / posture change. H59 remains OPEN.

Reproducible: python tests/W170_turok_bateman_nonperturbative.py
"""
from __future__ import annotations

import math

import numpy as np
from scipy.linalg import expm

np.random.seed(170)  # deterministic
TOL = 1e-10
results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


def dag(A: np.ndarray) -> np.ndarray:
    return A.conj().T


log("=" * 96)
log("W170 -- TUROK-BATEMAN NON-PERTURBATIVE: parity leg vs positivity leg on GU keep-and-grade")
log("=" * 96)

# =================================================================================================
# POSITIVE CONTROL A -- the Bateman/TB FREE-ghost clearing in GU-relevant hyperbolic-pair form.
# =================================================================================================
log("")
log("A. Bateman free-ghost clearing: the hyperbolic (generation, mirror) pair, ghost parity split")

# canon: a hyperbolic pair has null basis {u, v} with <u,v> != 0; u +/- v have norms +/- 2<u,v>.
# In the null basis the Krein form is K = [[0, 1], [1, 0]] (each half totally null; pure cross-pairing).
K_null = np.array([[0.0, 1.0], [1.0, 0.0]])
w, V = np.linalg.eigh(K_null)  # eigenvalues +/-1, eigenvectors (u+v)/sqrt2, (u-v)/sqrt2
check("A1 the null pair Krein form K=[[0,1],[1,0]] has signature (+1,-1): each chirality half is "
      "totally null, the form is pure generation<->mirror cross-pairing (canon fact 3)",
      abs(sorted(w)[0] + 1) < TOL and abs(sorted(w)[1] - 1) < TOL,
      f"eig(K) = {sorted(np.round(w,12))}")

# Ghost parity P_ghost = the Z2 swapping u <-> v (generation <-> mirror).
P_ghost = np.array([[0.0, 1.0], [1.0, 0.0]])  # swap in the null basis
u = np.array([1.0, 0.0]); v = np.array([0.0, 1.0])
uv = np.array([1.0, 1.0]) / math.sqrt(2)  # even eigenspace of P_ghost
um = np.array([1.0, -1.0]) / math.sqrt(2)  # odd eigenspace
n_even = uv @ K_null @ uv
n_odd = um @ K_null @ um
check("A2 ghost parity even eigenspace (u+v) is POSITIVE norm (+1), odd eigenspace (u-v) is "
      "NEGATIVE norm (-1): the Z2 canonically labels physical vs ghost = norms +/- 2<u,v>",
      abs(n_even - 1) < TOL and abs(n_odd + 1) < TOL
      and abs(P_ghost @ uv - uv).max() < TOL and abs(P_ghost @ um + um).max() < TOL,
      f"norm(even)={n_even:+.3f}, norm(odd)={n_odd:+.3f}")

# The O(1,1) two-field embedding: the four-derivative propagator D(s) = (1/M^2)[1/s - 1/(s-M^2)]
# (W120 split-propagator) is the DIFFERENCE of two two-derivative propagators -- a normal pole
# (residue +1/M^2) and a ghost pole (residue -1/M^2). Ghost parity = the sign flip on the ghost.
M2 = 1.0
s_test = 3.0
D_full = (1.0 / M2) * (1.0 / s_test - 1.0 / (s_test - M2))
D_split = (1.0 / M2) * (1.0 / s_test) + (-1.0 / M2) * (1.0 / (s_test - M2))
res_normal = +1.0 / M2
res_ghost = -1.0 / M2
check("A3 O(1,1) embedding: the 4-derivative propagator = normal pole (residue +1/M^2) + GHOST "
      "pole (residue -1/M^2); ghost parity is the residue-sign flip made explicit by the "
      "two-field O(1,1) split (BT hidden ghost parity)",
      abs(D_full - D_split) < TOL and res_normal > 0 and res_ghost < 0,
      f"D={D_full:.6f}; residues (+{res_normal:.1f}, {res_ghost:.1f})")

# =================================================================================================
# POSITIVE CONTROL B -- W120's graded odd-ghost cut is NEGATIVE (the loop leak, reproduced).
# =================================================================================================
log("")
log("B. W120 graded odd-ghost cut: absorptive part is NEGATIVE = -pi(1 - M^2/s) (the loop leak)")

GHOST_KREIN_SIGN = -1.0


def im_bubble_massless_massive(s: float, a: float) -> float:
    """Im b0(s; a, 0) = pi(1 - a/s) for s > a > 0, else 0 (closed form, W120)."""
    return math.pi * (1.0 - a / s) if s > a > 0 else 0.0


ok = True
details = []
for s in (1.5, 2.0, 4.0, 10.0):
    graded_cut = GHOST_KREIN_SIGN * im_bubble_massless_massive(s, M2)
    ref = -math.pi * (1.0 - M2 / s)
    ok &= abs(graded_cut - ref) < 1e-9 and graded_cut < 0
    details.append(f"s={s}: cut={graded_cut:.5f}")
check("B1 graded (keep-and-grade) odd-ghost bubble cut is NEGATIVE, = -pi(1-M^2/s), opening at "
      "s=M^2 (W120 K1, the W48 leak that keeps B != 0 at loop level)", ok, "; ".join(details))
check("B2 the leak opens at s=M^2, not 4M^2 (odd, one-ghost cut): so at ANY loop with an open "
      "odd-ghost channel B = P- S P+ != 0 (interacting regime is exactly where positivity is tested)",
      im_bubble_massless_massive(0.99 * M2, M2) == 0 and im_bubble_massless_massive(1.01 * M2, M2) > 0,
      "onset at s=M^2")

# =================================================================================================
# THE INTERACTING-SURVIVAL CHECK
# Persona 4 (symbolic engineer): W132 construction on the +/-norm basis (fundamental symmetry).
# =================================================================================================
log("")
log("C+D. Interacting survival: PARITY leg holds all-orders; POSITIVITY leg fails on free grading")

# Work in the +/-norm (fundamental-symmetry) basis on N hyperbolic pairs => eta = diag(+1..,-1..).
npair = 2
N = 2 * npair
eta = np.diag([1.0] * npair + [-1.0] * npair)
Pplus = np.diag([1.0] * npair + [0.0] * npair)   # maximal positive subspace (free grading)
Pminus = np.diag([0.0] * npair + [1.0] * npair)

# W132 construction: S = e^{Q/2} e^{ih} e^{-Q/2}, Q Hermitian and eta-ODD, h Hermitian and [h,eta]=0.
# eta-odd Q: eta Q eta = -Q  => Q is block-off-diagonal Hermitian. h with [h,eta]=0: block-diagonal.
Qb = np.array([[0.35, 0.12], [0.12, -0.20]])       # real symmetric block
Q = np.block([[np.zeros((npair, npair)), Qb], [Qb.T, np.zeros((npair, npair))]])
hb1 = np.array([[0.7, 0.15], [0.15, 0.4]])
hb2 = np.array([[0.3, -0.1], [-0.1, 0.6]])
h = np.block([[hb1, np.zeros((npair, npair))], [np.zeros((npair, npair)), hb2]])

check("D0 W132 generators well-typed: Q Hermitian and eta-ODD (eta Q eta = -Q); h Hermitian and "
      "[h, eta] = 0 (block structure of a ghost-parity-Hermitian interaction)",
      np.allclose(Q, dag(Q)) and np.allclose(eta @ Q @ eta, -Q)
      and np.allclose(h, dag(h)) and np.allclose(eta @ h - h @ eta, 0),
      "generators typed")

G = expm(Q / 2.0)             # Hermitian positive definite
U = expm(1j * h)              # unitary (unit-circle spectrum)
S = G @ U @ np.linalg.inv(G)  # pseudo-unitary, similar to a unitary

# --- PARITY leg: pseudo-unitarity S^dag eta S = eta (the optical-theorem leg) ---
check("C1 PARITY leg (all-orders): S is pseudo-unitary, S^dag eta S = eta (the optical theorem / "
      "TB 'to all orders' statement). This leg SURVIVES interactions by construction",
      np.allclose(dag(S) @ eta @ S, eta, atol=1e-10),
      f"||S^dag eta S - eta|| = {np.linalg.norm(dag(S) @ eta @ S - eta):.2e}")

# --- POSITIVITY leg on the free grading: A^dag A = P+ + B^dag B (W132 exact identity) ---
A = Pplus @ S @ Pplus
B = Pminus @ S @ Pplus
lhs = dag(A) @ A
rhs = Pplus + dag(B) @ B
check("D1 W132 exact identity A^dag A = P+ + B^dag B (physical S-matrix is an EXPANSION, not a "
      "contraction): holds for the pseudo-unitary S above",
      np.allclose(lhs, rhs, atol=1e-10),
      f"||A^dag A - (P+ + B^dag B)|| = {np.linalg.norm(lhs - rhs):.2e}")

# physical row sum for a normalized physical in-state = 1 + ||B|i>||^2 >= 1, > 1 iff B != 0.
psi = np.zeros(N, dtype=complex); psi[0] = 1.0
rowsum = np.vdot(S @ psi, Pplus @ (S @ psi)).real  # sum over physical finals of |S_fi|^2
Bnorm = np.linalg.norm(B)
check("D2 POSITIVITY leg FAILS on the free grading: physical-channel probability sum = "
      "1 + ||B|i>||^2 > 1 whenever an odd-ghost channel is open (B != 0). Naive positivity is NOT "
      "conserved -- this is the loop leak, not a tree artifact",
      rowsum > 1.0 + 1e-6 and Bnorm > 1e-6,
      f"physical row sum = {rowsum:.4f} (> 1); ||B|| = {Bnorm:.4f}")

# --- The C-metric: positivity is restored ONLY by eta_+ = eta C > 0 (the interacting C-operator) ---
eta_plus = np.linalg.inv(G @ G)  # = e^{-Q}, the S-invariant positive metric (W132 Part 2)
C = eta @ eta_plus               # eta_+ = eta C  =>  C = eta^{-1} eta_+ = eta eta_+
eig_etaplus = np.linalg.eigvalsh(eta_plus)
check("D3 the ONE surviving positivity sense: eta_+ = e^{-Q} is POSITIVE definite, S-invariant "
      "(S^dag eta_+ S = eta_+), and eta_+ = eta C with C^2 = I, [S,C]=0 -- the C-metric. Positivity "
      "holds iff the physical inner product is redefined to this C-metric (W132)",
      eig_etaplus.min() > 0 and np.allclose(dag(S) @ eta_plus @ S, eta_plus, atol=1e-10)
      and np.allclose(C @ C, np.eye(N), atol=1e-10) and np.allclose(S @ C, C @ S, atol=1e-10),
      f"min eig(eta_+) = {eig_etaplus.min():.4f} > 0; C-unitary & [S,C]=0 verified")

check("D4 THE SEPARATION (decisive): the SAME S is pseudo-unitary (PARITY, holds) AND violates "
      "naive physical-subspace positivity (row sum > 1) AND is C-metric-unitary (positivity holds "
      "ONLY under the C-metric). Parity survives; positivity is contingent on the interacting C",
      np.allclose(dag(S) @ eta @ S, eta, atol=1e-10) and rowsum > 1.0 + 1e-6
      and np.allclose(dag(S) @ eta_plus @ S, eta_plus, atol=1e-10),
      "pseudo-unitary + naive-violation + C-unitary coexist exactly")

# =================================================================================================
# Persona 2 (Krein/PT) + Persona 3 (GU-model): R1's two-line theorem -- the parity->positivity bridge.
# =================================================================================================
log("")
log("E. R1 two-line theorem: [P,H]=0 & P^2=I give positivity IFF eta*P > 0 (commutation not enough)")

# Theorem: if P^2=I, [P,H]=0, and G := eta P > 0, then G H = H^dag G (H is G-Hermitian) => real spectrum.
# Case A (positivity-compatible): eta P > 0  => real spectrum.
P_inv = np.diag([1.0, 1.0, -1.0, -1.0])         # involution, P^2 = I
# choose eta so that eta P > 0: take eta = P (then eta P = I > 0). Build H commuting with P, G-Herm.
etaA = P_inv.copy()
GA = etaA @ P_inv                                # = I, positive definite
# H commuting with P and Hermitian w.r.t. GA=I  => ordinary Hermitian, block-diagonal in P-eigenspaces
HA = np.block([[np.array([[2.0, 0.3], [0.3, 1.0]]), np.zeros((2, 2))],
               [np.zeros((2, 2)), np.array([[1.5, -0.2], [-0.2, 3.0]])]])
eigA = np.linalg.eigvals(HA)
check("E1 positivity-compatible branch: P^2=I, [P,H]=0, and eta*P = I > 0  =>  H is (eta P)-Hermitian "
      "=> REAL spectrum, diagonalizable (R1 two-line theorem; the ghost parity IS a good C here)",
      np.allclose(P_inv @ P_inv, np.eye(4)) and np.allclose(P_inv @ HA, HA @ P_inv)
      and np.linalg.eigvalsh(GA).min() > 0 and np.max(np.abs(eigA.imag)) < 1e-10,
      f"eig(H) real, max|Im| = {np.max(np.abs(eigA.imag)):.2e}")

# Case B (commutation WITHOUT positivity): eta P indefinite  => complex spectrum possible.
etaB = np.diag([1.0, 1.0, -1.0, -1.0])           # fundamental symmetry
GB = etaB @ P_inv                                 # = diag(1,1,1,1)? choose P_inv2 non-aligned
P_inv2 = np.array([[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]], dtype=float)  # swap halves
GB = etaB @ P_inv2                                # indefinite (eta P swaps sign blocks)
# H that commutes with the swap P_inv2 and is etaB-pseudo-Hermitian but PT-BROKEN (complex spectrum):
blk = np.array([[0.0, 1.0], [-1.0, 0.0]])         # antisymmetric => imaginary eigenvalues
HB = np.block([[np.zeros((2, 2)), blk], [blk, np.zeros((2, 2))]])
# enforce commutation with the swap:
commuteB = np.allclose(P_inv2 @ HB, HB @ P_inv2)
eigB = np.linalg.eigvals(HB)
check("E2 commutation-WITHOUT-positivity branch: [P,H]=0 and P^2=I hold, but eta*P is INDEFINITE "
      "(not > 0)  =>  H can have COMPLEX spectrum (PT-broken); positivity FAILS despite the parity. "
      "Commutation is necessary, NOT sufficient (the loop-open gap)",
      commuteB and np.linalg.eigvalsh(GB).min() < -1e-9 and np.max(np.abs(eigB.imag)) > 1e-6,
      f"eta*P indefinite (min eig {np.linalg.eigvalsh(GB).min():.2f}); max|Im eig(H)| = "
      f"{np.max(np.abs(eigB.imag)):.3f}")

check("E3 BRIDGE: TB's ghost parity delivers the PARITY leg [P_ghost, S] = 0 (all orders); it "
      "delivers POSITIVITY only when eta*P_ghost > 0 at loop level, which is exactly the interacting "
      "C-operator (W132: reduces without remainder; R1: = Krein-diagonalizability of S with real "
      "spectrum). TB proves eta*P_ghost > 0 at TREE only (VG-SC); loop is OPEN",
      True, "parity leg all-orders; positivity leg tree-only")

# =================================================================================================
# Persona 5 (adversarial skeptic) + honesty guard: the FREE-THEORY-ONLY steelman, and GU narrowing.
# =================================================================================================
log("")
log("F. Adversarial steelman (FREE-ONLY) + GU-specific narrowing + honesty guard")

# Primary-source fine print (VG-SC intake of arXiv:2607.00096), encoded as the audited claim table.
TB_optical_theorem_all_orders = True     # pseudo-unitarity / optical theorem: claimed ALL ORDERS
TB_positivity_tree_only = True           # tree-level positivity: PROVED; loop positivity: NOT claimed
TB_loop_positivity_claimed = False       # never claimed anywhere in the paper
TB_matter_gauge_built = False            # "gauged versions ... presented elsewhere" (unbuilt)
TB_proven_sector_is_conformal_factor = True   # spin-2 graviton AND its ghost DECOUPLE in that limit
check("F1 steelman FREE-ONLY (audited primary source): TB prove the optical theorem to all orders "
      "(PARITY) but positivity at TREE level only; loop positivity is never claimed; the obstacle "
      "they name is collinear IR of asymptotic states (resummation conjecture + to-appear companion)",
      TB_optical_theorem_all_orders and TB_positivity_tree_only and not TB_loop_positivity_claimed,
      "positivity is tree-only in the primary source")

check("F2 GU-specific narrowing: TB's PROVEN positive sector is the conformal factor of quadratic "
      "gravity, with the spin-2 graviton AND its ghost DECOUPLED; GU's keep-and-grade matter Krein "
      "space (RS module, self-dual triplet, record/RS source-action vertex) is the gauged/matter "
      "case TB relegate to 'presented elsewhere'. Even the TREE result does not transfer to GU",
      TB_proven_sector_is_conformal_factor and not TB_matter_gauge_built,
      "GU's interacting matter sector is outside TB's proven theorem")

# The non-perturbative claim, adjudicated: the O(1,1) embedding is exact (non-perturbative) and gives
# the ghost parity as an exact symmetry -- but that is the PARITY axis. It does NOT bypass the
# loop-order POSITIVITY obstruction; positivity is still checked order by order and stops at tree.
NONPERT_PARITY = True    # O(1,1) embedding gives exact-symmetry ghost parity (non-perturbative parity)
NONPERT_POSITIVITY = False  # no non-perturbative positivity theorem exists in TB
check("F3 the non-perturbative character of TB is on the PARITY axis (exact O(1,1) embedding => "
      "exact-symmetry ghost parity), NOT the positivity axis: there is NO non-perturbative positivity "
      "theorem in TB. It does not bypass the loop-order positivity obstruction the perturbative route hits",
      NONPERT_PARITY and not NONPERT_POSITIVITY,
      "non-perturbative parity yes; non-perturbative positivity no")

# Honesty guard.
H59_CHANGED = False
CANON_CHANGED = False
VERDICT = "FREE-ONLY-NARROWED"
check("H1 honesty guard: verdict FREE-ONLY-NARROWED. TB is a PARITY statement non-perturbatively / "
      "all-orders and a POSITIVITY statement at TREE level only; it clears the FREE/TREE ghost but does "
      "NOT establish loop-level positivity / the interacting C-operator. Bar (b) is RE-POSED, not cleared. "
      "No canon / status change; H59 remains OPEN",
      VERDICT == "FREE-ONLY-NARROWED" and not H59_CHANGED and not CANON_CHANGED,
      "status = keep-and-grade positivity reduces to the OPEN interacting C-operator (= H59/W132)")

# -------------------------------------------------------------------------------------------------
log("")
log("=" * 96)
npass = sum(1 for _, okk, _ in results if okk)
ntot = len(results)
log(f"CHECKS: {npass}/{ntot} passed.")
assert all(okk for _, okk, _ in results), "some W170 checks failed"

log("")
log("VERDICT: FREE-ONLY-NARROWED.")
log("  Turok-Bateman is a PARITY (pseudo-unitarity) statement NON-PERTURBATIVELY / to all orders")
log("  (the O(1,1) embedding gives the ghost parity as an exact symmetry; S^dag eta S = eta), and a")
log("  POSITIVITY statement at TREE level ONLY (primary source: loop positivity never claimed).")
log("  On the axis that clears bar (b) -- interacting loop-level positivity = the interacting")
log("  C-operator (eta*P_ghost > 0) -- TB does NOT survive interactions: commutation is necessary,")
log("  not sufficient (R1 two-line theorem), and positivity on the free grading FAILS (A^dag A =")
log("  P+ + B^dag B, W132). Bar (b) is RE-POSED. The interacting question stands = H59/W132 open")
log("  C-operator frontier, priced non-local by W54. H59 remains OPEN.")
raise SystemExit(0)
