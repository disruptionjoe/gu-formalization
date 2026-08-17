#!/usr/bin/env python3
"""K151 exact distortion-pairing and weighted-adjoint adapter.

K150 returns the selected Shiab coefficient in density-dual coordinates.  A
field-like distortion operator is obtained only after applying the inverse of
the indefinite ``Cl(7,7)`` Hodge/scalar-Clifford lowerer.  This module keeps
those objects distinct and delegates formal integration by parts to K149's
complete sparse differential-operator algebra.

The selected coordinate motion is an inner Spin motion.  Its moving basis has
a constant pairing and unit density by exact naturality, while the Shiab
coefficient itself has a live coordinate jet.  Consequently the first curved
formal-Euler correction already contains the derivative of that coefficient;
it is not the frozen shortcut ``(C-C.T)/2``.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import sympy as sp

import k150_moving_selected_shiab_coordinate_adapter as K150
from k149_sparse_differential_jet_api import (
    SparseDifferentialOperator,
    zero_index,
)


BasisEntry = tuple[int, int, int]


def _complex(value: K150.Scalar) -> sp.Expr:
    return sp.expand(value[0] + sp.I * value[1])


def _moving_direction(
    mu: int,
    mask: int,
    generator: K150.Element,
    coordinate: sp.Symbol,
    order: int,
) -> K150.Form:
    coefficient = K150.conjugation_series_element(
        K150.blade(K150.indices(mask)), generator, coordinate, order
    )
    return {1 << mu: coefficient}


def distortion_lowerer(basis: Iterable[BasisEntry]) -> sp.ImmutableMatrix:
    """Return the flat density-dual lowerer on an explicit Omega1 packet."""
    entries = tuple(basis)
    matrix = sp.zeros(len(entries))
    for row, (_, mu, mask) in enumerate(entries):
        primal = K150.direction(mu, mask)
        for column, (_, nu, other_mask) in enumerate(entries):
            dual = K150.hodge(K150.direction(nu, other_mask))
            matrix[row, column] = _complex(K150.pairing(primal, dual))
    return sp.ImmutableMatrix(matrix)


def moving_distortion_lowerer(
    basis: Iterable[BasisEntry],
    generator: K150.Element,
    coordinate: sp.Symbol,
    order: int,
) -> sp.ImmutableMatrix:
    """Pair a moving Spin basis with its moving Hodge-dual basis.

    The returned polynomial is a finite jet representative.  Naturality is
    tested coefficientwise at the jet origin; no truncated exponential is
    promoted to a global finite transformation.
    """
    entries = tuple(basis)
    moving = tuple(
        _moving_direction(mu, mask, generator, coordinate, order)
        for _, mu, mask in entries
    )
    matrix = sp.zeros(len(entries))
    for row, primal in enumerate(moving):
        for column, other in enumerate(moving):
            matrix[row, column] = _complex(K150.pairing(primal, K150.hodge(other)))
    return sp.ImmutableMatrix(matrix.applyfunc(sp.expand))


def add_operators(
    left: SparseDifferentialOperator,
    right: SparseDifferentialOperator,
    left_scale: sp.Expr = sp.Integer(1),
    right_scale: sp.Expr = sp.Integer(1),
) -> SparseDifferentialOperator:
    if (
        left.coordinates != right.coordinates
        or left.input_dimension != right.input_dimension
        or left.output_dimension != right.output_dimension
    ):
        raise ValueError("operators do not share one typed carrier")
    keys = set(left.coefficients) | set(right.coefficients)
    coefficients = {
        alpha: sp.ImmutableMatrix(
            (
                left_scale * sp.Matrix(left.coefficient(alpha))
                + right_scale * sp.Matrix(right.coefficient(alpha))
            ).applyfunc(sp.simplify)
        )
        for alpha in keys
    }
    return SparseDifferentialOperator(
        left.coordinates,
        left.input_dimension,
        left.output_dimension,
        coefficients,
    )


@dataclass(frozen=True)
class MovingDistortionPairing:
    coordinates: tuple[sp.Symbol, ...]
    lowerer: sp.ImmutableMatrix
    density: sp.Expr

    def __post_init__(self) -> None:
        lowerer = sp.ImmutableMatrix(self.lowerer)
        if lowerer.rows != lowerer.cols:
            raise ValueError("the distortion lowerer must be square")
        if lowerer.det() == 0:
            raise ValueError("the distortion lowerer must be nondegenerate")
        if sp.simplify(self.density) == 0:
            raise ValueError("the density must be nonzero")
        object.__setattr__(self, "lowerer", lowerer)
        object.__setattr__(self, "density", sp.simplify(self.density))

    @property
    def dimension(self) -> int:
        return self.lowerer.rows

    @property
    def primalizer(self) -> sp.ImmutableMatrix:
        return sp.ImmutableMatrix(sp.Matrix(self.lowerer).inv())

    def primalize_density_coefficient(
        self, coefficient: sp.MatrixBase
    ) -> sp.ImmutableMatrix:
        coefficient = sp.ImmutableMatrix(coefficient)
        if coefficient.rows != self.dimension:
            raise ValueError("density-dual coefficient has the wrong output carrier")
        return sp.ImmutableMatrix(
            (sp.Matrix(self.primalizer) * sp.Matrix(coefficient)).applyfunc(sp.simplify)
        )

    def first_order_raw_operator(
        self,
        density_dual_coefficient: sp.MatrixBase,
        axis: int,
    ) -> SparseDifferentialOperator:
        field_coefficient = self.primalize_density_coefficient(density_dual_coefficient)
        multiplication = SparseDifferentialOperator.multiplication(
            self.coordinates, field_coefficient
        )
        derivative = SparseDifferentialOperator.partial(
            self.coordinates, field_coefficient.cols, axis
        )
        return multiplication.compose(derivative)

    def formal_adjoint(
        self, operator: SparseDifferentialOperator
    ) -> SparseDifferentialOperator:
        return operator.weighted_formal_adjoint(
            self.lowerer, self.lowerer, self.density
        )

    def formal_euler(
        self, raw_operator: SparseDifferentialOperator
    ) -> SparseDifferentialOperator:
        return add_operators(
            raw_operator, self.formal_adjoint(raw_operator),
            sp.Rational(1, 2), sp.Rational(1, 2),
        )

    def lower_field_operator(
        self, operator: SparseDifferentialOperator
    ) -> SparseDifferentialOperator:
        lower = SparseDifferentialOperator.multiplication(
            self.coordinates, self.lowerer
        )
        return lower.compose(operator)


def coefficient_at(
    operator: SparseDifferentialOperator,
    order: int,
    coordinate_count: int = 1,
) -> sp.ImmutableMatrix:
    if coordinate_count != 1:
        raise ValueError("the convenience accessor is one-coordinate only")
    return operator.coefficient((order,)) if order else operator.coefficient(zero_index(1))
