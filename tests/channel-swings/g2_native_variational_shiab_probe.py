#!/usr/bin/env python3
"""Exact G2 transgression and variational-Shiab contract.

The native fourteen-dimensional carrier is tested by the inherited RB1c
probe.  This independent exact 3D transgression fixture tests the universal
field-space calculus that G2 needs:

* A=B+T and F_A=F_B+D_B T+q(T,T);
* the 1/2 and 1/3 coefficients normalize two and three variational slots;
* a cyclic invariant contraction simplifies the Euler covector to S(F_A);
* a moving noncentral contraction does not, while the unsimplified action
  still has an exact slot-symmetrized Euler derivative;
* B is graph-constrained and its moving-contraction response cannot be
  omitted.

All arithmetic uses fractions.  This is not a full Y^14 Green/BV calculation.
"""

from fractions import Fraction as F


def M(a, b, c, d):
    return ((F(a), F(b)), (F(c), F(d)))


ZERO = M(0, 0, 0, 0)
IDENTITY = M(1, 0, 0, 1)


def add(x, y):
    return tuple(tuple(x[i][j] + y[i][j] for j in range(2)) for i in range(2))


def neg(x):
    return tuple(tuple(-entry for entry in row) for row in x)


def sub(x, y):
    return add(x, neg(y))


def scale(c, x):
    c = F(c)
    return tuple(tuple(c * entry for entry in row) for row in x)


def mm(x, y):
    return tuple(
        tuple(sum((x[i][k] * y[k][j] for k in range(2)), F(0)) for j in range(2))
        for i in range(2)
    )


def inv(x):
    determinant = x[0][0] * x[1][1] - x[0][1] * x[1][0]
    assert determinant != 0
    return scale(F(1, 1) / determinant, M(x[1][1], -x[0][1], -x[1][0], x[0][0]))


def tr(x):
    return x[0][0] + x[1][1]


def comm(x, y):
    return sub(mm(x, y), mm(y, x))


def ad(g, x):
    return mm(mm(g, x), inv(g))


def form1(*entries):
    assert len(entries) == 3
    return tuple(entries)


def form2(f01, f02, f12):
    return (f01, f02, f12)


def f1_add(x, y):
    return tuple(add(x[i], y[i]) for i in range(3))


def f1_scale(c, x):
    return tuple(scale(c, x[i]) for i in range(3))


def f2_add(x, y):
    return tuple(add(x[i], y[i]) for i in range(3))


def f2_scale(c, x):
    return tuple(scale(c, x[i]) for i in range(3))


def f2_sub(x, y):
    return f2_add(x, f2_scale(-1, y))


def q(x, y):
    """Symmetric polarization of A wedge A; q(x,x)_ij=[x_i,x_j]."""

    return form2(
        scale(F(1, 2), sub(comm(x[0], y[1]), comm(x[1], y[0]))),
        scale(F(1, 2), sub(comm(x[0], y[2]), comm(x[2], y[0]))),
        scale(F(1, 2), sub(comm(x[1], y[2]), comm(x[2], y[1]))),
    )


def covariant_d(connection, one_form, exterior_d):
    return form2(
        add(exterior_d[0], sub(comm(connection[0], one_form[1]), comm(connection[1], one_form[0]))),
        add(exterior_d[1], sub(comm(connection[0], one_form[2]), comm(connection[2], one_form[0]))),
        add(exterior_d[2], sub(comm(connection[1], one_form[2]), comm(connection[2], one_form[1]))),
    )


def curvature(connection, exterior_d):
    return f2_add(exterior_d, q(connection, connection))


def wedge_pair(one_form, two_form):
    """Integral-density coefficient of ReTr(one_form wedge two_form)."""

    return tr(add(sub(mm(one_form[0], two_form[2]), mm(one_form[1], two_form[1])), mm(one_form[2], two_form[0])))


def star1(one_form):
    """Euclidean 3D density-dual control: x wedge *y=sum tr(x_i y_i)."""

    return form2(one_form[2], neg(one_form[1]), one_form[0])


def inner1(x, y):
    return wedge_pair(x, star1(y))


def shiab_identity(two_form):
    return two_form


def shiab_insert(insertion, two_form):
    return tuple(mm(insertion, entry) for entry in two_form)


def source_curvature(b_conn, d_b, t_form, d_t, a, b):
    return f2_add(
        curvature(b_conn, d_b),
        f2_add(f2_scale(a, covariant_d(b_conn, t_form, d_t)), f2_scale(b, q(t_form, t_form))),
    )


def source_action(b_conn, d_b, t_form, d_t, shiab, kappa, a=F(1, 2), b=F(1, 3)):
    c = source_curvature(b_conn, d_b, t_form, d_t, a, b)
    return wedge_pair(t_form, shiab(c)) + F(kappa, 2) * inner1(t_form, t_form)


def endpoint_action(a_conn, d_a, b_conn, d_b, shiab, kappa):
    t_form = f1_add(a_conn, f1_scale(-1, b_conn))
    d_t = f2_sub(d_a, d_b)
    return source_action(b_conn, d_b, t_form, d_t, shiab, kappa)


def richardson_derivative(function, step=F(1)):
    def central(h):
        return (function(h) - function(-h)) / (2 * h)

    return (4 * central(step / 2) - central(step)) / 3


def directional_derivative(b_conn, d_b, t_form, d_t, delta, d_delta, shiab, kappa, a=F(1, 2), b=F(1, 3)):
    c = source_curvature(b_conn, d_b, t_form, d_t, a, b)
    dc = f2_add(
        f2_scale(a, covariant_d(b_conn, delta, d_delta)),
        f2_scale(2 * b, q(t_form, delta)),
    )
    return wedge_pair(delta, shiab(c)) + wedge_pair(t_form, shiab(dc)) + kappa * inner1(delta, t_form)


def slot_symmetrized_derivative(b_conn, d_b, t_form, d_t, delta, d_delta, shiab, kappa):
    f_b = curvature(b_conn, d_b)
    d_t_cov = covariant_d(b_conn, t_form, d_t)
    d_delta_cov = covariant_d(b_conn, delta, d_delta)

    linear = wedge_pair(delta, shiab(f_b))
    quadratic = F(1, 2) * (
        wedge_pair(delta, shiab(d_t_cov)) + wedge_pair(t_form, shiab(d_delta_cov))
    )
    cubic = F(1, 3) * (
        wedge_pair(delta, shiab(q(t_form, t_form)))
        + 2 * wedge_pair(t_form, shiab(q(delta, t_form)))
    )
    return linear + quadratic + cubic + kappa * inner1(delta, t_form)


def simplified_source_derivative(b_conn, d_b, t_form, d_t, delta, shiab, kappa):
    a_conn = f1_add(b_conn, t_form)
    d_a = f2_add(d_b, d_t)
    return wedge_pair(delta, shiab(curvature(a_conn, d_a))) + kappa * inner1(delta, t_form)


def transform_f1(g, x):
    return tuple(ad(g, entry) for entry in x)


def transform_f2(g, x):
    return tuple(ad(g, entry) for entry in x)


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
    b_conn = form1(M(1, 1, 0, -1), M(0, 1, 2, 1), M(2, -1, 1, 0))
    t_form = form1(M(0, 2, -1, 1), M(1, -1, 1, 2), M(-1, 0, 2, 1))
    delta = form1(M(2, 0, 1, -1), M(-1, 2, 0, 1), M(1, 1, -2, 0))
    d_b = form2(M(0, 1, -1, 0), M(1, 0, 2, -1), M(-1, 2, 0, 1))
    # The cyclic/transgression fixture uses covariantly constant exterior
    # directions; nonzero dB retains a nontrivial background curvature.
    d_t = form2(ZERO, ZERO, ZERO)
    d_delta = form2(ZERO, ZERO, ZERO)
    kappa = F(5, 3)

    # Endpoint identity underlying the source completion.
    a_conn = f1_add(b_conn, t_form)
    d_a = f2_add(d_b, d_t)
    translated = f2_add(
        curvature(b_conn, d_b),
        f2_add(covariant_d(b_conn, t_form, d_t), q(t_form, t_form)),
    )
    exact("translated curvature", curvature(a_conn, d_a) == translated)

    # Positive Chern--Simons control: invariant trace and identity contraction.
    analytic_cyclic = directional_derivative(
        b_conn, d_b, t_form, d_t, delta, d_delta, shiab_identity, kappa
    )
    finite_cyclic = richardson_derivative(
        lambda s: source_action(
            b_conn,
            d_b,
            f1_add(t_form, f1_scale(s, delta)),
            f2_add(d_t, f2_scale(s, d_delta)),
            shiab_identity,
            kappa,
        )
    )
    exact("cyclic action exact derivative", analytic_cyclic == finite_cyclic)
    exact(
        "cyclic source simplification",
        analytic_cyclic
        == simplified_source_derivative(b_conn, d_b, t_form, d_t, delta, shiab_identity, kappa),
    )

    # A moving noncentral insertion is the finite analogue of the native
    # epsilon/trace-adapted contraction.  It is covariant, but not cyclic.
    insertion = M(1, 2, -1, 0)
    shiab_moving = lambda two_form: shiab_insert(insertion, two_form)
    analytic_moving = directional_derivative(
        b_conn, d_b, t_form, d_t, delta, d_delta, shiab_moving, kappa
    )
    finite_moving = richardson_derivative(
        lambda s: source_action(
            b_conn,
            d_b,
            f1_add(t_form, f1_scale(s, delta)),
            d_t,
            shiab_moving,
            kappa,
        )
    )
    exact("noncyclic action exact derivative", analytic_moving == finite_moving)
    exact(
        "slot-symmetrized Euler geometry",
        analytic_moving
        == slot_symmetrized_derivative(
            b_conn, d_b, t_form, d_t, delta, d_delta, shiab_moving, kappa
        ),
    )
    planted(
        "noncyclic source simplification",
        analytic_moving
        == simplified_source_derivative(b_conn, d_b, t_form, d_t, delta, shiab_moving, kappa),
    )

    # The source coefficients normalize slots. Wrong values remain perfectly
    # differentiable but do not equal the canonical 2/3-slot symmetrization.
    wrong_linear = directional_derivative(
        b_conn, d_b, t_form, d_t, delta, d_delta, shiab_moving, kappa, a=F(1), b=F(1, 3)
    )
    wrong_quadratic = directional_derivative(
        b_conn, d_b, t_form, d_t, delta, d_delta, shiab_moving, kappa, a=F(1, 2), b=F(1, 2)
    )
    planted("wrong 1/2 slot normalization", wrong_linear == analytic_moving)
    planted("wrong 1/3 slot normalization", wrong_quadratic == analytic_moving)

    # Constant gauge covariance requires the insertion to move.  Freezing it
    # is the exact analogue of freezing epsilon/reference data.
    g = M(1, 1, -1, 2)
    b_g = transform_f1(g, b_conn)
    t_g = transform_f1(g, t_form)
    db_g = transform_f2(g, d_b)
    insertion_g = ad(g, insertion)
    action_native = source_action(b_conn, d_b, t_form, d_t, shiab_moving, kappa)
    action_moved = source_action(
        b_g,
        db_g,
        t_g,
        d_t,
        lambda two_form: shiab_insert(insertion_g, two_form),
        kappa,
    )
    exact("moving-insertion covariance", action_native == action_moved)
    planted(
        "frozen-insertion covariance",
        action_native
        == source_action(
            b_g,
            db_g,
            t_g,
            d_t,
            lambda two_form: shiab_insert(insertion, two_form),
            kappa,
        ),
    )

    # Endpoint graph calculus: T=A-B. B variation at fixed A must carry
    # delta T=-delta B. Treating B as an independent endpoint creates a
    # different, nonzero equation.
    graph_direction = form1(M(1, -1, 0, 2), M(0, 1, -2, 1), M(2, 0, 1, -1))
    d_graph = form2(ZERO, ZERO, ZERO)
    base_endpoint = endpoint_action(a_conn, d_a, b_conn, d_b, shiab_moving, kappa)
    exact("endpoint action equals B+T action", base_endpoint == action_native)

    graph_derivative = richardson_derivative(
        lambda s: endpoint_action(
            a_conn,
            d_a,
            f1_add(b_conn, f1_scale(s, graph_direction)),
            f2_add(d_b, f2_scale(s, d_graph)),
            shiab_moving,
            kappa,
        )
    )
    partial_b_fixed_t = richardson_derivative(
        lambda s: source_action(
            f1_add(b_conn, f1_scale(s, graph_direction)),
            f2_add(d_b, f2_scale(s, d_graph)),
            t_form,
            d_t,
            shiab_moving,
            kappa,
        )
    )
    partial_t_minus = directional_derivative(
        b_conn,
        d_b,
        t_form,
        d_t,
        f1_scale(-1, graph_direction),
        f2_scale(-1, d_graph),
        shiab_moving,
        kappa,
    )
    exact("graph chain rule", graph_derivative == partial_b_fixed_t + partial_t_minus)
    planted("omit T=A-B graph response", graph_derivative == partial_b_fixed_t)
    planted("independent B equation vanishes", partial_b_fixed_t == 0)

    # Epsilon also moves the contraction. Its explicit response is exact and
    # nonzero on the chosen fixture.
    chi = M(0, 1, -1, 0)
    delta_insertion = comm(chi, insertion)
    insertion_response = wedge_pair(
        t_form,
        shiab_insert(delta_insertion, source_curvature(b_conn, d_b, t_form, d_t, F(1, 2), F(1, 3))),
    )
    exact("moving-Shiab epsilon response is live", insertion_response != 0)
    planted("epsilon response may be omitted", insertion_response == 0)

    # A zero polarized curvature does not force a zero slot-symmetrized Euler
    # response for a noncyclic insertion, blocking a fake linear factorization.
    y = form1(M(1, 0, 0, 0), ZERO, ZERO)
    z = form1(ZERO, M(0, 0, 0, 1), ZERO)
    # These diagonal matrices commute, so q(y,z)=0.
    exact("zero polarized curvature plant", q(y, z) == form2(ZERO, ZERO, ZERO))
    factorization_witness = F(1, 3) * (
        wedge_pair(delta, shiab_insert(insertion, q(y, z)))
        + wedge_pair(y, shiab_insert(insertion, q(delta, z)))
        + wedge_pair(z, shiab_insert(insertion, q(delta, y)))
    )
    exact("polarized Euler response need not factor through curvature", factorization_witness != 0)
    planted("one linear S of polarized curvature represents the Euler map", factorization_witness == 0)

    # Ensure the action and its two principal branch responses are nonvacuous.
    exact("source action nonzero", action_native != 0)
    exact("cyclic and moving contractions differ", analytic_cyclic != analytic_moving)
    planted("density degree may be omitted", wedge_pair(t_form, form2(ZERO, ZERO, ZERO)) == action_native)

    print(
        "G2-NATIVE-VARIATIONAL-SHIAB: "
        f"{exact_checks} exact checks + {planted_checks} planted failures = "
        f"{exact_checks + planted_checks} PASS"
    )
    print("RESULT: 1/2 and 1/3 normalize two- and three-slot action variations")
    print("RESULT: fixed-linear Shiab simplification needs cyclicity and fails for a moving noncentral insertion")
    print("RESULT: the unsimplified slot-symmetrized Euler geometry remains exact and graph-covariant")
    print("BOUNDARY: finite transgression calculus; no full Y14 Green/BV, VEV, index, count, or PP3")


if __name__ == "__main__":
    main()
