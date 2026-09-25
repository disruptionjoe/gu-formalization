#!/usr/bin/env python3
"""Independent controls and hostile mutations for K482."""

from __future__ import annotations

import copy
from fractions import Fraction

from k477_k152_multilevel_complement_tree import CertificateError
from k482_k152_uniform_uncertainty_radius import demo, uniform_uncertainty_radius


def checks(packet):
    theorem, control, native = packet["theorem"], packet["exact_control"], packet["native_release"]
    return [
        packet["result_id"] == "K482-K152-UNIFORM-UNCERTAINTY-RADIUS",
        packet["classification"] == "INTERNAL_STRUCTURAL_ONLY",
        packet["direction"] == "observed_to_native",
        "t<(ag-mu^2)" in theorem["radius"],
        "zero Schur slack" in theorem["sharpness"],
        "not a native" in theorem["ceiling"],
        control["nominal_gap_alpha"] == "4",
        control["nominal_gap_gamma"] == "7",
        control["nominal_cross_norm"] == "3",
        control["nominal_slack"] == "19",
        control["sharp_shared_radius_strict"] == "19/17",
        control["selected_radius"] == "1",
        control["effective_slack"] == "2",
        control["identity"].endswith("t(a+g+2mu)"),
        control["same_fixed_form"] is True,
        len(control["proof_refs"]) == 4,
        control["released"] is True,
        native["native_error_model_present"] is False,
        native["native_floor_emitted"] is False,
        native["K152_interval_emitted"] is False,
    ]


def main() -> int:
    packet = demo()
    base = checks(packet)
    mutations = [
        lambda d: d.__setitem__("classification", "PHYSICAL"),
        lambda d: d["theorem"].__setitem__("sharpness", "equality passes"),
        lambda d: d["theorem"].__setitem__("ceiling", "native interval"),
        lambda d: d["exact_control"].__setitem__("sharp_shared_radius_strict", "2"),
        lambda d: d["exact_control"].__setitem__("effective_slack", "0"),
        lambda d: d["exact_control"].__setitem__("identity", "wrong"),
        lambda d: d["exact_control"].__setitem__("proof_refs", []),
        lambda d: d["native_release"].__setitem__("K152_interval_emitted", True),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(packet)
        mutate(candidate)
        rejected += not all(checks(candidate))
    kwargs = dict(alpha=6, gamma=9, mu=3, target_floor=2, selected_radius=1,
                  proof_refs=["a", "g", "m", "t"], same_fixed_form=True)
    invalid = 0
    for update in ({"alpha": 2}, {"gamma": 2}, {"mu": -1}, {"mu": 6},
                   {"selected_radius": Fraction(19, 17)}, {"selected_radius": -1},
                   {"proof_refs": []}, {"same_fixed_form": False}):
        candidate = dict(kwargs)
        candidate.update(update)
        try:
            uniform_uncertainty_radius(**candidate)
        except CertificateError:
            invalid += 1
    print(f"K482 EXACT CONTROL: {sum(base)}/{len(base)} pass")
    print(f"K482 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
    print(f"K482 INVALID INPUTS: {invalid}/8 rejected")
    return 0 if all(base) and rejected == len(mutations) and invalid == 8 else 1


if __name__ == "__main__":
    raise SystemExit(main())
