#!/usr/bin/env python3
"""K462 existential center-zero coercivity extraction for the K162 carrier.

The theorem composes the already-proved K139/K141 common lower shift with the
fixed K168 reference extension at scalar coordinate zero, then records K153's
exact chart constants on the K156/K162 continuum carrier.  It deliberately
does not manufacture a numerical native lower-bound witness.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from typing import Any


class CertificateError(ValueError):
    """Raised when an exact coercivity control omits a required premise."""


def q(value: Any) -> Fraction:
    try:
        return value if isinstance(value, Fraction) else Fraction(value)
    except (TypeError, ValueError, ZeroDivisionError) as exc:
        raise CertificateError(f"invalid rational input: {value!r}") from exc


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def chart_transport(
    *, regular_lower_bound: Any, physical_shift: Any, contraction_upper: Any = Fraction(3, 8)
) -> dict[str, str]:
    """Apply K153's sign-sensitive regular-to-physical coercivity formula."""
    r0 = q(regular_lower_bound)
    shift = q(physical_shift)
    contraction = q(contraction_upper)
    if not 0 <= contraction < 1:
        raise CertificateError("chart contraction must lie in [0,1)")
    lower_factor = (1 - contraction) ** 2
    upper_factor = (1 + contraction) ** 2
    factor = lower_factor if r0 >= 0 else upper_factor
    floor = shift + r0 * factor
    if floor <= 0:
        raise CertificateError("supplied regular bound and shift do not prove positive coercivity")
    return {
        "regular_lower_bound": qstr(r0),
        "physical_shift": qstr(shift),
        "contraction_upper": qstr(contraction),
        "nonnegative_factor": qstr(lower_factor),
        "negative_factor": qstr(upper_factor),
        "factor_used": qstr(factor),
        "physical_coercivity_floor": qstr(floor),
    }


def compose_existential(
    *,
    k139_uniform_semibound: bool,
    k141_fixed_w_continuum_limit: bool,
    k168_reference_at_center_zero: bool,
    k153_exact_chart: bool,
    k156_k162_continuum_carrier: bool,
    complete_charge_sector_reducing: bool,
    quantitative_regular_lower_bound: Any | None = None,
    quantitative_physical_shift: Any | None = None,
) -> dict[str, Any]:
    """Compile the theorem chain and fail closed on a missing numeric witness."""
    required = {
        "K139_uniform_semibound": k139_uniform_semibound,
        "K141_fixed_W_continuum_limit": k141_fixed_w_continuum_limit,
        "K168_reference_at_scalar_center_zero": k168_reference_at_center_zero,
        "K153_exact_chart": k153_exact_chart,
        "K156_K162_continuum_carrier": k156_k162_continuum_carrier,
        "complete_charge_sector_reducing": complete_charge_sector_reducing,
    }
    missing = [name for name, present in required.items() if not present]
    existential = not missing
    has_lower = quantitative_regular_lower_bound is not None
    has_shift = quantitative_physical_shift is not None
    if has_lower != has_shift:
        raise CertificateError("quantitative release requires both a lower bound and a shift")
    quantitative = has_lower and has_shift
    if quantitative and not existential:
        raise CertificateError("a quantitative witness cannot repair a broken theorem chain")
    quantitative_control = None
    if quantitative:
        quantitative_control = chart_transport(
            regular_lower_bound=quantitative_regular_lower_bound,
            physical_shift=quantitative_physical_shift,
        )
    return {
        "required_references": required,
        "missing_references": missing,
        "fixed_extension": "K168 W_ref=diag(-2,1,1)",
        "scalar_extension_coordinate": "0",
        "existential_center_zero_semiboundedness": existential,
        "existential_shift_choice": "if H_ref,0>=-L0 then s0=L0+1 and c0=1",
        "complete_K162_charge_sector_covered": existential,
        "quantitative_regular_lower_bound_serialized": quantitative,
        "quantitative_center_zero_coercivity_released": quantitative,
        "quantitative_control": quantitative_control,
        "K457_numerical_evaluation_released": False,
        "K461_quantitative_readiness_released": False,
    }


def demo() -> dict[str, Any]:
    native = compose_existential(
        k139_uniform_semibound=True,
        k141_fixed_w_continuum_limit=True,
        k168_reference_at_center_zero=True,
        k153_exact_chart=True,
        k156_k162_continuum_carrier=True,
        complete_charge_sector_reducing=True,
        quantitative_regular_lower_bound=None,
        quantitative_physical_shift=None,
    )
    control = chart_transport(
        regular_lower_bound=-4,
        physical_shift=Fraction(137, 16),
        contraction_upper=Fraction(3, 8),
    )
    return {
        "schema_version": "1.0",
        "result_id": "K462-K152-CENTER-ZERO-COERCIVITY-EXTRACTION",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "continuum_composition": native,
        "exact_chart_constants": {
            "q_upper": "3/8",
            "one_minus_q_squared": "25/64",
            "one_plus_q_squared": "121/64",
            "gram_interval": ["64/121", "64/25"],
            "negative_r0_formula": "c0=s0+(121/64)r0",
            "nonnegative_r0_formula": "c0=s0+(25/64)r0",
        },
        "exact_positive_control": control,
        "coordinate_covariance": {
            "center_zero_is_physical_selection": False,
            "translated_shift": "s_E=s0-E",
            "relative_coercivity_family_transports": True,
            "absolute_physical_placement_released": False,
        },
        "decision": {
            "existential_center_zero_coercivity_proved": True,
            "named_native_lower_bound_witness_present": False,
            "quantitative_center_zero_coercivity_ref_released": False,
            "rank_one_below_b_certificate_present": False,
            "native_K152_interval_emitted": False,
            "next_exact_input": "Extract one exact or outward cancellation-safe lower-bound witness for the combined fixed K139/K168 center-zero form, and independently prove rank one below a named b on the complete K162 sector.",
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
