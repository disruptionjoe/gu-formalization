#!/usr/bin/env python3
"""K454 joint form/Gram perturbation bounds for the finite K152 consumer."""

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


K453 = _load("k454_k453", "k453_k152_finite_physical_consumer_audit.py")
K152 = K453.K152


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def subtract(left, right):
    return [[left[i][j] - right[i][j] for j in range(len(left))] for i in range(len(left))]


def scale_interval(numerator: tuple[Fraction, Fraction], denominator: tuple[Fraction, Fraction]):
    if denominator[0] <= 0:
        raise ValueError("positive denominator interval required")
    values = [x / y for x in numerator for y in denominator]
    return min(values), max(values)


def m_dual_residual_square(form, gram, seed: int) -> Fraction:
    vector = [Fraction(i == seed) for i in range(len(form))]
    norm = K152.dot(vector, K152.matvec(gram, vector))
    rho = K152.rayleigh_quotient(form, gram, vector)
    residual = [
        a - rho * b
        for a, b in zip(K152.matvec(form, vector), K152.matvec(gram, vector), strict=True)
    ]
    representative = K152.solve_linear(gram, residual)
    return K152.dot(residual, representative) / norm


def sector(charge: tuple[int, int], shift: int = 6) -> dict[str, Any]:
    form, gram, target_form, target_gram, seed = K453.pencils(charge)
    form_defect = subtract(target_form, form)
    gram_defect = subtract(target_gram, gram)
    beta, form_plus, form_minus = K453.relative_radius(gram, form_defect)
    alpha, gram_plus, gram_minus = K453.relative_radius(gram, gram_defect)
    if alpha >= 1:
        raise AssertionError("Gram perturbation does not preserve a positive comparison interval")

    first_lo, first_hi = K453.isolate(form, gram, 1)
    second_lo, second_hi = K453.isolate(form, gram, 2)
    target_first_lo, target_first_hi = K453.isolate(target_form, target_gram, 1)
    target_second_lo, target_second_hi = K453.isolate(target_form, target_gram, 2)
    gamma = beta + shift * alpha
    shifted_first_bounds = scale_interval(
        (first_lo + shift - gamma, first_hi + shift + gamma), (1 - alpha, 1 + alpha)
    )
    shifted_second_bounds = scale_interval(
        (second_lo + shift - gamma, second_hi + shift + gamma), (1 - alpha, 1 + alpha)
    )
    transferred_first = (shifted_first_bounds[0] - shift, shifted_first_bounds[1] - shift)
    transferred_second = (shifted_second_bounds[0] - shift, shifted_second_bounds[1] - shift)
    if not (transferred_first[0] <= target_first_lo <= target_first_hi <= transferred_first[1]):
        raise AssertionError("joint perturbation bound missed the first target eigenvalue")
    if not (transferred_second[0] <= target_second_lo <= target_second_hi <= transferred_second[1]):
        raise AssertionError("joint perturbation bound missed the second target eigenvalue")

    vector = [Fraction(i == seed) for i in range(len(form))]
    rho = K152.rayleigh_quotient(form, gram, vector)
    rho_target = K152.rayleigh_quotient(target_form, target_gram, vector)
    rayleigh_bounds = scale_interval((rho - beta, rho + beta), (1 - alpha, 1 + alpha))
    if not rayleigh_bounds[0] <= rho_target <= rayleigh_bounds[1]:
        raise AssertionError("joint perturbation bound missed the target Rayleigh quotient")

    base_mdual_sq = m_dual_residual_square(form, gram, seed)
    base_mdual = K152.sqrt_upper(base_mdual_sq, bits=96)
    rho_delta = max(abs(rho_target - rho), abs(rayleigh_bounds[0] - rho), abs(rayleigh_bounds[1] - rho))
    rho_target_abs = max(abs(rayleigh_bounds[0]), abs(rayleigh_bounds[1]))
    residual_mdual_upper = base_mdual + beta + rho_delta + rho_target_abs * alpha
    base_shifted_floor = first_lo + shift
    transferred_shifted_floor = base_shifted_floor - gamma
    if transferred_shifted_floor <= 0:
        raise AssertionError("finite shifted coercivity transfer failed")
    target_dual_upper = residual_mdual_upper**2 / transferred_shifted_floor / (1 - alpha)
    target_dual_actual = K152.finite_form_dual_residual_sq(
        target_form, target_gram, vector, shift
    )
    if target_dual_actual > target_dual_upper:
        raise AssertionError("residual transfer budget missed the target finite residual")

    return {
        "charge": list(charge),
        "form_relative_radius_beta": qstr(beta),
        "Gram_relative_radius_alpha": qstr(alpha),
        "form_two_sided_certified": form_plus and form_minus,
        "Gram_two_sided_certified": gram_plus and gram_minus,
        "shift": shift,
        "joint_shifted_perturbation_gamma": qstr(gamma),
        "transferred_first_generalized_interval": [qstr(x) for x in transferred_first],
        "actual_target_first_generalized_interval": [qstr(target_first_lo), qstr(target_first_hi)],
        "transferred_next_distinct_interval": [qstr(x) for x in transferred_second],
        "actual_target_next_distinct_interval": [qstr(target_second_lo), qstr(target_second_hi)],
        "transferred_Rayleigh_interval": [qstr(x) for x in rayleigh_bounds],
        "actual_target_Rayleigh": qstr(rho_target),
        "transferred_shifted_coercivity_lower": qstr(transferred_shifted_floor),
        "target_shifted_dual_residual_square_upper": qstr(target_dual_upper),
        "actual_target_shifted_dual_residual_square": qstr(target_dual_actual),
        "all_target_quantities_enclosed": True,
    }


def demo() -> dict[str, Any]:
    sectors = [sector(charge) for charge in ((0, 0), (1, 0), (0, 1))]
    return {
        "schema_version": "1.0",
        "result_id": "K454-K152-CONSUMER-FORM-DEFECT-TRANSFER",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "theorem": {
            "hypotheses": "-beta M <= A'-A <= beta M and -alpha M <= M'-M <= alpha M with alpha<1",
            "shifted_form_defect": "gamma=beta+s*alpha",
            "ordered_shifted_spectrum": "(mu-gamma)/(1+alpha) <= mu' <= (mu+gamma)/(1-alpha)",
            "Rayleigh": "all four endpoint ratios of [rho-beta,rho+beta]/[1-alpha,1+alpha]",
            "residual": "M-dual triangle bound plus transferred shifted coercivity and M'-normalization",
        },
        "sectors": sectors,
        "decision": {
            "joint_form_and_Gram_transfer_required": True,
            "K451_form_only_radius_is_complete_consumer_transfer": False,
            "finite_consumer_quantities_rigorously_transferred": all(
                row["all_target_quantities_enclosed"] for row in sectors
            ),
            "bound_is_cofinal_native_residual_certificate": False,
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
