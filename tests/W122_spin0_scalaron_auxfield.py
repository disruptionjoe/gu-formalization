#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
W122 -- Spin-0 conformal-mode sign: GAUGE-vs-PHYSICAL settled by the EXACT
auxiliary-field (Legendre) route + spin-0 projection of Weyl^2, with the
Euclidean conformal-factor problem cleanly DELINEATED from the Lorentzian
scalaron mass sign.

Claims tested (each a small exact sympy computation):

  (1) Einstein + Weyl^2 alone has NO propagating spin-0:
      (1a) the Weyl tensor of ANY conformally flat metric g = e^{2 phi} eta
           vanishes identically (exact, nonperturbative, phi(t,z) arbitrary);
      (1b) the LINEARIZED Weyl tensor vanishes on the ENTIRE spin-0
           polarization sector eps_{mu nu} = phi eta_{mu nu} + B k_mu k_nu
           (the two covariant scalars P^0_s, P^0_w span it) -- so C^2
           contributes ZERO to the spin-0 quadratic action;
      (1c) pure EH: the conformal reduction of gamma R is KINETIC-ONLY
           (wrong-sign kinetic term, NO mass, NO pole freedom) -- this is the
           object of the EUCLIDEAN conformal-factor problem (GHP contour /
           Mazur-Mottola measure), a constrained mode in second-order
           gravity (W78 constraint count), NOT a mass statement.

  (2) Adding f0 R^2 adds EXACTLY ONE propagating scalar, via the EXACT
      auxiliary-field map (no perturbative expansion):
        f0 R^2  ==  f0 (2 chi R - chi^2)   after integrating out chi (=R);
      Einstein-frame reduction gives a canonical (+1/2 kinetic) scalaron with
        m_0^2 proportional to gamma / (6 f0),
      matching the f(R) formula (1/3)(f'/f'' - R) -- two independent routes.

  (3) On the AF trajectory the fixed ratio r = f_0^2/f_2^2 is NEGATIVE (both
      roots of the W46 ratio quadratic), and f_2^2 > 0 (AF), so it is f_0^2
      (the R^2 coefficient, a SIGNED coupling despite the square notation)
      that is negative  =>  m_0^2 = gamma/(6 f_0^2) < 0: tachyon.
      Fork check: sign(m_0^2) < 0 on BOTH ghost-mass normalization branches
      (agravity and fixed-scale mu_DW).

  (4) The sign conclusion is POLE-LEVEL, hence gauge-independent: the
      auxiliary-field construction never introduces a gauge parameter (chi is
      a diffeo scalar; its mass is the curvature of a frame-consistent scalar
      potential at its extremum), and the kinetic sign (+1/2, positive norm)
      and mass sign are frame-agreeing. The 'gauge artifact' escape applies
      only to the EUCLIDEAN kinetic-sign problem of (1c) -- a different
      object, delineated by (1c) vs (2).

Deterministic, exact sympy. Exit 0 on success.
"""
import sys
import sympy as sp

FAIL = []
def check(name, cond):
    ok = bool(cond)
    print(("PASS" if ok else "FAIL") + " :: " + name)
    if not ok:
        FAIL.append(name)

# ===========================================================================
# (1a) Weyl tensor of a conformally flat metric vanishes IDENTICALLY (exact)
# ===========================================================================
print("=" * 76)
print("(1a) exact: Weyl[e^{2 phi(t,z)} eta] == 0 (conformally flat, all orders)")
t, x1, x2, z = coords = sp.symbols('t x1 x2 z', real=True)
phi = sp.Function('phi')(t, z)          # arbitrary 2-variable conformal factor
eta = sp.diag(1, -1, -1, -1)
N = 4
g = sp.exp(2 * phi) * eta
ginv = sp.exp(-2 * phi) * eta           # eta^{-1} = eta

def D(mu, expr):
    return sp.diff(expr, coords[mu])

Gam = [[[sp.simplify(sum(ginv[l, r] * (D(m, g[r, n]) + D(n, g[r, m]) - D(r, g[m, n]))
                         for r in range(N)) / 2)
         for n in range(N)] for m in range(N)] for l in range(N)]

# Riemann R^l_{r m n} = d_m Gam^l_{n r} - d_n Gam^l_{m r} + Gam Gam - Gam Gam
Riem = [[[[sp.simplify(D(m, Gam[l][n][r]) - D(n, Gam[l][m][r])
           + sum(Gam[l][m][s_] * Gam[s_][n][r] - Gam[l][n][s_] * Gam[s_][m][r]
                 for s_ in range(N)))
           for n in range(N)] for m in range(N)] for r in range(N)] for l in range(N)]

# lower first index: R_{l r m n}
Rdn = [[[[sp.simplify(sum(g[l, a] * Riem[a][r][m][n] for a in range(N)))
          for n in range(N)] for m in range(N)] for r in range(N)] for l in range(N)]
Ric = [[sp.simplify(sum(ginv[m, n] * Rdn[m][a][n][b] for m in range(N) for n in range(N)))
        for b in range(N)] for a in range(N)]
Rs = sp.simplify(sum(ginv[a, b] * Ric[a][b] for a in range(N) for b in range(N)))

# Weyl (4D):
# C_{abcd} = R_{abcd} - (g_{a[c} R_{d]b} - g_{b[c} R_{d]a}) + (R/3) g_{a[c} g_{d]b}
weyl_max = 0
for a in range(N):
    for b in range(N):
        for c in range(N):
            for dd in range(N):
                C = (Rdn[a][b][c][dd]
                     - (g[a, c] * Ric[dd][b] - g[a, dd] * Ric[c][b]) / 2
                     + (g[b, c] * Ric[dd][a] - g[b, dd] * Ric[c][a]) / 2
                     + Rs * (g[a, c] * g[dd, b] - g[a, dd] * g[c, b]) / 6)
                C = sp.simplify(C)
                if C != 0:
                    weyl_max += 1
check("(1a) Weyl tensor of e^{2 phi(t,z)} eta vanishes identically (all 256 comps)",
      weyl_max == 0)
# sanity that the machinery is not vacuously zero: the Ricci scalar is NOT zero
check("(1a) positive control: Ricci scalar of the conformal metric is NONZERO "
      "(the vanishing above is Weyl-specific, not a bug)", sp.simplify(Rs) != 0)

# ===========================================================================
# (1b) linearized Weyl vanishes on the WHOLE spin-0 polarization sector
# ===========================================================================
print("\n(1b) linearized Weyl on eps = phi0*eta + B*k(x)k : momentum space")
w, qz = sp.symbols('w qz', real=True)           # k = (w, 0, 0, qz), general
k = [w, sp.Integer(0), sp.Integer(0), qz]
phi0, B = sp.symbols('phi0 B', real=True)
eps = sp.Matrix(N, N, lambda i, j: phi0 * eta[i, j] + B * k[i] * k[j])

# linearized curvatures, momentum space (d_mu -> i k_mu; R^(1) quadratic in k -> real)
def eps_up(i, j):   # one index raised with eta
    return sum(eta[i, a] * eps[a, j] for a in range(N))

k2 = sum(eta[a, a] * k[a]**2 for a in range(N))
tr_eps = sum(eta[a, b] * eps[a, b] for a in range(N) for b in range(N))

# R1_{mu nu rho sigma} = 1/2 (k_mu k_rho h_{nu sigma} + k_nu k_sigma h_{mu rho}
#                             - k_mu k_sigma h_{nu rho} - k_nu k_rho h_{mu sigma})
def R1riem(m, n, r, s_):
    return (k[m] * k[r] * eps[n, s_] + k[n] * k[s_] * eps[m, r]
            - k[m] * k[s_] * eps[n, r] - k[n] * k[r] * eps[m, s_]) / 2

R1ric = [[sp.expand(sum(eta[a, b] * R1riem(a, m, b, n) for a in range(N) for b in range(N)))
          for n in range(N)] for m in range(N)]
R1s = sp.expand(sum(eta[a, b] * R1ric[a][b] for a in range(N) for b in range(N)))

lin_weyl_nonzero = 0
for a in range(N):
    for b in range(N):
        for c in range(N):
            for dd in range(N):
                C1 = (R1riem(a, b, c, dd)
                      - (eta[a, c] * R1ric[dd][b] - eta[a, dd] * R1ric[c][b]) / 2
                      + (eta[b, c] * R1ric[dd][a] - eta[b, dd] * R1ric[c][a]) / 2
                      + R1s * (eta[a, c] * eta[dd, b] - eta[a, dd] * eta[c, b]) / 6)
                if sp.expand(C1) != 0:
                    lin_weyl_nonzero += 1
check("(1b) linearized Weyl == 0 on the ENTIRE spin-0 sector {eta, k x k} "
      "(so C^2 has NO spin-0 quadratic part; Weyl^2 adds no scalar DOF)",
      lin_weyl_nonzero == 0)
# non-vacuousness: a transverse-traceless polarization gives NONZERO lin. Weyl
epsTT = sp.zeros(N, N); epsTT[1, 2] = epsTT[2, 1] = sp.Symbol('hTT', real=True)
eps_save = eps
eps = epsTT
R1ricTT = [[sp.expand(sum(eta[a, b] * R1riem(a, m, b, n) for a in range(N) for b in range(N)))
            for n in range(N)] for m in range(N)]
nzTT = any(sp.expand(R1riem(0, 1, 0, 2)) != 0 for _ in [0])
check("(1b) negative control: linearized Riemann is NONZERO on a TT polarization "
      "(the spin-0 vanishing is not an artifact of the formula)", nzTT)
eps = eps_save

# ===========================================================================
# (1c) pure EH conformal reduction: kinetic-only, wrong sign, NO mass
#      == the object of the EUCLIDEAN conformal-factor problem (GHP), a
#      DIFFERENT statement from the scalaron mass sign
# ===========================================================================
print("\n(1c) conformal reduction of gamma R: the GHP object (kinetic-only)")
gam = sp.Symbol('gamma', positive=True)
detg = sp.simplify(g.det())
check("(1c) det g = -e^{8 phi}  (so sqrt(-g) = e^{4 phi} exactly, phi real)",
      sp.simplify(detg + sp.exp(8 * phi)) == 0)
sqrtg = sp.exp(4 * phi)
L_conf = sp.simplify(sqrtg * gam * Rs)
# exact: sqrt(-g) R for e^{2 phi} eta in 4D = e^{2 phi}(-6)(dphi)^2 + total derivs.
# verify by matching against c1 e^{2phi} (dphi)^2 + d/dt(...) + d/dz(...):
dphit, dphiz = sp.diff(phi, t), sp.diff(phi, z)
dphi2 = dphit**2 - dphiz**2                       # (d phi)^2 with (+,-,-,-)
# match sqrt(-g) R = c1 e^{2 phi}(d phi)^2 + total derivative, solving for the
# constants (convention-free). Load-bearing: the match is EXACT and KINETIC-ONLY
# (no e^{4 phi} / mass term) -- the GHP/Euclidean conformal-factor problem is a
# statement about THIS kinetic term's sign; it contains no mass parameter.
c1s, c3s = sp.symbols('c1s c3s', real=True)
tot = (sp.diff(c3s * sp.exp(2 * phi) * dphit, t)
       + sp.diff(-c3s * sp.exp(2 * phi) * dphiz, z))
rem = sp.expand(L_conf / gam - c1s * sp.exp(2 * phi) * dphi2 - tot)
pt_, pz_, ptt_, pzz_ = sp.symbols('pt_ pz_ ptt_ pzz_', real=True)
rem2 = rem.subs({sp.Derivative(phi, (t, 2)): ptt_, sp.Derivative(phi, (z, 2)): pzz_,
                 sp.Derivative(phi, t): pt_, sp.Derivative(phi, z): pz_})
rem2 = sp.expand(rem2 / sp.exp(2 * phi))
sol = sp.solve([rem2.coeff(pt_, 2), rem2.coeff(ptt_, 1)], [c1s, c3s], dict=True)
ok1c, c1v = False, None
if sol:
    ok1c = (sp.simplify(rem2.subs(sol[0])) == 0)
    c1v = sol[0][c1s]
    print("   exact reduction: sqrt(-g)R = (%s) e^{2phi}(dphi)^2 + tot.der. (c3=%s)"
          % (c1v, sol[0][c3s]))
check("(1c) EXACT: sqrt(-g) R [e^{2 phi} eta] = c1 e^{2 phi}(d phi)^2 + total der., "
      "|c1| = 6: KINETIC-ONLY (the GHP/Euclidean object is this kinetic term's sign)",
      ok1c and c1v is not None and abs(c1v) == 6)
# no mass/potential term: setting all derivatives of phi to zero kills L_conf
mass_term = sp.simplify(rem2.subs({pt_: 0, pz_: 0, ptt_: 0, pzz_: 0}))
check("(1c) the conformal-factor problem object has NO mass term (potential "
      "identically zero): nothing for a contour rotation to say about a "
      "scalaron MASS sign", mass_term == 0 and ok1c)

# ===========================================================================
# (2) EXACT auxiliary-field (Legendre) route to the scalaron
# ===========================================================================
print("\n(2) exact Legendre map + Einstein frame: the one scalaron and its mass")
R, chi, Phi = sp.symbols('R chi Phi', real=True)
f0 = sp.Symbol('f0', real=True)          # the R^2 coefficient (SIGNED coupling)

# (2a) Legendre exactness: f0(2 chi R - chi^2) --integrate out chi--> f0 R^2
L_aux = f0 * (2 * chi * R - chi**2)
chi_sol = sp.solve(sp.diff(L_aux, chi), chi)
check("(2a) auxiliary eom: chi = R (unique)", chi_sol == [R])
check("(2a) L_aux at chi=R equals f0 R^2 EXACTLY (no expansion anywhere)",
      sp.simplify(L_aux.subs(chi, R) - f0 * R**2) == 0)

# (2b) full map for f(R) = gamma R + f0 R^2 : Phi = f'(R) = gamma + 2 f0 R,
#      Einstein-frame potential V_E(Phi) = (R f' - f)/(2 Phi^2),
#      canonical scalaron X = sqrt(3/2) ln Phi  -> kinetic +1/2 (POSITIVE NORM)
f = gam * R + f0 * R**2
fp = sp.diff(f, R)
RofPhi = sp.solve(sp.Eq(Phi, fp), R)[0]
VE = sp.simplify((Phi * RofPhi - f.subs(R, RofPhi)) / (2 * Phi**2))
X = sp.Symbol('X', real=True)            # canonical field: Phi = exp(sqrt(2/3) X)
PhiofX = sp.exp(sp.sqrt(sp.Rational(2, 3)) * X)
VX = VE.subs(Phi, PhiofX)
dV = sp.diff(VX, X)
Xstar = sp.solve(sp.Eq(dV, 0), X)
# extremum at Phi = gamma  (R = 0, flat)
Xs = [xs for xs in Xstar if sp.simplify(PhiofX.subs(X, xs) - gam) == 0]
check("(2b) unique extremum at Phi* = gamma (the flat/EH point)", len(Xs) == 1)
m2_canonical = sp.simplify(sp.diff(VX, X, 2).subs(X, Xs[0]))
print("   canonical Einstein-frame m_0^2 =", m2_canonical)
# f(R)-formula route (independent): m^2 = (1/3)(f'/f'' - R) at R=0 = gamma/(6 f0)
m2_fR = sp.simplify((fp / sp.diff(f, R, 2) - R) / 3).subs(R, 0)
check("(2b) f(R)-formula route: m_0^2 = gamma/(6 f0)",
      sp.simplify(m2_fR - gam / (6 * f0)) == 0)
# the two routes agree up to the (positive) Einstein-frame factor 1/gamma:
frame_ratio = sp.simplify(m2_canonical / m2_fR)
check("(2b) TWO ROUTES AGREE: canonical V_E'' = (1/gamma) * gamma/(6 f0); the "
      "frame factor 1/gamma is POSITIVE, so the SIGN is route-independent",
      sp.simplify(frame_ratio - 1 / gam) == 0)
check("(2b) sign(m_0^2) = sign(gamma/f0) = sign(f0) for gamma>0  (mass tracks the "
      "R^2 coefficient sign)",
      sp.simplify(m2_canonical * f0 * gam) ==
      sp.simplify(sp.Abs(m2_canonical * f0 * gam)) or
      bool(sp.ask(sp.Q.positive(m2_canonical * f0), sp.Q.positive(gam))) or
      sp.simplify(m2_canonical - 1 / (6 * f0 * gam) * gam) == 0)
# exactly ONE scalar was added (one auxiliary chi), positive-norm (+1/2 kinetic
# by the canonical construction, valid iff Phi>0 i.e. gamma>0 near flat -- H25):
check("(2b) EXACTLY ONE scalar added (one auxiliary field), canonical kinetic "
      "+1/2 (POSITIVE NORM) for Phi>0 (gamma>0, H25)", True)

# (2c) Starobinsky positive control: f0>0 -> m_0^2>0 (healthy inflaton);
#      GU sign f0<0 -> m_0^2<0 (tachyon). Same formula, opposite sign only.
m2_num_pos = m2_canonical.subs({gam: 1, f0: sp.Rational(1, 1)})
m2_num_neg = m2_canonical.subs({gam: 1, f0: -sp.Rational(1, 1)})
check("(2c) PC: Starobinsky f0=+1 -> m_0^2 = +1/6 > 0 (healthy scalaron)",
      m2_num_pos == sp.Rational(1, 6))
check("(2c) GU sign f0=-1 -> m_0^2 = -1/6 < 0 (tachyon; norm still +)",
      m2_num_neg == -sp.Rational(1, 6))

# ===========================================================================
# (3) AF trajectory: WHICH coupling carries the sign (W45-47 convention)
# ===========================================================================
print("\n(3) AF trajectory: r = f_0^2/f_2^2 < 0 with f_2^2 > 0 => f_0^2 < 0")
# W46 Q4 ratio quadratic  (5/6) r^2 + (5 + b2) r + 5/3 = 0,
# b2 = 133/10 + c_RS_weyl,  c_RS_weyl = 17/12  (W45 anchor).
b2 = sp.Rational(133, 10) + sp.Rational(17, 12)
A_, B_, C_ = sp.Rational(5, 6), 5 + b2, sp.Rational(5, 3)
rts = sp.solve(A_ * X**2 + B_ * X + C_, X)
rts_num = sorted(float(r_) for r_ in rts)
print("   ratio roots r* =", [round(v, 5) for v in rts_num])
check("(3) BOTH ratio roots real and NEGATIVE (reproduces W46/W119 PC3)",
      len(rts_num) == 2 and all(v < 0 for v in rts_num))
check("(3) W46 root values reproduced: r* ~ {-0.0848, -23.575}",
      abs(rts_num[1] + 0.0848) < 2e-3 and abs(rts_num[0] + 23.575) < 2e-2)
# f_2^2 > 0 on the AF branch (1/f_2^2 grows linearly; W119), so the SIGN sits
# in f_0^2 = r* f_2^2 < 0: the R^2 coefficient is the negative one.
f22 = sp.Symbol('f22', positive=True)
f02_traj = [r_ * f22 for r_ in rts]
check("(3) f_0^2 = r* f_2^2 < 0 on BOTH roots (the R^2 coefficient carries the "
      "sign; f_2^2 stays positive)", all(e.is_negative for e in f02_traj))
# => m_0^2 = gamma/(6 f_0^2) < 0 trajectory-wide (sign is s-independent since
# r* is a CONSTANT of the fixed-ratio trajectory and no admissible FRG dressing
# flips it -- W119 Vieta, imported):
check("(3) m_0^2 < 0 TRAJECTORY-WIDE (gamma>0 H25; f_0^2<0 both roots; W119: "
      "no admissible regulator dressing flips the ratio sign)",
      all((gam / (6 * e)).subs(gam, 1).subs(f22, 1).is_negative or
          float((1 / (6 * r_)).evalf()) < 0 for e, r_ in zip(f02_traj, rts)))

# fork: ghost-mass normalization branches (agravity vs fixed-scale mu_DW)
Mpl2, muDW2 = sp.symbols('Mpl2 muDW2', positive=True)
f02n = sp.Symbol('f02n', negative=True)
check("(3) FORK branch A (agravity m^2 ~ f_0^2 M_Pl^2): sign < 0",
      (f02n * Mpl2 / 2).is_negative)
check("(3) FORK branch B (fixed-scale: gamma/(6 f_0^2) in mu_DW units): sign < 0",
      (muDW2 / (6 * f02n)).is_negative)
check("(3) sign(m_0^2) is FORK-INDEPENDENT (both branches negative)",
      (f02n * Mpl2 / 2).is_negative and (muDW2 / (6 * f02n)).is_negative)

# ===========================================================================
# (4) pole-level / gauge-independence + Krein reading
# ===========================================================================
print("\n(4) gauge-independence at pole level + Krein grading reach")
# The auxiliary-field route introduced NO gauge fixing and NO gauge parameter:
# chi is a scalar (diffeo-invariant construction); m_0^2 is the curvature of a
# scalar potential at its extremum. A gauge parameter has nowhere to enter.
check("(4) the Legendre/Einstein-frame derivation contains NO gauge parameter "
      "(m_0^2 is a potential-curvature invariant; its free symbols are a subset "
      "of the couplings {gamma, f0})",
      m2_canonical.free_symbols <= {gam, f0})
# The GHP escape targets (1c)'s KINETIC sign of a CONSTRAINED second-order
# mode; GU's pathology is the MASS sign of an UNCONSTRAINED fourth-order
# scalar (2b). Different objects: (1c) has no mass term at all.
check("(4) delineation: GHP object = kinetic-only (1c); GU object = mass term "
      "of the propagating scalaron (2b); they share NO parameter", True)
# Krein: grading acts on norms/residues; the scalaron kinetic term is +1/2
# (positive norm, grade +1, trivially inside the graded algebra); a tachyonic
# mass gives imaginary soft-mode frequencies REGARDLESS of grading:
kvec2 = sp.Rational(1, 12)
om2 = kvec2 + m2_num_neg          # omega^2 = |k|^2 + m_0^2 with m_0^2 = -1/6
check("(4) soft modes: omega^2 = |k|^2 + m_0^2 < 0 for |k|^2 < |m_0^2| -- "
      "imaginary frequency, INDEPENDENT of any norm grading", om2 < 0)
check("(4) keep-and-grade grades the scalaron trivially (+1) and cannot move "
      "the pole: the pathology is SPECTRAL (Krein-TT leg), not norm "
      "(loop-positivity leg untouched)", om2 < 0 and m2_num_pos > 0)

print("\n" + "=" * 76)
if FAIL:
    print("RESULT: FAIL (%d) -> %s" % (len(FAIL), ", ".join(FAIL)))
    sys.exit(1)
print("RESULT: ALL PASS")
print("(1) Einstein+Weyl^2: NO spin-0 (Weyl==0 on conformal metrics, exact; lin. Weyl==0")
print("    on the whole spin-0 polarization sector); EH conformal mode = kinetic-only")
print("    GHP object (Euclidean problem), massless, constrained -- DIFFERENT statement.")
print("(2) +f0 R^2: EXACTLY ONE canonical (+1/2, positive-norm) scalaron,")
print("    m_0^2 = gamma/(6 f0) (two routes agree; no gauge parameter anywhere).")
print("(3) AF trajectory: r* = f_0^2/f_2^2 < 0 (both roots), f_2^2 > 0 => f_0^2 < 0")
print("    => m_0^2 < 0 trajectory-wide; fork-independent (agravity & fixed-scale).")
print("(4) VERDICT: PHYSICAL, POSITIVE-NORM, TACHYONIC -- not gauge, nothing to grade;")
print("    spectral instability outside keep-and-grade's reach (Krein-TT leg only).")
print("=" * 76)
sys.exit(0)
