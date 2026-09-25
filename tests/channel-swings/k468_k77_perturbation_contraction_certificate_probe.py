#!/usr/bin/env python3
"""Independent controls and hostile mutations for K468."""

from __future__ import annotations

import copy
from fractions import Fraction

from k468_k77_perturbation_contraction_certificate import certify, demo


def controls(packet):
    theorem = packet.get("theorem", {})
    exact = packet.get("exact_two_term_control", {})
    boundary = packet.get("boundary_control", {})
    native = packet.get("native_status", {})
    return [
        ("schema", packet.get("schema_version") == "1.0"),
        ("id", packet.get("result_id") == "K468-K77-PERTURBATION-CONTRACTION-CERTIFICATE"),
        ("classification", packet.get("classification") == "INTERNAL_STRUCTURAL_ONLY"),
        ("direction", packet.get("direction") == "observed_to_native"),
        ("base", theorem.get("base") == "dh+hd=I with h^2=0"),
        ("nilpotent", theorem.get("perturbation") == "D=d+delta, D^2=0"),
        ("strict norm", "<1" in theorem.get("quantitative_hypothesis", "")),
        ("formula", theorem.get("adapted_contraction") == "h_delta=h(1+delta h)^(-1)=(1+h delta)^(-1)h"),
        ("conclusion", "zero cohomology" in theorem.get("conclusion", "")),
        ("domain", theorem.get("closed_domain_preservation_still_required") is True),
        ("norm", exact.get("perturbation_norm_infinity") == "1/2"),
        ("inverse", exact.get("adapted_contraction") == [["2/3", "0"], ["0", "3/2"]]),
        ("identity", exact.get("left_and_right_identity") == [["1", "0"], ["0", "1"]]),
        ("acyclic", exact.get("cohomology_dimensions") == [0, 0]),
        ("boundary norm", boundary.get("norm_infinity") == "1"),
        ("boundary singular", boundary.get("perturbed_differential_singular") is True),
        ("boundary rejected", boundary.get("admitted") is False),
        ("constructive", native.get("K464_adapted_contraction_route_constructive") is True),
        ("no coefficients", native.get("actual_action_coefficients_present") is False),
        ("no selection", native.get("native_K77_packet_selected") is False),
        ("no physics", native.get("physical_cohomology_claimed") is False),
    ]


def invalid_rejections() -> int:
    cases = [
        ((-Fraction(1), Fraction(0)), (Fraction(0), -Fraction(1))),
        ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(0))),
    ]
    rejected = 0
    for matrix in cases:
        try:
            certify(matrix)
        except ValueError:
            rejected += 1
    return rejected


def main() -> int:
    packet = demo()
    base = controls(packet)
    mutations = [
        lambda d: d.__setitem__("schema_version", "0"),
        lambda d: d.__setitem__("result_id", "K464"),
        lambda d: d.__setitem__("classification", "PHYSICAL"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["theorem"].__setitem__("base", "dh=I"),
        lambda d: d["theorem"].__setitem__("perturbation", "D=d+delta"),
        lambda d: d["theorem"].__setitem__("quantitative_hypothesis", "||h delta||<=1"),
        lambda d: d["theorem"].__setitem__("adapted_contraction", "h"),
        lambda d: d["theorem"].__setitem__("conclusion", "selected action"),
        lambda d: d["theorem"].__setitem__("closed_domain_preservation_still_required", False),
        lambda d: d["exact_two_term_control"].__setitem__("perturbation_norm_infinity", "1"),
        lambda d: d["exact_two_term_control"].__setitem__("adapted_contraction", []),
        lambda d: d["exact_two_term_control"].__setitem__("left_and_right_identity", []),
        lambda d: d["exact_two_term_control"].__setitem__("cohomology_dimensions", [1, 0]),
        lambda d: d["boundary_control"].__setitem__("norm_infinity", "1/2"),
        lambda d: d["boundary_control"].__setitem__("perturbed_differential_singular", False),
        lambda d: d["boundary_control"].__setitem__("admitted", True),
        lambda d: d["native_status"].__setitem__("K464_adapted_contraction_route_constructive", False),
        lambda d: d["native_status"].__setitem__("actual_action_coefficients_present", True),
        lambda d: d["native_status"].__setitem__("native_K77_packet_selected", True),
        lambda d: d["native_status"].__setitem__("physical_cohomology_claimed", True),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(packet)
        mutate(candidate)
        rejected += not all(ok for _, ok in controls(candidate))
    invalid = invalid_rejections()
    print(f"K468 EXACT CONTROL: {sum(ok for _, ok in base)}/{len(base)} pass")
    print(f"K468 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
    print(f"K468 INVALID INPUTS: {invalid}/2 rejected")
    return 0 if all(ok for _, ok in base) and rejected == len(mutations) and invalid == 2 else 1


if __name__ == "__main__":
    raise SystemExit(main())
