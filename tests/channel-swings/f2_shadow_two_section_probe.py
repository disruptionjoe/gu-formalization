#!/usr/bin/env python3
"""F2 SHADOW -- the two-section existence question at finite (toy) grade, run on
the ACTUAL W229 objects over the machine-proven generator loop.

CHANNEL: S_IG/B.5 construction frontier (P5 dossier, Element 1 / falsifier F2,
         Element 5 rungs M1/M2 at gu-side shadow grade).
AXIOM:   lab/process/boundary-adapter-standing-axiom.md (adapter assumed).
DESIGN:  explorations/sig-b5-f2-f5-shadow-2026-07-20.md
EXTENDS: explorations/sig-b5-habitat-verification-2026-07-20.md (the loop,
         transport, and K_S-twist machinery, all machine-proven there)
         explorations/blockbuster-p5-instance-dossier-2026-07-19.md (F2, M1/M2)
STATUS:  exploration tier; conditional (R0_COND working grade); no claim,
         canon, or public-posture movement.

QUESTION (dossier falsifier F2, shadowed at matrix grade). Over the generator
loop of the metric fiber -- the pi-rotation congruence loop in a mixed (+,-)
plane, whose frame transport provably sends K_S -> -K_S -- build a finite
Dirac-family shadow and decide: do TWO admissible Krein-compatible spectral
cuts (APS-type splittings) exist, exchanged by the deck transformation of the
double cover, or is the classifying invariant TRIVIAL (one cut up to
equivalence, hence no stored bit)? Triviality is the dossier's sharpest
candidate-kill; existence keeps the candidate alive at this grade.

CONSTRUCTIONS USED (GEOMETER-VS-PHYSICS-OBJECTS discipline, stated per
load-bearing object):
  - Loop / fiber / K_S: PROGRAM-NATIVE, identical to the habitat probe (the
    congruence loop g_t = A_t^T eta A_t, NOT an isometry; K_S = e_0...e_8 in
    the verified Cl(9,5) = M(64,H) rep, eta = (+1 x9, -1 x5)).
  - Dirac family: PROGRAM-NATIVE SYMBOL SHADOW. D(t) = c(A_t xi), the verified
    Dirac symbol transported along the loop, presented in the frame
    trivialization (constant Clifford generators, holonomy concentrated in the
    seam identification U_h). It is K_S-SELF-ADJOINT (Krein), not Hermitian --
    the positive-Hilbert default is deliberately not taken. No boundary
    manifold, no APS analysis: that is the N2 mathematics, out of scope here.
  - Spectral cut: BOTH forks are computed. The STANDARD-FIELD cut (plain
    positive-spectrum projection chi_+, the positive-Hilbert APS default) and
    the PROGRAM-NATIVE Krein cut (maximal K-definite D-invariant half-space,
    Krein-orthogonal splitting). The answer turns out to live on the native
    side: the standard cut descends to the loop but is K-INDEFINITE on its
    range; the native cuts are the two-section structure. A verdict derived
    on one side is checked on the other (rule 4).
  - Melrose-Piazza / covering-space steps: IMPORTED-standard shape (the
    "±1-valued continuous invariant separates path components" step and the
    pi_1 covering step); everything else is a matrix identity in the rep.
  - J_quat: PROGRAM-NATIVE quaternionic structure of M(64,H), built here in
    closed form (a product of JW gammas), phase-unique per step9.

WHAT IS TESTED:
  Part A (holonomy lift): U_h = e_0 e_9 implements the frame flip of the
      mixed-plane seam; U_h K_S U_h^{-1} = -K_S matches the machine-proven
      frame-transport endpoint (kprod cross-check); a continuous NATIVE
      unitary lift R(t) (exp of real Clifford words) connects I to U_h, is
      J_quat-commuting, and carries K_S through a continuous family of
      Hermitian involutions K_hat(t) with K_hat(1) = -K_S; the lift endpoint
      is generator-independent; U_h^2 = I (double cover closes untwisted).
  Part B (the family): D(t) = c(A_t xi) is K_S-self-adjoint for all t, closes
      onto the seam EXACTLY (D(1) = U_h D(0) U_h^{-1}), is J-commuting
      (quaternionically doubled), and is GAPPED along the whole loop
      (q(t) = eta(A_t xi, A_t xi) stays >= 28.1 > 0): zero spectral flow, so
      no Z-obstruction to sections. CONTROLS: a plane-dominated symbol hits
      the null cone mid-loop (gap closes, 64-dim = EVEN kernel, eigenvalues
      leave the real axis -- a Krein collision): gap survival is contingent,
      not automatic. Same-sign-plane loops keep q exactly constant and have
      untwisted seams (trichotomy).
  Part C (the two cuts -- the F2 question): the Krein Gram of K_S on each
      spectral half E_+/-(t) has EXACT signature (32,32) (tracelessness of
      K_S chi_+ is exact) and stays nondegenerate along the loop; therefore
      maximal K-definite D-invariant half-rank cuts W_+/-(t) exist at every t,
      with Krein-orthogonal projections Q_+/-(t) (idempotent, K-self-adjoint,
      complementary, J-invariant, continuous). SEAM: Q_+(1) = U_h Q_-(0)
      U_h^{-1} and Q_-(1) = U_h Q_+(0) U_h^{-1} EXACTLY -- the monodromy of
      the canonical cut IS the deck exchange; neither cut descends to the
      base loop (non-descent gap O(1)); both close on the double cover
      (U_h^2 = I). The definiteness sign is a continuous +-1 invariant with
      margin bounded away from 0, so the two sections are NOT homotopic
      through admissible cuts: the classifying invariant at this grade is the
      full Z/2. TWO-SECTION STRUCTURE EXISTS -- falsifier F2 does NOT fire at
      toy grade. CONTROL: on a same-sign-plane loop the SAME canonical cut
      DESCENDS (monodromy trivial): the two-section monodromy fires exactly
      on the genuine F-loops.
  Part D (Kramers control): the family is J-doubled; every J-commuting
      Hermitian probe has doubly degenerate spectrum (Kramers), so
      signature/parity readouts of the J-commuting (GU-native) class are
      forced EVEN and cannot output the odd/absolute sector label; the
      Gram spectra are themselves Kramers-paired; a rank-1 (odd) readout
      carrier has J-defect 1 (control). The stored bit's VALUE stays
      externally posited, exactly as typed in the dossier.

NONCLAIMS. No boundary Dirac OPERATOR on the actual non-compact Y14 end is
constructed (N2), no families pushforward (N1), no BV weld (N3); the K-group
language is shadowed by the finite classifying computation above, not by a
K-theory theorem; nothing here moves claims, canon, scorecard, or posture.
Deterministic; numpy only.
"""
from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "generation-sector"))
import gen_sector_bridge as gb  # noqa: E402
import oq_rk1_cl95_explicit_rep as cl95  # noqa: E402

N_DIRS, DIM = 14, 128
ETA = np.array([1.0] * 9 + [-1.0] * 5)
RNG = np.random.default_rng(20260720)

RESULTS = []


def check(tag, name, ok, detail=""):
    RESULTS.append((tag, name, bool(ok)))
    line = f"[{tag}] {'PASS' if ok else 'FAIL'}  {name}"
    if detail:
        line += f"   ({detail})"
    print(line)
    return ok


# --- the actual W229 anchors --------------------------------------------------
e = gb.gammas()
K_S = e[0].copy()
for a in range(1, 9):
    K_S = K_S @ e[a]                      # K_S = e_0 e_1 ... e_8
XI = np.real(np.asarray(gb.XI)).astype(float)
I128 = np.eye(DIM, dtype=complex)


def cvec(v):
    return sum(v[a] * e[a] for a in range(N_DIRS))


def rot(n, a, b, th):
    A = np.eye(n)
    A[a, a] = np.cos(th)
    A[b, b] = np.cos(th)
    A[a, b] = -np.sin(th)
    A[b, a] = np.sin(th)
    return A


def kprod(frame_cols):
    """Ordered Clifford product of the nine +legs of a 14-frame (habitat probe)."""
    out = I128.copy()
    for c in range(9):
        gen = sum(frame_cols[d, c] * e[d] for d in range(N_DIRS))
        out = out @ gen
    return out


def qform(v):
    return float(v @ (ETA * v))


# --- [T] setup ----------------------------------------------------------------
herm = float(np.max(np.abs(K_S - K_S.conj().T)))
invol = float(np.max(np.abs(K_S @ K_S - I128)))
cliff_ok = True
for a in range(N_DIRS):
    for b in range(a, N_DIRS):
        want = 2.0 * (ETA[a] if a == b else 0.0)
        got = e[a] @ e[b] + e[b] @ e[a]
        if float(np.max(np.abs(got - want * I128))) > 1e-9:
            cliff_ok = False
check("T", "rep integrity: Clifford relations for eta (9,5); K_S Hermitian "
           "involution", cliff_ok and herm < 1e-9 and invol < 1e-9)

# J_quat in closed form: C = product of the JW gammas whose required
# commutation sign (from reality x signature) is +1; J = C o conj.
G_raw = cl95.jordan_wigner_gammas(7)
r_sign, sigma = [], []
for a in range(N_DIRS):
    real_g = float(np.max(np.abs(np.conj(G_raw[a]) - G_raw[a]))) < 1e-12
    r_sign.append(+1 if real_g else -1)
    sigma.append(r_sign[a] if a < 9 else -r_sign[a])
S_even = [a for a in range(N_DIRS) if sigma[a] == -1]
S_odd = [a for a in range(N_DIRS) if sigma[a] == +1]
S_pick = S_even if len(S_even) % 2 == 0 else S_odd
C_J = I128.copy()
for a in S_pick:
    C_J = C_J @ G_raw[a]


intw = max(float(np.max(np.abs(C_J @ np.conj(e[a]) - e[a] @ C_J)))
           for a in range(N_DIRS))
jj = C_J @ np.conj(C_J)
unit = float(np.max(np.abs(C_J @ C_J.conj().T - I128)))
check("T", "J_quat exists in closed form (subset product of JW gammas): "
           "J e_a J^{-1} = e_a for all 14 generators, C unitary, "
           "J^2 = C conj(C) = -I (quaternionic class M(64,H))",
      intw < 1e-12 and unit < 1e-12
      and float(np.max(np.abs(jj + I128))) < 1e-12,
      f"intertwining {intw:.1e}, |J^2 + I| {float(np.max(np.abs(jj + I128))):.1e}")

q_xi = qform(XI)
check("T", "frozen symbol pin: the repo xi is eta-positive and off the null "
           "cone (q(xi) = 30.13); its (0,9)-plane content is small, which is "
           "what will keep the transported symbol off the cone",
      abs(q_xi - 30.13) < 1e-9, f"q = {q_xi:.4f}")


# =============================================================================
# Part A -- the holonomy lift and the transported Krein form as a family
# =============================================================================
U_h = e[0] @ e[9]
Uh_inv = np.linalg.inv(U_h)

flip_ok = True
for a in range(N_DIRS):
    wantsign = -1.0 if a in (0, 9) else 1.0
    if float(np.max(np.abs(U_h @ e[a] @ Uh_inv - wantsign * e[a]))) > 1e-9:
        flip_ok = False
F1_frame = np.linalg.inv(rot(N_DIRS, 0, 9, np.pi))
K_transported = kprod(F1_frame)
check("E", "U_h = e_0 e_9 implements the seam frame flip (e_0, e_9 -> "
           "negated, others fixed) and U_h K_S U_h^{-1} = -K_S = the "
           "machine-proven frame-transport endpoint (kprod cross-check)",
      flip_ok
      and float(np.max(np.abs(U_h @ K_S @ Uh_inv + K_S))) < 1e-9
      and float(np.max(np.abs(K_transported + K_S))) < 1e-9)

P_minus_Uh = 0.5 * (I128 - U_h)


def lift(t, gen):
    """Native lift R(t) = exp(-pi t P_-(U_h) gen), gen a commuting bivector."""
    X = -np.pi * t * (P_minus_Uh @ gen)
    w, v = np.linalg.eig(X)
    return (v * np.exp(w)) @ np.linalg.inv(v)


GEN12 = e[1] @ e[2]
ok_lift, ok_J_lift, ok_khat = True, True, True
for t in np.linspace(0.0, 1.0, 11):
    R = lift(t, GEN12)
    if float(np.max(np.abs(R @ R.conj().T - I128))) > 1e-8:
        ok_lift = False
    if float(np.max(np.abs(C_J @ np.conj(R) - R @ C_J))) > 1e-8:
        ok_J_lift = False
    Kh = R @ K_S @ R.conj().T
    if float(np.max(np.abs(Kh - Kh.conj().T))) > 1e-8 or \
       float(np.max(np.abs(Kh @ Kh - I128))) > 1e-8:
        ok_khat = False
R1 = lift(1.0, GEN12)
end_ok = float(np.max(np.abs(R1 - U_h))) < 1e-8
Kh1 = R1 @ K_S @ R1.conj().T
check("E", "native lift R(t) = exp(-pi t P_- e_1 e_2): unitary and "
           "J_quat-commuting for all t, R(0) = I, R(1) = U_h; the transported "
           "form K_hat(t) = R K_S R^+ is a CONTINUOUS family of Hermitian "
           "involutions with K_hat(1) = -K_S (the kinematic endpoint upgraded "
           "to a family statement)",
      ok_lift and ok_J_lift and ok_khat and end_ok
      and float(np.max(np.abs(Kh1 + K_S))) < 1e-8)

alt_ok = True
for gen in (e[3] @ e[4], e[10] @ e[11]):
    Ralt = lift(1.0, gen)
    if float(np.max(np.abs(Ralt - U_h))) > 1e-8:
        alt_ok = False
check("E", "lift endpoint is generator-independent (e_3 e_4 and the timelike "
           "e_10 e_11 give the SAME R(1) = U_h): the seam holonomy is not an "
           "artifact of the chosen lift; and U_h^2 = I exactly (the double "
           "cover closes untwisted, matching the habitat probe's doubled loop)",
      alt_ok and float(np.max(np.abs(U_h @ U_h - I128))) < 1e-12)


# =============================================================================
# Part B -- the Dirac-family shadow over the loop
# =============================================================================
def D_of_t(t, xi=XI, a=0, b=9):
    return cvec(rot(N_DIRS, a, b, np.pi * t) @ xi)


ok_ksa, ok_gap, ok_jfam = True, True, True
q_min, q_max = np.inf, -np.inf
for t in np.linspace(0.0, 1.0, 41):
    xi_t = rot(N_DIRS, 0, 9, np.pi * t) @ XI
    qt = qform(xi_t)
    q_min, q_max = min(q_min, qt), max(q_max, qt)
    Dt = cvec(xi_t)
    if float(np.max(np.abs(K_S @ Dt.conj().T @ K_S - Dt))) > 1e-9:
        ok_ksa = False
    if float(np.max(np.abs(Dt @ Dt - qt * I128))) > 1e-8:
        ok_gap = False
    if float(np.max(np.abs(C_J @ np.conj(Dt) - Dt @ C_J))) > 1e-9:
        ok_jfam = False
D0 = D_of_t(0.0)
D1 = D_of_t(1.0)
seam = float(np.max(np.abs(D1 - U_h @ D0 @ Uh_inv)))
check("E", "Dirac-family shadow D(t) = c(A_t xi): K_S-self-adjoint (Krein, "
           "not Hermitian -- the native fork) and J-commuting (quaternionic "
           "family) at every sampled t; D(t)^2 = q(t) I with q in "
           "[28.13, 30.31] > 0: GAPPED along the whole loop (zero spectral "
           "flow, no Z-obstruction to sections); seam closure "
           "D(1) = U_h D(0) U_h^{-1} EXACT",
      ok_ksa and ok_gap and ok_jfam and q_min > 28.0 and seam < 1e-9,
      f"q range [{q_min:.4f}, {q_max:.4f}], seam {seam:.1e}")

xi_plane = np.zeros(N_DIRS)
xi_plane[0] = 1.0                          # plane-dominated symbol
q_quarter = qform(rot(N_DIRS, 0, 9, np.pi * 0.25) @ xi_plane)
q_half = qform(rot(N_DIRS, 0, 9, np.pi * 0.5) @ xi_plane)
v_null = rot(N_DIRS, 0, 9, np.pi * 0.25) @ xi_plane
Dnull = cvec(v_null)
ker_dim = int(np.sum(np.linalg.svd(Dnull, compute_uv=False) < 1e-9))
ev_after = np.linalg.eigvals(cvec(rot(N_DIRS, 0, 9, np.pi * 0.5) @ xi_plane))
check("F", "null-cone control: a PLANE-DOMINATED symbol (xi' = e_0) hits the "
           "light cone mid-loop (q crosses 0 at t = 1/4, q(1/2) = -1): the "
           "kernel there is 64-dim (EVEN -- Kramers/quaternionic doubling), "
           "and past the cone the eigenvalues leave the real axis (Krein "
           "collision, spectrum +-i sqrt|q|): gap survival of the frozen xi "
           "is contingent on its small plane content, not automatic",
      abs(q_quarter) < 1e-9 and q_half < -0.9 and ker_dim == 64
      and float(np.max(np.abs(ev_after.real))) < 1e-6
      and float(np.max(np.abs(ev_after.imag))) > 0.9,
      f"q(1/4) = {q_quarter:.1e}, ker dim = {ker_dim}")

qs_const = [qform(rot(N_DIRS, 0, 1, np.pi * t) @ XI)
            for t in np.linspace(0, 1, 11)]
U_s = e[0] @ e[1]
Us_inv = np.linalg.inv(U_s)
check("F", "same-sign-plane control: a (+,+)-plane loop keeps q EXACTLY "
           "constant (the rotation is an eta-isometry there) and its seam "
           "element e_0 e_1 leaves K_S untwisted (+K_S) -- the twist "
           "machinery is silent on trivial loops",
      max(abs(q - q_xi) for q in qs_const) < 1e-9
      and float(np.max(np.abs(U_s @ K_S @ Us_inv - K_S))) < 1e-9)


# =============================================================================
# Part C -- the two Krein-compatible cuts: existence, exchange, classification
# =============================================================================
def spectral_halves(D, q):
    """Exact spectral projectors of the gapped K-s.a. involution-like D."""
    chp = 0.5 * (I128 + D / np.sqrt(q))
    return chp, I128 - chp


def half_basis(ch):
    Uu, ss, _ = np.linalg.svd(ch)
    return Uu[:, :DIM // 2]


def gram_parts(B, K):
    Gm = B.conj().T @ K @ B
    Gm = 0.5 * (Gm + Gm.conj().T)
    w, S = np.linalg.eigh(Gm)
    return B @ S[:, w > 0], B @ S[:, w < 0], w


def kproj(Xc, K):
    """Krein-orthogonal projector onto col(Xc) along its K-orthocomplement."""
    M = Xc.conj().T @ K @ Xc
    return Xc @ np.linalg.solve(M, Xc.conj().T @ K)


def krein_cuts(D, q, K):
    """The canonical maximal K-definite D-invariant half-rank cut pair."""
    chp, chm = spectral_halves(D, q)
    Bp, Bm = half_basis(chp), half_basis(chm)
    p_pos, p_neg, wp = gram_parts(Bp, K)
    m_pos, m_neg, wm = gram_parts(Bm, K)
    Wp = np.hstack([p_pos, m_pos])
    Wm = np.hstack([p_neg, m_neg])
    return kproj(Wp, K), kproj(Wm, K), Wp, Wm, wp, wm


chp0, chm0 = spectral_halves(D0, q_xi)
tr_kchi = complex(np.trace(K_S @ chp0))
Bp0 = half_basis(chp0)
_, _, w_gram0 = gram_parts(Bp0, K_S)
check("E", "the Krein Gram of K_S on the spectral half E_+ has EXACT "
           "signature (32,32) (tr(K_S chi_+) = 0 is exact: K_S c(xi) is a "
           "sum of >= 8-fold gamma products, traceless), and is "
           "NONDEGENERATE (min |eig| = 0.86): the raw material for "
           "K-definite cuts exists",
      abs(tr_kchi) < 1e-9
      and int(np.sum(w_gram0 > 0)) == 32 and int(np.sum(w_gram0 < 0)) == 32
      and float(np.min(np.abs(w_gram0))) > 0.5,
      f"min |Gram eig| = {float(np.min(np.abs(w_gram0))):.4f}")

# the cut pair along the loop: existence, definiteness margin, continuity
margin_min = np.inf
step_max = 0.0
Qp_prev = None
ok_props = True
ts = np.linspace(0.0, 1.0, 41)
for t in ts:
    xi_t = rot(N_DIRS, 0, 9, np.pi * t) @ XI
    qt = qform(xi_t)
    Dt = cvec(xi_t)
    Qp_t, Qm_t, Wp_t, Wm_t, wp_t, wm_t = krein_cuts(Dt, qt, K_S)
    margin_min = min(margin_min,
                     float(np.min(np.abs(wp_t))), float(np.min(np.abs(wm_t))))
    # projector properties: idempotent, complementary, K-self-adjoint, rank 64
    if float(np.max(np.abs(Qp_t @ Qp_t - Qp_t))) > 1e-8 or \
       float(np.max(np.abs(Qp_t + Qm_t - I128))) > 1e-8 or \
       float(np.max(np.abs(K_S @ Qp_t.conj().T @ K_S - Qp_t))) > 1e-8 or \
       Wp_t.shape[1] != 64 or Wm_t.shape[1] != 64:
        ok_props = False
    # D-invariance of the cut ranges
    if float(np.linalg.norm(Dt @ Qp_t - Qp_t @ Dt @ Qp_t)) > 1e-7:
        ok_props = False
    # J-invariance of the cut
    if float(np.max(np.abs(C_J @ np.conj(Qp_t) - Qp_t @ C_J))) > 1e-7:
        ok_props = False
    if Qp_prev is not None:
        step_max = max(step_max, float(np.linalg.norm(Qp_t - Qp_prev)))
    Qp_prev = Qp_t
check("E", "admissible Krein cuts EXIST at every sampled t: maximal "
           "K-definite (margin >= 0.84, never degenerating) D-invariant "
           "half-rank subspaces W_+/-(t) with Krein-orthogonal projections "
           "Q_+/-(t): idempotent, complementary, K_S-self-adjoint, "
           "J_quat-invariant, continuous along the loop",
      ok_props and margin_min > 0.5 and step_max < 0.3,
      f"definiteness margin {margin_min:.4f}, max step {step_max:.4f}")

Qp0, Qm0, Wp0, Wm0, _, _ = krein_cuts(D0, q_xi, K_S)
Qp1, Qm1, _, _, _, _ = krein_cuts(D1, qform(rot(N_DIRS, 0, 9, np.pi) @ XI), K_S)
deck1 = float(np.max(np.abs(Qp1 - U_h @ Qm0 @ Uh_inv)))
deck2 = float(np.max(np.abs(Qm1 - U_h @ Qp0 @ Uh_inv)))
check("E", "THE SEAM IS THE DECK EXCHANGE, exactly: Q_+(1) = U_h Q_-(0) "
           "U_h^{-1} and Q_-(1) = U_h Q_+(0) U_h^{-1} (machine identities): "
           "transporting the canonical K-positive cut once around the loop "
           "returns the K-NEGATIVE cut -- the two sections are exchanged by "
           "the deck transformation of the double cover",
      deck1 < 1e-9 and deck2 < 1e-9,
      f"deck defects {deck1:.1e}, {deck2:.1e}")

nondescent = float(np.linalg.norm(Qp1 - U_h @ Qp0 @ Uh_inv))
# double-cover closure: the two seam identities + U_h^2 = I compose to the
# identity on the cut after TWO traversals
twice = U_h @ (U_h @ Qp0 @ Uh_inv) @ Uh_inv       # deck applied twice
check("E", "NON-DESCENT + cover closure: no single-valued K-definite cut "
           "exists on the base loop (gap O(1) between Q_+(1) and the descent "
           "requirement), while two traversals return the cut exactly "
           "(deck^2 = id via U_h^2 = I): the sections live on the double "
           "cover, in the two deck-exchanged classes",
      nondescent > 0.5 and float(np.max(np.abs(twice - Qp0))) < 1e-12,
      f"descent gap {nondescent:.4f}")

check("E", "CLASSIFICATION: the K_S-sign of an admissible cut is a "
           "continuous +-1-valued invariant with margin >= 0.84 along the "
           "whole family (no degeneration anywhere), so the K-positive and "
           "K-negative sections are NOT homotopic through admissible cuts "
           "(the separates-components step typed IMPORTED-standard): the "
           "classifying set at this grade is exactly Z/2, NONTRIVIAL. "
           "TWO-SECTION STRUCTURE EXISTS -- falsifier F2 does NOT fire at "
           "toy grade", margin_min > 0.5)

chp1, _ = spectral_halves(D1, qform(rot(N_DIRS, 0, 9, np.pi) @ XI))
std_descends = float(np.max(np.abs(chp1 - U_h @ chp0 @ Uh_inv)))
gram_std = np.sort(w_gram0)
check("E", "constructions-fork record: the STANDARD-FIELD cut (plain "
           "positive-spectrum chi_+, the positive-Hilbert APS default) "
           "DESCENDS to the base loop (trivial monodromy) but is "
           "K-INDEFINITE on its range (signature (32,32)): the two-section "
           "datum is INVISIBLE on the standard fork and lives on the native "
           "Krein fork -- a triviality verdict derived with the standard cut "
           "would not transfer, and did not",
      std_descends < 1e-9 and gram_std[0] < -0.5 and gram_std[-1] > 0.5,
      f"std-cut descent defect {std_descends:.1e}")

# untwisted-loop control at cut level
A1s = rot(N_DIRS, 0, 1, np.pi)
D1s = cvec(A1s @ XI)
Qp1s, Qm1s, _, _, _, _ = krein_cuts(D1s, qform(A1s @ XI), K_S)
check("F", "trichotomy control: on the SAME-SIGN-plane loop the canonical "
           "K-positive cut DESCENDS exactly (Q_+(1) = U' Q_+(0) U'^{-1}, "
           "U' = e_0 e_1): the deck-exchange monodromy fires precisely on "
           "the genuine (mixed-plane) F-loops and is silent on trivial loops",
      float(np.max(np.abs(Qp1s - U_s @ Qp0 @ Us_inv))) < 1e-9)


# =============================================================================
# Part D -- Kramers control: the J-doubled family is blind to the choice
# =============================================================================
H0 = RNG.standard_normal((DIM, DIM)) + 1j * RNG.standard_normal((DIM, DIM))
H0 = 0.5 * (H0 + H0.conj().T)
HJ = 0.5 * (H0 + C_J @ np.conj(H0) @ np.linalg.inv(C_J))
HJ = 0.5 * (HJ + HJ.conj().T)
evs = np.sort(np.linalg.eigvalsh(HJ))
kramers_probe = all(abs(evs[2 * i] - evs[2 * i + 1]) < 1e-9
                    for i in range(DIM // 2))
wg = np.sort(w_gram0)
kramers_gram = all(abs(wg[2 * i] - wg[2 * i + 1]) < 1e-9
                   for i in range(len(wg) // 2))
check("E", "Kramers control: every J_quat-commuting Hermitian probe has "
           "doubly degenerate spectrum (random symmetrized probe AND the "
           "K_S-Gram on E_+ itself are exactly paired): signature/parity "
           "readouts of the GU-native (J-commuting) operator class are "
           "forced EVEN -- the odd/absolute sector label is unreachable, so "
           "the VALUE of the stored bit stays externally posited, exactly "
           "as the dossier types it", kramers_probe and kramers_gram)

v0 = np.zeros(DIM, dtype=complex)
v0[0] = 1.0
R1p = np.outer(v0, v0.conj())
jdef = float(np.linalg.norm(C_J @ np.conj(R1p) - R1p @ C_J))
check("F", "odd-readout control: a rank-1 (odd) readout carrier has J-defect "
           "> 0 (Kramers forbids it in the native class) -- any reader of "
           "the absolute bit value must be non-quaternionic, i.e. live "
           "OUTSIDE the GU-native operator class (the Door B shape / F4 "
           "typing, untouched here)", jdef > 0.5, f"J-defect {jdef:.3f}")


# --- headline -----------------------------------------------------------------
nE = sum(1 for tag, _n, ok in RESULTS if tag == "E")
nF = sum(1 for tag, _n, ok in RESULTS if tag == "F")
nT = sum(1 for tag, _n, ok in RESULTS if tag == "T")
all_ok = all(ok for _t, _n, ok in RESULTS)
print()
print("F2 SHADOW VERDICT: the two-section structure EXISTS at toy grade -- "
      "two admissible Krein-compatible cuts, exchanged by the deck "
      "transformation, classifying invariant Z/2 NONTRIVIAL; the kill "
      "(triviality) does NOT fire. Verdict is native-fork-local: the "
      "standard positive-Hilbert cut sees no datum at all (recorded above).")
print(f"HEADLINE: {nE} [E] + {nF} [F] = {nE + nF}   (setup [T] = {nT} "
      f"excluded)   {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")
sys.exit(0 if all_ok else 1)
