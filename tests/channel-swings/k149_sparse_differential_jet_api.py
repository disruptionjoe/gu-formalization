#!/usr/bin/env python3
"""Small exact differential-operator algebra for K149 curved-jet gates.

This module is intentionally carrier-agnostic.  Coefficients are SymPy
matrices and derivatives are ordinary coordinate derivatives; covariant
connections, moving pairings, and densities are represented by explicit
zero-order multiplication operators.  Nothing here selects an I1B action
coefficient or a preferred Shiab.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
import math
from typing import Iterable, Mapping

import sympy as sp


MultiIndex = tuple[int, ...]


def zero_index(dimension: int) -> MultiIndex:
    return (0,) * dimension


def unit_index(dimension: int, axis: int) -> MultiIndex:
    return tuple(1 if i == axis else 0 for i in range(dimension))


def add_indices(left: MultiIndex, right: MultiIndex) -> MultiIndex:
    return tuple(a + b for a, b in zip(left, right))


def subindices(alpha: MultiIndex) -> Iterable[MultiIndex]:
    return product(*(range(power + 1) for power in alpha))


def multi_binomial(alpha: MultiIndex, beta: MultiIndex) -> int:
    result = 1
    for a, b in zip(alpha, beta):
        result *= math.comb(a, b)
    return result


def differentiate_matrix(
    matrix: sp.MatrixBase,
    coordinates: tuple[sp.Symbol, ...],
    alpha: MultiIndex,
) -> sp.ImmutableMatrix:
    value = sp.Matrix(matrix)
    for coordinate, power in zip(coordinates, alpha):
        if power:
            value = value.applyfunc(lambda item: sp.diff(item, coordinate, power))
    return sp.ImmutableMatrix(value.applyfunc(sp.simplify))


@dataclass(frozen=True)
class SparseDifferentialOperator:
    coordinates: tuple[sp.Symbol, ...]
    input_dimension: int
    output_dimension: int
    coefficients: Mapping[MultiIndex, sp.ImmutableMatrix]

    def __post_init__(self) -> None:
        dimension = len(self.coordinates)
        normalized: dict[MultiIndex, sp.ImmutableMatrix] = {}
        for alpha, coefficient in self.coefficients.items():
            if len(alpha) != dimension or any(power < 0 for power in alpha):
                raise ValueError(f"invalid multiindex {alpha}")
            matrix = sp.ImmutableMatrix(coefficient)
            if matrix.shape != (self.output_dimension, self.input_dimension):
                raise ValueError(
                    f"coefficient {alpha} has shape {matrix.shape}, expected "
                    f"{(self.output_dimension, self.input_dimension)}"
                )
            if matrix != sp.zeros(*matrix.shape):
                normalized[tuple(alpha)] = matrix
        object.__setattr__(self, "coefficients", normalized)

    @classmethod
    def multiplication(
        cls,
        coordinates: tuple[sp.Symbol, ...],
        matrix: sp.MatrixBase,
    ) -> "SparseDifferentialOperator":
        matrix = sp.ImmutableMatrix(matrix)
        return cls(coordinates, matrix.cols, matrix.rows, {zero_index(len(coordinates)): matrix})

    @classmethod
    def partial(
        cls,
        coordinates: tuple[sp.Symbol, ...],
        carrier_dimension: int,
        axis: int,
    ) -> "SparseDifferentialOperator":
        return cls(
            coordinates,
            carrier_dimension,
            carrier_dimension,
            {unit_index(len(coordinates), axis): sp.eye(carrier_dimension)},
        )

    def apply(self, vector: sp.MatrixBase) -> sp.ImmutableMatrix:
        vector = sp.Matrix(vector)
        if vector.shape != (self.input_dimension, 1):
            raise ValueError("input vector has the wrong shape")
        result = sp.zeros(self.output_dimension, 1)
        for alpha, coefficient in self.coefficients.items():
            differentiated = vector
            for coordinate, power in zip(self.coordinates, alpha):
                if power:
                    differentiated = differentiated.applyfunc(
                        lambda item: sp.diff(item, coordinate, power)
                    )
            result += sp.Matrix(coefficient) * differentiated
        return sp.ImmutableMatrix(result.applyfunc(sp.simplify))

    def compose(self, inner: "SparseDifferentialOperator") -> "SparseDifferentialOperator":
        """Return self after inner, with the complete multivariate Leibniz rule."""
        if self.coordinates != inner.coordinates:
            raise ValueError("coordinate systems differ")
        if self.input_dimension != inner.output_dimension:
            raise ValueError("carrier dimensions do not compose")
        output: dict[MultiIndex, sp.Matrix] = {}
        for alpha, outer_coefficient in self.coefficients.items():
            for beta in subindices(alpha):
                derivative_order = tuple(a - b for a, b in zip(alpha, beta))
                binomial = multi_binomial(alpha, beta)
                for gamma, inner_coefficient in inner.coefficients.items():
                    target = add_indices(beta, gamma)
                    term = (
                        binomial
                        * sp.Matrix(outer_coefficient)
                        * sp.Matrix(
                            differentiate_matrix(
                                inner_coefficient, self.coordinates, derivative_order
                            )
                        )
                    )
                    output[target] = output.get(
                        target, sp.zeros(self.output_dimension, inner.input_dimension)
                    ) + term
        return SparseDifferentialOperator(
            self.coordinates,
            inner.input_dimension,
            self.output_dimension,
            {alpha: sp.ImmutableMatrix(matrix.applyfunc(sp.simplify)) for alpha, matrix in output.items()},
        )

    def formal_transpose(self) -> "SparseDifferentialOperator":
        """Formal transpose for the coordinate density and standard pairings."""
        output: dict[MultiIndex, sp.Matrix] = {}
        for alpha, coefficient in self.coefficients.items():
            sign = (-1) ** sum(alpha)
            for beta in subindices(alpha):
                derivative_order = tuple(a - b for a, b in zip(alpha, beta))
                target = tuple(beta)
                term = (
                    sign
                    * multi_binomial(alpha, beta)
                    * sp.Matrix(
                        differentiate_matrix(
                            coefficient.T, self.coordinates, derivative_order
                        )
                    )
                )
                output[target] = output.get(
                    target, sp.zeros(self.input_dimension, self.output_dimension)
                ) + term
        return SparseDifferentialOperator(
            self.coordinates,
            self.output_dimension,
            self.input_dimension,
            {alpha: sp.ImmutableMatrix(matrix.applyfunc(sp.simplify)) for alpha, matrix in output.items()},
        )

    def weighted_formal_adjoint(
        self,
        input_pairing: sp.MatrixBase,
        output_pairing: sp.MatrixBase,
        density: sp.Expr,
    ) -> "SparseDifferentialOperator":
        """Adjoint for integral rho*u^T B v, including every moving coefficient."""
        input_pairing = sp.Matrix(input_pairing)
        output_pairing = sp.Matrix(output_pairing)
        left = SparseDifferentialOperator.multiplication(
            self.coordinates, sp.simplify(input_pairing.inv() / density)
        )
        weighted_output = SparseDifferentialOperator.multiplication(
            self.coordinates, sp.simplify(density * output_pairing)
        )
        return left.compose(self.formal_transpose().compose(weighted_output))

    def coefficient(self, alpha: MultiIndex) -> sp.ImmutableMatrix:
        return self.coefficients.get(
            alpha, sp.ImmutableMatrix.zeros(self.output_dimension, self.input_dimension)
        )

    def maximum_order(self) -> int:
        return max((sum(alpha) for alpha in self.coefficients), default=-1)


def total_covariant_derivative(
    coordinates: tuple[sp.Symbol, ...],
    axis: int,
    connection: sp.MatrixBase,
) -> SparseDifferentialOperator:
    """D_axis + connection on one already-flattened target carrier."""
    connection = sp.Matrix(connection)
    if connection.rows != connection.cols:
        raise ValueError("connection matrix must be square")
    partial = SparseDifferentialOperator.partial(coordinates, connection.rows, axis)
    multiplication = SparseDifferentialOperator.multiplication(coordinates, connection)
    coefficients = dict(partial.coefficients)
    for alpha, coefficient in multiplication.coefficients.items():
        coefficients[alpha] = coefficients.get(alpha, sp.zeros(*coefficient.shape)) + coefficient
    return SparseDifferentialOperator(
        coordinates, connection.rows, connection.rows, coefficients
    )


def integration_by_parts_residual(
    operator: SparseDifferentialOperator,
    adjoint: SparseDifferentialOperator,
    left_test: sp.MatrixBase,
    right_test: sp.MatrixBase,
    input_pairing: sp.MatrixBase,
    output_pairing: sp.MatrixBase,
    density: sp.Expr,
) -> sp.Expr:
    """Euler residual; a correct formal adjoint is a total divergence."""
    left_test = sp.Matrix(left_test)
    right_test = sp.Matrix(right_test)
    first = (left_test.T * sp.Matrix(output_pairing) * sp.Matrix(operator.apply(right_test)))[0]
    second = (sp.Matrix(adjoint.apply(left_test)).T * sp.Matrix(input_pairing) * right_test)[0]
    return sp.expand(density * (first - second))
