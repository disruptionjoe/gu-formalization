#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""WP-A4 / register item M-C3 — Krein-sign trichotomy input:
commutant of the constructed GU-native observable algebra on the record sector ker Gamma.

WHAT THIS COMPUTES (exact finite computation; trichotomy input only)
--------------------------------------------------------------------
Carrier: the record sector V = ker Gamma, dim_C = 13*128 = 1664, inside the kinematic
vector-spinor space C^14 (x) C^128 of the verified Cl(9,5) = M(64,H) fixtures
(tests/oq_rk1_cl95_explicit_rep.py via tests/generation-sector/gen_sector_bridge.py;
anchors bare ||[Pi_RS, M_D]|| = 58.7215 and C2 = 155.3625 are reproduced below).

Algebra: the real associative algebra
    A = <  Pi_RS (I_14 (x) Cl(9,5)) Pi_RS ,
           Pi_RS (so(9,5) frame generators (x) I_128) Pi_RS ,
           M_D (compressed) ,  Pi_RS  >
restricted to V (where Pi_RS acts as the identity).  Generator sub-list actually used:
the 14 compressed Clifford generators, 5 compressed higher Clifford words (including
beta = e0..e8 and the volume word omega = e0..e13), 12 compressed spin quadratics
sigma_ij = (1/2) e_i e_j, 12 compressed so(9,5) frame generators M_ij (x) I, and
compressed M_D.  Adding generators can only SHRINK a commutant, so certifying
commutant = C.I for this sub-list certifies it for the full generating family.

Commutant method (deliberately NOT a blind 1664^2 nullspace solve):
  (i)  Spectral-graph certificate on V.  A generic Hermitian element H1 of the
       complexified algebra (legitimate: the generator list is verified adjoint-closed)
       is eigendecomposed; simple spectrum (verified) forces any commutant element to be
       diagonal in its eigenbasis; a further generator K then forces d_i = d_j whenever
       (W^dag K W)_{ij} != 0.  dim_C(commutant) = number of connected components of the
       resulting graph.  Replicated at three edge thresholds and two independent seeds.
  (ii) Tensor-shortcut cross-check at ambient level.  Anything commuting with the full
       I (x) Cl(9,5) = I (x) M(64,H) part is of the form Y (x) (H-linear scalar): the
       spinor-factor commutant is certified = C.I at the 128 level, and over R the
       H-linear scalars are span{1, i, J, iJ}; imposing the frame part forces Y = c I
       (the nullspace of Y -> [Y, so(9,5)] on 14x14 matrices is computed and is
       1-dimensional); imposing the projector and M_D is then automatic (both are
       H-linear, verified).
  Antilinear leg: the fixtures' quaternionic structure J (J^2 = -1) preserves V and
  commutes with every generator (H-linearity defects ~ 1e-9), so the REAL commutant is
  (complex commutant) + (complex commutant).J.

Trichotomy read-out (computed, not assumed):
  - If dim_C commutant = 1: real commutant = span_R{I, iI, J, iJ} = H.I (dim_R 4);
    V is irreducible over H under A; the only complex-linear involutions in the
    commutant are +/-I, and every antilinear element of the commutant squares to
    -|c|^2 <= 0 (no antilinear involution): the Theorem-2 residual-family dimension
    sum_lambda dim_R(D_lambda) a_lambda b_lambda = 0.  No residual family.
  - Existence leg (Prop 1): admissibility of +/-I against the constructed Krein form
    eta_14 (x) beta restricted to V is decided by its computed signature; the algebra
    contains the compressed diagonal Spin(9,5) boost directions, and the probe exhibits
    a finite unboundedness WITNESS (exponential growth of ||exp(t D) v|| on V) for a
    boost one-parameter subgroup lying inside O(eta_V), with a compact rotation
    direction as bounded contrast control.  By the necessity leg of Prop 1, any
    invariance group containing that subgroup admits NO positivity-majorant.  Relative
    compactness of the closure of the FULL generated group is NOT decided by any finite
    list of matrix identities; the witness certifies non-compactness of specific
    directions only, and whether GU's physical observable algebra retains them is
    exactly W219 (open).

MANDATORY FENCES (verbatim):
  (1) this computes the commutant of the CONSTRUCTED algebra on the KINEMATIC carrier;
      whether this is GU's physical observable algebra is exactly the open
      dynamical-stabilizer question (W219);
  (2) no verdict, bar(b), H59, or claim-status change is made by this probe — per
      Joe's 2026-08-03 standing rule, moving any such bar additionally requires a
      hostile field-specialist review, which has not happened;
  (3) irreducible ⇒ "sign forced IF this is the observable algebra"; reducible ⇒
      report the computed Σ dim formula value as the size of the residual family.

Run:
  PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python -u \
      tests/observable-algebra/commutant_trichotomy_probe.py
Every check is a hard assert; the script exits nonzero on any failure.
"""
from __future__ import annotations

import os
import sys
import time

import numpy as np
import scipy.sparse as sp
from scipy.sparse.csgraph import connected_components

sys.dont_write_bytecode = True

_HERE = os.path.dirname(os.path.abspath(__file__))
_TESTS = os.path.normpath(os.path.join(_HERE, ".."))
_GEN = os.path.join(_TESTS, "generation-sector")
for _p in (_TESTS, _GEN):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import gen_sector_bridge as gu_bridge  # noqa: E402
import step11_gu_native_parity_theorem as step11  # noqa: E402  (reuse the fixtures' J)

N, DIM = gu_bridge.N, gu_bridge.DIM      # 14, 128
NV = (N - 1) * DIM                        # 13*128 = 1664 (record-sector dimension)
ETA = np.array([1.0] * 9 + [-1.0] * 5)

_n_checks = [0]


def check(name: str, cond: bool, detail: str = ""):
    _n_checks[0] += 1
    tag = "ok " if cond else "FAIL"
    print(f"  [{tag}] {name}" + (f"  ({detail})" if detail else ""), flush=True)
    assert cond, f"CHECK FAILED: {name}  {detail}"


def fnorm(X) -> float:
    return float(np.linalg.norm(X))


def word(e, idxs):
    out = np.eye(DIM, dtype=complex)
    for a in idxs:
        out = out @ e[a]
    return out


def sigma128(e, i, j):
    return 0.5 * (e[i] @ e[j])


def Mvec14(i, j):
    M = np.zeros((N, N))
    M[i, j] = ETA[j]
    M[j, i] = -ETA[i]
    return M


def graph_commutant(Ks, n, seed, taus=(1e-4, 1e-6, 1e-8)):
    """dim_C of the commutant of the (adjoint-closed) family Ks on C^n.

    Generic Hermitian element H1 = sum c_i K_i + h.c. (c_i complex Gaussian) lies in the
    complexified algebra; with simple spectrum, any commutant element is diagonal in its
    eigenbasis; each K then forces equality of diagonal entries across every index pair
    where |W^dag K W| is genuinely nonzero.  Components of that graph = commutant dim.
    Returns (mingap, spread, {tau: ncomp}, labels_at_mid_tau, (max_below, min_above)).
    """
    rng = np.random.default_rng(seed)
    H1 = np.zeros((n, n), dtype=complex)
    for K in Ks:
        c = rng.standard_normal() + 1j * rng.standard_normal()
        H1 += c * K
    H1 = H1 + H1.conj().T
    w, W = np.linalg.eigh(H1)
    mingap = float(np.diff(w).min())
    spread = float(w[-1] - w[0])
    Wc = W.conj().T
    adj = {t: np.zeros((n, n), dtype=bool) for t in taus}
    max_below, min_above = 0.0, np.inf
    mid = taus[len(taus) // 2]
    for K in Ks:
        T = Wc @ (K @ W)
        A = np.abs(T)
        np.fill_diagonal(A, 0.0)
        m = float(A.max())
        if m < 1e-9 * (1.0 + fnorm(K)):
            continue  # K is (numerically) diagonal in this basis: contributes no edges
        rel = A / m
        for t in taus:
            adj[t] |= rel > t
        below = rel[rel <= mid]
        above = rel[rel > mid]
        if below.size:
            max_below = max(max_below, float(below.max()))
        if above.size:
            min_above = min(min_above, float(above.min()))
    ncomp, labels_mid = {}, None
    for t in taus:
        nc, labels = connected_components(sp.csr_matrix(adj[t]), directed=False)
        ncomp[t] = int(nc)
        if t == mid:
            labels_mid = labels
    return mingap, spread, ncomp, labels_mid, (max_below, min_above)


def expv(Dm, v, kmax=120, tol=1e-17):
    """exp(Dm) v by Taylor series (||Dm|| is O(1) here; converges fast)."""
    wv = v.copy()
    term = v.copy()
    for k in range(1, kmax):
        term = (Dm @ term) / k
        wv = wv + term
        if fnorm(term) < tol * fnorm(wv):
            break
    return wv


def main():
    t0 = time.time()
    np.set_printoptions(precision=4, suppress=True, linewidth=170)
    print(f"[env] numpy {np.__version__}, n_amb = {N*DIM}, n_V = {NV} = 13*128", flush=True)

    # ------------------------------------------------------------------ [0] fixtures
    print("== [0] fixtures & anchors ==", flush=True)
    e, Gamma, Pi, M_D = gu_bridge.constraint_objects()
    bare = fnorm(Pi @ M_D - M_D @ Pi)
    c2 = fnorm(Gamma @ M_D @ Pi)
    check("anchor: bare ||[Pi_RS, M_D]|| = 58.7215", abs(bare - 58.7215) < 1e-2, f"{bare:.4f}")
    check("anchor: C2 = 155.3625", abs(c2 - 155.3625) < 1e-2, f"{c2:.4f}")
    cerr = 0.0
    Id = np.eye(DIM, dtype=complex)
    for a in range(N):
        for b in range(N):
            anti = e[a] @ e[b] + e[b] @ e[a]
            expc = (2.0 * ETA[a] if a == b else 0.0) * Id
            cerr = max(cerr, float(np.max(np.abs(anti - expc))))
    check("Clifford relations {e_a,e_b} = 2 eta_ab", cerr < 1e-9, f"max err {cerr:.2e}")

    # ------------------------------------------------- [1] controls: J^2=-1, projector
    print("== [1] positive controls: J^2 = -1, projector identities, Krein form ==", flush=True)
    U = step11.quaternionic_J(e, seed=1)
    check("U unitary", fnorm(U @ U.conj().T - Id) < 1e-8)
    check("J^2 = -1 on the spinor factor (U Ubar = -I)", fnorm(U @ U.conj() + Id) < 1e-7,
          f"residual {fnorm(U @ U.conj() + Id):.2e}")
    Jf = np.kron(np.eye(N), U)

    def hl128(x):  # H-linearity defect on the spinor factor: ||U xbar U^dag - x||
        return fnorm(U @ x.conj() @ U.conj().T - x)

    check("Pi idempotent", fnorm(Pi @ Pi - Pi) < 1e-9)
    check("Pi Hermitian", fnorm(Pi - Pi.conj().T) < 1e-9)
    check("trace Pi = 1664 = 13*128", abs(float(np.trace(Pi).real) - NV) < 1e-6)
    check("Gamma Pi = 0", fnorm(Gamma @ Pi) < 1e-8 * fnorm(Gamma))
    hlPi = fnorm(Jf @ Pi.conj() @ Jf.conj().T - Pi)
    check("Pi is H-linear (commutes with J)", hlPi < 1e-8, f"defect {hlPi:.2e}")

    hl_sing = max(hl128(e[a]) for a in range(N))
    check("all 14 Clifford generators H-linear", hl_sing < 1e-8, f"max defect {hl_sing:.2e}")
    PAIRS = [(0, 1), (1, 2), (2, 3), (4, 5), (6, 7), (7, 8),
             (0, 9), (4, 10), (8, 13), (9, 10), (10, 11), (12, 13)]
    hl_sig = max(hl128(sigma128(e, i, j)) for (i, j) in PAIRS)
    check("spin quadratics sigma_ij H-linear", hl_sig < 1e-8, f"max defect {hl_sig:.2e}")
    WORDS = [("e0e1e2", (0, 1, 2)), ("e3e4e5e6", (3, 4, 5, 6)), ("e9e10e11", (9, 10, 11)),
             ("beta=e0..e8", tuple(range(9))), ("omega=e0..e13", tuple(range(14)))]
    hl_w = max(hl128(word(e, idx)) for (_, idx) in WORDS)
    check("higher Clifford words H-linear", hl_w < 1e-8, f"max defect {hl_w:.2e}")
    so_err = max(fnorm(Mvec14(i, j).T @ np.diag(ETA) + np.diag(ETA) @ Mvec14(i, j))
                 for (i, j) in PAIRS)
    check("frame generators in so(9,5) (M^T eta + eta M = 0)", so_err < 1e-12, f"{so_err:.2e}")
    cxi = sum(gu_bridge.XI[a] * e[a] for a in range(N))
    check("M_D = I (x) c(xi) with c(xi) H-linear", hl128(cxi) < 1e-8, f"defect {hl128(cxi):.2e}")

    # Krein form on the spinor factor: beta = e0..e8
    beta = word(e, tuple(range(9)))
    check("beta Hermitian", fnorm(beta - beta.conj().T) < 1e-9)
    check("beta^2 = +I", fnorm(beta @ beta - Id) < 1e-9)
    ib_err = max(fnorm(beta @ e[a] @ beta - e[a].conj().T) for a in range(N))
    check("beta e_a beta^-1 = e_a^dag (Krein self-adjointness of the gammas)",
          ib_err < 1e-8, f"max err {ib_err:.2e}")
    sk_err = max(fnorm((beta @ sigma128(e, i, j)) + (beta @ sigma128(e, i, j)).conj().T)
                 for (i, j) in PAIRS)
    check("spin generators beta-skew (Spin(9,5) in U(beta))", sk_err < 1e-8, f"{sk_err:.2e}")
    evb = np.linalg.eigvalsh(beta)
    sig_beta = (int((evb > 0.5).sum()), int((evb < -0.5).sum()))
    check("signature(beta) = (64, 64)", sig_beta == (64, 64), str(sig_beta))

    # --------------------------------------------------- [2] record-sector basis of V
    print("== [2] record sector V = ker Gamma ==", flush=True)
    _, s_, vh = np.linalg.svd(Gamma)
    check("Gamma has full row rank 128", s_[-1] > 1e-6, f"s_min = {s_[-1]:.3e}")
    B = vh[DIM:].conj().T                                   # 1792 x 1664
    Bc = B.conj().T
    check("dim_C ker Gamma = 1664", B.shape == (N * DIM, NV))
    check("Gamma B = 0", fnorm(Gamma @ B) < 1e-9 * fnorm(Gamma))
    check("B orthonormal", fnorm(Bc @ B - np.eye(NV)) < 1e-9)
    check("Pi B = B (B spans ran Pi_RS)", fnorm(Pi @ B - B) < 1e-8)

    def compress_spinor(x):  # V-compression of I (x) x
        y = np.tensordot(x, B.reshape(N, DIM, NV), axes=([1], [1]))     # (DIM, N, NV)
        y = np.ascontiguousarray(y.transpose(1, 0, 2)).reshape(N * DIM, NV)
        return Bc @ y

    def compress_vector(M):  # V-compression of M (x) I
        y = (M.astype(complex) @ B.reshape(N, DIM * NV)).reshape(N * DIM, NV)
        return Bc @ y

    # antilinear structure on V:  Jv = U_V conj(v)
    JB = Jf @ B.conj()
    check("J preserves the record sector (J ker Gamma = ker Gamma)",
          fnorm(JB - Pi @ JB) < 1e-7, f"residual {fnorm(JB - Pi @ JB):.2e}")
    UV = Bc @ JB
    check("U_V unitary", fnorm(UV @ UV.conj().T - np.eye(NV)) < 1e-7)
    check("J^2 = -1 on V (U_V conj(U_V) = -I)", fnorm(UV @ UV.conj() + np.eye(NV)) < 1e-6,
          f"residual {fnorm(UV @ UV.conj() + np.eye(NV)):.2e}")
    UVc = UV.conj().T

    def hlV(K):  # H-linearity defect on V
        return fnorm(UV @ K.conj() @ UVc - K)

    # ------------------------------------------------ [3] compressed generator family
    print("== [3] compressed generators, adjoint closure, algebra-closure residuals ==",
          flush=True)
    gens = []                                              # (name, K)
    adj_sign = {}                                          # name -> +/-1 (K^dag = s K)
    for a in range(N):
        nm = f"cl:e{a}"
        gens.append((nm, compress_spinor(e[a])))
        adj_sign[nm] = +1 if a < 9 else -1
    for nm_w, idx in WORDS:
        gens.append((f"clw:{nm_w}", compress_spinor(word(e, idx))))
    for (i, j) in PAIRS:
        nm = f"sigma:{i},{j}"
        gens.append((nm, compress_spinor(sigma128(e, i, j))))
        adj_sign[nm] = -1 if ETA[i] * ETA[j] > 0 else +1
    for (i, j) in PAIRS:
        nm = f"frame:{i},{j}"
        gens.append((nm, compress_vector(Mvec14(i, j))))
        adj_sign[nm] = -1 if ETA[i] * ETA[j] > 0 else +1
    K_MD = compress_spinor(cxi)
    gens.append(("M_D", K_MD))
    print(f"  generator family: {len(gens)} compressed elements", flush=True)

    # adjoint closure (so that Hermitian combinations lie in the complexified algebra)
    worst_adj = 0.0
    for nm, K in gens:
        if nm in adj_sign:
            r = fnorm(K.conj().T - adj_sign[nm] * K)
        elif nm == "M_D":
            r = fnorm(K.conj().T - compress_spinor(cxi.conj().T))
        else:  # Clifford words: adjoint is +/- the same word
            r = min(fnorm(K.conj().T - K), fnorm(K.conj().T + K))
        worst_adj = max(worst_adj, r / (1.0 + fnorm(K)))
    check("generator family adjoint-closed (K^dag = +/-K or in-family element)",
          worst_adj < 1e-8, f"max rel residual {worst_adj:.2e}")

    # H-linearity on V for a class-covering subset (mathematically forced by ambient
    # H-linearity + [J, Pi] = 0; checked here as a numerical receipt)
    subset = ["cl:e0", "cl:e12", "clw:beta=e0..e8", "clw:omega=e0..e13",
              "sigma:0,1", "sigma:0,9", "sigma:12,13", "frame:0,1", "frame:0,9", "M_D"]
    gd = dict(gens)
    hl_v = max(hlV(gd[nm]) / (1.0 + fnorm(gd[nm])) for nm in subset)
    check("compressed generators H-linear on V (class-covering subset)",
          hl_v < 1e-7, f"max rel defect {hl_v:.2e}")

    # algebra-closure residual: random REAL-coefficient words of compressed generators
    rng = np.random.default_rng(7)
    Klist = [K for _, K in gens]
    worst_word = 0.0
    for _ in range(4):
        Wd = Klist[rng.integers(len(Klist))].copy()
        for _f in range(int(rng.integers(1, 3))):
            Wd = Wd @ Klist[rng.integers(len(Klist))]
        Wd = Wd + rng.standard_normal() * Klist[rng.integers(len(Klist))]
        worst_word = max(worst_word, hlV(Wd) / (1.0 + fnorm(Wd)))
    check("closure: random real words of compressed generators stay H-linear",
          worst_word < 1e-7, f"max rel defect {worst_word:.2e}")
    # corner-closure receipt at ambient level: products of compressions stay on V
    W_amb = (Pi @ np.kron(np.eye(N), e[0]) @ Pi) @ (Pi @ np.kron(np.eye(N), e[9]) @ Pi)
    corner = fnorm(W_amb - Pi @ W_amb @ Pi) / (1.0 + fnorm(W_amb))
    check("closure: products of compressions stay on the record sector",
          corner < 1e-10, f"rel residual {corner:.2e}")

    # -------------------------------------------- [4] commutant of A on V (main step)
    print("== [4] commutant of A on V: spectral-graph certificate ==", flush=True)
    mingap1, spread1, nc1, labels1, sep1 = graph_commutant(Klist, NV, seed=101)
    check("H1 has simple spectrum (seed 101)", mingap1 > 1e-10 * spread1,
          f"min gap {mingap1:.3e}, spread {spread1:.3e}")
    check("component count stable across edge thresholds 1e-4/1e-6/1e-8 (seed 101)",
          len(set(nc1.values())) == 1, str(nc1))
    print(f"  seed 101: dim_C commutant = {nc1[1e-6]}; edge separation: largest sub-threshold "
          f"rel entry {sep1[0]:.2e}, smallest supra-threshold {sep1[1]:.2e}", flush=True)
    rng2 = np.random.default_rng(555)
    sub_idx = rng2.choice(len(Klist), size=22, replace=False)
    Ksub = [Klist[i] for i in sub_idx]
    mingap2, spread2, nc2, _, sep2 = graph_commutant(Ksub, NV, seed=202)
    check("H1 has simple spectrum (seed 202, independent 22-generator subfamily)",
          mingap2 > 1e-10 * spread2, f"min gap {mingap2:.3e}")
    check("component count stable across thresholds (seed 202)",
          len(set(nc2.values())) == 1, str(nc2))
    check("independent replication: both seeds give the same commutant dimension",
          nc1[1e-6] == nc2[1e-6], f"{nc1[1e-6]} vs {nc2[1e-6]}")
    dimC = nc1[1e-6]
    dimR = 4 * dimC
    print(f"  ==> dim_C commutant = {dimC};  real commutant dim_R = 2*dimC + 2*dimC = {dimR}",
          flush=True)

    # ------------------------------------------------ [5] tensor-shortcut cross-check
    print("== [5] ambient tensor-shortcut cross-check ==", flush=True)
    Ks128 = [e[a] for a in range(N)] + [sigma128(e, i, j) for (i, j) in PAIRS] \
        + [word(e, idx) for _, idx in WORDS] + [cxi]
    mg128, sp128, nc128, _, _ = graph_commutant(Ks128, DIM, seed=303)
    check("spinor factor: commutant of Cl(9,5) on C^128 is C.I",
          mg128 > 1e-10 * sp128 and set(nc128.values()) == {1}, str(nc128))
    print("  => anything commuting with I (x) Cl(9,5) has the form Y (x) (H-linear scalar):",
          flush=True)
    print("     complex-linear part Y (x) I, antilinear part Y' (x) I . J  (J = quaternionic)",
          flush=True)
    pairs_all = [(i, j) for i in range(N) for j in range(i + 1, N)]
    Lb = []
    for (i, j) in pairs_all:
        M = Mvec14(i, j)
        Lm = np.zeros((N * N, N * N))
        for p in range(N):
            for q in range(N):
                Yb = np.zeros((N, N))
                Yb[p, q] = 1.0
                Lm[:, p * N + q] = (Yb @ M - M @ Yb).ravel()
        Lb.append(Lm)
    sv = np.linalg.svd(np.vstack(Lb), compute_uv=False)
    nullity = int((sv < 1e-10 * sv[0]).sum())
    check("frame step: {Y : [Y, so(9,5)] = 0} is 1-dimensional (Y = c I)",
          nullity == 1, f"nullity {nullity}")
    print("  => imposing the frame part forces Y = c I; the projector and M_D are H-linear",
          flush=True)
    print("     (defects above), so they impose nothing further: ambient commutant = H.I.",
          flush=True)

    # -------------------------------------------------- [6] Krein form on V, signature
    print("== [6] constructed Krein form on V: eta_14 (x) beta restricted ==", flush=True)
    tmpb = np.tensordot(beta, B.reshape(N, DIM, NV), axes=([1], [1]))   # (DIM, N, NV)
    tmpb = np.ascontiguousarray(tmpb.transpose(1, 0, 2))                # (N, DIM, NV)
    tmpb *= ETA[:, None, None]
    BV = Bc @ tmpb.reshape(N * DIM, NV)
    check("eta_V Hermitian", fnorm(BV - BV.conj().T) < 1e-8)
    evV = np.linalg.eigvalsh(0.5 * (BV + BV.conj().T))
    tolV = 1e-8 * float(np.abs(evV).max())
    pV = int((evV > tolV).sum())
    qV = int((evV < -tolV).sum())
    mineig = float(np.abs(evV).min())
    check("eta_V nondegenerate on V", mineig > 1e-8, f"min |eig| = {mineig:.3e}")
    check("signature counts fill V", pV + qV == NV, f"({pV},{qV})")
    print(f"  signature(eta_V) = ({pV}, {qV});  min |eig| = {mineig:.3e}", flush=True)

    # ------------------------------- [7] Prop-1 existence leg: non-compactness witness
    print("== [7] Prop-1 existence leg: unbounded direction inside the algebra ==", flush=True)
    I128c = np.eye(DIM, dtype=complex)
    rates = {}
    for nm, (i, j) in [("boost(0,9)", (0, 9)), ("rotation(0,1)", (0, 1))]:
        Damb = np.kron(Mvec14(i, j).astype(complex), I128c) \
            + np.kron(np.eye(N, dtype=complex), sigma128(e, i, j))
        DB = Damb @ B
        inv_res = fnorm(DB - Pi @ DB)
        check(f"diagonal {nm} preserves V (ker Gamma is diag-so(9,5) invariant)",
              inv_res < 1e-7, f"residual {inv_res:.2e}")
        DV = Bc @ DB
        SkV = BV @ DV
        skew = fnorm(SkV + SkV.conj().T) / (1.0 + fnorm(SkV))
        check(f"{nm} is eta_V-skew (one-parameter subgroup lies in O(eta_V))",
              skew < 1e-7, f"rel residual {skew:.2e}")
        rngv = np.random.default_rng(17)
        v = rngv.standard_normal(NV) + 1j * rngv.standard_normal(NV)
        v /= fnorm(v)
        incs = []
        for _step in range(40):
            v = expv(DV, v)
            nrm = fnorm(v)
            incs.append(np.log(nrm))
            v /= nrm
        rates[nm] = float(np.mean(incs[-10:]))
        print(f"  {nm}: log-growth rate of ||exp(t D) v|| ~ {rates[nm]:+.6f} per unit t",
              flush=True)
    K_D_alg = gd["frame:0,9"] + gd["sigma:0,9"]
    DV_boost = Bc @ ((np.kron(Mvec14(0, 9).astype(complex), I128c)
                      + np.kron(np.eye(N, dtype=complex), sigma128(e, 0, 9))) @ B)
    check("the unbounded boost direction is IN the constructed algebra "
          "(compressed frame + compressed sigma)",
          fnorm(DV_boost - K_D_alg) < 1e-8, f"residual {fnorm(DV_boost - K_D_alg):.2e}")
    check("boost flow unbounded on V (finite non-compactness WITNESS)",
          rates["boost(0,9)"] > 0.1, f"rate {rates['boost(0,9)']:.4f}")
    check("rotation flow bounded on V (compact contrast control)",
          abs(rates["rotation(0,1)"]) < 1e-8, f"rate {rates['rotation(0,1)']:.2e}")

    # ----------------------------------------------------------------- [8] verdict
    print("=" * 78)
    print("VERDICT — M-C3 Krein-sign trichotomy input (exact finite computation)")
    print("=" * 78)
    print(f"  dim_C commutant of A on ker Gamma (1664-dim record sector) : {dimC}")
    if dimC == 1:
        print(f"  real commutant: dim_R {dimR} = span_R{{I, iI, J, iJ}}  ~  H . I")
        print("  => V is IRREDUCIBLE over H under the constructed algebra A.")
        print("  Theorem-2 residual-family dimension:")
        print("      sum_lambda dim_R(D_lambda) a_lambda b_lambda = 0    (NO residual family)")
        print("  Complex-linear involutions in the commutant: {+I, -I} only.")
        print("  Antilinear elements (c J) square to -|c|^2 <= 0: no antilinear involution")
        print("  (the step10/step11 quaternionic Kramers wall at observable-algebra level).")
        if qV == 0:
            branch = "SINGLETON: F = {+I} (eta_V positive definite)"
        elif pV == 0:
            branch = "SINGLETON: F = {-I} (eta_V negative definite)"
        else:
            branch = (f"F = EMPTY for the constructed pair (A, eta_V): eta_V indefinite "
                      f"({pV},{qV}), the only candidates +/-I both fail positivity")
        print(f"  Existence leg against the constructed Krein form: {branch}")
        print(f"  Prop-1 consistency: A contains an eta_V-orthogonal one-parameter boost")
        print(f"  subgroup with witnessed exponential growth (rate ~ "
              f"{rates['boost(0,9)']:.3f}); by the necessity leg of Prop 1, any invariance")
        print("  group containing it admits no positivity-majorant on this carrier.")
        print("  TRICHOTOMY INPUT: classification leg = at most one admissible fundamental")
        print("  symmetry (no residual family; no free Z/2, no continuum); existence leg on")
        print("  the KINEMATIC carrier = EMPTY (non-compact/firewall branch).  A dynamical")
        print("  good-stable reduction to a positivity-admitting stabilizer (open W219)")
        print("  is what could move existence from EMPTY to SINGLETON; nothing here builds it.")
    else:
        print(f"  REDUCIBLE branch: dim_C commutant = {dimC} > 1; component data follow.")
        sizes = np.bincount(labels1)
        print(f"  component sizes: {sorted(sizes.tolist(), reverse=True)}")
        for ci in range(dimC):
            mask = labels1 == ci
            sub = BV[np.ix_(mask, mask)]
            evc = np.linalg.eigvalsh(0.5 * (sub + sub.conj().T))
            tc = 1e-8 * float(np.abs(evc).max())
            print(f"    component {ci}: dim {int(mask.sum())}, "
                  f"eta_V-signature ({int((evc > tc).sum())},{int((evc < -tc).sum())})")
        print("  Sigma-formula evaluation requires the per-type signature split across")
        print("  equivalent components; report the data above as the residual-family input.")
    print("-" * 78)
    print("MANDATORY FENCES (verbatim):")
    print("  (1) this computes the commutant of the CONSTRUCTED algebra on the KINEMATIC")
    print("      carrier; whether this is GU's physical observable algebra is exactly the")
    print("      open dynamical-stabilizer question (W219);")
    print("  (2) no verdict, bar(b), H59, or claim-status change is made by this probe —")
    print("      per Joe's 2026-08-03 standing rule, moving any such bar additionally")
    print("      requires a hostile field-specialist review, which has not happened;")
    print('  (3) irreducible ⇒ "sign forced IF this is the observable algebra";')
    print("      reducible ⇒ report the computed Σ dim formula value as the size of the")
    print("      residual family.")
    print("-" * 78)

    # REGRESSION PINS (observed on the 2026-08-03 run; pins of the computed result,
    # not assumptions — remove only with a recorded re-derivation)
    assert dimC == 1, "regression pin: complex commutant was C.I on 2026-08-03"
    assert dimR == 4, "regression pin: real commutant was H.I (dim_R 4) on 2026-08-03"
    assert (pV, qV) == (832, 832), "regression pin: signature(eta_V) was (832,832)"
    assert rates["boost(0,9)"] > 1.0, "regression pin: boost growth rate was ~1.5"

    print(f"[summary] {_n_checks[0]} checks passed; elapsed {time.time() - t0:.0f}s; exit 0",
          flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
