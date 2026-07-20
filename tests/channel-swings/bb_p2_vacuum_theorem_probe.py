#!/usr/bin/env python
"""BB-P2-VACUUM-THEOREM: lifting the CH-GR / P-K2 cancellation identity to a theorem.

Extends tests/channel-swings/pk2_gauge_covariance_probe.py (machinery mirrored;
conventions identical: eta = diag(-1,1,1,1), coordinate second-derivative bhat,
the gate's frozen (9,5)-inducing convention; per the CH-SIG77 port receipt every
algebraic identity here transfers verbatim to the (7,7)-inducing convention).

GROUP A -- the MASTER DEFECT LAW as a generic theorem:
  for ANY symmetric h:   t1 = (1/2)<(dH_sym).bhat> - <Ric^lin.bhat>,   hence
  Q^TF + [t2]^TF = (1/2)[<(dH_sym).bhat>]^TF - [<Ric^lin.bhat>]^TF
  (Q := t1 - t2, the gate's computed decomposition of the Willmore-type
  residual, ch_gr_vev_stress_probe.py PC4 -- cited, not re-derived).
  Proven on generic symbolic function entries; instantiated on a fully random
  polynomial h with BOTH defect terms nonzero simultaneously (new coverage:
  pk2 only ever had one term firing at a time), and on a two-center vacuum
  superposition (new background; stress carries cross-center interference).

GROUP B -- PRESENTATION-CLASS DISCHARGE (DEM-GR-3's shadow demand):
  Stueckelberg compensator phi_a with delta phi_a = xi_a makes
  htilde = h - (d phi)_sym gauge-INVARIANT, with H[htilde] = H[h] - box(phi).
  Nakanishi-Lautrup pair (bar_c, b) with gauge fermion
  Psi = <bar_c, H - (alpha/2) b>_eta gives S_gf = s(Psi) whose b-equation of
  motion in the Landau limit alpha -> 0 is EXACTLY Htilde_a = 0: the de
  Donder class becomes an equation of motion of the action's own auxiliary
  sector, not an external hypothesis. The generative identity is
  s H_a = box(c_a) -- literally pk2's n1 identity (the constraint defect of a
  gauge shift IS box of the gauge parameter). Teeth: a non-harmonic
  presentation is repaired by solving the compensator EOM box(phi) = H[h'];
  the EOM's solution space = the residual harmonic family; the cancellation
  holds with the frozen c = 1 on every repaired representative.

GROUP C -- FIRST NONLINEAR OBSTRUCTION (harmonic-coordinate Schwarzschild to
  O(M^2), exact series arithmetic, no floats):
  h1 + h2 extracted from the EXACT harmonic-gauge Schwarzschild metric;
  machinery validated by Ricci[eta + h1 + h2] = 0 at O(M) AND O(M^2), the
  inverse-metric identity, and the exact harmonic-coordinate condition
  g^{bc} Gamma^a_{bc} = 0 at both orders. Then the master law applied to
  h1 + h2 locates the first nonlinear obstruction at O(M^3):
    [t1]^TF|_{M^3} = (1/2)[<(dH[h2])_sym . bhat1>]^TF - [<Ric^lin[h2] . bhat1>]^TF
  with Ric^lin[h2] = -Ric^(2)[h1,h1] (second-order vacuum): a constraint
  piece (the linear de Donder defect of h2 -- the LINEAR class does not
  persist verbatim at second order even though the EXACT harmonic class
  does) plus the RICCI piece = gravitational self-energy entering the
  theorem's own matter slot, exactly as the K5 two-sided law types it.

Grassmann note (GROUP B): at this abelian quadratic grade the BRST algebra is
exhibited with commuting symbols; Koszul signs cancel pairwise for these
monomials (same stated convention as ch_src_minimal_action_toy.py).

Research probe, NOT a claim-status move. No map/canon/scorecard writes.
Run: python tests/channel-swings/bb_p2_vacuum_theorem_probe.py
"""

from __future__ import annotations

import random

import sympy as sp


FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL") + " :: " + name + ((" -- " + detail) if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


def log(message: str = "") -> None:
    print(message, flush=True)


# ---------------------------------------------------------------------------
# Shared weak-field machinery (mirrors pk2_gauge_covariance_probe.py exactly).
# ---------------------------------------------------------------------------
t, x, y, z, M = sp.symbols("t x y z M", real=True, positive=True)
coords = [t, x, y, z]
r = sp.sqrt(x**2 + y**2 + z**2)
eta = sp.diag(-1, 1, 1, 1)
HALF = sp.Rational(1, 2)
QUARTER = sp.Rational(1, 4)

# Exact rational probe points (r = 3, 7, 9). M is kept SYMBOLIC at these points
# wherever order-extraction is needed (Group C); set to 1 where a number is wanted.
PTS = [
    {x: 1, y: 2, z: 2, t: 1},
    {x: 2, y: 3, z: 6, t: 2},
    {x: 4, y: 4, z: 7, t: 3},
]


def schwarzschild_h() -> sp.Matrix:
    phi = M / r
    h = sp.zeros(4, 4)
    h[0, 0] = 2 * phi
    for i in (1, 2, 3):
        h[i, i] = 2 * phi
    return h


def d2_array(h: sp.Matrix):
    """d2[mu][nu][a][b] = d_mu d_nu h_ab (raw, unsimplified)."""
    return [
        [
            [[sp.diff(h[a, b], coords[mu], coords[nu]) for b in range(4)] for a in range(4)]
            for nu in range(4)
        ]
        for mu in range(4)
    ]


def riemann_of(h: sp.Matrix, simplify: bool = False):
    d2 = d2_array(h)
    R = [[[[None] * 4 for _ in range(4)] for _ in range(4)] for _ in range(4)]
    for mu in range(4):
        for a in range(4):
            for nu in range(4):
                for b in range(4):
                    val = HALF * (d2[mu][nu][a][b] + d2[a][b][mu][nu] - d2[mu][b][a][nu] - d2[a][nu][mu][b])
                    R[mu][a][nu][b] = sp.simplify(val) if simplify else val
    return R


def ricci_of(R):
    """Standard-sign linearized Ricci (GEN1 sign: box h = dH_sym - 2 ric)."""
    ric = sp.zeros(4, 4)
    for a in range(4):
        for b in range(4):
            ric[a, b] = -sum(eta[mu, mu] * R[mu][a][mu][b] for mu in range(4))
    return ric


def dedonder_H(h: sp.Matrix):
    """De Donder defect vector H_a = d^c h_ca - (1/2) d_a h."""
    trace = sum(eta[a, a] * h[a, a] for a in range(4))
    return [
        sum(eta[c, c] * sp.diff(h[c, a], coords[c]) for c in range(4)) - HALF * sp.diff(trace, coords[a])
        for a in range(4)
    ]


def gauge_shift(h: sp.Matrix, xi) -> sp.Matrix:
    out = sp.Matrix(h)
    for a in range(4):
        for b in range(4):
            out[a, b] = h[a, b] + sp.diff(xi[b], coords[a]) + sp.diff(xi[a], coords[b])
    return out


def box_of(expr):
    return sum(eta[m, m] * sp.diff(expr, coords[m], 2) for m in range(4))


def all_zero(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(matrix[i, j]) == 0 for i in range(4) for j in range(4))


def any_nonzero(matrix: sp.Matrix) -> bool:
    return any(sp.simplify(matrix[i, j]) != 0 for i in range(4) for j in range(4))


def sym_d(vec):
    """(d vec)_sym as a matrix: D_ab = d_a vec_b + d_b vec_a."""
    return sp.Matrix(4, 4, lambda a, b: sp.diff(vec[b], coords[a]) + sp.diff(vec[a], coords[b]))


def contract_with_bhat(A: sp.Matrix, bhat_fn):
    """<A.bhat>_mn = sum_ab eta^aa eta^bb A_ab bhat_{mn,ab}."""
    out = sp.zeros(4, 4)
    for m in range(4):
        for n in range(4):
            out[m, n] = sum(
                eta[a, a] * eta[b, b] * A[a, b] * bhat_fn(m, n, a, b) for a in range(4) for b in range(4)
            )
    return out


def blocks_of(d2n):
    """hmean, bhat, t1, t2 from a (possibly point-substituted) d2 array."""
    hmean = sp.Matrix(4, 4, lambda a, b: sum(eta[m, m] * d2n[m][m][a][b] for m in range(4)))

    def bhat(mu, nu, a, b):
        return d2n[mu][nu][a][b] - QUARTER * eta[mu, nu] * hmean[a, b]

    t1 = contract_with_bhat(HALF * hmean, bhat)
    t2 = sp.zeros(4, 4)
    for m in range(4):
        for n in range(4):
            t2[m, n] = sum(
                eta[p, p] * eta[a, a] * eta[b, b] * bhat(m, p, a, b) * bhat(p, n, a, b)
                for p in range(4)
                for a in range(4)
                for b in range(4)
            )
    return hmean, bhat, t1, t2


def tf_of(mat: sp.Matrix) -> sp.Matrix:
    trace = sum(eta[p, p] * mat[p, p] for p in range(4))
    return sp.Matrix(4, 4, lambda m, n: mat[m, n] - QUARTER * eta[m, n] * trace)


def psub(obj, pt):
    """Substitute a probe point (x,y,z,t only; M stays symbolic), exact."""
    if isinstance(obj, sp.Matrix):
        return obj.applyfunc(lambda e: sp.expand(e.subs(pt)))
    return sp.expand(obj.subs(pt))


def d2_at(d2, pt):
    return [
        [[[sp.expand(d2[mu][nu][a][b].subs(pt)) for b in range(4)] for a in range(4)] for nu in range(4)]
        for mu in range(4)
    ]


def mat_zero(mat: sp.Matrix) -> bool:
    return all(sp.simplify(mat[i, j]) == 0 for i in range(4) for j in range(4))


# Extended exact point set for Group C's per-instance legs (rational coords;
# radical values like sqrt(3) stay EXACT -- no floats). Honesty note: the
# Group C order-validation legs (C1a, C1b, C2a's O(M^2) leg, C3a, C3b) are
# point-exact instance checks at these six points, NOT generic symbolic
# proofs; the theorem's load-bearing generic legs (A1, B1-B3) are full
# symbolic proofs, and C2b/C4 receipts are exact closed forms / rationals.
CPTS = PTS + [
    {x: 1, y: 1, z: 1, t: 0},
    {x: 2, y: 1, z: 3, t: 1},
    {x: 3, y: 5, z: 1, t: 2},
]


def zero_at_points(e) -> bool:
    return all(sp.simplify(e.subs(pt)) == 0 for pt in CPTS)


def matrix_zero_at_points(mat: sp.Matrix) -> bool:
    return all(zero_at_points(mat[i, j]) for i in range(4) for j in range(4))


def matrix_nonzero_at_points(mat: sp.Matrix) -> bool:
    return any(
        sp.simplify(mat[i, j].subs(pt)) != 0 for pt in CPTS for i in range(4) for j in range(4)
    )


def constant_coefficient_scan(pairs):
    """Does one constant c satisfy qtf + c*stf = 0 across all components/points?"""
    values = []
    for qtf, stf in pairs:
        for m in range(4):
            for n in range(4):
                s_val = sp.simplify(stf[m, n])
                q_val = sp.simplify(qtf[m, n])
                if s_val == 0:
                    if q_val != 0:
                        return False, f"component ({m},{n}): stress 0 but residual nonzero"
                else:
                    values.append(sp.simplify(-q_val / s_val))
    if not values:
        return False, "stress identically zero at probe points"
    first = values[0]
    for v in values[1:]:
        if sp.simplify(v - first) != 0:
            return False, f"required coefficient not constant: {first} vs {v}"
    return True, f"constant coefficient c = {first}"


def main() -> None:
    # =======================================================================
    log("=" * 88)
    log("GROUP A -- THE MASTER DEFECT LAW (generic theorem; the vacuum theorem's engine)")
    log("=" * 88)

    # Generic symmetric h with function entries.
    hf = [[None] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(i, 4):
            f = sp.Function(f"h{i}{j}")(t, x, y, z)
            hf[i][j] = f
            hf[j][i] = f
    hfm = sp.Matrix(4, 4, lambda i, j: hf[i][j])

    Hg = dedonder_H(hfm)
    Dg = sym_d(Hg)
    ricg = ricci_of(riemann_of(hfm))

    gen1 = all(
        sp.expand(box_of(hfm[a, b]) - (Dg[a, b] - 2 * ricg[a, b])) == 0 for a in range(4) for b in range(4)
    )
    check(
        "A1a  GEN1 re-verified: box(h)_ab = (dH_sym)_ab - 2 Ric^lin_ab for GENERIC h",
        gen1,
        "self-containedness; identical to pk2 GEN1",
    )

    d2g = d2_array(hfm)
    hmean_g, bhat_g, t1_g, _ = blocks_of(d2g)
    law_rhs = HALF * contract_with_bhat(Dg, bhat_g) - contract_with_bhat(ricg, bhat_g)
    a1b = all(sp.expand(t1_g[m, n] - law_rhs[m, n]) == 0 for m in range(4) for n in range(4))
    check(
        "A1b  MASTER LAW generic: t1 = (1/2)<(dH_sym).bhat> - <Ric^lin.bhat> for GENERIC h",
        a1b,
        "hence Q^TF + [t2]^TF = (1/2)[<(dH_sym).bhat>]^TF - [<Ric.bhat>]^TF, identically",
    )
    log("")
    log("  COROLLARY (the vacuum theorem): H_a = 0 (de Donder class) AND Ric^lin = 0")
    log("  (gauge-invariant vacuum) kill both law terms => t1 = 0 => Q^TF = -[t2]^TF:")
    log("  the curvature-locked stress with sigma kappa^2 = 1 cancels exactly. Rigidity,")
    log("  sign gate, and the 4D Lanczos no-go are the pk2/gate receipts (cited).")
    log("")

    # A2: fully random polynomial h -- BOTH law terms nonzero simultaneously.
    rng = random.Random(20260719)

    def random_poly(deg: int):
        expr = sp.Integer(0)
        for _ in range(4):
            mono = sp.Integer(1)
            for _ in range(deg):
                mono *= coords[rng.randrange(4)]
            expr += sp.Rational(rng.choice([-3, -2, -1, 1, 2, 3]), rng.choice([1, 2, 3])) * mono
        return expr

    hr = sp.zeros(4, 4)
    for i in range(4):
        for j in range(i, 4):
            hr[i, j] = hr[j, i] = M * random_poly(3)
    Hr = dedonder_H(hr)
    Dr = sym_d(Hr)
    ricr = ricci_of(riemann_of(hr))
    check(
        "A2a  random polynomial h: BOTH defect sources nonzero (H != 0 AND Ric != 0)",
        any(sp.simplify(e) != 0 for e in Hr) and any_nonzero(ricr),
        "first instance in the program where both law terms fire at once",
    )
    d2r = d2_array(hr)
    ok_a2 = True
    for pt in PTS:
        ptM = dict(pt)
        ptM[M] = 1
        d2n = d2_at(d2r, ptM)
        _, bhat_n, t1_n, _ = blocks_of(d2n)
        con_n = HALF * contract_with_bhat(psub(Dr, ptM), bhat_n)
        ric_n = contract_with_bhat(psub(ricr, ptM), bhat_n)
        if not mat_zero(tf_of(t1_n) - tf_of(con_n) + tf_of(ric_n)):
            ok_a2 = False
    check(
        "A2b  master law instantiated: [t1]^TF = (1/2)[<dH_sym.bhat>]^TF - [<Ric.bhat>]^TF",
        ok_a2,
        "exact rational arithmetic, all components, r = 3, 7, 9 points",
    )
    log("")

    # A3: two-center vacuum superposition (new background; interference teeth).
    r1 = sp.sqrt(x**2 + y**2 + (z - 5) ** 2)
    r2 = sp.sqrt(x**2 + y**2 + (z + 5) ** 2)
    phi2c = M / r1 + M / r2
    h2c = sp.zeros(4, 4)
    h2c[0, 0] = 2 * phi2c
    for i in (1, 2, 3):
        h2c[i, i] = 2 * phi2c
    check(
        "A3a  two-center superposition is de Donder AND harmonic: H_a = 0, box(h) = 0",
        all(sp.simplify(e) == 0 for e in dedonder_H(h2c))
        and all(sp.simplify(box_of(h2c[a, b])) == 0 for a in range(4) for b in range(4)),
        "linearity of the class: sums of de Donder vacua stay in the class",
    )
    check(
        "A3b  linearized Ricci = 0 (gauge-invariant vacuum hypothesis holds)",
        all_zero(ricci_of(riemann_of(h2c))),
    )
    # box(h)=0 => hmean=0 => t1=0 identically => Q^TF = -[t2]^TF identically.
    # Exhibit nonvacuously at one point: TF stress nonzero AND carries
    # cross-center interference (t2[h1+h2] != t2[h1] + t2[h2]).
    pt0 = dict(PTS[0])
    pt0[M] = 1
    ha = sp.zeros(4, 4)
    ha[0, 0] = 2 * M / r1
    for i in (1, 2, 3):
        ha[i, i] = 2 * M / r1
    hb = sp.zeros(4, 4)
    hb[0, 0] = 2 * M / r2
    for i in (1, 2, 3):
        hb[i, i] = 2 * M / r2
    _, _, t1_2c, t2_2c = blocks_of(d2_at(d2_array(h2c), pt0))
    _, _, _, t2_a = blocks_of(d2_at(d2_array(ha), pt0))
    _, _, _, t2_b = blocks_of(d2_at(d2_array(hb), pt0))
    check(
        "A3c  identity holds on the NEW background with interference teeth",
        mat_zero(t1_2c)
        and any(sp.simplify(tf_of(t2_2c)[i, j]) != 0 for i in range(4) for j in range(4))
        and any(sp.simplify((t2_2c - t2_a - t2_b)[i, j]) != 0 for i in range(4) for j in range(4)),
        "t1 = 0 => Q^TF = -[t2]^TF with c = 1; stress has nonzero cross-center terms",
    )
    log("")

    # =======================================================================
    log("=" * 88)
    log("GROUP B -- PRESENTATION-CLASS DISCHARGE: de Donder as an equation of motion")
    log("=" * 88)

    phif = [sp.Function(f"phi{a}")(t, x, y, z) for a in range(4)]
    xif = [sp.Function(f"xi{a}")(t, x, y, z) for a in range(4)]

    def htilde(h, phi):
        return gauge_shift(h, [-p for p in phi])

    ht_shift = htilde(gauge_shift(hfm, xif), [phif[a] + xif[a] for a in range(4)])
    ht_base = htilde(hfm, phif)
    check(
        "B1  htilde = h - (d phi)_sym is GAUGE-INVARIANT (delta h = d xi_sym, delta phi = xi)",
        all(sp.expand(ht_shift[a, b] - ht_base[a, b]) == 0 for a in range(4) for b in range(4)),
        "generic function entries: the compensated field is a gauge-invariant object",
    )
    Ht = dedonder_H(ht_base)
    check(
        "B2  H[htilde] = H[h] - box(phi) for GENERIC h, phi",
        all(sp.expand(Ht[a] - (Hg[a] - box_of(phif[a]))) == 0 for a in range(4)),
        "the gauge-invariant constraint Htilde_a := H[h]_a - box(phi_a)",
    )
    cf = [sp.Function(f"c{a}")(t, x, y, z) for a in range(4)]
    Hc = dedonder_H(gauge_shift(hfm, cf))
    check(
        "B3  BRST generative identity: s H_a = box(c_a) (s h = (d c)_sym)",
        all(sp.expand(Hc[a] - Hg[a] - box_of(cf[a])) == 0 for a in range(4)),
        "pk2's n1 identity IS the gauge-fermion algebra: s Psi = <b,H> - (alpha/2)<b,b> - <bar_c, box c>",
    )
    log("")
    log("  Gauge-fermion bookkeeping at this abelian quadratic grade (commuting-symbol")
    log("  convention as in ch_src_minimal_action_toy.py): with s h = (dc)_sym, s c = 0,")
    log("  s bar_c = b, s b = 0 (s^2 = 0 termwise), Psi = <bar_c, H - (alpha/2) b>_eta:")
    log("    S_gf = s(Psi) = <b, H>_eta - (alpha/2)<b, b>_eta - <bar_c, box c>_eta,")
    log("  and s(S_gf) = <b, box c> - <b, box c> = 0 by B3. The Krein point: every")
    log("  bracket is the SAME indefinite eta form -- SRC-COH-1's one-form rule.")
    log("")

    b_syms = sp.symbols("b0 b1 b2 b3", real=True)
    Ht_syms = sp.symbols("Ht0 Ht1 Ht2 Ht3", real=True)
    alpha = sp.symbols("alpha", real=True, positive=True)
    S_aux = sum(eta[a, a] * b_syms[a] * Ht_syms[a] for a in range(4)) - HALF * alpha * sum(
        eta[a, a] * b_syms[a] ** 2 for a in range(4)
    )
    eoms = [sp.expand(sp.diff(S_aux, b_syms[a]) - eta[a, a] * (Ht_syms[a] - alpha * b_syms[a])) for a in range(4)]
    landau = [sp.diff(S_aux, b_syms[a]).subs(alpha, 0) - eta[a, a] * Ht_syms[a] for a in range(4)]
    check(
        "B4  Nakanishi-Lautrup EOM: dS/db_a = eta^aa (Htilde_a - alpha b_a); Landau limit => Htilde_a = 0",
        all(e == 0 for e in eoms) and all(sp.expand(e) == 0 for e in landau),
        "the de Donder class is the auxiliary sector's equation of motion, alpha -> 0",
    )
    log("")

    # B5: teeth -- repair a non-harmonic presentation by solving the compensator EOM.
    hs = schwarzschild_h()
    xi_bad = [M * x * y * z, M * (x**3 + t * y**2), M * (t**2 * z + y**3), M * (x**2 * z)]
    h_bad = gauge_shift(hs, xi_bad)
    H_bad = dedonder_H(h_bad)
    check(
        "B5a  non-harmonic presentation: H[h'] = box(xi_bad) != 0",
        all(sp.simplify(H_bad[a] - box_of(xi_bad[a])) == 0 for a in range(4))
        and any(sp.simplify(box_of(xi_bad[a])) != 0 for a in range(4)),
    )
    xi_harm = [sp.Integer(0), M * (x**3 - 3 * x * y**2), M * t * x * y, M * (z**3 - 3 * z * x**2)]
    phi_sol = [xi_bad[a] + xi_harm[a] for a in range(4)]
    check(
        "B5b  compensator EOM solved: box(phi) = H[h'] with a NONTRIVIAL harmonic kernel part",
        all(sp.simplify(box_of(phi_sol[a]) - H_bad[a]) == 0 for a in range(4))
        and any(sp.simplify(xi_harm[a]) != 0 for a in range(4)),
        "solution space of the EOM = particular + harmonic kernel = the residual family",
    )
    h_rep = htilde(h_bad, phi_sol)
    check(
        "B5c  repaired representative: H[htilde] = 0 and htilde differs from the base presentation",
        all(sp.simplify(e) == 0 for e in dedonder_H(h_rep))
        and any(sp.simplify(h_rep[a, b] - hs[a, b]) != 0 for a in range(4) for b in range(4)),
        "the EOM outputs a de Donder representative, unique up to the residual family",
    )
    pairs = []
    d2rep = d2_array(h_rep)
    for pt in PTS:
        ptM = dict(pt)
        ptM[M] = 1
        _, _, t1_n, t2_n = blocks_of(d2_at(d2rep, ptM))
        pairs.append((tf_of(t1_n - t2_n), tf_of(t2_n)))
    ok_scan, detail = constant_coefficient_scan(pairs)
    check(
        "B5d  the theorem holds on the repaired representative with the frozen coefficient",
        ok_scan and detail.endswith("c = 1"),
        detail,
    )
    log("")

    # =======================================================================
    log("=" * 88)
    log("GROUP C -- FIRST NONLINEAR OBSTRUCTION: harmonic Schwarzschild to O(M^2)")
    log("=" * 88)
    log("Exact harmonic-coordinate Schwarzschild (standard R = r + M form):")
    log("  g_00 = -(r-M)/(r+M);  g_ij = ((r+M)/(r-M)) n_i n_j + ((r+M)^2/r^2)(delta_ij - n_i n_j)")
    log("")

    xs = [x, y, z]
    g_exact = sp.zeros(4, 4)
    g_exact[0, 0] = -(r - M) / (r + M)
    for i in range(3):
        for j in range(3):
            nij = xs[i] * xs[j] / r**2
            g_exact[i + 1, j + 1] = ((r + M) / (r - M)) * nij + ((r + M) ** 2 / r**2) * (
                (1 if i == j else 0) - nij
            )

    def order_part(e, k):
        ser = sp.expand(sp.series(sp.together(e), M, 0, 3).removeO())
        return sp.expand(ser.coeff(M, k) * M**k)

    h1 = sp.Matrix(4, 4, lambda a, b: order_part(g_exact[a, b] - eta[a, b], 1))
    h2 = sp.Matrix(4, 4, lambda a, b: order_part(g_exact[a, b] - eta[a, b], 2))
    check(
        "C0a  O(M) piece of exact harmonic Schwarzschild = the gate's linear background h1",
        all(sp.simplify(h1[a, b] - hs[a, b]) == 0 for a in range(4) for b in range(4)),
        "h2_00 = -2M^2/r^2, h2_ij = M^2 (delta_ij/r^2 + x_i x_j/r^4) extracted alongside",
    )

    # Order-split series arithmetic: g^{-1} = eta + i1 + i2 with i1 = O(M),
    # i2 = O(M^2); every product below multiplies only SMALL fixed-order parts
    # (no monolithic truncation of mixed-order expansions).
    i1 = (-eta * h1 * eta).applyfunc(sp.expand)
    i2 = (eta * h1 * eta * h1 * eta - eta * h2 * eta).applyfunc(sp.expand)
    ord1 = (h1 * eta + eta * i1).applyfunc(sp.expand)
    ord2 = (h2 * eta + h1 * i1 + eta * i2).applyfunc(sp.expand)
    check(
        "C0b  inverse-metric identity to O(M^2): g . ginv = 1 + O(M^3), order by order",
        all(
            sp.simplify(ord1[a, b]) == 0 and sp.simplify(ord2[a, b]) == 0
            for a in range(4)
            for b in range(4)
        ),
    )

    log("  building order-split Christoffels and Ricci (exact series arithmetic)...")

    def lower_symbol(h, d, b, c):
        """L_d(bc)[h] = d_b h_dc + d_c h_bd - d_d h_bc."""
        return (
            sp.diff(h[d, c], coords[b]) + sp.diff(h[b, d], coords[c]) - sp.diff(h[b, c], coords[d])
        )

    def christoffel_orders(hA, hB):
        """Gamma^a_bc of eta + hA + hB as (G1, G2), exact orders O(M), O(M^2)."""
        iA = (-eta * hA * eta).applyfunc(sp.expand)
        G1 = [[[None] * 4 for _ in range(4)] for _ in range(4)]
        G2 = [[[None] * 4 for _ in range(4)] for _ in range(4)]
        for a in range(4):
            for b in range(4):
                for c in range(b, 4):
                    v1 = sp.expand(HALF * eta[a, a] * lower_symbol(hA, a, b, c))
                    v2 = sp.expand(
                        HALF * eta[a, a] * lower_symbol(hB, a, b, c)
                        + HALF * sum(iA[a, d] * lower_symbol(hA, d, b, c) for d in range(4))
                    )
                    G1[a][b][c] = G1[a][c][b] = v1
                    G2[a][b][c] = G2[a][c][b] = v2
        return G1, G2

    def ricci_orders(G1, G2):
        """(Ric at O(M), Ric at O(M^2)) from order-split Christoffels.
        Entries are kept as LAZY (unexpanded) expression trees: all Group C
        order-validation checks evaluate them at exact points, where the
        substituted trees collapse to exact numbers cheaply."""
        R1 = sp.zeros(4, 4)
        R2 = sp.zeros(4, 4)
        for a in range(4):
            for b in range(a, 4):
                e1 = sum(sp.diff(G1[c][a][b], coords[c]) for c in range(4)) - sum(
                    sp.diff(G1[c][c][b], coords[a]) for c in range(4)
                )
                e2 = (
                    sum(sp.diff(G2[c][a][b], coords[c]) for c in range(4))
                    - sum(sp.diff(G2[c][c][b], coords[a]) for c in range(4))
                    + sum(G1[c][c][d] * G1[d][a][b] for c in range(4) for d in range(4))
                    - sum(G1[c][a][d] * G1[d][c][b] for c in range(4) for d in range(4))
                )
                R1[a, b] = R1[b, a] = e1
                R2[a, b] = R2[b, a] = e2
        return R1, R2

    G1f, G2f = christoffel_orders(h1, h2)
    Ric1_full, Ric2_full = ricci_orders(G1f, G2f)
    check(
        "C1a  Ricci[eta + h1 + h2] vanishes at O(M) (linear vacuum leg reproduced)",
        matrix_zero_at_points(Ric1_full),
        "exact arithmetic at six exact points (instance check, stated as such)",
    )
    check(
        "C1b  Ricci[eta + h1 + h2] vanishes at O(M^2): h2 IS the true second-order piece",
        matrix_zero_at_points(Ric2_full),
        "exact arithmetic at six exact points (instance check, stated as such)",
    )

    # Exact harmonic-coordinate condition at both orders:
    # V^a = g^{bc} Gamma^a_bc; order 1 = eta^{bb} G1; order 2 = eta^{bb} G2 + i1^{bc} G1.
    V1 = [sum(eta[b, b] * G1f[a][b][b] for b in range(4)) for a in range(4)]
    V2 = [
        sum(eta[b, b] * G2f[a][b][b] for b in range(4))
        + sum(i1[b, c] * G1f[a][b][c] for b in range(4) for c in range(4))
        for a in range(4)
    ]
    check(
        "C2a  EXACT harmonic condition g^{bc} Gamma^a_{bc} = 0 holds at O(M) AND O(M^2)",
        all(sp.simplify(V1[a]) == 0 for a in range(4))
        and all(zero_at_points(V2[a]) for a in range(4)),
        "the exact-harmonic CLASS survives nonlinearly (O(M^2) leg at six exact points)",
    )
    H_h2 = dedonder_H(h2)
    H_h2_expected = [sp.Integer(0)] + [4 * M**2 * xs[i] / r**4 for i in range(3)]
    c2b = all(sp.simplify(H_h2[a] - H_h2_expected[a]) == 0 for a in range(4))
    check(
        "C2b  ...but the LINEAR de Donder defect of h2 is NONZERO: H[h2]_i = 4 M^2 x_i / r^4",
        c2b,
        "the linear class does NOT persist verbatim at second order; its defect is DETERMINED",
    )

    # Second-order Ricci of h1 alone (gravitational self-energy source).
    G1a, G2a = christoffel_orders(h1, sp.zeros(4, 4))
    _, Ric2_h1 = ricci_orders(G1a, G2a)
    check(
        "C3a  Ric^(2)[h1,h1] != 0 (gravitational self-energy is nonzero)",
        matrix_nonzero_at_points(Ric2_h1),
    )
    ric_h2 = ricci_of(riemann_of(h2))
    check(
        "C3b  second-order vacuum bookkeeping: Ric^lin[h2] = -Ric^(2)[h1,h1]",
        matrix_zero_at_points(ric_h2 + Ric2_h1),
        "exact arithmetic at six exact points; the h2 sector is sourced by h1's self-energy",
    )

    # The first obstruction at O(M^3), via the master law applied to h1 + h2.
    log("")
    log("  first obstruction: [t1[h1+h2]]^TF at O(M^3) vs the master law's two typed terms")
    D_h2 = sym_d(H_h2)
    d2_h1 = d2_array(h1)
    d2_full = d2_array(h1 + h2)
    obst_ok = True
    m2_clean = True
    ric_piece_nonzero = False
    con_piece_nonzero = False
    total_nonzero = False
    sample = None
    for pt in PTS:
        d2n1 = d2_at(d2_h1, pt)
        hmean1, bhat1, _, _ = blocks_of(d2n1)
        if not mat_zero(hmean1):
            obst_ok = False  # box h1 = 0 must hold
        d2nf = d2_at(d2_full, pt)
        _, _, t1_f, _ = blocks_of(d2nf)
        t1_f_tf = tf_of(t1_f).applyfunc(sp.expand)
        if any(sp.simplify(t1_f_tf[i, j].coeff(M, 2)) != 0 for i in range(4) for j in range(4)):
            m2_clean = False
        obst = sp.Matrix(4, 4, lambda i, j: t1_f_tf[i, j].coeff(M, 3) * M**3)
        con_term = tf_of(HALF * contract_with_bhat(psub(D_h2, pt), bhat1)).applyfunc(sp.expand)
        ric_term = tf_of(-contract_with_bhat(psub(ric_h2, pt), bhat1)).applyfunc(sp.expand)
        if not mat_zero(obst - con_term - ric_term):
            obst_ok = False
        if any_nonzero(ric_term):
            ric_piece_nonzero = True
        if any_nonzero(con_term):
            con_piece_nonzero = True
        if any_nonzero(obst):
            total_nonzero = True
        if sample is None:
            sample = (
                sp.simplify(obst[1, 1]),
                sp.simplify(con_term[1, 1]),
                sp.simplify(ric_term[1, 1]),
                sp.simplify(obst[0, 0]),
            )
    check(
        "C4a  the linear theorem is CLEAN at O(M^2): [t1[h1+h2]]^TF has no M^2 term",
        m2_clean,
        "the vacuum cancellation survives; the obstruction starts strictly at next order",
    )
    check(
        "C4b  FIRST OBSTRUCTION LAW at O(M^3): [t1]^TF|_M3 = (1/2)[<(dH[h2])_sym.bhat1>]^TF - [<Ric^lin[h2].bhat1>]^TF",
        obst_ok,
        "the master law types the nonlinear defect: constraint piece + Ricci piece, nothing else",
    )
    check(
        "C4c  the Ricci piece is NONZERO: gravitational self-energy enters the matter slot",
        ric_piece_nonzero,
        "+[<Ric^(2)[h1].bhat1>]^TF != 0 -- K5's two-sided law with self-energy as the matter",
    )
    check(
        "C4d  the total obstruction is NONZERO (and the constraint piece fires too)",
        total_nonzero and con_piece_nonzero,
        "the linear theorem does NOT extend verbatim to O(M^3); both typed pieces present",
    )
    if sample is not None:
        log("")
        log(f"  receipts at point (x,y,z)=(1,2,2), r=3 (exact, M symbolic):")
        log(f"    obstruction (1,1) component:  {sample[0]}")
        log(f"    constraint piece (1,1):       {sample[1]}")
        log(f"    Ricci piece (1,1):            {sample[2]}")
        log(f"    obstruction (0,0) component:  {sample[3]}")

    # =======================================================================
    log("")
    log("=" * 88)
    log("SUMMARY")
    log("=" * 88)
    log("A: master defect law proven generically; vacuum theorem = its corollary; new")
    log("   coverage: both-terms-firing random h, two-center vacuum with interference.")
    log("B: de Donder class discharged to an EQUATION OF MOTION (Stueckelberg compensator")
    log("   + Nakanishi-Lautrup pair, Landau limit); generative identity s H = box(c) is")
    log("   pk2's n1; EOM solution space = residual family; c = 1 on repaired reps.")
    log("C: first nonlinear obstruction located at O(M^3) and TYPED by the master law:")
    log("   constraint piece (linear-class defect of h2, determined not free) + Ricci")
    log("   piece (= gravitational self-energy in the theorem's matter slot). The exact")
    log("   harmonic CLASS persists (C2a); the linear theorem is clean at O(M^2) (C4a).")
    if FAIL:
        log(f"\nRESULT: {len(FAIL)} FAILED")
        for name in FAIL:
            log("  FAIL: " + name)
        raise SystemExit(1)
    log("\nRESULT: ALL PASS")


if __name__ == "__main__":
    main()
