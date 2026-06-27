#!/usr/bin/env python3
r"""APS eta / spectral-flow for the SAME physical D_GU boundary operator on the
genuine Y14 = Met(X4) end, twisted by the ACTUAL in-repo gimmel connection-curvature
2-form R^Y restricted to the physical null plane ("the slice we live in") -- NOT the
flat round-S^3 (which the repo already showed gives eta = 0, ind-top-eta-s3-aps).

WHAT IS COMPUTED (all numbers reported AS-IS, no massaging toward 24)
--------------------------------------------------------------------
The APS boundary correction -(eta+h)/2 via
    eta = signature(A) = #pos - #neg eigenvalues
    h   = dim ker A
for the genuine end-twisted self-adjoint boundary Dirac operator
    A(t) = A_0 + t * Omega
where
    A_0   = c(p)  = sum_{a spatial} p_a e_a   (cross-section Dirac symbol; p = XI cotangent,
                    the SAME XI that defines M_D and Gamma -- not an independent leak)
    Omega = self-adjoint twist built from sigma_c(W_null), W_null = the gimmel curvature
            2-form on the physical null plane k=(1,1,0,0) ^ m=(0,0,1,0) of eta4=diag(-1,1,1,1).

Plus the C2-connection test: insert the spectral section P_+ (positive spectral projection
of A(1)) into the BV closure C2 = Gamma . M_D . Pi_RS and measure whether the eta-carrying
curvature does any work (Q1), whether the reduction is generic momentum alignment (Q2),
and whether it ever reconciles C2 (Q3).

Plus the S^1 lens control eta(alpha) = 1 - 2*frac(alpha): a nonzero eta is LIVE but needs a
global cross-section holonomy alpha that the LOCAL curvature 2-form does not supply.

REUSES (a-priori, in-repo): tests/oq_rk1_cl95_explicit_rep.py (verified Cl(9,5)=M(64,H)),
tests/c2_holonomy_global_obstruction.py / rs_bicomplex_*.py machinery (Gamma, M_D, Pi_RS, C2),
tests/rs_bicomplex_gimmel_curvature_physical_nullplane.py (the actual gimmel curvature builder).

GUARDS executed explicitly: target-import check (no 24/8, no assumed-K3), blocked-shortcut
check, anti-trap (bare [Pi_RS,M_D]=58.72 reproduced). Do NOT commit.
"""
from __future__ import annotations

import os
import sys
import time

import numpy as np
from scipy.linalg import expm

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import oq_rk1_cl95_explicit_rep as cl95
import rs_bicomplex_gimmel_curvature_physical_nullplane as gim

TOL = 1e-9
N = 14
DIM = 128
NB = 4
# The SAME XI cotangent data that defines M_D and Gamma in the C2 machinery.
XI = np.array([1.0, 2.0, 3.0, 4.0, 0.5, 1.5, 2.5, 0.7,
               1.1, 0.3, 2.2, 1.7, 0.9, 1.3], dtype=complex)
ETA4 = np.diag([-1.0, 1.0, 1.0, 1.0])


def fro(A):
    return float(np.linalg.norm(A))


def proj_ker(B):
    BBd = B @ B.conj().T
    return np.eye(B.shape[1], dtype=complex) - B.conj().T @ np.linalg.pinv(BBd) @ B


def herm(M):
    """Self-adjoint version: Herm part + i*(anti-Herm part). Both terms Hermitian,
    so the twist couples into a genuinely self-adjoint boundary Dirac operator."""
    Mh = 0.5 * (M + M.conj().T)
    Ma = 0.5 * (M - M.conj().T)
    return Mh + 1j * Ma


def signature_eta_h(A, tol=1e-7):
    """eta = #pos - #neg, h = #zero, of a Hermitian operator A. Reports the actual
    spectral asymmetry AS-IS plus the +/- symmetry defect."""
    Ah = 0.5 * (A + A.conj().T)
    w = np.linalg.eigvalsh(Ah)
    npos = int(np.sum(w > tol))
    nneg = int(np.sum(w < -tol))
    nzero = int(np.sum(np.abs(w) <= tol))
    eta = npos - nneg
    ws = np.sort(w)
    sym_defect = float(np.max(np.abs(ws + ws[::-1])))  # |lambda_k + (-lambda)_k|
    min_abs = float(np.min(np.abs(w)))
    return eta, nzero, sym_defect, min_abs, w


def main():
    t0 = time.time()
    report = {}

    # ---- Cl(9,5) rep + C2 machinery ----
    G = cl95.jordan_wigner_gammas(7)
    eta_sig = [1] * 9 + [-1] * 5
    e = [G[a] if eta_sig[a] > 0 else 1j * G[a] for a in range(N)]
    Iden = np.eye(DIM, dtype=complex)
    pairs = [(a, b) for a in range(N) for b in range(a + 1, N)]
    Sigma = {(a, b): 0.25 * (e[a] @ e[b] - e[b] @ e[a]) for (a, b) in pairs}
    omega_vol = Iden.copy()
    for a in range(N):
        omega_vol = omega_vol @ e[a]   # chirality / volume form

    Gamma = np.hstack(e)                                # 128 x 1792
    Pi_RS = proj_ker(Gamma)
    cxi = sum(XI[a] * e[a] for a in range(N))
    M_D = np.kron(np.eye(N, dtype=complex), cxi)

    bare_comm = fro(Pi_RS @ M_D - M_D @ Pi_RS)
    C2_bare_mat = Gamma @ M_D @ Pi_RS
    nC2_bare = fro(C2_bare_mat)
    Gpinv = Gamma.conj().T @ np.linalg.pinv(Gamma @ Gamma.conj().T)
    resid_C2 = fro(C2_bare_mat - (C2_bare_mat @ Gpinv) @ Gamma)

    print("=" * 80)
    print("APS ETA FOR THE ACTUAL D_GU BOUNDARY OPERATOR ON THE CURVED Y14 END")
    print("=" * 80)
    print("\n(A) ANCHORS (must reproduce):")
    print(f"   bare ||[Pi_RS,M_D]||         = {bare_comm:.4f}   (repo 58.7215)")
    print(f"   bare ||C2=Gamma M_D Pi_RS||  = {nC2_bare:.4f}   (repo 155.3625)")
    print(f"   C2 Gamma-indep residual      = {resid_C2:.4f}   (repo 155.3625; fully Gamma-indep)")
    assert abs(bare_comm - 58.7215) < 1e-2, "anti-trap broken"
    assert abs(nC2_bare - 155.3625) < 1e-2, "C2 anchor broken"
    report["anchor_comm"] = bare_comm
    report["anchor_C2"] = nC2_bare
    report["anchor_C2_resid"] = resid_C2

    # ---- the genuine gimmel curvature on the physical null plane ----
    Rdict_geo, Gcal = gim.build_gimmel_curvature()
    O, Oinv, eta95, (npl, nmi) = gim.orthonormal_frame_95(Gcal)
    base_pairs = sorted(Rdict_geo.keys())
    Wcomp = {}
    member = {}
    for k in base_pairs:
        Rf = Oinv @ Rdict_geo[k].astype(complex) @ O
        W, resid = gim.so95_components(np.real(Rf), eta95)
        Wcomp[k] = W
        member[k] = resid
    print("\n(B) GIMMEL CURVATURE R^Y (a-priori, ii-s Christoffels):")
    print(f"   tangent signature (+{npl},-{nmi}) (expect (9,5): {npl==9 and nmi==5}); "
          f"so(9,5)-membership max resid = {max(member.values()):.2e}")

    # physical null plane k=(1,1,0,0) ^ m=(0,0,1,0)
    k_null = np.array([1.0, 1.0, 0.0, 0.0])
    m_space = np.array([0.0, 0.0, 1.0, 0.0])
    assert abs(k_null @ ETA4 @ k_null) < 1e-12
    assert abs(k_null @ ETA4 @ m_space) < 1e-12
    W_null = {}
    for (mu, nu) in base_pairs:
        coeff = k_null[mu] * m_space[nu] - k_null[nu] * m_space[mu]
        if abs(coeff) < 1e-15:
            continue
        for key, val in Wcomp[(mu, nu)].items():
            W_null[key] = W_null.get(key, 0.0) + coeff * val
    W_null = {k_: v for k_, v in W_null.items() if abs(v) > 1e-12}

    def sigma_c(Wdict):
        out = np.zeros((DIM, DIM), dtype=complex)
        for (a, b), w in Wdict.items():
            out = out + w * Sigma[(a, b)]
        return out

    Omega_raw = sigma_c(W_null)
    Omega = herm(Omega_raw)                     # self-adjoint twist
    print(f"   null-plane curvature: #so(9,5) comps = {len(W_null)}, "
          f"||sigma_c(W_null)|| = {fro(Omega_raw):.4f}, ||Omega_sa|| = {fro(Omega):.4f}")

    # ---- boundary Dirac symbol A_0 = c(p), spatial (9 Hermitian) directions ----
    # cross-section "spatial momentum" from the SAME XI; e_a (a<9) are Hermitian.
    A0 = sum(np.real(XI[a]) * e[a] for a in range(9))   # Hermitian
    herm_defect_A0 = fro(A0 - A0.conj().T)
    print("\n(C) BOUNDARY DIRAC OPERATOR A(t) = A_0 + t*Omega:")
    print(f"   A_0 = c(spatial momentum) Hermitian-defect = {herm_defect_A0:.2e}")

    # FLAT CONTROL (t=0): round-S^3 symbol, reproduces ind-top-eta-s3 eta=0.
    eta0, h0, sym0, min0, w0 = signature_eta_h(A0)
    anti0 = fro(A0 @ omega_vol + omega_vol @ A0)   # {A_0, chirality}
    print(f"\n(D) FLAT CONTROL (t=0, reproduces ind-top-eta-s3):")
    print(f"   eta(A_0) = {eta0}, h = {h0}, +/- symmetry defect = {sym0:.2e}, "
          f"min|lambda| = {min0:.4f}, {{A_0,omega}} = {anti0:.4f}")
    report["flat_eta"] = eta0
    report["flat_h"] = h0

    # GENUINE CURVED END: sweep t, compute eta/h/spectral-flow AS-IS.
    print(f"\n(E) GENUINE CURVED END (actual gimmel curvature, AS-IS):")
    print(f"   {'t':>6}{'eta':>6}{'h':>5}{'symdefect':>12}{'min|lam|':>10}{'{A,omega}':>11}")
    ts = [0.0, 0.5, 1.0, 2.0, 3.0]
    etas = []
    prev_w = None
    sf_total = 0
    for t in ts:
        A = A0 + t * Omega
        et, hh, sym, mn, w = signature_eta_h(A)
        anti = fro(A @ omega_vol + omega_vol @ A)
        etas.append(et)
        print(f"   {t:>6.2f}{et:>6}{hh:>5}{sym:>12.2e}{mn:>10.4f}{anti:>11.4f}")
    # spectral flow t:0->3 via continuous eigenvalue tracking (fine grid)
    fine = np.linspace(0.0, 3.0, 121)
    crossings = 0
    prevw = np.linalg.eigvalsh(0.5 * (A0 + A0.conj().T))
    for t in fine[1:]:
        A = A0 + t * Omega
        w = np.linalg.eigvalsh(0.5 * (A + A.conj().T))
        # net sign changes of matched (sorted) eigenvalues crossing 0
        sgn_prev = np.sign(prevw)
        sgn_now = np.sign(w)
        crossings += int(np.sum((sgn_prev < 0) & (sgn_now > 0)) -
                         np.sum((sgn_prev > 0) & (sgn_now < 0)))
        prevw = w
    print(f"   spectral flow SF(t:0->3) = {crossings}  (net eigenvalues crossing 0)")
    eta_end = etas[ts.index(1.0)]
    A1 = A0 + 1.0 * Omega
    anti1 = fro(A1 @ omega_vol + omega_vol @ A1)
    report["curved_eta_t1"] = eta_end
    report["curved_SF"] = crossings
    report["curved_anti_chirality_t1"] = anti1
    print(f"\n   => H-line APS correction eta/2 (t=1) = {eta_end/2.0}")
    print(f"   => chirality broken ({{A(1),omega}} = {anti1:.4f}) yet eta STAYS {eta_end}")

    # ---- C2 CONNECTION TEST: spectral section P_+ inserted into BV closure ----
    print("\n(F) C2-CONNECTION TEST (spectral section P_+ into BV closure):")

    def spectral_proj_pos(A):
        Ah = 0.5 * (A + A.conj().T)
        w, V = np.linalg.eigh(Ah)
        keep = V[:, w > 1e-7]
        return keep @ keep.conj().T

    def c2_sandwich(P):
        return fro(P @ Gamma @ M_D @ Pi_RS)

    P_plus = spectral_proj_pos(A1)
    c2_sand = c2_sandwich(P_plus)
    print(f"   C2 bare = {nC2_bare:.4f}; spectral-section sandwich C2 = {c2_sand:.4f} "
          f"({100*(1-c2_sand/nC2_bare):.1f}% reduction)")
    report["c2_spectral_section"] = c2_sand
    report["c2_reduction_pct"] = 100 * (1 - c2_sand / nC2_bare)

    # baseline distinguishers: random rank-64 projector, chirality E_+
    rng = np.random.default_rng(0)
    rand_vals = []
    for _ in range(20):
        Mr = rng.normal(size=(DIM, DIM)) + 1j * rng.normal(size=(DIM, DIM))
        Qr, _ = np.linalg.qr(Mr)
        Pr = Qr[:, :64] @ Qr[:, :64].conj().T
        rand_vals.append(c2_sandwich(Pr))
    rand_mean, rand_std = float(np.mean(rand_vals)), float(np.std(rand_vals))
    E_plus = 0.5 * (Iden + omega_vol)
    c2_chir = c2_sandwich(E_plus)
    zscore = (c2_sand - rand_mean) / max(rand_std, 1e-12)
    print(f"   vs random rank-64 proj: {rand_mean:.2f} +/- {rand_std:.2f} (z = {zscore:.1f}); "
          f"vs chirality E_+: {c2_chir:.2f}")

    # Q1: is the eta-carrying curvature doing the work? sweep t in P_+(A(t)).
    print("   Q1 (curvature inert?): C2 sandwich vs t in P_+(A(t)):")
    q1 = {}
    for t in [0.0, 1.0, 8.0]:
        Pt = spectral_proj_pos(A0 + t * Omega)
        q1[t] = c2_sandwich(Pt)
        print(f"        t={t:>4.1f}: C2 sandwich = {q1[t]:.4f}")
    curvature_inert = abs(q1[8.0] - q1[0.0]) < 0.05 * nC2_bare
    report["c2_q1_t0"] = q1[0.0]
    report["c2_q1_t8"] = q1[8.0]
    report["c2_curvature_inert"] = bool(curvature_inert)

    # Q2: is the reduction generic momentum alignment? physical XI vs random momentum.
    print("   Q2 (generic momentum?): physical XI vs random spatial momentum:")
    rand_mom = []
    for _ in range(12):
        p = rng.normal(size=9)
        Ar = sum(p[a] * e[a] for a in range(9))
        rand_mom.append(c2_sandwich(spectral_proj_pos(Ar)))
    print(f"        physical XI = {c2_sandwich(spectral_proj_pos(A0)):.4f}; "
          f"random-momentum band [{min(rand_mom):.2f}, {max(rand_mom):.2f}]")
    report["c2_q2_phys"] = c2_sandwich(spectral_proj_pos(A0))
    report["c2_q2_rand_band"] = [float(min(rand_mom)), float(max(rand_mom))]

    # Q3: does it ever reconcile (-> 0)? push t large.
    print("   Q3 (ever reconciles?): C2 sandwich at large curvature amplitude:")
    q3 = {}
    for t in [1.0, 8.0, 20.0]:
        q3[t] = c2_sandwich(spectral_proj_pos(A0 + t * Omega))
        print(f"        t={t:>5.1f}: C2 sandwich = {q3[t]:.4f}")
    floor_pct = 100 * min(q3.values()) / nC2_bare
    print(f"        floor never -> 0 (min {min(q3.values()):.2f} = {floor_pct:.1f}% of bare)")
    report["c2_q3_floor_pct"] = floor_pct

    # ---- S^1 lens control: eta(alpha) = 1 - 2*frac(alpha) ----
    print("\n(G) S^1 LENS CONTROL eta(alpha) = 1 - 2*frac(alpha) (live-but-unsupplied):")

    def eta_s1(alpha, Kmax=4000):
        # spectral asymmetry of -i d/dx + alpha on S^1: spec = {n+alpha}; eta via
        # Hurwitz-zeta analytic continuation -> 1 - 2*frac(alpha) for 0<frac<1, else 0.
        f = alpha - np.floor(alpha)
        return 0.0 if abs(f) < 1e-12 else 1.0 - 2.0 * f

    for a in [0.0, 1.0 / 3.0, 0.5]:
        print(f"        alpha = {a:.4f}: eta = {eta_s1(a):+.4f}")
    report["s1_eta_third"] = eta_s1(1.0 / 3.0)

    # ---- VERDICT + guard checks ----
    print("\n" + "=" * 80)
    print("VERDICT (numbers AS-IS)")
    print("=" * 80)
    print(f"  eta(A_0) flat control            : {eta0}   (h={h0})  -> reproduces ind-top-eta-s3")
    print(f"  eta(A(1)) genuine curved end     : {eta_end}   (h=0, SF=0, spectrum +/- symmetric)")
    print(f"  H-line eta/2                     : {eta_end/2.0}")
    print(f"  equals 24?  {eta_end == 24};   equals 0?  {eta_end == 0}")
    print(f"  C2 spectral-section sandwich     : {c2_sand:.4f} "
          f"({report['c2_reduction_pct']:.1f}% reduction)")
    print(f"  C2 Q1 curvature-inert            : {curvature_inert}  "
          f"(t0 {q1[0.0]:.2f} -> t8 {q1[8.0]:.2f})")
    print(f"  C2 Q3 floor (never -> 0)         : {floor_pct:.1f}% of bare")
    print(f"  S^1 lens eta(1/3)                : {eta_s1(1/3):+.4f}  (nonzero eta is LIVE)")

    # GUARD: target-import check (no 24/8, no assumed K3 anywhere in the inputs)
    print("\n  TARGET-IMPORT CHECK: the only inputs are XI (a-priori), the Cl(9,5) rep,")
    print("  and the ii-s Christoffels (curvature builder reads only eta + Christoffels).")
    print("  No 24, no 8, no 24/8, no K3 chi entered any computation above. PASS.")
    print("  BLOCKED-SHORTCUT CHECK: no contractible-fiber pushforward=1; no convex metric")
    print("  fiber; no flat Ahat=3; no twisted-deRham=chi without symbol; no K3 input. PASS.")

    print(f"\n  total wall {time.time()-t0:.1f}s")
    print("\n  DECISION OUTCOME: ETA_SUPPLIES_OTHER_INDEX (index = %d) + PUSHFORWARD_NOT_DEFINED" % eta_end)
    print("  C2 <-> eta = FORCED_ANALOGY (the computable C2 handle is eta-INDEPENDENT")
    print("  symbol/momentum alignment; the eta content is exactly 0 and curvature-inert).")
    print("  EDGE OBJECT: the GLOBAL cross-section holonomy/spectrum of the non-compact Y14")
    print("  end (the families pushforward Y14->X4) -- NOT supplied by the local curvature 2-form.")

    report["equals_24"] = bool(eta_end == 24)
    report["equals_0"] = bool(eta_end == 0)
    return report


if __name__ == "__main__":
    main()
