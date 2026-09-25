#!/usr/bin/env python3
"""K453 exact finite K152 consumer audit on the K447/K451 controls.

The independently rebuilt one-cell and compressed two-cell pencils are finite
diagnostics.  They are not restrictions of the fixed limiting K139 form.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent


def _load(name: str, filename: str):
    path = HERE / filename
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K447 = _load("k453_k447", "k447_k152_charge_sector_galerkin_defect_census.py")
K451 = _load("k453_k451", "k451_k152_physical_gram_independent_defect.py")
K152 = _load("k453_k152", "k152_form_dual_residual_enclosure_solver.py")
K163 = K447.K163


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def rational(matrix):
    if any(entry.b for row in matrix for entry in row):
        raise AssertionError("physical consumer audit unexpectedly left Q")
    return [[entry.a for entry in row] for row in matrix]


def physical_gram(
    energies: list[Any], couplings: list[Any], charge: tuple[int, int], shift: int, cell_sqrt
):
    states, free, _, cstar = K163.charge_components(energies, couplings, charge)
    unit = K163.identity(len(states))
    shifted = K163.add(free, K163.scale(shift, unit))
    shifted_inverse = K163.diagonal([K163.Q2.of(1) / shifted[i][i] for i in range(len(unit))])
    g = K163.scale(-1, K163.matmul(shifted_inverse, cstar))
    s = K163.inverse(K163.add(unit, K163.scale(-1, g)))
    weights = []
    for state in states:
        weight = K163.Q2.of(1)
        for _ in range(K163.bath_particles(state, len(energies))):
            weight *= cell_sqrt
        weights.append(weight)
    basis = K163.diagonal(weights)
    return K163.matmul(basis, K163.matmul(K163.transpose(s), K163.matmul(s, basis)))


def seed_index(states: list[int], mode_count: int) -> int:
    candidates = [i for i, state in enumerate(states) if K163.bath_particles(state, mode_count) == 0]
    if len(candidates) != 1:
        raise AssertionError("expected one zero-bath representative seed per charge sector")
    return candidates[0]


def isolate(form, gram, index: int) -> tuple[Fraction, Fraction]:
    lower, upper = Fraction(-16), Fraction(16)
    while True:
        below_lower, equal_lower = K152.generalized_spectral_count(form, gram, lower)
        below_upper, equal_upper = K152.generalized_spectral_count(form, gram, upper)
        if not equal_lower and not equal_upper and below_lower < index <= below_upper:
            return K152.isolate_generalized_eigenvalue(form, gram, index, lower, upper, 72)
        lower *= 2
        upper *= 2
        if abs(lower) > 1 << 20:
            raise AssertionError("failed to bracket finite generalized spectrum")


def relative_radius(reference, difference) -> tuple[Fraction, bool, bool]:
    ref_q2 = [[K163.Q2.of(value) for value in row] for row in reference]
    diff_q2 = [[K163.Q2.of(value) for value in row] for row in difference]
    relative = rational(K163.matmul(K163.inverse(ref_q2), diff_q2))
    beta = max(sum(abs(entry) for entry in row) for row in relative)
    plus = [[beta * reference[i][j] + difference[i][j] for j in range(len(reference))] for i in range(len(reference))]
    minus = [[beta * reference[i][j] - difference[i][j] for j in range(len(reference))] for i in range(len(reference))]
    return beta, K451.ldl_positive(plus), K451.ldl_positive(minus)


def diagnostic(form, gram, seed: int, shift: int = 6) -> dict[str, Any]:
    vector = [Fraction(i == seed) for i in range(len(form))]
    rayleigh = K152.rayleigh_quotient(form, gram, vector)
    residual = K152.finite_form_dual_residual_sq(form, gram, vector, shift)
    first_lo, first_hi = isolate(form, gram, 1)
    second_lo, second_hi = isolate(form, gram, 2)
    shifted_floor = first_lo + shift
    interval = None
    try:
        lower, upper, correction, projection = K152.dual_temple_ground_enclosure(
            rayleigh, residual, shift, shifted_floor, second_lo
        )
        interval = {
            "ground_interval": [qstr(lower), qstr(upper)],
            "correction_upper": qstr(correction),
            "projection_error_upper": qstr(projection),
        }
    except K152.CertificateError as exc:
        interval = {"certified": False, "reason": str(exc)}
    return {
        "dimension": len(form),
        "seed_index": seed,
        "shift": shift,
        "generalized_rayleigh": qstr(rayleigh),
        "shifted_form_dual_residual_square": qstr(residual),
        "first_generalized_eigenvalue_interval": [qstr(first_lo), qstr(first_hi)],
        "next_distinct_generalized_eigenvalue_interval": [qstr(second_lo), qstr(second_hi)],
        "shifted_coercivity_floor_lower": qstr(shifted_floor),
        "finite_dual_temple_result": interval,
    }


def pencils(charge: tuple[int, int]):
    root_two = K163.Q2(Fraction(0), Fraction(1))
    coarse = K163.regular_pullback([2], [root_two], charge, 4)
    fine = K163.regular_pullback([1, 3], [1, 1], charge, 4)
    coarse_states, fine_states, injection = K163.local_refinement(charge)
    if coarse_states != coarse["states"] or fine_states != fine["states"]:
        raise AssertionError("consumer audit and refinement bases disagree")
    coarse_form = rational(K163.unnormalized_form(coarse, "regular", root_two))
    fine_form = K163.unnormalized_form(fine, "regular", K163.Q2.of(1))
    compressed_form = rational(K163.congruence(fine_form, injection))
    coarse_gram = rational(physical_gram([2], [root_two], charge, 4, root_two))
    fine_gram = physical_gram([1, 3], [1, 1], charge, 4, K163.Q2.of(1))
    compressed_gram = rational(K163.congruence(fine_gram, injection))
    seed = seed_index(coarse_states, 1)
    return coarse_form, coarse_gram, compressed_form, compressed_gram, seed


def sector(charge: tuple[int, int]) -> dict[str, Any]:
    coarse_form, coarse_gram, compressed_form, compressed_gram, seed = pencils(charge)
    gram_defect = [
        [compressed_gram[i][j] - coarse_gram[i][j] for j in range(len(coarse_gram))]
        for i in range(len(coarse_gram))
    ]
    gram_radius, gram_plus, gram_minus = relative_radius(coarse_gram, gram_defect)
    rebuilt = diagnostic(coarse_form, coarse_gram, seed)
    compressed = diagnostic(compressed_form, compressed_gram, seed)
    return {
        "charge": list(charge),
        "physical_Gram_exactly_shared": compressed_gram == coarse_gram,
        "physical_Gram_defect_nonzero": any(entry for row in gram_defect for entry in row),
        "physical_Gram_relative_defect_radius": qstr(gram_radius),
        "physical_Gram_plus_certificate_positive_definite": gram_plus,
        "physical_Gram_minus_certificate_positive_definite": gram_minus,
        "one_cell_independent_rebuild": rebuilt,
        "compressed_two_cell_rebuild": compressed,
        "rayleigh_difference": qstr(
            abs(Fraction(rebuilt["generalized_rayleigh"]) - Fraction(compressed["generalized_rayleigh"]))
        ),
        "dual_residual_square_difference": qstr(
            abs(
                Fraction(rebuilt["shifted_form_dual_residual_square"])
                - Fraction(compressed["shifted_form_dual_residual_square"])
            )
        ),
    }


def demo() -> dict[str, Any]:
    sectors = [sector(charge) for charge in ((0, 0), (1, 0), (0, 1))]
    return {
        "schema_version": "1.0",
        "result_id": "K453-K152-FINITE-PHYSICAL-CONSUMER-AUDIT",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "sectors": sectors,
        "decision": {
            "complete_finite_consumer_quantities_evaluated": True,
            "physical_Gram_compresses_exactly_for_independent_rebuilds": all(
                row["physical_Gram_exactly_shared"] for row in sectors
            ),
            "physical_Gram_independent_rebuild_defect_certified": all(
                row["physical_Gram_defect_nonzero"]
                and row["physical_Gram_plus_certificate_positive_definite"]
                and row["physical_Gram_minus_certificate_positive_definite"]
                for row in sectors
            ),
            "independent_rebuild_changes_consumer_quantities": any(
                row["rayleigh_difference"] != "0" or row["dual_residual_square_difference"] != "0"
                for row in sectors
            ),
            "finite_controls_are_fixed_limiting_K139_form_restrictions": False,
            "finite_dual_residual_is_complete_native_K162_residual": False,
            "native_K152_interval_emitted": False,
        },
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
