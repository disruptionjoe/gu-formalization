#!/usr/bin/env python3
"""Exact primary-constraint potential and a reduced-energy witness for I1B.

The owner proves the geometric kernel lemma, compact-support energy bound
and observation statements. This script checks their finite coefficient
inputs at the previously certified real stationary algebraic branch.
"""
from fractions import Fraction
from functools import lru_cache
from math import comb
import hashlib
import json
import sys

import sympy as sp
from sympy.polys.matrices import DomainMatrix

from native_i1b_scalar_closure_probe import CORE, derivative_block, direction, exact
from native_zorro_stationary_background_probe import (
    algebraic_branch, expected_polynomials, fields_and_gradients, rational_interval,
)


SPATIAL = (1, 2, 3)
VERTICAL = (4, 5, 6, 7, 8, 9, 11, 12, 13)
RADIAL = 10


@lru_cache(maxsize=1)
def background_fields():
    return fields_and_gradients()[0]


@lru_cache(maxsize=None)
def constraint_block(horizontal_weight, vertical_weight):
    label = sum(1 << i for i in SPATIAL[:horizontal_weight]+VERTICAL[:vertical_weight])
    labels = [label, label ^ 1, label ^ (1 << RADIAL), label ^ 1 ^ (1 << RADIAL)]
    basis, derivative = derivative_block(0, labels)
    selected = [i for i, (_, mask) in enumerate(basis) if mask.bit_count() % 4 in (0, 3)]
    basis = [basis[i] for i in selected]
    derivative = derivative.extract(selected, selected)
    null = derivative.nullspace()
    kernel = sp.Matrix.hstack(*null)
    forms = []
    for column in null:
        form = {}
        for i, value in enumerate(column):
            if value:
                form = CORE.fadd(form, CORE.fscale(Fraction(value), direction(*basis[i])))
        forms.append(form)
    mass = sp.Matrix(len(forms), len(forms), lambda i, j:
                     exact(CORE.pair(forms[i], CORE.hodge(forms[j]))))
    hessians = []
    for background in background_fields():
        images = [CORE.shiab(CORE.fadd(CORE.wedge_raw(background, u),
                                      CORE.wedge_raw(u, background))) for u in forms]
        hessian = sp.zeros(len(forms))
        for i in range(len(forms)):
            for j in range(i, len(forms)):
                cross = CORE.fadd(CORE.wedge_raw(forms[i], forms[j]),
                                  CORE.wedge_raw(forms[j], forms[i]))
                value = (exact(CORE.pair(forms[i], images[j]))
                         + exact(CORE.pair(forms[j], images[i]))
                         + exact(CORE.pair(background, CORE.shiab(cross))))/3
                hessian[i, j] = hessian[j, i] = value
        hessians.append(hessian)
    return {"labels": labels, "basis": basis, "derivative": derivative,
            "kernel": kernel, "mass": mass, "hessians": hessians}


def stationary_field():
    w, polynomial, v, alpha, beta, k2, _, _ = algebraic_branch()
    interval = (sp.Rational(227427945967, 10**12), sp.Rational(227427945969, 10**12))
    assert polynomial.count_roots(*interval) == 1
    assert rational_interval(k2, w, interval)[0] > 0
    index = int(polynomial.count_roots(-sp.oo, interval[0]))
    root = sp.CRootOf(polynomial.as_expr(), index)
    field = sp.QQ.algebraic_field(root)
    theta = field.from_sympy(root)
    # The field must use this complete degree-ten minimal polynomial,
    # not an approximate root or an unrelated formal quotient.
    modulus = [sp.Rational(x) for x in field.mod.to_list()]
    assert [x/modulus[0] for x in modulus] == polynomial.monic().all_coeffs()

    def evaluate(expression):
        numerator, denominator = sp.fraction(sp.cancel(expression))
        def horner(part):
            value = field.zero
            for coefficient in sp.Poly(part, w).all_coeffs():
                value = value*theta+field.from_sympy(coefficient)
            return value
        return horner(numerator)/horner(denominator)

    values = [evaluate(x) for x in (alpha, beta, v, w, k2)]
    return field, values, {"minimal_polynomial": str(polynomial.as_expr()),
                           "root_index": index, "isolating_interval": [str(x) for x in interval],
                           "kappa_branch": "both nonzero square roots of the certified kappa_squared"}


def exact_potential_determinant(block, field, parameters):
    alpha, beta, v, w, k2 = parameters
    basis, kernel = block["basis"], block["kernel"]
    mass = block["mass"]
    ha, hc, hv, hw = block["hessians"]
    parities = []
    for j in range(kernel.cols):
        seen = {basis[i][1].bit_count() % 2 for i in range(kernel.rows) if kernel[i, j]}
        assert len(seen) == 1
        parities.append(seen.pop())
    entries = []
    for i in range(kernel.cols):
        row = []
        for j in range(kernel.cols):
            if parities[i] == parities[j]:
                assert hv[i, j] == hw[i, j] == 0
                value = field.from_sympy(mass[i, j])+alpha*field.from_sympy(ha[i, j])
                value += beta*field.from_sympy(hc[i, j])
                if parities[i] == 0:
                    value *= k2
            else:
                assert mass[i, j] == ha[i, j] == hc[i, j] == 0
                value = v*field.from_sympy(hv[i, j])+w*field.from_sympy(hw[i, j])
            row.append(value)
        entries.append(row)
    # Congruence multiplies the even kernel vectors by kappa and then
    # divides the whole matrix by kappa. Every remaining entry is in Q(w).
    size = kernel.cols
    determinant = DomainMatrix(entries, (size, size), field).det()
    assert determinant != field.zero
    coefficients = [str(x) for x in determinant.to_list()]
    return {"degree_of_reduced_determinant": len(coefficients)-1,
            "determinant_coefficients_sha256": hashlib.sha256(
                json.dumps(coefficients, separators=(",", ":")).encode()).hexdigest(),
            "nonzero_in_selected_number_field": True}


def certify(progress=None):
    passed = []
    def check(label, condition):
        if not bool(condition):
            raise AssertionError(label)
        passed.append(label)

    field, parameters, branch = stationary_field()
    check("the selected stationary root defines the exact degree-ten number field and positive kappa squared", True)
    a, c, v, w, k = sp.symbols('a c v w kappa')
    equations = expected_polynomials(a, c, v, w, k)
    mirror_parities = [1, 1, 1, -1, -1]
    check("both coupling branches are stationary under simultaneous reversal of a c and kappa",
          all(sp.expand(eq.subs({a: -a, c: -c, k: -k}, simultaneous=True)-sign*eq) == 0
              for eq, sign in zip(equations, mirror_parities)))
    records = []
    total_coefficients = total_kernel = 0
    for nh in range(4):
        for nv in range(10):
            block = constraint_block(nh, nv)
            e, n = block["derivative"], block["kernel"]
            assert e.T == -e and e*n == sp.zeros(e.rows, n.cols)
            assert n.rank() == n.cols and e.rank()+n.cols == e.rows
            assert all(h.T == h for h in [block["mass"]]+block["hessians"])
            # Each time-kernel column has one Clifford parity. The mirror
            # potential is -P W P: diagonal parity blocks change sign,
            # while grade-two background cross blocks are unchanged.
            parities = []
            for j in range(n.cols):
                grades = {(-1)**block['basis'][i][1].bit_count()
                          for i in range(n.rows) if n[i, j]}
                assert len(grades) == 1
                parities.append(grades.pop())
            parity = sp.diag(*parities)
            assert all(parity*h*parity == h for h in [block['mass']]+block['hessians'][:2])
            assert all(parity*h*parity == -h for h in block['hessians'][2:])
            determinant = exact_potential_determinant(block, field, parameters)
            multiplicity = comb(3, nh)*comb(9, nv)
            total_coefficients += multiplicity*e.rows
            total_kernel += multiplicity*n.cols
            records.append({"horizontal_weight": nh, "vertical_weight": nv,
                            "multiplicity": multiplicity, "coefficient_dimension": e.rows,
                            "kernel_dimension": n.cols, **determinant})
            if progress:
                progress(f"Exact primary-potential block ({nh},{nv}) passed")
    check("forty symmetry classes cover every imaginary-packet coefficient and primary kernel",
          len(records) == 40 and total_coefficients == 14*sum(
              comb(14, k) for k in range(15) if k % 4 in (0, 3))
          and sum(r["multiplicity"] for r in records) == 2**12)
    check("all forty primary-potential determinants are nonzero in the selected number field", True)
    check("all forty mirror potentials are negative congruences and remain invertible", True)

    source = constraint_block(0, 0)
    s = sp.zeros(len(source["basis"]), 1)
    s[source["basis"].index((RADIAL, 0))] = 1
    companion = source["derivative"]*s
    check("the radial scalar one-form is a genuine dynamical direction",
          companion != sp.zeros(companion.rows, 1)
          and source["kernel"].T*s == sp.zeros(source["kernel"].cols, 1))
    check("a nonzero time symplectic partner exists",
          (s.T*source["derivative"]*companion)[0] == -48)

    witnesses = []
    for axis, weights, sign in [(4, (0, 1), 1), (1, (1, 0), -1)]:
        target = constraint_block(*weights)
        labels = source["labels"]+target["labels"]
        basis, spatial_derivative = derivative_block(axis, labels)
        source_indices = [basis.index(x) for x in source["basis"]]
        target_indices = [basis.index(x) for x in target["basis"]]
        cross = spatial_derivative.extract(target_indices, source_indices)
        check(f"axis {axis}: spatial derivative pairs primary kernel vectors to zero",
              target["kernel"].T*cross*source["kernel"]
              == sp.zeros(target["kernel"].cols, source["kernel"].cols))
        force = target["kernel"].T*cross*s
        nonzero = [j for j in range(force.rows) if force[j]]
        assert len(nonzero) == 1
        distinguished = sp.eye(force.rows)[:, nonzero[0]]
        check(f"axis {axis}: full primary source has exact single-row coefficient two",
              force == 2*distinguished)
        recovered = target["kernel"]*distinguished
        receiver = (0, (1 << 0) | (1 << axis) | (1 << RADIAL))
        expected = sp.zeros(recovered.rows, 1)
        expected[target["basis"].index(receiver)] = 1
        check(f"axis {axis}: induced auxiliary field has the explicit horizontal receiver",
              recovered == expected)
        check(f"axis {axis}: primary direction has mass {sign} and zero background cubic columns",
              target["mass"]*distinguished == sign*distinguished
              and all(h*distinguished == sp.zeros(h.rows, 1) for h in target["hessians"]))
        kappa = sp.symbols("kappa", real=True, nonzero=True)
        energy = -(force.T*(2*distinguished/(sign*kappa)))[0]/2
        check(f"axis {axis}: exact imaginary-slice reduced energy coefficient on both coupling branches",
              energy == -2/(sign*kappa))
        witnesses.append({"time_axis": 0, "derivative_axis": axis,
            "radial_axis": RADIAL, "free_field": [RADIAL, 0],
            "primary_receiver": list(receiver), "all_fields_have_common_phase": "i",
            "primary_source_coefficient": "2", "primary_mass_sign": sign,
            "primary_potential_column": f"{sign} times kappa times the unit column",
            "recovered_auxiliary_coefficient": str(-2/(sign*kappa)),
            "reduced_principal_energy_coefficient": str(energy)})

    return {"passed": len(passed), "checks": passed, "branch": branch,
            "primary_potential_blocks": records,
            "raw_coefficient_dimension": total_coefficients,
            "primary_kernel_dimension": total_kernel,
            "nondegenerate_time_form_dimension": total_coefficients-total_kernel,
            "dimension_ceiling": "coefficient and presymplectic ranks, not particle or physical state counts",
            "mirror_equation_parities": mirror_parities,
            "mirror_primary_potential": "W_minus=-P W_plus P, P the Clifford parity on the primary kernel",
            "energy_witnesses": witnesses,
            "scope": "finite inputs for the owner's exact compact-core constrained-energy and observation obstruction"}


if __name__ == "__main__":
    print(json.dumps(certify(progress=lambda message: print(message, file=sys.stderr, flush=True)), indent=2))
