#!/usr/bin/env python3
r"""W131 -- THE COVARIANT OPERATOR ON Y14 (H68): first swing, build-or-prove-unbuildable.

CONTEXT
-------
W125 (explorations/W125-source-action-first-build-2026-07-13.md) built the source-action
candidate at the FLAT 14-dim symbol level and named ONE object blocking acceptance legs
(a)-full and (d)-full, SA-G9's arena, FC-VZ-1, and the first source-action number: the
covariant operator on curved Y14 = Met(X4). This file is the first build attempt.

THE CANDIDATE (the natural one, per the spec's consumers)
---------------------------------------------------------
  D  =  Pi (gamma^I nabla_I) Pi  +  m2 Pi     on sections of  ker Gamma  inside the
        RS bundle  T*Y14 (x) S(9,5),
with nabla the connection induced by the gimmel Levi-Civita connection (spin lift on S,
Levi-Civita on T*Y14; A = spin-lift(grad^gimmel) is the wave34 ledger item 2 datum).

THE CRUX is [nabla, Pi]. Pi is built pointwise from Gamma = (gamma-trace), so Pi is
parallel iff Gamma is parallel iff Gamma intertwines the so(9,5) action on V (x) S with
the action on S -- because ANY metric-compatible connection has an so(9,5)-valued
connection form in an orthonormal frame, and in such a frame Gamma is the CONSTANT
equivariant map. Equivariance was checked in W125 only on 3 self-dual (space-space)
generators; the boosts (space-time mixing, the II_s-shaped directions) were open.

WHAT THIS FILE COMPUTES (deterministic; the verified Cl(9,5) = M(64,H) rep throughout)
--------------------------------------------------------------------------------------
BLOCK A (exact algebra, all 91 generators of so(9,5)):
  A1. Gamma Gamma^dag = 14 I  (so Pi = I - Gamma^dag Gamma / 14, closed form).
  A2. FULL equivariance: Gamma rho(J) = Sigma_J Gamma AND rho(J) Gamma^dag =
      Gamma^dag Sigma_J for ALL 91 generators (rotations, time-time rotations, boosts),
      with the eta-corrected vector action M[i,j] = eta_j, M[j,i] = -eta_i.
      COROLLARY (with A1): [rho(J), Pi] = -(1/14) Gamma^dag (Sigma_J - Sigma_J) Gamma = 0
      for all 91: GAMMA IS PARALLEL, [nabla, Pi] = 0 for EVERY metric-compatible
      connection on Y14, in particular the gimmel Levi-Civita spin lift.
  A3. Direct full-matrix check of [rho(J), Pi] = 0 on 6 representative generators
      (space-space, time-time, boost).
  A4. Krein parallelism: rho(J)^dag K + K rho(J) = 0 for all 91 (K = eta_V (x) beta_S,
      the W125 Krein structure), via the exact factor identities M^dag eta + eta M = 0
      and Sigma^dag beta + beta Sigma = 0. So nabla K = 0: Krein self-adjointness of the
      built operator survives covariantization (SA-U1's tree leg goes curved).
  A5. Covariant leakage: Gamma rho(J) Pi = Sigma_J (Gamma Pi) = 0 -- the constraint
      closes under covariant differentiation; leakage stays 0 on curved Y14.

BLOCK B (the actual Y14 geometry, numeric, base dim n = 4 Lorentzian):
  B1. gimmel signature at Lorentzian points is (9,5): base (3,1) + trace-reversed
      DeWitt fiber (6,4). The pointwise model of the flat build IS eta(9,5).
  B2. Parallel transport along a curve in Y14 (RK4 on the finite-difference
      Christoffels of the explicit gimmel metric) preserves gimmel inner products:
      the holonomy/connection is O(9,5)-valued -- the hypothesis of Block A is the
      actual Y14 connection, machine-checked, not assumed.
  B3. Graph-section Gauss check at n = 4 (H21's theorem, numerically, native
      dimension): tangential part of the ambient derivative = Koszul of the induced
      metric; the normal residual II_s is nonzero and symmetric. So the section insert
      II_s is real, and it rides INSIDE the O(9,5) connection form (B2) -- it acts on
      the RS bundle through rho, i.e. through Block A.
BLOCK C (the covariant operator's symbol on curved Y14):
  C1. Flat-limit positive control: W125 anchors reproduced (C2 = 155.3625, rank Pi
      = 1664, leakage(g=1) = 0, R degree-1 exact, off-cone/on-cone sigma_min).
  C2. Curved-point symbol: at an actual curved-Y14 point (Block B metric), in a
      gimmel-orthonormal frame, the characteristic variety of the restricted symbol is
      exactly the gimmel null cone {G^{-1}(xi,xi) = 0} (off-cone non-degenerate both
      signs; an exact gimmel-null covector degenerates to machine precision).
  C3. Curvature/II_s inserts on curved Y14: ANY so(9,5)-valued zeroth-order insert
      B0 = rho(w) (curvature contractions, II_s blocks, connection-choice differences)
      (i) commutes with Pi, (ii) produces zero leakage, (iii) is Krein-compatible,
      (iv) is strictly subprincipal. The W125-D failure mode (first-order insert
      kron(II_sym, c(xi))) has a SYMMETRIC vector factor, provably OUTSIDE so(9,5):
      metric-compatible covariantization cannot generate it. SA-C4's protection
      survives curvature at symbol level as a STRUCTURE THEOREM, not an estimate.

HONEST SCOPE (read before quoting)
----------------------------------
- Frame/symbol level on the actual Y14 geometry: pointwise + holonomy checks on the
  explicit gimmel metric, exact algebra on the verified rep. NOT built here: the
  analytic layer (Fredholm/propagator theory on the NON-COMPACT Y14), all-orders
  well-posedness, and SA-G9 (even-sector linearization, untouched).
- Preconditions inherited, named: X4 spin (canon/w2-y14-spin-structure.md, W2-01:
  Y14 spin iff X4 spin) and gimmel nondegeneracy on the Lorentzian locus (checked
  pointwise at samples, not globally characterized).
- The 4D section-REDUCED Schur route (cure A) is untouched; the repo VZ verdict
  (CONDITIONALLY_RESOLVED) is not upgraded by this file.

Reproducible: python -u tests/W131_covariant_operator_y14.py  (exit 0 iff PASS).
Runtime ~2-4 min (full-matrix checks on 6 generators; a few 1664-dim SVDs).
"""
from __future__ import annotations

import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_GENSEC = os.path.normpath(os.path.join(_HERE, "generation-sector"))
for _p in (_GENSEC, _HERE):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import gen_sector_bridge as gb  # noqa: E402

TOL = 1e-9
FAIL: list[str] = []
N, DIM = 14, 128
ETA = np.array([1.0] * 9 + [-1.0] * 5)
RNG = np.random.default_rng(20260714)


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {detail}" if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)
    return bool(ok)


def log(msg):
    print(msg, flush=True)


# ==================================================================================================
# BLOCK A -- exact algebra: Gamma is parallel; [nabla, Pi] = 0; nabla K = 0
# ==================================================================================================
def block_A(e, Gamma, Pi):
    log("\n" + "=" * 100)
    log("BLOCK A -- [nabla, Pi] = 0: full so(9,5) equivariance of Gamma (all 91 generators)")
    log("=" * 100)

    I128 = np.eye(DIM, dtype=complex)
    I14 = np.eye(N, dtype=complex)

    # A1: Gamma Gamma^dag = 14 I  ->  Pi = I - Gamma^dag Gamma / 14 in closed form.
    GGd = Gamma @ Gamma.conj().T
    a1 = float(np.max(np.abs(GGd - N * np.eye(DIM))))
    Pi_closed = np.eye(N * DIM, dtype=complex) - Gamma.conj().T @ Gamma / N
    a1b = float(np.max(np.abs(Pi_closed - Pi)))
    check("A1. Gamma Gamma^dag = 14 I exactly, so Pi = I - Gamma^dag Gamma / 14 (closed form; "
          "the Gram inverse in Pi is scalar)",
          a1 < 1e-12 and a1b < 1e-12, f"||GG^dag - 14I||={a1:.1e}, ||Pi_closed - Pi||={a1b:.1e}")

    # so(9,5) generator factory: vector factor M_ij (eta-corrected) + spinor factor Sigma_ij.
    def Mvec(i, j):
        M = np.zeros((N, N), dtype=complex)
        M[i, j], M[j, i] = ETA[j], -ETA[i]
        return M

    def Sgen(i, j):
        return 0.25 * (e[i] @ e[j] - e[j] @ e[i])

    gens = [(i, j) for i in range(N) for j in range(i + 1, N)]
    assert len(gens) == 91

    # Krein structure (W125 B2): K = eta_V (x) beta_S, beta_S = e_0 ... e_8.
    beta_S = e[0].copy()
    for a in range(1, 9):
        beta_S = beta_S @ e[a]

    # A2: full equivariance, both sides, all 91 (blockwise: cheap).
    res_left, res_right, res_krM, res_krS, res_soM = [], [], [], [], []
    for (i, j) in gens:
        M, S = Mvec(i, j), Sgen(i, j)
        # left: Gamma rho(J) = Sigma Gamma. Gamma kron(I,S): blocks e_c S.
        # Gamma kron(M,I): block d = sum_c M[c,d] e_c.
        lhs_blocks = []
        for d in range(N):
            blk = e[d] @ S
            for c in range(N):
                if M[c, d] != 0:
                    blk = blk + M[c, d] * e[c]
            lhs_blocks.append(blk - S @ e[d])
        res_left.append(max(float(np.max(np.abs(b))) for b in lhs_blocks))
        # right: rho(J) Gamma^dag = Gamma^dag Sigma. Row block c of rho(J) Gamma^dag:
        # S e_c^dag + sum_d M[c,d] e_d^dag ; of Gamma^dag Sigma: e_c^dag S.
        rhs_blocks = []
        for c in range(N):
            blk = S @ e[c].conj().T - e[c].conj().T @ S
            for d in range(N):
                if M[c, d] != 0:
                    blk = blk + M[c, d] * e[d].conj().T
            rhs_blocks.append(blk)
        res_right.append(max(float(np.max(np.abs(b))) for b in rhs_blocks))
        # A4 factor identities: M^dag eta + eta M = 0 and Sigma^dag beta + beta Sigma = 0.
        res_krM.append(float(np.max(np.abs(M.conj().T @ np.diag(ETA) + np.diag(ETA) @ M))))
        res_krS.append(float(np.max(np.abs(S.conj().T @ beta_S + beta_S @ S))))
        # membership: eta M antisymmetric (M in so(9,5)).
        EM = np.diag(ETA) @ M
        res_soM.append(float(np.max(np.abs(EM + EM.T))))
    check("A2. FULL equivariance of Gamma under so(9,5), ALL 91 generators, BOTH sides "
          "(Gamma rho = Sigma Gamma and rho Gamma^dag = Gamma^dag Sigma; boosts included, "
          "the directions W125 left open) -- with A1 this PROVES [rho(J), Pi] = 0 for all 91: "
          "Gamma is parallel, [nabla, Pi] = 0 for every metric-compatible connection on Y14",
          max(res_left) < 1e-12 and max(res_right) < 1e-12 and max(res_soM) < 1e-12,
          f"max left={max(res_left):.1e}, max right={max(res_right):.1e}, "
          f"max ||eta M + (eta M)^T||={max(res_soM):.1e}")

    # A3: direct full-matrix confirmation on 6 representative generators.
    reps = [(0, 1), (2, 7), (9, 10), (12, 13), (0, 9), (8, 13)]  # 2 space, 2 time, 2 boost
    direct = []
    for (i, j) in reps:
        rho = np.kron(Mvec(i, j), I128) + np.kron(I14, Sgen(i, j))
        direct.append(float(np.linalg.norm(rho @ Pi - Pi @ rho)))
    check("A3. Direct full-matrix check: ||[rho(J), Pi]|| = 0 on 6 representative generators "
          "(2 space-space, 2 time-time, 2 BOOSTS -- the II_s-shaped mixing directions)",
          max(direct) < 1e-9,
          "; ".join(f"J({i},{j})={r:.1e}" for (i, j), r in zip(reps, direct)))

    # A4: Krein parallelism, all 91 via factors + full-matrix on the sampled 6.
    K = np.kron(np.diag(ETA).astype(complex), beta_S)
    kr_direct = []
    for (i, j) in reps:
        rho = np.kron(Mvec(i, j), I128) + np.kron(I14, Sgen(i, j))
        kr_direct.append(float(np.linalg.norm(rho.conj().T @ K + K @ rho)))
    check("A4. KREIN PARALLELISM: rho(J)^dag K + K rho(J) = 0 for ALL 91 generators "
          "(exact factor identities M^dag eta + eta M = 0, Sigma^dag beta + beta Sigma = 0; "
          "full-matrix on the sampled 6) -> nabla K = 0: the Krein structure is covariantly "
          "constant, tree [P,S] = 0 survives covariantization (SA-U1 tree leg goes curved)",
          max(res_krM) < 1e-12 and max(res_krS) < 1e-10 and max(kr_direct) < 1e-9,
          f"max factor residuals: M={max(res_krM):.1e}, Sigma={max(res_krS):.1e}; "
          f"max full={max(kr_direct):.1e}")

    # A5: covariant leakage.
    GPi = float(np.linalg.norm(Gamma @ Pi))
    leak_cov = []
    for (i, j) in reps:
        rho = np.kron(Mvec(i, j), I128) + np.kron(I14, Sgen(i, j))
        leak_cov.append(float(np.linalg.norm(Gamma @ rho @ Pi)))
    check("A5. COVARIANT LEAKAGE = 0: Gamma rho(J) Pi = Sigma (Gamma Pi) = 0 (Gamma Pi = 0 "
          "exactly + A2). The ker-Gamma constraint closes under covariant differentiation: "
          "the connection term of Pi (gamma . nabla) Pi leaks nothing on curved Y14",
          GPi < 1e-9 and max(leak_cov) < 1e-7,
          f"||Gamma Pi||={GPi:.1e}, max ||Gamma rho Pi||={max(leak_cov):.1e}")

    return Mvec, Sgen, K, beta_S


# ==================================================================================================
# BLOCK B -- the actual Y14 geometry (n = 4 Lorentzian): signature, holonomy, Gauss/II_s
# ==================================================================================================
PAIRS = [(a, b) for a in range(4) for b in range(a, 4)]  # 10 fiber coordinates
NF = len(PAIRS)


def vmat(comps):
    M = np.zeros((4, 4))
    for idx, (a, b) in enumerate(PAIRS):
        M[a, b] = comps[idx]
        M[b, a] = comps[idx]
    return M


def comps_of(M):
    return np.array([M[a, b] for (a, b) in PAIRS])


EBASIS = [vmat([1.0 if k == idx else 0.0 for k in range(NF)]) for idx in range(NF)]


def fiber_metric(h):
    """Trace-reversed DeWitt fiber metric V_h(k,l) = tr(h^-1 k h^-1 l) - 1/2 tr(h^-1 k) tr(h^-1 l)."""
    hinv = np.linalg.inv(h)
    A = [hinv @ Ek for Ek in EBASIS]
    V = np.zeros((NF, NF))
    for i in range(NF):
        for j in range(NF):
            V[i, j] = np.trace(A[i] @ A[j]) - 0.5 * np.trace(A[i]) * np.trace(A[j])
    return V


def gimmel(Hvec):
    """The 14x14 gimmel metric at fiber point h = vmat(Hvec): base block h, fiber block V_h."""
    h = vmat(Hvec)
    G = np.zeros((14, 14))
    G[:4, :4] = h
    G[4:, 4:] = fiber_metric(h)
    return G


def christoffel(Hvec, step=1e-5):
    """Christoffels of gimmel at (x, Hvec); metric depends only on the 10 fiber coords."""
    G = gimmel(Hvec)
    Ginv = np.linalg.inv(G)
    dG = np.zeros((14, 14, 14))  # dG[M] = partial_M G
    for k in range(NF):
        Hp, Hm = Hvec.copy(), Hvec.copy()
        Hp[k] += step
        Hm[k] -= step
        dG[4 + k] = (gimmel(Hp) - gimmel(Hm)) / (2 * step)
    Gam = np.zeros((14, 14, 14))  # Gam[I,J,K] = Gamma^I_{JK}
    for J in range(14):
        for K in range(14):
            v = 0.5 * (dG[J][:, K] + dG[K][:, J] - dG[:, J, K])
            Gam[:, J, K] = Ginv @ v
    return Gam


def block_B():
    log("\n" + "=" * 100)
    log("BLOCK B -- the actual Y14 = Met(X4) geometry: signature (9,5), O(9,5) holonomy, II_s")
    log("=" * 100)

    # B1: signature at Lorentzian sample points.
    sigs = []
    for _ in range(3):
        h = np.diag([1.0, 1.0, 1.0, -1.0]) + 0.15 * _sym4()
        G = gimmel(comps_of(h))
        w = np.linalg.eigvalsh(G)
        sigs.append((int(np.sum(w > 0)), int(np.sum(w < 0))))
    check("B1. gimmel SIGNATURE = (9,5) at Lorentzian sample points: base (3,1) + trace-reversed "
          "DeWitt fiber (6,4). The flat eta(9,5) symbol model of W125 IS the pointwise model of "
          "curved Y14 (this is the load-bearing pointwise identification)",
          all(s == (9, 5) for s in sigs), f"signatures={sigs}")

    # B2: parallel transport preserves gimmel -> holonomy in O(9,5).
    H0 = comps_of(np.diag([1.0, 1.0, 1.0, -1.0]) + 0.1 * _sym4())
    dH = 0.3 * RNG.normal(size=NF)
    v = RNG.normal(size=14)
    w = RNG.normal(size=14)
    G0 = gimmel(H0)
    ips0 = (v @ G0 @ v, v @ G0 @ w, w @ G0 @ w)

    def rhs(t, state):
        vv, ww = state
        H = H0 + t * dH
        Gam = christoffel(H)
        zdot = np.concatenate([np.zeros(4), dH])
        dv = -np.einsum('ijk,j,k->i', Gam, zdot, vv)
        dw = -np.einsum('ijk,j,k->i', Gam, zdot, ww)
        return dv, dw

    nsteps, hstep = 40, 1.0 / 40
    t = 0.0
    for _ in range(nsteps):
        k1 = rhs(t, (v, w))
        k2 = rhs(t + hstep / 2, (v + hstep / 2 * k1[0], w + hstep / 2 * k1[1]))
        k3 = rhs(t + hstep / 2, (v + hstep / 2 * k2[0], w + hstep / 2 * k2[1]))
        k4 = rhs(t + hstep, (v + hstep * k3[0], w + hstep * k3[1]))
        v = v + hstep / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        w = w + hstep / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        t += hstep
    G1 = gimmel(H0 + dH)
    ips1 = (v @ G1 @ v, v @ G1 @ w, w @ G1 @ w)
    drift = max(abs(a - b) for a, b in zip(ips0, ips1)) / max(abs(x) for x in ips0)
    check("B2. HOLONOMY IN O(9,5): parallel transport (RK4 on the finite-difference Christoffels "
          "of the explicit gimmel metric) preserves gimmel inner products along a curve in Y14. "
          "So the actual Y14 connection form is so(9,5)-valued in orthonormal frames: Block A's "
          "hypothesis is the REAL geometry, machine-checked",
          drift < 1e-5, f"relative inner-product drift over the curve = {drift:.1e}")

    # B3: graph-section Gauss check at native n = 4 (H21's theorem numerically).
    h = np.diag([1.0, 1.0, 1.0, -1.0]) + 0.1 * _sym4()
    Dg = [0.08 * _sym4() for _ in range(4)]                     # dg/dx_mu at x0 = 0
    DDg = [[None] * 4 for _ in range(4)]                        # ddg, symmetric in (mu,nu)
    for mu in range(4):
        for nu in range(mu, 4):
            S = 0.08 * _sym4()
            DDg[mu][nu] = S
            DDg[nu][mu] = S

    def gx(x):
        M = h.copy()
        for mu in range(4):
            M = M + x[mu] * Dg[mu]
            for nu in range(4):
                M = M + 0.5 * x[mu] * x[nu] * DDg[mu][nu]
        return M

    def tangents(x):
        T = np.zeros((4, 14))
        step = 1e-5
        for mu in range(4):
            T[mu, mu] = 1.0
            xp, xm = x.copy(), x.copy()
            xp[mu] += step
            xm[mu] -= step
            T[mu, 4:] = comps_of((gx(xp) - gx(xm)) / (2 * step))
        return T

    x0 = np.zeros(4)
    Hs = comps_of(gx(x0))
    Gs = gimmel(Hs)
    Gam = christoffel(Hs)
    T = tangents(x0)
    # ambient covariant derivative nabla_{T_mu} T_nu at s(x0)
    nab = np.zeros((4, 4, 14))
    for mu in range(4):
        for nu in range(4):
            nab[mu, nu, 4:] = comps_of(DDg[mu][nu])            # d_mu T_nu (fiber part)
            nab[mu, nu] += np.einsum('ijk,j,k->i', Gam, T[mu], T[nu])
    gbar = T @ Gs @ T.T                                         # induced metric
    # Koszul of the induced metric via finite differences in x
    step = 1e-4
    dgbar = np.zeros((4, 4, 4))
    for lam in range(4):
        xp, xm = x0.copy(), x0.copy()
        xp[lam] += step
        xm[lam] -= step
        Tp, Tm = tangents(xp), tangents(xm)
        Gp, Gm = gimmel(comps_of(gx(xp))), gimmel(comps_of(gx(xm)))
        dgbar[lam] = (Tp @ Gp @ Tp.T - Tm @ Gm @ Tm.T) / (2 * step)
    gauss_res, II = 0.0, np.zeros((4, 4, 14))
    gbari = np.linalg.inv(gbar)
    for mu in range(4):
        for nu in range(4):
            kosz = 0.5 * (dgbar[mu][nu] + dgbar[nu][mu] - dgbar[:, mu, nu])  # (lam)
            proj = T @ Gs @ nab[mu, nu]                         # gimmel(nabla, T_lam)
            gauss_res = max(gauss_res, float(np.max(np.abs(proj - kosz))))
            coeff = gbari @ proj
            II[mu, nu] = nab[mu, nu] - coeff @ T
    II_norm = float(np.linalg.norm(II))
    II_asym = float(np.max(np.abs(II - II.transpose(1, 0, 2))))
    check("B3. GAUSS AT NATIVE n = 4 (H21's theorem, numerically, off-shell data): the "
          "tangential part of the ambient gimmel derivative equals the Koszul bracket of the "
          "induced metric; the normal residual II_s = s*(theta) is NONZERO and symmetric. The "
          "section insert is real, and by B2 it sits inside an so(9,5)-valued connection form: "
          "it acts on the RS bundle through rho, i.e. through Block A",
          gauss_res < 1e-4 and II_norm > 1e-3 and II_asym < 1e-6,
          f"Gauss residual={gauss_res:.1e}, ||II||={II_norm:.3f}, asym={II_asym:.1e}")

    return Hs


def _sym4():
    S = RNG.normal(size=(4, 4))
    return 0.5 * (S + S.T)


# ==================================================================================================
# BLOCK C -- the covariant operator's symbol on curved Y14
# ==================================================================================================
def block_C(e, Gamma, Pi, Mvec, Sgen, K_krein, Hs):
    log("\n" + "=" * 100)
    log("BLOCK C -- the covariant symbol: curved characteristic cone; inserts are subprincipal")
    log("=" * 100)

    I128 = np.eye(DIM, dtype=complex)
    I14 = np.eye(N, dtype=complex)
    w_, V_ = np.linalg.eigh(Pi)
    Kb = V_[:, w_ > 0.5]                                        # 1792 x 1664 ker-Gamma basis

    def cxi(xi):
        return sum(xi[a] * e[a] for a in range(N))

    def R(xi, extra=None):
        M = np.kron(I14, cxi(xi))
        if extra is not None:
            M = M + extra
        return Kb.conj().T @ (M @ Kb)

    def smin(xi, extra=None):
        return float(np.linalg.svd(R(xi, extra), compute_uv=False)[-1])

    # C1: flat-limit positive control (W125 anchors).
    C2 = gb.C2()
    MD = np.kron(I14, cxi(gb.XI))
    leak1 = float(np.linalg.norm(Gamma @ (Pi @ MD @ Pi) @ Pi))
    xi = RNG.normal(size=N)
    lin = float(np.max(np.abs(R(2 * xi) - 2 * R(xi))))
    xin = np.zeros(N)
    xin[0], xin[9] = 1.0, 1.0
    s_null_flat = smin(xin)
    s_off_flat = smin(xi)
    check("C1. FLAT-LIMIT POSITIVE CONTROL (W125 anchors reproduced): C2 = 155.3625, "
          "rank Pi = 1664, leakage(g=1) = 0, R exactly degree-1, eta-null covector degenerate, "
          "off-cone non-degenerate",
          abs(C2 - 155.3625069) < 1e-4 and int(round(np.trace(Pi).real)) == 1664
          and leak1 < TOL and lin < 1e-10 and s_null_flat < 1e-10 and s_off_flat > 1e-2,
          f"C2={C2:.4f}, leak={leak1:.1e}, lin={lin:.1e}, smin(null)={s_null_flat:.1e}, "
          f"smin(off)={s_off_flat:.3e}")

    # C2: curved-point symbol at the Block B point: frame + characteristic variety.
    G = gimmel(Hs)
    Ginv = np.linalg.inv(G)
    wG, QG = np.linalg.eigh(G)
    order = np.argsort(-np.sign(wG))                            # 9 positive first, 5 negative
    wG, QG = wG[order], QG[:, order]
    E = QG / np.sqrt(np.abs(wG))                                # frame: E^T G E = eta
    frame_res = float(np.max(np.abs(E.T @ G @ E - np.diag(ETA))))
    offcone = []
    signs = set()
    tries = 0
    while len(offcone) < 4 and tries < 60:
        tries += 1
        xi_c = RNG.normal(size=N)                               # coordinate covector on Y14
        q = float(xi_c @ Ginv @ xi_c)
        if abs(q) < 0.3:
            continue
        if (q > 0 and (+1) not in signs) or (q < 0 and (-1) not in signs) or len(signs) == 2:
            xi_f = E.T @ xi_c                                   # frame components
            qf = float(np.sum(ETA * xi_f ** 2))
            offcone.append((q, qf, smin(xi_f)))
            signs.add(+1 if q > 0 else -1)
    ok_match = all(abs(q - qf) < 1e-8 * max(1, abs(q)) for q, qf, _ in offcone)
    ok_off = len(offcone) == 4 and all(s > 1e-2 for _, _, s in offcone) and len(signs) == 2
    # exact gimmel-null coordinate covector: null in the frame, mapped back
    xif_null = np.zeros(N)
    xif_null[0], xif_null[9] = 1.0, 1.0
    xic_null = G @ E @ (ETA * xif_null)                         # E^{-T} = G E eta
    q_null = float(xic_null @ Ginv @ xic_null)
    s_null = smin(E.T @ xic_null)
    check("C2. CURVED-POINT CHARACTERISTIC VARIETY = the gimmel null cone: at an actual "
          "curved-Y14 point, in a gimmel-orthonormal frame, G^{-1}(xi,xi) equals the frame "
          "eta-form exactly; off-cone covectors (both signs) are non-degenerate and an exact "
          "gimmel-null covector degenerates to machine precision. SA-C4's degree-1 principal "
          "symbol property holds POINTWISE ON CURVED Y14, not only in the flat model",
          frame_res < 1e-10 and ok_match and ok_off and abs(q_null) < 1e-10 and s_null < 1e-8,
          f"frame residual={frame_res:.1e}; " +
          "; ".join(f"q={q:+.2f} smin={s:.2e}" for q, _, s in offcone) +
          f"; null: q={q_null:.1e} smin={s_null:.1e}")

    # C3: so(9,5)-valued zeroth-order inserts (curvature terms, II_s blocks, connection choices).
    def rho_of(wmat):
        """rho(w) for w in so(9,5): w = sum c_ij J_ij with c_ij = w[i,j]/eta_j."""
        Sig = np.zeros((DIM, DIM), dtype=complex)
        for i in range(N):
            for j in range(i + 1, N):
                c = wmat[i, j] / ETA[j]
                if c != 0:
                    Sig = Sig + c * Sgen(i, j)
        return np.kron(wmat, I128) + np.kron(I14, Sig)

    # (a) generic so(9,5) element; (b) pure boost block (the II_s-shaped mixing directions)
    B_anti = RNG.normal(size=(N, N))
    B_anti = 0.5 * (B_anti - B_anti.T)
    w_gen = np.diag(ETA) @ B_anti                               # eta w antisym -> w in so(9,5)
    w_boost = np.zeros((N, N))
    w_boost[:9, 9:] = RNG.normal(size=(9, 5))
    w_boost[9:, :9] = w_boost[:9, 9:].T                         # eta w antisym for mixed block
    results = []
    for tag, wmat in (("generic", w_gen), ("boost/II-block", w_boost)):
        B0 = rho_of(wmat)
        commPi = float(np.linalg.norm(B0 @ Pi - Pi @ B0))
        leak = float(np.linalg.norm(Gamma @ B0 @ Pi))
        krein = float(np.linalg.norm(B0.conj().T @ K_krein + K_krein @ B0))
        L = 1.0e6
        sub = float(np.max(np.abs(
            (Kb.conj().T @ ((np.kron(I14, cxi(L * xi)) + B0) @ Kb)) / L - R(xi))))
        results.append((tag, commPi, leak, krein, sub))
    ok3 = all(c < 1e-8 and lk < 1e-8 and kr < 1e-7 and sb < 1e-4 for _, c, lk, kr, sb in results)
    check("C3a. so(9,5)-VALUED ZEROTH-ORDER INSERTS (curvature contractions rho(R), II_s "
          "blocks, connection-choice differences): commute with Pi, zero leakage, "
          "Krein-compatible, strictly subprincipal -- for a generic algebra element AND a pure "
          "boost/II-type block. Covariantization terms CANNOT reopen SA-C4 at symbol level: "
          "a structure theorem (algebra membership), not an estimate",
          ok3, "; ".join(f"{t}: [.,Pi]={c:.1e} leak={lk:.1e} Krein={kr:.1e} subpr={sb:.1e}"
                         for t, c, lk, kr, sb in results))

    # The named boundary: the W125-D dangerous insert has a SYMMETRIC vector factor.
    IIsym = _symN()
    memb = float(np.max(np.abs(np.diag(ETA) @ IIsym - (np.diag(ETA) @ IIsym).T)))
    check("C3b. THE PROTECTION BOUNDARY, named: the W125 Block-D failure mode "
          "(first-order insert kron(II_sym, c(xi))) has a SYMMETRIC vector factor, which is "
          "NOT in so(9,5) (eta.II_sym is not antisymmetric): metric-compatible "
          "covariantization can never generate it. If a future NON-metric coupling produces a "
          "symmetric first-order insert, SA-C4 reopens quantitatively with W125-D's window",
          memb > 1e-2, f"||eta II_sym - (eta II_sym)^T|| = {memb:.2f} != 0 (outside the algebra)")


def _symN():
    S = RNG.normal(size=(N, N))
    S = 0.5 * (S + S.T)
    return S / float(np.linalg.norm(S, 2))


def main():
    log("=" * 100)
    log("W131 / H68 -- THE COVARIANT OPERATOR ON Y14: build attempt (frame/symbol level)")
    log("=" * 100)

    e, Gamma, Pi, _ = gb.constraint_objects()
    Mvec, Sgen, K_krein, beta_S = block_A(e, Gamma, Pi)
    Hs = block_B()
    block_C(e, Gamma, Pi, Mvec, Sgen, K_krein, Hs)

    log("\n" + "=" * 100)
    log("SYNTHESIS -- the covariant operator on Y14")
    log("=" * 100)
    log("  D = Pi (gamma . nabla) Pi + m2 Pi on ker Gamma inside T*Y14 (x) S(9,5), nabla the")
    log("  gimmel Levi-Civita spin lift. BUILT at frame/symbol level with properties machine-")
    log("  checked: [nabla, Pi] = 0 (Gamma parallel: full 91-generator equivariance, boosts")
    log("  included), nabla K = 0 (Krein survives), covariant leakage 0, pointwise curved")
    log("  characteristic variety = the gimmel null cone, and ALL covariantization-generated")
    log("  zeroth-order inserts (curvature, II_s) provably subprincipal by algebra membership.")
    log("  The actual Y14 geometry supplies the hypotheses: signature (9,5) at Lorentzian")
    log("  points, O(9,5) holonomy, Gauss/II_s at native n = 4.")
    log("  NOT built: the analytic layer (Fredholm/propagator theory on NON-COMPACT Y14),")
    log("  all-orders well-posedness, SA-G9. Preconditions named: X4 spin (W2-01), gimmel")
    log("  nondegeneracy on the Lorentzian locus. The 4D Schur route and the repo VZ verdict")
    log("  are untouched.")
    if FAIL:
        log(f"SOME CHECKS FAILED: {FAIL}")
        return 1
    log("ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
