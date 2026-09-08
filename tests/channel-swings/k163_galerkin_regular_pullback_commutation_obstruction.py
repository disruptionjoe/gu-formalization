#!/usr/bin/env python3
"""K163 exact Galerkin/regular-pullback compatibility certificates.

The finite control uses one coarse momentum cell of width two and its two
unit-width children.  Point-form couplings scale by the square root of cell
width.  Exact arithmetic in Q(sqrt(2)) keeps the physical scaling literal.

The module distinguishes three statements:

* the free quadratic form compresses exactly under dyadic refinement;
* independently rebuilding the cutoff counterterm and nonlinear boundary
  chart need not commute with Galerkin compression; and
* K161's weighted tail bounds fixed-cylinder action columns only after a
  same-family finite anchor is supplied.  That column bound is not a complete
  form-dual residual, coercivity estimate, or spectral floor.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from pathlib import Path
from typing import Any, Iterable, Sequence


HERE = Path(__file__).resolve().parent


def _load(name: str):
    path = HERE / name
    spec = importlib.util.spec_from_file_location(f"k163_{path.stem}", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load sibling {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K151 = _load("k151_native_charge_block_assembler.py")
K161 = _load("k161_weighted_denominator_smoothing_obstruction.py")


class CertificateError(ValueError):
    """Raised when an asserted native bridge omits a required premise."""


@dataclass(frozen=True)
class Q2:
    """Exact ``a+b*sqrt(2)`` arithmetic."""

    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    @classmethod
    def of(cls, value: Any) -> "Q2":
        if isinstance(value, cls):
            return value
        return cls(Fraction(value), Fraction(0))

    def __add__(self, other: Any) -> "Q2":
        rhs = Q2.of(other)
        return Q2(self.a + rhs.a, self.b + rhs.b)

    __radd__ = __add__

    def __neg__(self) -> "Q2":
        return Q2(-self.a, -self.b)

    def __sub__(self, other: Any) -> "Q2":
        return self + (-Q2.of(other))

    def __rsub__(self, other: Any) -> "Q2":
        return Q2.of(other) - self

    def __mul__(self, other: Any) -> "Q2":
        rhs = Q2.of(other)
        return Q2(self.a * rhs.a + 2 * self.b * rhs.b, self.a * rhs.b + self.b * rhs.a)

    __rmul__ = __mul__

    def inverse(self) -> "Q2":
        denominator = self.a * self.a - 2 * self.b * self.b
        if not denominator:
            raise CertificateError("division by zero in Q(sqrt(2))")
        return Q2(self.a / denominator, -self.b / denominator)

    def __truediv__(self, other: Any) -> "Q2":
        return self * Q2.of(other).inverse()

    def __rtruediv__(self, other: Any) -> "Q2":
        return Q2.of(other) / self

    def __bool__(self) -> bool:
        return bool(self.a or self.b)

    def exact(self) -> str:
        if not self.b:
            return qstr(self.a)
        if not self.a:
            return f"{qstr(self.b)}*sqrt(2)"
        sign = "+" if self.b > 0 else "-"
        return f"{qstr(self.a)}{sign}{qstr(abs(self.b))}*sqrt(2)"


Matrix = list[list[Q2]]


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def q(value: Any) -> Fraction:
    return Fraction(value)


def zero(rows: int, columns: int) -> Matrix:
    return [[Q2() for _ in range(columns)] for _ in range(rows)]


def identity(size: int) -> Matrix:
    return [[Q2.of(i == j) for j in range(size)] for i in range(size)]


def transpose(matrix: Matrix) -> Matrix:
    return [list(row) for row in zip(*matrix)]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return [
        [sum((left[i][k] * right[k][j] for k in range(len(right))), Q2()) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def add(*matrices: Matrix) -> Matrix:
    if not matrices:
        raise CertificateError("matrix sum requires an input")
    return [
        [sum((matrix[i][j] for matrix in matrices), Q2()) for j in range(len(matrices[0][0]))]
        for i in range(len(matrices[0]))
    ]


def scale(value: Any, matrix: Matrix) -> Matrix:
    factor = Q2.of(value)
    return [[factor * entry for entry in row] for row in matrix]


def diagonal(values: Iterable[Any]) -> Matrix:
    entries = [Q2.of(value) for value in values]
    return [[entry if i == j else Q2() for j in range(len(entries))] for i, entry in enumerate(entries)]


def inverse(matrix: Matrix) -> Matrix:
    size = len(matrix)
    work = [row[:] + unit[:] for row, unit in zip(matrix, identity(size), strict=True)]
    for column in range(size):
        pivot = next((row for row in range(column, size) if work[row][column]), None)
        if pivot is None:
            raise CertificateError("singular boundary chart")
        work[column], work[pivot] = work[pivot], work[column]
        pivot_value = work[column][column]
        work[column] = [entry / pivot_value for entry in work[column]]
        for row in range(size):
            if row == column or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [left - factor * right for left, right in zip(work[row], work[column], strict=True)]
    return [row[size:] for row in work]


def charge_components(
    energies: Sequence[Any], couplings: Sequence[Any], charge: tuple[int, int]
) -> tuple[list[int], Matrix, Matrix, Matrix]:
    mode_count = len(energies)
    states = K151.basis(mode_count, charge, hard_core=True)
    index = {state: position for position, state in enumerate(states)}
    free = zero(len(states), len(states))
    c = zero(len(states), len(states))
    cstar = zero(len(states), len(states))
    eps = [Q2.of(value) for value in energies]
    gs = [Q2.of(value) for value in couplings]
    for column, state in enumerate(states):
        free[column][column] = sum(
            (
                eps[mode] * K151.occupied(
                    state, K151.bath_orbital(flavor, polarity, mode, mode_count)
                )
                for flavor, polarity, mode in product((0, 1), ("+", "-"), range(mode_count))
            ),
            Q2(),
        )
        for flavor in (0, 1):
            for mode, coupling in enumerate(gs):
                plus = K151.bath_orbital(flavor, "+", mode, mode_count)
                minus = K151.bath_orbital(flavor, "-", mode, mode_count)
                for target_matrix, word in (
                    (c, ((flavor, True), (plus, False))),
                    (c, ((minus, False), (flavor, False))),
                    (cstar, ((plus, True), (flavor, False))),
                    (cstar, ((flavor, True), (minus, True))),
                ):
                    result = K151.apply_word(state, word)
                    if result is None:
                        continue
                    target, sign = result
                    if K151.occupied(target, 0) and K151.occupied(target, 1):
                        continue
                    target_matrix[index[target]][column] += coupling * sign
    if transpose(c) != cstar:
        raise AssertionError("boundary halves are not exact adjoints")
    return states, free, c, cstar


def regular_pullback(
    energies: Sequence[Any], couplings: Sequence[Any], charge: tuple[int, int], shift: Any
) -> dict[str, Any]:
    states, free, c, cstar = charge_components(energies, couplings, charge)
    lam = Q2.of(shift)
    unit = identity(len(states))
    shifted_free = add(free, scale(lam, unit))
    shifted_inverse = diagonal([Q2.of(1) / shifted_free[i][i] for i in range(len(states))])
    g = scale(-1, matmul(shifted_inverse, cstar))
    u_inverse = inverse(add(unit, scale(-1, g)))
    coefficient = sum(
        (Q2.of(coupling) * Q2.of(coupling) / (Q2.of(energy) + lam) for energy, coupling in zip(energies, couplings, strict=True)),
        Q2(),
    )
    endpoint = diagonal(
        [coefficient * (1 if K151.occupied(state, 0) or K151.occupied(state, 1) else 2) for state in states]
    )
    raw = add(free, c, cstar, endpoint)
    regular_core = add(endpoint, scale(-lam, unit), scale(-1, matmul(transpose(g), matmul(shifted_free, g))))
    regular = add(shifted_free, matmul(transpose(u_inverse), matmul(regular_core, u_inverse)))
    direct = matmul(transpose(u_inverse), matmul(raw, u_inverse))
    if regular != direct:
        raise AssertionError("regular pullback identity failed")
    return {
        "states": states,
        "mode_count": len(energies),
        "free": free,
        "raw": raw,
        "regular_core": regular_core,
        "regular": regular,
    }


def bath_particles(state: int, mode_count: int) -> int:
    return sum(K151.occupied(state, orbital) for orbital in range(2, 2 + 4 * mode_count))


def unnormalized_form(packet: dict[str, Any], field: str, cell_sqrt: Q2) -> Matrix:
    mode_count = packet["mode_count"]
    weights = [Q2.of(1) for _ in packet["states"]]
    for i, state in enumerate(packet["states"]):
        for _ in range(bath_particles(state, mode_count)):
            weights[i] = weights[i] * cell_sqrt
    return [
        [weights[i] * packet[field][i][j] * weights[j] for j in range(len(weights))]
        for i in range(len(weights))
    ]


def local_refinement(charge: tuple[int, int]) -> tuple[list[int], list[int], Matrix]:
    coarse = K151.basis(1, charge, hard_core=True)
    fine = K151.basis(2, charge, hard_core=True)
    fine_index = {state: position for position, state in enumerate(fine)}
    injection = zero(len(fine), len(coarse))
    for column, state in enumerate(coarse):
        factors: list[tuple[int, ...]] = []
        for orbital in range(6):
            if not K151.occupied(state, orbital):
                continue
            if orbital < 2:
                factors.append((orbital,))
                continue
            local = orbital - 2
            flavor, polarity_index = divmod(local, 2)
            polarity = "+" if polarity_index == 0 else "-"
            factors.append(tuple(K151.bath_orbital(flavor, polarity, child, 2) for child in (0, 1)))
        for selection in product(*factors):
            inversions = sum(selection[i] > selection[j] for i in range(len(selection)) for j in range(i + 1, len(selection)))
            target = sum(1 << orbital for orbital in selection)
            injection[fine_index[target]][column] += -1 if inversions % 2 else 1
    return coarse, fine, injection


def congruence(matrix: Matrix, injection: Matrix) -> Matrix:
    return matmul(transpose(injection), matmul(matrix, injection))


def first_difference(left: Matrix, right: Matrix) -> dict[str, Any] | None:
    for i in range(len(left)):
        for j in range(len(left)):
            if left[i][j] != right[i][j]:
                return {"row": i, "column": j, "left": left[i][j].exact(), "right": right[i][j].exact(), "difference": (left[i][j] - right[i][j]).exact()}
    return None


def commutation_discriminator(charge: tuple[int, int] = (0, 0), shift: int = 4) -> dict[str, Any]:
    """Test exact compression for a physical one-to-two-cell refinement."""
    root_two = Q2(Fraction(0), Fraction(1))
    coarse = regular_pullback([2], [root_two], charge, shift)
    fine = regular_pullback([1, 3], [1, 1], charge, shift)
    coarse_states, fine_states, injection = local_refinement(charge)
    if coarse_states != coarse["states"] or fine_states != fine["states"]:
        raise AssertionError("refinement and operator bases disagree")
    coarse_free = unnormalized_form(coarse, "free", root_two)
    fine_free = unnormalized_form(fine, "free", Q2.of(1))
    pulled_free = congruence(fine_free, injection)
    if pulled_free != coarse_free:
        raise AssertionError("physical free-form Galerkin compression failed")
    coarse_raw = unnormalized_form(coarse, "raw", root_two)
    fine_raw = unnormalized_form(fine, "raw", Q2.of(1))
    coarse_regular = unnormalized_form(coarse, "regular", root_two)
    fine_regular = unnormalized_form(fine, "regular", Q2.of(1))
    raw_difference = first_difference(congruence(fine_raw, injection), coarse_raw)
    regular_difference = first_difference(congruence(fine_regular, injection), coarse_regular)
    if raw_difference is None or regular_difference is None:
        raise AssertionError("nonlinear cutoff construction unexpectedly commuted")
    return {
        "charge": list(charge),
        "coarse_dimension": len(coarse_states),
        "fine_dimension": len(fine_states),
        "cell_widths": {"coarse": "2", "fine": "1"},
        "fine_energies": ["1", "3"],
        "coarse_free_energy": "2",
        "point_couplings": {"coarse": "sqrt(2)", "fine": ["1", "1"]},
        "free_form_galerkin_congruence": True,
        "raw_cutoff_hamiltonian_congruence": False,
        "regular_pullback_congruence": False,
        "first_raw_defect": raw_difference,
        "first_regular_defect": regular_difference,
        "independent_coarse_rediscretization_is_native_anchor": False,
        "required_repair": "define coarse data by compression of one fixed limiting form or enclose the finite-to-limit defect on the same family",
    }


def fixed_cylinder_column_enclosure(
    *, cutoff: int, spectator_energy: Any, same_family_anchor_ref: str | None,
    refinement_gram_ref: str | None,
) -> dict[str, Any]:
    """Convert K161's right-weighted tail into a fixed-vector column bound."""
    if not same_family_anchor_ref:
        raise CertificateError("fixed-cylinder enclosure requires a same-family finite anchor")
    if not refinement_gram_ref:
        raise CertificateError("fixed-cylinder enclosure requires the exact K162 refinement/Gram proof")
    energy = Fraction(spectator_energy)
    if energy < 0:
        raise CertificateError("spectator energy must be nonnegative")
    tail = K161.complete_weighted_tail(cutoff)
    epsilon = Fraction(tail["complete_weighted_denominator_error_upper"])
    column = epsilon * (1 + energy)
    return {
        "cutoff": cutoff,
        "spectator_energy_upper": qstr(energy),
        "complete_weighted_tail_upper": qstr(epsilon),
        "fixed_cylinder_action_column_error_upper": qstr(column),
        "same_family_anchor_ref": same_family_anchor_ref,
        "refinement_gram_ref": refinement_gram_ref,
        "all_five_K161_components_used": True,
        "complete_form_dual_residual": False,
        "coercivity_or_spectral_floor": False,
    }


def native_k152_readiness(**refs: str | None) -> dict[str, Any]:
    required = (
        "same_family_regular_form_ref",
        "complete_shifted_form_dual_residual_ref",
        "coercivity_ref",
        "next_distinct_spectrum_ref",
        "native_left_floor_ref",
        "signed_charge_intertwiner_ref",
    )
    missing = [name for name in required if not refs.get(name)]
    return {
        "native_K152_interface_complete": not missing,
        "missing_native_references": missing,
        "native_ground_count_emitted": False,
        "native_K152_interval_emitted": False,
    }


def demo() -> dict[str, Any]:
    discriminator = commutation_discriminator()
    try:
        fixed_cylinder_column_enclosure(
            cutoff=4096, spectator_energy=4,
            same_family_anchor_ref=None,
            refinement_gram_ref="K162#exact-refinement-gram",
        )
    except CertificateError as exc:
        native_anchor_failure = str(exc)
    else:
        raise AssertionError("missing native anchor unexpectedly admitted")
    return {
        "schema_version": "1.0",
        "arithmetic": "exact_Q_sqrt2_and_rational_outward_bounds",
        "commutation_discriminator": discriminator,
        "conditional_fixed_cylinder_n4096": fixed_cylinder_column_enclosure(
            cutoff=4096,
            spectator_energy=4,
            same_family_anchor_ref="conditional-same-family-anchor",
            refinement_gram_ref="K162#exact-refinement-gram",
        ),
        "conditional_fixed_cylinder_n65536": fixed_cylinder_column_enclosure(
            cutoff=65536,
            spectator_energy=4,
            same_family_anchor_ref="conditional-same-family-anchor",
            refinement_gram_ref="K162#exact-refinement-gram",
        ),
        "native_anchor_failure": native_anchor_failure,
        "native_K152_readiness": native_k152_readiness(
            same_family_regular_form_ref=None,
            complete_shifted_form_dual_residual_ref=None,
            coercivity_ref=None,
            next_distinct_spectrum_ref=None,
            native_left_floor_ref=None,
            signed_charge_intertwiner_ref="K162#signed-flavor-transport",
        ),
        "route_verdict": "INDEPENDENT_REDISCRETIZATION_NOT_NATIVE__FORM_LEVEL_GALERKIN_ANCHOR_REQUIRED",
        "physical_or_source_selection": False,
        "Born_prediction_or_confirmation_credit": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    if not args.demo:
        parser.error("use --demo")
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
