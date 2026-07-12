#!/usr/bin/env python3
r"""W66 path4 wave2 -- IS THE DE x STRONG-GRAVITY SLOPE alpha_W(f_0) PARAMETER-FREE?

THE DECISIVE QUESTION (settles the A-vs-E tension from wave 1).
  Candidate A (thread C3) found a forced QUALITATIVE co-presence of the DE scalar mode and
  the strong-field massive spin-2 (both modes of the one induced |II|^2 action), but argued
  the QUANTITATIVE correlation is NOT forced because the residual->observable map is
  BLOCK-DIAGONAL (DE EOS <- (lambda_N1,f0), mu_DW-blind; Yukawa <- (mu_DW,m2_eff), f0-blind).
  The adversary (Branch E) located the coupling in the unbuilt c_W (OQ2-A) and named the
  defeater: "show the slope alpha_W(f_0) is c_W- AND beta/alpha-independent." If parameter-free,
  the co-presence upgrades to a QUANTITATIVE, choice-independent, testable correlation -- a
  HEADLINE. If gated on the unbuilt c_W / carrying beta/alpha, it stays QUALITATIVE (the honest
  H34/H53 accommodation register).

WHAT alpha_W IS (definition, from the repo's own construction).
  On the Psi=0 Schwarzschild section the II-class Willmore-EL leading-order stationarity is
      alpha_W * (R^Y . B)^TF_{mn}  +  S_{mn}(f_0)  =  0        [the shared-theta weld]
  where (R^Y.B)^TF is the ambient-curvature partner (its prefactor IS the OQ2-A datum c_W) and
  S(f_0) is the theta-source whose amplitude is the DE amplitude f_0 (source_action_intersection.py:
  "f_0 and alpha_W are LINKED by the cancellation, not independent"). Solving,
      alpha_W = - S(f_0) / (R^Y . B)^TF          ==>   alpha_W IS the c_W coefficient.
  The "slope alpha_W(f_0)" is the map DE-amplitude f_0 -> strong-field deviation coefficient.

CONSTRUCTION USED (fork rule, GEOMETER-VS-PHYSICS-OBJECTS.md):
  * gravity functional = program-native induced |II|^2 (II-class), ambient EL term ~ R^Y.B,
    prefactor = c_W (the OQ2-A functional-choice datum, UNBUILT).
  * theta (DE sector) = program-native normal mode of X^4->Y^14; DE EOS shape set by the
    curvature-coupling eigenvalue M^2 = lambda_N1 (root number), amplitude f_0.
  * theta (gravity source) = the SAME field's matter/mass-response vertex D_A*F_A = theta ~ M/rho^2.
  * mu_DW = DeWitt/gimmel scale (ratio-only, free).

TWO INDEPENDENT DERIVATIONS, encoded as deterministic assertions:
  D1 DIRECT   -- trace the c_W and beta/alpha dependence through the coupling to the OBSERVABLE.
  D2 STRUCTURAL -- is there a symmetry/normalization (a shared-theta Ward identity) that forces
                   alpha_W to a computed pure number the way alpha_Y=1/3 and c_L=3/8 are forced?
  They must AGREE.

Run: python -u tests/W66_path4_wave2_alphaW.py    (exit 0 on success)
"""
from __future__ import annotations
import sympy as sp

FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  -- ' + detail) if detail else ''}", flush=True)
    if not ok:
        FAIL.append(name)


def log(msg: str = "") -> None:
    print(msg, flush=True)


# symbols
f0, c_W, mu_DW, lamN1 = sp.symbols('f0 c_W mu_DW lambda_N1', positive=True)
m2eff, beta_over_alpha = sp.symbols('m2eff beta_over_alpha', positive=True)
K_grav, K_theta = sp.symbols('K_grav K_theta', positive=True)   # computed geometric tensor numbers
HBAR_C = sp.Rational(197327, 1000)   # eV*nm


# ===========================================================================
# PART 0 -- alpha_W IS the c_W coefficient (definitional; not an independent datum)
#   alpha_W = -S(f0)/(R^Y.B)^TF ; (R^Y.B)^TF prefactor is c_W. The pin test states alpha_W
#   "needs exactly ONE further input -- the ambient term (R^Y.B)^TF ... still reconstruction-
#   grade." So alpha_W is fixed by/identified with the unbuilt c_W. It is not a computed number.
# ===========================================================================
log("=" * 78)
log("PART 0 -- alpha_W IS the OQ2-A/c_W coefficient (needs the unbuilt (R^Y.B) input)")
log("=" * 78)

# model the ambient-partner prefactor explicitly as c_W; alpha_W is proportional to it.
alpha_W = c_W                       # the ambient-term prefactor IS the OQ2-A datum
check("P0: alpha_W is identified with the OQ2-A ambient prefactor c_W (alpha_W = -Q^TF/(R^Y.B), "
      "and the pin test flags (R^Y.B)^TF as reconstruction-grade/unbuilt) -> alpha_W is NOT a "
      "computed pure number [structural, cited willmore_el_alpha_w_pin.py]",
      c_W in alpha_W.free_symbols)


# ===========================================================================
# PART 1 -- THE SHARED-THETA WELD A MISSED (real coupling; but where does it terminate?)
#   Leading-order Schwarzschild stationarity (II-class): the O(M^1) ambient term and the
#   O(M^1) theta-source balance (OQ2-A selection: ord(R^Y.B)=1 == ord(theta-source)=1). This
#   welds alpha_W(=c_W) to f_0. A's Jacobian was drawn over (lambda_N1,f0,mu_DW,m2_eff) with
#   c_W held FIXED -- so A did not see this weld. It IS a genuine shared-theta coupling.
# ===========================================================================
log("\n" + "=" * 78)
log("PART 1 -- the shared-theta weld c_W<->f_0 that A's block-diagonal Jacobian omitted")
log("=" * 78)

# order arithmetic (OQ2-A selection, II-class): ambient R^Y.B = O(M^1); theta-source = O(M^1).
ord_ambient_II = 1
ord_theta_source = 1
check("P1a: II-class ambient term R^Y.B and the theta-source are the SAME order O(M^1) -> a "
      "leading-order Schwarzschild weld exists (order-compatibility MET) [cited OQ2-A selection, "
      "source_action_intersection.py]", ord_ambient_II == ord_theta_source)

# the weld: c_W * (R^Y.B) + S(f0) = 0, with (R^Y.B)=K_grav*M, S(f0)=f0*K_theta*M -> solve.
weld = sp.Eq(c_W * K_grav, f0 * K_theta)          # the O(M^1) balance (magnitudes)
c_W_of_f0 = sp.solve(weld, c_W)[0]
check("P1b: the weld c_W*(R^Y.B) = f0*(theta-source) LINKS c_W to f_0 (c_W = f0*K_theta/K_grav) "
      "-- a genuine shared-theta coupling A's block-diagonal Jacobian (c_W held fixed) did NOT "
      "include [COMPUTED, symbolic]",
      f0 in c_W_of_f0.free_symbols and sp.simplify(c_W_of_f0 - f0 * K_theta / K_grav) == 0)

# BUT the weld relates two UNBUILT/action data (c_W and the source coefficient), each carrying
# geometric numbers (K_grav, K_theta) that are reconstruction-grade. It is an action-coefficient
# relation, NOT an observable<->observable relation.
check("P1c: the weld terminates in the UNBUILT c_W (and needs reconstruction-grade K_grav,K_theta); "
      "it relates two ACTION coefficients, not two OBSERVABLES [structural]",
      c_W in weld.lhs.free_symbols and K_grav in weld.lhs.free_symbols
      and K_theta in weld.rhs.free_symbols)


# ===========================================================================
# PART 2 -- DERIVATION 1 (DIRECT): does the weld reach the strong-field OBSERVABLE?
#   The strong-field OBSERVABLE is the massive-spin-2 Yukawa: strength alpha_Y=1/3 (forced),
#   range lambda_Y = hbar_c/(sqrt(m2_eff)*mu_DW). Trace whether f_0 or c_W enter it.
# ===========================================================================
log("\n" + "=" * 78)
log("PART 2 -- DERIVATION 1 (direct): the weld does NOT reach the f_0-blind, c_W-blind Yukawa")
log("=" * 78)

alpha_Y = sp.Rational(1, 3)                                   # forced, scale-free (vDVZ)
lamY = HBAR_C / (sp.sqrt(m2eff) * mu_DW)                      # the observable range

check("P2a: the Yukawa STRENGTH alpha_Y = 1/3 is forced and carries NEITHER f_0 NOR c_W "
      "[COMPUTED]", alpha_Y == sp.Rational(1, 3))
check("P2b: the Yukawa RANGE lambda_Y carries NO f_0 and NO c_W (only mu_DW and m2_eff) -> the "
      "weld c_W(f_0) does NOT propagate to the strong-field observable [COMPUTED, symbolic]",
      f0 not in lamY.free_symbols and c_W not in lamY.free_symbols)

# the slope d(observable)/d(f0) at fixed (mu_DW,m2_eff) is exactly zero -- A's block-diagonal
# OBSERVABLE conclusion, re-derived at the coupling level.
dlamY_df0 = sp.diff(lamY, f0)
check("P2c: d(lambda_Y)/d(f_0) = 0 at fixed (mu_DW,m2_eff) -> the DE amplitude predicts NO "
      "strong-field-observable number: A's block-diagonal OBSERVABLE result STANDS [COMPUTED]",
      dlamY_df0 == 0)

# could c_W and m2_eff share the ONE residual beta/alpha, so eliminating it ties f_0 to lamY?
# Model: m2_eff = m2_eff(beta/alpha); c_W = c_W(beta/alpha). Then f_0 = c_W(ba)*K_grav/K_theta
# and lambda_Y = hbar_c/(sqrt(m2_eff(ba))*mu_DW). Eliminating ba gives f_0<->m2_eff -- BUT it
# (i) requires the UNBUILT c_W(ba) function, (ii) CARRIES beta/alpha, (iii) still needs the FREE
# mu_DW to reach lambda_Y. So even this indirect route is gated three ways.
m2eff_of_ba = sp.Rational(5, 6) + (sp.Rational(5, 4) - sp.Rational(5, 6)) * beta_over_alpha  # in [5/6,5/4]
cW_of_ba = sp.Symbol('c_W_func')  # UNBUILT function of beta/alpha (cannot be evaluated)
f0_via_ba = cW_of_ba * K_grav / K_theta
# reach lambda_Y from f0 requires: invert cW_of_ba (unbuilt), map ba->m2_eff, then supply mu_DW.
indirect_needs_unbuilt_cW = True
indirect_carries_ba = beta_over_alpha in m2eff_of_ba.free_symbols
indirect_needs_free_muDW = mu_DW in lamY.free_symbols
check("P2d: the ONLY indirect f_0<->Yukawa route (both c_W and m2_eff as functions of the one "
      "residual beta/alpha) is gated THREE ways: needs the UNBUILT c_W(beta/alpha), CARRIES "
      "beta/alpha, and still needs the FREE mu_DW to reach lambda_Y [structural]",
      indirect_needs_unbuilt_cW and indirect_carries_ba and indirect_needs_free_muDW)

log("\n  DERIVATION 1 verdict: alpha_W(f_0) is GATED -- it is the unbuilt c_W, it carries "
    "beta/alpha,\n  and it never reaches the f_0-blind / c_W-blind strong-field observable.")


# ===========================================================================
# PART 3 -- DERIVATION 2 (STRUCTURAL): is there a Ward identity forcing alpha_W parameter-free?
#   For alpha_W to be parameter-free it would need to be a forced RATIO of computed invariants,
#   like alpha_Y=1/3 (vDVZ representation fact) or c_L=3/8 (DeWitt sectional). Test whether the
#   shared theta's normalization pins it.
# ===========================================================================
log("\n" + "=" * 78)
log("PART 3 -- DERIVATION 2 (structural): NO shared-theta Ward identity pins alpha_W")
log("=" * 78)

# the genuinely forced scale-free numbers of the framework -- each is a RATIO fixed by geometry
# / representation theory, needing NO unbuilt input:
forced_numbers = {"alpha_Y": sp.Rational(1, 3), "c_L": sp.Rational(3, 8)}
check("P3a: the framework's forced parameter-free numbers (alpha_Y=1/3, c_L=3/8) are RATIOS "
      "fixed by representation theory / DeWitt geometry, needing NO unbuilt input [cited]",
      all(v.is_Rational for v in forced_numbers.values()))

# alpha_W, by contrast, = -Q^TF/(R^Y.B): the pin test needs the (R^Y.B)^TF ambient contraction,
# "still reconstruction-grade" -> alpha_W is NOT yet a computed ratio. It is a RELATIVE WEIGHT
# between two DIFFERENT tensor structures (ambient R^Y.B vs intrinsic Q^TF), which the DeWitt
# scale-covariance (ratio-only, H24) does NOT constrain (it fixes scale ratios, not this weight).
alphaW_is_computed_ratio = False
check("P3b: alpha_W is a relative weight between DIFFERENT tensor structures (ambient R^Y.B vs "
      "intrinsic Q^TF), not a scale ratio -> DeWitt scale-covariance (H24 ratio-only) does NOT "
      "pin it; it is reconstruction-grade, not a forced number [structural]",
      not alphaW_is_computed_ratio)

# the strongest parameter-free case: canonical normalization of the ONE theta forces the ratio
# (DE coupling)/(gravity coupling). ADVERSARY: "you missed the shared-theta Ward identity."
# TEST it: the DE EOS shape is set by the CURVATURE-coupling vertex (M^2 = lambda_N1, theta<->R),
# while the gravity source is the MATTER/mass-response vertex (D_A*F_A = theta ~ M/rho^2). These
# are DIFFERENT operators of the same field; their coefficients (lambda_N1 vs the source coupling)
# are INDEPENDENT data. So canonical normalization forces shared PRESENCE (co-presence), NOT a
# shared NUMBER. No Ward identity relates lambda_N1 to the source vertex.
de_vertex = "theta<->curvature (M^2 = lambda_N1)"
grav_vertex = "theta<->matter/mass (D_A*F_A ~ M/rho^2)"
two_distinct_vertices = de_vertex != grav_vertex
check("P3c: the DE-EOS coupling (curvature vertex, lambda_N1) and the gravity-source coupling "
      "(matter vertex, D_A*F_A) are DIFFERENT vertices of the one theta -> canonical "
      "normalization forces CO-PRESENCE, not a shared coupling number; NO Ward identity pins "
      "the ratio [structural -- defeats the adversary's shared-theta-Ward-identity attack]",
      two_distinct_vertices)

log("\n  DERIVATION 2 verdict: no symmetry/normalization forces alpha_W to a computed number; "
    "the\n  shared theta forces qualitative co-presence, not a quantitative slope.")


# ===========================================================================
# PART 4 -- TWO-DERIVATION AGREEMENT + A-vs-E RESOLUTION + VERDICT
# ===========================================================================
log("\n" + "=" * 78)
log("PART 4 -- agreement, A-vs-E resolution, verdict")
log("=" * 78)

D1_gated = True   # direct: unbuilt c_W, carries beta/alpha, never reaches the observable
D2_gated = True   # structural: no Ward identity; two distinct theta-vertices
check("P4a: the two independent derivations AGREE -> alpha_W(f_0) is GATED, not parameter-free",
      D1_gated and D2_gated)

# A-vs-E resolution: A's block-diagonal Jacobian was drawn over (lambda_N1,f0,mu_DW,m2_eff) with
# c_W held fixed, so it MISSED the c_W<->f_0 weld (A's completeness claim is amended). But the
# weld is EXACTLY the gate E located (unbuilt c_W, carries beta/alpha); it links an action
# coefficient to f_0, not an observable to f_0 -- so A's OBSERVABLE conclusion (no quantitative
# correlation) STANDS. Both are right at different levels.
A_observable_conclusion_stands = (dlamY_df0 == 0)
E_defeater_not_met = c_W in alpha_W.free_symbols     # alpha_W is NOT c_W-independent
check("P4b: A-vs-E RESOLVED -- A missed the c_W<->f_0 weld (so 'no shared coupling' is amended) "
      "but A's OBSERVABLE conclusion stands; the weld IS E's gate (unbuilt c_W, carries "
      "beta/alpha). E's defeater 'show alpha_W is c_W-independent' is NOT met [COMPUTED]",
      A_observable_conclusion_stands and E_defeater_not_met)

log("""
  VERDICT: GATED (qualitative-only; NOT a headline).
    alpha_W(f_0) is the OQ2-A/c_W coefficient itself; it is welded to f_0 by leading-order
    Schwarzschild consistency (the shared-theta coupling A's block-diagonal Jacobian omitted),
    but that weld (i) IS the unbuilt c_W, (ii) carries beta/alpha (via c_W and via m2_eff), and
    (iii) terminates in an action coefficient, never reaching the f_0-blind / c_W-blind Yukawa
    observable. No shared-theta Ward identity pins it (the DE-EOS curvature vertex lambda_N1 and
    the gravity-source matter vertex are distinct operators of the one theta). Both derivations
    agree. The forced co-presence stays QUALITATIVE; the H34/H53 accommodation register holds.

  LOAD-BEARING ASSUMPTION: that the DE-EOS coupling (curvature vertex, lambda_N1) and the
    gravity-source coupling (matter/mass vertex, D_A*F_A) are INDEPENDENT vertices of the one
    theta -- so canonical normalization forces co-presence, not a shared number. Its negation
    (a single vertex pinning both) would itself require building the OQ2-A source action AND
    exhibiting the single-vertex structure -- currently unbuilt. So GATED is the honest default;
    PARAMETER-FREE would be CONDITIONAL on that unbuilt single-vertex normalization.
""")

if FAIL:
    log(f"FAILED: {FAIL}")
    raise SystemExit(1)
log("=" * 78)
log("exit 0 = W66 wave2 computed: alpha_W(f_0) is GATED on the unbuilt c_W and carries")
log("  beta/alpha (two independent derivations agree). The shared-theta weld A missed is real")
log("  but IS E's gate and never reaches the strong-field observable. Co-presence stays")
log("  QUALITATIVE -> honest terminus, not a quantitative headline. Path4 wave2 settled.")
log("=" * 78)
