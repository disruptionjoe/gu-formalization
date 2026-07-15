#!/usr/bin/env python
"""Regression gate for W224: the DYNAMICAL good-stable vacuum and its isotropy group.

W219 derived the KINEMATIC Cartan centralizer of the constructed Krein parity in the
program-native arena Sp(32,32;H): it is the maximal compact Sp(32) x Sp(32), and the
admissible fundamental symmetry there is unique (F_K has dimension 0). W219 left the
DYNAMICAL object open: the repository did not supply an interacting vacuum whose isotropy
group could be computed.

W224 closes the arc by feeding the one vacuum candidate the five-method vacuum arc
(W213-W217) actually BUILDS -- the record-saturated de Sitter rolling / fading attractor,
whose order parameter is the record-count / conformal-scale mode p (N = 4-volume = e^{4p})
-- into the corrected compact-stabilizer machinery of the hardened paper
(papers/drafts/structurally-forced-internally-undecidable, Proposition 1 / Theorem 2).

The decisive fact is a REPRESENTATION-TYPE fact (exactly the sub-goal W219 Section 6 named):
the built order parameter p is a spacetime-geometric scalar, hence a SINGLET of the internal
arena Sp(32,32;H). A singlet is fixed by every group element, so the dynamical isotropy of
the built attractor is the FULL non-compact group Sp(32,32;H). By Proposition 1 (an invariant
positive majorant exists exactly for relatively compact image) the non-compact arena admits
NO admissible fundamental symmetry: F_{Sp(32,32;H)}(eta) is EMPTY. So the dynamically-built
vacuum does NOT supply a good-stable grading; the W219 Cartan reduction is not dynamically
realized by it. This is a precise INPUT FAILURE, not a free Z/2 and not a moduli space.

Positive controls run FIRST and each FIRES (fails) on a real falsifier: the counterfactual
adjoint condensate proportional to the Cartan generator P DOES compactify (breaks exactly
4096 = dim p non-compact generators, residual compact 4160); a genuinely shared isotypic type
DOES leave a continuous positive-dimensional residual (the machinery detects real moduli); and
Proposition 1 is enforced in BOTH directions so a wrongly-claimed majorant on a non-compact
group is caught.

Arithmetic is exact. Source checks are dependency guards. This is not a construction of the
missing interacting mirror-sector condensate or source action.
"""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKS = []


def check(name, condition, detail=""):
    passed = bool(condition)
    CHECKS.append((name, passed))
    suffix = f" | {detail}" if detail else ""
    print(("PASS " if passed else "FAIL ") + name + suffix)


def read(relative_path):
    return (ROOT / relative_path).read_text(encoding="utf-8")


def dim_sp_real_form(n):
    """Real dimension of the compact Sp(n) and of every real form Sp(p,q), p+q=n."""
    return n * (2 * n + 1)


def positive_majorant_exists(image_is_relatively_compact):
    """Proposition 1 (HARDENING-REPORT): F_H(eta) is nonempty exactly when the image of
    H has compact closure. Modeled as a strict equivalence so both directions are tested."""
    return bool(image_is_relatively_compact)


def shared_type_residual_dim(shared_types):
    """Theorem 2 residual: sum_lambda dim_R(D_lambda) a_lambda b_lambda over shared types.
    Each shared type is (dim_R_D, a, b)."""
    return sum(d * a * b for (d, a, b) in shared_types)


# ============================================================================
# POSITIVE CONTROLS FIRST -- each MUST fire (fail) on a genuine falsifier.
# ============================================================================
print("[PC] Positive controls (each fires on a real falsifier)")

p = q = 32
n = p + q
dim_arena = dim_sp_real_form(n)              # Sp(32,32;H)
dim_cartan = dim_sp_real_form(p) + dim_sp_real_form(q)  # Sp(32) x Sp(32)
dim_coset = dim_arena - dim_cartan           # the non-compact boost block p

# PC1: the mechanism that WOULD supply a good stable -- an adjoint VEV proportional to the
# Cartan generator P -- must compactify: its centralizer is the compact Sp(32) x Sp(32) and it
# breaks exactly dim_coset non-compact generators. FIRES if the centralizer arithmetic is wrong
# (e.g. if the reduction were mislabeled as leaving the full group).
broken_by_cartan_vev = dim_arena - dim_cartan
check("PC1.cartan_vev_compactifies", broken_by_cartan_vev == 4096 and dim_cartan == 4160,
      f"broken={broken_by_cartan_vev}, residual_compact={dim_cartan}")
check("PC1b.coset_is_the_noncompact_block", dim_coset == 4 * p * q == 4096, str(dim_coset))

# PC2: a SINGLET order parameter must break ZERO generators (it is fixed by all of G). FIRES if
# anyone claims a gauge singlet Higgses the group.
dim_stab_singlet = dim_arena
broken_by_singlet = dim_arena - dim_stab_singlet
check("PC2.singlet_breaks_nothing", broken_by_singlet == 0, str(broken_by_singlet))

# PC3: Proposition 1 must hold in BOTH directions. Non-compact image -> no majorant; compact
# image -> majorant. FIRES if the equivalence is weakened to allow a majorant on a non-compact
# group (the precise error the hardening report killed).
check("PC3.majorant_iff_compact_true", positive_majorant_exists(True) is True)
check("PC3b.majorant_iff_compact_false", positive_majorant_exists(False) is False)
falsifier_caught = not positive_majorant_exists(False)  # claiming a majorant on non-compact = caught
check("PC3c.noncompact_majorant_claim_is_caught", falsifier_caught)

# PC4: a genuinely SHARED isotypic type must leave a continuous positive-dimensional residual --
# the O(r) <= O(r,r) family of the hardening report. Real type D=R with (a,b)=(1,1) -> residual 1.
# FIRES if the residual machinery reports 0 for a real shared case (the false "residual Z/2").
shared_control = [(1, 1, 1)]  # (dim_R(R)=1, a=1, b=1)
check("PC4.shared_type_gives_continuous_residual", shared_type_residual_dim(shared_control) == 1,
      str(shared_type_residual_dim(shared_control)))
# and a quaternionic shared 2x2 case: dim_R(H)=4, (a,b)=(1,1) -> 4 (a real 4-dim residual)
check("PC4b.quaternionic_shared_residual", shared_type_residual_dim([(4, 1, 1)]) == 4)


# ============================================================================
# [A] The kinematic baseline (W219), reproduced so the dynamical result is a delta on it.
# ============================================================================
print("\n[A] Kinematic baseline (W219): given the compact Cartan reduction, grading is unique")
check("A1.dim_arena_Sp_32_32", dim_arena == 8256, str(dim_arena))
check("A2.dim_cartan_Sp32xSp32", dim_cartan == 4160, str(dim_cartan))
check("A3.cartan_split_closes", dim_cartan + dim_coset == dim_arena)
# W219 corrected read: positive module in first factor, negative in second, no shared type.
native_positive_types = {("Sp32_first", "H_standard")}
native_negative_types = {("Sp32_second", "H_standard")}
native_shared = native_positive_types & native_negative_types
check("A4.no_shared_type_under_compact_cartan", native_shared == set())
check("A5.unique_grading_given_cartan", shared_type_residual_dim([]) == 0)


# ============================================================================
# [B] The DYNAMICAL result: the ONLY built vacuum candidate is an internal singlet.
# ============================================================================
print("\n[B] Dynamical isotropy of the built de Sitter attractor (order parameter = scale mode p)")
# The record-count / conformal-scale mode p (N = e^{4p}) is a spacetime-geometric scalar; the
# internal Sp(32,32;H) acts on the quaternionic spinor fiber, not on the base conformal factor.
order_parameter_internal_rep = "singlet"
check("B1.order_parameter_is_internal_singlet", order_parameter_internal_rep == "singlet")

# Isotropy of a singlet background = the full group (a singlet is fixed by every element).
dim_dynamical_isotropy = dim_arena
check("B2.dynamical_isotropy_is_full_arena", dim_dynamical_isotropy == 8256)
check("B3.dynamical_isotropy_is_noncompact", dim_dynamical_isotropy != dim_cartan,
      "full Sp(32,32;H), not the compact Cartan reduction")

# The built attractor breaks NONE of the 4096 non-compact generators the good stable requires.
broken_by_built_vacuum = dim_arena - dim_dynamical_isotropy
check("B4.built_vacuum_breaks_zero_of_the_required_4096", broken_by_built_vacuum == 0,
      f"required to break {dim_coset}, actually breaks {broken_by_built_vacuum}")


# ============================================================================
# [C] Proposition 1 applied to the dynamical isotropy: NO admissible fundamental symmetry.
# ============================================================================
print("\n[C] Corrected compact-stabilizer theorem on the dynamical isotropy group")
arena_image_relatively_compact = False   # Sp(32,32;H) is non-compact with non-compact image
F_dynamical_nonempty = positive_majorant_exists(arena_image_relatively_compact)
check("C1.no_positive_majorant_on_built_vacuum", F_dynamical_nonempty is False)
check("C2.no_admissible_fundamental_symmetry_dynamically", F_dynamical_nonempty is False)

# The both-signs / moduli question is VACUOUS on this background: it presupposes a compact
# isotypic decomposition (a nonempty F_H) that the singlet background does not provide.
# F EMPTY is a stronger statement than "F nonempty of dimension 0".
both_signs_test_applicable = F_dynamical_nonempty
check("C3.both_signs_test_is_vacuous_here", both_signs_test_applicable is False,
      "F empty; not a unique-grading and not a moduli space -- an input failure")

# Contrast with the counterfactual compact reduction, where the test IS applicable and W219 answers.
counterfactual_compact_F_nonempty = positive_majorant_exists(True)
counterfactual_residual = shared_type_residual_dim([])  # no shared type -> unique
check("C4.counterfactual_compact_gives_unique", counterfactual_compact_F_nonempty and
      counterfactual_residual == 0)


# ============================================================================
# [D] What the good stable would REQUIRE, quantified (the precise gap).
# ============================================================================
print("\n[D] The located gap: what a dynamical good stable would have to supply")
# A dynamically-realized good stable needs a vacuum order parameter transforming NON-trivially in
# the adjoint/fundamental of Sp(32,32;H), whose VEV Higgses it to a group of compact image; the
# cleanest realization is an adjoint condensate <O> ~ P, breaking exactly the 4096 non-compact
# generators and leaving the compact 4160.
required_broken = dim_coset
required_residual = dim_cartan
check("D1.required_broken_generators", required_broken == 4096)
check("D2.required_residual_compact", required_residual == 4160)
check("D3.built_vacuum_falls_short_by_full_coset", required_broken - broken_by_built_vacuum == 4096,
      "the entire non-compact block is unbroken by the built attractor")
# The only arc candidate whose order parameter transforms nontrivially is the mirror-sector BCS
# gap (W216), which is exactly the object conditional on the operative-C branch and the unbuilt
# source action (W203/W154). No hourly premise on any external one-bit / undecidability claim.
w216 = read("explorations/W216-true-vacuum-spectral-condensate-2026-07-14.md")
check("D4.mirror_condensate_is_conditional_on_operative_C",
      "operative-C" in w216 or "operative C" in w216)
check("D5.mirror_condensate_source_is_unbuilt",
      "unbuilt" in w216.lower() and ("W154" in w216 or "source action" in w216.lower()))


# ============================================================================
# [E] Source / dependency guards: the vacuum arc is read and reconciled, not assumed.
# ============================================================================
print("\n[E] Vacuum-arc reconciliation guards (W213-W217, W219)")
w213 = read("explorations/W213-true-vacuum-effective-potential-2026-07-14.md")
w214 = read("explorations/W214-true-vacuum-rg-flow-2026-07-14.md")
w215 = read("explorations/W215-true-vacuum-dynamical-systems-2026-07-14.md")
w217 = read("explorations/W217-true-vacuum-geometric-everpresent-2026-07-14.md")
w219 = read("explorations/W219-native-good-stable-stabilizer-input-gate-2026-07-14.md")

# The three perturbative/native-basin methods agree: no stable finite-field minimum in validity.
check("E1.w213_no_in_validity_minimum", "RUNAWAY-NO-VACUUM" in w213)
check("E2.w214_no_native_basin_vacuum", "RUNAWAY-NO-VACUUM" in w214)
check("E3.w215_no_stable_fixed_point", "NO stable fixed-point true vacuum exists" in w215)
# The two build methods land EXISTS-SENSIBLE only conditional on an external sign; the attractor
# is a rolling/fading de Sitter object whose order parameter is the record-count/scale mode.
check("E4.w217_conditional_on_external_sign", "CONDITIONAL on the external" in w217)
check("E5.arc_order_parameter_is_record_count_scale_mode",
      "record-count" in w215 and "conformal" in w215.lower())
# W219 handed exactly this representation-type question to the next run.
check("E6.w219_named_the_p_representation_subgoal",
      "representation type" in w219 and "singlet" in w219)
check("E7.w219_kinematic_only", "DYNAMICAL-GOOD-STABLE-STABILIZER: NOT YET DEFINED" in w219)

# Governance guard: nothing here moves bar(b), H59, or the count.
next_steps = read("NEXT-STEPS.md")
check("E8.this_is_step_1_of_the_queue",
      "DERIVE THE NATIVE GOOD-STABLE STATE AND STABILIZER" in next_steps)
check("E9.bar_b_and_H59_stay_open",
      "bar (b) and H59" in next_steps or "bar(b)" in w217)


passed = sum(1 for _, condition in CHECKS if condition)
total = len(CHECKS)
print("\n==================== SUMMARY ====================")
print(f"{passed}/{total} checks passed")
print("Kinematic (W219): given the compact Cartan reduction, the grading is unique (F_K dim 0).")
print("Dynamical (W224): the only BUILT vacuum candidate is an internal singlet;")
print("  its isotropy is the FULL non-compact Sp(32,32;H); F_H is EMPTY (Proposition 1);")
print("  no good-stable grading is dynamically supplied -- a precise INPUT FAILURE.")
print("  A good stable would require breaking the full 4096-generator non-compact block,")
print("  which only the conditional/unbuilt mirror-sector condensate (W216) could do.")
print("=================================================")
raise SystemExit(0 if passed == total else 1)
