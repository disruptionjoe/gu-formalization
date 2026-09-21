#!/usr/bin/env python3
"""Exact K270 sharp K152 spectral and consumer-budget certificate.

The scalar theorem is conditional on K152's native operator hypotheses.  This
module proves and checks the exact rational algebra; it does not construct the
missing native form, residual, exterior gap, or downstream decision margin.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k270-k152-sharp-spectral-budget-certificate.json"


class CertificateError(ValueError):
    """Raised when exact inputs do not satisfy the K270 contract."""


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


def sharp_ground_error_upper(a: Any, g: Any, residual_sq: Any) -> Fraction:
    """Return e*a*(a+g)/(a*g+e*(a+g))."""
    aa, gg, ee = q(a), q(g), q(residual_sq)
    if aa <= 0 or gg <= 0 or ee < 0:
        raise CertificateError("sharp bound requires a>0, g>0, and e>=0")
    return ee * aa * (aa + gg) / (aa * gg + ee * (aa + gg))


def sharp_residual_budget(a: Any, g: Any, target_error: Any) -> Fraction:
    """Sufficient e budget for sharp ground error at most d."""
    aa, gg, dd = q(a), q(g), q(target_error)
    if aa <= 0 or gg <= 0 or not 0 < dd < aa:
        raise CertificateError("sharp residual budget requires a,g>0 and 0<d<a")
    return dd * aa * gg / ((aa + gg) * (aa - dd))


def legacy_residual_budget(a: Any, g: Any, target_error: Any) -> Fraction:
    """K152's existing sufficient e budget from its square-root correction."""
    aa, gg, dd = q(a), q(g), q(target_error)
    if aa <= 0 or gg <= 0 or dd <= 0:
        raise CertificateError("legacy residual budget requires a,g,d>0")
    return gg * dd * dd / (aa * (gg + dd))


def projection_residual_budget(a: Any, g: Any, projection_tolerance: Any) -> Fraction:
    """Sufficient e budget for K152's projection error eta_P."""
    aa, gg, eta = q(a), q(g), q(projection_tolerance)
    if aa <= 0 or gg <= 0 or not 0 < eta < 1:
        raise CertificateError("projection budget requires a,g>0 and 0<eta<1")
    return eta * eta * gg * gg / (aa + gg)


def propagated_residual_sq_upper(
    nominal_residual_norm: Any,
    integral_map_norm: Any,
    certified_integral_radius: Any,
    omitted_integral_tail: Any,
    other_residual_error: Any,
) -> Fraction:
    """Triangle-bound a complete residual while preserving error provenance."""
    r0 = q(nominal_residual_norm)
    kappa = q(integral_map_norm)
    radius = q(certified_integral_radius)
    tail = q(omitted_integral_tail)
    other = q(other_residual_error)
    if min(r0, kappa, radius, tail, other) < 0:
        raise CertificateError("consumer budget components must be nonnegative")
    return (r0 + kappa * (radius + tail) + other) ** 2


def discrete_spectral_certificate(
    points: list[Any],
    weights: list[Any],
    ground: Any,
    exterior: Any,
    shift: Any,
) -> dict[str, Fraction | bool]:
    """Check the proof identity on a finite exact spectral measure.

    Accepted support is the ground point together with [b,infinity).  The
    returned identity is a finite-measure replay of the analytic proof.
    """
    xs = [q(value) for value in points]
    ws = [q(value) for value in weights]
    lam, b, s = q(ground), q(exterior), q(shift)
    if not xs or len(xs) != len(ws) or any(weight < 0 for weight in ws):
        raise CertificateError("spectral points require matching nonnegative weights")
    if sum(ws, Fraction()) != 1:
        raise CertificateError("spectral weights must sum to one")
    if any(x != lam and x < b for x in xs):
        raise CertificateError("support must lie at lambda0 or in [b,infinity)")
    if any(x + s <= 0 for x in xs):
        raise CertificateError("the shifted operator must be positive on support")
    rho = sum((w * x for x, w in zip(xs, ws)), Fraction())
    delta, a, g = rho - lam, rho + s, b - rho
    if delta < 0 or a <= 0 or g <= 0:
        raise CertificateError("measure must have lambda0<=rho<b and rho+s>0")
    residual_sq = sum(
        (w * (x - rho) ** 2 / (x + s) for x, w in zip(xs, ws)),
        Fraction(),
    )
    nonnegative_integral = sum(
        (w * (x - lam) * (x - b) / (x + s) for x, w in zip(xs, ws)),
        Fraction(),
    )
    algebraic_numerator = residual_sq * (a - delta) * (a + g) - a * delta * g
    identity_replay = a * a * nonnegative_integral
    bound = sharp_ground_error_upper(a, g, residual_sq)
    return {
        "rho": rho,
        "delta": delta,
        "a": a,
        "g": g,
        "residual_sq": residual_sq,
        "nonnegative_integral": nonnegative_integral,
        "algebraic_numerator": algebraic_numerator,
        "identity_replay": identity_replay,
        "sharp_error_upper": bound,
        "identity_exact": algebraic_numerator == identity_replay,
        "bound_closes": delta <= bound,
    }


def manifest_failures(data: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY":
        failures.append("classification")
    if data.get("direction") != "observed_to_native":
        failures.append("direction")
    workset = data.get("reassessment_disposition", {})
    if {key: workset.get(key, {}).get("state") for key in ("R1", "R2", "R3")} != {
        "R1": "concluded",
        "R2": "concluded",
        "R3": "concluded",
    }:
        failures.append("workset")
    theorem = data.get("sharp_spectral_certificate", {})
    expected = {
        "support": "{lambda0} union [b,infinity)",
        "shifted_positivity": "lambda0+s>0",
        "mean": "rho",
        "a": "rho+s",
        "g": "b-rho",
        "residual_square": "e=integral (x-rho)^2/(x+s) dmu",
        "proof_integrand": "(x-lambda0)(x-b)/(x+s)>=0 on support",
        "proof_identity": "a^2 integral proof_integrand dmu=e(a-delta)(a+g)-a delta g",
        "sharp_bound": "delta<=e a(a+g)/(a g+e(a+g))",
        "target_budget": "e<=d a g/((a+g)(a-d)) for 0<d<a",
        "two_point_equality": True,
    }
    if any(theorem.get(key) != value for key, value in expected.items()):
        failures.append("theorem")
    consumer = data.get("value_to_consumer_budget", {})
    required = {
        "integral_decomposition": "I=I_hat+error, |error|<=r_I+tau_I",
        "residual_decomposition": "sqrt(e)<=r_nominal+kappa(r_I+tau_I)+eta_other",
        "residual_upper": "e_max=[r_nominal+kappa(r_I+tau_I)+eta_other]^2",
        "energy_requirement": "e_max<=d a g/((a+g)(a-d))",
        "projection_requirement": "e_max<=eta_P^2 g^2/(a+g)",
        "historical_1e-21_is_full_value_target": False,
        "historical_1e-21_is_k152_error_margin": False,
        "native_numeric_budget_emitted": False,
    }
    if any(consumer.get(key) != value for key, value in required.items()):
        failures.append("consumer")
    native = data.get("native_input_audit", {})
    absent = (
        "native_conforming_form_gram",
        "native_coercive_shift_proof",
        "native_complete_dual_residual",
        "native_exterior_gap",
        "native_energy_decision_margin",
        "native_projection_tolerance",
        "order_six_integral_to_residual_map_norm",
    )
    if any(native.get(key) is not False for key in absent):
        failures.append("native audit")
    boundaries = data.get("boundaries", {})
    denied = (
        "native_K152_interval_emitted",
        "full_K218_integral_sign",
        "complete_order_six_error",
        "source_claim_change",
        "physics_ledger_change",
        "canon_change",
        "paper_or_public_posture_change",
        "prediction_or_confirmation_credit",
    )
    if any(boundaries.get(key) is not False for key in denied):
        failures.append("boundaries")
    return failures


def exact_checks(data: dict[str, Any]) -> list[tuple[str, bool]]:
    equality = discrete_spectral_certificate([0, 4], ["1/2", "1/2"], 0, 4, 1)
    strict = discrete_spectral_certificate([0, 4, 6], ["1/2", "1/4", "1/4"], 0, 4, 1)
    a, g, d = Fraction(3), Fraction(2), Fraction(1)
    sharp_budget = sharp_residual_budget(a, g, d)
    legacy_budget = legacy_residual_budget(a, g, d)
    projection_budget = projection_residual_budget(a, g, Fraction(1, 2))
    propagated = propagated_residual_sq_upper(
        Fraction(1, 10), 2, Fraction(1, 100), Fraction(1, 200), Fraction(1, 50)
    )
    return [
        ("manifest contract", not manifest_failures(data)),
        ("two-point identity", equality["identity_exact"] is True),
        ("two-point nonnegative integral zero", equality["nonnegative_integral"] == 0),
        ("two-point delta", equality["delta"] == 2),
        ("two-point residual", equality["residual_sq"] == Fraction(12, 5)),
        ("two-point equality", equality["sharp_error_upper"] == equality["delta"]),
        ("strict identity", strict["identity_exact"] is True),
        ("strict support gives slack", strict["nonnegative_integral"] > 0),
        ("strict bound closes", strict["bound_closes"] is True),
        ("sharp target budget", sharp_budget == Fraction(3, 5)),
        ("legacy target budget", legacy_budget == Fraction(2, 9)),
        ("sharp budget is looser", sharp_budget / legacy_budget == Fraction(27, 10)),
        ("projection budget", projection_budget == Fraction(1, 5)),
        ("propagation separates components", propagated == Fraction(9, 400)),
        ("combined sample closes", propagated <= min(sharp_budget, projection_budget)),
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    data = json.loads(MANIFEST.read_text())
    checks = exact_checks(data)
    failed = [name for name, ok in checks if not ok]
    if failed:
        print(f"FAIL K270: {failed}")
        return 1
    if args.selftest:
        hostile = [
            lambda: sharp_ground_error_upper(0, 1, 0),
            lambda: sharp_residual_budget(1, 1, 1),
            lambda: projection_residual_budget(1, 1, 1),
            lambda: propagated_residual_sq_upper(0, 1, -1, 0, 0),
            lambda: discrete_spectral_certificate([0, 2], ["1/2", "1/2"], 0, 4, 1),
            lambda: discrete_spectral_certificate([0, 4], ["1/3", "1/3"], 0, 4, 1),
        ]
        caught = 0
        for attack in hostile:
            try:
                attack()
            except CertificateError:
                caught += 1
        if caught != len(hostile):
            print(f"FAIL K270 hostile controls caught {caught}/{len(hostile)}")
            return 1
        print(f"PASS K270 hostile controls caught {caught}/{len(hostile)}")
    print(f"PASS {len(checks)}/{len(checks)} K270 exact spectral/budget controls")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
