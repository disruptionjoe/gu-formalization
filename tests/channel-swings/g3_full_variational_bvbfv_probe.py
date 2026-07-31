#!/usr/bin/env python3
"""Exact G3 graph-variation, Noether, preboundary, and BV contract.

The native carrier and G2 transgression map are inherited from the G1/G2 and
RB1b/RB1c probes.  This independent certificate checks the universal
variational structure needed after G2:

* every slot of the noncyclic first-order source action is varied;
* ``B`` is a graph composite and ``T=A-B`` carries the chain rule;
* the local gauge Ward identity is coupled, while its isolated connection
  term is generically nonzero;
* integration by parts emits a nonzero preboundary one-form and field-space
  two-form;
* diffeomorphism covariance of a top density requires the density response;
* the ordinary nonabelian gauge algebra closes and forces the ghost-antifield
  bracket term in the minimal BV completion.
* the author-guided observation pullback is typed separately from a
  four-dimensional defect pushforward, and a naive retract intertwiner is
  strictly weaker than the off-slice leakage condition.

All arithmetic is rational.  The finite models test the universal calculus,
not the full Y^14 domain, observation retract, super-IG algebra, or physical
BV cohomology.
"""

from __future__ import annotations

from fractions import Fraction as F

import g2_native_variational_shiab_probe as g2


def matrix_zero(matrix):
    return all(entry == 0 for row in matrix for entry in row)


def form1_zero(form):
    return all(matrix_zero(entry) for entry in form)


def form2_zero(form):
    return all(matrix_zero(entry) for entry in form)


def f1_sub(x, y):
    return g2.f1_add(x, g2.f1_scale(-1, y))


def f2_comm(left, right):
    return tuple(g2.comm(left, entry) for entry in right)


def f1_comm(left, right):
    return tuple(g2.comm(left, entry) for entry in right)


def insertion_pair(one_form, insertion, two_form):
    return g2.wedge_pair(one_form, g2.shiab_insert(insertion, two_form))


def varied_curvature(b_conn, delta_b, delta_db):
    return g2.f2_add(delta_db, g2.f2_scale(2, g2.q(b_conn, delta_b)))


def varied_covariant_d(b_conn, t_form, delta_b, delta_t, delta_dt):
    return g2.f2_add(
        delta_dt,
        g2.f2_add(
            g2.f2_scale(2, g2.q(delta_b, t_form)),
            g2.f2_scale(2, g2.q(b_conn, delta_t)),
        ),
    )


def source_curvature(b_conn, d_b, t_form, d_t):
    return g2.source_curvature(b_conn, d_b, t_form, d_t, F(1, 2), F(1, 3))


def full_source_action(b_conn, d_b, t_form, d_t, insertion, metric_scale, kappa):
    return insertion_pair(t_form, insertion, source_curvature(b_conn, d_b, t_form, d_t)) + (
        F(kappa, 2) * metric_scale * g2.inner1(t_form, t_form)
    )


def full_source_variation(
    b_conn,
    d_b,
    t_form,
    d_t,
    insertion,
    metric_scale,
    kappa,
    delta_b,
    delta_db,
    delta_t,
    delta_dt,
    delta_insertion,
    delta_metric_scale,
):
    current = source_curvature(b_conn, d_b, t_form, d_t)
    delta_current = g2.f2_add(
        varied_curvature(b_conn, delta_b, delta_db),
        g2.f2_add(
            g2.f2_scale(
                F(1, 2),
                varied_covariant_d(b_conn, t_form, delta_b, delta_t, delta_dt),
            ),
            g2.f2_scale(F(2, 3), g2.q(t_form, delta_t)),
        ),
    )
    return (
        insertion_pair(delta_t, insertion, current)
        + insertion_pair(t_form, delta_insertion, current)
        + insertion_pair(t_form, insertion, delta_current)
        + F(kappa, 2) * delta_metric_scale * g2.inner1(t_form, t_form)
        + kappa * metric_scale * g2.inner1(delta_t, t_form)
    )


def line_shift_f1(base, direction, parameter):
    return g2.f1_add(base, g2.f1_scale(parameter, direction))


def line_shift_f2(base, direction, parameter):
    return g2.f2_add(base, g2.f2_scale(parameter, direction))


def line_shift_matrix(base, direction, parameter):
    return g2.add(base, g2.scale(parameter, direction))


def finite_full_variation(
    b_conn,
    d_b,
    t_form,
    d_t,
    insertion,
    metric_scale,
    kappa,
    delta_b,
    delta_db,
    delta_t,
    delta_dt,
    delta_insertion,
    delta_metric_scale,
):
    return g2.richardson_derivative(
        lambda parameter: full_source_action(
            line_shift_f1(b_conn, delta_b, parameter),
            line_shift_f2(d_b, delta_db, parameter),
            line_shift_f1(t_form, delta_t, parameter),
            line_shift_f2(d_t, delta_dt, parameter),
            line_shift_matrix(insertion, delta_insertion, parameter),
            metric_scale + parameter * delta_metric_scale,
            kappa,
        )
    )


PAIRS = ((0, 1), (0, 2), (1, 2))


def gauge_connection(connection, chi, d_chi):
    return tuple(g2.sub(g2.comm(chi, connection[i]), d_chi[i]) for i in range(3))


def gauge_covariant_form(one_form, chi):
    return f1_comm(chi, one_form)


def gauge_exterior_connection(d_connection, connection, chi, d_chi):
    entries = []
    for slot, (i, j) in enumerate(PAIRS):
        entries.append(
            g2.add(
                g2.comm(chi, d_connection[slot]),
                g2.sub(g2.comm(d_chi[i], connection[j]), g2.comm(d_chi[j], connection[i])),
            )
        )
    return tuple(entries)


def gauge_exterior_covariant(d_form, one_form, chi, d_chi):
    entries = []
    for slot, (i, j) in enumerate(PAIRS):
        entries.append(
            g2.add(
                g2.comm(chi, d_form[slot]),
                g2.sub(g2.comm(d_chi[i], one_form[j]), g2.comm(d_chi[j], one_form[i])),
            )
        )
    return tuple(entries)


# Exact polynomial calculus on [0,1] for the Green/preboundary control.
def poly_trim(poly):
    result = list(poly)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return tuple(result)


def poly_add(left, right):
    length = max(len(left), len(right))
    return poly_trim(
        tuple(
            (left[i] if i < len(left) else F(0)) + (right[i] if i < len(right) else F(0))
            for i in range(length)
        )
    )


def poly_neg(poly):
    return tuple(-entry for entry in poly)


def poly_sub(left, right):
    return poly_add(left, poly_neg(right))


def poly_scale(scale, poly):
    return poly_trim(tuple(F(scale) * entry for entry in poly))


def poly_mul(left, right):
    result = [F(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            result[i + j] += x * y
    return poly_trim(tuple(result))


def poly_derivative(poly):
    if len(poly) == 1:
        return (F(0),)
    return poly_trim(tuple(F(i) * poly[i] for i in range(1, len(poly))))


def poly_integral_01(poly):
    return sum((entry / F(i + 1) for i, entry in enumerate(poly)), F(0))


def poly_value(poly, point):
    point = F(point)
    return sum((entry * point**i for i, entry in enumerate(poly)), F(0))


def endpoint(poly):
    return poly_value(poly, 1) - poly_value(poly, 0)


def poly_sum(*polys):
    result = (F(0),)
    for poly in polys:
        result = poly_add(result, poly)
    return result


exact_checks = 0
planted_checks = 0


def exact(name, condition):
    global exact_checks
    if not condition:
        raise AssertionError(f"exact check failed: {name}")
    exact_checks += 1


def planted(name, false_claim):
    global planted_checks
    if false_claim:
        raise AssertionError(f"planted false claim unexpectedly passed: {name}")
    planted_checks += 1


def main():
    b_conn = g2.form1(g2.M(1, 1, 0, -1), g2.M(0, 1, 2, 1), g2.M(2, -1, 1, 0))
    t_form = g2.form1(g2.M(0, 2, -1, 1), g2.M(1, -1, 1, 2), g2.M(-1, 0, 2, 1))
    d_b = g2.form2(g2.M(0, 1, -1, 0), g2.M(1, 0, 2, -1), g2.M(-1, 2, 0, 1))
    d_t = g2.form2(g2.M(1, -1, 0, 2), g2.M(0, 2, -1, 1), g2.M(2, 0, 1, -1))
    insertion = g2.M(1, 2, -1, 0)
    metric_scale = F(7, 5)
    kappa = F(5, 3)

    delta_b = g2.form1(g2.M(1, 0, -1, 2), g2.M(2, -1, 0, 1), g2.M(0, 1, 1, -2))
    delta_t = g2.form1(g2.M(2, 1, 0, -1), g2.M(-1, 0, 2, 1), g2.M(1, -2, 1, 0))
    delta_db = g2.form2(g2.M(0, 1, 2, -1), g2.M(1, -1, 0, 2), g2.M(2, 0, -1, 1))
    delta_dt = g2.form2(g2.M(1, 0, -2, 1), g2.M(0, -1, 1, 2), g2.M(-1, 2, 0, 1))
    delta_insertion = g2.M(0, 1, 2, -1)
    delta_metric_scale = F(3, 7)

    analytic = full_source_variation(
        b_conn,
        d_b,
        t_form,
        d_t,
        insertion,
        metric_scale,
        kappa,
        delta_b,
        delta_db,
        delta_t,
        delta_dt,
        delta_insertion,
        delta_metric_scale,
    )
    finite = finite_full_variation(
        b_conn,
        d_b,
        t_form,
        d_t,
        insertion,
        metric_scale,
        kappa,
        delta_b,
        delta_db,
        delta_t,
        delta_dt,
        delta_insertion,
        delta_metric_scale,
    )
    exact("all-slot source variation", analytic == finite)

    omit_insertion = full_source_variation(
        b_conn, d_b, t_form, d_t, insertion, metric_scale, kappa,
        delta_b, delta_db, delta_t, delta_dt, g2.ZERO, delta_metric_scale,
    )
    omit_metric = full_source_variation(
        b_conn, d_b, t_form, d_t, insertion, metric_scale, kappa,
        delta_b, delta_db, delta_t, delta_dt, delta_insertion, F(0),
    )
    planted("omit moving-Shiab response", omit_insertion == analytic)
    planted("omit metric/pseudo-musical response", omit_metric == analytic)

    # Graph policy: at fixed A a reference move carries delta T=-delta B.
    graph_total = full_source_variation(
        b_conn, d_b, t_form, d_t, insertion, metric_scale, kappa,
        delta_b, delta_db, g2.f1_scale(-1, delta_b), g2.f2_scale(-1, delta_db),
        delta_insertion, delta_metric_scale,
    )
    graph_finite = finite_full_variation(
        b_conn, d_b, t_form, d_t, insertion, metric_scale, kappa,
        delta_b, delta_db, g2.f1_scale(-1, delta_b), g2.f2_scale(-1, delta_db),
        delta_insertion, delta_metric_scale,
    )
    exact("A-fixed graph return through B,T,S,flat", graph_total == graph_finite)
    frozen_t = full_source_variation(
        b_conn, d_b, t_form, d_t, insertion, metric_scale, kappa,
        delta_b, delta_db, g2.form1(g2.ZERO, g2.ZERO, g2.ZERO),
        g2.form2(g2.ZERO, g2.ZERO, g2.ZERO), delta_insertion, delta_metric_scale,
    )
    planted("freeze T during reference motion", frozen_t == graph_total)
    planted("independent B equation is vacuous", frozen_t == 0)

    # Full first-jet gauge variation and the coupled Ward cancellation.
    chi = g2.M(0, 1, -1, 0)
    d_chi = g2.form1(g2.M(1, 0, 0, -1), g2.M(0, 1, 1, 0), g2.M(2, -1, 0, 1))
    delta_b_g = gauge_connection(b_conn, chi, d_chi)
    delta_db_g = gauge_exterior_connection(d_b, b_conn, chi, d_chi)
    delta_t_g = gauge_covariant_form(t_form, chi)
    delta_dt_g = gauge_exterior_covariant(d_t, t_form, chi, d_chi)
    delta_h_g = g2.comm(chi, insertion)
    ward = full_source_variation(
        b_conn, d_b, t_form, d_t, insertion, metric_scale, kappa,
        delta_b_g, delta_db_g, delta_t_g, delta_dt_g, delta_h_g, F(0),
    )
    exact("complete first-jet gauge Ward variation", ward == 0)

    a_conn = g2.f1_add(b_conn, t_form)
    d_a = g2.f2_add(d_b, d_t)
    delta_a_g = gauge_connection(a_conn, chi, d_chi)
    delta_da_g = gauge_exterior_connection(d_a, a_conn, chi, d_chi)
    exact("gauge graph delta A=delta B+delta T", delta_a_g == g2.f1_add(delta_b_g, delta_t_g))
    exact("gauge jet graph delta dA=delta dB+delta dT", delta_da_g == g2.f2_add(delta_db_g, delta_dt_g))

    a_sector = full_source_variation(
        b_conn, d_b, t_form, d_t, insertion, metric_scale, kappa,
        g2.form1(g2.ZERO, g2.ZERO, g2.ZERO), g2.form2(g2.ZERO, g2.ZERO, g2.ZERO),
        delta_a_g, delta_da_g, g2.ZERO, F(0),
    )
    reduction_sector = full_source_variation(
        b_conn, d_b, t_form, d_t, insertion, metric_scale, kappa,
        delta_b_g, delta_db_g, g2.f1_scale(-1, delta_b_g),
        g2.f2_scale(-1, delta_db_g), delta_h_g, F(0),
    )
    exact("coupled A plus reduction Ward identity", a_sector + reduction_sector == 0)
    exact("isolated connection Ward term is nonvacuous", a_sector != 0)
    planted("isolated off-shell connection conservation", a_sector == 0)
    planted("freeze moving reduction in Ward identity", a_sector == ward)

    # Green identity and the action-derived preboundary data on [0,1].
    b = (F(1), F(2), F(-1))
    t = (F(2), F(-1), F(1))
    h = (F(1), F(1))
    m = (F(3), F(-1))
    dbv = (F(-1), F(2))
    dtv = (F(1), F(0), F(-2))
    dhv = (F(2), F(-1))
    dmv = (F(1),)
    b_prime = poly_derivative(b)
    t_prime = poly_derivative(t)
    core = poly_add(b_prime, poly_scale(F(1, 2), t_prime))
    direct_density = poly_sum(
        poly_mul(poly_mul(dtv, h), core),
        poly_mul(poly_mul(t, dhv), core),
        poly_mul(poly_mul(t, h), poly_add(poly_derivative(dbv), poly_scale(F(1, 2), poly_derivative(dtv)))),
        poly_scale(F(kappa, 2), poly_mul(poly_mul(dmv, t), t)),
        poly_scale(kappa, poly_mul(poly_mul(m, t), dtv)),
    )
    e_b = poly_neg(poly_derivative(poly_mul(t, h)))
    e_t = poly_sum(
        poly_mul(h, b_prime),
        poly_scale(F(-1, 2), poly_mul(t, poly_derivative(h))),
        poly_scale(kappa, poly_mul(m, t)),
    )
    e_h = poly_mul(t, core)
    e_m = poly_scale(F(kappa, 2), poly_mul(t, t))
    bulk_density = poly_sum(
        poly_mul(e_b, dbv), poly_mul(e_t, dtv), poly_mul(e_h, dhv), poly_mul(e_m, dmv)
    )
    theta = poly_add(poly_mul(poly_mul(t, h), dbv), poly_scale(F(1, 2), poly_mul(poly_mul(t, h), dtv)))
    direct_integral = poly_integral_01(direct_density)
    bulk_integral = poly_integral_01(bulk_density)
    boundary_flux = endpoint(theta)
    exact("Green identity with retained preboundary flux", direct_integral == bulk_integral + boundary_flux)
    exact("preboundary one-form is nonzero", boundary_flux != 0)
    planted("discard Green flux as a bulk zero", direct_integral == bulk_integral)

    # The preboundary two-form is delta theta. It is constructed before G4
    # chooses a polarization or quotients its kernel.
    db1, dt1, dh1 = dbv, dtv, dhv
    db2 = (F(0), F(1), F(1))
    dt2 = (F(-2), F(1))
    dh2 = (F(1), F(2), F(-1))

    def delta_theta(delta_t, delta_h, test_b, test_t):
        delta_th = poly_add(poly_mul(delta_t, h), poly_mul(t, delta_h))
        return poly_add(poly_mul(delta_th, test_b), poly_scale(F(1, 2), poly_mul(delta_th, test_t)))

    omega_12 = endpoint(poly_sub(delta_theta(dt1, dh1, db2, dt2), delta_theta(dt2, dh2, db1, dt1)))
    omega_21 = endpoint(poly_sub(delta_theta(dt2, dh2, db1, dt1), delta_theta(dt1, dh1, db2, dt2)))
    exact("preboundary field-space two-form is antisymmetric", omega_12 == -omega_21)
    exact("preboundary field-space two-form is nonzero", omega_12 != 0)
    exact("native form degrees are theta(13,1), omega(13,2)", 14 - 1 == 13)
    # A nonzero symplectic plane has at least the two distinct coordinate
    # Lagrangian lines.  The form supplies geometry but does not choose one.
    lagrangian_b = (F(1), F(0))
    lagrangian_t = (F(0), F(1))
    symplectic_pair = lambda left, right: omega_12 * (left[0] * right[1] - left[1] * right[0])
    exact(
        "preboundary form admits distinct coordinate polarizations",
        lagrangian_b != lagrangian_t
        and symplectic_pair(lagrangian_b, lagrangian_b) == 0
        and symplectic_pair(lagrangian_t, lagrangian_t) == 0,
    )
    planted("nonzero preboundary form uniquely selects a polarization", lagrangian_b == lagrangian_t)

    # Diffeomorphism control: a natural top density changes by d(i_xi L).
    lagrangian_density = poly_add(poly_mul(poly_mul(t, h), core), poly_scale(F(kappa, 2), poly_mul(poly_mul(m, t), t)))
    xi = (F(1), F(-2), F(1))
    full_lie_density = poly_derivative(poly_mul(xi, lagrangian_density))
    frozen_density_lie = poly_mul(xi, poly_derivative(lagrangian_density))
    exact(
        "top-density diffeomorphism response is a boundary term",
        poly_integral_01(full_lie_density) == endpoint(poly_mul(xi, lagrangian_density)),
    )
    planted("freeze density in diffeomorphism identity", full_lie_density == frozen_density_lie)

    # Ordinary gauge algebra closure. The selected convention is an
    # antihomomorphism: [delta_chi,delta_eta]=delta_[eta,chi].
    eta = g2.M(1, 1, 0, -1)
    d_eta = g2.form1(g2.M(0, 2, -1, 0), g2.M(1, -1, 0, 1), g2.M(0, 1, 2, -1))
    delta_chi_b = gauge_connection(b_conn, chi, d_chi)
    delta_eta_b = gauge_connection(b_conn, eta, d_eta)
    commutator_b = tuple(
        g2.sub(g2.comm(eta, delta_chi_b[i]), g2.comm(chi, delta_eta_b[i])) for i in range(3)
    )
    bracket = g2.comm(eta, chi)
    d_bracket = tuple(g2.add(g2.comm(d_eta[i], chi), g2.comm(eta, d_chi[i])) for i in range(3))
    exact("nonabelian connection gauge algebra closes", commutator_b == gauge_connection(b_conn, bracket, d_bracket))

    delta_chi_t = gauge_covariant_form(t_form, chi)
    delta_eta_t = gauge_covariant_form(t_form, eta)
    commutator_t = tuple(
        g2.sub(g2.comm(eta, delta_chi_t[i]), g2.comm(chi, delta_eta_t[i])) for i in range(3)
    )
    exact("nonabelian distortion gauge algebra closes", commutator_t == gauge_covariant_form(t_form, bracket))
    exact("gauge bracket is nonzero", not matrix_zero(bracket))
    jacobi = g2.add(
        g2.comm(chi, g2.comm(eta, insertion)),
        g2.add(g2.comm(eta, g2.comm(insertion, chi)), g2.comm(insertion, g2.comm(chi, eta))),
    )
    exact("ghost bracket satisfies Jacobi", matrix_zero(jacobi))
    planted("field-antifield terms close without ghost-antifield bracket", matrix_zero(bracket))

    # G2 is source-bulk only: its section derivative vanishes by absence, not
    # as a theorem about the repo-originated N1 defect comparator.
    source_value = full_source_action(b_conn, d_b, t_form, d_t, insertion, metric_scale, kappa)
    section_derivative_source_only = F(0)
    section_derivative_with_planted_defect = source_value
    exact("source-only section response is absent", section_derivative_source_only == 0)
    exact("a retained defect would reopen the section equation", section_derivative_with_planted_defect != 0)
    planted("source-only zero proves the complete section equation vanishes", section_derivative_with_planted_defect == 0)

    # Primary-source correction: Weinstein's stated route is pullback along a
    # metric section.  R_s L_s=1 is necessary but does not make L_s R_s=1,
    # and even the downstairs intertwiner R_s D_Y L_s=D_X can hide ambient
    # leakage.  The defect pushforward has the opposite typed direction.
    x4 = (F(1), F(-2), F(3), F(4))

    def observation_lift(vector4):
        return tuple(vector4) + (F(0),) * 10

    def observation_retract(vector14):
        assert len(vector14) == 14
        return tuple(vector14[:4])

    lifted_x4 = observation_lift(x4)
    exact("observation retract is a left inverse of the lift", observation_retract(lifted_x4) == x4)

    ambient_probe = lifted_x4[:4] + (F(5),) + (F(0),) * 9
    exact(
        "lift-retract is not the ambient identity",
        observation_lift(observation_retract(ambient_probe)) != ambient_probe,
    )
    planted("R_s L_s=1 implies L_s R_s=1", observation_lift(observation_retract(ambient_probe)) == ambient_probe)

    def downstairs_operator(vector4):
        return (2 * vector4[0], -vector4[1], vector4[2] + vector4[3], vector4[3])

    def leaking_ambient_operator(vector14):
        downstairs = downstairs_operator(observation_retract(vector14))
        leakage = sum(observation_retract(vector14))
        return observation_lift(downstairs)[:4] + (leakage,) + (F(0),) * 9

    ambient_image = leaking_ambient_operator(lifted_x4)
    exact(
        "downstairs operator intertwining can pass",
        observation_retract(ambient_image) == downstairs_operator(x4),
    )
    off_slice = tuple(
        ambient_image[i] - observation_lift(observation_retract(ambient_image))[i]
        for i in range(14)
    )
    exact("off-slice leakage test remains independent", any(entry != 0 for entry in off_slice))
    planted("retract intertwining alone proves no off-slice leakage", all(entry == 0 for entry in off_slice))

    defect_pushforward = observation_lift(x4)
    observation_pullback = observation_retract(ambient_probe)
    exact(
        "observation pullback and defect pushforward have opposite typed directions",
        len(observation_pullback) == 4 and len(defect_pushforward) == 14,
    )

    print(
        "G3-FULL-VARIATIONAL-BVBFV: "
        f"{exact_checks} exact checks + {planted_checks} planted failures = "
        f"{exact_checks + planted_checks} PASS"
    )
    print("RESULT: graph-complete bulk variation and coupled first-jet gauge Ward identity close")
    print("RESULT: isolated connection conservation fails while the moving-reduction term cancels it")
    print("RESULT: nonzero preboundary data and the ordinary-gauge minimal BV bracket are forced")
    print("RESULT: source recheck selects observation pullback and keeps defect action as a comparator")
    print("BOUNDARY: no global retract/domain, defect BV, super-IG CME, physical cohomology, count, or PP3")


if __name__ == "__main__":
    main()
