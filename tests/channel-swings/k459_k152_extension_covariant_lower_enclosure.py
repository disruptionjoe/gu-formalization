#!/usr/bin/env python3
"""K459 exact scalar-extension covariance for the K152 lower enclosure."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import isqrt
from typing import Any


class CertificateError(ValueError):
    pass


def q(value: Any) -> Fraction:
    try:
        return value if isinstance(value, Fraction) else Fraction(value)
    except (TypeError, ValueError, ZeroDivisionError) as exc:
        raise CertificateError(f"invalid rational input: {value!r}") from exc


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def sqrt_fraction_exact(value: Fraction) -> Fraction:
    if value < 0:
        raise CertificateError("square root input must be nonnegative")
    numerator, denominator = isqrt(value.numerator), isqrt(value.denominator)
    if numerator * numerator != value.numerator or denominator * denominator != value.denominator:
        raise CertificateError("control discriminant must be an exact rational square")
    return Fraction(numerator, denominator)


def k152_packet(*, rho: Any, shift: Any, exterior_floor: Any, residual_square: Any) -> dict[str, Fraction]:
    rho_q, shift_q = q(rho), q(shift)
    b_q, eps_q = q(exterior_floor), q(residual_square)
    a = rho_q + shift_q
    gap = b_q - rho_q
    if a <= 0 or gap <= 0 or eps_q < 0:
        raise CertificateError("K152 requires rho+s>0, b-rho>0, and nonnegative residual square")
    energy = a * eps_q
    discriminant = energy * energy + 4 * gap * gap * energy
    correction = (energy + sqrt_fraction_exact(discriminant)) / (2 * gap)
    return {
        "rho": rho_q,
        "shift": shift_q,
        "exterior_floor": b_q,
        "residual_square": eps_q,
        "a": a,
        "gap": gap,
        "residual_energy": energy,
        "correction": correction,
        "interval_lower": rho_q - correction,
        "interval_upper": rho_q,
    }


def translate(packet: dict[str, Fraction], extension: Any) -> dict[str, Fraction]:
    e = q(extension)
    return k152_packet(
        rho=packet["rho"] + e,
        shift=packet["shift"] - e,
        exterior_floor=packet["exterior_floor"] + e,
        residual_square=packet["residual_square"],
    )


def demo() -> dict[str, Any]:
    base = k152_packet(rho=-2, shift=6, exterior_floor=1, residual_square=Fraction(3, 16))
    extension = Fraction(7)
    moved = translate(base, extension)
    invariant_keys = ("a", "gap", "residual_square", "residual_energy", "correction")
    return {
        "schema_version": "1.0",
        "result_id": "K459-K152-EXTENSION-COVARIANT-LOWER-ENCLOSURE",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "exact_control": {
            "extension": qstr(extension),
            "base": {key: qstr(value) for key, value in base.items()},
            "translated": {key: qstr(value) for key, value in moved.items()},
        },
        "covariance": {
            "rayleigh_translates_by_extension": moved["rho"] == base["rho"] + extension,
            "exterior_floor_translates_by_extension": moved["exterior_floor"] == base["exterior_floor"] + extension,
            "coercive_shift_translates_oppositely": moved["shift"] == base["shift"] - extension,
            "all_K152_internal_quantities_invariant": all(moved[key] == base[key] for key in invariant_keys),
            "interval_translates_by_extension": (
                moved["interval_lower"] == base["interval_lower"] + extension
                and moved["interval_upper"] == base["interval_upper"] + extension
            ),
        },
        "native_boundary": {
            "selected_scalar_center_required_for_relative_coordinate_family": False,
            "selected_scalar_center_required_for_absolute_physical_placement": True,
            "center_zero_coercivity_or_left_floor_still_required": True,
            "complete_complement_or_count_certificate_still_required": True,
            "native_K162_values_emitted": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    parser.parse_args()
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
