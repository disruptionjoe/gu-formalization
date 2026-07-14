"""
W152 -- Marble and cheap wood: the record-substrate / source-action fix, computed checks.

Team MARBLE (W152). Exploration grade; conditional register. Nothing here asserts GU or
that any decomposition is physical; every computed object is a property of a DECLARED
conditional structure, exactly as W136/W144/W145/W146 keep the register.

This test backs the three-term scorecard in
explorations/W152-marble-and-wood-source-fix-2026-07-14.md with deterministic arithmetic.

Positive controls run FIRST (as the wave brief requires):
  PC1  the standard contracted Bianchi identity nabla_mu G^{mu nu} = 0 on a curved metric
       (spatially-flat FRW with arbitrary a(t)) -- reproduces the MARBLE.
  PC2  the W144 CPL closed-form zero-crossing of Q(a) at z ~ 0.405 (a_x = 0.71163).

Then the wave's own computed objects:
  A  the transcript's product-rule fact: nabla_mu(Lambda(t) g^{mu nu}) = 0  <=>  Lambda' = 0
     (constant Lambda is divergence-free for the LOUSY reason; a varying Lambda is NOT
     divergence-free by itself and must be compensated by a source exchange Q).
  B  the interacting-vacuum bookkeeping: with the varying Lambda(x) carried as a w=-1 vacuum,
     nabla_mu(G + Lambda(x) g) = 0 forces nabla_mu Lambda g = Q = -8 pi nabla_mu T_matter;
     verified as the self-consistent CPL continuity relation Q = rho_DE' (everything in Q).
  C  the "rise and fall" quantification of W144's Q: single sign change, O(1) amplitude in
     the Planck-ladder unit q_B, and schedule drift 0.744/e-fold (2.48x outside the W138 G2
     mimic band 0.3) -- Weinstein's "rise and fall to meet the curvature", made quantitative.
  D  the MARBLE-SURVIVAL check: the GU induced action adds a higher-derivative sector to the
     Einstein term (W126/W130: a1 = 1/3 Einstein PLUS an R^2 sector). The R^2 field tensor
     E_{mu nu} from delta(int sqrt g R^2) is verified covariantly conserved on FRW
     (generalized Bianchi). So the divergence-free LEFT SIDE (the marble structure) SURVIVES,
     but is MODIFIED: left side = a1 G + (extra divergence-free tensor), and the extra tensor
     is exactly the tachyonic/ghost Stelle sector (W122/W126/W130). Marble kept, augmented.

Run: python -u tests/W152_marble_and_wood_source_fix.py   (expect exit 0)
"""

import sympy as sp

PASS = 0
FAIL = 0


def check(name, cond):
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"  PASS  {name}")
    else:
        FAIL += 1
        print(f"  FAIL  {name}")


# ----------------------------------------------------------------------------
# Shared geometry machinery: spatially-flat FRW, arbitrary a(t).
# coords (t, x, y, z); g = diag(-1, a^2, a^2, a^2).
# ----------------------------------------------------------------------------
t, x, y, z = sp.symbols("t x y z", real=True)
a = sp.Function("a", positive=True)(t)
coords = [t, x, y, z]
n = 4

g = sp.diag(-1, a**2, a**2, a**2)
ginv = g.inv()


def christoffel(g, ginv, coords):
    n = len(coords)
    Gamma = [[[sp.S(0)] * n for _ in range(n)] for _ in range(n)]
    for l in range(n):
        for mu in range(n):
            for nu in range(n):
                s = sp.S(0)
                for sig in range(n):
                    s += ginv[l, sig] * (
                        sp.diff(g[sig, mu], coords[nu])
                        + sp.diff(g[sig, nu], coords[mu])
                        - sp.diff(g[mu, nu], coords[sig])
                    )
                Gamma[l][mu][nu] = sp.simplify(s / 2)
    return Gamma


def ricci(Gamma, coords):
    n = len(coords)
    Ric = sp.zeros(n, n)
    for mu in range(n):
        for nu in range(n):
            s = sp.S(0)
            for l in range(n):
                s += sp.diff(Gamma[l][mu][nu], coords[l]) - sp.diff(
                    Gamma[l][mu][l], coords[nu]
                )
                for sig in range(n):
                    s += (
                        Gamma[l][l][sig] * Gamma[sig][mu][nu]
                        - Gamma[l][nu][sig] * Gamma[sig][mu][l]
                    )
            Ric[mu, nu] = sp.simplify(s)
    return Ric


def cov_div_20(T_low, g, ginv, Gamma, coords):
    """Covariant divergence nabla_mu T^{mu}_{ nu} of a (0,2) tensor T_low (T_{mu nu}),
    returned as the covector (nabla^mu T_{mu nu}) with the upper index raised by ginv.
    Returns a length-n vector, each entry simplified."""
    n = len(coords)
    # nabla_alpha T_{mu nu}
    out = []
    for nu in range(n):
        total = sp.S(0)
        for mu in range(n):
            for al in range(n):
                covderiv = sp.diff(T_low[mu, nu], coords[al])
                for lam in range(n):
                    covderiv -= Gamma[lam][al][mu] * T_low[lam, nu]
                    covderiv -= Gamma[lam][al][nu] * T_low[mu, lam]
                total += ginv[mu, al] * covderiv
        out.append(sp.simplify(total))
    return out


Gamma = christoffel(g, ginv, coords)
Ric = ricci(Gamma, coords)
Rscalar = sp.simplify(sum(ginv[i, j] * Ric[i, j] for i in range(n) for j in range(n)))

print("=" * 70)
print("W152 marble-and-wood computed checks")
print("=" * 70)

# ----------------------------------------------------------------------------
# PC1 -- contracted Bianchi identity for the Einstein tensor (the MARBLE).
# ----------------------------------------------------------------------------
print("\n[PC1] contracted Bianchi identity: nabla_mu G^{mu nu} = 0 (the marble)")
G_ein = sp.simplify(Ric - sp.Rational(1, 2) * Rscalar * g)
divG = cov_div_20(G_ein, g, ginv, Gamma, coords)
check("Einstein tensor divergence vanishes identically (all 4 components)",
      all(sp.simplify(c) == 0 for c in divG))
# sanity: the Einstein tensor is nontrivial (G_tt is the Friedmann 3(a'/a)^2)
check("Einstein tensor is nontrivial (G_tt != 0)", sp.simplify(G_ein[0, 0]) != 0)

# ----------------------------------------------------------------------------
# PC2 -- W144 CPL closed-form zero-crossing of Q(a).
# w(a) = w0 + wa(1-a), w0 = -0.752, wa = -0.86 (repo-verified DESI+CMB+DESY5 digits).
# ----------------------------------------------------------------------------
print("\n[PC2] W144 CPL Q(a) zero-crossing at z ~ 0.405")
w0, wa = -0.752, -0.86
# crossing w = -1:  wa(1-a) = -(1+w0)
a_x = 1 + (1 + w0) / wa
z_x = 1 / a_x - 1
check("crossing scale a_x = 0.71163", abs(a_x - 0.71163) < 1e-4)
check("crossing redshift z_x = 0.40523", abs(z_x - 0.40523) < 1e-4)


def w_cpl(av):
    return w0 + wa * (1 - av)


def one_plus_w(av):
    return 1 + w_cpl(av)


# Q(a) sign = sign of -(1+w) (since Q = -3 H (1+w) rho_DE, H>0, rho_DE>0).
def Q_sign(av):
    val = -one_plus_w(av)
    return 1 if val > 0 else (-1 if val < 0 else 0)


check("Q > 0 (ISSUANCE) for a < a_x, e.g. a=0.4 (z=1.5)", Q_sign(0.40) == +1)
check("Q > 0 (ISSUANCE) for a=0.5", Q_sign(0.50) == +1)
check("Q < 0 (WITHDRAWAL) for a > a_x, e.g. a=0.9", Q_sign(0.90) == -1)
check("Q < 0 (WITHDRAWAL) today a=1", Q_sign(1.00) == -1)
check("exactly one sign change across the DESI window", Q_sign(0.4) * Q_sign(1.0) == -1)

# ----------------------------------------------------------------------------
# A -- the transcript's product-rule fact (the LOUSY reason), computed.
# nabla_mu ( Lambda(t) g^{mu nu} ) : since nabla g = 0, = g^{mu nu} d_mu Lambda = d^nu Lambda.
# Constant Lambda => 0 (divergence-free for the lousy metric-compatibility reason).
# Varying Lambda(t) => nonzero => NOT divergence-free alone; needs a source Q.
# ----------------------------------------------------------------------------
print("\n[A] product rule: nabla_mu(Lambda g) = 0  <=>  Lambda' = 0 (the lousy reason)")
Lam = sp.Function("Lambda")(t)
Lam_g_low = Lam * g  # (0,2) tensor Lambda g_{mu nu}
divLamg = cov_div_20(Lam_g_low, g, ginv, Gamma, coords)
# only the nu=t component can be nonzero on FRW; it equals -Lambda'(t) (g^{tt} = -1).
check("nabla_mu(Lambda g) spatial components vanish",
      all(sp.simplify(divLamg[i]) == 0 for i in (1, 2, 3)))
# cov_div returns the lower-nu covector (nabla^mu (Lambda g)_{mu nu}) = d_nu Lambda; the
# t-component is Lambda'(t) (the raised-index form d^t Lambda = -Lambda'(t) differs only by
# g^{tt}; either way it is nonzero iff Lambda varies -- the transcript's point).
check("nabla_mu(Lambda g)^t proportional to Lambda'(t) (nonzero iff Lambda varies)",
      sp.simplify(divLamg[0] - sp.diff(Lam, t)) == 0)
# constant-Lambda specialization: substitute Lambda -> const => divergence vanishes.
Lam_const = sp.Symbol("Lambda0", real=True)
divLamg_const = [sp.simplify(c.subs(sp.Derivative(Lam, t), 0).subs(Lam, Lam_const))
                 for c in divLamg]
check("constant Lambda => nabla_mu(Lambda g) = 0 (divergence-free, lousy reason)",
      all(c == 0 for c in divLamg_const))

# ----------------------------------------------------------------------------
# B -- interacting-vacuum bookkeeping: the varying Lambda is compensated by Q.
# Carry the DESI CPL history as a w=-1 vacuum with rho_V(a) = rho_DE(a); then
# rho_V' = Q exactly, and the effective eq. of state read off the history is
# w_eff(a) = -1 - (1/3) d ln rho_DE / d ln a.  We verify the identity
#   Q(a) = -3 H (1 + w_eff) rho_DE   ==   rho_DE'(a) (cosmic-time derivative)
# holds by construction (the "everything in Q" decomposition is self-consistent),
# i.e. the position-dependent Lambda is divergence-compensated by the source exchange.
# ----------------------------------------------------------------------------
print("\n[B] interacting-vacuum: Q = rho_DE' compensates the varying Lambda (self-consistent)")
av = sp.Symbol("a", positive=True)
# Use EXACT rationals so symbolic identities reduce to 0 (float exponents leave 1e-16 dust).
w0r, war = sp.Rational(-752, 1000), sp.Rational(-86, 100)
# CPL density history (W144 closed form), rho normalized to rho_DE(1) = 1:
rho_DE = av ** (-3 * (1 + w0r + war)) * sp.exp(-3 * war * (1 - av))
dln_rho_dln_a = sp.simplify(av * sp.diff(rho_DE, av) / rho_DE)
w_eff = sp.simplify(-1 - sp.Rational(1, 3) * dln_rho_dln_a)
# w_eff should equal the CPL w(a) exactly for this history:
w_cpl_sym = w0r + war * (1 - av)
check("w_eff(a) reconstructed from rho history equals CPL w(a) exactly",
      sp.simplify(w_eff - w_cpl_sym) == 0)
# continuity identity: with ' = d/dt = a H d/da, Q = rho_DE' = a H drho/da, and
# -3 H (1+w_eff) rho_DE = -3 H rho_DE (1+w_eff). Cancel H; check a drho/da = -3(1+w_eff)rho.
lhs = sp.simplify(av * sp.diff(rho_DE, av))
rhs = sp.simplify(-3 * (1 + w_eff) * rho_DE)
check("continuity Q = -3H(1+w_eff)rho_DE holds identically (Bianchi bookkeeping closes)",
      sp.simplify(lhs - rhs) == 0)

# ----------------------------------------------------------------------------
# C -- "rise and fall" quantification of W144's Q (Weinstein's criterion).
# ----------------------------------------------------------------------------
print("\n[C] rise-and-fall quantification of Q vs the W138 G2 mimic band")
# schedule drift today (z=0, a=1): |d ln rho / d ln a| = |{-3(1+w0)}| ... use w_eff at a=1.
drift_today = float(abs(dln_rho_dln_a.subs(av, 1)))
# = 3|1+w0| = 3*0.248 = 0.744
check("schedule drift today = 0.744/e-fold (2.48x outside G2 band 0.3)",
      abs(drift_today - 0.744) < 1e-3 and drift_today > 0.3)
# Q amplitude in q_B units: Q/q_B = -(1+w) * (rho_DE/rho_L) * (H/H0) ... the W144 table
# reports Q today = -0.248 q_B and issuance side up to ~ +0.98 q_B; check O(1), sign flip.
Q_today_over_qB = -(1 + w0)  # -0.248 (at a=1, rho_DE=rho_L, H=H0 to leading normalization)
check("Q today = -0.248 q_B (O(1), withdrawal sign)", abs(Q_today_over_qB + 0.248) < 1e-3)
# a single monotone-in-sign structure: issuance amplitude (past) positive and O(1):
# at a=0.30 (window edge), 1+w = 1 + w0 + wa*0.70 = 1 -0.752 -0.602 = -0.354 -> Q>0
one_plus_w_030 = 1 + w0 + wa * (1 - 0.30)
check("issuance side (a=0.30): 1+w < 0 so Q > 0, amplitude O(1)",
      one_plus_w_030 < 0 and abs(one_plus_w_030) < 1.0)
# Weinstein criterion summary: Q not forced constant (varies with a), rises then falls,
# crosses zero once. Encapsulate as a boolean.
rises_and_falls = (Q_sign(0.4) == +1) and (Q_sign(1.0) == -1) and (drift_today > 0.0)
check("Weinstein 'rise and fall' met: Q varies, single zero-crossing, sign flip",
      rises_and_falls)

# ----------------------------------------------------------------------------
# D -- MARBLE SURVIVAL: the higher-derivative (R^2 / Stelle) sector is ALSO
# covariantly conserved (generalized Bianchi). Marble kept but augmented.
# E_{mu nu} from L = R^2:  E = 2 R R_{mu nu} - (1/2) R^2 g + 2(g box - nabla nabla) R.
# Verify nabla^mu E_{mu nu} = 0 on FRW with arbitrary a(t).
# ----------------------------------------------------------------------------
print("\n[D] marble survival: R^2-sector field tensor is divergence-free (generalized Bianchi)")


def box_scalar(f, g, ginv, Gamma, coords):
    # box f = g^{ab}( d_a d_b f - Gamma^l_{ab} d_l f )
    n = len(coords)
    s = sp.S(0)
    for a_ in range(n):
        for b_ in range(n):
            term = sp.diff(f, coords[a_], coords[b_])
            for l in range(n):
                term -= Gamma[l][a_][b_] * sp.diff(f, coords[l])
            s += ginv[a_, b_] * term
    return sp.simplify(s)


def hess_scalar(f, Gamma, coords):
    # (nabla_mu nabla_nu f)_{mu nu} = d_mu d_nu f - Gamma^l_{mu nu} d_l f
    n = len(coords)
    H = sp.zeros(n, n)
    for mu in range(n):
        for nu in range(n):
            term = sp.diff(f, coords[mu], coords[nu])
            for l in range(n):
                term -= Gamma[l][mu][nu] * sp.diff(f, coords[l])
            H[mu, nu] = sp.simplify(term)
    return H


boxR = box_scalar(Rscalar, g, ginv, Gamma, coords)
HessR = hess_scalar(Rscalar, Gamma, coords)
E_R2 = sp.zeros(n, n)
for mu in range(n):
    for nu in range(n):
        E_R2[mu, nu] = sp.simplify(
            2 * Rscalar * Ric[mu, nu]
            - sp.Rational(1, 2) * Rscalar**2 * g[mu, nu]
            + 2 * (g[mu, nu] * boxR - HessR[mu, nu])
        )
divE = cov_div_20(E_R2, g, ginv, Gamma, coords)
check("R^2-sector tensor E_{mu nu} divergence vanishes identically (marble survives)",
      all(sp.simplify(c) == 0 for c in divE))
check("R^2-sector tensor is nontrivial and distinct from G (E_tt != 0, E != G)",
      sp.simplify(E_R2[0, 0]) != 0 and sp.simplify(E_R2[0, 0] - G_ein[0, 0]) != 0)

# The GU induced left side (schematic) a1*G + higher-deriv sector: BOTH legs are
# separately divergence-free, so the combined left side is divergence-free for a GENUINE
# (geometric / generalized-Bianchi) reason. The augmentation carries the W122/W126/W130
# tachyon/ghost; recorded as the marble-modified verdict, not spoiled.
a1 = sp.Rational(1, 3)  # W126/W130 Einstein coefficient
c2 = sp.Rational(8, 9)  # W126 slice R^2 coefficient (illustrative combination)
L_combined = sp.zeros(n, n)
for mu in range(n):
    for nu in range(n):
        L_combined[mu, nu] = a1 * G_ein[mu, nu] + c2 * E_R2[mu, nu]
divL = cov_div_20(L_combined, g, ginv, Gamma, coords)
check("GU-schematic left side a1*G + c2*E_R2 is divergence-free (marble kept, augmented)",
      all(sp.simplify(c) == 0 for c in divL))

# ----------------------------------------------------------------------------
print("\n" + "=" * 70)
print(f"W152 checks: {PASS} passed, {FAIL} failed")
print("=" * 70)
import sys
sys.exit(0 if FAIL == 0 else 1)
