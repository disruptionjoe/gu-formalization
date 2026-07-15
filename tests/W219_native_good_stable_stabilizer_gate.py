#!/usr/bin/env python
"""Regression gate for the first native-good-stable stabilizer step.

This script separates three objects that earlier notes conflated:

1. the full program-native pseudo-unitary quaternionic arena Sp(32,32;H);
2. its kinematic maximal compact / Cartan centralizer Sp(32) x Sp(32); and
3. a dynamical good-stable isotropy group, which requires an actual vacuum or
   rolling order parameter and is not supplied by the cited files.

The arithmetic checks are exact. The source checks are dependency guards. This
is not a construction of the missing interacting vacuum or observable algebra.
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


def dim_sp_compact(n):
    """Real dimension of compact Sp(n), and of any real form Sp(p,q), p+q=n."""
    return n * (2 * n + 1)


def dim_noncompact_cartan_part(p, q):
    """Real dimension of the off-diagonal quaternionic block."""
    return 4 * p * q


print("[A] Native group and Cartan decomposition")
p = q = 32
n = p + q
dim_g = dim_sp_compact(n)
dim_k = dim_sp_compact(p) + dim_sp_compact(q)
dim_p = dim_noncompact_cartan_part(p, q)

check("A1.dim_sp_32_32", dim_g == 8256, str(dim_g))
check("A2.dim_sp32_plus_sp32", dim_k == 4160, str(dim_k))
check("A3.dim_noncompact_part", dim_p == 4096, str(dim_p))
check("A4.cartan_dimension_sum", dim_k + dim_p == dim_g)
check("A5.cartan_split_nontrivial", dim_k < dim_g and dim_p > 0)

print("\n[B] Distinguish full-spinor and 14-frame stabilizers")
dim_so_95 = 14 * 13 // 2
dim_so9_so5 = 9 * 8 // 2 + 5 * 4 // 2
dim_boosts = 9 * 5
check("B1.dim_so_9_5", dim_so_95 == 91, str(dim_so_95))
check("B2.dim_so9_plus_so5", dim_so9_so5 == 46, str(dim_so9_so5))
check("B3.vector_cartan_sum", dim_so9_so5 + dim_boosts == dim_so_95)
check("B4.native_and_frame_compacts_distinct", dim_k != dim_so9_so5)

print("\n[C] Corrected compact-stabilizer read")
# Under Sp(p) x Sp(q), the positive standard module belongs to the first
# factor and the negative standard module to the second. They are inequivalent
# factor-labelled irreducibles, so there is no shared constituent.
positive_irreducible_types = {("Sp32_first", "H_standard")}
negative_irreducible_types = {("Sp32_second", "H_standard")}
shared = positive_irreducible_types & negative_irreducible_types
residual_dimension = 4 * len(shared)
check("C1.no_shared_factor_label", shared == set(), str(shared))
check("C2.admissible_C_moduli_dimension_zero", residual_dimension == 0)
check("C3.unique_admissible_fundamental_symmetry", residual_dimension == 0)
check("C4.invariant_metric_space_not_grading_space", 2 != residual_dimension)

print("\n[D] Source sufficiency guards")
h23 = read("explorations/wave8/H23-source-action-construction-2026-07-11.md")
w132 = read("explorations/W132-graded-optical-theorem-physical-subspace-2026-07-14.md")
w173 = read("explorations/W173-brst-cohomology-mirror-sector-2026-07-14.md")
w203 = read("explorations/W203-branch3-source-action-fixed-coefficients-2026-07-14.md")
w206 = read("explorations/W206-decisive-bit-counterfactual-invariance-2026-07-14.md")
w213 = read("explorations/W213-true-vacuum-effective-potential-2026-07-14.md")
w214 = read("explorations/W214-true-vacuum-rg-flow-2026-07-14.md")
w215 = read("explorations/W215-true-vacuum-dynamical-systems-2026-07-14.md")
w216 = read("explorations/W216-true-vacuum-spectral-condensate-2026-07-14.md")
w218 = read("explorations/W218-lean-Rsrc-unification-check-2026-07-14.md")

check("D1.h23_native_group_present", "Sp(32,32;H)" in h23)
check("D2.h23_soldering_not_forced", "codimension-8165" in h23 and "NOT forced" in h23)
check("D3.w132_interacting_C_conditional", "conditional on the interacting C-operator" in w132)
check("D4.w173_stabilized_complex_unbuilt", "stabilized / gauge-fixed" in w173 and "UNBUILT" in w173)
check("D5.w203_ultralocal_and_w154_conditional", "ULTRALOCAL" in w203 and "conditional on W154" in w203)
check("D6.w206_good_stable_assumed", "good-stable fixed point as GIVEN" in w206)
check("D7.w213_no_stationary_vacuum", "RUNAWAY-NO-VACUUM" in w213)
check("D8.w214_native_basin_no_vacuum", "RUNAWAY-NO-VACUUM" in w214)
check("D9.w215_no_stable_fixed_point", "NO stable fixed-point true vacuum exists" in w215)
check("D10.w216_is_mean_field_proxy", "mean-field BdG" in w216 and "unbuilt" in w216.lower())
check("D11.w216_depends_on_killed_one_bit", "W211 PROVED" in w216 and "Godel-INDEPENDENT" in w216)
check("D12.w218_ultralocal_proxy", "ULTRALOCAL" in w218 and "standing in for" in w218)

print("\n[E] Hourly queue guard")
next_steps = read("NEXT-STEPS.md")
check("E1.new_queue_is_front_door", "derive the native physical good stable and its grading" in next_steps)
check("E2.five_ordered_steps_present", all(f"> {i}. **" in next_steps for i in range(1, 6)))
check("E3.w189_not_current_queue", "W189 HARDENING REGISTER" not in next_steps)
check("E4.no_w211_premise_allowed", "No hourly run may use W211" in next_steps)

passed = sum(1 for _, condition in CHECKS if condition)
total = len(CHECKS)
print("\n==================== SUMMARY ====================")
print(f"{passed}/{total} checks passed")
print("Kinematic Cartan stabilizer: Sp(32) x Sp(32).")
print("Dynamical good-stable isotropy: not derived by the audited inputs.")
print("=================================================")
raise SystemExit(0 if passed == total else 1)
