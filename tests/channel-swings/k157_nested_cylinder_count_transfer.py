#!/usr/bin/env python3
"""Exact K157 nested-core controls and fail-closed count transfer.

Finite spectra are regulator anchors only.  A native count is returned only
after a complete common-carrier Riesz-contour resolvent error is supplied.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent


def _load(name: str):
    path = HERE / name
    spec = importlib.util.spec_from_file_location(name.replace(".", "_"), path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load sibling {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K150 = _load("k150_certified_schur_tail_solver.py")
K151 = _load("k151_native_charge_block_assembler.py")
K152 = _load("k152_form_dual_residual_enclosure_solver.py")
K155 = _load("k155_finite_regular_pullback.py")


class CertificateError(ValueError):
    pass


def q(value: Any) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    return Fraction(value)


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def dyadic_upper(value: Fraction, bits: int = 40) -> Fraction:
    scale = 1 << bits
    return Fraction((value.numerator * scale + value.denominator - 1) // value.denominator, scale)


def dyadic_lower(value: Fraction, bits: int = 40) -> Fraction:
    scale = 1 << bits
    return Fraction((value.numerator * scale) // value.denominator, scale)


def embedded_state(state: int, old_modes: int, new_modes: int) -> int:
    """Embed a finite-mode occupation word by leaving new modes empty."""
    if not 0 < old_modes <= new_modes:
        raise CertificateError("mode counts must satisfy 0 < old <= new")
    target = state & 0b11
    for flavor in (0, 1):
        for polarity in ("+", "-"):
            for mode in range(old_modes):
                old = K151.bath_orbital(flavor, polarity, mode, old_modes)
                if K151.occupied(state, old):
                    new = K151.bath_orbital(flavor, polarity, mode, new_modes)
                    target |= 1 << new
    return target


def graph_radius_indices(matrix: list[list[Fraction]], seed: int, radius: int) -> list[int]:
    if radius < 0 or not 0 <= seed < len(matrix):
        raise CertificateError("invalid graph seed or radius")
    seen, frontier = {seed}, {seed}
    for _ in range(radius):
        nxt = {
            j
            for i in frontier
            for j, value in enumerate(matrix[i])
            if j != i and value and j not in seen
        }
        seen.update(nxt)
        frontier = nxt
    return sorted(seen)


def nested_core_census(charge: tuple[int, int], seed_state: int) -> dict[str, Any]:
    dimensions: dict[str, int] = {}
    previous: set[int] = set()
    for modes, energies in ((1, ["5/4"]), (2, ["5/4", "3/2"])):
        packet = K155.regular_pullback(energies, ["1"] * modes, charge, 256)
        seed = packet["states"].index(seed_state)
        for radius in range(5):
            indices = graph_radius_indices(packet["H"], seed, radius)
            key = f"M{modes}R{radius}"
            dimensions[key] = len(indices)
            if radius and not previous.issubset(indices):
                raise AssertionError("graph-radius cores are not nested")
            previous = set(indices)
        previous = set()
    old_states = K151.basis(1, charge)
    new_states = set(K151.basis(2, charge))
    embedded = [embedded_state(state, 1, 2) for state in old_states]
    if len(set(embedded)) != len(old_states) or any(state not in new_states for state in embedded):
        raise AssertionError("mode-support embedding failed")
    return {
        "charge": list(charge),
        "seed": K151.state_label(seed_state, 2),
        "dimensions": dimensions,
        "mode_one_embeds_in_mode_two": True,
        "graph_radius_is_nested": True,
    }


def matrix_vector(matrix: list[list[Fraction]], vector: list[Fraction]) -> list[Fraction]:
    return [sum((entry * value for entry, value in zip(row, vector)), Fraction()) for row in matrix]


def inverse_iteration_anchor(charge: tuple[int, int], seed_state: int, steps: int = 2) -> dict[str, Any]:
    packet = K155.regular_pullback(["5/4", "3/2"], ["1", "1"], charge, 256)
    matrix = packet["H"]
    seed = packet["states"].index(seed_state)
    shifted = K155.add(matrix, K155.scale(Fraction(2), K155.identity(len(matrix))))
    vector = [Fraction(i == seed) for i in range(len(matrix))]
    for _ in range(steps):
        vector = K152.solve_linear(shifted, vector)
    norm_sq = sum((value * value for value in vector), Fraction())
    action = matrix_vector(matrix, vector)
    rayleigh = sum((x * y for x, y in zip(vector, action)), Fraction()) / norm_sq
    residual = [y - rayleigh * x for x, y in zip(vector, action)]
    residual_sq = sum((value * value for value in residual), Fraction()) / norm_sq
    seed_rayleigh = matrix[seed][seed]
    below_seed, equal_seed = K150.spectral_count(matrix, seed_rayleigh)
    below_threshold, equal_threshold = K150.spectral_count(matrix, Fraction(-1))
    return {
        "charge": list(charge),
        "dimension": len(matrix),
        "threshold": "-1",
        "spectral_count_below_threshold": below_threshold,
        "threshold_multiplicity": equal_threshold,
        "seed_rayleigh": qstr(seed_rayleigh),
        "spectral_count_below_seed_rayleigh": below_seed,
        "seed_rayleigh_multiplicity": equal_seed,
        "inverse_iterations": steps,
        "trial_rayleigh_dyadic_interval": [
            qstr(dyadic_lower(rayleigh)), qstr(dyadic_upper(rayleigh))
        ],
        "trial_residual_sq_dyadic_upper": qstr(dyadic_upper(residual_sq)),
        "finite_regulator_only": True,
    }


def cofinal_component_ledger(index: int) -> dict[str, Any]:
    """Outward elementary bounds for delta=1/n and momentum radius n^2.

    The physical cutoff is K=n.  Since 1/pi < 1/3 and omega(p)>=|p|,
    the continuum dressed-vector tail square is <=1/(3n).  Four equal
    edge/polarity coefficients give the displayed Hilbert boundary error.
    The graph-boundary and normal-ordered-core constants remain required.
    """
    if index <= 0:
        raise CertificateError("cofinal index must be positive")
    n = Fraction(index)
    dressed_tail_sq = Fraction(1, 3 * index)
    boundary_error = 4 * K152.sqrt_upper(dressed_tail_sq, bits=40)
    return {
        "delta": qstr(1 / n),
        "mode_radius": index * index,
        "physical_momentum_radius": index,
        "free_graph_relative_error_upper": qstr(1 / n),
        "dressed_point_tail_sq_upper": qstr(dressed_tail_sq),
        "hilbert_boundary_error_upper": qstr(boundary_error),
        "graph_boundary_error_upper": None,
        "normal_ordered_core_graph_error_upper": None,
        "complete_K156_total_tail_emitted": False,
    }


def riesz_rank_transfer(
    *, contour_perimeter: Any, resolvent_error_upper: Any,
    finite_projection_rank: int, common_carrier: bool, complete_contour: bool,
) -> dict[str, Any]:
    """Transfer a finite spectral rank by a complete Riesz contour.

    The exact sufficient inequality L*eta<6 uses 2*pi>6, hence
    ||P-P_N|| <= L*eta/(2*pi) < 1.  Projections within norm one have equal
    rank.  `complete_contour` must include the whole spectral island, not only
    the threshold point or one contour edge.
    """
    perimeter, error = q(contour_perimeter), q(resolvent_error_upper)
    if perimeter <= 0 or error < 0 or finite_projection_rank < 0:
        raise CertificateError("invalid contour certificate data")
    if common_carrier is not True or complete_contour is not True:
        raise CertificateError("rank transfer requires one carrier and the complete contour")
    if perimeter * error >= 6:
        raise CertificateError("Riesz projection norm gap does not close")
    return {
        "finite_projection_rank": finite_projection_rank,
        "native_projection_rank": finite_projection_rank,
        "projection_difference_norm_strictly_below_one": True,
        "sufficient_exact_inequality": "contour_perimeter * resolvent_error_upper < 6 < 2*pi",
    }


def finite_contour_anchor(charge: tuple[int, int]) -> dict[str, Any]:
    packet = K155.regular_pullback(["5/4", "3/2"], ["1", "1"], charge, 256)
    matrix = packet["H"]
    lower = min(
        matrix[i][i] - sum((abs(matrix[i][j]) for j in range(len(matrix)) if j != i), Fraction())
        for i in range(len(matrix))
    )
    count, equal = K150.spectral_count(matrix, Fraction(-1))
    if not lower > -5 or (count, equal) != (1, 0):
        raise AssertionError("finite rectangle does not isolate rank one")
    return {
        "charge": list(charge),
        "rectangle_real_interval": ["-5", "-1"],
        "rectangle_imaginary_half_height": "1/2",
        "contour_perimeter": "10",
        "gershgorin_lower_bound": qstr(lower),
        "finite_projection_rank": 1,
        "complete_native_contour_resolvent_error_upper": None,
        "native_rank_transferred": False,
    }


def demo() -> dict[str, Any]:
    q00 = inverse_iteration_anchor((0, 0), 0)
    q10 = inverse_iteration_anchor((1, 0), 1)
    return {
        "schema_version": "1.0",
        "arithmetic": "exact_rational_with_outward_dyadic_display",
        "cores": [nested_core_census((0, 0), 0), nested_core_census((1, 0), 1)],
        "finite_anchors": [q00, q10],
        "cofinal_component_ledger_n4096": cofinal_component_ledger(4096),
        "finite_contours": [finite_contour_anchor((0, 0)), finite_contour_anchor((1, 0))],
        "abstract_positive_rank_transfer": riesz_rank_transfer(
            contour_perimeter=10, resolvent_error_upper="1/2",
            finite_projection_rank=1, common_carrier=True, complete_contour=True,
        ),
        "native_count_emitted": False,
        "native_energy_interval_emitted": False,
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
