#!/usr/bin/env python3
"""Independent controls and hostile mutations for K454."""

from __future__ import annotations

import copy
from fractions import Fraction

from k454_k152_consumer_form_defect_transfer import demo


def inside(interval, actual):
    return Fraction(interval[0]) <= Fraction(actual[0]) <= Fraction(actual[1]) <= Fraction(interval[1])


def controls(packet):
    rows = packet.get("sectors", [])
    decision = packet.get("decision", {})
    theorem = packet.get("theorem", {})
    return [
        ("schema", packet.get("schema_version") == "1.0"),
        ("id", packet.get("result_id") == "K454-K152-CONSUMER-FORM-DEFECT-TRANSFER"),
        ("classification", packet.get("classification") == "INTERNAL_STRUCTURAL_ONLY"),
        ("direction", packet.get("direction") == "observed_to_native"),
        ("three sectors", len(rows) == 3),
        ("two-sided forms", all(row.get("form_two_sided_certified") is True for row in rows)),
        ("two-sided Grams", all(row.get("Gram_two_sided_certified") is True for row in rows)),
        ("positive alphas", all(Fraction(row.get("Gram_relative_radius_alpha", "0")) > 0 for row in rows)),
        ("gamma formula", all(Fraction(row["joint_shifted_perturbation_gamma"]) == Fraction(row["form_relative_radius_beta"]) + row["shift"] * Fraction(row["Gram_relative_radius_alpha"]) for row in rows)),
        ("first enclosed", all(inside(row["transferred_first_generalized_interval"], row["actual_target_first_generalized_interval"]) for row in rows)),
        ("next enclosed", all(inside(row["transferred_next_distinct_interval"], row["actual_target_next_distinct_interval"]) for row in rows)),
        ("residual enclosed", all(Fraction(row["actual_target_shifted_dual_residual_square"]) <= Fraction(row["target_shifted_dual_residual_square_upper"]) for row in rows)),
        ("row decision", all(row.get("all_target_quantities_enclosed") is True for row in rows)),
        ("joint required", decision.get("joint_form_and_Gram_transfer_required") is True),
        ("form-only refused", decision.get("K451_form_only_radius_is_complete_consumer_transfer") is False),
        ("finite transfer", decision.get("finite_consumer_quantities_rigorously_transferred") is True),
        ("not native", decision.get("bound_is_cofinal_native_residual_certificate") is False),
        ("no interval", decision.get("native_K152_interval_emitted") is False),
        ("theorem gamma", theorem.get("shifted_form_defect") == "gamma=beta+s*alpha"),
    ]


def main() -> int:
    packet = demo()
    base = controls(packet)
    mutations = [
        lambda d: d.__setitem__("schema_version", "0"),
        lambda d: d.__setitem__("result_id", "K453"),
        lambda d: d.__setitem__("classification", "PHYSICAL"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["sectors"].pop(),
        lambda d: d["sectors"][0].__setitem__("form_two_sided_certified", False),
        lambda d: d["sectors"][0].__setitem__("Gram_two_sided_certified", False),
        lambda d: d["sectors"][0].__setitem__("Gram_relative_radius_alpha", "0"),
        lambda d: d["sectors"][0].__setitem__("joint_shifted_perturbation_gamma", "0"),
        lambda d: d["sectors"][0].__setitem__("transferred_first_generalized_interval", ["0", "0"]),
        lambda d: d["sectors"][0].__setitem__("transferred_next_distinct_interval", ["0", "0"]),
        lambda d: d["sectors"][0].__setitem__("target_shifted_dual_residual_square_upper", "0"),
        lambda d: d["sectors"][0].__setitem__("all_target_quantities_enclosed", False),
        lambda d: d["decision"].__setitem__("joint_form_and_Gram_transfer_required", False),
        lambda d: d["decision"].__setitem__("K451_form_only_radius_is_complete_consumer_transfer", True),
        lambda d: d["decision"].__setitem__("finite_consumer_quantities_rigorously_transferred", False),
        lambda d: d["decision"].__setitem__("bound_is_cofinal_native_residual_certificate", True),
        lambda d: d["decision"].__setitem__("native_K152_interval_emitted", True),
        lambda d: d["theorem"].__setitem__("shifted_form_defect", "beta"),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(packet)
        mutate(candidate)
        if not all(ok for _, ok in controls(candidate)):
            rejected += 1
    print(f"K454 EXACT CONTROL: {sum(ok for _, ok in base)}/{len(base)} pass")
    print(f"K454 HOSTILE MUTATIONS: {rejected}/{len(mutations)} rejected")
    return 0 if all(ok for _, ok in base) and rejected == len(mutations) else 1


if __name__ == "__main__":
    raise SystemExit(main())
