#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Anchor-council Wave A-1, item DQ2 — the (7,7) rerun of the trichotomy's two
legs (existence: eta-skew diagonal boost; classification: real commutant type).

PREREGISTERED (before this script was written) in
explorations/chirality-grading-and-77-rerun-2026-08-03.md §1.2, with seat 1's
two outcomes verbatim:
  (i)  larger candidate set => nonzero residual family => seat-1 H5 and the
       "at most one" holding are (9,5) artifacts;
  (ii) the O(p,q)-type Krein structure forces the sign (9,5) leaves open =>
       register M-H4's conjecture lands.
plus the registered possibility that the result lands in NEITHER shape.

METHOD: re-parameterisation of the corrected M-C3 probe
(tests/observable-algebra/commutant_trichotomy_probe.py, hostile review
2026-08-03 corrections 1-12 applied there) to signature (7,7); the graph
certificate, compression construction, and witness machinery are reused with
attribution. Differences forced by the real form Cl(7,7) = M(128,R):
  - the commuting antiunitary J now has J^2 = +1 (real class; firewall Round
    2, tests/generation-sector/signature_77_rerun.py) — antilinear candidates
    c J have (cJ)^2 = +|c|^2 and are legitimate involutions for |c| = 1;
  - the spinor Krein symmetry must be beta = i * e_0..e_6 (p = 7 == 3 mod 4;
    unique up to a REAL scalar because the spinor-factor commutant is C.I),
    and the factor i makes J ANTI-commute with beta — so whether eta_V is
    J-real (an O(p,q) form on the real points, M-H4's route) or J-skew (an
    Sp form, no sign to force) is decided by computation below.

TYPE DISCLOSURE (inherited from the reviewed probe, unchanged): A is the
COMPRESSION algebra of GU-native blocks on the KINEMATIC record sector — NOT a
Dirac (constraint-preserving) observable algebra (census below: 1/44
generators preserves ker Gamma); by Burnside it is the FULL matrix algebra for
this generating choice, so the trichotomy branch is chosen, not discovered;
the constraint-preserving covariant choice lands on the REDUCIBLE branch
(contrast run below).

MANDATORY FENCES (verbatim):
  (1) kinematic carrier only; whether any physical observable algebra survives
      on it is exactly the open dynamical-stabilizer question (W219); nothing
      transports to the interacting theory (rankN, Pi_kappa regime);
  (2) no verdict, bar(b), H59, or claim-status change is made by this script —
      results are pre-deposit; J5 (hostile field-specialist review, two-sided
      charge) gates any bar move;
  (3) irreducible + compact => "sign forced IF this is the observable algebra"
      (this run: irreducible but NON-compact — no sign is forced);
      reducible => report the residual-family data.

Run:
  PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python -u \
      tests/observable-algebra/dq2_trichotomy_77_rerun.py
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
if _TESTS not in sys.path:
    sys.path.insert(0, _TESTS)

import oq_rk1_cl95_explicit_rep as cl95  # noqa: E402  (verified JW gammas)

N, DIM = 14, 128
NV = (N - 1) * DIM                          # 1664
ETA = np.array([1.0] * 7 + [-1.0] * 7)      # the (7,7) signature
XI = np.array([1.0, 2.0, 3.0, 4.0, 0.5, 1.5, 2.5, 0.7,
               1.1, 0.3, 2.2, 1.7, 0.9, 1.3], dtype=complex)  # fixtures' vector

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


def graph_commutant(Ks, n, seed, taus=(1e-4, 1e-6, 1e-8), real=False,
                    aug_words=0):
    """dim of the commutant of the adjoint/transpose-closed family Ks on
    C^n (real=False) or R^n (real=True). Same certificate as the reviewed
    (9,5) probe: generic (Hermitian|symmetric) element with simple spectrum
    forces commutant elements diagonal in its eigenbasis; each K then forces
    equality of diagonal entries across genuinely nonzero entries; connected
    components of that graph = commutant dimension.

    aug_words > 0 augments the family with that many random SECOND-ORDER
    words K_a K_b (legitimate: any commutant element commutes with algebra
    words). Needed over R: the real symmetric span of the bare generators is
    only the ~22 Hermitian directions (the i(K - K^dag) Hermitian directions
    available over C do not restrict to real operators), and that thin span
    is exactly degenerate (verified: a Clifford-vector combination has
    multiplicities 768/768/64/64 on V^J), so genericity needs words."""
    rng = np.random.default_rng(seed)
    if aug_words > 0:
        Ks = list(Ks)
        idx = rng.integers(0, len(Ks), size=(aug_words, 2))
        Ks += [Ks[a] @ Ks[b] for a, b in idx]
    if real:
        H1 = np.zeros((n, n))
        for K in Ks:
            H1 += rng.standard_normal() * K
        H1 = H1 + H1.T
    else:
        H1 = np.zeros((n, n), dtype=complex)
        for K in Ks:
            c = rng.standard_normal() + 1j * rng.standard_normal()
            H1 += c * K
        H1 = H1 + H1.conj().T
    w, W = np.linalg.eigh(H1)
    mingap = float(np.diff(w).min())
    spread = float(w[-1] - w[0])
    Wc = W.T if real else W.conj().T
    adj = {t: np.zeros((n, n), dtype=bool) for t in taus}
    for K in Ks:
        T = Wc @ (K @ W)
        A = np.abs(T)
        np.fill_diagonal(A, 0.0)
        m = float(A.max())
        if m < 1e-9 * (1.0 + fnorm(K)):
            continue
        rel = A / m
        for t in taus:
            adj[t] |= rel > t
    ncomp = {}
    for t in taus:
        nc, _ = connected_components(sp.csr_matrix(adj[t]), directed=False)
        ncomp[t] = int(nc)
    return mingap, spread, ncomp


def expv(Dm, v, kmax=120, tol=1e-17):
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
    print(f"[env] numpy {np.__version__}, n_amb = {N * DIM}, n_V = {NV} = 13*128",
          flush=True)

    # ------------------------------------------------------------ [0] fixtures
    print("== [0] (7,7) fixtures & anchors ==", flush=True)
    G = cl95.jordan_wigner_gammas(7)
    e = [G[a] if ETA[a] > 0 else 1j * G[a] for a in range(N)]
    Id = np.eye(DIM, dtype=complex)
    cerr = max(
        float(np.max(np.abs(e[a] @ e[b] + e[b] @ e[a]
                            - (2.0 * ETA[a] if a == b else 0.0) * Id)))
        for a in range(N) for b in range(N))
    check("(7,7) Clifford relations {e_a,e_b} = 2 eta_ab", cerr < 1e-9,
          f"max err {cerr:.2e}")
    Gamma = np.hstack(e)
    Pi = np.eye(N * DIM, dtype=complex) \
        - Gamma.conj().T @ np.linalg.inv(Gamma @ Gamma.conj().T) @ Gamma
    cxi = sum(XI[a] * e[a] for a in range(N))
    M_D = np.kron(np.eye(N, dtype=complex), cxi)
    bare = fnorm(Pi @ M_D - M_D @ Pi)
    c2 = fnorm(Gamma @ M_D @ Pi)
    check("anchor: bare ||[Pi_RS, M_D]|| = 58.7215 (signature-identical)",
          abs(bare - 58.7215) < 1e-2, f"{bare:.4f}")
    check("anchor: C2 = 155.3625 (signature-identical)",
          abs(c2 - 155.3625) < 1e-2, f"{c2:.4f}")
    check("trace Pi = 1664 = 13*128",
          abs(float(np.trace(Pi).real) - NV) < 1e-6)

    # ----------------------------------- [1] real structure J with J^2 = +1
    print("== [1] real structure: commuting antiunitary J, J^2 = +1 ==", flush=True)

    def Phi(U):
        out = np.zeros_like(U)
        for a in range(N):
            out += ETA[a] * (e[a] @ U @ e[a].conj())
        return out / N

    rng = np.random.default_rng(1)
    U = rng.standard_normal((DIM, DIM)) + 1j * rng.standard_normal((DIM, DIM))
    for _ in range(400):
        U = 0.5 * (U + Phi(U))
        U /= np.linalg.norm(U)
    Us, _, Vs = np.linalg.svd(U)
    U = Us @ Vs
    check("U unitary", fnorm(U @ U.conj().T - Id) < 1e-8)
    check("J^2 = +1 on the spinor factor (U Ubar = +I; REAL class, no Kramers)",
          fnorm(U @ U.conj() - Id) < 1e-7, f"residual {fnorm(U @ U.conj() - Id):.2e}")

    def jlin128(x):  # J-linearity defect: ||U xbar U^dag - x||
        return fnorm(U @ x.conj() @ U.conj().T - x)

    jl = max(jlin128(e[a]) for a in range(N))
    check("J commutes with all 14 Clifford generators", jl < 1e-7,
          f"max defect {jl:.2e}")
    Jf = np.kron(np.eye(N), U)

    # ------------------------- [2] the forced (7,7) Krein symmetry beta
    print("== [2] beta = i e0..e6: the forced (7,7) spinor Krein symmetry ==",
          flush=True)
    w7 = word(e, tuple(range(7)))
    check("real word (e0..e6)^2 = -I (p = 7 == 3 mod 4: i factor REQUIRED)",
          fnorm(w7 @ w7 + Id) < 1e-8)
    beta = 1j * w7
    check("beta Hermitian", fnorm(beta - beta.conj().T) < 1e-9)
    check("beta^2 = +I", fnorm(beta @ beta - Id) < 1e-9)
    ib_err = max(fnorm(beta @ e[a] @ beta - e[a].conj().T) for a in range(N))
    check("beta e_a beta^-1 = e_a^dag (Krein self-adjointness of the gammas)",
          ib_err < 1e-8, f"max err {ib_err:.2e}")
    evb = np.linalg.eigvalsh(beta)
    sig_beta = (int((evb > 0.5).sum()), int((evb < -0.5).sum()))
    check("signature(beta) = (64, 64)", sig_beta == (64, 64), str(sig_beta))
    # uniqueness: spinor-factor commutant is C.I => beta unique up to REAL scalar
    PAIRS = [(0, 1), (1, 2), (2, 3), (4, 5), (6, 7), (7, 8),
             (0, 9), (4, 10), (8, 13), (9, 10), (10, 11), (12, 13)]
    WORDS = [("e0e1e2", (0, 1, 2)), ("e3e4e5e6", (3, 4, 5, 6)),
             ("e9e10e11", (9, 10, 11)), ("w7=e0..e6", tuple(range(7))),
             ("omega=e0..e13", tuple(range(14)))]
    Ks128 = [e[a] for a in range(N)] + [sigma128(e, i, j) for (i, j) in PAIRS] \
        + [word(e, idx) for _, idx in WORDS] + [cxi]
    mg128, sp128, nc128 = graph_commutant(Ks128, DIM, seed=303)
    check("spinor factor: commutant of Cl(7,7) on C^128 is C.I "
          "(=> beta unique up to real scalar; J-anticommutation is FORCED)",
          mg128 > 1e-10 * sp128 and set(nc128.values()) == {1}, str(nc128))
    sk_err = max(fnorm((beta @ sigma128(e, i, j)) + (beta @ sigma128(e, i, j)).conj().T)
                 for (i, j) in PAIRS)
    check("spin generators beta-skew (Spin(7,7) in U(beta))", sk_err < 1e-8,
          f"{sk_err:.2e}")
    anti = fnorm(U @ beta.conj() @ U.conj().T + beta)
    check("STRUCTURAL: J ANTI-commutes with beta (U betabar U^dag = -beta)",
          anti < 1e-7, f"residual {anti:.2e}")

    # --------------------------------------------- [3] record sector V, J on V
    print("== [3] record sector V = ker Gamma; J restricted, J^2 = +1 on V ==",
          flush=True)
    _, s_, vh = np.linalg.svd(Gamma)
    check("Gamma has full row rank 128", s_[-1] > 1e-6, f"s_min = {s_[-1]:.3e}")
    B = vh[DIM:].conj().T
    Bc = B.conj().T
    check("dim_C ker Gamma = 1664", B.shape == (N * DIM, NV))
    check("B orthonormal", fnorm(Bc @ B - np.eye(NV)) < 1e-9)
    JB = Jf @ B.conj()
    check("J preserves the record sector", fnorm(JB - Pi @ JB) < 1e-7,
          f"residual {fnorm(JB - Pi @ JB):.2e}")
    UV = Bc @ JB
    UVc = UV.conj().T
    check("U_V unitary", fnorm(UV @ UVc - np.eye(NV)) < 1e-7)
    check("J^2 = +1 on V (U_V conj(U_V) = +I)",
          fnorm(UV @ UV.conj() - np.eye(NV)) < 1e-6,
          f"residual {fnorm(UV @ UV.conj() - np.eye(NV)):.2e}")

    def hlV(K):  # J-linearity defect on V
        return fnorm(UV @ K.conj() @ UVc - K)

    def compress_spinor(x):
        y = np.tensordot(x, B.reshape(N, DIM, NV), axes=([1], [1]))
        y = np.ascontiguousarray(y.transpose(1, 0, 2)).reshape(N * DIM, NV)
        return Bc @ y

    def compress_vector(M):
        y = (M.astype(complex) @ B.reshape(N, DIM * NV)).reshape(N * DIM, NV)
        return Bc @ y

    # ------------------------------------- [4] compressed generator family (44)
    print("== [4] compressed generators, adjoint closure, census ==", flush=True)
    gens = []
    adj_sign = {}
    for a in range(N):
        nm = f"cl:e{a}"
        gens.append((nm, compress_spinor(e[a])))
        adj_sign[nm] = +1 if ETA[a] > 0 else -1
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
    gens.append(("M_D", compress_spinor(cxi)))
    check("generator family has 44 compressed elements", len(gens) == 44,
          str(len(gens)))
    worst_adj = 0.0
    for nm, K in gens:
        if nm in adj_sign:
            r = fnorm(K.conj().T - adj_sign[nm] * K)
        elif nm == "M_D":
            r = fnorm(K.conj().T - compress_spinor(cxi.conj().T))
        else:
            r = min(fnorm(K.conj().T - K), fnorm(K.conj().T + K))
        worst_adj = max(worst_adj, r / (1.0 + fnorm(K)))
    check("generator family adjoint-closed", worst_adj < 1e-8,
          f"max rel residual {worst_adj:.2e}")
    gd = dict(gens)
    subset = ["cl:e0", "cl:e12", "clw:w7=e0..e6", "clw:omega=e0..e13",
              "sigma:0,1", "sigma:0,9", "sigma:12,13", "frame:0,1", "frame:0,9",
              "M_D"]
    hl_v = max(hlV(gd[nm]) / (1.0 + fnorm(gd[nm])) for nm in subset)
    check("compressed generators commute with J on V (class-covering subset)",
          hl_v < 1e-6, f"max rel defect {hl_v:.2e}")

    # census: 1/44 ambient counterparts preserve ker Gamma (type disclosure)
    def amb_spinor(x):
        y = np.tensordot(x, B.reshape(N, DIM, NV), axes=([1], [1]))
        return np.ascontiguousarray(y.transpose(1, 0, 2)).reshape(N * DIM, NV)

    def amb_vector(M):
        return (M.astype(complex) @ B.reshape(N, DIM * NV)).reshape(N * DIM, NV)

    amb_cols = [(f"cl:e{a}", amb_spinor(e[a])) for a in range(N)]
    amb_cols += [(f"clw:{nm_w}", amb_spinor(word(e, idx))) for nm_w, idx in WORDS]
    amb_cols += [(f"sigma:{i},{j}", amb_spinor(sigma128(e, i, j))) for (i, j) in PAIRS]
    amb_cols += [(f"frame:{i},{j}", amb_vector(Mvec14(i, j))) for (i, j) in PAIRS]
    amb_cols.append(("M_D", amb_spinor(cxi)))
    nG = fnorm(Gamma)
    rels = {nm: fnorm(Gamma @ XB) / (nG * fnorm(XB)) for nm, XB in amb_cols}
    ordered = sorted(rels.items(), key=lambda kv: kv[1])
    preserving = [nm for nm, r in ordered if r < 1e-6]
    check("census: exactly 1/44 generators preserves ker Gamma (omega) — "
          "A is a COMPRESSION algebra under (7,7) too",
          preserving == ["clw:omega=e0..e13"], f"preserving = {preserving}")
    check("census margin: every other generator violates the constraint",
          ordered[1][1] > 1e-3, f"second-smallest {ordered[1][1]:.2e} ({ordered[1][0]})")

    # covariant contrast: constraint-preserving diagonal Spin(7,7) is REDUCIBLE
    pairs_all = [(i, j) for i in range(N) for j in range(i + 1, N)]
    omega128 = word(e, tuple(range(N)))
    worst_inv = 0.0
    for (i, j) in pairs_all:
        DBij = amb_vector(Mvec14(i, j)) + amb_spinor(sigma128(e, i, j))
        worst_inv = max(worst_inv, fnorm(Gamma @ DBij) / (nG * (1.0 + fnorm(DBij))))
    check("contrast: ALL 91 diagonal Spin(7,7) generators preserve ker Gamma",
          worst_inv < 1e-7, f"max rel residual {worst_inv:.2e}")
    omV = gd["clw:omega=e0..e13"]
    dist_scalar = fnorm(omV - (complex(np.trace(omV)) / NV) * np.eye(NV))
    check("contrast: omega_V is NOT a scalar => covariant (Dirac-sense) choice "
          "lands on the REDUCIBLE branch under (7,7) too", dist_scalar > 1.0,
          f"{dist_scalar:.3f}")

    # ------------------------- [5] CLASSIFICATION leg: complex graph commutant
    print("== [5] classification leg: commutant of A on V ==", flush=True)
    t5 = time.time()
    Klist = [K for _, K in gens]
    mg1, spread1, nc1 = graph_commutant(Klist, NV, seed=101)
    check("H1 has simple spectrum (seed 101)", mg1 > 1e-10 * spread1,
          f"min gap {mg1:.3e}")
    check("component count stable across thresholds (seed 101)",
          len(set(nc1.values())) == 1, str(nc1))
    rng2 = np.random.default_rng(555)
    sub_idx = rng2.choice(len(Klist), size=22, replace=False)
    mg2, spread2, nc2 = graph_commutant([Klist[i] for i in sub_idx], NV, seed=202)
    check("H1 has simple spectrum (seed 202, independent 22-generator subfamily)",
          mg2 > 1e-10 * spread2, f"min gap {mg2:.3e}")
    check("component count stable across thresholds (seed 202)",
          len(set(nc2.values())) == 1, str(nc2))
    check("independent replication: same commutant dimension",
          nc1[1e-6] == nc2[1e-6], f"{nc1[1e-6]} vs {nc2[1e-6]}")
    dimC = nc1[1e-6]
    print(f"  ==> dim_C commutant = {dimC}  [{time.time() - t5:.0f}s]", flush=True)

    # --------------- [6] real commutant TYPE: split quaternions, R.I on V^J
    print("== [6] real commutant type: M(2,R) (split), R.I on the real form ==",
          flush=True)
    t6 = time.time()
    # (a) the four-dimensional real commutant span{I, iI, J, iJ} with J^2 = +1
    rngv = np.random.default_rng(9)
    v = rngv.standard_normal(NV) + 1j * rngv.standard_normal(NV)
    v /= fnorm(v)

    def Jact(x):
        return UV @ x.conj()

    check("J^2 = +1 on samples", fnorm(Jact(Jact(v)) - v) < 1e-7)
    check("(iJ)^2 = +1 (LEGITIMATE antilinear involution, unlike (9,5))",
          fnorm(1j * Jact(1j * Jact(v)) - v) < 1e-7)
    check("J and iJ anticommute (split-quaternion relations, NOT H)",
          fnorm(Jact(1j * Jact(v)) + 1j * Jact(Jact(v))) < 1e-7)
    Pj = 0.5 * (v + Jact(v))
    check("(1+J)/2 is a real-linear idempotent: real commutant has PROPER "
          "idempotents => NOT a division algebra => Kramers wall ABSENT",
          fnorm(0.5 * (Pj + Jact(Pj)) - Pj) < 1e-7)
    ncl = fnorm(0.5 * (1j * v + Jact(1j * v)) - 1j * Pj)
    check("(1+J)/2 is NOT complex-linear (it is a real-form projection)",
          ncl > 0.1, f"defect {ncl:.3f}")

    # (b) real form V^J: orthonormal real basis from the involutive symmetric
    #     orthogonal T = [[Re UV, Im UV], [Im UV, -Re UV]] (fixed space of J)
    Tr = np.block([[UV.real, UV.imag], [UV.imag, -UV.real]])
    check("T symmetric (J antiunitary involution)", fnorm(Tr - Tr.T) < 1e-6)
    check("T^2 = I", fnorm(Tr @ Tr - np.eye(2 * NV)) < 1e-6)
    wT, QT = np.linalg.eigh(Tr)
    n_minus_T = int((wT < 0).sum())
    check("T has eigenvalues -1/+1 with multiplicity 1664/1664 "
          "(dim_R V^J = 1664)", n_minus_T == NV and (2 * NV - n_minus_T) == NV,
          f"n(-1) = {n_minus_T}")
    Qfix = QT[:, NV:]                      # eigenvalue +1 block
    Qc = Qfix[:NV, :] + 1j * Qfix[NV:, :]  # complex vectors, J-fixed
    check("real basis is J-fixed (U_V conj(Q) = Q)",
          fnorm(UV @ Qc.conj() - Qc) < 1e-6)
    check("real basis is complex-orthonormal",
          fnorm(Qc.conj().T @ Qc - np.eye(NV)) < 1e-6)
    # restrict all 44 generators to V^J (real matrices)
    Ks_real = []
    worst_im, worst_res = 0.0, 0.0
    Qcc = Qc.conj().T
    for nm, K in gens:
        Kq = Qcc @ (K @ Qc)
        worst_im = max(worst_im, fnorm(Kq.imag) / (1.0 + fnorm(Kq)))
        Kr = Kq.real
        worst_res = max(worst_res,
                        fnorm(K @ Qc - Qc @ Kr) / (1.0 + fnorm(K)))
        Ks_real.append(Kr)
    check("all 44 generators restrict to REAL operators on V^J",
          worst_im < 1e-6, f"max rel imag {worst_im:.2e}")
    check("V^J is invariant under the algebra (restriction residual)",
          worst_res < 1e-6, f"max rel residual {worst_res:.2e}")
    mgr, spreadr, ncr = graph_commutant(Ks_real, NV, seed=404, real=True,
                                        aug_words=60)
    check("real generic element (generators + 60 second-order words) has "
          "simple spectrum", mgr > 1e-10 * spreadr, f"min gap {mgr:.3e}")
    check("REAL commutant on the real form V^J is R.I (dim_R = 1)",
          set(ncr.values()) == {1}, str(ncr))
    print(f"  ==> real commutant on V^J: R.I; complex commutant C.I; real "
          f"commutant of the complex carrier: split quaternions ~ M(2,R)  "
          f"[{time.time() - t6:.0f}s]", flush=True)

    # -------- [7] candidate sets: linear {+-I}; raw antilinear phase orbit
    print("== [7] involution candidate sets ==", flush=True)
    for c, nmc in ((1.0, "J"), (1j, "iJ"), ((1 + 1j) / np.sqrt(2.0), "e^{i pi/4} J")):
        check(f"(cJ)^2 = +1 for c = {nmc} (raw phase orbit of antilinear "
              f"involutions EXISTS)",
              fnorm(c * Jact(c * Jact(v)) - v) < 1e-7)
    print("  linear commuting involutions: commutant C.I => {cI : c^2 = 1} = "
          "{+I, -I} (UNCHANGED from (9,5))", flush=True)
    print("  antilinear commuting involutions: {c J : |c| = 1} — a raw phase orbit,")
    print("  not a residual modulus (scalar-phase conjugation is transitive),")
    print("  EMPTY under (9,5) ((cJ)^2 = -|c|^2 there). The enlargement is real")
    print("  and confined to the ANTILINEAR sector.", flush=True)

    # ---------------- [8] Krein form on V: signature; J-reality vs J-skewness
    print("== [8] Krein form eta_14 (x) beta on V: signature and J-type ==",
          flush=True)
    tmpb = np.tensordot(beta, B.reshape(N, DIM, NV), axes=([1], [1]))
    tmpb = np.ascontiguousarray(tmpb.transpose(1, 0, 2))
    tmpb *= ETA[:, None, None]
    BV = Bc @ tmpb.reshape(N * DIM, NV)
    check("eta_V Hermitian", fnorm(BV - BV.conj().T) < 1e-8)
    evV = np.linalg.eigvalsh(0.5 * (BV + BV.conj().T))
    tolV = 1e-8 * float(np.abs(evV).max())
    pV = int((evV > tolV).sum())
    qV = int((evV < -tolV).sum())
    check("eta_V nondegenerate on V", float(np.abs(evV).min()) > 1e-8,
          f"min |eig| = {float(np.abs(evV).min()):.3e}")
    check("signature(eta_V) = (832, 832) under (7,7) as well",
          (pV, qV) == (832, 832), f"({pV},{qV})")
    ac = fnorm(omega128 @ beta + beta @ omega128)
    check("structural: omega beta + beta omega = 0 under (7,7)", ac < 1e-8,
          f"{ac:.2e}")
    sq = omV @ omV
    c_sq = complex(np.trace(sq)) / NV
    check("omega_V^2 = +I", fnorm(sq - c_sq * np.eye(NV)) < 1e-6
          and abs(c_sq - 1.0) < 1e-6, f"c = {c_sq:.6f}")
    Pp = 0.5 * (np.eye(NV) + omV)
    Pm = 0.5 * (np.eye(NV) - omV)
    iso = max(fnorm(Pp.conj().T @ BV @ Pp), fnorm(Pm.conj().T @ BV @ Pm)) / fnorm(BV)
    check("both omega-halves totally isotropic => (832,832) FORCED", iso < 1e-7,
          f"max rel norm {iso:.2e}")
    # J-type of the form: eta(Jx, Jy) = conj(x^T Abar y) with A = UV^dag BV UV
    Amat = np.conj(UVc @ BV @ UV)
    r_real = fnorm(Amat - BV) / fnorm(BV)
    r_skew = fnorm(Amat + BV) / fnorm(BV)
    print(f"  J-reality residual {r_real:.3e}  vs  J-SKEWNESS residual "
          f"{r_skew:.3e}", flush=True)
    check("eta_V is J-SKEW (eta(Jx,Jy) = -conj(eta(x,y))): forced by "
          "J beta = -beta J", r_skew < 1e-6 and r_real > 0.5,
          f"skew {r_skew:.2e}, real {r_real:.2e}")
    Gform = Qcc @ (BV @ Qc)
    rel_re = fnorm(Gform.real) / fnorm(Gform)
    Sform = Gform.imag
    check("restricted pairing on the real points V^J is PURELY IMAGINARY",
          rel_re < 1e-6, f"rel Re {rel_re:.2e}")
    check("Im-part is SKEW-symmetric: V^J carries an Sp(1664,R)-type "
          "form, NOT an O(p,q) form on that fixed real form",
          fnorm(Sform + Sform.T) / (1.0 + fnorm(Sform)) < 1e-6)
    sv = np.linalg.svd(Sform, compute_uv=False)
    check("the symplectic form is nondegenerate", sv[-1] > 1e-6 * sv[0],
          f"s_min/s_max = {sv[-1] / sv[0]:.3e}")
    print("  => the canonical J-fixed M-H4 sign route closes: there is no")
    print("     O(p,q) restriction on V^J whose signature could force a sign.")
    print("     The realification still carries Re(eta_V); the actual stabilizer")
    print("     commutant and global signature fork remain open.", flush=True)

    # -------------------- [9] EXISTENCE leg: eta_V-skew boost, numerical spectrum
    print("== [9] existence leg: unbounded eta_V-skew boost inside A ==",
          flush=True)
    t9 = time.time()
    I128c = np.eye(DIM, dtype=complex)
    rates = {}
    DVs = {}
    for nm, (i, j) in [("boost(0,9)", (0, 9)), ("rotation(0,1)", (0, 1))]:
        Damb = np.kron(Mvec14(i, j).astype(complex), I128c) \
            + np.kron(np.eye(N, dtype=complex), sigma128(e, i, j))
        DB = Damb @ B
        check(f"diagonal {nm} preserves V", fnorm(DB - Pi @ DB) < 1e-7)
        DV = Bc @ DB
        DVs[nm] = DV
        SkV = BV @ DV
        check(f"{nm} is eta_V-skew (subgroup lies in U(eta_V), or O(Re eta_V) after realification)",
              fnorm(SkV + SkV.conj().T) / (1.0 + fnorm(SkV)) < 1e-7)
        rv = np.random.default_rng(17)
        vv = rv.standard_normal(NV) + 1j * rv.standard_normal(NV)
        vv /= fnorm(vv)
        incs = []
        for _step in range(40):
            vv = expv(DV, vv)
            nrm = fnorm(vv)
            incs.append(np.log(nrm))
            vv /= nrm
        rates[nm] = float(np.mean(incs[-10:]))
        print(f"  {nm}: log-growth rate ~ {rates[nm]:+.6f} per unit t", flush=True)
    K_D_alg = gd["frame:0,9"] + gd["sigma:0,9"]
    check("the boost direction is IN the constructed algebra",
          fnorm(DVs["boost(0,9)"] - K_D_alg) < 1e-8)
    check("boost flow unbounded on V (non-compactness WITNESS)",
          rates["boost(0,9)"] > 1.0, f"rate {rates['boost(0,9)']:.4f}")
    check("rotation flow bounded on V (compact contrast)",
          abs(rates["rotation(0,1)"]) < 1e-8, f"rate {rates['rotation(0,1)']:.2e}")
    evD = np.linalg.eigvals(DVs["boost(0,9)"])
    check("boost spectrum is real on V", float(np.abs(evD.imag).max()) < 1e-5,
          f"max |Im| = {float(np.abs(evD.imag).max()):.2e}")
    re_r = np.round(evD.real * 2.0) / 2.0
    vals = sorted(set(re_r.tolist()))
    mult = {vl: int((np.abs(evD.real - vl) < 1e-4).sum()) for vl in vals}
    check("numerical boost spectrum on V matches Re spec(D) = {-3/2, -1/2, +1/2, +3/2} "
          "(vector weight 1 + spinor weight 1/2)",
          vals == [-1.5, -0.5, 0.5, 1.5]
          and float(np.max(np.abs(evD.real - re_r))) < 1e-5, f"multiplicities {mult}")
    check("boost spectrum symmetric (eta_V-skew)",
          mult[-1.5] == mult[1.5] and mult[-0.5] == mult[0.5], str(mult))
    print(f"  [{time.time() - t9:.0f}s]", flush=True)

    # ----------------------------------------------------------- [10] verdict
    print("=" * 78)
    print("VERDICT — DQ2: the (7,7) rerun of the trichotomy's two legs")
    print("=" * 78)
    print(f"  CLASSIFICATION leg: dim_C commutant = {dimC}; real commutant of the")
    print("  complex carrier = span_R{I, iI, J, iJ} with J^2 = +1 = the SPLIT")
    print("  quaternions ~ M(2,R) (proper idempotents; NOT the division algebra H).")
    print("  On the real form V^J (dim_R 1664): real commutant R.I, R-irreducible.")
    print("  => the quaternionic Kramers wall is ABSENT at algebra level under")
    print("     (7,7): seat-1 H5 is (9,5)-ONLY, exactly as fenced. BUT the linear")
    print("     candidate set is UNCHANGED: {cI : c^2 = 1} = {+-I}, so the")
    print("     'at most one admissible fundamental symmetry' holding TRANSFERS")
    print("     (it rests on commutant triviality, not on the wall). The")
    print("     enlargement is real and confined to the ANTILINEAR sector:")
    print("     {cJ : |c| = 1}, a raw phase orbit empty under (9,5).")
    print("  EXISTENCE leg: the eta_V-skew diagonal boost lies in A with numerical")
    print(f"  Re spec {{-3/2,-1/2,+1/2,+3/2}} and witnessed growth rate "
          f"{rates['boost(0,9)']:+.3f};")
    print("  by Prop 1's necessity leg (no property of eta used), F = EMPTY for")
    print("  EVERY nondegenerate form and every invariance structure containing")
    print("  that direction. F = empty is SIGNATURE-ROBUST.")
    print("  M-H4 canonical J-fixed sign route: CLOSED at kinematic scope. beta")
    print("  is i*e0..e6 up to real scalar, eta_V is J-SKEW, and V^J is")
    print("  symplectic. The actual stabilizer row and global signature selection")
    print("  remain OPEN.")
    print("  PREREGISTRATION readout: neither (i) nor (ii) lands as stated —")
    print("  (i) fails for the LINEAR family (still {+-I}, residual family 0);")
    print("  (i) holds for the ANTILINEAR raw phase orbit only;")
    print("  (ii) dies on the canonical J-fixed route (Sp-type, not O-type).")
    print("  The actual stabilizer/global signature question remains open. H5 was fenced")
    print("  (9,5)-only and stays; the (9,5) F = empty is NOT an artifact.")
    print("-" * 78)
    print("MANDATORY FENCES (verbatim):")
    print("  (1) kinematic carrier only; the physical observable algebra is the")
    print("      open dynamical-stabilizer question (W219); nothing transports")
    print("      to the interacting theory (rankN, Pi_kappa regime);")
    print("  (2) no verdict, bar(b), H59, or claim-status change — pre-deposit;")
    print("      J5 gates any bar move;")
    print("  (3) irreducible + compact => sign forced IF observable algebra;")
    print("      this run: irreducible but NON-compact — no sign forced.")
    print("-" * 78)

    # REGRESSION PINS (observed on the 2026-08-03 run; pins of the computed
    # result, not assumptions — remove only with a recorded re-derivation)
    assert dimC == 1, "regression pin: complex commutant was C.I on 2026-08-03"
    assert set(ncr.values()) == {1}, \
        "regression pin: real commutant on V^J was R.I on 2026-08-03"
    assert (pV, qV) == (832, 832), "regression pin: signature(eta_V) was (832,832)"
    assert rates["boost(0,9)"] > 1.0, "regression pin: boost growth rate was ~1.5"
    assert r_skew < 1e-6 < r_real, \
        "regression pin: eta_V was J-SKEW (Sp-type real form) on 2026-08-03"

    print(f"[summary] {_n_checks[0]} checks passed; elapsed "
          f"{time.time() - t0:.0f}s; exit 0", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
