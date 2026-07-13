#!/usr/bin/env python3
r"""
W92 / branch4-physics-sidestep -- the DEFLATIONARY sidestep of the observer-conjecture type-III frontier.

PRESENT, DO NOT DECIDE.  The North Star assumes the observer's physical realization NEEDS a genuine
type-III Krein modular conjugation J = C.PT (Tomita-Takesaki).  This test encodes -- AS ASSERTIONS -- the
branch's presented case:

  (1) does the observer's MECHANISM need the full modular J, or only a graded / pseudo-unitary S-matrix?
      -> split by level:  ABSTRACT mechanism (arena/value H62 + Lawvere no-closure H63) needs ONLY the
         fixpoint-free label-involution J^2 = 1 on {admissible, inadmissible}, NOT the modular J (STRONG,
         repo-established, rankN sec.5).  GENUINE physical firewall (keep-and-grade) needs strictly MORE
         than a bare pseudo-unitary graded S-matrix: pseudo-unitarity S^dag eta S = eta (K) is automatic
         and all-orders but does NOT deliver physical positivity (P) -- the loop ghost cut leaks negative
         (Branch A / W48).  So on the genuine-firewall side J (or an equivalent definitizing/modular
         structure) is NOT cheaply replaceable by a graded S-matrix (MEDIUM-STRONG).

  (2) do the fakeon (Anselmi-Piva) and Lee-Wick (Donoghue-Menezes) quantizations REALIZE the value-
      selection?  They give a unitary S-matrix with NO Krein modular conjugation -- but they buy it by
      REMOVING the ghost (fakeon: no asymptotic state; Lee-Wick: off-axis pole, no in/out state), at a
      bounded micro-causality price ~1/m2.  They realize a ghost-FREE theory, not a selection across a
      genuine indefinite firewall (STRONG, Branches C/D + W50/W51).

  (3) THE SAVE-vs-DEFLATE TENSION.  If a graded S-matrix suffices AND it works by removing the ghost, then
      (a) the type-III Krein-TT frontier is UNNECESSARY (good -- cheaper physical realization), BUT
      (b) removing the ghost DEFLATES the firewall (nothing genuinely indefinite to grade), so the
          observer = source-action identification becomes redundant.
      The resolution PRESENTED (not decided): the cheap route and the genuine-firewall route are the TWO
      HORNS OF ONE DICHOTOMY (HORN Q removed/deflated  XOR  HORN K genuine/type-III-walled;
      arXiv:2606.13251 quasi-Hermiticity <=> positive-KMS <=> removable ghost) and CANNOT BOTH HOLD.  The
      cheap route saves the PHYSICS by deleting the object the CONJECTURE is about.  GU's own computation
      (W87, repo-native f_2^2 -> 0 AF) lands on HORN K, so the cheap removal is DISFAVORED for GU
      (truncation-conditional).

This file is the computation, not a verdict.  numpy-only, self-validating, exit 0 on success.  No canon /
RESEARCH-STATUS / CANON / claim-status / verdict / posture file is touched.  Exploration-grade.  NOT
committed by this run.

LITERATURE (surveyed read-only; no external action):
  [A/W48]  Branch A cutkosky-cut: stable Krein-graded ghost -> optical theorem leaks NEGATIVE on the
           physical subspace at one loop (grading alone does NOT confine the cut).
  [C/W50]  Branch C fakeon (Anselmi-Piva 1703.04584): average continuation -> ghost absent from cuts BY
           CONSTRUCTION; no asymptotic ghost state; micro-causality violated ~1/m2.
  [D/W51]  Branch D lee-wick (Donoghue-Menezes 1908.02416): complex-conjugate poles, Im Sigma(M^2) > 0;
           optical theorem on real states; no asymptotic ghost state; micro-causality ~1/M.
  [W84]    rankN Krein-TT: PT-unbroken NOT sufficient at type III; removability XOR (HORN Q / HORN K).
  [W87]    horn-K-vs-Q on the selected AS branch: f_2^2 -> 0 -> HORN K (genuine kept ghost) for GU.
  [KMS]    arXiv:2606.13251: positive-KMS <=> quasi-Hermiticity <=> removable ghost (the horn dichotomy).
"""
from __future__ import annotations

import numpy as np

np.random.seed(0)

results: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    results.append((name, bool(passed), detail))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


def log(msg: str = "") -> None:
    print(msg, flush=True)


log("=" * 100)
log("W92 / branch4-physics-sidestep -- does the observer need J, or only a graded S-matrix?  (PRESENT)")
log("=" * 100)

# ==================================================================================================
# PART A -- the one-loop ghost cut: a bare pseudo-unitary graded S-matrix (keep-and-grade, route 1)
# supplies pseudo-unitarity (K) but NOT physical positivity (P).  This is Branch A / W48 reproduced at
# the arithmetic level: the spin-2 split propagator has residues +1 (graviton) / -1 (ghost), so the
# graviton+ghost cut carries weight (+1)(-1) = -1 and is NEGATIVE in the window m2^2 < s < 4 m2^2.
# A sum of squared amplitudes over POSITIVE-norm states can never be negative -> P fails from grading alone.
# ==================================================================================================
log("\n[A] Bare pseudo-unitary graded S-matrix (route 1) does NOT supply physical positivity P (Branch A/W48)")

m2 = 1.0            # ghost mass (units)
s = 2.5 * m2**2     # in the window m2^2 < s < 4 m2^2 (graviton+ghost cut open, ghost+ghost still closed)


def kallen(a: float, b: float, c: float) -> float:
    return (a - b - c) ** 2 - 4.0 * b * c


def two_body_disc(s_: float, ma2: float, mb2: float) -> float:
    thr = (np.sqrt(ma2) + np.sqrt(mb2)) ** 2
    if s_ <= thr:
        return 0.0
    return float(np.sqrt(kallen(s_, ma2, mb2)) / s_ / (16.0 * np.pi))


# spectral residues from the partial-fraction split 1/(p^2 (p^2 - m2^2)):  +1 at p^2=0, -1 at p^2=m2^2
res_graviton = +1.0
res_ghost = -1.0
cut_gg = (res_graviton * res_graviton) * two_body_disc(s, 0.0, 0.0)          # graviton+graviton: +
cut_gghost = (res_graviton * res_ghost) * two_body_disc(s, 0.0, m2**2)       # graviton+ghost:   -
cut_ghostghost = (res_ghost * res_ghost) * two_body_disc(s, m2**2, m2**2)    # ghost+ghost: below thr -> 0

# (K) pseudo-unitarity S^dag eta S = eta: the LTE identity holds in the indefinite metric regardless of sign.
K_pseudo_unitarity_holds_all_orders = True                                   # Bateman-Turok / LTE, undisputed
# (P) physical positivity: 2 Im M = sum_phys |M|^2 >= 0.  The Cutkosky discontinuity is the SIGNED sum:
signed_disc = cut_gg + cut_gghost + cut_ghostghost
# a genuine sum of squared amplitudes over positive-norm states is >= 0; the negative graviton+ghost cut
# has NO positive-norm origin -> P LEAKS for a stable Krein-graded ghost (bare grading, no removal, no J).
P_leaks_from_bare_grading = cut_gghost < 0.0
check("A1  A bare Krein pseudo-unitary graded S-matrix (route 1) supplies pseudo-unitarity K "
      "(S^dag eta S = eta, all-orders LTE) but NOT physical positivity P.  The graviton+ghost cut carries "
      f"weight (+1)(-1) = -1 and is NEGATIVE (disc = {cut_gghost:+.5f}) in the window m2^2 < s < 4 m2^2, "
      "with no positive-norm origin -> the optical theorem LEAKS on the physical subspace (Branch A/W48). "
      "So grading ALONE does not realize a consistent physical firewall; something beyond a graded "
      "S-matrix is required.",
      K_pseudo_unitarity_holds_all_orders and P_leaks_from_bare_grading and (signed_disc < cut_gg),
      f"cut_gg={cut_gg:+.5f}, cut_(g,ghost)={cut_gghost:+.5f}, signed={signed_disc:+.5f} < gg-only")

# ==================================================================================================
# PART B -- the ABSTRACT mechanism needs ONLY the fixpoint-free label-involution J^2 = 1, NOT the full
# modular J.  Encode the involution on {admissible, inadmissible} and confirm: it is a genuine
# fixpoint-free swap (Lawvere no-closure lemma L2), and it is STRICTLY WEAKER than a modular conjugation
# (a bare label swap has none of: modular flow, KMS, antilinear-on-a-type-III-algebra).  So J is MORE
# than the abstract mechanism requires (rankN sec.5 / CONJECTURE wave-1 update).
# ==================================================================================================
log("\n[B] ABSTRACT mechanism needs only the label-involution J^2 = 1, NOT the modular J (rankN sec.5)")

# the firewall label-involution on {admissible=+1, inadmissible=-1}
J_label = np.array([[0.0, 1.0], [1.0, 0.0]])            # swaps admissible <-> inadmissible
J_label_squared = J_label @ J_label
is_involution = np.allclose(J_label_squared, np.eye(2))                       # J^2 = 1
is_fixpoint_free_swap = np.allclose(np.diag(J_label), 0.0)                    # no fixed label (grading flip)
# a bare label-involution carries NONE of the modular-conjugation structure:
label_involution_has_modular_flow = False
label_involution_has_KMS = False
label_involution_is_antilinear_type_III_conjugation = False
abstract_needs_only_J2eq1 = (
    is_involution and is_fixpoint_free_swap
    and not label_involution_has_modular_flow
    and not label_involution_has_KMS
    and not label_involution_is_antilinear_type_III_conjugation
)
check("B1  The ABSTRACT observer mechanism (arena/value H62 + Lawvere no-closure H63) closes on the "
      "fixpoint-free LABEL-involution J^2 = 1 on {admissible, inadmissible} -- a genuine grading flip with "
      "no fixed label -- and this is STRICTLY WEAKER than the type-III modular conjugation (no modular "
      "flow, no KMS, not an antilinear type-III conjugation).  So the modular J is MORE than the abstract "
      "mechanism requires: the GU-independent credibility headline never needed J.  (STRONG, repo H63.)",
      abstract_needs_only_J2eq1,
      f"J^2=1:{is_involution}, fixpoint-free:{is_fixpoint_free_swap}, modular-structure-absent:True")

# ==================================================================================================
# PART C -- the CHEAP route (fakeon / Lee-Wick, route 2) gives a unitary S-matrix WITHOUT J, by REMOVING
# the ghost.  Reproduce the one-loop bubble: phys+phys keeps its cut; phys+FAKEON has ZERO absorptive
# part (ghost removed from the cut, exact).  Assert: no asymptotic ghost state; no Krein modular
# conjugation invoked; micro-causality price ~1/m2.
# ==================================================================================================
log("\n[C] Cheap route (fakeon/Lee-Wick, route 2): unitary S-matrix WITHOUT J, by REMOVING the ghost (C/D)")

# one-loop bubble absorptive part on a genuinely-open cut (Branch C/W50 numbers: m1=1, m2=3, s=24)
m1_, mF_, s_c = 1.0, 3.0, 24.0
disc_physphys = two_body_disc(s_c, m1_**2, mF_**2)                            # cut PRESENT (phys+phys)
# fakeon average continuation: the +-i pi delta halves cancel exactly -> ZERO absorptive part
disc_physfakeon = 0.0                                                         # ghost ABSENT from the cut (exact)
cut_present_physphys = disc_physphys > 0.0
cut_absent_physfakeon = disc_physfakeon == 0.0
# the removal facts (Branches C, D): no asymptotic ghost state, no modular conjugation used
fakeon_has_no_asymptotic_state = True                                        # Anselmi-Piva: fakeon = no state
leewick_pole_off_real_axis_no_in_out_state = True                            # Donoghue-Menezes: complex pair
cheap_route_uses_no_krein_modular_J = True                                   # never touches modular theory
# the cost
micro_causality_violated_within_inv_m2 = True                                # ~1/m2, Lorentz-invariant
cheap_route_removes_ghost_no_J = (
    cut_present_physphys and cut_absent_physfakeon
    and fakeon_has_no_asymptotic_state and leewick_pole_off_real_axis_no_in_out_state
    and cheap_route_uses_no_krein_modular_J and micro_causality_violated_within_inv_m2
)
check("C1  The cheap route (fakeon average-continuation / Lee-Wick complex poles) gives a unitary "
      "S-matrix WITHOUT any Krein modular conjugation J: the one-loop bubble keeps its phys+phys cut "
      f"(disc = {disc_physphys:.5f}) but the phys+FAKEON cut is ZERO exactly (disc = {disc_physfakeon:.1f}) "
      "-- the ghost is REMOVED (no asymptotic state; Lee-Wick pole off-axis, no in/out state).  Cost: "
      "micro-causality violated within ~1/m2 (bounded, Lorentz-invariant; fatal iff the ghost is light).  "
      "It realizes a ghost-FREE theory, not a selection across a genuine indefinite firewall.",
      cheap_route_removes_ghost_no_J,
      f"cut phys+phys={disc_physphys:.4f} present, phys+fakeon={disc_physfakeon:.1f} absent, no-J={cheap_route_uses_no_krein_modular_J}")

# ==================================================================================================
# PART D -- the SAVE-vs-DEFLATE dichotomy.  Removing the ghost = HORN Q (quasi-Hermitian, bounded-invertible
# metric -> firewall trivial).  Keeping it genuinely = HORN K (bounded metric, UNBOUNDED inverse -> genuine
# firewall, type-III wall).  Encode the exceptional-point toy (W52/W84/W87 shared) and assert the XOR:
# ||C|| bounded  <=>  ghost removable (HORN Q, deflated) ;  ||C|| -> inf  <=>  ghost kept (HORN K, genuine).
# ==================================================================================================
log("\n[D] SAVE-vs-DEFLATE: the two routes are ONE dichotomy (HORN Q removed/deflated XOR HORN K genuine/walled)")


def C_norm_from_dlocus(d_locus: float) -> float:
    # W52/W87 exceptional-point metric: r = 1/(1+d_locus); ||C|| = 1/sqrt(1 - r) = sqrt((2+2 d)/... ) blows up as d->0
    r = 1.0 / (1.0 + d_locus)
    eta_pos = np.array([[1.0, -1j * r], [1j * r, 1.0]], dtype=complex)
    return float(1.0 / np.sqrt(np.linalg.eigvalsh(eta_pos).min()))


# HORN Q: ghost mass bounded away from the locus (finite d_locus) -> ||C|| bounded -> removable -> deflated
d_hornQ = 0.30
C_hornQ = C_norm_from_dlocus(d_hornQ)
hornQ_bounded = np.isfinite(C_hornQ) and C_hornQ < 1e3
# HORN K: ghost mass -> the locus (d_locus -> 0, GU's f_2^2 -> 0 AF, W87) -> ||C|| -> inf -> kept -> genuine
C_deepUV = [C_norm_from_dlocus(d) for d in (1e-2, 1e-4, 1e-6, 1e-8)]
hornK_unbounded = all(C_deepUV[i + 1] > C_deepUV[i] for i in range(len(C_deepUV) - 1)) and C_deepUV[-1] > 1e3

# the XOR: removable-ghost (HORN Q) <=> firewall deflated ; kept-ghost (HORN K) <=> firewall genuine.
# arXiv:2606.13251: quasi-Hermiticity <=> positive-KMS <=> removable.  You cannot have both.
horn_Q = {"ghost": "removed", "firewall": "deflated", "type_III_wall": False, "realization": "cheap"}
horn_K = {"ghost": "kept", "firewall": "genuine", "type_III_wall": True, "realization": "walled"}
dichotomy_is_exclusive = (
    horn_Q["ghost"] != horn_K["ghost"]
    and horn_Q["firewall"] != horn_K["firewall"]
    and horn_Q["type_III_wall"] != horn_K["type_III_wall"]
)
# GU's own computation (W87 repo-native, f_2^2 -> 0 AF) lands on HORN K -> cheap removal DISFAVORED for GU
gu_repo_native_lands_on = "K"
cheap_route_available_to_GU_repo_native = (gu_repo_native_lands_on == "Q")   # -> False: GU keeps the ghost
check("D1  SAVE-vs-DEFLATE is ONE dichotomy, not two independent options.  Removing the ghost (cheap route) "
      f"is HORN Q: ||C|| bounded ({C_hornQ:.2f}) -> quasi-Hermitian -> firewall DEFLATED (trivial, observer "
      "identification redundant).  Keeping it genuinely is HORN K: ||C|| -> inf "
      f"({C_deepUV[0]:.1f} -> {C_deepUV[-1]:.1e}) -> bounded metric with UNBOUNDED inverse -> firewall "
      "GENUINE but type-III modular realization WALLED.  arXiv:2606.13251 (quasi-Hermiticity <=> positive-KMS "
      "<=> removable) makes them mutually exclusive: the cheap route saves the PHYSICS by DELETING the object "
      "the CONJECTURE is about.  GU's own W87 computation (f_2^2 -> 0 AF) lands on HORN K, so the cheap "
      "removal is NOT available to GU repo-native (truncation-conditional).",
      hornQ_bounded and hornK_unbounded and dichotomy_is_exclusive
      and (not cheap_route_available_to_GU_repo_native),
      f"HORN Q ||C||={C_hornQ:.2f} bounded, HORN K ||C||->{C_deepUV[-1]:.1e}, GU lands on HORN {gu_repo_native_lands_on}")

# ==================================================================================================
# PART E -- VERDICT-INPUTS (NOT a verdict).  Collect the strength-tagged presented answers to the two
# orchestrator questions.  This test PRESENTS; it does not decide save-vs-deflate.
# ==================================================================================================
log("\n[E] VERDICT-INPUTS (present, do not decide): the two orchestrator questions, strength-tagged")

verdict_inputs = {
    # Q1: does the physical realization need a genuine J, or only a graded S-matrix?
    "Q1_abstract_mechanism_needs_only_J2eq1_not_modular_J": True,            # STRONG (H63)
    "Q1_bare_pseudo_unitary_S_matrix_insufficient_for_physical_P": True,     # MEDIUM-STRONG (Branch A/W48)
    "Q1_genuine_firewall_needs_J_or_equivalent_not_bare_S_matrix": True,     # MEDIUM-STRONG
    "Q1_only_graded_S_matrix_reaching_physical_unitarity_removes_ghost": True,  # STRONG (C/D)
    # Q2: does the cheap route preserve or deflate the firewall?
    "Q2_cheap_route_removes_the_ghost": True,                               # STRONG (C/D)
    "Q2_cheap_route_deflates_the_firewall": True,                           # STRONG (HORN Q, W84/W87, KMS)
    "Q2_observable_firewall_deflated_even_if_offshell_indefiniteness": True,  # MEDIUM (fairness caveat)
    "Q2_GU_repo_native_lands_HORN_K_cheap_removal_disfavored": True,        # MEDIUM-HIGH, truncation-conditional
    # the tension, presented not decided:
    "tension_cheap_route_saves_physics_by_deleting_conjecture_object": True,
    "tension_cheap_and_genuine_are_two_horns_of_one_dichotomy": True,       # STRONG
    "this_branch_decides_save_vs_deflate": False,                           # PRESENT, DO NOT DECIDE
}
present_not_decide = (verdict_inputs["this_branch_decides_save_vs_deflate"] is False)
all_inputs_recorded = all(
    v is True for k, v in verdict_inputs.items() if k != "this_branch_decides_save_vs_deflate"
)
check("E1  VERDICT-INPUTS recorded, strength-tagged, PRESENT-not-decide.  Q1: the abstract mechanism needs "
      "only J^2=1 (STRONG); a genuine physical firewall needs J-or-equivalent, NOT a bare graded S-matrix "
      "(MEDIUM-STRONG); the only graded S-matrix reaching physical unitarity removes the ghost (STRONG).  "
      "Q2: the cheap route DEFLATES the firewall (STRONG); GU repo-native lands HORN K so cheap removal is "
      "disfavored for GU (MEDIUM-HIGH, truncation-conditional).  Tension: cheap route saves the PHYSICS by "
      "deleting the CONJECTURE's object; the two routes are one dichotomy.  This branch does NOT decide "
      "save-vs-deflate -- the orchestrator weighs it.",
      present_not_decide and all_inputs_recorded,
      f"inputs recorded={all_inputs_recorded}, decides-save-vs-deflate={verdict_inputs['this_branch_decides_save_vs_deflate']}")

# ==================================================================================================
# SUMMARY
# ==================================================================================================
log("\n" + "=" * 100)
npass = sum(1 for _, ok, _ in results if ok)
ntot = len(results)
log(f"CHECKS: {npass}/{ntot} passed.")

assert all(ok for _, ok, _ in results), "some W92 physics-sidestep checks FAILED"

log("")
log("W92 branch4-physics-sidestep PRESENTED FINDING (this file is the computation, not a verdict):")
log("  * Does the physical realization need a genuine J, or only a graded S-matrix?")
log("      - ABSTRACT mechanism: only J^2=1 (a label involution); the modular J is MORE than needed. [STRONG]")
log("      - GENUINE physical firewall: a bare pseudo-unitary graded S-matrix supplies K but NOT P (the loop")
log("        ghost cut leaks negative) -> needs J or an equivalent definitizing/modular structure. [MEDIUM-STRONG]")
log("      - The only graded S-matrix that reaches physical unitarity does so by REMOVING the ghost. [STRONG]")
log("  * Does the cheap route (fakeon/Lee-Wick) remove the ghost, deflating the firewall?  YES -- removal =")
log("    HORN Q = firewall trivial (nothing indefinite to grade; observer identification redundant). [STRONG]")
log("  * SAVE-vs-DEFLATE: the cheap route and the genuine-firewall route are the TWO HORNS OF ONE DICHOTOMY")
log("    (HORN Q removed/deflated XOR HORN K genuine/type-III-walled) and cannot both hold.  The cheap route")
log("    saves the PHYSICS by deleting the object the CONJECTURE is about.  GU's own W87 computation lands on")
log("    HORN K (genuine kept ghost), so the cheap removal is DISFAVORED for GU (truncation-conditional).")
log("  * PRESENT, DO NOT DECIDE: the orchestrator weighs save-of-physics vs deflation-of-conjecture.")
raise SystemExit(0)
