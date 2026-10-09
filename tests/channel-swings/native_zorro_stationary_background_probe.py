#!/usr/bin/env python3
"""Exact curved I1B background, with all distortion receivers checked.

The action, real packet and geometry are the declared K77 reconstruction.
This does not construct a physical Hamiltonian, observation quotient or QFT.
The accompanying owner gives the analytic epsilon and base-metric arguments;
the numerical-looking branch below is certified by rational root isolation.
"""

from fractions import Fraction
from itertools import combinations
import json

import sympy as sp

from native_zorro_geometry_probe import (
    BASIS, ETA4, geometry, rational_frame, vertical_coordinates,
)
from native_zorro_i1b_probe import (
    clifford_form, covariant_gradient, first_order_euler,
    invariant_projectors, spin_curvature,
)
from native_i1b_scalar_closure_probe import (
    CORE, ETA, cubic_gradient, direction, dual_rows, exact,
)


def fields_and_gradients():
    g, _, gamma, curvature, _ = geometry()
    frame = rational_frame(g)
    inverse = frame.inv()
    projectors = invariant_projectors()
    forms = [clifford_form(inverse*p*frame) for p, _ in projectors]
    gradients = [covariant_gradient(p, dp, gamma, frame)
                 for p, dp in projectors]
    radial = sp.Matrix([0]*4 + list(vertical_coordinates(ETA4)/2))
    first = [sp.zeros(14, 1) for _ in range(4)]
    first += [sp.Matrix([0]*4 + list(vertical_coordinates(b)/2)) for b in BASIS]
    nr = sp.Matrix.hstack(*(first[s]+gamma[s]*radial for s in range(14)))
    assert (radial.T*g*radial)[0] == -1
    assert inverse*radial == sp.eye(14)[:, 10]
    assert nr == projectors[0][0]/4, "independent coordinate derivative of r"

    # gamma(r) gamma(P_i .), i=H,V0; the factors are perpendicular.
    r = CORE.blade(10)
    mixed, mixed_grad = [], []
    for i in (0, 1):
        mixed.append(CORE.fclean({fm: CORE.emul(r, e) for fm, e in forms[i].items()}))
        col = []
        for s in range(14):
            dr = CORE.escale(Fraction(1, 4), CORE.blade(s)) if s < 4 else {}
            col.append(CORE.fadd(
                {fm: CORE.emul(dr, e) for fm, e in forms[i].items()},
                {fm: CORE.emul(r, e) for fm, e in gradients[i][s].items()},
            ))
        mixed_grad.append(col)
    # K_Hr = -(1/8) gamma(r) gamma(P_H .) is the spin lift of the
    # horizontal/trace part of the difference to the adapted connection.
    fields = [CORE.fadd(forms[0], forms[1]), forms[2],
              CORE.fscale(Fraction(-1, 8), mixed[0]), mixed[1]]
    deriv = [[CORE.fadd(gradients[0][s], gradients[1][s]) for s in range(14)],
             gradients[2],
             [CORE.fscale(Fraction(-1, 8), z) for z in mixed_grad[0]],
             mixed_grad[1]]
    f, _ = spin_curvature(frame, curvature)
    return fields, deriv, dual_rows(CORE.shiab(f))


def full_polynomials(fields, gradients, forcing):
    a, c, v, w, k = sp.symbols("a c v w kappa")
    variables = (a, c, v, w)
    linear = [first_order_euler(g) for g in gradients]
    mass = [dual_rows(CORE.hodge(f)) for f in fields]
    labels = [{fm ^ cm for fm, element in f.items() for cm in element} for f in fields]
    assert labels == [{0}, {0}, {1 << 10}, {1 << 10}]
    # For the diagonal Phi_i, Shiab preserves form XOR Clifford mask up
    # to the full exterior mask; the top-degree pairing cancels that mask.
    # Every cubic Euler receiver therefore has the XOR of two input labels.
    all_labels = {x ^ y for ls in labels for rs in labels for x in ls for y in rs}
    possible = {(mu, label ^ (1 << mu)) for label in all_labels for mu in range(14)}
    possible |= set(forcing).union(*(set(z) for z in linear+mass))
    rows = {}
    for row in sorted(possible):
        receiver = direction(*row)
        diagonal = [cubic_gradient(f, receiver) for f in fields]
        value = forcing.get(row, 0)
        value += sum(variables[i]*(linear[i].get(row, 0)+k*mass[i].get(row, 0))
                     + variables[i]**2*diagonal[i] for i in range(4))
        for i, j in combinations(range(4), 2):
            cross = cubic_gradient(CORE.fadd(fields[i], fields[j]), receiver)
            value += variables[i]*variables[j]*(cross-diagonal[i]-diagonal[j])
        value = sp.expand(value)
        if value != 0:
            rows[row] = value
    return rows, variables, k, linear, mass


def expected_polynomials(a, c, v, w, k):
    return [
        (4224*a*a+768*a*c+16*a*k+v*v-72*v*w-3*v+768*w*w+108*w-84)/16,
        (6336*a*a+1152*a*c+24*a*k+3*v*v-128*v*w-12*v+896*w*w+168*w-90)/24,
        (7488*a*a+24*c*k+v*v-144*v*w-6*v+864*w*w+216*w-126)/24,
        (132*a*v-3168*a*w+12*a+4*c*v-288*c*w-12*c+3*k*v)/24,
        (22*a*v-352*a*w+3*a+2*c*v-24*c*w-3*c-3*k*w)/3,
    ]


def iadd(x, y):
    return x[0]+y[0], x[1]+y[1]


def imul(x, y):
    z = [a*b for a in x for b in y]
    return min(z), max(z)


def idiv(x, y):
    assert y[0]*y[1] > 0, "interval denominator could vanish"
    return imul(x, (1/y[1], 1/y[0]))


def polynomial_interval(poly, var, interval):
    out = (sp.S.Zero, sp.S.Zero)
    for coefficient in sp.Poly(poly, var).all_coeffs():
        out = iadd(imul(out, interval), (coefficient, coefficient))
    return out


def rational_interval(expr, var, interval):
    numerator, denominator = sp.fraction(sp.cancel(expr))
    return idiv(polynomial_interval(numerator, var, interval),
                polynomial_interval(denominator, var, interval))


def algebraic_branch():
    v, w = sp.symbols("v w")
    matrix = sp.Matrix([[132*v-3168*w+12, 4*v-288*w-12],
                        [22*v-352*w+3, 2*v-24*w-3]])
    alpha, beta = [sp.factor(z) for z in matrix.inv()*sp.Matrix([-3*v, 3*w])]
    h = 4224*alpha**2+768*alpha*beta+16*alpha
    r = 7488*alpha**2+24*beta
    vh = v*v-72*v*w-3*v+768*w*w+108*w-84
    vr = v*v-144*v*w-6*v+864*w*w+216*w-126
    conic = 3*v*v-40*v*w-512*w*w-15*v+12*w+72
    compatibility = sp.fraction(sp.factor(vh*r-vr*h))[0]
    remainder = sp.Poly(sp.rem(compatibility, conic, v), v)
    vf = sp.cancel(-remainder.nth(0)/remainder.nth(1))
    resultant = sp.Poly(sp.resultant(conic, compatibility, v), w).primitive()[1]
    if resultant.LC() < 0:
        resultant = -resultant
    af = sp.cancel(alpha.subs(v, vf))
    bf = sp.cancel(beta.subs(v, vf))
    k2 = sp.cancel((-vh/h).subs(v, vf))
    return w, resultant, vf, af, bf, k2, conic, matrix.det()


def certify():
    passed = []

    def check(label, condition):
        if not bool(condition):
            raise AssertionError(label)
        passed.append(label)

    fields, gradients, forcing = fields_and_gradients()
    check("unit trace vector and its covariant derivative computed from the coordinate connection", True)
    check("four intrinsic fields and their gradients are real",
          all(z[1] == 0 for f in fields+[x for g in gradients for x in g]
              for e in f.values() for z in e.values()))
    rows, variables, k, linear, mass = full_polynomials(fields, gradients, forcing)
    a, c, v, w = variables
    expected = expected_polynomials(a, c, v, w, k)
    representatives = [(0, 1), (4, 16), (10, 1024), (0, 1025), (4, 1040)]
    check("all five representative equations come from the differentiated action",
          all(sp.expand(rows[r]-p) == 0 for r, p in zip(representatives, expected)))
    normalized = {sp.Poly(p, *variables, k).monic().as_expr() for p in expected}
    check("complete distortion image consists of 27 rows and exactly five equations",
          len(rows) == 27 and
          {sp.Poly(z, *variables, k).monic().as_expr() for z in rows.values()} == normalized)
    check("the only possible scalar receiver is identically zero", (10, 0) not in rows)
    check("no hidden linear receivers outside the declared image",
          set(forcing).union(*(set(p) for p in linear+mass)) <= set(rows))
    # Re-evaluate the derivative coefficients of the five decisive rows from
    # the two varied action terms, without the dual-row/XOR adjoint routine.
    direct = sp.zeros(5, 4)
    for i, row in enumerate(representatives):
        receiver = direction(*row)
        for j, grad in enumerate(gradients):
            for axis, value in enumerate(grad):
                left = CORE.shiab(CORE.wedge_raw(direction(axis, 0), value))
                right = CORE.shiab(CORE.wedge_raw(direction(axis, 0), receiver))
                direct[i, j] += (exact(CORE.pair(receiver, left))
                                 - exact(CORE.pair(value, right)))/2
    check("independent integration-by-parts evaluation matches every derivative coefficient",
          direct == sp.Matrix([[p.get(r, 0) for p in linear] for r in representatives]))
    mass_matrix = sp.Matrix(4, 4, lambda i, j: exact(CORE.pair(fields[i], CORE.hodge(fields[j]))))
    check("ansatz mass pairing has the declared normalization",
          mass_matrix == sp.diag(13, 1, sp.Rational(1, 16), 9))

    t, p, vf, af, bf, k2, conic, determinant = algebraic_branch()
    check("elimination gives a squarefree polynomial of degree ten",
          p.degree() == 10 and sp.gcd(p, p.diff()).degree() == 0)
    interval = (sp.Rational(227427945967, 10**12), sp.Rational(227427945969, 10**12))
    check("Sturm isolation certifies exactly one real root in the chosen rational interval",
          p.count_roots(*interval) == 1 and p.eval(interval[0])*p.eval(interval[1]) < 0)
    check("all rational branch denominators are coprime to the defining polynomial",
          all(sp.gcd(p, sp.Poly(sp.fraction(f)[1], t)).degree() == 0 for f in (vf, af, bf, k2)))
    intervals = {name: rational_interval(f, t, interval)
                 for name, f in (("v", vf), ("alpha", af), ("beta", bf), ("kappa_squared", k2))}
    det_interval = rational_interval(determinant.subs(v, vf), t, interval)
    h_interval = rational_interval(4224*af**2+768*af*bf+16*af, t, interval)
    check("the original linear solve and coupling formulas have nonzero denominators",
          det_interval[0]*det_interval[1] > 0 and h_interval[0]*h_interval[1] > 0)
    check("rational interval arithmetic certifies a positive nonzero real coupling",
          intervals["kappa_squared"][0] > 0)
    check("the selected branch is separated from the omitted-component family", interval[0] > 0)
    # Every equation is homogeneous in kappa or depends only on kappa^2
    # after a=kappa alpha, c=kappa beta. Reduce rational numerators modulo p.
    for i, eq in enumerate(expected):
        value = sp.Poly(eq.subs({a: k*af, c: k*bf, v: vf, w: t}), k)
        if i < 3:
            assert value.degree() <= 2 and value.nth(1) == 0
            residual = sp.cancel(value.nth(2)*k2+value.nth(0))
        else:
            assert value.degree() <= 1 and value.nth(0) == 0
            residual = sp.cancel(value.nth(1))
        numerator, denominator = sp.fraction(residual)
        check(f"stationary equation {i+1} vanishes exactly in the algebraic number field",
              sp.rem(numerator, p.as_expr(), t) == 0 and
              sp.gcd(p, sp.Poly(denominator, t)).degree() == 0)
    check("setting w to zero recovers a strictly positive obstruction",
          sp.expand((expected[1]-expected[0]).subs(w, 0)
                    - (v*v-5*v+24)/16) == 0)
    check("obstruction lower bound is 71/64 in the unscaled Euler difference",
          sp.expand((v*v-5*v+24)/16-((v-sp.Rational(5, 2))**2/16+sp.Rational(71, 64))) == 0)

    # A direct metric-jet control. For arbitrary constant observing g,
    # Gamma(g)=0 and the ambient metric has no undifferentiated g dependence.
    # The owner proves the all-orders local-density / compact-support argument.
    ds = sp.symbols("d0:40")
    dg = [sp.zeros(4) for _ in range(4)]
    slots = [(i, j) for i in range(4) for j in range(i, 4)]
    for s in range(4):
        for m, (i, j) in enumerate(slots):
            dg[s][i, j] = dg[s][j, i] = ds[10*s+m]
    delta_gamma = [sum(ETA4[l, m]*(dg[i][m, j]+dg[j][m, i]-dg[m][i, j])/2
                       for m in range(4))
                   for l in range(4) for i in range(4) for j in range(4)]
    check("linearized observing Levi-Civita coefficients contain first base derivatives only",
          all(sp.Poly(z, *ds).total_degree() <= 1 and z.subs(dict.fromkeys(ds, 0)) == 0
              for z in delta_gamma))
    midpoint = sum(interval)/2
    approximations = {name: str(sp.N(f.subs(t, midpoint), 12))
                      for name, f in (("w", t), ("v", vf), ("alpha", af), ("beta", bf), ("kappa_squared", k2))}
    return {
        "result_id": "NATIVE-ZORRO-STATIONARY-BACKGROUND",
        "checks_passed": len(passed), "checks": passed,
        "selected_shiab": ["comm", "symi", "symi"], "sympy_version": sp.__version__,
        "full_distortion_rows": len(rows),
        "equations": [str(sp.factor(z)) for z in expected],
        "defining_polynomial": str(p.as_expr()),
        "root_interval": list(map(str, interval)),
        "rational_parameter_formulas": {"v": str(vf), "alpha": str(af), "beta": str(bf), "kappa_squared": str(k2)},
        "certified_intervals": {name: list(map(str, bound)) for name, bound in intervals.items()},
        "approximations_for_orientation_only": approximations,
        "analytic_obligations_in_owner": [
            "XOR support completeness", "affine isometry transport of the local solution",
            "epsilon dressing identity", "observing-metric first variation on the product patch",
        ],
        "claim_ceiling": "Selected reconstructed local stationary bosonic background; no global action domain, physical reduction, positive conserved pairing, semibounded Hamiltonian or quantum claim.",
    }


if __name__ == "__main__":
    print(json.dumps(certify(), indent=2))
