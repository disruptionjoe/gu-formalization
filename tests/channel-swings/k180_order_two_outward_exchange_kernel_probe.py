#!/usr/bin/env python3
"""Exact, numerical-boundary, and hostile controls for K180."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
import sys
from decimal import Decimal
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
SOLVER_PATH = Path(__file__).with_name("k180_order_two_outward_exchange_kernel.py")
MANIFEST = ROOT / "lab/process/k180-order-two-outward-exchange-kernel-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k180-order-two-outward-exchange-kernel-wave-2026-09-09.md"


def load_solver():
    spec = importlib.util.spec_from_file_location("k180_solver", SOLVER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {SOLVER_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


K180 = load_solver()


def manifest_failures(data: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    fixed = data.get("fixed_control", {})
    analytic = data.get("analytic_reduction", {})
    family = data.get("order_two_family", {})
    outward = data.get("outward_evaluation", {})
    seed = data.get("seedwise_exchange_vector", {})
    release = data.get("release_test", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    if fixed.get("coefficient_family_sha256") != "ee24469ef5c6bb8d606efe1d529b294cbc7097b14adc51df80a51627aa7eb686":
        failures.append("K179_pin")
    if analytic.get("coordinatewise_positive_and_decreasing") is not True or analytic.get("order_two_determinants_are_rank_one") is not True:
        failures.append("analytic_structure")
    if family.get("order_two_terms") != 6 or family.get("each_seed_has_two_orthogonal_output_signatures") is not True:
        failures.append("order_two_family")
    if family.get("determinant_rank_at_order_two") != 1:
        failures.append("determinant_rank")
    census = family.get("higher_order_repeated_species_census", {})
    if census.get("3") != {"terms": 8, "terms_with_repeated_output_species": 4}:
        failures.append("order_three_switch")
    lower = Decimal(outward.get("single_kernel_norm_squared_lower", "NaN"))
    upper = Decimal(outward.get("single_kernel_norm_squared_upper", "NaN"))
    compressed = Decimal(outward.get("midpoint_compression_norm_squared", "NaN"))
    if not (Decimal("6.15e-8") < lower < compressed < upper < Decimal("7.84e-8")):
        failures.append("outward_interval")
    if outward.get("midpoint_compression_inside_outward_enclosure") is not True:
        failures.append("compression")
    if not all(row.get("closed_form_inside_direct_enclosure") is True for row in outward.get("direct_integral_anchor_controls", [])):
        failures.append("direct_integral_controls")
    if len(outward.get("direct_integral_anchor_controls", [])) != 3:
        failures.append("direct_integral_count")
    if Decimal(seed.get("norm_squared_lower", "NaN")) != Decimal(2) * lower or Decimal(seed.get("norm_squared_upper", "NaN")) != Decimal(2) * upper:
        failures.append("seed_norm")
    required = (
        "all_six_order_two_kernels_evaluated",
        "determinant_level_outward_bounds_certified",
        "same_family_conforming_compression_with_error_certified",
        "order_two_normalization_agrees",
    )
    if any(release.get(key) is not True for key in required):
        failures.append("release_positive")
    denied = (
        "order_three_through_twelve_nontrivial_determinants_evaluated",
        "coefficient_complete_base_action_column_evaluated",
        "complete_R_ref_form_dual_residual_serialized",
        "positive_complete_M_orthogonal_complement_or_flux_floor_serialized",
        "scalar_center_left_floor_serialized",
        "native_K152_interval_emitted",
    )
    if any(release.get(key) is not False for key in denied):
        failures.append("release_fence")
    if data.get("ledger_effect") != {
        "SC-META-53": "UNCERTAIN_UNCHANGED", "LT-SM8": "NEEDS_UNCHANGED",
        "RA-F1": "NEEDS_UNCHANGED", "AC-F1": "NEEDS_UNCHANGED",
    }:
        failures.append("ledger")
    if any(data.get(key) is not False for key in ("physical_or_source_selection", "Born_prediction_or_confirmation_credit", "canon_paper_release_or_public_posture_move")):
        failures.append("scope")
    return failures


def exact_checks(data: dict[str, Any]) -> list[tuple[str, bool]]:
    text = ARTIFACT.read_text()
    outward = data["outward_evaluation"]
    family = data["order_two_family"]
    return [
        ("manifest exact", not manifest_failures(data)),
        ("K179 family pin", data["fixed_control"]["coefficient_family_sha256"] == K180.K179.family_digest(K180.K179.coefficient_family())),
        ("six native order-two terms", family["order_two_terms"] == 6),
        ("common unsigned kernel", family["all_share_common_unsigned_kernel"] is True),
        ("orthogonal outputs per seed", family["each_seed_has_two_orthogonal_output_signatures"] is True),
        ("rank-one order-two determinants", family["determinant_rank_at_order_two"] == 1),
        ("first higher determinant at order three", family["higher_order_repeated_species_census"]["3"]["terms_with_repeated_output_species"] == 4),
        ("positive monotone kernel", data["analytic_reduction"]["coordinatewise_positive_and_decreasing"] is True),
        ("dyadic mesh fixed", Decimal(outward["positive_axis_cutoff"]) == Decimal(2) ** 40 and outward["positive_quadrant_cells"] == 60516),
        ("finite outward order", Decimal(outward["finite_positive_quadrant_raw_lower"]) < Decimal(outward["finite_positive_quadrant_raw_upper"])),
        ("positive analytic tail", Decimal(outward["full_raw_tail_upper"]) > 0),
        ("norm interval nonempty", Decimal(outward["single_kernel_norm_squared_lower"]) < Decimal(outward["single_kernel_norm_squared_upper"])),
        ("compression inside enclosure", outward["midpoint_compression_inside_outward_enclosure"] is True),
        ("compression error positive", Decimal(outward["midpoint_compression_l2_error_upper"]) > 0),
        ("three direct controls", len(outward["direct_integral_anchor_controls"]) == 3),
        ("direct controls enclose closed form", all(row["closed_form_inside_direct_enclosure"] for row in outward["direct_integral_anchor_controls"])),
        ("seed norm doubles one kernel", Decimal(data["seedwise_exchange_vector"]["norm_squared_lower"]) == 2 * Decimal(outward["single_kernel_norm_squared_lower"])),
        ("signs retained", data["seedwise_exchange_vector"]["signs_preserved_in_action_coordinates"] is True),
        ("orthogonality explains norm split", data["seedwise_exchange_vector"]["cross_terms_vanish_by_impurity_species_output_orthogonality"] is True),
        ("order two released", data["release_test"]["all_six_order_two_kernels_evaluated"] is True),
        ("higher orders fenced", data["release_test"]["order_three_through_twelve_nontrivial_determinants_evaluated"] is False),
        ("action fenced", data["release_test"]["coefficient_complete_base_action_column_evaluated"] is False),
        ("residual fenced", data["release_test"]["complete_R_ref_form_dual_residual_serialized"] is False),
        ("complement fenced", data["release_test"]["positive_complete_M_orthogonal_complement_or_flux_floor_serialized"] is False),
        ("K152 fenced", data["release_test"]["native_K152_interval_emitted"] is False),
        ("source ledger unchanged", all(value.endswith("_UNCHANGED") for value in data["ledger_effect"].values())),
        ("no physical selection", data["physical_or_source_selection"] is False),
        ("no Born credit", data["Born_prediction_or_confirmation_credit"] is False),
        ("no public move", data["canon_paper_release_or_public_posture_move"] is False),
        ("routing notice", "GU-COMPARATOR-ROUTING" in text),
        ("classification", "Classification: INTERNAL_STRUCTURAL_ONLY." in text),
        ("typed objects", "```gu-typed-objects" in text),
        ("outward derivation documented", "Weighted AM--GM" in text),
        ("compression error documented", "cellwise error" in text),
        ("order-three switch documented", "four of the eight order-three" in text),
    ]


def hostile_checks(data: dict[str, Any]) -> list[tuple[str, bool]]:
    mutations: list[tuple[str, Any]] = []
    updates = (
        ("change_K179_pin", lambda d: d["fixed_control"].__setitem__("coefficient_family_sha256", "0" * 64)),
        ("erase_monotonicity", lambda d: d["analytic_reduction"].__setitem__("coordinatewise_positive_and_decreasing", False)),
        ("invent_rank_two", lambda d: d["order_two_family"].__setitem__("determinant_rank_at_order_two", 2)),
        ("collapse_term_count", lambda d: d["order_two_family"].__setitem__("order_two_terms", 5)),
        ("erase_orthogonality", lambda d: d["order_two_family"].__setitem__("each_seed_has_two_orthogonal_output_signatures", False)),
        ("erase_order_three_switch", lambda d: d["order_two_family"]["higher_order_repeated_species_census"]["3"].__setitem__("terms_with_repeated_output_species", 0)),
        ("invert_interval", lambda d: d["outward_evaluation"].__setitem__("single_kernel_norm_squared_lower", "9e-8")),
        ("move_compression_outside", lambda d: d["outward_evaluation"].__setitem__("midpoint_compression_norm_squared", "9e-8")),
        ("erase_compression_flag", lambda d: d["outward_evaluation"].__setitem__("midpoint_compression_inside_outward_enclosure", False)),
        ("break_direct_control", lambda d: d["outward_evaluation"]["direct_integral_anchor_controls"][0].__setitem__("closed_form_inside_direct_enclosure", False)),
        ("invent_higher_orders", lambda d: d["release_test"].__setitem__("order_three_through_twelve_nontrivial_determinants_evaluated", True)),
        ("invent_action", lambda d: d["release_test"].__setitem__("coefficient_complete_base_action_column_evaluated", True)),
        ("invent_residual", lambda d: d["release_test"].__setitem__("complete_R_ref_form_dual_residual_serialized", True)),
        ("invent_complement", lambda d: d["release_test"].__setitem__("positive_complete_M_orthogonal_complement_or_flux_floor_serialized", True)),
        ("invent_K152", lambda d: d["release_test"].__setitem__("native_K152_interval_emitted", True)),
        ("move_ledger", lambda d: d["ledger_effect"].__setitem__("SC-META-53", "RESOLVED")),
        ("invent_physical", lambda d: d.__setitem__("physical_or_source_selection", True)),
        ("invent_Born", lambda d: d.__setitem__("Born_prediction_or_confirmation_credit", True)),
        ("invent_public", lambda d: d.__setitem__("canon_paper_release_or_public_posture_move", True)),
    )
    for name, update in updates:
        broken = copy.deepcopy(data)
        update(broken)
        mutations.append((name, bool(manifest_failures(broken))))
    return mutations


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
