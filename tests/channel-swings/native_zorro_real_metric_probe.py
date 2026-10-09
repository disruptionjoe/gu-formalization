#!/usr/bin/env python3
"""Pure metric Hessian and a real-packet acceleration certificate.

Exact coordinate curvature jets, full covariant compensator derivatives,
all primary receivers touched by the five spatial traceless polarizations,
and independent occupation-state checks. This is a local bulk coefficient
certificate, not a completed physical Hamiltonian or a Cauchy theorem.
"""

from fractions import Fraction
from functools import lru_cache
from itertools import combinations
import json
import sys

import sympy as sp

from native_zorro_metric_perturbation_probe import (
    CORE,
    ETA,
    ETA4,
    BASIS,
    direction,
    dewitt,
    metric,
    metric_lift,
    base_connection,
    base_ricci,
    lift_derivative,
    diagonal_fibre_frame,
    spin_connection_symbol,
    first_order_euler,
    vertical_coordinates,
    christoffel_from_first,
    ricci_from_curvature,
    principal_ricci,
)
from native_zorro_geometry_probe import connection, metric_derivative
from native_zorro_constrained_energy_probe import background_fields
from native_i1b_scalar_closure_probe import derivative_block, exact
from native_zorro_stationary_background_probe import (
    algebraic_branch,
    rational_interval,
    fields_and_gradients,
)
from native_zorro_i1b_probe import clifford_form
from native_zorro_matrix_energy_probe import (
    word,
    packet_basis,
    time_block,
    mass_entry,
    cubic_entry,
    backgrounds,
)


def curvature_square_jet(q4, u, h):
    hi = h.inv()
    G = metric(h, hi)
    Gi = G.inv()
    bc = base_connection(q4, u)
    k, c = metric_lift(h, hi, bc)
    first = [q4[i] * k for i in range(4)] + [sp.zeros(14)] * 10
    # Coefficient of epsilon^2 in the second derivatives of G,
    # not the epsilon Hessian (which is twice this coefficient).
    hh = sp.Matrix(4, 4, lambda i, j: dewitt(hi, c[i], c[j]))
    second = [
        [
            (
                2 * q4[i] * q4[j] * sp.diag(hh, sp.zeros(10))
                if i < 4 and j < 4
                else sp.zeros(14)
            )
            for j in range(14)
        ]
        for i in range(14)
    ]
    dg = christoffel_from_first(Gi, first)
    ddg = [
        [
            x - Gi * first[axis] * dg[r]
            for r, x in enumerate(christoffel_from_first(Gi, second[axis]))
        ]
        for axis in range(14)
    ]
    R2 = {
        (i, j): ddg[i][j] - ddg[j][i] + dg[i] * dg[j] - dg[j] * dg[i]
        for i, j in combinations(range(14), 2)
    }
    ric = ricci_from_curvature(R2)
    scal = sp.trace(Gi * ric)
    fnorm = 0
    for i, j in combinations(range(4), 2):
        R = q4[i] * bc[j] - q4[j] * bc[i]
        F = R.T * h + h * R
        for p, l in combinations(range(4), 2):
            Rother = q4[p] * bc[l] - q4[l] * bc[p]
            Fother = Rother.T * h + h * Rother
            fnorm += (
                2 * (hi[i, p] * hi[j, l] - hi[i, l] * hi[j, p]) * dewitt(hi, F, Fother)
            )
    assert sp.factor(scal + fnorm / 4) == 0, (scal, fnorm)
    radial = sp.Matrix([0] * 4 + list(vertical_coordinates(h) / 2))
    assert (radial.T * ric * radial)[0] == 0
    return scal, fnorm


def oneform_spin_lift(Y, frame):
    inv = frame.inv()
    out = {}
    for mu in range(14):
        val = (
            inv
            * sum((frame[axis, mu] * Y[axis] for axis in range(14)), sp.zeros(14))
            * frame
        )
        for a, b in combinations(range(14), 2):
            c = val[a, b] * ETA[b] / 2
            if c:
                out = CORE.fadd(
                    out, CORE.fscale(Fraction(c), direction(mu, (1 << a) | (1 << b)))
                )
    return out


def compensator_gradient(q4, u, h, frame, connection_coefficient=None):
    hi = h.inv()
    G = metric(h, hi)
    Gi = G.inv()
    q = sp.Matrix(q4 + [0] * 10)
    bc = (
        base_connection(q4, u)
        if connection_coefficient is None
        else connection_coefficient
    )
    k, _ = metric_lift(h, hi, bc)
    raised = Gi * q
    div = k * raised
    qn = (q.T * raised)[0]
    cross = q * div.T + div * q.T
    kp = k - cross / qn
    Y = [(Gi * kp[:, mu] * q.T - raised * kp[:, mu].T) / 2 for mu in range(14)]
    y = oneform_spin_lift(Y, frame)
    expected = spin_connection_symbol(frame.T * q, frame.T * kp * frame)
    assert y == expected
    partial = [[sp.zeros(14) for mu in range(14)] for axis in range(14)]
    for axis, a in enumerate(BASIS, 4):
        dG = metric_derivative(hi, a)
        dGi = -Gi * dG * Gi
        dk = lift_derivative(h, hi, bc, a)
        draised = dGi * q
        ddiv = dk * raised + k * draised
        dqn = (q.T * draised)[0]
        dkp = dk - (q * ddiv.T + ddiv * q.T) / qn + cross * dqn / qn**2
        partial[axis] = [
            (
                dGi * kp[:, mu] * q.T
                + Gi * dkp[:, mu] * q.T
                - draised * kp[:, mu].T
                - raised * dkp[:, mu].T
            )
            / 2
            for mu in range(14)
        ]
    gamma = connection(h, hi)
    cov = [
        [
            partial[axis][mu]
            + gamma[axis] * Y[mu]
            - Y[mu] * gamma[axis]
            - sum((gamma[axis][nu, mu] * Y[nu] for nu in range(14)), sp.zeros(14))
            for mu in range(14)
        ]
        for axis in range(14)
    ]
    gradient = [
        oneform_spin_lift(
            [
                sum(
                    (frame[axis, s] * cov[axis][mu] for axis in range(14)), sp.zeros(14)
                )
                for mu in range(14)
            ],
            frame,
        )
        for s in range(14)
    ]
    return y, gradient, first_order_euler(gradient)


@lru_cache(None)
def real_full_block(seed):
    labels = [seed, seed ^ 1, seed ^ 1024, seed ^ 1025]
    basis, e = derivative_block(0, labels)
    take = [i for i, (_, mask) in enumerate(basis) if mask.bit_count() % 4 in (1, 2)]
    basis = [basis[i] for i in take]
    e = e.extract(take, take)
    n = sp.Matrix.hstack(*e.nullspace())
    fs = [direction(*row) for row in basis]
    mass = sp.diag(*[exact(CORE.pair(f, CORE.hodge(f))) for f in fs])
    hs = []
    for bg in background_fields():
        images = [
            CORE.shiab(CORE.fadd(CORE.wedge_raw(bg, u), CORE.wedge_raw(u, bg)))
            for u in fs
        ]
        hh = sp.zeros(len(fs))
        for i in range(len(fs)):
            for j in range(i, len(fs)):
                cross = CORE.fadd(
                    CORE.wedge_raw(fs[i], fs[j]), CORE.wedge_raw(fs[j], fs[i])
                )
                val = (
                    exact(CORE.pair(fs[i], images[j]))
                    + exact(CORE.pair(fs[j], images[i]))
                    + exact(CORE.pair(bg, CORE.shiab(cross)))
                ) / 3
                hh[i, j] = hh[j, i] = val
        hs.append(hh)
    return basis, e, n, mass, hs


def curvature_connection(f):
    """Koszul curvature correction in a horizontal/vertical adapted frame."""
    zero = sp.zeros(14, 1)
    delta = [sp.zeros(14) for _ in range(14)]
    vertical = [v for v in range(4, 14) if v != 10]
    for i in range(4):
        for j in range(4):
            delta[i][:, j] = f.get((i, j), zero) / 2
        for v in vertical:
            for k in range(4):
                delta[i][k, v] = delta[v][k, i] = (
                    -ETA[k] * ETA[v] * f.get((i, k), zero)[v] / 2
                )
    return delta


def symbolic_scalar_identity():
    vertical = [v for v in range(4, 14) if v != 10]
    pairs = list(combinations(range(4), 2))
    variables = sp.symbols("f0:54")
    f = {}
    for p, (i, j) in enumerate(pairs):
        f[i, j] = sp.Matrix(
            [
                variables[9 * p + vertical.index(v)] if v in vertical else 0
                for v in range(14)
            ]
        )
        f[j, i] = -f[i, j]
    delta = curvature_connection(f)
    zero = sp.zeros(14, 1)
    curvature = {
        (i, j): delta[i] * delta[j]
        - delta[j] * delta[i]
        - sum((f.get((i, j), zero)[v] * delta[v] for v in vertical), sp.zeros(14))
        for i, j in combinations(range(14), 2)
    }
    ricci = ricci_from_curvature(curvature)
    norm = 2 * sum(
        ETA[i] * ETA[j] * ETA[v] * f[i, j][v] ** 2 for i, j in pairs for v in vertical
    )
    assert sp.expand(sum(ETA[i] * ricci[i, i] for i in range(14)) + norm / 4) == 0
    assert ricci[10, 10] == 0


def first_order_density_identity():
    fields = fields_and_gradients()[0]
    ph = sp.diag(sp.eye(4), sp.zeros(10))
    count = 0
    for i, j in combinations(range(4), 2):
        for v in range(4, 14):
            if v == 10:
                continue
            f = {(i, j): sp.eye(14)[:, v], (j, i): -sp.eye(14)[:, v]}
            gradient = [clifford_form(z * ph - ph * z) for z in curvature_connection(f)]
            gradient = [
                CORE.fclean(
                    {fm: CORE.emul(CORE.blade(10), e) for fm, e in field.items()}
                )
                for field in gradient
            ]
            exterior = {}
            for axis, field in enumerate(gradient):
                exterior = CORE.fadd(
                    exterior, CORE.wedge_raw(direction(axis, 0), field)
                )
            image = CORE.shiab(exterior)
            assert all(exact(CORE.pair(bg, image)) == 0 for bg in fields[:2])
            count += 1
    assert count == 54


def form_rows(form):
    return {
        (fm.bit_length() - 1, cm): exact(value)
        for fm, element in form.items()
        for cm, value in element.items()
    }


def certify(progress=None):
    checks = []

    def check(label, condition=True):
        assert condition, label
        checks.append(label)
        if progress:
            progress(label)

    symbolic_scalar_identity()
    check(
        "all 54 curvature variables give scalar correction minus one quarter F squared"
    )
    first_order_density_identity()
    check(
        "all 54 curvature directions vanish in the natural first-order action density"
    )
    jets = 0
    for h in [ETA4, sp.diag(4, -1, -1, -1), sp.diag(1, -4, -1, -1)]:
        for q in [[1, 0, 0, 0], [1, 1, 0, 0]]:
            for u in [sp.diag(0, 0, 1, -1), BASIS[1], BASIS[4]]:
                curvature_square_jet(q, u, h)
                jets += 1
    check(
        "18 independent coordinate quadratic jets verify scalar and radial Ricci identities",
        jets == 18,
    )
    for h in [ETA4, sp.diag(4, -1, -1, -1)]:
        check(
            f"coordinate volume identity at diagonal {list(h.diagonal())}",
            abs(metric(h, h.inv()).det()) == 64 / h.det() ** 4,
        )

    h = sp.diag(4, -1, -1, -1)
    frame = diagonal_fibre_frame(sp.diag(2, 1, 1, 1))
    q4 = [1, 0, 0, 0]
    polarizations = [
        sp.diag(0, 1, -1, 0),
        sp.diag(0, 0, 1, -1),
        BASIS[5],
        BASIS[6],
        BASIS[8],
    ]
    gram = sp.Matrix(5, 5, lambda i, j: sp.trace(polarizations[i] * polarizations[j]))
    ys, rs, horizontal_sources = [], [], []
    norms = []
    for u in polarizations:
        y, gradient, dy = compensator_gradient(q4, u, h, frame)
        ys.append(form_rows(y))
        ricci = sp.diag(base_ricci(q4, u), sp.zeros(10))
        sharp = sp.diag(*ETA) * frame.T * ricci * frame
        einstein = sharp - sp.trace(sharp) * sp.eye(14) / 2
        a2 = {
            (mu, 1 << nu): -einstein[mu, nu]
            for nu, mu in einstein.todok()
            if einstein[nu, mu]
        }
        horizontal_sources.append(
            sp.Matrix(16, 1, lambda i, _: -einstein[i // 4, i % 4])
        )
        k, _ = metric_lift(h, h.inv(), base_connection(q4, u))
        a3_ricci = principal_ricci(metric(h, h.inv()), k, sp.Matrix(q4 + [0] * 10))
        assert a3_ricci[:4, :4] == sp.zeros(4)
        residual = {row: a2.get(row, 0) - dy.get(row, 0) for row in set(a2) | set(dy)}
        rs.append({row: value for row, value in residual.items() if value})
        norms.append(curvature_square_jet(q4, u, h)[1])
    check(
        "five spatial traceless metric polarizations have positive Frobenius Gram",
        gram.det() == 24 and all(z == sp.Rational(9, 8) for z in norms),
    )
    check(
        "horizontal second-time metric source is injective while the third-time source is mixed",
        sp.Matrix.hstack(*horizontal_sources).rank() == 5,
    )

    seeds = sorted(
        {((1 << mu) ^ mask) & ~1025 for rows in ys + rs for mu, mask in rows}
    )
    quadratic = [sp.zeros(5) for _ in range(5)]
    primary_records = []
    for seed in seeds:
        basis, e, n, mass, hs = real_full_block(seed)
        y = sp.Matrix(len(basis), 5, lambda i, j: ys[j].get(basis[i], 0))
        residual = sp.Matrix(len(basis), 5, lambda i, j: rs[j].get(basis[i], 0))
        assert n.T * residual == sp.zeros(n.cols, 5)
        for index, matrix in enumerate([mass] + hs):
            assert n.T * matrix * y == sp.zeros(n.cols, 5)
            quadratic[index] += y.T * matrix * y
        primary_records.append(dict(label=seed, coefficients=len(basis), kernel=n.cols))
    check(
        "full covariant compensator residual and all five potential columns annihilate every primary receiver"
    )
    check(
        "complete traceless acceleration potential has the exact mass and cubic Gram matrices",
        quadratic
        == [
            sp.Rational(-9, 256) * gram,
            sp.Rational(39, 64) * gram,
            sp.Rational(3, 64) * gram,
            sp.zeros(5),
            sp.zeros(5),
        ],
    )

    # Check the Clifford contractions with the independent 128-state engine.
    matrix_y = [
        [(value, (mu, word(mask))) for (mu, mask), value in rows.items()] for rows in ys
    ]
    independent = [sp.zeros(5) for _ in range(3)]
    for i in range(5):
        for j in range(i, 5):
            independent[0][i, j] = sum(
                a * b * mass_entry(u, v) for a, u in matrix_y[i] for b, v in matrix_y[j]
            )
            for k in range(2):
                independent[1 + k][i, j] = sum(
                    a * b * cubic_entry(backgrounds()[k], u, v)
                    for a, u in matrix_y[i]
                    for b, v in matrix_y[j]
                )
            for matrix in independent:
                matrix[j, i] = matrix[i, j]
    check(
        "independent occupation-state matrices reproduce all three nonzero compensator Gram matrices",
        independent == quadratic[:3],
    )

    for u in [BASIS[0], BASIS[1], BASIS[2], BASIS[3]]:
        y, _, dy = compensator_gradient(q4, u, h, frame)
        assert not y and not dy and base_ricci(q4, u) == sp.zeros(4)
    check(
        "the lapse and all three shift polarizations have zero acceleration source at this fibre point"
    )
    w, polynomial, v, alpha, beta, k2, _, _ = algebraic_branch()
    interval = (sp.Rational(227427945967, 10**12), sp.Rational(227427945969, 10**12))
    coefficient = 1 + sp.Rational(8, 3) * (10 * alpha + beta)
    bounds = rational_interval(coefficient, w, interval)
    check(
        "rational interval arithmetic certifies a nonzero acceleration coefficient on both coupling branches",
        bounds[0] > 3 and bounds[1] < sp.Rational(31, 10),
    )

    # A zero column for the four stationary directions is not a universal
    # background identity. This control does not assert another equilibrium.
    receiver = (0, (0, 4, 10))
    basis = packet_basis((1 << 4) ^ (1 << 10) ^ (1 << 0) ^ (1 << 1))
    n = sp.Matrix.hstack(*time_block(basis).nullspace())
    bg = [(sp.S.One, (0, (1,)))]
    column = n.T * sp.Matrix([cubic_entry(bg, row, receiver) for row in basis])
    nonzero = [(i, str(z)) for i, z in enumerate(column) if z]
    check(
        "an off-diagonal real grade-one background breaks the claimed universal zero-column identity",
        nonzero == [(0, "-4/3"), (1, "-4/3")],
    )
    return dict(
        passed=len(checks),
        checks=checks,
        coordinate_quadratic_controls=jets,
        primary_receiver_blocks=primary_records,
        spatial_traceless_gram=[[str(z) for z in row] for row in gram.tolist()],
        natural_action_curvature_coefficient="K=(11a+c)/2",
        acceleration_hessian_per_frobenius_norm="-9/256*(kappa+8/3*(10*a+c))",
        primary_acceleration_correction="zero at h=diag(4,-1,-1,-1)",
        positive_factor_interval=list(map(str, bounds)),
        mirror_behavior="acceleration Hessian changes sign and stays nondegenerate",
        background_control=dict(
            background="e^0 gamma_1",
            receiver="e^0 gamma_0 gamma_4 gamma_10",
            nonzero_primary_rows=nonzero,
            stationary_claim=False,
        ),
        scope="pure-base Hessian and real local acceleration coefficient; conditional homogeneous Hamiltonian consequence only",
    )


if __name__ == "__main__":
    print(
        json.dumps(
            certify(lambda message: print(message, file=sys.stderr, flush=True)),
            indent=2,
        )
    )
