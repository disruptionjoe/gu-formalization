#!/usr/bin/env python3
"""Exact G1 probe for the derivative cocycle and moving reference.

This is a one-coordinate jet fixture, not a discretization of Y^14.  A gauge
transformation is represented at one point by `(g, dg)`, so the probe can
distinguish a genuine connection cocycle from the zero-jet E0 shadow.  It also
checks an exact reductive moving-reference construction, local-lift descent,
patch/gauge covariance, tilted reduction and stabilizers, right-H linearity,
and preservation of the trace-reversed metric-fibre form.
"""

from fractions import Fraction as F


def matrix(rows):
    return tuple(tuple(F(x) for x in row) for row in rows)


def zero(n):
    return matrix([[0] * n for _ in range(n)])


def identity(n):
    return matrix([[1 if i == j else 0 for j in range(n)] for i in range(n)])


def add(x, y):
    return tuple(
        tuple(x[i][j] + y[i][j] for j in range(len(x[0])))
        for i in range(len(x))
    )


def neg(x):
    return tuple(tuple(-entry for entry in row) for row in x)


def sub(x, y):
    return add(x, neg(y))


def scale(c, x):
    c = F(c)
    return tuple(tuple(c * entry for entry in row) for row in x)


def transpose(x):
    return tuple(tuple(x[j][i] for j in range(len(x))) for i in range(len(x[0])))


def mm(x, y):
    return tuple(
        tuple(
            sum((x[i][k] * y[k][j] for k in range(len(y))), F(0))
            for j in range(len(y[0]))
        )
        for i in range(len(x))
    )


def inverse_2(x):
    determinant = x[0][0] * x[1][1] - x[0][1] * x[1][0]
    assert determinant != 0
    return scale(
        F(1, 1) / determinant,
        matrix([[x[1][1], -x[0][1]], [-x[1][0], x[0][0]]]),
    )


def determinant(x):
    """Exact determinant by fraction-preserving elimination."""

    work = [list(row) for row in x]
    result = F(1)
    for column in range(len(work)):
        pivot = next((row for row in range(column, len(work)) if work[row][column] != 0), None)
        if pivot is None:
            return F(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            result = -result
        pivot_value = work[column][column]
        result *= pivot_value
        for row in range(column + 1, len(work)):
            multiplier = work[row][column] / pivot_value
            for entry in range(column + 1, len(work)):
                work[row][entry] -= multiplier * work[column][entry]
    return result


def positive_definite(x):
    return all(determinant(tuple(row[:size] for row in x[:size])) > 0 for size in range(1, len(x) + 1))


def ad(g, x):
    return mm(mm(g, x), inverse_2(g))


# A one-coordinate first jet `(value, derivative)`.
def jet_mul(x, y):
    g, dg = x
    h, dh = y
    return mm(g, h), add(mm(dg, h), mm(g, dh))


def jet_inv(x):
    g, dg = x
    gi = inverse_2(g)
    return gi, neg(mm(mm(gi, dg), gi))


def jet_conjugate(k, g):
    return jet_mul(jet_mul(k, g), jet_inv(k))


def gauge_action(g_jet, connection):
    """Left convention: g.A = Ad_g A - (dg)g^-1."""

    g, dg = g_jet
    return sub(ad(g, connection), mm(dg, inverse_2(g)))


def derivative_cocycle(connection, g_jet):
    """q_A(g)=A-g.A=A-Ad_g A+(dg)g^-1."""

    return sub(connection, gauge_action(g_jet, connection))


def zero_jet_shadow(connection, g_jet):
    g, _ = g_jet
    return sub(connection, ad(g, connection))


def ig_mul(x, y):
    g_jet, a = x
    h_jet, b = y
    g, _ = g_jet
    return jet_mul(g_jet, h_jet), add(a, ad(g, b))


def tau(connection, g_jet):
    return g_jet, derivative_cocycle(connection, g_jet)


def theta(connection, omega):
    g_jet, a = omega
    g, _ = g_jet
    return ad(inverse_2(g), sub(a, derivative_cocycle(connection, g_jet)))


def transform_ig(k_jet, omega):
    """Move the reference chart: (g,a) -> (kgk^-1, Ad_k a)."""

    k, _ = k_jet
    g_jet, a = omega
    return jet_conjugate(k_jet, g_jet), ad(k, a)


def project_h(x):
    """Reductive GL(2)/diagonal comparator projection."""

    return matrix([[x[0][0], 0], [0, x[1][1]]])


def induced_reference(background, lift_jet):
    """Gamma^A0_epsilon from the reductive projection in the moving frame."""

    u, du = lift_jet
    ui = inverse_2(u)
    b = add(mm(mm(ui, background), u), mm(ui, du))
    omega_h = project_h(b)
    return sub(mm(mm(u, omega_h), ui), mm(du, ui))


def extended_lc_reference(lift_jet, omega_h):
    """Extend an H-connection through a local lift of the reduction."""

    u, du = lift_jet
    ui = inverse_2(u)
    return sub(mm(mm(u, omega_h), ui), mm(du, ui))


def change_h_connection(h_jet, omega_h):
    """Right lift change u -> uh induces omega -> h^-1 omega h+h^-1 dh."""

    h, dh = h_jet
    hi = inverse_2(h)
    return add(mm(mm(hi, omega_h), h), mm(hi, dh))


def bare_maurer(lift_jet):
    u, du = lift_jet
    return neg(mm(du, inverse_2(u)))


def de_witt(h, k, metric):
    """Trace-reversed Frobenius form on Sym^2 for a Lorentz metric."""

    gi = metric  # chosen metric is diagonal with entries +/-1
    raised_k = mm(mm(gi, k), gi)
    raw = sum((h[i][j] * raised_k[i][j] for i in range(4) for j in range(4)), F(0))
    tr_h = sum((gi[i][j] * h[j][i] for i in range(4) for j in range(4)), F(0))
    tr_k = sum((gi[i][j] * k[j][i] for i in range(4) for j in range(4)), F(0))
    return raw - F(1, 2) * tr_h * tr_k


def sym_action(generator, h):
    return add(mm(transpose(generator), h), mm(h, generator))


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
    i2 = identity(2)
    a_ref = matrix([[2, 1], [3, -1]])
    g_jet = (matrix([[1, 1], [0, 1]]), matrix([[1, 0], [2, -1]]))
    h_jet = (matrix([[2, 0], [1, 1]]), matrix([[0, 1], [-1, 2]]))
    k_jet = (matrix([[1, 0], [-1, 1]]), matrix([[2, -1], [0, 1]]))

    # The derivative-bearing connection cocycle and its planted zero-jet rival.
    gh_jet = jet_mul(g_jet, h_jet)
    g, _ = g_jet
    exact(
        "derivative cocycle",
        derivative_cocycle(a_ref, gh_jet)
        == add(derivative_cocycle(a_ref, g_jet), ad(g, derivative_cocycle(a_ref, h_jet))),
    )
    exact("tilted graph homomorphism", ig_mul(tau(a_ref, g_jet), tau(a_ref, h_jet)) == tau(a_ref, gh_jet))

    nonzero_derivative = matrix([[0, 1], [-1, 0]])
    pure_jet = (i2, nonzero_derivative)
    exact("jet plant sees dg", derivative_cocycle(a_ref, pure_jet) == nonzero_derivative)
    planted("zero-jet shadow sees dg", zero_jet_shadow(a_ref, pure_jet) != zero(2))
    planted("full cocycle equals zero-jet shadow", derivative_cocycle(a_ref, g_jet) == zero_jet_shadow(a_ref, g_jet))

    # Fixed-reference tilted identities survive with the genuine cocycle.
    translation = matrix([[1, 2], [-2, 3]])
    omega = (g_jet, translation)
    th = theta(a_ref, omega)
    exact("left tilted invariance", theta(a_ref, ig_mul(tau(a_ref, k_jet), omega)) == th)
    exact(
        "right tilted adjoint covariance",
        theta(a_ref, ig_mul(omega, tau(a_ref, h_jet))) == ad(inverse_2(h_jet[0]), th),
    )
    planted("raw translation left invariant", ig_mul(tau(a_ref, k_jet), omega)[1] == translation)

    # A moving reference conjugates the entire tilted subgroup and theta map.
    moved_ref = gauge_action(k_jet, a_ref)
    conjugated_g = jet_conjugate(k_jet, g_jet)
    exact(
        "moving-reference cocycle conjugation",
        derivative_cocycle(moved_ref, conjugated_g) == ad(k_jet[0], derivative_cocycle(a_ref, g_jet)),
    )
    exact(
        "moving theta covariance",
        theta(moved_ref, transform_ig(k_jet, omega)) == ad(k_jet[0], th),
    )
    planted(
        "frozen reference patches covariantly",
        derivative_cocycle(a_ref, conjugated_g) == ad(k_jet[0], derivative_cocycle(a_ref, g_jet)),
    )

    # Exact moving reduction/reference construction.
    u_jet = (matrix([[1, 1], [1, 2]]), matrix([[1, -1], [0, 2]]))
    diagonal_h_jet = (matrix([[2, 0], [0, 3]]), matrix([[1, 0], [0, -1]]))
    changed_lift = jet_mul(u_jet, diagonal_h_jet)
    gamma = induced_reference(a_ref, u_jet)
    exact("reductive reference lift descent", induced_reference(a_ref, changed_lift) == gamma)
    planted("bare Maurer-Cartan lift descent", bare_maurer(changed_lift) == bare_maurer(u_jet))

    moved_u = jet_mul(k_jet, u_jet)
    exact(
        "reductive reference gauge covariance",
        induced_reference(moved_ref, moved_u) == gauge_action(k_jet, gamma),
    )
    planted(
        "inert background gauge covariance",
        induced_reference(a_ref, moved_u) == gauge_action(k_jet, gamma),
    )

    # The actual Levi-Civita extension has the same lift law.  Equality with
    # the A0 branch holds only under the explicit compatibility equation.
    u, du = u_jet
    ui = inverse_2(u)
    b = add(mm(mm(ui, a_ref), u), mm(ui, du))
    omega_h = project_h(b)
    omega_h_changed = change_h_connection(diagonal_h_jet, omega_h)
    exact(
        "LC extension lift descent",
        extended_lc_reference(changed_lift, omega_h_changed) == extended_lc_reference(u_jet, omega_h),
    )
    exact("A0-LC compatibility control", extended_lc_reference(u_jet, omega_h) == gamma)
    incompatible_omega = add(omega_h, matrix([[1, 0], [0, 0]]))
    planted("arbitrary reductive reference is Levi-Civita", extended_lc_reference(u_jet, incompatible_omega) == gamma)

    # Canonical left reduction of the double action and stabilizers.
    reduced = ig_mul(tau(a_ref, jet_inv(g_jet)), omega)
    exact("left quotient canonical representative", reduced[0] == (i2, zero(2)) and reduced[1] == th)

    stabilizing_value = add(i2, th)
    if stabilizing_value[0][0] * stabilizing_value[1][1] - stabilizing_value[0][1] * stabilizing_value[1][0] == 0:
        stabilizing_value = sub(scale(2, i2), th)
    stabilizing_h = (stabilizing_value, zero(2))
    exact("chosen adjoint stabilizer", ad(stabilizing_value, th) == th)
    stabilizing_k = jet_mul(jet_mul(g_jet, jet_inv(stabilizing_h)), jet_inv(g_jet))
    fixed = ig_mul(ig_mul(tau(a_ref, stabilizing_k), omega), tau(a_ref, stabilizing_h))
    exact("double-action stabilizer matches adjoint stabilizer", fixed == omega)

    nonstabilizing_h = (matrix([[1, 1], [0, 1]]), zero(2))
    planted("generic right factor stabilizes theta", ad(nonstabilizing_h[0], th) == th)
    planted(
        "adjoint quotient automatically equals fixed-reference connection quotient",
        gauge_action(pure_jet, a_ref) == a_ref,
    )

    # Native structural controls: left quaternionic coefficients commute with
    # right-H scalars; trace reversal yields the (6,4) fibre and is preserved
    # infinitesimally by the Lorentz/Spin connection.
    left_i = matrix([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]])
    right_j = matrix([[0, 0, -1, 0], [0, 0, 0, -1], [1, 0, 0, 0], [0, 1, 0, 0]])
    left_j = matrix([[0, 0, -1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, -1, 0, 0]])
    exact("right-H compatibility", mm(left_i, right_j) == mm(right_j, left_i))
    planted("arbitrary left quaternion commutes", mm(left_i, left_j) == mm(left_j, left_i))

    eta = matrix([[-1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    trace_line = eta
    time_space = []
    for spatial in (1, 2, 3):
        h = [[0] * 4 for _ in range(4)]
        h[0][spatial] = h[spatial][0] = 1
        time_space.append(matrix(h))
    spatial_offdiag = []
    for i, j in ((1, 2), (1, 3), (2, 3)):
        h = [[0] * 4 for _ in range(4)]
        h[i][j] = h[j][i] = 1
        spatial_offdiag.append(matrix(h))
    diagonal_positive = [
        matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]),
        matrix([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]),
        matrix([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]),
    ]
    negative_basis = [trace_line] + time_space
    positive_basis = spatial_offdiag + diagonal_positive
    negative_gram = tuple(tuple(de_witt(h, k, eta) for k in negative_basis) for h in negative_basis)
    positive_gram = tuple(tuple(de_witt(h, k, eta) for k in positive_basis) for h in positive_basis)
    cross_gram = tuple(tuple(de_witt(h, k, eta) for k in positive_basis) for h in negative_basis)
    exact("trace-reversed negative four-plane", positive_definite(scale(-1, negative_gram)))
    exact("trace-reversed positive six-plane", positive_definite(positive_gram))
    exact("trace-reversed 4+6 orthogonality", cross_gram == tuple(tuple(F(0) for _ in positive_basis) for _ in negative_basis))

    boost = matrix([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    sym_basis = negative_basis + positive_basis
    exact(
        "Spin connection preserves trace-reversed form",
        all(
            de_witt(sym_action(boost, h), k, eta) + de_witt(h, sym_action(boost, k), eta) == 0
            for h in sym_basis
            for k in sym_basis
        ),
    )

    print(
        "G1-DERIVATIVE-COCYCLE-MOVING-REFERENCE: "
        f"{exact_checks} exact checks + {planted_checks} planted failures = "
        f"{exact_checks + planted_checks} PASS"
    )
    print("RESULT: q_A(g)=A-g.A contains dg and retains the tilted algebra")
    print("RESULT: the LC/reductive reference descends only with its H-connection and moving background")
    print("RESULT: the double quotient is an adjoint distortion quotient with matching stabilizers")
    print("BOUNDARY: no automatic Conn/G equivalence, selected reduction, action, VEV, index, or count")


if __name__ == "__main__":
    main()
