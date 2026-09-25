#!/usr/bin/env python3
"""K463 exact composition of an M-complement count with coercivity.

The theorem is stated in the physical ``M`` Hilbert geometry.  For an
M-normalized trial vector ``u``, write the fixed limiting form as

    [[rho, ell*], [ell, B]]

on ``span(u) + u^(perp_M)``.  If ``B >= beta > b > rho`` and
``||ell|| <= eta``, Schur congruence gives exactly one spectral value below
``b``.  The same data give the global lower floor

    lambda_- = (rho + beta - sqrt((beta-rho)^2 + 4 eta^2))/2.

Native use is fail-closed: an HVZ member, a finite independent rebuild, or a
finite Ritz count is not a complete same-form M-orthogonal-complement floor.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from fractions import Fraction
from math import isqrt
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent


def _load_k152():
    path = HERE / "k152_form_dual_residual_enclosure_solver.py"
    spec = importlib.util.spec_from_file_location("k463_k152", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load exact inertia dependency at {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K152 = _load_k152()


class CertificateError(ValueError):
    """Raised when the proposed packet omits a theorem premise."""


def q(value: Any) -> Fraction:
    try:
        return value if isinstance(value, Fraction) else Fraction(value)
    except (TypeError, ValueError, ZeroDivisionError) as exc:
        raise CertificateError(f"invalid rational input: {value!r}") from exc


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def sqrt_interval(value: Any, bits: int = 96) -> tuple[Fraction, Fraction]:
    """Return rigorous dyadic lower and upper bounds for a square root."""
    radicand = q(value)
    if radicand < 0:
        raise CertificateError("square-root radicand must be nonnegative")
    if radicand == 0:
        return Fraction(0), Fraction(0)
    scale = 1 << bits
    target = radicand.numerator * scale * scale
    quotient = target // radicand.denominator
    lower_num = isqrt(quotient)
    lower = Fraction(lower_num, scale)
    upper = lower if lower * lower == radicand else Fraction(lower_num + 1, scale)
    if not lower * lower <= radicand <= upper * upper:
        raise AssertionError("internal square-root enclosure failure")
    return lower, upper


def compose_rank_one_and_coercivity(
    *,
    trial_rayleigh: Any,
    count_threshold: Any,
    complete_complement_floor: Any,
    cross_action_norm_upper: Any,
    coercive_shift: Any,
    fixed_limiting_form_ref: str | None,
    physical_metric_ref: str | None,
    trial_line_ref: str | None,
    complete_m_complement_ref: str | None,
    cross_action_column_ref: str | None,
    same_fixed_limiting_form: bool,
    complete_charge_sector_complement: bool,
    bits: int = 96,
) -> dict[str, Any]:
    """Compose exact rank-one count and global lower/coercivity bounds."""
    refs = {
        "fixed_limiting_form_ref": fixed_limiting_form_ref,
        "physical_metric_ref": physical_metric_ref,
        "trial_line_ref": trial_line_ref,
        "complete_m_complement_ref": complete_m_complement_ref,
        "cross_action_column_ref": cross_action_column_ref,
    }
    missing = [name for name, ref in refs.items() if not isinstance(ref, str) or not ref.strip()]
    if missing:
        raise CertificateError(f"missing proof references: {', '.join(missing)}")
    if same_fixed_limiting_form is not True:
        raise CertificateError("finite independent rebuilds cannot substitute for the fixed limiting form")
    if complete_charge_sector_complement is not True:
        raise CertificateError("the M-orthogonal floor must cover the complete charge-sector complement")

    rho = q(trial_rayleigh)
    b = q(count_threshold)
    beta = q(complete_complement_floor)
    eta = q(cross_action_norm_upper)
    shift = q(coercive_shift)
    if eta < 0:
        raise CertificateError("cross/action-column norm upper bound must be nonnegative")
    if not rho < b < beta:
        raise CertificateError("rank-one composition requires rho < b < beta")

    discriminant = (beta - rho) ** 2 + 4 * eta * eta
    root_lower, root_upper = sqrt_interval(discriminant, bits=bits)
    lambda_lower = (rho + beta - root_upper) / 2
    lambda_upper = (rho + beta - root_lower) / 2
    coercivity_lower = lambda_lower + shift
    if coercivity_lower <= 0:
        raise CertificateError("supplied shift does not make the outward global lower floor coercive")

    return {
        "trial_rayleigh": qstr(rho),
        "count_threshold": qstr(b),
        "complete_M_orthogonal_complement_floor": qstr(beta),
        "cross_action_column_norm_upper": qstr(eta),
        "strict_order": "rho < b < beta",
        "spectral_count_strictly_below_b": 1,
        "count_proof": "positive complete Q block plus negative scalar Schur complement",
        "global_lower_floor_formula": "lambda_-=(rho+beta-sqrt((beta-rho)^2+4*eta^2))/2",
        "discriminant": qstr(discriminant),
        "sqrt_discriminant_outward_interval": [qstr(root_lower), qstr(root_upper)],
        "global_lower_floor_outward_interval": [qstr(lambda_lower), qstr(lambda_upper)],
        "coercive_shift": qstr(shift),
        "shifted_coercivity_lower": qstr(coercivity_lower),
        "same_fixed_limiting_form": True,
        "complete_charge_sector_complement": True,
        "proof_references": refs,
    }


def exact_generalized_control() -> dict[str, Any]:
    """Nonidentity-M control whose discriminant is the exact square 25."""
    metric = [
        [Fraction(1), Fraction(1), Fraction(0)],
        [Fraction(1), Fraction(2), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1)],
    ]
    regular_form = [
        [Fraction(-2), Fraction(-1, 2), Fraction(0)],
        [Fraction(-1, 2), Fraction(3), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(3)],
    ]
    pencil = K152.add(regular_form, metric, Fraction(0))
    count_inertia = K152.inertia(pencil)
    certificate = compose_rank_one_and_coercivity(
        trial_rayleigh=-2,
        count_threshold=0,
        complete_complement_floor=2,
        cross_action_norm_upper=Fraction(3, 2),
        coercive_shift=3,
        fixed_limiting_form_ref="control#R",
        physical_metric_ref="control#M",
        trial_line_ref="control#u",
        complete_m_complement_ref="control#Q(R-bM)Q",
        cross_action_column_ref="control#ell",
        same_fixed_limiting_form=True,
        complete_charge_sector_complement=True,
    )
    if count_inertia != (1, 0, 2):
        raise AssertionError("generalized exact control has the wrong inertia")
    return {
        "physical_metric": [[qstr(value) for value in row] for row in metric],
        "regular_form": [[qstr(value) for value in row] for row in regular_form],
        "M_orthonormal_coordinates": ["u=e1", "q1=(-1,1,0)", "q2=e3"],
        "block_form_in_M_orthonormal_coordinates": [["-2", "3/2", "0"], ["3/2", "2", "0"], ["0", "0", "3"]],
        "full_pencil_inertia_at_b": list(count_inertia),
        "exact_generalized_spectrum": ["-5/2", "5/2", "3"],
        "certificate": certificate,
        "control_is_native_K162_packet": False,
    }


def native_readiness(**refs: str | None) -> dict[str, Any]:
    required = (
        "native_trial_rayleigh_ref",
        "native_threshold_ref",
        "complete_M_complement_floor_ref",
        "native_cross_action_norm_ref",
        "center_zero_coercive_shift_ref",
    )
    missing = [name for name in required if not refs.get(name)]
    return {
        "required_native_references": list(required),
        "missing_native_references": missing,
        "native_rank_one_below_b_certificate_emitted": False,
        "native_center_zero_coercivity_emitted": False,
        "K461_relative_readiness_complete": False,
    }


def outward_nonsquare_control() -> dict[str, Any]:
    """Exercise a genuinely outward, non-square discriminant enclosure."""
    certificate = compose_rank_one_and_coercivity(
        trial_rayleigh=-1,
        count_threshold=0,
        complete_complement_floor=2,
        cross_action_norm_upper=1,
        coercive_shift=2,
        fixed_limiting_form_ref="outward-control#R",
        physical_metric_ref="outward-control#M",
        trial_line_ref="outward-control#u",
        complete_m_complement_ref="outward-control#Q",
        cross_action_column_ref="outward-control#ell",
        same_fixed_limiting_form=True,
        complete_charge_sector_complement=True,
        bits=16,
    )
    return {
        "discriminant_is_nonsquare": certificate["discriminant"] == "13",
        "dyadic_bits": 16,
        "certificate": certificate,
        "control_is_native_K162_packet": False,
    }


def demo() -> dict[str, Any]:
    return {
        "schema_version": "1.0",
        "result_id": "K463-K152-COMPLEMENT-COERCIVITY-COMPOSITION",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "theorem": {
            "geometry": "generalized self-adjoint form in the physical M-Hilbert space",
            "decomposition": "span(u) direct-sum u^(perp_M), with ||u||_M=1",
            "premises": ["rho<b<beta", "Q(R-bM)Q >= (beta-b) Q_M", "||Q(R-rho*M)u||_(Q,M-dual) <= eta"],
            "count": "rank 1_(minus_infinity,b)(R,M)=1",
            "global_floor": "lambda_-=(rho+beta-sqrt((beta-rho)^2+4*eta^2))/2",
            "coercivity": "any shift s>-lambda_- makes R+sM positive",
        },
        "exact_positive_control": exact_generalized_control(),
        "outward_nonsquare_control": outward_nonsquare_control(),
        "substitution_boundary": {
            "K169_HVZ_threshold_member_is_complete_Q_floor": False,
            "K447_K453_independent_finite_rebuild_is_same_limiting_form": False,
            "finite_Ritz_rank_is_native_complete_count": False,
            "K456_K457_trial_column_or_residual_determines_Q_floor": False,
        },
        "current_native_readiness": native_readiness(),
        "decision": {
            "composition_theorem_complete": True,
            "native_constants_evaluated": False,
            "next_exact_input": "On one fixed K162/K450 restriction, prove native rho<b<beta on the complete M-orthogonal complement and bound eta; the same packet then emits rank one and a center-zero coercive shift for K461.",
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
