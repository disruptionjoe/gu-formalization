#!/usr/bin/env python3
"""Exact/reporting and hostile controls for the K187 radial-log certificate."""

from __future__ import annotations

import argparse
import copy
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k187-order-six-radial-log-endpoint-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k187-order-six-radial-log-endpoint-wave-2026-09-09.md"
SOLVER = ROOT / "tests/channel-swings/k187_order_six_radial_log_endpoint.py"
K186_MANIFEST = ROOT / "lab/process/k186-order-six-bessel-vandermonde-wave.json"


def as_fraction(row: dict[str, Any]) -> Fraction:
    return Fraction(int(row["numerator"]), int(row["denominator"]))


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def pattern_key(record: dict[str, Any]) -> str:
    return (
        f"m{record['size']}|"
        f"L{','.join(map(str, record['left_canonical_positions']))}|"
        f"R{','.join(map(str, record['right_canonical_positions']))}"
    )


def recompute_coefficient(record: dict[str, Any]) -> Fraction:
    primitives = [Fraction(1, 14)] * 14
    times = [sum(primitives[position - 1 : 7], Fraction(0)) for position in record["left_canonical_positions"]]
    other_times = [sum(primitives[7 + position - 1 :], Fraction(0)) for position in record["right_canonical_positions"]]
    cauchy = [[Fraction(2, 1) / (left + right) for right in other_times] for left in times]
    perturbation = [[left + right for right in other_times] for left in times]
    derivative = Fraction(0)
    for row in range(len(cauchy)):
        for column in range(len(cauchy)):
            submatrix = [
                values[:column] + values[column + 1 :]
                for index, values in enumerate(cauchy)
                if index != row
            ]
            derivative += ((-1) ** (row + column)) * determinant(submatrix) * perturbation[row][column]
    return derivative / determinant(cauchy)


def manifest_failures(data: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    fixed = data.get("fixed_control", {})
    cert = data.get("radial_log_certificate", {})
    face = data.get("coalescent_face_audit", {})
    controls = data.get("independent_controls", {})
    release = data.get("release_test", {})
    route = data.get("replacement_route", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY": failures.append("classification")
    if (fixed.get("source_patterns"), fixed.get("source_nontrivial_occurrences"), fixed.get("source_time_gram_entries")) != (53, 468, 234): failures.append("fixed_census")
    if fixed.get("angular_profile_inside_face_stripped_core") is not True: failures.append("profile_domain")
    patterns = cert.get("patterns", {})
    if len(patterns) != 53: failures.append("pattern_count")
    source = json.loads(K186_MANIFEST.read_text())
    source_patterns = source.get("unique_patterns", {})
    expected_occurrences: dict[str, int] = {}
    for entry in source.get("complete_factorization_inventory", {}).get("entries", []):
        for factor in entry.get("species_factors", []):
            if factor.get("size", 0) > 1:
                key = pattern_key(factor)
                expected_occurrences[key] = expected_occurrences.get(key, 0) + 1
    if set(patterns) != set(source_patterns): failures.append("pattern_ids")
    coefficients = []
    occurrences = 0
    for pattern_id, row in patterns.items():
        value = as_fraction(row.get("equal_angular_profile_coefficient", {}))
        coefficients.append(value)
        occurrences += int(row.get("occurrences", 0))
        if value <= 0: failures.append(f"coefficient:{pattern_id}")
        if row.get("size") not in (2, 3): failures.append(f"size:{pattern_id}")
        if pattern_id in source_patterns and value != recompute_coefficient(source_patterns[pattern_id]): failures.append(f"coefficient_replay:{pattern_id}")
        if row.get("occurrences") != expected_occurrences.get(pattern_id): failures.append(f"occurrence_replay:{pattern_id}")
    if occurrences != 468: failures.append("occurrences")
    if len(set(coefficients)) != 10 or min(coefficients, default=0) != Fraction(8, 49) or max(coefficients, default=0) != Fraction(169, 98): failures.append("coefficient_range")
    if as_fraction(cert.get("coefficient_range", {}).get("minimum", {})) != Fraction(8, 49) or as_fraction(cert.get("coefficient_range", {}).get("maximum", {})) != Fraction(169, 98): failures.append("reported_range")
    if cert.get("all_53_profile_coefficients_exact") is not True or cert.get("all_53_profile_coefficients_positive") is not True or cert.get("distinct_exact_coefficients") != 10: failures.append("certificate_summary")
    expansion = cert.get("regularizer_expansion", "")
    if "rho^2" not in expansion or "log(rho)" not in expansion or "rho^4*log(rho)^2" not in expansion or "unbounded" not in cert.get("second_derivative_consequence", ""): failures.append("theorem")
    if face.get("k186_time_coalescence_extension_preserved") is not True or face.get("radial_endpoint_is_a_distinct_boundary") is not True: failures.append("face_split")
    if face.get("all_angular_coefficient_sign_claimed") is not False or face.get("uniform_mixed_duffy_derivative_enclosure_claimed") is not False: failures.append("scope_guard")
    maxima = controls.get("max_absolute_error_by_radius", {})
    try:
        values = [DecimalLike(maxima[key]) for key in ("2^-20", "2^-40", "2^-80")]
    except Exception:
        failures.append("control_shape")
        values = []
    if values and not (values[2] < values[1] < values[0]): failures.append("control_convergence")
    if controls.get("error_strictly_decreases_at_each_radius") is not True or len(controls.get("rows", [])) != 159: failures.append("controls")
    required_true = (
        "all_53_factor_patterns_censused", "all_468_nontrivial_occurrences_propagated",
        "all_234_time_gram_entries_remain_in_scope", "nonzero_rho_squared_log_rho_coefficient_proved",
        "k186_continuity_and_positive_coalescent_extension_preserved",
    )
    required_false = (
        "bounded_second_radial_derivative_on_zero_inclusive_core",
        "ordinary_smooth_endpoint_jacobi_remainder_applicable",
        "outward_log_aware_or_split_domain_total_error_serialized",
        "accurate_order_six_prefix_released", "complete_base_action_column_evaluated",
        "complete_R_ref_form_dual_residual_serialized",
        "positive_complete_M_orthogonal_complement_or_flux_floor_serialized",
        "scalar_center_left_floor_serialized", "native_K152_interval_emitted",
    )
    if any(release.get(key) is not True for key in required_true): failures.append("release_true")
    if any(release.get(key) is not False for key in required_false): failures.append("release_false")
    if "log-weight" not in route.get("next_exact_input", "") or "small-rho" not in route.get("release_condition", ""): failures.append("replacement_route")
    if not all(str(value).endswith("_UNCHANGED") for value in data.get("ledger_effect", {}).values()): failures.append("ledger")
    if data.get("physical_or_source_selection") is not False: failures.append("physical")
    if data.get("Born_prediction_or_confirmation_credit") is not False: failures.append("Born")
    if data.get("canon_paper_release_or_public_posture_move") is not False: failures.append("public")
    return failures


def DecimalLike(value: Any):
    from decimal import Decimal

    return Decimal(str(value))


def exact_checks(data: dict[str, Any]) -> list[tuple[str, bool]]:
    text = ARTIFACT.read_text() if ARTIFACT.exists() else ""
    failures = manifest_failures(data)
    return [
        ("manifest", not failures),
        ("artifact exists", ARTIFACT.exists()),
        ("solver exists", SOLVER.exists()),
        ("routing notice", "GU-COMPARATOR-ROUTING" in text),
        ("classification", "Classification: INTERNAL_STRUCTURAL_ONLY." in text),
        ("typed objects", "```gu-typed-objects" in text),
        ("53 patterns", "53 K186 patterns" in text),
        ("468 occurrences", "468 nontrivial" in text),
        ("log term", "rho^2 log(rho)" in text),
        ("C2 obstruction", "not C^2" in text),
        ("coalescent preserved", "coalescent" in text and "preserved" in text),
        ("prefix withheld", "accurate order-six prefix remains" in text),
        ("ledger unchanged", "SC-META-53" in text and "remain unchanged" in text),
    ] + [(f"no {failure}", False) for failure in failures]


def hostile_checks(data: dict[str, Any]) -> list[tuple[str, bool]]:
    mutations = (
        ("drop_pattern", lambda d: d["radial_log_certificate"]["patterns"].pop(next(iter(d["radial_log_certificate"]["patterns"]), None))),
        ("drop_occurrence", lambda d: next(iter(d["radial_log_certificate"]["patterns"].values()), None).__setitem__("occurrences", 0)),
        ("zero_coefficient", lambda d: next(iter(d["radial_log_certificate"]["patterns"].values()), None)["equal_angular_profile_coefficient"].__setitem__("numerator", 0)),
        ("wrong_size", lambda d: next(iter(d["radial_log_certificate"]["patterns"].values()), None).__setitem__("size", 4)),
        ("wrong_min", lambda d: d["radial_log_certificate"]["coefficient_range"]["minimum"].__setitem__("numerator", 9)),
        ("invent_all_angular", lambda d: d["coalescent_face_audit"].__setitem__("all_angular_coefficient_sign_claimed", True)),
        ("invent_uniform_derivative", lambda d: d["coalescent_face_audit"].__setitem__("uniform_mixed_duffy_derivative_enclosure_claimed", True)),
        ("reverse_controls", lambda d: d["independent_controls"]["max_absolute_error_by_radius"].__setitem__("2^-80", "9")),
        ("invent_C2", lambda d: d["release_test"].__setitem__("bounded_second_radial_derivative_on_zero_inclusive_core", True)),
        ("invent_jacobi", lambda d: d["release_test"].__setitem__("ordinary_smooth_endpoint_jacobi_remainder_applicable", True)),
        ("invent_total_error", lambda d: d["release_test"].__setitem__("outward_log_aware_or_split_domain_total_error_serialized", True)),
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
