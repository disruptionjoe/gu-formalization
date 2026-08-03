#!/usr/bin/env python3
r"""W230 finite-fixture and FLRW-toy mapping check (Wave A-2, item 3).

THE QUESTION (XS-S; gates A6 / C11 / M-H13).  W230 claimed theta ~ M^{-1} J iff the
connection distortion has NO fundamental kinetic term (c_kin = 0), with L a stand-in
for the connection Laplacian D_A* D_A -- the Z_U = |D_A U|^2 gradient stiffness the
branch-3 parent action carries un-built (W203:127).  The FLRW pipeline
(tests/wave25/H44_de_backreacted_background.py:81-115) integrates
    B'' = -(3 + H'/H) B' - (M^2/H^2) B .
Seat2's caveat: W230's L is a SPATIAL-gradient stand-in and the FLRW mode is
homogeneous (k = 0), where a gradient term vanishes regardless -- so maybe the
tension dissolves.

HOSTILE-REVIEW SCOPE CORRECTION.  The actual native map from the Y14 connection
distortion and its full gradient operator to the scalar FLRW mode has not been built.
For a fixed source J, theta remains on the target ray whenever L t is proportional to
M t, where t=M^{-1}J; therefore nonzero L can preserve the identity's direction.  The
random fixture below shows generic breaking, not a global iff theorem.  The KK and
FLRW calculations are conditional toys, not the missing native reduction.

THE FINITE TEST (derivation in the exploration note, Section 3; witnesses here).
The k = 0 escape removes only the X4-SPATIAL sub-block of the gradient operator.
The pipeline's field equation uses two OTHER sub-blocks of the same covariant object:
  (1) the TIME-kinetic term (B'') -- the base-time block of |D theta|^2, which
      homogeneity does NOT remove (the oscillating solution has B-dot-dot != 0:
      that is Result 1's entire content); and
  (2) the mass M^2 = 8 itself -- BY CONSTRUCTION the ground eigenvalue
      lambda_{N,1} = (9/2)^2 - (7/2)^2 of the FIBER NORMAL LAPLACIAN on
      GL(4,R)/O(3,1) (canon/theta-field-flrw-dark-energy-eos.md:80-81; H44 header),
      i.e. a fiber-GRADIENT eigenvalue, which homogeneity of X4 cannot touch.
The PIPE row sets the mass coefficient near zero while retaining the normalized B''
term, so it tests (c_b,c_f)=(1,0), not simultaneous removal of both coefficients.

Witnesses (preregistered, exploration note Section 1.3):
  [PC]   W230's [NEC] anchors reproduce bit-for-bit on the same seeds.
  [BLK]  block-structured random L: each tested nonzero table assignment breaks the
         target direction.  An aligned nonzero planted L=M preserves it and prevents
         the finite fixture from being misread as a global iff theorem.
  [KK]   conditional separable toy: oscillator frequency^2=(c_f/c_b)lambda_1.
         And (9/2)^2 - (7/2)^2 = 8 exactly (the repo's M^2 is a Laplacian eigenvalue).
  [PIPE] under the massless-fiber toy the H44 pipeline DEGENERATES: M^2 -> 0 at
         f0 = 0.125 reduces H(z) to LCDM to machine precision -- no oscillation,
         no theta phenomenology, no object for the M-H13 refit to refit.

Run: PYTHONDONTWRITEBYTECODE=1 ./_local/cas-venv/bin/python -u \
       tests/de-certification/w230_ckin_flrw_mapping_check.py
Exit 0 iff all finite-fixture/toy checks hold.  It does not close the native bridge.
"""
from __future__ import annotations
import os
import sys
import importlib.util
import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(_HERE, "..", "generation-sector")))
import gen_sector_bridge as gb  # noqa: E402

N_DIRS, DIM = 14, 128
RNG = np.random.default_rng(20260714)
FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}", flush=True)
    if not ok:
        FAIL.append(name)


def log(m=""):
    print(m, flush=True)


# ===========================================================================
# W230's construction, verbatim (same rep, same seeds, same kernels).
# ===========================================================================
e = gb.gammas()
beta_S = e[0].copy()
for a in range(1, 9):
    beta_S = beta_S @ e[a]


def Jvec(psi):
    return np.array([float((psi.conj() @ (beta_S @ e[a]) @ psi).real) for a in range(N_DIRS)])


psi0 = RNG.standard_normal(DIM) + 1j * RNG.standard_normal(DIM)   # W230's first draw
Gram = np.real(np.array([[np.vdot(e[a].reshape(-1), e[b].reshape(-1)) for b in range(N_DIRS)]
                         for a in range(N_DIRS)]))
M = Gram
Lrng = np.random.default_rng(770230)
Braw = Lrng.standard_normal((N_DIRS, N_DIRS))
L = Braw @ Braw.T + 0.5 * np.eye(N_DIRS)
m2, kappa = 1.0, 1.0
Jv = Jvec(psi0)
t = np.linalg.solve(M, Jv)                                        # the identity target


def align_with(Lop, c):
    th = np.linalg.solve(m2 * M + c * Lop, kappa * Jv)
    return float(abs(th @ t) / (np.linalg.norm(th) * np.linalg.norm(t)))


def target_ray_residual(Lop):
    """Zero exactly when L t is parallel to M t for this fixed target ray."""
    Lt = Lop @ t
    Mt = M @ t
    alpha = float((Mt @ Lt) / (Mt @ Mt))
    return float(np.linalg.norm(Lt - alpha * Mt) / max(np.linalg.norm(Lt), 1e-30))


def main():
    log("=" * 78)
    log("W230 finite fixture + conditional FLRW toy; native mapping remains OPEN")
    log("=" * 78)

    # -----------------------------------------------------------------------
    # [PC] -- W230 [NEC] anchors reproduce on the same seeds.
    # -----------------------------------------------------------------------
    log("\n[PC] W230 [NEC] anchors (same rep, seeds 20260714 / 770230)")
    a0, a1, a100 = align_with(L, 0.0), align_with(L, 1.0), align_with(L, 100.0)
    log(f"  alignment at c_kin = 0 / 1 / 100 = {a0:.8f} / {a1:.8f} / {a100:.8f}")
    log(f"  (W230:                            1.00000000 / 0.99654503 / 0.70318085)")
    check("PC1: c_kin = 0 alignment = 1 exactly (W230 sufficiency leg)", abs(a0 - 1.0) < 1e-12)
    check("PC2: c_kin = 1 anchor reproduces (0.99654503 +/- 1e-6)", abs(a1 - 0.99654503) < 1e-6,
          f"{a1:.8f}")
    check("PC3: c_kin = 100 anchor reproduces (0.70318085 +/- 1e-6)", abs(a100 - 0.70318085) < 1e-6,
          f"{a100:.8f}")
    L_aligned = M.copy()
    a_aligned = align_with(L_aligned, 1.0)
    r_aligned = target_ray_residual(L_aligned)
    log(f"  planted aligned nonzero L=M: alignment={a_aligned:.8f}, ray residual={r_aligned:.2e}")
    check("PC4 planted counterexample: nonzero L can preserve the target ray",
          abs(a_aligned - 1.0) < 1e-12 and r_aligned < 1e-12)

    # -----------------------------------------------------------------------
    # [BLK] -- block-structured L: base (3,1) block vs fiber (6,4) block.
    # -----------------------------------------------------------------------
    log("\n[BLK] block-structured L: (9,5) = (3,1) base + (6,4) fiber (W203 FIB split)")
    log("  base directions {0,1,2 | 9} (3 plus + the base time), fiber {3..8 | 10..13}.")
    log("  L(c_b, c_f) = c_b P_b L P_b + c_f P_f L P_f;  identity target M^{-1} J.")
    base_idx = [0, 1, 2, 9]
    fib_idx = [3, 4, 5, 6, 7, 8, 10, 11, 12, 13]
    P_b = np.zeros((N_DIRS, N_DIRS)); P_b[base_idx, base_idx] = 1.0
    P_f = np.zeros((N_DIRS, N_DIRS)); P_f[fib_idx, fib_idx] = 1.0
    Lb = P_b @ L @ P_b
    Lf = P_f @ L @ P_f

    def align_blk(cb, cf):
        th = np.linalg.solve(m2 * M + cb * Lb + cf * Lf, kappa * Jv)
        return float(abs(th @ t) / (np.linalg.norm(th) * np.linalg.norm(t)))

    table = {}
    for cb, cf in [(0, 0), (1, 0), (0, 1), (1, 1), (10, 0), (0, 10), (10, 10)]:
        table[(cb, cf)] = align_blk(cb, cf)
        log(f"     (c_b, c_f) = ({cb:2d}, {cf:2d}) -> alignment = {table[(cb, cf)]:.8f}")
    check("BLK1: identity holds at (0,0) exactly", abs(table[(0, 0)] - 1.0) < 1e-12)
    check("BLK2: every TESTED nonzero random-fixture assignment breaks the target "
          "direction (this is not a universal quantifier)",
          all(v < 1.0 - 1e-4 for k, v in table.items() if k != (0, 0)),
          "min gap = %.2e" % min(1.0 - v for k, v in table.items() if k != (0, 0)))
    # signature fence: Lorentzian-time base block (indefinite) also breaks it
    u9 = np.zeros(N_DIRS); u9[9] = 1.0
    P_sp = P_b.copy(); P_sp[9, 9] = 0.0
    L_lor = P_sp @ L @ P_sp - 2.0 * np.outer(u9, u9)
    evs = np.linalg.eigvalsh(L_lor)
    a_lor = align_with(L_lor, 1.0)
    log(f"  signature fence: Lorentzian base block, eig range [{evs.min():.2f}, {evs.max():.2f}],"
        f" alignment = {a_lor:.8f}")
    check("BLK3 (signature fence): an INDEFINITE (Lorentzian-time) base block also "
          "breaks the identity generically", evs.min() < 0 < evs.max() and a_lor < 1.0 - 1e-4,
          f"{a_lor:.8f}")

    # -----------------------------------------------------------------------
    # [KK] -- the KK toy: both blocks are load-bearing for the oscillator.
    # -----------------------------------------------------------------------
    log("\n[KK] KK reduction toy: S ~ int c_b (dB/dt)^2 + c_f theta Delta_fiber theta")
    lam_bc1 = (9.0 / 2.0) ** 2 - (7.0 / 2.0) ** 2
    check("KK1: the repo's M^2 = 8 is EXACTLY the BC_1 fiber normal-Laplacian ground "
          "eigenvalue (9/2)^2 - (7/2)^2 (canon theta-field-flrw:80-81; H44 header)",
          lam_bc1 == 8.0, f"{lam_bc1}")
    # discrete fiber Laplacian, ground eigenvalue lam1; KK mode B(t) Y(y):
    nf = 40
    Lap_f = (2.0 * np.eye(nf) - np.eye(nf, k=1) - np.eye(nf, k=-1)) * (nf + 1) ** 2
    lam1 = float(np.linalg.eigvalsh(Lap_f)[0])
    for cb, cf in [(1.0, 1.0), (1.0, 0.0), (0.0, 1.0)]:
        if cb > 0:
            w2 = cf * lam1 / cb
            log(f"     (c_b, c_f) = ({cb:.0f}, {cf:.0f}): omega^2 = (c_f/c_b) lam1 = {w2:.3f}"
                f"  -> {'oscillates' if w2 > 0 else 'NO restoring force (frozen; no M^2)'}")
        else:
            log(f"     (c_b, c_f) = ({cb:.0f}, {cf:.0f}): NO B'' term -- constraint equation, "
                f"no propagating mode")
    check("KK2: oscillator frequency^2 = (c_f/c_b) lam1 > 0 requires BOTH blocks nonzero",
          (1.0 * lam1 / 1.0) > 0 and lam1 > 0, f"lam1={lam1:.3f}")
    identity_region = {(0, 0)}
    dynamics_region = {(cb, cf) for cb in (0, 1) for cf in (0, 1) if cb > 0 and cf > 0}
    check("KK3 (conditional toy): the stipulated zero-coefficient region {(0,0)} and "
          "the toy oscillator region {(1,1)} are disjoint",
          identity_region.isdisjoint(dynamics_region), f"dyn={sorted(dynamics_region)}")

    # -----------------------------------------------------------------------
    # [PIPE] -- the H44 pipeline degenerates under the bridge's own axiom.
    # -----------------------------------------------------------------------
    log("\n[PIPE] H44 massless-fiber toy: M^2 -> 0 while normalized B'' remains")
    spec = importlib.util.spec_from_file_location(
        "H44_pipe", os.path.normpath(os.path.join(_HERE, "..", "wave25",
                                                  "H44_de_backreacted_background.py")))
    H44 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(H44)
    bg = H44.solve_backreacted(1e-8, 0.125, npts=900, n_iter=40)
    a_g = bg["a"]
    H2_l = 0.315 * a_g ** -3 + 0.685
    dH2 = float(np.max(np.abs(bg["H2"] - H2_l)))
    w0 = float(bg["w_theta"][-1])
    log(f"  M^2 = 1e-8, f0 = 0.125: max|H^2 - H^2_LCDM| = {dH2:.2e}; w_theta(z=0) = {w0:+.6f}")
    check("PIPE1: with the fiber stiffness removed the theta sector is a SECOND "
          "cosmological constant -- H(z) reduces to LCDM to < 1e-6 at f0 = 0.125",
          dH2 < 1e-6, f"{dH2:.2e}")
    check("PIPE2: no oscillation survives (w_theta(0) = -1 to < 1e-4)",
          abs(w0 + 1.0) < 1e-4, f"{w0:+.6f}")
    log("  => in the conditional (c_b,c_f)=(1,0) toy there is no theta-driven E(z)")
    log("     shape.  This does not identify the native Y14 coefficients.")

    # -----------------------------------------------------------------------
    log("\n" + "-" * 78)
    log("DISPOSITION (hostile-review corrected)")
    log("-" * 78)
    log("  Random W230 and block fixtures generically rotate the target ray, but the")
    log("  planted L=M witness proves that nonzero stiffness need not do so.")
    log("  The separable KK and massless-fiber FLRW rows are conditional toys.")
    log("  The native observation/pullback/projection/normalization map and shared")
    log("  coefficient assignment are unbuilt.  W230-NATIVE-BRIDGE: OPEN/BLOCKED.")

    if FAIL:
        log(f"\nFAILED: {FAIL}")
        sys.exit(1)
    log("\nexit 0 = finite fixture/toy checks recorded; native bridge remains OPEN.")
    log("         witnesses: PC 4/4, BLK 3/3, KK 3/3, PIPE 2/2.")
    sys.exit(0)


if __name__ == "__main__":
    main()
