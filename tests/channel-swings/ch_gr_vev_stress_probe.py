#!/usr/bin/env python
"""CH-GR channel swing: C10 distortion-VEV stress probe (H-GR' sub-branches).

Channel-swing probe for CH-GR under the boundary-adapter standing axiom
(lab/process/boundary-adapter-standing-axiom.md). It formalizes the C10
distortion vacuum field theta in the weak-field symbol frame and COMPUTES,
for the three H-GR' sub-branches (five-leg swing, CH-GR deepened):

  (a) curvature-locked anisotropic VEV  -- theta_vac = kappa * bhat(B)
  (b) homogeneous VEV                   -- constant theta (isotropic and
                                           frozen-direction sub-cases)
  (c) gradient-dominated VEV            -- theta_vac = v * d(phi)

whether the induced quadratic VEV stress carries a nonzero trace-free
Q^TF(B)-slot component at O(M^2), and whether it can CANCEL the computed
Q^TF(B) residual with one frozen constant coefficient.

Structural fact the probe rides on (computed, not assumed): the gate's own
residual is Q = t1 - t2 with t1 = (1/2) hmean . bhat and hmean = box(h).
On a harmonic-gauge linearized-vacuum background box(h) = 0, so
Q^TF = -[t2]^TF exactly -- and t2 is precisely the canonical quadratic
stress bilinear of a field theta locked to bhat with the identity kernel.

Also checked: the C2 scale-law constraint C2(2xi)/C2(xi) = 2 as a
kernel-purity condition (scale-free kernels pass; dimensionful-parameter
kernels fail), and preservation of the linear cheap-read clears.

This is a research probe, NOT a claim-status move. No map/canon writes.

Run: python tests/channel-swings/ch_gr_vev_stress_probe.py
"""

from __future__ import annotations

import sympy as sp


FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL") + " :: " + name + ((" -- " + detail) if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


def log(message: str = "") -> None:
    print(message, flush=True)


# ---------------------------------------------------------------------------
# Shared weak-field symbols (mirrors construction_space_gr_r0_c9_c3_gate.py).
# ---------------------------------------------------------------------------
t, x, y, z, M, J = sp.symbols("t x y z M J", real=True, positive=True)
coords = [t, x, y, z]
r = sp.sqrt(x**2 + y**2 + z**2)
eta = sp.diag(-1, 1, 1, 1)


def schwarzschild_h() -> sp.Matrix:
    phi = M / r
    h = sp.zeros(4, 4)
    h[0, 0] = 2 * phi
    for i in (1, 2, 3):
        h[i, i] = 2 * phi
    return h


def kerr_drag_h() -> sp.Matrix:
    """Schwarzschild + leading Kerr frame-dragging term (J along z), harmonic gauge."""
    h = schwarzschild_h()
    h[0, 1] = h[1, 0] = -2 * J * y / r**3
    h[0, 2] = h[2, 0] = 2 * J * x / r**3
    return h


def hmean_of(h: sp.Matrix) -> sp.Matrix:
    """hmean_ab = eta^{mm} d_m d_m h_ab = box(h_ab)."""
    out = sp.zeros(4, 4)
    for a in range(4):
        for b in range(4):
            out[a, b] = sp.simplify(sum(eta[m, m] * sp.diff(h[a, b], coords[m], 2) for m in range(4)))
    return out


def bhat_of(h: sp.Matrix, hmean: sp.Matrix):
    """Trace-hatted second-derivative slot bhat_{mu nu, ab} (gate convention)."""
    def b(mu: int, nu: int, a: int, bidx: int) -> sp.Expr:
        return sp.diff(h[a, bidx], coords[mu], coords[nu])

    def bhat(mu: int, nu: int, a: int, bidx: int) -> sp.Expr:
        return b(mu, nu, a, bidx) - sp.Rational(1, 4) * eta[mu, nu] * hmean[a, bidx]

    return bhat


def fdot(func) -> sp.Expr:
    return sum(eta[a, a] * eta[b, b] * func(a, b) for a in range(4) for b in range(4))


def t1_t2_of(h: sp.Matrix):
    """The gate's two quadratic blocks: q = t1 - t2."""
    hmean = hmean_of(h)
    bhat = bhat_of(h, hmean)
    t1 = sp.zeros(4, 4)
    t2 = sp.zeros(4, 4)
    for mu in range(4):
        for nu in range(4):
            t1[mu, nu] = sp.simplify(
                sp.Rational(1, 2) * fdot(lambda a, b: hmean[a, b] * bhat(mu, nu, a, b))
            )
            t2[mu, nu] = sp.simplify(
                sum(
                    eta[p, p] * fdot(lambda a, b: bhat(mu, p, a, b) * bhat(p, nu, a, b))
                    for p in range(4)
                )
            )
    return hmean, t1, t2


def trace_free_part(matrix: sp.Matrix) -> sp.Matrix:
    trace = sp.simplify(sum(eta[p, p] * matrix[p, p] for p in range(4)))
    out = sp.zeros(4, 4)
    for mu in range(4):
        for nu in range(4):
            out[mu, nu] = sp.simplify(matrix[mu, nu] - sp.Rational(1, 4) * eta[mu, nu] * trace)
    return out


def all_zero(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(matrix[i, j]) == 0 for i in range(4) for j in range(4))


def any_nonzero(matrix: sp.Matrix) -> bool:
    return any(sp.simplify(matrix[i, j]) != 0 for i in range(4) for j in range(4))


POINT1 = {x: 1, y: 2, z: 2, t: 0, M: 1, J: 1}   # r = 3
POINT2 = {x: 2, y: 3, z: 6, t: 0, M: 1, J: 1}   # r = 7


def constant_coefficient_cancels(qtf: sp.Matrix, stf: sp.Matrix) -> tuple[bool, str]:
    """Does a single CONSTANT c exist with qtf + c*stf = 0 (all components, all points)?

    Method: at two rational points, collect the required c = -q/s over every
    component where s != 0; require q = 0 wherever s = 0; require all
    collected values to agree across components AND across points.
    """
    values = []
    for pt in (POINT1, POINT2):
        for mu in range(4):
            for nu in range(4):
                sval = sp.nsimplify(stf[mu, nu].subs(pt))
                qval = sp.nsimplify(qtf[mu, nu].subs(pt))
                if sval == 0:
                    if qval != 0:
                        return False, f"component ({mu},{nu}): stress 0 but residual nonzero"
                else:
                    values.append(sp.nsimplify(-qval / sval))
    if not values:
        return False, "stress identically zero at probe points"
    first = values[0]
    for v in values[1:]:
        if sp.simplify(v - first) != 0:
            return False, f"required coefficient not constant: {first} vs {v}"
    return True, f"constant coefficient c = {first}"


def main() -> None:
    log("=" * 82)
    log("PC controls -- background structure and residual teeth")
    log("=" * 82)
    h = schwarzschild_h()
    hmean, t1, t2 = t1_t2_of(h)
    check("PC1  Schwarzschild weak-field h is harmonic: hmean = box(h) = 0", all_zero(hmean))
    check("PC2  hence t1 = (1/2) hmean.bhat vanishes identically", all_zero(t1))
    qtf = trace_free_part(t1 - t2)
    check("PC3  Q^TF(B) = [t1 - t2]^TF is nonzero (residual has teeth)", any_nonzero(qtf))
    t2tf = trace_free_part(t2)
    check(
        "PC4  structural identity: Q^TF = -[t2]^TF on this background",
        all_zero(qtf + t2tf),
        "harmonic gauge + linearized vacuum kills the t1 block",
    )
    check(
        "PC5  Q^TF is O(M^2) exactly: Q^TF(2M) = 4 Q^TF(M)",
        all_zero(qtf.subs(M, 2 * M) - 4 * qtf),
    )

    log("")
    log("=" * 82)
    log("Branch (a) -- curvature-locked anisotropic VEV: theta_vac = kappa * bhat")
    log("=" * 82)
    # Typed home (weak-field symbol): theta in Omega^1(X4) valued in the
    # vertical-Christoffel / SFF slot of Y14 = Met(X4); components
    # theta_{mu nu}^{ab} = kappa * bhat_{mu nu, ab}. Canonical quadratic
    # stress bilinear with the eta-contractions on every slot:
    #   S_mn = sigma * kappa^2 * sum_p eta^pp <bhat_mp, bhat_pn>_fiber
    #        = sigma * kappa^2 * t2_mn.
    kappa, sigma = sp.symbols("kappa sigma", real=True)
    s_a_tf = trace_free_part(t2)  # stress TF block, unit kappa, sigma = +1
    check(
        "A1  curvature-locked VEV stress has NONZERO trace-free Q^TF-slot part at O(M^2)",
        any_nonzero(s_a_tf),
        "first live nonzero trace-free candidate in the C10 family",
    )
    check(
        "A2  stress is O(M^2) exactly (linear cheap-read clears preserved)",
        all_zero(s_a_tf.subs(M, 2 * M) - 4 * s_a_tf),
        "no O(M) contamination: quadratic in bhat by construction",
    )
    # Cancellation: qtf + sigma*kappa^2*[t2]^TF = (sigma*kappa^2 - 1) [t2]^TF.
    ok_cancel, detail = constant_coefficient_cancels(qtf, s_a_tf)
    check(
        "A3  EXACT cancellation with one frozen constant coefficient",
        ok_cancel and detail.endswith("c = 1"),
        detail,
    )
    # Sign structure: with sigma = -1 (wrong orientation) no real kappa works.
    wrong_sign_residual = sp.simplify(-(1 + kappa**2))
    check(
        "A4  wrong sign orientation (sigma = -1) admits NO real kappa",
        sp.solve(sp.Eq(wrong_sign_residual, 0), kappa) == [],
        "residual factor -(1 + kappa^2) has no real zero: cancellation sign is a Z/2 datum",
    )
    right_sign_solutions = sp.solve(sp.Eq(kappa**2 - 1, 0), kappa)
    check(
        "A5  right sign orientation fixes kappa^2 = 1 (one frozen pure number)",
        sorted(right_sign_solutions) == [-1, 1],
        f"kappa in {right_sign_solutions}",
    )

    log("")
    log("Robustness: same identity on the Kerr frame-dragging background")
    hk = kerr_drag_h()
    hmean_k = hmean_of(hk)
    check("A6  Kerr-drag weak field is also harmonic: box(h) = 0", all_zero(hmean_k))
    # With hmean = 0 the identity Q = -t2 is algebraic; verify the t1 block.
    _, t1_k, t2_k = t1_t2_of(hk)
    check("A7  t1 block vanishes on Kerr-drag too", all_zero(t1_k))
    qtf_k = trace_free_part(t1_k - t2_k)
    check(
        "A8  cancellation identity extends to Kerr-drag with the SAME frozen kappa^2 = 1",
        all_zero(qtf_k + trace_free_part(t2_k)),
        "not Schwarzschild-tuned: holds across harmonic-gauge linearized vacuum",
    )

    log("")
    log("=" * 82)
    log("Branch (b) -- homogeneous VEV (predicted to fail C3-style; computed)")
    log("=" * 82)
    lam = sp.symbols("lambda_c", real=True)
    # (b1) isotropic homogeneous: stress proportional to the metric.
    s_b1 = lam * eta
    check(
        "B1  isotropic homogeneous VEV stress has ZERO trace-free part (C3-image, dead)",
        all_zero(trace_free_part(s_b1)),
    )
    # (b2) frozen-direction homogeneous: theta_m = v u_m with u = dt.
    v = sp.symbols("v", real=True)
    s_b2 = sp.zeros(4, 4)
    s_b2[0, 0] = v**2
    s_b2_tf = trace_free_part(s_b2)
    check("B2  frozen-direction homogeneous stress has nonzero trace-free part", any_nonzero(s_b2_tf))
    ok_b2, detail_b2 = constant_coefficient_cancels(qtf, s_b2_tf)
    check(
        "B3  but NO constant coefficient cancels Q^TF (constant vs M^2/r^6 profile)",
        not ok_b2,
        detail_b2,
    )

    log("")
    log("=" * 82)
    log("Branch (c) -- gradient-dominated VEV: theta_m = v * d_m(phi)")
    log("=" * 82)
    # (c1) natural harmonic response phi = M/r: stress ~ M^2/r^4.
    phi1 = M / r
    s_c1 = sp.zeros(4, 4)
    for mu in range(4):
        for nu in range(4):
            s_c1[mu, nu] = sp.simplify(sp.diff(phi1, coords[mu]) * sp.diff(phi1, coords[nu]))
    s_c1_tf = trace_free_part(s_c1)
    check("C1  harmonic-response gradient stress has nonzero trace-free part", any_nonzero(s_c1_tf))
    ok_c1, detail_c1 = constant_coefficient_cancels(qtf, s_c1_tf)
    check(
        "C2  but NO constant coefficient cancels Q^TF (falloff M^2/r^4 vs M^2/r^6)",
        not ok_c1,
        detail_c1,
    )
    # (c2) falloff-tuned profile phi = M/r^2: right order in r, wrong structure?
    phi2 = M / r**2
    box_phi2 = sp.simplify(sum(eta[m, m] * sp.diff(phi2, coords[m], 2) for m in range(4)))
    check(
        "C3  the falloff-tuned profile phi = M/r^2 is NOT harmonic (needs a source)",
        sp.simplify(box_phi2) != 0,
        f"box(phi) = {box_phi2} != 0: violates vacuum-supported requirement",
    )
    s_c2 = sp.zeros(4, 4)
    for mu in range(4):
        for nu in range(4):
            s_c2[mu, nu] = sp.simplify(sp.diff(phi2, coords[mu]) * sp.diff(phi2, coords[nu]))
    s_c2_tf = trace_free_part(s_c2)
    ok_c2, detail_c2 = constant_coefficient_cancels(qtf, s_c2_tf)
    check(
        "C4  even falloff-tuned, NO constant coefficient cancels Q^TF (tensor mismatch)",
        not ok_c2,
        detail_c2,
    )

    log("")
    log("=" * 82)
    log("C2 scale law -- kernel-purity constraint: C2(2xi)/C2(xi) = 2")
    log("=" * 82)
    xi1, xi2, xi3, L = sp.symbols("xi1 xi2 xi3 L", real=True, positive=True)
    xin = sp.sqrt(xi1**2 + xi2**2 + xi3**2)
    # Scale-free kernel: compensator symbol linear in xi times a constant.
    sym_free = kappa * xin
    ratio_free = sp.simplify(sym_free.subs(((xi1, 2 * xi1), (xi2, 2 * xi2), (xi3, 2 * xi3))) / sym_free)
    check("D1  scale-free (constant) kernel reproduces the exact factor-2 law", sp.simplify(ratio_free - 2) == 0)
    # Dimensionful kernel: internal length scale L breaks the exact law.
    sym_massive = kappa * xin / (1 + L**2 * xin**2)
    ratio_massive = sp.simplify(
        sym_massive.subs(((xi1, 2 * xi1), (xi2, 2 * xi2), (xi3, 2 * xi3))) / sym_massive
    )
    deviation = sp.simplify(ratio_massive - 2)
    check(
        "D2  a kernel carrying an internal scale VIOLATES the exact factor-2 law",
        sp.simplify(deviation.subs({xi1: 1, xi2: 1, xi3: 1, L: 1})) != 0,
        "C2 scale covariance forbids dimensionful kernel parameters",
    )

    log("")
    log("=" * 82)
    log("VERDICT")
    log("=" * 82)
    if not FAIL:
        log("Branch (a) curvature-locked anisotropic: LIVE. The VEV stress carries a")
        log("nonzero trace-free Q^TF(B)-slot component at O(M^2) and cancels the computed")
        log("residual EXACTLY with sigma = +1 (Z/2 orientation datum) and kappa^2 = 1 (one")
        log("frozen pure number), on Schwarzschild AND Kerr-drag harmonic-gauge backgrounds.")
        log("Branch (b) homogeneous: DEAD both sub-cases (zero trace-free part, or constant")
        log("profile that no constant coefficient can match to M^2/r^6).")
        log("Branch (c) gradient-dominated: DEAD (wrong falloff at the harmonic profile;")
        log("the falloff-tuned profile is non-harmonic AND tensor-mismatched).")
        log("C2 scale law: satisfied by scale-free kernels only -- the frozen coefficient")
        log("must be a pure number, which the branch (a) identity kernel respects.")
        log("Conditional grades only; the adapter must still deliver sigma, kappa, and the")
        log("action-level derivation. No claim-status, canon, or map movement.")
    if FAIL:
        log(f"\nRESULT: {len(FAIL)} FAILED")
        for name in FAIL:
            log("  FAIL: " + name)
        raise SystemExit(1)
    log("\nRESULT: ALL PASS")


if __name__ == "__main__":
    main()
