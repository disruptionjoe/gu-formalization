#!/usr/bin/env python3
"""Independent controls and hostile mutations for K467."""

from __future__ import annotations

import copy
from fractions import Fraction

from k467_k152_residual_accuracy_scheduler import demo, schedule


def controls(packet):
    comp = packet.get("composition", {})
    exact = packet.get("exact_control", {})
    release = packet.get("release_rule", {})
    return [
        ("schema", packet.get("schema_version") == "1.0"),
        ("id", packet.get("result_id") == "K467-K152-RESIDUAL-ACCURACY-SCHEDULER"),
        ("classification", packet.get("classification") == "INTERNAL_STRUCTURAL_ONLY"),
        ("direction", packet.get("direction") == "observed_to_native"),
        ("K270", comp.get("K270_energy_budget") == "d*a*g/((a+g)(a-d))"),
        ("K466", comp.get("K466_bridge_requirement") == "eta_M^2 <= c*E_budget"),
        ("K457", comp.get("K457_finite_requirement") == "sqrt(Q_12)+epsilon_tail <= sqrt(c*E_budget)"),
        ("K463", comp.get("K463_coercivity_input") == "c=lambda_-+s>0"),
        ("energy", exact.get("shifted_energy_budget") == "3/5"),
        ("M budget", exact.get("M_dual_square_budget") == "1"),
        ("finite norm", exact.get("finite_norm_budget") == "835849301/838860800"),
        ("finite square", exact.get("finite_Gram_square_budget") == "698644053982188601/703687441776640000"),
        ("entries", release.get("finite_Gram_entries") == 59586),
        ("no premature evaluation", release.get("evaluate_before_native_c_and_energy_budget") is False),
        ("no native constants", release.get("native_constants_present") is False),
        ("no native accuracy", release.get("native_accuracy_released") is False),
    ]


def invalid_rejections() -> int:
    tail = Fraction(3011499, 838860800)
    cases = [
        (Fraction(1), Fraction(2), Fraction(1), Fraction(1), tail),
        (Fraction(3), Fraction(2), Fraction(1), Fraction(0), tail),
        (Fraction(3), Fraction(2), Fraction(1), Fraction(5, 3), Fraction(1)),
        (Fraction(3), Fraction(2), Fraction(1), Fraction(1), tail),
    ]
    rejected = 0
    for args in cases:
        try:
            schedule(*args)
        except ValueError:
            rejected += 1
    return rejected


def main() -> int:
    packet = demo()
    base = controls(packet)
    mutations = [
        lambda d: d.__setitem__("schema_version", "0"),
        lambda d: d.__setitem__("result_id", "K466"),
        lambda d: d.__setitem__("classification", "PHYSICAL"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["composition"].__setitem__("K270_energy_budget", "d"),
        lambda d: d["composition"].__setitem__("K466_bridge_requirement", "eta<=E"),
        lambda d: d["composition"].__setitem__("K457_finite_requirement", "Q<=E"),
        lambda d: d["composition"].__setitem__("K463_coercivity_input", "c=1"),
        lambda d: d["exact_control"].__setitem__("shifted_energy_budget", "1"),
        lambda d: d["exact_control"].__setitem__("M_dual_square_budget", "3/5"),
        lambda d: d["exact_control"].__setitem__("finite_norm_budget", "1"),
        lambda d: d["exact_control"].__setitem__("finite_Gram_square_budget", "1"),
        lambda d: d["release_rule"].__setitem__("finite_Gram_entries", 59234),
        lambda d: d["release_rule"].__setitem__("evaluate_before_native_c_and_energy_budget", True),
        lambda d: d["release_rule"].__setitem__("native_constants_present", True),
        lambda d: d["release_rule"].__setitem__("native_accuracy_released", True),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(packet)
        mutate(candidate)
        rejected += not all(ok for _, ok in controls(candidate))
    invalid = invalid_rejections()
    print(f"K467 EXACT CONTROL: {sum(ok for _, ok in base)}/{len(base)} pass")
    print(f"K467 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
    print(f"K467 INVALID INPUTS: {invalid}/4 rejected")
    return 0 if all(ok for _, ok in base) and rejected == len(mutations) and invalid == 4 else 1


if __name__ == "__main__":
    raise SystemExit(main())
