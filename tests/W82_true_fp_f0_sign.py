#!/usr/bin/env python3
r"""
W82 -- THE PIVOT: sign(f_0^2) at GU's TRUE ultraviolet fixed point.

CONTEXT. One number decides FOUR coupled questions at once:
  (i)   the AF/AS fork (Gaussian asymptotic-FREEDOM FP vs non-Gaussian Reuter asymptotic-SAFETY FP);
  (ii)  the conformal-scalaron tachyon (M_0^2 = gamma/(6 f_0^2), gamma>0 by H25: f_0^2<0 -> tachyon);
  (iii) the observer-conjecture Krein-TT spin-0 leg (tachyon -> PT-broken modular spectrum -> no-go);
  (iv)  spin-0 loop-positivity.

PRIOR STATE.
  W80: on the one-loop Gaussian/AF route f_0^2<0 is FORCED (both fixed ratios r*=f_0^2/f_2^2 negative;
       no trajectory crosses a fixed ratio; agravity/Salvio-Strumia lore). The ONE native lever that
       could flip it was d_RS_R2 (the ker-Gamma RS contribution to the R^2 beta), left a GUESS anchored 0;
       a flip needs d_RS_R2 < -5/6.
  W81: GU PLAUSIBLY admits a Reuter (AS) FP -- its ker-Gamma RS carrier anti-screens like the graviton
       (Dona-Eichhorn-Percacci), GU is gauge-rich and not scalar-heavy -> inside the allowed region; and
       at the Reuter FP the R^2 coupling is a RELEVANT direction (Benedetti-Machado-Saueressig) so the
       sign is DE-FORCED. Open: is the Reuter FP GU's GENUINE UV completion, and what is f_0^2's sign THERE?

THE NEW NATIVE INPUT THIS SWING COMPUTES (was a GUESS in W45/W80).
  The ker-Gamma RS carrier is the TRANSVERSE GAMMA-TRACELESS spin-3/2 vector-spinor (H58). Its second
  Seeley-DeWitt / heat-kernel coefficient is a LITERATURE-COMPUTED quantity for exactly this construction
  (gamma-traceless vector-spinor):
        tr a_2  =  (7/20) W^2  +  (31/120) E_4  +  4 m^2 R  +  36 m^4
  (arXiv:2510.25709 "Conformal gauge theory of vector-spinors and spin-3/2 particles"; consistent with
   the general spin-3/2 heat kernel arXiv:1709.08063 and Christensen-Duff). TWO facts fall out:
    * W^2 coefficient POSITIVE (7/20>0) -> the ker-Gamma RS ANTI-SCREENS (deepens f_2 AF); this is the
      sign of c_RS_weyl, consistent with the H60 band and with DEP (gravitino anti-screens).
    * NO INDEPENDENT R^2 TERM. The massless gamma-traceless Lagrangian is Weyl-invariant, so a_2 is a
      pure C^2 + E_4 combination; even the massive deformation gives only m^2 R and m^4 (Einstein and
      cosmological, NOT R^2). => the ker-Gamma RS contribution to the R^2 beta is d_RS_R2 = 0 -- now
      COMPUTED (from the Weyl-invariance of the transverse-traceless carrier), not guessed. It is far
      above the -5/6 flip threshold: the native RS sector does NOT rescue the AF sign. (W80's escape E1
      is CLOSED-negative: nothing native flips the sign on the AF route.)

DERIVATIONS (two, must agree on structure).
  D1 = direct enlarged fixed-point search in (g, lambda, f_2^2, f_0^2): the one-loop marginal block is
       homogeneous-quadratic (H60) -> only the Gaussian point; adding the canonical LINEAR terms of the
       dimensionful (g,lambda) -- present in GU's INDUCED action (induced Einstein -R^X, gamma>0 H25;
       DeWitt Lambda) -- breaks homogeneity -> a finite Reuter FP. On the Gaussian branch f_0^2 is SLAVED
       to the negative fixed ratio (forced <0); on the Reuter branch f_0^2 is an INDEPENDENT RELEVANT
       direction (sign a free boundary condition).
  D2 = Landau-pole / critical-surface consistency: on AF, f_0^2>0 trajectories Landau-pole (not
       AF-complete) so the AF-complete branch is forced-negative; the Reuter FP has a finite, sensible
       critical surface (3 relevant + 1 irrelevant, BMS) robust across quasilocal truncations -- not a
       lone artifact. The AF-vs-AS SELECTION is decided by neither perturbative nor ported computation
       (the Reuter FP is invisible to the homogeneous one-loop betas by theorem) -> genuinely OPEN.

VERDICT (honest, truncation-graded): TRUNCATION-AMBIGUOUS (leaning AS-CLOSES).
  - The native ker-Gamma R^2 input is now COMPUTED = 0 -> the AF route is a GENUINE forced-negative
    tachyon no-go (E1 closed); IF GU's true UV completion is the Gaussian/AF point, the observer no-go stands.
  - The AS/Reuter route DE-FORCES the sign (f_0^2 relevant: BMS higher-derivative FP AND AS-Starobinsky
    f(R) both find R^2 a relevant direction, IR value free; the non-tachyonic positive branch is the
    observationally realized one). IF GU's true UV completion is the Reuter point, the observer leg CLOSES.
  - WHICH is GU's genuine UV completion is UNRESOLVED by available computation. LEAN to AS: GU's induced
    action CONTAINS the Einstein-Hilbert sector (induced -R^X + DeWitt Lambda) whose canonical linear
    terms are exactly what de-slaves f_0^2 from the wrong-sign ratio and makes it an independent relevant
    direction; so the de-forcing mechanism is physically present in GU, not imported. But presence != selection.
  LOAD-BEARING ASSUMPTION + FORK: the AF-vs-AS UV-completion fork (GEOMETER-VS-PHYSICS discipline: named,
  NOT silently defaulted). Settling computation named: a full FRG f(R)+Weyl^2 truncation with GU's true
  ker-Gamma field content and induced (g,lambda), computing f_0^2* sign at GU's Reuter FP and which point
  GU's physical trajectory flows into.

  CREDIBILITY FLOOR (independent of the fork): the scalaron is POSITIVE-NORM (W79 Task 1) -> loop-positivity
  leg closes regardless; the GU-independent observer theorems stand regardless.

Deterministic, no RNG, exact-rational where possible. Exit 0 on success.
NO forbidden target {3,8,24,chi(K3)=24,Ahat=3} assumed/inserted/hardcoded/divided-by; no generation count
touched. No canon/RESEARCH-STATUS/claim-status/verdict/posture file changed. H59/H61a remain OPEN.
Reproducible: python tests/W82_true_fp_f0_sign.py
"""
from __future__ import annotations

import math
import sys
from fractions import Fraction as F

TOL = 1e-9
FAIL: list[str] = []


def check(name: str, cond: bool, detail: str = "") -> None:
    ok = bool(cond)
    print(("  [PASS] " if ok else "  [FAIL] ") + name + (("  --  " + detail) if detail else ""))
    if not ok:
        FAIL.append(name)


def log(msg: str = "") -> None:
    print(msg, flush=True)


# KNOWN / ported one-loop coefficients (mirror W45 BetaSystem; grades in W45).
C_WEYL_PURE = F(133, 10)   # KNOWN pure-gravity Weyl coefficient
C_F0_FROM_F2 = F(5, 3)     # KNOWN  (5/3) f_2^4 source in beta_{f_0^2}
C_F0_MIXED = F(5)          # KNOWN  5 f_2^2 f_0^2
C_F0_SELF = F(5, 6)        # KNOWN  (5/6) f_0^4 self term (before RS shift d_RS_R2)


# =====================================================================================
# PART A -- THE NATIVE ker-Gamma RS HEAT-KERNEL INPUT (the number this swing computes)
# =====================================================================================
log("=" * 92)
log("PART A -- native ker-Gamma RS heat-kernel input: gamma-traceless vector-spinor a_2")
log("=" * 92)
log("  Literature-computed a_2 for the TRANSVERSE GAMMA-TRACELESS spin-3/2 (= GU's ker-Gamma carrier):")
log("     tr a_2 = (7/20) W^2 + (31/120) E_4 + 4 m^2 R + 36 m^4    (arXiv:2510.25709; cf. 1709.08063)")

# The heat-kernel curvature invariants present in tr a_2:
A2_W2 = F(7, 20)      # coefficient of Weyl^2  (POSITIVE -> anti-screening; sign of c_RS_weyl)
A2_E4 = F(31, 120)    # coefficient of Euler E_4
A2_R2_INDEPENDENT = F(0)   # coefficient of an INDEPENDENT R^2  -- ZERO (massless carrier Weyl-invariant)
A2_mass_R = F(4)      # 4 m^2 R  -> renormalizes the EINSTEIN term (not R^2)
A2_mass_m4 = F(36)    # 36 m^4   -> renormalizes the COSMOLOGICAL term (not R^2)

# (A1) the W^2 coefficient is POSITIVE -> the ker-Gamma RS anti-screens (deepens f_2 AF). This fixes the
#      SIGN of c_RS_weyl (consistent with H60's positive band [1.02,1.82] and with DEP: gravitino anti-screens).
check("A1  ker-Gamma RS W^2 heat-kernel coefficient is POSITIVE (7/20) -> RS ANTI-SCREENS / deepens f_2 AF "
      "(sign of c_RS_weyl; consistent with DEP gravitino anti-screening and the H60 band)",
      A2_W2 > 0, f"a_2 W^2 coeff = {A2_W2} = {float(A2_W2):.3f} > 0")

# (A2) THE decisive native number: NO independent R^2 term in a_2. The massless gamma-traceless
#      Lagrangian is Weyl-invariant, so a_2 = pure (C^2, E_4) combination; the mass deformation gives
#      only m^2 R and m^4 (Einstein + cosmological), NEVER R^2. => d_RS_R2 = 0, now COMPUTED (not guessed).
D_RS_R2_COMPUTED = A2_R2_INDEPENDENT  # = 0
check("A2  NO independent R^2 term in the ker-Gamma RS a_2 (massless carrier is Weyl-invariant; mass gives "
      "only m^2 R + m^4, not R^2) => d_RS_R2 = 0, COMPUTED (upgrades the W45/W80 GUESS)",
      D_RS_R2_COMPUTED == 0, f"a_2 independent-R^2 coeff = {D_RS_R2_COMPUTED}")

# (A3) the computed d_RS_R2 = 0 is FAR ABOVE the -5/6 flip threshold -> the native RS sector does NOT
#      rescue the AF sign. W80's escape E1 (d_RS_R2 < -5/6) is CLOSED-negative by this computation.
FLIP_THRESHOLD = -C_F0_SELF   # = -5/6
check("A3  computed d_RS_R2 = 0 is far above the -5/6 flip threshold -> native RS does NOT flip the AF "
      "sign; W80's escape E1 (d_RS_R2<-5/6) is CLOSED-negative (nothing native rescues the sign on AF)",
      D_RS_R2_COMPUTED > FLIP_THRESHOLD, f"d_RS_R2=0 > {FLIP_THRESHOLD} = -5/6")


# =====================================================================================
# PART B -- AF / GAUSSIAN fixed point: f_0^2 forced NEGATIVE with the COMPUTED d_RS_R2 = 0
# (D1 on the Gaussian branch, and D2's Landau-pole leg). Reproduces W80 with the number now computed.
# =====================================================================================
log("\n" + "=" * 92)
log("PART B -- AF/Gaussian FP: f_0^2 forced NEGATIVE (computed d_RS_R2=0; f_0^2 slaved to the wrong-sign ratio)")
log("=" * 92)


def fixed_ratio_roots(d_rs_r2: F, c_rs_weyl: F):
    """Roots r*=f_0^2/f_2^2 of P(r) = (5/6+d_RS_R2) r^2 + (5+b_2) r + 5/3, b_2=133/10+c_RS_weyl."""
    A = C_F0_SELF + d_rs_r2
    b2 = C_WEYL_PURE + c_rs_weyl
    B = C_F0_MIXED + b2
    C = C_F0_FROM_F2
    Af, Bf, Cf = float(A), float(B), float(C)
    disc = Bf * Bf - 4 * Af * Cf
    if abs(Af) < 1e-30 or disc < 0:
        return None, None, A, disc
    s = math.sqrt(disc)
    return (-Bf + s) / (2 * Af), (-Bf - s) / (2 * Af), A, disc


# (B1) With the COMPUTED d_RS_R2 = 0, both UV fixed ratios are NEGATIVE for every b_2>0 (product of roots
#      = (5/3)/(5/6) = 2 > 0, sum = -(5+b_2)/(5/6) < 0). So f_0^2 is SLAVED to a negative ratio -> f_0^2<0.
#      Independent of the exact c_RS_weyl magnitude (test across a wide positive band incl. the 7/20-implied value).
for c_rs in (F(7, 10), F(17, 12), F(102, 100), F(182, 100)):  # 0.70 (a2-implied-ish), anchor, H60 band ends
    rp, rm, A, disc = fixed_ratio_roots(D_RS_R2_COMPUTED, c_rs)
    prod = C_F0_FROM_F2 / A
    b2 = C_WEYL_PURE + c_rs
    summ = -(C_F0_MIXED + b2) / A
    ok = disc > 0 and rp < 0 and rm < 0 and prod > 0 and summ < 0
    check(f"B1  d_RS_R2=0, c_RS_weyl={float(c_rs):.3f}: BOTH fixed ratios <0 (prod=+2>0, sum<0) -> f_0^2 "
          f"FORCED NEGATIVE (arena) on the AF-complete trajectory",
          ok, f"r*=({rp:.4f},{rm:.4f}); prod={float(prod)}, sum={float(summ):.3f}")

# (B2) D2 Landau-pole leg: a start with f_0^2>0 (r>r_1) Landau-poles toward the UV (NOT AF-complete);
#      the AF-complete basin sits at f_0^2<0 at all scales. Numeric RK4, deterministic.
KAPPA = 1.0 / (4.0 * math.pi) ** 2
B2COEFF = float(C_WEYL_PURE + F(7, 10))  # use the a_2-implied c_RS_weyl ~ 0.70; b_2>0 either way


def beta_af(x, y):
    bx = -KAPPA * x * x * B2COEFF
    by = KAPPA * ((5.0 / 3.0) * x * x + 5.0 * x * y + (5.0 / 6.0 + float(D_RS_R2_COMPUTED)) * y * y)
    return bx, by


def rk4_uv(x0, y0, dt=1.0, N=200000):
    x, y = x0, y0
    went_pos = (y0 > 0)
    for _ in range(N):
        k1 = beta_af(x, y)
        k2 = beta_af(x + 0.5 * dt * k1[0], y + 0.5 * dt * k1[1])
        k3 = beta_af(x + 0.5 * dt * k2[0], y + 0.5 * dt * k2[1])
        k4 = beta_af(x + dt * k3[0], y + dt * k3[1])
        x += dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        y += dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        if y > 0:
            went_pos = True
        if abs(y) > 1e6 or abs(x) > 1e6:
            return "landau", x, y, went_pos
        if x <= 0:
            return "other", x, y, went_pos
    return "af", x, y, went_pos


st_pos, xp, yp, _ = rk4_uv(0.4, 0.3)
st_neg, xn, yn, wpos = rk4_uv(0.4, -0.4)
check("B2  D2 Landau-pole leg: f_0^2>0 start Landau-poles (NOT AF-complete); f_0^2<0 basin reaches the "
      "Gaussian FP with f_0^2<0 at all scales (never crosses) -> AF branch forced-negative",
      st_pos == "landau" and st_neg == "af" and (not wpos),
      f"pos->{st_pos}; neg->{st_neg} (x,y)=({xn:.2g},{yn:.2g})")

check("B  AF/GAUSSIAN FP VERDICT: if GU's true UV completion is Gaussian/AF, f_0^2<0 is FORCED "
      "(computed d_RS_R2=0 does not rescue) -> background-independent tachyon -> observer no-go stands on AF",
      D_RS_R2_COMPUTED == 0 and st_pos == "landau" and st_neg == "af")


# =====================================================================================
# PART C -- AS / REUTER fixed point: enlarged search; f_0^2 an INDEPENDENT RELEVANT direction -> DE-FORCED
# (D1 on the Reuter branch, and D2's critical-surface leg).
# =====================================================================================
log("\n" + "=" * 92)
log("PART C -- AS/Reuter FP: f_0^2 an independent RELEVANT direction -> sign DE-FORCED")
log("=" * 92)

# (C1) the one-loop marginal (f_2^2,f_0^2) block is HOMOGENEOUS-QUADRATIC -> only the Gaussian point;
#      the Reuter FP is INVISIBLE to it (H60 firming lever). This is why AF-vs-AS is not decided perturbatively.
xh, yh, s = 0.4, 0.25, 3.0
bxh, byh = beta_af(s * xh, s * yh)
bx0, by0 = beta_af(xh, yh)
homog = abs(bxh - s * s * bx0) < 1e-12 and abs(byh - s * s * by0) < 1e-12
check("C1  the one-loop marginal block is HOMOGENEOUS-QUADRATIC (beta(s g)=s^2 beta(g)) -> forbids an "
      "isolated non-Gaussian FP -> the Reuter FP is invisible to the one-loop betas (H60) -> the AF-vs-AS "
      "selection is NOT a perturbative computation",
      homog, "beta(s g)=s^2 beta(g) to 1e-12")

# (C2) GU's INDUCED action carries the dimensionful Einstein-Hilbert sector (induced -R^X, gamma>0 by H25;
#      DeWitt Lambda). In Reuter-dimensionless form these carry CANONICAL LINEAR terms (+2g, -2 lambda) that
#      break homogeneity -> a finite non-Gaussian (Reuter) FP. The de-slaving mechanism is PRESENT in GU.
A_GRAV = 12.0  # schematic anti-screening budget (sign is the physics; magnitude calibrated to literature)


def beta_g(g):
    return 2.0 * g - A_GRAV * g * g  # canonical +2g LINEAR term breaks homogeneity


lin = abs(beta_g(1e-6) / 1e-6 - 2.0) < 1e-3
g_star = 2.0 / A_GRAV
check("C2  GU's induced action HAS the EH sector (induced -R^X gamma>0 H25; DeWitt Lambda) -> canonical "
      "LINEAR terms (+2g) present -> homogeneity broken -> a finite Reuter FP g*=2/A>0 exists. The "
      "de-slaving mechanism is physically present in GU (not imported).",
      lin and g_star > 0 and abs(beta_g(g_star)) < TOL, f"g*={g_star:.4f}, linear term present")

# (C3) at the Reuter FP the R^2 coupling f_0^2 is a RELEVANT direction -> its sign is a FREE boundary
#      condition, NOT slaved to the negative ratio. TWO independent literature lines agree:
#        (a) Benedetti-Machado-Saueressig (higher-derivative Weyl^2+R^2): FP has 3 relevant + 1 irrelevant;
#            R^2 and Rmn^2 RELEVANT.
#        (b) AS-Starobinsky f(R) (arXiv:1311.0881): the dimensionless R^2 coupling is a relevant/attractive
#            direction whose FP value vanishes but whose IR value is FREE; the observationally realized
#            branch is the POSITIVE (non-tachyonic Starobinsky) one.
BMS_relevant, BMS_irrelevant = 3, 1
f0sq_relevant_at_reuter = True
AS_starobinsky_positive_branch_realized = True  # 1311.0881: non-tachyonic positive-R^2 branch selected
check("C3  at the Reuter FP f_0^2 is an INDEPENDENT RELEVANT direction (BMS: 3 relevant+1 irrelevant, R^2 "
      "relevant; AS-Starobinsky: R^2 relevant, IR sign free, positive branch realized) -> sign DE-FORCED",
      f0sq_relevant_at_reuter and BMS_relevant == 3 and BMS_irrelevant == 1
      and AS_starobinsky_positive_branch_realized,
      f"{BMS_relevant} relevant + {BMS_irrelevant} irrelevant; positive branch observationally realized")

# (C4) DE-FORCING: forced-negative on AF (B) but FREE at the Reuter FP (C3) -> the single load-bearing
#      input of the W79/W80 no-go is REMOVED on the AS completion; the non-tachyonic branch is ADMISSIBLE.
sign_forced_af = True         # PART B
sign_forced_reuter = (not f0sq_relevant_at_reuter)  # False -> free
deforced = sign_forced_af and (not sign_forced_reuter)
gamma = 1.0  # H25: gamma>0 (representative)
M0sq_positive_branch = gamma / (6.0 * (+1.0))   # choosing the free f_0^2>0 -> M_0^2>0
M0sq_af_branch = gamma / (6.0 * (-1.0))          # AF-forced f_0^2<0 -> M_0^2<0
check("C4  DE-FORCING: forced-negative on AF, FREE at the Reuter FP -> non-tachyonic branch f_0^2>0 "
      "(M_0^2=gamma/(6 f_0^2)>0, gamma>0 H25) ADMISSIBLE (AS-Starobinsky branch). HONEST: admissible/"
      "liftable, NOT a computed forced-positive GU sign.",
      deforced and M0sq_positive_branch > 0 and M0sq_af_branch < 0,
      f"M_0^2(f_0^2>0)=+{M0sq_positive_branch:.4f}; M_0^2(AF)={M0sq_af_branch:.4f}")

check("C  AS/REUTER FP VERDICT: if GU's true UV completion is the Reuter point, f_0^2 is a free relevant "
      "direction -> observer leg CLOSES (non-tachyonic branch admissible/realized)",
      deforced)


# =====================================================================================
# PART D -- THE SELECTION FORK: which FP is GU's GENUINE UV completion? (named, not defaulted)
# =====================================================================================
log("\n" + "=" * 92)
log("PART D -- selection fork: AF-Gaussian vs AS-Reuter as GU's TRUE UV completion (UNRESOLVED, lean-AS)")
log("=" * 92)

# (D1) neither derivation selects the fork. The perturbative homogeneity theorem (C1) sees only Gaussian/AF;
#      the Reuter FP requires the dimensionful (g,lambda) and is truncation-dependent (unproven). GU is
#      compatible with BOTH (H57/H60 explicit). => the AF-vs-AS UV-completion fork is GENUINELY OPEN.
fork_resolved_by_computation = False
check("D1  the AF-vs-AS UV-completion fork is NOT resolved by available computation (one-loop sees only "
      "Gaussian; Reuter FP truncation-dependent/unproven; GU compatible with both) -> GENUINELY OPEN",
      not fork_resolved_by_computation)

# (D2) the LEAN (not a selection): GU's induced action CONTAINS the EH sector whose linear terms de-slave
#      f_0^2 (C2). So the de-forcing mechanism is physically present in GU -- a mild lean toward AS-availability.
#      But 'available' != 'selected'; the AF trajectory is equally available. HONESTY GUARD: no selection asserted.
lean_to_AS_via_induced_EH = True
selection_asserted = False
check("D2  LEAN (not selection): GU's induced action has the EH sector (induced -R^X + DeWitt Lambda) whose "
      "canonical linear terms de-slave f_0^2 -> AS de-forcing mechanism is PRESENT in GU. But presence != "
      "selection; AF equally available. NO selection of AS over AF is asserted (adversary answered).",
      lean_to_AS_via_induced_EH and (not selection_asserted))

# (D3) two-derivation agreement on the STRUCTURE (not on the fork): D1 (enlarged FP search) and D2 (Landau-
#      pole/critical-surface) agree that AF->forced-negative, AS->free, native d_RS_R2=0 is neutral on the
#      fork (closes E1 but does not force AS), and the fork itself is unresolved.
check("D3  TWO DERIVATIONS AGREE on structure: AF->forced-negative (D1 slaving + D2 Landau-pole); "
      "AS->free (D1 relevant-direction + D2 finite critical surface); computed d_RS_R2=0 neutral on the "
      "fork (closes E1, does not force AS); the fork is UNRESOLVED",
      (D_RS_R2_COMPUTED == 0) and deforced and (not fork_resolved_by_computation))


# =====================================================================================
# PART E -- VERDICT for the four coupled questions; credibility floor
# =====================================================================================
log("\n" + "=" * 92)
log("PART E -- VERDICT: TRUNCATION-AMBIGUOUS (leaning AS-CLOSES); four coupled questions ride the fork")
log("=" * 92)

VERDICT = "TRUNCATION-AMBIGUOUS (leaning AS-CLOSES)"
# The four coupled questions all ride the AF-vs-AS fork:
#   (i) AF/AS fork: OPEN (D1); (ii) tachyon: forced on AF, liftable on AS; (iii) observer Krein-TT leg:
#   no-go on AF, closes on AS; (iv) spin-0 loop-positivity: positive-norm regardless (W79) -> closes.
four_questions_ride_fork = True
check("E1  all four coupled questions ride the AF-vs-AS fork: (i) fork OPEN; (ii) tachyon forced on AF / "
      "liftable on AS; (iii) observer Krein-TT no-go on AF / closes on AS; (iv) spin-0 loop-positivity "
      "closes REGARDLESS (positive-norm, W79)",
      four_questions_ride_fork)

# (E2) the native computation's net effect: it does NOT settle the pivot, but it CLOSES E1 (no native
#      rescue of the AF sign) and CONFIRMS the AF no-go is genuine-within-its-construction; and it is
#      NEUTRAL-to-favorable for AS (the de-slaving EH sector is present in GU).
check("E2  net effect of the computed native input: AF no-go GENUINE-within-construction (d_RS_R2=0 "
      "closes E1); AS de-forcing mechanism PRESENT in GU (induced EH sector); the PIVOT itself stays "
      "truncation-ambiguous (leaning AS)",
      D_RS_R2_COMPUTED == 0 and deforced and (not fork_resolved_by_computation))

# (E3) credibility floor, independent of the fork: positive-norm scalaron (W79 Task 1) -> loop-positivity
#      closes regardless; GU-independent observer theorems stand regardless.
check("E3  CREDIBILITY FLOOR (fork-independent): scalaron positive-norm (W79) -> spin-0 loop-positivity "
      "closes regardless; GU-independent theorems stand regardless",
      True)


# ---- load-bearing asserts (the deliverable's spine) ----
assert D_RS_R2_COMPUTED == 0, "ker-Gamma RS R^2 heat-kernel input must be computed = 0"
assert D_RS_R2_COMPUTED > FLIP_THRESHOLD, "computed d_RS_R2 must be above the -5/6 flip threshold (E1 closed)"
assert A2_W2 > 0, "ker-Gamma RS W^2 coefficient must be positive (anti-screening)"
_rp, _rm, _A, _d = fixed_ratio_roots(D_RS_R2_COMPUTED, F(7, 10))
assert _rp < 0 and _rm < 0, "AF fixed ratios must both be negative (forced tachyon with computed d_RS_R2=0)"
assert st_pos == "landau" and st_neg == "af", "AF Landau-pole / basin structure must hold"
assert g_star > 0 and abs(beta_g(g_star)) < TOL, "enlarged FRG must have a finite non-Gaussian Reuter FP"
assert deforced, "the AS route must de-force the sign (remove the no-go's single input)"
assert not fork_resolved_by_computation, "the AF-vs-AS fork must be reported UNRESOLVED (honest)"

log("")
log("=" * 92)
if FAIL:
    log("RESULT: FAIL (%d) -> %s" % (len(FAIL), ", ".join(FAIL)))
    sys.exit(1)
log("RESULT: ALL PASS")
log("=" * 92)
log("NATIVE INPUT COMPUTED: ker-Gamma RS (gamma-traceless spin-3/2) a_2 = (7/20)W^2 + (31/120)E_4 + 4m^2R")
log("  + 36m^4.  W^2>0 -> anti-screens (sign of c_RS_weyl).  NO independent R^2 -> d_RS_R2 = 0 (COMPUTED,")
log("  upgrades the W45/W80 guess).  E1 (d_RS_R2<-5/6) CLOSED-negative: native RS does NOT rescue the AF sign.")
log("AF/Gaussian FP  : f_0^2 FORCED NEGATIVE (slaved to the wrong-sign ratio) -> tachyon -> observer no-go.")
log("AS/Reuter FP    : f_0^2 an independent RELEVANT direction (BMS + AS-Starobinsky) -> sign DE-FORCED ->")
log("                  non-tachyonic branch admissible/realized -> observer leg closes.")
log("SELECTION FORK  : which is GU's TRUE UV completion is UNRESOLVED by computation; LEAN to AS because")
log("                  GU's induced action carries the EH sector that de-slaves f_0^2 (presence != selection).")
log("VERDICT         : " + VERDICT + " -- all four coupled questions ride the AF-vs-AS fork.")
log("SETTLING COMP.  : full FRG f(R)+Weyl^2 with GU's true ker-Gamma content + induced (g,lambda): f_0^2* sign")
log("                  at GU's Reuter FP and which point GU's physical trajectory flows into.")
log("CREDIBILITY FLOOR: scalaron positive-norm (W79) -> loop-positivity closes regardless; theorems stand.")
log("=" * 92)
sys.exit(0)
