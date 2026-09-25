#!/usr/bin/env python3
"""K482 sharp shared gap/cross uncertainty radius for K473."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from typing import Any

from k477_k152_multilevel_complement_tree import CertificateError, q, qstr


def uniform_uncertainty_radius(
    *, alpha: Any, gamma: Any, mu: Any, target_floor: Any,
    selected_radius: Any, proof_refs: list[str], same_fixed_form: bool,
) -> dict[str, Any]:
    alpha_q, gamma_q, mu_q, target_q, t_q = map(
        q, (alpha, gamma, mu, target_floor, selected_radius)
    )
    if same_fixed_form is not True:
        raise CertificateError("same fixed form required")
    if len(proof_refs) != 4 or any(not isinstance(ref, str) or not ref.strip() for ref in proof_refs):
        raise CertificateError("four nonempty proof references required")
    a, g = alpha_q - target_q, gamma_q - target_q
    if mu_q < 0 or a <= 0 or g <= 0:
        raise CertificateError("positive gaps and nonnegative cross norm required")
    slack = a * g - mu_q * mu_q
    if slack <= 0:
        raise CertificateError("nominal strict margin required")
    denominator = a + g + 2 * mu_q
    radius = slack / denominator
    if t_q < 0 or t_q >= radius:
        raise CertificateError("selected radius must be nonnegative and strictly below the sharp radius")
    effective_slack = (a - t_q) * (g - t_q) - (mu_q + t_q) ** 2
    identity_slack = slack - denominator * t_q
    if effective_slack != identity_slack or effective_slack <= 0:
        raise CertificateError("shared uncertainty identity failed")
    return {
        "nominal_gap_alpha": qstr(a),
        "nominal_gap_gamma": qstr(g),
        "nominal_cross_norm": qstr(mu_q),
        "nominal_slack": qstr(slack),
        "sharp_shared_radius_strict": qstr(radius),
        "selected_radius": qstr(t_q),
        "effective_slack": qstr(effective_slack),
        "identity": "(a-t)(g-t)-(mu+t)^2 = ag-mu^2-t(a+g+2mu)",
        "same_fixed_form": True,
        "proof_refs": proof_refs,
        "released": True,
    }


def demo() -> dict[str, Any]:
    control = uniform_uncertainty_radius(
        alpha=6, gamma=9, mu=3, target_floor=2, selected_radius=1,
        proof_refs=["control#alpha", "control#gamma", "control#mu", "control#target"],
        same_fixed_form=True,
    )
    return {
        "schema_version": "1.0",
        "result_id": "K482-K152-UNIFORM-UNCERTAINTY-RADIUS",
        "classification": "INTERNAL_STRUCTURAL_ONLY",
        "direction": "observed_to_native",
        "theorem": {
            "radius": "If both certified gaps may decrease by t and the cross norm may increase by t, strict K473 margin survives exactly for t<(ag-mu^2)/(a+g+2mu).",
            "sharpness": "Equality gives zero Schur slack, so the boundary is not releasable.",
            "ceiling": "The radius is an input-tolerance contract, not a native uncertainty estimate or K152 interval.",
        },
        "exact_control": control,
        "native_release": {
            "native_error_model_present": False,
            "native_floor_emitted": False,
            "K152_interval_emitted": False,
        },
    }


def main() -> int:
    argparse.ArgumentParser().parse_args()
    print(json.dumps(demo(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
