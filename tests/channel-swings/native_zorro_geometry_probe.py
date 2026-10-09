#!/usr/bin/env python3
"""Exact local geometry of the canonical Zorro reconstruction over a flat base.

The fibre coordinate h and observing metric g are distinct variables.
G_Y(g)=h dx dx + D_h(dh-C(Gamma(g))dx, dh-C(Gamma(g))dx).
At Gamma(g)=0 this is curved despite the flat observed metric.
"""

from itertools import combinations
import json

import sympy as sp


SLOTS = [(i, j) for i in range(4) for j in range(i, 4)]
ETA4 = sp.diag(1, -1, -1, -1)


def symmetric_basis():
    result = []
    for i, j in SLOTS:
        a = sp.zeros(4)
        a[i, j] = a[j, i] = 1
        result.append(a)
    return result


BASIS = symmetric_basis()


def vertical_coordinates(a):
    return sp.Matrix([a[i, j] for i, j in SLOTS])


def dewitt(h_inverse, a, b):
    return sp.trace(h_inverse*a*h_inverse*b) - sp.trace(h_inverse*a)*sp.trace(h_inverse*b)/2


def metric(h, h_inverse):
    return sp.diag(h, sp.Matrix(10, 10, lambda i, j: dewitt(h_inverse, BASIS[i], BASIS[j])))


def metric_derivative(h_inverse, a):
    di = -h_inverse*a*h_inverse
    def entry(b, c):
        return (sp.trace(di*b*h_inverse*c+h_inverse*b*di*c)
                - (sp.trace(di*b)*sp.trace(h_inverse*c)
                   + sp.trace(h_inverse*b)*sp.trace(di*c))/2)
    return sp.diag(a, sp.Matrix(10, 10, lambda i, j: entry(BASIS[i], BASIS[j])))


def connection(h, h_inverse, variation=None):
    """Coordinate Levi-Civita coefficients and their exact fibre derivative.

    These formulas follow from the Koszul formula. The probe also checks
    torsion and metricity against independently differentiated metric entries.
    """
    gamma = [sp.zeros(14) for _ in range(14)]
    for i in range(4):
        for j in range(4):
            if variation is None:
                value = -(h[:, i]*h[j, :]+h[:, j]*h[i, :])/4+h[i, j]*h/4
            else:
                v = variation
                value = -(v[:, i]*h[j, :]+h[:, i]*v[j, :]
                          +v[:, j]*h[i, :]+h[:, j]*v[i, :])/4
                value += (v[i, j]*h+h[i, j]*v)/4
            gamma[i][4:, j] = vertical_coordinates(value)
    for a, av in enumerate(BASIS):
        product = h_inverse*av/2 if variation is None else -h_inverse*variation*h_inverse*av/2
        for i in range(4):
            gamma[4+a][:4, i] = product[:, i]
            gamma[i][:4, 4+a] = product[:, i]
        for b, bv in enumerate(BASIS):
            if variation is None:
                value = -(av*h_inverse*bv+bv*h_inverse*av)/2
            else:
                value = (av*h_inverse*variation*h_inverse*bv
                         +bv*h_inverse*variation*h_inverse*av)/2
            gamma[4+a][4:, 4+b] = vertical_coordinates(value)
    return gamma


def geometry():
    h = h_inverse = ETA4
    g = metric(h, h_inverse)
    gamma = connection(h, h_inverse)
    first = [sp.zeros(14) for _ in range(4)] + [metric_derivative(h_inverse, a) for a in BASIS]
    dgamma = [[sp.zeros(14) for _ in range(14)] for _ in range(4)]
    dgamma += [connection(h, h_inverse, a) for a in BASIS]
    curvature = {(a, b): dgamma[a][b]-dgamma[b][a]+gamma[a]*gamma[b]-gamma[b]*gamma[a]
                 for a, b in combinations(range(14), 2)}
    def riemann(a, b):
        if a == b:
            return sp.zeros(14)
        return curvature[(a, b)] if a < b else -curvature[(b, a)]
    ricci = sp.Matrix(14, 14, lambda i, j: sum(riemann(k, j)[k, i] for k in range(14)))
    return g, first, gamma, curvature, ricci


def rational_frame(g):
    """A rational orthonormal frame; no square-root coefficient field needed."""
    vectors = []
    # Three trace-free diagonal matrices and the metric trace line.
    for signs in ((1,1,-1,-1), (1,-1,1,-1), (1,-1,-1,1), (1,1,1,1)):
        vectors.append(vertical_coordinates(ETA4*sp.diag(*signs)/2))
    positive, negative = vectors[:3], [vectors[3]]
    # Pair each norm +2 spatial off-diagonal with one norm -2 time-spatial.
    for p, n in zip(((1,2),(1,3),(2,3)), ((0,1),(0,2),(0,3))):
        vp, vn = sp.eye(10)[:, SLOTS.index(p)], sp.eye(10)[:, SLOTS.index(n)]
        positive.append((3*vp+vn)/4)
        negative.append((vp+3*vn)/4)
    return sp.diag(sp.eye(4), sp.Matrix.hstack(*(positive+negative)))


def certify():
    g, first, gamma, curvature, ricci = geometry()
    passed = []
    def check(label, condition):
        if not bool(condition):
            raise AssertionError(label)
        passed.append(label)

    check("connection is torsion free in every coordinate pair",
          all(gamma[a][:, b] == gamma[b][:, a] for a, b in combinations(range(14), 2)))
    check("connection is metric in all fourteen directions",
          all(first[a] == gamma[a].T*g+g*gamma[a] for a in range(14)))
    check("curvature is metric-skew in all ninety-one two-planes",
          all(r.T*g+g*r == sp.zeros(14) for r in curvature.values()))
    check("Ricci tensor is symmetric", ricci == ricci.T)
    def r(a, b):
        return curvature[(a,b)] if a < b else -curvature[(b,a)]
    check("full curvature satisfies every algebraic first Bianchi identity",
          all(r(a,b)[:,c]+r(b,c)[:,a]+r(c,a)[:,b] == sp.zeros(14,1)
              for a,b,c in combinations(range(14),3)))
    frame = rational_frame(g)
    eta = sp.diag(1,-1,-1,-1,1,1,1,1,1,1,-1,-1,-1,-1)
    check("rational frame has the selected K77 signature", frame.T*g*frame == eta)

    # A source metric rescaling leaves Gamma(g) invariant; in a fixed fibre
    # chart it leaves G_Y invariant. Moving the observation point h is distinct.
    scale = sp.symbols("scale", positive=True)
    observed_inverse = ETA4/scale
    dg = sp.diag(2, 3, -1, 4)
    check("constant rescaling cancels in the base Levi-Civita coefficient",
          observed_inverse*(scale*dg) == ETA4*dg)
    trace_normal = sp.zeros(14)
    for a, coeff in enumerate(vertical_coordinates(ETA4)):
        trace_normal += coeff*first[4+a]
    check("moving the fibre point retains the separate minus-eight density derivative",
          sp.trace(g.inv()*trace_normal)/2 == -8)

    # Purely vertical traceless two-plane. Its sectional curvature is -1/2.
    a = vertical_coordinates(sp.diag(0, 1, -1, 0))
    bv = sp.zeros(4); bv[1,2] = bv[2,1] = 1
    b = vertical_coordinates(bv)
    av, bv = sp.Matrix([0]*4+list(a)), sp.Matrix([0]*4+list(b))
    rab = sp.zeros(14)
    for i, j in combinations(range(14), 2):
        rab += (av[i]*bv[j]-av[j]*bv[i])*curvature[(i,j)]
    numerator = (av.T*g*rab*bv)[0]
    denominator = (av.T*g*av)[0]*(bv.T*g*bv)[0]-(av.T*g*bv)[0]**2
    check("vertical traceless plane has sectional curvature minus one half",
          numerator == -2 and denominator == 4)

    ricci_frame = frame.T*ricci*frame
    sharp = eta*ricci_frame
    check("horizontal and trace Ricci eigenvalue is one quarter, traceless is minus five quarters",
          sharp == sp.diag(*[sp.Rational(1 if mu < 4 or mu == 10 else -5,4) for mu in range(14)]))
    return {"checks_passed":len(passed), "checks":passed,
            "ricci_endomorphism":str(sharp),
            "ricci_eigenvalues":{str(k):v for k,v in sharp.eigenvals().items()},
            "scalar_curvature":str(sp.trace(sharp)),
            "vertical_sectional_curvature":"-1/2",
            "claim_ceiling":"Canonical connection-metric reconstruction only; source uniqueness, stationary I1B background and physical domain not established."}


if __name__ == "__main__":
    print(json.dumps(certify(),indent=2))
