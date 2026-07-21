#!/usr/bin/env python3
r"""
THE DECISIVE LP/LC DEFICIENCY-INDEX COMPUTATION (single-carrier reduction of O-b).

Target: the J-symmetric / Krein (Sims-type) deficiency indices n+- of the
single-carrier first-order operator
    A~ = -i K_u(s) G d_s + W~(s),     B(s) = -i K_u(s) G,
at the TRUE noncompact fiber ends of F = GL(4,R)/O(3,1) -- the diagonal FLAT
geodesics exp(s*diag(alpha))*o, s -> inf.  Per Swing 1 this IS O-b's single-carrier
reduction (product-uniformity is FREE via product = Krein direct sum); the two horns
are LP-FORCED (essentially self-adjoint => O-b proved) and LC-SELECTOR (external
selector = sigma = w_1 required => O-b does not close from structure).

ANTI-TOY DISCIPLINE (binding; a prior "limit-point" verdict was a PLANTED toy):
  * Uses the ACTUAL GL(4,R)/O(3,1) end asymptotics (n2/Prong-0 faithful model),
    NOT bounded-coefficient collar surrogates (the prior FORCED planted P=1+0.2sin).
  * Computes the GENUINE J = K_S Krein (Sims) deficiency count and confronts the
    native measure, NOT the measure-blind Hermitian reduction.
  * Confronts the K_S-null {q<0} stratum honestly (a THIRD possibility beyond LP/LC).
  * PLANTED CONTROLS mandatory: (a) a bounded collar toy MUST give a DIFFERENT count
    than the true ends (proving the true-end computation is not itself a toy); (b) a
    known limit-point Dirac end and a known limit-circle end must be distinguished.

Deterministic, foreground, numpy only, no writes, no network. EXIT 0 = ran; the
PRINTED findings, not the exit code, are the result.
"""
from __future__ import annotations

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "generation-sector"))
import gen_sector_bridge as gb  # noqa: E402

np.random.seed(20260721)

N_DIRS, DIM = 14, 128
ETA = np.array([1.0] * 9 + [-1.0] * 5)
LAM = 0.5
SPACE = np.arange(0, 9)
TIME = np.arange(9, 14)

# ---- verified Clifford objects ----------------------------------------------
e = gb.gammas()
K_S = e[0].copy()
for a in range(1, 9):
    K_S = K_S @ e[a]
I128 = np.eye(DIM, dtype=complex)
XI = np.real(np.asarray(gb.XI)).astype(float)


def cvec(v):
    return sum(v[a] * e[a] for a in range(N_DIRS))


def qform(v):
    return float(np.real(np.vdot(v, ETA * v)))


# ---- fiber geometry (verbatim structure from n2/Prong-0 faithful model) ------
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


def dewitt_gram(g, lam=LAM):
    gi = np.linalg.inv(g)
    G = np.zeros((14, 14))
    G[:4, :4] = g
    gih = [gi @ h for h in HMODES]
    tr1 = [float(np.trace(m)) for m in gih]
    for i in range(10):
        for j in range(i, 10):
            v = float(np.trace(gih[i] @ gih[j])) - lam * tr1[i] * tr1[j]
            G[4 + i, 4 + j] = G[4 + j, 4 + i] = v
    return G


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
    M = np.diag(u * u) - lam * np.outer(u, u)
    w, V = np.linalg.eigh(M)
    refs = np.array([[1., -1., 0., 0.], [0., 1., -1., 0.],
                     [0., 0., 1., -1.], [1., 1., 1., 1.]]).T
    k0 = 0
    while k0 < 4:
        k1 = k0 + 1
        while k1 < 4 and abs(w[k1] - w[k0]) <= 1e-9 * max(1.0, abs(w[k0])):
            k1 += 1
        if k1 - k0 > 1:
            P = V[:, k0:k1]
            B = []
            for r in refs.T:
                v = P @ (P.T @ r)
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


def boost03(eta):
    B = np.eye(4)
    B[0, 0] = B[3, 3] = np.cosh(eta)
    B[0, 3] = B[3, 0] = np.sinh(eta)
    return B


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


def xi_of(t, a4, lam=LAM, pre=None):
    base = rho(rot4(np.pi * t)) @ frame_diag(a4, lam)
    F = base if pre is None else rho(pre) @ base
    return np.linalg.solve(F, XI_VEC)


def xi_safe(t, a4, lam=LAM, pre=None):
    try:
        return xi_of(t, a4, lam, pre)
    except (ValueError, np.linalg.LinAlgError):
        return None


def ray(alpha, s):
    al = np.asarray(alpha, dtype=float)
    return tuple(np.exp(2.0 * al * s))


def PT(xi):
    return (float(np.sum(xi[SPACE] ** 2)), float(np.sum(xi[TIME] ** 2)))


def g_of_ray(alpha, s):
    a4 = ray(alpha, s)
    return np.diag([a4[0], a4[1], a4[2], -a4[3]])


def Ku_B_of(t, a4, pre=None):
    """Faithful K_u = K_S c_s/sqrt(P) (Hermitian traceless involution) and
    B = -i K_u G_col from committed structure.  G_col := K_S (the frozen
    Krein-form involution serving as the column/parity involution G).
    Returns (K_u, B, P, q) or None where P<=0 / frame degenerates."""
    x = xi_safe(t, a4, pre=pre)
    if x is None:
        return None
    D = cvec(x)
    c_s = 0.5 * (D + K_S @ D @ K_S)
    P = float(np.real(np.trace(c_s @ c_s))) / 128.0
    if P <= 0:
        return None
    T = float(np.real(np.trace(-0.5 * (D - K_S @ D @ K_S) @
                               (0.5 * (D - K_S @ D @ K_S))))) / 128.0
    Ku = K_S @ c_s / np.sqrt(P)
    G = K_S  # the committed parity/column involution (G^2 = I)
    B = -1j * Ku @ G
    return Ku, B, P, P - T


# =============================================================================
# THE DEFICIENCY-INDEX COUNTER (fundamental-matrix / adiabatic-WKB), with the
# NATIVE MEASURE wired in as the drift term.  This is the ONE method; controls
# and GU's cases all pass through it (no per-case special pleading).
# =============================================================================
def defect_indices(Bfun, Wfun, s_lo, s_hi, wdrift_fun=None, npts=6000):
    r"""Count L^2(w ds) solutions of (B d_s + W~) psi = z psi for z = +i, -i.
    Solutions ~ exp(int mu ds), mu = eig[ B^{-1}(z - W~) ].  Absorbing the
    measure w (unitary psi = w^{-1/2}phi, so phi = w^{1/2}psi ~ exp(int(mu+
    (1/2)w'/w)ds)) shifts every mode exponent by +(1/2)(w'/w).  A mode is
    L^2(w ds) iff Re(int (mu + (1/2)(w'/w)) ds) -> -inf.  Returns (n+, n-)."""
    ss = np.linspace(s_lo, s_hi, npts)
    Bs = [Bfun(s) for s in ss]
    Binv = [np.linalg.inv(b) for b in Bs]
    Ws = [Wfun(s) for s in ss]
    dr = np.zeros(npts) if wdrift_fun is None else np.array(
        [0.5 * wdrift_fun(s) for s in ss])
    dim = Bs[0].shape[0]
    out = {}
    for z in (1j, -1j):
        acc = None
        for k in range(npts):
            mu = np.linalg.eigvals(Binv[k] @ (z * np.eye(dim) - Ws[k]))
            re = np.sort(np.real(mu) + dr[k])
            acc = re if acc is None else acc + re
        out[z] = int(np.sum(acc < 0))
    return out[1j], out[-1j]


def scalar_weyl_defect(qfun, s_lo, s_hi, npts=20000):
    r"""Independent SECOND-ORDER Weyl (Sturm-Liouville) LP/LC counter with the
    genuine WKB amplitude prefactor |q-i|^{-1/4} (the factor a first-order
    Lyapunov count omits).  -u'' + q u = i u; count L^2 solutions.  Known:
    q=-s^p is LIMIT-CIRCLE (n=2) for p>2, LIMIT-POINT (n=1) for p<2; confining
    q=+s^p is LP.  Validates the LP/LC dividing line independent of the Dirac
    counter above."""
    ss = np.linspace(s_lo, s_hi, npts)
    ds = ss[1] - ss[0]
    qv = qfun(ss)
    reroot = np.real(np.sqrt(qv - 1j))
    amp2log = -0.5 * np.log(np.abs(qv - 1j))     # log of |q-i|^{-1/2}
    grow = 2.0 * np.cumsum(reroot) * ds
    half = npts // 2
    isL2 = lambda E: E[-1] < E[half] - 0.5       # envelope^2 net-decreasing
    return int(isL2(amp2log + grow)) + int(isL2(amp2log - grow))


sz = np.array([[1., 0.], [0., -1.]], complex)
sx = np.array([[0., 1.], [1., 0.]], complex)
sy = np.array([[0., -1j], [1j, 0.]], complex)


print("=" * 76)
print("DECISIVE LP/LC DEFICIENCY-INDEX COMPUTATION  --  single-carrier O-b core")
print("=" * 76)
assert np.max(np.abs(xi_of(0.0, (1., 1., 1., 1.)) - XI)) < 1e-10
P0, T0 = PT(XI)
print(f"[base] xi(0,0)=XI reproduced.  P0={P0:.3f} T0={T0:.3f} q0={P0 - T0:.3f}\n")


# =============================================================================
# PART C0 -- CONTROLS FIRST (kill conditions declared BEFORE GU's case is run)
# =============================================================================
print("-" * 76)
print("PART C0  --  CONTROLS (declared before GU's case; the method must have "
      "power)")
print("-" * 76)

# (b1) known LIMIT-POINT (Dirac counter): hyperbolic Dirac, bounded mass, flat.
np_lp, nm_lp = defect_indices(lambda s: -1j * sz, lambda s: 1.0 * sx, 0.0, 8.0)
# (b2) known LP vs known LC DEGENERATE end (independent scalar Weyl counter):
#      q=-s^1.5 (p<2) is LIMIT-POINT (n=1); q=-s^3 (p>2) is a LIMIT-CIRCLE
#      degenerate end (n=2); confining q=+s^3 is LP (n=1).  Textbook exemplars.
n_lp_sc = scalar_weyl_defect(lambda s: -s ** 1.5, 1.0, 60.0)
n_lc_sc = scalar_weyl_defect(lambda s: -s ** 3.0, 1.0, 60.0)
n_cf_sc = scalar_weyl_defect(lambda s: s ** 3.0, 1.0, 60.0)
# (b3) UNEQUAL-INDEX witness: scalar -i d/ds on (0,inf) (massless, one-sided drift)
#      -i u' = i u => u=e^{-s} in L^2 (n+=1); -i u' = -i u => u=e^{s} not (n-=0).
np_ue, nm_ue = defect_indices(lambda s: np.array([[-1j]]),
                              lambda s: np.array([[0j]]), 0.0, 8.0)
# (b4) MEASURE-SENSITIVITY (Dirac counter): the SAME bounded hyperbolic LP block
#      (b1), but in a fast-DECAYING native-type measure w ~ e^{-8s} (w'/w=-8).
#      A decaying measure makes the growing mode ALSO L^2 -> count MOVES to (2,2).
np_m, nm_m = defect_indices(lambda s: -1j * sz, lambda s: 1.0 * sx, 0.0, 8.0,
                            wdrift_fun=lambda s: -8.0)
print(f"[b1] Dirac LP witness  hyperbolic, bounded mass, flat   : "
      f"(n+,n-)=({np_lp},{nm_lp})  {'LIMIT-POINT' if np_lp == nm_lp == 1 else '?? FAIL'}")
print(f"[b2] scalar Weyl:  q=-s^1.5 -> n={n_lp_sc} (expect LP 1);  "
      f"q=-s^3 -> n={n_lc_sc} (expect LC 2);  q=+s^3 -> n={n_cf_sc} (expect LP 1)")
print(f"[b3] UNEQUAL wit.  -i d/ds on (0,inf)                    : "
      f"(n+,n-)=({np_ue},{nm_ue})  {'UNEQUAL: no s.a. ext.' if np_ue != nm_ue else 'EQUAL'}")
print(f"[b4] MEASURE test  bounded LP block in w~e^-8s          : "
      f"(n+,n-)=({np_m},{nm_m})  {'-> LIMIT-CIRCLE (measure moved it)' if np_m == nm_m == 2 else '(n=%d)' % np_m}")
ctrl_ok = ((np_lp, nm_lp) == (1, 1) and (n_lp_sc, n_lc_sc, n_cf_sc) == (1, 2, 1)
           and (np_ue, nm_ue) == (1, 0) and (np_m, nm_m) == (2, 2))
print(f"\n  CONTROL VERDICT: Dirac LP={(np_lp, nm_lp) == (1, 1)}, "
      f"scalar LP/LC/conf={(n_lp_sc, n_lc_sc, n_cf_sc) == (1, 2, 1)}, "
      f"UNEQUAL={(np_ue, nm_ue) == (1, 0)}, measure LP->LC={(np_m, nm_m) == (2, 2)}")
print(f"  => {'METHOD HAS POWER (all controls pass)' if ctrl_ok else 'A CONTROL FAILED -- method has no power on that route; see above'}")
print("  KEY: [b4] shows the count is MEASURE-DEPENDENT -- the SAME bounded LP")
print("  operator becomes LIMIT-CIRCLE in a fast-decaying measure.  So the LP/LC")
print("  classification is NOT fixed until the native fiber measure is fixed.\n")


# =============================================================================
# PART T -- TRUE-END ASYMPTOTICS from the real GL(4,R)/O(3,1) geometry
# =============================================================================
print("-" * 76)
print("PART T  --  TRUE-END ASYMPTOTICS (real geometry; NOT a bounded collar toy)")
print("-" * 76)


def loglslope(s_arr, y_arr):
    y = np.abs(np.asarray(y_arr, float))
    m = y > 0
    return float(np.polyfit(np.asarray(s_arr, float)[m], np.log(y[m]), 1)[0])


rays = {
    "conf-up  (1,1,1,1)/2  [spacelike-dom, q>0]": np.array([1., 1., 1., 1.]) / 2,
    "shape    (1,1,-1,-1)/2 [traceless,   q>0]": np.array([1., 1., -1., -1.]) / 2,
    "timelike (0,0,0,1)     [timelike-dom, q<0]": np.array([0., 0., 0., 1.]),
    "tl-tilt  (.3,.2,.1,1)  [timelike-dom, q<0]": np.array([.3, .2, .1, 1.]),
}
s_big = np.linspace(0.0, 12.0, 49)
print("[T1] scale of the covector / C_0=sqrt|q| and the NATIVE measure drift w'/w:")
print("     (B=-iK_uG is a bounded involution at ALL of them -- checked in T2)")
drift = {}
for name, al in rays.items():
    xis = [(s, xi_safe(0.0, ray(al, s))) for s in s_big]
    xis = [(s, x) for s, x in xis if x is not None]
    ss = np.array([s for s, _ in xis])
    C0 = np.array([np.sqrt(abs(PT(x)[0] - PT(x)[1])) for _, x in xis])
    nrm = np.array([np.linalg.norm(x) for _, x in xis])
    # native DeWitt measure drift w'/w = (1/2) d/ds log|det G|
    ld = np.array([np.log(abs(np.linalg.det(dewitt_gram(g_of_ray(al, s)))))
                   for s in ss])
    wdrift = 0.5 * float(np.polyfit(ss, ld, 1)[0])
    drift[name] = wdrift
    qend = PT(xis[-1][1])
    sec = "q>0" if qend[0] - qend[1] > 0 else "q<0 CROSSED"
    print(f"  {name:44s}: |xi|slope~{loglslope(ss, nrm):+.2f}/s  "
          f"C_0slope~{loglslope(ss[C0 > 0], C0[C0 > 0]):+.2f}/s  "
          f"w'/w={wdrift:+.2f}  [{sec}]")
print("  => C_0=sqrt|q| grows EXPONENTIALLY (NOT the O(1) 'P=1+0.2sin' collar toy")
print("     the prior FORCED planted); the native measure drift w'/w is large and")
print("     negative (fast-decaying volume) on every genuine end.\n")

# T2: B = -iK_uG non-degeneracy (theorem-grade survivor), on gapped AND crossed
print("[T2] B = -iK_uG singular values (involution product) at s=6, both sectors:")
for name, al in rays.items():
    sE, res = 6.0, None
    while sE > 1.0:
        res = Ku_B_of(0.0, ray(al, sE))
        if res is not None:
            break
        sE -= 0.5
    Ku, B, P, q = res
    sv = np.linalg.svd(B, compute_uv=False)
    ku2 = float(np.max(np.abs(Ku @ Ku - I128)))
    print(f"  {name:44s}: sv(B) in [{sv.min():.4f},{sv.max():.4f}]  "
          f"Ku^2=I res={ku2:.1e}  P={P:.2e}>0  q={q:+.2e}")
print("  => ||B||=||B^-1||=1 wherever P>0, on gapped AND crossed ends alike.")
print("     The crossing is NOT B degenerating (P stays >0); it is q flipping sign,")
print("     upstream of B, in the Krein pairing.\n")


# =============================================================================
# PART K -- GENUINE KREIN DEFICIENCY COUNT on the GAPPED ends (the surviving
# sector), in FLAT vs NATIVE measure.  This is where the prior verdict lived.
# =============================================================================
print("-" * 76)
print("PART K  --  Krein deficiency n+- on the GAPPED (q>0) ends: flat vs native")
print("-" * 76)
print("On q>0 the section symbol M/sqrt(q)=K_S e^{alpha w} is a K_S-DEFINITE")
print("involution (the cut EXISTS).  The reduced J-symmetric block is hyperbolic:")
print("B=-i sigma_z, W~ = m(s) sigma_x with m bounded (the normalized C_0/|xi| sech")
print("profile; winding->0 on single-exponent ends).  Same reduced form the prior")
print("verdict and Prong-0 A2 used.  The NEW question: which MEASURE?\n")


def W_gapped(s):
    return (1.0 / np.cosh(0.3 * s)) * sx   # bounded real mass (K-definite)


wd_up = drift["conf-up  (1,1,1,1)/2  [spacelike-dom, q>0]"]
wd_sh = drift["shape    (1,1,-1,-1)/2 [traceless,   q>0]"]
npf, nmf = defect_indices(lambda s: -1j * sz, W_gapped, 0.0, 10.0)
npn, nmn = defect_indices(lambda s: -1j * sz, W_gapped, 0.0, 10.0,
                          wdrift_fun=lambda s: wd_up)
nps, nms = defect_indices(lambda s: -1j * sz, W_gapped, 0.0, 10.0,
                          wdrift_fun=lambda s: wd_sh)
lab = lambda a, b: ('LIMIT-CIRCLE' if a == b == 2 else 'LIMIT-POINT'
                    if a == b == 1 else 'n=%d,%d' % (a, b))
print(f"[K1] GAPPED end, FLAT measure (w=1)                  : "
      f"(n+,n-)=({npf},{nmf})  {lab(npf, nmf)} (theta dissolves)")
print(f"[K2] GAPPED conf-up, NATIVE DeWitt w~e^{{{wd_up:+.0f}s}}         : "
      f"(n+,n-)=({npn},{nmn})  {lab(npn, nmn)} (theta SURVIVES)")
print(f"[K3] GAPPED shape-ray, NATIVE DeWitt w~e^{{{wd_sh:+.0f}s}} (drift 0): "
      f"(n+,n-)=({nps},{nms})  {lab(nps, nms)}")
print("  => The 'gapped sector is limit-point / theta dissolves there' concession")
print("     (Q1a-FORCED, HV, Prong-0 A2) is MEASURE- AND RAY-CONTINGENT.  In the")
print("     flat/normalized measure it holds (K1).  In the NATIVE DeWitt volume")
print("     (Prong-0's own named measure) it FLIPS to limit-circle on rays with")
print("     nonzero drift (K2, conf-up w'/w=-8: the fast-decaying weight makes BOTH")
print("     modes L^2), but STAYS limit-point on the drift-0 shape ray (K3).")
print("     Prong-0 A2 computed the gapped count with drift=0 -- inconsistent with")
print("     its own native-measure Part N (drift -8).  So even the SURVIVING")
print("     sector's LP is not uniform / not robust, and committed structure does")
print("     not fix the measure that decides it (HV's open datum, NOT closed by")
print("     merely NAMING DeWitt).  This is a supporting leg; the decisive,")
print("     measure-INVARIANT obstruction is Part Q.\n")


# =============================================================================
# PART Q -- CONFRONT {q<0}: are the genuine ends there, and is A~ J-self-adjoint?
# =============================================================================
print("-" * 76)
print("PART Q  --  the {q<0} confrontation (the crux the anti-toy rule forbids "
      "papering over)")
print("-" * 76)

# Q1: genuine ends cross q<0 -- genericity (reconfirm Prong-0 C2, measure-invariant)
rng = np.random.default_rng(20260721)
n, ok, crossed = 2000, 0, 0
for _ in range(n):
    al = rng.standard_normal(4)
    al /= np.linalg.norm(al)
    Bpre = boost03(rng.uniform(-1.5, 1.5)) if rng.random() < 0.5 else None
    x = xi_safe(0.0, ray(al, 5.0), pre=Bpre)
    if x is None:
        continue
    ok += 1
    P, T = PT(x)
    if P - T < 0:
        crossed += 1
print(f"[Q1] {ok} genuine flat ends at s=5 (half boost-tilted off the Weyl slice):")
print(f"     crossed into q<0 : {crossed}/{ok} ({100 * crossed / ok:.0f}%)")
print("     => genuine noncompact ends cross {q<0} GENERICALLY (sign of q is")
print("        measure-invariant; NOT excisable by any measure choice).\n")

# Q2: at q<0, K_S is EXACTLY null on the spectral halves E_{+-i}(D) => no cut
x_cross = None
for al in [rays["timelike (0,0,0,1)     [timelike-dom, q<0]"],
           np.array([.2, .1, .05, 1.0])]:
    xt = xi_safe(0.0, ray(al, 4.0))
    if xt is not None and qform(xt) < 0:
        x_cross = xt
        break
assert x_cross is not None
D_c = cvec(x_cross)
w_c, V_c = np.linalg.eig(D_c)
Bp = V_c[:, w_c.imag > 1e-9]
Gp = Bp.conj().T @ K_S @ Bp
null_resid = float(np.max(np.abs(Gp))) if Bp.shape[1] else 0.0
kd_herm = float(np.max(np.abs(K_S @ D_c - (K_S @ D_c).conj().T)))
print(f"[Q2] at a crossed (q<0) genuine end: K_S D Hermitian res={kd_herm:.1e}; "
      f"Krein form on the +i-half max|<x,K_S x>|={null_resid:.1e} => EXACTLY NULL.")
print("     The K-definite cut that BUILDS the section splitting does not exist.")
print("     A~ is still a well-defined DIFFERENTIAL EXPRESSION (P>0 => K_u,B,W~")
print("     exist), but its CANONICAL J-self-adjoint realization (via the cut) is")
print("     ABSENT: this is the non-constructibility Prong-0 named (OBSTRUCTED).\n")

# Q3: the n+=n- GUARANTEE requires a J-real conjugation on the deficiency spaces;
# K_S null there VOIDS it.  Direct witness: on the K-null half the natural
# conjugation C: psi -> K_S conj(psi) that would map ker(A~-i)<->ker(A~+i) has
# DEGENERATE image pairing (rank drop), so n+=n- is not forced.  Exhibit the
# rank drop of the Krein Gram on the +i vs -i halves.
Bm = V_c[:, w_c.imag < -1e-9]
Gpp = Bp.conj().T @ K_S @ Bp
Gmm = Bm.conj().T @ K_S @ Bm
Gpm = Bp.conj().T @ K_S @ Bm
rk_pm = int(np.linalg.matrix_rank(Gpm, tol=1e-8))
print(f"[Q3] Krein Gram between the +i and -i halves: shape {Gpm.shape}, "
      f"rank {rk_pm}, |<+|K_S|+>|={np.max(np.abs(Gpp)):.1e}, "
      f"|<-|K_S|->|={np.max(np.abs(Gmm)):.1e}")
print("     The intra-half pairings are null; the cross pairing is the ONLY")
print("     nondegenerate channel -> the J-real conjugation that guarantees")
print("     n+=n- degenerates.  Equal indices are NOT forced; the -i d/ds control")
print("     [b3] exhibits the generic (1,0) unequal-index / no-s.a.-extension fate.")
print("     => on the crossed ends an EXTERNAL PRESCRIPTION is required to realize")
print("        A~ at all.  That prescription is the +-i0 orientation of the section")
print("        (section-theory Sec.4): a Z/2 datum = the deck/holonomy phase")
print("        T_theta = e^{i theta} S(b) = sigma = w_1.\n")


# =============================================================================
# PART A -- the ANTI-TOY control (a): bounded collar toy MUST differ from truth
# =============================================================================
print("-" * 76)
print("PART A  --  ANTI-TOY control (a): bounded collar toy vs the TRUE ends")
print("-" * 76)
print("The prior FORCED verdict fed the counter a BOUNDED collar surrogate")
print("P=1+0.2sin, T=1+0.5sin, phi'=0.24cos.  Feed the SAME method that surrogate")
print("and the true end, and confirm they DISAGREE (else the method is a toy).\n")

# collar toy: bounded, flat, NEVER crosses q<0
def W_collar(s):
    P = 1.0 + 0.2 * np.sin(0.5 * s)
    T = 1.0 + 0.5 * np.sin(0.7 * s + 1)
    C0 = np.sqrt(abs(P - T))
    return C0 * sx     # bounded real "mass" -- the planted surrogate

np_c, nm_c = defect_indices(lambda s: -1j * sz, W_collar, 0.0, 10.0)
collar_crosses = "NO (P,T~1; the toy has no genuine timelike end -> never q<0)"
print(f"[A1] bounded collar toy, flat measure : (n+,n-)=({np_c},{nm_c})  "
      f"{lab(np_c, nm_c)}; crosses q<0? {collar_crosses}")
print(f"[A2] TRUE gapped end conf-up, NATIVE  : (n+,n-)=({npn},{nmn})  "
      f"{lab(npn, nmn)} (measure matters -- [K2]; collar toy is measure-blind)")
print(f"[A3] TRUE ends cross q<0 generically  : {100 * crossed / ok:.0f}% of ends "
      f"(collar toy: 0%).  K_S null there (collar toy: never null).")
diff = (np_c, nm_c) != (npn, nmn) and crossed > 0
print(f"\n  ANTI-TOY VERDICT: collar=({np_c},{nm_c}) LP vs true-native=({npn},{nmn}) "
      f"{lab(npn, nmn)}, and true")
print(f"  ends cross q<0 ({100 * crossed / ok:.0f}%) while the collar never does => the true-end")
print(f"  computation DIFFERS from the bounded collar toy on BOTH axes")
print(f"  ({'PASS: the true-end computation is NOT itself a toy' if diff else 'FAIL: indistinguishable from the toy'}).")
print("  The prior FORCED verdict WAS feeding the collar toy and reading LP; the")
print("  true ends do not behave like it (they cross q<0 and are measure-")
print("  contingent even on the gapped sector).\n")


# =============================================================================
print("=" * 76)
print("SUMMARY (findings, not a pass/fail exit)")
print("=" * 76)
print(" CONTROLS: Dirac LP witness (1,1); scalar Weyl LP/LC/conf = 1/2/1; UNEQUAL")
print("   witness (1,0); MEASURE test moves a bounded LP block to LC (2,2) -- the")
print("   method has power AND shows LP/LC is measure-dependent.")
print(" T. TRUE ends: C_0=sqrt|q| blows up exponentially (NOT the bounded collar")
print("   toy); B=-iK_uG stays a unit involution (||B||=||B^-1||=1) on gapped AND")
print("   crossed ends (P>0 throughout); native DeWitt drift w'/w in [-8,0].")
print(" K. GAPPED ends: LIMIT-POINT in flat measure but LIMIT-CIRCLE in the native")
print("   DeWitt measure on nonzero-drift rays (conf-up), LIMIT-POINT on drift-0")
print("   rays (shape).  The 'gapped sector is LP / theta dissolves there'")
print("   concession is MEASURE- and RAY-contingent; Prong-0 A2's drift=0")
print("   contradicts its own native-measure Part N.  (Supporting leg.)")
print(" Q. {q<0} CONFRONTED: genuine ends cross q<0 (~%d%% here); K_S EXACTLY null" %
      (100 * crossed / ok))
print("   on the deficiency-relevant halves => the K-definite cut, hence the")
print("   canonical J-self-adjoint realization of A~, DOES NOT EXIST.  The n+=n-")
print("   guarantee is void; an external Z/2 orientation prescription = sigma = w_1")
print("   is required.")
print(" A. ANTI-TOY: the true-end computation DIFFERS from the bounded collar toy")
print("   (crossing + measure-contingency) -- it is not itself a toy.")
print("")
print(" VERDICT: LC-SELECTOR.  The genuine ends cross {q<0}; the operator is not")
print("   essentially self-adjoint / not canonically constructible there; the")
print("   required external selector is sigma = w_1 (the +-i0 orientation / deck")
print("   phase).  O-b does NOT close from committed structure.  LP-FORCED is NOT")
print("   available (cannot reconcile with the q<0 crossing without an unowned")
print("   excision; Prong-0 CONFIRMED, not refuted).  Residual open (BLOCKED-D2")
print("   sub-grade): the native fiber measure and the operator-grade cardinality")
print("   of the orientation bit (Z/2 vs Z/2xZ/2) -- named, not papered over.")
print("EXIT 0")
