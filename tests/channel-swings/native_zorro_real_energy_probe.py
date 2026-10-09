#!/usr/bin/env python3
"""Exact real-packet energy witnesses and a metric-free reflection character.

Finite Clifford coefficients are rebuilt by the sparse and occupation-state
engines. The owner supplies the disjoint-support, symmetry, oscillatory-bound
and all-order formal boundary-compatibility arguments. No global Cauchy
solution or source-selected physical domain is certified here.
"""

from itertools import product
import json
import sys

import sympy as sp

from native_zorro_real_metric_probe import real_full_block
from native_zorro_constrained_energy_probe import (
    algebraic_branch,
    derivative_block,
    rational_interval,
)
from native_zorro_geometry_probe import SLOTS
from native_zorro_matrix_energy_probe import (
    ETA,
    backgrounds,
    cubic_entry,
    derivative_entry,
    mass_entry,
    packet_basis,
    time_block,
)

FULL = (1 << 14) - 1
SEED = (FULL ^ 1) & ~1025


def projected_potentials(basis, kernel):
    """Independent occupation-state coefficients; no sparse values passed in."""
    mass = sp.Matrix(
        len(basis), len(basis), lambda i, j: mass_entry(basis[i], basis[j])
    )
    potentials = [
        sp.Matrix(
            len(basis),
            len(basis),
            lambda i, j: cubic_entry(background, basis[i], basis[j]),
        )
        for background in backgrounds()
    ]
    return [kernel.T * h * kernel for h in [mass] + potentials]


def connected_component(matrices, start):
    found, previous = {start}, set()
    while found != previous:
        previous = set(found)
        found |= {
            i
            for i in range(matrices[0].rows)
            for j in previous
            if any(m[i, j] for m in matrices)
        }
    return sorted(found)


def certify(progress=None):
    checks = []

    def check(name, condition=True):
        assert condition, name
        checks.append(name)
        if progress:
            progress(name)

    source, e0, n0, _, _ = real_full_block(SEED)
    free = sp.eye(len(source))[:, source.index((0, FULL))]
    source_matrix = packet_basis(SEED, imaginary=False)
    e0_matrix = time_block(source_matrix)
    check(
        "the real grade-14 source has a nonzero time symplectic partner",
        len(source) == 18
        and (free.T * e0 * e0 * free)[0] == -13
        and n0.T * free == sp.zeros(n0.cols, 1),
    )
    check(
        "independent matrices reproduce the complete source time form", e0_matrix == e0
    )
    k, a, c, v, w = sp.symbols("kappa a c v w")
    tau = 116 * a + 4 * c - 3 * k
    denominator = 11 * k * tau + 2 * (v + 8 * w) ** 2
    records = []
    for axis in (4, 11):
        target_seed = SEED ^ (1 << axis)
        target, et, nt, mass, potentials = real_full_block(target_seed)
        labels = [
            s ^ toggle for s in (SEED, target_seed) for toggle in (0, 1, 1024, 1025)
        ]
        combined, derivative = derivative_block(axis, labels)
        cross = derivative.extract(
            [combined.index(x) for x in target], [combined.index(x) for x in source]
        )
        force = nt.T * cross * free
        positions = [i for i, value in enumerate(force) if value]
        assert len(positions) == 1
        j = positions[0]
        receiver = sp.eye(len(target))[:, target.index((0, FULL ^ (1 << axis)))]
        check(
            f"axis {axis}: exact complete primary source and kernel pairing",
            force == sp.eye(nt.cols)[:, j]
            and nt[:, j] == receiver
            and nt.T * cross * n0 == sp.zeros(nt.cols, n0.cols),
        )
        matrices = [nt.T * h * nt for h in [mass] + potentials]
        independent_basis = packet_basis(target_seed, imaginary=False)
        independent_time = time_block(independent_basis)
        independent_kernel = sp.Matrix.hstack(*independent_time.nullspace())
        independent_cross = sp.Matrix(
            len(independent_basis),
            len(source_matrix),
            lambda i, j: derivative_entry(axis, independent_basis[i], source_matrix[j]),
        )
        check(
            f"axis {axis}: independent matrix time form, kernel and derivative source agree",
            independent_time == et
            and independent_kernel == nt
            and independent_cross == cross,
        )
        independent = projected_potentials(independent_basis, independent_kernel)
        check(
            f"axis {axis}: all five complete primary potentials agree with independent matrices",
            independent == matrices,
        )
        component = connected_component(matrices, j)
        other = [i for i in component if i != j]
        assert len(component) == 11 and len(other) == 10 and nt.cols == 12
        g = matrices[0].extract(other, other)
        h = matrices[3].extract(other, [j])
        eta = ETA[axis]
        check(
            f"axis {axis}: exact eleven-dimensional Schur component identities",
            matrices[0][j, j] == -eta
            and matrices[0].extract(other, [j]) == sp.zeros(10, 1)
            and matrices[1].extract(other, other) == -sp.Rational(116, 3) * g
            and matrices[2].extract(other, other) == -sp.Rational(4, 3) * g
            and matrices[3].extract(other, other)
            == matrices[4].extract(other, other)
            == sp.zeros(10)
            and matrices[4].extract(other, [j]) == 8 * h
            and all(
                matrices[i].extract(component, [j]) == sp.zeros(11, 1) for i in (1, 2)
            ),
        )
        # h^T G^-1 h suffices; no symbolic inverse of a full potential is assumed.
        gh = g.inv() * h
        check(
            f"axis {axis}: the exact secondary Schur contraction is minus eta times 2/33",
            (h.T * gh)[0] == -eta * sp.Rational(2, 33),
        )
        lam = k - (116 * a + 4 * c) / 3
        z_j = -eta * 11 * tau / denominator
        z = sp.zeros(nt.cols, 1)
        z[j] = z_j
        for index, coefficient in zip(other, gh):
            z[index] = -(v + 8 * w) * coefficient * z_j / lam
        total = sum(
            (p * m for p, m in zip((k, a, c, v, w), matrices)), sp.zeros(nt.cols)
        )
        check(
            f"axis {axis}: symbolic recovery solves every primary row",
            all(sp.cancel(value) == 0 for value in total * z - force),
        )
        energy = -eta * 11 * tau / (2 * denominator)
        check(
            f"axis {axis}: the real Hamiltonian coefficient and mirror sign are exact",
            sp.cancel((force.T * z)[0] / 2 - energy) == 0
            and sp.cancel(
                energy.subs({k: -k, a: -a, c: -c}, simultaneous=True) + energy
            )
            == 0,
        )
        records.append(
            dict(
                axis=axis,
                axis_square=eta,
                receiver=[0, FULL ^ (1 << axis)],
                source_coefficient=1,
                time_kernel_dimension=nt.cols,
                schur_component_dimension=len(component),
                schur_contraction=str(-eta * sp.Rational(2, 33)),
                real_energy_coefficient=str(energy),
            )
        )

    root, _, vroot, alpha, beta, k2, *_ = algebraic_branch()
    normalized_tau = 116 * alpha + 4 * beta - 3
    coefficient = sp.cancel(
        11
        * k2
        * normalized_tau
        / (2 * (11 * k2 * normalized_tau + 2 * (vroot + 8 * root) ** 2))
    )
    interval = (sp.Rational(227427945967, 10**12), sp.Rational(227427945969, 10**12))
    tau_bounds = rational_interval(normalized_tau, root, interval)
    coefficient_bounds = rational_interval(coefficient, root, interval)
    check(
        "rational stationary-branch bounds certify the nonzero Schur numerator",
        6 < tau_bounds[0] < tau_bounds[1] < 8,
    )
    check(
        "both real energy signs have normalized magnitude strictly between 0.388 and 0.389",
        sp.Rational(388, 1000)
        < coefficient_bounds[0]
        < coefficient_bounds[1]
        < sp.Rational(389, 1000),
    )

    # Actual geometric action of base sign reflections on TX plus Sym^2(T*X).
    projector = sp.zeros(10)
    control = sp.zeros(10)
    character_rows = []
    orbit = set()
    h0 = sp.diag(4, -1, -1, -1)
    fixture = h0.copy()
    for i in range(1, 4):
        fixture[0, i] = fixture[i, 0] = sp.Rational(i, 1000)
    for signs in product((-1, 1), repeat=3):
        base = [1] + list(signs)
        vertical = [base[i] * base[j] for i, j in SLOTS]
        action = sp.diag(*vertical)
        character = sp.prod(signs)
        assert sp.prod(base + vertical) == 1
        projector += character * action / 8
        control += signs[0] * signs[1] * action / 8
        reflected = sp.diag(*base) * fixture * sp.diag(*base)
        orbit.add(tuple(reflected))
        character_rows.append(
            dict(
                signs=list(signs),
                character=int(character),
                ambient_orientation=int(sp.prod(base + vertical)),
            )
        )
    check(
        "all eight base reflections preserve the induced ambient orientation",
        len(character_rows) == 8
        and all(row["ambient_orientation"] == 1 for row in character_rows),
    )
    check(
        "the triple-sign character is absent from all ten homogeneous metric components",
        projector == sp.zeros(10),
    )
    check(
        "a two-sign control retains a metric component",
        control.rank() == 1 and control[SLOTS.index((1, 2)), SLOTS.index((1, 2))] == 1,
    )
    check(
        "a Lorentzian nearby fibre fixture has eight distinct orbit points",
        len(orbit) == 8 and fixture.det() < 0 and fixture.inv()[0, 0] > 0,
    )
    return dict(
        passed=len(checks),
        checks=checks,
        source=[0, FULL],
        source_symplectic_contraction=-13,
        witnesses=records,
        normalized_magnitude="11*kappa^2*(116*alpha+4*beta-3)/(2*(11*kappa^2*(116*alpha+4*beta-3)+2*(v+8*w)^2))",
        normalized_magnitude_interval=list(map(str, coefficient_bounds)),
        reflection_characters=character_rows,
        homogeneous_metric_character_rank=0,
        matrix_implementation="128 occupation-state Clifford engine; complete primary matrices rebuilt independently of sparse entries",
        scope="real compact-core two-sided energy with metric-decoupling character and all-order formal boundary compatibility proved in owner; no global evolution or physical-domain selection theorem",
    )


if __name__ == "__main__":
    print(
        json.dumps(
            certify(lambda message: print(message, file=sys.stderr, flush=True)),
            indent=2,
        )
    )
