"""THREAD D1 -- concrete algebraic check: does the H-class GU section Willmore-EL, at leading
(linearized) order, match the field equation of conformal (Weyl) gravity -- i.e. the linearized Bach
equation?

BACKGROUND (what is being compared).
  * H-class GU: the section s: X^4 -> Y^14 = Met(X^4), s(x) = (x, g_ab(x)), extremizes E[s] = int |H|^2
    (mean-curvature functional; the conformal-Willmore member). Its EL is the Willmore equation
        Delta^perp H + Q^TF(B) + c_W (R^Y . H)^TF = 0.
    Principled (section-6.1 normalized) mean-curvature vector at linear order in the fiber perturbation
    h_ab = g_ab - eta_ab is the trace of the graph Hessian:
        H^(1)_ab = eta^{mu nu} d_mu d_nu h_ab = box(h)_ab.
    The leading (linear) Willmore-EL operator is then Delta^perp H^(1) = box H^(1) = box^2 h_ab
    (flat normal connection at linear order). => a FOURTH-ORDER operator on the metric perturbation.
  * Conformal (Weyl) gravity (Mannheim): S = -alpha_g int C_{mnrs} C^{mnrs}, EOM = Bach equation
    B_{mn} = nabla^r nabla^s C_{mrns} + (1/2) R^{rs} C_{mrns} = 0. FOURTH-ORDER in g. Linearized about
    flat space the second term is O(h^2), so B^(1)_{mn} = d^r d^s C^(1)_{mrns}.

CLAIM UNDER TEST (concrete, non-imported):
  On a transverse-traceless (TT) metric perturbation, the linearized H-class Willmore-EL operator box^2 h
  is PROPORTIONAL to the linearized Bach tensor -- they are the SAME fourth-order operator on the spin-2
  (TT) sector -- while OFF the TT sector (a pure-trace / conformal mode) they DIFFER: Bach vanishes
  (conformally-flat => Weyl = 0 => Bach = 0) but box^2 h does not. This pins the identification as
  "H-class GU CONTAINS the conformal-gravity operator on the spin-2 sector, and differs precisely in the
  trace/conformal sector (the sector the conformal-Willmore subtraction and the GU fiber structure govern)."

Method: exact sympy. h_ab = eps_ab * F(k.x) for a symbolic single-variable F, so every derivative is exact
and the identity is tested for ALL wave profiles F at once. Non-null k kept general (k.k symbolic).

Run: python tests/threads/D_hclass_vs_conformal_gravity.py
"""
from __future__ import annotations

import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{('  ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(name)


# ---------------------------------------------------------------------------
# Setup: flat background, coordinates, a symbolic plane-wave profile.
# ---------------------------------------------------------------------------
t, x, y, z = sp.symbols('t x y z', real=True)
coords = [t, x, y, z]
eta = sp.diag(-1, 1, 1, 1)
eta_inv = eta  # eta is its own inverse

# wavevector k_mu (lower). Keep t,x components general; y,z zero so TT choice below is clean.
kt, kx = sp.symbols('k_t k_x', real=True)
klow = [kt, kx, 0, 0]
kup = [sum(eta_inv[m, n] * klow[n] for n in range(4)) for m in range(4)]  # k^mu
kk = sp.simplify(sum(kup[m] * klow[m] for m in range(4)))                 # k.k = -k_t^2 + k_x^2

u = sum(klow[m] * coords[m] for m in range(4))
F = sp.Function('F')


def wave(pol):
    """h_ab(x) = pol_ab * F(k.x)."""
    return sp.Matrix(4, 4, lambda a, b: pol[a][b] * F(u))


def d(expr, mu):
    return sp.diff(expr, coords[mu])


# ---------------------------------------------------------------------------
# Linearized curvature machinery (exact, index loops).
# ---------------------------------------------------------------------------
def riem_low(h):
    # R^(1)_{a b c d} = 1/2 ( d_b d_c h_ad + d_a d_d h_bc - d_a d_c h_bd - d_b d_d h_ac )
    R = {}
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for dd in range(4):
                    R[(a, b, c, dd)] = sp.Rational(1, 2) * (
                        d(d(h[a, dd], b), c) + d(d(h[b, c], a), dd)
                        - d(d(h[b, dd], a), c) - d(d(h[a, c], b), dd)
                    )
    return R


def ricci_low(R):
    Ric = sp.zeros(4, 4)
    for a in range(4):
        for b in range(4):
            Ric[a, b] = sum(eta_inv[c, dd] * R[(c, a, dd, b)] for c in range(4) for dd in range(4))
    return Ric


def ricci_scalar(Ric):
    return sum(eta_inv[a, b] * Ric[a, b] for a in range(4) for b in range(4))


def weyl_low(R, Ric, Rs):
    # 4D: C_abcd = R_abcd - (g_a[c Ric_d]b - g_b[c Ric_d]a) + (1/3) Rs g_a[c g_d]b
    # antisymmetrization [c d] with weight 1/2.
    def g(a, b):
        return eta[a, b]
    C = {}
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for dd in range(4):
                    term_ric = sp.Rational(1, 2) * (
                        g(a, c) * Ric[dd, b] - g(a, dd) * Ric[c, b]
                        - g(b, c) * Ric[dd, a] + g(b, dd) * Ric[c, a]
                    )
                    term_rs = sp.Rational(1, 3) * Rs * sp.Rational(1, 2) * (
                        g(a, c) * g(dd, b) - g(a, dd) * g(c, b)
                    )
                    C[(a, b, c, dd)] = R[(a, b, c, dd)] - term_ric + term_rs
    return C


def bach_lin(C):
    # B^(1)_{mn} = d^r d^s C_{m r n s}  (linear order; the (1/2)R^{rs}C term is O(h^2))
    B = sp.zeros(4, 4)
    for m in range(4):
        for n in range(4):
            s_expr = 0
            for r in range(4):
                for s2 in range(4):
                    ru = sum(eta_inv[r, rp] for rp in [r])  # placeholder; do raise explicitly below
            # explicit raise of r,s
            acc = 0
            for r in range(4):
                for s2 in range(4):
                    for rp in range(4):
                        for sp_ in range(4):
                            acc += eta_inv[r, rp] * eta_inv[s2, sp_] * d(d(C[(m, r, n, s2)], rp), sp_)
            B[m, n] = sp.simplify(acc)
    return B


def box(h):
    return sp.Matrix(4, 4, lambda a, b: sum(eta_inv[m, n] * d(d(h[a, b], m), n) for m in range(4) for n in range(4)))


# ===========================================================================
# (1) TT sector: h_ab = TT graviton, k in t-x plane, polarization in y-z block.
#     transverse (k^mu eps_{mu a}=0) holds since eps has only y,z entries;
#     traceless (eta^{ab} eps_ab = 0): eps_yy + eps_zz = 1 + (-1) = 0.
# ===========================================================================
eps_TT = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, -1]]
h_TT = wave(eps_TT)

# verify TT algebraically
trace_TT = sp.simplify(sum(eta_inv[a, b] * h_TT[a, b] for a in range(4) for b in range(4)))
transv_TT = [sp.simplify(sum(kup[m] * h_TT[m, a] for m in range(4))) for a in range(4)]
check("TT ansatz is traceless (eta^ab h_ab = 0)", trace_TT == 0)
check("TT ansatz is transverse (k^mu h_{mu a} = 0 all a)", all(e == 0 for e in transv_TT))

R_TT = riem_low(h_TT)
Ric_TT = ricci_low(R_TT)
Rs_TT = sp.simplify(ricci_scalar(Ric_TT))
C_TT = weyl_low(R_TT, Ric_TT, Rs_TT)
B_TT = bach_lin(C_TT)
box2_TT = box(box(h_TT))

# H-class leading Willmore-EL operator = box^2 h.  Compare component-by-component to Bach.
# Find the proportionality constant on the (y,y) component (nonzero).
def max_deriv_order(expr):
    orders = [sum(n for _, n in dv.variable_count) for dv in expr.atoms(sp.Derivative)]
    return max(orders) if orders else 0
comp = (2, 2)  # y,y
b_yy = sp.simplify(B_TT[comp])
w_yy = sp.simplify(box2_TT[comp])
print(f"[TT sector]  k.k = {kk}")
print(f"    box^2 h_yy         = {w_yy}")
print(f"    Bach^(1)_yy        = {b_yy}")

# proportionality: is box^2 h == lambda * Bach on TT, with a single scalar lambda for all components?
# Solve lambda from the yy component, then verify on every component.
lam = sp.symbols('lambda')
sol = sp.solve(sp.Eq(w_yy, lam * b_yy), lam)
lam_val = sp.simplify(sol[0]) if sol else None
print(f"    => box^2 h = ({lam_val}) * Bach^(1) on the yy component")

allmatch = True
for a in range(4):
    for b in range(4):
        diff = sp.simplify(box2_TT[a, b] - lam_val * B_TT[a, b])
        if diff != 0:
            allmatch = False
check("on the TT (spin-2) sector, box^2 h = lambda * Bach^(1) with ONE scalar lambda for ALL components",
      allmatch and lam_val is not None,
      f"lambda = {lam_val} (H-class Willmore-EL operator == conformal-gravity Bach operator on spin-2)")
check("the shared operator is genuinely FOURTH-ORDER (both carry 4 derivatives of F)",
      max_deriv_order(b_yy) == 4 and max_deriv_order(w_yy) == 4,
      f"max deriv order: Bach={max_deriv_order(b_yy)}, box^2 h={max_deriv_order(w_yy)} -- NOT 2nd-order Einstein")

# record lambda: it is a fixed nonzero RATIONAL constant (its exact sign/magnitude is fixed by the
# Riemann/Weyl/Bach sign convention -- here box^2 h = -4 * Bach, i.e. Bach = -(1/4) box^2 h on TT).
# What is convention-INDEPENDENT and load-bearing: a SINGLE rational scalar relates the two operators
# on the entire spin-2 sector, and it is nonzero -- i.e. the operators are proportional, not merely
# "same order". The specific rational (-4) is not a fitted number; it is what the computation returns.
check("the proportionality constant is a fixed nonzero RATIONAL (convention-dependent sign/magnitude)",
      lam_val is not None and lam_val.is_rational and lam_val != 0,
      f"box^2 h = ({lam_val}) * Bach^(1) on TT -- one number relates the two fourth-order operators")

# ===========================================================================
# (2) Trace / conformal sector: h_ab = phi * eta_ab (pure conformal mode).
#     Weyl of a conformally-flat metric = 0 => Bach = 0. But box^2 h != 0.
#     This is exactly WHERE H-class GU (naive |H|^2) and conformal gravity DIFFER.
# ===========================================================================
eps_tr = [[eta[a, b] for b in range(4)] for a in range(4)]   # eps_ab = eta_ab  (phi = F)
h_tr = wave(eps_tr)
R_tr = riem_low(h_tr)
Ric_tr = ricci_low(R_tr)
Rs_tr = sp.simplify(ricci_scalar(Ric_tr))
C_tr = weyl_low(R_tr, Ric_tr, Rs_tr)
B_tr = bach_lin(C_tr)
box2_tr = box(box(h_tr))

weyl_zero = all(sp.simplify(C_tr[key]) == 0 for key in C_tr)
bach_zero = all(sp.simplify(B_tr[a, b]) == 0 for a in range(4) for b in range(4))
box2_nonzero = any(sp.simplify(box2_tr[a, b]) != 0 for a in range(4) for b in range(4))
print(f"\n[trace/conformal sector]  h_ab = phi * eta_ab")
print(f"    linearized Weyl C^(1) == 0 (conformally flat): {weyl_zero}")
print(f"    Bach^(1) == 0:                                 {bach_zero}")
print(f"    box^2 h == 0:                                  {not box2_nonzero}  (box^2 h_yy = {sp.simplify(box2_tr[2,2])})")
check("conformal gravity: Bach VANISHES on the pure-conformal mode (Weyl^(1)=0)", weyl_zero and bach_zero)
check("H-class naive box^2 h does NOT vanish on the conformal mode -> the two theories DIFFER off spin-2",
      box2_nonzero,
      "this is the trace/conformal sector governed by the conformal-Willmore subtraction + the GU fiber")

# ===========================================================================
print("\n[verdict -- D1]")
print("  The linearized H-class GU section Willmore-EL operator (box^2 h) and the linearized conformal-")
print("  gravity Bach operator are the SAME fourth-order operator on the transverse-traceless (spin-2)")
print(f"  sector: box^2 h = ({lam_val}) * Bach^(1) there, exactly (one rational scalar; sign is convention).")
print("  They DIFFER on the trace/conformal sector, where")
print("  Bach vanishes (Weyl=0) but the naive |H|^2 Willmore operator does not. Reading:")
print("   - IDENTITY at the level of the leading spin-2 kinetic operator (both = box^2 on the graviton);")
print("     H-class GU is a conformal-Willmore / fourth-order-gravity-class theory, not Einstein-class.")
print("   - NOT a literal identity of theories: (a) GU's is the EXTRINSIC Willmore functional of the")
print("     section into Met(X^4), whose FULL nonlinear EL also carries the O(M^0) DeWitt algebraic-slice /")
print("     ambient-curvature pieces (ii-s-coordinate-formula sec 6.1) that pure Weyl^2 has no analog for;")
print("   - (b) the trace-sector mismatch is removed only by the conformal-Willmore subtraction (|H|^2 ->")
print("     conformally invariant combination) AND by GU's fiber/gauge (Sp(64)/theta) structure, which")
print("     conformal gravity does not have. So: SPECIAL-CASE / CONTAINS on the spin-2 operator, genuinely")
print("     RICHER (fiber + ambient) off it. Grade: concrete algebraic identity on the spin-2 sector;")
print("     structural for the full-theory relationship.")

if FAIL:
    print(f"\nFAILED: {FAIL}")
    raise SystemExit(1)
print("\nexit 0 = H-class Willmore-EL proportional to conformal-gravity Bach operator on spin-2")
print("         (box^2 h = -4*Bach, one rational scalar); differs on the trace/conformal sector;")
print("         full identity gated on conformal-Willmore subtraction + GU fiber structure.")
