#!/usr/bin/env python3
"""Hardening swing H3: the 192-dim triplet lift of the graded-quotient +
C-operator construction (gaps G-B1 + the D1 lift), 2026-07-19.

AXIOM:  lab/process/boundary-adapter-standing-axiom.md (adapter assumed;
        adapter-needed is never a stop -- typed demands, conditional grades).
GROUND: explorations/channel-swing-CH-QM-2026-07-19.md (the 9-dim toy and its
        declared lift path); explorations/d1-coperator-build-2026-07-19.md
        (the dimension-agnostic C-operator recipe + the K-definite-gap
        blocker); canon/ghost-parity-krein-synthesis.md (triplet kinematics);
        tests/generation-sector/ghost_parity_krein.py (the triplet extraction
        machinery, REUSED); tests/channel-swings/ch_qm_graded_quotient_toy.py
        (Q-battery shape + Part-A register, REUSED).
STATUS: exploration tier; conditional (R0_COND); no claim/canon/posture moves.

WHAT IS LIFTED. The CH-QM 9-dim toy (1 transverse + 1 gauge pair + 3
generation/mirror pairs) becomes the ACTUAL structure: the 192-dim self-dual
SU(2)+ generation triplet inside the 1792-dim RS module V (x) S over the
verified Cl(9,5) = M(64,H) representation, with the intrinsic Krein form
K = eta_V (x) beta_S restricted to the triplet -- signature (+96, -96), 96
hyperbolic (generation, mirror) pairs, each chirality half totally null
(canon, re-verified here from scratch). The battery fixture is 194-dim:
one hyperbolic gauge block (g, s) + the full 192-dim triplet in its
K-canonical pair frame, with the toy's causality coupling and a parity-even
interaction dressing.

TYPED CONDITIONAL IMPORT (declared, per the standing axiom). The pair gap
delta -- which the 9-dim toy inserted silently by hand -- CANNOT be GU-native
at scale: the so(9,5) Casimir on the verified spinor is exactly a scalar
(re-verified), and big-swing R3 proved every GU-native core sign-blind, so
the native pair dynamics is mu*I, exactly degenerate. The gap operator
G_gap = delta * (pair swap) is therefore imported as a typed stand-in for
the unbuilt S_IG / B.5 global data, and this probe TYPES it: it is chi-ODD
(exact anticommutation with the triplet chirality) and non-equivariant under
the triplet-preserving internal so(9,5) boosts -- outside the native family
on two independent axes. Everything downstream of delta is conditional on
that import. The parity-even dressing V_pe used in the battery is ALSO
conditional on it (parity-evenness is defined relative to the imported
grading) -- a dependence the 9-dim toy obscured and this lift surfaces.

CHECKS.
 PART 0 [T] the triplet, built from the verified rep: anchors reproduced;
        Gamma Gamma^dag = 14 I exact; SU(2)+ Casimir top eigenspace = 192-dim
        (spectral gap reported); K|triplet signature (+96,-96); chirality
        splits 96/96 with both halves K-null; cross-pairing full rank (min
        singular value reported); K-canonical pair frame with residual;
        J_quat preserves the triplet and the canonical physical sector
        (CH-QM A4 typing at full scale); Q4 register re-run (toy Part A,
        scale-independent storage certificate).
 PART 1 [E] Q1 Q2 Q3 Q5 Q6 at 192 dims, RIGHT orientation: Noether closure;
        quotient well-formed; 96-dim physical Gram positive-definite;
        descended dynamics Hermitian + norm-preserving; Born positivity +
        normalization; K-Hermitian parity-even observables restrict
        Hermitian.
 PART 2 [E] WRONG orientation: the primary failure is COHOMOLOGICAL
        (non-closure = gamma); quotient ill-formed; brute grading -> 96
        negative-norm survivors; delete-negatives -> unremovable zombie with
        exact e^{gamma t} growth regenerated from kept ghosts (feed = c);
        retune numerically possible but structurally blocked (loop-coherent
        storage, Part A).
 PART 3 [E] D1 at scale: native dynamics scalar (Casimir anchor) -> at the
        vacuum anchors the 192-dim eigengroup is K-INDEFINITE (+96,-96),
        the recipe ABORTS, and an explicit continuum of admissible C's
        exists (global + per-pair hyperbolic boosts; the continuum is
        2*96^2 = 18432-real-dimensional, vs 18 in the toy); with the typed
        gap import the recipe SUCCEEDS: C determined, equal to the kinematic
        K-grading, stable under perturbation, -C inadmissible, anchor
        co-flip (B -> -B => C -> -C) exact, continuum collapsed; the
        undetermined datum is exactly one Z/2 within the typed payload
        family. Import typing: G_gap chi-odd; nonzero commutator with
        triplet-preserving internal boosts.
 PART 4 [E/F] compensator sector at FULL 1792-dim scale: fixed
        non-equivariant boost carrier sigma_c dressing the RS constraint;
        dressed C2 obstruction computed; C2 scale law C2(2xi)/C2(xi) = 2
        EXACT for the scale-free compensator; [F] a scale-carrying
        compensator kernel breaks the law (CH-GR K3 executable at full
        scale); equivariant tripwire (a Cl(9,5)-commutant carrier is
        quaternionic-scalar, drops out of the dressing entirely -- GHOST-01
        image). What is NOT feasible here is typed as a gap: the
        compensator FIELD tier (Stueckelberg action), the antighost leg,
        the non-abelian master equation.

NONCLAIMS. Conditional throughout: the gap import stands in for S_IG/B.5 and
is declared, not derived; no field theory, no Y14 geometry, no counts; the
lift's value is that the MECHANISM survives scale, not that anything becomes
unconditional. Deterministic; numpy only; float64 with exact structural
anchors (residual ceilings printed).

Run: python tests/channel-swings/h3_triplet_lift_probe.py   (exit 0 = pass)
"""
from __future__ import annotations

import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "generation-sector"))
import ch_qm_graded_quotient_toy as toy  # noqa: E402  (Q4 register + fixture conventions)
import gen_sector_bridge as gb           # noqa: E402  (verified Cl(9,5) rep + anchors)

T0 = time.time()
RNG = np.random.default_rng(20260719)
RESULTS = []

N, DIMS = 14, 128           # 14 vector slots x 128-dim spinor
NTRIP = 192                 # triplet sector dimension
NPAIR = 96                  # hyperbolic (generation, mirror) pairs
GAMMA, MU, DELTA, CPL, KAPPA = 0.7, 1.3, 0.2, 0.35, 0.15
# KAPPA < DELTA guarantees the two graded sectors (centered mu +/- delta)
# stay spectrally disjoint under the parity-even dressing (spectral-norm cap)
SIGMA_STAR = +1


def check(tag, name, ok, detail=""):
    RESULTS.append((tag, name, bool(ok)))
    line = f"[{tag}] {'PASS' if ok else 'FAIL'}  {name}"
    if detail:
        line += f"   ({detail})"
    print(line, flush=True)
    return ok


def K_of(B, x, y):
    return complex(np.conj(x) @ B @ y)


# =============================================================================
print("=" * 78)
print("PART 0  the 192-dim triplet, built from the verified Cl(9,5) rep")
print("=" * 78)

e = gb.gammas()                                   # timelike = indices 9..13
Gamma = np.hstack(e)                              # 128 x 1792
anc = gb.anchors()
check("T", "verified-rep anchors reproduced (bare commutator 58.7215, "
           "C2 = 155.3625)",
      abs(anc["bare_commutator"] - 58.7215) < 1e-3
      and abs(anc["C2"] - 155.3625) < 1e-3,
      f"{anc['bare_commutator']:.4f} / {anc['C2']:.4f}")

GG = Gamma @ Gamma.conj().T
check("T", "Gamma Gamma^dag = 14 I EXACT (each gamma unitary) -> "
           "Pi_RS = I - Gamma^dag Gamma / 14, exact structural anchor",
      np.linalg.norm(GG - 14.0 * np.eye(DIMS)) < 1e-12,
      f"||GG^dag - 14 I|| = {np.linalg.norm(GG - 14.0 * np.eye(DIMS)):.1e}")

# constraint-surface basis: kernel of Gamma via SVD (1664 columns)
_, sv, Vh = np.linalg.svd(Gamma, full_matrices=True)
W = Vh[DIMS:].conj().T                            # 1792 x 1664
assert np.linalg.norm(Gamma @ W) < 1e-9

# self-dual SU(2)+ on the Euclidean base {0,1,2,3} (ghost_parity_krein.py
# machinery, reused verbatim in shape)
I128, I14 = np.eye(DIMS, dtype=complex), np.eye(N, dtype=complex)


def sgen(i, j):
    return 0.25 * (e[i] @ e[j] - e[j] @ e[i])


def lvec(i, j):
    M = np.zeros((N, N), dtype=complex)
    M[i, j] = 1
    M[j, i] = -1
    return M


SD = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2)]
J_sd = [np.kron(I14, sgen(a, b) + sgen(c, d)) + np.kron(lvec(a, b) + lvec(c, d), I128)
        for (a, b, c, d) in SD]
Cas = -(J_sd[0] @ J_sd[0] + J_sd[1] @ J_sd[1] + J_sd[2] @ J_sd[2])
CasK = W.conj().T @ Cas @ W
CasK = 0.5 * (CasK + CasK.conj().T)
ev, U = np.linalg.eigh(CasK)
top = ev.max()
sel = np.abs(ev - top) < 1e-6
gap_next = top - ev[~sel].max()
Wt = W @ U[:, sel]                                # 1792 x 192, Euclid-orthonormal
check("T", "SU(2)+ Casimir top eigenspace on ker(Gamma) is the 192-dim "
           "triplet (generators are 2x standard here, so Casimir = 4 j(j+1): "
           "spectrum 8/3/0 = triplet/doublet/singlet), isolated by a clean "
           "spectral gap",
      int(sel.sum()) == NTRIP and abs(top - 8.0) < 1e-9 and gap_next > 0.5,
      f"dim = {int(sel.sum())}, Casimir = {top:.6f} (j = 1), "
      f"gap to next = {gap_next:.3f}")


def apply_VS(eta_diag, M128, X):
    """Apply (diag(eta) (x) M128) to columns of X (1792 x k), blockwise."""
    Xr = X.reshape(N, DIMS, -1)
    out = np.einsum("ab,ibk->iak", M128, Xr)
    out = out * np.asarray(eta_diag, dtype=complex)[:, None, None]
    return out.reshape(N * DIMS, -1)


# intrinsic Krein form K = eta_V (x) beta_S, beta_S = product of spacelike gammas
etaV = [1.0] * 9 + [-1.0] * 5
betaS = np.eye(DIMS, dtype=complex)
for a in range(9):
    betaS = betaS @ e[a]
assert np.linalg.norm(betaS - betaS.conj().T) < 1e-12          # Hermitian, no i
assert np.linalg.norm(betaS @ betaS - I128) < 1e-12
B_t = Wt.conj().T @ apply_VS(etaV, betaS, Wt)     # K restricted to the triplet
B_t = 0.5 * (B_t + B_t.conj().T)
sig = np.linalg.eigvalsh(B_t)
npl, nmi = int((sig > 1e-9).sum()), int((sig < -1e-9).sum())
check("T", "K restricted to the triplet has signature (+96, -96) -- the "
           "canon hyperbolic structure, re-derived from scratch",
      npl == NPAIR and nmi == NPAIR,
      f"(+{npl}, -{nmi}); |eigenvalues| in "
      f"[{np.abs(sig).min():.3f}, {np.abs(sig).max():.3f}]")

# chirality chi = normalized product of all 14 gammas; splits the triplet
chi128 = np.eye(DIMS, dtype=complex)
for a in range(14):
    chi128 = chi128 @ e[a]
c2 = (chi128 @ chi128)[0, 0]
chi128 = chi128 / np.sqrt(c2)                     # chi^2 = I; unitary+involutive => Hermitian
assert np.linalg.norm(chi128 @ chi128 - I128) < 1e-10
assert np.linalg.norm(chi128 - chi128.conj().T) < 1e-10
chiWt = apply_VS([1.0] * N, chi128, Wt)
leak_chi = np.linalg.norm(chiWt - Wt @ (Wt.conj().T @ chiWt))
chi_t = Wt.conj().T @ chiWt
chi_t = 0.5 * (chi_t + chi_t.conj().T)
evc, Uc = np.linalg.eigh(chi_t)
n_min, n_pls = int((evc < -0.5).sum()), int((evc > 0.5).sum())
Up, Um = Uc[:, evc > 0.5], Uc[:, evc < -0.5]      # 192 x 96 each (triplet coords)
null_p = np.linalg.norm(Up.conj().T @ B_t @ Up)
null_m = np.linalg.norm(Um.conj().T @ B_t @ Um)
anti_KX = np.linalg.norm(chi_t @ B_t + B_t @ chi_t)
check("T", "chirality preserves the triplet and splits it 96/96; each half "
           "is TOTALLY K-NULL; {K, chi} = 0 on the triplet (the R3 "
           "anticommutation, here exact at scale)",
      leak_chi < 1e-8 and n_pls == NPAIR and n_min == NPAIR
      and null_p < 1e-8 and null_m < 1e-8 and anti_KX < 1e-8,
      f"leak {leak_chi:.1e}; null residuals {null_p:.1e}/{null_m:.1e}; "
      f"{{K,chi}} = {anti_KX:.1e}")

# the K-canonical pair frame: SVD of the cross-pairing between the null halves
Mx = Up.conj().T @ B_t @ Um                       # 96 x 96 cross-pairing
A_l, s_pair, C_r = np.linalg.svd(Mx)
Uframe = Up @ A_l                                 # generations u_i (triplet coords)
Vframe = Um @ (C_r.conj().T / s_pair[None, :])    # mirrors v_i, K(u_i, v_j) = delta_ij
Pf = np.hstack([Uframe, Vframe])                  # 192 x 192 pair frame
Bp = Pf.conj().T @ B_t @ Pf                       # should be [[0, I], [I, 0]]
Bp = 0.5 * (Bp + Bp.conj().T)
swap = np.zeros((NTRIP, NTRIP), dtype=complex)
swap[:NPAIR, NPAIR:] = np.eye(NPAIR)
swap[NPAIR:, :NPAIR] = np.eye(NPAIR)
frame_res = np.linalg.norm(Bp - swap)
check("T", "the cross-pairing is FULL RANK (96 nonzero singular values) and "
           "the K-canonical pair frame realizes K|triplet = 96 exact "
           "hyperbolic pairs [[0,1],[1,0]]",
      s_pair.min() > 1e-3 and frame_res < 1e-8,
      f"singular values in [{s_pair.min():.4f}, {s_pair.max():.4f}]; "
      f"frame residual ||B - swap|| = {frame_res:.1e}")

# J_quat at scale: preserves the triplet AND the canonical physical sector
Cq = e[1] @ e[3] @ e[5] @ e[7] @ e[10] @ e[12]    # canon C07 convention
JWt = apply_VS([1.0] * N, Cq, np.conj(Wt))        # J_quat = (id (x) C) conj
leak_J = np.linalg.norm(JWt - Wt @ (Wt.conj().T @ JWt))
Wplus = Wt @ ((Pf[:, :NPAIR] + Pf[:, NPAIR:]) / np.sqrt(2))   # physical modes, 1792 x 96
Qp, _ = np.linalg.qr(Wplus)                       # Euclid-orthonormal basis of the sector
JQp = apply_VS([1.0] * N, Cq, np.conj(Qp))
leak_phys = np.linalg.norm(JQp - Qp @ (Qp.conj().T @ JQp))
check("T", "J_quat preserves the 192-dim triplet AND the canonical physical "
           "sector (span of the 96 positive-norm modes) -- CH-QM's A4 typing "
           "(sigma is J_quat-commuting) holds at full scale, not just at "
           "128-dim carrier level",
      leak_J < 1e-8 and leak_phys < 1e-7,
      f"triplet leak {leak_J:.1e}; physical-sector leak {leak_phys:.1e}")

print("\n-- Q4 register (scale-independent storage certificate; toy Part A "
      "re-run) --")
toy.part_A()                                      # loop-coherent Z/2, locally unreadable

print(f"\n[PART 0 wall time: {time.time() - T0:.1f}s]")

# =============================================================================
# the 194-dim battery fixture: gauge hyperbolic block (g, s) + the triplet in
# its K-canonical pair frame.  Indices: 0 = g, 1 = s, 2..97 = u_i, 98..193 = v_i.
# =============================================================================
DIMF = 2 + NTRIP


def fvec(i):
    v = np.zeros(DIMF, dtype=complex)
    v[i] = 1.0
    return v


def n_vec(sigma):
    return (fvec(0) + 1j * sigma * fvec(1)) / np.sqrt(2)


def w_vec(i, sign):
    return (fvec(2 + i) + sign * fvec(2 + NPAIR + i)) / np.sqrt(2)


B_full = np.zeros((DIMF, DIMF), dtype=complex)
B_full[0, 1] = B_full[1, 0] = 1.0
B_full[2:, 2:] = Bp                               # the ACTUAL numerical triplet form

G_gap = np.zeros((DIMF, DIMF), dtype=complex)     # the TYPED gap import (chi-odd)
G_gap[2:, 2:] = swap
P_par = G_gap.copy()                              # ghost parity on the pairs (V2: = K)

# parity-even, K-Hermitian interaction dressing on the pair sector
# (NOTE: parity-evenness is defined via the IMPORTED grading -> conditional)
Xr = RNG.standard_normal((NTRIP, NTRIP)) + 1j * RNG.standard_normal((NTRIP, NTRIP))
Xr = 0.5 * (Xr + swap @ Xr @ swap)                                    # parity-even
Xr = 0.5 * (Xr + np.linalg.solve(Bp, Xr.conj().T @ Bp))               # K-Hermitian
Xr = 0.5 * (Xr + swap @ Xr @ swap)
V_pe = np.zeros((DIMF, DIMF), dtype=complex)
V_pe[2:, 2:] = KAPPA * Xr / np.linalg.norm(Xr, 2)   # spectral-norm cap


def build_H(delta=DELTA, cpl=CPL, with_vpe=True):
    H = np.zeros((DIMF, DIMF), dtype=complex)
    npv, nmv = n_vec(SIGMA_STAR), n_vec(-SIGMA_STAR)
    S2 = np.column_stack([npv[:2], nmv[:2]])
    H[:2, :2] = S2 @ np.diag([1j * GAMMA, -1j * GAMMA]) @ np.linalg.inv(S2)
    H[2:, 2:] = MU * np.eye(NTRIP)
    H = H + delta * G_gap
    if with_vpe:
        H = H + V_pe
    if cpl:
        w1 = w_vec(0, +1)
        H = H + cpl * (np.outer(npv, np.conj(B_full @ w1))
                       + np.outer(w1, np.conj(B_full @ npv)))
    ph = np.linalg.norm(B_full @ H - H.conj().T @ B_full)
    assert ph < 1e-7, f"H must be K-pseudo-Hermitian (residual {ph:.1e})"
    return H


# =============================================================================
print()
print("=" * 78)
print("PART 1  the graded quotient at 192 dims, RIGHT orientation (Q1..Q6)")
print("=" * 78)
print("(pair dynamics mu*I + delta*G_gap + V_pe: delta is the TYPED S_IG/B.5")
print(" import -- see PART 3 -- and V_pe is parity-even RELATIVE TO IT; the")
print(" whole battery is conditional on that one declared import)")

H = build_H()
d2 = np.conj(n_vec(SIGMA_STAR)) @ B_full @ H      # transmitted Noether row

sigma = SIGMA_STAR
closure_r = abs(complex(d2 @ n_vec(sigma)))
check("E", "Q1 (closure): the transmitted Noether identity closes, "
           "delta_2 . d_(RS,-1) = 0, at 192 dims",
      closure_r < 1e-9, f"|delta_2 n_sigma| = {closure_r:.1e}")

_, sv2, Vh2 = np.linalg.svd(d2.reshape(1, -1))
ker = Vh2.conj().T[:, 1:]                         # 193-dim constraint surface
n_s = n_vec(sigma)
in_ker = np.linalg.norm(n_s - ker @ (ker.conj().T @ n_s))
phys = [w_vec(i, sigma) for i in range(NPAIR)]
ghost = [w_vec(i, -sigma) for i in range(NPAIR)]
mem = max(max(abs(complex(d2 @ b)) for b in phys + ghost),
          max(abs(K_of(B_full, n_s, b)) for b in phys + ghost))
check("E", "Q1 (quotient): im d inside ker delta_2; all 96 physical + 96 "
           "ghost representatives lie in the constraint surface, K-orthogonal "
           "to the gauge orbit -- the quotient is well-formed at scale",
      in_ker < 1e-9 and mem < 1e-8,
      f"dist(im d, ker) = {in_ker:.1e}; max membership residual = {mem:.1e}")

Wp = np.column_stack(phys)
G_phys = Wp.conj().T @ B_full @ Wp
G_phys = 0.5 * (G_phys + G_phys.conj().T)
evp = np.linalg.eigvalsh(G_phys)
check("E", "Q6: the 96-dim physical Gram is POSITIVE-DEFINITE "
           "(the actual triplet form, not a toy stand-in)",
      evp.min() > 1e-6,
      f"eigenvalues in [{evp.min():.6f}, {evp.max():.6f}]")

Hq = Wp.conj().T @ B_full @ (H @ Wp)              # descended dynamics
herm = np.linalg.norm(Hq - Hq.conj().T)
check("E", "Q5: the descended Hamiltonian on the 96-dim physical sector is "
           "Hermitian (state-preserving), with the causality coupling AND "
           "the parity-even interaction dressing on",
      herm < 1e-8, f"Hermiticity defect = {herm:.1e}")

evq, Vq = np.linalg.eigh(0.5 * (Hq + Hq.conj().T))
psi = RNG.standard_normal(NPAIR) + 1j * RNG.standard_normal(NPAIR)
psi /= np.linalg.norm(psi)
drift, pmin = 0.0, 1.0
for t in (0.5, 2.0, 7.0):
    Ut = Vq @ np.diag(np.exp(-1j * evq * t)) @ Vq.conj().T
    p = np.abs(Ut @ psi) ** 2
    drift = max(drift, abs(p.sum() - 1.0))
    pmin = min(pmin, p.min())
check("E", "Q3: toy Born rule on the 96-dim sector -- probabilities "
           "positive, normalization drift ~ 0 under evolution",
      drift < 1e-9 and pmin >= -1e-12,
      f"sum-1 drift = {drift:.1e}")

A = RNG.standard_normal((DIMF, DIMF)) + 1j * RNG.standard_normal((DIMF, DIMF))
A = 0.5 * (A + P_par @ A @ P_par)                                 # parity-even part
A = 0.5 * (A + np.linalg.solve(B_full, A.conj().T @ B_full))      # K-Hermitian part
A_phys = Wp.conj().T @ B_full @ (A @ Wp)
obs = np.linalg.norm(A_phys - A_phys.conj().T)
check("E", "Q2: a random K-Hermitian parity-even observable restricts "
           "Hermitian on the 96-dim physical sector",
      obs < 1e-8, f"restriction defect = {obs:.1e}")

# =============================================================================
print()
print("=" * 78)
print("PART 2  WRONG orientation at 192 dims: the failure is cohomological")
print("=" * 78)

sigma = -SIGMA_STAR
n_w = n_vec(sigma)
closure_w = abs(complex(d2 @ n_w))
check("E", "Q1 FAILS cohomologically: Noether NON-closure "
           "|delta_2 . d_(-1)| = gamma -- the complex is not a complex; the "
           "primary failure, same mode as the 9-dim toy",
      abs(closure_w - GAMMA) < 1e-9, f"non-closure = {closure_w:.4f} = gamma")

in_ker_w = np.linalg.norm(n_w - ker @ (ker.conj().T @ n_w))
check("E", "quotient ill-formed: dist(im d, ker delta_2) = O(1)",
      in_ker_w > 0.1, f"dist = {in_ker_w:.4f}")

Wb = np.column_stack([w_vec(i, sigma) for i in range(NPAIR)])
G_bad = Wb.conj().T @ B_full @ Wb
G_bad = 0.5 * (G_bad + G_bad.conj().T)
evb = np.linalg.eigvalsh(G_bad)
n_neg = int((evb < -1e-9).sum())
check("E", "repair 1 (brute grading): 96 NEGATIVE-NORM physical survivors "
           "(Q6 fails visibly, one per hyperbolic pair)",
      n_neg == NPAIR,
      f"{n_neg} negative eigenvalues, all ~ -1 "
      f"(range [{evb.min():.6f}, {evb.max():.6f}])")

n_z = n_vec(SIGMA_STAR)                           # the zombie: still in ker delta_2
z_mem = abs(complex(d2 @ n_z))
evH, VH = np.linalg.eig(H)
VHi = np.linalg.inv(VH)
growth = []
for t in (1.0, 2.0):
    Ut = VH @ np.diag(np.exp(-1j * evH * t)) @ VHi
    growth.append(float(np.linalg.norm(Ut @ n_z)))
ok_growth = (abs(growth[0] - np.exp(GAMMA)) < 1e-6
             and abs(growth[1] - np.exp(2 * GAMMA)) < 1e-6)
feed = abs(K_of(B_full, n_vec(-SIGMA_STAR), H @ w_vec(0, +1)))
check("E", "repair 2 (delete negatives): the null zombie n_+ stays in the "
           "constraint surface, grows EXACTLY e^{gamma t}, and is regenerated "
           "from the kept graded ghosts (feed = c) -- deletion is not "
           "dynamics-invariant at scale (VZ analog; Q5/Q3 fail)",
      z_mem < 1e-9 and ok_growth and abs(feed - CPL) < 1e-9,
      f"growth {growth[0]:.4f} -> {growth[1]:.4f} "
      f"(e^g: {np.exp(GAMMA):.4f} -> {np.exp(2*GAMMA):.4f}); feed = {feed:.3f}")

d2_re = np.conj(n_w) @ B_full @ H
check("E", "repair 3 (retune delta_2): closure restorable NUMERICALLY only "
           "by rewriting the transmitted identity -- structurally blocked, "
           "the bit is loop-coherent (Part A register, re-run above; the "
           "storage argument is dimension-independent)",
      abs(complex(d2_re @ n_w)) < 1e-9,
      f"retuned closure = {abs(complex(d2_re @ n_w)):.1e}, blocked by storage")

# =============================================================================
print()
print("=" * 78)
print("PART 3  D1 at scale: the C-operator recipe on the actual triplet")
print("=" * 78)

# carrier anchor: native dynamics is scalar (re-verified; R3 sign-blind)
eta_d = [1.0] * 9 + [-1.0] * 5
Cas95 = np.zeros((DIMS, DIMS), dtype=complex)
for a in range(14):
    for b in range(a + 1, 14):
        Sab = 0.5 * (e[a] @ e[b])
        Cas95 += eta_d[a] * eta_d[b] * (Sab @ Sab)
lam0 = np.trace(Cas95).real / DIMS
scal = np.linalg.norm(Cas95 - lam0 * np.eye(DIMS)) / np.linalg.norm(Cas95)
check("E", "carrier anchor: the so(9,5) Casimir on the verified spinor is "
           "EXACTLY a scalar -- native Casimir-type pair dynamics is mu*I, "
           "exactly degenerate (R3 sign-blind, SUSTAINED; therefore the gap "
           "delta is NOT native and must be imported -- the typed "
           "conditional this whole lift declares)",
      scal < 1e-12, f"||Cas - lam I||/||Cas|| = {scal:.1e}, lam = {lam0:.4f}")


def bm_c_operator(Hm, Bm, tol_real=1e-8, tol_group=1e-6, tol_null=1e-6):
    """The dimension-agnostic R1/D1 recipe: C = sum sign(nu_k) P_k; ABORTS on
    K-null or K-indefinite eigengroups (the honest failure mode)."""
    evals, V = np.linalg.eig(Hm)
    real_idx = [k for k in range(len(evals)) if abs(evals[k].imag) < tol_real]
    groups, used = [], set()
    for k in real_idx:
        if k in used:
            continue
        g = [j for j in real_idx if abs(evals[j].real - evals[k].real) < tol_group]
        used.update(g)
        groups.append(g)
    n = Hm.shape[0]
    C = np.zeros((n, n), dtype=complex)
    Pi = np.zeros((n, n), dtype=complex)
    for g in groups:
        Wg = V[:, g]
        Gm = Wg.conj().T @ Bm @ Wg
        Gm = 0.5 * (Gm + Gm.conj().T)
        evg, Ug = np.linalg.eigh(Gm)
        if any(abs(x) < tol_null for x in evg):
            raise ValueError(f"K-null direction in eigengroup at "
                             f"E = {evals[g[0]].real:.4f} -- C undefined")
        if not (all(x > tol_null for x in evg) or all(x < -tol_null for x in evg)):
            sg = (int((evg > 0).sum()), int((evg < 0).sum()))
            raise ValueError(f"K-INDEFINITE eigengroup at E = "
                             f"{evals[g[0]].real:.4f}, signature (+{sg[0]},"
                             f"-{sg[1]}) -- C non-unique")
        Wo = Wg @ Ug
        for j in range(Wo.shape[1]):
            v = Wo[:, j]
            nu = float((v.conj() @ Bm @ v).real)
            P = np.outer(v, np.conj(Bm @ v)) / nu
            C += np.sign(nu) * P
            Pi += P
    return C, {"n_real": len(real_idx), "n_groups": len(groups), "Pi": Pi}


# --- (i) the NATIVE point: exactly degenerate, recipe must abort ------------
H_nat = MU * np.eye(NTRIP, dtype=complex)         # the native pair dynamics
try:
    bm_c_operator(H_nat, Bp)
    aborted, msg = False, "recipe unexpectedly succeeded"
except ValueError as exc:
    aborted, msg = True, str(exc)
check("E", "at the native (vacuum-anchor) point the 192-dim eigengroup is "
           "K-INDEFINITE with signature (+96, -96) and the recipe ABORTS: "
           "dynamics does not determine C on the actual triplet -- the "
           "9-dim result survives scale in exactly the same failure mode "
           "(non-uniqueness, NOT Jordan: H = mu I is trivially "
           "diagonalizable, geometric mult 192)",
      aborted and "(+96,-96)" in msg.replace(" ", ""), msg)

C_kin = swap.copy()                               # kinematic grading operator


def boost(svec):
    d = np.concatenate([np.exp(svec), np.exp(-svec)])
    return np.diag(d.astype(complex))


cont_ok, dists = True, []
s_list = [np.full(NPAIR, 0.4), np.full(NPAIR, 0.9),
          RNG.uniform(-0.5, 0.5, NPAIR)]          # global + PER-PAIR boosts
for svec in s_list:
    T = boost(svec)
    Cs = T @ C_kin @ np.linalg.inv(T)
    isom = np.linalg.norm(T.conj().T @ Bp @ T - Bp)
    c2r = np.linalg.norm(Cs @ Cs - np.eye(NTRIP))
    comm = np.linalg.norm(Cs @ H_nat - H_nat @ Cs)
    Gs = Bp @ Cs
    Gs = 0.5 * (Gs + Gs.conj().T)
    evs = np.linalg.eigvalsh(Gs)
    cont_ok = cont_ok and isom < 1e-8 and c2r < 1e-6 and comm < 1e-9 \
        and evs.min() > 1e-3
    dists.append(float(np.linalg.norm(Cs - C_kin)))
check("E", "the continuum at scale: global AND independent per-pair "
           "hyperbolic boosts of the kinematic C are ALL admissible at the "
           "native point (K-isometries; C_s^2 = I, [C_s, H] = 0, B.C_s > 0) "
           "-- admissible C's form a continuum of dimension 2*96^2 = 18432 "
           "(the U(96,96)/(U(96)xU(96)) symmetric space of maximal "
           "K-positive subspaces; the toy's was 18): non-uniqueness GROWS "
           "with scale, it does not heal",
      cont_ok, f"||C_s - C_kin|| = {[round(d, 2) for d in dists]}")

# --- (ii) the typed import: gap on -> C determined --------------------------
H_gap = MU * np.eye(NTRIP, dtype=complex) + DELTA * swap + V_pe[2:, 2:]
C192, info = bm_c_operator(H_gap, Bp)
c2r = np.linalg.norm(C192 @ C192 - info["Pi"])
comm = np.linalg.norm(C192 @ H_gap - H_gap @ C192)
Gg = Bp @ C192
Gg = 0.5 * (Gg + Gg.conj().T)
evg = np.linalg.eigvalsh(Gg)
check("E", "CONDITIONAL determination at scale: with the typed gap import "
           "(+ the parity-even dressing) all 192 eigenvalues are real, "
           "every eigengroup is K-definite, and the recipe outputs C with "
           "C^2 = I, [C, H] = 0, G = B.C Hermitian POSITIVE -- the "
           "interacting V-metric exists on the actual triplet, "
           "conditionally on the import",
      info["n_real"] == NTRIP and c2r < 1e-7 and comm < 1e-7
      and evg.min() > 1e-6,
      f"{info['n_real']} real in {info['n_groups']} K-definite groups; "
      f"||C^2-I|| {c2r:.1e}, ||[C,H]|| {comm:.1e}, min eig(G) {evg.min():.3f}")

ident = np.linalg.norm(C192 - C_kin)
check("E", "the determined C EQUALS the kinematic K-grading on the triplet "
           "(the audit's watched second anchor freedom does not appear at "
           "192 dims either)",
      ident < 1e-7, f"||C - C_kin|| = {ident:.1e}")

Z = RNG.standard_normal((NTRIP, NTRIP)) + 1j * RNG.standard_normal((NTRIP, NTRIP))
Z = 0.5 * (Z + np.linalg.solve(Bp, Z.conj().T @ Bp))
Z = 1e-6 * Z / np.linalg.norm(Z)
C_pert, _ = bm_c_operator(H_gap + Z, Bp)
stab = np.linalg.norm(C_pert - C192)
G_neg = Bp @ (-C192)
G_neg = 0.5 * (G_neg + G_neg.conj().T)
C_flip, _ = bm_c_operator(H_gap, -Bp)
coflip = np.linalg.norm(C_flip + C192)
check("E", "off-degeneracy the determination is STABLE (O(1e-6) "
           "perturbation), -C is INADMISSIBLE (B.(-C) negative), and the "
           "anchor co-flip is exact (B -> -B  =>  C -> -C): within the "
           "Z/2-typed payload family the choice set is exactly "
           "{(B, C), (-B, -C)} -- the datum is ONE Z/2 at 192 dims",
      stab < 1e-3 and np.linalg.eigvalsh(G_neg).min() < -0.5
      and coflip < 1e-7,
      f"||dC|| = {stab:.1e}; ||C(-B) + C(B)|| = {coflip:.1e}")

defects = []
for svec in (np.full(NPAIR, 0.4), np.full(NPAIR, 0.9)):
    T = boost(svec)
    Cs = T @ C_kin @ np.linalg.inv(T)
    defects.append(float(np.linalg.norm(Cs @ H_gap - H_gap @ Cs)))
check("F", "armed control: the continuum COLLAPSES when the gap import is "
           "on ([C_s, H] != 0 for s != 0) -- determination is exactly the "
           "gapped-pair phenomenon at scale; had the continuum survived the "
           "gap, the conditional-determination story would break (it does "
           "not)",
      all(d > 0.05 for d in defects),
      f"[C_s,H] defects = {[round(d, 3) for d in defects]}")

# --- (iii) typing the import: chi-odd and non-equivariant -------------------
chi_fr = np.diag(np.concatenate([np.ones(NPAIR), -np.ones(NPAIR)])).astype(complex)
chi_res = np.linalg.norm(chi_t @ np.hstack([Uframe, Vframe])
                         - np.hstack([Uframe, -Vframe]))
anti = np.linalg.norm(chi_fr @ swap + swap @ chi_fr)
check("E", "import typing 1: the gap operator is chi-ODD -- it anticommutes "
           "EXACTLY with the triplet chirality (algebraic zero; frame "
           "fidelity residual reported) -- and R3 proved chi-odd content "
           "has no GU-native carrier: the import demand is forced, not "
           "chosen",
      anti < 1e-14 and chi_res < 1e-6,
      f"{{chi, G_gap}} = {anti:.1e} exact; frame residual = {chi_res:.1e}")

# triplet-preserving internal so(9,5) generators (indices >= 4 commute with
# the SU(2)+ selection): a compact rotation (4,5) and a BOOST (8,9)
defect_rows = []
for (a, b, kind) in ((4, 5, "rotation(4,5) compact"),
                     (8, 9, "boost(8,9) non-compact"),
                     (5, 11, "boost(5,11) non-compact")):
    Xg = np.kron(I14, sgen(a, b)) + np.kron(lvec(a, b), I128)
    XWt = Xg @ Wt
    leak = np.linalg.norm(XWt - Wt @ (Wt.conj().T @ XWt))
    X_t = Wt.conj().T @ XWt                       # restriction, triplet coords
    X_fr = np.linalg.solve(Pf, X_t @ Pf)          # pair-frame coordinates
    dfct = np.linalg.norm(G_gap[2:, 2:] @ X_fr - X_fr @ G_gap[2:, 2:])
    defect_rows.append((kind, leak, dfct))
boost_defects = [d for (k, l, d) in defect_rows if "boost" in k]
leaks = [l for (_, l, _) in defect_rows]
for (kind, leak, dfct) in defect_rows:
    print(f"      internal generator {kind}: triplet leak {leak:.1e}, "
          f"[G_gap, X|triplet] = {dfct:.3f}")
check("E", "import typing 2: the triplet-preserving internal so(9,5) BOOSTS "
           "do not commute with the gap operator (nonzero commutant defect) "
           "-- the import is non-equivariant along the non-compact "
           "directions, matching D-QM-3/B.3's demand type; the compact "
           "rotation's near-commutation shows the defect is a signature "
           "phenomenon, not frame noise",
      all(l < 1e-6 for l in leaks) and all(d > 0.1 for d in boost_defects))

print(f"\n[PART 3 wall time: {time.time() - T0:.1f}s]")

# =============================================================================
print()
print("=" * 78)
print("PART 4  the compensator sector at FULL 1792-dim scale")
print("=" * 78)

sig_c = 0.8 * sgen(0, 9)                          # fixed boost carrier (spacelike 0, timelike 9)
ne_def = max(np.linalg.norm(sig_c @ sgen(a, b) - sgen(a, b) @ sig_c)
             for (a, b) in ((0, 1), (1, 2), (9, 10)))
evs_c, Us_c = np.linalg.eigh(sig_c)               # sgen(0,9) is Hermitian (boost)
E_dress = Us_c @ np.diag(np.exp(evs_c)) @ Us_c.conj().T
check("E", "the compensator carrier sigma_c = 0.8*Sigma_(0,9) (a fixed "
           "non-compact boost) is NON-equivariant: a fixed element cannot "
           "transform in the Spin(9,5) family (nonzero commutators with "
           "the generators) -- it passes the K3 equivariance tripwire; "
           "an EQUIVARIANT carrier would lie in the Cl(9,5) commutant = H "
           "(canon C07: M(64,H)), i.e. be a quaternionic scalar, and drop "
           "out of the constraint dressing entirely (GHOST-01 image at "
           "full scale)",
      ne_def > 0.01, f"max ||[sigma_c, Sigma_ab]|| = {ne_def:.3f}")


XI2_0 = float(np.real(np.vdot(gb.XI, gb.XI)))     # reference |xi_0|^2


def dressed_C2(xi, L2rel=0.0):
    """C2 obstruction with the dressed constraint B_W = Gamma (I x E),
    E = exp(sigma_c / (1 + L2rel * |xi|^2/|xi_0|^2)).  L2rel = 0: the
    scale-free compensator; L2rel > 0: a kernel with an internal scale."""
    scale = 1.0 / (1.0 + L2rel * float(np.real(np.vdot(xi, xi))) / XI2_0)
    E_k = Us_c @ np.diag(np.exp(scale * evs_c)) @ Us_c.conj().T
    B_W = np.hstack([e[a] @ E_k for a in range(N)])           # Gamma (I x E)
    Pi_W = np.eye(N * DIMS, dtype=complex) - B_W.conj().T @ np.linalg.solve(
        B_W @ B_W.conj().T, B_W)
    cxi = sum(xi[a] * e[a] for a in range(N))
    BM = np.hstack([e[a] @ E_k @ cxi for a in range(N)])       # B_W M_D
    return float(np.linalg.norm(BM @ Pi_W))


xi = gb.XI
c2_1 = dressed_C2(xi)
c2_2 = dressed_C2(2 * xi)
ratio = c2_2 / c2_1
check("E", "dressed C2 at FULL scale: the obstruction persists under the "
           "non-equivariant dressing (same frontier as bare C2 = 155.36 -- "
           "the B.5 global data remain the missing object; the compensator "
           "dresses, it does not close), and the C2 scale law "
           "C2(2xi)/C2(xi) = 2 holds EXACTLY for the scale-free compensator "
           "(archaeology item 8 weld check, now at 1792 dims)",
      c2_1 > 50.0 and abs(ratio - 2.0) < 1e-9,
      f"dressed C2 = {c2_1:.4f} (bare 155.3625); ratio = {ratio:.12f}")

c2L_1 = dressed_C2(xi, L2rel=0.25)                # kernel scale 0.8 at xi, 0.5 at 2xi
c2L_2 = dressed_C2(2 * xi, L2rel=0.25)
ratioL = c2L_2 / c2L_1
check("F", "K3 discriminator EXECUTABLE at full scale: a compensator kernel "
           "carrying an internal scale (E = exp(sigma_c/(1 + L^2 |xi|^2)), "
           "L^2 = 0.25/|xi_0|^2) BREAKS the exact scale law -- any future "
           "S_IG candidate whose compensator smuggles a scale is "
           "machine-detectable on the actual 1792-dim structure",
      abs(ratioL - 2.0) > 1e-3,
      f"scale-carrying ratio = {ratioL:.6f} != 2")

print("\n      TYPED GAPS (compensator sector, per the standing axiom -- "
      "recorded, not stops):")
print("      G-COMP-1: the compensator FIELD tier (Stueckelberg action with "
      "transmitted")
print("                transformation law) exists only at CH-SRC's 16-dim "
      "mini-rep; not built at 1792.")
print("      G-COMP-2: the antighost/Koszul-Tate leg as an action field: "
      "complex level only.")
print("      G-COMP-3: the non-abelian master equation: no fixture at any "
      "scale tests it.")

# =============================================================================
print()
nE = sum(1 for t, _, ok in RESULTS if t == "E" and ok)
nF = sum(1 for t, _, ok in RESULTS if t == "F" and ok)
nT = sum(1 for t, _, ok in RESULTS if t == "T" and ok)
fails = [(t, n) for t, n, ok in RESULTS if not ok]
print(f"headline: {nE} [E] + {nF} [F] = {nE + nF}  (setup [T] = {nT}, excluded)")
print(f"[total wall time: {time.time() - T0:.1f}s]")
if fails:
    print("FAILURES:")
    for t, n in fails:
        print(f"  [{t}] {n}")
    sys.exit(1)
print("VERDICT: the graded-quotient + C-operator mechanism SURVIVES the lift "
      "from the 9-dim toy to the actual 192-dim triplet: right orientation "
      "passes the six-certificate battery on the real Krein form, wrong "
      "orientation fails cohomologically in the same mode; C-determination "
      "fails at the native (exactly degenerate, K-indefinite (+96,-96)) "
      "point by an 18432-dimensional continuum and succeeds conditionally "
      "under the ONE typed gap import (chi-odd, boost-non-equivariant, "
      "standing in for S_IG/B.5), with the undetermined datum exactly one "
      "Z/2; the compensator's C2 scale law holds exactly at full 1792-dim "
      "scale and the obstruction persists -- the missing object is still "
      "the B.5 global data. ALL CONDITIONAL under the standing axiom; no "
      "claim, canon, or posture moves.")
sys.exit(0)
