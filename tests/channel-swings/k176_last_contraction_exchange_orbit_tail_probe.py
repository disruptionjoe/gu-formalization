#!/usr/bin/env python3
"""Baseline-first exact and hostile controls for K176."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOLVER = Path(__file__).with_name("k176_last_contraction_exchange_orbit_tail.py")
MANIFEST = ROOT / "lab/process/k176-last-contraction-exchange-orbit-tail-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k176-last-contraction-exchange-orbit-tail-wave-2026-09-09.md"


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K176 = load(SOLVER, "k176_solver")


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    normal = data.get("normal_form", {})
    for key in (
        "finite_cutoff_first",
        "matched_endpoint_before_limit",
        "adjacent_wick_contraction_cancelled",
        "older_letter_count_equals_order",
        "two_resolvent_kernel_on_every_older_letter",
        "all_16_exchange_monomials_included",
        "spectator_shifts_nonnegative",
        "sector_uniform_CAR_sum_bound",
    ):
        if normal.get(key) is not True:
            failures.append(key)
    if normal.get("cross_polarity_cancellation_required") is not False:
        failures.append("cross_polarity")
    if data.get("kernel", {}).get("norm_squared_upper") != "2/3":
        failures.append("kernel")
    census = data.get("exchange_census", {})
    if census.get("monomials") != 16 or census.get("coefficient_upper") != "40/3":
        failures.append("census")
    tail = data.get("post_adjoint_tail", {})
    if tail.get("after_order_12") != "3011499/838860800" or tail.get("native_complete_exchange_tail_convergent") is not True:
        failures.append("tail")
    release = data.get("release_test", {})
    if release.get("coefficient_complete_exchange_action_column_tail_serialized") is not True:
        failures.append("tail_release")
    for key in (
        "resolved_exchange_vectors_through_order_12_evaluated",
        "coefficient_complete_base_action_column_evaluated",
        "complete_R_ref_form_dual_residual_serialized",
        "native_K152_interval_emitted",
    ):
        if release.get(key) is not False:
            failures.append(key)
    return failures


def checks(data: dict, text: str) -> list[tuple[str, bool]]:
    result = K176.demo()
    normal = result["normal_form"]
    kernel = result["kernel"]
    census = result["exchange_census"]
    tail = result["post_adjoint_tail"]
    release = result["release_test"]
    return [
        ("schema", result["schema_version"] == "1.0"),
        ("manifest", not manifest_failures(data)),
        ("Hilbert ratio", result["fixed_control"]["Hilbert_boundary_ratio"] == "3/8"),
        ("finite cutoff", normal["finite_cutoff_first"] is True),
        ("matched endpoint", normal["matched_endpoint_before_limit"] is True),
        ("adjacent cancellation", normal["adjacent_wick_contraction_cancelled"] is True),
        ("older-letter count", normal["older_letter_count_equals_order"] is True),
        ("two resolvents", normal["two_resolvent_kernel_on_every_older_letter"] is True),
        ("all monomials", normal["all_16_exchange_monomials_included"] is True),
        ("spectator order", normal["spectator_shifts_nonnegative"] is True),
        ("CAR bound", normal["sector_uniform_CAR_sum_bound"] is True),
        ("no invented cancellation", normal["cross_polarity_cancellation_required"] is False),
        ("kernel definition", kernel["definition"] == "J_256(e)=D_256(e)/e"),
        ("integral split", kernel["integral_split_upper"] == "6"),
        ("kernel square", kernel["norm_squared_upper"] == "2/3"),
        ("kernel norm", kernel["norm_upper"] == "5/6"),
        ("rational rounding", Fraction(2, 3) < Fraction(25, 36)),
        ("census", census["monomials"] == 16),
        ("coefficient", census["coefficient_upper"] == "40/3"),
        ("hostile premises rejected", census["all_missing_premises_rejected"] is True),
        ("order one block", K176.exchange_block_bound(1) == Fraction(40, 3)),
        ("tail order one", tail["after_order_1"] == "832/25"),
        ("tail order twelve", tail["after_order_12"] == "3011499/838860800"),
        ("tail target", tail["after_order_12_less_than_1_over_250"] is True),
        ("tail decreases", K176.exchange_tail(12) < K176.exchange_tail(11)),
        ("exchange tail closed", release["coefficient_complete_exchange_action_column_tail_serialized"] is True),
        ("resolved prefix open", release["resolved_exchange_vectors_through_order_12_evaluated"] is False),
        ("action column open", release["coefficient_complete_base_action_column_evaluated"] is False),
        ("residual open", release["complete_R_ref_form_dual_residual_serialized"] is False),
        ("K152 open", release["native_K152_interval_emitted"] is False),
        ("routing notice", "GU-COMPARATOR-ROUTING" in text),
        ("classification prose", "Classification: INTERNAL_STRUCTURAL_ONLY." in text),
        ("typed objects", "```gu-typed-objects" in text),
        ("adjacent prose", "adjacent Wick contraction" in text),
        ("cross-polarity correction", "cross-polarity cancellation" in text and "not" in text),
        ("coefficient scope", "coefficient-specific" in text),
        ("ledger fence", all(value.endswith("_UNCHANGED") for value in result["ledger_effect"].values())),
        ("no physical selection", result["physical_or_source_selection"] is False),
        ("no export credit", result["Born_prediction_or_confirmation_credit"] is False),
        ("no posture move", result["canon_paper_release_or_public_posture_move"] is False),
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    data = json.loads(MANIFEST.read_text())
    text = ARTIFACT.read_text()
    baseline = checks(data, text)
    failed = [name for name, ok in baseline if not ok]
    if failed:
        print(f"FAIL baseline {len(baseline)-len(failed)}/{len(baseline)}: {failed}")
        return 1
    if not args.selftest:
        print(f"PASS {len(baseline)}/{len(baseline)} K176 exact controls")
        return 0

    mutations = [
        lambda d: d.__setitem__("classification", "SOURCE_NATIVE"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["normal_form"].__setitem__("finite_cutoff_first", False),
        lambda d: d["normal_form"].__setitem__("matched_endpoint_before_limit", False),
        lambda d: d["normal_form"].__setitem__("adjacent_wick_contraction_cancelled", False),
        lambda d: d["normal_form"].__setitem__("older_letter_count_equals_order", False),
        lambda d: d["normal_form"].__setitem__("two_resolvent_kernel_on_every_older_letter", False),
        lambda d: d["normal_form"].__setitem__("all_16_exchange_monomials_included", False),
        lambda d: d["normal_form"].__setitem__("spectator_shifts_nonnegative", False),
        lambda d: d["normal_form"].__setitem__("sector_uniform_CAR_sum_bound", False),
        lambda d: d["normal_form"].__setitem__("cross_polarity_cancellation_required", True),
        lambda d: d["kernel"].__setitem__("norm_squared_upper", "1/2"),
        lambda d: d["exchange_census"].__setitem__("monomials", 15),
        lambda d: d["exchange_census"].__setitem__("coefficient_upper", "1"),
        lambda d: d["post_adjoint_tail"].__setitem__("after_order_12", "0"),
        lambda d: d["post_adjoint_tail"].__setitem__("native_complete_exchange_tail_convergent", False),
        lambda d: d["release_test"].__setitem__("coefficient_complete_exchange_action_column_tail_serialized", False),
        lambda d: d["release_test"].__setitem__("resolved_exchange_vectors_through_order_12_evaluated", True),
        lambda d: d["release_test"].__setitem__("coefficient_complete_base_action_column_evaluated", True),
        lambda d: d["release_test"].__setitem__("complete_R_ref_form_dual_residual_serialized", True),
        lambda d: d["release_test"].__setitem__("native_K152_interval_emitted", True),
    ]
    caught = 0
    for mutate in mutations:
        mutant = copy.deepcopy(data)
        mutate(mutant)
        if manifest_failures(mutant):
            caught += 1
    prose_mutants = [
        text.replace("GU-COMPARATOR-ROUTING", "ROUTING"),
        text.replace("Classification: INTERNAL_STRUCTURAL_ONLY.", ""),
        text.replace("```gu-typed-objects", "```text"),
        text.replace("adjacent Wick contraction", "local contraction"),
        text.replace("cross-polarity cancellation", "cross cancellation"),
        text.replace("coefficient-specific", "global"),
    ]
    for mutant in prose_mutants:
        if any(not ok for _, ok in checks(data, mutant)):
            caught += 1
    expected = len(mutations) + len(prose_mutants)
    if caught != expected:
        print(f"FAIL hostile {caught}/{expected}")
        return 1
    print(f"PASS hostile {caught}/{expected} mutations caught")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
