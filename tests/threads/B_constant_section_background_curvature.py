"""THREAD B1 -- first swing.

Is the O(M^0) intrinsic curvature of Met(X4) -- the "a constant section is NOT
totally geodesic" term (ii-s-coordinate-formula-2026-06-23.md section 6.1) that the
Willmore arc currently SUBTRACTS as a normalization convention -- actually a
cosmological-constant / vacuum-energy (Lambda-like) term?

The object. For a CONSTANT graph section s(x)=(x,eta) of Y14 = Met(X4) (flat base
g = eta, so partial g = 0), the vertical second fundamental form reduces (section 6.1)
to the pure DeWitt vertical Christoffel:

    B^V_{mu nu, ab} = -(1/2) ( eta_{a(mu} eta_{nu)b} - (1/2) eta_{ab} eta_{mu nu} ),

with symmetrization weight 1/2. This is nonzero even though the section is constant --
the space of metrics is intrinsically curved, so a constant slice is not totally
geodesic. The arc subtracts this as a "reference." This test asks whether that
subtracted object is the algebraic fingerprint of a cosmological constant.

What a Lambda term looks like, algebraically:
  (1) a shape-energy DENSITY that is CONSTANT over spacetime (independent of x) --
      because int sqrt(g) * const = vacuum energy = Lambda; and
  (2) an induced stress that is PROPORTIONAL TO THE METRIC (T_{mu nu} ~ eta_{mu nu}) --
      the defining property of a vacuum stress-energy tensor.

We test both, exactly (sympy), for the constant section. We also do the honest
dimension-dependence check: the proportionality coefficient is (n-2)/4, so its 4D
value 1/2 is a CONSEQUENCE of n=4, not an imported number (it vanishes at n=2).

NOTHING here is fit to a target. No 24, no 8, no chi. The only inputs are the DeWitt
metric on Met(X4) (from GU's own gimmel construction) and eta.

Run: python tests/threads/B_constant_section_background_curvature.py
"""
from __future__ import annotations

import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


# ---------------------------------------------------------------------------
# 4D setup: eta = diag(-1,1,1,1). Fiber (ab) and base (mu nu) indices both run 0..3.
# ---------------------------------------------------------------------------
n = 4
eta = sp.diag(-1, 1, 1, 1)
etaU = eta.inv()   # = eta for signature +-1 entries


def sym2(A, i, j, k, l):
    """symmetrize with weight 1/2: A_{i(k} A_{l)j} etc."""
    return sp.Rational(1, 2) * (A[i, k] * A[j, l] + A[i, l] * A[j, k])


def B(mu, nu, a, b):
    """Vertical SFF of the CONSTANT section (section 6.1):
       B^V_{mu nu,ab} = -(1/2)( eta_{a(mu} eta_{nu)b} - (1/2) eta_{ab} eta_{mu nu} )."""
    return -sp.Rational(1, 2) * (sym2(eta, a, b, mu, nu) - sp.Rational(1, 2) * eta[a, b] * eta[mu, nu])


print("[B1] O(M^0) DeWitt background curvature of the constant section -- Lambda test\n")

# ---- symmetries (sanity) --------------------------------------------------
sym_mn = all(sp.simplify(B(mu, nu, a, b) - B(nu, mu, a, b)) == 0
             for mu in range(n) for nu in range(n) for a in range(n) for b in range(n))
sym_ab = all(sp.simplify(B(mu, nu, a, b) - B(mu, nu, b, a)) == 0
             for mu in range(n) for nu in range(n) for a in range(n) for b in range(n))
check("B^V symmetric in base pair (mu<->nu) and fiber pair (a<->b)", sym_mn and sym_ab)

# ---- B is NONZERO: the constant section is not totally geodesic ------------
nonzero = any(sp.simplify(B(mu, nu, a, b)) != 0
              for mu in range(n) for nu in range(n) for a in range(n) for b in range(n))
check("constant section has B^V != 0 (Met(X4) intrinsically curved; NOT totally geodesic)", nonzero)

# ---------------------------------------------------------------------------
# (1) FIBER-TRACE T_{mu nu} = eta^{ab} B^V_{mu nu,ab}: the induced base (0,2) object.
#     If this is proportional to eta_{mu nu}, it is a vacuum-stress (Lambda) signature.
# ---------------------------------------------------------------------------
T = sp.zeros(n, n)
for mu in range(n):
    for nu in range(n):
        T[mu, nu] = sp.simplify(sum(etaU[a, b] * B(mu, nu, a, b) for a in range(n) for b in range(n)))

# proportional to eta?  T = c_fib * eta
c_fib = sp.simplify(T[1, 1] / eta[1, 1])
prop_fiber = all(sp.simplify(T[mu, nu] - c_fib * eta[mu, nu]) == 0 for mu in range(n) for nu in range(n))
print(f"    fiber-trace  T_mn = eta^ab B_mn,ab  =  ({c_fib}) * eta_mn")
check("fiber-trace of B^V is EXACTLY proportional to eta_{mu nu} (cosmological-constant signature)",
      prop_fiber, f"coefficient = {c_fib}")

# ---------------------------------------------------------------------------
# (2) MEAN CURVATURE H_{ab} = eta^{mu nu} B^V_{mu nu,ab}: the normal (fiber) vector.
#     By the same structure it should be proportional to the fiber metric eta_{ab}.
# ---------------------------------------------------------------------------
H = sp.zeros(n, n)
for a in range(n):
    for b in range(n):
        H[a, b] = sp.simplify(sum(etaU[mu, nu] * B(mu, nu, a, b) for mu in range(n) for nu in range(n)))
c_base = sp.simplify(H[1, 1] / eta[1, 1])
prop_base = all(sp.simplify(H[a, b] - c_base * eta[a, b]) == 0 for a in range(n) for b in range(n))
print(f"    mean curv    H_ab = eta^mn B_mn,ab  =  ({c_base}) * eta_ab")
check("mean curvature H_{ab} is proportional to eta_{ab} (pure-trace normal; the Lambda direction)",
      prop_base, f"coefficient = {c_base}")

# ---------------------------------------------------------------------------
# TRACE-FREE (shear) part in the base indices: B - (1/n) eta_mn * (fiber-agnostic base trace).
#     The base-index trace of B (over mu nu, at fixed ab) is H_ab; remove it.
#     If the trace-free part is nonzero, the constant section carries Lambda + shear,
#     and the Lambda piece is the PURE-TRACE part isolated above -- honest, not umbilic.
# ---------------------------------------------------------------------------
def Btf(mu, nu, a, b):
    return B(mu, nu, a, b) - sp.Rational(1, n) * eta[mu, nu] * H[a, b]

tf_nonzero = any(sp.simplify(Btf(mu, nu, a, b)) != 0
                 for mu in range(n) for nu in range(n) for a in range(n) for b in range(n))
check("base trace-free (shear) part is NONZERO -> constant section is Lambda + shear, not umbilic",
      tf_nonzero, "the Lambda piece is the isolated pure-trace part, not the whole SFF")

# ---------------------------------------------------------------------------
# CONSTANT SHAPE-ENERGY DENSITIES with the DeWitt vertical metric V.
#   V_{ab,cd}(eta) = eta_{a(c} eta_{d)b} - (1/2) eta_{ab} eta_{cd}   (lowered)
#   V^{ab,cd}(eta) = eta^{a(c} eta^{d)b} - (1/2) eta^{ab} eta^{cd}   (raised)
# |H|^2 = V^{ab,cd} H_ab H_cd ;  |II|^2 = eta^{mu rho} eta^{nu sig} V^{ab,cd} B B.
# These are CONSTANTS (x-independent). A constant density is a Lambda term:
#   S ~ int sqrt(g) * (const)  =  vacuum energy.
# ---------------------------------------------------------------------------
def Vup(a, b, c, d):
    return sym2(etaU, a, b, c, d) - sp.Rational(1, 2) * etaU[a, b] * etaU[c, d]


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
print(f"    DeWitt shape-energy densities (constant, x-independent):  |H|^2_V = {H2}   |II|^2_V = {II2}")
check("shape-energy densities |H|^2, |II|^2 are NONZERO CONSTANTS "
      "(constant density over spacetime = a cosmological-constant term)",
      sp.simplify(H2) != 0 and sp.simplify(II2) != 0,
      "int sqrt(g)*const = vacuum energy")

# ---------------------------------------------------------------------------
# HONEST provenance check: the 4D coefficient 1/2 is NOT imported. It equals (n-2)/4
# for general dimension n -- a consequence of n=4, vanishing at n=2. Compute symbolically.
# ---------------------------------------------------------------------------
nn = sp.Symbol('nn', positive=True)
# fiber trace in general n:  eta^{ab} eta_{a(mu}eta_{nu)b} = eta_{mu nu};  eta^{ab}eta_{ab} = nn.
# T_mn = -(1/2)( eta_mn - (1/2) nn eta_mn ) = ( (nn-2)/4 ) eta_mn.
c_general = sp.simplify(-sp.Rational(1, 2) * (1 - sp.Rational(1, 2) * nn))
c_general = sp.nsimplify(sp.expand(c_general))
c_at_4 = c_general.subs(nn, 4)
c_at_2 = c_general.subs(nn, 2)
print(f"    general-dimension coefficient = (nn-2)/4 = {c_general};  n=4 -> {c_at_4};  n=2 -> {c_at_2}")
check("the coefficient is (n-2)/4: the value 1/2 is a CONSEQUENCE of n=4 (not imported), zero at n=2",
      sp.simplify(c_general - (nn - 2) / 4) == 0 and c_at_4 == sp.Rational(1, 2) and c_at_2 == 0)

# ---------------------------------------------------------------------------
print("\n[verdict]")
print("  The constant section of Met(X4) has a NONZERO, x-independent vertical SFF (Met(X4) is")
print("  intrinsically curved -- the section is not totally geodesic). Two exact Lambda fingerprints:")
print(f"    (1) its fiber-trace is PROPORTIONAL TO THE METRIC:  eta^ab B_mn,ab = ({c_fib}) eta_mn")
print(f"        -- an induced base stress ~ eta_mn, the defining form of a vacuum (cosmological-constant) stress;")
print(f"    (2) its shape-energy density is a NONZERO CONSTANT (|H|^2={H2}, |II|^2={II2}); a spatially")
print("        constant density integrated over spacetime IS a cosmological-constant term.")
print("  So a Lambda-like term arises FOR FREE from the curvature of the space of metrics.")
print("  HONEST CAVEATS (not overclaimed): this is the ALGEBRAIC signature (order/structural grade), not a")
print("  derived Einstein-Lambda stress -- that needs the full higher-codimension Willmore first variation")
print("  (the named top technical task, NOT done here). The SIGN and MAGNITUDE of any physical Lambda are")
print("  gated on (i) the OQ2-A functional scalar c_W and (ii) the keep-vs-subtract convention that the arc")
print("  currently resolves by SUBTRACTING this very term. The contribution here: that subtracted object is")
print("  exactly Lambda-shaped, so 'subtract it' is a physical choice about the vacuum energy, not a free gauge.")

if FAIL:
    print(f"\nFAILED: {FAIL}")
    raise SystemExit(1)
print(f"\nexit 0 = constant-section DeWitt background is Lambda-shaped (fiber-trace ~ ({c_fib}) eta_mn,")
print("         constant shape-energy density); sign/magnitude gated on c_W + keep/subtract convention.")
