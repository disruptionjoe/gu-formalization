#!/usr/bin/env python3
r"""TRACK-2 (H47 declare-and-build) -- T2B: the RAW (non-CPL) dark-energy curves of
the conditional theory GU-given-S: w(z) and H(z) tabulated over z in [0, 2].

FIREWALL: every output is "given S" (the declared postulate set; see
explorations/track2-conditional-numbers-2026-07-13.md).  Nothing here asserts S.

STATED UP FRONT (scope): the CPL (w0,wa) comparison is ALREADY FALSIFIED (H43:
global closest 3.20 sigma on a fixed LCDM background; H44: 3.22 sigma on the fully
backreacted background; no admissible M^2, f0, ansatz, IC, or background rescues it).
What is NOT settled is the RAW expansion history: the non-CPL H(z) mimics DESI-CPL
distances to ~1% (canon DARK-ENERGY-03 degeneracy).  THIS test emits those raw
curves as the conditional theory's dark-energy deliverable.  The DESI DR2 BAO
full-likelihood verification is a PARALLEL team's job (Team 2) and is deliberately
NOT duplicated here.

MODEL (declared shape, free amplitude):
  DE = constant DeWitt-Lambda (w = -1) + Klein-Gordon theta field B, mass
  M^2 = 8 H0^2  (S7: BC_1 ground eigenvalue lambda_{N,1} = (9/2)^2 - (7/2)^2 on
  GL(4,R)/O(3,1); reconstruction-grade, declared).  Amplitude f0 = rho_theta(0)/rho_L
  is FREE (the one data-facing fit; H42).  Slow-roll IC at z = 30.  Background is
  SELF-CONSISTENT (theta backreacts on H; the H44 solver, reproduced with attribution).

DISCIPLINE: solver core reproduced from tests/wave25/H44_de_backreacted_background.py
(same physics, same conventions).  Load-bearing curves cross-checked by an
INDEPENDENT integrator (scipy solve_ivp, adaptive Radau) against the fixed-step RK4.
No em-dash characters.

Run: python -u tests/track2/T2B_dark_energy_curves.py   (exit 0 iff all PASS)
"""
from __future__ import annotations
import sys
import numpy as np
from scipy.integrate import solve_ivp

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}", flush=True)
    if not ok:
        FAIL.append(name)


def log(m=""):
    print(m, flush=True)


# ===========================================================================
# Cosmology + solver core (reproduced from tests/wave25/H44, attributed above).
# ===========================================================================
Om, OL = 0.315, 0.685
Z_START = 30.0
M2_BC1 = 8.0


def H2_lcdm(a):
    return Om * a ** -3 + OL


def _rk4_kg(Ngrid, H2, H2_mid, HpoH, HpoH_mid, M2, B0, BN0):
    n = Ngrid.shape[0]
    h = Ngrid[1] - Ngrid[0]
    B = np.empty(n)
    BN = np.empty(n)
    B[0] = B0
    BN[0] = BN0
    for i in range(n - 1):
        b = B[i]; d = BN[i]
        h2a = H2[i]; hpa = HpoH[i]
        h2m = H2_mid[i]; hpm = HpoH_mid[i]
        h2b = H2[i + 1]; hpb = HpoH[i + 1]
        k1b = d
        k1d = -(3.0 + hpa) * d - (M2 / h2a) * b
        b2 = b + 0.5 * h * k1b; d2 = d + 0.5 * h * k1d
        k2b = d2
        k2d = -(3.0 + hpm) * d2 - (M2 / h2m) * b2
        b3 = b + 0.5 * h * k2b; d3 = d + 0.5 * h * k2d
        k3b = d3
        k3d = -(3.0 + hpm) * d3 - (M2 / h2m) * b3
        b4 = b + h * k3b; d4 = d + h * k3d
        k4b = d4
        k4d = -(3.0 + hpb) * d4 - (M2 / h2b) * b4
        B[i + 1] = b + (h / 6.0) * (k1b + 2 * k2b + 2 * k3b + k4b)
        BN[i + 1] = d + (h / 6.0) * (k1d + 2 * k2d + 2 * k3d + k4d)
    return B, BN


def solve_backreacted(M2, f0, z_start=Z_START, npts=1400, n_iter=60, tol=1e-12):
    rho_L = OL / (1.0 + f0)
    rho_theta0 = OL * f0 / (1.0 + f0)
    a0 = 1.0 / (1.0 + z_start)
    Ngrid = np.linspace(np.log(a0), 0.0, npts)
    Nmid = 0.5 * (Ngrid[:-1] + Ngrid[1:])
    a_g = np.exp(Ngrid)
    rho_m = Om * a_g ** -3

    H2 = rho_m + OL
    rho_theta = np.zeros_like(Ngrid)
    p_theta = np.zeros_like(Ngrid)
    B = np.ones_like(Ngrid)
    BN = np.zeros_like(Ngrid)
    dmax = np.inf
    for _ in range(n_iter):
        HpoH = -1.5 * (rho_m + (rho_theta + p_theta)) / H2
        H2_mid = np.interp(Nmid, Ngrid, H2)
        HpoH_mid = np.interp(Nmid, Ngrid, HpoH)
        BN0 = -M2 / (3.0 * H2[0])
        B, BN = _rk4_kg(Ngrid, H2, H2_mid, HpoH, HpoH_mid, M2, 1.0, BN0)
        Bdot = np.sqrt(H2) * BN
        KE = 0.5 * Bdot ** 2
        PE = 0.5 * M2 * B ** 2
        shape = KE + PE
        A = rho_theta0 / shape[-1]
        rho_theta_new = A * shape
        p_theta_new = A * (KE - PE)
        H2_new = rho_m + rho_L + rho_theta_new
        dmax = float(np.max(np.abs(H2_new - H2)))
        rho_theta, p_theta, H2 = rho_theta_new, p_theta_new, H2_new
        if dmax < tol:
            break
    Bdot = np.sqrt(H2) * BN
    w_theta = (0.5 * Bdot ** 2 - 0.5 * M2 * B ** 2) / (0.5 * Bdot ** 2 + 0.5 * M2 * B ** 2)
    return dict(N=Ngrid, a=a_g, z=1.0 / a_g - 1.0, B=B, BN=BN,
                rho_theta=rho_theta, w_theta=w_theta, H2=H2, rho_L=rho_L,
                converged_delta=dmax)


def wDE(bg):
    p_theta = bg["w_theta"] * bg["rho_theta"]
    return (-bg["rho_L"] + p_theta) / (bg["rho_L"] + bg["rho_theta"])


def cpl_fit(z, w, zmax=2.0, ngrid=400):
    i = np.argsort(z)
    zs, ws = z[i], w[i]
    zg = np.linspace(0.0, zmax, ngrid)
    wg = np.interp(zg, zs, ws)
    x = zg / (1.0 + zg)
    A = np.vstack([np.ones_like(x), x]).T
    (w0, wa), *_ = np.linalg.lstsq(A, wg, rcond=None)
    return w0, wa


def sample(z, y, zq):
    """Sample y(z) at zq (grids run z descending)."""
    i = np.argsort(z)
    return np.interp(zq, z[i], y[i])


def main():
    log("=" * 78)
    log("T2B -- raw (non-CPL) dark-energy curves of GU-given-S: w(z), H(z), z in [0,2]")
    log("=" * 78)
    log("SCOPE: the CPL (w0,wa) comparison is FALSIFIED (H43 3.20s / H44 3.22s; stated")
    log("up front, not softened).  These are the RAW curves at the declared shape")
    log("M^2 = 8 H0^2 with the amplitude f0 FREE (a FIT parameter, labeled as such).")
    log("The DESI DR2 BAO full-likelihood check is Team 2's parallel deliverable.")

    # -----------------------------------------------------------------------
    # GUARD 1: f0 -> 0 reduces to LCDM.
    # -----------------------------------------------------------------------
    log("\n[GUARD] f0 -> 0: background must reduce to LCDM.")
    bg0 = solve_backreacted(M2_BC1, 1e-6)
    err = float(np.max(np.abs(bg0["H2"] - H2_lcdm(bg0["a"]))))
    check("f0->0 backreacted background reduces to LCDM to < 1e-4", err < 1e-4,
          f"max|dH2|={err:.2e}")

    # -----------------------------------------------------------------------
    # GUARD 2: canonical point reproduces H44's published (w0,wa).
    # -----------------------------------------------------------------------
    bg_c = solve_backreacted(M2_BC1, 0.125)
    w0c, wac = cpl_fit(bg_c["z"], wDE(bg_c))
    check("canonical (M^2=8, f0=0.125) reproduces H44 (w0,wa)=(-0.7922,-0.2450) to 0.01",
          abs(w0c + 0.7922) < 0.01 and abs(wac + 0.2450) < 0.01,
          f"({w0c:+.4f},{wac:+.4f})")

    # -----------------------------------------------------------------------
    # GUARD 3: independent integrator (solve_ivp Radau) on the CONVERGED background
    # reproduces the RK4 field -> w(z) to < 5e-3 at all sample z.
    # -----------------------------------------------------------------------
    log("\n[GUARD] independent route: adaptive Radau vs fixed-step RK4 (f0=0.125).")
    Ngrid = bg_c["N"]
    H2g = bg_c["H2"]
    rho_m = Om * np.exp(Ngrid) ** -3
    p_th = bg_c["w_theta"] * bg_c["rho_theta"]
    HpoH = -1.5 * (rho_m + (bg_c["rho_theta"] + p_th)) / H2g

    def rhs(N, y):
        b, d = y
        h2 = np.interp(N, Ngrid, H2g)
        hp = np.interp(N, Ngrid, HpoH)
        return [d, -(3.0 + hp) * d - (M2_BC1 / h2) * b]

    sol = solve_ivp(rhs, (Ngrid[0], 0.0), [1.0, -M2_BC1 / (3.0 * H2g[0])],
                    method="Radau", rtol=1e-10, atol=1e-12, dense_output=True)
    Bi, BNi = sol.sol(Ngrid)
    Bdi = np.sqrt(H2g) * BNi
    KEi, PEi = 0.5 * Bdi ** 2, 0.5 * M2_BC1 * Bi ** 2
    w_th_i = (KEi - PEi) / (KEi + PEi)
    rho_sh = KEi + PEi
    A = (bg_c["rho_theta"][-1]) / rho_sh[-1]
    w_de_i = (-bg_c["rho_L"] + A * (KEi - PEi)) / (bg_c["rho_L"] + A * rho_sh)
    zq = np.linspace(0.0, 2.0, 9)
    w_rk4 = sample(bg_c["z"], wDE(bg_c), zq)
    w_ind = sample(bg_c["z"], w_de_i, zq)
    dmax = float(np.max(np.abs(w_rk4 - w_ind)))
    check("independent Radau route matches RK4 w(z) to < 5e-3 over z in [0,2]",
          dmax < 5e-3, f"max|dw|={dmax:.1e}")
    _ = w_th_i  # (theta-only EOS available; combined w is the deliverable)

    # -----------------------------------------------------------------------
    # THE DELIVERABLE: tabulated raw curves, M^2 = 8, f0 in {0.05, 0.125, 0.5}.
    # -----------------------------------------------------------------------
    zq = np.arange(0.0, 2.01, 0.25)
    for f0 in (0.05, 0.125, 0.5):
        bg = solve_backreacted(M2_BC1, f0)
        w = wDE(bg)
        Hn = np.sqrt(bg["H2"])                      # H/H0 (flat, H(0)=H0)
        dH = np.sqrt(bg["H2"] / H2_lcdm(bg["a"])) - 1.0
        w0f, waf = cpl_fit(bg["z"], w)
        log("\n" + "-" * 78)
        log(f"M^2 = 8 H0^2, f0 = {f0}  [f0 = FIT; curve shape given (S, f0)]"
            f"   (CPL projection ({w0f:+.3f},{waf:+.3f}) shown for cross-ref only)")
        log(f"  {'z':>5} | {'w_DE(z)':>9} | {'H(z)/H0':>9} | {'H/H_LCDM - 1':>12}")
        for z in zq:
            log(f"  {z:5.2f} | {sample(bg['z'], w, z):+9.4f} | "
                f"{sample(bg['z'], Hn, z):9.4f} | {sample(bg['z'], dH, z):+11.4%}")
        if abs(f0 - 0.125) < 1e-12:
            wt = [sample(bg['z'], w, z) for z in (0.0, 0.5, 1.0, 2.0)]
            check("canonical w(z) samples reproduce H44 Q1 "
                  "(-0.853, -0.855, -0.910, -0.966) to 0.005",
                  max(abs(wt[0] + 0.853), abs(wt[1] + 0.855),
                      abs(wt[2] + 0.910), abs(wt[3] + 0.966)) < 5e-3,
                  f"w={[f'{v:+.3f}' for v in wt]}")

    log("\nSTRUCTURE of the curves (given S, any f0 > 0): w_DE(z) is NON-CPL and")
    log("non-monotone (shallow peak near z ~ 0.25, then w -> -1 at high z as the theta")
    log("density damps); H(z) sits above LCDM by O(f0) percent at intermediate z and")
    log("is pinned to H0 at z = 0 by flatness.  The f0 -> 0 limit is exactly LCDM.")

    log("\n" + "-" * 78)
    if FAIL:
        log(f"FAILED: {FAIL}")
        sys.exit(1)
    log("exit 0 = T2B recorded.  Raw w(z) and H(z) curves emitted for GU-given-S at")
    log("M^2 = 8 H0^2 (declared) with f0 free (FIT); CPL falsification (H43/H44)")
    log("stated up front; DESI full-likelihood deferred to Team 2 (no duplication).")
    sys.exit(0)


if __name__ == "__main__":
    main()
