#!/usr/bin/env python3
"""Exact coordinate-jet adapter for the selected conditional K77 Shiab.

The adapter deliberately rebuilds the displayed two-term tensor formula over
the settled real ``Cl(7,7)`` backend.  It does not import a frozen K132 matrix
as a coefficient and does not select Weinstein's unrecovered historical
Shiab.  A coordinate chart is represented by finite Taylor series of the
source-owned conjugation law ``delta Phi_i = [Phi_i, chi]``.  The resulting
matrix is a zero-order coefficient operator compatible with K149's sparse
differential algebra.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import factorial
from typing import Iterable

import sympy as sp

from k149_sparse_differential_jet_api import SparseDifferentialOperator, zero_index


N = 14
ETA = (1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1)
FULL = (1 << N) - 1
CHANNELS = ("comm", "symi", "symi")

Scalar = tuple[sp.Expr, sp.Expr]
Element = dict[int, Scalar]
Form = dict[int, Element]
ZERO: Scalar = (sp.Integer(0), sp.Integer(0))
ONE: Scalar = (sp.Integer(1), sp.Integer(0))
I: Scalar = (sp.Integer(0), sp.Integer(1))


def scalar(value: int | Fraction | sp.Expr) -> Scalar:
    return sp.sympify(value), sp.Integer(0)


def sadd(left: Scalar, right: Scalar) -> Scalar:
    return sp.expand(left[0] + right[0]), sp.expand(left[1] + right[1])


def smul(left: Scalar, right: Scalar) -> Scalar:
    return (
        sp.expand(left[0] * right[0] - left[1] * right[1]),
        sp.expand(left[0] * right[1] + left[1] * right[0]),
    )


def sscale(factor: int | Fraction | sp.Expr | Scalar, value: Scalar) -> Scalar:
    factor_pair = factor if isinstance(factor, tuple) else scalar(factor)
    return smul(factor_pair, value)


def is_zero(value: Scalar) -> bool:
    return sp.simplify(value[0]) == 0 and sp.simplify(value[1]) == 0


def indices(mask: int) -> tuple[int, ...]:
    return tuple(index for index in range(N) if mask & (1 << index))


def eclean(value: Element) -> Element:
    return {mask: coefficient for mask, coefficient in value.items() if not is_zero(coefficient)}


def eadd(*values: Element) -> Element:
    output: Element = {}
    for value in values:
        for mask, coefficient in value.items():
            output[mask] = sadd(output.get(mask, ZERO), coefficient)
    return eclean(output)


def escale(factor: int | Fraction | sp.Expr | Scalar, value: Element) -> Element:
    return eclean({mask: sscale(factor, coefficient) for mask, coefficient in value.items()})


def blade_product(left: int, right: int) -> tuple[int, int]:
    inversions = sum(1 for i in indices(left) for j in indices(right) if i > j)
    sign = -1 if inversions % 2 else 1
    for index in indices(left & right):
        sign *= ETA[index]
    return left ^ right, sign


def emul(left: Element, right: Element) -> Element:
    output: Element = {}
    for left_mask, left_coefficient in left.items():
        for right_mask, right_coefficient in right.items():
            mask, sign = blade_product(left_mask, right_mask)
            term = sscale(sign, smul(left_coefficient, right_coefficient))
            output[mask] = sadd(output.get(mask, ZERO), term)
    return eclean(output)


def blade(item: int | tuple[int, ...], coefficient: Scalar = ONE) -> Element:
    indices_value = (item,) if isinstance(item, int) else item
    return {sum(1 << index for index in indices_value): coefficient}


def comm(left: Element, right: Element) -> Element:
    return eadd(emul(left, right), escale(-1, emul(right, left)))


def fclean(value: Form) -> Form:
    return {mask: eclean(coefficient) for mask, coefficient in value.items() if eclean(coefficient)}


def fadd(*values: Form) -> Form:
    output: Form = {}
    for value in values:
        for mask, coefficient in value.items():
            output[mask] = eadd(output.get(mask, {}), coefficient)
    return fclean(output)


def fscale(factor: int | Fraction | sp.Expr | Scalar, value: Form) -> Form:
    return fclean({mask: escale(factor, coefficient) for mask, coefficient in value.items()})


def wedge_sign(left: int, right: int) -> int:
    if left & right:
        return 0
    inversions = sum(1 for i in indices(left) for j in indices(right) if i > j)
    return -1 if inversions % 2 else 1


def coefficient_product(left: Element, right: Element, channel: str) -> Element:
    left_right = emul(left, right)
    right_left = emul(right, left)
    if channel == "comm":
        return eadd(left_right, escale(-1, right_left))
    if channel == "symi":
        return escale(I, eadd(left_right, right_left))
    raise ValueError(channel)


def wedge(left: Form, right: Form, channel: str = "comm") -> Form:
    output: Form = {}
    for left_mask, left_coefficient in left.items():
        for right_mask, right_coefficient in right.items():
            sign = wedge_sign(left_mask, right_mask)
            if not sign:
                continue
            mask = left_mask | right_mask
            term = escale(sign, coefficient_product(left_coefficient, right_coefficient, channel))
            output[mask] = eadd(output.get(mask, {}), term)
    return fclean(output)


def wedge_raw(left: Form, right: Form) -> Form:
    output: Form = {}
    for left_mask, left_coefficient in left.items():
        for right_mask, right_coefficient in right.items():
            sign = wedge_sign(left_mask, right_mask)
            if not sign:
                continue
            mask = left_mask | right_mask
            term = escale(sign, emul(left_coefficient, right_coefficient))
            output[mask] = eadd(output.get(mask, {}), term)
    return fclean(output)


def hodge(value: Form) -> Form:
    output: Form = {}
    for mask, coefficient in value.items():
        complement = FULL ^ mask
        sign = wedge_sign(mask, complement)
        norm = 1
        for index in indices(mask):
            norm *= ETA[index]
        output[complement] = eadd(output.get(complement, {}), escale(sign * norm, coefficient))
    return fclean(output)


def canonical_phi() -> tuple[Form, Form]:
    phi_one = {1 << index: blade(index) for index in range(N)}
    phi_two = fscale(Fraction(1, 2), wedge_raw(phi_one, phi_one))
    return phi_one, phi_two


PHI_ONE, PHI_TWO = canonical_phi()


def selected_shiab(curvature: Form, phi_one: Form = PHI_ONE, phi_two: Form = PHI_TWO) -> Form:
    """The selected conditional comm/symi/symi two-term Shiab formula."""
    first_channel, inner_channel, outer_channel = CHANNELS
    star_curvature = hodge(curvature)
    first = wedge(phi_one, star_curvature, first_channel)
    middle = hodge(wedge(phi_two, star_curvature, inner_channel))
    second = hodge(wedge(phi_one, middle, outer_channel))
    return fadd(first, fscale(Fraction(-1, 2), second))


def conjugation_series_element(value: Element, generator: Element, coordinate: sp.Symbol, order: int) -> Element:
    output: Element = {}
    derivative = value
    for degree in range(order + 1):
        output = eadd(output, escale(coordinate ** degree / factorial(degree), derivative))
        derivative = comm(derivative, generator)
    return output


def conjugation_series_form(value: Form, generator: Element, coordinate: sp.Symbol, order: int) -> Form:
    return fclean({
        mask: conjugation_series_element(coefficient, generator, coordinate, order)
        for mask, coefficient in value.items()
    })


def moving_phi(
    coordinates: tuple[sp.Symbol, ...],
    generators: tuple[Element, ...],
    jet_order: int,
) -> tuple[Form, Form]:
    if len(coordinates) != len(generators):
        raise ValueError("each coordinate requires one Clifford generator")
    phi_one = PHI_ONE
    for coordinate, generator in zip(coordinates, generators):
        phi_one = conjugation_series_form(phi_one, generator, coordinate, jet_order)
    # Recomputing Phi2 from moving Phi1 preserves the displayed tensor formula
    # instead of differentiating a stored frozen matrix.
    phi_two = fscale(Fraction(1, 2), wedge_raw(phi_one, phi_one))
    return phi_one, phi_two


def flatten(value: Form) -> dict[tuple[int, int], sp.Expr]:
    return {
        (form_mask, clifford_mask): sp.expand(real + sp.I * imaginary)
        for form_mask, element in value.items()
        for clifford_mask, (real, imaginary) in element.items()
        if sp.simplify(real) != 0 or sp.simplify(imaginary) != 0
    }


def scalar_one_form(covector: Iterable[int | Fraction | sp.Expr]) -> Form:
    return {
        1 << index: {0: scalar(value)}
        for index, value in enumerate(covector)
        if sp.sympify(value) != 0
    }


def direction(mu: int, mask: int) -> Form:
    return {1 << mu: {mask: ONE}}


def top_scalar(value: Form) -> Scalar:
    return value.get(FULL, {}).get(0, ZERO)


def pairing(left: Form, right: Form) -> Scalar:
    return top_scalar(wedge_raw(left, right))


def rows_for_image(image: Form) -> list[tuple[int, int, Scalar]]:
    output: list[tuple[int, int, Scalar]] = []
    for form_mask, element in image.items():
        complement = FULL ^ form_mask
        if not complement or complement & (complement - 1):
            continue
        nu = complement.bit_length() - 1
        for clifford_mask, value in element.items():
            if is_zero(value):
                continue
            result = pairing(direction(nu, clifford_mask), image)
            if not is_zero(result):
                output.append((nu, clifford_mask, result))
    return output


@dataclass(frozen=True)
class MovingSelectedShiabAdapter:
    coordinates: tuple[sp.Symbol, ...]
    generators: tuple[Element, ...]
    jet_order: int

    def raw_block(
        self,
        covector: tuple[int | Fraction | sp.Expr, ...],
        labels: tuple[int, ...],
    ) -> tuple[list[tuple[int, int, int]], sp.ImmutableMatrix, sp.ImmutableMatrix]:
        phi_one, phi_two = moving_phi(self.coordinates, self.generators, self.jet_order)
        covector_form = scalar_one_form(covector)
        basis = [(label, mu, label ^ (1 << mu)) for label in labels for mu in range(N)]
        index = {(label, mu): position for position, (label, mu, _) in enumerate(basis)}
        raw = sp.zeros(len(basis))
        for column, (_, mu, mask) in enumerate(basis):
            curvature = wedge_raw(covector_form, direction(mu, mask))
            image = selected_shiab(curvature, phi_one, phi_two)
            for nu, output_mask, value in rows_for_image(image):
                row_label = output_mask ^ (1 << nu)
                if (row_label, nu) not in index:
                    continue
                real, imaginary = value
                raw[index[(row_label, nu)], column] += sp.expand(real + sp.I * imaginary)
        raw = raw.applyfunc(sp.expand)
        euler = ((raw - raw.T) / 2).applyfunc(sp.expand)
        return basis, sp.ImmutableMatrix(raw), sp.ImmutableMatrix(euler)

    def coefficient_matrix(
        self,
        curvature_columns: tuple[Form, ...],
    ) -> tuple[tuple[tuple[int, int], ...], sp.ImmutableMatrix]:
        """Return the moving Shiab matrix on explicit curvature columns.

        Output coordinates are the union of every polynomially live form and
        Clifford mask.  This is the target coefficient before a distortion
        pairing is chosen; keeping that boundary explicit prevents the K132
        frozen self-pairing from being mistaken for the moving coefficient.
        """
        phi_one, phi_two = moving_phi(self.coordinates, self.generators, self.jet_order)
        images = [flatten(selected_shiab(column, phi_one, phi_two)) for column in curvature_columns]
        output_keys = tuple(sorted(set().union(*(image.keys() for image in images))))
        matrix = sp.Matrix([
            [sp.expand(image.get(key, 0)) for image in images]
            for key in output_keys
        ])
        return output_keys, sp.ImmutableMatrix(matrix)

    def coefficient_operator(
        self,
        curvature_columns: tuple[Form, ...],
    ) -> tuple[tuple[tuple[int, int], ...], SparseDifferentialOperator]:
        output_keys, matrix = self.coefficient_matrix(curvature_columns)
        return output_keys, SparseDifferentialOperator.multiplication(self.coordinates, matrix)


def bivector(left: int, right: int, coefficient: int | Fraction = 1) -> Element:
    return blade((left, right), scalar(coefficient))
