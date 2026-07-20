#!/usr/bin/env python3
"""F5 SHADOW -- does the C2 accounting respond to the holonomy-sector flip?
An end-model on the ACTUAL W229 objects, with the real C2 anchors.

CHANNEL: S_IG/B.5 construction frontier (P5 dossier, Element 6 falsifier F5,
         Element 5 rung M2 at gu-side shadow grade).
AXIOM:   lab/process/boundary-adapter-standing-axiom.md (adapter assumed).
DESIGN:  explorations/sig-b5-f2-f5-shadow-2026-07-20.md
EXTENDS: tests/channel-swings/f2_shadow_two_section_probe.py (the sector cuts)
         tests/channel-swings/sig_b5_habitat_probe.py (loop/twist machinery)
         explorations/blockbuster-p5-instance-dossier-2026-07-19.md (F5)
STATUS:  exploration tier; conditional (R0_COND working grade); no claim,
         canon, or public-posture movement.

QUESTION (dossier falsifier F5, shadowed at symbol/matrix grade). Build an
end-model in which the C2 analog -- the real obstruction norm, anchors
bare = 58.7215 and C2 = 155.3625 -- can be computed under BOTH holonomy
dressings (the two sectors of the loop), and test: does the C2 accounting
respond to the sector flip, or is it invariant? Per the dossier, invariance
in a faithful end-model fires F5 (carrier coherent but irrelevant); a genuine
holonomy-tied difference means the carrier is load-bearing.

THE END-MODEL. The sector datum is the choice of Krein-compatible cut Q_+/-
of the boundary Dirac-family shadow (the F2 probe's canonical pair; the two
dressings are literally "boundary condition as given" vs "boundary condition
transported once around the loop", since the deck identity
Q_-(0) = U_h^{-1} Q_+(1) U_h is machine-exact). The C2 accounting under a
dressing is the obstruction map X = Gamma M_D Pi_RS resolved by the sector
projector on its output (end/spinor) leg:
    magnitude readout  r_sigma  = ||Q_sigma X||_F
    Krein-signed readout k_sigma = Re tr(X^+ K_S Q_sigma X).
This is the dossier's weld shape (Element 4(4): the spectral section is the
asymptotic boundary condition the C-operator/BV data must match); no other
channel is available at symbol grade.

RESULT (established below, machine-exact, then controlled):
  (1) The MAGNITUDE accounting is EXACTLY invariant, r_+ = r_- (and the full
      singular-value spectra of Q_+X and Q_-X coincide) -- but this is
      THEOREM-FORCED, not evidence: the obstruction density A = X X^+
      satisfies the exact scalar identity
          A + K_S A K_S = (C2^2/64) I,
      which makes ||Q X|| = ||(I-Q) X|| for EVERY Krein-orthogonal half-rank
      splitting Q whatsoever (sector-canonical or random). A magnitude
      invariance that holds for every splitting carries ZERO discriminating
      power about THIS carrier: the F5 magnitude test is structurally
      incapable of firing at symbol grade. (It is also the invariance the
      standing regression SRC-REJ-1 DEMANDS: symbol-level data must not move
      C2.)
  (2) The SIGNED accounting RESPONDS exactly: k_sigma = sigma * 14421.0033
      (|k|/C2^2 = 0.5975, a large fraction of the obstruction content), with
      k_+ + k_- = 0 exact (corollary tr(K_S A) = 0). Flipping the sector =
      transporting the boundary condition around the mixed loop flips the
      signed accounting; the SAME operation around a same-sign-plane loop
      changes NOTHING (the transported cut returns identical) -- the response
      is holonomy-tied, with the trichotomy control demanded.
  VERDICT: F5 does NOT fire, and is NOT discharged: the sector datum is
  load-bearing in the one channel open at this grade (Krein-signed,
  relational), while the magnitude channel is parity-closed by theorem. The
  honest F5 test remains an N2-grade computation, exactly where the dossier
  filed it; what this shadow adds is that any faithful end-model must consume
  the sector through the signed/Krein channel, never as a magnitude dressing.

CONSTRUCTIONS USED (GEOMETER-VS-PHYSICS-OBJECTS discipline): C2 is the
PROGRAM-NATIVE obstruction norm (NOT an index -- killed list honored;
degree-1 homogeneous). The sector cut is the native Krein cut of the F2
probe (the standard positive-Hilbert cut carries no sector datum -- recorded
there). The dressing pair is a genuine holonomy pair (deck identity), not a
frame choice; frame artifacts are excluded by the covariant-dressing control.

NONCLAIMS. No claim that the sector datum reduces or closes C2 (it provably
cannot at symbol grade -- that is SRC-REJ-1 compliance, verified as a guard);
no anyon/TEE language; no N2 mathematics; no claim/canon/posture movement.
Deterministic; numpy only.
"""
from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "generation-sector"))
import gen_sector_bridge as gb  # noqa: E402

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
    K_S = K_S @ e[a]
XI = np.real(np.asarray(gb.XI)).astype(float)
I128 = np.eye(DIM, dtype=complex)
U_h = e[0] @ e[9]
Uh_inv = np.linalg.inv(U_h)


def cvec(v):
    return sum(v[a] * e[a] for a in range(N_DIRS))


def rot(n, a, b, th):
    A = np.eye(n)
    A[a, a] = np.cos(th)
    A[b, b] = np.cos(th)
    A[a, b] = -np.sin(th)
    A[b, a] = np.sin(th)
    return A


def qform(v):
    return float(v @ (ETA * v))


def half_basis(ch):
    Uu, _s, _v = np.linalg.svd(ch)
    return Uu[:, :DIM // 2]


def gram_parts(B, K):
    Gm = B.conj().T @ K @ B
    Gm = 0.5 * (Gm + Gm.conj().T)
    w, S = np.linalg.eigh(Gm)
    return B @ S[:, w > 0], B @ S[:, w < 0], w


def kproj(Xc, K):
    M = Xc.conj().T @ K @ Xc
    return Xc @ np.linalg.solve(M, Xc.conj().T @ K)


def krein_cuts(D, q, K):
    chp = 0.5 * (I128 + D / np.sqrt(q))
    chm = I128 - chp
    Bp, Bm = half_basis(chp), half_basis(chm)
    p_pos, p_neg, _ = gram_parts(Bp, K)
    m_pos, m_neg, _ = gram_parts(Bm, K)
    return (kproj(np.hstack([p_pos, m_pos]), K),
            kproj(np.hstack([p_neg, m_neg]), K))


# --- [T] setup ----------------------------------------------------------------
e_, Gamma, Pi_RS, M_D = gb.constraint_objects()
X = Gamma @ M_D @ Pi_RS
A = X @ X.conj().T
C2 = float(np.linalg.norm(X))
bare = float(np.linalg.norm(Pi_RS @ M_D - M_D @ Pi_RS))
check("T", "the REAL C2 anchors reproduce: bare ||[Pi_RS, M_D]|| = 58.7215, "
           "C2 = ||Gamma M_D Pi_RS|| = 155.3625 (the verified Cl(9,5) "
           "machinery, not a mini-rep)",
      abs(bare - 58.7215) < 1e-2 and abs(C2 - 155.3625) < 1e-2,
      f"bare {bare:.4f}, C2 {C2:.4f}")

D0 = cvec(XI)
q0 = qform(XI)
Qp, Qm = krein_cuts(D0, q0, K_S)
props = (float(np.max(np.abs(Qp @ Qp - Qp))) < 1e-8
         and float(np.max(np.abs(Qp + Qm - I128))) < 1e-8
         and float(np.max(np.abs(K_S @ Qp.conj().T @ K_S - Qp))) < 1e-8)
check("T", "the sector cuts rebuild (F2 probe's canonical Krein pair): "
           "idempotent, complementary, K_S-self-adjoint", props)

D1 = cvec(rot(N_DIRS, 0, 9, np.pi) @ XI)
Qp1, Qm1 = krein_cuts(D1, qform(rot(N_DIRS, 0, 9, np.pi) @ XI), K_S)
deck = float(np.max(np.abs(Qp1 - U_h @ Qm @ Uh_inv)))
check("T", "the two dressings ARE the holonomy pair: the deck identity "
           "Q_+(1) = U_h Q_-(0) U_h^{-1} is machine-exact, so 'flip the "
           "sector' = 'transport the boundary condition once around the "
           "mixed loop' (F2 probe, re-verified here)", deck < 1e-9,
      f"deck defect {deck:.1e}")


# =============================================================================
# Part A -- the master identity and its corollaries (the blindness theorem)
# =============================================================================
Srem = A + K_S @ A @ K_S - (np.trace(A).real / 64.0) * I128
master = float(np.linalg.norm(Srem))
check("E", "MASTER IDENTITY (machine-exact, mechanism underived): the "
           "obstruction density A = X X^+ satisfies A + K_S A K_S = "
           "(C2^2/64) I -- the K_S-even part of the C2 density is pure "
           "scalar. Consequence: ||Q X|| = ||(I-Q) X|| for EVERY "
           "Krein-orthogonal half-rank splitting Q",
      master < 1e-9 * float(np.linalg.norm(A)),
      f"residual {master:.2e} vs ||A+KAK|| = "
      f"{float(np.linalg.norm(A + K_S @ A @ K_S)):.1f}")

trKA = complex(np.trace(K_S @ A))
check("E", "corollary: tr(K_S A) = 0 exactly -- the total Krein-signed "
           "obstruction content vanishes, so ANY complementary Krein "
           "splitting resolves it into equal-and-opposite halves",
      abs(trKA) < 1e-8, f"|tr(K A)| = {abs(trKA):.2e}")


# =============================================================================
# Part B -- the two readouts under the two dressings
# =============================================================================
r_p = float(np.linalg.norm(Qp @ X))
r_m = float(np.linalg.norm(Qm @ X))
sv_p = np.linalg.svd(Qp @ X, compute_uv=False)
sv_m = np.linalg.svd(Qm @ X, compute_uv=False)
check("E", "MAGNITUDE accounting: r_+ = r_- to machine precision "
           "(129.2640 each) and the FULL singular-value spectra of the two "
           "dressed obstruction maps coincide -- no magnitude or spectral "
           "readout of the dressed C2 distinguishes the sectors",
      abs(r_p - r_m) < 1e-9 * C2
      and float(np.max(np.abs(sv_p - sv_m))) < 1e-9,
      f"r_+ = {r_p:.4f}, r_- = {r_m:.4f}, sv diff "
      f"{float(np.max(np.abs(sv_p - sv_m))):.1e}")

# the invariance is splitting-generic (theorem, not evidence about the sector)
Z = RNG.standard_normal((DIM, 64)) + 1j * RNG.standard_normal((DIM, 64))
Qz = kproj(Z, K_S)
chp0 = 0.5 * (I128 + D0 / np.sqrt(q0))
r_z, r_zc = float(np.linalg.norm(Qz @ X)), float(np.linalg.norm((I128 - Qz) @ X))
r_c, r_cc = float(np.linalg.norm(chp0 @ X)), float(np.linalg.norm((I128 - chp0) @ X))
check("E", "the magnitude invariance is SPLITTING-GENERIC (a seeded RANDOM "
           "K-orthogonal half-splitting and the plain spectral cut are "
           "equally blind): it follows from the master identity for every "
           "Krein-orthogonal Q, so it carries NO discriminating power about "
           "the sector carrier -- the F5 magnitude test is structurally "
           "incapable of firing at symbol grade",
      abs(r_z - r_zc) < 1e-8 * C2 and abs(r_c - r_cc) < 1e-8 * C2,
      f"random split {r_z:.4f} vs {r_zc:.4f}; plain cut {r_c:.4f} vs {r_cc:.4f}")

k_p = float(np.trace(X.conj().T @ K_S @ Qp @ X).real)
k_m = float(np.trace(X.conj().T @ K_S @ Qm @ X).real)
check("E", "SIGNED (Krein) accounting RESPONDS: k_sigma = sigma * 14421.0 "
           "(|k|/C2^2 = 0.60 -- a large resolved fraction of the obstruction "
           "content), k_+ + k_- = 0 exact: the sector flip reverses the "
           "signed C2 accounting exactly. The carrier is NOT inert in the "
           "C2 accounting; its footprint is relational (sign), not absolute "
           "(magnitude)",
      k_p > 1e3 and abs(k_p + k_m) < 1e-6 * abs(k_p)
      and abs(k_p / C2 ** 2 - 0.5975) < 1e-2,
      f"k_+ = {k_p:.4f}, k_- = {k_m:.4f}, |k|/C2^2 = {k_p / C2 ** 2:.4f}")

check("E", "the response is HOLONOMY-TIED: by the deck identity ([T]3), "
           "flipping k's sign is achieved by the geometric operation "
           "'transport the boundary condition around the mixed loop' "
           "(k evaluated with the transported cut U_h^{-1} Q_+(1) U_h "
           "equals k_-)",
      abs(float(np.trace(X.conj().T @ K_S @ (Uh_inv @ Qp1 @ U_h) @ X).real)
          - k_m) < 1e-6 * abs(k_m))


# =============================================================================
# Part C -- controls: trichotomy, frame artifacts, SRC-REJ-1 guard
# =============================================================================
A1s = rot(N_DIRS, 0, 1, np.pi)
D1s = cvec(A1s @ XI)
Qp1s, _ = krein_cuts(D1s, qform(A1s @ XI), K_S)
U_s = e[0] @ e[1]
Q_transported_trivial = np.linalg.inv(U_s) @ Qp1s @ U_s
r_triv = float(np.linalg.norm(Q_transported_trivial @ X))
k_triv = float(np.trace(X.conj().T @ K_S @ Q_transported_trivial @ X).real)
check("F", "trichotomy control: transporting the boundary condition around a "
           "SAME-SIGN-plane loop returns the IDENTICAL cut (descent, F2 "
           "probe) and produces NO difference in either readout (r and k "
           "unchanged to machine precision) -- the signed response is a "
           "genuine mixed-loop holonomy effect, not a transport artifact",
      float(np.max(np.abs(Q_transported_trivial - Qp))) < 1e-9
      and abs(r_triv - r_p) < 1e-9 * C2 and abs(k_triv - k_p) < 1e-6 * abs(k_p),
      f"r {r_triv:.4f} vs {r_p:.4f}; k {k_triv:.4f} vs {k_p:.4f}")

# covariant (frame) dressing: conjugate ALL data by the holonomy -- a pure
# frame operation; every readout must be exactly unchanged
h_vec = rot(N_DIRS, 0, 9, np.pi)                  # the vector-index flip
big = np.kron(h_vec, U_h)
X_cov = U_h @ X @ big.conj().T
Qp_cov = U_h @ Qp @ Uh_inv
K_cov = U_h @ K_S @ Uh_inv                        # = -K_S (the twist)
r_cov = float(np.linalg.norm(Qp_cov @ X_cov))
k_cov = float(np.trace(X_cov.conj().T @ K_cov @ Qp_cov @ X_cov).real)
k_incoh = float(np.trace(X.conj().T @ (-K_S) @ Qp @ X).real)
check("F", "frame-artifact control: dressing EVERYTHING covariantly (spinor "
           "leg, vector leg, cut, AND the form, which returns as -K_S) is "
           "the IDENTITY on both readouts (r_cov = r_+, k_cov = k_+): a "
           "frame operation changes nothing. Only SELECTIVE flips move k: "
           "cut alone -> k_- (the sector flip), form alone -> -k_+ (the "
           "SRC-COH-1 incoherence, = k_- here because the pair co-flips): "
           "the sector operation is selective, never a frame relabel",
      abs(r_cov - r_p) < 1e-9 * C2 and abs(k_cov - k_p) < 1e-6 * abs(k_p)
      and abs(k_incoh - k_m) < 1e-6 * abs(k_m),
      f"r_cov {r_cov:.4f}; k_cov {k_cov:.4f} = k_+; selective flips give "
      f"{k_m:.1f}")

check("F", "SRC-REJ-1 guard: neither dressing reduces or closes the total C2 "
           "at symbol level (r_sigma = 129.26 in (0, C2); ||X|| = 155.3625 "
           "untouched): the sector datum refuses to do C2's job with "
           "symbol-level data, exactly as the standing regression demands "
           "of a genuine global datum",
      100.0 < r_p < C2 and abs(float(np.linalg.norm(X)) - C2) < 1e-9,
      f"r_sigma = {r_p:.4f}, C2 = {C2:.4f}")


# --- headline -----------------------------------------------------------------
nE = sum(1 for tag, _n, ok in RESULTS if tag == "E")
nF = sum(1 for tag, _n, ok in RESULTS if tag == "F")
nT = sum(1 for tag, _n, ok in RESULTS if tag == "T")
all_ok = all(ok for _t, _n, ok in RESULTS)
print()
print("F5 SHADOW VERDICT: NOT FIRED, NOT DISCHARGED. The magnitude "
      "accounting is exactly invariant -- but theorem-forced for EVERY "
      "Krein splitting (master identity), hence evidentially null for F5; "
      "the signed accounting responds exactly (sigma * 14421, zero-sum, "
      "holonomy-tied, trichotomy-controlled): the carrier is load-bearing "
      "in the one channel open at symbol grade. The decisive F5 test "
      "remains N2-grade, as the dossier filed it.")
print(f"HEADLINE: {nE} [E] + {nF} [F] = {nE + nF}   (setup [T] = {nT} "
      f"excluded)   {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")
sys.exit(0 if all_ok else 1)
