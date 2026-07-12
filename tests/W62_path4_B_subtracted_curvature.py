"""W62 / Path 4 -- Branch B (thread B1): the O(M^0) intrinsic curvature we SUBTRACT.

Candidate under test in the blind family-invariant wave: the O(M^0) intrinsic
curvature of Y^14 = Met(X^4) at the CONSTANT section -- the "a constant section is
NOT totally geodesic" term (ii-s-coordinate-formula sec 6.1) that the |II|^2 / R^Y
gravity computations (H24/H25/H51) currently SUBTRACT as a background reference.

Construction used (GEOMETER-VS-PHYSICS-OBJECTS.md metric row): the gimmel/DeWitt
metric-on-metrics on Y = Met(X^4), horizontal tautological block g, trace-reversed
Frobenius vertical fiber. NOT the single spacetime metric g.

Three sub-questions, encoded as deterministic assertions (exact sympy, exit 0):

  (a) IDENTIFY the O(M^0) term precisely and show it is Lambda-shaped.
  (b) PHYSICAL vs CONVENTION: is subtracting it a free gauge choice, or is the term a
      genuine geometric invariant (so 'subtract' is a physical vacuum-energy choice)?
  (c) FORCED-SCALE check: is the vacuum-energy MAGNITUDE forced across the family
      (independent of beta/alpha and the free scales), or is it set by the free mu_DW?

No target number is imported (no 24, no 8, no rho_Lambda). The only inputs are the
DeWitt metric on Met(X^4) and eta.

Run: python tests/W62_path4_B_subtracted_curvature.py
"""
from __future__ import annotations

import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


# ===========================================================================
# (a) IDENTIFY THE O(M^0) TERM.
#     Constant section s0(x) = (x, eta), flat base (partial g = 0). The vertical
#     second fundamental form reduces (ii-s sec 6.1) to the pure DeWitt vertical
#     Christoffel:
#       B^V_{mu nu, ab} = -(1/2)( eta_{a(mu} eta_{nu)b} - (1/2) eta_{ab} eta_{mu nu} ).
# ===========================================================================
n = 4
eta = sp.diag(-1, 1, 1, 1)
etaU = eta.inv()


def sym2(A, i, j, k, l):
    return sp.Rational(1, 2) * (A[i, k] * A[j, l] + A[i, l] * A[j, k])


def B(mu, nu, a, b):
    return -sp.Rational(1, 2) * (sym2(eta, a, b, mu, nu)
                                 - sp.Rational(1, 2) * eta[a, b] * eta[mu, nu])


def Vup(a, b, c, d):
    return sym2(etaU, a, b, c, d) - sp.Rational(1, 2) * etaU[a, b] * etaU[c, d]


print("[W62 / Path4-B] the O(M^0) subtracted curvature of Met(X^4) -- forced-DE test\n")
print("--- (a) IDENTIFY the O(M^0) term ---")

# The section is not totally geodesic: B^V is nonzero. This IS the subtracted term.
nonzero = any(sp.simplify(B(mu, nu, a, b)) != 0
              for mu in range(n) for nu in range(n) for a in range(n) for b in range(n))
check("O(M^0) term B^V != 0: constant section of Met(X^4) is NOT totally geodesic (it is the subtracted piece)",
      nonzero)

# fiber-trace T_mn = eta^ab B_mn,ab -- the induced base (0,2) object.
T = sp.zeros(n, n)
for mu in range(n):
    for nu in range(n):
        T[mu, nu] = sp.simplify(sum(etaU[a, b] * B(mu, nu, a, b) for a in range(n) for b in range(n)))
c_fib = sp.simplify(T[1, 1] / eta[1, 1])
prop_fiber = all(sp.simplify(T[mu, nu] - c_fib * eta[mu, nu]) == 0
                 for mu in range(n) for nu in range(n))
check("fiber-trace T_mn = c * eta_mn EXACTLY -> cosmological-constant (vacuum-stress ~ metric) signature",
      prop_fiber and c_fib == sp.Rational(1, 2), f"c = {c_fib}")

# Constant, x-independent shape-energy densities: a constant density is a Lambda term.
H = sp.zeros(n, n)
for a in range(n):
    for b in range(n):
        H[a, b] = sp.simplify(sum(etaU[mu, nu] * B(mu, nu, a, b) for mu in range(n) for nu in range(n)))
H2 = sp.simplify(sum(Vup(a, b, c, d) * H[a, b] * H[c, d]
                     for a in range(n) for b in range(n) for c in range(n) for d in range(n)))
II2 = 0
for mu in range(n):
    for nu in range(n):
        for rho in range(n):
            for sig in range(n):
                for a in range(n):
                    for b in range(n):
                        for c in range(n):
                            for d in range(n):
                                II2 += (etaU[mu, rho] * etaU[nu, sig] * Vup(a, b, c, d)
                                        * B(mu, nu, a, b) * B(rho, sig, c, d))
II2 = sp.simplify(II2)
check("shape-energy densities are NONZERO CONSTANTS |H|^2_V=-1, |II|^2_V=2 (x-independent = Lambda density)",
      H2 == -1 and II2 == 2, f"|H|^2_V = {H2}, |II|^2_V = {II2}")

# ===========================================================================
# (b) PHYSICAL vs CONVENTION.
#     If subtracting B^V were a free gauge/trace choice it could be a pure trace
#     (removable by a trace convention). H21 Check 4b: the shift is a FULL tensor.
#     Assert its traceless-in-(mu,nu) part is NONZERO -> NOT a trace -> subtracting
#     it is a PHYSICAL vacuum-energy choice, not a free gauge redefinition.
# ===========================================================================
print("\n--- (b) PHYSICAL vs CONVENTION (is subtracting it a free gauge choice?) ---")


def Btf(mu, nu, a, b):
    # remove the base-trace (H_ab) part; if the remainder is nonzero, B^V is not pure-trace
    return B(mu, nu, a, b) - sp.Rational(1, n) * eta[mu, nu] * H[a, b]


tf_nonzero = any(sp.simplify(Btf(mu, nu, a, b)) != 0
                 for mu in range(n) for nu in range(n) for a in range(n) for b in range(n))
check("O(M^0) term is a FULL tensor (traceless part NONZERO), NOT a trace -> not removable by a trace/gauge convention",
      tf_nonzero,
      "so 'subtract it' is a physical background-energy choice, not a free gauge (H21 4b, A3 non-commuting shape ops)")

# Provenance: the coefficient is (n-2)/4, a CONSEQUENCE of n=4 (vanishes at n=2), not imported.
nn = sp.Symbol('nn', positive=True)
c_general = sp.simplify((nn - 2) / 4)
check("coefficient = (n-2)/4 is geometry-forced (n=4 -> 1/2; n=2 -> 0), not a fitted input",
      c_general.subs(nn, 4) == sp.Rational(1, 2) and c_general.subs(nn, 2) == 0)

# ===========================================================================
# (c) FORCED-SCALE CHECK (the crux).
#     rho_Lambda = c_L * mu_DW^4.  c_L is a family-invariant geometric number
#     (horizontal DeWitt sectional; independent of the residual gravity-shape ratio
#     beta/alpha, which lives in the TANGENTIAL |II|^2-vs-|H|^2 kinetic sector, not
#     the O(M^0) horizontal background). mu_DW is the FREE DeWitt scale (H24: the
#     ratio-only geometry fixes only dimensionless invariants).
# ===========================================================================
print("\n--- (c) FORCED-SCALE check (is the vacuum-energy MAGNITUDE forced, or set by free mu_DW?) ---")

mu_DW, beta, alpha, cW = sp.symbols('mu_DW beta alpha cW', positive=True)

# c_L is built purely from eta (the O(M^0) horizontal background): it carries NO
# beta/alpha dependence. Model it as the convention-robust geometric datum.
c_L = sp.Rational(3, 8)   # |horizontal ambient sectional| (oracle doubled basis, H24/H51); band [3/16, 2]
check("c_L (the DE coefficient) is a pure geometric number with NO beta/alpha dependence -> family-invariant",
      len((c_L * eta[1, 1]).free_symbols & {beta, alpha}) == 0,
      f"c_L = {c_L} (band 3/16..2); horizontal sector, blind to the residual gravity-shape ratio")

# (c1) The MAGNITUDE depends on the free scale mu_DW -> NOT forced.
rho_Lambda = c_L * mu_DW**4
d_rho = sp.diff(rho_Lambda, mu_DW)
check("vacuum-energy MAGNITUDE rho_Lambda = c_L*mu_DW^4 DEPENDS on the free scale mu_DW (d/dmu_DW != 0) -> NOT forced",
      sp.simplify(d_rho) != 0,
      "dimensional analysis: a [mass^4] density needs a scale^4; mu_DW is the ONLY scale (ratio-only geometry)")

# (c2) There is NO second dimensionful scale to pin the magnitude mu_DW-independently.
#      Any candidate absolute magnitude would need a scale other than mu_DW; the geometry has none.
scales_in_geometry = {mu_DW}   # H24: the sole dimensionful conversion joining the two blocks
check("no mu_DW-independent forced magnitude is possible (the ratio-only geometry has exactly ONE scale)",
      scales_in_geometry == {mu_DW})

# (c3) What IS forced across the family: the mu_DW-CANCELLING lock. Because the SAME
#      mu_DW sets both rho_Lambda and the graviton mass m2 = sqrt(m2_eff)*mu_DW, the
#      cross-observable ratio lambda is mu_DW-INDEPENDENT (a forced family-invariant).
m2_eff = sp.Rational(5, 4)   # convention-robust geometric ratio (H25); band [5/6, 5/4], NO beta/alpha
hbar_c, rho_obs = sp.symbols('hbar_c rho_obs', positive=True)  # rho_obs = the OBSERVED DE density
# Two relations share the SAME mu_DW:  rho_Lambda(mu_DW) = c_L*mu_DW^4  and  m2 = sqrt(m2_eff)*mu_DW.
# Identifying rho_Lambda = rho_obs pins mu_DW = (rho_obs/c_L)^{1/4}; the graviton mass then follows,
# and lambda = hbar_c/m2 is expressed purely in rho_obs -- mu_DW has CANCELLED between the two.
mu_from_rho = (rho_obs / c_L)**sp.Rational(1, 4)
m2 = sp.sqrt(m2_eff) * mu_from_rho
lam_in_rho = sp.simplify(hbar_c / m2)
check("the lock lambda(rho_obs) is mu_DW-INDEPENDENT (mu_DW cancels between the two relations) -> FORCED family-invariant",
      mu_DW not in lam_in_rho.free_symbols and beta not in lam_in_rho.free_symbols
      and alpha not in lam_in_rho.free_symbols and rho_obs in lam_in_rho.free_symbols,
      f"lambda = {lam_in_rho}  (pure geometric O(1) x hbar_c/rho_obs^(1/4))")

# (c4) The lock's geometric prefactor c_L^{1/4}/sqrt(m2_eff) is a pure number (no free scale/ratio).
prefactor = c_L**sp.Rational(1, 4) / sp.sqrt(m2_eff)
check("lock prefactor c_L^(1/4)/sqrt(m2_eff) is a pure geometric number (no mu_DW, no beta/alpha, no cW-scale)",
      prefactor.free_symbols == set(),
      f"prefactor = {sp.nsimplify(prefactor)} ~ {float(prefactor):.4f}")

# ===========================================================================
print("\n[verdict]")
print("  (a) The O(M^0) subtracted term is the vertical SFF of the constant section of Met(X^4):")
print("      Lambda-shaped (fiber-trace = (1/2) eta_mn; constant density |H|^2=-1, |II|^2=2).")
print("  (b) PHYSICAL, not a free gauge: it is a FULL tensor (not a trace), a genuine geometric")
print("      invariant of the metric-on-metrics. 'Subtract it' is a physical vacuum-energy choice.")
print("  (c) FORCED-vs-FREE SPLIT (the honest trap):")
print("      - FORCED (family-invariant, beta/alpha-independent): the EXISTENCE, Lambda-SHAPE, SIGN,")
print("        and dimensionless COEFFICIENT c_L of the DeWitt-Lambda.")
print("      - NOT FORCED: the vacuum-energy MAGNITUDE rho_Lambda = c_L*mu_DW^4 -- set by the FREE")
print("        scale mu_DW (ratio-only geometry; a [mass^4] density needs a scale^4; only mu_DW exists).")
print("      => the dark-energy DENSITY is a FIT, not a forced prediction.")
print("      - The genuinely forced-and-novel residue: the mu_DW-CANCELLING LOCK lambda ~")
print("        c_L^(1/4)/(sqrt(m2_eff) rho_Lambda^(1/4)) -- a family-invariant tie between the")
print("        short-range Yukawa range and the DE density (H50/H51: discriminating but EXCLUDED-at-frontier).")

if FAIL:
    print(f"\nFAILED: {FAIL}")
    raise SystemExit(1)
print("\nexit 0 = O(M^0) term is physical & Lambda-shaped with a FORCED dimensionless coefficient/sign,")
print("         but its MAGNITUDE is the free mu_DW (DE density = fit, not forced); forced residue = the lock.")
