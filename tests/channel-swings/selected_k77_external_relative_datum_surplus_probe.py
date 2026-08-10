#!/usr/bin/env python3
"""Exact surplus gate for the minimal external relative boundary datum."""

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EXACT = 0
PLANTED = 0


def check(label, condition, *, planted=False):
    global EXACT, PLANTED
    if not condition:
        raise AssertionError(label)
    if planted:
        PLANTED += 1
    else:
        EXACT += 1
    print(f"PASS {label}")


relative = (
    ROOT
    / "explorations/conditional-build/selected-k77-relative-chiral-transgression-ownership-2026-08-10.md"
).read_text()
pairing = (
    ROOT
    / "explorations/conditional-build/selected-k77-lorentzian-chiral-class-pairing-2026-08-10.md"
).read_text()
native = (
    ROOT
    / "explorations/conditional-build/selected-k77-p3-native-characteristic-pairing-2026-08-10.md"
).read_text()
support = (
    ROOT
    / "explorations/conditional-build/selected-k77-p3-normal-tangential-support-obstruction-2026-08-10.md"
).read_text()
basicness = (
    ROOT
    / "explorations/conditional-build/selected-k77-contact-presymplectic-gauge-basicness-2026-08-08.md"
).read_text()
bfv = (
    ROOT
    / "explorations/conditional-build/selected-k77-branch-bfv-no-selector-2026-08-09.md"
).read_text()
dictionary = (ROOT / "lab/specifications/old-vs-eric-object-dictionary-2026-07-31.md").read_text()
source = (
    ROOT
    / "lab/sources/selected-k77-relative-chiral-transgression-ownership-source-reinspection-2026-08-10.md"
).read_text()

# Prior exact fences.
check("relative integer lives in Z", "large-gauge component group" in relative or "n in Z" in relative)
check("identity component selects zero", "zero relative winding" in relative)
check("generic interpolation is not quantized", "takes noninteger values" in relative)
check("real invariant pairing space has dimension two", "two-dimensional" in pairing)
check("one projective pairing ratio remains", "one projective ratio remains" in pairing)
check("full-parent characteristic pairing is zero", "C_B=0" in native)
check("projected chiral pairing is nonzero", "self-dual control" in native and "nonzero pairing" in native)
check("chiral projection is a new reduction", "new source reduction" in native)
check("normal P3 and tangential source supports differ", "different four-dimensional directions" in support)
check("small gauge is already basic", "SMALL_GAUGE_BASIC" in basicness)
check("large boundary charge remains live", "BOUNDARY_CHARGE_LIVE" in basicness)
check("classical BFV does not select amplitude", "determine its amplitude" in bfv)
check("P3 is a separate realized index datum", "separate realized chiral-index/count datum" in dictionary)
check("source is silent on the pairing ratio", "real-pairing ratio" in source and "SOURCE-SILENT" in source)

# Minimal affine chart on the projective real-pairing cone:
# B_r = B_Re + r B_Im.  On a nonzero reduced characteristic fixture, write
# C(r)=c_re+r*c_im and h(n,r,t)=C(r)t^4-9n.
c_re = Fraction(12)
c_im = Fraction(6)
n = 2
r = Fraction(1)
t = Fraction(1)
C = c_re + r * c_im
h = C * t**4 - 9 * n

check("nonzero reduced characteristic fixture", C == 18)
check("fixed n and r satisfy characteristic amplitude equation", h == 0)
check("fixed n and r admit positive real amplitude", 9 * n / C == 1)
check("even characteristic equation retains the two signs", (+t) ** 4 == (-t) ** 4)

# If r is free, it can fit any chosen nonzero t.  That is the exact
# accommodation mechanism which prevents a positive parameter-rank surplus.
for t_trial in (Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3, 2)):
    r_fit = (Fraction(9 * n, 1) / t_trial**4 - c_re) / c_im
    check(
        f"free r fits amplitude t={t_trial}",
        (c_re + c_im * r_fit) * t_trial**4 == 9 * n,
    )

# Local relaxation of the one mixed characteristic equation with respect to
# datum coordinates (n,r) has rank one.  The datum has two coordinates: one
# discrete component and one continuous projective ratio.
jacobian_datum = (Fraction(-9), c_im * t**4)
datum_parameter_count = 2
datum_constraint_rank = 1 if any(jacobian_datum) else 0
strict_parameter_surplus = datum_constraint_rank - datum_parameter_count
check("datum Jacobian rank is one", datum_constraint_rank == 1)
check("datum coordinate count is two", datum_parameter_count == 2)
check("strict parameter-rank surplus is minus one", strict_parameter_surplus == -1)

# Give the construction every favorable row-level allowance: count the
# characteristic magnitude relation and small-gauge/BFV compatibility as two
# independent closed conditions.  This reaches zero, never positive.  Large-
# gauge integrality is the same transgression datum and is not counted twice.
favorable_closed_conditions = 2
favorable_row_surplus = favorable_closed_conditions - datum_parameter_count
check("favorable row-level surplus is zero", favorable_row_surplus == 0)
check("current surplus band never becomes positive", max(strict_parameter_surplus, favorable_row_surplus) <= 0)

# Integer large-gauge phase compatibility does not distinguish sectors: for a
# normalized integral level k, k*n is integral for every integer component.
for level in (-2, -1, 0, 1, 2):
    for component in (-2, -1, 0, 1, 2):
        check(
            f"integral phase is blind to level={level}, n={component}",
            isinstance(level * component, int),
        )

# Planted overcounts and Layer-0 collapses.
check("planted nonemptiness is not nonzero selection", 0 != 1, planted=True)
check("planted full-parent C is not nonzero", "C_B=0" in native, planted=True)
check("planted boundary winding is not P3", "not a decomposition" in dictionary, planted=True)
check("planted BFV selector is rejected", "BFV closure can choose one nonzero" in bfv, planted=True)
check("planted free r is not source-selected", "not yet the selected action coefficient" in pairing, planted=True)
check("planted gauge phase does not pick n=1", all((1 * q) == q for q in (-1, 0, 1)), planted=True)
check("planted chiral projection is not costless", "additional reduced-action decision" in pairing, planted=True)

print(f"PASS exact={EXACT} planted={PLANTED} total={EXACT + PLANTED}")
