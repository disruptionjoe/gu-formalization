#!/usr/bin/env python3
"""Full curvature forcing and invariant grade-one tests for reconstructed I1B.

This uses the canonical connection metric with flat observing metric, not a
flat fourteen-dimensional surrogate. All calculations are exact rationals.
"""
from fractions import Fraction
from itertools import combinations
import json

import sympy as sp

from native_zorro_geometry_probe import (BASIS, ETA4, geometry, rational_frame,
                                         vertical_coordinates)
from native_i1b_scalar_closure_probe import (CORE, ETA, cubic_gradient,
                                            direction, dual_rows, exact)


def clifford_form(matrix):
    """matrix[nu,mu] is the gamma_nu coefficient of the mu one-form."""
    result = {}
    for nu, mu in matrix.todok():
        result = CORE.fadd(result, CORE.fscale(Fraction(matrix[nu, mu]), direction(mu, 1 << nu)))
    return result


def spin_curvature(frame, curvature):
    inverse = frame.inv()
    frames, result = {}, {}
    for mu, nu in combinations(range(14), 2):
        r = sp.zeros(14)
        for i, j in combinations(range(14), 2):
            coefficient = frame[i, mu]*frame[j, nu]-frame[j, mu]*frame[i, nu]
            if coefficient:
                r += coefficient*curvature[(i, j)]
        r = inverse*r*frame
        frames[(mu, nu)] = r
        element = {}
        for a, b in combinations(range(14), 2):
            coefficient = r[a, b]*ETA[b]/2
            if coefficient:
                element = CORE.eadd(element, CORE.escale(Fraction(coefficient), CORE.blade((a, b))))
        if element:
            result[(1 << mu) | (1 << nu)] = element
    return result, frames


def invariant_projectors():
    horizontal = sp.diag(sp.eye(4), sp.zeros(10))
    row = sp.Matrix([[sp.trace(ETA4*b) for b in BASIS]])
    trace = sp.diag(sp.zeros(4), vertical_coordinates(ETA4)*row/4)
    trace_first = [sp.zeros(14) for _ in range(4)]
    for a in BASIS:
        first_row = sp.Matrix([[-sp.trace(ETA4*a*ETA4*b) for b in BASIS]])
        trace_first.append(sp.diag(sp.zeros(4),
            (vertical_coordinates(a)*row+vertical_coordinates(ETA4)*first_row)/4))
    zero = [sp.zeros(14) for _ in range(14)]
    return [(horizontal, zero), (sp.eye(14)-horizontal-trace, [-x for x in trace_first]),
            (trace, trace_first)]


def covariant_gradient(projector, first, gamma, frame):
    inverse = frame.inv()
    coordinate = [first[a]+gamma[a]*projector-projector*gamma[a] for a in range(14)]
    return [clifford_form(inverse*sum((frame[a, mu]*coordinate[a] for a in range(14)), sp.zeros(14))*frame)
            for mu in range(14)]


def first_order_euler(gradient):
    """Formal covariant adjoint of 1/2<T,S(DT)> before any restriction.

    Phi and Hodge are parallel for the spin Levi-Civita connection. In a
    normal orthonormal frame the Euler derivative is (raw-raw^transpose)/2.
    XOR selection identifies every possible adjoint receiver, of any grade.
    """
    dt = {}
    for axis, value in enumerate(gradient):
        dt = CORE.fadd(dt, CORE.wedge_raw(direction(axis, 0), value))
    rows = {r: v/2 for r, v in dual_rows(CORE.shiab(dt)).items()}
    for axis, value in enumerate(gradient):
        labels = {form ^ mask ^ (1 << axis) for form, element in value.items() for mask in element}
        for label in labels:
            for mu in range(14):
                mask = label ^ (1 << mu)
                receiver = direction(mu, mask)
                image = CORE.shiab(CORE.wedge_raw(direction(axis, 0), receiver))
                contribution = exact(CORE.pair(value, image))/2
                if contribution:
                    rows[(mu, mask)] = rows.get((mu, mask), 0)-contribution
    return {r: sp.factor(v) for r, v in rows.items() if v}


def certify():
    passed = []
    def check(label, condition):
        if not bool(condition):
            raise AssertionError(label)
        passed.append(label)
    g, first, gamma, curvature, ricci = geometry()
    frame = rational_frame(g)
    f, riemann = spin_curvature(frame, curvature)
    for pair, r in riemann.items():
        element = f.get((1 << pair[0]) | (1 << pair[1]), {})
        for c in range(14):
            gc = CORE.blade((c,))
            commutator = CORE.eadd(CORE.emul(element, gc), CORE.escale(-1, CORE.emul(gc, element)))
            expected = {}
            for a in range(14):
                if r[a, c]:
                    expected = CORE.eadd(expected, CORE.escale(Fraction(r[a, c]), CORE.blade((a,))))
            assert commutator == expected, (pair, c)
    check("spin curvature induces every full tangent curvature matrix", True)
    forcing = dual_rows(CORE.shiab(f))
    expected = {(mu, 1 << mu): -sp.Rational(21 if mu < 4 or mu == 10 else 15, 4)
                for mu in range(14)}
    check("complete I1B curvature forcing has only fourteen grade-one rows", forcing == expected)
    sharp = sp.diag(*ETA)*frame.T*ricci*frame
    einstein = sharp-sp.trace(sharp)*sp.eye(14)/2
    check("direct Shiab contraction equals the separately computed negative Einstein endomorphism",
          einstein == sp.diag(*[-forcing[(mu, 1 << mu)] for mu in range(14)]))
    check("zero distortion is not stationary on the canonical curved geometry", forcing != {})
    check("parallel radial distortion cannot cancel unequal curvature forcing",
          forcing[(0, 1)]-forcing[(4, 1 << 4)] == -sp.Rational(3, 2))

    projectors = invariant_projectors()
    check("horizontal, vertical-traceless and vertical-trace projectors resolve identity",
          sum((p for p, _ in projectors), sp.zeros(14)) == sp.eye(14)
          and all(p*p == p for p, _ in projectors))
    gradients = [covariant_gradient(p, dp, gamma, frame) for p, dp in projectors]
    check("sum of the three fields is the covariantly parallel solder form",
          all(CORE.fadd(CORE.fadd(gradients[0][a], gradients[1][a]), gradients[2][a]) == {}
              for a in range(14)))
    columns = [first_order_euler(grad) for grad in gradients]
    labels = sorted(set().union(*(set(c) for c in columns)))
    matrix = sp.Matrix([[c.get(r, 0) for c in columns] for r in labels])
    check("derivative Euler forcing is confined to Clifford grade two",
          all(mask.bit_count() == 2 for _, mask in labels))
    check("derivative forcing annihilates the common radial coefficient", matrix*sp.ones(3, 1) == sp.zeros(len(labels), 1))
    check("all invariant grade-one derivative equations force equal coefficients",
          matrix.rank() == 2 and matrix.nullspace() == [sp.ones(3, 1)])
    # Two necessary normal equations already have rank two. Their algebraic
    # cubic terms vanish, checked by complete quadratic polarization in the
    # three coefficients. No nonlinear truncation assumption enters.
    test_rows = [(0, 17), (0, 1025)]
    direct = sp.zeros(2, 3)
    for i, row in enumerate(test_rows):
        receiver = direction(*row)
        for j, gradient in enumerate(gradients):
            for axis, value in enumerate(gradient):
                # Recompute these decisive rows without XOR receiver routing
                # or dual_rows, from the two terms in the varied functional.
                left = CORE.shiab(CORE.wedge_raw(direction(axis,0), value))
                right = CORE.shiab(CORE.wedge_raw(direction(axis,0), receiver))
                direct[i,j] += (exact(CORE.pair(receiver,left))-exact(CORE.pair(value,right)))/2
    check("two explicit normal equations independently have rank two",
          [columns[j].get(test_rows[0], 0) for j in range(3)] == [-sp.Rational(1,2),sp.Rational(1,2),0]
          and [columns[j].get(test_rows[1], 0) for j in range(3)] == [sp.Rational(1,2),0,-sp.Rational(1,2)]
          and direct == sp.Matrix([[-sp.Rational(1,2),sp.Rational(1,2),0],
                                  [sp.Rational(1,2),0,-sp.Rational(1,2)]]))
    fields = [clifford_form(frame.inv()*p*frame) for p, _ in projectors]
    polarized = fields+[CORE.fadd(fields[i], fields[j]) for i,j in combinations(range(3),2)]
    check("curvature, cubic and mass cannot cancel the two necessary bivector equations",
          all(cubic_gradient(t, direction(*r)) == 0
              and exact(CORE.pair(direction(*r), CORE.hodge(t))) == 0
              and forcing.get(r, 0) == 0 for t in polarized for r in test_rows))
    check("every radial cubic normal row is 312 and every radial mass row is one",
          all(cubic_gradient(CORE.phi1, direction(mu,1<<mu)) == 312
              and exact(CORE.pair(direction(mu,1<<mu), CORE.hodge(CORE.phi1))) == 1
              for mu in range(14)))

    # A compact bump supported away from the observation section has zero
    # section jets of every order. These two coefficient directions provide
    # opposite nonzero quadratic action values on that observation kernel.
    # This is action non-descent, not a Hamiltonian instability argument.
    invisible = [direction(0,1<<4), direction(0,1<<10)]
    check("observation-invisible rank-one carriers have opposite Hodge norms",
          [exact(CORE.pair(t,CORE.hodge(t))) for t in invisible] == [1,-1])
    check("rank-one invisible fields have identically zero cubic term",
          all(CORE.wedge_raw(t,t) == {} for t in invisible))
    # Every homogeneous Shiab summand contains an odd total number of Phi
    # Clifford factors. It reverses Clifford parity. A covariant derivative
    # preserves the grade-one bundle, hence <T,S(DT)> vanishes for grade-one
    # T even when the local frame and bump vary. Direct basis witnesses:
    check("grade-one derivative witnesses have even Clifford parity after Shiab",
          all(all(mask.bit_count()%2 == 0 for element in
                  CORE.shiab(CORE.wedge_raw(direction(axis,0),t)).values() for mask in element)
              for axis in range(14) for t in invisible))
    return {"checks_passed":len(passed), "checks":passed,
            "curvature_forcing":{"horizontal_and_trace":"-21/4", "vertical_traceless":"-15/4"},
            "first_order_rank":matrix.rank(),
            "first_order_nullspace":[list(map(str,x)) for x in matrix.nullspace()],
            "invariant_grade_one_verdict":"No constant horizontal/traceless/trace coefficient triple solves the full distortion equations, for any real kappa.",
            "observation_kernel_quadratic_action":"+kappa and -kappa times the same positive bump norm; not a Hamiltonian claim",
            "first_order_rows":[[mu, mask, list(map(str,matrix[i,:]))] for i,(mu,mask) in enumerate(labels)],
            "claim_ceiling":"Canonical reconstructed geometry; necessary full I1B distortion equations only; no physical-state or Hamiltonian construction."}

if __name__ == "__main__":
    print(json.dumps(certify(), indent=2))
