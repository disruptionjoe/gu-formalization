#!/usr/bin/env python3
"""ARAKI CUT ENTROPY PROBE -- the honest finite-dimensional (type-I) Araki-form
retry of the cut relative-entropy route, on the ACTUAL two-section pair.

CHANNEL: S_IG/B.5 scale slot (entropy-route retry after the Umegaki negative
         of commit b895d95, explorations/f2-cut-relative-entropy-2026-07-20.md).
AXIOM:   lab/process/boundary-adapter-standing-axiom.md (adapter assumed; the
         SECTOR reading of the cuts stays R0_COND exactly as in F2/F5).
DESIGN:  explorations/araki-scale-route-2026-07-20.md (kill conditions K-a..K-d
         pre-declared there before this probe was run).
EXTENDS: tests/channel-swings/f2_shadow_two_section_probe.py (cut machinery),
         tests/channel-swings/f2_cut_relative_entropy_probe.py (the Umegaki
         negative being retried), explorations/f5-signed-fraction-2026-07-20.md
         (canonical cut S = K_S e^{alpha w}; closed form of A; w involution).
STATUS:  exploration tier; no claim, canon, or public-posture movement.

THE FINITE TYPE-I ARAKI DEFINITION USED (stated precisely, then machine-checked
against an independent modular-operator implementation at small dimension):
  For positive trace-one rho, sigma on a finite-dimensional Hilbert space H
  with M = B(H) (a type-I factor), the GNS space is the Hilbert-Schmidt space,
  xi_rho = rho^{1/2}, and the relative modular operator is
      Delta_{sigma|rho} X = sigma X rho^{-1}   (on the support subspace).
  Araki's relative entropy is
      S(rho||sigma) = - <xi_rho, ln(Delta_{sigma|rho}) xi_rho>
                    =   Tr rho (ln rho - ln sigma)   if supp rho <= supp sigma,
                    =   +infinity                     otherwise.
  At type I the Araki functional IS Umegaki-with-the-support-condition. The
  modular formulation cures TYPE (III) / UV pathologies -- finiteness for
  states in the same folium (e.g. coherent displacements of the vacuum,
  arXiv:2510.24491 Eq. 8 and footnote 2) -- it does NOT repair a genuine
  support violation, and it assigns +infinity to distinct pure/rank-deficient
  states.  The honest retry therefore has two jobs: (i) treat supports
  correctly (violating mass = Tr[rho (1 - supp sigma)]), and (ii) supply the
  NATIVE faithful (full-rank) states the naive run lacked -- the K_S-twisted
  cut states K_S Q_sigma and the derived positive dressing e^{alpha w}
  (= K_S S, positivity DERIVED in the F5 signed-fraction doc, not assumed).

WHAT THE PROBE ESTABLISHES (headline: the route is dead at toy grade, K-b,
with the mechanism NAMED):
  Part 1  the definition: modular = Umegaki+support at type I; support law;
          pure-state +infinity law (the b895d95 disease was purity/support,
          which Araki does not cure).
  Part 2  the pair: naive Hilbertized cut states AND K_S-twisted cut states
          have mutually violating supports -> Araki +infinity BOTH directions
          (K-a for the direct pairings).
  Part 3  the finite retry: against the native faithful reference
          gamma = e^{alpha w}/Z, both directions are FINITE -- and exactly
          equal: the deck-odd difference is IDENTICALLY ZERO. Mechanism: the
          unit mixed involution w (Hermitian, w^2 = I, from the F5 derivation)
          conjugates Q_+ <-> Q_-, K_S -> -K_S, and FIXES every w-even
          reference (gamma, the C2 density A, any function of {I, w}).  A
          positive (state-valued) K_S-twist must absorb the K_S sign flip
          into the sector label, so every covariant Araki-form functional of
          the pair is SWAP-SYMMETRIC and its deck-odd part vanishes -- the
          entropy channel is w-EVEN while the sector datum is w-ODD.  The
          swap group is in fact LARGER than w: out-of-plane mixed bivectors
          V = c_m c_tau commute with D itself and anticommute with K_S, so
          the sector is stored ONLY in the relative sign between K_S and the
          cut -- every K_S-even functional (every entropy) is blind.  The
          F5 Krein-signed functional k_sigma escapes precisely because it is
          LINEAR in K_S (odd pairing, not a positive state); the one nonzero
          entropic escape (a K_S-linear Gibbs reference) collapses exactly
          to that linear moment times a hand-inserted coefficient.
  Part 4  scale: every normalized functional here is invariant under
          xi -> lambda xi; the A-dressed unnormalized (Lindblad-form) variant
          is homogeneous of degree 2 -- it would have carried the symbol's
          normalization (k_sigma-type homogeneity, no absolute unit), but its
          deck-odd part is also w-forced to zero.
  Part 5  bridge: Bianconi's emergent-Lambda functional Tr(G - 1 - ln G)
          (arXiv:2408.14391 / worked form arXiv:2602.13694 Eq. 12) evaluated
          on the native positive dressing G = e^{alpha w} equals
          128 (cosh alpha - 1): finite and positive BECAUSE positivity of the
          dressing is derived -- but w-even (sector-blind) and scale-free.

CONSTRUCTIONS (GEOMETER-VS-PHYSICS-OBJECTS discipline):
  Q_+/Q_-:   PROGRAM-NATIVE canonical Krein cuts (maximal K-definite,
             D-invariant), machinery identical to the F2 probe.
  States:    the K_S-twist M_sigma = sigma K_S Q_sigma is the native positive
             normalization (PSD because the cut ranges are K-definite); the
             Hilbertized projector states are the STANDARD-FIELD fork,
             computed for the record (both forks reported).
  gamma, A:  PROGRAM-NATIVE: gamma = e^{alpha w}/Z is the derived positive
             dressing K_S S; A = (26/7) s I + (4/7) sqrt(PT) w is the closed
             form of the C2 obstruction density X X^+ (master-identity doc),
             consumed as INPUT here, not re-derived.
  Araki:     IMPORTED-standard mathematics (modular theory specialized to
             finite type I), stated above and verified in-probe.

NONCLAIMS: no N2 boundary family, no S_IG, no claim/canon/posture movement;
the w-forced vanishing is a toy-grade structural negative about Araki-form
functionals of THIS pair, not a no-go for entropy on an actual end family.
Deterministic; numpy only; seeded 20260720.
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
TOL = 1e-9
RNG = np.random.default_rng(20260720)
RESULTS: list[tuple[str, str, bool]] = []


def check(tag: str, name: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((tag, name, bool(ok)))
    line = f"[{tag}] {'PASS' if ok else 'FAIL'}  {name}"
    if detail:
        line += f"   ({detail})"
    print(line)


# --- anchors ------------------------------------------------------------------
e = gb.gammas()
XI = np.real(np.asarray(gb.XI)).astype(float)
I128 = np.eye(DIM, dtype=complex)
K_S = e[0].copy()
for a in range(1, 9):
    K_S = K_S @ e[a]


def cvec(v: np.ndarray) -> np.ndarray:
    return sum(v[a] * e[a] for a in range(N_DIRS))


def qform(v: np.ndarray) -> float:
    return float(v @ (ETA * v))


def rot(n: int, a: int, b: int, th: float) -> np.ndarray:
    A = np.eye(n)
    A[a, a] = A[b, b] = np.cos(th)
    A[a, b] = -np.sin(th)
    A[b, a] = np.sin(th)
    return A


# --- cut machinery (identical construction to the F2 / b895d95 probes) --------
def spectral_halves(D: np.ndarray, q: float):
    plus = 0.5 * (I128 + D / np.sqrt(q))
    return plus, I128 - plus


def half_basis(ch: np.ndarray) -> np.ndarray:
    left, _s, _r = np.linalg.svd(ch)
    return left[:, : DIM // 2]


def gram_parts(B: np.ndarray):
    G = B.conj().T @ K_S @ B
    G = 0.5 * (G + G.conj().T)
    w_, S_ = np.linalg.eigh(G)
    return B @ S_[:, w_ > 0], B @ S_[:, w_ < 0]


def kproj(Xc: np.ndarray) -> np.ndarray:
    M = Xc.conj().T @ K_S @ Xc
    return Xc @ np.linalg.solve(M, Xc.conj().T @ K_S)


def krein_cuts(D: np.ndarray, q: float):
    chp, chm = spectral_halves(D, q)
    p_pos, p_neg = gram_parts(half_basis(chp))
    m_pos, m_neg = gram_parts(half_basis(chm))
    Wp = np.hstack([p_pos, m_pos])
    Wm = np.hstack([p_neg, m_neg])
    return kproj(Wp), kproj(Wm), Wp, Wm


def hilbert_projector(cols: np.ndarray) -> np.ndarray:
    Qc, _ = np.linalg.qr(cols)
    return Qc @ Qc.conj().T


# --- entropy machinery (finite type-I Araki = Umegaki + support law) -----------
def eigh_clip(M: np.ndarray):
    vals, vecs = np.linalg.eigh(0.5 * (M + M.conj().T))
    return vals, vecs


def support_projector(M: np.ndarray, tol: float = 1e-10) -> np.ndarray:
    vals, vecs = eigh_clip(M)
    keep = vecs[:, vals > tol * max(1.0, float(np.max(np.abs(vals))))]
    return keep @ keep.conj().T


def violating_mass(rho: np.ndarray, sigma: np.ndarray) -> float:
    n = rho.shape[0]
    comp = np.eye(n, dtype=complex) - support_projector(sigma)
    return float(np.trace(rho @ comp).real)


def trace_ln_on_support(M: np.ndarray) -> np.ndarray:
    """ln(M) on supp(M) (0 outside): valid inside traces against operators
    supported in supp(M)."""
    vals, vecs = eigh_clip(M)
    floor = 1e-14 * max(1.0, float(np.max(np.abs(vals))))
    lv = np.where(vals > floor, np.log(np.maximum(vals, floor)), 0.0)
    return (vecs * lv) @ vecs.conj().T


def araki(rho: np.ndarray, sigma: np.ndarray, tol: float = 1e-8):
    """Finite type-I Araki relative entropy with the support convention.
    Returns (value, finite_flag)."""
    if violating_mass(rho, sigma) > tol:
        return np.inf, False
    val = np.trace(rho @ (trace_ln_on_support(rho)
                          - trace_ln_on_support(sigma))).real
    return float(val), True


def araki_unnormalized(M: np.ndarray, N: np.ndarray, tol: float = 1e-8):
    """Lindblad extension to positive weights:
    S(M||N) = Tr[M(ln M - ln N) - M + N]; same support law."""
    if violating_mass(M, N) > tol * max(1.0, float(np.trace(M).real)):
        return np.inf, False
    val = np.trace(M @ (trace_ln_on_support(M) - trace_ln_on_support(N))
                   - M + N).real
    return float(val), True


# =============================================================================
# [T] setup: rep, xi split, w involution, canonical cut = K_S e^{alpha w}
# =============================================================================
q_xi = qform(XI)
herm = float(np.max(np.abs(K_S - K_S.conj().T)))
invol = float(np.max(np.abs(K_S @ K_S - I128)))
check("T", "anchors: K_S Hermitian involution; frozen xi has q = 30.13",
      herm < TOL and invol < TOL and abs(q_xi - 30.13) < 1e-9,
      f"q = {q_xi:.4f}")

xi_s = XI.copy()
xi_s[9:] = 0.0
xi_t = XI - xi_s
P_sp = float(xi_s @ xi_s)
T_tm = float(xi_t @ xi_t)
s_tot = P_sp + T_tm
alpha = float(np.arctanh(np.sqrt(T_tm / P_sp)))
w_inv = (cvec(xi_s) @ cvec(xi_t)) / np.sqrt(P_sp * T_tm)
w_herm = float(np.max(np.abs(w_inv - w_inv.conj().T)))
w_sq = float(np.max(np.abs(w_inv @ w_inv - I128)))
w_anti = float(np.max(np.abs(K_S @ w_inv + w_inv @ K_S)))
check("T", "w = c_s c_t / sqrt(PT) is a traceless Hermitian unitary involution "
           "anticommuting with K_S; alpha = artanh(sqrt(T/P)) = 0.556134 "
           "(the F5 rapidity)",
      w_herm < TOL and w_sq < TOL and w_anti < TOL
      and abs(complex(np.trace(w_inv))) < TOL and abs(alpha - 0.556134) < 1e-6,
      f"alpha = {alpha:.6f}")

EXP_AW = np.cosh(alpha) * I128 + np.sinh(alpha) * w_inv     # e^{alpha w}
E_HAT = K_S @ EXP_AW                                        # K_S e^{alpha w}

D0 = cvec(XI)
Qp, Qm, Wp, Wm = krein_cuts(D0, q_xi)
S_cut = Qp - Qm
sgn = 1.0 if float(np.max(np.abs(S_cut - E_HAT))) < 1e-6 else -1.0
cut_match = float(np.max(np.abs(S_cut - sgn * E_HAT)))
check("T", "canonical cut pair reproduced: Q_+ + Q_- = I, K-self-adjoint, and "
           "S = Q_+ - Q_- equals K_S e^{alpha w} (F5 closed form; positivity "
           "of the dressing e^{alpha w} = K_S S is DERIVED, spectrum "
           "{e^-a, e^+a})",
      float(np.max(np.abs(Qp + Qm - I128))) < 1e-8
      and float(np.max(np.abs(K_S @ Qp.conj().T @ K_S - Qp))) < 1e-8
      and cut_match < 1e-8 and sgn == 1.0,
      f"|S - K_S e^(aw)| = {cut_match:.1e}")

A_C2 = (26.0 / 7.0) * s_tot * I128 + (4.0 / 7.0) * np.sqrt(P_sp * T_tm) * w_inv
a_eigs = np.linalg.eigvalsh(A_C2)
C2SQ = (3328.0 / 7.0) * s_tot
check("T", "C2 obstruction density in closed form (master-identity input): "
           "A = (26/7) s I + (4/7) sqrt(PT) w is Hermitian, FULL-RANK "
           "positive, Tr A = C2^2 = 24137.51",
      float(np.min(a_eigs)) > 1.0
      and abs(float(np.trace(A_C2).real) - C2SQ) < 1e-6,
      f"min eig {float(np.min(a_eigs)):.2f}, Tr A = {float(np.trace(A_C2).real):.2f}")


# =============================================================================
# Part 1 -- the definition, machine-checked (small dimension)
# =============================================================================
def rand_state(d: int, rank: int | None = None) -> np.ndarray:
    r = rank if rank is not None else d
    B = RNG.standard_normal((d, r)) + 1j * RNG.standard_normal((d, r))
    M = B @ B.conj().T
    return M / np.trace(M).real


d_small = 8
rho_s = rand_state(d_small)
sig_s = rand_state(d_small)
# modular route: Delta_{sigma|rho} X = sigma X rho^{-1} on HS space;
# S = -<rho^{1/2}, ln Delta rho^{1/2}>_HS, evaluated in the joint eigenbases.
rv, rV = eigh_clip(rho_s)
sv, sV = eigh_clip(sig_s)
xi_vec = rV @ np.diag(np.sqrt(np.maximum(rv, 0.0))) @ rV.conj().T
Msx = sV.conj().T @ xi_vec @ rV        # <s_i| xi |r_j>
S_mod = 0.0
for i in range(d_small):
    for j in range(d_small):
        S_mod -= np.log(sv[i] / rv[j]) * float(np.abs(Msx[i, j]) ** 2)
S_ume, fin = araki(rho_s, sig_s)
check("E", "finite type-I Araki = Umegaki: the relative modular operator "
           "Delta_{sigma|rho} X = sigma X rho^{-1} gives "
           "-<xi_rho, ln Delta xi_rho> equal to Tr rho(ln rho - ln sigma) on "
           "a seeded faithful pair (the definition is implemented, not "
           "assumed)",
      fin and abs(S_mod - S_ume) < 1e-10,
      f"modular {S_mod:.10f} vs Umegaki {S_ume:.10f}")

sig_def = rand_state(d_small, rank=5)
rho_full = rand_state(d_small)
m_viol = violating_mass(rho_full, sig_def)
eps_list = (1e-4, 1e-6, 1e-8)
vals_eps = []
for eps in eps_list:
    sig_eps = (1.0 - eps) * sig_def + eps * np.eye(d_small) / d_small
    v, _ = araki(rho_full, sig_eps)
    vals_eps.append(v)
slope1 = (vals_eps[1] - vals_eps[0]) / np.log(eps_list[0] / eps_list[1])
slope2 = (vals_eps[2] - vals_eps[1]) / np.log(eps_list[1] / eps_list[2])
check("E", "the support law is quantitative: for supp rho !<= supp sigma the "
           "regularized value diverges like (violating mass) x ln(1/eps) -- "
           "+infinity is the modular fact, not a regulator artifact",
      m_viol > 1e-3 and abs(slope1 - m_viol) < 0.05 * m_viol
      and abs(slope2 - m_viol) < 0.05 * m_viol,
      f"mass {m_viol:.4f}, slopes {slope1:.4f}, {slope2:.4f}")

psi0 = np.zeros(4, dtype=complex)
psi0[0] = 1.0
psi1 = np.zeros(4, dtype=complex)
psi1[0], psi1[1] = np.cos(0.7), np.sin(0.7)
P0 = np.outer(psi0, psi0.conj())
P1 = np.outer(psi1, psi1.conj())
_, f01 = araki(P0, P1)
_, f10 = araki(P1, P0)
check("F", "pure-state law control: Araki relative entropy between DISTINCT "
           "pure states is +infinity in both directions -- the b895d95 "
           "disease is purity/support, which the modular formulation does "
           "not cure at type I (type-III finiteness, arXiv:2510.24491, is a "
           "same-folium phenomenon, a different animal)",
      (not f01) and (not f10))


# =============================================================================
# Part 2 -- the actual pair: support verdicts (K-a for the direct pairings)
# =============================================================================
Pp_h = hilbert_projector(Wp)
Pm_h = hilbert_projector(Wm)
rho_hp = Pp_h / (DIM // 2)
rho_hm = Pm_h / (DIM // 2)
mv1 = violating_mass(rho_hp, rho_hm)
mv2 = violating_mass(rho_hm, rho_hp)
check("E", "naive (Hilbertized-projector) pair at modular grade: mutual "
           "support violation, Araki = +infinity BOTH directions -- K-a "
           "fires for the b895d95 pairing under the honest definition "
           "(Araki changes nothing there, as it must)",
      mv1 > 1e-2 and mv2 > 1e-2,
      f"violating masses {mv1:.3f}, {mv2:.3f}")

M_plus = K_S @ Qp                       # = Q_+^dag K_S Q_+ (K-selfadjointness)
M_minus = -K_S @ Qm
alt_p = float(np.max(np.abs(M_plus - Qp.conj().T @ K_S @ Qp)))
alt_m = float(np.max(np.abs(M_minus + Qm.conj().T @ K_S @ Qm)))
mp_e = np.linalg.eigvalsh(0.5 * (M_plus + M_plus.conj().T))
mm_e = np.linalg.eigvalsh(0.5 * (M_minus + M_minus.conj().T))
tr_mp = float(np.trace(M_plus).real)
rho_tp = 0.5 * (M_plus + M_plus.conj().T) / tr_mp
rho_tm = 0.5 * (M_minus + M_minus.conj().T) / float(np.trace(M_minus).real)
check("E", "the K_S-TWISTED cut states are the native positive "
           "normalization: M_sigma = sigma K_S Q_sigma = Q_sigma^+ K_S "
           "Q_sigma is Hermitian PSD of rank 64 (positivity from "
           "K-definiteness of the cut ranges, NOT assumed), with "
           "Tr M_+ = 64 cosh(alpha)",
      alt_p < 1e-8 and alt_m < 1e-8
      and float(mp_e[0]) > -1e-8 and float(mm_e[0]) > -1e-8
      and int(np.sum(mp_e > 1e-8)) == 64 and int(np.sum(mm_e > 1e-8)) == 64
      and abs(tr_mp - 64.0 * np.cosh(alpha)) < 1e-6,
      f"Tr M_+ = {tr_mp:.4f} = 64 cosh a")

tv1 = violating_mass(rho_tp, rho_tm)
tv2 = violating_mass(rho_tm, rho_tp)
check("E", "twisted pair, direct pairing: supports are still distinct rank-64 "
           "subspaces -- Araki = +infinity BOTH directions (K-a): the "
           "K_S-twist fixes positivity, not mutual support",
      tv1 > 1e-2 and tv2 > 1e-2,
      f"violating masses {tv1:.3f}, {tv2:.3f}")


# =============================================================================
# Part 3 -- the finite retry against faithful native references, and the
#           w-involution mechanism that forces the deck-odd part to zero
# =============================================================================
Z_gam = float(np.trace(EXP_AW).real)
gamma = EXP_AW / Z_gam
Sp_g, fp_g = araki(rho_tp, gamma)
Sm_g, fm_g = araki(rho_tm, gamma)
F_gamma = Sp_g - Sm_g
check("E", "finite at last: against the native faithful reference "
           "gamma = e^{alpha w}/Z (the derived positive dressing K_S S), "
           "both twisted cut states have FINITE Araki entropy -- and the "
           "two values are EXACTLY equal: the deck-odd difference is "
           "IDENTICALLY ZERO (K-b)",
      fp_g and fm_g and abs(F_gamma) < 1e-9,
      f"S(rho_+||gamma) = {Sp_g:.10f}, S(rho_-||gamma) = {Sm_g:.10f}, "
      f"diff = {F_gamma:.2e}")

sw_q = float(np.max(np.abs(w_inv @ Qp @ w_inv - Qm)))
sw_m = float(np.max(np.abs(w_inv @ (0.5 * (M_plus + M_plus.conj().T)) @ w_inv
                           - 0.5 * (M_minus + M_minus.conj().T))))
sw_g = float(np.max(np.abs(w_inv @ gamma @ w_inv - gamma)))
sw_a = float(np.max(np.abs(w_inv @ A_C2 @ w_inv - A_C2)))
sw_k = float(np.max(np.abs(w_inv @ K_S @ w_inv + K_S)))
check("E", "THE MECHANISM, machine-exact: the w-involution conjugates "
           "Q_+ <-> Q_-, M_+ <-> M_- (the K_S sign flip is absorbed by the "
           "sector label -- forced by positivity), and FIXES gamma and A "
           "while sending K_S -> -K_S: every Araki-form functional of the "
           "pair against a w-even reference is swap-symmetric, so its "
           "deck-odd part VANISHES IDENTICALLY -- the entropy channel is "
           "w-even, the sector datum is w-odd",
      sw_q < 1e-8 and sw_m < 1e-8 and sw_g < 1e-12 and sw_a < 1e-12
      and sw_k < 1e-12,
      f"defects: wQ+w-Q- {sw_q:.1e}, wM+w-M- {sw_m:.1e}, [w,gamma] {sw_g:.1e}")

sqA = None
av, aV = eigh_clip(A_C2)
sqA = (aV * np.sqrt(av)) @ aV.conj().T
C_p = sqA @ rho_tp @ sqA
C_m = sqA @ rho_tm @ sqA
Su_p, fu_p = araki_unnormalized(C_p, A_C2)
Su_m, fu_m = araki_unnormalized(C_m, A_C2)
F_un = Su_p - Su_m
cv1 = violating_mass(C_p / np.trace(C_p).real, C_m / np.trace(C_m).real)
check("E", "the A-dressed (C2-density-weighted, Bianconi-mirror UNNORMALIZED "
           "Lindblad form) variant: C_sigma = A^{1/2} rho_sigma A^{1/2} vs "
           "reference A -- finite both directions, deck-odd part ALSO "
           "identically zero (w fixes A); direct C_+ vs C_- pairing still "
           "support-violating (+infinity)",
      fu_p and fu_m and abs(F_un) < 1e-6 and cv1 > 1e-2,
      f"S_un(C_+||A) = {Su_p:.6f}, S_un(C_-||A) = {Su_m:.6f}, "
      f"diff = {F_un:.2e}")


# =============================================================================
# Part 4 -- deck covariance at the seam, and scale
# =============================================================================
U_h = e[0] @ e[9]
Uh_inv = np.linalg.inv(U_h)
A_pi = rot(N_DIRS, 0, 9, np.pi)
xi_1 = A_pi @ XI
D1 = cvec(xi_1)
Qp1, Qm1, _, _ = krein_cuts(D1, qform(xi_1))
deck1 = float(np.max(np.abs(Qp1 - U_h @ Qm @ Uh_inv)))
xi_s1 = xi_1.copy()
xi_s1[9:] = 0.0
xi_t1 = xi_1 - xi_s1
w_1 = (cvec(xi_s1) @ cvec(xi_t1)) / np.sqrt(float(xi_s1 @ xi_s1)
                                            * float(xi_t1 @ xi_t1))
gam_1 = (np.cosh(alpha) * I128 + np.sinh(alpha) * w_1) / Z_gam
M_p1 = 0.5 * ((K_S @ Qp1) + (K_S @ Qp1).conj().T)
rho_tp1 = M_p1 / float(np.trace(M_p1).real)
seam_g = float(np.max(np.abs(gam_1 - U_h @ gamma @ Uh_inv)))
seam_m = float(np.max(np.abs(rho_tp1 - U_h @ rho_tm @ Uh_inv)))
Sp_g1, _ = araki(rho_tp1, gam_1)
check("E", "seam covariance: at t = 1 the transported data obey "
           "gamma(1) = U_h gamma(0) U_h^{-1} and rho_+(1) = U_h rho_-(0) "
           "U_h^{-1} (deck exchange), so the covariant functional satisfies "
           "F(1) = -F(0) by unitary invariance: HOLONOMY-ODD BY "
           "CONSTRUCTION -- and identically zero in value (S(rho_+(1)||"
           "gamma(1)) = S(rho_-(0)||gamma(0))): the odd functional exists "
           "only as 0",
      deck1 < 1e-8 and seam_g < 1e-8 and seam_m < 1e-7
      and abs(Sp_g1 - Sm_g) < 1e-7,
      f"deck {deck1:.1e}, seam gamma {seam_g:.1e}, "
      f"S at seam {Sp_g1:.8f} vs {Sm_g:.8f}")

scale_norm, scale_hom = [], []
for lam in (0.25, 2.0, 7.0):
    xi_l = lam * XI
    Ql_p, Ql_m, _, _ = krein_cuts(cvec(xi_l), qform(xi_l))
    Ml_p = 0.5 * ((K_S @ Ql_p) + (K_S @ Ql_p).conj().T)
    rho_lp = Ml_p / float(np.trace(Ml_p).real)
    Sl, _ = araki(rho_lp, gamma)          # gamma is xi-scale-invariant (alpha, w)
    scale_norm.append(abs(Sl - Sp_g))
    A_l = lam * lam * A_C2                # A is homogeneous degree 2 in xi
    avl, aVl = eigh_clip(A_l)
    sqAl = (aVl * np.sqrt(avl)) @ aVl.conj().T
    C_lp = sqAl @ rho_lp @ sqAl
    Sul, _ = araki_unnormalized(C_lp, A_l)
    scale_hom.append(abs(Sul - lam * lam * Su_p))
check("E", "scale: every normalized functional is invariant under "
           "xi -> lambda xi (the cuts, w, alpha carry no scale -- b895d95 "
           "finding 5 is structural); the unnormalized A-dressed form is "
           "exactly homogeneous of degree 2 (k_sigma-type: it reads the "
           "symbol's normalization, no absolute unit) -- a dial LOCATION, "
           "but its odd part is zero, so nothing is delivered on it",
      max(scale_norm) < 1e-7 and max(scale_hom) < 1e-5,
      f"norm-invariance defect {max(scale_norm):.1e}, "
      f"homogeneity defect {max(scale_hom):.1e}")


# =============================================================================
# Part 5 -- bridge and escape controls
# =============================================================================
lamG = float(np.trace(EXP_AW - I128
                      - alpha * w_inv).real)   # ln e^{alpha w} = alpha w
lamG_closed = 128.0 * (np.cosh(alpha) - 1.0)
check("E", "Bianconi bridge: her emergent-Lambda functional "
           "Tr(G - 1 - ln G) (arXiv:2408.14391; worked form arXiv:2602.13694 "
           "Eq. 12) evaluated on the NATIVE positive dressing G = e^{alpha w} "
           "= 128(cosh alpha - 1) = 20.31: finite and positive because the "
           "dressing's positivity is DERIVED -- but w-even (sector-blind) "
           "and scale-free: on the native pair her functional lands in the "
           "same even channel",
      abs(lamG - lamG_closed) < 1e-9 and lamG > 0.0,
      f"Lambda_G[e^(aw)] = {lamG:.4f}")

u_op = cvec(xi_s) / np.sqrt(P_sp)
H_brk = alpha * w_inv + 0.3 * u_op
hv, hV = eigh_clip(H_brk)
gam_brk = (hV * np.exp(hv)) @ hV.conj().T
gam_brk = gam_brk / float(np.trace(gam_brk).real)
Sb_p, _ = araki(rho_tp, gam_brk)
Sb_m, _ = araki(rho_tm, gam_brk)
F_brk = Sb_p - Sb_m
brk_def = float(np.linalg.norm(w_inv @ gam_brk @ w_inv - gam_brk)
                / np.linalg.norm(gam_brk))

# the out-of-plane swap: m spatial unit vector K-orthogonal to xi_s, tau
# timelike unit vector K-orthogonal to xi_t; V = c_m c_tau.
m_vec = np.zeros(N_DIRS)
m_vec[0] = 1.0
m_vec[:9] -= (m_vec[:9] @ xi_s[:9]) / P_sp * xi_s[:9]
m_vec /= np.sqrt(m_vec @ m_vec)
tau_vec = np.zeros(N_DIRS)
tau_vec[9] = 1.0
tau_vec[9:] -= (tau_vec[9:] @ xi_t[9:]) / T_tm * xi_t[9:]
tau_vec /= np.sqrt(tau_vec @ tau_vec)
V_sw = cvec(m_vec) @ cvec(tau_vec)
v_props = max(float(np.max(np.abs(V_sw - V_sw.conj().T))),
              float(np.max(np.abs(V_sw @ V_sw - I128))),
              float(np.max(np.abs(V_sw @ u_op - u_op @ V_sw))),
              float(np.max(np.abs(V_sw @ w_inv - w_inv @ V_sw))),
              float(np.max(np.abs(V_sw @ D0 - D0 @ V_sw))))
v_anti = float(np.max(np.abs(V_sw @ K_S + K_S @ V_sw)))
v_swap = float(np.max(np.abs(V_sw @ Qp @ V_sw - Qm)))
v_fix = float(np.max(np.abs(V_sw @ gam_brk @ V_sw - gam_brk)))
check("E", "the swap group is LARGER than w -- exhaustion leg: the w-broken "
           "reference e^{alpha w + 0.3 u} STILL gives an exactly zero "
           "difference, and the responsible symmetry is exhibited: "
           "V = c_m c_tau (out-of-plane mixed bivector, m K-orthogonal to "
           "xi_s, tau K-orthogonal to xi_t) is a Hermitian unitary "
           "involution COMMUTING with u, w, and D itself, ANTICOMMUTING "
           "with K_S, swapping Q_+ <-> Q_- and fixing the reference: the "
           "sector is stored ONLY in the relative sign between K_S and the "
           "cut, so every K_S-EVEN functional -- every entropy -- is blind "
           "to it (the entropy-level image of storable-but-locally-"
           "unreadable)",
      brk_def > 0.1 and abs(F_brk) < 1e-9
      and v_props < 1e-9 and v_anti < 1e-9 and v_swap < 1e-7
      and v_fix < 1e-9,
      f"F(u-broken ref) = {F_brk:.2e}, V-swap defect {v_swap:.1e}")

eps_K = 0.3
H_K = alpha * w_inv + eps_K * K_S
kv, kV = eigh_clip(H_K)
gam_K = (kV * np.exp(kv)) @ kV.conj().T
gam_K = gam_K / float(np.trace(gam_K).real)
SK_p, _ = araki(rho_tp, gam_K)
SK_m, _ = araki(rho_tm, gam_K)
F_K = SK_p - SK_m
sech_a = 1.0 / np.cosh(alpha)
F_K_closed = -2.0 * eps_K * sech_a
mom_p = float(np.trace(rho_tp @ K_S).real)
mom_m = float(np.trace(rho_tm @ K_S).real)
check("F", "the only nonzero escape, and it collapses to the linear "
           "channel: a K_S-LINEAR reference term (gamma_K ~ "
           "e^{alpha w + eps K_S}, eps = 0.3 inserted BY HAND) makes the "
           "difference nonzero -- but EXACTLY F = -2 eps sech(alpha) = "
           "-eps [Tr rho_+ K_S - Tr rho_- K_S]: the Gibbs reference turns "
           "relative entropy into the K_S-linear odd moment (= sigma "
           "sech(alpha), the F5 definiteness margin) times the inserted "
           "coefficient -- the entropic wrapper contributes NOTHING beyond "
           "the k_sigma-type linear pairing, the coefficient is a hand "
           "dial, and the value is scale-free",
      abs(F_K - F_K_closed) < 1e-9
      and abs(mom_p - sech_a) < 1e-9 and abs(mom_m + sech_a) < 1e-9,
      f"F_K = {F_K:.6f} vs closed form {F_K_closed:.6f}; "
      f"Tr rho_sigma K_S = sigma {sech_a:.4f}")

k_plus = float(np.trace(K_S @ Qp @ A_C2).real)
k_minus = float(np.trace(K_S @ Qm @ A_C2).real)
k_exact = 14421.0033
check("F", "the escape that is REAL: the F5 Krein-signed functional "
           "k_sigma = Re tr(K_S Q_sigma A) reads the sector at this same "
           "grade (k_+ = -k_- = 14421.0033) because it is LINEAR in the "
           "w-ODD object K_S -- an odd pairing, not a positive state: the "
           "sector lives in the odd channel, and positivity (any entropy) "
           "forces evenness",
      abs(k_plus - k_exact) < 0.01 and abs(k_plus + k_minus) < 1e-6,
      f"k_+ = {k_plus:.4f}, k_+ + k_- = {k_plus + k_minus:.2e}")


# --- headline -----------------------------------------------------------------
nE = sum(1 for t, _n, _o in RESULTS if t == "E")
nF = sum(1 for t, _n, _o in RESULTS if t == "F")
nT = sum(1 for t, _n, _o in RESULTS if t == "T")
all_ok = all(ok for _t, _n, ok in RESULTS)
print()
print("ARAKI CUT ENTROPY VERDICT: the entropic route between the two Krein "
      "cuts is DEAD at toy grade with the mechanism named -- K-a (support "
      "+infinity) for every direct pairing, K-b (identically zero deck-odd "
      "part) for every finite covariant retry: a swap group of unitary "
      "involutions (in-plane w and out-of-plane V = c_m c_tau, the latter "
      "commuting with D itself) exchanges the cuts while anticommuting with "
      "K_S and fixing every K_S-even positive reference; positivity forces "
      "the K_S-twist to absorb the sign that carried the sector. Entropy is "
      "K_S-even; the sector is the relative K_S sign; only K_S-linear "
      "pairings (k_sigma) read it -- and the sole entropic escape collapses "
      "exactly to that linear moment times a hand dial.")
print(f"HEADLINE: {nE} [E] + {nF} [F] = {nE + nF} (setup [T] = {nT} excluded) "
      f"{'ALL PASS' if all_ok else 'FAILURES PRESENT'}")
sys.exit(0 if all_ok else 1)
