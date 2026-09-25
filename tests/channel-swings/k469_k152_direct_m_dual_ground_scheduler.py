#!/usr/bin/env python3
"""K469 direct M-dual ground-deficit scheduler."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import isqrt
from typing import Any


def q(value: Any) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    raise ValueError("exact rational input required")


def sqrt_fraction(value: Fraction) -> Fraction:
    if value < 0:
        raise ValueError("nonnegative radicand required")
    n, d = isqrt(value.numerator), isqrt(value.denominator)
    if n * n != value.numerator or d * d != value.denominator:
        raise ValueError("exact square control required")
    return Fraction(n, d)


def deficit_upper(rho: Any, beta: Any, eta_sq: Any) -> Fraction:
    rho_q, beta_q, eta_q = q(rho), q(beta), q(eta_sq)
    if beta_q <= rho_q or eta_q < 0:
        raise ValueError("requires beta>rho and eta_sq>=0")
    gap = beta_q - rho_q
    return (sqrt_fraction(gap * gap + 4 * eta_q) - gap) / 2


def residual_budget(rho: Any, beta: Any, target_deficit: Any) -> Fraction:
    rho_q, beta_q, target_q = q(rho), q(beta), q(target_deficit)
    gap = beta_q - rho_q
    if gap <= 0 or target_q <= 0:
        raise ValueError("requires beta>rho and target_deficit>0")
    return target_q * (gap + target_q)


def demo() -> dict[str, Any]:
    rho, beta, eta_sq, target = Fraction(-2), Fraction(2), Fraction(9, 4), Fraction(1, 2)
    return {
        "schema_version": "1.0",
        "result_id": "K469-K152-DIRECT-M-DUAL-GROUND-SCHEDULER",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "theorem": {
            "premise": "rho<beta and Q R Q>=beta Q_M on the complete M-orthogonal complement",
            "cross_norm": "eta=||Q(R-rho M)u||_(M-dual)",
            "ground_interval": "[rho-delta,rho] with delta=(sqrt((beta-rho)^2+4 eta^2)-(beta-rho))/2",
            "target_budget": "eta^2<=d(beta-rho+d)",
            "shift_required": False,
            "K466_bridge_required_on_this_route": False,
            "complete_complement_floor_still_required": True,
        },
        "exact_two_block_control": {
            "rho": "-2",
            "beta": "2",
            "eta": "3/2",
            "eta_sq": "9/4",
            "exact_ground": "-5/2",
            "ground_deficit": str(deficit_upper(rho, beta, eta_sq)),
            "target_deficit": "1/2",
            "M_dual_square_budget": str(residual_budget(rho, beta, target)),
            "equality": deficit_upper(rho, beta, eta_sq) == target,
        },
        "release_rule": {
            "finite_Gram_entries": 59586,
            "native_beta_present": False,
            "native_target_deficit_present": False,
            "native_accuracy_released": False,
        },
    }


def main() -> int:
    argparse.ArgumentParser().parse_args()
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
