#!/usr/bin/env python3
"""Exact finite shadow of the Eric-guided IG/displacement/action chain.

This is not a model of the full gauge group on Y^14.  It checks the algebraic
load-bearing identities in a noncommutative 2x2 rational-matrix fixture:

  cocycle -> tilted homomorphism -> double-coset displacement
  -> invariant quadratic/curvature action -> transported Euler covector.

The fixture is intentionally exact (fractions only) and includes planted wrong
claims.  Its main Layer-0 result is that the displacement field and the Euler
covector are related but are not literally the same typed object in a generic
connection chart.
"""

from fractions import Fraction as F


def M(a, b, c, d):
    return ((F(a), F(b)), (F(c), F(d)))


ZERO = M(0, 0, 0, 0)
IDENTITY = M(1, 0, 0, 1)
A0 = M(2, 1, 0, -1)


def add(x, y):
    return tuple(tuple(x[i][j] + y[i][j] for j in range(2)) for i in range(2))


def neg(x):
    return tuple(tuple(-x[i][j] for j in range(2)) for i in range(2))


def sub(x, y):
    return add(x, neg(y))


def scale(q, x):
    q = F(q)
    return tuple(tuple(q * x[i][j] for j in range(2)) for i in range(2))


def mm(x, y):
    return tuple(
        tuple(sum((x[i][k] * y[k][j] for k in range(2)), F(0)) for j in range(2))
        for i in range(2)
    )


def inv(x):
    det = x[0][0] * x[1][1] - x[0][1] * x[1][0]
    assert det != 0
    return scale(F(1, 1) / det, ((x[1][1], -x[0][1]), (-x[1][0], x[0][0])))


def tr(x):
    return x[0][0] + x[1][1]


def pair(x, y):
    return tr(mm(x, y))


def comm(x, y):
    return sub(mm(x, y), mm(y, x))


def ad(g, x):
    return mm(mm(g, x), inv(g))


def cocycle(g):
    """Coboundary convention c(g)=A0-Ad_g(A0).

    It obeys c(gh)=c(g)+Ad_g c(h), hence tau(g)=(g,c(g)) is a
    homomorphism for the semidirect-product convention below.  The source's
    g^{-1}d_A g notation is the inverse/right-action presentation of this
    finite shadow; a global use must fix one convention explicitly.
    """

    return sub(A0, ad(g, A0))


def ig_mul(x, y):
    g, a = x
    h, b = y
    return mm(g, h), add(a, ad(g, b))


def tau(g):
    return g, cocycle(g)


def theta(omega):
    """Left-tilted invariant, right-tilted adjoint displacement."""

    g, a = omega
    return ad(inv(g), sub(a, cocycle(g)))


def theta_lambda(omega, lam):
    """Planted wrong coefficient in front of the Maurer-Cartan cocycle."""

    g, a = omega
    return ad(inv(g), sub(a, scale(lam, cocycle(g))))


def action(th, curvature, kappa):
    return pair(th, curvature) + F(kappa, 2) * pair(th, th)


def euler_theta(th, curvature, kappa):
    return add(curvature, scale(kappa, th))


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
    g = M(1, 1, 0, 1)
    h = M(2, 0, 1, 1)
    k = M(1, 0, -1, 1)
    a = M(1, 2, 3, -2)
    omega = (g, a)

    # Positive controls for the exact arithmetic and group representation.
    exact("inverse", mm(g, inv(g)) == IDENTITY and mm(inv(h), h) == IDENTITY)
    exact("trace pairing cyclic", pair(a, A0) == pair(A0, a))
    exact("adjoint representation", ad(mm(g, h), a) == ad(g, ad(h, a)))

    # The tilted embedding and the double-coset displacement.
    exact(
        "cocycle",
        cocycle(mm(g, h)) == add(cocycle(g), ad(g, cocycle(h))),
    )
    exact("tau homomorphism", ig_mul(tau(g), tau(h)) == tau(mm(g, h)))

    th = theta(omega)
    left = ig_mul(tau(k), omega)
    right = ig_mul(omega, tau(h))
    exact("left tilted action cancels", theta(left) == th)
    exact("right tilted action is adjoint", theta(right) == ad(inv(h), th))

    # A wrong Maurer-Cartan coefficient and raw translation coordinate both
    # fail the defining invariance.  These controls prevent a vacuous matcher.
    planted("lambda=2 left invariance", theta_lambda(left, 2) == theta_lambda(omega, 2))
    planted("raw translation is left invariant", left[1] == omega[1])

    # Minimal curvature-plus-quadratic source shadow.
    curvature = M(0, 3, -2, 1)
    kappa = F(3)
    transformed_th = ad(inv(h), th)
    transformed_curvature = ad(inv(h), curvature)
    exact(
        "right-adjoint action invariance",
        action(transformed_th, transformed_curvature, kappa)
        == action(th, curvature, kappa),
    )

    # Central difference is exact for this quadratic functional.  It verifies
    # E_theta = curvature + kappa*theta, not E_theta = theta.
    delta = M(2, -1, 1, 0)
    fd = (action(add(th, delta), curvature, kappa) - action(sub(th, delta), curvature, kappa)) / 2
    e_th = euler_theta(th, curvature, kappa)
    exact("first variation", fd == pair(delta, e_th))
    planted("Euler covector literally equals displacement", e_th == th)

    # In the affine connection coordinate a, delta theta = Ad_{g^-1} delta a.
    # Cyclicity transports the Euler covector back as E_a = Ad_g(E_theta).
    delta_a = M(-1, 2, 0, 1)
    delta_th = ad(inv(g), delta_a)
    fd_a = (
        action(add(th, delta_th), curvature, kappa)
        - action(sub(th, delta_th), curvature, kappa)
    ) / 2
    e_a = ad(g, e_th)
    exact("connection-chart Euler transport", fd_a == pair(delta_a, e_a))
    planted("Euler covector needs no chart transport", e_a == e_th)

    # The simultaneous adjoint variation supplies the finite Ward shadow.
    xi = M(1, 2, -1, 0)
    dth = comm(th, xi)
    dcurvature = comm(curvature, xi)
    ward = pair(dth, e_th) + pair(th, dcurvature)
    exact("adjoint Ward identity", ward == 0)

    # The field equation is curvature + kappa*theta = 0.  A nonzero theta can
    # be stationary; stationarity does not identify the field with its Euler
    # derivative.  The pure quadratic control recovers literal equality.
    on_shell_curvature = scale(-kappa, th)
    exact("nonzero on-shell displacement", th != ZERO)
    exact("source equation", euler_theta(th, on_shell_curvature, kappa) == ZERO)
    exact("pure quadratic identity control", euler_theta(th, ZERO, 1) == th)

    print(
        "WEINSTEIN-GUIDED-IG-SOURCE-SHADOW: "
        f"{exact_checks} exact checks + {planted_checks} planted failures = "
        f"{exact_checks + planted_checks} PASS"
    )
    print("RESULT: tau coefficient 1 selected by left invariance")
    print("RESULT: double-coset displacement is left-invariant/right-adjoint")
    print("RESULT: E_theta=curvature+kappa*theta; E_a=Ad_g(E_theta)")
    print("BOUNDARY: finite exact shadow only; no global quotient, native Shiab, VEV, or count")


if __name__ == "__main__":
    main()
