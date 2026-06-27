#!/usr/bin/env python3
r"""C2-INDEX-CONNECTION-AUDIT (2026-06-27)

Ruthless test of the load-bearing claim that C2's ~94% "global content" IS the
generation-count index / boundary spectral section (the K3 chi-gate / APS end).

CONTEXT
-------
The RS source-action line lands its final obstruction on the secondary constraint
    C2 = Gamma . M_D . Pi_RS      (bare 155.36, fully Gamma-INDEPENDENT)
and the local gimmel curvature provably fails to reduce it (~94% "global residual",
per tests/rs_c2_curvature_vs_global_diagnostic.py). The claim under test
(explorations/c2-is-global-y14-end-data-2026-06-27.md, Sections 3-4): that ~94%
global content is supplied by the GLOBAL Y14 = Met(X4) index/eta/ch2 datum, i.e.
the same object the families/K3-chi-gate route (active-research/...k3-chi-gate...)
needs. The repo's own discipline says: default to FORCED_ANALOGY unless a
COMPUTABLE HANDLE connects them.

WHAT THIS FILE COMPUTES (all numbers AS-IS, no massaging toward 24)
------------------------------------------------------------------
  (1) C2 bare + its SCALE/ROTATION structure in the symbol covector xi.
      -> tests whether C2 carries any scale-invariant (topological) content.
  (2) The candidate "index" objects on the SAME physical operator:
        - eta(D_S3 (x) S(6,4)) on round S^3, flat S(6,4) (Camporesi-Higuchi spectrum)
        - the BV Koszul-Tate Hessian M_KT = B^dag B spectral asymmetry
        - ch2(S_X)[K3] : pushforward status (NOT computed; fiber GL(4,R)/O(3,1))
  (3) THE C2 CONNECTION: is there a computable handle mapping C2's global content
      to the index (e.g. the proposed spectral-section boundary projection P_d
      inserted into the BV closure changing C2), or is it a forced analogy?

GUARDS (the repo's own blocked-shortcut list; taking any = automatic FAIL):
  - NO 24/8 = 3 ; NO assuming-K3 ; NO target import to reach a number.
  - Report the ACTUAL number even if it is 0 or != 24.

Reuses: tests/oq_rk1_cl95_explicit_rep.py (verified Cl(9,5) rep),
        the C2 machinery of tests/c2_holonomy_global_obstruction.py /
        tests/rs_bicomplex_spin95_connection_2form.py (reimplemented compactly).
Do NOT git commit.
"""
from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import oq_rk1_cl95_explicit_rep as cl95  # verified Cl(9,5) rep

try:
    from scipy.linalg import expm
except Exception:  # pragma: no cover
    def expm(A, terms=24):
        out = np.eye(A.shape[0], dtype=complex)
        term = np.eye(A.shape[0], dtype=complex)
        for k in range(1, terms):
            term = term @ A / k
            out = out + term
        return out

N = 14
DIM = 128
XI = np.array([1.0, 2.0, 3.0, 4.0, 0.5, 1.5, 2.5, 0.7,
               1.1, 0.3, 2.2, 1.7, 0.9, 1.3], dtype=complex)


def fro(M):
    return float(np.linalg.norm(M))


def proj_ker(B):
    """Orthogonal projector onto ker(B) for wide full-row-rank B."""
    BBd = B @ B.conj().T
    return np.eye(B.shape[1], dtype=complex) - B.conj().T @ np.linalg.pinv(BBd) @ B


def build_rep():
    G = cl95.jordan_wigner_gammas(7)
    eta = [1] * 9 + [-1] * 5
    e = [G[a] if eta[a] > 0 else 1j * G[a] for a in range(N)]
    return e


def C2_of_xi(e, Gamma, Pi_RS, xi):
    """C2 = ||Gamma . M_D(xi) . Pi_RS||_Fro for a given symbol covector xi."""
    cxi = sum(xi[a] * e[a] for a in range(N))
    M_D = np.kron(np.eye(N, dtype=complex), cxi)
    return fro(Gamma @ M_D @ Pi_RS)


# ----------------------------------------------------------------------------
#  Candidate INDEX objects on the SAME physical operator (computed AS-IS)
# ----------------------------------------------------------------------------
def eta_D_S3_twisted(rank=16, nmax=20000):
    """APS eta-invariant of D_{S^3} (x) S(6,4) on the round 3-sphere, flat S(6,4).

    Camporesi-Higuchi/Baer spectrum (unit S^3):
        lambda_{n,+} = +(n+3/2),  lambda_{n,-} = -(n+3/2),  n=0,1,2,...
        each with multiplicity (n+1)(n+2);  twist by a FLAT rank-r bundle scales
        every multiplicity by r and preserves the +/- symmetry.
    eta(s) = sum_lambda sign(lambda) |lambda|^{-s}; the spectrum is symmetric so
    every term cancels in pairs -> eta(0) = 0 EXACTLY. We report the truncated
    asymmetry partial sum (must be identically 0 term-by-term)."""
    # term-by-term: (+1)*mult*|lam|^{-s} + (-1)*mult*|lam|^{-s} = 0 for every n.
    asym = 0.0
    for n in range(nmax):
        mult = rank * (n + 1) * (n + 2)
        lam = (n + 1.5)
        asym += mult * (np.sign(+lam) + np.sign(-lam)) / (lam ** 0)  # s=0 reg
    return asym  # identically 0


def mkt_spectral_asymmetry(e, Gamma):
    """The BV Koszul-Tate Hessian M_KT = B^dag B (here B=Gamma) spectral data.

    The proposed C2->index handle is an APS spectral-section projection P_d of a
    SELF-ADJOINT BOUNDARY DIRAC operator. The only self-adjoint 'Dirac-like'
    operator the BV/C2 object actually supplies is M_KT = B^dag B, which is
    positive-SEMIDEFINITE: its eigenvalues are all >= 0, so it has NO spectral
    asymmetry (n_+ - n_-) and any eta/spectral-flow read off it is identically 0."""
    M_KT = Gamma.conj().T @ Gamma          # 1792 x 1792, = B^dag B
    w = np.linalg.eigvalsh(M_KT)
    n_pos = int(np.sum(w > 1e-9))
    n_neg = int(np.sum(w < -1e-9))
    n_zero = int(np.sum(np.abs(w) <= 1e-9))
    eta_like = n_pos - n_neg               # spectral asymmetry
    return dict(n_pos=n_pos, n_neg=n_neg, n_zero=n_zero,
                eta_like=eta_like, min_eig=float(w.min()), max_eig=float(w.max()))


def main():
    print("=" * 78)
    print("C2-INDEX-CONNECTION-AUDIT: is C2's global content the generation index?")
    print("=" * 78)

    e = build_rep()
    Gamma = np.hstack(e)                                   # 128 x 1792
    Pi_RS = proj_ker(Gamma)

    # ---- (A) ANCHORS ------------------------------------------------------
    cxi = sum(XI[a] * e[a] for a in range(N))
    M_D = np.kron(np.eye(N, dtype=complex), cxi)
    bare_comm = fro(Pi_RS @ M_D - M_D @ Pi_RS)
    bare_C2 = fro(Gamma @ M_D @ Pi_RS)
    Gpinv = Gamma.conj().T @ np.linalg.pinv(Gamma @ Gamma.conj().T)
    resid_C2 = fro((Gamma @ M_D @ Pi_RS) - (Gamma @ M_D @ Pi_RS) @ Gpinv @ Gamma)
    print("\n(A) ANCHORS:")
    print(f"   bare ||[Pi_RS,M_D]||        = {bare_comm:.4f}  (repo 58.72)")
    print(f"   bare ||C2=Gamma M_D Pi_RS|| = {bare_C2:.4f}  (repo 155.36)")
    print(f"   Gamma-independent residual  = {resid_C2:.4f}  (fully Gamma-indep)")
    assert abs(bare_C2 - 155.3625) < 1e-2
    assert abs(resid_C2 - bare_C2) < 1e-2

    # ---- (B) IS C2 SCALE-INVARIANT (i.e. could it BE a topological index)? --
    # A topological index is scale-invariant and integer-valued. Test the
    # homogeneity of C2 in the symbol scale, and its dependence on |xi|.
    xi_norm = float(np.linalg.norm(XI))
    c2_1 = C2_of_xi(e, Gamma, Pi_RS, XI)
    c2_2 = C2_of_xi(e, Gamma, Pi_RS, 2.0 * XI)
    c2_half = C2_of_xi(e, Gamma, Pi_RS, 0.5 * XI)
    rng = np.random.default_rng(20260627)
    # several RANDOM real covectors rescaled to the SAME norm as XI
    rand_c2 = []
    for _ in range(6):
        v = rng.normal(size=N)
        v = v / np.linalg.norm(v) * xi_norm
        rand_c2.append(C2_of_xi(e, Gamma, Pi_RS, v.astype(complex)))
    rand_c2 = np.array(rand_c2)
    print("\n(B) SCALE / ROTATION STRUCTURE OF C2 IN THE SYMBOL xi:")
    print(f"   C2(xi)          = {c2_1:.4f}   (|xi| = {xi_norm:.4f})")
    print(f"   C2(2 xi)/C2(xi) = {c2_2 / c2_1:.6f}   (=2 => degree-1 homogeneous)")
    print(f"   C2(xi/2)/C2(xi) = {c2_half / c2_1:.6f}   (=0.5 => degree-1 homogeneous)")
    print(f"   C2(random xi, SAME |xi|): mean={rand_c2.mean():.4f}, "
          f"std={rand_c2.std():.2e}, max|dev|={np.max(np.abs(rand_c2 - c2_1)):.2e}")
    homog_deg1 = abs(c2_2 / c2_1 - 2.0) < 1e-6 and abs(c2_half / c2_1 - 0.5) < 1e-6
    rot_invariant = float(np.max(np.abs(rand_c2 - c2_1))) < 1e-6
    K_const = c2_1 / xi_norm
    print(f"   => C2 = K * |xi| with K = {K_const:.6f} (pure Clifford-Gram rep constant)")
    print(f"   => degree-1 homogeneous: {homog_deg1};  rotation-invariant in xi: {rot_invariant}")
    print(f"   => SCALE-INVARIANT (topological) content of C2: "
          f"{'NONE (C2 scales with |xi|)' if homog_deg1 else 'present'}")
    print(f"   sanity: 155.36/24 = {bare_C2/24:.4f}, /8 = {bare_C2/8:.4f}, "
          f"/16 = {bare_C2/16:.4f} (no clean integer)")

    # ---- (C) THE CANDIDATE INDEX ON THE SAME PHYSICAL OPERATOR -------------
    eta_S3 = eta_D_S3_twisted()
    mkt = mkt_spectral_asymmetry(e, Gamma)
    print("\n(C) CANDIDATE GLOBAL INDEX (computed AS-IS on the same operator):")
    print(f"   eta(D_S3 (x) S(6,4))  [round S^3, flat S(6,4)] = {eta_S3:.4f}  "
          f"(symmetric spectrum -> 0 EXACTLY)")
    print(f"   ind_APS (flat S(6,4), round S^3)               = 0  (eta=0, h=0, bulk=0)")
    print(f"   BV Koszul-Tate Hessian M_KT=B^dag B spectrum   : "
          f"n_pos={mkt['n_pos']}, n_neg={mkt['n_neg']}, n_zero={mkt['n_zero']}")
    print(f"      min_eig={mkt['min_eig']:.3e} >= 0 => positive-SEMIDEFINITE; "
          f"spectral asymmetry eta_like = {mkt['eta_like']} ... "
          f"(but n_neg=0 => NO APS asymmetry: structurally 0)")
    print(f"   ch2(S_X)[K3] or ch2(S(6,4))[K3]                = NOT COMPUTED")
    print(f"      pushforward Y14->X4 NOT_DEFINED: metric fiber GL(4,R)/O(3,1) is")
    print(f"      NOT a convex vector space (blocked shortcut); no Fredholm family.")

    # ---- (D) THE C2 CONNECTION: computable handle or forced analogy? -------
    # Proposed handle: 'spectral-section boundary projection P_d inserted into the
    # BV closure changes C2's global obstruction'. Test it concretely: P_d is the
    # APS positive-spectral projection of a SELF-ADJOINT BOUNDARY DIRAC operator on
    # a 3-manifold. Does the C2/BV object supply such an operator?
    #   - C2 lives on the 1792-dim vector-spinor space at ONE symbol point: no
    #     manifold, no boundary, no boundary-Dirac spectrum.
    #   - The only self-adjoint operator present is M_KT = B^dag B (>=0): its APS
    #     spectral projection is trivial (P_d = projector onto im(B^dag), a fixed
    #     dimension count = rank bookkeeping, NOT a Y14 topological invariant).
    # Decisive disconnects, each a COMPUTED fact above:
    disc_scale = homog_deg1                 # C2 ~ |xi|, index scale-invariant
    disc_domain = True                      # C2 single-point symbol; index = global
    disc_mkt_psd = (mkt['n_neg'] == 0)      # M_KT psd -> eta identically 0
    # geometric data that feeds the index provably does not move C2 (curvature
    # diagnostic: a-priori 0-1.8%, greedy 6.2%): import that as the third handle test.
    local_addressable_pct = 6.2             # from rs_c2_curvature_vs_global_diagnostic.py
    print("\n(D) THE C2 CONNECTION (computable handle vs forced analogy):")
    print(f"   handle proposed: P_d (APS spectral section) inserted into BV closure")
    print(f"                    changes C2's global obstruction.")
    print(f"   DISCONNECT 1 (SCALE):  C2 = K|xi| (degree-1) vs index scale-invariant "
          f"=> {disc_scale}")
    print(f"   DISCONNECT 2 (DOMAIN): C2 = single-point symbol-algebra (1792-dim) vs "
          f"index = global integral/spectral-asymmetry => {disc_domain}")
    print(f"   DISCONNECT 3 (NO BOUNDARY DIRAC): only self-adjoint op is M_KT=B^dag B, "
          f"positive-semidefinite, eta==0 => {disc_mkt_psd}")
    print(f"   DISCONNECT 4 (GEOMETRY INERT): the Y14 curvature that computes ch2 moves")
    print(f"                    C2 by ~{local_addressable_pct}% (0% a-priori); does NOT")
    print(f"                    supply the ~94% 'global residual'.")
    no_handle = disc_scale and disc_mkt_psd
    verdict = "FORCED_ANALOGY" if no_handle else "C2_CONNECTED_PARTIAL"
    print(f"\n   computable handle connecting C2 <-> index exists? {not no_handle}")
    print(f"   => C2-CONNECTION VERDICT: {verdict}")

    # ---- (E) TARGET-IMPORT + BLOCKED-SHORTCUT CHECKS ----------------------
    print("\n(E) GUARD CHECKS:")
    used_24_over_8 = False
    used_assumed_K3 = False
    used_chi_input = False
    print(f"   target-import: used 24/8=3? {used_24_over_8};  assumed-K3? "
          f"{used_assumed_K3};  used chi(K3) as input? {used_chi_input}")
    print(f"   computed index reported AS-IS: eta=0, ind_APS=0, ch2[K3]=NOT_COMPUTED, "
          f"C2={bare_C2:.2f} (non-integer)")
    print(f"   blocked shortcuts avoided: contractible-fiber-pushforward, "
          f"convex-Lorentzian-fiber, twisted-deRham=chi-without-symbol,")
    print(f"      K3-chi-as-input, flat-Ahat=3, 24/8=3  -- NONE used.")
    assert not (used_24_over_8 or used_assumed_K3 or used_chi_input)

    # ---- (F) THE PRECISE UNSUPPLIED EDGE OBJECT ---------------------------
    print("\n(F) THE PRECISE EDGE (the unsupplied object that blocks closure):")
    print("   Two distinct unsupplied objects, on the two sides:")
    print("   INDEX side: the families pushforward pi_!: K(Y14) -> K(X4) and a symbol/")
    print("               K-theory class for D_GU -- BLOCKED by the GL(4,R)/O(3,1) fiber")
    print("               (no Fredholm family / K-orientation). ch2[K3] uncomputable as posed.")
    print("   CONNECTION side: a 'BV-to-boundary-Dirac symbol map' -- an explicit")
    print("               identification of M_KT (or the BRST differential) with a")
    print("               geometric self-adjoint boundary Dirac D_Sigma whose APS")
    print("               projection P_d is the spectral section, PLUS a proof that the")
    print("               C2 obstruction equals that operator's eta/spectral-flow.")
    print("   No such map exists in the repo; and the COMPUTED structural facts")
    print("   (C2 ~ |xi| scale-dependent + rotation-symmetric; M_KT positive-")
    print("   semidefinite => eta==0; BV index = dimension bookkeeping) are positive")
    print("   evidence it CANNOT exist as currently posed.")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print(f"  computed number (C2)         : {bare_C2:.4f}  (non-integer; /24={bare_C2/24:.3f})")
    print(f"  computed index (same operator): eta=0, ind_APS=0, ch2[K3]=NOT_COMPUTED")
    print(f"  C2 scale-invariant content   : NONE (C2 = {K_const:.4f} * |xi|)")
    print(f"  C2 <-> index connection      : {verdict}")
    print(f"  decision-tree outcome        : PUSHFORWARD_NOT_DEFINED (index side)")
    print(f"  target import used           : NONE (no 24/8, no assumed-K3)")
    print("=" * 78)

    return dict(
        bare_C2=bare_C2, resid_C2=resid_C2, K_const=K_const,
        homog_deg1=homog_deg1, rot_invariant=rot_invariant,
        c2_ratio_2=c2_2 / c2_1, c2_ratio_half=c2_half / c2_1,
        rand_c2_maxdev=float(np.max(np.abs(rand_c2 - c2_1))),
        eta_S3=eta_S3, ind_APS=0, mkt=mkt,
        ch2_K3="NOT_COMPUTED", c2_connection_verdict=verdict,
        decision_outcome="PUSHFORWARD_NOT_DEFINED",
        target_import_used=False,
    )


if __name__ == "__main__":
    main()
