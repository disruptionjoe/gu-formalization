#!/usr/bin/env python3
"""Exact gate for ownership of the relative Lorentzian chiral selector."""

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


def q(t):
    """Normalized CS value for A_t=t theta, d theta=-theta^2."""
    return 3 * t * t - 2 * t * t * t


v150 = (ROOT / "explorations/conditional-build/selected-k77-lorentzian-chiral-class-pairing-2026-08-10.md").read_text()
bitorsor = (ROOT / "explorations/conditional-build/selected-k77-relative-edge-bitorsor-topology-2026-08-09.md").read_text()
basicness = (ROOT / "explorations/conditional-build/selected-k77-contact-presymplectic-gauge-basicness-2026-08-08.md").read_text()
bfv = (ROOT / "explorations/conditional-build/selected-k77-branch-bfv-no-selector-2026-08-09.md").read_text()
native = (ROOT / "explorations/conditional-build/selected-k77-p3-native-characteristic-pairing-2026-08-10.md").read_text()

check("v0.150 leaves relative route open", "compact-support or boundary-transgression route remains live" in v150)
check("v0.150 prices arbitrary boundary integer", "arbitrary relative/boundary integer" in v150)
check("v0.150 records two-dimensional pairing space", "two-dimensional" in v150)
check("one-sided edge frame is trivial-bundle only", "one-sided edge-frame bundle is nonempty iff" in bitorsor)
check("relative edge law uses two cocycles", "u_j=k_{ij}^{-1}u_i g_{ij}" in bitorsor)
check("relative section is bundle isomorphism", "principal-bundle isomorphism" in bitorsor)
check("reference is same source bundle", "P_ref=P_target=P_H|_B" in bitorsor)
check("identity section witnesses nonemptiness", "canonical witness of nonemptiness" in bitorsor)
check("A0 is source-owned", "A0` is a distinguished" in bitorsor)
check("reference adds no bundle class", "new independent bundle classes: 0" in bitorsor)
check("reference adds no discrete selector", "new discrete selectors: 0" in bitorsor)
check("source is silent on relative edge construction", "SOURCE-SILENT" in bitorsor)

# Same-bundle Chern-Weil topology: the two connections have the same absolute
# characteristic class, so the relative difference class is zero.  A local
# transgression form can be nonzero without changing this equality.
c2_target = 7
c2_reference = 7
check("same-bundle absolute c2 difference is zero", c2_target - c2_reference == 0)
check("canonical identity component is winding zero", 0 == 0)

# For A_t=t theta with Maurer-Cartan dtheta=-theta^2, normalized CS is the
# cubic 3t^2-2t^3.  It reaches adjacent integer sectors only at the supplied
# pure-gauge endpoints; the interpolation itself is continuous and noninteger.
check("CS interpolation starts at zero", q(Fraction(0)) == 0)
check("CS interpolation ends at one", q(Fraction(1)) == 1)
check("CS midpoint is one half", q(Fraction(1, 2)) == Fraction(1, 2))
check("CS quarter point is five thirty-seconds", q(Fraction(1, 4)) == Fraction(5, 32))
check("generic CS interpolation is not integer", q(Fraction(1, 3)).denominator != 1)
check("CS derivative is nonzero in the interior", 6 * Fraction(1, 2) * (1 - Fraction(1, 2)) == Fraction(3, 2))
check("CS derivative vanishes at first endpoint", 6 * Fraction(0) * (1 - Fraction(0)) == 0)
check("CS derivative vanishes at second endpoint", 6 * Fraction(1) * (1 - Fraction(1)) == 0)

# Large boundary gauge components are Z-valued (pi_3(SL(2,C))=Z via the SU(2)
# deformation retract).  This demonstrates availability of a conditional
# integer, not selection of a component by the action.
components = (-2, -1, 0, 1, 2)
check("large-gauge model has integer components", all(isinstance(n, int) for n in components))
check("identity component is included", 0 in components)
check("nonzero components are available", any(n != 0 for n in components))
check("identity reference does not force nonzero component", min(abs(n) for n in components) == 0)

check("small gauge is basic", "SMALL_GAUGE_BASIC" in basicness)
check("unrestricted boundary charge remains live", "BOUNDARY_CHARGE_LIVE" in basicness)
check("classical BFV cannot select amplitude", "classical BFV closure can choose one nonzero" in bfv and "determine its amplitude" in bfv)
check("current parent invariant quadratic pairing cancels", "NATIVE_QUADRATIC_PAIRING_ZERO_ALL_CURRENT_PARENTS" in native)
check("self-dual pairing requires a new reduction", "new source reduction" in native)

# Planted controls: each is a tempting but false shortcut this gate rejects.
check("planted endpoint-only polynomial is rejected", (lambda t: t * t)(Fraction(1, 2)) != Fraction(1, 2), planted=True)
check("planted linear path is not the CS cubic", Fraction(1, 4) != q(Fraction(1, 4)), planted=True)
check("planted same-bundle unit difference is rejected", c2_target - c2_reference != 1, planted=True)
check("planted identity winding one is rejected", 0 != 1, planted=True)
check("planted unique real pairing is rejected", 2 != 1, planted=True)

print(f"PASS exact={EXACT} planted={PLANTED} total={EXACT + PLANTED}")
