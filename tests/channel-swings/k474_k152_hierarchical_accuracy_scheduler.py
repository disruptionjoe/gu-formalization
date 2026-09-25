#!/usr/bin/env python3
"""K474 composition of K473's recursive floor with K469's accuracy budget."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from typing import Any

from k473_k152_recursive_complement_floor import CertificateError, q, qstr, recursive_floor, sqrt_interval


def schedule(
    *, rho: Any, b: Any, alpha: Any, gamma: Any, mu: Any,
    eta_sq: Any, target_deficit: Any, certified_tail: Any,
    finite_slice_ref: str | None, complete_tail_ref: str | None,
    complement_cross_ref: str | None, residual_ref: str | None,
) -> dict[str, Any]:
    floor = recursive_floor(
        finite_slice_floor=alpha, tail_floor=gamma, cross_norm_upper=mu,
        target_threshold=b, finite_slice_ref=finite_slice_ref,
        complete_tail_ref=complete_tail_ref, cross_block_ref=complement_cross_ref,
        same_fixed_form=True, complete_m_orthogonal_partition=True,
    )
    rho_q, b_q, eta_q = q(rho), q(b), q(eta_sq)
    d, tail = q(target_deficit), q(certified_tail)
    beta_lo = Fraction(floor["complete_complement_floor_outward_interval"][0])
    if not rho_q < b_q < beta_lo or eta_q < 0 or d <= 0 or tail < 0:
        raise CertificateError("invalid ground-budget ordering or nonnegative inputs")
    if not isinstance(residual_ref, str) or not residual_ref.strip():
        raise CertificateError("complete residual reference required")
    budget = d * (beta_lo - rho_q + d)
    if eta_q > budget:
        raise CertificateError("complete M-dual residual exceeds the K469 target budget")
    root_lo, _ = sqrt_interval(budget)
    finite_allowance = root_lo - tail
    if finite_allowance <= 0:
        raise CertificateError("certified tail consumes the complete residual allowance")
    return {
        "recursive_floor": floor,
        "trial_rayleigh": qstr(rho_q),
        "count_threshold": qstr(b_q),
        "target_deficit": qstr(d),
        "complete_M_dual_residual_square_upper": qstr(eta_q),
        "K469_residual_square_budget_lower": qstr(budget),
        "budget_pass": True,
        "certified_norm_tail": qstr(tail),
        "finite_Gram_sqrt_allowance": qstr(finite_allowance),
        "release_inequality": "sqrt(Q12)+tail<=sqrt(d(beta-rho+d))",
        "finite_Gram_entries": 59586,
        "native_accuracy_released": False,
        "residual_ref": residual_ref,
    }


def demo() -> dict[str, Any]:
    tail = Fraction(3011499, 838860800)
    control = schedule(
        rho=-2, b=1, alpha=3, gamma=6, mu=2,
        eta_sq=Fraction(9, 4), target_deficit=Fraction(1, 2),
        certified_tail=tail, finite_slice_ref="control#F",
        complete_tail_ref="control#T", complement_cross_ref="control#X",
        residual_ref="control#K457",
    )
    return {
        "schema_version": "1.0",
        "result_id": "K474-K152-HIERARCHICAL-ACCURACY-SCHEDULER",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "theorem": {
            "inputs": ["K473 finite/tail/cross complement packet", "K469 rho,d,eta packet", "K457 certified norm tail"],
            "two_fail_closed_tests": ["mu^2<(alpha-b)(gamma-b)", "eta^2<=d(beta-rho+d)"],
            "release": "only the conjunction releases a finite-Gram accuracy",
        },
        "exact_composed_control": control,
        "native_release": {
            "native_hierarchical_packet_present": False,
            "native_target_deficit_present": False,
            "K457_evaluation_started": False,
            "native_K152_interval_emitted": False,
        },
    }


def main() -> int:
    argparse.ArgumentParser().parse_args()
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
