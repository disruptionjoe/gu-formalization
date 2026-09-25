#!/usr/bin/env python3
"""K478 robust interval form of the K473 strict complement margin."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from typing import Any

from k477_k152_multilevel_complement_tree import CertificateError, q, qstr, sqrt_interval


def robust_interval_margin(
    *,
    alpha_nominal: Any,
    alpha_error: Any,
    gamma_nominal: Any,
    gamma_error: Any,
    mu_nominal: Any,
    mu_error: Any,
    threshold_nominal: Any,
    threshold_error: Any,
    proof_refs: list[str],
    same_fixed_form: bool,
    complete_partition: bool,
    bits: int = 80,
) -> dict[str, Any]:
    values = [q(v) for v in (alpha_nominal, alpha_error, gamma_nominal, gamma_error,
                              mu_nominal, mu_error, threshold_nominal, threshold_error)]
    alpha0, ea, gamma0, eg, mu0, em, b0, eb = values
    if any(err < 0 for err in (ea, eg, em, eb)) or mu0 < 0:
        raise CertificateError("nominal norm and all error radii must be nonnegative")
    if same_fixed_form is not True or complete_partition is not True:
        raise CertificateError("same-form complete partition required")
    if len(proof_refs) != 4 or any(not isinstance(ref, str) or not ref.strip() for ref in proof_refs):
        raise CertificateError("four nonempty interval proof references required")
    alpha = alpha0 - ea
    gamma = gamma0 - eg
    mu = mu0 + em
    b = b0 + eb
    if not alpha > b or not gamma > b:
        raise CertificateError("worst-case diagonal floors must exceed worst-case threshold")
    slack = (alpha - b) * (gamma - b) - mu * mu
    if not slack > 0:
        raise CertificateError("worst-case strict Schur slack must be positive")
    disc = (alpha - gamma) ** 2 + 4 * mu * mu
    root_lo, root_hi = sqrt_interval(disc, bits)
    beta_lo = (alpha + gamma - root_hi) / 2
    beta_hi = (alpha + gamma - root_lo) / 2
    if not beta_lo > b:
        raise CertificateError("worst-case outward beta must exceed threshold")
    return {
        "effective_alpha_lower": qstr(alpha),
        "effective_gamma_lower": qstr(gamma),
        "effective_mu_upper": qstr(mu),
        "effective_threshold_upper": qstr(b),
        "strict_schur_slack": qstr(slack),
        "discriminant": qstr(disc),
        "sqrt_outward_interval": [qstr(root_lo), qstr(root_hi)],
        "beta_outward_interval": [qstr(beta_lo), qstr(beta_hi)],
        "robust_release": True,
        "same_fixed_form": True,
        "complete_partition": True,
        "proof_refs": proof_refs,
    }


def demo() -> dict[str, Any]:
    control = robust_interval_margin(
        alpha_nominal=3, alpha_error=Fraction(1, 16),
        gamma_nominal=6, gamma_error=Fraction(1, 16),
        mu_nominal=2, mu_error=Fraction(1, 16),
        threshold_nominal=1, threshold_error=Fraction(1, 16),
        proof_refs=["control#alpha", "control#gamma", "control#mu", "control#b"],
        same_fixed_form=True, complete_partition=True, bits=32,
    )
    return {
        "schema_version": "1.0",
        "result_id": "K478-K152-ROBUST-INTERVAL-MARGIN",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "theorem": {
            "monotone_substitution": "Use alpha_lower, gamma_lower, mu_upper and b_upper in the K473 test.",
            "strict_test": "(alpha_lower-b_upper)(gamma_lower-b_upper)-mu_upper^2>0",
            "release": "A positive worst-case slack and outward beta_lower>b_upper certify every value in the supplied intervals.",
        },
        "rational_error_control": control,
        "native_release": {
            "native_intervals_present": False,
            "native_beta_emitted": False,
            "K457_evaluation_released": False,
        },
    }


def main() -> int:
    argparse.ArgumentParser().parse_args()
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
