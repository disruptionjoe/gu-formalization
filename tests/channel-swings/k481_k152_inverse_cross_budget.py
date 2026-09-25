#!/usr/bin/env python3
"""K481 inverse cross-norm budget for a requested K473 floor."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from typing import Any

from k477_k152_multilevel_complement_tree import CertificateError, q, qstr, sqrt_interval


def inverse_cross_budget(
    *, alpha: Any, gamma: Any, target_floor: Any, selected_mu: Any,
    proof_refs: list[str], same_fixed_form: bool, complete_partition: bool,
    bits: int = 80,
) -> dict[str, Any]:
    alpha_q, gamma_q, target_q, mu_q = map(q, (alpha, gamma, target_floor, selected_mu))
    if same_fixed_form is not True or complete_partition is not True:
        raise CertificateError("same-form complete partition required")
    if len(proof_refs) != 3 or any(not isinstance(ref, str) or not ref.strip() for ref in proof_refs):
        raise CertificateError("three nonempty proof references required")
    if mu_q < 0 or alpha_q <= target_q or gamma_q <= target_q:
        raise CertificateError("nonnegative norm and diagonal floors above target required")
    budget_sq = (alpha_q - target_q) * (gamma_q - target_q)
    slack = budget_sq - mu_q * mu_q
    if slack <= 0:
        raise CertificateError("selected cross norm must lie strictly inside the budget")
    disc = (alpha_q - gamma_q) ** 2 + 4 * mu_q * mu_q
    root_lo, root_hi = sqrt_interval(disc, bits)
    beta_lo = (alpha_q + gamma_q - root_hi) / 2
    if beta_lo <= target_q:
        raise CertificateError("outward lower root must exceed requested target")
    return {
        "alpha_lower": qstr(alpha_q),
        "gamma_lower": qstr(gamma_q),
        "requested_floor": qstr(target_q),
        "maximum_cross_norm_squared_strict": qstr(budget_sq),
        "selected_cross_norm": qstr(mu_q),
        "strict_budget_slack": qstr(slack),
        "beta_outward_lower": qstr(beta_lo),
        "same_fixed_form": True,
        "complete_partition": True,
        "proof_refs": proof_refs,
        "released": True,
    }


def demo() -> dict[str, Any]:
    control = inverse_cross_budget(
        alpha=5, gamma=8, target_floor=3, selected_mu=3,
        proof_refs=["control#alpha", "control#gamma", "control#target"],
        same_fixed_form=True, complete_partition=True, bits=32,
    )
    return {
        "schema_version": "1.0",
        "result_id": "K481-K152-INVERSE-CROSS-BUDGET",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "theorem": {
            "inverse_budget": "To certify beta>t, require mu^2<(alpha-t)(gamma-t).",
            "use": "A requested complete-complement floor determines the strict cross-norm acquisition budget before numerical evaluation.",
            "ceiling": "The budget supplies no native floor, cross norm, completeness witness or K152 interval.",
        },
        "exact_control": control,
        "native_release": {
            "native_inputs_present": False,
            "K457_evaluation_released": False,
            "K152_interval_emitted": False,
        },
    }


def main() -> int:
    argparse.ArgumentParser().parse_args()
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
