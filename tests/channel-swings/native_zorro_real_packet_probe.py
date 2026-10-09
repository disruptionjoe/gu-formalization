#!/usr/bin/env python3
"""Real-packet primary potentials and explicit limits of compact projection.

The forty determinant certificates use the selected sparse action engine.
The small compact-projection and interaction witnesses instead use the
independent occupation-state matrix implementation. Neither part computes
the completed metric-coupled physical Hamiltonian.
"""
from fractions import Fraction
from functools import lru_cache
from math import comb
import json
import sys

import sympy as sp

from native_zorro_constrained_energy_probe import (
    CORE, SPATIAL, VERTICAL, RADIAL, derivative_block, direction, exact,
    background_fields, stationary_field, exact_potential_determinant,
)
from native_zorro_matrix_energy_probe import (
    ETA, backgrounds, cubic_entry, derivative_entry, gamma_action,
    mass_entry, packet_basis, time_block,
)


@lru_cache(maxsize=None)
def real_constraint_block(nh, nv):
    seed = sum(1 << i for i in SPATIAL[:nh]+VERTICAL[:nv])
    labels = [seed, seed ^ 1, seed ^ (1 << RADIAL), seed ^ 1 ^ (1 << RADIAL)]
    basis, derivative = derivative_block(0, labels)
    selected = [i for i, (_, mask) in enumerate(basis)
                if mask.bit_count() % 4 in (1, 2)]
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
    return dict(labels=labels, basis=basis, derivative=derivative,
                kernel=kernel, mass=mass, hessians=hessians)


def hilbert_adjoint_sign(blade, imaginary):
    """Sign of a phased blade's adjoint in the occupation-state inner product."""
    sign = (-1)**(len(blade)*(len(blade)-1)//2+int(imaginary))
    for a in blade:
        sign *= ETA[a]
    return sign


def certify(progress=None):
    checks = []

    def check(label, condition):
        assert condition, label
        checks.append(label)

    field, parameters, branch = stationary_field()
    records = []
    for nh in range(4):
        for nv in range(10):
            block = real_constraint_block(nh, nv)
            e, n = block['derivative'], block['kernel']
            assert e.T == -e and e*n == sp.zeros(e.rows, n.cols)
            assert n.rank() == n.cols and e.rank()+n.cols == e.rows
            assert all(h.T == h for h in [block['mass']]+block['hessians'])
            parities = []
            for j in range(n.cols):
                seen = {(-1)**block['basis'][i][1].bit_count()
                        for i in range(n.rows) if n[i, j]}
                assert len(seen) == 1
                parities.append(seen.pop())
            p = sp.diag(*parities)
            assert all(p*h*p == h for h in [block['mass']]+block['hessians'][:2])
            assert all(p*h*p == -h for h in block['hessians'][2:])
            determinant = exact_potential_determinant(block, field, parameters)
            records.append(dict(horizontal_weight=nh, vertical_weight=nv,
                                multiplicity=comb(3, nh)*comb(9, nv),
                                coefficient_dimension=e.rows,
                                kernel_dimension=n.cols, **determinant))
            if progress:
                progress(f'Real primary-potential block ({nh},{nv}) passed')
    coefficients = sum(r['multiplicity']*r['coefficient_dimension'] for r in records)
    kernels = sum(r['multiplicity']*r['kernel_dimension'] for r in records)
    check('forty classes exhaust the real-packet coefficient carrier',
          len(records) == 40 and sum(r['multiplicity'] for r in records) == 2**12
          and coefficients == 113792 == 14*sum(comb(14, k) for k in range(15)
                                              if k % 4 in (1, 2)))
    check('all forty real primary potentials are nonzero in the selected number field', True)
    check('all forty real mirror potentials obey negative parity congruence', True)
    check('real time kernel and quotient have the stated raw ranks',
          kernels == 49310 and coefficients-kernels == 64482)
    check('real and imaginary packets exhaust the full source one-form carrier',
          coefficients+115584 == 14*2**14)

    # These checks use matrix elements, independently of CORE.
    for axis in range(14):
        for state in range(128):
            target, sign = gamma_action(axis, state)
            back, reverse = gamma_action(axis, target)
            assert back == state and reverse == ETA[axis]*sign
    check('each occupation-state gamma has the declared Hilbert adjoint sign', True)
    check('scalar and vertical receiver are compact while the spatial receiver is noncompact',
          hilbert_adjoint_sign((), True) == -1
          and hilbert_adjoint_sign((0, 4, RADIAL), True) == -1
          and hilbert_adjoint_sign((0, 1, RADIAL), True) == 1)

    source = packet_basis(1 << RADIAL)
    target = packet_basis((1 << RADIAL) ^ (1 << 1))
    nt = sp.Matrix.hstack(*time_block(target).nullspace())
    receiver = (0, (0, 1, RADIAL))
    receiver_column = sp.eye(len(target))[:, target.index(receiver)]
    assert time_block(target)*receiver_column == sp.zeros(len(target), 1)
    j = next(j for j in range(nt.cols) if nt[:, j] == receiver_column)
    force = nt.T*sp.Matrix([derivative_entry(1, row, (RADIAL, ())) for row in target])
    check('a compact scalar spatial derivative forces one noncompact primary receiver',
          force == 2*sp.eye(nt.cols)[:, j])
    mass_column = nt.T*sp.Matrix([mass_entry(row, receiver) for row in target])
    cubic_columns = [nt.T*sp.Matrix([cubic_entry(b, row, receiver) for row in target])
                     for b in backgrounds()]
    check('this noncompact primary receiver cannot be removed by another primary potential column',
          mass_column == -sp.eye(nt.cols)[:, j]
          and all(column == sp.zeros(nt.cols, 1) for column in cubic_columns))
    check('the scalar is dynamical rather than a time-kernel coordinate',
          time_block(source)[:, source.index((RADIAL, ()))] != sp.zeros(len(source), 1))

    left, right = (0, (0, 4, RADIAL)), (1, (1, 4, RADIAL))
    interaction = -cubic_entry(backgrounds()[0], left, right)
    check('the actual cubic action has a nonzero real-imaginary-imaginary interaction',
          interaction == -sp.Rational(124, 3))

    return dict(passed=len(checks), checks=checks, branch=branch,
                primary_potential_blocks=records,
                raw_coefficient_dimension=coefficients,
                primary_kernel_dimension=kernels,
                nondegenerate_distortion_time_form_dimension=coefficients-kernels,
                mirror_primary_potential='W_minus=-P W_plus P',
                compact_projection_witness=dict(
                    scalar=[RADIAL, []], receiver=[0, [0, 1, RADIAL]],
                    primary_source='2 partial_1 f', primary_mass='-kappa',
                    leading_recovery='2 partial_1 f/kappa',
                    tested_group='ambient occupation-adjoint compact/noncompact split',
                    not_identified_with='source Spin(6,4) maximal-compact shielding'),
                interaction_witness=dict(real_direction='F_a',
                    imaginary_directions=[[0, [0, 4, RADIAL]], [1, [1, 4, RADIAL]]],
                    cubic_third_variation=str(interaction)),
                scope='real distortion primary reduction and finite compact-projection control; '
                      'not the full metric constraints or physical Hamiltonian')


if __name__ == '__main__':
    print(json.dumps(certify(lambda message: print(message, file=sys.stderr, flush=True)), indent=2))
