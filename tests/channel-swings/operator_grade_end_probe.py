#!/usr/bin/env python3
"""OPERATOR-GRADE END FAMILY (summit wave, 2026-07-20) -- ONE discretized
L^2-grade collar operator answering Q-A (norm-resolvent boundary value of
M_op (q_op + i delta)^{-1/2}: exists? deck-odd?) and Q-B (the +-i0
orientation bit at operator grade: gauge or data?).

CHANNEL: big swing (Joe direct chat, 2026-07-20: operator-grade end family).
DESIGN:  explorations/operator-grade-end-2026-07-20.md (pre-declared
         outcome branches written to file BEFORE this probe computed).
EXTENDS: replicates the n2/sector end-model machinery (same conventions;
         those files are not touched). REFINEMENT LADDER NRES in
         {64,128,256} is the honesty instrument: every operator-grade
         number is reported as a convergence column (value per NRES +
         trend), never a single-N number.

THE OPERATOR (doubled internal space C^2 x C^128, smatrix precedent):
    G_col = sigma2 x I               (collar Clifford element, Hermitian)
    D_op  = P_N x G_col + blkdiag(sigma1 x c(xi(t,s_j)))
    P_N   = -i d/ds (central difference, Dirichlet: Hermitian)
    K_op  = I_N x I_2 x K_S          (K_S lifted pointwise)
K-self-adjointness K_op D_op K_op = D_op^dag is exact by construction.
Section objects lifted pointwise (multiplication operators): Ku_op, q_op;
M_op = Ku_op D_op;  N_delta,op = M_op (q_op + i delta)^{-1/2}.

Q-A modes measured (successive-delta differences, per NRES):
  (i)   plain operator norm ||N_d - N_d'||           (sup mode)
  (ii)  norm-resolvent ||(N_d - z)^-1 - (N_d' - z)^-1||, z = 2i
  (iii) graph-relative ||(N_d - N_d')(D_op - 2i)^-1||
Deterministic; numpy + scipy.sparse; no RNG.
"""
from __future__ import annotations

import os
import sys
import time

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "generation-sector"))
import gen_sector_bridge as gb  # noqa: E402
import oq_rk1_cl95_explicit_rep as cl95  # noqa: E402

N_DIRS, DIM = 14, 128
ETA = np.array([1.0] * 9 + [-1.0] * 5)
LAM = 0.5
RESULTS = []
T0 = time.time()


def check(tag, name, ok, detail=""):
    RESULTS.append((tag, name, bool(ok)))
    line = f"[{tag}] {'PASS' if ok else 'FAIL'}  {name}"
    if detail:
        line += f"   ({detail})"
    print(line, flush=True)
    return ok


def log(msg):
    print(f"    .. {msg}  [t={time.time()-T0:7.1f}s]", flush=True)


# --- verified Clifford objects + doubling -------------------------------------
e = gb.gammas()
K_S = e[0].copy()
for a in range(1, 9):
    K_S = K_S @ e[a]
XI = np.real(np.asarray(gb.XI)).astype(float)
I128 = np.eye(DIM, dtype=complex)
S1 = np.array([[0, 1], [1, 0]], dtype=complex)
S2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
I2 = np.eye(2, dtype=complex)
G_COL = np.kron(S2, I128)            # Hermitian collar element
K_DBL = np.kron(I2, K_S)             # doubled Krein structure
OM = I128.copy()
for a in range(N_DIRS):
    OM = OM @ e[a]                   # orientation conjugator core
U_h = e[0] @ e[3] @ e[4] @ e[9] @ e[11] @ e[12]
U_ss = e[0] @ e[1] @ e[4] @ e[5] @ e[10] @ e[11]

# J_quat (identical construction to the n2/m1/sector probes)
G_raw = cl95.jordan_wigner_gammas(7)
r_sign, sigma_s = [], []
for a in range(N_DIRS):
    real_g = float(np.max(np.abs(np.conj(G_raw[a]) - G_raw[a]))) < 1e-12
    r_sign.append(+1 if real_g else -1)
    sigma_s.append(r_sign[a] if a < 9 else -r_sign[a])
S_even = [a for a in range(N_DIRS) if sigma_s[a] == -1]
S_odd = [a for a in range(N_DIRS) if sigma_s[a] == +1]
S_pick = S_even if len(S_even) % 2 == 0 else S_odd
C_J = I128.copy()
for a in S_pick:
    C_J = C_J @ G_raw[a]


def cvec(v):
    return sum(v[a] * e[a] for a in range(N_DIRS))


def qform(v):
    return float(np.real(np.vdot(v, ETA * v)))


# --- end-model machinery (REPLICATED from n2/sector probes; same conventions) --
SYM_IDX = [(0, 0), (1, 1), (2, 2), (3, 3),
           (0, 1), (0, 2), (1, 2), (0, 3), (1, 3), (2, 3)]


def sym_mat(i):
    a, b = SYM_IDX[i]
    m = np.zeros((4, 4))
    if a == b:
        m[a, a] = 1.0
    else:
        m[a, b] = m[b, a] = 1.0 / np.sqrt(2.0)
    return m


HMODES = [sym_mat(i) for i in range(10)]


def fixsign(v):
    k = int(np.argmax(np.abs(v)))
    return v if v[k] > 0 else -v


def frame_diag(a4, lam=LAM):
    a0, a1, a2, a3 = [float(x) for x in a4]
    F = np.zeros((14, 14))
    F[0, 0] = 1.0 / np.sqrt(a0)
    F[1, 1] = 1.0 / np.sqrt(a1)
    F[2, 2] = 1.0 / np.sqrt(a2)
    F[3, 9] = 1.0 / np.sqrt(a3)
    F[8, 3] = np.sqrt(a0 * a1)
    F[9, 4] = np.sqrt(a0 * a2)
    F[10, 5] = np.sqrt(a1 * a2)
    F[11, 10] = np.sqrt(a0 * a3)
    F[12, 11] = np.sqrt(a1 * a3)
    F[13, 12] = np.sqrt(a2 * a3)
    u = np.array([1.0 / a0, 1.0 / a1, 1.0 / a2, -1.0 / a3])
    M4 = np.diag(u * u) - lam * np.outer(u, u)
    w, V = np.linalg.eigh(M4)
    refs = np.array([[1., -1., 0., 0.], [0., 1., -1., 0.],
                     [0., 0., 1., -1.], [1., 1., 1., 1.]]).T
    k0 = 0
    while k0 < 4:
        k1 = k0 + 1
        while k1 < 4 and abs(w[k1] - w[k0]) <= 1e-9 * max(1.0, abs(w[k0])):
            k1 += 1
        if k1 - k0 > 1:
            Pp = V[:, k0:k1]
            B = []
            for r in refs.T:
                v = Pp @ (Pp.T @ r)
                for b in B:
                    v = v - b * float(b @ v)
                nv = float(np.linalg.norm(v))
                if nv > 1e-8:
                    B.append(v / nv)
                if len(B) == k1 - k0:
                    break
            V[:, k0:k1] = np.stack(B, axis=1)
        k0 = k1
    pos = [k for k in range(4) if w[k] > 0]
    neg = [k for k in range(4) if w[k] < 0]
    if len(pos) != 3 or len(neg) != 1:
        raise ValueError(f"diag block signature not (3,1): {w}")
    for j, k in enumerate(pos):
        F[4:8, 6 + j] = fixsign(V[:, k]) / np.sqrt(w[k])
    F[4:8, 13] = fixsign(V[:, neg[0]]) / np.sqrt(-w[neg[0]])
    return F


def rot4(th):
    R = np.eye(4)
    R[0, 0] = R[3, 3] = np.cos(th)
    R[0, 3] = -np.sin(th)
    R[3, 0] = np.sin(th)
    return R


def rho(R):
    P = np.zeros((14, 14))
    P[:4, :4] = R
    for i in range(10):
        RhR = R @ HMODES[i] @ R.T
        for j in range(10):
            P[4 + j, 4 + i] = float(np.sum(RhR * HMODES[j]))
    return P


F_BASE = frame_diag((1.0, 1.0, 1.0, 1.0))
XI_VEC = F_BASE @ XI


def xi_of(t, a4, lam=LAM):
    F = rho(rot4(np.pi * t)) @ frame_diag(a4, lam)
    return np.linalg.solve(F, XI_VEC)


def ray(alpha, s):
    al = np.asarray(alpha, dtype=float)
    return tuple(np.exp(2.0 * al * s))


A_CONF_UP = (1.0, 1.0, 1.0, 1.0)
A_CONF_DN = (-1.0, -1.0, -1.0, -1.0)
TGRID = np.linspace(0.0, 1.0, 41)


def q_profile(alpha, s):
    a4 = ray(alpha, s)
    return np.array([qform(xi_of(t, a4)) for t in TGRID])


def crossing_scan(alpha, s_hi):
    for s in np.linspace(0.0, s_hi, 61):
        q = q_profile(alpha, s)
        if np.min(q) < 0.0:
            t_star = float(TGRID[int(np.argmin(q))])
            return float(s), t_star
    return None, None


def bisect_wall(alpha, t_star, s_hi):
    lo, hi = 0.0, s_hi
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if qform(xi_of(t_star, ray(alpha, mid))) > 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


# --- section objects, pointwise (from {D, K_S} alone) --------------------------
def sec_parts(D):
    cs = 0.5 * (D + K_S @ D @ K_S)
    ct = D - cs
    P = float(np.real(np.trace(cs @ cs))) / DIM
    T = -float(np.real(np.trace(ct @ ct))) / DIM
    return cs, ct, P, T, P - T


def a_density(D):
    cs, ct, P, T, _q = sec_parts(D)
    s_E = P + T
    return (26.0 / 7.0) * s_E * I128 + (4.0 / 7.0) * (cs @ ct)


# =============================================================================
# [T] geometry of the minimal configuration
# =============================================================================
s0, t0 = crossing_scan(A_CONF_DN, 3.0)
s_star = bisect_wall(A_CONF_DN, t0, s0 + 0.2)
check("T", "minimal configuration located: conf-down ray crosses; wall "
           "radius s* bisected at fixed t*",
      s0 is not None and 0 < s_star < 3.0, f"s* = {s_star:.4f}, t* = {t0:.3f}")

# deep-wall configuration: the operator window must contain its wall
# INTERIOR to the collar (s > 0) and away from the Dirichlet ends; choose
# the loop coordinate whose wall radius is nearest 0.6 (a named geometric
# choice, not a tuning: the ray class and the wall are the family's own)
def wall_radius(t, s_hi=1.5):
    svals = np.linspace(0.0, s_hi, 61)
    qv = [qform(xi_of(t, ray(A_CONF_DN, s))) for s in svals]
    if qv[0] <= 0 or min(qv) > 0:
        return None
    j = next(i for i in range(1, len(qv)) if qv[i] < 0)
    lo, hi = svals[j - 1], svals[j]
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if qform(xi_of(t, ray(A_CONF_DN, mid))) > 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


T_OP, S_STAR_OP, best = t0, s_star, 1e9
for tt in np.linspace(t0 - 0.25, t0 + 0.25, 101):
    sw = wall_radius(float(tt))
    if sw is not None and abs(sw - 0.6) < best:
        best, T_OP, S_STAR_OP = abs(sw - 0.6), float(tt), sw
S_LO, S_HI = S_STAR_OP - 0.4, S_STAR_OP + 0.4
eps = 1e-4
QPRIME = (qform(xi_of(T_OP, ray(A_CONF_DN, S_STAR_OP + eps)))
          - qform(xi_of(T_OP, ray(A_CONF_DN, S_STAR_OP - eps)))) / (2 * eps)
qs_c = [qform(xi_of(T_OP, ray(A_CONF_DN, s)))
        for s in np.linspace(S_LO, S_HI, 41)]
qs_g = [qform(xi_of(T_OP, ray(A_CONF_UP, s)))
        for s in np.linspace(0.0, 1.2, 41)]
Ps_c = [sec_parts(cvec(xi_of(T_OP, ray(A_CONF_DN, s))))[2]
        for s in np.linspace(S_LO, S_HI, 9)]
sgn = np.sign(qs_c)
check("T", "operator windows: crossing collar spans its wall interior to "
           "the collar (single sign change, s > 0 throughout), gapped "
           "control collar has q > 0 throughout, P > 0 on both",
      int(np.sum(np.abs(np.diff(sgn)) > 0)) == 1 and S_LO > 0
      and min(qs_g) > 0 and min(Ps_c) > 0,
      f"t_op = {T_OP:.4f}, s*_op = {S_STAR_OP:.4f}, dq/ds|wall = "
      f"{QPRIME:.2f}; q ends ({qs_c[0]:.3f}, {qs_c[-1]:.3f}); "
      f"gapped min q {min(qs_g):.3f}")

xa = xi_of(0.25, ray(A_CONF_DN, s_star + 0.3))
xb = xi_of(1.25, ray(A_CONF_DN, s_star + 0.3))
deck_cov = float(np.max(np.abs(U_h @ cvec(xa) @ np.linalg.inv(U_h) - cvec(xb))))
check("T", "pointwise deck covariance on the collar: U_h c(xi(t,s)) U_h^-1 "
           "= c(xi(t+1,s)) and U_h K_S U_h^-1 = -K_S (the twist survives "
           "pointwise -- premise of operator-grade deck-oddness)",
      deck_cov < 1e-9
      and float(np.max(np.abs(U_h @ K_S @ np.linalg.inv(U_h) + K_S))) < 1e-12,
      f"covariance defect {deck_cov:.1e}")


# =============================================================================
# the operator builder (resolution NRES; sparse block-tridiagonal)
# =============================================================================
def build_ops(alpha, t, s_lo, s_hi, nres):
    """D_op, M_op, q-vector, per-point section data on the collar."""
    hstep = (s_hi - s_lo) / (nres + 1)
    sj = s_lo + hstep * np.arange(1, nres + 1)
    Ds, Kus, qs, Ans = [], [], [], []
    for s in sj:
        D = cvec(xi_of(t, ray(alpha, float(s))))
        cs, _ct, P, _T, q = sec_parts(D)
        Ds.append(D)
        Kus.append(K_S @ cs / np.sqrt(P))
        qs.append(q)
        Ans.append(a_density(D))
    qs = np.array(qs)
    Pn = sp.diags([np.full(nres - 1, 1.0), np.full(nres - 1, -1.0)], [1, -1],
                  format="csr") * (-1j / (2 * hstep))
    DER = sp.kron(Pn, sp.csr_matrix(G_COL), format="csr")
    SYM = sp.block_diag([sp.csr_matrix(np.kron(S1, D)) for D in Ds],
                        format="csr")
    D_op = (DER + SYM).tocsr()
    KU = sp.block_diag([sp.csr_matrix(np.kron(I2, Ku)) for Ku in Kus],
                       format="csr")
    M_op = (KU @ D_op).tocsr()
    return dict(h=hstep, sj=sj, qs=qs, Ds=Ds, Kus=Kus, Ans=Ans,
                D_op=D_op, M_op=M_op, nres=nres)


def fvec(qs, delta):
    """(q + i delta)^(-1/2), one global principal branch, per grid point."""
    return 1.0 / np.sqrt(qs + 1j * delta)


def scale_cols(M_op, fs):
    d = np.repeat(fs, 256)
    return (M_op @ sp.diags(d)).tocsr()


def opnorm(A, iters=70):
    """Largest singular value via deterministic power iteration on A^dag A
    (accuracy ~1%, sufficient for rate columns; svds with tight tol stalls
    on the clustered spectra here -- named numerical-analyst decision)."""
    n = A.shape[0]
    v = np.cos(0.7 * np.arange(n)) + 0.31j * np.sin(1.3 * np.arange(n) + 0.4)
    v /= np.linalg.norm(v)
    ismat = hasattr(A, "tocsr") or isinstance(A, np.ndarray)
    if ismat:
        Ah = A.conj().T.tocsr() if hasattr(A, "tocsr") else A.conj().T
        mv, rmv = (lambda x: A @ x), (lambda x: Ah @ x)
    else:
        mv, rmv = A.matvec, A.rmatvec
    s = 0.0
    for _ in range(iters):
        w = rmv(mv(v))
        s = float(np.linalg.norm(w))
        if s == 0.0:
            return 0.0
        v = w / s
    return float(np.sqrt(s))


class BlockTriLU:
    """Block-Thomas LU for block-tridiagonal sparse matrices with dense
    bs x bs blocks (the operator structure here). splu's fill on these
    matrices is catastrophic; this is the structure-honest solver.
    Holds factorizations of A and A^H so trans='N'/'H' solves are exact."""

    def __init__(self, Asp, nres, bs=256):
        from scipy.linalg import lu_factor, lu_solve
        self._lu_solve = lu_solve
        self.n, self.bs = nres, bs
        A = Asp.tocsr()

        def blocks(M):
            dg, up, lo = [], [], []
            for j in range(nres):
                s = slice(j * bs, (j + 1) * bs)
                dg.append(M[s, s].toarray())
                up.append(M[s, j * bs + bs:j * bs + 2 * bs].toarray()
                          if j < nres - 1 else None)
                lo.append(M[s, j * bs - bs:j * bs].toarray()
                          if j > 0 else None)
            return dg, up, lo

        self.f = {}
        for key, M in (("N", A), ("H", A.conj().T.tocsr())):
            dg, up, lo = blocks(M)
            Ls, Ss = [None], [lu_factor(dg[0])]
            for j in range(1, nres):
                # L_j = C_j S_{j-1}^{-1}  via  S^T X^T = C^T (pure transpose)
                Lj = self._lu_solve(Ss[j - 1], lo[j].T, trans=1).T
                Ls.append(Lj)
                Ss.append(lu_factor(dg[j] - Lj @ up[j - 1]))
            self.f[key] = (Ls, Ss, up)

    def solve(self, b, trans="N"):
        Ls, Ss, up = self.f[trans]
        n, bs = self.n, self.bs
        y = np.empty_like(b, dtype=complex)
        for j in range(n):
            seg = b[j * bs:(j + 1) * bs].astype(complex)
            if j > 0:
                seg = seg - Ls[j] @ y[(j - 1) * bs:j * bs]
            y[j * bs:(j + 1) * bs] = seg
        x = np.empty_like(y)
        for j in range(n - 1, -1, -1):
            seg = y[j * bs:(j + 1) * bs]
            if j < n - 1:
                seg = seg - up[j] @ x[(j + 1) * bs:(j + 2) * bs]
            x[j * bs:(j + 1) * bs] = self._lu_solve(Ss[j], seg)
        return x


def res_diff_norm(NA, NB, z=2.0j):
    n = NA.shape[0]
    nres = n // 256
    luA = BlockTriLU((NA - z * sp.identity(n)).tocsr(), nres)
    luB = BlockTriLU((NB - z * sp.identity(n)).tocsr(), nres)

    def mv(v):
        return luA.solve(v) - luB.solve(v)

    def rmv(v):
        return luA.solve(v, trans="H") - luB.solve(v, trans="H")

    L = spla.LinearOperator((n, n), matvec=mv, rmatvec=rmv, dtype=complex)
    return opnorm(L)


DELTAS = np.array([1.0, 0.3, 0.1, 0.03, 0.01, 0.003, 0.001])
NRES_LADDER = (64, 128, 256)


def slope(xs, ys):
    """log-log fitted slope of ys vs xs (least squares)."""
    xs, ys = np.log(np.asarray(xs)), np.log(np.asarray(ys))
    return float(np.polyfit(xs, ys, 1)[0])


def qa_battery(alpha, t, s_lo, s_hi, label, do_resolvent):
    """Q-A on one collar: convergence columns for the three modes."""
    cols = {}
    for nres in NRES_LADDER:
        log(f"{label}: building operators at NRES = {nres}")
        ops = build_ops(alpha, t, s_lo, s_hi, nres)
        M_op, qs, D_op = ops["M_op"], ops["qs"], ops["D_op"]
        n = M_op.shape[0]
        lu_D = BlockTriLU((D_op - (2.0 + 2.0j) * sp.identity(n)).tocsr(),
                          nres)
        normN, dplain, dgraph, dres = [], [], [], []
        for i, dl in enumerate(DELTAS):
            Nd = scale_cols(M_op, fvec(qs, dl))
            normN.append(opnorm(Nd))
            if i > 0:
                DF = scale_cols(M_op, fvec(qs, dl) - fvec(qs, DELTAS[i - 1]))
                DFh = DF.conj().T.tocsr()
                dplain.append(opnorm(DF))

                def gmv(v, DF=DF):
                    return DF @ lu_D.solve(v)

                def grmv(v, DFh=DFh):
                    return lu_D.solve(DFh @ v, trans="H")

                L = spla.LinearOperator((n, n), matvec=gmv, rmatvec=grmv,
                                        dtype=complex)
                dgraph.append(opnorm(L))
                if do_resolvent:
                    try:
                        Ndp = scale_cols(M_op, fvec(qs, DELTAS[i - 1]))
                        dres.append(res_diff_norm(Nd, Ndp))
                        del Ndp
                    except Exception as ex:
                        print(f"    !! resolvent mode failed at NRES={nres} "
                              f"delta={dl:g}: {ex}", flush=True)
                        dres.append(float("nan"))
            log(f"{label} NRES={nres} delta={dl:g}: ||N_d|| = {normN[-1]:.4g}"
                + (f", dplain = {dplain[-1]:.4g}, dgraph = {dgraph[-1]:.4g}"
                   if i > 0 else "")
                + (f", dres = {dres[-1]:.4g}" if i > 0 and do_resolvent
                   else ""))
        cols[nres] = dict(normN=normN, dplain=dplain, dgraph=dgraph,
                          dres=dres, minq=float(np.min(np.abs(qs))))
        del ops, lu_D
    return cols


def deck_battery(alpha, t, s_lo, s_hi, nres, delta):
    """||U N_d(t) U^-1 + N_d(t+1)||_max-entry / scale, at one (NRES, delta)."""
    ops0 = build_ops(alpha, t, s_lo, s_hi, nres)
    ops1 = build_ops(alpha, t + 1.0, s_lo, s_hi, nres)
    U = sp.block_diag([sp.csr_matrix(np.kron(I2, U_h))] * nres, format="csr")
    Ui = sp.block_diag([sp.csr_matrix(np.kron(I2, np.linalg.inv(U_h)))] * nres,
                       format="csr")
    N0 = scale_cols(ops0["M_op"], fvec(ops0["qs"], delta))
    N1 = scale_cols(ops1["M_op"], fvec(ops1["qs"], delta))
    R = (U @ N0 @ Ui + N1).tocoo()
    scale = max(1.0, float(np.max(np.abs(N0.data))))
    dq = float(np.max(np.abs(ops0["qs"] - ops1["qs"])))
    return (float(np.max(np.abs(R.data))) / scale if R.nnz else 0.0), dq


def stage1():
    print("\n=== STAGE 1: Q-A (the section theorem at operator grade) ===",
          flush=True)
    colsG = qa_battery(A_CONF_UP, T_OP, 0.0, 1.2, "gapped",
                       do_resolvent=False)
    colsC = qa_battery(A_CONF_DN, T_OP, S_LO, S_HI, "crossing",
                       do_resolvent=True)

    # gapped control: every mode Cauchy with positive delta-rate at every NRES
    okG = all(slope(DELTAS[1:], c["dplain"]) > 0.5
              and slope(DELTAS[1:], c["dgraph"]) > 0.5
              and all(np.diff(c["dplain"]) < 0)
              for c in colsG.values())
    det = "; ".join(f"N{n}: plain slope {slope(DELTAS[1:], c['dplain']):.2f}, "
                    f"graph slope {slope(DELTAS[1:], c['dgraph']):.2f}"
                    for n, c in colsG.items())
    check("E", "Q-A gapped control: N_delta,op is delta-Cauchy in PLAIN and "
               "GRAPH-RELATIVE norm at every resolution with positive fitted "
               "rate (the boundary value exists trivially off the wall)", okG,
          det)

    # crossing collar: report the mode structure
    pl_slopes = {n: slope(DELTAS[1:], c["dplain"]) for n, c in colsC.items()}
    gr_slopes = {n: slope(DELTAS[1:], c["dgraph"]) for n, c in colsC.items()}
    rs_slopes = {n: slope(DELTAS[1:], c["dres"]) for n, c in colsC.items()}
    nn = {n: c["normN"] for n, c in colsC.items()}
    print(f"    crossing plain-diff slopes per NRES: {pl_slopes}", flush=True)
    print(f"    crossing graph-diff slopes per NRES: {gr_slopes}", flush=True)
    print(f"    crossing resolvent-diff slopes per NRES: {rs_slopes}",
          flush=True)
    print(f"    crossing ||N_delta|| columns: {nn}", flush=True)
    return colsG, colsC, pl_slopes, gr_slopes, rs_slopes


def stage2(colsC):
    print("\n=== STAGE 2: Q-B (the +-i0 orientation bit at operator grade) "
          "===", flush=True)
    nres = 128
    ops = build_ops(A_CONF_DN, T_OP, S_LO, S_HI, nres)
    M_op, qs = ops["M_op"], ops["qs"]
    CJt_blk = sp.block_diag([sp.csr_matrix(np.kron(I2, C_J))] * nres,
                            format="csr")
    CJt_inv = sp.block_diag(
        [sp.csr_matrix(np.kron(I2, np.linalg.inv(C_J)))] * nres, format="csr")
    W_blk = sp.block_diag([sp.csr_matrix(np.kron(I2, OM))] * nres,
                          format="csr")
    W_inv = sp.block_diag([sp.csr_matrix(np.kron(I2, np.linalg.inv(OM)))]
                          * nres, format="csr")
    K_blk = sp.block_diag([sp.csr_matrix(K_DBL)] * nres, format="csr")

    # (b1) the antiunitary intertwiner lifts: J N_{+d} J^-1 = N_{-d} exactly
    dl = 0.003
    Np = scale_cols(M_op, fvec(qs, dl))
    Nm = scale_cols(M_op, fvec(qs, -dl))
    R = (CJt_blk @ Np.conj() @ CJt_inv - Nm).tocoo()
    sc = max(1.0, float(np.max(np.abs(Np.data))))
    b1 = (float(np.max(np.abs(R.data))) / sc) if R.nnz else 0.0
    jd = (CJt_blk @ ops["D_op"].conj() @ CJt_inv - ops["D_op"]).tocoo()
    b1d = (float(np.max(np.abs(jd.data))) if jd.nnz else 0.0)
    check("E", "Q-B: J_op = (I x J_quat) o conj COMMUTES with the full "
               "collar operator D_op (derivative term included) and maps "
               "the +i0 family onto the -i0 family exactly -- the "
               "matrix-grade intertwiner LIFTS to operator grade",
          b1 < 1e-10 and b1d < 1e-9,
          f"intertwiner defect {b1:.1e}; [J, D_op] defect {b1d:.1e}")

    # (b2) parity transfer at operator grade: W D_op(xi) W^-1 = D_op(-xi)
    SYMn = sp.block_diag([sp.csr_matrix(np.kron(S1, -D)) for D in ops["Ds"]],
                         format="csr")
    Pn = sp.diags([np.full(nres - 1, 1.0), np.full(nres - 1, -1.0)], [1, -1],
                  format="csr") * (-1j / (2 * ops["h"]))
    D_neg = (sp.kron(Pn, sp.csr_matrix(G_COL), format="csr") + SYMn).tocsr()
    wd = (W_blk @ ops["D_op"] @ W_inv - D_neg).tocoo()
    b2 = float(np.max(np.abs(wd.data))) if wd.nnz else 0.0
    # and the section family is xi-EVEN: M(-xi) = M, q(-xi) = q pointwise
    Dm = -ops["Ds"][nres // 2]
    csm, _c, Pm, _t, qm = sec_parts(Dm)
    Mm = (K_S @ csm / np.sqrt(Pm)) @ Dm
    M0 = ops["Kus"][nres // 2] @ ops["Ds"][nres // 2]
    # NOTE: M(-xi) at the same point vs M(xi): both computed pointwise
    b2b = float(np.max(np.abs(Mm - M0)))
    check("E", "Q-B: parity transfer lifts -- W = I x omega maps D_op(xi) "
               "to D_op(-xi) exactly (collar term W-invariant), and the "
               "section symbol is xi-EVEN pointwise (M(-xi) = M(xi)): the "
               "orientation flip cannot be soaked into the section datum, "
               "so the only exchanger of the +-i0 prescriptions among the "
               "lifted symmetries is the ANTIUNITARY J_op",
          b2 < 1e-9 and b2b < 1e-9,
          f"W-transfer defect {b2:.1e}; xi-evenness of M {b2b:.1e}")

    # (b3) the separator battery: conserved K_S-derivable readings, ladder
    print("    separator battery k_op(+d) vs k_op(-d), convergence column:",
          flush=True)
    seps = {}
    for nr in NRES_LADDER:
        op2 = build_ops(A_CONF_DN, T_OP, S_LO, S_HI, nr)
        # K_S-linear pairing channel in the doubled space: sigma1 x K_S
        # (the I2 x K_S channel is trace-blind to the sigma1-carried symbol
        # -- checked below as ks_blind; the sigma1 channel restricts to the
        # symbol-grade reading tr(K_S N A) pointwise)
        KX = sp.block_diag([sp.csr_matrix(np.kron(S1, K_S))] * nr,
                           format="csr")
        KI = sp.block_diag([sp.csr_matrix(K_DBL)] * nr, format="csr")
        A2 = sp.block_diag([sp.csr_matrix(np.kron(I2, A)) for A in op2["Ans"]],
                           format="csr")
        row = {}
        for dl2 in (0.01, 0.003, 0.001):
            Ndp2 = scale_cols(op2["M_op"], fvec(op2["qs"], dl2))
            Ndm2 = scale_cols(op2["M_op"], fvec(op2["qs"], -dl2))
            kp = 0.25 * (KX @ Ndp2 @ A2).diagonal().sum() / nr
            km = 0.25 * (KX @ Ndm2 @ A2).diagonal().sum() / nr
            kblind = 0.25 * abs((KI @ Ndp2 @ A2).diagonal().sum()) / nr
            row[dl2] = (complex(kp), complex(km), float(kblind))
        seps[nr] = row
        print(f"      NRES={nr}: " + "; ".join(
            f"d={d:g}: k+ = {v[0]:.6g}, k- = {v[1]:.6g}, blind = {v[2]:.1e}"
            for d, v in row.items()), flush=True)
    # separator verdict: Re parts equal (delta-even), Im parts conjugate-flip
    re_gap = max(abs(v[0].real - v[1].real) / max(1.0, abs(v[0].real))
                 for row in seps.values() for v in row.values())
    im_flip = max(abs(v[0].imag + v[1].imag) / max(1.0, abs(v[0].imag))
                  for row in seps.values() for v in row.values())
    ks_blind = max(v[2] for row in seps.values() for v in row.values())
    check("E", "Q-B separator structure at every resolution: the conserved "
               "K_S-derivable reading k_op (sigma1 x K_S channel, A-density "
               "paired) has Re k identical between the two prescriptions "
               "and Im k exactly conjugate-flipped -- the difference is "
               "precisely the J_op-image, i.e. the separator is MOVED BY A "
               "SYMMETRY OF THE FAMILY (gauge), not fixed by any "
               "K_S-derivable datum; the flat I2 x K_S channel is "
               "trace-blind (selection-rule consistency)",
          re_gap < 1e-9 and im_flip < 1e-9 and ks_blind < 1e-9,
          f"Re gap {re_gap:.1e}; Im anti-flip defect {im_flip:.1e}; "
          f"blind channel {ks_blind:.1e}")
    return seps


def stage1b():
    print("\n=== STAGE 1b: deck-oddness at operator grade (ladder) ===",
          flush=True)
    defects = {}
    for nr in NRES_LADDER:
        d, dq = deck_battery(A_CONF_DN, T_OP, S_LO, S_HI, nr, 0.001)
        defects[nr] = d
        log(f"deck defect NRES={nr}: {d:.2e} (q deck-invariance {dq:.2e})")
    check("E", "Q-A deck-oddness: U_h N_delta,op(t) U_h^-1 = -N_delta,op(t+1) "
               "at machine precision at EVERY resolution (inherited from "
               "exact pointwise covariance -- the deck statement survives "
               "the operator lift by algebra, not by limit)",
          max(defects.values()) < 1e-9,
          "; ".join(f"N{n}: {v:.1e}" for n, v in defects.items()))
    return defects


def classify_mode(diffs):
    """(label, rate): 'converges' if successive-delta diffs decrease
    monotonically (fitted log-log slope > 0.2), else 'diverges'/'flat'."""
    d = np.asarray(diffs)
    sl = slope(DELTAS4[1:], d)
    if np.all(np.diff(d) < 0) and sl > 0.2:
        return "converges", sl
    return ("diverges" if sl < -0.2 else "flat"), sl


DELTAS4 = np.array([0.1, 0.03, 0.01, 0.003])


def qa_small(alpha, t, s_lo, s_hi, nres):
    """Reduced Q-A battery for the stage-4 sweep: dplain/dgraph columns."""
    ops = build_ops(alpha, t, s_lo, s_hi, nres)
    n = ops["M_op"].shape[0]
    lu_D = BlockTriLU((ops["D_op"] - (2.0 + 2.0j) * sp.identity(n)).tocsr(),
                      nres)
    dplain, dgraph = [], []
    for i in range(1, len(DELTAS4)):
        DF = scale_cols(ops["M_op"],
                        fvec(ops["qs"], DELTAS4[i])
                        - fvec(ops["qs"], DELTAS4[i - 1]))
        DFh = DF.conj().T.tocsr()
        dplain.append(opnorm(DF))
        L = spla.LinearOperator(
            (n, n), matvec=lambda v, DF=DF: DF @ lu_D.solve(v),
            rmatvec=lambda v, DFh=DFh: lu_D.solve(DFh @ v, trans="H"),
            dtype=complex)
        dgraph.append(opnorm(L))
    return dplain, dgraph


def stage4():
    """Sampled corroboration over ~6 rays. Fresh NAMED seeded stream
    (default_rng(20260720), independent draws -- ray-class statistics
    corroborate n2's census shape; these are not the identical 53 rays)."""
    print("\n=== STAGE 4: sampled corroboration (~6 rays) ===", flush=True)
    rng = np.random.default_rng(20260720)
    configs = []

    def wall_at(alpha, t, s_hi=1.3):
        sv = np.linspace(0.02, s_hi, 53)
        qv = [qform(xi_of(t, ray(alpha, s))) for s in sv]
        if qv[0] <= 0 or min(qv) > 0:
            return None
        j = next(i for i in range(1, len(qv)) if qv[i] < 0)
        lo, hi = sv[j - 1], sv[j]
        for _ in range(50):
            mid = 0.5 * (lo + hi)
            (lo, hi) = (mid, hi) if qform(
                xi_of(t, ray(alpha, mid))) > 0 else (lo, mid)
        return 0.5 * (lo + hi)

    tries = 0
    while (sum(1 for c in configs if c[0] == "crossing") < 3
           or sum(1 for c in configs if c[0] == "gapped") < 2) and tries < 300:
        tries += 1
        al = rng.standard_normal(4)
        al = tuple(al / np.linalg.norm(al))
        qmins = [min(qform(xi_of(t, ray(al, s))) for t in TGRID[::4])
                 for s in (0.6, 1.2)]
        if min(qmins) > 0:
            if sum(1 for c in configs if c[0] == "gapped") < 2:
                configs.append(("gapped", al, 0.41, 0.1, 1.1))
            continue
        for t in TGRID[::2]:
            sw = wall_at(al, float(t))
            if sw is not None and 0.30 < sw < 0.90:
                qa = qform(xi_of(float(t), ray(al, sw - 0.35)))
                qb = qform(xi_of(float(t), ray(al, sw + 0.35)))
                if qa > 0 > qb and sum(
                        1 for c in configs if c[0] == "crossing") < 3:
                    configs.append(("crossing", al, float(t),
                                    sw - 0.35, sw + 0.35))
                break
    swb = wall_at((1.0, 0.0, 0.0, 1.0), 0.41)
    if swb and 0.3 < swb < 0.9:
        configs.append(("crossing", (1.0, 0.0, 0.0, 1.0), 0.41,
                        swb - 0.35, swb + 0.35))
    else:
        configs.append(("gapped", (1.0, 0.0, 0.0, 1.0), 0.41, 0.1, 1.1))
    log(f"stage-4 configs ({tries} draws): "
        + "; ".join(f"{c[0]} alpha=({', '.join(f'{a:.2f}' for a in c[1])}) "
                    f"t={c[2]:.2f}" for c in configs))

    ok_gap, ok_cross, ok_deck, rows = True, True, True, []
    for kind, al, t, s_lo, s_hi in configs[:6]:
        cols = {}
        for nres in (64, 128):
            cols[nres] = qa_small(al, t, s_lo, s_hi, nres)
        dk, _ = deck_battery(al, t, s_lo, s_hi, 64, 0.003)
        ok_deck &= dk < 1e-9
        clp = {n: classify_mode(c[0]) for n, c in cols.items()}
        clg = {n: classify_mode(c[1]) for n, c in cols.items()}
        gstab = abs(cols[128][1][-1] - cols[64][1][-1]) / max(
            1e-30, cols[128][1][-1])
        rows.append((kind, clp, clg, gstab, dk))
        log(f"{kind}: plain {clp}, graph {clg}, graph N-spread(last pair) "
            f"{gstab:.2f}, deck {dk:.1e}")
        if kind == "gapped":
            ok_gap &= (all(v[0] == "converges" for v in clg.values())
                       and gstab < 0.3)
        else:
            ok_cross &= all(v[0] == "converges" for v in clg.values())
    check("E", "STAGE-4 SAMPLED CORROBORATION: on a fresh seeded 6-ray "
               "sample (3 crossing + gapped + boost-class), the "
               "graph-relative mode converges on EVERY ray at every "
               "resolution (N-stable on gapped rays), and operator-grade "
               "deck-oddness is machine-exact on every ray -- the "
               "minimal-configuration mode structure is generic, not a "
               "ray accident",
          ok_gap and ok_cross and ok_deck and len(rows) >= 5,
          f"{len(rows)} rays; deck all < 1e-9: {ok_deck}")
    return rows


if __name__ == "__main__":
    if os.environ.get("OPGRADE_STAGE4"):
        stage4()
        bad = [r for r in RESULTS if not r[2]]
        print("\nHEADLINE (stage 4): sampled corroboration of the "
              "operator-grade mode structure on a fresh seeded 6-ray "
              "sample -- " + ("CORROBORATED" if not bad else "FAILED"),
              flush=True)
        print(f"\n{'ALL PASS' if not bad else 'FAILURES: ' + str(len(bad))}"
              f"  ({len(RESULTS)} checks)  [t={time.time()-T0:.1f}s]")
        sys.exit(0 if not bad else 1)
    colsG, colsC, _pl, _gr, _rs = stage1()
    deck_defects = stage1b()
    n_before = len(RESULTS)
    stage2(colsC)
    qb_ok = all(r[2] for r in RESULTS[n_before:])

    # ---- outcome adjudication (pre-declared branches, Section 0 of doc) ----
    res_ok_perN, res_last = {}, {}
    for nr, c in colsC.items():
        d = np.asarray(c["dres"])
        res_ok_perN[nr] = bool(np.all(np.diff(d) < 0)
                               and slope(DELTAS[1:], d) > 0.2)
        res_last[nr] = float(d[-1])
    vals = [res_last[n] for n in NRES_LADDER]
    res_uniform = max(vals) / max(1e-30, min(vals)) < 4.0
    deck_ok = max(deck_defects.values()) < 1e-9
    sup_ceiling = {n: c["normN"][-1] for n, c in colsC.items()}
    grow = np.log2(sup_ceiling[NRES_LADDER[-1]]
                   / sup_ceiling[NRES_LADDER[0]]) / np.log2(
        NRES_LADDER[-1] / NRES_LADDER[0])
    if all(res_ok_perN.values()) and res_uniform and deck_ok:
        qa = ("A1 -- the delta -> 0 boundary value EXISTS in the "
              "NORM-RESOLVENT sense (resolvent-difference columns Cauchy "
              "at every resolution, N-stable) and is DECK-ODD at machine "
              "precision at every resolution; the plain (uniform-norm) "
              "mode is the named NON-UNIFORM mode: ||N_delta,op|| "
              f"saturates to an N-growing ceiling ~ N^{grow:.2f} "
              "(h^{-1/2}-type wall blow-up)")
        qa_ok = True
    elif all(res_ok_perN.values()) and deck_ok:
        qa = ("A3 -- resolvent mode converges per-resolution but is NOT "
              "N-uniform: named divergence, theorem needs modification")
        qa_ok = True
    elif not deck_ok:
        qa = "A2 -- convergence without deck-oddness"
        qa_ok = False
    else:
        qa = "A3 -- no mode converges; named divergence columns printed"
        qa_ok = False
    check("E", "Q-A adjudication against the pre-declared branches "
               "(norm-resolvent columns per NRES + deck ladder)",
          qa_ok, f"res last-pair per NRES {res_last}; deck "
                 f"{max(deck_defects.values()):.1e}")
    print(f"\nQ-A OUTCOME: {qa}", flush=True)
    print("Q-B OUTCOME: " + ("B-GAUGE -- the matrix-grade intertwiners "
          "lift exactly (J_op and parity transfer commute with the collar "
          "term); the ONLY separator of the two prescriptions is Im k_op, "
          "which is exactly the J_op-image: scheme, not data; the "
          "classification stays Z/2" if qb_ok else
          "B-UNDECIDED/B-DATA -- see failed receipts"), flush=True)
    print("\nHEADLINE: operator-grade end family built (NRES = 64/128/256 "
          "refinement ladder, K-self-adjointness exact); Q-A = "
          + ("A1 (norm-resolvent boundary value exists, deck-odd exact)"
             if qa_ok and res_uniform else qa.split(" -- ")[0])
          + "; Q-B = " + ("GAUGE (Z/2 stands)" if qb_ok else "OPEN"),
          flush=True)
    bad = [r for r in RESULTS if not r[2]]
    print(f"\n{'ALL PASS' if not bad else 'FAILURES: ' + str(len(bad))}"
          f"  ({len(RESULTS)} checks)  [t={time.time()-T0:.1f}s]")
    sys.exit(0 if not bad else 1)
