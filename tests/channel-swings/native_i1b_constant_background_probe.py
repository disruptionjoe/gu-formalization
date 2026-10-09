#!/usr/bin/env python3
"""Exact necessary equations for constant backgrounds of the selected I1B.

Flat geometry, constant coefficients, full metric variation, kappa != 0.
The five pulled-back distortion rows are necessary, not asserted sufficient.
Their ideal together with the metric trace contains every field amplitude.
This is a background obstruction, not a GU physical-domain theorem.
"""

from itertools import combinations_with_replacement
import json

import sympy as sp

from native_i1b_scalar_closure_probe import CORE, cubic_gradient, direction, exact


def field_basis():
    fields = [direction(0, 1)]
    for axes, offset in ((range(1, 4), 0), (range(4, 14), 0),
                         (range(1, 4), 1), (range(4, 14), 1)):
        fields.append(CORE.fadd(*[direction(mu, (1 << mu) ^ offset) for mu in axes]))
    return fields


def action_polynomials(fields, variables):
    """Polarize the actual Clifford action, with its 1/3 coefficient."""
    cubic = 0
    for j, k in combinations_with_replacement(range(len(fields)), 2):
        packet = CORE.wedge_raw(fields[j], fields[k])
        if j != k:
            packet = CORE.fadd(packet, CORE.wedge_raw(fields[k], fields[j]))
        image = CORE.shiab(packet)
        for i, field in enumerate(fields):
            cubic += exact(CORE.pair(field, image)) * variables[i] * variables[j] * variables[k] / 3
    norm = sum(exact(CORE.pair(left, CORE.hodge(right))) * variables[i] * variables[j]
               for i, left in enumerate(fields) for j, right in enumerate(fields))
    return sp.expand(cubic), sp.expand(norm)


def metric_density_row():
    """Differentiate the actual ten-dimensional DeWitt Gram, not a 14D Weyl guess."""
    inverse = sp.diag(1, -1, -1, -1)
    slots = [(i, j) for i in range(4) for j in range(i, 4)]
    basis = []
    for i, j in slots:
        h = sp.zeros(4)
        h[i, j] = h[j, i] = 1
        basis.append(h)

    def dewitt(k, l):
        return sp.trace(inverse*k*inverse*l) - sp.trace(inverse*k)*sp.trace(inverse*l)/2

    gram = sp.Matrix(10, 10, lambda i, j: dewitt(basis[i], basis[j]))
    gram_inverse = gram.inv()
    row = []
    for h in basis:
        di = -inverse*h*inverse

        def varied(k, l):
            return (sp.trace(di*k*inverse*l + inverse*k*di*l)
                    - (sp.trace(di*k)*sp.trace(inverse*l)
                       + sp.trace(inverse*k)*sp.trace(di*l))/2)

        derivative = sp.Matrix(10, 10, lambda i, j: varied(basis[i], basis[j]))
        row.append((sp.trace(inverse*h) + sp.trace(gram_inverse*derivative))/2)
    return gram, sp.Matrix(row)


def certify():
    passed = []

    def check(label, condition):
        if not bool(condition):
            raise AssertionError(label)
        passed.append(label)

    def zero(expression):
        return sp.expand(expression) == 0

    gram, rho = metric_density_row()
    check("DeWitt fibre determinant and selected real signature",
          gram.det() == 64 and gram.eigenvals() == {1: 3, -1: 1, -2: 3, 2: 3})
    check("all ten metric density derivatives derived from the DeWitt definition",
          rho == sp.Matrix([-2, 0, 0, 0, 2, 0, 0, 2, 0, 2]))
    conformal = sp.Matrix([1, 0, 0, 0, -1, 0, 0, -1, 0, -1])
    check("induced four-plus-ten conformal density variation is minus eight",
          (rho.T*conformal)[0] == -8)
    s = sp.symbols("s", positive=True)
    check("finite conformal scaling independently reproduces the density derivative",
          sp.diff(s**sp.Rational(4-20, 2), s).subs(s, 1) == -8)

    a, b, d, u, w = variables = sp.symbols("a b d u w", real=True)
    kap, t = sp.symbols("kappa t", real=True)
    fields = field_basis()
    cubic, norm = action_polynomials(fields, variables)
    expected = (12*a*b*b + 120*a*b*d + 180*a*d*d - 40*a*u*w - sp.Rational(140, 3)*a*w*w
                + 4*b**3 + 120*b*b*d + 540*b*d*d - 4*b*u*u - 80*b*u*w - 180*b*w*w
                + 480*d**3 - 40*d*u*u - 360*d*u*w - 480*d*w*w)
    check("five-field cubic derived from selected Shiab transgression", zero(cubic-expected))
    check("five-field Hodge form retains negative bivector directions",
          norm == a*a+3*b*b+10*d*d-3*u*u-10*w*w)
    diagonal_fields = [direction(mu, 1 << mu) for mu in range(14)]
    diagonal_gram = sp.Matrix(14, 14, lambda i, j:
                             exact(CORE.pair(diagonal_fields[i], CORE.hodge(diagonal_fields[j]))))
    check("all fourteen diagonal grade-one distortions have positive Hodge form",
          diagonal_gram == sp.eye(14))

    lagrangian = cubic+kap*norm/2
    rows = [sp.diff(lagrangian, x) for x in variables]
    check("Euler homogeneity supplies the metric-trace identity",
          zero(3*lagrangian-sum(x*row for x, row in zip(variables, rows))-kap*norm/2))
    radial = {a:t, b:t, d:t, u:0, w:0}
    check("radial restriction reproduces the predecessor action",
          zero(lagrangian.subs(radial)-1456*t**3-7*kap*t*t))
    root = {a:-kap/312, b:-kap/312, d:-kap/312, u:0, w:0}
    check("nonzero radial root satisfies every tested distortion row",
          all(zero(row.subs(root)) for row in rows))
    root_density = sp.factor(lagrangian.subs(root))
    check("same radial root has a nonzero action density for nonzero kappa",
          root_density == 7*kap**3/292032)
    check("radial root has nonzero conformal metric Euler response",
          (rho.T*conformal)[0]*root_density == -7*kap**3/36504)

    isotropic = {d:b, w:u}
    check("independent longitudinal field and common bivector reproduce three-field polynomial",
          zero(cubic.subs(isotropic)-(312*a*b*b-sp.Rational(260, 3)*a*u*u
                                     +1144*b**3-1144*b*u*u)))

    # A separately differentiated full-action receiver check. These are
    # sums of normal equations, which suffice to reject backgrounds.
    sample = (2, -1, 3, 1, -2)
    sample_map = dict(zip(variables, sample))
    field = CORE.fadd(*[CORE.fscale(coefficient, f) for coefficient, f in zip(sample, fields)])
    check("polarization agrees with direct scalar-action evaluation",
          cubic.subs(sample_map) == exact(CORE.pair(field, CORE.shiab(CORE.wedge_raw(field, field))))/3)
    for i, receiver in enumerate(fields):
        check(f"normal action variation independently reproduces necessary distortion row {i+1}",
              sp.diff(cubic, variables[i]).subs(sample_map) == cubic_gradient(field, receiver))

    # Nonzero kappa of either sign is removed by T=kappa X; no sign choice
    # and no division by any field amplitude enters the ideal computation.
    scaled = {x:kap*x for x in variables}
    unit_rows = [row.subs(kap, 1) for row in rows]
    check("nonzero kappa scaling preserves all five equations with factor kappa squared",
          all(zero(row.subs(scaled, simultaneous=True)-kap**2*unit)
              for row, unit in zip(rows, unit_rows)))
    check("metric trace and norm constraints are equivalent on distortion stationarity",
          zero((3*lagrangian-sum(x*row for x, row in zip(variables, rows))).subs(kap, 1)-norm/2))
    basis = sp.groebner(unit_rows+[norm], *variables, order="grevlex", domain=sp.QQ)
    check("exact rational stationary ideal contains every amplitude",
          [p.as_expr() for p in basis.polys] == list(variables))
    check("the zero background satisfies the original equations and metric trace",
          all(row.subs(dict.fromkeys(variables, 0)) == 0 for row in rows)
          and lagrangian.subs(dict.fromkeys(variables, 0)) == 0)

    # Scope controls: neither positivity nor the metric equation is silently
    # assumed, and the zero-coupling stratum is explicitly outside the theorem.
    null_example = {a:3, b:1, d:0, u:2, w:0}
    check("the enlarged real carrier has nonzero Hodge-null vectors",
          norm.subs(null_example) == 0 and any(row.subs(null_example).subs(kap, 1) != 0 for row in rows))
    check("dropping the metric equation admits the rejected nonzero radial root",
          norm.subs(root) == 7*kap**2/48672)
    kappa_zero_example = {a:1, b:0, d:0, u:0, w:0, kap:0}
    check("kappa zero admits a nonzero solution of the necessary equations and is excluded",
          all(row.subs(kappa_zero_example) == 0 for row in rows)
          and lagrangian.subs(kappa_zero_example) == 0)

    return {
        "result_id": "NATIVE-I1B-CONSTANT-BACKGROUND",
        "checks_passed": len(passed), "checks": passed,
        "sympy_version": sp.__version__,
        "cubic": str(cubic), "hodge_norm": str(norm),
        "metric_density_row": list(map(str, rho)),
        "radial_nonzero_density": str(root_density),
        "stationary_ideal_generators": [str(p.as_expr()) for p in basis.polys],
        "necessary_equations": [str(row) for row in rows],
        "claim_ceiling": "No nonzero constant flat background in the declared five-field family for real kappa != 0; no general GU no-go or physical-domain conclusion.",
    }


if __name__ == "__main__":
    print(json.dumps(certify(), indent=2))
