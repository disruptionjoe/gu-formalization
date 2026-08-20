#!/usr/bin/env python3
"""Exact K152 normal-coordinate curved metric-bridge adapter.

The bridge differentiates the Riemann tensor of a metric germ at a normal-
coordinate point, including both the second-order metric-variation term and
the zero-order term forced by the background Ricci-flat Weyl tensor.  It then
applies the selected conditional ``comm/symi/symi`` Shiab and records the
result as a K149 sparse differential operator.

The returned bridge is density-dual on the distortion output.  K151's
indefinite Hodge/scalar-Clifford lowerer is therefore inverted before the
field-like operator is formed.  The native DeWitt and distortion pairings are
then passed to K149 for the complete formal adjoint.  No fivefold composition,
preferred historical Shiab, inverse, domain, or physical quotient is selected
here.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product
from typing import Mapping

import sympy as sp

import k150_moving_selected_shiab_coordinate_adapter as K150
import k151_moving_distortion_pairing_adapter as K151
from k149_sparse_differential_jet_api import SparseDifferentialOperator, zero_index


ETA4 = sp.diag(1, -1, -1, -1)
METRIC_SLOTS = tuple((i, j) for i in range(4) for j in range(i, 4))
DERIVATIVE_PAIRS = tuple((i, j) for i in range(4) for j in range(i, 4))
FORM_PAIRS = tuple(combinations(range(K150.N), 2))

Curvature = Mapping[tuple[int, int, int, int], sp.Expr]
BasisEntry = tuple[int, int, int]


def metric_basis(slot: tuple[int, int]) -> sp.ImmutableMatrix:
    matrix = sp.zeros(4)
    i, j = slot
    matrix[i, j] = 1
    matrix[j, i] = 1
    return sp.ImmutableMatrix(matrix)


def metric_vector(matrix: sp.MatrixBase) -> sp.ImmutableMatrix:
    matrix = sp.Matrix(matrix)
    return sp.ImmutableMatrix([matrix[i, j] for i, j in METRIC_SLOTS])


def dewitt_pairing() -> sp.ImmutableMatrix:
    basis = tuple(metric_basis(slot) for slot in METRIC_SLOTS)

    def pair(left: sp.MatrixBase, right: sp.MatrixBase) -> sp.Expr:
        left = sp.Matrix(left)
        right = sp.Matrix(right)
        right_up = ETA4 * right * ETA4
        contraction = sum(
            left[i, j] * right_up[i, j] for i, j in product(range(4), repeat=2)
        )
        return sp.simplify(
            contraction
            - sp.Rational(1, 2)
            * sp.trace(ETA4 * left)
            * sp.trace(ETA4 * right)
        )

    return sp.ImmutableMatrix([[pair(left, right) for right in basis] for left in basis])


def weyl_from_electric(electric: sp.MatrixBase) -> dict[tuple[int, int, int, int], sp.Expr]:
    """Pure-electric Ricci-flat Weyl tensor in the K127 convention."""
    electric = sp.Matrix(electric)
    output: dict[tuple[int, int, int, int], sp.Expr] = {}

    def put(a: int, b: int, c: int, d: int, value: sp.Expr) -> None:
        for indices, sign in (
            ((a, b, c, d), 1),
            ((b, a, c, d), -1),
            ((a, b, d, c), -1),
            ((b, a, d, c), 1),
            ((c, d, a, b), 1),
            ((d, c, a, b), -1),
            ((c, d, b, a), -1),
            ((d, c, b, a), 1),
        ):
            output[indices] = sp.simplify(sign * value)

    for i in range(1, 4):
        for j in range(1, 4):
            put(0, i, 0, j, electric[i - 1, j - 1])
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                for ell in range(1, 4):
                    value = -sum(
                        sp.LeviCivita(i - 1, j - 1, m - 1)
                        * sp.LeviCivita(k - 1, ell - 1, n - 1)
                        * electric[m - 1, n - 1]
                        for m in range(1, 4)
                        for n in range(1, 4)
                    )
                    put(i, j, k, ell, value)
    return output


def normal_metric_twojet(
    curvature: Curvature, mu: int, nu: int, alpha: int, beta: int
) -> sp.Expr:
    return sp.simplify(
        -sp.Rational(1, 3)
        * (
            curvature.get((mu, alpha, nu, beta), 0)
            + curvature.get((mu, beta, nu, alpha), 0)
        )
    )


def reconstructed_curvature(
    curvature: Curvature, rho: int, sigma: int, mu: int, nu: int
) -> sp.Expr:
    g2 = normal_metric_twojet
    return sp.simplify(
        sp.Rational(1, 2)
        * (
            g2(curvature, rho, nu, sigma, mu)
            + g2(curvature, sigma, mu, rho, nu)
            - g2(curvature, rho, mu, sigma, nu)
            - g2(curvature, sigma, nu, rho, mu)
        )
    )


def _metric_twojet(curvature: Curvature) -> list[list[list[list[sp.Expr]]]]:
    return [
        [
            [
                [normal_metric_twojet(curvature, a, b, c, d) for d in range(4)]
                for c in range(4)
            ]
            for b in range(4)
        ]
        for a in range(4)
    ]


def _variation_twojet(
    slot: tuple[int, int], derivative_pair: tuple[int, int] | None
) -> list[list[list[list[sp.Expr]]]]:
    output = [[[[sp.Integer(0) for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(4)]
    if derivative_pair is None:
        return output
    i, j = derivative_pair
    variation = metric_basis(slot)
    for a in range(4):
        for b in range(4):
            output[a][b][i][j] = variation[a, b]
            output[a][b][j][i] = variation[a, b]
    return output


def _d_gamma(
    inverse: sp.MatrixBase,
    twojet: list[list[list[list[sp.Expr]]]],
    rho: int,
    mu: int,
    nu: int,
    derivative: int,
) -> sp.Expr:
    return sp.simplify(
        sp.Rational(1, 2)
        * sum(
            inverse[rho, sigma]
            * (
                twojet[sigma][nu][mu][derivative]
                + twojet[sigma][mu][nu][derivative]
                - twojet[mu][nu][sigma][derivative]
            )
            for sigma in range(4)
        )
    )


def linearized_riemann_normal(
    background: Curvature,
    slot: tuple[int, int],
    derivative_pair: tuple[int, int] | None,
) -> dict[tuple[int, int, int, int], sp.Expr]:
    """Linearized all-lowered Riemann tensor at a normal-coordinate point.

    ``derivative_pair=None`` returns the coefficient of the undifferentiated
    metric variation.  A pair ``(i,j)`` returns the coefficient of
    ``D_i D_j h`` in K149's commuting multiindex convention.
    """
    h0 = sp.Matrix(metric_basis(slot)) if derivative_pair is None else sp.zeros(4)
    background_twojet = _metric_twojet(background)
    variation_twojet = _variation_twojet(slot, derivative_pair)
    inverse_variation = -ETA4 * h0 * ETA4
    output: dict[tuple[int, int, int, int], sp.Expr] = {}

    def riemann_up(
        inverse: sp.MatrixBase,
        twojet: list[list[list[list[sp.Expr]]]],
        rho: int,
        sigma: int,
        mu: int,
        nu: int,
    ) -> sp.Expr:
        return sp.simplify(
            _d_gamma(inverse, twojet, rho, nu, sigma, mu)
            - _d_gamma(inverse, twojet, rho, mu, sigma, nu)
        )

    for alpha in range(4):
        for sigma in range(4):
            for mu in range(4):
                for nu in range(4):
                    value = sum(
                        h0[alpha, rho]
                        * riemann_up(ETA4, background_twojet, rho, sigma, mu, nu)
                        + ETA4[alpha, rho]
                        * (
                            riemann_up(
                                inverse_variation,
                                background_twojet,
                                rho,
                                sigma,
                                mu,
                                nu,
                            )
                            + riemann_up(
                                ETA4,
                                variation_twojet,
                                rho,
                                sigma,
                                mu,
                                nu,
                            )
                        )
                        for rho in range(4)
                    )
                    value = sp.simplify(value)
                    if value:
                        output[(alpha, sigma, mu, nu)] = value
    return output


def linearized_einstein_normal(
    background: Curvature,
    slot: tuple[int, int],
    derivative_pair: tuple[int, int] | None,
) -> sp.ImmutableMatrix:
    """Linearized covariant Einstein tensor at a Ricci-flat normal point."""
    variation = linearized_riemann_normal(background, slot, derivative_pair)
    h0 = sp.Matrix(metric_basis(slot)) if derivative_pair is None else sp.zeros(4)
    inverse_variation = -ETA4 * h0 * ETA4
    ricci = sp.zeros(4)
    for sigma in range(4):
        for nu in range(4):
            ricci[sigma, nu] = sp.simplify(
                sum(
                    ETA4[alpha, rho]
                    * variation.get((alpha, sigma, rho, nu), 0)
                    + inverse_variation[alpha, rho]
                    * background.get((alpha, sigma, rho, nu), 0)
                    for alpha in range(4)
                    for rho in range(4)
                )
            )
    scalar = sp.simplify(sum(ETA4[sigma, nu] * ricci[sigma, nu] for sigma in range(4) for nu in range(4)))
    return sp.ImmutableMatrix(
        sp.Matrix(4, 4, lambda sigma, nu: sp.simplify(
            ricci[sigma, nu] - sp.Rational(1, 2) * ETA4[sigma, nu] * scalar
        ))
    )


def conformally_flat_curvature_from_einstein(
    einstein: sp.MatrixBase,
) -> dict[tuple[int, int, int, int], sp.Expr]:
    """One algebraic curvature representative with the supplied Einstein row.

    The selected Shiab factors through the Einstein contraction on the
    horizontal curvature packet.  Choosing the zero-Weyl representative
    therefore serializes the response without inventing a new background.
    """
    einstein = sp.Matrix(einstein)
    trace_einstein = sp.simplify(
        sum(ETA4[a, b] * einstein[a, b] for a in range(4) for b in range(4))
    )
    scalar = -trace_einstein
    ricci = sp.Matrix(4, 4, lambda a, b: sp.simplify(
        einstein[a, b] - sp.Rational(1, 2) * ETA4[a, b] * trace_einstein
    ))
    output: dict[tuple[int, int, int, int], sp.Expr] = {}
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    value = sp.simplify(
                        sp.Rational(1, 2)
                        * (
                            ETA4[a, c] * ricci[b, d]
                            - ETA4[a, d] * ricci[b, c]
                            - ETA4[b, c] * ricci[a, d]
                            + ETA4[b, d] * ricci[a, c]
                        )
                        - sp.Rational(1, 6)
                        * scalar
                        * (
                            ETA4[a, c] * ETA4[b, d]
                            - ETA4[a, d] * ETA4[b, c]
                        )
                    )
                    if value:
                        output[(a, b, c, d)] = value
    return output


def selected_einstein_coefficient(
    background: Curvature,
    derivative_pair: tuple[int, int] | None,
) -> sp.ImmutableMatrix:
    """The K129 ``-2 delta G`` coefficient on the metric carrier."""
    columns = []
    for slot in METRIC_SLOTS:
        value = -2 * sp.Matrix(
            linearized_einstein_normal(background, slot, derivative_pair)
        )
        columns.append(metric_vector(value))
    return sp.ImmutableMatrix.hstack(*columns)


def spin_curvature_injection(curvature: Curvature) -> K150.Form:
    output: K150.Form = {}
    for i, j in FORM_PAIRS:
        coefficient: K150.Element = {}
        for a, b in FORM_PAIRS:
            value = sp.simplify(K150.ETA[a] * K150.ETA[b] * curvature.get((i, j, a, b), 0))
            if value:
                coefficient = K150.eadd(
                    coefficient,
                    K150.escale(value, K150.emul(K150.blade(a), K150.blade(b))),
                )
        if coefficient:
            output[(1 << i) | (1 << j)] = coefficient
    return K150.fclean(output)


def _density_rows(image: K150.Form) -> dict[tuple[int, int], sp.Expr]:
    output: dict[tuple[int, int], sp.Expr] = {}
    for nu, clifford_mask, value in K150.rows_for_image(image):
        label = clifford_mask ^ (1 << nu)
        expression = sp.expand(value[0] + sp.I * value[1])
        output[(label, nu)] = sp.expand(output.get((label, nu), 0) + expression)
    return {key: value for key, value in output.items() if sp.simplify(value) != 0}


def _multiindex(pair: tuple[int, int], dimension: int = 4) -> tuple[int, ...]:
    output = [0] * dimension
    output[pair[0]] += 1
    output[pair[1]] += 1
    return tuple(output)


@dataclass(frozen=True)
class CurvedMetricBridge:
    coordinates: tuple[sp.Symbol, ...]
    basis: tuple[BasisEntry, ...]
    density_dual: SparseDifferentialOperator
    metric_pairing: sp.ImmutableMatrix
    distortion_pairing: sp.ImmutableMatrix
    density: sp.Expr = sp.Integer(1)

    @property
    def field_operator(self) -> SparseDifferentialOperator:
        primalize = SparseDifferentialOperator.multiplication(
            self.coordinates, sp.Matrix(self.distortion_pairing).inv()
        )
        return primalize.compose(self.density_dual)

    @property
    def formal_adjoint(self) -> SparseDifferentialOperator:
        return self.field_operator.weighted_formal_adjoint(
            self.metric_pairing, self.distortion_pairing, self.density
        )

    @property
    def lowered_formal_adjoint(self) -> SparseDifferentialOperator:
        lower = SparseDifferentialOperator.multiplication(
            self.coordinates, self.metric_pairing
        )
        return lower.compose(self.formal_adjoint)

    def symbol(
        self,
        covector: tuple[sp.Expr, ...],
        substitutions: Mapping[sp.Symbol, sp.Expr] | None = None,
    ) -> sp.ImmutableMatrix:
        substitutions = substitutions or dict.fromkeys(self.coordinates, 0)
        matrix = sp.zeros(self.density_dual.output_dimension, self.density_dual.input_dimension)
        for alpha, coefficient in self.density_dual.coefficients.items():
            if sum(alpha) != 2:
                continue
            monomial = sp.prod(value**power for value, power in zip(covector, alpha))
            matrix += monomial * sp.Matrix(coefficient)
        return sp.ImmutableMatrix(matrix.subs(substitutions).applyfunc(sp.simplify))

    def zero_order(
        self, substitutions: Mapping[sp.Symbol, sp.Expr] | None = None
    ) -> sp.ImmutableMatrix:
        substitutions = substitutions or dict.fromkeys(self.coordinates, 0)
        return sp.ImmutableMatrix(
            sp.Matrix(self.density_dual.coefficient(zero_index(4)))
            .subs(substitutions)
            .applyfunc(sp.simplify)
        )


def build_curved_metric_bridge(
    background: Curvature,
    coordinates: tuple[sp.Symbol, ...],
    generators: tuple[K150.Element, ...],
    jet_order: int = 1,
) -> CurvedMetricBridge:
    if len(coordinates) != 4 or len(generators) != 4:
        raise ValueError("the horizontal metric bridge requires four coordinates and generators")
    phi_one, phi_two = K150.moving_phi(coordinates, generators, jet_order)
    row_columns: dict[tuple[int, ...], list[dict[tuple[int, int], sp.Expr]]] = {}

    for pair in DERIVATIVE_PAIRS:
        alpha = _multiindex(pair)
        row_columns[alpha] = []
        for slot in METRIC_SLOTS:
            # The selected horizontal Shiab is exactly minus twice the
            # Einstein contraction in the K127/K129 convention.
            einstein = -2 * sp.Matrix(linearized_einstein_normal({}, slot, pair))
            curvature = conformally_flat_curvature_from_einstein(einstein)
            image = K150.selected_shiab(
                spin_curvature_injection(curvature), phi_one, phi_two
            )
            row_columns[alpha].append(_density_rows(image))

    zero = zero_index(4)
    row_columns[zero] = []
    for slot in METRIC_SLOTS:
        einstein = -2 * sp.Matrix(
            linearized_einstein_normal(background, slot, None)
        )
        curvature = conformally_flat_curvature_from_einstein(einstein)
        image = K150.selected_shiab(
            spin_curvature_injection(curvature), phi_one, phi_two
        )
        row_columns[zero].append(_density_rows(image))

    labels = tuple(
        sorted(
            {
                label
                for columns in row_columns.values()
                for column in columns
                for label, _ in column
            }
        )
    )
    basis = tuple((label, mu, label ^ (1 << mu)) for label in labels for mu in range(K150.N))
    index = {(label, mu): position for position, (label, mu, _) in enumerate(basis)}
    coefficients: dict[tuple[int, ...], sp.ImmutableMatrix] = {}
    for alpha, columns in row_columns.items():
        matrix = sp.zeros(len(basis), len(METRIC_SLOTS))
        for column_index, column in enumerate(columns):
            for key, value in column.items():
                matrix[index[key], column_index] = value
        if matrix != sp.zeros(*matrix.shape):
            coefficients[alpha] = sp.ImmutableMatrix(matrix.applyfunc(sp.expand))

    density_dual = SparseDifferentialOperator(
        coordinates,
        len(METRIC_SLOTS),
        len(basis),
        coefficients,
    )
    return CurvedMetricBridge(
        coordinates=coordinates,
        basis=basis,
        density_dual=density_dual,
        metric_pairing=dewitt_pairing(),
        distortion_pairing=K151.distortion_lowerer(basis),
    )
