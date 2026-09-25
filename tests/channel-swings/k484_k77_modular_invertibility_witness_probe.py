#!/usr/bin/env python3
"""Independent controls and hostile mutations for K484."""

from __future__ import annotations

import copy
from fractions import Fraction

from k484_k77_modular_invertibility_witness import demo, determinant_mod_prime, modular_witness


def checks(packet):
    theorem, control, k77 = packet["theorem"], packet["exact_control"], packet["K77_application"]
    return [
        packet["result_id"] == "K484-K77-MODULAR-INVERTIBILITY-WITNESS",
        packet["classification"] == "BRIDGE_OR_SEMANTIC_BOUNDARY",
        packet["direction"] == "observed_to_native",
        "nonzero determinant modulo one prime" in theorem["witness"],
        "Combined with K483" in theorem["composition"],
        "zero modular determinant is inconclusive" in theorem["ceiling"],
        control["matrix_size"] == 4,
        control["denominator_lcm"] == 6,
        control["prime"] == 5,
        control["cleared_determinant_mod_prime"] == 1,
        control["exact_rational_determinant"] == "1/6",
        control["invertibility_certified"] is True,
        bool(control["proof_ref"]),
        k77["square_certificate_size"] == 46592,
        k77["nilpotence_still_required"] is True,
        k77["native_matrix_present"] is False,
        k77["physical_cohomology_emitted"] is False,
    ]


def main() -> int:
    packet = demo()
    base = checks(packet)
    mutations = [
        lambda d: d.__setitem__("classification", "PHYSICAL"),
        lambda d: d["theorem"].__setitem__("witness", "probabilistic hint"),
        lambda d: d["theorem"].__setitem__("ceiling", "zero proves singular"),
        lambda d: d["exact_control"].__setitem__("denominator_lcm", 1),
        lambda d: d["exact_control"].__setitem__("cleared_determinant_mod_prime", 0),
        lambda d: d["exact_control"].__setitem__("exact_rational_determinant", "0"),
        lambda d: d["K77_application"].__setitem__("nilpotence_still_required", False),
        lambda d: d["K77_application"].__setitem__("physical_cohomology_emitted", True),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(packet)
        mutate(candidate)
        rejected += not all(checks(candidate))
    invalid = 0
    singular = [[1, 2], [2, 4]]
    cases = [
        lambda: modular_witness(singular, 5, "singular"),
        lambda: modular_witness([[5]], 5, "nonzero-but-divisible"),
        lambda: modular_witness([[1]], 4, "composite"),
        lambda: modular_witness([[1, 2]], 5, "shape"),
        lambda: modular_witness([[1]], 5, ""),
        lambda: determinant_mod_prime([], 5),
        lambda: determinant_mod_prime([[1]], 1),
    ]
    for case in cases:
        try:
            case()
        except ValueError:
            invalid += 1
    print(f"K484 EXACT CONTROL: {sum(base)}/{len(base)} pass")
    print(f"K484 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
    print(f"K484 INVALID INPUTS: {invalid}/{len(cases)} rejected")
    return 0 if all(base) and rejected == len(mutations) and invalid == len(cases) else 1


if __name__ == "__main__":
    raise SystemExit(main())
