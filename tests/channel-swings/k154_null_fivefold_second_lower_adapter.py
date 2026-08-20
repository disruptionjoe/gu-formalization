#!/usr/bin/env python3
"""Exact second-jet null fivefold adapter for the selected conditional Shiab.

K153 closes the 448-dimensional action packet and propagates the top and first
lower coefficients of ``P**5``.  This module adds exactly the coefficient jets
needed for the next layer: the second jet of the principal coefficient, the
first jet of the formal-Euler lower coefficient, and the first jet of K152's
moving order-two bridge symbol.  It computes the complete order-five
coefficient of ``K P**5 K A``; no lower coefficient or all-order descent is
inferred.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Mapping

import sympy as sp

import k150_moving_selected_shiab_coordinate_adapter as K150
import k153_null_fivefold_first_lower_adapter as K153

K151 = K153.K151
K152 = K153.K152


BasisEntry = tuple[int, int, int]


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


def close_second_jet_labels(
    covector4: tuple[sp.Expr, ...],
    coordinate: sp.Symbol,
    generator: K150.Element,
    seeds: Iterable[int] = K153.SEED_LABELS,
) -> tuple[int, ...]:
    """Close the bridge seed under every polynomially live second-jet output."""
    covector = tuple(covector4) + (sp.Integer(0),) * 10
    phi_one, phi_two = K150.moving_phi((coordinate,), (generator,), 2)
    labels = set(seeds)
    while True:
        enlarged = labels | _output_labels(covector, labels, phi_one, phi_two)
        if enlarged == labels:
            return tuple(sorted(labels))
        labels = enlarged


@dataclass(frozen=True)
class NullFivefoldSecondLower:
    covector4: tuple[sp.Expr, ...]
    coordinate: sp.Symbol
    labels: tuple[int, ...]
    basis: tuple[BasisEntry, ...]
    lowerer: sp.SparseMatrix
    raw_value: sp.SparseMatrix
    raw_first_jet: sp.SparseMatrix
    raw_second_jet: sp.SparseMatrix
    p_principal_value: sp.SparseMatrix
    p_principal_first_jet: sp.SparseMatrix
    p_principal_second_jet: sp.SparseMatrix
    p_lower_value: sp.SparseMatrix
    p_lower_first_jet: sp.SparseMatrix
    fifth_principal_value: sp.SparseMatrix
    fifth_first_lower_value: sp.SparseMatrix
    fifth_second_lower_value: sp.SparseMatrix

    @property
    def dimension(self) -> int:
        return len(self.basis)


def top_three_power_layers(
    principal_value: sp.SparseMatrix,
    principal_first_jet: sp.SparseMatrix,
    principal_second_jet: sp.SparseMatrix,
    lower_value: sp.SparseMatrix,
    lower_first_jet: sp.SparseMatrix,
    power: int,
) -> tuple[sp.SparseMatrix, sp.SparseMatrix, sp.SparseMatrix]:
    """Return the top three coefficient layers of ``(A(t)D+B(t))**power``.

    Jets are ordinary derivatives at the origin, not divided-power Taylor
    coefficients.  The recurrence is the complete one-variable Leibniz rule
    restricted to the exact horizon that can affect orders ``power``,
    ``power-1`` and ``power-2``.
    """
    if power < 2:
        raise ValueError("power must be at least two")

    a0 = sp.SparseMatrix(principal_value)
    a1 = sp.SparseMatrix(principal_first_jet)
    a2 = sp.SparseMatrix(principal_second_jet)
    b0 = sp.SparseMatrix(lower_value)
    b1 = sp.SparseMatrix(lower_first_jet)

    top0, top1, top2 = a0, a1, a2
    first0, first1 = b0, b1
    second0 = sp.SparseMatrix.zeros(a0.rows, a0.cols)

    for _ in range(1, power):
        next_second0 = a0 * second0 + a0 * first1 + b0 * first0
        next_first1 = (
            a1 * first0
            + a0 * first1
            + a1 * top1
            + a0 * top2
            + b1 * top0
            + b0 * top1
        )
        next_first0 = a0 * first0 + a0 * top1 + b0 * top0
        next_top2 = a2 * top0 + 2 * a1 * top1 + a0 * top2
        next_top1 = a1 * top0 + a0 * top1
        next_top0 = a0 * top0
        top0, top1, top2 = (
            sp.SparseMatrix(next_top0),
            sp.SparseMatrix(next_top1),
            sp.SparseMatrix(next_top2),
        )
        first0, first1 = (
            sp.SparseMatrix(next_first0),
            sp.SparseMatrix(next_first1),
        )
        second0 = sp.SparseMatrix(next_second0)

    return top0, first0, second0


def build_null_fivefold_second_lower(
    covector4: tuple[sp.Expr, ...],
    coordinate: sp.Symbol,
    generator: K150.Element,
    labels: tuple[int, ...] = K153.FIRST_JET_CLOSED_LABELS,
) -> NullFivefoldSecondLower:
    covector = tuple(covector4) + (sp.Integer(0),) * 10
    adapter = K150.MovingSelectedShiabAdapter((coordinate,), (generator,), 2)
    basis_list, raw, _ = adapter.raw_block(covector, labels)
    basis = tuple(tuple(entry) for entry in basis_list)
    lowerer = sp.SparseMatrix(K151.distortion_lowerer(basis))
    raw_value = sp.SparseMatrix(raw.subs(coordinate, 0))
    raw_first_jet = sp.SparseMatrix(raw.diff(coordinate).subs(coordinate, 0))
    raw_second_jet = sp.SparseMatrix(
        raw.diff(coordinate, 2).subs(coordinate, 0)
    )

    c0 = sp.SparseMatrix((raw_value - raw_value.T) / 2)
    c1 = sp.SparseMatrix((raw_first_jet - raw_first_jet.T) / 2)
    c2 = sp.SparseMatrix((raw_second_jet - raw_second_jet.T) / 2)
    d0 = sp.SparseMatrix(-raw_first_jet.T / 2)
    d1 = sp.SparseMatrix(-raw_second_jet.T / 2)
    a0, a1, a2 = lowerer * c0, lowerer * c1, lowerer * c2
    b0, b1 = lowerer * d0, lowerer * d1
    fifth_top, fifth_first, fifth_second = top_three_power_layers(
        a0, a1, a2, b0, b1, 5
    )
    return NullFivefoldSecondLower(
        covector4=tuple(covector4),
        coordinate=coordinate,
        labels=tuple(labels),
        basis=basis,
        lowerer=lowerer,
        raw_value=raw_value,
        raw_first_jet=raw_first_jet,
        raw_second_jet=raw_second_jet,
        p_principal_value=sp.SparseMatrix(a0),
        p_principal_first_jet=sp.SparseMatrix(a1),
        p_principal_second_jet=sp.SparseMatrix(a2),
        p_lower_value=sp.SparseMatrix(b0),
        p_lower_first_jet=sp.SparseMatrix(b1),
        fifth_principal_value=fifth_top,
        fifth_first_lower_value=fifth_first,
        fifth_second_lower_value=fifth_second,
    )


def embedded_bridge_symbol_jet(
    packet: NullFivefoldSecondLower,
    bridge: K152.CurvedMetricBridge,
    substitutions: Mapping[sp.Symbol, sp.Expr],
    derivative_axis: int,
    derivative_order: int,
) -> sp.SparseMatrix:
    """Embed a coordinate jet of K152's moving order-two bridge symbol."""
    packet_index = {entry: index for index, entry in enumerate(packet.basis)}
    embedding = sp.MutableSparseMatrix(packet.dimension, len(bridge.basis), {})
    for column, entry in enumerate(bridge.basis):
        if entry not in packet_index:
            raise ValueError(
                f"bridge basis entry {entry} is outside the second-jet packet"
            )
        embedding[packet_index[entry], column] = 1

    symbol = sp.zeros(
        bridge.density_dual.output_dimension,
        bridge.density_dual.input_dimension,
    )
    for alpha, coefficient in bridge.density_dual.coefficients.items():
        if sum(alpha) != 2:
            continue
        monomial = sp.prod(
            value**power for value, power in zip(packet.covector4, alpha)
        )
        symbol += monomial * sp.Matrix(coefficient)
    coordinate = bridge.coordinates[derivative_axis]
    symbol = symbol.diff(coordinate, derivative_order).subs(substitutions)
    return sp.SparseMatrix(embedding * sp.SparseMatrix(symbol))


@dataclass(frozen=True)
class RestrictedSecondLower:
    direct_term: sp.SparseMatrix
    bridge_jet_term: sp.SparseMatrix
    complete: sp.SparseMatrix


def restricted_second_lower(
    packet: NullFivefoldSecondLower,
    bridge: K152.CurvedMetricBridge,
    substitutions: Mapping[sp.Symbol, sp.Expr],
    derivative_axis: int = 0,
) -> RestrictedSecondLower:
    """Complete order-five coefficient of ``K P**5 K A``.

    K152 has order-two and order-zero coefficients but no order-one
    coefficient.  Since ``[P**5]_5`` vanishes at the null jet origin, the
    complete total-order-five coefficient is

    ``K [P**5]_3 K A_2 + 4 K [P**5]_4 K (A_2)'``.
    """
    bridge_value = embedded_bridge_symbol_jet(
        packet, bridge, substitutions, derivative_axis, 0
    )
    bridge_first_jet = embedded_bridge_symbol_jet(
        packet, bridge, substitutions, derivative_axis, 1
    )
    direct = sp.SparseMatrix(
        packet.lowerer
        * packet.fifth_second_lower_value
        * packet.lowerer
        * bridge_value
    )
    bridge_jet = sp.SparseMatrix(
        4
        * packet.lowerer
        * packet.fifth_first_lower_value
        * packet.lowerer
        * bridge_first_jet
    )
    return RestrictedSecondLower(
        direct_term=direct,
        bridge_jet_term=bridge_jet,
        complete=sp.SparseMatrix(direct + bridge_jet),
    )


def frozen_second_lower(principal_value: sp.SparseMatrix) -> sp.SparseMatrix:
    zero = sp.SparseMatrix.zeros(principal_value.rows, principal_value.cols)
    return top_three_power_layers(
        principal_value, zero, zero, zero, zero, 5
    )[2]
