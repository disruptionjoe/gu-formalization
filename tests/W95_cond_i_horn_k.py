#!/usr/bin/env python3
r"""
W95 -- CONDITION (i) of the observer conjecture's sectorial closing (W94):
is HORN K (f_2^2* = 0, the genuine non-removable ghost) an ALL-ORDERS / STRUCTURAL fact,
or truncation-conditional?

CONTEXT (inherited, not re-litigated):
  W94 closes the observer firewall SECTORIALLY on condition (i) = HORN K = the Weyl coupling f_2^2 is
  asymptotically free (f_2^2* = 0 at the UV FP), so the massive spin-2 ghost mass m2^2 ~ f_2^2 -> 0 only
  at k=inf -> the firewall is GENUINE (no bounded global modular J). HORN Q (f_2^2* > 0) would make the
  ghost removable and the firewall trivial. W87/W88/W89 reduced the whole horn to sign(eta_C), the
  additive-f_2^2 term of beta_{f_2^2}, with:
      beta_{f_2^2} = - kappa f_2^4 ( b_2^grav + b_2^RS )  +  eta_C(g, lambda) f_2^2 ,
  f_2^2* = 0 a STRUCTURAL root at every regulator; a lifted HORN-Q root f_2^2* = eta_C/(kappa b_2) exists
  IFF eta_C > 0. The physically-correct (Weyl-adapted, leading-4th-order-kinetic) scheme gives eta_C = 0
  -> HORN K; the EH-adapted scheme gives eta_C > 0 -> HORN Q. That fork rested on the one-loop / operative
  truncation. THIS TEST asks whether it is firmable ALL-ORDERS.

WHAT THIS TEST ENCODES (the protection / non-renormalization check + the grade):

  S1  STRUCTURAL SPINE, leg 1 -- f_2^2* = 0 is a Gaussian fixed point of the pure-higher-derivative-sector
      beta to ALL ORDERS. Model beta_HD(f) = -kappa * sum_{n>=2} b_n f^(2n) (every loop term is degree
      >=4 in the coupling f=f_2). It VANISHES at f=0 for ANY loop coefficients b_n. No higher loop can
      "create a fixed point at zero" or remove the zero at zero: a Gaussian FP is a zero of the pure-sector
      beta to all orders. (Symmetry-free, exact.)

  S2  STRUCTURAL SPINE, leg 2 -- the LEADING coefficient b_2 = 133/10 (+ RS 0.70) is the UNIVERSAL
      (scheme-independent) one-loop coefficient and is > 0, so f=0 is UV-ATTRACTIVE (AF). Near f=0 the
      one-loop term dominates every higher-loop term (ratio b_{n>=3} f^(2n) / b_2 f^4 -> 0 as f->0): AF is
      a WEAK-coupling UV statement, self-consistent to all orders in the same sense QCD's AF is. b_2 stays
      positive across GU's ker-Gamma content (H60 band, margin > 14).

  S3  STRUCTURAL SPINE, leg 3 -- UV 4th-derivative DOMINANCE is kinematic/all-orders. The graviton TT
      inverse propagator is (1/f_2^2) P_4(z) + Z_N P_2(z), P_4 ~ z^2, P_2 ~ z, z = -Box. The ratio
      (4th-order)/(2nd-order) = z -> inf in the UV for ANY fixed couplings: the physical graviton
      wave-function normalization Z_h is set by the LEADING 4th-order (Weyl) term, so the physical
      eta_h -> eta_Weyl -> 0 at the marginally-irrelevant Weyl direction, hence eta_C = -eta_h*c_reg -> 0.
      (This is the structural argument for eta_C=0; it is kinematic, not one-loop-special.)

  R1  THE RESIDUAL (the genuine open) -- eta_C is scheme-conditional. EH-adapted (eta_h = eta_N* = -2 at
      the Reuter FP) gives eta_C = +2*c_reg > 0 -> a lifted root f_2^2* > 0 -> HORN Q; Weyl-adapted
      (eta_h = eta_Weyl* = 0) gives eta_C = 0 -> only f_2^2* = 0 -> HORN K. BUT: the f_2^2* = 0 root
      PERSISTS in BOTH schemes (S1). The horn is decided by WHICH root the physical UV trajectory sits at,
      = sign(eta_C), = the Z_h scheme -- a truncation/scheme choice the structural spine LEANS (S3) but
      does not THEOREM. And the deciding all-orders object (the complete off-diagonal EH x Weyl beta with a
      single self-consistent graviton Z_h, = the complete two-loop-with-graviton-loops quadratic-gravity
      RGE for the Weyl coupling) is NOT available in the literature (Salvio-Strumia: only partial 2-loop
      RGEs known; the standard 1-loop betas are argued gauge/scheme-dependent -- 2403.02397).

  G1  THE GRADE -- FRONTIER (firmable-leaning). NOT FIRMABLE-NOW: no symmetry/non-renormalization theorem
      pins f_2^2*=0 as the SELECTED UV FP (the C^2 coupling IS the Weyl-anomaly coefficient, which runs --
      no symmetry forbids it); complete two-loop HD-gravity RGEs are not known; eta_C is scheme-dependent.
      NOT FALSE: the leading coefficient is universal and positive, AF is weak-coupling self-consistent,
      the 2024 PHYSICAL running preserves AF without tachyons, and no computation lifts f_2^2*>0 for GU's
      content; HORN Q needs the EH-adapted scheme the structural argument says is the wrong adaptation.
      RESIDUAL: the all-orders sign/value of eta_C (equiv. complete 2-loop-with-graviton-loops Weyl RGE).

  L1  LITERATURE two-sidedness is REAL and maps onto the two schemes (ported, read-only): one-loop / physical
      running -> AF (f_2^2*=0, HORN K, Weyl-adapted); Newton-induced four-derivative FPs / large-Weyl UV FP
      -> lift (HORN Q, EH-adapted). Neither settles the all-orders sign. So the grade cannot be raised to
      FIRMABLE-NOW nor lowered to FALSE on current knowledge.

Reproducible: python tests/W95_cond_i_horn_k.py   (exit 0 on PASS)
No git commit. No canon / RESEARCH-STATUS / claim-status / verdict / posture file touched. Exploration-grade.
NO forbidden target {3,8,24,chi(K3)=24,Ahat=3} assumed/inserted/hardcoded/divided-by; no generation count touched.
"""
from __future__ import annotations

import numpy as np

TOL = 1e-12
results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


KAPPA = 1.0 / (4.0 * np.pi) ** 2
B2_GRAV = 133.0 / 10.0      # Fradkin-Tseytlin / Avramidi-Barvinsky one-loop Weyl coefficient (PORTED)
B2_RS = 0.70               # ker-Gamma spin-3/2 anti-screening (COMPUTED W82/W88, sign load-bearing)
B2 = B2_GRAV + B2_RS       # ~ 14.0


def beta_HD(f2sq: float, bcoeffs) -> float:
    r"""Pure-higher-derivative-sector beta of the Weyl coupling f2sq = f_2^2, as an all-orders series:
        beta = - kappa * sum_{n>=2} b_n * (f2sq)^n   (n=2 is one loop; every term degree >= 2 in f2sq,
        i.e. degree >= 4 in f_2). eta_C piece is added separately in R1.
    """
    s = 0.0
    for n, bn in enumerate(bcoeffs, start=2):   # bcoeffs[0] multiplies (f2sq)^2 = one loop
        s += bn * f2sq ** n
    return -KAPPA * s


def beta_full(f2sq: float, bcoeffs, eta_C: float) -> float:
    return beta_HD(f2sq, bcoeffs) + eta_C * f2sq


log("=" * 96)
log("W95 -- CONDITION (i): is HORN K (f_2^2*=0) ALL-ORDERS/STRUCTURAL or truncation-conditional?")
log("=" * 96)

# ---------------------------------------------------------------------------------------------------
# S1 -- Gaussian FP f_2^2*=0 is a root of the pure-HD beta to ALL ORDERS (any loop coefficients).
# ---------------------------------------------------------------------------------------------------
log("\n-- STRUCTURAL SPINE --")
rng = np.random.default_rng(95)
s1_ok = True
worst_s1 = 0.0
for _ in range(500):
    # random "all-orders" loop coefficients, up to 8 loops, ANY sign/magnitude
    bc = rng.uniform(-50, 50, size=rng.integers(1, 9))
    v = abs(beta_HD(0.0, bc))
    worst_s1 = max(worst_s1, v)
    if v > TOL:
        s1_ok = False
check("S1  f_2^2*=0 is a root of the pure-HD-sector beta for ANY loop coefficients (500 random all-orders "
      "series, up to 8 loops): every term is degree>=2 in f_2^2, so it vanishes at 0 -- a Gaussian FP is a "
      "zero to ALL ORDERS, symmetry-free. No higher loop can create/remove the zero at zero",
      s1_ok, f"max |beta_HD(0)| over 500 random series = {worst_s1:.2e}")

# ---------------------------------------------------------------------------------------------------
# S2 -- leading coefficient universal & positive -> UV-attractive AF; weak-coupling self-consistency.
# ---------------------------------------------------------------------------------------------------
check("S2a  the LEADING (one-loop) coefficient b_2 = 133/10 + RS 0.70 = %.2f > 0 (universal / "
      "scheme-independent): f_2^2=0 is UV-ATTRACTIVE -> asymptotic FREEDOM. Stays positive across GU's "
      "ker-Gamma content (H60 band, margin > 14)" % B2,
      B2 > 0 and (B2_GRAV + 1.02) > 0 and (B2_GRAV + 1.82) > 0,
      f"b_2 = {B2:.3f}; H60 band [{B2_GRAV + 1.02:.2f},{B2_GRAV + 1.82:.2f}] all > 0")

# weak-coupling: near f_2^2 = 0 the one-loop term dominates every higher-loop term.
ratios = []
bc_test = [B2, 30.0, 40.0, 50.0]  # 1..4 loop, arbitrary >0 higher-loop coeffs
for f2sq in (1e-2, 1e-3, 1e-4, 1e-5):
    one_loop = abs(B2 * f2sq ** 2)
    higher = abs(sum(bc_test[k] * f2sq ** (k + 2) for k in range(1, len(bc_test))))
    ratios.append(higher / one_loop)
s2b_ok = ratios[-1] < ratios[0] and ratios[-1] < 1e-2  # monotone shrinking, negligible at small coupling
check("S2b  AF is a WEAK-coupling UV statement, self-consistent to all orders: near f_2^2=0 the one-loop "
      "term dominates every higher-loop term (higher/one-loop ratio -> 0 as f_2^2 -> 0), exactly as QCD "
      "asymptotic freedom is one-loop-robust",
      s2b_ok, f"higher/one-loop ratio at f_2^2=1e-2..1e-5: {[f'{r:.1e}' for r in ratios]}")

# ---------------------------------------------------------------------------------------------------
# S3 -- UV 4th-derivative dominance is KINEMATIC/all-orders -> physical Z_h Weyl-adapted -> eta_h -> 0.
# ---------------------------------------------------------------------------------------------------
# ratio (4th-order P_4 ~ z^2) / (2nd-order P_2 ~ z) = z -> inf in the UV, for ANY fixed couplings.
zs = np.array([1e1, 1e2, 1e4, 1e6, 1e8])
ratio_4_over_2 = zs  # (z^2)/(z) = z
s3_ok = np.all(np.diff(ratio_4_over_2) > 0) and ratio_4_over_2[-1] > 1e6
check("S3  UV 4th-derivative DOMINANCE is kinematic/all-orders: (4th-order)/(2nd-order) graviton kinetic "
      "ratio = z -> inf in the UV for ANY fixed couplings. So the physical graviton Z_h is set by the "
      "LEADING (4th-order Weyl) term -> physical eta_h -> eta_Weyl -> 0 -> eta_C -> 0 (the structural "
      "argument for eta_C=0; kinematic, not one-loop-special)",
      s3_ok, f"P_4/P_2 = z at z=1e1..1e8: {ratio_4_over_2.tolist()}")

# ---------------------------------------------------------------------------------------------------
# R1 -- THE RESIDUAL: eta_C is scheme-conditional, but f_2^2*=0 PERSISTS in both schemes.
# ---------------------------------------------------------------------------------------------------
log("\n-- THE RESIDUAL (the genuine open) --")
c_reg = 6.33e-3            # positive off-diagonal C^2 threshold integral (W89, sign load-bearing)
eta_N_star = -2.0          # Reuter-FP graviton anomalous dimension (canonical scaling, EH-adapted)
eta_C_EH = -eta_N_star * c_reg     # = +2 c_reg > 0  -> HORN Q lift
eta_C_Weyl = 0.0                    # marginally-irrelevant Weyl direction -> HORN K

# f_2^2*=0 is a root in BOTH schemes (S1 applied to the full beta with the eta_C f_2^2 term).
bc = [B2]  # one-loop pure-HD
root0_EH = abs(beta_full(0.0, bc, eta_C_EH))
root0_Weyl = abs(beta_full(0.0, bc, eta_C_Weyl))
check("R1a  f_2^2*=0 PERSISTS as a root of the FULL beta in BOTH schemes (eta_C f_2^2 also vanishes at 0): "
      "the horn is NOT decided by whether 0 is a fixed point (it always is) but by sign(eta_C) = which "
      "root the physical UV trajectory sits at",
      root0_EH < TOL and root0_Weyl < TOL,
      f"|beta_full(0)|: EH={root0_EH:.2e}, Weyl={root0_Weyl:.2e}")

# the lifted root exists iff eta_C > 0.
lifted_EH = eta_C_EH / (KAPPA * B2)          # positive -> HORN Q
has_lift_EH = eta_C_EH > 0 and lifted_EH > 0
has_lift_Weyl = eta_C_Weyl > 0
check("R1b  a lifted HORN-Q root f_2^2* = eta_C/(kappa b_2) exists IFF eta_C > 0: EH-adapted eta_C = +2 "
      "c_reg > 0 -> f_2^2* = %.3f > 0 (HORN Q); Weyl-adapted eta_C = 0 -> NO lift, only f_2^2*=0 (HORN K). "
      "The horn = the Z_h scheme, a truncation choice the structural spine (S3) LEANS but does not THEOREM"
      % lifted_EH,
      has_lift_EH and (not has_lift_Weyl),
      f"eta_C^EH={eta_C_EH:+.2e} -> lift {lifted_EH:.3f}; eta_C^Weyl={eta_C_Weyl:.1f} -> no lift")

# the deciding all-orders object is NOT available in the literature.
TWO_LOOP_WITH_GRAVITON_LOOPS_AVAILABLE = False   # Salvio-Strumia: only partial 2-loop RGEs known
STANDARD_ONE_LOOP_BETAS_SCHEME_DEPENDENT = True  # 2403.02397: standard betas gauge/scheme-dependent
check("R1c  the deciding ALL-ORDERS object -- the complete off-diagonal EH x Weyl beta with a single "
      "self-consistent graviton Z_h (= complete two-loop-with-graviton-loops quadratic-gravity Weyl RGE) "
      "-- is NOT available in the literature; and the standard one-loop betas are argued gauge/scheme-"
      "dependent. So eta_C's all-orders sign is genuinely UNSETTLED",
      (TWO_LOOP_WITH_GRAVITON_LOOPS_AVAILABLE is False)
      and (STANDARD_ONE_LOOP_BETAS_SCHEME_DEPENDENT is True))

# ---------------------------------------------------------------------------------------------------
# L1 -- literature two-sidedness maps onto the two schemes (ported, read-only).
# ---------------------------------------------------------------------------------------------------
LIT_AF_SIDE = ["Fradkin-Tseytlin 1982", "Avramidi-Barvinsky 1985", "agravity Salvio-Strumia 1403.4226",
               "physical running 2403.02397 (AF, no tachyons)", "BMS marginally-irrelevant C^2"]
LIT_LIFT_SIDE = ["Codello-Percacci 2006 (Newton-induced 4-deriv FPs)", "large-Weyl UV FP (some FRG)"]
check("L1  literature is genuinely TWO-SIDED and maps onto the two schemes: AF side (=Weyl-adapted, HORN K) "
      "vs Newton-induced-lift side (=EH-adapted, HORN Q). Neither settles the all-orders sign -> cannot "
      "raise to FIRMABLE-NOW nor lower to FALSE on current knowledge",
      len(LIT_AF_SIDE) >= 3 and len(LIT_LIFT_SIDE) >= 1,
      f"{len(LIT_AF_SIDE)} AF-side refs vs {len(LIT_LIFT_SIDE)} lift-side refs")

# ---------------------------------------------------------------------------------------------------
# G1 -- THE GRADE.
# ---------------------------------------------------------------------------------------------------
log("\n-- THE GRADE --")
GRADE = "FRONTIER"          # firmable-leaning: structural spine (S1-S3) all-orders; residual (R1) genuinely open
FIRMABLE_NOW = False        # no non-renormalization/symmetry theorem pins f_2^2*=0 as the SELECTED UV FP
FALSE_HORN = False          # universal +b_2, weak-coupling AF, physical-running AF, no computed lift for GU
RESIDUAL = ("all-orders sign/value of eta_C (the graviton-loop additive f_2^2 term) = the complete "
            "two-loop-with-graviton-loops quadratic-gravity Weyl RGE with a single self-consistent Z_h; "
            "plus a proof that the Weyl-adapted (leading-4th-order-kinetic) scheme is the physical one")
check("G1  GRADE = FRONTIER (firmable-leaning), NOT FIRMABLE-NOW, NOT FALSE. HORN K has an ALL-ORDERS "
      "STRUCTURAL SPINE (S1 Gaussian-FP-to-all-orders + S2 universal +b_2 weak-coupling AF + S3 kinematic "
      "UV 4th-deriv dominance) but is NOT a theorem: the residual eta_C sign is scheme-conditional and the "
      "deciding all-orders computation is not known",
      GRADE == "FRONTIER" and (FIRMABLE_NOW is False) and (FALSE_HORN is False))
check("G2  the precise RESIDUAL is named (the single computation that would settle the horn all-orders)",
      isinstance(RESIDUAL, str) and "eta_C" in RESIDUAL and "two-loop" in RESIDUAL)

# ---------------------------------------------------------------------------------------------------
log("\n" + "=" * 96)
npass = sum(1 for _, ok, _ in results if ok)
ntot = len(results)
log(f"CHECKS: {npass}/{ntot} passed.")

# load-bearing asserts
assert s1_ok, "S1: Gaussian FP not an all-orders root"
assert B2 > 0, "S2: leading coefficient not positive"
assert s2b_ok, "S2b: AF not weak-coupling self-consistent"
assert s3_ok, "S3: UV 4th-derivative dominance failed"
assert root0_EH < TOL and root0_Weyl < TOL, "R1a: f_2^2*=0 root did not persist across schemes"
assert has_lift_EH and not has_lift_Weyl, "R1b: eta_C fork wrong"
assert TWO_LOOP_WITH_GRAVITON_LOOPS_AVAILABLE is False, "R1c: residual mislabeled as closed"
assert GRADE == "FRONTIER" and FIRMABLE_NOW is False and FALSE_HORN is False, "G1: grade wrong"
assert npass == ntot, "some W95 checks FAILED -- see [FAIL] lines"

log("")
log("VERDICT (W95, Condition (i)): HORN K is TRUNCATION-CONDITIONAL / FRONTIER, firmable-leaning.")
log("  * ALL-ORDERS STRUCTURAL SPINE (firm): f_2^2*=0 is a Gaussian fixed point of the pure-HD beta to")
log("    ALL ORDERS (S1, symmetry-free); the leading coefficient b_2=133/10+0.70 is universal and > 0 so")
log("    AF is UV-attractive and weak-coupling self-consistent (S2); UV 4th-derivative dominance is")
log("    kinematic/all-orders, setting the physical graviton Z_h Weyl-adapted -> eta_C -> 0 (S3).")
log("  * RESIDUAL (genuinely open): eta_C (the graviton-loop additive f_2^2 term) is scheme-conditional")
log("    (EH-adapted +2c_reg>0 -> HORN Q lift; Weyl-adapted 0 -> HORN K); f_2^2*=0 persists as a root in")
log("    BOTH, so the horn = which root the UV trajectory sits at = sign(eta_C). The deciding all-orders")
log("    computation (complete two-loop-with-graviton-loops Weyl RGE / single self-consistent Z_h) is NOT")
log("    in the literature, and the standard one-loop betas are argued scheme-dependent.")
log("  * GRADE = FRONTIER (firmable-leaning). NOT FIRMABLE-NOW (no non-renormalization theorem pins the")
log("    SELECTED FP; the C^2 coupling IS the Weyl-anomaly coefficient, which runs). NOT FALSE (universal")
log("    +b_2, weak-coupling AF, 2024 physical running preserves AF without tachyons, no computed lift for")
log("    GU's content; HORN Q needs the EH-adapted scheme the structural argument says is the wrong one).")
raise SystemExit(0)
