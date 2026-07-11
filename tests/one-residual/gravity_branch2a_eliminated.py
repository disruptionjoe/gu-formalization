#!/usr/bin/env python3
r"""One Residual paper -- GRAVITY Branch-2A elimination (DISPROOF of ONE branch).

CLAIM (paper Sec 2.5 / four-legs-resolved-gu-live-candidate-2026-07-11.md, row "Gravity"):
    On isotropic Schwarzschild, the geometric distortion 1-form theta ~ M/rho^2.
    The BARE source law   D_A *F_A = theta   then FORCES  F ~ M/rho, whose Yang-Mills
    action int |F|^2 sqrt(g) DIVERGES.  A FINITE-action (Coulomb ~ 1/rho^2) field instead
    REQUIRES theta = 0 in the exterior.  These two are MUTUALLY EXCLUSIVE, so Branch 2A
    cannot host exact Schwarzschild with a finite-action gauge field.  =>  the conservative
    IG branch set narrows {2A,3} -> {3}.

WHAT THIS FILE ESTABLISHES (honest grade -- DISPROOF of one branch, NOT a clear of gravity):
    A real sympy computation of the four load-bearing steps of the exclusivity argument:
      (1) theta on isotropic Schwarzschild scales as M/rho^2  (symbolic series of the
          geometric distortion 1-form theta = d log(Psi), Psi = 1 + M/(2 rho)).
      (2) the bare source law (1/rho^2) d/drho(rho^2 E) = theta_rho, solved by sympy dsolve,
          FORCES a field component E with a term ~ M/rho.
      (3) the Yang-Mills action integral int rho^2 E^2 drho with E ~ M/rho DIVERGES at rho->oo
          (sympy integrate = oo).
      (4) the SAME integral CONVERGES iff the M/rho coefficient is zero, i.e. iff theta = 0
          (Coulomb E ~ 1/rho^2 -> finite).  Exclusivity: {theta != 0} (Schwarzschild) and
          {finite action} intersect in the empty set.

HONEST-SCOPE / RECONSTRUCTION CAVEAT:
    * The IDENTIFICATION of the GU "geometric distortion 1-form" with theta = d log(Psi) is a
      modeling choice (reconstruction-grade: read from the spoken IG-source picture, not a
      written GU action).  What is derivation-grade and load-bearing is the SCALING M/rho^2:
      ANY 1-form built from one derivative of the isotropic-Schwarzschild metric (Christoffel
      level, dPsi/Psi) carries exactly this M/rho^2 leading behaviour.  The exclusivity
      conclusion depends only on that scaling, not on the exact identity of theta.
    * This DISPROVES that Branch 2A (bare source D_A*F_A = theta) can host exact Schwarzschild
      with a finite-action field.  It does NOT clear gravity: Branch 3 survives, blocked on one
      undetermined ambient-curvature Willmore-EL scalar (paper Sec 2.5).

Exit 0 iff every PASS check holds.
"""
from __future__ import annotations
import sympy as sp

FAILS: list[str] = []

def check(label: str, ok: bool, detail: str = "") -> None:
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {label}" + (f"   {detail}" if detail else ""))
    if not ok:
        FAILS.append(label)

rho, M, Q, C1, rho0 = sp.symbols('rho M Q C1 rho0', positive=True)

print("=" * 78)
print("STEP 1 -- geometric distortion 1-form theta ~ M/rho^2 on isotropic Schwarzschild")
print("=" * 78)
# Isotropic Schwarzschild spatial metric: Psi^4 * delta_ij, conformal factor
#   Psi = 1 + M/(2 rho).   (Standard; e.g. MTW. Psi -> 1 at infinity.)
# The geometric distortion 1-form (deviation of the connection from flat) is at Christoffel
# level d log(Psi); its radial component:
Psi = 1 + M / (2 * rho)
theta_rho = sp.diff(sp.log(Psi), rho)
theta_rho = sp.simplify(theta_rho)
print(f"  theta_rho = d/drho log(Psi) = {theta_rho}")

# Leading large-rho behaviour: series in 1/rho.  Substitute rho -> 1/u, series about u=0.
u = sp.symbols('u', positive=True)
theta_u = theta_rho.subs(rho, 1 / u)
ser = sp.series(theta_u, u, 0, 4).removeO()
ser = sp.expand(ser)
# leading term in u  <->  leading term in 1/rho.  Collect lowest power of u.
poly_u = sp.Poly(ser, u)
lowest_deg = min(deg for (deg,) in poly_u.monoms())
lead_coeff = poly_u.coeff_monomial(u ** lowest_deg)
print(f"  leading term of theta_rho at large rho:  ({lead_coeff}) * rho^(-{lowest_deg})")
# Expect leading ~ (-M/2) * rho^-2   (u^2 term).
check("theta_rho leading power in rho is -2  (theta ~ 1/rho^2)", lowest_deg == 2,
      f"power = -{lowest_deg}")
check("theta_rho leading coefficient is linear in M  (theta ~ M/rho^2, ->0 as M->0)",
      sp.simplify(lead_coeff / M).free_symbols == set() and sp.simplify(lead_coeff.subs(M, 0)) == 0,
      f"coeff = {lead_coeff}")
# Independent recompute: at M->0 (flat) theta must vanish identically.
check("flat limit: theta_rho(M=0) == 0 identically", sp.simplify(theta_rho.subs(M, 0)) == 0)

print()
print("=" * 78)
print("STEP 2 -- bare source law  (1/rho^2) d/drho(rho^2 E) = theta_rho  FORCES  E ~ M/rho")
print("=" * 78)
# Spherically-symmetric static radial field: Gauss-law radial component of D_A *F_A = theta.
# Use the leading theta source s(rho) = -M/(2 rho^2) (Step-1 leading term); the subleading
# metric/Psi corrections are higher order in 1/rho and do not change the leading E-scaling.
E = sp.Function('E')
s_source = lead_coeff / rho ** lowest_deg          # = -M/(2 rho^2), the geometric source
ode = sp.Eq(sp.diff(rho ** 2 * E(rho), rho) / rho ** 2, s_source)
sol = sp.dsolve(ode, E(rho))
E_sol = sp.expand(sol.rhs)
print(f"  dsolve source law ->  E(rho) = {E_sol}")
# Extract the coefficient of the 1/rho ("theta-sourced") term and the 1/rho^2 (homogeneous) term.
coeff_1_over_rho = sp.simplify((E_sol * rho).subs(rho, sp.oo))      # limit rho*E as rho->oo
# more robustly: series in 1/rho
E_u = E_sol.subs(rho, 1 / u)
E_ser = sp.series(E_u, u, 0, 3).removeO()
E_poly = sp.Poly(sp.expand(E_ser), u)
c1 = E_poly.coeff_monomial(u ** 1)   # coeff of 1/rho
c2 = E_poly.coeff_monomial(u ** 2)   # coeff of 1/rho^2
print(f"  E(rho) = ({c1})/rho + ({c2})/rho^2 + ...   (c1 = theta-forced, c2 = free Coulomb const)")
check("source law forces a nonzero 1/rho term proportional to M",
      sp.simplify(c1) != 0 and sp.simplify(c1.subs(M, 0)) == 0,
      f"c1 = {c1}")
# Sanity: with theta=0 (no source) the 1/rho term is absent (pure Coulomb 1/rho^2).
ode0 = sp.Eq(sp.diff(rho ** 2 * E(rho), rho) / rho ** 2, 0)
E0 = sp.dsolve(ode0, E(rho)).rhs
check("with theta=0 the forced 1/rho term vanishes (pure Coulomb 1/rho^2 survives)",
      sp.simplify(sp.limit(E0 * rho, rho, sp.oo)) == 0,
      f"E(theta=0) = {sp.expand(E0)}")

print()
print("=" * 78)
print("STEP 3 -- Yang-Mills action of the theta-forced field  E ~ M/rho  DIVERGES")
print("=" * 78)
# YM action density ~ |F|^2 sqrt(g); for a static radial E-field in 3-space the exterior action
# per unit time is  int_{rho0}^{oo} E(rho)^2 * (measure ~ rho^2) drho.  (Psi -> 1 at infinity,
# so the measure is asymptotically flat rho^2 and the divergence is genuine, not a gauge/measure
# artifact.)  Take the theta-forced field E = M/rho:
E_theta = M / rho
integrand_theta = sp.simplify(rho ** 2 * E_theta ** 2)
print(f"  integrand (theta-forced): rho^2 * (M/rho)^2 = {integrand_theta}")
action_theta = sp.integrate(integrand_theta, (rho, rho0, sp.oo))
print(f"  S_theta = int_rho0^oo {integrand_theta} drho = {action_theta}")
check("theta-forced field E~M/rho has DIVERGENT Yang-Mills action",
      action_theta == sp.oo)

# Coulomb comparison: E = Q/rho^2 (the finite-action, theta=0 field).
E_coulomb = Q / rho ** 2
integrand_c = sp.simplify(rho ** 2 * E_coulomb ** 2)
print(f"  integrand (Coulomb):      rho^2 * (Q/rho^2)^2 = {integrand_c}")
action_c = sp.integrate(integrand_c, (rho, rho0, sp.oo))
print(f"  S_Coulomb = int_rho0^oo {integrand_c} drho = {action_c}   (finite)")
check("Coulomb field E~Q/rho^2 has FINITE Yang-Mills action (converges at infinity)",
      action_c.is_finite is True)

print()
print("=" * 78)
print("STEP 4 -- EXCLUSIVITY: finite action  <=>  (M/rho coefficient = 0)  <=>  theta = 0")
print("=" * 78)
# General exterior field from Step 2: E = a/rho + b/rho^2, with a = theta-forced (prop. to M),
# b = the free Coulomb constant (theta-independent).  Classify each tail term by its PURE
# rho-power n:  int_{rho0}^oo rho^n drho converges iff n < -1  (both the a^2 term n=0 and the
# cross term a*b/rho n=-1 diverge; only the pure-b term b^2/rho^2 n=-2 converges).
a, b = sp.symbols('a b', real=True, nonzero=True)
E_gen = a / rho + b / rho ** 2
integrand_gen = sp.expand(rho ** 2 * E_gen ** 2)
print(f"  general exterior integrand: rho^2 (a/rho + b/rho^2)^2 = {integrand_gen}")

def rho_power(term):
    # exponent n in term = c * rho^n (c independent of rho):  n = rho * d/drho(term) / term
    return sp.simplify(rho * sp.diff(term, rho) / term)

divergent_terms, finite_terms = [], []
for term in integrand_gen.as_ordered_terms():
    n = rho_power(term)
    converges = sp.simplify(n < -1) is sp.true
    (finite_terms if converges else divergent_terms).append((term, n))
print("  tail-integral term analysis (rho0 -> oo), by pure rho-power n:")
for term, n in divergent_terms:
    print(f"     DIVERGES (n={n} >= -1): {term}")
for term, n in finite_terms:
    print(f"     finite   (n={n} <  -1): {term}")

# Load-bearing structural fact: EVERY divergent tail term carries the theta-forced factor `a`;
# NO divergent term is a pure function of the free Coulomb constant b.  So a=0 kills every
# divergence, and a!=0 leaves at least one.
there_is_a_divergence = len(divergent_terms) >= 1
every_div_has_a = all(a in term.free_symbols for term, _ in divergent_terms)
check("at least one tail term diverges when the theta-forced amplitude a != 0",
      there_is_a_divergence, f"{len(divergent_terms)} divergent term(s)")
check("EVERY divergent tail term carries the theta-forced factor a (none is pure Coulomb b)",
      every_div_has_a)

# Direct confirmation: setting a=0 (theta=0) makes the exterior action FINITE.
action_a0 = sp.integrate(integrand_gen.subs(a, 0), (rho, rho0, sp.oo))
check("setting a=0 (theta=0) makes the exterior action FINITE (pure Coulomb b/rho^2 tail)",
      action_a0.is_finite is True, f"S(a=0) = {action_a0}")

# theta = 0  =>  (Step 2) forced coeff c1 = 0  =>  a = 0  =>  finite.
# theta != 0 (Schwarzschild, M != 0)  =>  a != 0  =>  divergent.  Empty intersection.
schwarzschild_has_theta = (sp.simplify(theta_rho.subs(M, 0)) == 0
                           and sp.simplify(theta_rho) != 0)
check("finite action REQUIRES a=0, i.e. theta=0 in the exterior",
      there_is_a_divergence and every_div_has_a and action_a0.is_finite is True)
check("exact Schwarzschild (M != 0) has theta != 0  ->  cannot also have finite action",
      schwarzschild_has_theta)
check("MUTUAL EXCLUSIVITY: {theta != 0} INTERSECT {finite action} = empty",
      there_is_a_divergence and every_div_has_a and schwarzschild_has_theta)

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
if FAILS:
    print(f"  {len(FAILS)} check(s) FAILED: {FAILS}")
    print("  Branch-2A elimination NOT established by this run.")
    raise SystemExit(1)
print("""  ALL CHECKS PASSED.
  Established (DISPROOF-grade, ONE branch):
    theta ~ M/rho^2 on isotropic Schwarzschild;  the bare source law D_A*F_A = theta forces
    E ~ M/rho;  its Yang-Mills action DIVERGES;  a finite-action (Coulomb) field REQUIRES
    theta = 0.  These are mutually exclusive, so Branch 2A (bare source) CANNOT host exact
    Schwarzschild with a finite-action gauge field.  The conservative IG branch set narrows
    {2A, 3} -> {3}.
  NOT established (honest scope): this does NOT clear gravity.  Branch 3 survives, blocked on
    one undetermined ambient-curvature Willmore-EL scalar (paper Sec 2.5).  The identification
    theta = d log(Psi) is reconstruction-grade; the load-bearing content is the M/rho^2 scaling
    and the divergence/finiteness exclusivity, which hold for any Christoffel-level distortion
    1-form.""")
raise SystemExit(0)
