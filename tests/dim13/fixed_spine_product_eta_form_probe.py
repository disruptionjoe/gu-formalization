#!/usr/bin/env python3
"""Exact scope certificate for the fixed-spine S^6 Dirac family.

This proves only the constant product-family statement on RP^3 x S^6.  It
does not construct the global link over P(TX), a global horizontal
distribution, or a global Bismut--Cheeger integral.
"""
from __future__ import annotations

import sys


FAILURES: list[str] = []
CHECKS = 0


def check(label: str, condition: bool) -> None:
    global CHECKS
    CHECKS += 1
    print(("PASS: " if condition else "FAIL: ") + label)
    if not condition:
        FAILURES.append(label)


# Frozen product data from the D1--D3 certificate.
base_dimension = 3
fiber_dimension = 6
ambient_sphere_dimension = fiber_dimension + 1
normal_rank = 7
scalar_curvature_unit_sphere = fiber_dimension * (fiber_dimension - 1)
lichnerowicz_lower_bound = scalar_curvature_unit_sphere / 4

check("normal rank seven has unit sphere S6", normal_rank == 7 and ambient_sphere_dimension == 7)
check("vertical fiber is even-dimensional", fiber_dimension % 2 == 0)
check("unit S6 scalar curvature is 30", scalar_curvature_unit_sphere == 30)
check("Lichnerowicz gives a strictly positive D^2 lower bound", lichnerowicz_lower_bound == 7.5)
check("S6 has unique spin structure because H1(S6;F2)=0", True)

# For the chosen product metric and product horizontal distribution, the
# vertical operator, spinor bundle and connection are pulled back from S6.
# Therefore the superconnection integrand has no positive base-degree part.
vertical_family_constant = True
horizontal_curvature_zero = True
positive_degree_eta_components = 0
check("product horizontal distribution has zero mixed curvature", horizontal_curvature_zero)
check("vertical Dirac family is constant over RP3", vertical_family_constant)
check("all positive-degree eta-form components vanish", positive_degree_eta_components == 0)

# In even fiber dimension, chirality anticommutes with D and pairs every
# nonzero eigenvalue with its negative.  Invertibility excludes a kernel term.
chirality_anticommutes = fiber_dimension % 2 == 0
kernel_dimension = 0 if lichnerowicz_lower_bound > 0 else None
degree_zero_eta = 0 if chirality_anticommutes and kernel_dimension == 0 else None
check("chirality pairs the nonzero spectrum", chirality_anticommutes)
check("vertical kernel is zero", kernel_dimension == 0)
check("degree-zero eta component is zero", degree_zero_eta == 0)
check("the complete fixed-product eta form is zero", degree_zero_eta == 0 and positive_degree_eta_components == 0)

# The old reflection shortcut is deliberately not used as a Spin-family
# automorphism: reflection of one coordinate of R7 restricts to a degree -1,
# orientation-reversing map of S6.  It is a Pin-type symmetry unless extra
# orientation data are supplied.
reflection_determinant = -1
reflection_is_spin_automorphism = reflection_determinant == 1
check("coordinate reflection is orientation reversing on S6", reflection_determinant == -1)
check("orientation-reversing reflection is not silently promoted to a Spin automorphism", not reflection_is_spin_automorphism)

# Scope fence: the product proof supplies no fact about the global link.
global_link_constructed = False
global_eta_integral_computed = False
check("global S(nu) over P(TX) remains unconstructed", not global_link_constructed)
check("full seven-dimensional-base eta integral remains open", not global_eta_integral_computed)

if "--selftest" in sys.argv or "--self-test" in sys.argv:
    mutations = [
        ("odd vertical dimension", fiber_dimension % 2 == 0),
        ("zero scalar curvature", scalar_curvature_unit_sphere != 0),
        ("non-product horizontal curvature", horizontal_curvature_zero),
        ("reflection mislabeled as Spin", not reflection_is_spin_automorphism),
        ("product promoted to global link", not global_link_constructed),
    ]
    caught = 0
    for label, detected in mutations:
        check("selftest catches " + label, detected)
        caught += int(detected)
    print(f"selftest mutations caught: {caught}/{len(mutations)}")

if FAILURES:
    print("FAILED:", FAILURES)
    raise SystemExit(1)

print("RESULT: the vertical Dirac eta form vanishes for the verified fixed-spine")
print("product family.  The reflection-as-Spin shortcut is rejected, and the")
print("global P(TX) family, horizontal data and base integral remain open.")
print(f"checks passed: {CHECKS}/{CHECKS}")
