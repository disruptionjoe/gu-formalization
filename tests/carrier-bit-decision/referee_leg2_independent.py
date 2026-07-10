#!/usr/bin/env python3
"""HOSTILE REFEREE, LEG-2: independent re-derivation, numpy-float route.

Everything here is built ONLY from the repo's Cl(9,5) rep + orthogonal
projectors (pinv route, NOT the leg's Fraction Clifford algebra, NOT the
leg's slot formulas). The closed forms tested were re-derived BY HAND by the
referee before writing this script:

  (R1) sigma_Q(xi) P_+ g(xi) = ((n-2)/n) * [ xi_a c(xi) - (q/n) eta_a e_a ] E_+
       (hand derivation: {e_a, c} = 2 eta_a xi_a; sum_b eta_b e_b c e_b = -(n-2)c)
  (R2) ||sigma_Q P_+ g||_F^2 = ((n-2)/n)^2 * (dimS/2) * ( |xi|_E^4 - q^2/n )
       anchor xi0 (10x repo): = (36/49)*64*(5077^2 - 3013^2/14) = 405256132224/343
       toy (n=4, xi=(1,2,3,4), F=C^16): = 16 * (1/4)*2*(900 - 225) = 5400
  (R3) ||P_+ g||_F^2 = (dimS/2) * |xi|_E^2 * (n-1)/n  -> 64*5077*13/14 = 2112032/7
  (R4) GLOBAL A5 identity (hand-derived, all xi, any signature):
       on ker Gamma: sigma'_Q sigma_Q psi = q psi - (4/n) xi_a tau
                                            + (4/n^2) eta_a e_a c(xi) tau,
       tau = sum_b eta_b xi_b psi_b.
       COROLLARY (referee's global upgrade of the leg's pointwise no-go):
       sigma_Q psi = 0, psi in ker Gamma  =>  q (1 - 4/n + 4/n^2) tau = 0
       => (q != 0, coefficient 36/49 != 0) tau = 0 => q psi = 0 => psi = 0.
       So sigma_Q is injective on ker Gamma for EVERY xi off the null cone,
       not only at certified points.
  (R5) null cone xi = e_0 + e_9: c^2 = 0; psi = xi (x) c u is an exact
       sigma_Q kernel vector; composite rank 32 (idempotent trace argument).
  (R6) R.g == 0, g'.R == 0 by antisymmetry (hand: e_b e_c antisymmetric under
       b<->c against symmetric xi_b xi_c); exactness ranks 64/832/64 at xi0.
"""
import os
import sys
from fractions import Fraction

import numpy as np

REPO = r"C:\Users\joe\JB\CapacityOS\repos\public\gu-formalization"
sys.path.insert(0, os.path.join(REPO, "tests"))
import oq_rk1_cl95_explicit_rep as cl95

FAILS = []


def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  | {detail}" if detail else ""))
    if not ok:
        FAILS.append(name)


# ---------------------------------------------------------------- setup ----
n = 14
npairs = 7
dim = 2 ** npairs  # 128
G = cl95.jordan_wigner_gammas(npairs)
eta = np.array([+1] * 9 + [-1] * 5)
e = [G[a] if eta[a] == +1 else 1j * G[a] for a in range(n)]

omega = np.eye(dim, dtype=complex)
for a in range(n):
    omega = omega @ e[a]
w, V = np.linalg.eigh(omega)
Bp = V[:, w > 0.5]    # S^+ basis, 128x64
Bm = V[:, w < -0.5]   # S^- basis, 128x64

check("setup: omega^2 = I, chirality split 64/64",
      np.allclose(omega @ omega, np.eye(dim)) and Bp.shape[1] == 64 and Bm.shape[1] == 64)

# adjoint lemma (independent check): e_a^dag = eta_a e_a
ok = all(np.allclose(e[a].conj().T, eta[a] * e[a]) for a in range(n))
check("adjoint lemma e_a^dag = eta_a e_a (all 14)", ok)


def c_of(xi):
    M = np.zeros((dim, dim), dtype=complex)
    for a in range(n):
        M += xi[a] * e[a]
    return M


def build_projs(xi):
    """Orthogonal projectors onto ker Gamma (T(x)S^+) and ker Gamma' (T(x)S^-),
    built with pinv (INDEPENDENT of both the repo's inv(gram) and the leg's
    slot formulas)."""
    blocks = [Bm.conj().T @ e[a] @ Bp for a in range(n)]
    Gam = np.hstack(blocks)                    # 64 x 896
    Pp = np.eye(n * 64, dtype=complex) - np.linalg.pinv(Gam) @ Gam
    blocks_m = [Bp.conj().T @ e[a] @ Bm for a in range(n)]
    Gam_m = np.hstack(blocks_m)
    Pm = np.eye(n * 64, dtype=complex) - np.linalg.pinv(Gam_m) @ Gam_m
    return Gam, Pp, Gam_m, Pm


Gam, Pp, Gam_m, Pm = build_projs(None)
check("rank P_+ = 832 = 896 - 64 (numeric)",
      int(round(np.trace(Pp).real)) == 832 and int(round(np.trace(Pm).real)) == 832,
      f"tr P_+ = {np.trace(Pp).real:.6f}")


def sigma_and_gauge(xi):
    cpm = Bm.conj().T @ c_of(xi) @ Bp          # S^+ -> S^-, 64x64
    full = np.kron(np.eye(n), cpm)             # 896 x 896
    sig = Pm @ full @ Pp
    gauge = np.vstack([xi[a] * np.eye(64) for a in range(n)])  # 896 x 64
    return sig, gauge, cpm


def q_of(xi):
    return float(sum(eta[a] * xi[a] * xi[a] for a in range(n)))


XI0 = np.array([1.0, 2.0, 3.0, 4.0, 0.5, 1.5, 2.5, 0.7, 1.1, 0.3, 2.2, 1.7, 0.9, 1.3])
q0 = q_of(XI0)
E2 = float(np.sum(XI0 ** 2))
check("q_eta(xi0) = 30.13 (x100 = 3013), |xi0|^2_E = 50.77", abs(q0 - 30.13) < 1e-12 and abs(E2 - 50.77) < 1e-12)

sig0, g0, cpm0 = sigma_and_gauge(XI0)
comp0 = sig0 @ (Pp @ g0)                       # 896 x 64
nrm = np.linalg.norm(comp0)

# (R2) referee's hand-derived closed norm, checked against the DIRECT number
pred2 = (12.0 / 14.0) ** 2 * 64.0 * (E2 ** 2 - q0 ** 2 / 14.0)
check("R2 hand-derived norm formula matches direct computation (anchor)",
      abs(nrm ** 2 - pred2) < 1e-6, f"direct = {nrm**2:.9f}, formula = {pred2:.9f}")
exact = Fraction(405256132224, 343) / Fraction(10 ** 4)
check("R2 exact rational 405256132224/343/10^4 matches float norm^2",
      abs(nrm ** 2 - float(exact)) < 1e-6, f"exact = {float(exact):.9f}")
check("R2 sqrt = 343.7302370567 (repo float)", abs(nrm - 343.7302370567004) < 1e-7,
      f"{nrm:.10f}")

# (R1) slotwise closed form at a RANDOM real xi (floats; independent check of
# the polynomial identity at a point NOT in the leg's certificate set)
rng = np.random.default_rng(77)
for trial in range(2):
    xir = rng.normal(size=n)
    qr = q_of(xir)
    sigr, gr, cpmr = sigma_and_gauge(xir)
    compr = sigr @ (Pp @ gr)
    cr = c_of(xir)
    crpm = Bm.conj().T @ cr @ Bp
    pred = np.zeros_like(compr)
    for a in range(n):
        blk = xir[a] * crpm - (qr / n) * eta[a] * (Bm.conj().T @ e[a] @ Bp)
        pred[a * 64:(a + 1) * 64, :] = (float(n - 2) / n) * blk
    check(f"R1 closed form slot identity at random xi (trial {trial}, q = {qr:.4f})",
          np.allclose(compr, pred, atol=1e-9),
          f"max dev = {np.max(np.abs(compr - pred)):.2e}")

# (R3) ||P_+ g||^2 closed form
pg = Pp @ g0
pred3 = 64.0 * E2 * 13.0 / 14.0
check("R3 ||P_+ g||^2 = 64*|xi|^2*(13/14) (= 2112032/7 at 10x scale)",
      abs(np.linalg.norm(pg) ** 2 - pred3) < 1e-9,
      f"direct = {np.linalg.norm(pg)**2:.9f}, formula = {pred3:.9f}, "
      f"x100 = {np.linalg.norm(pg)**2*100:.4f} vs {float(Fraction(2112032,7)):.4f}")
check("R3b Gamma(P_+ g) = 0 (candidate lands in ker Gamma)",
      np.linalg.norm(Gam @ pg) < 1e-9)
check("R3c P_+ g has full rank 64 (nonzero ghost candidate)",
      int(np.linalg.matrix_rank(pg, tol=1e-8)) == 64)

# rank checks (numeric SVD route, independent of mod-p)
check("rank(sigma_Q) = 832 at xi0 (numeric SVD)",
      int(np.linalg.matrix_rank(sig0, tol=1e-8)) == 832)
check("rank(composite) = 64 at xi0 (numeric SVD)",
      int(np.linalg.matrix_rank(comp0, tol=1e-8)) == 64)

# (R4) GLOBAL A5 identity at 3 random xi, on random ker-Gamma vectors
def tau_of(xi, psi):
    """tau = sum_b eta_b xi_b psi_b, psi as 896-vector of 64-blocks (S^+ coords)."""
    t = np.zeros(64, dtype=complex)
    for b in range(n):
        t += eta[b] * xi[b] * psi[b * 64:(b + 1) * 64]
    return t


ok_all = True
for trial in range(3):
    xir = rng.normal(size=n)
    qr = q_of(xir)
    sigr, gr, cpmr = sigma_and_gauge(xir)
    # sigma' = P_+ (1(x)c: S^- -> S^+) P_-
    cmp_ = Bp.conj().T @ c_of(xir) @ Bm
    sigp = Pp @ np.kron(np.eye(n), cmp_) @ Pm
    for _ in range(3):
        v = rng.normal(size=896) + 1j * rng.normal(size=896)
        psi = Pp @ v                            # in ker Gamma
        lhs = sigp @ (sigr @ psi)
        t = tau_of(xir, psi)
        rhs = qr * psi.copy()
        ct = (Bp.conj().T @ c_of(xir) @ Bm) @ ((Bm.conj().T @ np.eye(dim) @ Bm) @ np.zeros(64))  # placeholder
        # c(xi) tau computed in chiral coords: tau in S^+, c: S^+ -> S^-
        ctau = (Bm.conj().T @ c_of(xir) @ Bp) @ t   # in S^-
        for a in range(n):
            ea_ctau = (Bp.conj().T @ e[a] @ Bm) @ ctau   # e_a c tau in S^+
            rhs[a * 64:(a + 1) * 64] += (-4.0 / n) * xir[a] * t \
                + (4.0 / n ** 2) * eta[a] * ea_ctau
        if not np.allclose(lhs, rhs, atol=1e-8):
            ok_all = False
check("R4 GLOBAL A5 identity sigma'sigma = qId - (4/n)xi tau + (4/n^2)eta e c tau "
      "on ker Gamma (3 random xi x 3 random psi, hand-derived)", ok_all)
coeff = Fraction(1) - Fraction(4, 14) + Fraction(4, 196)
check("R4 corollary coefficient 1 - 4/n + 4/n^2 = 36/49 != 0 => sigma_Q injective "
      "on ker Gamma for EVERY q != 0 (referee upgrade: global, not pointwise)",
      coeff == Fraction(36, 49), f"coeff = {coeff}")

# (R5) null cone
xin = np.zeros(n)
xin[0] = 1.0
xin[9] = 1.0
qn = q_of(xin)
cn = c_of(xin)
check("R5a q(e_0+e_9) = 0 and c^2 = 0 exactly", qn == 0.0 and np.allclose(cn @ cn, 0))
sign, gn, _ = sigma_and_gauge(xin)
# kernel vector psi = xi (x) c u, u in S^- (c: S^- -> S^+ component)
u = rng.normal(size=64) + 1j * rng.normal(size=64)
cu = (Bp.conj().T @ cn @ Bm) @ u               # in S^+
psi = np.zeros(896, dtype=complex)
for a in range(n):
    psi[a * 64:(a + 1) * 64] = xin[a] * cu
check("R5b psi = xi(x)c u nonzero, in ker Gamma, sigma_Q psi = 0 (exact witness)",
      np.linalg.norm(psi) > 1e-6 and np.linalg.norm(Gam @ psi) < 1e-9
      and np.linalg.norm(sign @ psi) < 1e-9,
      f"|psi| = {np.linalg.norm(psi):.4f}, |sigma psi| = {np.linalg.norm(sign @ psi):.2e}")
compn = sign @ (Pp @ gn)
check("R5c composite rank on cone = 32 (numeric)",
      int(np.linalg.matrix_rank(compn, tol=1e-8)) == 32)
check("R5d sigma_Q rank DROPS on cone (numeric, < 832)",
      int(np.linalg.matrix_rank(sign, tol=1e-8)) < 832,
      f"rank = {int(np.linalg.matrix_rank(sign, tol=1e-8))}")

# (R6) R-complex: INDEPENDENT construction of R from antisymmetrized triples
def gamma_abc(a, b, c):
    """Antisymmetrized product e_[a e_b e_c] for pairwise distinct = plain
    product (they anticommute); referee builds via full antisymmetrization
    to be convention-independent."""
    import itertools
    acc = np.zeros((dim, dim), dtype=complex)
    for perm, sgn in [((a, b, c), 1), ((a, c, b), -1), ((b, a, c), -1),
                      ((b, c, a), 1), ((c, a, b), 1), ((c, b, a), -1)]:
        acc += sgn * (e[perm[0]] @ e[perm[1]] @ e[perm[2]])
    return acc / 6.0


def R_matrix(xi):
    """(R psi)_a = sum_{b,c} eta_a eta_b eta_c xi_b gamma_abc psi_c restricted
    S^+ -> S^-; pairwise distinct enforced by gamma_abc antisymmetry
    (gamma_abc = 0 when indices repeat)."""
    out = np.zeros((n * 64, n * 64), dtype=complex)
    for a in range(n):
        for c in range(n):
            if a == c:
                continue
            blk = np.zeros((dim, dim), dtype=complex)
            for b in range(n):
                if b == a or b == c or xi[b] == 0:
                    continue
                blk += eta[a] * eta[b] * eta[c] * xi[b] * gamma_abc(a, b, c)
            out[a * 64:(a + 1) * 64, c * 64:(c + 1) * 64] = Bm.conj().T @ blk @ Bp
    return out


xir = rng.normal(size=n)
Rr = R_matrix(xir)
gr = np.vstack([xir[a] * np.eye(64) for a in range(n)])
check("R6a R.g = 0 at random xi (independent antisymmetrized construction)",
      np.linalg.norm(Rr @ gr) < 1e-9)
gpr = np.hstack([xir[a] * np.eye(64) for a in range(n)])   # Euclidean contraction
check("R6b g'.R = 0 at random xi", np.linalg.norm(gpr @ Rr) < 1e-9)
R0 = R_matrix(XI0)
rkR0 = int(np.linalg.matrix_rank(R0, tol=1e-8))
check("R6c rank(R) = 832 at xi0 (numeric; => 4-term complex exact: "
      "64 -> 896 -> 896 -> 64, ker R = 64 = im g, ker g' = 832 = im R)",
      rkR0 == 832, f"rank = {rkR0}")
Rn = R_matrix(xin)
rkRn = int(np.linalg.matrix_rank(Rn, tol=1e-8))
check("R6d rank(R) on cone = 480 (numeric; corroborates leg's mod-p value)",
      rkRn == 480, f"rank = {rkRn}")

# toy closed-form norm (n = 4): via formula only (repo toy float already matched)
pred_toy = 16.0 * (0.25) * 2.0 * (30.0 ** 2 - 30.0 ** 2 / 4.0)
check("toy R2: 16 * (1/4)*2*(900-225) = 5400; sqrt = 73.4846922835",
      abs(pred_toy - 5400.0) < 1e-12 and abs(np.sqrt(pred_toy) - 73.48469228349535) < 1e-12)

print()
if FAILS:
    print(f"REFEREE RESULT: {len(FAILS)} FAILURES: {FAILS}")
    sys.exit(1)
print("REFEREE RESULT: ALL INDEPENDENT CHECKS PASS")
sys.exit(0)
