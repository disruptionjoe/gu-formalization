#!/usr/bin/env python3
"""Exact/reporting and hostile controls for the K186 factorization certificate."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
import math
from decimal import Decimal, localcontext
from pathlib import Path
from typing import Any

from scipy.special import k1


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k186-order-six-bessel-vandermonde-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k186-order-six-bessel-vandermonde-wave-2026-09-09.md"
SOLVER = ROOT / "tests/channel-swings/k186_order_six_bessel_vandermonde.py"


def load_solver():
    spec = importlib.util.spec_from_file_location("k186_solver", SOLVER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SOLVER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K186 = load_solver()


def expected_parity(values: list[int]) -> int:
    inversions = sum(
        values[i] > values[j]
        for i in range(len(values))
        for j in range(i + 1, len(values))
    )
    return -1 if inversions % 2 else 1


def manifest_failures(data: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    fixed = data.get("fixed_control", {})
    inventory = data.get("complete_factorization_inventory", {})
    certificate = data.get("factorization_certificate", {})
    controls = data.get("independent_controls", {})
    release = data.get("release_test", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY":
        failures.append("classification")
    if (
        fixed.get("source_entries"),
        fixed.get("primitive_time_variables"),
        fixed.get("radial_cutoff"),
        fixed.get("face_strip_floor"),
    ) != (234, 14, "1/4", "2^-180"):
        failures.append("fixed")
    if inventory.get("size_histogram") != {"1": 404, "2": 404, "3": 64}:
        failures.append("size_histogram")
    if (
        inventory.get("species_determinant_occurrences"),
        inventory.get("nontrivial_size_two_or_three_occurrences"),
        inventory.get("unique_nontrivial_factor_patterns"),
    ) != (872, 468, 53):
        failures.append("census")
    entries = inventory.get("entries", [])
    if len(entries) != 234:
        failures.append("entries")
    for entry_index, entry in enumerate(entries):
        factor_sign = 1
        for factor_index, factor in enumerate(entry.get("species_factors", [])):
            size = factor.get("size")
            left = factor.get("left_canonical_positions", [])
            right = factor.get("right_canonical_positions", [])
            left_original = factor.get("left_original_positions", [])
            right_original = factor.get("right_original_positions", [])
            label = f"{entry_index}:{factor_index}"
            if size not in (1, 2, 3) or len(left) != size or len(right) != size:
                failures.append(f"shape:{label}")
                continue
            if left != sorted(left) or right != sorted(right):
                failures.append(f"order:{label}")
            left_sign = expected_parity(left_original)
            right_sign = expected_parity(right_original)
            if factor.get("left_permutation_sign") != left_sign:
                failures.append(f"left_sign:{label}")
            if factor.get("right_permutation_sign") != right_sign:
                failures.append(f"right_sign:{label}")
            if factor.get("determinant_sign") != left_sign * right_sign:
                failures.append(f"det_sign:{label}")
            factor_sign *= factor.get("determinant_sign", 0)
            expected_gaps = size * (size - 1) // 2
            if len(factor.get("left_vandermonde_gaps", [])) != expected_gaps:
                failures.append(f"left_gaps:{label}")
            if len(factor.get("right_vandermonde_gaps", [])) != expected_gaps:
                failures.append(f"right_gaps:{label}")
            if len(factor.get("cauchy_denominator_supports", [])) != size * size:
                failures.append(f"denominators:{label}")
            for row in factor.get("left_vandermonde_gaps", []):
                first, second = row["positions"]
                if row.get("primitive_support") != [f"s{i}" for i in range(first, second)]:
                    failures.append(f"left_support:{label}")
            for row in factor.get("right_vandermonde_gaps", []):
                first, second = row["positions"]
                if row.get("primitive_support") != [f"v{i}" for i in range(first, second)]:
                    failures.append(f"right_support:{label}")
        if entry.get("entry_integrand_sign") != entry.get("coefficient_product") * factor_sign:
            failures.append(f"entry_sign:{entry_index}")
    if inventory.get("all_sizes_at_most_three") is not True:
        failures.append("size_ceiling")
    if inventory.get("every_nontrivial_factor_has_two_vandermonde_families") is not True:
        failures.append("vandermonde_families")
    required_certificate = (
        "cauchy_identity",
        "bessel_identity",
        "strict_positivity",
        "coalescent_extension",
        "small_radius_limit",
    )
    if any(not certificate.get(key) for key in required_certificate):
        failures.append("certificate")
    all_entry = controls.get("all_entry_double_precision", {})
    if (
        all_entry.get("tested_nontrivial_determinants"),
        all_entry.get("canonical_determinants_positive"),
        all_entry.get("original_sign_matches_record"),
    ) != (468, 468, 468):
        failures.append("all_entry_control")
    divided = controls.get("mixed_divided_difference", {})
    if divided.get("tested_pattern_profiles") != 159:
        failures.append("divided_count")
    if divided.get("direct_vs_mixed_divided_difference_max_relative_error", 1) >= 1e-24:
        failures.append("divided_error")
    stress = controls.get("stress", {})
    if stress.get("all_positive") is not True or len(stress.get("rows", [])) != 4:
        failures.append("stress")
    if stress.get("maximum_relative_difference", 1) >= 1e-150:
        failures.append("stress_error")
    required_true = (
        "all_234_time_gram_entries_replayed",
        "all_size_two_and_three_determinants_factored",
        "canonical_signs_serialized",
        "primitive_vandermonde_gap_supports_serialized",
        "positive_regularizer_defined",
        "coalescent_extension_defined",
        "bounded_compact_core_regularizer_proved_qualitatively",
    )
    required_false = (
        "outward_regularizer_interval_serialized",
        "determinant_preserving_compact_core_quadrature_error_serialized",
        "accurate_order_six_prefix_released",
        "complete_base_action_column_evaluated",
        "complete_R_ref_form_dual_residual_serialized",
        "positive_complete_M_orthogonal_complement_or_flux_floor_serialized",
        "scalar_center_left_floor_serialized",
        "native_K152_interval_emitted",
    )
    if any(release.get(key) is not True for key in required_true):
        failures.append("release_true")
    if any(release.get(key) is not False for key in required_false):
        failures.append("release_false")
    if not all(str(value).endswith("_UNCHANGED") for value in data.get("ledger_effect", {}).values()):
        failures.append("ledger")
    if data.get("physical_or_source_selection") is not False:
        failures.append("physical")
    if data.get("Born_prediction_or_confirmation_credit") is not False:
        failures.append("Born")
    if data.get("canon_paper_release_or_public_posture_move") is not False:
        failures.append("public")
    return failures


def analytic_controls(data: dict[str, Any]) -> list[tuple[str, bool]]:
    checks: list[tuple[str, bool]] = []
    for value in ("1e-8", "1e-4", "1e-2", "0.25"):
        decimal_value = Decimal(value)
        evaluated = float(K186.decimal_bessel_k1(decimal_value, 90))
        reference = float(k1(float(decimal_value)))
        checks.append((f"K1 series {value}", abs(evaluated - reference) / reference < 2e-15))
    patterns = data["unique_patterns"]
    with localcontext() as context:
        context.prec = 100
        s, v = K186.deterministic_profile(23, Decimal("0.2"))
        maximum = Decimal(0)
        for key, record in patterns.items():
            left = K186.times_for(record["left_canonical_positions"], s)
            right = K186.times_for(record["right_canonical_positions"], v)
            direct = K186.determinant(
                [[Decimal(2) / (x + y) for y in right] for x in left]
            )
            factored = K186.cauchy_determinant(left, right)
            maximum = max(maximum, abs(direct - factored) / abs(direct))
        checks.append(("all 53 Cauchy identities", maximum < Decimal("1e-85")))
    checks.append(("synthetic odd row parity", K186.parity((3, 1, 2)) == 1))
    checks.append(("synthetic odd transposition", K186.parity((2, 1, 3)) == -1))
    return checks


def exact_checks(data: dict[str, Any]) -> list[tuple[str, bool]]:
    text = ARTIFACT.read_text() if ARTIFACT.exists() else ""
    failures = manifest_failures(data)
    return [
        ("manifest", not failures),
        ("deterministic manifest replay", K186.build() == data),
        ("artifact exists", ARTIFACT.exists()),
        ("solver exists", SOLVER.exists()),
        ("routing notice", "GU-COMPARATOR-ROUTING" in text),
        ("classification", "Classification: INTERNAL_STRUCTURAL_ONLY." in text),
        ("typed objects", "```gu-typed-objects" in text),
        ("234 entries", "234 time-Gram entries" in text),
        ("468 determinants", "468 nontrivial" in text),
        ("Cauchy factor", "Cauchy--Vandermonde" in text),
        ("total positivity", "Andreief" in text and "strictly positive" in text),
        ("proof/control split", "not outward intervals" in text),
        ("compact error open", "compact-core quadrature error remains open" in text),
        ("ledger unchanged", "SC-META-53" in text and "remain unchanged" in text),
    ] + analytic_controls(data) + [(f"no {failure}", False) for failure in failures]


def hostile_checks(data: dict[str, Any]) -> list[tuple[str, bool]]:
    mutations = (
        ("drop_entry", lambda d: d["complete_factorization_inventory"]["entries"].pop()),
        ("break_histogram", lambda d: d["complete_factorization_inventory"]["size_histogram"].__setitem__("3", 63)),
        ("break_census", lambda d: d["complete_factorization_inventory"].__setitem__("nontrivial_size_two_or_three_occurrences", 467)),
        ("break_order", lambda d: d["complete_factorization_inventory"]["entries"][0]["species_factors"][2].__setitem__("left_canonical_positions", [6, 4])),
        ("break_sign", lambda d: d["complete_factorization_inventory"]["entries"][0]["species_factors"][2].__setitem__("determinant_sign", -1)),
        ("break_gap", lambda d: d["complete_factorization_inventory"]["entries"][0]["species_factors"][2].__setitem__("left_vandermonde_gaps", [])),
        ("break_support", lambda d: d["complete_factorization_inventory"]["entries"][0]["species_factors"][2]["left_vandermonde_gaps"][0].__setitem__("primitive_support", ["s1"])),
        ("break_denominator", lambda d: d["complete_factorization_inventory"]["entries"][0]["species_factors"][2].__setitem__("cauchy_denominator_supports", [])),
        ("break_certificate", lambda d: d["factorization_certificate"].__setitem__("strict_positivity", "")),
        ("break_control", lambda d: d["independent_controls"]["all_entry_double_precision"].__setitem__("canonical_determinants_positive", 467)),
        ("break_divided", lambda d: d["independent_controls"]["mixed_divided_difference"].__setitem__("direct_vs_mixed_divided_difference_max_relative_error", 1.0)),
        ("break_stress", lambda d: d["independent_controls"]["stress"].__setitem__("all_positive", False)),
        ("invent_interval", lambda d: d["release_test"].__setitem__("outward_regularizer_interval_serialized", True)),
        ("invent_core", lambda d: d["release_test"].__setitem__("determinant_preserving_compact_core_quadrature_error_serialized", True)),
        ("invent_prefix", lambda d: d["release_test"].__setitem__("accurate_order_six_prefix_released", True)),
        ("invent_action", lambda d: d["release_test"].__setitem__("complete_base_action_column_evaluated", True)),
        ("move_ledger", lambda d: d["ledger_effect"].__setitem__("SC-META-53", "RESOLVED")),
        ("invent_physical", lambda d: d.__setitem__("physical_or_source_selection", True)),
        ("invent_Born", lambda d: d.__setitem__("Born_prediction_or_confirmation_credit", True)),
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
