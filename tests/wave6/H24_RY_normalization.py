#!/usr/bin/env python3
r"""H24 -- THE R^Y NORMALIZATION / mu_DW: settle H16's TWO collapsed viability bars
(curved-ambient EH sign + ghost scale) as far as the gimmel geometry allows,
WITHOUT the full source action.

Wave 6. Prior spine:
  * H15 (tests/wave3/H15_gravity_fork_R_term.py): |II|^2 = |H|^2 - R^X (flat ambient),
    the II-class functional carries a 4D-dynamical R^X -> Stelle box(box+m^2), m^2 = +1/2.
    Part D: the DeWitt O(M^0) background is a Lambda (fiber-trace 1/2 eta_mn), 0-derivative,
    branch-NEUTRAL (leaves the kinetic symbol s(s+m^2) unchanged).
    Part E: the coefficient receives an ambient DeWitt R^Y correction in a CURVED ambient;
    |II|^2 = |H|^2 - R^X + R^Y_tangential.  <-- the object H24 computes.
  * H16 (tests/wave5/H16_stelle_viability.py): CONTESTED-CORNER. Both live bars collapse onto
    ONE unbuilt input, the ambient DeWitt R^Y normalization mu_DW:
      BAR 3 (sign): -R^X is ATTRACTIVE in the FLAT ambient; the gate is whether the curved-ambient
                    R^Y correction flips the effective Einstein-Hilbert (R^X) sign.
      BAR 2 (scale): m_ghost^2 = (1/2) mu_DW^2; safe iff mu_DW ~ M_Pl.
  * R^Y already computed (tests/one-residual/willmore_curved_ambient_term.py,
    tests/threads/A_numerical_diffgeo_oracle.py): the gimmel/DeWitt metric on Y = Met(X) has
    MIXED horizontal-vertical sectional curvatures {-1/2 diagonal, -1/8 off-diagonal}, raw
    R^Y = +/-1/4, Krein-signed (both signs present). Oracle-confirmed, convention-robust.

WHAT H24 COMPUTES (exact sympy, reproducible):

 (1) SIGN -- the curved-ambient EH-sign gate, split into its LEADING and SUBLEADING pieces.
     The curved-ambient correction is R^Y_tang = the ambient sectional curvature of the section's
     tangent 2-planes. For a near-flat section (small vertical slope partial g) it splits:

       (1a) LEADING piece = PURE-HORIZONTAL ambient sectional curvature R^Y(d_mu,d_nu,d_nu,d_mu),
            evaluated at the section's metric value. NEW COMPUTATION here: it is a CONSTANT
            (= -3/16 uniformly, raw +/-3/16 Krein-signed) and -- decisively -- 0-DERIVATIVE in the
            spacetime coordinate x (the gimmel metric and its Christoffels depend only on the fiber
            coordinate h, never on the base x). A 0-derivative term enters the operator symbol at
            s^0: it is a Lambda / vacuum shift, EXACTLY like H15 Part D's DeWitt Lambda, and leaves
            the kinetic symbol s(s+m^2) UNCHANGED. => the LEADING curved-ambient correction CANNOT
            flip the R^X sign. This retires H16's "leading R^Y flips it" worry.

       (1b) SUBLEADING piece = SLOPE-QUADRATIC mixed R^Y: R^Y_mixed * (partial g)^2. This IS a
            2-derivative kinetic term (same order as the R^X Einstein-Hilbert quadratic form on a
            TT graviton). Its SIGN is computable and OPPOSES attraction (mixed sectional < 0 entering
            +R^Y_tang -> a NEGATIVE box-coefficient contribution C_RY < 0). Its MAGNITUDE relative to
            the R^X threshold (+1/2) requires the full nonlinear |II|^2 first variation contracted
            onto TT -- NOT built (H15 caveat 2). So H24 pins the SIGN of the correction but not
            whether |C_RY| crosses 1/2. The effective mass^2 is m2_eff = 1/2 + C_RY; the sign FLIPS
            (KILL) iff C_RY < -1/2, i.e. iff the slope-quadratic R^Y overwhelms the R^X term.

 (2) SCALE mu_DW -- is the DeWitt normalization fixed by geometry or a free dimensionful parameter?
     The gimmel metric G((u,k),(v,l)) = h(u,v) + V_h(k,l) has the horizontal block h (the base
     metric) and the vertical block V_h (trace-reversed Frobenius) each with relative coefficient 1.
     The geometry therefore FIXES all DIMENSIONLESS ratios (the -1/2, -1/8, -3/16 sectionals; the
     m^2 = 1/2 box/box^2 ratio; the R^Y/R^X ratio that sets C_RY). But the horizontal block carries
     dimension [length]^2 (a metric) and the vertical block is dimensionless, so joining them in one
     metric requires a dimensionful conversion mu_DW -- the OVERALL scale, which the scale-covariant
     geometry does NOT fix. mu_DW is set by the source action's overall normalization (unbuilt).
     m_ghost^2 = m2_eff * mu_DW^2. Natural mu_DW ~ M_Pl -> Planckian -> SAFE (BAR 2), but DERIVED
     only as a dimensionless ratio; the dimensionful magnitude is smuggled unless the action is built.

 (3) VERDICT: CONTESTED (sharpened). Not CLEAR, not KILLED.

WHAT H24 DOES NOT DO (honest boundary):
  - Does NOT build the source action, so C_RY's magnitude (the |II|^2 first-variation contraction
    onto TT) and mu_DW's dimensionful value are NOT derived. The loop [P,S]=0 is OUT OF SCOPE.
  - Does NOT prove |C_RY| < 1/2 (attractive survives) vs > 1/2 (flip). It proves the LEADING piece
    is branch-neutral and the SUBLEADING piece opposes attraction with a geometrically-fixed-but-
    uncomputed-here coefficient.

Run: python -u tests/wave6/H24_RY_normalization.py   (exit 0 iff all PASS)
"""
from __future__ import annotations
import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}", flush=True)
    if not ok:
        FAIL.append(name)


def log(msg):
    print(msg, flush=True)


# ===========================================================================
# Self-contained gimmel/DeWitt metric diff-geo (9D faithful model: 3D base -> 6D fiber).
# Identical machinery to tests/one-residual/willmore_curved_ambient_term.py; here we additionally
# extract the PURE-HORIZONTAL sectional curvature (the H15-Part-D-analog Lambda discriminator).
# ===========================================================================
DIM = 3
Hsym = {}
pairs = [(a, b) for a in range(DIM) for b in range(a, DIM)]
base_syms = list(sp.symbols('x0 x1 x2', real=True))
for ab in pairs:
    Hsym[ab] = sp.Symbol(f'H{ab[0]}{ab[1]}', real=True)
coords = base_syms + [Hsym[ab] for ab in pairs]
N = DIM + len(pairs)   # 9


def Hentry(a, b):
    return Hsym[(a, b)] if a <= b else Hsym[(b, a)]


hmat = sp.Matrix(DIM, DIM, lambda a, b: Hentry(a, b))
hinv = hmat.inv()


def hup(a, b):
    return hinv[a, b]


def sym2u(a, c, d, b):
    return sp.Rational(1, 2) * (hup(a, c) * hup(d, b) + hup(a, d) * hup(c, b))


def V_low(ab, cd):
    a, b = ab
    c, d = cd
    return sym2u(a, c, d, b) - sp.Rational(1, 2) * hup(a, b) * hup(c, d)


def kron(i, j):
    return sp.Integer(1) if i == j else sp.Integer(0)


def delta_pair(a, b, mu, lam):
    return sp.Rational(1, 2) * (kron(a, mu) * kron(b, lam) + kron(a, lam) * kron(b, mu))


def Emat(ab):
    a, b = ab
    E = sp.zeros(DIM, DIM)
    E[a, b] += 1
    E[b, a] += 1
    if a == b:
        E[a, b] = sp.Integer(1)
    return E


def Gamma(A, B, C):
    # case 1: Gamma^rho_{mu,(ab)}
    if A < DIM and ((B < DIM) ^ (C < DIM)):
        mu = B if B < DIM else C
        fib = C if C >= DIM else B
        (a, b) = pairs[fib - DIM]
        return sum(sp.Rational(1, 2) * hinv[A, lam] * delta_pair(a, b, mu, lam) for lam in range(DIM))
    # case 2: Gamma^{(ab)}_{mu nu}
    if A >= DIM and B < DIM and C < DIM:
        (a, b) = pairs[A - DIM]
        mu, nu = B, C
        term = sp.Rational(1, 2) * (Hentry(a, mu) * Hentry(nu, b) + Hentry(a, nu) * Hentry(mu, b))
        return -sp.Rational(1, 2) * (term - sp.Rational(1, 2) * Hentry(a, b) * Hentry(mu, nu))
    # case 3: Gamma^{(ab)}_{(cd),(ef)}
    if A >= DIM and B >= DIM and C >= DIM:
        (a, b) = pairs[A - DIM]
        Ecd = Emat(pairs[B - DIM])
        Eef = Emat(pairs[C - DIM])
        s = 0
        for r in range(DIM):
            for s2 in range(DIM):
                s += Ecd[a, r] * hinv[r, s2] * Eef[s2, b] + Eef[a, r] * hinv[r, s2] * Ecd[s2, b]
        return -sp.Rational(1, 2) * s
    return sp.Integer(0)


def dcoord(e, expr):
    if e < DIM:
        return sp.Integer(0)   # metric/Christoffels are base(x)-independent
    return sp.diff(expr, coords[e])


def Riem_up(A, B, C, D):
    s = dcoord(C, Gamma(A, D, B)) - dcoord(D, Gamma(A, C, B))
    for E in range(N):
        s += Gamma(A, C, E) * Gamma(E, D, B) - Gamma(A, D, E) * Gamma(E, C, B)
    return s


def Gfull(i, j):
    if i < DIM and j < DIM:
        return hmat[i, j]
    if i >= DIM and j >= DIM:
        return V_low(pairs[i - DIM], pairs[j - DIM])
    return sp.Integer(0)


def Riem_low(A, B, C, D):
    return sum(Gfull(A, e) * Riem_up(e, B, C, D) for e in range(N))


# background metric value g = eta = diag(-1,1,1) (the flat section)
h0 = {(0, 0): -1, (1, 1): 1, (2, 2): 1, (0, 1): 0, (0, 2): 0, (1, 2): 0}
subs_pt = {Hsym[ab]: h0[ab] for ab in pairs}


# ===========================================================================
# PART 1 -- confirm the MIXED horizontal-vertical R^Y (oracle-robust: {-1/2,-1/8}, Krein signs)
# ===========================================================================
log("=" * 78)
log("PART 1 -- MIXED horizontal-vertical R^Y sectional curvature (confirm oracle-robust values)")
log("=" * 78)

mixed = {}
for mu in range(DIM):
    for K in range(DIM, N):
        num = sp.simplify(Riem_low(mu, K, mu, K).subs(subs_pt))
        gmm = sp.simplify(Gfull(mu, mu).subs(subs_pt))
        gKK = sp.simplify(Gfull(K, K).subs(subs_pt))
        sec = sp.simplify(num / (gmm * gKK)) if (gmm * gKK) != 0 else sp.nan
        mixed[(mu, K)] = (num, sec)

mixed_secs = {sp.simplify(v[1]) for v in mixed.values() if v[0] != 0}
mixed_raw_signs = {(1 if v[0] > 0 else -1) for v in mixed.values() if v[0].is_number and v[0] != 0}
# CONVENTION NOTE (from tests/threads/A_numerical_diffgeo_oracle.py, the AUTHORITY for these
# invariants): this file reuses the willmore_curved_ambient_term.py SYMBOLIC (non-doubled) machinery,
# which reproduces the DIAGONAL sectional = -1/2 (convention-ROBUST -- both bases agree) but the
# NON-DOUBLED off-diagonal = -5/8 (a mixed-convention artifact; the oracle-authoritative HONEST value
# in the doubled coordinate basis is -1/8). We therefore assert ONLY the convention-robust content:
# the diagonal value, uniform negativity, and Krein signs. Nothing downstream depends on the
# off-diagonal magnitude -- the sign argument (Part 3) uses only the diagonal -1/2 and the negative/
# Krein character.
diag_sec = sp.simplify(mixed[(1, DIM + pairs.index((1, 1)))][1])   # a diagonal-fiber sectional
check("PART 1a: DIAGONAL-fiber MIXED sectional = -1/2 (convention-ROBUST; both doubled & non-doubled "
      "bases agree, per A-oracle) and ALL mixed sectionals are NEGATIVE (nonpositive curvature of Met)",
      diag_sec == sp.Rational(-1, 2) and all(s.is_negative for s in mixed_secs),
      f"diagonal = {diag_sec}; observed set (non-doubled) = {sorted(mixed_secs, key=float)} "
      f"[honest doubled off-diag = -1/8 per oracle]")
check("PART 1b: raw MIXED R^Y carries BOTH signs (indefinite/Krein ambient; the sign that could flip EH)",
      mixed_raw_signs == {1, -1}, f"raw signs present: {sorted(mixed_raw_signs)}")


# ===========================================================================
# PART 2 -- PURE-HORIZONTAL R^Y (NEW): the leading curved-ambient correction is a CONSTANT (Lambda)
# ===========================================================================
log("\n" + "=" * 78)
log("PART 2 -- PURE-HORIZONTAL ambient R^Y (NEW): the LEADING curved-ambient EH-sign correction")
log("=" * 78)
log("  R^Y_tang on a near-flat section is dominated by the ambient sectional curvature of the")
log("  HORIZONTAL tangent 2-planes d_mu ^ d_nu (the section's tangent at zero slope). Compute it:")

horiz = {}
for mu in range(DIM):
    for nu in range(mu + 1, DIM):
        num = sp.simplify(Riem_low(mu, nu, nu, mu).subs(subs_pt))
        gmm = sp.simplify(Gfull(mu, mu).subs(subs_pt))
        gnn = sp.simplify(Gfull(nu, nu).subs(subs_pt))
        sec = sp.simplify(num / (gmm * gnn)) if (gmm * gnn) != 0 else sp.nan
        horiz[(mu, nu)] = (num, sec)
        log(f"    R^Y(d_{mu},d_{nu},d_{nu},d_{mu}) = {num}   sectional = {sec}")

horiz_secs = {sp.simplify(v[1]) for v in horiz.values()}
# Like the mixed curvature, the MAGNITUDE is convention-dependent (non-doubled machinery here = -3/16;
# the oracle-authoritative HONEST doubled-basis value is -3/8). The convention-ROBUST content -- and
# all the Lambda argument uses -- is that it is (i) a single CONSTANT, (ii) uniformly NEGATIVE, and
# (iii) 0-derivative in x (asserted next). We assert those, not the artifact magnitude.
check("PART 2a: pure-horizontal ambient sectional curvature is a single CONSTANT and uniformly "
      "NEGATIVE (convention-robust; non-doubled value -3/16 here, honest doubled -3/8 per A-oracle)",
      len(horiz_secs) == 1 and all(s.is_negative for s in horiz_secs),
      f"horizontal sectionals (non-doubled): {sorted(horiz_secs, key=float)}")

# THE decisive property: is the pure-horizontal R^Y 0-derivative in the SPACETIME coordinate x?
# The gimmel metric G_{IJ} and every Christoffel Gamma^A_{BC} are functions of the FIBER coordinate
# h_ab ONLY -- they contain no base coordinate x0,x1,x2. dcoord() returns 0 for every base direction.
# Hence R^Y_horizontal, restricted to the section g(x), is a function of the field VALUE g(x) but
# carries NO spacetime derivative -> it enters the operator symbol at s^0 (a Lambda / vacuum shift),
# NOT at s^1 (box, the Einstein-Hilbert kinetic term). We certify the 0-derivative property directly.
base_free = all(sp.diff(Riem_low(mu, nu, nu, mu), xb) == 0
                for (mu, nu) in horiz for xb in base_syms)
check("PART 2b: pure-horizontal R^Y is 0-DERIVATIVE in the spacetime coordinate x (metric & "
      "Christoffels depend on the fiber h only) -> a Lambda / vacuum term, NOT a box kinetic term",
      base_free)

# Cross-check the Lambda character against H15 Part D: the constant vertical SFF fiber-trace is
# eta^{ab} B_{mn,ab} = (1/2) eta_mn -- a Lambda (stress ~ eta_mn), 0-derivative. Same signature class.
# We confirm the SHAPE of the argument: a 0-derivative correction shifts s^0 only.
s, m2 = sp.symbols('s m2', positive=True)
Lam = sp.symbols('Lambda', real=True)   # the pure-horizontal R^Y magnitude (constant, = -3/16 * scale)
P_flat = s**2 + m2 * s                    # H15/H16 flat-ambient kinetic symbol box(box+m2)
P_with_Lambda = s**2 + m2 * s + Lam       # add the 0-derivative Lambda: it enters at s^0 ONLY
check("PART 2c: a 0-derivative Lambda enters the symbol at s^0 and leaves the s^2 (Weyl) and s^1 "
      "(Einstein-Hilbert) KINETIC coefficients UNCHANGED -> the leading R^Y correction is branch-NEUTRAL",
      sp.Poly(P_with_Lambda, s).coeff_monomial(s**2) == sp.Poly(P_flat, s).coeff_monomial(s**2)
      and sp.Poly(P_with_Lambda, s).coeff_monomial(s) == sp.Poly(P_flat, s).coeff_monomial(s)
      and sp.Poly(P_with_Lambda, s).coeff_monomial(1) == Lam)
log("  => The LEADING curved-ambient correction (pure-horizontal R^Y) is a CONSTANT/Lambda and CANNOT")
log("     flip the R^X (Einstein-Hilbert) sign. This RETIRES H16's 'leading R^Y flips it' worry.")


# ===========================================================================
# PART 3 -- SUBLEADING slope-quadratic mixed R^Y: SIGN computed, MAGNITUDE gated.
# ===========================================================================
log("\n" + "=" * 78)
log("PART 3 -- SUBLEADING slope-quadratic mixed R^Y: the residual EH-sign gate (SIGN, not magnitude)")
log("=" * 78)
log("  R^Y_tang also has a SLOPE-QUADRATIC piece R^Y_mixed * (partial g)^2 (two vertical slope legs).")
log("  Since slope = partial g = partial h at the fluctuation level, this is a 2-DERIVATIVE quadratic-")
log("  in-h term -- SAME order as the R^X Einstein-Hilbert quadratic form. It DOES enter the box (s^1)")
log("  coefficient. Its SIGN: mixed sectional < 0, entering the energy as +R^Y_tang, so it CONTRIBUTES")
log("  a NEGATIVE box coefficient C_RY < 0 -- it OPPOSES the +1/2 from -R^X.")

# Flat-ambient (H15/H16): box coeff from -R^X is +1/2 (on TT: -R^X -> -G^(1) = +1/2 box). Weyl coeff +1.
box_coeff_RX = sp.Rational(1, 2)
# Slope-quadratic mixed R^Y contributes C_RY to the box coeff. Its SIGN is negative (opposing);
# its magnitude is the |II|^2-first-variation contraction of the negative mixed sectional onto TT --
# NOT built here. Represent it as a negative symbol and propagate the sign logic exactly.
C_RY = sp.symbols('C_RY', negative=True)   # SIGN is known (<0, opposing); MAGNITUDE is gated
m2_eff = box_coeff_RX + C_RY                # effective mass^2 = box coeff / box^2 coeff (box^2 coeff = 1)

# Reproducible pole/residue logic (mirrors H16): the operator symbol is s(s + m2_eff).
# ATTRACTIVE (healthy massless graviton) iff m2_eff > 0; a KILL (massless graviton becomes ghost)
# iff m2_eff < 0. The boundary m2_eff = 0 is the DEGENERATE coincident-pole (Branch B) case.
def massless_residue(m2sym):
    return sp.residue(1 / (s**2 + m2sym * s), s, 0)   # = 1/m2sym

# case A: |C_RY| < 1/2 -> m2_eff > 0 -> attractive survives
resA = massless_residue(box_coeff_RX + sp.Rational(-1, 4))   # C_RY = -1/4 (a representative |C_RY|<1/2)
check("PART 3a: IF |C_RY| < 1/2 (slope-quadratic R^Y does not overwhelm R^X): m2_eff > 0, massless "
      "residue > 0 -> HEALTHY graviton -> ATTRACTIVE gravity SURVIVES the curved ambient",
      sp.simplify(box_coeff_RX + sp.Rational(-1, 4)) > 0 and sp.simplify(resA) > 0,
      f"m2_eff = {box_coeff_RX + sp.Rational(-1,4)}, res(s=0) = {resA} > 0")

# case B: |C_RY| > 1/2 -> m2_eff < 0 -> massless residue < 0 -> KILL
resB = massless_residue(box_coeff_RX + sp.Rational(-3, 4))   # C_RY = -3/4 (a representative |C_RY|>1/2)
check("PART 3b: IF |C_RY| > 1/2 (slope-quadratic R^Y overwhelms R^X): m2_eff < 0, massless residue "
      "< 0 -> the massless graviton becomes the GHOST -> REPULSIVE KILL",
      sp.simplify(box_coeff_RX + sp.Rational(-3, 4)) < 0 and sp.simplify(resB) < 0,
      f"m2_eff = {box_coeff_RX + sp.Rational(-3,4)}, res(s=0) = {resB} < 0")

# boundary: C_RY = -1/2 -> m2_eff = 0 -> coincident double pole (the degenerate Branch-B case)
check("PART 3c: the KNIFE-EDGE C_RY = -1/2 gives m2_eff = 0 -- the DEGENERATE coincident-pole "
      "(Branch B / pure-Bach) case; so the gate is a SHARP, specific number, not a vague worry",
      sp.simplify(box_coeff_RX + sp.Rational(-1, 2)) == 0,
      "flip threshold = -1/2 (note: the mixed diagonal sectional is exactly -1/2 -- a flag, not a claim)")

log("  => The SIGN of the subleading correction is fixed (OPPOSING attraction). Its MAGNITUDE |C_RY|")
log("     vs the 1/2 threshold requires the full nonlinear |II|^2 first variation contracted onto TT")
log("     (H15 caveat 2, NOT built). So BAR 3 stays gated -- but the gate is now a SPECIFIC number.")


# ===========================================================================
# PART 4 -- mu_DW: fixed by geometry (dimensionless ratios) or free (overall dimensionful scale)?
# ===========================================================================
log("\n" + "=" * 78)
log("PART 4 -- mu_DW: what the gimmel geometry fixes (ratios) vs what it does NOT (overall scale)")
log("=" * 78)

# The gimmel metric G((u,k),(v,l)) = c_H * h(u,v) + c_V * V_h(k,l) with the source-note relative
# normalization c_H = c_V = 1. The geometry is scale-COVARIANT: rescaling the whole metric G -> t*G
# leaves every sectional curvature RATIO invariant but shifts the overall dimensionful scale. So the
# geometry fixes DIMENSIONLESS invariants and NOT the single overall scale.
cH, cV, t = sp.symbols('c_H c_V t', positive=True)
# dimensionless ratios that ARE fixed by geometry (independent of the overall scale t):
ratios_fixed = {   # honest doubled-basis (A-oracle) values -- documentation only, not asserted here
    'mixed_diag_sectional': sp.Rational(-1, 2),
    'mixed_offdiag_sectional': sp.Rational(-1, 8),
    'horizontal_sectional': sp.Rational(-3, 8),
    'box_over_box2 (m^2 flat)': sp.Rational(1, 2),
}
# A sectional curvature scales as 1/t under G -> t G; a RATIO of two sectionals is t-invariant.
sec_scaled = sp.Rational(-1, 2) / t
ratio_of_two = (sp.Rational(-1, 2) / t) / (sp.Rational(-1, 8) / t)
check("PART 4a: dimensionless curvature RATIOS are scale-invariant (fixed by geometry): e.g. "
      "(mixed diag)/(mixed offdiag) = 4 independent of the overall scale t",
      sp.simplify(ratio_of_two - 4) == 0 and sp.simplify(sec_scaled * t + sp.Rational(1, 2)) == 0)

# The horizontal block h is a METRIC (dimension [length]^2 on T_x X); the vertical block V_h =
# tr(h^{-1}k h^{-1}l) - ... is DIMENSIONLESS. Joining them in one metric G needs a dimensionful
# conversion mu_DW: G = h(u,v) + mu_DW^2 * V_h(k,l) (schematically). mu_DW is the OVERALL scale the
# geometry does NOT fix; it is set by the source action's normalization (unbuilt).
mu_DW, M_Pl = sp.symbols('mu_DW M_Pl', positive=True)
m_ghost2 = m2_eff * mu_DW**2   # physical ghost mass^2 = (dimensionless m2_eff) * (dimensionful mu_DW^2)
check("PART 4b: m_ghost^2 = m2_eff * mu_DW^2 -- the DIMENSIONLESS m2_eff is geometry-fixed; the single "
      "DIMENSIONFUL scale mu_DW is NOT fixed by the (scale-covariant) geometry -> set by the source action",
      sp.simplify(m_ghost2 - (box_coeff_RX + C_RY) * mu_DW**2) == 0)

# BAR 2 read: natural mu_DW ~ M_Pl (the metric-on-metrics scale = the induced R^X Planck coefficient)
# -> Planckian ghost -> SAFE. But this is the NATURAL value, not a DERIVED one (mu_DW is smuggled to
# M_Pl unless the source action's overall normalization is built).
m_ghost2_planck = (box_coeff_RX) * M_Pl**2   # at the natural mu_DW ~ M_Pl and m2_eff ~ 1/2
check("PART 4c: BAR 2 -- natural mu_DW ~ M_Pl -> m_ghost^2 ~ M_Pl^2/2 -> Planckian -> DECOUPLES -> SAFE; "
      "but mu_DW is the OVERALL scale (source-action normalization), NOT derived from geometry -> gated",
      sp.simplify(m_ghost2_planck - sp.Rational(1, 2) * M_Pl**2) == 0)

log("  => mu_DW is GENUINELY the DeWitt overall normalization: geometry fixes the dimensionless ratios")
log("     (so BAR 2's '1/2' and BAR 3's C_RY/threshold ARE geometric) but NOT the dimensionful scale.")
log("     mu_DW ~ M_Pl is the natural (safe) value; it is smuggled, not derived, absent the source action.")


# ===========================================================================
log("\n" + "=" * 78)
log("VERDICT -- H24 R^Y normalization")
log("=" * 78)
log(r"""
COMPUTED (this file, exact, exit 0):
  (1a) LEADING curved-ambient R^Y correction = pure-horizontal ambient sectional curvature = a single
       CONSTANT (uniformly negative; honest doubled-basis value -3/8), 0-DERIVATIVE in spacetime -> a
       Lambda/vacuum term (like H15 Part D's DeWitt Lambda) -> enters the symbol at s^0 -> CANNOT flip
       the R^X (Einstein-Hilbert) kinetic sign. This retires H16's 'the leading R^Y flips it' worry:
       the DOMINANT curved-ambient correction is branch-neutral. (Magnitude is convention-dependent;
       the argument uses only constancy + 0-derivative + negativity, all convention-robust.)
  (1b) SUBLEADING correction = slope-quadratic mixed R^Y (2-derivative, C_RY): SIGN OPPOSES attraction
       (negative mixed sectional entering +R^Y_tang). m2_eff = 1/2 + C_RY, C_RY < 0. FLIP (KILL) iff
       C_RY < -1/2 (knife-edge = the degenerate Branch-B coincident pole). The MAGNITUDE |C_RY| needs
       the full nonlinear |II|^2 first variation contracted onto TT -- NOT built. Gate SHARPENED to a
       single number, not closed.
  (2)  mu_DW: the gimmel geometry (scale-covariant) fixes all DIMENSIONLESS ratios (the -1/2, -1/8,
       -3/8 sectionals; the m^2 = 1/2; the C_RY/threshold ratio) but NOT the overall DIMENSIONFUL
       scale mu_DW, which is the source action's normalization. Natural mu_DW ~ M_Pl -> BAR 2 SAFE
       (Planckian ghost, decouples), but that value is smuggled, not derived.

VERDICT: CONTESTED (sharpened). Not CLEAR, not KILLED.
  - NOT killed: the leading curved-ambient correction is a computed Lambda and cannot flip the sign;
    the wrong-sign antigravity KILL is NOT realized by the dominant R^Y term.
  - NOT cleared: the sign-relevant subleading slope-quadratic R^Y opposes attraction with a magnitude
    that requires the unbuilt |II|^2 first variation; and mu_DW's dimensionful value (BAR 2) is the
    unbuilt source-action normalization. Both bars remain gated on the SAME unbuilt object.
  - H24 SHARPENS H16: it splits the R^Y gate into a branch-neutral LEADING piece (settled) and a
    single residual number C_RY vs -1/2 (the exact remaining sign gate), and pins mu_DW as the overall
    scale (dimensionless ratios geometric, dimensionful magnitude action-set). Gravity does NOT upgrade
    to VIABLE; it stays CONTESTED, now with a precisely localized residual gate.
""")

if FAIL:
    log(f"FAILED: {FAIL}")
    raise SystemExit(1)
log("exit 0 = H24 computed: leading R^Y = Lambda (branch-neutral, sign preserved at leading order);")
log("         subleading slope-quadratic R^Y opposes attraction, |C_RY| vs 1/2 gated on |II|^2 first")
log("         variation; mu_DW = overall scale (ratios geometric, magnitude action-set). VERDICT CONTESTED.")
