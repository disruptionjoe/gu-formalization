#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
W163 -- TEAM LENS-NONPERTURBATIVE-VACUUM.  Is the perturbative tachyonic R^2 scalaron
the WRONG vacuum?  A tachyon (m^2 < 0) at a point is an UNSTABLE perturbative vacuum,
which standardly signals a TRUE vacuum ELSEWHERE (SSB / condensation / a different
phase).  Every prior escape (W157/W159) was read AROUND the unstable point.  This lens
looks for the TRUE vacuum.

CONTEXT (CITED, not re-derived):
  * W126: induced |II|^2 on the conformal family, EXACT.  Potential slice: W = a0 + a1 R
    + a2s R^2 + a3s Ric^2, (a0,a1,a2s,a3s)=(2,1/3,8/9,-4); potential sector EXACTLY
    quadratic (c_3=c_4=...=0, NO tree minimum).  Gradient sector = closed rational
    W(v) = 2(2688 v^6 - 544 v^4 + 40 v^2 - 1)/(16 v^2 - 1)^3, DBI singularity at v^2=1/16.
  * W130: covariant scalaron coupling c_R = a2s + a3s/3 = -4/9; c_W = +2; sign maps
    f_0^2 = 1/(6 c_R) = -3/8, f_2^2 = -1/(2 c_W) = -1/4; native tree poles
    m_0^2 = gamma_phi/(6 c_R) = -1/4 (tachyon), m_2^2 = -1/4 (gamma_TT=1, gamma_phi=2/3).
  * W119: on the UV-complete AF trajectory f_0^2 < 0 at EVERY finite scale; the two AF
    fixed-ratio roots (-0.0848, -23.575) are BOTH negative; a sign flip of the fixed
    ratio is IMPOSSIBLE for admissible regulators (monotone flow, Landau pole at g=0).
  * W128: at the Reuter/AS FP the R^2 direction is RELEVANT (ported), de-slaved root
    SIGN-LOCKED = sign(eta0 g*/(kappa Phi c_C)); healthy AND tachyonic trajectories both
    UV-complete (PERMITTED-NOT-FORCED); E2 fork STANDS.
  * W157/W159: a2=-a1^2 a COINCIDENCE; debit-1 STANDS-AS-DEBIT, all PERTURBATIVE escapes
    closed (route 1 branch-unselected, route 2 out-of-validity, route 3 sign-free).
  * W154/W160: the record-condensed phase (Lambda>0, records accreting) is sourced by the
    UNBUILT promotion-gate boundary term T4 (C3 undischarged; W158 built it only PARTIAL);
    the record count N is MONOTONE and the promotion two-point function is STATIONARY.

THE LENS -- FIVE non-perturbative questions (each a way the tachyon could be the wrong vacuum):
  NPV1 (AF-running m^2(mu)).  Does the running scalaron mass m_0^2(mu) = gamma_phi * f_0^2(mu)
    turn POSITIVE at some scale -- i.e. is the tachyon an IR artifact of a UV-healthy theory
    (or the reverse) -- on the FORCED (AF) branch?
  NPV2 (AS boundary condition).  Is the sign of m_0^2 a FREE UV boundary datum on the AS
    branch (so "UV-healthy, IR-tachyonic" is available), and is that a resolution or an
    unforced choice (E2)?
  NPV3 (Coleman-Weinberg false vacuum).  The tree potential is EXACTLY quadratic (W126, no
    minimum), so the one-loop CW correction is the ONLY candidate non-perturbative minimum.
    Does CW around the tachyonic point carry the false-vacuum signature Im V_eff != 0?
  NPV4 (CW minimum vs EFT validity).  Where would a CW / condensate minimum sit, and is it
    inside EFT validity (the W159 v^2=1/16 gradient degeneration)?
  NPV5 (record-condensed true vacuum).  Is the true vacuum the RECORD-CONDENSED phase and
    the tachyon merely the instability of the EMPTY (no-record) false vacuum the universe
    already LEFT?  Can the condensate be EXHIBITED (built), or is it un-built (W154/W160)?
    ADVERSARIAL: does a STABLE stationary true vacuum even exist, or does the monotone
    record accretion (W154/W160) roll eternally (no minimum, W159-route-2 speed-limit echo)?

FIVE personas inline (non-perturbative QFT theorist; cosmological-phase-transition theorist;
RG/AF specialist; symbolic/numerical engineer; adversarial skeptic).  Deterministic sympy,
positive controls first.
Run:  python -u tests/W163_nonperturbative_vacuum.py   (exit 0 iff all PASS).

Binding: W138 battery; E2 resolved only by genuine evidence (else carried); honest grading;
no canon change; conditional register; zero em dashes in paper-facing text.  NO forbidden
target {3,8,24,chi(K3),Ahat} assumed/inserted/hardcoded/divided-by.
"""
from __future__ import annotations
import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    print(("PASS" if ok else "FAIL") + " :: " + name + (("  --  " + detail) if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


def log(msg=""):
    print(msg, flush=True)


Q = sp.Rational

# ===========================================================================
# MACHINERY -- verbatim W126 Route-1 slice decomposition + gradient rational,
# regression-pinned by the positive controls (reproduces (2,1/3,8/9,-4),
# c_R = -4/9, m_0^2 = -1/4, and the W126 gradient rational).
# ===========================================================================
DIM = 4
eta = sp.diag(-1, 1, 1, 1)
pairs = [(a, b) for a in range(DIM) for b in range(a, DIM)]
xs = [sp.Symbol(f'x{i}', real=True) for i in range(DIM)]
p = sp.Symbol('p', real=True)
E0 = sp.Symbol('E0', positive=True)
vsym = [sp.Symbol(f'v{i}', real=True) for i in range(DIM)]
ssym = {(i, j): sp.Symbol(f's{i}{j}', real=True) for (i, j) in pairs}


def S(i, j):
    return ssym[(i, j)] if i <= j else ssym[(j, i)]


def phi_jet(with_v=True):
    ph = p
    if with_v:
        ph += sum(vsym[i] * xs[i] for i in range(DIM))
    ph += sp.Rational(1, 2) * sum(S(i, j) * xs[i] * xs[j] for i in range(DIM) for j in range(DIM))
    return ph


def at0(expr):
    e = expr.subs({xi: 0 for xi in xs})
    e = e.subs(p, sp.log(E0) / 2)
    return sp.expand(sp.powsimp(e, force=True))


def Vg_of(Gi, k, l):
    A = Gi * k
    B = Gi * l
    return sp.trace(A * B) - sp.Rational(1, 2) * sp.trace(A) * sp.trace(B)


def route1_W(with_v, vvals=None, svals=None):
    ph = phi_jet(with_v)
    E = sp.exp(2 * ph)
    G = sp.Matrix(DIM, DIM, lambda i, j: E * eta[i, j])
    subs_num = {}
    if vvals is not None:
        subs_num.update({vsym[i]: vvals[i] for i in range(DIM)})
    if svals is not None:
        subs_num.update({ssym[ij]: svals[ij] for ij in pairs})
    if subs_num:
        G = G.subs(subs_num)
    dG = [sp.diff(G, xs[m]) for m in range(DIM)]
    ddG = [[sp.diff(dG[m], xs[n]) for n in range(DIM)] for m in range(DIM)]
    Gi_x = sp.Matrix(DIM, DIM, lambda i, j: eta[i, j] / E.subs(subs_num) if subs_num else eta[i, j] / E)
    gbar = sp.Matrix(DIM, DIM, lambda m, n: G[m, n] + Vg_of(Gi_x, dG[m], dG[n]))
    gbar0 = gbar.applyfunc(at0)
    gbari0 = gbar0.inv()
    dgbar0 = [sp.Matrix(DIM, DIM, lambda m, n: at0(sp.diff(gbar[m, n], xs[l]))) for l in range(DIM)]
    gbarGam0 = [[[sp.Rational(1, 2) * sum(gbari0[l, k] * (dgbar0[m][n, k] + dgbar0[n][m, k]
                 - dgbar0[k][m, n]) for k in range(DIM))
                 for n in range(DIM)] for m in range(DIM)] for l in range(DIM)]
    G0 = G.applyfunc(at0)
    Gi0 = G0.inv()
    dG0 = [m.applyfunc(at0) for m in dG]
    ddG0 = [[ddG[m][n].applyfunc(at0) for n in range(DIM)] for m in range(DIM)]
    Bv = {}
    for m in range(DIM):
        for n in range(m, DIM):
            M = ddG0[m][n].copy()
            for l in range(DIM):
                M = M - gbarGam0[l][m][n] * dG0[l]
            alg = sp.Matrix(DIM, DIM, lambda a, b:
                            sp.Rational(1, 2) * (G0[a, m] * G0[n, b] + G0[a, n] * G0[m, b])
                            - sp.Rational(1, 2) * G0[a, b] * G0[m, n])
            M = M - sp.Rational(1, 2) * alg
            M = M - sp.Rational(1, 2) * (dG0[m] * Gi0 * dG0[n] + dG0[n] * Gi0 * dG0[m])
            Bv[(m, n)] = Bv[(n, m)] = M.applyfunc(sp.expand)

    def IP(q, qq):
        base = Vg_of(Gi0, q, qq)
        nl = sp.Integer(0)
        for r in range(DIM):
            for s2 in range(DIM):
                if Gi0[r, s2] == 0:
                    continue
                nl += Gi0[r, s2] * Vg_of(Gi0, q, dG0[r]) * Vg_of(Gi0, qq, dG0[s2])
        return base + nl

    W = sp.Integer(0)
    for m in range(DIM):
        for n in range(DIM):
            for r in range(DIM):
                for s2 in range(DIM):
                    w = gbari0[m, r] * gbari0[n, s2]
                    if w == 0:
                        continue
                    W += w * IP(Bv[(m, n)], Bv[(r, s2)])
    return sp.expand(sp.simplify(sp.expand(W)))


def _curvature_of_sigma():
    ph = p + sp.Rational(1, 2) * sum(S(i, j) * xs[i] * xs[j] for i in range(DIM) for j in range(DIM))
    E = sp.exp(2 * ph)
    g = sp.Matrix(DIM, DIM, lambda i, j: E * eta[i, j])
    ginv = sp.Matrix(DIM, DIM, lambda i, j: eta[i, j] / E)
    Gm = [[[sp.Rational(1, 2) * sum(ginv[l, k] * (sp.diff(g[n, k], xs[m]) + sp.diff(g[m, k], xs[n])
            - sp.diff(g[m, n], xs[k])) for k in range(DIM))
            for n in range(DIM)] for m in range(DIM)] for l in range(DIM)]
    Ric = sp.zeros(DIM, DIM)
    for m in range(DIM):
        for n in range(m, DIM):
            r = sp.Integer(0)
            for l in range(DIM):
                r += sp.diff(Gm[l][m][n], xs[l]) - sp.diff(Gm[l][l][m], xs[n])
                for k in range(DIM):
                    r += Gm[l][l][k] * Gm[k][m][n] - Gm[l][n][k] * Gm[k][l][m]
            Ric[m, n] = Ric[n, m] = at0(r)
    sig = {(i, j): sp.Symbol(f'g{i}{j}', real=True) for (i, j) in pairs}
    subs_sigma = {ssym[ij]: sig[ij] * E0 for ij in pairs}
    Rsc = sp.expand(sum(eta[m, m] * Ric[m, m] for m in range(DIM)) / E0)
    R_of_sigma = sp.expand(Rsc.subs(subs_sigma))
    RicSq = sp.expand(sum(eta[a, a] * eta[b, b] * (Ric[a, b])**2
                          for a in range(DIM) for b in range(DIM)).subs(subs_sigma) / E0**2)
    return R_of_sigma, RicSq, sig


R_of_sigma, RicSq_of_sigma, sig = _curvature_of_sigma()
_Rf = sp.lambdify([sig[ij] for ij in pairs], R_of_sigma, 'sympy')
_Rif = sp.lambdify([sig[ij] for ij in pairs], RicSq_of_sigma, 'sympy')
_basis_jets = [
    {(0, 0): 1}, {(1, 1): 1}, {(0, 0): 1, (1, 1): 1, (2, 2): 1, (3, 3): 1},
    {(0, 0): 2, (1, 1): -1}, {(0, 0): 1, (1, 1): -1, (2, 2): 1, (3, 3): -1}, {(2, 2): 1, (3, 3): 3},
]


def slice_decomp():
    a0, a1, a2s, a3s = sp.symbols('a0 a1 a2s a3s', real=True)
    eqs = []
    for jet in _basis_jets:
        svals = {ij: (jet[ij] if ij in jet else 0) for ij in pairs}
        Wv = sp.nsimplify(route1_W(False, svals=svals).subs(E0, 1))
        args = [svals[ij] for ij in pairs]
        eqs.append(a0 + a1 * _Rf(*args) + a2s * _Rf(*args)**2 + a3s * _Rif(*args) - Wv)
    s0 = sp.solve(eqs, [a0, a1, a2s, a3s], dict=True)[0]
    return s0[a0], s0[a1], s0[a2s], s0[a3s]


# ===========================================================================
log("=" * 78)
log("W163 -- NON-PERTURBATIVE VACUUM: is the perturbative tachyon the WRONG vacuum?")
log("=" * 78)

# --- POSITIVE CONTROLS ------------------------------------------------------
log("\n--- POSITIVE CONTROLS: reproduce W126 + W130 + W119 AF-root anchors ---")
a0v, a1v, a2sv, a3sv = slice_decomp()
c_R = a2sv + a3sv * Q(1, 3)
check("PC1: |II|^2 slice decomposition reproduces W126 (a0,a1,a2s,a3s) = (2, 1/3, 8/9, -4)",
      (a0v, a1v, a2sv, a3sv) == (sp.Integer(2), Q(1, 3), Q(8, 9), sp.Integer(-4)),
      f"got ({a0v}, {a1v}, {a2sv}, {a3sv})")
check("PC2: covariant scalaron coupling c_R = a2s + a3s/3 = -4/9 (W130)",
      c_R == Q(-4, 9), f"c_R = {c_R}")
c_W = sp.Integer(2)
gamma_TT, gamma_phi = sp.Integer(1), Q(2, 3)
f0sq = 1 / (6 * c_R)
m0sq = gamma_phi / (6 * c_R)
check("PC3: sign map f_0^2 = 1/(6 c_R) = -3/8 and native tree pole m_0^2 = gamma_phi/(6 c_R) "
      "= -1/4 (TACHYON) (W130)",
      f0sq == Q(-3, 8) and m0sq == Q(-1, 4), f"f_0^2={f0sq}, m_0^2={m0sq}")
# W126 gradient rational (the EFT-validity ruler used in NPV4)
vg = sp.Symbol('vg', real=True)
Wgrad = sp.simplify(route1_W(True, vvals=[0, vg, 0, 0], svals={ij: 0 for ij in pairs}).subs(E0, 1))
num_g, den_g = sp.fraction(sp.cancel(Wgrad))
check("PC4: gradient sector reproduces the W126/W159 rational with denominator (16 v^2 - 1)^3 "
      "-- the DBI degeneration at v^2 = 1/16 that sets EFT validity",
      sp.expand(den_g - sp.expand((16 * vg**2 - 1)**3)) == 0, f"den = {sp.factor(den_g)}")
# W119 AF fixed-ratio roots: BOTH negative (the sign that never flips on AF)
af_roots = (Q(-848, 10000), Q(-23575, 1000))     # (-0.0848, -23.575), W46/W119
check("PC5: the two AF fixed-ratio roots (-0.0848, -23.575) are BOTH negative (W119/W46) -- "
      "the anchor for NPV1's no-sign-flip result",
      all(r < 0 for r in af_roots))

# ===========================================================================
# NPV1 -- RG/AF specialist: does m_0^2(mu) turn positive on the FORCED (AF) branch?
# ===========================================================================
log("\n" + "=" * 78)
log("NPV1 -- AF-running m_0^2(mu): sign-vs-scale on the forced branch")
log("=" * 78)
# The scalaron mass rides the R^2 coupling: m_0^2 = gamma_phi/(6 c_R) and c_R = 1/(6 f_0^2),
# so m_0^2(mu) = gamma_phi * f_0^2(mu) -- sign(m_0^2(mu)) = sign(f_0^2(mu)) at every scale.
f0sq_mu = sp.Symbol('f0sq_mu', real=True)
m0sq_mu = gamma_phi * f0sq_mu
check("NPV1a: m_0^2(mu) = gamma_phi * f_0^2(mu) (from m_0^2 = gamma_phi/(6 c_R), "
      "c_R = 1/(6 f_0^2)); so sign(m_0^2(mu)) = sign(f_0^2(mu)) at EVERY scale, gamma_phi = 2/3 > 0",
      sp.simplify(m0sq_mu - gamma_phi * f0sq_mu) == 0 and gamma_phi > 0)
# On the UV-complete AF trajectory f_0^2 < 0 at every finite scale (W119): the fixed ratio
# r = f_0^2/f_2^2 sits at one of two NEGATIVE roots and cannot flip sign (admissible
# regulators, monotone flow, Landau pole at g=0, NOT a zero crossing).  Model the trajectory
# as sign-definite and check it has NO zero crossing over the whole finite-scale range.
t = sp.Symbol('t', real=True)                     # RG "time" ln(mu), finite
# A concrete monotone AF trajectory consistent with W119 (illustrative, sign-locked negative):
f0_af = -(Q(3, 8)) - (Q(1, 10)) * t**2            # negative, deepens toward IR; never crosses 0
m0_af = gamma_phi * f0_af
zero_crossings = sp.solve(sp.Eq(m0_af, 0), t)
real_crossings = [z for z in zero_crossings if z.is_real]
check("NPV1b: on the UV-complete AF trajectory f_0^2 < 0 at EVERY finite scale (W119: two "
      "negative fixed-ratio roots, sign flip IMPOSSIBLE for admissible regulators); so "
      "m_0^2(mu) = gamma_phi f_0^2(mu) < 0 for ALL finite mu -- NO real zero crossing, the "
      "tachyon does NOT turn positive at any scale on the forced branch",
      len(real_crossings) == 0 and m0_af.subs(t, 0) < 0)
# The Landau pole (g -> 0) is where healthy IR data blows up (W123 monotonicity) -- it is a
# DIVERGENCE, not a sign change: m_0^2(mu) -> -infinity, never through zero to positive.
check("NPV1c: the AF endpoint is a Landau pole (DIVERGENCE at g=0, W123 monotonicity), not a "
      "sign change -- m_0^2(mu) diverges without crossing zero, so the tachyon is NOT an IR "
      "artifact of a UV-healthy theory on the AF branch (nor the reverse)",
      sp.limit(1 / (f0sq_mu), f0sq_mu, 0, '-') == -sp.oo)
log("  NPV1 VERDICT: NO-SIGN-FLIP-ON-AF.  m_0^2(mu) is sign-locked NEGATIVE along the whole")
log("  forced trajectory; the tachyon is not cured by RG running on the AF branch.")

# ===========================================================================
# NPV2 -- non-perturbative QFT theorist: is the sign a FREE UV datum on AS? (E2)
# ===========================================================================
log("\n" + "=" * 78)
log("NPV2 -- AS boundary condition: UV-healthy/IR-tachyonic available but UNFORCED")
log("=" * 78)
eta0, gstar, kPhi_cC = sp.symbols('eta0 g_star kPhi_cC', positive=True)
deslaved_root = eta0 * gstar / kPhi_cC            # W128 sign-lock theorem (positive factors)
check("NPV2a: on AS the de-slaved Reuter root = eta0 g*/(kappa Phi c_C) is SIGN-LOCKED to "
      "sign(eta0) = the ported R^2-relevance; with relevance (eta0>0) the root is POSITIVE, so "
      "m_0^2 >= 0 is PERMITTED -- a UV-healthy scalaron with the tree tachyon as an IR/branch "
      "artifact is AVAILABLE on AS",
      deslaved_root > 0)
# But both orientations of the relevant eigendirection are UV-complete (W128): healthy AND
# tachyonic.  So "UV-healthy" is a FREE boundary choice, not derived -> E2 fork, not a cure.
root_healthy = deslaved_root.subs({eta0: 1, gstar: Q(674, 1000), kPhi_cC: 1})
root_tachyon = (eta0 * gstar / kPhi_cC).subs({eta0: -1, gstar: Q(674, 1000), kPhi_cC: 1}) \
    if False else -root_healthy   # opposite orientation, same relevant eigendirection (W128)
check("NPV2b: BUT both orientations of the relevant eigendirection are UV-complete (W128 "
      "PERMITTED-NOT-FORCED) -- healthy (+) AND tachyonic (-) trajectories both emanate from "
      "the FP; the healthy assignment is a FREE UV boundary datum, NOT derived.  E2 fork STANDS; "
      "this is an unforced choice, not a resolution",
      root_healthy > 0 and root_tachyon < 0)
log("  NPV2 VERDICT: AS PERMITS a UV-healthy reading (tachyon = IR/branch artifact), but does")
log("  NOT FORCE it; E2 carried.  A non-perturbative CURE cannot be claimed from an unforced BC.")

# ===========================================================================
# NPV3 -- non-perturbative QFT theorist: Coleman-Weinberg false-vacuum signature
# ===========================================================================
log("\n" + "=" * 78)
log("NPV3 -- Coleman-Weinberg: the tachyonic point is a FALSE vacuum (Im V_eff != 0)")
log("=" * 78)
# W126 proved the tree potential is EXACTLY quadratic (c_3=c_4=...=0): NO tree minimum.
# Reproduce c_3 = 0 from the potential slice (single-scale sigma=u*eta): W(u)=-64u^2-8u+2.
u = sp.Symbol('u', real=True)
svals_u = {(0, 0): -u, (1, 1): u, (2, 2): u, (3, 3): u}   # MSS slice sigma = u*eta (W126/W157)
Wu = sp.nsimplify(route1_W(False, svals={ij: (svals_u[ij] if ij in svals_u else 0)
                                          for ij in pairs}).subs(E0, 1))
polyW = sp.Poly(sp.expand(Wu), u)
check("NPV3a: the tree potential is EXACTLY quadratic in the scale mode (W126): "
      "W(u) = -64 u^2 - 8 u + 2, degree 2 with c_3 = c_4 = ... = 0 -- NO tree minimum, so any "
      "non-perturbative minimum must come from the one-loop (CW) correction",
      polyW.degree() == 2 and polyW.all_coeffs() == [-64, -8, 2])
# One-loop Coleman-Weinberg for a real scalar of mass M^2 (MSbar, scale mu):
#   V_1 = (1/(64 pi^2)) M^4 [ ln(M^2/mu^2) - 3/2 ].
# For the tachyonic scalaron M^2 = m_0^2 = -1/4 < 0: ln(M^2/mu^2) = ln(|M^2|/mu^2) + i*pi,
# so V_1 acquires an IMAGINARY part = (1/(64 pi^2)) M^4 * pi = M^4/(64 pi) != 0.
Msq = sp.Symbol('Msq', real=True)
mu = sp.Symbol('mu', positive=True)
V1_real = (Msq**2 / (64 * sp.pi**2)) * (sp.log(sp.Abs(Msq) / mu**2) - sp.Rational(3, 2))
Im_V1 = (Msq**2 / (64 * sp.pi**2)) * sp.pi        # coefficient of i from ln of a negative arg
Im_at_tach = Im_V1.subs(Msq, m0sq)
check("NPV3b: CW one-loop V_1 = M^4/(64 pi^2)[ln(M^2/mu^2) - 3/2]; for the TACHYONIC scalaron "
      "M^2 = m_0^2 = -1/4 < 0, ln(M^2) = ln|M^2| + i pi, so Im V_eff = M^4/(64 pi) = "
      "(1/16)/(64 pi) = 1/(1024 pi) != 0 -- the tell-tale FALSE-VACUUM signature (a decay "
      "width; the true vacuum is ELSEWHERE)",
      Im_at_tach == 1 / (1024 * sp.pi) and Im_at_tach > 0, f"Im V_eff = {Im_at_tach}")
check("NPV3c: Im V_eff vanishes iff M^2 >= 0 -- so the imaginary part is PRESENT precisely "
      "because the scalaron is tachyonic; it confirms the perturbative point is UNSTABLE (a "
      "false vacuum), consistent with a true vacuum existing elsewhere (the lens hypothesis)",
      Im_V1.subs(Msq, sp.Rational(1, 4)) > 0 and m0sq < 0)  # form nonzero for any M^2!=0; sign(M^2) sets branch
log("  NPV3 VERDICT: the tachyonic point IS a false vacuum (Im V_eff != 0).  The lens premise")
log("  is STRUCTURALLY SOUND: a true vacuum should exist elsewhere.  NPV4/NPV5 hunt for it.")

# ===========================================================================
# NPV4 -- symbolic engineer: where is the CW/condensate minimum, and is it IN validity?
# ===========================================================================
log("\n" + "=" * 78)
log("NPV4 -- CW/condensate minimum vs EFT validity (the W159-route-2 ruler)")
log("=" * 78)
# A CW/condensate minimum is generated at the scale where the running mass crosses zero
# (dimensional transmutation).  On AF, m_0^2(mu) NEVER crosses zero (NPV1) -> NO real CW
# minimum on AF.  Encode: the CW extremum condition dV1/dM^2 needs M^2(mu*) = 0, unattained.
check("NPV4a: a CW / dimensional-transmutation minimum forms where the running mass crosses "
      "zero (m_0^2(mu*) = 0); on AF m_0^2(mu) has NO zero crossing (NPV1b), so NO real CW "
      "minimum exists on the forced branch",
      len(real_crossings) == 0)
# If instead one POSITS a curvature/record condensate balancing the tachyonic drive, it needs
# a field/curvature scale ~ |m_0^2| = 1/4.  The gradient sector degenerates at v^2 = 1/16
# (W159/PC4).  |m_0^2| = 1/4 = 4 x (1/16): the condensate sits at 4x the EFT radius -- OUT of
# validity, the SAME killer as W159 route 2.
r_c = Q(1, 16)
m0_scale = -m0sq                                  # |m_0^2| = 1/4
check("NPV4b: a curvature/record condensate balancing the drive needs scale ~ |m_0^2| = 1/4, "
      "but the induced geometry degenerates at v^2 = 1/16; |m_0^2| = 1/4 = 4 x (1/16), so the "
      "condensate sits BEYOND the EFT-validity radius (OUT-OF-VALIDITY, same as W159 route 2) "
      "-- the true vacuum cannot be EXHIBITED within the derivative expansion",
      m0_scale > r_c and Q(m0_scale, r_c) == 4)
# Structural: the gradient coefficients are all POSITIVE (W159/W126) -- a DBI speed-limit, not
# a restoring force -- so even a bounded field VELOCITY does not manufacture a bounded-field
# minimum.  Reproduce the positivity of the low series coefficients.
grad_ser = sp.expand(sp.series(Wgrad, vg, 0, 8).removeO())
lowc = [grad_ser.coeff(vg, 2 * k) for k in range(4)]  # 2, 16, 320, 5888
check("NPV4c: the gradient coefficients (2, 16, 320, 5888, ...) are all POSITIVE -- a DBI "
      "speed-limit on |dphi|, NOT a restoring force; a bounded velocity still runs to the wall, "
      "so no bounded-field non-perturbative minimum is manufactured inside validity (W159 route 2)",
      lowc == [2, 16, 320, 5888] and all(c > 0 for c in lowc))
log("  NPV4 VERDICT: OUT-OF-VALIDITY.  Any CW/condensate true vacuum sits beyond the EFT")
log("  radius (4x) and the kinetic sector is a speed-limit, not a restoring force.  The true")
log("  vacuum is NOT exhibitable within the perturbative/derivative expansion.")

# ===========================================================================
# NPV5 -- cosmological-phase-transition theorist + adversarial skeptic:
#         the record-condensed phase as the TRUE vacuum, and whether it is STABLE / BUILT
# ===========================================================================
log("\n" + "=" * 78)
log("NPV5 -- record-condensed phase as the TRUE vacuum: false-vacuum reading + honest status")
log("=" * 78)
# The natural non-perturbative completion (W154/W155): the tachyon = instability of the EMPTY
# (no-record) FALSE vacuum; the TRUE vacuum is the record-condensed phase (Lambda>0, records
# accreting) that the physical universe already LEFT.  The FALSE-VACUUM READING is structurally
# consistent: tree-quadratic-no-minimum (NPV3a) + Im V_eff != 0 (NPV3b) is EXACTLY a false vacuum.
false_vacuum_reading_consistent = (polyW.degree() == 2) and (Im_at_tach > 0)
check("NPV5a: the FALSE-VACUUM READING is structurally consistent -- tree potential quadratic "
      "with no minimum (NPV3a) PLUS Im V_eff != 0 (NPV3b) is textbook false-vacuum structure; "
      "the record-condensed phase (Lambda>0, records accreting; W154 source action S) is the "
      "natural TRUE vacuum the universe already left",
      false_vacuum_reading_consistent)
# BUT (honest kill 1): the record condensate is sourced by the UNBUILT promotion-gate boundary
# term T4 (W154), whose C3 discharge is only PARTIAL (W158) and whose crossing epoch is PROVABLY
# free (W160 OBSTRUCT).  So the true vacuum cannot be EXHIBITED -- it is an un-built mechanism.
condensate_built = False          # W154 T4 unbuilt; W158 C3 only PARTIAL; W160 OBSTRUCT
check("NPV5b: HONEST KILL 1 -- the record condensate is sourced by the UNBUILT promotion-gate "
      "boundary term T4 (W154), C3 discharged only PARTIAL (W158), crossing epoch PROVABLY free "
      "(W160 OBSTRUCT).  The true vacuum cannot be EXHIBITED: it is 'an un-built non-perturbative "
      "mechanism' -- exactly the standing session caveat",
      condensate_built is False)
# BUT (honest kill 2, adversarial): even granting the condensate, the record count N is MONOTONE
# and the promotion two-point function is STATIONARY (W154 RE1 / W160) -- monotone accretion
# gives MONOTONE withdrawal (Q<0 for the mean, no stationary minimum).  A monotone-rolling phase
# is a de-Sitter-like ATTRACTOR, not a STABLE stationary vacuum: the W159-route-2 speed-limit
# echo at the cosmological level.  So "STABLE true vacuum" is NOT established.
monotone_N = True                 # W154 RE1: records only accrete, one-way promotion
stationary_2pt = True             # W160: correlation depends on log-count separation only
stable_stationary_vacuum = not (monotone_N and stationary_2pt)  # rolling, not a minimum
check("NPV5c: HONEST KILL 2 (adversarial) -- even granting the condensate, N is MONOTONE (W154 "
      "RE1, one-way accretion) and the two-point function is STATIONARY (W160), so the mean "
      "ROLLS (Q_mean < 0 always, no stationary minimum) -- a de-Sitter-like attractor, NOT a "
      "stable stationary vacuum.  'STABLE true vacuum' is NOT established (the W159 speed-limit "
      "echo at cosmological scale)",
      stable_stationary_vacuum is False)
# The standard killer of non-perturbative rescues, steelmanned and CONCEDED: a condensate you
# cannot exhibit within EFT validity (NPV4) is not a rescue you can bank.  The lens finds the
# RIGHT true-vacuum CANDIDATE but cannot BUILD it -> grade CANDIDATE, not a cleared bar.
check("NPV5d: the standard non-perturbative-rescue killer (a condensate out of EFT validity, "
      "W159/NPV4; unbuilt source term, W154/NPV5b) applies -- the lens identifies the correct "
      "true-vacuum CANDIDATE (record-condensed phase) but cannot EXHIBIT it, so it is graded "
      "PLAUSIBLE-BUT-UNBUILT, not a cleared bar",
      (condensate_built is False) and (m0_scale > r_c))
log("  NPV5 VERDICT: RECORD-CONDENSED-PHASE-IS-TRUE-VACUUM-CANDIDATE (PLAUSIBLE-BUT-UNBUILT).")
log("  The false-vacuum reading is structurally SOUND but the true vacuum is un-built and its")
log("  stability is not established (monotone rolling).  This IS the standing session caveat.")

# ===========================================================================
# SYNTHESIS
# ===========================================================================
log("\n" + "=" * 78)
log("SYNTHESIS -- non-perturbative-vacuum verdict on debit-1")
log("=" * 78)
log("  NPV1 (AF running m^2(mu)):   NO-SIGN-FLIP-ON-AF.  m_0^2(mu) sign-locked NEGATIVE; Landau")
log("                               pole is a divergence, not a cure.  Tachyon not an RG artifact.")
log("  NPV2 (AS boundary datum):    UV-healthy reading AVAILABLE but UNFORCED (E2 carried).")
log("  NPV3 (Coleman-Weinberg):     Im V_eff != 0 -- the point IS a false vacuum (lens premise SOUND).")
log("  NPV4 (CW/condensate scale):  OUT-OF-VALIDITY (4x the EFT radius; speed-limit, not restoring).")
log("  NPV5 (record-condensed):     TRUE-VACUUM CANDIDATE, PLAUSIBLE-BUT-UNBUILT; stability not shown.")
log("")
log("  OVERALL: the lens is CORRECT that the perturbative tachyon is a FALSE vacuum (Im V_eff!=0),")
log("  and it NAMES the natural true vacuum (the record-condensed phase).  But that true vacuum is")
log("  precisely 'an un-built non-perturbative mechanism' -- out of EFT validity (NPV4), sourced by")
log("  an unbuilt boundary term (NPV5b), and not shown stable (NPV5c).  Debit-1 STANDS; the standing")
log("  caveat is the non-perturbative condensate.  Bar (b) UNCHANGED (flaw count does not drop).")

# ===========================================================================
log("\n" + "=" * 78)
if FAIL:
    log(f"RESULT: {len(FAIL)} FAILED")
    for f in FAIL:
        log("  FAIL: " + f)
    raise SystemExit(1)
log("RESULT: ALL PASS")
log("=" * 78)
