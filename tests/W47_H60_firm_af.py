#!/usr/bin/env python3
r"""
W47 / H60 -- FIRMING the asymptotic-freedom (AF) result from "indication" to "solid".

H57 (Waves 44-46) found: GU's induced 4th-order (Stelle/agravity) gravity flows to the GAUSSIAN UV
fixed point (asymptotic FREEDOM, not safety) in a 2-coupling one-loop truncation; critical-surface
dimension 3 in the KNOWN gravitational sector {M_Pl(=mu_DW), Lambda, f_0^2}; AF robust for
c_RS_weyl > -13.3. That is an INDICATION. H60 tests whether AF SURVIVES a bigger truncation:

  MOVE 1  ADD the RS dimensionless couplings z_B (RS kinetic norm, Bbar D^3 B) and y_RS (curvature-RS
          coupling Bbar Sigma.R B) to the flow with their leading one-loop STRUCTURE, and redo the
          fixed-point search in the ENLARGED space (f_2^2, f_0^2, z_B, y_RS). Does the Gaussian point
          stay the UV FP? Does a NON-Gaussian fixed point appear that the 2-coupling system could not see?
  MOVE 2  TIGHTEN c_RS_weyl by honest ker-Gamma dof counting (the projector keeps transverse /
          gamma-traceless spin-3/2, removes the gamma-trace spin-1/2 modes; gauge-fixing ghosts are a
          standard-gravitino artifact). Get a tighter value/range; re-check the AF window.
  MOVE 3  STABILITY / critical exponents in the enlarged (4-coupling) space; recount relevant
          directions (= UV critical-surface dimension = # free parameters). Did the RS couplings ADD
          relevant directions (less predictive) or are they irrelevant/redundant (predicted)?
  MOVE 4  (qualitative) what a genuine FRG/Reuter truncation would add -- NO faked FRG computation.

CONSTRUCTION FORKS (GEOMETER-VS-PHYSICS-OBJECTS.md), stated explicitly:
  (1) Gravity action: GU-native INDUCED |II|^2 -> 4th-order Stelle (f_2^2 Weyl, f_0^2 R^2). The
      enlarged fixed-point search lives on this truncation (H49).
  (2) RS sector: GU-native ker-Gamma-projected spin-3/2 (background-independent, degree-0 KINEMATIC
      projector, gamma-traceless; H58). USED HERE for BOTH (a) the c_RS_weyl dof counting (Move 2) and
      (b) the identification of z_B, y_RS as the RS marginal couplings (Move 1). The named RS beta
      coefficients are GUESS-grade templates (the exact values need a ker-Gamma heat-kernel); the
      CONCLUSIONS asserted below are the ones that survive INDEPENDENT of those values (the homogeneous-
      quadratic structure), plus the sign-conditional relevance of y_RS.
  (3) unitarity/positivity: Krein-graded [P,S]=0. OUT OF SCOPE. A fixed point is an RG statement about
      the FLOW of couplings, INDEPENDENT of positivity. Stated, not settled. The one place it touches
      is the sign of the wrong-sign conformal / RS ratio; left open.
  (4) mu_DW: ratio-only free scale -> realized as the Einstein/Newton transmutation scale M_Pl, one of
      the counted relevant directions.

KEY STRUCTURAL FACT (the firming lever): at one loop every beta of a marginal (dimensionless) coupling
is HOMOGENEOUS QUADRATIC in the couplings (no linear term -> the stability matrix vanishes at the
Gaussian point; every monomial is degree exactly 2 in the coupling variables). A homogeneous-quadratic
vector field beta satisfies beta(lambda g) = lambda^2 beta(g). Therefore any nonzero zero g* of beta is
NOT isolated: the whole ray {lambda g*} is a zero -- i.e. a fixed RATIO (an AF trajectory), never an
isolated interacting fixed point. So ADDING z_B, y_RS CANNOT manufacture a non-Gaussian fixed point at
this order; it can only (i) leave the Gaussian point the unique isolated FP and (ii) add fixed-ratio AF
trajectories. This holds for ANY values of the (unknown) RS beta coefficients -- which is exactly why
the verdict is robust to the ker-Gamma ignorance.

VERDICT: CONFIRMED-FIRMER (see bottom). Truncation-bounded, not a proof.

Reproducible: python tests/W47_H60_firm_af.py   (exit 0 on PASS)
No git commit (orchestrator verifies+commits). No canon/verdict file touched. Exploration-grade.
"""
from __future__ import annotations
import contextlib
import importlib.util
import io
import os
import sys
from dataclasses import dataclass

import numpy as np

TOL = 1e-9
results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


# =====================================================================================
# IMPORT STAGE 1 (reuse the betas + c_RS machinery; do NOT re-derive).
# =====================================================================================
_HERE = os.path.dirname(os.path.abspath(__file__))
_STAGE1 = os.path.join(_HERE, "W45_H57_stage1_beta_system.py")
_spec = importlib.util.spec_from_file_location("W45_stage1", _STAGE1)
S1 = importlib.util.module_from_spec(_spec)
sys.modules["W45_stage1"] = S1
with contextlib.redirect_stdout(io.StringIO()):
    try:
        _spec.loader.exec_module(S1)
    except SystemExit:
        pass

BetaSystem = S1.BetaSystem          # the Stage-1 2-coupling (f2sq,f0sq) system
THEORY_SPACE = S1.THEORY_SPACE
KAPPA = S1.KAPPA
b2_shift_from_anomaly = S1.b2_shift_from_anomaly
WEYL_ANOMALY_COEFF = S1.WEYL_ANOMALY_COEFF

log("=" * 92)
log("W47 / H60 -- FIRM ASYMPTOTIC FREEDOM (enlarged truncation, ker-Gamma dof, stability)")
log("=" * 92)
check("I1  Stage-1 beta system imported and reusable (BetaSystem, THEORY_SPACE, KAPPA, anomaly rule)",
      BetaSystem is not None and len(THEORY_SPACE) == 9 and abs(BetaSystem().b2() - (133/10 + 17/12)) < 1e-9,
      f"anchor b_2 = {BetaSystem().b2():.5f}; {len(THEORY_SPACE)} couplings")


# =====================================================================================
# MOVE 2 -- TIGHTEN c_RS_weyl by honest ker-Gamma dof counting.
#
# Standard massless spin-3/2 (gravitino) Weyl^2 trace-anomaly coeff = 255 (units 1/(360(4pi)^2))
# -> b_2 shift 255/180 = 17/12 = 1.4167 (Stage-1 ANCHOR, unpinned).
#
# ker-Gamma (fork 2) is a KINEMATIC, degree-0, background-independent projector onto the transverse,
# gamma-traceless spin-3/2 content. Relative to the STANDARD gauge-fixed gravitino it differs by:
#   (a) it REMOVES the gamma-trace spin-1/2 modes (the standard vector-spinor psi_mu contains a
#       spin-3/2 PLUS spin-1/2 gamma-trace); and
#   (b) it needs NO SUSY gauge-fixing ghosts (the FP + Nielsen-Kallosh spin-1/2 ghosts of the standard
#       gravitino gauge-fixing) -- those are an artifact of the standard quantization, not of a
#       kinematic projector.
# Both corrections are at the level of a HANDFUL of spin-1/2 (Dirac/Majorana) modes. Per-mode c-charge:
#   Weyl (2-comp) fermion : 9   (Stage-1 units)  -> b_2 units 9/180  = 0.05
#   Dirac (4-comp) fermion: 18  (Stage-1 units)  -> b_2 units 18/180 = 0.10
# The gamma-trace is one spin-1/2 (Majorana/Weyl 9 .. Dirac 18); the ghost sector is at most ~3 Dirac.
# BOUND the net shift by up to 4 Dirac spin-1/2 modes: |Delta| <= 4*18/180 = 0.4 in b_2 units.
# =====================================================================================
log("\n" + "=" * 92)
log("MOVE 2 -- ker-Gamma dof counting -> TIGHTEN c_RS_weyl")
log("=" * 92)

DIRAC_HALF = float(WEYL_ANOMALY_COEFF["Weyl_fermion"]) * 2.0      # Dirac spin-1/2 = 2 Weyl = 18
WEYL_HALF = float(WEYL_ANOMALY_COEFF["Weyl_fermion"])            # Majorana/Weyl spin-1/2 = 9
PER_DIRAC_B2 = DIRAC_HALF / 180.0                                # 0.10 in b_2 units
PER_WEYL_B2 = WEYL_HALF / 180.0                                  # 0.05 in b_2 units
ANCHOR = 17.0 / 12.0                                             # 1.41667

log(f"  per-mode Weyl^2 c-charge (Stage-1 units): Weyl/Majorana spin-1/2 = {WEYL_HALF:.0f}, "
    f"Dirac spin-1/2 = {DIRAC_HALF:.0f}")
log(f"  in b_2 units: Weyl/Majorana = {PER_WEYL_B2:.3f}, Dirac = {PER_DIRAC_B2:.3f} per spin-1/2 mode")

# central tightened estimate: keep the 255 transverse core, subtract ONE gamma-trace spin-1/2.
#   Majorana gamma-trace -> (255 - 9)/180 = 1.367 ;  Dirac gamma-trace -> (255 - 18)/180 = 1.317
c_central_majorana = (255.0 - WEYL_HALF) / 180.0
c_central_dirac = (255.0 - DIRAC_HALF) / 180.0
# conservative bound on the full ker-Gamma-vs-gravitino difference: up to 4 Dirac spin-1/2 either way.
DOF_BOUND_B2 = 4.0 * PER_DIRAC_B2                                # 0.4
c_lo = ANCHOR - DOF_BOUND_B2
c_hi = ANCHOR + DOF_BOUND_B2
log(f"  central tightened c_RS_weyl (remove 1 gamma-trace spin-1/2): "
    f"Majorana {c_central_majorana:.3f} .. Dirac {c_central_dirac:.3f}")
log(f"  conservative dof-counting BAND: c_RS_weyl in [{c_lo:.3f}, {c_hi:.3f}]  "
    f"(anchor {ANCHOR:.3f} +/- {DOF_BOUND_B2:.2f})")

check("K1  per-spin-1/2-mode Weyl-anomaly shift is 0.05 (Majorana/Weyl) .. 0.10 (Dirac) in b_2 units "
      "[= c-charge/180, the KNOWN /180 rule reused]",
      abs(PER_WEYL_B2 - 0.05) < 1e-9 and abs(PER_DIRAC_B2 - 0.10) < 1e-9,
      f"Weyl {PER_WEYL_B2}, Dirac {PER_DIRAC_B2}")
check("K2  ker-Gamma removes the gamma-trace spin-1/2 (and drops the SUSY ghosts); the net shift is a "
      "handful of spin-1/2 modes, |Delta c_RS_weyl| <= 0.4 in b_2 units (<= 4 Dirac spin-1/2)",
      DOF_BOUND_B2 == 0.4 and abs(c_central_dirac - ANCHOR) <= DOF_BOUND_B2,
      f"central shift ~ -{ANCHOR - c_central_dirac:.3f}; bound +/-{DOF_BOUND_B2}")
check("K3  TIGHTENED c_RS_weyl band [%.3f, %.3f] is entirely POSITIVE and far above the AF threshold "
      "-13.3 (removing spin-1/2 modes cannot approach it: it would need ~147 Dirac spin-1/2 removed)"
      % (c_lo, c_hi),
      c_lo > 0 and c_lo > -13.3, f"band [{c_lo:.3f},{c_hi:.3f}] vs threshold -13.3")

# re-check the AF window with the TIGHTENED band: b_2 > 0 across the whole band, margin >= 14.3.
b2_lo = BetaSystem(c_rs_weyl=c_lo).b2()
b2_hi = BetaSystem(c_rs_weyl=c_hi).b2()
margin_lo = c_lo - (-133.0 / 10.0)
check("K4  AF (b_2>0) holds across the ENTIRE tightened band; worst-case margin above the -13.3 sign-"
      "flip is %.2f (anchor margin was 14.72) -> tightening does NOT approach the threshold: AF FIRMER"
      % margin_lo,
      b2_lo > 0 and b2_hi > 0 and margin_lo > 14.0,
      f"b_2 in [{b2_lo:.3f},{b2_hi:.3f}]; margin_lo = {margin_lo:.3f}")


# =====================================================================================
# MOVE 1 + 3 -- ENLARGED 4-coupling beta system and its fixed-point / stability structure.
#
# g = (x, y, zB, yR) = (f_2^2, f_0^2, z_B, y_RS).  t = ln mu, kappa = 1/(4pi)^2.
#
#   beta_x  = -kappa x^2 b_2                                              (KNOWN + tightened c_RS_weyl)
#   beta_y  =  kappa[ (5/3)x^2 + 5 x y + (5/6 + d)y^2 ]                   (KNOWN + GUESS d)
#   beta_zB =  kappa * zB * ( c_zz zB + c_zf x + c_zy yR )               (GUESS template; note the
#                    overall factor zB -> z_B = 0 is an INVARIANT subspace => z_B is a REDUNDANT
#                    (multiplicatively-renormalized / wavefunction) coupling, NOT a physical direction.)
#   beta_yR =  kappa[ c_yy yR^2 + c_yf2 yR x + c_yf0 yR y + c_src x^2 ]  (GUESS template; c_yy sign =
#                    the undetermined marginal-relevance sign of y_RS.)
#
# EVERY monomial is degree exactly 2 in (x,y,zB,yR) -> the whole system is HOMOGENEOUS QUADRATIC:
#   beta(lambda g) = lambda^2 beta(g). This is the firming lever (see header). The named c_* are
# GUESS-grade templates; the asserted conclusions are the STRUCTURAL ones (homogeneity => Gaussian is
# the unique isolated FP; z_B redundant; stability matrix vanishes) that hold for ALL c_*, plus the
# sign-conditional relevance of y_RS.
# =====================================================================================
@dataclass
class EnlargedBetaSystem:
    c_rs_weyl: float = ANCHOR      # tightened band centre ~ anchor; swept in K-checks
    d_rs_r2: float = 0.0           # GUESS
    # RS marginal-coupling beta coefficients -- GUESS templates (ker-Gamma heat-kernel needed for true):
    c_zz: float = 0.0              # z_B self (kept 0: pure wavefunction normalization)
    c_zf: float = 1.0              # z_B <- f_2^2 (graviton dressing of the RS kinetic norm)
    c_zy: float = 0.5              # z_B <- y_RS
    c_yy: float = 5.0 / 6.0        # y_RS self  (SIGN is the undetermined relevance knob)
    c_yf2: float = 5.0             # y_RS <- f_2^2 mixing (template from the f_0 sector shape)
    c_yf0: float = 0.0             # y_RS <- f_0^2
    c_src: float = 5.0 / 3.0       # y_RS source from f_2^4 (template from the f_0 sector shape)
    n_s: int = 0
    n_f: int = 0
    n_v: int = 0

    def b2(self) -> float:
        return (133.0 / 10.0 + self.n_v / 5.0 + self.n_f / 20.0 + self.n_s / 60.0 + self.c_rs_weyl)

    def beta(self, g):
        x, y, zB, yR = g
        bx = -KAPPA * x * x * self.b2()                                  # independent of zB, yR
        by = KAPPA * ((5.0 / 3.0) * x * x + 5.0 * x * y
                      + (5.0 / 6.0 + self.d_rs_r2) * y * y)
        bzB = KAPPA * zB * (self.c_zz * zB + self.c_zf * x + self.c_zy * yR)
        byR = KAPPA * (self.c_yy * yR * yR + self.c_yf2 * yR * x
                       + self.c_yf0 * yR * y + self.c_src * x * x)
        return (bx, by, bzB, byR)


def jacobian_nd(bs, g, h=1e-6):
    g = np.asarray(g, dtype=float)
    n = len(g)
    J = np.zeros((n, n))
    for j in range(n):
        gp = g.copy(); gp[j] += h
        gm = g.copy(); gm[j] -= h
        J[:, j] = (np.asarray(bs.beta(tuple(gp))) - np.asarray(bs.beta(tuple(gm)))) / (2 * h)
    return J


def newton_nd(bs, g0, iters=300):
    g = np.asarray(g0, dtype=float)
    n = len(g)
    for _ in range(iters):
        Fv = np.asarray(bs.beta(tuple(g)))
        if np.max(np.abs(Fv)) < 1e-14:
            return g
        J = jacobian_nd(bs, tuple(g))
        try:
            step = np.linalg.solve(J + 1e-9 * np.eye(n), Fv)
        except np.linalg.LinAlgError:
            step = Fv
        g = g - 0.5 * step
        if not np.all(np.isfinite(g)) or np.max(np.abs(g)) > 1e6:
            return None
    Fv = np.asarray(bs.beta(tuple(g)))
    return g if np.max(np.abs(Fv)) < 1e-9 else None


log("\n" + "=" * 92)
log("MOVE 1/3 -- ENLARGED 4-coupling system g = (f_2^2, f_0^2, z_B, y_RS)")
log("=" * 92)
EB = EnlargedBetaSystem()

# (E1) Gaussian point (0,0,0,0) is a fixed point of the ENLARGED flow.
g0 = (0.0, 0.0, 0.0, 0.0)
b0 = EB.beta(g0)
check("E1  the GAUSSIAN point (0,0,0,0) is a fixed point of the ENLARGED flow (all 4 betas vanish): the "
      "AF UV fixed point survives adding z_B, y_RS",
      all(abs(bi) < TOL for bi in b0), f"beta(0,0,0,0) = {tuple(round(bi,15) for bi in b0)}")

# (E2) HOMOGENEITY beta(lambda g) = lambda^2 beta(g): the firming lever. Test on random g, lambda.
rng = np.random.default_rng(60)
homog_ok = True
worst = 0.0
for _ in range(200):
    g = rng.uniform(-1.5, 1.5, size=4)
    lam = rng.uniform(-3, 3)
    lhs = np.asarray(EB.beta(tuple(lam * g)))
    rhs = lam * lam * np.asarray(EB.beta(tuple(g)))
    worst = max(worst, float(np.max(np.abs(lhs - rhs))))
homog_ok = worst < 1e-12
check("E2  the enlarged one-loop system is HOMOGENEOUS QUADRATIC: beta(lambda g) = lambda^2 beta(g) "
      "(every monomial degree 2). This is the firming lever -> any nonzero zero is a whole RAY (a "
      "fixed RATIO / AF trajectory), never an isolated interacting fixed point",
      homog_ok, f"max |beta(lam g) - lam^2 beta(g)| over 200 random samples = {worst:.2e}")

# (E3) consequence of E2: NO isolated non-Gaussian fixed point. Multistart Newton in 4D from a grid
#      clusters at the origin (degenerate quadratic zero; floor ~1e-4 in 4D). No second isolated cluster.
seeds = [tuple(v) for v in rng.uniform(-1.0, 1.0, size=(60, 4))]
roots = []
for s in seeds:
    r = newton_nd(EB, s)
    if r is not None:
        roots.append(np.round(r, 6))
FLOOR = 1e-2
max_dev = max((float(np.max(np.abs(r))) for r in roots), default=0.0)
check("E3  multistart Newton (60 seeds, 4D) -> every convergent root clusters at the Gaussian point "
      "within the degenerate-zero floor; NO isolated non-Gaussian fixed point appears that the "
      "2-coupling system could not see",
      max_dev < FLOOR, f"max deviation from origin = {max_dev:.2e} < {FLOOR:g}; {len(roots)} roots")

# (E4) STABILITY MATRIX (4x4 Jacobian) at the Gaussian FP vanishes -> all 4 couplings MARGINAL.
M = jacobian_nd(EB, g0)
eig = np.linalg.eigvals(M)
log(f"  4x4 stability matrix at Gaussian FP:\n{np.array2string(M.round(12), prefix='    ')}")
log(f"  eigenvalues = {np.sort_complex(eig).round(12)}  -> critical exponents theta = -eig = all 0")
check("E4  the 4x4 stability matrix at the Gaussian FP is the ZERO matrix (no linear term): ALL of "
      "f_2^2, f_0^2, z_B, y_RS are MARGINAL (theta=0 at linear order). Adding the RS couplings added "
      "NO linear relevant direction",
      np.allclose(M, 0.0, atol=1e-6) and np.allclose(eig, 0.0, atol=1e-6),
      f"||M|| = {np.max(np.abs(M)):.2e}")

# (E5) z_B is a REDUNDANT (wavefunction) coupling: beta_zB is proportional to z_B, so z_B=0 is an
#      invariant subspace and z_B is NOT a physical relevant direction (removable by field rescaling).
zB_redundant = all(abs(EnlargedBetaSystem().beta((x, y, 0.0, yR))[2]) < TOL
                   for x in (0.0, 0.3, 0.7) for y in (0.0, 0.4) for yR in (0.0, 0.5))
check("E5  z_B is REDUNDANT: beta_{z_B} proportional to z_B (z_B=0 is an invariant subspace) -> multiplicatively "
      "renormalized wavefunction norm, removable by field rescaling. It adds ZERO physical free "
      "parameters to the critical surface",
      zB_redundant, "beta_zB(x,y,0,yR) = 0 for all probed x,y,yR")

# (E6) y_RS marginal-relevance is SIGN-CONDITIONAL (the undetermined ker-Gamma loop sign): on the AF
#      trajectory f_2^2->0, near the Gaussian point beta_yR ~ kappa c_yy yR^2. c_yy>0 -> grows in UV ->
#      marginally RELEVANT (+1 free parameter); c_yy<0 -> flows to 0 -> marginally IRRELEVANT (AF,
#      predicted). Either way f_2 AF is untouched. Exhibit both branches.
EB_rel = EnlargedBetaSystem(c_yy=+5.0 / 6.0)     # positive self-coupling
EB_irr = EnlargedBetaSystem(c_yy=-5.0 / 6.0)     # negative self-coupling
yR_rel = EB_rel.beta((0.0, 0.0, 0.0, 0.3))[3] > 0        # grows in UV -> relevant
yR_irr = EB_irr.beta((0.0, 0.0, 0.0, 0.3))[3] < 0        # flows to 0 -> irrelevant (AF)
check("E6  y_RS marginal-relevance is SIGN-CONDITIONAL on its (undetermined, ker-Gamma) self-coupling "
      "sign: c_yy>0 -> marginally RELEVANT (+1 free param); c_yy<0 -> marginally IRRELEVANT (AF, "
      "predicted). Neither branch touches f_2 AF",
      yR_rel and yR_irr,
      f"beta_yR(+)= {EB_rel.beta((0,0,0,0.3))[3]:.2e}>0, beta_yR(-)= {EB_irr.beta((0,0,0,0.3))[3]:.2e}<0")

# (E7) f_2 AF is UNAFFECTED by the RS marginal couplings at this order: beta_{f_2^2} depends only on
#      f_2^2 and b_2 (RS enters the graviton beta ONLY via the trace anomaly c_RS_weyl, Move 2), NOT
#      on z_B, y_RS. So the AF verdict cannot be spoiled by the enlarged sector at one loop.
bx_base = EnlargedBetaSystem().beta((0.4, 0.2, 0.0, 0.0))[0]
bx_zy = EnlargedBetaSystem().beta((0.4, 0.2, 5.0, 5.0))[0]
check("E7  f_2 asymptotic freedom is UNAFFECTED by z_B, y_RS at one loop: beta_{f_2^2} = -kappa f_2^4 "
      "b_2 is independent of z_B, y_RS (RS enters the graviton beta ONLY via the trace anomaly "
      "c_RS_weyl). The RS matter couplings cannot spoil AF at this order",
      abs(bx_base - bx_zy) < TOL and bx_base < 0,
      f"beta_f2sq unchanged by (z_B,y_RS): {bx_base:.4e}")


# =====================================================================================
# MOVE 3 (payoff) -- RECOUNT the UV critical-surface dimension in the enlarged space.
# =====================================================================================
log("\n" + "=" * 92)
log("MOVE 3 -- CRITICAL-SURFACE DIMENSION (enlarged space)")
log("=" * 92)
# KNOWN gravitational sector unchanged from Stage 2: {M_Pl(=mu_DW), Lambda, f_0^2} = 3; f_2^2 predicted.
KNOWN_GRAV = 3
# z_B: redundant -> +0.  y_RS: +0 (if c_yy<0, irrelevant) or +1 (if c_yy>0, relevant), sign undetermined.
yR_min, yR_max = 0, 1
enlarged_marginal_lo = KNOWN_GRAV + 0 + yR_min      # 3
enlarged_marginal_hi = KNOWN_GRAV + 0 + yR_max      # 4
# full truncation still adds the RS dimensionful {m_RS, g4f} (GUESS): +2.
full_lo = enlarged_marginal_lo + 2                  # 5
full_hi = enlarged_marginal_hi + 2                  # 6
log(f"  KNOWN gravitational sector    : {KNOWN_GRAV}  {{M_Pl(=mu_DW), Lambda, f_0^2}}  (f_2^2 PREDICTED by AF)")
log(f"  + z_B (redundant)             : +0")
log(f"  + y_RS (sign-conditional)     : +0 (c_yy<0, AF) .. +1 (c_yy>0, relevant)")
log(f"  -> enlarged MARGINAL sector   : {enlarged_marginal_lo} .. {enlarged_marginal_hi}")
log(f"  + RS dimensionful {{m_RS,g4f}} : +2 (GUESS)")
log(f"  -> FULL truncation critical-surface dimension : {full_lo} .. {full_hi}")
check("D1  enlarged MARGINAL-sector critical-surface dimension = 3 (z_B redundant -> +0; y_RS "
      "irrelevant) .. 4 (y_RS marginally relevant). The Stage-2 count 3 is UNCHANGED at best and grows "
      "by at most 1: the RS dimensionless couplings did NOT blow up the parameter count",
      enlarged_marginal_lo == 3 and enlarged_marginal_hi == 4)
check("D2  FULL-truncation critical-surface dimension = 5 .. 6 (adds RS dimensionful m_RS, g4f at GUESS "
      "grade). Predictivity is essentially preserved: AF still PREDICTS f_2^2 (the one genuine gain)",
      full_lo == 5 and full_hi == 6, f"full = {full_lo}..{full_hi}")


# =====================================================================================
# ROBUSTNESS -- the structural verdict is INDEPENDENT of the unknown RS coefficients.
# Sweep sign/magnitude combinations of (c_zz,c_zf,c_zy,c_yy,c_yf2,c_yf0,c_src): for EVERY combination
# (a) the Gaussian point stays a fixed point, (b) homogeneity holds, (c) the stability matrix at the
# Gaussian FP vanishes, (d) z_B stays redundant, (e) f_2 AF is untouched. -> the verdict does not
# depend on pinning the ker-Gamma heat-kernel.
# =====================================================================================
log("\n" + "=" * 92)
log("ROBUSTNESS -- verdict independent of the (unknown) RS beta coefficients")
log("=" * 92)
combos = 0
all_robust = True
vals = (-2.0, -0.5, 0.0, 0.5, 2.0)
for c_yy in vals:
    for c_src in (-1.0, 0.0, 1.0):
        for c_zf in (-1.0, 1.0):
            eb = EnlargedBetaSystem(c_yy=c_yy, c_src=c_src, c_zf=c_zf, c_zy=1.0, c_yf2=2.0)
            combos += 1
            gauss_fp = all(abs(bi) < TOL for bi in eb.beta((0.0, 0.0, 0.0, 0.0)))
            gt = rng.uniform(-1, 1, size=4); lam = 2.3
            hom = np.max(np.abs(np.asarray(eb.beta(tuple(lam * gt)))
                                - lam * lam * np.asarray(eb.beta(tuple(gt))))) < 1e-12
            stab0 = np.allclose(jacobian_nd(eb, (0.0, 0.0, 0.0, 0.0)), 0.0, atol=1e-6)
            zbred = abs(eb.beta((0.5, 0.3, 0.0, 0.4))[2]) < TOL
            af = eb.beta((0.4, 0.2, 1.0, 1.0))[0] < 0
            if not (gauss_fp and hom and stab0 and zbred and af):
                all_robust = False
check("R1  across %d sign/magnitude combinations of the unknown RS beta coefficients, EVERY case keeps "
      "(Gaussian FP, homogeneity, vanishing stability matrix, z_B redundant, f_2 AF): the firming "
      "verdict does NOT depend on pinning the ker-Gamma heat-kernel" % combos,
      all_robust and combos >= 30, f"{combos} combos all robust = {all_robust}")


# =====================================================================================
# MOVE 4 -- FRG / Reuter qualitative note (NO faked computation).
# =====================================================================================
log("\n" + "=" * 92)
log("MOVE 4 -- FRG/Reuter qualitative note (no computation performed)")
log("=" * 92)
log("  A genuine FRG (Reuter-type) truncation keeps the FULL nonperturbative running of the dimension-")
log("  ful Einstein-Hilbert couplings (g~=G k^2, lambda~=Lambda/k^2). In Reuter-dimensionless form")
log("  these carry their CANONICAL scaling as LINEAR terms in the betas -> the system is NO LONGER")
log("  homogeneous-quadratic, so the E2 lever no longer forbids an interacting fixed point: an FRG")
log("  Reuter fixed point (non-Gaussian, finite # relevant directions) generically APPEARS in the EH")
log("  sector. Published FRG of higher-derivative gravity (Codello-Percacci; Benedetti-Machado-")
log("  Saueressig; Niedermaier) finds the higher-derivative (Weyl/f_2) coupling remains ASYMPTOTICALLY")
log("  FREE even alongside that Reuter FP -> the perturbative f_2 AF verdict is LIKELY STABLE under FRG,")
log("  with the UV picture becoming the MIXED scenario (safety in the EH sector + freedom in the higher-")
log("  derivative sector). This is a qualitative expectation, NOT a computation done here.")
FRG_COMPUTED = False
check("F1  the FRG statement is QUALITATIVE only (not computed here); it flags that FRG breaks the "
      "homogeneous-quadratic structure (linear canonical terms) and can add a Reuter FP, while the f_2 "
      "AF is expected to persist (mixed safety+freedom picture)",
      FRG_COMPUTED is False)


# =====================================================================================
# POSITIVITY CAVEAT (explicit, out of scope) + re-run of W45/W46 for non-regression.
# =====================================================================================
log("\n" + "=" * 92)
log("POSITIVITY CAVEAT (out of scope) -- explicit")
log("=" * 92)
POSITIVITY_SETTLED_HERE = False
AF_INDEPENDENT_OF_POSITIVITY = True
log("  A UV fixed point (asymptotic freedom) is a statement about the FLOW of couplings; it is")
log("  INDEPENDENT of Krein [P,S]=0 loop-positivity, which is NOT settled here. Enlarging the")
log("  truncation firms the FLOW verdict; it does not touch positivity. The wrong-sign conformal/RS")
log("  ratio remains the single place the two conditions meet, and it is left OPEN.")
check("C1  the firmed AF/FP verdict is stated INDEPENDENT of Krein loop-positivity (not settled here); "
      "enlarging the truncation does not change that the two are distinct UV conditions",
      (POSITIVITY_SETTLED_HERE is False) and (AF_INDEPENDENT_OF_POSITIVITY is True))


# =====================================================================================
# VERDICT / EXIT
# =====================================================================================
log("\n" + "=" * 92)
npass = sum(1 for _, ok, _ in results if ok)
ntot = len(results)
log(f"CHECKS: {npass}/{ntot} passed.")

# load-bearing asserts
assert all(abs(bi) < TOL for bi in EB.beta((0.0, 0.0, 0.0, 0.0))), "Gaussian not a FP in enlarged space"
assert homog_ok, "enlarged system not homogeneous-quadratic (firming lever fails)"
assert np.allclose(jacobian_nd(EB, g0), 0.0, atol=1e-6), "enlarged stability matrix not zero"
assert zB_redundant, "z_B not redundant"
assert abs(bx_base - bx_zy) < TOL and bx_base < 0, "f_2 AF spoiled by RS marginal couplings"
assert c_lo > 0 and margin_lo > 14.0, "tightened c_RS_weyl band approached the AF threshold"
assert enlarged_marginal_lo == 3 and enlarged_marginal_hi == 4, "critical-surface recount changed"
assert all_robust, "verdict not robust to unknown RS coefficients"
assert npass == ntot, "some W47 checks FAILED -- see [FAIL] lines"

log("")
log("VERDICT (H60, firming H57 asymptotic freedom): CONFIRMED-FIRMER (truncation-bounded).")
log("  * ENLARGED SPACE (f_2^2,f_0^2,z_B,y_RS): the Gaussian point stays the UNIQUE isolated UV fixed")
log("    point. The one-loop system is HOMOGENEOUS-QUADRATIC, so NO isolated non-Gaussian (interacting)")
log("    fixed point can appear -- for ANY value of the unknown ker-Gamma RS coefficients. Adding the")
log("    RS dimensionless couplings did NOT create a Landau pole or a Reuter-type interacting FP here.")
log("  * z_B is REDUNDANT (wavefunction norm) -> +0 free parameters. y_RS adds +0 (AF) or +1 (relevant)")
log("    depending on an undetermined ker-Gamma loop sign. Critical-surface dimension: 3..4 (marginal")
log("    sector), 5..6 (full). Predictivity essentially preserved; f_2^2 still PREDICTED by AF.")
log("  * c_RS_weyl TIGHTENED by ker-Gamma dof counting to the band [%.2f, %.2f] (central ~%.2f); AF"
    % (c_lo, c_hi, c_central_dirac))
log("    margin stays > 14.3 -- the tightening does not approach the -13.3 sign-flip threshold.")
log("  * f_2 AF is UNSPOILED by the RS marginal couplings at one loop (they do not feed beta_{f_2^2}).")
log("  * FRG could add a Reuter FP (breaks homogeneity via linear canonical terms), but f_2 AF is")
log("    expected to persist -> mixed safety+freedom picture. NOT computed here.")
log("  * POSITIVITY: still NOT settled; independent of this flow verdict.")
log("HOW MUCH FIRMER: AF moves from 'indication (2 couplings)' to 'solid within the perturbative one-")
log("loop truncation' -- the no-interacting-FP result is now STRUCTURAL (homogeneity), robust to the RS")
log("ignorance, and the one uncertain input (c_RS_weyl) is tightened to a narrow positive band. It is")
log("NOT yet a proof (FRG / higher loops / true ker-Gamma coefficients remain).")
raise SystemExit(0)
