#!/usr/bin/env python3
"""K417 native-seed-matched K152 completion identifiability obstruction."""

from __future__ import annotations

import argparse
import importlib.util
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


K170_PATH = Path(__file__).with_name("k170_direct_gram_reference_shape_slice.py")


def load_k170():
    spec = importlib.util.spec_from_file_location("k170_solver_for_k417", K170_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K170")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K170 = load_k170()


def q(value: str | int) -> Fraction:
    return Fraction(value)


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def midpoint(bounds: list[str]) -> Fraction:
    return (q(bounds[0]) + q(bounds[1])) / 2


def demo() -> dict[str, Any]:
    native = K170.demo()
    rows = {tuple(row["charge"]): row for row in native["native_seed_slices"]}
    q00, q10 = rows[(0, 0)], rows[(1, 0)]
    m0, m1 = midpoint(q00["physical_Gram_interval"]), midpoint(q10["physical_Gram_interval"])
    w0 = midpoint(q00["dressed_reference_shape_Rayleigh_interval"])
    w1 = midpoint(q10["dressed_reference_shape_Rayleigh_interval"])
    # K152 is a fixed-charge-sector theorem.  Build the three-dimensional
    # completion wholly inside q00 and retain q10 only as a separate matched
    # spectator constraint; do not mix charge sectors into one pencil.
    gram = [m0, m0, m0]
    shape_rayleigh = [w0, w0, w0]

    gap_rows = []
    for n in (1, 2, 4, 16, 256):
        epsilon = Fraction(1, n)
        total_generalized = [Fraction(0), epsilon, Fraction(1)]
        base_generalized = [total_generalized[i] - shape_rayleigh[i] for i in range(3)]
        gap_rows.append({
            "n": n,
            "gram_diagonal": [qstr(x) for x in gram],
            "shape_generalized_diagonal": [qstr(x) for x in shape_rayleigh],
            "base_R0_generalized_diagonal": [qstr(x) for x in base_generalized],
            "combined_Rref_generalized_diagonal": [qstr(x) for x in total_generalized],
            "ground_rayleigh": "0",
            "complete_residual_square": "0",
            "exterior_gap": qstr(epsilon),
            "K270_budget_at_a3_d1": qstr(Fraction(3, 2 * (3 * n + 1))),
        })

    sensitivity_rows = []
    for n in (1, 2, 4, 16, 64):
        sensitivity_rows.append({
            "map_norm": n,
            "fixed_energy_budget": "3/5",
            "maximum_integral_uncertainty_squared": qstr(Fraction(3, 5 * n * n)),
        })

    return {
        "schema_version": "1.0",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "matched_native_seed_constraints": {
            "q00_Gram_interval": q00["physical_Gram_interval"],
            "q10_Gram_interval": q10["physical_Gram_interval"],
            "chosen_Gram_diagonal": [qstr(x) for x in gram],
            "q10_spectator_Gram": qstr(m1),
            "q00_shape_Rayleigh_interval": q00["dressed_reference_shape_Rayleigh_interval"],
            "q10_shape_Rayleigh_interval": q10["dressed_reference_shape_Rayleigh_interval"],
            "chosen_shape_generalized_diagonal": [qstr(x) for x in shape_rayleigh],
            "q10_spectator_shape_Rayleigh": qstr(w1),
            "shape_order_bounds": ["-2", "1"],
            "chosen_shape_residual_square": "0",
            "q00_reported_residual_square_upper": q00["matched_M_inverse_residual_sq_upper"],
            "q10_reported_residual_square_upper": q10["matched_M_inverse_residual_sq_upper"],
        },
        "gap_completion_family": gap_rows,
        "sensitivity_completion_family": sensitivity_rows,
        "K278_positive_scalar": {
            "strictly_positive": True,
            "lower_witness": "4.188726504117970533861167897643613085462580367515119245539396497540573174E-81",
            "serialized_coupling_to_base_R0_gap_or_map_norm": False,
        },
        "decision": {
            "K170_seed_constraints_identify_positive_uniform_gap": False,
            "K170_plus_K278_identify_positive_uniform_gap": False,
            "K170_plus_K278_identify_finite_uniform_map_norm": False,
            "K170_plus_K278_identify_positive_integral_tolerance": False,
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
