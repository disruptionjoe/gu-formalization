#!/usr/bin/env python3
"""Exact first-jet null fivefold adapter for the selected conditional Shiab.

K152's 112-dimensional bridge packet is an output packet, not an invariant
distortion carrier.  This module closes that seed under the frozen and
first-coordinate-jet selected-Shiab action, constructs the native generalized
coefficient ``P = K C``, and propagates only the top and first-lower
coefficients of ``P**5``.  That is the smallest coefficient horizon needed by
K153; later lower coefficients require higher jets and are deliberately not
inferred here.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb
from typing import Iterable, Mapping

import sympy as sp
from sympy.polys.matrices import DomainMatrix

import k150_moving_selected_shiab_coordinate_adapter as K150
import k151_moving_distortion_pairing_adapter as K151
import k152_curved_metric_bridge_adapter as K152


BasisEntry = tuple[int, int, int]
SEED_LABELS = (0, 3, 5, 6, 9, 10, 12, 17)
FIRST_JET_CLOSED_LABELS = tuple(range(32))


def exact_rank(matrix: sp.MatrixBase) -> int:
    """Fast exact rank over the smallest extension field containing entries."""
    return DomainMatrix.from_Matrix(sp.Matrix(matrix), extension=True).rank()


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
            output.update(mask ^ (1 << nu) for nu, mask, _ in K150.rows_for_image(image))
    return output


def close_first_jet_labels(
    covector4: tuple[sp.Expr, ...],
    coordinate: sp.Symbol,
    generator: K150.Element,
    seeds: Iterable[int] = SEED_LABELS,
) -> tuple[int, ...]:
    """Close bridge labels under every polynomially live first-jet output."""
    covector = tuple(covector4) + (sp.Integer(0),) * 10
    phi_one, phi_two = K150.moving_phi((coordinate,), (generator,), 1)
    labels = set(seeds)
    while True:
        enlarged = labels | _output_labels(covector, labels, phi_one, phi_two)
        if enlarged == labels:
            return tuple(sorted(labels))
        labels = enlarged


@dataclass(frozen=True)
class NullFivefoldFirstLower:
    covector4: tuple[sp.Expr, ...]
    coordinate: sp.Symbol
    labels: tuple[int, ...]
    basis: tuple[BasisEntry, ...]
    lowerer: sp.SparseMatrix
    raw_value: sp.SparseMatrix
    raw_first_jet: sp.SparseMatrix
    p_principal_value: sp.SparseMatrix
    p_principal_first_jet: sp.SparseMatrix
    p_lower_value: sp.SparseMatrix
    fifth_principal_value: sp.SparseMatrix
    fifth_first_lower_value: sp.SparseMatrix

    @property
    def dimension(self) -> int:
        return len(self.basis)


def top_and_first_lower_power(
    principal_value: sp.SparseMatrix,
    principal_first_jet: sp.SparseMatrix,
    lower_value: sp.SparseMatrix,
    power: int,
) -> tuple[sp.SparseMatrix, sp.SparseMatrix]:
    """Return D**power and D**(power-1) coefficients at the jet origin.

    For ``P=A(t)D+B(t)``, only ``A(0)``, ``A'(0)`` and ``B(0)`` enter this
    horizon.  The recursion is the exact one-variable Leibniz rule, not a
    frozen matrix power.
    """
    if power < 1:
        raise ValueError("power must be positive")
    top = principal_value
    top_first_jet = principal_first_jet
    lower = lower_value
    for _ in range(1, power):
        lower = (
            principal_value * lower
            + principal_value * top_first_jet
            + lower_value * top
        )
        top_first_jet = (
            principal_first_jet * top + principal_value * top_first_jet
        )
        top = principal_value * top
    return sp.SparseMatrix(top), sp.SparseMatrix(lower)


def build_null_fivefold_first_lower(
    covector4: tuple[sp.Expr, ...],
    coordinate: sp.Symbol,
    generator: K150.Element,
    labels: tuple[int, ...] = FIRST_JET_CLOSED_LABELS,
) -> NullFivefoldFirstLower:
    covector = tuple(covector4) + (sp.Integer(0),) * 10
    adapter = K150.MovingSelectedShiabAdapter((coordinate,), (generator,), 1)
    basis_list, raw, _ = adapter.raw_block(covector, labels)
    basis = tuple(tuple(entry) for entry in basis_list)
    lowerer = sp.SparseMatrix(K151.distortion_lowerer(basis))
    raw_value = sp.SparseMatrix(raw.subs(coordinate, 0))
    raw_first_jet = sp.SparseMatrix(raw.diff(coordinate).subs(coordinate, 0))

    # C is the lowered formal-Euler operator.  P=K C is field-like.  Constant
    # K and unit density are exact for this inner-Spin chart (K151).
    c_principal_value = sp.SparseMatrix((raw_value - raw_value.T) / 2)
    c_principal_first_jet = sp.SparseMatrix(
        (raw_first_jet - raw_first_jet.T) / 2
    )
    c_lower_value = sp.SparseMatrix(-raw_first_jet.T / 2)
    p_principal_value = lowerer * c_principal_value
    p_principal_first_jet = lowerer * c_principal_first_jet
    p_lower_value = lowerer * c_lower_value
    fifth_principal, fifth_first_lower = top_and_first_lower_power(
        p_principal_value, p_principal_first_jet, p_lower_value, 5
    )
    return NullFivefoldFirstLower(
        covector4=tuple(covector4),
        coordinate=coordinate,
        labels=tuple(labels),
        basis=basis,
        lowerer=lowerer,
        raw_value=raw_value,
        raw_first_jet=raw_first_jet,
        p_principal_value=sp.SparseMatrix(p_principal_value),
        p_principal_first_jet=sp.SparseMatrix(p_principal_first_jet),
        p_lower_value=sp.SparseMatrix(p_lower_value),
        fifth_principal_value=fifth_principal,
        fifth_first_lower_value=fifth_first_lower,
    )


def embed_bridge_symbol(
    packet: NullFivefoldFirstLower,
    bridge: K152.CurvedMetricBridge,
    substitutions: Mapping[sp.Symbol, sp.Expr],
) -> sp.SparseMatrix:
    """Embed K152's density-dual null symbol without a projection."""
    packet_index = {entry: index for index, entry in enumerate(packet.basis)}
    embedding = sp.MutableSparseMatrix(packet.dimension, len(bridge.basis), {})
    for column, entry in enumerate(bridge.basis):
        if entry not in packet_index:
            raise ValueError(f"bridge basis entry {entry} is outside the closed packet")
        embedding[packet_index[entry], column] = 1
    return sp.SparseMatrix(embedding) * sp.SparseMatrix(
        bridge.symbol(packet.covector4, substitutions)
    )


def restricted_first_lower(
    packet: NullFivefoldFirstLower,
    bridge: K152.CurvedMetricBridge,
    substitutions: Mapping[sp.Symbol, sp.Expr],
) -> sp.SparseMatrix:
    """Order-six coefficient of K P**5 K A on the pulled-back null line.

    The order-seven term is zero by ``P(n)**5=0``.  At order six the only
    surviving candidate is ``K [P**5]_4 K A_2``; the term in which a top
    coefficient differentiates ``A_2`` is multiplied by the zero fifth power.
    """
    bridge_symbol = embed_bridge_symbol(packet, bridge, substitutions)
    return sp.SparseMatrix(
        packet.lowerer
        * packet.fifth_first_lower_value
        * packet.lowerer
        * bridge_symbol
    )


def frozen_first_lower(
    principal_value: sp.SparseMatrix,
) -> sp.SparseMatrix:
    zero = sp.SparseMatrix.zeros(principal_value.rows, principal_value.cols)
    _, lower = top_and_first_lower_power(principal_value, zero, zero, 5)
    return lower
