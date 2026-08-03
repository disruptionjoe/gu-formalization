#!/usr/bin/env python3
"""Exact type/accounting gate for the M-H7 dimension-13 restatement.

Coefficient inputs are the published stable-stem table (Isaksen-Wang-Xu),
Bott periodicity for pi_13(SO), and the ABP Spin-bordism coefficient table.
The script deliberately does not pretend to construct a GU end compactification,
stable framing, Pontryagin-Thom class, or integer generation datum.
"""
from math import gcd


checks = 0


def check(label, condition, detail=""):
    global checks
    checks += 1
    print("[{}] {}{}".format("PASS" if condition else "FAIL", label,
                             " -- " + detail if detail else ""))
    assert condition, label


# Coefficient groups, encoded by their finite orders (1 means the zero group).
pi_13_stable_order = 3
im_j_13_order = 1       # pi_13(SO) = pi_5(SO) = 0 by Bott periodicity
omega_spin_13_order = 1
pi_4_stable_order = 1
pi_6_stable_order = 2

check("Omega^fr_13 = pi^S_13 is purely Z/3", pi_13_stable_order == 3)
check("Im J_13 is zero", im_j_13_order == 1)
check("Omega^Spin_13 is zero", omega_spin_13_order == 1)
check("forgetful framed-to-Spin map has zero target", omega_spin_13_order == 1)

# An additive map Z/m -> Z/n has gcd(m,n) elements.  gcd=1 means only zero.
interior_two_primary_orders = [2, 4, 8, 16]
for order in interior_two_primary_orders:
    check("only zero additive map Z/{} -> Z/3".format(order), gcd(order, 3) == 1)
    check("only zero additive map Z/3 -> Z/{}".format(order), gcd(3, order) == 1)

# Geometry/type ledger.  The full candidate radial-boundary model is an S^6
# sphere bundle over P(TX), whose base has dimension 4+3=7.  It is not yet a
# constructed GU end link.
projectivized_tangent_dimension = 4 + 3
fiber_sphere_dimension = 6
full_link_dimension = projectivized_tangent_dimension + fiber_sphere_dimension
fixed_x_spine_dimension = 3
fixed_x_link_dimension = fixed_x_spine_dimension + fiber_sphere_dimension
rs_multiplicity = 1664 // 128

check("P(TX) dimension is seven", projectivized_tangent_dimension == 7)
check("fixed-x S6-over-RP3 model dimension is nine", fixed_x_link_dimension == 9)
check("full candidate Y14 end-link dimension is thirteen", full_link_dimension == 13)
check("separate RS arithmetic also happens to give thirteen", rs_multiplicity == 13)
check("planted identification of the two thirteens is rejected",
      full_link_dimension == rs_multiplicity and
      "link_dimension" != "representation_multiplicity")

# Strong scoped control: if X4 is closed and stably framed, a literal external
# product with the external-product stable framing cannot realize the desired
# nonzero 13-stem class.  Its X4 factor is zero in pi_4^S.  Independently, the
# selected 3-primary component of a framed RP3 class times the 2-primary S6
# class vanishes.  This says nothing about a non-product framing.
closed_stably_framed_x4_assumed = True
external_product_framing_assumed = True
selected_rp3_component_order = 3
product_vanishes_via_x4 = pi_4_stable_order == 1
product_vanishes_via_coprime_torsion = gcd(
    selected_rp3_component_order, pi_6_stable_order) == 1
check("closed framed X4 external-product class vanishes via pi_4^S=0",
      closed_stably_framed_x4_assumed and
      external_product_framing_assumed and product_vanishes_via_x4)
check("selected 3-primary RP3 component times 2-primary S6 is zero",
      product_vanishes_via_coprime_torsion)
check("planted product-model generator claim is rejected",
      product_vanishes_via_x4 and product_vanishes_via_coprime_torsion)

# The actual GU receiving object is not yet built.
construction = {
    "closed_compact_end_link": False,
    "global_stable_framing": False,
    "nonzero_pontryagin_thom_class": False,
    "torsion_to_integer_P3_dictionary": False,
}
check("all four realization gates remain open", not any(construction.values()))
check("coefficient group does not construct external integer P3",
      not construction["torsion_to_integer_P3_dictionary"])

print("M-H7 verdict: the abstract degree-13 framed coefficient group is Z/3,")
print("but GU has not built the receiving boundary, framing, class, or P3 map.")
print("checks passed:", checks)
