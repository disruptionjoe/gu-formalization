#!/usr/bin/env python3
"""Exact third-jet null fivefold adapter for the selected conditional Shiab.

K154 closes the 448-dimensional action packet through second coefficient jets
and computes the complete restricted order-five coefficient.  This module adds
exactly the next jet horizon: the third principal jet, second formal-Euler
lower jet, second jet of K152's moving order-two bridge symbol, and its
Weyl-dependent zero-order coefficient.  It computes the complete order-four
coefficient of ``K P**5 K A``; no lower coefficient or all-order descent is
inferred.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Iterable, Mapping, Sequence

import sympy as sp

import k150_moving_selected_shiab_coordinate_adapter as K150
import k154_null_fivefold_second_lower_adapter as K154

K151 = K154.K151
K152 = K154.K152
K153 = K154.K153


BasisEntry = tuple[int, int, int]
POLYNOMIAL_DEGREE_BOUND = 9
INTERPOLATION_POINTS = tuple(sp.Integer(value) for value in range(10))


def _output_labels(
    covector: tuple[sp.Expr, ...],
    labels: Iterable[int],
    phi_one: K150.Form,
    phi_two: K150.Form,
) -> set[int]:
    covector_form = K150.scalar_one_form(covector)
    output: set[int] = set()
    for label in labels:
        for mu in range(K150.N):
            curvature = K150.wedge_raw(
                covector_form, K150.direction(mu, label ^ (1 << mu))
            )
            image = K150.selected_shiab(curvature, phi_one, phi_two)
            output.update(
                mask ^ (1 << nu) for nu, mask, _ in K150.rows_for_image(image)
            )
    return output


def close_third_jet_labels(
    covector4: tuple[sp.Expr, ...],
    coordinate: sp.Symbol,
    generator: K150.Element,
    seeds: Iterable[int] = K153.SEED_LABELS,
) -> tuple[int, ...]:
    """Close the bridge seed under every polynomially live third-jet output.

    The order-three conjugation series makes ``Phi_1`` degree three and
    ``Phi_2=Phi_1 wedge Phi_1/2`` degree six.  The selected two-term Shiab is
    therefore degree at most nine.  A nonzero polynomial of degree at most
    nine cannot vanish at all ten interpolation points, so the union of their
    exact supports equals the full polynomial support without symbolic
    simplification of the degree-nine expressions.
    """
    covector = tuple(covector4) + (sp.Integer(0),) * 10
    phi_one, phi_two = K150.moving_phi((coordinate,), (generator,), 3)
    samples = tuple(
        (
            _evaluate_form(phi_one, coordinate, point),
            _evaluate_form(phi_two, coordinate, point),
        )
        for point in INTERPOLATION_POINTS
    )
    labels = set(seeds)
    while True:
        outputs: set[int] = set()
        for phi_one_value, phi_two_value in samples:
            outputs |= _output_labels(
                covector, labels, phi_one_value, phi_two_value
            )
        enlarged = labels | outputs
        if enlarged == labels:
            return tuple(sorted(labels))
        labels = enlarged


def _evaluate_form(
    form: K150.Form, coordinate: sp.Symbol, value: sp.Expr
) -> K150.Form:
    return {
        form_mask: {
            clifford_mask: (
                sp.expand(real.subs(coordinate, value)),
                sp.expand(imaginary.subs(coordinate, value)),
            )
            for clifford_mask, (real, imaginary) in element.items()
        }
        for form_mask, element in form.items()
    }


def _raw_block_at_phi(
    covector: tuple[sp.Expr, ...],
    labels: tuple[int, ...],
    phi_one: K150.Form,
    phi_two: K150.Form,
) -> tuple[tuple[BasisEntry, ...], sp.SparseMatrix]:
    covector_form = K150.scalar_one_form(covector)
    basis = tuple(
        (label, mu, label ^ (1 << mu))
        for label in labels
        for mu in range(K150.N)
    )
    index = {
        (label, mu): position
        for position, (label, mu, _) in enumerate(basis)
    }
    raw = sp.MutableSparseMatrix(len(basis), len(basis), {})
    for column, (_, mu, mask) in enumerate(basis):
        curvature = K150.wedge_raw(covector_form, K150.direction(mu, mask))
        image = K150.selected_shiab(curvature, phi_one, phi_two)
        for nu, output_mask, scalar in K150.rows_for_image(image):
            row = index.get((output_mask ^ (1 << nu), nu))
            if row is None:
                continue
            real, imaginary = scalar
            raw[row, column] += sp.expand(real + sp.I * imaginary)
    return basis, sp.SparseMatrix(raw)


def interpolated_raw_jets(
    covector: tuple[sp.Expr, ...],
    labels: tuple[int, ...],
    coordinate: sp.Symbol,
    generator: K150.Element,
    maximum_jet: int = 3,
) -> tuple[tuple[BasisEntry, ...], tuple[sp.SparseMatrix, ...]]:
    """Recover raw coefficient jets exactly from the ten-point degree bound."""
    if not 0 <= maximum_jet <= POLYNOMIAL_DEGREE_BOUND:
        raise ValueError("maximum_jet exceeds the polynomial degree bound")
    phi_one, phi_two = K150.moving_phi((coordinate,), (generator,), 3)
    samples: list[sp.SparseMatrix] = []
    basis: tuple[BasisEntry, ...] | None = None
    for point in INTERPOLATION_POINTS:
        sample_basis, raw = _raw_block_at_phi(
            covector,
            labels,
            _evaluate_form(phi_one, coordinate, point),
            _evaluate_form(phi_two, coordinate, point),
        )
        if basis is None:
            basis = sample_basis
        elif sample_basis != basis:
            raise ValueError("interpolation samples changed the packet basis")
        samples.append(raw)

    vandermonde = sp.Matrix(
        [
            [point**degree for degree in range(POLYNOMIAL_DEGREE_BOUND + 1)]
            for point in INTERPOLATION_POINTS
        ]
    )
    inverse = vandermonde.inv()
    jets: list[sp.SparseMatrix] = []
    for order in range(maximum_jet + 1):
        jet = sp.SparseMatrix.zeros(samples[0].rows, samples[0].cols)
        for sample_index, sample in enumerate(samples):
            weight = sp.factorial(order) * inverse[order, sample_index]
            if weight:
                jet += weight * sample
        jets.append(sp.SparseMatrix(jet))
    assert basis is not None
    return basis, tuple(jets)


def _sparse(value: sp.MatrixBase) -> sp.SparseMatrix:
    return sp.SparseMatrix(value)


def top_power_layers(
    principal_jets: Sequence[sp.MatrixBase],
    lower_jets: Sequence[sp.MatrixBase],
    power: int,
    horizon: int,
) -> tuple[sp.SparseMatrix, ...]:
    """Return the top ``horizon + 1`` layers of ``(A(t)D+B(t))**power``.

    ``principal_jets[j]`` and ``lower_jets[j]`` are ordinary derivatives at
    the origin, not divided-power Taylor coefficients.  The recurrence is the
    exact one-variable Leibniz rule

    ``(A D+B) o sum(C_r D^r) = sum((A C_{r-1}+A C_r'+B C_r) D^r)``.

    Only coefficient jets that can reach the requested layer horizon are
    propagated.  The principal input therefore needs jets zero through
    ``horizon`` and the lower input jets zero through ``horizon-1``.
    """
    if power < 1:
        raise ValueError("power must be positive")
    if horizon < 0 or horizon > power:
        raise ValueError("horizon must lie between zero and power")
    if len(principal_jets) < horizon + 1:
        raise ValueError("insufficient principal jets")
    if horizon and len(lower_jets) < horizon:
        raise ValueError("insufficient lower jets")

    a = tuple(_sparse(matrix) for matrix in principal_jets[: horizon + 1])
    b = tuple(_sparse(matrix) for matrix in lower_jets[:horizon])
    dimension = a[0].rows
    zero = sp.SparseMatrix.zeros(dimension, dimension)

    # (differential order, coordinate-jet order) -> coefficient jet.
    coefficients: dict[tuple[int, int], sp.SparseMatrix] = {
        (1, jet): matrix for jet, matrix in enumerate(a)
    }
    coefficients.update({(0, jet): matrix for jet, matrix in enumerate(b)})

    def get(
        source: Mapping[tuple[int, int], sp.SparseMatrix], order: int, jet: int
    ) -> sp.SparseMatrix:
        if order < 0 or jet < 0:
            return zero
        return source.get((order, jet), zero)

    for current_power in range(1, power):
        next_power = current_power + 1
        updated: dict[tuple[int, int], sp.SparseMatrix] = {}
        for deficit in range(horizon + 1):
            order = next_power - deficit
            for jet in range(horizon - deficit + 1):
                value = zero
                for split in range(jet + 1):
                    factor = math.comb(jet, split)
                    a_split = a[split]
                    left = get(coefficients, order - 1, jet - split)
                    derived = get(coefficients, order, jet - split + 1)
                    if left.nnz():
                        value += factor * a_split * left
                    if derived.nnz():
                        value += factor * a_split * derived
                    if split < len(b):
                        same = get(coefficients, order, jet - split)
                        if same.nnz():
                            value += factor * b[split] * same
                updated[(order, jet)] = _sparse(value)
        coefficients = updated

    return tuple(
        get(coefficients, power - deficit, 0)
        for deficit in range(horizon + 1)
    )


@dataclass(frozen=True)
class NullFivefoldThirdLower:
    covector4: tuple[sp.Expr, ...]
    coordinate: sp.Symbol
    labels: tuple[int, ...]
    basis: tuple[BasisEntry, ...]
    lowerer: sp.SparseMatrix
    raw_value: sp.SparseMatrix
    raw_first_jet: sp.SparseMatrix
    raw_second_jet: sp.SparseMatrix
    raw_third_jet: sp.SparseMatrix
    p_principal_value: sp.SparseMatrix
    p_principal_first_jet: sp.SparseMatrix
    p_principal_second_jet: sp.SparseMatrix
    p_principal_third_jet: sp.SparseMatrix
    p_lower_value: sp.SparseMatrix
    p_lower_first_jet: sp.SparseMatrix
    p_lower_second_jet: sp.SparseMatrix
    fifth_principal_value: sp.SparseMatrix
    fifth_first_lower_value: sp.SparseMatrix
    fifth_second_lower_value: sp.SparseMatrix
    fifth_third_lower_value: sp.SparseMatrix

    @property
    def dimension(self) -> int:
        return len(self.basis)


def build_null_fivefold_third_lower(
    covector4: tuple[sp.Expr, ...],
    coordinate: sp.Symbol,
    generator: K150.Element,
    labels: tuple[int, ...] = K153.FIRST_JET_CLOSED_LABELS,
) -> NullFivefoldThirdLower:
    covector = tuple(covector4) + (sp.Integer(0),) * 10
    basis, raw_jets = interpolated_raw_jets(
        covector, labels, coordinate, generator, 3
    )
    lowerer = _sparse(K151.distortion_lowerer(basis))
    principal_jets = tuple(
        _sparse(lowerer * ((matrix - matrix.T) / 2))
        for matrix in raw_jets
    )
    lower_jets = tuple(
        _sparse(lowerer * (-raw_jets[order + 1].T / 2))
        for order in range(3)
    )
    fifth = top_power_layers(principal_jets, lower_jets, 5, 3)
    return NullFivefoldThirdLower(
        covector4=tuple(covector4),
        coordinate=coordinate,
        labels=tuple(labels),
        basis=basis,
        lowerer=lowerer,
        raw_value=raw_jets[0],
        raw_first_jet=raw_jets[1],
        raw_second_jet=raw_jets[2],
        raw_third_jet=raw_jets[3],
        p_principal_value=principal_jets[0],
        p_principal_first_jet=principal_jets[1],
        p_principal_second_jet=principal_jets[2],
        p_principal_third_jet=principal_jets[3],
        p_lower_value=lower_jets[0],
        p_lower_first_jet=lower_jets[1],
        p_lower_second_jet=lower_jets[2],
        fifth_principal_value=fifth[0],
        fifth_first_lower_value=fifth[1],
        fifth_second_lower_value=fifth[2],
        fifth_third_lower_value=fifth[3],
    )


def embedded_bridge_coefficient_jet(
    packet: NullFivefoldThirdLower,
    bridge: K152.CurvedMetricBridge,
    substitutions: Mapping[sp.Symbol, sp.Expr],
    coefficient_order: int,
    derivative_axis: int,
    derivative_order: int,
) -> sp.SparseMatrix:
    """Embed one coordinate jet of a K152 bridge coefficient."""
    packet_index = {entry: index for index, entry in enumerate(packet.basis)}
    embedding = sp.MutableSparseMatrix(packet.dimension, len(bridge.basis), {})
    for column, entry in enumerate(bridge.basis):
        if entry not in packet_index:
            raise ValueError(
                f"bridge basis entry {entry} is outside the third-jet packet"
            )
        embedding[packet_index[entry], column] = 1

    coefficient = sp.zeros(
        bridge.density_dual.output_dimension,
        bridge.density_dual.input_dimension,
    )
    for alpha, matrix in bridge.density_dual.coefficients.items():
        if sum(alpha) != coefficient_order:
            continue
        monomial = sp.prod(
            value**power for value, power in zip(packet.covector4, alpha)
        )
        coefficient += monomial * sp.Matrix(matrix)
    coordinate = bridge.coordinates[derivative_axis]
    coefficient = coefficient.diff(coordinate, derivative_order).subs(
        substitutions
    )
    return _sparse(embedding * _sparse(coefficient))


@dataclass(frozen=True)
class RestrictedThirdLower:
    direct_term: sp.SparseMatrix
    first_bridge_jet_term: sp.SparseMatrix
    second_bridge_jet_term: sp.SparseMatrix
    zero_order_bridge_term: sp.SparseMatrix
    complete: sp.SparseMatrix


def restricted_third_lower(
    packet: NullFivefoldThirdLower,
    bridge: K152.CurvedMetricBridge,
    substitutions: Mapping[sp.Symbol, sp.Expr],
    derivative_axis: int = 0,
) -> RestrictedThirdLower:
    """Complete order-four coefficient of ``K P**5 K A``.

    K152 has order-two and order-zero coefficients but no order-one
    coefficient.  Since ``[P**5]_5`` vanishes at the null jet origin, the
    complete total-order-four coefficient is

    ``K [P**5]_2 K A_2 + 3 K [P**5]_3 K (A_2)'``
    ``+ 6 K [P**5]_4 K (A_2)'' + K [P**5]_4 K A_0``.
    """
    bridge_value = embedded_bridge_coefficient_jet(
        packet, bridge, substitutions, 2, derivative_axis, 0
    )
    bridge_first = embedded_bridge_coefficient_jet(
        packet, bridge, substitutions, 2, derivative_axis, 1
    )
    bridge_second = embedded_bridge_coefficient_jet(
        packet, bridge, substitutions, 2, derivative_axis, 2
    )
    bridge_zero = embedded_bridge_coefficient_jet(
        packet, bridge, substitutions, 0, derivative_axis, 0
    )
    direct = _sparse(
        packet.lowerer
        * packet.fifth_third_lower_value
        * packet.lowerer
        * bridge_value
    )
    first_jet = _sparse(
        3
        * packet.lowerer
        * packet.fifth_second_lower_value
        * packet.lowerer
        * bridge_first
    )
    second_jet = _sparse(
        6
        * packet.lowerer
        * packet.fifth_first_lower_value
        * packet.lowerer
        * bridge_second
    )
    zero_order = _sparse(
        packet.lowerer
        * packet.fifth_first_lower_value
        * packet.lowerer
        * bridge_zero
    )
    return RestrictedThirdLower(
        direct_term=direct,
        first_bridge_jet_term=first_jet,
        second_bridge_jet_term=second_jet,
        zero_order_bridge_term=zero_order,
        complete=_sparse(direct + first_jet + second_jet + zero_order),
    )


def frozen_third_lower(principal_value: sp.MatrixBase) -> sp.SparseMatrix:
    zero = sp.SparseMatrix.zeros(principal_value.rows, principal_value.cols)
    return top_power_layers((principal_value, zero, zero, zero), (zero, zero, zero), 5, 3)[3]
