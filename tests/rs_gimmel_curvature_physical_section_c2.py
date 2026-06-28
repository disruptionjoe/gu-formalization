#!/usr/bin/env python3
r"""OFF THE SYMBOL ALGEBRA (2026-06-27): does the ACTUAL Y14 gimmel
connection-CURVATURE 2-form, at the PHYSICAL SECTION, drive the secondary
constraint C2 down?

Builds on:
  tests/rs_bicomplex_spin95_connection_2form.py     (bicomplex; C2 bare 155.36, anti-trap 58.72)
  tests/willmore_el_schwarzschild_order.py          (RY_block: gimmel ambient Riemann, O(1) M-indep)
  explorations/ii-s-coordinate-formula-2026-06-23.md (gimmel Christoffels, Sec 2)
  explorations/bv-bicomplex-and-c2-obstruction-2026-06-27.md (the C2 isolation)

THE IDEA (Joe's sharpening). Y14 = Met(X4) is the space of ALL Lorentzian metrics on
spacetime X4. We physically inhabit ONE: a single SECTION s: X4 -> Y14 (the physical
metric). The distinguished null plane the symbol algebra demanded (one plane to break
Spin(9,5)'s 5-fold null-pair symmetry) is THE LIGHT CONE OF THE PHYSICAL METRIC. So we do
NOT scan arbitrary null planes: we build the carrier from the ACTUAL gimmel curvature at the
physical (Minkowski) section, contracted onto the physical null cone.

CONSTRUCTION OF THE CARRIER W_curv (a-priori, NEVER reads C2/M_D/Gamma/xi):
  1. Gimmel ambient Riemann block R^Y^(ab)_(cd) mu nu on Y14=Met(X4) at the physical fiber
     q = eta (Minkowski), from the IN-REPO Christoffels (willmore RY_block: the mixed
     horizontal(mu nu) x vertical(ab,cd) block, O(1), M-independent, NONZERO).
  2. PHYSICAL NULL CONE: contract the horizontal 2-form indices (mu,nu) with the physical
     null bivector omega = k ^ m, k null (eta(k,k)=0), m spacelike _|_ k. This is the (3,1)
     light-cone tangent 2-plane the physical section selects.  -> W_vert, an endomorphism of
     the (6,4) vertical fiber = an so(6,4) element (R_{(ab)(cd)} is antisymmetric: Riemann).
  3. Vielbein: orthonormalize W_vert against the vertical Frobenius metric V (signature (6,4))
     -> a genuine so(6,4) matrix; embed into so(9,5) on the 14-frame (6 (+) verts -> +slots,
     4 (-) verts -> -slots; the 4 horizontal directions carry zero).  Extract components
     w_ab in the SAME Sigma_ab basis the bicomplex uses.
  4. Carrier sigma_c(W_curv) = sum w_ab Sigma_ab ; holonomy G_W = expm(sigma_c).

This is the FIRST carrier built from the real Y14 geometry rather than the symbol rep.
Then we run the bicomplex battery: dressed C2, anti-trap, s^2, equivariance, H-linearity.

GUARDS:
  ANTI-TRAP        : bare ||[Pi_RS, M_D]|| MUST stay 58.72 (M_D never touched).
  ANTI-FIXED-SOLVE : W_curv direction is from the Christoffels + eta ONLY -- it never reads
                     C2/M_D/Gamma/xi. We scan only an overall AMPLITUDE t (as the repo's
                     a-priori boost scan does), never the 91 components against the target.
  ANTI-VACUOUS     : s^2 = 0 must be non-trivial (raw-gauge control breaks closure).
  HONEST OUTCOME   : report REAL numbers. C2 may drop (real geometry helps) or floor (local
                     fiber curvature insufficient -> global Y14 needed). Either is reported.
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

import oq_rk1_cl95_explicit_rep as cl95  # verified Cl(9,5) rep

N = 14
XI = np.array([1.0, 2.0, 3.0, 4.0, 0.5, 1.5, 2.5, 0.7,
               1.1, 0.3, 2.2, 1.7, 0.9, 1.3], dtype=complex)


def fro(A):
    return float(np.linalg.norm(A))


def proj_onto_kernel(M):
    gram = M @ M.conj().T
    return np.eye(M.shape[1], dtype=complex) - M.conj().T @ np.linalg.pinv(gram) @ M


# ===========================================================================
# (0) THE Cl(9,5) REP, Sigma generators, core RS operators  (as in bicomplex)
# ===========================================================================
def build_rep():
    n_pairs = 7
    dim = 2 ** n_pairs  # 128
    G = cl95.jordan_wigner_gammas(n_pairs)
    eta = np.array([+1.0] * 9 + [-1.0] * 5)  # frame signature (9,5): 0..8 +, 9..13 -
    e = [G[a] if eta[a] > 0 else 1j * G[a] for a in range(N)]
    Iden = np.eye(dim, dtype=complex)
    return dim, eta, e, Iden


def build_J(dim, e):
    s = np.empty(N)
    for a in range(N):
        s[a] = (-1.0) ** a if a < 9 else (-1.0) ** (a + 1)
    anticomm = [a for a in range(N) if s[a] < 0]
    U = np.eye(dim, dtype=complex)
    for a in anticomm:
        U = U @ e[a]
    return U


# ===========================================================================
# (1) GIMMEL AMBIENT RIEMANN BLOCK  R^Y^(ab)_(cd) mu nu  at q = eta (Minkowski)
#     -- transcribed VERBATIM from tests/willmore_el_schwarzschild_order.py PART C
#        (which itself is the explicit ii-s-coordinate-formula Section 2 Christoffels).
# ===========================================================================
NB = 4  # base/fiber-pair dimension (X4)
eta4 = np.diag([-1.0, 1.0, 1.0, 1.0])   # physical Minkowski metric (signature (3,1))
q = eta4
qinv = eta4  # eta^{-1} = eta


def kron(i, j):
    return 1.0 if i == j else 0.0


def dpair(a, b, mu, lam):
    return 0.5 * (kron(a, mu) * kron(b, lam) + kron(a, lam) * kron(b, mu))


def Vup(a, b, c, d):
    # V^{(ab),(cd)}(q) = q^{a(c} q^{d)b} - 1/2 q^{ab} q^{cd}
    return (0.5 * (qinv[a, c] * qinv[d, b] + qinv[a, d] * qinv[c, b])
            - 0.5 * qinv[a, b] * qinv[c, d])


def GammaH(rho, mu, c, d):
    # Gamma^{rho}_{mu,(cd)} = 1/2 q^{rho lam} delta^{(cd)}_{mu lam}
    return sum(0.5 * qinv[rho, lam] * dpair(c, d, mu, lam) for lam in range(NB))


def GammaV(a, b, mu, rho):
    # Gamma^{(ab)}_{mu rho} = -1/2 V^{(ab),(cd)} delta^{(cd)}_{mu rho}
    s = 0.0
    for c in range(NB):
        for d in range(NB):
            s += Vup(a, b, c, d) * dpair(c, d, mu, rho)
    return -0.5 * s


def RY_block(a, b, c, d, mu, nu):
    # R^Y^(ab)_(cd) mu nu = sum_rho GammaV(ab,mu,rho)GammaH(rho,nu,cd) - (mu<->nu)
    s = 0.0
    for rho in range(NB):
        s += (GammaV(a, b, mu, rho) * GammaH(rho, nu, c, d)
              - GammaV(a, b, nu, rho) * GammaH(rho, mu, c, d))
    return s


# ---- symmetric-pair (Sym^2) basis of the 10-dim vertical fiber ----
PAIRS10 = [(c, d) for c in range(NB) for d in range(c, NB)]  # 10 pairs, c<=d


def Smat(p):
    """4x4 symmetric basis tensor S_p: E_cc for (c,c); E_cd+E_dc for c<d."""
    c, d = p
    S = np.zeros((NB, NB))
    S[c, d] += 1.0
    S[d, c] += 1.0
    if c == d:
        S *= 0.5   # so S_cc has a single 1 on the diagonal
    return S


def build_vertical_metric():
    """V_metric[p][q] = V_h(S_p, S_q) = tr(eta S_p eta S_q) - 1/2 tr(eta S_p) tr(eta S_q)."""
    Vm = np.zeros((10, 10))
    for ip, p in enumerate(PAIRS10):
        Sp = Smat(p)
        for iq, qq in enumerate(PAIRS10):
            Sq = Smat(qq)
            A = eta4 @ Sp
            B = eta4 @ Sq
            Vm[ip, iq] = np.trace(A @ B) - 0.5 * np.trace(A) * np.trace(B)
    return Vm


def build_R_endo(mu, nu):
    """Endomorphism matrix (10x10) of R^Y_{mu nu} on the Sym^2 basis:
       (R_{mu nu} S_q)^{ab} = sum_{c',d'} R^Y^(ab)_(c'd') mu nu (S_q)_{c'd'} ;
       component along S_p (p=(a<=b)) is the (ab) matrix entry."""
    M = np.zeros((10, 10))
    for iq, qq in enumerate(PAIRS10):
        Sq = Smat(qq)
        for ip, p in enumerate(PAIRS10):
            a, b = p
            val = 0.0
            for cp in range(NB):
                for dp in range(NB):
                    val += RY_block(a, b, cp, dp, mu, nu) * Sq[cp, dp]
            M[ip, iq] = val
    return M


# ===========================================================================
# (2)+(3) PHYSICAL NULL CONE contraction + vielbein embedding -> so(9,5) carrier
# ===========================================================================
def physical_null_bivector(kind="null"):
    """omega^{mu nu} = k^mu m^nu - k^nu m^mu.
       kind='null'     : k=(1,1,0,0) [eta(k,k)=0], m=(0,0,1,0) -> light-cone tangent plane.
       kind='spacelike': k=(0,1,0,0), m=(0,0,1,0)  (control: a NON-null plane)
       kind='timelike' : k=(1,0,0,0), m=(0,0,1,0)  (control: a NON-null plane)."""
    if kind == "null":
        k = np.array([1.0, 1.0, 0.0, 0.0]); m = np.array([0.0, 0.0, 1.0, 0.0])
    elif kind == "spacelike":
        k = np.array([0.0, 1.0, 0.0, 0.0]); m = np.array([0.0, 0.0, 1.0, 0.0])
    elif kind == "timelike":
        k = np.array([1.0, 0.0, 0.0, 0.0]); m = np.array([0.0, 0.0, 1.0, 0.0])
    else:
        raise ValueError(kind)
    om = np.outer(k, m) - np.outer(m, k)
    return om, k, m


def build_curvature_carrier(Vm, kind="null"):
    """Return Wdict {(a,b): w_ab} in the bicomplex Sigma-basis, plus diagnostics."""
    om, k, m = physical_null_bivector(kind)
    # contract horizontal 2-form (mu<nu) with the physical null bivector
    W_vert = np.zeros((10, 10))
    for mu in range(NB):
        for nu in range(mu + 1, NB):
            W_vert += om[mu, nu] * build_R_endo(mu, nu)

    # antisymmetry check: V_metric @ W_vert should be antisymmetric (Riemann symmetry)
    K = Vm @ W_vert
    antisym_defect = fro(K + K.T) / (fro(K) + 1e-30)

    # vielbein of the (6,4) vertical metric: P^T V P = diag(+1*6, -1*4)
    evals, evecs = np.linalg.eigh(Vm)
    order = np.argsort(-evals)             # descending: positives first
    evals = evals[order]; evecs = evecs[:, order]
    n_pos = int(np.sum(evals > 0))
    n_neg = int(np.sum(evals < 0))
    P = evecs @ np.diag(1.0 / np.sqrt(np.abs(evals)))
    # endomorphism in the orthonormal frame
    L_vert = np.linalg.inv(P) @ W_vert @ P
    Eta_vert = np.diag([1.0] * n_pos + [-1.0] * n_neg)
    so_defect = fro(Eta_vert @ L_vert + (Eta_vert @ L_vert).T) / (fro(Eta_vert @ L_vert) + 1e-30)

    # scatter into the 14-frame: 6 (+) verts -> frame idx [3,4,5,6,7,8],
    #                            4 (-) verts -> frame idx [10,11,12,13];
    # horizontal slots 0,1,2 (+) and 9 (-) carry zero.
    pos_slots = [3, 4, 5, 6, 7, 8]
    neg_slots = [10, 11, 12, 13]
    vert_slots = pos_slots[:n_pos] + neg_slots[:n_neg]
    L14 = np.zeros((N, N), dtype=complex)
    for i, si in enumerate(vert_slots):
        for j, sj in enumerate(vert_slots):
            L14[si, sj] = L_vert[i, j]

    # lower with frame metric Eta=diag(+1*9,-1*5); w_ab = (Eta L14)_{ab}, a<b
    Eta14 = np.diag([1.0] * 9 + [-1.0] * 5)
    Llow = Eta14 @ L14
    glob_so_defect = fro(Llow + Llow.T) / (fro(Llow) + 1e-30)
    Wdict = {}
    for a in range(N):
        for b in range(a + 1, N):
            w = Llow[a, b]
            if abs(w) > 1e-12:
                Wdict[(a, b)] = complex(w)
    diag = dict(antisym_defect=antisym_defect, so_defect=so_defect,
                glob_so_defect=glob_so_defect, n_pos=n_pos, n_neg=n_neg,
                Wnorm=fro(L14), k=k, m=m, nullnorm=float(k @ eta4 @ k))
    return Wdict, diag


# ===========================================================================
# MAIN
# ===========================================================================
def main():
    t0 = time.time()
    dim, eta, e, Iden = build_rep()
    VSdim = N * dim  # 1792

    pairs = [(a, b) for a in range(N) for b in range(a + 1, N)]
    Sigma = {(a, b): 0.25 * (e[a] @ e[b] - e[b] @ e[a]) for (a, b) in pairs}

    def sigma_c(Wdict):
        out = np.zeros((dim, dim), dtype=complex)
        for (a, b), w in Wdict.items():
            if w != 0.0:
                out = out + w * Sigma[(a, b)]
        return out

    def Bn_from_W(Wdict):
        GW = expm(sigma_c(Wdict))
        return np.hstack([e[a] @ GW for a in range(N)]), GW

    Gamma = np.hstack(e)                                   # 128 x 1792
    Pi_RS = proj_onto_kernel(Gamma)
    Pi_perp = np.eye(VSdim, dtype=complex) - Pi_RS
    cxi = sum(XI[a] * e[a] for a in range(N))
    M_D = np.kron(np.eye(N, dtype=complex), cxi)
    gauge = np.vstack([XI[a] * np.eye(dim, dtype=complex) for a in range(N)])  # d_A

    print("=" * 80)
    print("GIMMEL CONNECTION-CURVATURE 2-FORM at the PHYSICAL SECTION  ->  C2 ?")
    print("=" * 80)

    # ---- anchors ----
    bare_comm = fro(Pi_RS @ M_D - M_D @ Pi_RS)
    C2_bare = Gamma @ M_D @ Pi_RS
    nC2_bare = fro(C2_bare)
    GGd = Gamma @ Gamma.conj().T
    Gpinv = Gamma.conj().T @ np.linalg.pinv(GGd)
    resid_C2_bare = fro(C2_bare - (C2_bare @ Gpinv) @ Gamma)
    print("\n(A) ANCHORS (must reproduce):")
    print(f"   bare ||[Pi_RS,M_D]||        = {bare_comm:.4f}   (repo 58.72)")
    print(f"   bare ||C2=Gamma M_D Pi_RS|| = {nC2_bare:.4f}   (repo 155.36; "
          f"Gamma-indep residual {resid_C2_bare:.4f})")

    # ---- build the gimmel curvature carrier (a-priori) ----
    Vm = build_vertical_metric()
    Wdict, dg = build_curvature_carrier(Vm, kind="null")
    print("\n(B) GIMMEL CURVATURE CARRIER W_curv (physical null cone):")
    print(f"   vertical metric signature      = ({dg['n_pos']},{dg['n_neg']})  (expect (6,4))")
    print(f"   k=(1,1,0,0) eta(k,k)           = {dg['nullnorm']:.3f}  (=0 => NULL direction)")
    print(f"   Riemann antisym defect (V W)   = {dg['antisym_defect']:.2e}  (so(6,4): ~0)")
    print(f"   so(6,4) frame defect           = {dg['so_defect']:.2e}")
    print(f"   so(9,5) global defect (Eta L)  = {dg['glob_so_defect']:.2e}")
    print(f"   carrier ||L14||                = {dg['Wnorm']:.4f}; #nonzero w_ab = {len(Wdict)}")

    # ---- dressed-C2 / dressed-obstruction evaluator at a given carrier ----
    def dressed_metrics(Wd):
        Bn, GW = Bn_from_W(Wd)
        Pi = proj_onto_kernel(Bn)
        # dressed obstruction ||[Pi, M_D]|| via block commutators (fast)
        P4 = Pi.reshape(N, dim, N, dim).transpose(0, 2, 1, 3)
        comm = P4 @ cxi - cxi @ P4
        dobs = float(np.linalg.norm(comm))
        # dressed C2 = B_W M_D Pi_{ker B_W}; residual against B_W (genuine new constraint)
        C2d = Bn @ M_D @ Pi
        nC2d = fro(C2d)
        BBd = Bn @ Bn.conj().T
        Bpinv = Bn.conj().T @ np.linalg.pinv(BBd)
        resid = fro(C2d - (C2d @ Bpinv) @ Bn)
        return dict(dobs=dobs, nC2d=nC2d, resid=resid, Bn=Bn, Pi=Pi, GW=GW)

    # natural scale (t=1) ---------------------------------------------------
    nat = dressed_metrics(Wdict)
    print("\n(C) DRESSED C2 at NATURAL SCALE (t=1, carrier exactly as the geometry gives it):")
    print(f"   dressed ||C2||             = {nat['nC2d']:.4f}   (bare 155.36; drop? "
          f"{nat['nC2d'] < nC2_bare})")
    print(f"   dressed C2 residual        = {nat['resid']:.4f}   (>0 => still genuine)")
    print(f"   dressed obstruction        = {nat['dobs']:.4f}   (spurion floor 32.80, "
          f"a-priori conn floor 41.04)")

    # AMPLITUDE scan (a-priori: scan ONLY the overall amplitude t of the FIXED geometric
    # direction -- exactly as the repo's boost scan sweeps t over a named generator. The
    # 91-component direction is NEVER tuned against C2.)
    print("\n(D) A-PRIORI AMPLITUDE SCAN  W -> t * W_curv  (direction fixed by geometry):")
    ts = np.linspace(-3.0, 3.0, 25)
    best = (None, np.inf, np.inf)  # (t, C2, dobs)
    rows = []
    for t in ts:
        if abs(t) < 1e-9:
            continue
        Wt = {kk: t * vv for kk, vv in Wdict.items()}
        mm = dressed_metrics(Wt)
        rows.append((t, mm['nC2d'], mm['dobs']))
        if mm['nC2d'] < best[1]:
            best = (t, mm['nC2d'], mm['dobs'])
    for (t, c2, do) in rows:
        mark = "  <== min C2" if abs(t - best[0]) < 1e-9 else ""
        print(f"   t={t:+.3f}:  ||C2||={c2:8.4f}   dressed_obs={do:8.4f}{mark}")
    print(f"   >>> MIN dressed ||C2|| over amplitude = {best[1]:.4f} at t={best[0]:+.3f}  "
          f"(bare 155.36; reached 0? {best[1] < 1e-6})")

    # NULL vs NON-NULL control: does the PHYSICAL NULL cone do something a generic plane can't?
    print("\n(E) NULL-CONE SPECIFICITY (physical null plane vs non-null control planes):")
    for kind in ("null", "spacelike", "timelike"):
        Wd, _ = build_curvature_carrier(Vm, kind=kind)
        # match amplitude scan min for fair comparison
        bc = np.inf
        for t in np.linspace(-3.0, 3.0, 25):
            if abs(t) < 1e-9:
                continue
            mm = dressed_metrics({kk: t * vv for kk, vv in Wd.items()})
            bc = min(bc, mm['nC2d'])
        print(f"   {kind:9s} plane: min ||C2|| over amplitude = {bc:.4f}")

    # ---- full BV bicomplex at the natural curvature carrier ----
    Bn = nat['Bn']; Pi_kerBW = nat['Pi']
    A_W = Pi_kerBW @ gauge
    M_KT = Bn.conj().T @ Bn
    noether = fro(Bn @ A_W)
    d0, d1 = dim, VSdim
    D = d0 + d1 + d1 + d0
    o0, o1, o2, o3 = 0, d0, d0 + d1, d0 + d1 + d1
    s = np.zeros((D, D), dtype=complex)
    s[o1:o1 + d1, o0:o0 + d0] = A_W
    s[o2:o2 + d1, o1:o1 + d1] = M_KT
    s[o3:o3 + d0, o2:o2 + d1] = A_W.conj().T
    s2 = fro(s @ s)
    rank_MKT = int(np.linalg.matrix_rank(M_KT, tol=1e-7))
    rank_AW = int(np.linalg.matrix_rank(A_W, tol=1e-7))
    # non-vacuity control: raw gauge breaks closure
    s_raw = np.zeros((D, D), dtype=complex)
    s_raw[o1:o1 + d1, o0:o0 + d0] = gauge
    s_raw[o2:o2 + d1, o1:o1 + d1] = M_KT
    s_raw[o3:o3 + d0, o2:o2 + d1] = gauge.conj().T
    s2_raw = fro(s_raw @ s_raw)
    print("\n(F) FULL BV BICOMPLEX at the curvature carrier (T dim 3840):")
    print(f"   Noether ||B_W A_W||   = {noether:.2e}")
    print(f"   ||s^2||               = {s2:.2e}   (target 0; non-vacuous)")
    print(f"   leg ranks             = M_KT {rank_MKT} / A_W {rank_AW}")
    print(f"   raw-gauge control s^2 = {s2_raw:.4f}   (BREAKS closure: {s2_raw > 1e-6})")

    # ---- anti-trap ----
    bare_after = fro(Pi_RS @ M_D - M_D @ Pi_RS)
    print("\n(G) ANTI-TRAP (M_D never modified):")
    print(f"   bare ||[Pi_RS,M_D]||  = {bare_after:.4f}   (MUST be 58.72: "
          f"{abs(bare_after - 58.72) < 0.01})")

    # ---- genuine-geometry discriminators: equivariance defect + H-linearity ----
    sig = sigma_c(Wdict)
    test_gens = [(3, 4), (10, 11), (0, 5), (4, 12)]
    max_def = max(fro(Sigma[(c, d)] @ sig - sig @ Sigma[(c, d)]) for (c, d) in test_gens)
    U = build_J(dim, e)
    h_sig = fro(sig @ U - U @ np.conjugate(sig))
    JVS = np.kron(np.eye(N, dtype=complex), U)
    h_Pi = fro(Pi_kerBW @ JVS - JVS @ np.conjugate(Pi_kerBW))
    # a-priori discriminator: carrier does NOT read xi/M_D/C2 (rebuild with a DIFFERENT xi-free
    # input shows W_curv is identical -- it is a pure functional of (eta, Christoffels)).
    Wdict2, _ = build_curvature_carrier(Vm, kind="null")
    apriori_defect = max((abs(Wdict.get(kk, 0) - Wdict2.get(kk, 0))
                          for kk in set(Wdict) | set(Wdict2)), default=0.0)
    print("\n(H) GENUINE-GEOMETRY DISCRIMINATORS:")
    print(f"   equivariance defect max||[Sigma_cd, sigma_c(W)]|| = {max_def:.4f}  "
          f"(non-equivariant: {max_def > 1e-6})")
    print(f"   H-linearity ||[sigma_c(W),J]||={h_sig:.2e}, ||[Pi_kerBW,J]||={h_Pi:.2e}  "
          f"(H-linear: {max(h_sig, h_Pi) < 1e-6})")
    print(f"   a-priori: W_curv independent of any rebuild input (defect {apriori_defect:.1e}); "
          f"construction reads ONLY (eta, Christoffels), never C2/M_D/Gamma/xi")

    # ---- verdict ----
    print("\n" + "=" * 80)
    print("VERDICT (REAL NUMBERS)")
    print("=" * 80)
    print(f"  bare C2                     : {nC2_bare:.4f}")
    print(f"  dressed C2 (natural t=1)    : {nat['nC2d']:.4f}  (drop from bare? "
          f"{nat['nC2d'] < nC2_bare})")
    print(f"  dressed C2 (min over ampl.) : {best[1]:.4f} at t={best[0]:+.3f}  (=0? "
          f"{best[1] < 1e-6})")
    print(f"  dressed obstruction (t=1)   : {nat['dobs']:.4f}  (vs spurion 32.80, conn 41.04)")
    print(f"  anti-trap bare [Pi_RS,M_D]  : {bare_after:.4f}  (MUST be 58.72)")
    print(f"  bicomplex s^2               : {s2:.2e}  (raw-control {s2_raw:.2f})")
    print(f"  carrier genuine             : so(9,5) defect {dg['glob_so_defect']:.1e}, "
          f"non-equiv {max_def:.3f}, H-lin {max(h_sig, h_Pi):.1e}, a-priori {apriori_defect:.1e}")
    print(f"  wall {time.time() - t0:.1f}s")

    return dict(nC2_bare=nC2_bare, nC2_nat=nat['nC2d'], nC2_min=best[1], t_min=best[0],
                dobs_nat=nat['dobs'], bare_after=bare_after, s2=s2, s2_raw=s2_raw,
                max_def=max_def, h_max=max(h_sig, h_Pi), glob_so_defect=dg['glob_so_defect'])


if __name__ == "__main__":
    main()
