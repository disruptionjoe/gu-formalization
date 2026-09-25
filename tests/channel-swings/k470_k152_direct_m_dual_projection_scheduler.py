#!/usr/bin/env python3
"""K470 direct M-dual ground-projection scheduler."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from typing import Any

from k469_k152_direct_m_dual_ground_scheduler import deficit_upper, q, residual_budget


def projection_sq_upper(rho: Any, beta: Any, eta_sq: Any) -> Fraction:
    rho_q, beta_q, eta_q = q(rho), q(beta), q(eta_sq)
    gap = beta_q - rho_q
    if gap <= 0 or eta_q < 0:
        raise ValueError("requires beta>rho and eta_sq>=0")
    delta = deficit_upper(rho_q, beta_q, eta_q)
    return delta / (gap + delta)


def projection_residual_budget(rho: Any, beta: Any, projection_tolerance: Any) -> Fraction:
    rho_q, beta_q, p = q(rho), q(beta), q(projection_tolerance)
    gap = beta_q - rho_q
    if gap <= 0 or not 0 < p < 1:
        raise ValueError("requires beta>rho and 0<p<1")
    target_deficit = p * p * gap / (1 - p * p)
    return residual_budget(rho_q, beta_q, target_deficit)


def demo() -> dict[str, Any]:
    rho, beta, eta_sq, p = Fraction(-2), Fraction(2), Fraction(9, 4), Fraction(1, 3)
    return {
        "schema_version": "1.0",
        "result_id": "K470-K152-DIRECT-M-DUAL-PROJECTION-SCHEDULER",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "theorem": {
            "premise": "the K469 complete-complement packet has exactly one spectral direction below beta",
            "projection_bound": "sin_M^2(u,E0)<=delta/(beta-rho+delta)",
            "delta": "(sqrt((beta-rho)^2+4 eta^2)-(beta-rho))/2",
            "target_budget": "eta^2<=p^2(beta-rho)^2/(1-p^2)^2",
            "complete_ground_eigenspace_projection": True,
            "finite_Ritz_projection_substitutable": False,
        },
        "exact_two_block_control": {
            "rho": "-2",
            "beta": "2",
            "eta": "3/2",
            "ground_deficit": "1/2",
            "projection_square": str(projection_sq_upper(rho, beta, eta_sq)),
            "projection_tolerance": "1/3",
            "M_dual_square_budget": str(projection_residual_budget(rho, beta, p)),
            "equality": projection_sq_upper(rho, beta, eta_sq) == p * p,
        },
        "native_status": {
            "native_complete_complement_floor_present": False,
            "native_projection_tolerance_selected": False,
            "native_projection_claim_emitted": False,
        },
    }


def main() -> int:
    argparse.ArgumentParser().parse_args()
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
