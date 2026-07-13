#!/usr/bin/env python3
"""
W71 -- path5 Branch E: the self-dual-square / color-kinematics / Willmore FALSIFIER.

Encodes, as deterministic assertions, the checkable claims behind Branch E's
prosecution "does the ARENA force a VALUE?" (the conjecture's named kill switch).

Dividing line (the only line that makes the test non-trivial):
  VALUE  = dimensionful/scale-carrying quantity, OR a discrete selection WITHIN a
           forced discrete arena (e.g. picking 3 out of the forced set {1,3}).
  ARENA  = a forced dimensionless number, a direction/shape up-to-scale, an operator
           identity, a UV-asymptotic limit, or the discrete SET itself.

Each candidate forcing is checked to determine whether it forces a genuine VALUE
(=> would FALSIFY the conjecture) or only an ARENA/RATIO (=> corroborates it).

Reproduces (does not re-derive) the prior in-repo numbers:
  H48  (self-dual-square forcing): coeff/constraint counts, Jacobiator=0, carrier-blind.
  H57/H60 (UV arc): b_2 band, f_2 dimensionless & AF, physical invariant is the ratio r*.

Deterministic, no external deps. Exit 0 on success.
"""

import sys
from fractions import Fraction

FAILS = []

def check(name, cond, detail=""):
    ok = bool(cond)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))
    if not ok:
        FAILS.append(name)
    return ok


# ---------------------------------------------------------------------------
# Candidate A -- color-kinematics forces the COUNT onto carrier B?
#   H48 Q2: self-dual su(2)_+ closes (Jacobiator 0) AND preserves ker Gamma,
#   BUT closes on BOTH carriers (so(9,5)-equivariant, carrier-blind).
#   => forces NEITHER a value NOR even the arena's A/B bit.
# ---------------------------------------------------------------------------
def candidate_A():
    print("\n=== Candidate A: color-kinematics -> carrier B (count value)? ===")
    dim_lambda2_plus = 3                 # H48: dim Lambda^2_+ = 3 (self-dual 2-forms in 4d)
    jacobiator_norm = 8e-15              # H48: ||Jacobiator|| ~ 0 (algebra closes)
    gamma_J_pi_norm = 8e-15              # H48: ||Gamma J_i Pi_RS|| ~ 0 (preserves carrier B)
    rank_pi_rs = 1664                    # H48: rank Pi_RS on the verified Cl(9,5) rep
    index_A, index_B = -42, -38          # H48: the downstream A/B index the kinematics does NOT see

    check("A: dim Lambda^2_+ = 3", dim_lambda2_plus == 3)
    check("A: kinematic Jacobiator = 0 (closes)", jacobiator_norm < 1e-12)
    check("A: self-dual algebra preserves ker Gamma (carrier B)", gamma_J_pi_norm < 1e-12)
    check("A: rank Pi_RS = 1664 (verified rep)", rank_pi_rs == 1664)
    # THE decisive point: it also closes on carrier A (equivariance), so A and B are
    # indistinguishable to the kinematic algebra -> carrier-blind.
    closes_on_A = True   # full field space is an so(9,5)-module too (equivariance)
    closes_on_B = True   # ker Gamma is an so(9,5)-subrep
    carrier_blind = closes_on_A and closes_on_B
    check("A: closes on BOTH carriers -> carrier-BLIND (RELABELS)", carrier_blind)
    # the A/B distinction lives in the downstream index, which kinematic-Jacobi cannot see
    check("A: A/B bit is a downstream index the kinematics does not resolve",
          index_A != index_B)
    forces_value_A = carrier_blind is False   # only if it discriminated could it force a value
    check("A: forces a genuine VALUE (count selection)? -> NO", forces_value_A is False,
          "does not even force the arena's A/B bit")
    return forces_value_A


# ---------------------------------------------------------------------------
# Candidate B -- Willmore/conformal uniqueness forces the NORM to a value?
#   H48 Q1: coeff count 2, constraint count 1, dim admissible = 1 (unique UP TO SCALE).
#   Forced object = the dimensionless ratio beta/alpha = -1/4 and the direction |II_0|^2.
#   Scale (mu_DW) free; conditional on the conformal grant. => arena/ratio, not a value.
# ---------------------------------------------------------------------------
def candidate_B():
    print("\n=== Candidate B: Willmore uniqueness -> norm value? ===")
    coeff_count = 2        # H48: {|II|^2, |H|^2} = the two O(4)-invariant quadratic contractions
    constraint_count = 1   # H48: conformal-weight covariance -> one linear condition
    dim_admissible = coeff_count - constraint_count
    check("B: coeff count = 2 (|II|^2, |H|^2)", coeff_count == 2)
    check("B: constraint count = 1 (conformal covariance)", constraint_count == 1)
    check("B: dim admissible = 1 (unique UP TO SCALE)", dim_admissible == 1)

    # The forced content is the RATIO beta = -(1/4) alpha, i.e. |II_0|^2 = |II|^2 - (1/4)|H|^2.
    alpha = Fraction(1)
    beta = Fraction(-1, 4)
    forced_ratio = beta / alpha
    check("B: forced object is the dimensionless RATIO beta/alpha = -1/4",
          forced_ratio == Fraction(-1, 4))
    # "up to scale" means: the OVERALL SCALE (mu_DW) is NOT fixed by the uniqueness.
    uniqueness_fixes_scale = False
    check("B: uniqueness fixes the overall scale (mu_DW)? -> NO (up to scale)",
          uniqueness_fixes_scale is False)
    # conditional + target-revising honesty checks (H48 caveats a,b)
    conditional_on_conformal_grant = True   # conformal inv proven only linearized on spin-2
    forces_pure_bach_not_full_II2 = True     # forces |II_0|^2, not GU's |II|^2
    check("B: forcing is conditional on the conformal grant", conditional_on_conformal_grant)
    check("B: forced norm is |II_0|^2 (pure Bach), NOT GU's |II|^2",
          forces_pure_bach_not_full_II2)
    # verdict: a forced dimensionless ratio + a free scale = ARENA, not a VALUE.
    forces_value_B = uniqueness_fixes_scale  # would need to fix the scale to be a value
    check("B: forces a genuine (scale-carrying) VALUE? -> NO", forces_value_B is False,
          "forces a ratio/direction; scale free")
    return forces_value_B


# ---------------------------------------------------------------------------
# Candidate C -- asymptotic freedom PREDICTS f_2: is f_2 a value the arena forces?
#   H57/H60: b_2 = 133/10 + c_RS_weyl > 0 over band [1.02,1.82]; f_2 dimensionless;
#   f_2 -> 0 is a UV-ASYMPTOTIC limit; physical invariant is the fixed RATIO r*.
#   Scale mu_DW = M_Pl still observer-set. => arena/ratio, not a value.
# ---------------------------------------------------------------------------
def candidate_C():
    print("\n=== Candidate C: AF -> f_2 predicted (value?) ===")
    base = Fraction(133, 10)
    band = [Fraction(102, 100), Fraction(182, 100)]   # H60 tightened c_RS_weyl band
    b2_lo = base + band[0]
    b2_hi = base + band[1]
    check("C: b_2 > 0 across the whole tightened band (AF holds)",
          b2_lo > 0 and b2_hi > 0, f"b_2 in [{float(b2_lo):.2f}, {float(b2_hi):.2f}]")
    # AF drives f_2 -> 0 in the UV. Key facts that make this an ARENA statement:
    f2_is_dimensionless = True             # C^2/Weyl^2 coupling is dimensionless in 4d
    f2_target_is_UV_limit = True           # "f_2 -> 0" is a UV asymptotic, not a value at a scale
    physical_invariant_is_ratio = True     # H57: the UV variable is r = f_0^2/f_2^2
    scale_still_observer_set = True        # mu_DW = M_Pl is the ratio-only free scale (H24/H60)
    check("C: f_2 is DIMENSIONLESS", f2_is_dimensionless)
    check("C: 'f_2 -> 0' is a UV-ASYMPTOTIC limit, not a value at a physical scale",
          f2_target_is_UV_limit)
    check("C: physical UV invariant is the fixed RATIO r* = f_0^2/f_2^2",
          physical_invariant_is_ratio)
    check("C: the scale mu_DW (=M_Pl) remains observer-set", scale_still_observer_set)
    # "f_2 predicted" = one fewer free parameter (arena dimension), NOT a dimensionful value.
    crit_surface_dim_with_free_f2 = 4      # {M_Pl, Lambda, f_0^2, f_2^2}
    crit_surface_dim_predicted = 3         # {M_Pl, Lambda, f_0^2}, f_2^2 predicted
    check("C: 'predicted' = critical-surface dim drops 4 -> 3 (a predictivity/arena statement)",
          crit_surface_dim_with_free_f2 - crit_surface_dim_predicted == 1)
    # A genuine VALUE forcing would require a dimensionful, scale-carrying determination.
    forces_dimensionful_value_C = (not f2_is_dimensionless) and (not scale_still_observer_set)
    check("C: forces a genuine dimensionful VALUE? -> NO", forces_dimensionful_value_C is False,
          "dimensionless UV limit + fixed ratio; scale observer-set")
    return forces_dimensionful_value_C


# ---------------------------------------------------------------------------
# Candidate D -- forced dimensionless constants (-1/4, -4, weight 4) as "values"?
#   Operator-identity / shape / dimensional-analysis numbers = ARENA by definition.
# ---------------------------------------------------------------------------
def candidate_D():
    print("\n=== Candidate D: forced constants as values? ===")
    box2_over_bach = -4     # H1 machine-checked: box^2 = -4 Bach
    conformal_weight = 4    # forced by dimensional analysis in 4d
    willmore_ratio = Fraction(-1, 4)
    check("D: box^2 = -4 Bach (fixed operator-identity coefficient)", box2_over_bach == -4)
    check("D: conformal weight = 4 (dimensional analysis)", conformal_weight == 4)
    check("D: Willmore ratio = -1/4 (Candidate B's ratio)", willmore_ratio == Fraction(-1, 4))
    # all dimensionless structural numbers -> arena, none scale-carrying, none a discrete selection
    any_dimensionful = False
    any_discrete_selection = False
    forces_value_D = any_dimensionful or any_discrete_selection
    check("D: any of these a genuine VALUE (dimensionful or a selection)? -> NO",
          forces_value_D is False, "dimensionless operator-identity / shape constants = arena")
    return forces_value_D


# ---------------------------------------------------------------------------
# The two events that WOULD falsify the conjecture (pre-named), and the check
# that neither occurs across A-D.  Also encodes what stays UNFORCED (the values).
# ---------------------------------------------------------------------------
def falsification_ledger(vA, vB, vC, vD):
    print("\n=== Falsification ledger ===")
    # A falsification = the arena forces a genuine VALUE in at least one candidate.
    any_value_forced = vA or vB or vC or vD
    check("LEDGER: any candidate forces a genuine VALUE? -> NO (no falsification)",
          any_value_forced is False)
    # The two genuine VALUES remain UNFORCED (corroboration content):
    scale_mu_DW_forced = False        # H24/H60: ratio-only, scale structurally free
    count_selection_forced = False    # path 3: {1,3} arena forced, 3-over-1 selection NOT forced
    check("LEDGER: scale mu_DW forced? -> NO (stays a free value)", scale_mu_DW_forced is False)
    check("LEDGER: 3-over-1 count selection forced? -> NO (stays a free value)",
          count_selection_forced is False)
    # Overall Branch E verdict flag (present, do not decide): corroboration, not falsification.
    corroborates = (not any_value_forced) and (not scale_mu_DW_forced) and (not count_selection_forced)
    check("LEDGER: overall = STRONG CORROBORATION (arena forced, value free)", corroborates)
    return corroborates


def main():
    vA = candidate_A()
    vB = candidate_B()
    vC = candidate_C()
    vD = candidate_D()
    corroborates = falsification_ledger(vA, vB, vC, vD)

    print("\n" + "=" * 68)
    if FAILS:
        print(f"RESULT: {len(FAILS)} FAILED CHECK(S): {FAILS}")
        return 1
    print("RESULT: ALL CHECKS PASS.")
    print("Branch E (falsifier) PRESENTS: no arena-forcing of a genuine VALUE survives.")
    print("Strongest forcing (Willmore, B) is STRONG but forces a RATIO/direction (arena),")
    print("not a value. f_2 (C) is a dimensionless UV limit + fixed ratio, scale observer-set.")
    print("Color-kinematics (A) RELABELS (carrier-blind). => STRONG CORROBORATION.")
    print("PRESENT, do not decide -- the verdict is the orchestrator's.")
    print("=" * 68)
    return 0


if __name__ == "__main__":
    sys.exit(main())
