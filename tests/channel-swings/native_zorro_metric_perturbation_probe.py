#!/usr/bin/env python3
"""Metric-to-distortion perturbation map on the curved I1B background.

Exact curvature jets, observing-section cancellation, an off-section null
wave control, and its leading distortion compensator. No mode/domain claim.
"""
from functools import lru_cache
from fractions import Fraction
from itertools import combinations
import json

import sympy as sp

from native_zorro_geometry_probe import (
    BASIS, ETA4, dewitt, geometry, metric, rational_frame, vertical_coordinates,
)
from native_zorro_i1b_probe import invariant_projectors, spin_curvature, first_order_euler
from native_i1b_scalar_closure_probe import CORE, ETA, direction, dual_rows


def base_connection(q, u):
    """Coefficient of the linearized observing Levi-Civita connection."""
    return [sp.Matrix(4, 4, lambda a, j: sum(
        ETA4[a, b]*(q[i]*u[b, j]+q[j]*u[b, i]-q[b]*u[i, j])/2
        for b in range(4))) for i in range(4)]


def metric_lift(h, inverse, connection):
    c = [z.T*h+h*z for z in connection]
    k = sp.zeros(14)
    for i in range(4):
        for a, field in enumerate(BASIS):
            k[i, 4+a] = k[4+a, i] = -dewitt(inverse, c[i], field)
    return k, c


def lift_derivative(h, inverse, connection, normal):
    c = [z.T*h+h*z for z in connection]
    dc = [z.T*normal+normal*z for z in connection]
    di = -inverse*normal*inverse
    k = sp.zeros(14)
    for i in range(4):
        for a, field in enumerate(BASIS):
            value = -sp.trace(di*c[i]*inverse*field+inverse*dc[i]*inverse*field
                              +inverse*c[i]*di*field)
            value += (sp.trace(di*c[i]+inverse*dc[i])*sp.trace(inverse*field)
                      +sp.trace(inverse*c[i])*sp.trace(di*field))/2
            k[i, 4+a] = k[4+a, i] = value
    return k


def christoffel_from_first(inverse, first):
    return [sp.Matrix(14, 14, lambda a, b: sum(
        inverse[a, j]*(first[r][j, b]+first[b][j, r]-first[j][r, b])/2
        for j in range(14) if inverse[a, j])) for r in range(14)]


@lru_cache(maxsize=1)
def background_geometry():
    g, first, gamma, _, _ = geometry()
    return g, g.inv(), first, gamma, rational_frame(g)


def ricci_from_curvature(curvature):
    zero = sp.zeros(14)
    def r(a, b):
        return zero if a == b else curvature[a, b] if a < b else -curvature[b, a]
    return sp.Matrix(14, 14, lambda i, j: sum(r(k, j)[k, i] for k in range(14)))


def section_second_jet(q, u):
    """delta g=(q.x)^2 u/2 at x=0, with value and first jet zero."""
    g, inverse, first, gamma, frame = background_geometry()
    connection = base_connection(q, u)
    k, c = metric_lift(ETA4, ETA4, connection)
    dk = [lift_derivative(ETA4, ETA4, connection, a) for a in BASIS]
    zero = sp.zeros(14)
    df = [q[i]*k for i in range(4)] + [zero]*10
    ddf = [[zero]*14 for _ in range(14)]
    for i in range(4):
        for a in range(10):
            ddf[i][4+a] = ddf[4+a][i] = q[i]*dk[a]
    dgamma = christoffel_from_first(inverse, df)
    ddgamma = []
    for caxis in range(14):
        term = christoffel_from_first(inverse, ddf[caxis])
        # Both the varied inverse metric and the background inverse metric
        # are differentiated; omitting either term changes the curved jet.
        ddgamma.append([term[r]-inverse*first[caxis]*dgamma[r]
                        -inverse*df[caxis]*gamma[r] for r in range(14)])
    curvature = {(i, j): ddgamma[i][j]-ddgamma[j][i]
                 +dgamma[i]*gamma[j]+gamma[i]*dgamma[j]
                 -dgamma[j]*gamma[i]-gamma[j]*dgamma[i]
                 for i, j in combinations(range(14), 2)}
    ricci = ricci_from_curvature(curvature)
    # Natural field coordinates T=T_*(g)+t: check the moving projectors.
    projectors = invariant_projectors()
    radial = sp.Matrix([0]*4+list(vertical_coordinates(ETA4)/2))
    defects = []
    for index, (p, _) in enumerate(projectors):
        for axis in range(4):
            dh = sp.zeros(14)
            dh[4:, :4] = sp.Matrix.hstack(*[vertical_coordinates(z) for z in c])*q[axis]
            dr = sp.zeros(14)
            for j in range(4):
                dr[:, j] = radial*dewitt(ETA4, ETA4/2, c[j])*q[axis]
            dp = dh if index == 0 else dr if index == 2 else -dh-dr
            defects.append(dp+dgamma[axis]*p-p*dgamma[axis])
    defects.extend(z*radial for z in dgamma)
    return ricci, curvature, defects


def base_ricci(q, u):
    gamma = base_connection(q, u)
    return sp.Matrix(4, 4, lambda i, j: sum(
        (q[k]*gamma[j]-q[j]*gamma[k])[k, i] for k in range(4)))


def principal_ricci(g, k, q):
    inverse = g.inv()
    raised = inverse*q
    return (q*(k*raised).T+(k*raised)*q.T
            -(q.T*raised)[0]*k-sp.trace(inverse*k)*q*q.T)/2


def principal_curvature(g, k, q):
    second = [[q[i]*q[j]*k for j in range(14)] for i in range(14)]
    derivative = [christoffel_from_first(g.inv(), row) for row in second]
    return {(i, j): derivative[i][j]-derivative[j][i]
            for i, j in combinations(range(14), 2)}


def diagonal_fibre_frame(change):
    frame = background_geometry()[-1]
    vertical = sp.Matrix.hstack(*[vertical_coordinates(change.T*a*change) for a in BASIS])
    return sp.diag(change.inv(), vertical)*frame


def spin_connection_symbol(q, k):
    """Symmetric-frame Levi-Civita variation for an ambient metric symbol."""
    out = {}
    for mu in range(14):
        for a, b in combinations(range(14), 2):
            coefficient = ETA[a]*ETA[b]*(q[b]*k[a, mu]-q[a]*k[mu, b])/4
            if coefficient:
                out = CORE.fadd(out, CORE.fscale(Fraction(coefficient),
                    direction(mu, (1 << a) | (1 << b))))
    return out


def raw_curvature_response(q, connection):
    curvature = {}
    for axis, value in enumerate(q):
        curvature = CORE.fadd(curvature, CORE.wedge_raw(
            CORE.fscale(Fraction(value), direction(axis, 0)), connection))
    return dual_rows(CORE.shiab(curvature))


def certify():
    passed = []
    def check(label, condition):
        if not bool(condition):
            raise AssertionError(label)
        passed.append(label)
    def zero(matrix):
        return all(sp.expand(x) == 0 for x in matrix)

    # Symbolic, arbitrary base covector and symmetric metric polarization.
    qs = sp.symbols("q0:4")
    coeff = sp.symbols("u0:10")
    us = sum((c*b for c, b in zip(coeff, BASIS)), sp.zeros(4))
    lifted, c = metric_lift(ETA4, ETA4, base_connection(qs, us))
    check("observing-section connection lift is q_i times the polarization",
          all(zero(c[i]-qs[i]*us) for i in range(4)))
    extended = sp.Matrix(list(qs)+[0]*10)
    g, inverse, first, gamma, frame = background_geometry()
    check("third derivative Ricci response vanishes identically at observation",
          zero(principal_ricci(g, lifted, extended)))

    # Three Lorentz orbits, all ten symmetric polarizations. Homogeneity,
    # linearity and Lorentz covariance extend these exact checks to real q.
    orbit_records = []
    for label, q in (("timelike", [1, 0, 0, 0]),
                     ("spacelike", [0, 1, 0, 0]),
                     ("null", [1, 1, 0, 0])):
        for i, u in enumerate(BASIS):
            ricci, curvature, defects = section_second_jet(q, u)
            expected = sp.diag(base_ricci(q, u), sp.zeros(10))
            assert ricci == expected, (label, i)
            assert all(zero(z) for z in defects), (label, i, "moving projectors")
            f, _ = spin_curvature(frame, curvature)
            rows = dual_rows(CORE.shiab(f))
            sharp = sp.diag(*ETA)*frame.T*ricci*frame
            einstein = sharp-sp.trace(sharp)*sp.eye(14)/2
            # Euler covector, not the Riesz endomorphism: the grade-one
            # Hodge pairing contributes eta_mu eta_nu and transposes this
            # metric-self-adjoint endomorphism in the coefficient array.
            expected_rows = {(mu, 1 << nu): -einstein[mu, nu]
                             for nu, mu in einstein.todok() if einstein[nu, mu]}
            assert rows == expected_rows, (label, i, "Shiab")
        orbit_records.append({"orbit": label, "polarizations": 10})
        check(f"{label}: full curved second-jet Ricci, moving fields and Shiab response", True)

    # A genuine observed null transverse-traceless polarization.
    q = [1, 1, 0, 0]
    u = sp.diag(0, 0, 1, -1)
    q4 = sp.Matrix(q)
    check("observed test wave is null, transverse, traceless and Ricci-flat to first order",
          (q4.T*ETA4*q4)[0] == 0 and q4.T*ETA4*u == sp.zeros(1, 4)
          and sp.trace(ETA4*u) == 0 and base_ricci(q, u) == sp.zeros(4))
    check("the metric polarization is not a base diffeomorphism symbol",
          q[2] == 0 and u[2, 2] == 1)
    rho = sp.symbols("rho")
    h = sp.diag(1+rho, -1, -1, -1)
    lifted, _ = metric_lift(h, h.inv(), base_connection(q, u))
    qr = sp.Matrix(q+[0]*10)
    ricci = principal_ricci(metric(h, h.inv()), lifted, qr).applyfunc(sp.cancel)
    expected = sp.zeros(14)
    expected[2, 6] = expected[6, 2] = -rho**2/(2*(1+rho)**2)
    expected[3, 7] = expected[7, 3] = rho**2/(2*(1+rho)**2)
    check("off-section cubic response is exactly the stated normal quadratic rational tensor",
          zero(ricci-expected))
    check("response is invisible to section value and this first normal derivative",
          ricci.subs(rho, 0) == sp.zeros(14)
          and ricci.diff(rho).subs(rho, 0) == sp.zeros(14)
          and ricci.diff(rho, 2).subs(rho, 0)[2, 6] == -1)

    # Rational orthonormal frame at h=diag(4,-1,-1,-1).
    h = sp.diag(4, -1, -1, -1)
    g = metric(h, h.inv())
    frame = diagonal_fibre_frame(sp.diag(2, 1, 1, 1))
    check("off-section frame has the exact same K77 pairing", frame.T*g*frame == sp.diag(*ETA))
    lifted, _ = metric_lift(h, h.inv(), base_connection(q, u))
    curvature = principal_curvature(g, lifted, qr)
    check("independent Christoffel curvature calculation matches the Ricci formula",
          ricci_from_curvature(curvature) == expected.subs(rho, 3))
    f, _ = spin_curvature(frame, curvature)
    source = dual_rows(CORE.shiab(f))
    expected_source = {(2, 256): -sp.Rational(9, 64), (2, 4096): -sp.Rational(27, 64),
                       (3, 512): sp.Rational(9, 64), (3, 8192): sp.Rational(27, 64),
                       (8, 4): sp.Rational(9, 64), (9, 8): -sp.Rational(9, 64),
                       (12, 4): -sp.Rational(27, 64), (13, 8): sp.Rational(27, 64)}
    check("actual Shiab gives eight nonzero grade-one cubic source rows", source == expected_source)
    # Constructive countercontrol: the leading forcing is in the actual
    # distortion derivative image. This prevents calling it a physical kill.
    witness = {(0, 260): Fraction(9, 32), (2, 257): Fraction(-9, 32),
               (0, 520): Fraction(-9, 32), (3, 513): Fraction(9, 32),
               (0, 4100): Fraction(-27, 32), (2, 4097): Fraction(27, 32),
               (0, 8200): Fraction(27, 32), (3, 8193): Fraction(-27, 32)}
    y = CORE.fadd(*(CORE.fscale(z, direction(*row)) for row, z in witness.items()))
    qframe = frame.T*qr
    gradient = [CORE.fscale(Fraction(z), y) for z in qframe]
    response = first_order_euler(gradient)
    check("eight-component distortion compensator solves every leading source row", response == source)
    check("compensator is grade two and annihilates every grade-one metric source covector",
          all(mask.bit_count() == 2 for _, mask in witness)
          and all(mask.bit_count() == 1 for _, mask in source))
    # Complete transverse tracefree metric basis at a unit positive covector.
    # Equivariance, homogeneity and polynomial continuation give the lemma
    # at any non-null ambient covector; no physical quotient is inferred.
    unit = sp.Matrix([1]+[0]*13)
    tt = []
    for i, j in combinations(range(1, 14), 2):
        z = sp.zeros(14)
        z[i, j] = z[j, i] = 1
        tt.append(z)
    for i in range(1, 13):
        z = sp.zeros(14)
        z[i, i], z[13, 13] = ETA[i], -ETA[13]
        tt.append(z)
    assert len(tt) == 90
    for z in tt:
        assert z*unit == sp.zeros(14, 1) and sp.trace(sp.diag(*ETA)*z) == 0
        b = spin_connection_symbol(unit, z)
        assert first_order_euler([b]+[{}]*13) == raw_curvature_response(unit, b)
    check("full 90-dimensional transverse tracefree metric basis has a connection compensator", True)
    # Apply the covariant construction at the rational off-section point.
    kframe = frame.T*lifted*frame
    eta = sp.diag(*ETA)
    divergence = kframe*eta*qframe
    qnorm = (qframe.T*eta*qframe)[0]
    perpendicular = kframe-(qframe*divergence.T+divergence*qframe.T)/qnorm
    check("mixed metric lift admits the stated transverse tracefree projection",
          perpendicular*eta*qframe == sp.zeros(14, 1)
          and sp.trace(eta*perpendicular) == 0)
    geometric_y = spin_connection_symbol(qframe, perpendicular)
    check("projected Levi-Civita symbol is a second exact leading compensator",
          first_order_euler([CORE.fscale(Fraction(z), geometric_y) for z in qframe]) == source
          and raw_curvature_response(qframe, geometric_y) == source)
    unprojected = spin_connection_symbol(qframe, kframe)
    unprojected_rows = first_order_euler([CORE.fscale(Fraction(z), unprojected) for z in qframe])
    extras = {r: unprojected_rows.get(r, 0)-source.get(r, 0)
              for r in set(unprojected_rows)|set(source)
              if unprojected_rows.get(r, 0) != source.get(r, 0)}
    check("omitting the transverse projection leaves four exact unwanted Euler rows",
          extras == {(6, 1): sp.Rational(3, 32), (5, 1): -sp.Rational(3, 32),
                     (5, 2): -sp.Rational(3, 16), (6, 2): sp.Rational(3, 16)})
    # Four exact gauge controls at the off-section point.
    for j in range(4):
        xi = sp.eye(4)[:, j]
        gauge = q4*xi.T+xi*q4.T
        kg, _ = metric_lift(h, h.inv(), base_connection(q, gauge))
        assert principal_ricci(g, kg, qr) == sp.zeros(14)
    check("all four base-diffeomorphism polarizations have zero cubic response off section", True)
    return {
        "result_id": "NATIVE-ZORRO-METRIC-PERTURBATION",
        "checks_passed": len(passed), "checks": passed,
        "section_second_jet_controls": orbit_records,
        "selected_action": "same reconstructed comm/symi/symi I1B stationary branch",
        "field_coordinates": "T=T_star(g)+t using the natural projector/radial tensor formula",
        "off_section_family": "h=diag(1+rho,-1,-1,-1), rho>-1",
        "observed_null_wave": {"q": q, "polarization": "diag(0,0,1,-1)"},
        "nonzero_cubic_ricci": "R_(2,02)=-rho^2/(2(1+rho)^2), R_(3,03)=+rho^2/(2(1+rho)^2), symmetric counterparts",
        "rational_point": "rho=3",
        "source_rows": [[mu, mask, str(value)] for (mu, mask), value in source.items()],
        "compensator_rows": [[mu, mask, str(value)] for (mu, mask), value in witness.items()],
        "principal_identity": "E(q)y=A3(q)u; t=-z^2 y cancels z^3 A3(q)u",
        "geometric_compensator": "For Q^2!=0, k_perp=k-(Q tensor div(k)+div(k) tensor Q)/Q^2; y is its symmetric-frame spin Levi-Civita symbol.",
        "transverse_tracefree_basis_controls": 90,
        "claim_ceiling": "Actual mixed highest-derivative response, exact observation-section second jet and one principal compensator; no completed coupled Hessian, mode, constraint propagation, physical quotient or energy theorem.",
    }


if __name__ == "__main__":
    print(json.dumps(certify(), indent=2))
