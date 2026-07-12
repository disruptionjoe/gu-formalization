#!/usr/bin/env python3
r"""
W45 / H57 (Stage 1 of 2) -- THEORY SPACE + BETA-FUNCTION STRUCTURE for the GU asymptotic-safety /
asymptotic-freedom flow. This module ENCODES the one-loop beta-function system as data + callables
so Stage 2 can import it, search for a UV fixed point, and count relevant directions (= dimension of
the UV critical surface = number of free parameters).

FLOW QUESTION (H57): does GU flow to a UV fixed point, and how predictive is it? This is the live
SECOND UV route now that power-counting renormalizability is confirmed (H58: GU renormalizable,
D<=4 on the ker-Gamma subspace; RS adds its own finite closed counterterm set beyond pure Stelle).

STAGE 1 (this module) sets up the theory space and PORTS the known 4th-order-gravity beta functions,
adds the RS (spin-3/2) matter shift, and assembles the ODE system dg_i/dt = beta_i(g). Stage 2 takes
this and answers: (Q1) does a UV fixed point exist? (Q2) how many UV-relevant directions (critical
surface dimension)?

CONSTRUCTION FORKS (GEOMETER-VS-PHYSICS-OBJECTS.md) used here, stated explicitly:
  (1) Gravity action: GU program-native INDUCED |II|^2 -> 4th-order Stelle (Weyl^2 + R^2), NOT a
      freely chosen R^2 Lagrangian. USED: the Stelle/agravity two-coupling (f_2, f_0) truncation --
      this IS GU's spin-2 + conformal-mode sector (H49). Ported beta functions live on this side.
  (2) RS sector: GU program-native ker-Gamma-projected spin-3/2 (background-independent, degree-0
      projector, H58), NOT the standard massive-RS constraint-solve. USED: ker-Gamma. CONSEQUENCE:
      the RS contribution c_RS to the gravitational beta coefficients is a NAMED PARAMETER, anchored
      at the standard massless-spin-3/2 (Christensen-Duff) value but NOT pinned, because the ker-Gamma
      projection changes the effective propagating dof from the naive massive-RS / gravitino count.
  (3) unitarity/positivity: Krein-graded [P,S]=0. OUT OF SCOPE for the flow (H57 asks about the FLOW,
      not ghost positivity). A Krein ghost could in principle flip a beta-coefficient SIGN; that is
      flagged as the one place the AF prior could fail, and is left to the positivity frontier.
  (4) mu_DW: ratio-only free scale. The dimensionful couplings (G, Lambda, RS masses) are measured in
      cutoff units; only their dimensionless ratios are physical. Only the DIMENSIONLESS couplings run
      to a fixed point -- those are f_2^2, f_0^2, and the marginal RS couplings.

KNOWN / ESTIMATED / GUESS grading is attached to every coefficient below.

Ported one-loop beta functions (t = ln mu, kappa = 1/(4pi)^2):
  [KNOWN, cited] (4pi)^2 df_2^2/dt = -f_2^4 (133/10 + N_V/5 + N_f/20 + N_s/60)   (Weyl; asympt. FREE)
  [KNOWN, cited] (4pi)^2 df_0^2/dt = (5/3) f_2^4 + 5 f_2^2 f_0^2 + (5/6) f_0^4 + (scalar matter)
    Refs: Fradkin-Tseytlin (1982); Avramidi-Barvinsky (1985); Salvio-Strumia "Agravity" JHEP 06 (2014)
    080 = arXiv:1403.4226; Salvio "Quadratic Gravity" arXiv:1804.09944. The 133/10 pure-gravity Weyl
    coefficient and the matter shifts (N_V/5, N_f/20, N_s/60) are theirs, verbatim.
  [KNOWN, cited] matter shift of the Weyl coefficient b_2 = (field's Weyl^2 trace-anomaly coefficient
    in units of 1/(360(4pi)^2)) / 180. Verified below to reproduce scalar->1/60, Weyl-fermion->1/20,
    vector->1/5. (Christensen-Duff / Duff "Twenty years of the Weyl anomaly".)

RS matter shift:
  [ESTIMATED, named parameter] a spin-3/2 field's Christensen-Duff Weyl^2 trace-anomaly coefficient is
    255 (units 1/(360(4pi)^2)) -> b_2 shift = 255/180 = 17/12 ~ 1.4167. This is the STANDARD-FIELD
    ANCHOR. The GU ker-Gamma carrier's true value is the named parameter C_RS_WEYL; anchor 17/12, but
    the ker-Gamma projection removes the spin-1/2 modes (H58) so the propagating dof -- hence C_RS_WEYL
    -- is not the naive massless-gravitino count. Sign: standard anchor is POSITIVE, so it deepens
    asymptotic freedom of f_2; a Krein-ghost sign flip would need C_RS_WEYL < -133/10 to break AF.
  [GUESS, named parameter, anchor 0] D_RS_R2 = RS contribution to the f_0^2 (R^2) beta. The standard
    agravity f_0 matter term is scalar-only (via the non-minimal xi); a pure fermion does not
    renormalize R^2 at leading order. The ker-Gamma RS carrier's non-minimal Bbar Sigma.R B coupling
    COULD contribute, but that coefficient needs a real ker-Gamma heat-kernel computation. Anchor 0.

This module: encodes the couplings (with mass dimensions), the beta callables (parametrized by
C_RS_WEYL, D_RS_R2, and standard matter multiplicities), and self-consistency checks. Exit 0 on PASS.

Reproducible: python tests/W45_H57_stage1_beta_system.py
No git commit (orchestrator verifies+commits). No canon/verdict file touched. Exploration-grade.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from fractions import Fraction as F
from typing import Callable

TOL = 1e-12
results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


# =====================================================================================
# THEORY SPACE -- the running couplings, with canonical mass dimensions.
#   RUN-AND-CAN-HIT-A-FIXED-POINT  <=>  dimensionless (the marginal couplings).
#   DIMENSIONFUL couplings are measured in cutoff units (fork 4, mu_DW ratio-only); they are the
#   relevant directions carried along the flow but do not themselves have an interacting fixed value
#   independent of the cutoff -- Stage 2 treats them via the dimensionless combinations g~=G k^2,
#   lambda~=Lambda/k^2 if it wants the full Reuter-type system.
# =====================================================================================
@dataclass(frozen=True)
class Coupling:
    name: str
    symbol: str
    mass_dim: F           # canonical mass dimension of the COUPLING/coefficient
    dimensionless: bool   # True => runs to a fixed point (marginal); False => dimensionful/relevant
    sector: str
    grade: str            # KNOWN / ESTIMATED / GUESS for its beta structure
    note: str = ""


THEORY_SPACE: list[Coupling] = [
    # ---- 4th-order gravity sector (GU induced |II|^2 -> Stelle; fork 1) ----
    Coupling("Weyl-squared coupling", "f_2^2", F(0), True, "gravity-4th", "KNOWN",
             "coeff of C^2 ~ 1/(2 f_2^2); asymptotically FREE (b_2>0)."),
    Coupling("R-squared coupling", "f_0^2", F(0), True, "gravity-4th", "KNOWN",
             "coeff of R^2 ~ 1/(6 f_0^2); NOT asymptotically free (conformal mode)."),
    Coupling("Gauss-Bonnet coeff", "b_GB", F(0), True, "gravity-4th", "KNOWN",
             "topological in 4D; total derivative, does not feed the other betas. Spectator."),
    Coupling("Newton constant", "G", F(-2), False, "gravity-EH", "KNOWN",
             "dimensionful; Reuter-dimensionless g~ = G k^2. Generated by dim. transmutation."),
    Coupling("cosmological constant", "Lambda", F(2), False, "gravity-EH", "KNOWN",
             "dimensionful; Reuter-dimensionless lambda~ = Lambda / k^2."),
    # ---- RS (spin-3/2) sector: ker-Gamma-projected, program-native (fork 2). From H58 enumeration. ----
    Coupling("RS 4th-order kinetic norm", "z_B", F(0), True, "RS", "ESTIMATED",
             "dimensionless normalization of Bbar D^3 B (the marginal RS kinetic); [B]=1/2."),
    Coupling("curvature-RS coupling", "y_RS", F(0), True, "RS", "ESTIMATED",
             "coeff of the dim-4 non-minimal Bbar Sigma.R B (marginal; can hit a fixed point)."),
    Coupling("RS mass term", "m_RS", F(3), False, "RS", "GUESS",
             "coeff of Bbar B (dim-1 op); dimensionful/relevant. mu_DW-set, ratio-only."),
    Coupling("four-fermi (Bbar B)^2", "g4f", F(2), False, "RS", "GUESS",
             "coeff of (Bbar B)^2 (dim-2 op); dimensionful/relevant."),
]

log("=" * 92)
log("THEORY SPACE (Stage 1) -- running couplings and mass dimensions")
log("=" * 92)
log(f"  {'symbol':10s} {'dim':>5s}  {'runs?':5s}  {'sector':12s} {'grade':9s}  note")
for c in THEORY_SPACE:
    runs = "YES" if c.dimensionless else "no"
    log(f"  {c.symbol:10s} {str(c.mass_dim):>5s}  {runs:5s}  {c.sector:12s} {c.grade:9s}  {c.note}")

DIMLESS = [c.symbol for c in THEORY_SPACE if c.dimensionless]
check("T1  the dimensionless (marginal) couplings -- the ones that RUN to a fixed point -- are "
      "isolated", set(DIMLESS) == {"f_2^2", "f_0^2", "b_GB", "z_B", "y_RS"},
      f"dimensionless: {DIMLESS}")
check("T2  the load-bearing UV couplings for the fixed-point search are f_2^2 and f_0^2 (plus RS "
      "marginal z_B, y_RS)", "f_2^2" in DIMLESS and "f_0^2" in DIMLESS,
      "f_2^2 (Weyl, AF) and f_0^2 (R^2, not AF) are the pure-gravity pair")


# =====================================================================================
# KNOWN matter-shift rule: b_2 contribution per field = (Weyl^2 trace-anomaly coeff)/180,
# in units where the anomaly is written (1/(360(4pi)^2))[ (coeff) W^2 + ... ]. Verify it reproduces
# the agravity matter shifts (N_V/5, N_f/20, N_s/60) from the Christensen-Duff c-central charges.
# =====================================================================================
log("\n" + "=" * 92)
log("PORTED matter-shift rule: b_2 contribution = (Weyl^2 anomaly coeff)/180  [KNOWN, cited]")
log("=" * 92)

# Christensen-Duff Weyl^2 (C^2) trace-anomaly coefficients, units 1/(360(4pi)^2):
WEYL_ANOMALY_COEFF = {          # field : coefficient of W^2
    "real_scalar": F(3),
    "Weyl_fermion": F(9),
    "vector": F(36),
    "spin_3_2_gravitino": F(255),   # <-- the standard massless spin-3/2 value (the RS ANCHOR)
}
# agravity matter shifts of b_2 (Salvio-Strumia), the ground truth to reproduce:
AGRAVITY_SHIFT = {"real_scalar": F(1, 60), "Weyl_fermion": F(1, 20), "vector": F(1, 5)}


def b2_shift_from_anomaly(field: str) -> F:
    """KNOWN rule: matter contribution to the Weyl beta coefficient b_2 = anomaly_coeff / 180."""
    return WEYL_ANOMALY_COEFF[field] / 180


rule_ok = all(b2_shift_from_anomaly(f) == AGRAVITY_SHIFT[f] for f in AGRAVITY_SHIFT)
for f in AGRAVITY_SHIFT:
    log(f"    {f:14s}: anomaly {str(WEYL_ANOMALY_COEFF[f]):>4s}/180 = {str(b2_shift_from_anomaly(f)):>5s}"
        f"   (agravity: {str(AGRAVITY_SHIFT[f]):>5s})")
check("M1  the /180 rule reproduces the agravity matter shifts (scalar->1/60, Weyl-fermion->1/20, "
      "vector->1/5) from the Christensen-Duff c-charges [KNOWN cross-check]", rule_ok,
      "the Weyl-beta matter shift IS the conformal c-central charge, up to the fixed 1/180")

# The RS anchor (ESTIMATED): standard massless spin-3/2 Weyl^2 coeff 255 -> shift 255/180 = 17/12.
C_RS_WEYL_ANCHOR = b2_shift_from_anomaly("spin_3_2_gravitino")   # = 17/12
log(f"\n    spin-3/2 ANCHOR: anomaly 255/180 = {C_RS_WEYL_ANCHOR} = {float(C_RS_WEYL_ANCHOR):.4f}  "
    f"[ESTIMATED -- named parameter C_RS_WEYL; ker-Gamma changes effective dof]")
check("M2  standard massless spin-3/2 anchor for the RS Weyl-beta shift is 255/180 = 17/12 (>0, so "
      "it DEEPENS asymptotic freedom of f_2) [ESTIMATED anchor]",
      C_RS_WEYL_ANCHOR == F(17, 12) and C_RS_WEYL_ANCHOR > 0,
      f"C_RS_WEYL anchor = {C_RS_WEYL_ANCHOR}; true GU value left as a named parameter")


# =====================================================================================
# THE ASSEMBLED BETA-FUNCTION SYSTEM  (dg_i/dt = beta_i(g)), t = ln mu, kappa = 1/(4pi)^2.
# Encoded as callables parametrized by the RS named parameters and standard matter multiplicities.
# This is the object Stage 2 imports.
# =====================================================================================
KAPPA = 1.0 / (4.0 * 3.141592653589793) ** 2   # 1/(4pi)^2


@dataclass
class BetaSystem:
    """One-loop beta functions for the dimensionless gravitational couplings g = (f2sq, f0sq).

    Parameters (Stage 2 may vary):
      c_rs_weyl : RS contribution to the Weyl beta coefficient b_2 (ESTIMATED; anchor 17/12).
      d_rs_r2   : RS contribution to the f_0^2 (R^2) beta (GUESS; anchor 0).
      n_s,n_f,n_v : extra standard matter (real scalars / Weyl fermions / vectors), default 0
                    (GU's propagating content beyond the RS carrier; kept explicit for Stage-2 sweeps).
    """
    c_rs_weyl: float = float(F(17, 12))   # ESTIMATED anchor; NAMED PARAMETER for Stage 2
    d_rs_r2: float = 0.0                  # GUESS anchor 0; NAMED PARAMETER for Stage 2
    n_s: int = 0
    n_f: int = 0
    n_v: int = 0

    def b2(self) -> float:
        """Weyl beta coefficient b_2 = 133/10 + matter + RS. beta_{f2sq} = -kappa f2sq^2 * b_2."""
        return (133.0 / 10.0
                + self.n_v / 5.0 + self.n_f / 20.0 + self.n_s / 60.0
                + self.c_rs_weyl)

    def beta_f2sq(self, f2sq: float, f0sq: float) -> float:
        # (4pi)^2 df2sq/dt = -f2sq^2 (133/10 + matter + c_rs_weyl)   [KNOWN + ESTIMATED]
        return -KAPPA * f2sq * f2sq * self.b2()

    def beta_f0sq(self, f2sq: float, f0sq: float) -> float:
        # (4pi)^2 df0sq/dt = (5/3) f2sq^2 + 5 f2sq f0sq + (5/6) f0sq^2 + d_rs_r2 * f0sq^2   [KNOWN + GUESS]
        return KAPPA * ((5.0 / 3.0) * f2sq * f2sq
                        + 5.0 * f2sq * f0sq
                        + (5.0 / 6.0) * f0sq * f0sq
                        + self.d_rs_r2 * f0sq * f0sq)

    def beta(self, g: tuple[float, float]) -> tuple[float, float]:
        """Full RHS dg/dt for g=(f2sq,f0sq). The callable Stage 2 integrates / root-finds."""
        f2sq, f0sq = g
        return (self.beta_f2sq(f2sq, f0sq), self.beta_f0sq(f2sq, f0sq))


log("\n" + "=" * 92)
log("ASSEMBLED BETA SYSTEM  dg/dt = beta(g),  g = (f_2^2, f_0^2)")
log("=" * 92)
BS = BetaSystem()  # RS anchor values
log(f"  b_2 (Weyl coeff, RS anchor) = 133/10 + 17/12 = {BS.b2():.5f}   -> beta_{{f2^2}} < 0 (AF)")
log("  beta_{f0^2} = kappa[(5/3)f2^4 + 5 f2^2 f0^2 + (5/6)f0^4 + d_RS f0^4],  d_RS anchor 0")


# ------- self-consistency checks the module ASSERTS (so it is a real test, not a print) -------
log("\n" + "=" * 92)
log("SELF-CONSISTENCY CHECKS")
log("=" * 92)

# (S1) pure-gravity Weyl coefficient is exactly 133/10 (no matter, no RS).
pure = BetaSystem(c_rs_weyl=0.0)
check("S1  pure-gravity Weyl beta coefficient b_2 = 133/10 = 13.3 exactly [KNOWN, cited]",
      abs(pure.b2() - 133.0 / 10.0) < TOL, f"b_2(pure) = {pure.b2()}")

# (S2) THE load-bearing sign: pure-gravity Weyl^2 coupling is ASYMPTOTICALLY FREE
#      (beta_{f2sq} < 0 for f2sq>0), the strong prior from Fradkin-Tseytlin / Avramidi-Barvinsky.
b_f2 = pure.beta_f2sq(0.5, 0.3)
check("S2  pure-gravity f_2^2 is ASYMPTOTICALLY FREE: beta_{f2^2} < 0 for f2^2>0 (Fradkin-Tseytlin, "
      "Avramidi-Barvinsky) [KNOWN, the strong prior]", b_f2 < 0,
      f"beta_{{f2^2}}(0.5,0.3) = {b_f2:.6e} < 0 -> f_2 -> 0 in the UV")

# (S3) adding the RS field at the standard anchor KEEPS asymptotic freedom (b_2 grows, stays >0).
withRS = BetaSystem()  # anchor
check("S3  RS at the standard anchor DEEPENS asymptotic freedom (b_2 = 13.3 + 1.4167 > 13.3 > 0), "
      "so f_2 stays AF [KNOWN+ESTIMATED]", withRS.b2() > pure.b2() > 0,
      f"b_2: pure {pure.b2():.4f} -> with RS {withRS.b2():.4f}")

# (S4) AF of f_2 is ROBUST: it survives unless the RS/Krein construction drives c_RS below -133/10.
#      Exhibit the sign-flip threshold as data for Stage 2 (the one way the AF prior could fail).
flip = BetaSystem(c_rs_weyl=-133.0 / 10.0 - 0.01)
check("S4  f_2 AF fails ONLY if c_RS_weyl < -133/10 ~ -13.3 (a large NEGATIVE RS/Krein contribution). "
      "The standard anchor +1.42 is far from this. [boundary data for Stage 2]",
      flip.b2() < 0 and withRS.b2() > 0,
      f"threshold b_2<0 needs c_RS < -13.3; anchor is +1.42")

# (S5) the Gaussian point f_2^2=f_0^2=0 is a FIXED POINT (all betas vanish) -- the AF/free UV FP.
g0 = (0.0, 0.0)
b0 = BS.beta(g0)
check("S5  the Gaussian point (f_2^2,f_0^2)=(0,0) is a FIXED POINT (beta=0): the asymptotically-free "
      "UV fixed point candidate [KNOWN]", abs(b0[0]) < TOL and abs(b0[1]) < TOL,
      f"beta(0,0) = {b0}")

# (S6) f_0^2 is NOT asymptotically free: at f_2^2=0, beta_{f0^2} = kappa(5/6)f0^4 > 0 (f0 grows in UV).
#      This is the known 'conformal mode' obstruction Stage 2 must handle (f0->inf / xi->-1/6 route).
b_f0 = BS.beta_f0sq(0.0, 0.4)
check("S6  f_0^2 is NOT asymptotically free: at f_2^2=0, beta_{f0^2} = kappa(5/6)f0^4 > 0 -> f_0 grows "
      "in the UV (the conformal-mode issue; Salvio-Strumia f0->inf / xi->-1/6 resolution) [KNOWN]",
      b_f0 > 0, f"beta_{{f0^2}}(0,0.4) = {b_f0:.6e} > 0")

# (S7) the beta callable is usable by Stage 2: returns a 2-tuple of finite floats off the FP.
gt = BS.beta((0.4, 0.25))
import math as _m
check("S7  beta(g) is a Stage-2-usable callable: finite 2-tuple RHS off the fixed point",
      len(gt) == 2 and all(_m.isfinite(x) for x in gt),
      f"beta(0.4,0.25) = ({gt[0]:.4e}, {gt[1]:.4e})")

# (S8) d_RS is a live GUESS knob: it shifts the f_0 beta and must actually change the flow.
alt = BetaSystem(d_rs_r2=1.0)
check("S8  d_RS_R2 (RS -> R^2 beta, GUESS anchor 0) is a live named parameter: changing it changes "
      "beta_{f0^2} [structural]",
      abs(alt.beta_f0sq(0.4, 0.3) - BS.beta_f0sq(0.4, 0.3)) > 1e-6,
      "Stage 2 can sweep d_RS_R2; anchor 0 = fermion does not renormalize R^2 at leading order")


# =====================================================================================
# HANDOFF TO STAGE 2 (printed, and encoded in STAGE2_HANDOFF for import).
# =====================================================================================
STAGE2_HANDOFF = {
    "dimensionless_couplings_that_run": ["f_2^2", "f_0^2", "b_GB(spectator)", "z_B", "y_RS"],
    "pure_gravity_betas_(4pi)^2": {
        "df_2^2/dt": "-f_2^4 (133/10 + N_V/5 + N_f/20 + N_s/60 + c_RS_weyl)",
        "df_0^2/dt": "(5/3)f_2^4 + 5 f_2^2 f_0^2 + (5/6)f_0^4 + d_RS_R2 f_0^4",
    },
    "known_coefficients": {"weyl_pure": F(133, 10), "f0_from_f2^4": F(5, 3),
                           "f0_mixed": F(5), "f0_self": F(5, 6)},
    "rs_named_parameters": {
        "c_RS_weyl": {"anchor": str(F(17, 12)), "grade": "ESTIMATED",
                      "why": "std massless spin-3/2 Weyl-anomaly 255/180; ker-Gamma changes dof"},
        "d_RS_R2": {"anchor": "0", "grade": "GUESS",
                    "why": "fermion does not renormalize R^2 at leading order; needs ker-Gamma heat-kernel"},
    },
    "questions_for_stage2": [
        "Q1: does a UV fixed point exist? (Gaussian FP (0,0) is AF; is there a nontrivial one?)",
        "Q2: dimension of the UV critical surface = number of relevant directions = # free parameters?",
        "Q3: is f_2 AF robust to the RS/Krein construction (does c_RS_weyl stay > -133/10)?",
        "Q4: how is the f_0 conformal-mode non-AF resolved (f_0->inf / xi->-1/6 / RS y_RS backreaction)?",
        "Q5: linearize beta at the FP -> stability matrix eigenvalues -> critical exponents theta_i.",
    ],
}
log("\n" + "=" * 92)
log("HANDOFF TO STAGE 2")
log("=" * 92)
log("  RUNNING (dimensionless) couplings : " + ", ".join(STAGE2_HANDOFF["dimensionless_couplings_that_run"]))
log("  beta (4pi)^2 df_2^2/dt = " + STAGE2_HANDOFF["pure_gravity_betas_(4pi)^2"]["df_2^2/dt"])
log("  beta (4pi)^2 df_0^2/dt = " + STAGE2_HANDOFF["pure_gravity_betas_(4pi)^2"]["df_0^2/dt"])
log("  RS named params : c_RS_weyl (anchor 17/12, ESTIMATED), d_RS_R2 (anchor 0, GUESS)")
for q in STAGE2_HANDOFF["questions_for_stage2"]:
    log("    " + q)


# =====================================================================================
# VERDICT / EXIT
# =====================================================================================
npass = sum(1 for _, ok, _ in results if ok)
ntot = len(results)
log("\n" + "=" * 92)
log(f"CHECKS: {npass}/{ntot} passed.")

assert npass == ntot, "some Stage-1 beta-system checks FAILED -- see [FAIL] lines"
# the load-bearing asserts:
assert abs(pure.b2() - 13.3) < TOL, "pure-gravity Weyl coefficient != 133/10"
assert pure.beta_f2sq(0.5, 0.3) < 0, "pure-gravity f_2^2 not asymptotically free"
assert withRS.b2() > 0, "RS anchor broke asymptotic freedom of f_2 (should not, at the anchor)"
assert abs(BS.beta((0.0, 0.0))[0]) < TOL and abs(BS.beta((0.0, 0.0))[1]) < TOL, \
    "Gaussian point is not a fixed point"
assert BS.beta_f0sq(0.0, 0.4) > 0, "f_0^2 unexpectedly asymptotically free"

log("")
log("ALL CHECKS PASS. Stage 1 beta-function structure assembled and self-consistent.")
log("HEADLINE for Stage 2: pure-gravity f_2^2 is ASYMPTOTICALLY FREE (b_2=133/10>0), and the RS field")
log("at its standard anchor (+17/12) DEEPENS that AF -> the Gaussian (0,0) is an AF UV fixed point")
log("candidate. Open for Stage 2: the f_0 conformal-mode non-AF, the ker-Gamma value of c_RS_weyl, and")
log("the critical-surface dimension (predictivity). Solidity: pure-gravity betas KNOWN/ported; RS shift")
log("ESTIMATED (anchored, not pinned); d_RS_R2 a GUESS. No positivity claim (out of scope).")
raise SystemExit(0)
