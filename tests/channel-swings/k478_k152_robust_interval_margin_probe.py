#!/usr/bin/env python3
"""Independent controls and hostile mutations for K478."""

from __future__ import annotations

import copy
from fractions import Fraction

from k477_k152_multilevel_complement_tree import CertificateError
from k478_k152_robust_interval_margin import demo, robust_interval_margin


def checks(packet):
    theorem, control, native = packet["theorem"], packet["rational_error_control"], packet["native_release"]
    return [
        packet["result_id"] == "K478-K152-ROBUST-INTERVAL-MARGIN",
        packet["classification"] == "INTERNAL_STRUCTURAL_ONLY",
        packet["direction"] == "observed_to_native",
        "alpha_lower" in theorem["monotone_substitution"],
        theorem["strict_test"].endswith(">0"),
        "every value" in theorem["release"],
        control["effective_alpha_lower"] == "47/16",
        control["effective_gamma_lower"] == "95/16",
        control["effective_mu_upper"] == "33/16",
        control["effective_threshold_upper"] == "17/16",
        control["strict_schur_slack"] == "1251/256",
        Fraction(control["beta_outward_interval"][0]) > Fraction(17, 16),
        control["robust_release"] is True,
        control["same_fixed_form"] is True,
        control["complete_partition"] is True,
        len(control["proof_refs"]) == 4,
        native["native_intervals_present"] is False,
        native["native_beta_emitted"] is False,
        native["K457_evaluation_released"] is False,
    ]


def main() -> int:
    packet = demo()
    base = checks(packet)
    mutations = [
        lambda d: d.__setitem__("classification", "PHYSICAL"),
        lambda d: d["theorem"].__setitem__("strict_test", "slack>=0"),
        lambda d: d["theorem"].__setitem__("release", "one nominal value"),
        lambda d: d["rational_error_control"].__setitem__("effective_alpha_lower", "3"),
        lambda d: d["rational_error_control"].__setitem__("strict_schur_slack", "0"),
        lambda d: d["rational_error_control"].__setitem__("robust_release", False),
        lambda d: d["rational_error_control"].__setitem__("same_fixed_form", False),
        lambda d: d["rational_error_control"].__setitem__("proof_refs", []),
        lambda d: d["native_release"].__setitem__("K457_evaluation_released", True),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(packet)
        mutate(candidate)
        rejected += not all(checks(candidate))
    kwargs = dict(alpha_nominal=3, alpha_error=Fraction(1, 16), gamma_nominal=6,
                  gamma_error=Fraction(1, 16), mu_nominal=2, mu_error=Fraction(1, 16),
                  threshold_nominal=1, threshold_error=Fraction(1, 16),
                  proof_refs=["a", "g", "m", "b"], same_fixed_form=True,
                  complete_partition=True)
    invalid = 0
    for update in ({"alpha_error": -1}, {"mu_nominal": -1}, {"alpha_error": 2},
                   {"mu_error": 4}, {"proof_refs": []}, {"same_fixed_form": False},
                   {"complete_partition": False}):
        candidate = dict(kwargs)
        candidate.update(update)
        try:
            robust_interval_margin(**candidate)
        except CertificateError:
            invalid += 1
    print(f"K478 EXACT CONTROL: {sum(base)}/{len(base)} pass")
    print(f"K478 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
    print(f"K478 INVALID INPUTS: {invalid}/7 rejected")
    return 0 if all(base) and rejected == len(mutations) and invalid == 7 else 1


if __name__ == "__main__":
    raise SystemExit(main())
