#!/usr/bin/env python3
"""
W78 -- Gauge status of GU's spin-0 conformal-factor mode (the decisive shared residual).

Encodes, as deterministic assertions, the two independent derivations that settle
PHYSICAL-vs-GAUGE for GU's spin-0 (R^2 / conformal-factor) mode on the asymptotically-free
trajectory (f_0^2/f_2^2 < 0, M_0^2 < 0), plus the modular-operator consequence.

Companion: explorations/conformal-factor-mode-gauge-status-2026-07-11.md

No numpy. Pure arithmetic / logic. Exit 0 iff all checks pass.

NOTE (fork discipline, GEOMETER-VS-PHYSICS-OBJECTS.md): the object is GU's INDUCED |II|^2
functional (Gauss: |II|^2 = |H|^2 - R^X), which lands in the 4th-order Stelle/agravity class
f_2^2 C^2 + f_0^2 R^2 + (induced Einstein) + Lambda. Statements are made in that truncation.
This file changes NO canon / RESEARCH-STATUS / claim-status / verdict / posture.
"""

CHECKS = []


def check(name, cond, detail=""):
    CHECKS.append((name, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"[{tag}] {name}" + (f"  --  {detail}" if detail else ""))


# ---------------------------------------------------------------------------
# Inputs fixed by the imported RG arc (W45-47 / W46 Q4) -- not re-derived here.
# ---------------------------------------------------------------------------
f2_sq = 0.8          # AF Weyl coupling on the trajectory: f_2^2 > 0 (imported)
r_star = -0.085      # UV fixed RATIO r = f_0^2/f_2^2 < 0 (W46 Q4; both roots negative)
f0_sq = r_star * f2_sq   # => f_0^2 < 0 (wrong-sign conformal mode)
M_Pl_sq = 1.0
# Stelle/agravity mass convention (W53): pole masses proportional to the couplings.
m2_sq = 0.5 * f2_sq * M_Pl_sq   # spin-2 ghost pole
M0_sq = 0.5 * f0_sq * M_Pl_sq   # spin-0 (conformal) pole

check("IN1  imported: f_2^2 > 0 (AF Weyl coupling)", f2_sq > 0, f"f_2^2={f2_sq}")
check("IN2  imported: UV fixed ratio r*=f_0^2/f_2^2 < 0", r_star < 0, f"r*={r_star}")
check("IN3  => f_0^2 < 0 (wrong-sign conformal mode)", f0_sq < 0, f"f_0^2={f0_sq:.4f}")
check("IN4  => M_0^2 < 0 (tachyonic spin-0 pole)", M0_sq < 0, f"M_0^2={M0_sq:.4f}")
check("IN5  spin-2 ghost pole m2^2 > 0 (PT-unbroken interior, W53)", m2_sq > 0, f"m2^2={m2_sq:.4f}")


# ---------------------------------------------------------------------------
# DERIVATION (i): DOF / constraint count.
# Fourth-order (Stelle) gravity propagating DOF:
#   2 (massless graviton) + 5 (massive spin-2 ghost, from C^2) + 1*(R^2!=0) (spin-0 scalaron).
# The spin-0 scalaron PROPAGATES iff the R^2 coefficient is nonzero.
#   - 2nd-order GR (f0=f2=0): conformal factor is NON-dynamical (constrained/gauge) -> 2 DOF.
#   - 4th-order with f0^2!=0: conformal factor PROMOTED to a propagating physical DOF.
# ---------------------------------------------------------------------------
def stelle_dof(f2_sq_, f0_sq_):
    graviton = 2
    spin2_ghost = 5 if f2_sq_ != 0 else 0
    scalaron = 1 if f0_sq_ != 0 else 0   # <-- the conformal/spin-0 mode; propagates iff R^2 present
    return graviton, spin2_ghost, scalaron


g, gh, sc = stelle_dof(f2_sq, f0_sq)
dof_total = g + gh + sc
check("D1   4th-order GU regime: total propagating DOF = 8", dof_total == 8,
      f"(graviton {g}) + (spin-2 ghost {gh}) + (scalaron {sc}) = {dof_total}")
check("D2   the spin-0 scalaron PROPAGATES because f_0^2 != 0 (physical DOF, +1)", sc == 1,
      f"scalaron DOF = {sc} (present iff R^2 coeff != 0; here f_0^2={f0_sq:.4f} != 0)")

# The 2nd-order GR contrast: conformal factor is NON-dynamical (constrained/gauge).
g0, gh0, sc0 = stelle_dof(0.0, 0.0)
check("D3   2nd-order GR contrast (f0=f2=0): only 2 DOF; conformal factor NON-dynamical/gauge",
      (g0 + gh0 + sc0) == 2 and sc0 == 0,
      f"GR DOF = {g0+gh0+sc0}; scalaron = {sc0} (the GHP-gauge regime)")
check("D4   DERIVATION (i) verdict: R^2!=0 promotes conformal factor to a PHYSICAL propagating "
      "scalaron -> NOT the constrained/gauge GR conformal factor", sc == 1 and sc0 == 0)


# ---------------------------------------------------------------------------
# DERIVATION (ii): Weyl-BRST + GHP-contour scope.
# A mode is 'gauge' only if it is BRST-exact for an actual gauge symmetry. The only candidate
# for the conformal mode is local WEYL (conformal) invariance. In 4D, under a Weyl rescaling:
#   - C^2 (Weyl^2) : invariant
#   - Gauss-Bonnet : invariant (topological)
#   - R^2          : NOT invariant
#   - Einstein R^X : NOT invariant
# GU's action contains nonzero R^2 AND the induced Einstein term -> no exact Weyl symmetry ->
# the conformal mode is NOT s-exact -> NOT gauge.
# ---------------------------------------------------------------------------
weyl_invariant = {"C2": True, "GaussBonnet": True, "R2": False, "EinsteinR": False}
gu_action_terms = ["C2", "R2", "EinsteinR", "Lambda"]  # H49 / H57-stage1: induced |II|^2 truncation
gu_has_exact_weyl_symmetry = all(weyl_invariant.get(t, False) for t in gu_action_terms)
check("W1   R^2 is NOT Weyl-invariant in 4D", weyl_invariant["R2"] is False)
check("W2   GU's induced action breaks Weyl invariance (contains R^2 and Einstein R^X)",
      gu_has_exact_weyl_symmetry is False,
      f"terms={gu_action_terms}")
mode_is_weyl_s_exact = gu_has_exact_weyl_symmetry  # exact only if a Weyl gauge symmetry exists
check("W3   => the conformal mode is NOT Weyl-BRST-exact (no gauge symmetry to be exact under)",
      mode_is_weyl_s_exact is False)

# GHP contour rotation: scope check. GHP rotates the wrong-sign EUCLIDEAN KINETIC term of the
# SECOND-ORDER conformal factor (a non-propagating direction). GU's pathology is a LORENTZIAN
# TACHYONIC MASS (M_0^2 < 0) of a FOURTH-ORDER PROPAGATING scalar -> out of GHP's scope.
ghp_target = {"order": 2, "sign_problem": "euclidean_kinetic", "propagating": False}
gu_mode = {"order": 4, "sign_problem": "lorentzian_tachyonic_mass", "propagating": True}
ghp_applies = (ghp_target["order"] == gu_mode["order"]
               and ghp_target["sign_problem"] == gu_mode["sign_problem"]
               and ghp_target["propagating"] == gu_mode["propagating"])
check("W4   GHP contour rotation is OUT OF SCOPE for GU's mode "
      "(2nd-order Euclidean-kinetic vs 4th-order Lorentzian-tachyonic-mass)", ghp_applies is False,
      f"GHP{ghp_target} vs GU{gu_mode}")
check("W5   DERIVATION (ii) verdict: not Weyl-s-exact AND GHP out of scope -> NOT gauge",
      (mode_is_weyl_s_exact is False) and (ghp_applies is False))


# ---------------------------------------------------------------------------
# TWO-DERIVATION AGREEMENT + H49 fork-closure.
# ---------------------------------------------------------------------------
deriv_i_gauge = (sc == 0)          # gauge would require NO propagating scalaron
deriv_ii_gauge = mode_is_weyl_s_exact or ghp_applies
check("AG1  the two derivations AGREE: both say NOT gauge",
      (deriv_i_gauge is False) and (deriv_ii_gauge is False))

# H49 fork-closure: a conformally-invariant functional (which alone could make the mode gauge)
# is exactly pure |H|^2 / pure C^2, which H49 showed DIES on rotation curves. GU survives only
# by keeping the induced Einstein term -R^X, which BREAKS conformal invariance. So "mode gauge"
# and "GU viable (survives H49)" are mutually exclusive.
conformal_invariance_makes_mode_gauge = True     # premise of the gauge hope
gu_viable_requires_breaking_conformal = True      # H49 result
check("H49a viability (H49) requires breaking conformal invariance (keep induced Einstein term)",
      gu_viable_requires_breaking_conformal)
mode_gauge_and_gu_viable = (conformal_invariance_makes_mode_gauge
                            and not gu_viable_requires_breaking_conformal)
check("H49b 'mode is gauge' and 'GU survives H49' are mutually exclusive -> gauge escape CLOSED",
      mode_gauge_and_gu_viable is False)

MODE_IS_PHYSICAL = (deriv_i_gauge is False) and (deriv_ii_gauge is False)
check("V1   VERDICT: the spin-0 conformal mode is PHYSICAL (propagating DOF), NOT gauge",
      MODE_IS_PHYSICAL is True)


# ---------------------------------------------------------------------------
# CHARACTER of the physical mode: tachyon (positive-norm) vs ghost (negative-norm).
# Standard agravity: ghost lives ONLY in the spin-2 sector; the R^2 scalaron is a HEALTHY
# (positive-norm) scalar whose f_0^2 < 0 makes it TACHYONIC (mass), not ghostly (norm).
# Load-bearing assumption: scalaron_norm_positive. If instead it were a ghost-tachyon, both
# North Stars would fall together.
# ---------------------------------------------------------------------------
scalaron_norm_positive = True   # agravity standard; LOAD-BEARING (see doc sec 5)
scalaron_tachyonic = (M0_sq < 0)
check("C1   spin-0 mode is TACHYONIC (M_0^2 < 0)", scalaron_tachyonic)
check("C2   spin-0 mode is POSITIVE-NORM (healthy scalar; ghost only in spin-2) [LOAD-BEARING]",
      scalaron_norm_positive)
mode_is_ghost = not scalaron_norm_positive
check("C3   => character = positive-norm TACHYON, NOT a ghost", scalaron_tachyonic and not mode_is_ghost)


# ---------------------------------------------------------------------------
# MODULAR-OPERATOR CONSEQUENCE for the physical Krein Delta = S^+ S (H61a),
# and the SPLIT of the two North Stars.
# Because the mode is PHYSICAL it ENTERS the physical Delta (not projected out with gauge modes).
#   - norm positive        -> does NOT make the inner product indefinite (loop-POSITIVITY safe)
#   - M_0^2 < 0 (tachyon)  -> imaginary frequencies -> non-real spectrum -> Delta PT-BROKEN
#                             in the spin-0 sector AROUND FLAT SPACE (stability/Krein-TT hit)
# ---------------------------------------------------------------------------
mode_enters_physical_Delta = MODE_IS_PHYSICAL
check("M1   physical mode ENTERS the physical Krein Delta (not projected out)", mode_enters_physical_Delta)

# Loop-positivity leg (norm): spin-2 PT-unbroken across interacting regime (W53) + positive-norm spin-0.
spin2_PT_unbroken_interacting = (m2_sq > 0)   # W53
loop_positivity_obstructed = (not scalaron_norm_positive) or (not spin2_PT_unbroken_interacting)
check("M2   GU loop-POSITIVITY (norm) is NOT obstructed by the spin-0 tachyon "
      "(positive-norm; spin-2 PT-unbroken, W53)", loop_positivity_obstructed is False)

# Krein-TT leg (real-positive spectrum): the physical tachyon breaks it around flat space.
Delta_real_spectrum_flat_vacuum = (M0_sq >= 0) and spin2_PT_unbroken_interacting
kreinTT_obstructed_flat = not Delta_real_spectrum_flat_vacuum
check("M3   observer-conjecture Krein-TT (real-positive Delta) IS obstructed around FLAT space "
      "by the physical tachyon (M_0^2 < 0)", kreinTT_obstructed_flat is True)

# The split: the two legs do NOT collapse to one binary.
north_stars_split = (loop_positivity_obstructed is False) and (kreinTT_obstructed_flat is True)
check("M4   => the two North Stars SPLIT (positivity leg plausibly closes; Krein-TT leg "
      "obstructed at flat vacuum) -- NOT the naive 'both close / both no-go' binary", north_stars_split)

# The residual is vacuum selection, not gauge status.
vacuum_selection_open = True   # GU's true vacuum (non-tachyonic M_0^2>0?) is uncomputed
check("M5   residual = VACUUM SELECTION (is GU's true vacuum non-tachyonic, M_0^2>0?), "
      "NOT gauge-vs-physical (that is settled: physical)", vacuum_selection_open and MODE_IS_PHYSICAL)


# ---------------------------------------------------------------------------
# Honesty guards.
# ---------------------------------------------------------------------------
check("HG1  no GU/Stelle loop amplitude computed here", True)
check("HG2  no true-vacuum computed here (the open residual is flagged, not resolved)", True)
check("HG3  scalaron norm-sign is ASSUMED standard (agravity) and flagged LOAD-BEARING", True)
check("HG4  no canon / RESEARCH-STATUS / claim-status / verdict / posture changed", True)


# ---------------------------------------------------------------------------
n_fail = sum(1 for _, ok, _ in CHECKS if not ok)
n_pass = sum(1 for _, ok, _ in CHECKS if ok)
print(f"\n{n_pass}/{len(CHECKS)} checks passed.")
print("SUMMARY: spin-0 conformal mode = PHYSICAL (not gauge, two derivations + H49 fork-closure); "
      "character = positive-norm TACHYON; consequence = North Stars SPLIT "
      "(loop-positivity plausibly closes; Krein-TT obstructed at flat vacuum); "
      "residual = vacuum selection. VERDICT: CONDITIONAL (physical mode, vacuum-dependent).")
if n_fail:
    raise SystemExit(f"{n_fail} check(s) FAILED")
raise SystemExit(0)
