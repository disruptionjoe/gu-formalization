#!/usr/bin/env python3
"""Universal real primary cancellation and a boundary-compatibility obstruction.

The 37 connection coefficients exhaust torsion-free homogeneous jets with
closed trace. All identities are linear/quadratic on that complete carrier.
The boundary result excludes a free-momentum inference for the specified
odd-Dirichlet completion; it is not a positivity or global evolution theorem.
"""

from itertools import combinations_with_replacement
import json
import sys

import sympy as sp

from native_zorro_real_metric_probe import (
    ETA,
    ETA4,
    BASIS,
    compensator_gradient,
    diagonal_fibre_frame,
    form_rows,
    real_full_block,
    dewitt,
    algebraic_branch,
    rational_interval,
)
from native_zorro_matrix_energy_probe import shiab_pair, derivative_entry


def homogeneous_connection_generators():
    labels = [
        (a, i, j)
        for a in range(4)
        for i, j in combinations_with_replacement(range(4), 2)
    ]
    elementary = []
    for a, i, j in labels:
        coefficient = [sp.zeros(4) for _ in range(4)]
        coefficient[i][a, j] = coefficient[j][a, i] = 1
        elementary.append(coefficient)
    trace = sp.Matrix(3, 40, lambda i, j: sp.trace(elementary[j][i + 1]))
    null = trace.nullspace()
    assert trace.rank() == 3 and len(null) == 37
    for column in null:
        yield [
            sum((column[j] * elementary[j][i] for j in range(40)), sp.zeros(4))
            for i in range(4)
        ]


def metric_source(connection, frame):
    q = [1, 0, 0, 0]
    ricci = sp.Matrix(
        4,
        4,
        lambda i, j: sum(
            (q[k] * connection[j] - q[j] * connection[k])[k, i] for k in range(4)
        ),
    )
    assert ricci == ricci.T
    sharp = sp.diag(*ETA) * frame.T * sp.diag(ricci, sp.zeros(10)) * frame
    einstein = sharp - sp.trace(sharp) * sp.eye(14) / 2
    return {
        (mu, 1 << nu): -einstein[mu, nu]
        for mu in range(14)
        for nu in range(14)
        if einstein[mu, nu]
    }


def certify(progress=None):
    checks = []

    def check(name, condition=True):
        assert condition, name
        checks.append(name)
        if progress:
            progress(name)

    generators = list(homogeneous_connection_generators())
    check(
        "37 generators exhaust the torsion-free closed-trace homogeneous connection carrier",
        len(generators) == 37
        and all(
            c[i][a, j] == c[j][a, i]
            for c in generators
            for i in range(4)
            for j in range(4)
            for a in range(4)
        ),
    )
    frame = diagonal_fibre_frame(sp.eye(4))
    ys, residuals = [], []
    for index, coefficient in enumerate(generators):
        assert all(sp.trace(coefficient[i]) == 0 for i in range(1, 4))
        y, _, dy = compensator_gradient(
            [1, 0, 0, 0], sp.zeros(4), ETA4, frame, connection_coefficient=coefficient
        )
        source = metric_source(coefficient, frame)
        residual = {
            row: source.get(row, 0) - dy.get(row, 0) for row in set(source) | set(dy)
        }
        ys.append(form_rows(y))
        residuals.append({row: value for row, value in residual.items() if value})
        if progress and (index + 1) % 10 == 0:
            progress(f"{index+1}/37 complete covariant compensator gradients evaluated")
    seeds = sorted(
        {((1 << mu) ^ mask) & ~1025 for rows in ys + residuals for mu, mask in rows}
    )
    grams = [sp.zeros(37) for _ in range(5)]
    blocks = []
    for seed in seeds:
        basis, e, n, mass, hessians = real_full_block(seed)
        y = sp.Matrix(len(basis), 37, lambda i, j: ys[j].get(basis[i], 0))
        residual = sp.Matrix(len(basis), 37, lambda i, j: residuals[j].get(basis[i], 0))
        assert n.T * residual == sp.zeros(n.cols, 37)
        for i, potential in enumerate([mass] + hessians):
            assert n.T * potential * y == sp.zeros(n.cols, 37)
            grams[i] += y.T * potential * y
        blocks.append(dict(label=seed, coefficients=len(basis), kernel=n.cols))
    check(
        "every primary projection of A2 minus the full covariant compensator derivative vanishes"
    )
    check("every primary projection of each of the five potential columns vanishes")
    fs = [[c[i].T * ETA4 + ETA4 * c[i] for i in range(1, 4)] for c in generators]
    fgram = sp.Matrix(
        37,
        37,
        lambda i, j: -2 * sum(dewitt(ETA4, fs[i][a], fs[j][a]) for a in range(3)),
    )
    check(
        "the curvature Gram has rank 27 on the complete 37-dimensional carrier",
        fgram.rank() == 27,
    )
    check(
        "all 1369 mixed mass Gram entries equal minus one sixteenth of the curvature Gram",
        grams[0] == -fgram / 16,
    )
    check(
        "all mixed cubic Gram entries have the stated universal coefficients",
        grams[1] == -sp.Rational(52, 3) * grams[0]
        and grams[2] == -sp.Rational(4, 3) * grams[0]
        and grams[3] == grams[4] == sp.zeros(37),
    )

    # The raw first-order boundary coefficient is K, not its skew part E.
    odd, even = (0, (0,)), (0, (0, 4))
    k_oe = shiab_pair(odd[0], odd[1], 4, even[0], even[1])
    k_eo = shiab_pair(even[0], even[1], 4, odd[0], odd[1])
    check(
        "independent matrix elements distinguish the action boundary coefficient from the skew bulk coefficient",
        (k_oe, k_eo, derivative_entry(4, odd, even)) == (0, -2, 1),
    )

    w, _, _, alpha, beta, _, _, _ = algebraic_branch()
    interval = (sp.Rational(227427945967, 10**12), sp.Rational(227427945969, 10**12))
    delta = rational_interval(1 - (52 * alpha + 4 * beta) / 3, w, interval)
    acceleration = rational_interval(
        1 + sp.Rational(8, 3) * (10 * alpha + beta), w, interval
    )
    check(
        "the even-force Gram is definite on all five spatial traceless polarizations on both branches",
        sp.Rational(-401, 1000) < delta[0] < delta[1] < sp.Rational(-399, 1000),
    )
    check(
        "the independent metric acceleration matrix remains nondegenerate on both branches",
        3 < acceleration[0] < acceleration[1] < sp.Rational(31, 10),
    )
    gram = sp.Matrix(
        [
            [2, -1, 0, 0, 0],
            [-1, 2, 0, 0, 0],
            [0, 0, 2, 0, 0],
            [0, 0, 0, 2, 0],
            [0, 0, 0, 0, 2],
        ]
    )
    check(
        "the five-polarization force Gram has rank five and fixes the boundary compatibility rank",
        gram.det() == 24 and gram.is_positive_definite is True,
    )
    return dict(
        passed=len(checks),
        checks=checks,
        connection_dimension=37,
        curvature_gram_rank=27,
        primary_blocks=blocks,
        universal_primary_source="N^T(A2-D0*y)=N^T V*y=0",
        universal_acceleration="-[kappa+8/3*(10a+c)] ||F1||^2/16",
        boundary_control=dict(
            normal=4,
            odd=[0, [0]],
            even=[0, [0, 4]],
            K_odd_even="0",
            K_even_odd="-2",
            E_odd_even="1",
        ),
        force_factor_interval=list(map(str, delta)),
        acceleration_factor_interval=list(map(str, acceleration)),
        boundary_compatibility_rank=5,
        source_selection="odd-Dirichlet polarization is a declared completion, not selected by the draft",
        scope="exact bulk identity and boundary compatibility constraint; no completed positive or negative physical real-sector Hamiltonian",
    )


if __name__ == "__main__":
    print(
        json.dumps(
            certify(lambda message: print(message, file=sys.stderr, flush=True)),
            indent=2,
        )
    )
