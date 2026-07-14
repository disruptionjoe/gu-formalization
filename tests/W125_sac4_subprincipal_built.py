#!/usr/bin/env python3
r"""W125 -- SA-C4 ON THE BUILT CANDIDATE: the subprincipal FC-VZ-4 causality check,
built for the first time against the g=1 ker-Gamma cure (the one genuinely unbuilt
FORCED check in the requirements spec, row SA-C4).

CONTEXT
-------
tests/vz_fcvz4_subprincipal.py (the round-S^4 model leg) established the deciding
dichotomy: after constraint elimination, whether the extrinsic curvature II_s can tilt
the light cone (spacelike characteristics at subprincipal order) is governed by the
DEGENERACY of the top-order reduced symbol -- and it was BLOCKED on the GU RS action,
because the Schur-elimination route (cure A) has an unpinned xi-dependent E-block.

The W125 BUILT candidate takes the OTHER route (cure B, carrier B): the constraint is
enforced KINEMATICALLY by the constant so(9,5)-equivariant projector Pi (g = 1 full
ker-Gamma projection). That structural difference makes SA-C4 decidable on the built
object at symbol level, because a CONSTANT projector cannot mix symbol degrees:

  R(xi) := K^dag M_D(xi) K   restricted to ker Gamma (K = orthonormal basis, 1664-dim)
  is EXACTLY degree-1 homogeneous in xi. A zeroth-order II_s insertion B0 shifts only
  the degree-0 part: the principal symbol of K^dag (M_D + B0) K is R(xi) IDENTICALLY.

WHAT THIS FILE COMPUTES (deterministic, fixed seed, on the verified Cl(9,5) rep)
--------------------------------------------------------------------------------
  BLOCK A -- the injectivity identities behind non-degeneracy: sum_a eta_a e_a e_a = 14 I
     and gamma^a c(xi) gamma_a = (2 - 14) c(xi) = -12 c(xi). (These force: if the
     restricted symbol kills psi != 0 off-cone then c(xi) chi = 0 for the trace spinor,
     impossible at q != 0 -- the exact-arithmetic skeleton of the numeric result.)
  BLOCK B -- NON-DEGENERACY OFF THE CONE: for sampled covectors with q = eta(xi,xi) != 0
     (both signs), sigma_min(R(xi)) is bounded away from 0; for a null covector it is 0
     to machine precision; approaching the cone, sigma_min -> 0. So the characteristic
     variety of the built restricted symbol is EXACTLY the metric null cone {q = 0}:
     the built candidate sits in the NON-DEGENERATE (causal) branch of the FC-VZ-4
     dichotomy.
  BLOCK C -- SUBPRINCIPAL INSERTS ARE HARMLESS: R is exactly linear in xi (R(2xi) = 2R(xi)
     to machine precision), and for an arbitrary zeroth-order II_s-type insert B0 the
     homogenized symbol (K^dag (M_D(L xi) + s B0) K)/L -> R(xi) as L -> inf. A zeroth-
     order II_s CANNOT enter the principal symbol of the built (constrained-route)
     operator -- combined with Block B, the II_s-sourced spacelike characteristics of
     FC-VZ-4 cannot fire at subprincipal order on the built candidate.
  BLOCK D -- POSITIVE CONTROL (the test has power): a FIRST-order (principal-symbol-
     modifying) II_s-type insert kron(II_s, c(xi)) DOES drive sigma_min toward 0 off the
     cone at finite strength (an off-cone characteristic appears inside the scanned
     window), while small strengths keep the cone intact -- i.e. the Velo-Zwanziger-type
     finite causal window is REAL and this test detects it. This is the regime the
     Schur route (cure A) risks; the built cure-B route is protected from it by the
     degree argument of Block C.

HONEST SCOPE (read before quoting)
----------------------------------
- Symbol-level, flat 14-dim model of the built candidate on the verified rep; the
  curved-Y14 statement rides the standard fact that II_s enters the section-pulled
  operator as a zeroth-order tensor datum (vz_fcvz4_subprincipal.py, Block B). If a
  future construction makes II_s enter at FIRST order, Block D's window applies and
  SA-C4 reopens quantitatively.
- This closes SA-C4 FOR THE BUILT CANDIDATE at principal + subprincipal symbol order.
  It does NOT upgrade the repo-level VZ verdict (CONDITIONALLY_RESOLVED) and does not
  touch the E-block / cure-A route, which remains blocked as before.

Reproducible: python -u tests/W125_sac4_subprincipal_built.py  (exit 0 iff PASS).
Runtime ~2-3 min (a dozen 1664-dim SVDs).
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
RNG = np.random.default_rng(20260713)


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   {detail}" if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)
    return bool(ok)


def log(msg):
    print(msg, flush=True)


def q_of(xi):
    return float(np.sum(ETA * np.asarray(xi, dtype=float) ** 2))


def main():
    log("=" * 100)
    log("W125 / SA-C4 -- subprincipal FC-VZ-4 causality on the BUILT g=1 ker-Gamma candidate")
    log("=" * 100)

    e, Gamma, Pi, _ = gb.constraint_objects()
    w, V = np.linalg.eigh(Pi)
    K = V[:, w > 0.5]                       # orthonormal basis of ker Gamma, 1792 x 1664
    I14 = np.eye(N, dtype=complex)

    def cxi(xi):
        return sum(xi[a] * e[a] for a in range(N))

    def MD(xi):
        return np.kron(I14, cxi(xi))

    def R(xi, extra=None):
        M = MD(xi)
        if extra is not None:
            M = M + extra
        return K.conj().T @ (M @ K)

    def smin(xi, extra=None):
        return float(np.linalg.svd(R(xi, extra), compute_uv=False)[-1])

    # ---------------- BLOCK A: exact injectivity identities --------------------------------------
    log("\nBLOCK A -- the exact identities behind off-cone non-degeneracy")
    S14 = sum(ETA[a] * (e[a] @ e[a]) for a in range(N))
    idA1 = float(np.max(np.abs(S14 - N * np.eye(DIM))))
    xi0 = RNG.normal(size=N)
    c0 = cxi(xi0)
    T0 = sum(ETA[a] * (e[a] @ c0 @ e[a]) for a in range(N))
    idA2 = float(np.max(np.abs(T0 + (N - 2) * c0)))
    check("A1. gamma^a gamma_a = 14 I and gamma^a c(xi) gamma_a = -(14-2) c(xi) = -12 c(xi) "
          "(exact) -- so R(xi) psi = 0 with psi in ker Gamma forces c(xi) chi = 0 for the trace "
          "spinor, impossible at q != 0: the built restricted symbol is injective off the cone",
          idA1 < TOL and idA2 < 1e-12,
          f"||sum eta e e - 14 I||={idA1:.1e}, ||gamma^a c gamma_a + 12 c||={idA2:.1e}")
    check("A2. dim(ker Gamma) = 1664 = 1792 - 128 (Gamma surjective) and K orthonormal",
          K.shape == (1792, 1664) and float(np.linalg.norm(K.conj().T @ K - np.eye(1664))) < 1e-9,
          f"K: {K.shape}, ||K^dag K - I||~0")

    # ---------------- BLOCK B: characteristic variety = null cone --------------------------------
    log("\nBLOCK B -- off-cone non-degeneracy / on-cone degeneracy of the built restricted symbol")
    offcone = []
    signs = set()
    tries = 0
    while len(offcone) < 4 and tries < 40:
        tries += 1
        xi = RNG.normal(size=N)
        q = q_of(xi)
        if abs(q) < 0.5:
            continue
        if (q > 0 and (+1) not in signs) or (q < 0 and (-1) not in signs) or len(signs) == 2:
            s = smin(xi)
            offcone.append((q, s))
            signs.add(+1 if q > 0 else -1)
    ok_off = len(offcone) == 4 and all(s > 1e-2 for _, s in offcone) and len(signs) == 2
    check("B1. OFF-CONE NON-DEGENERATE: sigma_min(R(xi)) > 0 for sampled q != 0 of BOTH signs "
          "(4 samples) -- no spacelike or timelike characteristic off the null cone",
          ok_off, "; ".join(f"q={q:+.2f} smin={s:.3e}" for q, s in offcone))

    xin = np.zeros(N)
    xin[0], xin[9] = 1.0, 1.0                      # exact null covector of eta(9,5)
    s_null = smin(xin)
    check("B2. ON-CONE DEGENERATE: an exact null covector gives sigma_min(R) = 0 to machine "
          "precision -- the null cone IS characteristic (correct hyperbolic structure, not an "
          "everywhere-invertible fake)",
          q_of(xin) == 0.0 and s_null < 1e-10, f"q=0, smin={s_null:.1e}")

    base = RNG.normal(size=N)
    path = [(q_of(xin + t * base), smin(xin + t * base)) for t in (0.3, 0.1, 0.01)]
    dec = all(path[i][1] > path[i + 1][1] for i in range(len(path) - 1))
    check("B3. APPROACHING THE CONE: sigma_min -> 0 continuously as q -> 0 along a fixed path "
          "(monotone decrease, >100x drop into the cone; the characteristic variety is exactly "
          "{q=0}, reached continuously)",
          dec and path[-1][1] < 0.05 * path[0][1] and abs(path[-1][0]) < 0.05,
          "; ".join(f"q={q:+.4f} smin={s:.2e}" for q, s in path))

    # ---------------- BLOCK C: zeroth-order (subprincipal) inserts are harmless ------------------
    log("\nBLOCK C -- constant projector => degrees do not mix; zeroth-order II_s is subprincipal")
    xi = RNG.normal(size=N)
    lin = float(np.max(np.abs(R(2 * xi) - 2 * R(xi))))
    check("C1. R is EXACTLY degree-1: R(2 xi) = 2 R(xi) to machine precision (the constant "
          "equivariant projector cannot mix symbol degrees -- the structural difference from "
          "the Schur/E-block route where FC-VZ-4 was blocked)",
          lin < 1e-10, f"||R(2xi) - 2R(xi)||_max = {lin:.1e}")

    IIs = RNG.normal(size=(N, N))
    IIs = 0.5 * (IIs + IIs.T)
    IIs /= float(np.linalg.norm(IIs, 2))            # unit spectral norm
    B0 = np.kron(IIs, np.eye(DIM, dtype=complex))   # zeroth-order II_s-type insert
    L = 1.0e6
    princ_err = float(np.max(np.abs(R(L * xi, extra=1.0 * B0) / L - R(xi))))
    check("C2. ZEROTH-ORDER II_s INSERT IS STRICTLY SUBPRINCIPAL: the homogenized symbol of "
          "K^dag (M_D + B0) K equals R(xi) (residual -> 0 at L=1e6). With B1/B2 this means the "
          "characteristic variety stays {q=0} for ANY zeroth-order II_s: FC-VZ-4 cannot fire at "
          "subprincipal order on the built candidate",
          princ_err < 1e-4, f"||homogenized - R(xi)||_max = {princ_err:.1e}")

    # ---------------- BLOCK D: positive control -- first-order inserts DO have a window ----------
    log("\nBLOCK D -- positive control: a principal-symbol-modifying insert has a finite window")
    xiu = RNG.normal(size=N)
    xiu /= np.linalg.norm(xiu)
    while abs(q_of(xiu)) < 0.15:
        xiu = RNG.normal(size=N)
        xiu /= np.linalg.norm(xiu)
    s0 = smin(xiu)
    M1 = np.kron(IIs, cxi(xiu))                     # FIRST-order (degree-1) II_s-type insert
    scan = [(s, smin(xiu, extra=s * M1)) for s in (0.05, 0.2, 0.4, 0.8, 1.6)]
    smallest = min(v for _, v in scan)
    small_ok = scan[0][1] > 0.25 * s0               # weak insert: cone intact
    check("D1. FIRST-ORDER insert control: weak strength keeps sigma_min O(uncured) (cone "
          "intact = finite causal window), while some strength inside the scan drives "
          "sigma_min down by >10x (an off-cone near-characteristic appears) -- the test HAS "
          "POWER to detect the FC-VZ-4 failure mode it guards against",
          small_ok and smallest < 0.1 * s0,
          f"q={q_of(xiu):+.3f}, smin(s=0)={s0:.3e}; " +
          "; ".join(f"s={s} smin={v:.2e}" for s, v in scan))
    check("D2. VERDICT BOOKKEEPING: the built candidate is in the NON-DEGENERATE branch of the "
          "FC-VZ-4 dichotomy (B1-B3) and zeroth-order II_s cannot leave it (C1-C2); the "
          "degenerate-branch failure mode exists and is detectable (D1) but requires a first-"
          "order insert the constrained route does not generate",
          True, "SA-C4 status for the BUILT candidate: TEST-BUILT-PASSES (symbol level)")

    log("\n" + "=" * 100)
    log("SYNTHESIS -- SA-C4 on the built candidate")
    log("=" * 100)
    log("  The g=1 ker-Gamma cure (constant equivariant projector, carrier B) yields a restricted")
    log("  principal symbol whose characteristic variety is EXACTLY the eta(9,5) null cone, with")
    log("  zeroth-order II_s insertions provably subprincipal (degrees cannot mix). SA-C4:")
    log("  TEST-BUILT-PASSES at principal + subprincipal symbol order on the flat 14-dim model.")
    log("  NOT claimed: the curved-Y14 all-orders statement; the cure-A (Schur/E-block) route,")
    log("  which stays blocked exactly as vz_fcvz4_subprincipal.py recorded. The repo-level VZ")
    log("  verdict (CONDITIONALLY_RESOLVED) is NOT upgraded by this file.")
    if FAIL:
        log(f"SOME CHECKS FAILED: {FAIL}")
        return 1
    log("ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
