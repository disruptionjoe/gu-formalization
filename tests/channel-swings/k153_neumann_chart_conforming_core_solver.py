#!/usr/bin/env python3
"""Exact bounds for K139 Neumann-chart conforming trial cores.

The compiler proves chart, Gram, pullback-form, coercivity, and residual-norm
interfaces.  It does not assemble the regular charge-sector operator or prove
the next-distinct-spectrum floor required by K152.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


class CertificateError(ValueError):
    """Raised when exact inputs do not certify the requested conclusion."""


def q(value: Any) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    if not isinstance(value, str):
        raise CertificateError("exact inputs must be integers or rational strings")
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise CertificateError(f"invalid rational value: {value!r}") from exc


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def signed_point_h2_upper(auxiliary_shift: Any) -> Fraction:
    """Upper-bound sum_k (sqrt(1+k^2)+lambda)^-2 on Z.

    The k=0 term is exact.  For k>=1 use sqrt(1+k^2)>=k and
    sum_{k>=1}(k+lambda)^-2 <= (1+lambda)^-2+(1+lambda)^-1.
    """
    shift = q(auxiliary_shift)
    if shift <= 0:
        raise CertificateError("auxiliary chart shift must be positive")
    scale = shift + 1
    return 3 / (scale * scale) + 2 / scale


def certify_contraction(
    auxiliary_shift: Any,
    coefficient_l1: Any,
    contraction_upper: Any,
) -> dict[str, Fraction]:
    shift = q(auxiliary_shift)
    coefficient = q(coefficient_l1)
    contraction = q(contraction_upper)
    if coefficient < 0:
        raise CertificateError("coupling coefficient l1 bound must be nonnegative")
    if not 0 <= contraction < 1:
        raise CertificateError("Neumann contraction upper must lie in [0,1)")
    h2 = signed_point_h2_upper(shift)
    norm_sq = coefficient * coefficient * h2
    if contraction * contraction < norm_sq:
        raise CertificateError("claimed contraction does not dominate the analytic norm-square bound")
    return {
        "auxiliary_shift": shift,
        "h2_upper": h2,
        "boundary_map_norm_sq_upper": norm_sq,
        "contraction_upper": contraction,
    }


def neumann_tail(contraction_upper: Any, word_order: int, vector_norm_upper: Any = 1) -> Fraction:
    contraction = q(contraction_upper)
    norm = q(vector_norm_upper)
    if not 0 <= contraction < 1:
        raise CertificateError("Neumann contraction upper must lie in [0,1)")
    if not isinstance(word_order, int) or word_order < 0:
        raise CertificateError("word order must be a nonnegative integer")
    if norm < 0:
        raise CertificateError("vector norm bound must be nonnegative")
    return norm * contraction ** (word_order + 1) / (1 - contraction)


def cutoff_inverse_tail(
    contraction_upper: Any,
    boundary_map_error_upper: Any,
    vector_norm_upper: Any = 1,
) -> Fraction:
    """Resolvent-identity bound for U^-1-U_N^-1 on one vector."""
    contraction = q(contraction_upper)
    error = q(boundary_map_error_upper)
    norm = q(vector_norm_upper)
    if not 0 <= contraction < 1:
        raise CertificateError("Neumann contraction upper must lie in [0,1)")
    if error < 0 or norm < 0:
        raise CertificateError("operator and vector error bounds must be nonnegative")
    return norm * error / ((1 - contraction) * (1 - contraction))


def finite_cutoff_word_tail(
    contraction_upper: Any,
    boundary_map_error_upper: Any,
    word_order: int,
    vector_norm_upper: Any = 1,
) -> Fraction:
    return cutoff_inverse_tail(contraction_upper, boundary_map_error_upper, vector_norm_upper) + neumann_tail(
        contraction_upper, word_order, vector_norm_upper
    )


def gram_spectral_bounds(contraction_upper: Any) -> tuple[Fraction, Fraction]:
    """Bounds for the Gram spectrum of U^-1 on an orthonormal core."""
    contraction = q(contraction_upper)
    if not 0 <= contraction < 1:
        raise CertificateError("Neumann contraction upper must lie in [0,1)")
    return 1 / ((1 + contraction) ** 2), 1 / ((1 - contraction) ** 2)


def coercive_floor(regular_lower_bound: Any, physical_shift: Any, contraction_upper: Any) -> Fraction:
    """Lower bound for U* R U+s from R>=r0 and ||G||<=q."""
    regular = q(regular_lower_bound)
    shift = q(physical_shift)
    contraction = q(contraction_upper)
    if not 0 <= contraction < 1:
        raise CertificateError("Neumann contraction upper must lie in [0,1)")
    chart_factor = (1 - contraction) ** 2 if regular >= 0 else (1 + contraction) ** 2
    return shift + regular * chart_factor


def hilbert_to_form_dual_residual_sq(hilbert_residual_norm_upper: Any, coercivity_floor: Any) -> Fraction:
    residual = q(hilbert_residual_norm_upper)
    coercivity = q(coercivity_floor)
    if residual < 0:
        raise CertificateError("Hilbert residual norm bound must be nonnegative")
    if coercivity <= 0:
        raise CertificateError("shifted form coercivity floor must be positive")
    return residual * residual / coercivity


def coarse_chart_residual_norm(
    regular_action_norm_upper: Any,
    rayleigh_abs_upper: Any,
    contraction_upper: Any,
    core_vector_norm_upper: Any = 1,
) -> Fraction:
    """Bound ||U*R phi-rho U^-1 phi|| without a raw point field."""
    action = q(regular_action_norm_upper)
    rayleigh = q(rayleigh_abs_upper)
    contraction = q(contraction_upper)
    norm = q(core_vector_norm_upper)
    if action < 0 or rayleigh < 0 or norm < 0:
        raise CertificateError("norm and absolute-value bounds must be nonnegative")
    if not 0 <= contraction < 1:
        raise CertificateError("Neumann contraction upper must lie in [0,1)")
    return (1 + contraction) * action + rayleigh * norm / (1 - contraction)


def validate_native_chart(native: Any) -> bool:
    if not isinstance(native, dict):
        raise CertificateError("native chart contract must be an object")
    if native.get("claim_native_chart") is not True:
        return False
    if native.get("charge_sector") not in ([0, 0], [1, 0], [0, 1]):
        raise CertificateError("native charge must be a selected representative or flavor partner")
    required = (
        "k139_domain_ref",
        "charge_core_ref",
        "contraction_proof_ref",
        "regular_pullback_ref",
    )
    if any(not isinstance(native.get(key), str) or not native[key].strip() for key in required):
        raise CertificateError("native chart claim is missing a proof reference")
    if native["charge_sector"] == [0, 1] and (
        not isinstance(native.get("signed_flavor_transport_ref"), str)
        or not native["signed_flavor_transport_ref"].strip()
    ):
        raise CertificateError("q=(0,1) chart transport requires the signed flavor proof")
    return True


def k152_ready(native: Any) -> bool:
    if not validate_native_chart(native):
        return False
    required = (
        "regular_form_action_data_ref",
        "coercive_shift_proof_ref",
        "dual_residual_proof_ref",
        "next_distinct_spectrum_floor_ref",
    )
    return all(isinstance(native.get(key), str) and native[key].strip() for key in required)


def solve(payload: dict[str, Any]) -> dict[str, Any]:
    certificate = certify_contraction(
        payload["auxiliary_shift"],
        payload["coefficient_l1"],
        payload["contraction_upper"],
    )
    contraction = certificate["contraction_upper"]
    word_order = int(payload.get("word_order", 8))
    boundary_error = q(payload.get("boundary_map_error_upper", 0))
    gram_lower, gram_upper = gram_spectral_bounds(contraction)
    result = {
        "schema_version": "1.0",
        "arithmetic": "exact_rational_outer_bounds",
        "auxiliary_chart_shift": qstr(certificate["auxiliary_shift"]),
        "h2_upper": qstr(certificate["h2_upper"]),
        "boundary_map_norm_sq_upper": qstr(certificate["boundary_map_norm_sq_upper"]),
        "contraction_upper": qstr(contraction),
        "inverse_norm_upper": qstr(1 / (1 - contraction)),
        "orthonormal_core_gram_spectrum": [qstr(gram_lower), qstr(gram_upper)],
        "neumann_word_tail_upper": qstr(neumann_tail(contraction, word_order)),
        "cutoff_plus_word_tail_upper": qstr(finite_cutoff_word_tail(contraction, boundary_error, word_order)),
        "native_trial_vectors": "psi_i=U_lambda^-1 phi_i",
        "form_matrix_rule": "a(psi_i,psi_j)=r(phi_i,phi_j)",
        "raw_point_field_norm_used": False,
    }
    if "regular_lower_bound" in payload and "physical_shift" in payload:
        floor = coercive_floor(payload["regular_lower_bound"], payload["physical_shift"], contraction)
        result["shifted_form_coercivity_floor"] = qstr(floor)
        if "hilbert_residual_norm_upper" in payload:
            result["form_dual_residual_sq_upper"] = qstr(
                hilbert_to_form_dual_residual_sq(payload["hilbert_residual_norm_upper"], floor)
            )
    native = payload.get("native_input", {})
    result["native_chart_contract_satisfied"] = validate_native_chart(native)
    result["k152_native_contract_complete"] = k152_ready(native) if result["native_chart_contract_satisfied"] else False
    result["native_energy_interval_emitted"] = False
    return result


DEMO = {
    "auxiliary_shift": "256",
    "coefficient_l1": "4",
    "contraction_upper": "3/8",
    "word_order": 8,
    "boundary_map_error_upper": "1/1000",
    "regular_lower_bound": "-1",
    "physical_shift": "2",
    "hilbert_residual_norm_upper": "1/8",
    "native_input": {
        "claim_native_chart": True,
        "charge_sector": [0, 0],
        "k139_domain_ref": "k139#equation-9",
        "charge_core_ref": "k153#vacuum-core",
        "contraction_proof_ref": "k153#equations-3-5",
        "regular_pullback_ref": "k153#equation-9",
    },
}


def main() -> int:
    parser = argparse.ArgumentParser()
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--input", type=Path)
    source.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    try:
        payload = DEMO if args.demo or args.input is None else json.loads(args.input.read_text())
        print(json.dumps(solve(payload), indent=2, sort_keys=True))
    except (CertificateError, KeyError, TypeError, ValueError, json.JSONDecodeError, OSError) as exc:
        print(json.dumps({"certified": False, "error": str(exc)}, sort_keys=True))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
