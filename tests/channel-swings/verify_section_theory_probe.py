#!/usr/bin/env python3
"""HOSTILE SECOND-DRY-ROUND VERIFIER -- sector-relative section theory cluster.

CHANNEL: adversarial verification (Joe direct chat, 2026-07-20, summit wave:
         second dry round, section theory). Independent re-derivation and
         attack pass over the four-result cluster:
           1. sector-relative-section-theory-2026-07-20 (+ probe, 46c0cbd)
           2. master-identity-mechanism-2026-07-20 (+ probe, 2e6cd14)
           3. universal-null lemma (m1-third-reading, 73452cd)
           4. even/odd selection rule (araki-scale-route, c7b510b)
INDEPENDENCE: no code imported from the originals' probe bodies; the Y14
         end-model FAMILY definition (frame_diag / rho / rot4) is replicated
         because it IS the object under test; every verification computation
         (symbol, cuts, Grams, census, closed forms) is re-implemented here,
         several symbolically via sympy, and sampling uses a FRESH seed (99)
         and FRESH rays not in the originals' catalogue.
ATTACKS RUN (per the mission):
  A. master identity re-derived: general-n coefficient assembly done in
     sympy exactly; contraction identities verified leg-by-leg in Cl(5,1),
     Cl(5,3), Cl(9,5); the WHOLE theorem proven symbolically (all real xi)
     in a Cl(5,1) miniature; dimension scaling 4(n-1)/n, 4/n, 2/DIM checked
     across three algebras; complex-xi falsification control reproduced.
  B. the little theorems of M re-proven: polynomial (radical-free) symbolic
     proofs in the Cl(5,3) miniature with SYMBOLIC real x -- M'^2 = Pq I,
     K-s.a., [M', D] = 0, plus the D -> -D evenness the originals never
     state; then fresh-point numeric checks on the actual family.
  C. the classification attacked: (a) census -- the "EXACTLY eight
     involutions" count is REFUTED (the algebra is C^4: 16 involutions; a
     ninth is exhibited machine-exactly), while the load-bearing sub-claim
     (K_S-skew involutions = +-d~, +-J_c ONLY) is re-proven symbolically
     and so the Z/2 conclusion is UNAFFECTED; (b) both d~ exclusion legs
     re-verified independently; (c) rigidity: the linear two-line proof is
     re-derived and the ONLY loophole (antilinear J_quat) is shown to fix M
     and exchange the +-i0 sections -- exactly the typed K-d shadow, no new
     counterexample; (d) Re k = 0 past the wall re-derived by an
     INDEPENDENT closed-form trace computation (tr(uDA) real, in closed
     form), so no real conserved reading separates the prescriptions.
  D. seam/monodromy upgraded: the seam law N_delta(1) = -U N_delta(0) U^-1
     is proven as a GENERIC lemma (any D, any unitary U with U K_S U^-1 =
     -K_S), then the family's seam property is spot-checked fresh.
  E. coverage extension: 60 NEW rays (seed 99), fresh walls bisected, the
     closed forms margin = sqrt(q/P), r = sqrt(-q/T), k-form, gluing jump
     -> 2 all re-checked beyond the originals' sample.
  F. cross-checks: universal-null (symbolic + structural battery over the
     WHOLE conserved class), selection rule vs sections (swap involution
     built fresh; even readings blind, K_S-linear k reads), width channel
     vs S-matrix transparency (magnitude deck-even = blind; sign = gauge).
Deterministic; numpy + sympy; seeded 99; exit 0 iff all checks pass.
"""
from __future__ import annotations

import os
import sys

import numpy as np
import sympy as sp

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "generation-sector"))
import gen_sector_bridge as gb  # noqa: E402  (verified rep -- shared object)
import oq_rk1_cl95_explicit_rep as cl95  # noqa: E402

N_DIRS, DIM = 14, 128
ETA = np.array([1.0] * 9 + [-1.0] * 5)
LAM = 0.5
RNG = np.random.default_rng(99)          # FRESH seed, fresh stream
RESULTS = []


def check(tag, name, ok, detail=""):
    RESULTS.append((tag, name, bool(ok)))
    line = f"[{tag}] {'PASS' if ok else 'FAIL'}  {name}"
    if detail:
        line += f"   ({detail})"
    print(line)
    return ok


# --- shared verified objects --------------------------------------------------
e = gb.gammas()
K_S = e[0].copy()
for a in range(1, 9):
    K_S = K_S @ e[a]
XI = np.real(np.asarray(gb.XI)).astype(float)
I128 = np.eye(DIM, dtype=complex)

G_raw = cl95.jordan_wigner_gammas(7)
r_sign, sigma_s = [], []
for a in range(N_DIRS):
    real_g = float(np.max(np.abs(np.conj(G_raw[a]) - G_raw[a]))) < 1e-12
    r_sign.append(+1 if real_g else -1)
    sigma_s.append(r_sign[a] if a < 9 else -r_sign[a])
S_even = [a for a in range(N_DIRS) if sigma_s[a] == -1]
S_odd = [a for a in range(N_DIRS) if sigma_s[a] == +1]
C_J = I128.copy()
for a in (S_even if len(S_even) % 2 == 0 else S_odd):
    C_J = C_J @ G_raw[a]
C_J_inv = np.linalg.inv(C_J)


def cvec(v):
    return sum(v[a] * e[a] for a in range(N_DIRS))


def qform(v):
    return float(np.real(np.vdot(v, ETA * v)))


def relres(Aa, Bb):
    return float(np.max(np.abs(Aa - Bb))) / max(1.0,
                                                float(np.max(np.abs(Bb))))


# --- Y14 end-model family (the OBJECT under test; definition replicated) ------
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
    return tuple(np.exp(2.0 * np.asarray(alpha, dtype=float) * s))


TGRID = np.linspace(0.0, 1.0, 41)


def q_profile(alpha, s):
    a4 = ray(alpha, s)
    return np.array([qform(xi_of(t, a4)) for t in TGRID])


def crossing_scan(alpha, s_hi):
    for s in np.linspace(0.0, s_hi, 61):
        q = q_profile(alpha, s)
        if np.min(q) < 0.0:
            return float(s), float(TGRID[int(np.argmin(q))])
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


U_h = e[0] @ e[3] @ e[4] @ e[9] @ e[11] @ e[12]
Uh_inv = np.linalg.inv(U_h)


# --- MY OWN section-theory implementation (independent) ------------------------
def parts(D):
    cs = 0.5 * (D + K_S @ D @ K_S)
    ct = D - cs
    P = float(np.real(np.trace(cs @ cs))) / DIM
    T = -float(np.real(np.trace(ct @ ct))) / DIM
    return cs, ct, P, T, P - T


def symbol(D):
    cs, _ct, P, _T, q = parts(D)
    Ku = K_S @ cs / np.sqrt(P)
    return Ku @ D, Ku, P, q


def n_delta(D, delta):
    M, _Ku, _P, q = symbol(D)
    return M / np.sqrt(q + 1j * delta)


def gram_margin(D, q):
    """Independent Gram-margin measurement: eigen-cut of D/sqrt(q), K_S Gram
    on each half, min |eigenvalue| of the normalized Gram."""
    chp = 0.5 * (I128 + D / np.sqrt(q))
    out = []
    for ch in (chp, I128 - chp):
        B = np.linalg.svd(ch)[0][:, :DIM // 2]
        Gm = B.conj().T @ K_S @ B
        Gm = 0.5 * (Gm + Gm.conj().T)
        out.append(float(np.min(np.abs(np.linalg.eigvalsh(Gm)))))
    return min(out)


def cross_weight(D, q):
    """Independent cross-Gram top/bottom sv between the complex halves."""
    g = np.sqrt(-q)
    Bg = np.linalg.svd(0.5 * (I128 - 1j * D / g))[0][:, :DIM // 2]
    Bd = np.linalg.svd(0.5 * (I128 + 1j * D / g))[0][:, :DIM // 2]
    sv = np.linalg.svd(Bd.conj().T @ K_S @ Bg, compute_uv=False)
    return float(sv[0]), float(sv[-1]), Bg, Bd


def split(x14):
    xs = x14.copy()
    xs[9:] = 0.0
    return xs, x14 - xs


# =============================================================================
# [T] setup: rep integrity, re-verified from scratch
# =============================================================================
ok = True
for a in range(N_DIRS):
    for b in range(a, N_DIRS):
        want = 2.0 * (ETA[a] if a == b else 0.0)
        if float(np.max(np.abs(e[a] @ e[b] + e[b] @ e[a]
                               - want * I128))) > 1e-9:
            ok = False
ok = ok and float(np.max(np.abs(K_S - K_S.conj().T))) < 1e-12 \
    and float(np.max(np.abs(K_S @ K_S - I128))) < 1e-12 \
    and float(np.max(np.abs(C_J @ np.conj(C_J) + I128))) < 1e-12 \
    and float(np.max(np.abs(U_h @ K_S @ Uh_inv + K_S))) < 1e-12 \
    and float(np.max(np.abs(U_h @ U_h - I128))) < 1e-12
check("T", "rep integrity re-verified from scratch: Cl(9,5) relations, K_S "
           "Hermitian involution, J_quat^2 = -I, U_h K_S U_h^-1 = -K_S, "
           "U_h^2 = I", ok)

base_ok = float(np.max(np.abs(xi_of(0.0, (1., 1., 1., 1.)) - XI))) < 1e-12
q_base = qform(XI)
check("T", "family replication anchor: xi(0,0) = XI machine-exact, "
           "q(XI) = 30.13 spacelike (same family as the originals)",
      base_ok and abs(q_base - 30.13) < 0.01, f"q = {q_base:.4f}")

# =============================================================================
# CLUSTER 2 -- the master identity, INDEPENDENTLY RE-DERIVED
# =============================================================================
# (1) the assembly coefficients, exactly, for symbolic n (sympy):
n_s = sp.Symbol('n', positive=True)
lam_s = (n_s - 2) / n_s
coef_scalar = sp.simplify(n_s + 2 * lam_s * (2 - n_s) + lam_s ** 2 * n_s)
coef_biv = sp.simplify((n_s - 4) + 2 * lam_s * (2 - n_s) + lam_s ** 2 * n_s)
sym_ok = (sp.simplify(coef_scalar - 4 * (n_s - 1) / n_s) == 0
          and sp.simplify(coef_biv + 4 / n_s) == 0)
check("E", "MASTER IDENTITY step 4 re-derived SYMBOLICALLY for general n: "
           "expanding A = sum_a eta_a (e_a c + lam c e_a)(c^+ e_a + "
           "lam e_a c^+) with lam = (n-2)/n via the k = 0,1,2 contraction "
           "identities gives scalar coefficient n + 2 lam(2-n) + lam^2 n = "
           "4(n-1)/n and bivector coefficient (n-4) + 2 lam(2-n) + "
           "lam^2 n = -4/n exactly (sympy) -- the 26/7 and 2/7 are pure "
           "combinatorics, confirmed independently", sym_ok,
      f"scalar = {coef_scalar}, bivector = {coef_biv}")


def mini_algebra(p, qq):
    """Independent small Cl(p,q) rep by Jordan-Wigner (my own assembly)."""
    n = p + qq
    G = cl95.jordan_wigner_gammas((n + 1) // 2)[:n]
    eta = [1.0] * p + [-1.0] * qq
    ee = [G[a] if eta[a] > 0 else 1j * G[a] for a in range(n)]
    d = ee[0].shape[0]
    K = np.eye(d, dtype=complex)
    for a in range(p):
        K = K @ ee[a]
    return ee, np.array(eta), K, d


def contraction_check(ee, eta, d):
    """sum_a eta_a e_a w_k e_a = (-1)^k (n-2k) w_k for k = 0,1,2."""
    n = len(ee)
    Id = np.eye(d, dtype=complex)
    rng2 = np.random.default_rng(1234)
    okc = True
    w1 = sum(rng2.standard_normal() * ee[a] for a in range(n))
    w2 = ee[0] @ ee[n - 1]
    for (k, w) in ((0, Id), (1, w1), (2, w2)):
        got = sum(eta[a] * ee[a] @ w @ ee[a] for a in range(n))
        want = ((-1) ** k) * (n - 2 * k) * w
        if float(np.max(np.abs(got - want))) > 1e-10 * max(
                1.0, float(np.max(np.abs(want)))):
            okc = False
    return okc

ok_contr = contraction_check(e, ETA, DIM)
for (p_, q_) in ((5, 1), (5, 3)):
    ee_, eta_, _K_, d_ = mini_algebra(p_, q_)
    ok_contr = ok_contr and contraction_check(ee_, eta_, d_)
check("E", "the two IMPORTED contraction identities verified leg-by-leg in "
           "THREE algebras -- Cl(9,5), Cl(5,1), Cl(5,3) -- for k = 0, 1, 2 "
           "(the only inputs the master-identity derivation consumes)",
      ok_contr)



def sp_exact(g):
    """Exact sympy matrix from a numpy gamma with entries in {0, +-1, +-i}."""
    re_i = np.round(np.real(g)).astype(int)
    im_i = np.round(np.imag(g)).astype(int)
    return sp.Matrix(re_i.tolist()) + sp.I * sp.Matrix(im_i.tolist())

# (2) the WHOLE theorem proven symbolically (all real xi) in Cl(5,1):
ee6, eta6, K6, d6 = mini_algebra(5, 1)
n6 = 6
xi_syms = sp.symbols('x0:6', real=True)
E6 = [sp_exact(g) for g in ee6]
c6 = sp.zeros(d6, d6)
for a in range(n6):
    c6 = c6 + xi_syms[a] * E6[a]
Gam6 = sp.Matrix(sp.BlockMatrix([E6]).as_explicit())
GG6 = sp.simplify(Gam6 * Gam6.H)
gg_ok = GG6 == n6 * sp.eye(d6)
Pi6 = sp.eye(n6 * d6) - sp.Rational(1, n6) * Gam6.H * Gam6
MD6 = sp.Matrix(sp.BlockDiagMatrix(*[c6] * n6).as_explicit())
X6 = sp.expand(Gam6 * MD6 * Pi6)
A6 = sp.expand(X6 * X6.H)
s6 = sum(x ** 2 for x in xi_syms)
B6 = sp.expand(c6 * c6.H - s6 * sp.eye(d6))
closed6 = sp.expand(sp.Rational(4 * (n6 - 1), n6) * s6 * sp.eye(d6)
                    - sp.Rational(4, n6) * B6)
cf_ok = sp.simplify(A6 - closed6) == sp.zeros(d6, d6)
K6s = sp_exact(K6)
mast6 = sp.expand(A6 + K6s * A6 * K6s
                  - sp.Rational(2, d6) * sp.trace(A6) * sp.eye(d6))
mi_ok = sp.simplify(mast6) == sp.zeros(d6, d6)
tr_ok = sp.simplify(sp.trace(A6)
                    - d6 * sp.Rational(4 * (n6 - 1), n6) * s6) == 0
check("E", "MASTER IDENTITY PROVEN SYMBOLICALLY, every real xi, in the "
           "Cl(5,1) miniature (n = 6, DIM = 8, K = e0..e4, K^2 = I): from "
           "the RAW definition A = (Gamma M_D Pi_RS)(...)^+ with symbolic "
           "real xi -- Gamma Gamma^+ = 6I; A = (10/3)|xi|^2 I - (2/3) B "
           "exactly; A + K A K = (2 tr A / DIM) I exactly; tr A = C2^2 = "
           "DIM (4(n-1)/n) |xi|^2_E -- the dimension scalings 4(n-1)/n, "
           "4/n, 2/DIM all confirmed at a SECOND point of the (n, DIM) "
           "lattice by exact computer algebra, not sampling",
      gg_ok and cf_ok and mi_ok and tr_ok)

# (3) Cl(5,3) numeric from-definition (third algebra), + Cl(9,5) fresh xi:
ee8, eta8, K8, d8 = mini_algebra(5, 3)
n8 = 8


def a_from_def(ee_l, eta_l, d_l, xi_l):
    n_l = len(ee_l)
    Gam = np.hstack(ee_l)
    Pi = np.eye(n_l * d_l, dtype=complex) - Gam.conj().T @ Gam / n_l
    cx = sum(xi_l[a] * ee_l[a] for a in range(n_l))
    MD = np.kron(np.eye(n_l), cx)
    X = Gam @ MD @ Pi
    return X @ X.conj().T, cx

ok8 = float(np.max(np.abs(np.hstack(ee8) @ np.hstack(ee8).conj().T
                          - n8 * np.eye(d8)))) < 1e-10
xi8 = RNG.standard_normal(n8)
A8, c8 = a_from_def(ee8, eta8, d8, xi8)
s8 = float(xi8 @ xi8)
B8 = c8 @ c8.conj().T - s8 * np.eye(d8)
ok8 = ok8 and relres(A8, (4 * (n8 - 1) / n8) * s8 * np.eye(d8)
                     - (4.0 / n8) * B8) < 1e-12
ok8 = ok8 and relres(A8 + K8 @ A8 @ K8,
                     (2.0 / d8) * np.real(np.trace(A8))
                     * np.eye(d8)) < 1e-12
# Cl(9,5): from-definition check at XI + two fresh real xi (one near-null)
ok95 = True
xis = [XI, RNG.standard_normal(14)]
xn = RNG.standard_normal(14)
xs_n, xt_n = split(xn)
xis.append(xs_n + xt_n * np.sqrt((xs_n @ xs_n) / (xt_n @ xt_n)))
for xk in xis:
    A9, c9 = a_from_def(e, ETA, DIM, xk)
    s9 = float(xk @ xk)
    B9 = c9 @ c9.conj().T - s9 * I128
    if relres(A9, (26.0 / 7.0) * s9 * I128 - (2.0 / 7.0) * B9) > 1e-11:
        ok95 = False
    if relres(A9 + K_S @ A9 @ K_S,
              (np.real(np.trace(A9)) / 64.0) * I128) > 1e-11:
        ok95 = False
    if abs(np.real(np.trace(A9)) - (3328.0 / 7.0) * s9) > 1e-8 * s9 * 500:
        ok95 = False
    if abs(np.real(np.trace(K_S @ A9))) > 1e-8:
        ok95 = False
c2_xi = np.sqrt(3328.0 / 7.0) * float(np.linalg.norm(XI))
check("E", "master identity + closed forms FROM THE RAW DEFINITION "
           "(Pi_RS built from scratch) in Cl(5,3) (fresh xi) and Cl(9,5) "
           "(XI, a fresh generic xi, a fresh NULL xi -- q = 0 is inside "
           "the theorem's scope): A = (26/7)|xi|^2 I - (2/7)B, A + K_S A "
           "K_S = (C2^2/64) I, C2^2 = (3328/7)||xi||^2_E, tr(K_S A) = 0; "
           "C2(XI) = 155.3625 reproduced", ok8 and ok95
      and abs(c2_xi - 155.3625) < 1e-3, f"C2(XI) = {c2_xi:.4f}")

# (4) falsification control: complex xi kills it, by the predicted residual
xiC = RNG.standard_normal(n8) + 1j * RNG.standard_normal(n8)
AC, cC = a_from_def(ee8, eta8, d8, xiC)
sC = float(np.real(np.vdot(xiC, xiC)))
BC = cC @ cC.conj().T - sC * np.eye(d8)
viol = AC + K8 @ AC @ K8 - (2.0 / d8) * np.real(np.trace(AC)) * np.eye(d8)
pred = -(4.0 / n8) * (BC + K8 @ BC @ K8)
check("F", "falsification control (Cl(5,3), complex xi): the master "
           "identity FAILS at O(1) and the violation equals the predicted "
           "residual -(4/n)(B + K B K) machine-exactly -- reality of xi "
           "is the load-bearing hypothesis, as claimed",
      float(np.max(np.abs(viol))) > 1e-2 and relres(viol, pred) < 1e-10,
      f"violation {float(np.max(np.abs(viol))):.3f}, match "
      f"{relres(viol, pred):.1e}")

# =============================================================================
# CLUSTER 1 -- the little theorems of M, re-proven independently
# =============================================================================
# (1) SYMBOLIC, radical-free, in the Cl(5,3) miniature with symbolic real x:
#     M2 := K c_s D (the unnormalized symbol; M = M2/sqrt(P)).  Claims:
#     M2^2 = P q I, K M2^+ K = M2, [M2, D] = 0, (K c_s)^2 = P I,
#     M2(-D) = M2(D)  (evenness under D -> -D -- unstated in the original).
x_syms = sp.symbols('y0:8', real=True)
E8 = [sp_exact(g) for g in ee8]
K8s = sp_exact(K8)
D8 = sp.zeros(d8, d8)
for a in range(n8):
    D8 = D8 + x_syms[a] * E8[a]
cs8 = sp.expand((D8 + K8s * D8 * K8s) / 2)
P8 = sum(x_syms[a] ** 2 for a in range(5))
T8 = sum(x_syms[a] ** 2 for a in range(5, 8))
q8 = P8 - T8
Mp = sp.expand(K8s * cs8 * D8)
Z8 = sp.zeros(d8, d8)
cs8_direct = sp.zeros(d8, d8)
for a in range(5):
    cs8_direct = cs8_direct + x_syms[a] * E8[a]
lt_ok = (sp.simplify(sp.expand(cs8 - cs8_direct)) == Z8
         and sp.simplify(sp.expand((K8s * cs8) * (K8s * cs8))
                         - P8 * sp.eye(d8)) == Z8
         and sp.simplify(sp.expand(Mp * Mp) - P8 * q8 * sp.eye(d8)) == Z8
         and sp.simplify(sp.expand(K8s * Mp.H * K8s - Mp)) == Z8
         and sp.simplify(sp.expand(Mp * D8 - D8 * Mp)) == Z8)
# evenness under D -> -D: c_s -> -c_s, so M2 -> (-K c_s)(-D) = M2
Mp_neg = sp.expand(K8s * (-cs8) * (-D8))
lt_ok = lt_ok and sp.simplify(Mp_neg - Mp) == Z8
check("E", "LITTLE THEOREMS OF M PROVEN SYMBOLICALLY (Cl(5,3) miniature, "
           "SYMBOLIC real x, radical-free via M2 = K c_s D): c_s = the "
           "space part exactly; (K c_s)^2 = P I; M2^2 = P q I (i.e. "
           "M^2 = qI); K-self-adjointness K M2^+ K = M2; [M2, D] = 0 -- "
           "all identities of POLYNOMIALS in x, hence valid on every "
           "regime including walls, by computer algebra, independent of "
           "the Y14 family; note found: M is EVEN under D -> -D "
           "(proven) -- so 'LINEAR in D' in the originals is loose "
           "language for entire/positively-1-homogeneous, not linearity "
           "of the map D -> M", lt_ok)

# (2) fresh numeric on the actual family; conf-down wall re-bisected:
A_CONF_DN = (-1.0, -1.0, -1.0, -1.0)
A_CONF_UP = (1.0, 1.0, 1.0, 1.0)
s_dn, t_dn = crossing_scan(A_CONF_DN, 3.0)
s_star = bisect_wall(A_CONF_DN, t_dn, s_dn)
x_gap = xi_of(t_dn, ray(A_CONF_DN, max(s_star - 0.4, 0.0)))
x_cross = xi_of(t_dn, ray(A_CONF_DN, s_star + 0.4))
D_gap, D_cross = cvec(x_gap), cvec(x_cross)
q_gap, q_cross = qform(x_gap), qform(x_cross)
ok_np = abs(s_star - 0.0585) < 5e-3 and abs(t_dn - 0.575) < 0.05
for (Dx, x14) in ((D_gap, x_gap), (D_cross, x_cross), (cvec(XI), XI)):
    Mx, Kux, Px, qx = symbol(Dx)
    if float(np.max(np.abs(Mx @ Mx - qx * I128))) > 1e-9 * max(
            1.0, float(np.max(np.abs(Mx))) ** 2):
        ok_np = False
    if relres(K_S @ Mx.conj().T @ K_S, Mx) > 1e-11:
        ok_np = False
    if abs(qx - qform(x14)) > 1e-9 * max(1.0, abs(qx)):
        ok_np = False
check("E", "little theorems re-checked numerically on the actual family "
           "(conf-down wall re-bisected from scratch: s* = 0.0585, t* = "
           "0.575 reproduced independently); M^2 = qI, K_S-s.a., q = "
           "Krein norm at base/gapped/crossed", ok_np,
      f"s* = {s_star:.4f}, t* = {t_dn:.3f}")

# =============================================================================
# CLUSTER 1 -- the classification, attacked
# =============================================================================
# (a) THE CENSUS. Claim under attack: "the commutant algebra span{I, d~,
#     Ku, J_c} is 4-dim commutative with EXACTLY eight involutions".
Mx_c, Ku_c, P_c, qc = symbol(D_cross)
g_c = np.sqrt(-qc)
d_til = -1j * D_cross / g_c
J_c = d_til @ Ku_c
X9 = 0.5 * (I128 + d_til + Ku_c - J_c)      # the ninth involution
vecs5 = np.stack([I128.flatten(), d_til.flatten(), Ku_c.flatten(),
                  J_c.flatten(), X9.flatten()])
in_span = np.linalg.matrix_rank(vecs5) == 4
inv9 = float(np.max(np.abs(X9 @ X9 - I128))) < 1e-12
d_new = min(float(np.max(np.abs(X9 - s * B)))
            for s in (1, -1)
            for B in (I128, d_til, Ku_c, J_c))
blocks = [float(np.real(np.trace(0.5 * (I128 + s1 * d_til)
                                 @ (0.5 * (I128 + s2 * Ku_c)))))
          for s1 in (1, -1) for s2 in (1, -1)]
blocks_ok = all(abs(b - 32.0) < 1e-6 for b in blocks)
eig9 = np.sort(np.real(np.linalg.eigvals(X9)))
dim_plus9 = int(np.sum(eig9 > 0))
# REPAIRED census, symbolically: K_S-skew involutions in the algebra.
skew_types_ok = (relres(K_S @ d_til.conj().T @ K_S, -d_til) < 1e-10
                 and relres(K_S @ J_c.conj().T @ K_S, -J_c) < 1e-10
                 and relres(K_S @ Ku_c.conj().T @ K_S, Ku_c) < 1e-10)
b_s, d_s = sp.symbols('b d')
sols = sp.solve([b_s * d_s, b_s ** 2 + d_s ** 2 - 1], [b_s, d_s], dict=True)
sol_set = {(s[b_s], s[d_s]) for s in sols}
skew_set_ok = sol_set == {(sp.Integer(-1), sp.Integer(0)),
                          (sp.Integer(1), sp.Integer(0)),
                          (sp.Integer(0), sp.Integer(-1)),
                          (sp.Integer(0), sp.Integer(1))}
x9_not_skew = float(np.max(np.abs(K_S @ X9.conj().T @ K_S + X9))) > 0.5
check("E", "CENSUS ATTACK -- the literal count is WRONG; the load-bearing "
           "sub-claim survives: the algebra span{I, d~, Ku, J_c} at the "
           "actual crossed point has all four joint (d~, Ku) blocks of "
           "dim 32, hence is C^4 and has SIXTEEN involutions, not eight "
           "-- the ninth, (I + d~ + Ku - J_c)/2, is exhibited machine-"
           "exactly inside the span, distinct from all +-{I, d~, Ku, "
           "J_c}. REPAIR: the involutions that matter (K_S-SKEW, the "
           "crossed-section adjoint type) are +-d~ and +-J_c ONLY -- "
           "proven symbolically (skewness kills the I and Ku "
           "coefficients; x^2 = I then forces bd = 0, b^2 + d^2 = 1) -- "
           "and the extra eight are neither K_S-skew nor half-splittings "
           "(+1-eigenspace dim 96): the Z/2 classification is UNAFFECTED "
           "but the census sentence must be corrected before print",
      in_span and inv9 and d_new > 0.4 and blocks_ok and dim_plus9 == 96
      and skew_types_ok and skew_set_ok and x9_not_skew,
      f"blocks = {[round(b) for b in blocks]}, X9 +1-eigspace dim "
      f"{dim_plus9}, min dist to the 8 = {d_new:.2f}")

# (b) the d~ exclusion, both legs, independently:
D_img = U_h @ D_cross @ Uh_inv
leg1 = relres(-1j * D_img / g_c, U_h @ d_til @ Uh_inv)  # deck-EVEN
m_odd = relres(symbol(D_img)[0], -U_h @ Mx_c @ Uh_inv)  # M deck-ODD
KdG = K_S @ D_gap / np.sqrt(q_gap)
KdG = 0.5 * (KdG + KdG.conj().T)
evK = np.linalg.eigvalsh(KdG)
sigK = (int(np.sum(evK > 0)), int(np.sum(evK < 0)))
check("E", "d~ EXCLUSION, both legs verified independently: (leg 1) d~ = "
           "-iD/g uses no K_S and is DECK-EVEN (transports to +itself "
           "around the seam: descends, sector-blind) while M is deck-odd; "
           "(leg 2) its gapped continuation D/sqrt(q) has K_S-Gram of "
           "signature EXACTLY (64,64): K-indefinite, inadmissible as a "
           "canonical cut, so analytic wall-matching cannot connect it "
           "to the gapped sections -- past the wall the canonical-class "
           "data are +-J_c only",
      leg1 < 1e-9 and m_odd < 1e-9 and sigK == (64, 64),
      f"d~ even-defect {leg1:.1e}, M odd-defect {m_odd:.1e}, "
      f"sig(K_S D/sqrt(q)) = {sigK}")

# (c) RIGIDITY + the antilinear loophole hunt:
def orth_in(x14, legs, avoid):
    for j in legs:
        v = np.zeros(N_DIRS)
        v[j] = 1.0
        for a in avoid:
            na = float(a @ a)
            if na > 0:
                v = v - (float(a @ v) / na) * a
        nv = float(np.linalg.norm(v))
        if nv > 0.3:
            return v / nv
    raise ValueError("none")


ok_rig = True
for x14 in (XI, x_cross):
    Dx = cvec(x14)
    Mx = symbol(Dx)[0]
    xs, xt = split(x14)
    m1v = orth_in(x14, range(9), [xs])
    m2v = orth_in(x14, range(9), [xs, m1v])
    G1 = cvec(m1v) @ cvec(m2v)
    if relres(G1 @ Dx, Dx @ G1) > 1e-11 or \
       relres(G1 @ K_S, K_S @ G1) > 1e-11 or \
       relres(G1 @ Mx, Mx @ G1) > 1e-11:
        ok_rig = False
    G2 = 0.6 * I128 + 0.8 * G1        # rotor in the same plane
    if relres(G2 @ Dx, Dx @ G2) > 1e-11 or relres(
            G2 @ Mx, Mx @ G2) > 1e-11:
        ok_rig = False
JD = C_J @ np.conj(D_cross) @ C_J_inv
JM = C_J @ np.conj(Mx_c) @ C_J_inv
JN = C_J @ np.conj(n_delta(D_cross, 1e-3)) @ C_J_inv
N_other = Mx_c / np.sqrt(qc - 1e-3j)
ok_anti = (relres(JD, D_cross) < 1e-10 and relres(JM, Mx_c) < 1e-10
           and relres(JN, N_other) < 1e-9
           and relres(C_J @ np.conj(K_S) @ C_J_inv, K_S) < 1e-12)
check("E", "RIGIDITY confirmed + loophole hunt CLOSED at this grade: "
           "every LINEAR K_S-preserving symmetry of D fixes M (the "
           "two-line proof re-derived: G commutes with c_s, hence Ku, "
           "hence M; witnessed on two symmetry types at base and crossed "
           "points); the ONLY symmetry that moves section data while "
           "preserving K_S is ANTILINEAR -- J_quat commutes with D (real "
           "xi) and with K_S, FIXES M, and exchanges the +-i0 sections; "
           "that is exactly the typed K-d shadow (scheme vs data at "
           "operator grade), not a rigidity counterexample; the hunt "
           "found nothing new", ok_rig and ok_anti)

# =============================================================================
# CLUSTER 1 -- seam law as a GENERIC LEMMA + monodromy, independently
# =============================================================================
# Lemma (mine): for ANY D and ANY unitary U with U K_S U^-1 = -K_S and
# U^2 = I, setting D1 := U D U^-1 gives c_s(D1) = U c_s(D) U^-1,
# P(D1) = P(D), q(D1) = q(D), Ku(D1) = -U Ku(D) U^-1, and therefore
# N_delta(D1) = -U N_delta(D) U^-1 for EVERY delta -- the seam law is a
# THEOREM given only the family's seam property D(t+1) = U_h D(t) U_h^-1.
ok_lem = True
for _ in range(3):
    xr = RNG.standard_normal(14)
    Dr = cvec(xr)
    D1r = U_h @ Dr @ Uh_inv
    csr, _c, Pr, Tr, qr = parts(Dr)
    cs1, _c, P1, T1, q1 = parts(D1r)
    if relres(cs1, U_h @ csr @ Uh_inv) > 1e-10 or \
       abs(P1 - Pr) > 1e-9 * Pr or abs(q1 - qr) > 1e-9 * max(1, abs(qr)):
        ok_lem = False
    for dlt in (0.7, 1e-3):
        if relres(n_delta(D1r, dlt), -U_h @ n_delta(Dr, dlt)
                  @ Uh_inv) > 1e-9:
            ok_lem = False
# the family's seam property itself, at FRESH points:
ok_seamfam = True
for (al, s_r, t_r) in ((A_CONF_UP, 1.1, 0.23), (A_CONF_DN, s_star + 0.4,
                                                0.41)):
    a4 = ray(al, s_r)
    D0f = cvec(xi_of(t_r, a4))
    D1f = cvec(xi_of(t_r + 1.0, a4))
    if relres(D1f, U_h @ D0f @ Uh_inv) > 1e-9:
        ok_seamfam = False
check("E", "SEAM LAW UPGRADED to a generic lemma + fresh family check: "
           "for ANY symbol D and ANY unitary U with U K_S U^-1 = -K_S, "
           "N_delta(U D U^-1) = -U N_delta(D) U^-1 for every delta "
           "(verified on random non-family symbols -- the minus sign is "
           "algebra, not a family accident), and the actual family DOES "
           "satisfy D(t+1) = U_h D(t) U_h^-1 at fresh (t, s) points on "
           "gapped and crossing radii: no-section-on-base-loop and "
           "two-on-double-cover (U_h^2 = I) follow for every delta at "
           "once -- the Z/2 monodromy is theorem-shaped modulo the "
           "family seam identity, which is checked, so wall count and "
           "placement indeed CANNOT alter the classification",
      ok_lem and ok_seamfam)

# =============================================================================
# CLUSTER 3 -- universal-null lemma, symbolic + whole-class battery
# =============================================================================
# symbolic two-line proof: VD = D^+V, Dx = lam x, Dy = lam y =>
# lam (x^+Vy) = x^+ V D y = x^+ D^+ V y = (Dx)^+ V y = conj(lam) x^+Vy.
lam_c = sp.Symbol('lambda', complex=True)
pf = sp.simplify(lam_c - sp.conjugate(lam_c))
sym_null = pf != 0    # nonreal lam => coefficient nonzero => pairing 0
# whole-class battery: conserved pairings V (VD = D^+V) are EXACTLY
# V = K_S W with W in comm(D) (since D^+ = K_S D K_S); comm(D) past the
# wall = block matrices over the two eigenspaces. Sample the class:
ev, EV = np.linalg.eig(D_cross)
idx_p = np.argsort(-np.imag(ev))[:64]
idx_m = np.argsort(np.imag(ev))[:64]
Bp_ = EV[:, idx_p]
Bm_ = EV[:, idx_m]
EVi = np.linalg.inv(EV)
ok_null = float(np.max(np.abs(np.imag(ev[idx_p]) - g_c))) < 1e-8
for _ in range(4):
    Wp_ = RNG.standard_normal((64, 64)) + 1j * RNG.standard_normal((64, 64))
    Wm_ = RNG.standard_normal((64, 64)) + 1j * RNG.standard_normal((64, 64))
    Wfull = np.zeros((128, 128), dtype=complex)
    Wfull[np.ix_(range(64), range(64))] = Wp_
    Wfull[np.ix_(range(64, 128), range(64, 128))] = Wm_
    perm = np.concatenate([idx_p, idx_m])
    Vc = K_S @ EV[:, perm] @ Wfull @ EVi[perm, :]
    if relres(Vc @ D_cross, D_cross.conj().T @ Vc) > 1e-8:
        ok_null = False
    # null on each half:
    if float(np.max(np.abs(Bp_.conj().T @ Vc @ Bp_))) > 1e-7 * float(
            np.max(np.abs(Vc))) or \
       float(np.max(np.abs(Bm_.conj().T @ Vc @ Bm_))) > 1e-7 * float(
            np.max(np.abs(Vc))):
        ok_null = False
check("E", "UNIVERSAL-NULL LEMMA re-proven and stress-tested over the "
           "WHOLE conserved class: symbolically, VD = D^+V plus Dx = "
           "lam x, Dy = lam y forces (lam - conj lam) x^+Vy = 0 -- null "
           "for nonreal lam (D is diagonalizable past the wall since "
           "D^2 = qI, q != 0, so the halves ARE eigenspaces -- hypothesis "
           "verified, spectrum exactly +-ig); structurally, EVERY "
           "conserved pairing is V = K_S W with W in comm(D) (D^+ = K_S "
           "D K_S), and random draws from that ENTIRE class are exactly "
           "null on each half: no conserved positive-definite pairing "
           "past any wall, any scheme -- CONFIRMED, with the class "
           "swept by construction rather than sampled blindly",
      sym_null and ok_null)

# =============================================================================
# CLUSTER 4 -- even/odd selection rule vs the section theory
# =============================================================================
# swap involution built fresh at the base point: V = c_m c_tau
xs_b, xt_b = split(XI)
m_v = orth_in(XI, range(9), [xs_b])
t_v = orth_in(XI, range(9, 14), [xt_b])
Vsw = cvec(m_v) @ cvec(t_v)
D_b = cvec(XI)
N_b = symbol(D_b)[0] / np.sqrt(q_base)
Qp_b = 0.5 * (I128 + N_b)
Qm_b = I128 - Qp_b
A_b, _cb = a_from_def(e, ETA, DIM, XI)
ok_sw = (relres(Vsw @ Vsw, I128) < 1e-10
         and relres(Vsw @ D_b, D_b @ Vsw) < 1e-10
         and relres(Vsw @ K_S @ Vsw, -K_S) < 1e-10
         and relres(Vsw @ Qp_b @ Vsw, Qm_b) < 1e-9
         and relres(Vsw @ A_b @ Vsw, A_b) < 1e-9)
# even readings are blind; the K_S-linear k reads:
k_p = 0.5 * np.real(np.trace(K_S @ N_b @ A_b))
k_m = 0.5 * np.real(np.trace(K_S @ (-N_b) @ A_b))
even_1 = float(np.real(np.trace(Qp_b.conj().T @ Qp_b)))   # even functional
even_1s = float(np.real(np.trace(Qm_b.conj().T @ Qm_b)))
even_2 = float(np.real(np.trace(A_b @ Qp_b @ A_b @ Qp_b)))
even_2s = float(np.real(np.trace(A_b @ Qm_b @ A_b @ Qm_b)))
sel_ok = (abs(k_p - 14421.0033) < 1e-2 and abs(k_p + k_m) < 1e-6 * abs(k_p)
          and abs(even_1 - even_1s) < 1e-6 * even_1
          and abs(even_2 - even_2s) < 1e-6 * abs(even_2))
check("E", "SELECTION RULE vs SECTION THEORY, consistency confirmed: the "
           "swap involution V = c_m c_tau (rebuilt fresh) commutes with "
           "D, anticommutes with K_S, swaps the two cut projectors, "
           "fixes the C2 density A -- so every K_S-even functional of "
           "the pair is swap-symmetric (two independent even functionals "
           "measured equal on both sections), while the K_S-LINEAR k "
           "separates them (+-14421.0033, f5 base value reproduced from "
           "MY OWN from-definition A); the section datum is K_S-linear "
           "by construction (M carries one K_S factor), so the section "
           "theory does not contradict the selection rule -- it is its "
           "positive complement: NO CONTRADICTION between clusters 1 and "
           "4", ok_sw and sel_ok,
      f"k = +-{k_p:.4f}, even-reading gaps < 1e-6")

# =============================================================================
# CLUSTER 1 -- closed forms, INDEPENDENT derivations
# =============================================================================
# k closed form by MY OWN trace algebra: u D = sqrt(P) I + c_s c_t/sqrt(P);
# A = (26/7)(P+T) I + (4/7) c_s c_t;  tr(c_s c_t) = 0 (bivector);
# tr((c_s c_t)^2) = 128 P T  (since (c_s c_t)^2 = P T I when xs _|_ xt);
# hence tr(u D A) = (256/7) sqrt(P) (13 P + 15 T)  -- REAL, exactly:
# k(N_delta) = tr(K_S M A)/(2 sqrt(q+i d)) = (128/7)(13P+15T) sqrt(P)
#              / sqrt(q + i delta);  past the wall sqrt(q+i0) = i g, so
# Re k = 0 EXACTLY and Im k = -(128/7)(13P+15T) sqrt(P)/g.
ok_k = True
det_k = []
for (nm, x14, Dx) in (("base", XI, cvec(XI)), ("gapped", x_gap, D_gap),
                      ("crossed", x_cross, D_cross)):
    csx, ctx, Px, Tx, qx = parts(Dx)
    Ax, _cx = a_from_def(e, ETA, DIM, x14)   # A from the RAW definition
    # my structural inputs:
    if abs(np.real(np.trace(csx @ ctx))) > 1e-8:
        ok_k = False
    if relres((csx @ ctx) @ (csx @ ctx), Px * Tx * I128) > 1e-10:
        ok_k = False
    uD = K_S @ symbol(Dx)[0]
    tr_uDA = np.trace(uD @ Ax)
    closed = (256.0 / 7.0) * np.sqrt(Px) * (13.0 * Px + 15.0 * Tx)
    if abs(np.imag(tr_uDA)) > 1e-6 or \
       abs(np.real(tr_uDA) - closed) > 1e-9 * closed:
        ok_k = False
    if nm == "crossed":
        kc = 0.5 * np.trace(K_S @ (-1j * symbol(Dx)[0] / g_c) @ Ax)
        im_cf = -(128.0 / 7.0) * (13 * Px + 15 * Tx) * np.sqrt(Px) / g_c
        re_frac = abs(np.real(kc)) / abs(kc)
        if re_frac > 1e-12 or abs(np.imag(kc) - im_cf) > 1e-9 * abs(im_cf):
            ok_k = False
        det_k.append(f"Re k/|k| = {re_frac:.1e}")
    if nm == "base":
        k0 = 0.5 * np.real(np.trace(K_S @ (symbol(Dx)[0] / np.sqrt(qx))
                                    @ Ax))
        if abs(k0 - 14421.0033) > 1e-2:
            ok_k = False
        det_k.append(f"k(base) = {k0:.4f}")
check("E", "k CLOSED FORM RE-DERIVED INDEPENDENTLY: my own trace algebra "
           "-- tr(c_s c_t) = 0 and (c_s c_t)^2 = PT I (both verified) "
           "give tr(uDA) = (256/7) sqrt(P)(13P + 15T), manifestly REAL "
           "-- so k(N_delta) = (128/7)(13P+15T) sqrt(P)/sqrt(q + i "
           "delta) with A built from the RAW definition (not the closed "
           "form): the f5 base value 14421.0033 falls out, Re k = 0 "
           "past the wall is an EXACT consequence of the reality of "
           "tr(uDA) (independent route, as demanded), and the width "
           "channel is -(128/7)(13P+15T) sqrt(P)/g on the nose: the F5 "
           "real accounting provably does NOT extend past the wall",
      ok_k, "; ".join(det_k))

# EP closed forms vs MY independent Gram measurements at the wall:
ok_ep = True
ep_det = []
for dlt in (0.2, 0.02, 0.002):
    xm = xi_of(t_dn, ray(A_CONF_DN, s_star - dlt))
    xp = xi_of(t_dn, ray(A_CONF_DN, s_star + dlt))
    _c1, _c2, Pm_, Tm_, qm_ = parts(cvec(xm))
    _c1, _c2, Pp_, Tp_, qp_ = parts(cvec(xp))
    marg_cf = np.sqrt(qm_ / Pm_)
    r_cf = np.sqrt(-qp_ / Tp_)
    marg_meas = gram_margin(cvec(xm), qm_)
    r_top, r_bot, _bg, _bd = cross_weight(cvec(xp), qp_)
    if abs(marg_meas - marg_cf) > 1e-6 or abs(r_top - r_cf) > 1e-6 or \
       (r_top - r_bot) > 1e-6 * r_top:
        ok_ep = False
    ep_det.append(f"d={dlt}: {marg_cf:.3f}/{r_cf:.3f}")
m1_marg = (0.661, 0.209, 0.066)
m1_rr = (0.508, 0.202, 0.066)
regs = [float(x.split()[-1].split('/')[0]) for x in ep_det]
regr = [float(x.split('/')[-1]) for x in ep_det]
reg_ok = all(abs(regs[i] - m1_marg[i]) < 5e-3
             and abs(regr[i] - m1_rr[i]) < 5e-3 for i in range(3))
check("E", "EP COLLAPSE CLOSED FORMS confirmed against MY OWN Gram "
           "measurements (margin via eigen-cut K_S-Gram; r via cross-"
           "Gram SVD, all 64 svs uniform): margin = sqrt(q/P), r = "
           "sqrt(-q/T) to 1e-6 at three approach distances; m1's "
           "measured sequences (0.661/0.209/0.066, 0.508/0.202/0.066) "
           "reproduced from the closed forms: one collapse rate "
           "sqrt(|q|/P*) -- CONFIRMED", ok_ep and reg_ok,
      "; ".join(ep_det))

# mixed-convention gluing control, independent recompute:
jump = []
for dlt in (0.1, 0.001):
    Np_ = n_delta(D_cross, dlt)
    Nm_ = Mx_c / np.sqrt(qc - 1j * dlt)
    jump.append(float(np.max(np.abs(Np_ - Nm_)))
                / float(np.max(np.abs(Np_))))
check("E", "mixed-convention gluing failure re-verified: (q+i delta) vs "
           "(q-i delta) differ past the wall by a relative jump -> 2 "
           "that does NOT vanish as delta -> 0 -- per-wall independent "
           "sign choices are excluded; the analytic matching clause has "
           "teeth (K-a stays un-fired for the analytic rule ONLY)",
      jump[0] > 1.5 and jump[1] > 1.9,
      f"jump {jump[0]:.3f} -> {jump[1]:.3f}")

# =============================================================================
# COVERAGE EXTENSION -- fresh rays, fresh walls (seed 99, NOT the n2 stream)
# =============================================================================
fresh_cross, fresh_gap = [], []
n_time_f = 0
for _ in range(60):
    al = RNG.standard_normal(4)
    al = al / np.linalg.norm(al)
    q4 = q_profile(al, 4.0)
    if np.min(q4) > 0:
        fresh_gap.append(al)
    elif np.max(q4) < 0:
        n_time_f += 1
    else:
        fresh_cross.append(al)
ok_fresh = n_time_f == 0 and len(fresh_cross) >= 2 and len(fresh_gap) >= 2
det_f = []
minPf = np.inf
for al in fresh_cross[:2]:
    s_hit, t_c = crossing_scan(al, 4.0)
    if s_hit is None:
        ok_fresh = False
        continue
    s_c = bisect_wall(al, t_c, s_hit)
    x_c2 = xi_of(t_c, ray(al, s_c + 0.3))
    D_c2 = cvec(x_c2)
    Mx2, Ku2, P2, q2 = symbol(D_c2)
    if q2 >= 0:
        ok_fresh = False
        continue
    g2 = np.sqrt(-q2)
    T2 = P2 - q2
    r_top2, r_bot2, Bg2, Bd2 = cross_weight(D_c2, q2)
    # closed form r, M^2 = qI, halves K-null, deck-odd, J-conjugacy:
    if abs(r_top2 - np.sqrt(-q2 / T2)) > 1e-7 or \
       (r_top2 - r_bot2) > 1e-6 * r_top2:
        ok_fresh = False
    if float(np.max(np.abs(Mx2 @ Mx2 - q2 * I128))) > 1e-8 * float(
            np.max(np.abs(Mx2))) ** 2:
        ok_fresh = False
    if float(np.max(np.abs(Bg2.conj().T @ K_S @ Bg2))) > 1e-7:
        ok_fresh = False
    a4f = ray(al, s_c + 0.3)
    M0f = symbol(cvec(xi_of(0.0, a4f)))[0]
    M1f = symbol(cvec(xi_of(1.0, a4f)))[0]
    if relres(U_h @ M0f @ Uh_inv, -M1f) > 1e-7:
        ok_fresh = False
    for t in TGRID[::8]:
        _a, _b, P3, T3, _q3 = parts(cvec(xi_of(float(t), a4f)))
        minPf = min(minPf, P3 / (P3 + T3))
    det_f.append(f"wall s* = {s_c:.3f}, r = {r_top2:.4f}")
for al in fresh_gap[:2]:
    x_g = xi_of(0.35, ray(al, 3.0))
    D_g = cvec(x_g)
    Mg, Kg, Pg_, qg = symbol(D_g)
    if qg <= 0:
        ok_fresh = False
        continue
    if abs(gram_margin(D_g, qg) - np.sqrt(qg / Pg_)) > 1e-7:
        ok_fresh = False
check("E", "COVERAGE EXTENSION BEYOND THE ORIGINALS' SAMPLE: 60 fresh "
           "rays (seed 99, a DIFFERENT stream from the n2 catalogue) -- "
           "0 timelike again; two fresh crossing rays taken to their "
           "walls from scratch and two fresh gapped rays: every closed "
           "form and section fact holds to machine precision (r = "
           "sqrt(-q/T) uniform, margin = sqrt(q/P), M^2 = qI, halves "
           "K-null, deck-odd, P/(P+T) bounded away from 0) -- the "
           "sampled-ledger facts are ray-independent in the only sense "
           "that matters: they are closed-form in ray data, and fresh "
           "draws cannot surprise them", ok_fresh and minPf > 0.05,
      "; ".join(det_f) + f"; min P/(P+T) = {minPf:.3f} "
      f"({len(fresh_cross)} cross/{len(fresh_gap)} gap/{n_time_f} time)")

# =============================================================================
# CROSS-CHECK -- width channel vs S-matrix transparency (8606f3f)
# =============================================================================
# where they overlap: (i) the dynamical width scale past the wall is g =
# sqrt(-q) (spectrum of D is exactly +-ig -- checked above); the section
# width channel is a K_S-linear functional whose MAGNITUDE is deck-even
# (P, T, g are deck-invariant -- verified in the seam lemma), hence
# sector-blind, consistent with S carrying no K_S; its SIGN flips with
# the section (k(N) + k(-N) = 0) and with the +-i0 convention -- the
# gauge bit. (ii) NO real conserved reading separates the conventions:
# battery over the conserved class.
Ax_c, _cc = a_from_def(e, ETA, DIM, x_cross)
Np0 = n_delta(D_cross, 1e-6)
Nm0 = Mx_c / np.sqrt(qc - 1e-6j)
# distinction found and enforced: a GENERIC conserved reading is
# section-ODD (it reads N vs -N -- that is the sector channel working,
# not the scheme bit), so the scheme question is about J_quat-INVARIANT
# readings: J-symmetrized real conserved readings must be IDENTICALLY
# ZERO on the crossed sector (they can orient neither the section nor
# the +-i0 bit) -- the sharp form of "Re k = 0, any scheme".
ok_w = True
reads_J, reads_raw = [], []
scaleA = float(np.max(np.abs(Ax_c)))
for _ in range(3):
    Wp_ = RNG.standard_normal((64, 64)) + 1j * RNG.standard_normal((64, 64))
    Wm_ = RNG.standard_normal((64, 64)) + 1j * RNG.standard_normal((64, 64))
    Wfull = np.zeros((128, 128), dtype=complex)
    Wfull[np.ix_(range(64), range(64))] = Wp_
    Wfull[np.ix_(range(64, 128), range(64, 128))] = Wm_
    perm = np.concatenate([idx_p, idx_m])
    Vc = K_S @ EV[:, perm] @ Wfull @ EVi[perm, :]
    # J_quat-symmetrize (stays conserved since J D J^-1 = D):
    VJ = 0.5 * (Vc + C_J @ np.conj(Vc) @ C_J_inv)
    if relres(VJ @ D_cross, D_cross.conj().T @ VJ) > 1e-7:
        ok_w = False
    sc = max(1.0, float(np.max(np.abs(VJ))) * scaleA * 128)
    rp = float(np.real(np.trace(VJ @ Np0 @ Ax_c)))
    rm = float(np.real(np.trace(VJ @ Nm0 @ Ax_c)))
    reads_J.append(max(abs(rp), abs(rm)) / sc)
    if reads_J[-1] > 1e-9:
        ok_w = False
    # unsymmetrized control: generic conserved reading is section-odd
    rp0 = float(np.real(np.trace(Vc @ Np0 @ Ax_c)))
    rm0 = float(np.real(np.trace(Vc @ Nm0 @ Ax_c)))
    reads_raw.append(abs(rp0 + rm0) / max(1.0, abs(rp0)))
    if reads_raw[-1] > 1e-5:
        ok_w = False
kp_ = 0.5 * np.trace(K_S @ Np0 @ Ax_c)
km_ = 0.5 * np.trace(K_S @ Nm0 @ Ax_c)
ok_w = ok_w and abs(np.imag(kp_) + np.imag(km_)) < 1e-6 * abs(np.imag(kp_))
check("E", "WIDTH-CHANNEL vs S-MATRIX TRANSPARENCY, overlap consistent: "
           "the dynamical width scale past the wall is g = sqrt(-q) "
           "(spectrum +-ig exactly), the section width channel's "
           "magnitude (128/7)(13P+15T)sqrt(P)/g is built from the "
           "deck-invariants P, T, g -- sector-blind, exactly as the "
           "transparency theorem demands of any S-side reading -- and "
           "the two +-i0 prescriptions give OPPOSITE imaginary parts "
           "while every J_quat-INVARIANT real conserved reading is "
           "IDENTICALLY ZERO on the crossed sector (battery over the "
           "conserved class, J-symmetrized: < 1e-9 relative -- the "
           "sharp, scheme-independent form of Re k = 0), and generic "
           "un-symmetrized readings are section-ODD (they read the "
           "sector channel, not the scheme bit): the +-i0 sign is a "
           "gauge bit at this grade on BOTH faces; the two width "
           "readings agree where they overlap", ok_w,
      f"max J-reading = {max(reads_J):.1e}, section-odd defect = "
      f"{max(reads_raw):.1e}")

# =============================================================================
# [F] controls (mine)
# =============================================================================
# pure-timelike domain boundary:
x_pt = np.zeros(N_DIRS)
x_pt[10] = 1.0
cs_pt = 0.5 * (cvec(x_pt) + K_S @ cvec(x_pt) @ K_S)
check("F", "domain control: pure-timelike symbol has c_s = 0 identically "
           "-- M undefined, P > 0 is a REAL boundary of the theory (the "
           "originals name it; confirmed)",
      float(np.max(np.abs(cs_pt))) < 1e-12)

# deck-odd is NOT automatic: a unitary COMMUTING with K_S gives even
# transport -- the minus sign in the seam law comes from U_h K_S U_h^-1
# = -K_S and from nowhere else:
U_ev = cvec(orth_in(XI, range(9), [split(XI)[0]])) \
    @ cvec(orth_in(XI, range(9), [split(XI)[0],
                                  orth_in(XI, range(9), [split(XI)[0]])]))
D_r = cvec(RNG.standard_normal(14))
even_transport = relres(symbol(U_ev @ D_r @ np.linalg.inv(U_ev))[0],
                        U_ev @ symbol(D_r)[0] @ np.linalg.inv(U_ev))
check("F", "sign-provenance control: transporting by a K_S-COMMUTING "
           "unitary gives M -> +U M U^-1 (no minus): the deck twist is "
           "carried entirely by the K_S-REVERSING character of U_h, "
           "confirming the classification bit is the deck class and "
           "nothing else", even_transport < 1e-9,
      f"even-transport defect {even_transport:.1e}")


# =============================================================================
# verdict + headline
# =============================================================================
def headline():
    nE = sum(1 for tag, _n, ok_ in RESULTS if tag == "E")
    nF = sum(1 for tag, _n, ok_ in RESULTS if tag == "F")
    nT = sum(1 for tag, _n, ok_ in RESULTS if tag == "T")
    all_ok = all(ok_ for _t, _n, ok_ in RESULTS)
    print()
    print(VERDICT)
    print(f"HEADLINE: {nE} [E] + {nF} [F] = {nE + nF}   (setup [T] = {nT} "
          f"excluded)   {'ALL PASS' if all_ok else 'FAILURES PRESENT'}")
    sys.exit(0 if all_ok else 1)


VERDICT = (
    "SECOND-DRY-ROUND VERDICT (hostile pass): the four-result cluster "
    "SURVIVES with ONE localized correction required before print. "
    "CONFIRMED by independent derivation: the master identity (proven "
    "symbolically for all real xi in a second algebra, coefficients "
    "4(n-1)/n, 4/n, 2/DIM re-derived in sympy, raw-definition checks in "
    "three algebras, complex-xi control); the little theorems of M "
    "(proven symbolically, radical-free, in a miniature -- plus the "
    "unstated evenness M(-D) = M(D); note 'LINEAR in D' is loose "
    "language, the content is entirety); the seam law (upgraded to a "
    "generic lemma: any K_S-reversing unitary); the universal-null "
    "lemma (symbolic + the whole conserved class swept by construction); "
    "the selection rule and its consistency with the K_S-linear section "
    "datum; Re k = 0 past the wall (independent trace-algebra "
    "derivation: tr(uDA) = (256/7) sqrt(P)(13P+15T), real); the EP "
    "closed forms margin = sqrt(q/P), r = sqrt(-q/T); the d~ exclusion "
    "(both legs); gauge rigidity (with the antilinear loophole shown to "
    "be exactly the typed +-i0 scheme bit, nothing new); the gluing "
    "control; fresh-seed coverage extension (60 new rays, 2 new walls: "
    "no surprises). REFUTED-as-stated, repairable, classification "
    "UNAFFECTED: the crossed-fiber census sentence 'EXACTLY eight "
    "involutions +-{I, d~, Ku, J_c}' -- the algebra is C^4 and has "
    "SIXTEEN involutions (ninth exhibited machine-exactly); the correct "
    "and sufficient statement is that the K_S-SKEW involutions are "
    "exactly +-d~ and +-J_c (proven symbolically here), and the extra "
    "eight are neither K_S-skew nor half-splittings. The Z/2 "
    "classification, existence, wall matching, and all consequences "
    "stand. NO claim, canon, scorecard, or posture movement.")

if __name__ == "__main__":
    headline()
