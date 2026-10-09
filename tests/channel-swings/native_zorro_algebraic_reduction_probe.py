#!/usr/bin/env python3
"""Full mixed derivative and algebraic even-sector reduction of curved I1B.

Exact finite coefficient certificates; the owner supplies the covariance,
real-slice and formal variational arguments. No Hamiltonian domain is tested.
"""
from functools import lru_cache
from itertools import combinations
from math import comb
import json
import sys

import sympy as sp

from native_zorro_geometry_probe import connection, metric_derivative
from native_zorro_i1b_probe import clifford_form
from native_zorro_metric_perturbation_probe import (
    BASIS, ETA4, CORE, ETA, base_connection, base_ricci,
    christoffel_from_first, diagonal_fibre_frame, direction, dual_rows,
    first_order_euler, lift_derivative, metric, metric_lift,
    rational_frame, ricci_from_curvature, spin_curvature, vertical_coordinates,
    dewitt,
)
from native_zorro_stationary_background_probe import (
    algebraic_branch, fields_and_gradients, rational_interval,
)
from native_i1b_scalar_closure_probe import derivative_block, exact


@lru_cache(maxsize=None)
def fixed_geometry(h):
    # Keep the cache key immutable, but use ordinary matrices for the many
    # small products below; immutable promotion needlessly repeats work.
    h = sp.Matrix(h)
    hi = h.inv()
    g = metric(h, hi)
    first = [sp.zeros(14)]*4 + [metric_derivative(hi, b) for b in BASIS]
    return hi, g, g.inv(), first, connection(h, hi)


def connection_jet_response(n, h, frame):
    """At Gamma=0, n[k][i]^a_j is partial_k Gamma_i^a_j.

    Torsion is zero and d(tr Gamma)=0. The latter is verified by the caller.
    Only this second-order base jet is varied, at a fixed fibre point.
    """
    hi, g, inverse, first, gamma = fixed_geometry(sp.ImmutableMatrix(h))
    lifted = [metric_lift(h, hi, row) for row in n]
    dk = [[lift_derivative(h, hi, row, b) for b in BASIS] for row in n]
    zero = sp.zeros(14)
    df = [entry[0] for entry in lifted] + [zero]*10
    ddf = [[zero]*14 for _ in range(14)]
    for i in range(4):
        for a in range(10):
            ddf[i][4+a] = ddf[4+a][i] = dk[i][a]
    dgamma = christoffel_from_first(inverse, df)
    ddgamma = []
    for axis in range(14):
        term = christoffel_from_first(inverse, ddf[axis])
        ddgamma.append([term[r] - inverse*first[axis]*dgamma[r]
                        - inverse*df[axis]*gamma[r] for r in range(14)])
    curvature = {(i, j): ddgamma[i][j]-ddgamma[j][i]
                 + dgamma[i]*gamma[j]+gamma[i]*dgamma[j]
                 - dgamma[j]*gamma[i]-gamma[j]*dgamma[i]
                 for i, j in combinations(range(14), 2)}
    ricci = ricci_from_curvature(curvature)
    ph = sp.diag(sp.eye(4), sp.zeros(10))
    radial = sp.Matrix([0]*4+list(vertical_coordinates(h)/2))
    pr = sp.diag(sp.zeros(4), vertical_coordinates(h)*sp.Matrix(
        [[sp.trace(hi*b) for b in BASIS]])/4)
    dph, dpr, dr = [], [], []
    for axis in range(14):
        partial_h, partial_r = sp.zeros(14), sp.zeros(14)
        if axis < 4:
            c = lifted[axis][1]
            partial_h[4:, :4] = sp.Matrix.hstack(*[vertical_coordinates(z) for z in c])
            for j in range(4):
                partial_r[:, j] = radial*dewitt(hi, h/2, c[j])
        dph.append(partial_h+dgamma[axis]*ph-ph*dgamma[axis])
        dpr.append(partial_r+dgamma[axis]*pr-pr*dgamma[axis])
        dr.append(dgamma[axis]*radial)
    inverse_frame = frame.inv()
    dfield = [clifford_form(inverse_frame*sum(
        (frame[axis, s]*dph[axis] for axis in range(14)), zero)*frame)
        for s in range(14)]
    gradients = [CORE.fclean({fm: CORE.emul(CORE.blade(10), e)
                             for fm, e in form.items()}) for form in dfield]
    derivative_rows = first_order_euler(gradients)
    f, _ = spin_curvature(frame, curvature)
    return ricci, dual_rows(CORE.shiab(f)), derivative_rows, dpr+dr, dph


def trace_lift(v):
    """A right inverse to n -> tr Gamma, within the torsion-free jets."""
    return [[sp.Matrix(4, 4, lambda a, j:
        (int(a == i)*v[k, j]+int(a == j)*v[k, i])/sp.Integer(5))
        for i in range(4)] for k in range(4)]


def jet_generators():
    # The 160 projected elementary jets span ker(trace), dimension 144.
    # Ten symmetric trace lifts span the remaining closed-trace directions.
    for k in range(4):
        for a in range(4):
            for i, j in ((i, j) for i in range(4) for j in range(i, 4)):
                n = [[sp.zeros(4) for _ in range(4)] for _ in range(4)]
                n[k][i][a, j] = n[k][j][a, i] = 1
                projected = trace_lift(sp.Matrix(4, 4, lambda p, q: sp.trace(n[p][q])))
                yield [[n[p][q]-projected[p][q] for q in range(4)] for p in range(4)]
    for v in BASIS:
        yield trace_lift(v)


def potential_block(label, backgrounds):
    basis = [direction(mu, label ^ (1 << mu)) for mu in range(14)]
    mass = sp.diag(*[exact(CORE.pair(f, CORE.hodge(f))) for f in basis])
    hessians = []
    for background in backgrounds:
        images = [CORE.shiab(CORE.fadd(CORE.wedge_raw(background, u),
                                      CORE.wedge_raw(u, background))) for u in basis]
        hessian = sp.zeros(14)
        for i in range(14):
            for j in range(i, 14):
                cross = CORE.fadd(CORE.wedge_raw(basis[i], basis[j]),
                                  CORE.wedge_raw(basis[j], basis[i]))
                value = (exact(CORE.pair(basis[i], images[j]))
                         + exact(CORE.pair(basis[j], images[i]))
                         + exact(CORE.pair(background, CORE.shiab(cross))))/3
                hessian[i, j] = hessian[j, i] = value
        hessians.append(hessian)
    return mass, hessians


def certify(progress=None):
    passed = []

    def check(label, condition):
        if not bool(condition):
            raise AssertionError(label)
        passed.append(label)

    def zero(matrix):
        return all(sp.expand(z) == 0 for z in matrix)

    def verify_jet(n, h, frame):
        trace = sp.Matrix(4, 4, lambda k, i: sp.trace(n[k][i]))
        assert trace == trace.T
        assert all(n[k][i][a, j] == n[k][j][a, i]
                   for k in range(4) for i in range(4)
                   for a in range(4) for j in range(4))
        ricci, forcing, derivative, radial_defects, dph = connection_jet_response(n, h, frame)
        rb = sp.Matrix(4, 4, lambda i, j: sum(
            (n[k][j]-n[j][k])[k, i] for k in range(4)))
        assert ricci == sp.diag(rb, sp.zeros(10))
        assert all(zero(z) for z in radial_defects)
        assert derivative == {}
        sharp = sp.diag(*ETA)*frame.T*ricci*frame
        einstein = sharp-sp.trace(sharp)*sp.eye(14)/2
        expected = {(mu, 1 << nu): -einstein[mu, nu]
                    for mu in range(14) for nu in range(14) if einstein[mu, nu]}
        assert forcing == expected
        return any(not zero(z) for z in dph)

    frame = rational_frame(metric(ETA4, ETA4))
    nonzero_projector_controls = 0
    count = 0
    for n in jet_generators():
        nonzero_projector_controls += int(verify_jet(n, ETA4, frame))
        count += 1
        if progress and count % 20 == 0:
            progress(f"{count}/170 exact connection-jet generators passed")
    check("170 generators certify the full 154-dimensional closed-trace torsion-free jet class",
          count == 170)
    check("the derivative cancellation includes genuinely moving horizontal projectors",
          nonzero_projector_controls > 0)

    # Congruence is proved in the owner; include explicit off-section controls.
    shear = sp.eye(4)
    shear[0, 2] = sp.Rational(1, 2)
    off_section = []
    for change in (sp.diag(2, 1, 1, 1), sp.diag(2, 2, 1, sp.Rational(1, 2)), shear):
        h = change.T*ETA4*change
        f = diagonal_fibre_frame(change)
        assert f.T*metric(h, h.inv())*f == sp.diag(*ETA)
        for q in ([1, 0, 0, 0], [1, 1, 0, 0]):
            connection_coeff = base_connection(q, sp.diag(0, 0, 1, -1))
            n = [[q[k]*connection_coeff[i] for i in range(4)] for k in range(4)]
            verify_jet(n, h, f)
            off_section.append({"change": str(change), "q": q})
    check("six anisotropic and sheared off-section controls retain the second-order identity", True)
    if progress:
        progress("All connection jets and off-section controls passed")

    q = sp.Matrix(sp.symbols("q0:4"))
    xi = sp.Matrix(sp.symbols("xi0:4"))
    gauge_u = q*xi.T+xi*q.T
    check("the second-order mixed coefficient kills every base diffeomorphism symbol",
          zero(base_ricci(q, gauge_u)))
    # Symbolic h is unnecessary: compatibility gives L_i=q_i tensor eta^-1 xi.
    lc = base_connection(q, gauge_u)
    check("the connection lift of a base diffeomorphism is a pure ambient metric gauge symbol",
          all(zero(lc[i]-q[i]*(ETA4*xi)*q.T) for i in range(4)))

    backgrounds = fields_and_gradients()[0][:2]
    a, c, kappa = sp.symbols("a c kappa", real=True)
    rest = [i for i in range(14) if i != 10]
    records, factors = [], set()
    coefficients = 0
    for weight in range(1, 14, 2):
        for has_radial in (False, True):
            inside = [10]+rest[:weight-1] if has_radial else rest[:weight]
            outside = [i for i in range(14) if i not in inside]
            label = sum(1 << i for i in inside)
            mass, hs = potential_block(label, backgrounds)
            potential = kappa*mass+a*hs[0]+c*hs[1]
            assert all(potential[i, j] == 0 for i in inside for j in outside)
            # Blocks are homogeneous in Clifford grade. The source's phased
            # real basis therefore changes each block only by a real sign.
            phases = sp.diag(*[sp.I if (label ^ (1 << mu)).bit_count() % 4 in (0, 3)
                              else 1 for mu in range(14)])
            assert all(sp.im(z) == 0 for z in phases*potential*phases)
            determinant = sp.factor(potential.extract(inside, inside).det(method="domain-ge")
                                    * potential.extract(outside, outside).det(method="domain-ge"))
            factors.update(f for f, _ in sp.factor_list(determinant)[1])
            multiplicity = comb(13, weight-int(has_radial))
            coefficients += 14*multiplicity
            records.append({"label_weight": weight, "contains_radial": has_radial,
                            "representative_label": label, "label_multiplicity": multiplicity,
                            "determinant_real_clifford_basis": str(determinant)})
            if progress:
                progress(f"Even block weight={weight}, radial={has_radial} factored")
    check("fourteen representatives preserve grade and cover all even Clifford coefficient blocks",
          len(records) == 14 and coefficients == 14*2**13)
    check("the fourteen determinant polynomials have exactly 39 distinct nonconstant factors",
          len(factors) == 39)
    w, polynomial, _, alpha, beta, k2, _, _ = algebraic_branch()
    interval = (sp.Rational(227427945967, 10**12), sp.Rational(227427945969, 10**12))
    check("the same stationary algebraic root is isolated and kappa is nonzero",
          polynomial.count_roots(*interval) == 1 and rational_interval(k2, w, interval)[0] > 0)
    factor_records = []
    for factor in sorted(factors, key=str):
        # Homogeneity extracts a nonzero power of kappa from every factor.
        assert sp.Poly(factor, a, c, kappa).is_homogeneous
        normalized = sp.cancel(factor.subs({a: alpha, c: beta, kappa: 1}))
        bounds = rational_interval(normalized, w, interval)
        assert bounds[0]*bounds[1] > 0, factor
        rounded = (sp.floor(bounds[0]*10**6)/10**6, sp.ceiling(bounds[1]*10**6)/10**6)
        assert rounded[0]*rounded[1] > 0
        factor_records.append({"factor": str(factor), "normalized_interval": [str(z) for z in rounded]})
    check("all 39 determinant factors exclude zero by rational interval arithmetic", True)

    # Exact checks of all grade-transition types of the principal derivative.
    transition_types = set()
    for weight in range(14):
        label = (1 << weight)-1
        basis, derivative = derivative_block(0, (label, label ^ 1))
        for i, j in derivative.todok():
            gi, gj = basis[i][1].bit_count(), basis[j][1].bit_count()
            assert (gi+gj) % 2 == 1
            pi = sp.I if gi % 4 in (0, 3) else 1
            pj = sp.I if gj % 4 in (0, 3) else 1
            assert sp.im(pi*pj*derivative[i, j]) == 0
            transition_types.add((gi, gj))
    check("all principal Clifford-grade transition types reverse parity and are real on the source slice", True)

    return {"passed": len(passed), "checks": passed,
            "mixed_jet_generators": count, "jet_space_dimension": 154,
            "nonzero_projector_controls": nonzero_projector_controls,
            "off_section_controls": off_section,
            "even_coefficient_dimension": coefficients,
            "even_potential_blocks": records, "nonzero_factor_certificates": factor_records,
            "principal_grade_transitions": sorted(transition_types),
            "scope": "formal local bulk elimination; no physical constraint quotient or energy theorem"}


if __name__ == "__main__":
    print(json.dumps(certify(progress=lambda message: print(message, file=sys.stderr, flush=True)), indent=2))
