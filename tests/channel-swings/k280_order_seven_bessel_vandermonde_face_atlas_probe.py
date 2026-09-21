#!/usr/bin/env python3
"""Independent replay and hostile controls for K280."""

from __future__ import annotations

import copy
import importlib.util
import json
import math
from collections import Counter, defaultdict
from decimal import Decimal
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
SOLVER = Path(__file__).with_name("k280_order_seven_bessel_vandermonde_face_atlas.py")
MANIFEST = ROOT / "lab/process/k280-order-seven-bessel-vandermonde-face-atlas.json"
ARTIFACT = (
    ROOT
    / "explorations/conditional-build/k280-order-seven-bessel-vandermonde-face-atlas-2026-09-21.md"
)
EXPECTED_SIZE_HISTOGRAM = {"1": 564, "2": 720, "3": 252, "4": 24}
EXPECTED_PATTERNS_BY_SIZE = {"2": 72, "3": 25, "4": 1}


def load_solver():
    spec = importlib.util.spec_from_file_location("k280_solver", SOLVER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SOLVER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K280 = load_solver()


def expected_parity(values: list[int]) -> int:
    inversions = sum(
        values[i] > values[j]
        for i in range(len(values))
        for j in range(i + 1, len(values))
    )
    return -1 if inversions % 2 else 1


def independent_source_counts() -> tuple[int, int, int]:
    terms = K280.order_terms()
    groups: dict[tuple[int, str], int] = defaultdict(int)
    for term in terms:
        groups[K280.group_key(term)] += 1
    entries = sum(count * (count + 1) // 2 for count in groups.values())
    return len(terms), len(groups), entries


def manifest_failures(data: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    fixed = data.get("fixed_control", {})
    inventory = data.get("complete_factorization_inventory", {})
    certificate = data.get("factorization_certificate", {})
    controls = data.get("independent_controls", {})
    reuse = data.get("predecessor_reuse", {})
    release = data.get("release_test", {})
    factor_patterns = data.get("factor_patterns", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY":
        failures.append("classification")
    if independent_source_counts() != (96, 16, 408):
        failures.append("source_counts")
    if (
        fixed.get("source_paths"),
        fixed.get("source_groups"),
        fixed.get("source_gram_entries"),
        fixed.get("primitive_time_variables"),
    ) != (96, 16, 408, 16):
        failures.append("fixed")
    if inventory.get("size_histogram") != EXPECTED_SIZE_HISTOGRAM:
        failures.append("size_histogram")
    if inventory.get("unique_patterns_by_size") != EXPECTED_PATTERNS_BY_SIZE:
        failures.append("patterns_by_size")
    if (
        inventory.get("species_determinant_occurrences"),
        inventory.get("nontrivial_size_two_through_four_occurrences"),
        inventory.get("unique_nontrivial_factor_patterns"),
    ) != (1560, 996, 98):
        failures.append("census")
    entries = inventory.get("entries", [])
    if len(entries) != 408:
        failures.append("entries")
    observed_histogram: Counter[int] = Counter()
    for entry_index, entry in enumerate(entries):
        factor_sign = 1
        for factor_index, factor in enumerate(entry.get("species_factors", [])):
            label = f"{entry_index}:{factor_index}"
            size = factor.get("size")
            observed_histogram[size] += 1
            record = factor_patterns.get(factor.get("pattern"), {})
            left = record.get("left_canonical_positions", [])
            right = record.get("right_canonical_positions", [])
            left_original = record.get("left_original_positions", [])
            right_original = record.get("right_original_positions", [])
            if size not in (1, 2, 3, 4) or len(left) != size or len(right) != size:
                failures.append(f"shape:{label}")
                continue
            if left != sorted(left) or right != sorted(right):
                failures.append(f"order:{label}")
            left_sign = expected_parity(left_original)
            right_sign = expected_parity(right_original)
            if record.get("left_permutation_sign") != left_sign:
                failures.append(f"left_sign:{label}")
            if record.get("right_permutation_sign") != right_sign:
                failures.append(f"right_sign:{label}")
            if factor.get("determinant_sign") != left_sign * right_sign:
                failures.append(f"det_sign:{label}")
            factor_sign *= factor.get("determinant_sign", 0)
            expected_gaps = size * (size - 1) // 2
            if len(record.get("left_vandermonde_gaps", [])) != expected_gaps:
                failures.append(f"left_gaps:{label}")
            if len(record.get("right_vandermonde_gaps", [])) != expected_gaps:
                failures.append(f"right_gaps:{label}")
            if len(record.get("cauchy_denominator_supports", [])) != size * size:
                failures.append(f"denominators:{label}")
            for row in record.get("left_vandermonde_gaps", []):
                first, second = row["positions"]
                if row.get("primitive_support") != [f"s{i}" for i in range(first, second)]:
                    failures.append(f"left_support:{label}")
            for row in record.get("right_vandermonde_gaps", []):
                first, second = row["positions"]
                if row.get("primitive_support") != [f"v{i}" for i in range(first, second)]:
                    failures.append(f"right_support:{label}")
        if entry.get("entry_integrand_sign") != entry.get("coefficient_product") * factor_sign:
            failures.append(f"entry_sign:{entry_index}")
    if {str(key): value for key, value in sorted(observed_histogram.items())} != EXPECTED_SIZE_HISTOGRAM:
        failures.append("entry_histogram")
    if inventory.get("all_sizes_at_most_four") is not True:
        failures.append("size_ceiling")
    if inventory.get("size_four_present") is not True:
        failures.append("size_four")
    if inventory.get("every_nontrivial_factor_has_two_vandermonde_families") is not True:
        failures.append("vandermonde_families")
    if (
        reuse.get("K186_order_six_patterns"),
        reuse.get("K280_order_seven_patterns"),
        reuse.get("exact_pattern_overlap"),
        reuse.get("exact_overlap_by_size"),
        reuse.get("new_patterns_by_size"),
    ) != (53, 98, 52, {"2": 45, "3": 7, "4": 0}, {"2": 27, "3": 18, "4": 1}):
        failures.append("predecessor_reuse")
    if reuse.get("K192_certified_union_reusable_for_identical_patterns") is not True:
        failures.append("reuse_domain")
    if reuse.get("K192_arbitrary_gap_ratio_domain_covered") is not False:
        failures.append("reuse_gap_ceiling")
    if reuse.get("K192_noncoalescent_face_atlas_serialized") is not False:
        failures.append("reuse_face_ceiling")
    if any(not row.get("exact_equality") for row in certificate.get("exact_cauchy_controls", [])):
        failures.append("exact_cauchy")
    if len(certificate.get("exact_cauchy_controls", [])) != 4:
        failures.append("exact_cauchy_count")
    divided = controls.get("mixed_divided_difference", {})
    if (
        divided.get("tested_pattern_profiles"),
        divided.get("size_four_profiles"),
        divided.get("all_positive"),
    ) != (196, 2, True):
        failures.append("divided_counts")
    if Decimal(divided.get("maximum_relative_difference", "1")) >= Decimal("1e-150"):
        failures.append("divided_error")
    stress = controls.get("stress", {})
    if stress.get("all_positive") is not True or len(stress.get("rows", [])) != 6:
        failures.append("stress")
    if stress.get("size_four_near_face_and_small_radius_controls") != 2:
        failures.append("stress_size_four")
    if Decimal(stress.get("maximum_relative_difference", "1")) >= Decimal("1e-200"):
        failures.append("stress_error")
    required_true = (
        "all_408_order_seven_gram_entries_replayed",
        "all_size_one_through_four_determinants_factored",
        "canonical_signs_serialized",
        "primitive_vandermonde_gap_supports_serialized",
        "positive_regularizers_defined_through_size_four",
        "coalescent_extension_defined_through_size_four",
        "all_exact_cauchy_controls_pass",
    )
    required_false = (
        "outward_R2_R3_R4_intervals_serialized",
        "duffy_derivative_envelopes_serialized",
        "determinant_valued_cubature_error_serialized",
        "coefficient_complete_base_action_column_evaluated",
        "complete_R_ref_form_dual_residual_serialized",
        "positive_complete_M_orthogonal_complement_or_flux_floor_serialized",
        "native_K152_interval_emitted",
    )
    if any(release.get(key) is not True for key in required_true):
        failures.append("release_true")
    if any(release.get(key) is not False for key in required_false):
        failures.append("release_false")
    if not all(str(value).endswith("_UNCHANGED") for value in data.get("ledger_effect", {}).values()):
        failures.append("ledger")
    return failures


def hostile_controls(data: dict[str, Any]) -> dict[str, bool]:
    mutations = (
        ("drop_entry", lambda d: d["complete_factorization_inventory"]["entries"].pop()),
        ("break_size_four_count", lambda d: d["complete_factorization_inventory"]["size_histogram"].__setitem__("4", 23)),
        ("erase_size_four_pattern", lambda d: d["complete_factorization_inventory"]["unique_patterns_by_size"].__setitem__("4", 0)),
        ("break_entry_sign", lambda d: d["complete_factorization_inventory"]["entries"][0].__setitem__("entry_integrand_sign", -1)),
        ("break_gap_support", lambda d: d["factor_patterns"][next(iter(d["factor_patterns"]))].__setitem__("cauchy_denominator_supports", [])),
        ("break_cauchy", lambda d: d["factorization_certificate"]["exact_cauchy_controls"][3].__setitem__("exact_equality", False)),
        ("break_divided", lambda d: d["independent_controls"]["mixed_divided_difference"].__setitem__("maximum_relative_difference", "1")),
        ("break_stress", lambda d: d["independent_controls"]["stress"].__setitem__("all_positive", False)),
        ("invent_predecessor_coverage", lambda d: d["predecessor_reuse"].__setitem__("K192_arbitrary_gap_ratio_domain_covered", True)),
        ("invent_interval", lambda d: d["release_test"].__setitem__("outward_R2_R3_R4_intervals_serialized", True)),
        ("invent_cubature", lambda d: d["release_test"].__setitem__("determinant_valued_cubature_error_serialized", True)),
        ("invent_action", lambda d: d["release_test"].__setitem__("coefficient_complete_base_action_column_evaluated", True)),
        ("move_ledger", lambda d: d["ledger_effect"].__setitem__("SC-META-53", "RESOLVED")),
    )
    results = {}
    for name, mutate in mutations:
        broken = copy.deepcopy(data)
        mutate(broken)
        results[name] = bool(manifest_failures(broken))
    return results


def main() -> int:
    data = json.loads(MANIFEST.read_text())
    text = ARTIFACT.read_text() if ARTIFACT.exists() else ""
    failures = manifest_failures(data)
    hostile = hostile_controls(data)
    checks = {
        "manifest_replay": not failures,
        "deterministic_producer_replay": K280.build() == data,
        "independent_source_census": independent_source_counts() == (96, 16, 408),
        "artifact_exists": ARTIFACT.exists(),
        "routing_and_typed_objects": "GU-COMPARATOR-ROUTING" in text and "```gu-typed-objects" in text,
        "size_four_result_reported": "size-four" in text and "24" in text,
        "claim_ceiling_preserved": "not outward intervals" in text and "action column" in text,
        "all_hostile_mutations_rejected": all(hostile.values()),
    }
    payload = {
        "schema_version": "1.0",
        "producer_result_id": data.get("result_id"),
        "checks": checks,
        "manifest_failures": failures,
        "hostile_controls": hostile,
        "pass_count": sum(checks.values()),
        "check_count": len(checks),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
