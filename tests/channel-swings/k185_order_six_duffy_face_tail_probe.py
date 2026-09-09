#!/usr/bin/env python3
"""Exact/reporting and hostile controls for the K185 Duffy certificate."""

from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k185-order-six-duffy-face-tail-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k185-order-six-duffy-face-tail-wave-2026-09-09.md"
SOLVER = ROOT / "tests/channel-swings/k185_order_six_duffy_face_tail.py"


def fraction(row: dict[str, Any]) -> Fraction:
    return Fraction(int(row["numerator"]), int(row["denominator"]))


def hall_bound(masks: list[int]) -> Fraction:
    result = Fraction(0)
    for subset in range(1, 1 << len(masks)):
        union = 0
        count = 0
        for index, mask in enumerate(masks):
            if subset & (1 << index):
                union |= mask
                count += 1
        result = max(result, Fraction(count, union.bit_count()))
    return result


def allocation_failures(catalog: dict[str, Any]) -> list[str]:
    failures = []
    for allocation_id, row in catalog.items():
        masks = [int(value, 16) for value in row.get("support_masks_hex", "").split(",") if value]
        weights = []
        for factor in row.get("weights", "").split(";"):
            entries = []
            for encoded in factor.split(","):
                if not encoded:
                    continue
                variable, value = encoded.split(":", 1)
                entries.append((int(variable), Fraction(value)))
            weights.append(entries)
        encoded_loads = [Fraction(value) for value in row.get("loads", "").split(",") if value]
        if len(masks) != 8 or len(weights) != 8 or len(encoded_loads) != 14:
            failures.append(f"shape:{allocation_id}")
            continue
        loads = [Fraction(0) for _ in range(14)]
        for factor, entries in enumerate(weights):
            total = Fraction(0)
            for variable, value in entries:
                if not (0 <= variable < 14) or not (masks[factor] & (1 << variable)):
                    failures.append(f"support:{allocation_id}")
                if value <= 0:
                    failures.append(f"weight:{allocation_id}")
                total += value
                loads[variable] += value
            if total != 1:
                failures.append(f"factor_sum:{allocation_id}")
        expected_loads = encoded_loads
        if loads != expected_loads:
            failures.append(f"loads:{allocation_id}")
        maximum = max(loads)
        if maximum >= 1 or sum(loads) != 8:
            failures.append(f"integrability:{allocation_id}")
        if Fraction(row.get("maximum_load", "0")) != maximum:
            failures.append(f"maximum:{allocation_id}")
        if hall_bound(masks) != maximum:
            failures.append(f"hall:{allocation_id}")
    return failures


def manifest_failures(data: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    fixed = data.get("fixed_control", {})
    graph = data.get("complete_face_hypergraph", {})
    certificate = data.get("exact_allocation_certificate", {})
    radial = data.get("radial_duffy_certificate", {})
    groups = data.get("groups", {})
    controls = data.get("independent_controls", {})
    release = data.get("release_test", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY": failures.append("classification")
    if (fixed.get("source_entries"), fixed.get("bessel_factors_per_term"), fixed.get("primitive_time_variables"), fixed.get("chart_shift")) != (234, 8, 14, 256): failures.append("fixed")
    entries = graph.get("entries", [])
    terms = [term for entry in entries for term in entry.get("terms", [])]
    if (graph.get("gram_entries"), graph.get("leibniz_terms"), len(entries), len(terms)) != (234, 1864, 234, 1864): failures.append("census")
    term_ids = [term.get("term_id") for term in terms]
    if len(term_ids) != len(set(term_ids)): failures.append("term_ids")
    catalog = certificate.get("allocation_catalog", {})
    raw = json.dumps(catalog, separators=(",", ":"), sort_keys=True).encode()
    if hashlib.sha256(raw).hexdigest() != certificate.get("allocation_catalog_sha256"): failures.append("catalog_digest")
    if any(term.get("allocation_id") not in catalog for term in terms): failures.append("allocation_refs")
    failures.extend(allocation_failures(catalog))
    hist: dict[str, int] = {}
    for term in terms:
        if term.get("allocation_id") not in catalog:
            continue
        maximum = Fraction(catalog[term["allocation_id"]]["maximum_load"])
        key = f"{maximum.numerator}/{maximum.denominator}"
        hist[key] = hist.get(key, 0) + 1
    if hist != certificate.get("maximum_load_histogram"): failures.append("histogram")
    if certificate.get("worst_maximum_load") != "2/3" or certificate.get("minimum_dirichlet_parameter") != "1/3": failures.append("worst_load")
    if any(certificate.get(key) is not True for key in ("all_denominator_weights_sum_to_one", "all_variable_loads_strictly_below_one", "all_allocations_attain_exact_hall_lower_bound")): failures.append("allocation_summary")
    if radial.get("radial_shape") != 6 or radial.get("all_beta_at_least_one_third") is not True or radial.get("determinants_remain_unexpanded_in_numerical_core") is not True: failures.append("radial")
    expected_per_term = Fraction(27, 8) ** 14 / Fraction(3**8 * 256**6)
    expected_tail = Fraction(3, 8) ** 64 * sum(Fraction(64**k, math.factorial(k)) for k in range(6))
    expected_face = Fraction(2688, 2**60)
    if len(groups) != 18: failures.append("group_count")
    for group_id, row in groups.items():
        weighted_count = row.get("weighted_leibniz_term_count", 0)
        bounds = row.get("proof_safe_bounds", {})
        if fraction(bounds.get("per_leibniz_term_global_ceiling", {})) != expected_per_term: failures.append(f"per_term:{group_id}")
        if fraction(bounds.get("whole_group_global_ceiling", {})) != weighted_count * expected_per_term: failures.append(f"global:{group_id}")
        if fraction(bounds.get("rho_greater_than_one_quarter_fraction_ceiling", {})) != expected_tail: failures.append(f"tail_fraction:{group_id}")
        if fraction(bounds.get("any_simplex_coordinate_below_2^-180_fraction_ceiling", {})) != expected_face: failures.append(f"face_fraction:{group_id}")
        if fraction(bounds.get("rho_greater_than_one_quarter_group_ceiling", {})) != weighted_count * expected_per_term * expected_tail: failures.append(f"tail:{group_id}")
        if fraction(bounds.get("any_simplex_coordinate_below_2^-180_group_ceiling", {})) != weighted_count * expected_per_term * expected_face: failures.append(f"face:{group_id}")
        if not 0 < row.get("gamma_formula_group_control", 0) < float(fraction(bounds["whole_group_global_ceiling"])): failures.append(f"gamma:{group_id}")
        if row.get("proof_safe_improvement_factor", 0) < 1e5: failures.append(f"improvement:{group_id}")
    if controls.get("pointwise_amgm_samples_passed") != controls.get("pointwise_amgm_samples_total") or controls.get("pointwise_amgm_samples_total") != 256: failures.append("pointwise")
    required_true = (
        "all_234_time_gram_entries_covered", "all_1864_leibniz_terms_covered",
        "all_faces_have_exact_integrable_duffy_weights", "large_radius_tail_has_explicit_bound",
        "face_strip_has_explicit_bound",
    )
    required_false = (
        "determinant_preserving_compact_core_quadrature_error_serialized",
        "accurate_order_six_prefix_released", "coefficient_complete_base_action_column_evaluated",
        "complete_R_ref_form_dual_residual_serialized",
        "positive_complete_M_orthogonal_complement_or_flux_floor_serialized",
        "scalar_center_left_floor_serialized", "native_K152_interval_emitted",
    )
    if any(release.get(key) is not True for key in required_true): failures.append("release_true")
    if any(release.get(key) is not False for key in required_false): failures.append("release_false")
    if not all(str(value).endswith("_UNCHANGED") for value in data.get("ledger_effect", {}).values()): failures.append("ledger")
    if data.get("physical_or_source_selection") is not False: failures.append("physical")
    if data.get("Born_prediction_or_confirmation_credit") is not False: failures.append("Born")
    if data.get("canon_paper_release_or_public_posture_move") is not False: failures.append("public")
    return failures


def exact_checks(data: dict[str, Any]) -> list[tuple[str, bool]]:
    text = ARTIFACT.read_text() if ARTIFACT.exists() else ""
    failures = manifest_failures(data)
    return [
        ("manifest", not failures), ("artifact exists", ARTIFACT.exists()), ("solver exists", SOLVER.exists()),
        ("routing notice", "GU-COMPARATOR-ROUTING" in text),
        ("classification", "Classification: INTERNAL_STRUCTURAL_ONLY." in text),
        ("typed objects", "```gu-typed-objects" in text),
        ("234 entries", "234 time-Gram entries" in text),
        ("1864 terms", "1,864 Leibniz terms" in text),
        ("load ceiling", "2/3" in text and "Dirichlet parameter" in text),
        ("radial shape", "Gamma shape six" in text and "rho^5" in text),
        ("proof/control split", "proof-safe rational ceiling" in text),
        ("compact core open", "compact determinant-core error remains open" in text),
        ("ledger unchanged", "SC-META-53" in text and "remain unchanged" in text),
    ] + [(f"no {failure}", False) for failure in failures]


def hostile_checks(data: dict[str, Any]) -> list[tuple[str, bool]]:
    mutations = (
        ("drop_entry", lambda d: d["complete_face_hypergraph"].__setitem__("gram_entries", 233)),
        ("drop_term", lambda d: d["complete_face_hypergraph"].__setitem__("leibniz_terms", 1863)),
        ("break_digest", lambda d: d["exact_allocation_certificate"].__setitem__("allocation_catalog_sha256", "0" * 64)),
        ("break_ref", lambda d: d["complete_face_hypergraph"]["entries"][0]["terms"][0].__setitem__("allocation_id", "missing")),
        ("break_weight", lambda d: next(iter(d["exact_allocation_certificate"]["allocation_catalog"].values()), None).__setitem__("weights", "0:99/1")),
        ("break_load", lambda d: next(iter(d["exact_allocation_certificate"]["allocation_catalog"].values()), None).__setitem__("loads", "99/1")),
        ("break_max", lambda d: next(iter(d["exact_allocation_certificate"]["allocation_catalog"].values()), None).__setitem__("maximum_load", "1/1")),
        ("break_radial", lambda d: d["radial_duffy_certificate"].__setitem__("radial_shape", 5)),
        ("break_group", lambda d: d["groups"].pop(next(iter(d["groups"]), None))),
        ("break_global", lambda d: next(iter(d["groups"].values()), None)["proof_safe_bounds"]["whole_group_global_ceiling"].__setitem__("numerator", 1)),
        ("break_tail", lambda d: next(iter(d["groups"].values()), None)["proof_safe_bounds"]["rho_greater_than_one_quarter_group_ceiling"].__setitem__("numerator", 1)),
        ("break_face", lambda d: next(iter(d["groups"].values()), None)["proof_safe_bounds"]["any_simplex_coordinate_below_2^-180_group_ceiling"].__setitem__("numerator", 1)),
        ("invent_core", lambda d: d["release_test"].__setitem__("determinant_preserving_compact_core_quadrature_error_serialized", True)),
        ("invent_prefix", lambda d: d["release_test"].__setitem__("accurate_order_six_prefix_released", True)),
        ("invent_action", lambda d: d["release_test"].__setitem__("coefficient_complete_base_action_column_evaluated", True)),
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
