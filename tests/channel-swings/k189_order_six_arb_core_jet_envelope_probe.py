#!/usr/bin/env python3
"""Independent reporting, replay, and hostile controls for K189."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k189-order-six-arb-core-jet-envelope-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k189-order-six-arb-core-jet-envelope-wave-2026-09-09.md"
SOLVER = ROOT / "tests/channel-swings/k189_order_six_arb_core_jet_envelope.py"
K186 = ROOT / "lab/process/k186-order-six-bessel-vandermonde-wave.json"
K188 = ROOT / "lab/process/k188-order-six-small-rho-strip-wave.json"


def load_solver():
    spec = importlib.util.spec_from_file_location("k189_solver", SOLVER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SOLVER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K189 = load_solver()


def expected_occurrences(source: dict[str, Any]) -> dict[str, int]:
    result: dict[str, int] = {}
    for entry in source["complete_factorization_inventory"]["entries"]:
        for factor in entry["species_factors"]:
            if factor["size"] <= 1:
                continue
            key = (
                f"m{factor['size']}|"
                f"L{','.join(map(str, factor['left_canonical_positions']))}|"
                f"R{','.join(map(str, factor['right_canonical_positions']))}"
            )
            result[key] = result.get(key, 0) + 1
    return result


def manifest_failures(data: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    source = json.loads(K186.read_text())
    split = json.loads(K188.read_text())
    fixed = data.get("fixed_control", {})
    backend = data.get("arb_backend", {})
    theorem = data.get("theorem_certificate", {})
    envelope = data.get("complete_pattern_envelopes", {})
    release = data.get("release_test", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY":
        failures.append("classification")
    expected_fixed = ("2^-20", "2^-180", "2^-200", "1/4", 53, 468, 234, 18, 4)
    actual_fixed = (
        fixed.get("radial_floor"), fixed.get("angular_floor"), fixed.get("primitive_floor"),
        fixed.get("radial_ceiling"), fixed.get("source_patterns"),
        fixed.get("source_nontrivial_occurrences"), fixed.get("source_time_gram_entries"),
        fixed.get("source_coherent_groups"), fixed.get("maximum_primitive_mixed_derivative_order"),
    )
    if actual_fixed != expected_fixed:
        failures.append("fixed")
    if fixed.get("domain") != split["next_exact_input"]["domain"]:
        failures.append("domain")
    if (
        backend.get("python_flint_version") != "0.9.0"
        or backend.get("flint_version") != "3.6.0"
        or backend.get("decimal_digits") != 100
        or backend.get("threads") != 1
        or backend.get("all_endpoint_values_are_nonzero_width_balls") is not True
    ):
        failures.append("backend")
    required_theorem = (
        "kernel", "complete_monotonicity", "derivative_identity",
        "tensor_hermite_genocchi", "pattern_argument_floor",
        "determinant_derivative_bound", "normalization",
        "normalization_derivative_bound", "scope",
    )
    if any(not theorem.get(key) for key in required_theorem):
        failures.append("theorem")
    occurrences = expected_occurrences(source)
    patterns = envelope.get("patterns", {})
    if set(patterns) != set(source["unique_patterns"]) or len(patterns) != 53:
        failures.append("pattern_ids")
    for pattern_id, row in patterns.items():
        if pattern_id not in occurrences:
            continue
        prior = source["unique_patterns"][pattern_id]
        if row.get("size") != prior["size"]:
            failures.append(f"size:{pattern_id}")
        if row.get("left_canonical_positions") != prior["left_canonical_positions"]:
            failures.append(f"left:{pattern_id}")
        if row.get("right_canonical_positions") != prior["right_canonical_positions"]:
            failures.append(f"right:{pattern_id}")
        if row.get("occurrences") != occurrences[pattern_id]:
            failures.append(f"occurrences:{pattern_id}")
        derivatives = row.get("primitive_mixed_derivative_absolute_bounds", {})
        if set(derivatives) != {"0", "1", "2", "3", "4"}:
            failures.append(f"derivative_orders:{pattern_id}")
            continue
        if row.get("value_interval") != ["0", derivatives["0"].get("bound")]:
            failures.append(f"value_interval:{pattern_id}")
        previous = 0
        for order in range(5):
            bound = derivatives[str(order)]
            power = bound.get("power")
            if (
                not isinstance(power, int)
                or bound.get("bound") != f"10^{power}"
                or bound.get("strictly_contains_arb_ball") is not True
                or not bound.get("arb_log10_ball")
            ):
                failures.append(f"bound:{pattern_id}:{order}")
            if order and isinstance(power, int) and power <= previous:
                failures.append(f"monotone_power:{pattern_id}:{order}")
            if isinstance(power, int):
                previous = power
    required_coverage = (
        "all_53_patterns_covered", "all_468_occurrences_covered",
        "all_234_entries_remain_in_scope", "all_18_groups_remain_in_scope",
    )
    if any(envelope.get(key) is not True for key in required_coverage):
        failures.append("coverage")
    ranges = envelope.get("power_ranges_by_size_and_derivative_order", {})
    expected_ranges = {
        "2": {"0": (235, 238), "1": (295, 298), "2": (355, 359), "3": (415, 419), "4": (475, 480)},
        "3": {"0": (531, 533), "1": (592, 594), "2": (652, 655), "3": (713, 716), "4": (773, 776)},
    }
    for size, orders in expected_ranges.items():
        for order, pair in orders.items():
            row = ranges.get(size, {}).get(order, {})
            if (row.get("minimum_power"), row.get("maximum_power")) != pair:
                failures.append(f"range:{size}:{order}")
    sensitivity = data.get("scale_sensitivity", {}).get("rows", [])
    if [row.get("total_primitive_floor") for row in sensitivity] != [
        "2^-8", "2^-12", "2^-16", "2^-24", "2^-40", "2^-80", "2^-120", "2^-160", "2^-200"
    ]:
        failures.append("sensitivity_floors")
    if [row.get("maximum_value_ceiling_power_by_size", {}).get("3") for row in sensitivity] != [
        13, 24, 35, 56, 100, 208, 317, 425, 533
    ]:
        failures.append("sensitivity_values")
    controls = data.get("independent_controls", {})
    recurrence = controls.get("bessel_derivative_recurrence", {})
    if (
        recurrence.get("orders") != "0..8"
        or len(recurrence.get("rows", [])) != 9
        or recurrence.get("maximum_relative_midpoint_difference", 1) >= 3e-15
    ):
        failures.append("recurrence_control")
    sample = controls.get("k186_sampled_regularizer_range", [])
    if len(sample) != 2 or not (0 < sample[0] < sample[1] < 1):
        failures.append("sample_control")
    required_true = (
        "exact_bessel_derivative_identity_banked", "hermite_genocchi_gap_free_entry_bound_banked",
        "arb_directed_endpoint_evaluation_banked", "all_53_regularizer_value_envelopes_serialized",
        "all_53_primitive_mixed_derivative_envelopes_through_order_four_serialized",
    )
    required_false = (
        "duffy_jacobi_chain_rule_envelopes_serialized", "single_global_core_box_decision_grade",
        "determinant_preserving_positive_radius_core_error_serialized",
        "complete_outward_order_six_total_error_serialized", "accurate_order_six_prefix_released",
        "complete_base_action_column_evaluated", "complete_R_ref_form_dual_residual_serialized",
        "positive_complete_M_orthogonal_complement_or_flux_floor_serialized",
        "scalar_center_left_floor_serialized", "native_K152_interval_emitted",
    )
    if any(release.get(key) is not True for key in required_true):
        failures.append("release_true")
    if any(release.get(key) is not False for key in required_false):
        failures.append("release_false")
    switch = data.get("route_switch", {})
    if "10^533" not in switch.get("reason", "") or "10^776" not in switch.get("reason", ""):
        failures.append("switch_quantities")
    if "cancellation-preserving" not in switch.get("next_exact_input", ""):
        failures.append("next_route")
    if not all(str(value).endswith("_UNCHANGED") for value in data.get("ledger_effect", {}).values()):
        failures.append("ledger")
    if data.get("physical_or_source_selection") is not False:
        failures.append("physical")
    if data.get("Born_prediction_or_confirmation_credit") is not False:
        failures.append("Born")
    if data.get("canon_paper_release_or_public_posture_move") is not False:
        failures.append("public")
    return failures


def exact_checks(data: dict[str, Any]) -> list[tuple[str, bool]]:
    text = ARTIFACT.read_text() if ARTIFACT.exists() else ""
    failures = manifest_failures(data)
    return [
        ("manifest", not failures),
        ("deterministic Arb replay", K189.build() == data),
        ("artifact exists", ARTIFACT.exists()),
        ("solver exists", SOLVER.exists()),
        ("routing notice", "GU-COMPARATOR-ROUTING" in text),
        ("classification", "Classification: INTERNAL_STRUCTURAL_ONLY." in text),
        ("typed objects", "```gu-typed-objects" in text),
        ("Hermite--Genocchi", "Hermite--Genocchi" in text),
        ("Arb backend", "python-flint 0.9.0" in text and "FLINT 3.6.0" in text),
        ("complete census", "53 patterns" in text and "468 occurrences" in text),
        ("global route rejected", "single global" in text and "not decision-grade" in text),
        ("prefix withheld", "accurate order-six prefix remains" in text),
        ("ledger unchanged", "SC-META-53" in text and "remain unchanged" in text),
    ] + [(f"no {failure}", False) for failure in failures]


def first_pattern_key(data: dict[str, Any]) -> str:
    return next(iter(data["complete_pattern_envelopes"]["patterns"]), "")


def first_pattern_row(data: dict[str, Any]) -> dict[str, Any]:
    return data["complete_pattern_envelopes"]["patterns"][first_pattern_key(data)]


def hostile_checks(data: dict[str, Any]) -> list[tuple[str, bool]]:
    mutations = (
        ("wrong_floor", lambda d: d["fixed_control"].__setitem__("primitive_floor", "2^-199")),
        ("wrong_backend", lambda d: d["arb_backend"].__setitem__("python_flint_version", "0.8.0")),
        ("zero_width", lambda d: d["arb_backend"].__setitem__("all_endpoint_values_are_nonzero_width_balls", False)),
        ("drop_theorem", lambda d: d["theorem_certificate"].__setitem__("tensor_hermite_genocchi", "")),
        ("drop_pattern", lambda d: d["complete_pattern_envelopes"]["patterns"].pop(first_pattern_key(d))),
        ("wrong_occurrence", lambda d: first_pattern_row(d).__setitem__("occurrences", 0)),
        ("drop_order", lambda d: first_pattern_row(d)["primitive_mixed_derivative_absolute_bounds"].pop("4")),
        ("wrong_decimal", lambda d: first_pattern_row(d)["primitive_mixed_derivative_absolute_bounds"]["0"].__setitem__("bound", "10^1")),
        ("wrong_range", lambda d: d["complete_pattern_envelopes"]["power_ranges_by_size_and_derivative_order"]["3"]["4"].__setitem__("maximum_power", 775)),
        ("drop_coverage", lambda d: d["complete_pattern_envelopes"].__setitem__("all_468_occurrences_covered", False)),
        ("wrong_sensitivity", lambda d: d["scale_sensitivity"]["rows"][-1]["maximum_value_ceiling_power_by_size"].__setitem__("3", 532)),
        ("weak_control", lambda d: d["independent_controls"]["bessel_derivative_recurrence"].__setitem__("maximum_relative_midpoint_difference", 1.0)),
        ("invent_chain", lambda d: d["release_test"].__setitem__("duffy_jacobi_chain_rule_envelopes_serialized", True)),
        ("invent_decision", lambda d: d["release_test"].__setitem__("single_global_core_box_decision_grade", True)),
        ("invent_core", lambda d: d["release_test"].__setitem__("determinant_preserving_positive_radius_core_error_serialized", True)),
        ("invent_total", lambda d: d["release_test"].__setitem__("complete_outward_order_six_total_error_serialized", True)),
        ("invent_prefix", lambda d: d["release_test"].__setitem__("accurate_order_six_prefix_released", True)),
        ("move_ledger", lambda d: d["ledger_effect"].__setitem__("SC-META-53", "RESOLVED")),
        ("invent_physical", lambda d: d.__setitem__("physical_or_source_selection", True)),
        ("invent_public", lambda d: d.__setitem__("canon_paper_release_or_public_posture_move", True)),
    )
    results = []
    for name, mutate in mutations:
        broken = copy.deepcopy(data)
        mutate(broken)
        results.append((name, bool(manifest_failures(broken))))
    return results


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    data = json.loads(MANIFEST.read_text())
    checks = exact_checks(data)
    failed = [name for name, ok in checks if not ok]
    if failed:
        print(f"FAIL {len(failed)}/{len(checks)}: {', '.join(failed)}")
        return 1
    if args.selftest:
        hostile = hostile_checks(data)
        missed = [name for name, caught in hostile if not caught]
        if missed:
            print(f"HOSTILE FAIL {len(missed)}/{len(hostile)}: {', '.join(missed)}")
            return 1
        print(f"PASS {len(checks)}/{len(checks)}; hostile {len(hostile)}/{len(hostile)} caught")
        return 0
    print(f"PASS {len(checks)}/{len(checks)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
