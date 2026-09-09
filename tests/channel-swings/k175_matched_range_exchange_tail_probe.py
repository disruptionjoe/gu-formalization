#!/usr/bin/env python3
"""Baseline-first exact and hostile controls for K175."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOLVER = Path(__file__).with_name("k175_matched_range_exchange_tail.py")
MANIFEST = ROOT / "lab/process/k175-matched-range-exchange-tail-wave.json"
ARTIFACT = ROOT / "explorations/conditional-build/k175-matched-range-exchange-tail-wave-2026-09-09.md"


def load_solver():
    spec = importlib.util.spec_from_file_location("k175_solver", SOLVER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K175 solver")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K175 = load_solver()


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        failures.append("routing")
    matched = data.get("matched_range", {})
    if matched.get("matched_before_limit") is not True or matched.get("isolated_exchange_trace_bounded") is not False:
        failures.append("matched_scope")
    diagonal = data.get("diagonal_orbit_tail", {})
    if diagonal.get("tail_after_order_1") != "68644/190125" or diagonal.get("all_order_diagonal_tail_serialized") is not True:
        failures.append("diagonal_tail")
    scalar = data.get("scalar_metric_resummation", {})
    if scalar.get("error_at_J_12") != "1594323/419430400" or scalar.get("convergent") is not True:
        failures.append("scalar_tail")
    exchange = data.get("exchange_tail_audit", {})
    if exchange.get("componentwise_four_over_pi_shortcut_valid") is not False:
        failures.append("false_shortcut")
    if exchange.get("native_complete_exchange_tail_serialized") is not False:
        failures.append("native_exchange_tail")
    release = data.get("release_test", {})
    if release.get("scalar_core_action_column_convergent") is not True:
        failures.append("scalar_action")
    for key in (
        "coefficient_complete_exchange_action_column_serialized",
        "complete_R_ref_form_dual_residual_serialized",
        "native_K152_interval_emitted",
    ):
        if release.get(key) is not False:
            failures.append(key)
    return failures


def checks(data: dict, text: str) -> list[tuple[str, bool]]:
    result = K175.demo()
    matched = result["matched_range"]
    diagonal = result["diagonal_orbit_tail"]
    scalar = result["scalar_metric_resummation"]
    exchange = result["exchange_tail_audit"]
    release = result["release_test"]
    return [
        ("schema", result["schema_version"] == "1.0"),
        ("manifest", not manifest_failures(data)),
        ("quarter ratio", result["fixed_control"]["quarter_graph_ratio"] == "131/300"),
        ("Hilbert ratio", result["fixed_control"]["Hilbert_ratio"] == "3/8"),
        ("matched identity", "1/(a+e)-1/a" in matched["identity"]),
        ("matched limit order", matched["matched_before_limit"] is True),
        ("isolated trace fence", matched["isolated_exchange_trace_bounded"] is False),
        ("diagonal multiplicity", diagonal["multiplicity_upper"] == 2),
        ("diagonal beta", diagonal["coefficient_beta_upper"] == "2/3"),
        ("diagonal exact tail", diagonal["tail_after_order_1"] == "68644/190125"),
        ("diagonal all order", diagonal["all_order_diagonal_tail_serialized"] is True),
        ("scalar identity", scalar["identity"] == "-256*S* S"),
        ("scalar exact tail", scalar["error_at_J_12"] == "1594323/419430400"),
        ("scalar convergent", scalar["convergent"] is True),
        ("shortcut refused", exchange["componentwise_four_over_pi_shortcut_valid"] is False),
        ("cross identity absent", exchange["required_cross_term_identity_serialized"] is False),
        ("CAR bound absent", exchange["required_sector_uniform_CAR_bound_serialized"] is False),
        ("abstract control", exchange["abstract_positive_control_tail"] == "9/1600"),
        ("hostile premises rejected", exchange["missing_native_premises_rejected"] is True),
        ("native exchange open", exchange["native_complete_exchange_tail_serialized"] is False),
        ("scalar action closed", release["scalar_core_action_column_convergent"] is True),
        ("diagonal action closed", release["matched_diagonal_action_column_convergent"] is True),
        ("complete action open", release["coefficient_complete_exchange_action_column_serialized"] is False),
        ("residual open", release["complete_R_ref_form_dual_residual_serialized"] is False),
        ("K152 open", release["native_K152_interval_emitted"] is False),
        ("routing notice", "GU-COMPARATOR-ROUTING" in text),
        ("classification prose", "Classification: INTERNAL_STRUCTURAL_ONLY." in text),
        ("typed objects", "```gu-typed-objects" in text),
        ("range-specific prose", "range-specific" in text),
        ("four-over-pi refusal", "4/pi" in text and "invalid" in text),
        ("K174 preservation", "K174" in text and "isolated exchange" in text),
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
        print(f"PASS {len(baseline)}/{len(baseline)} K175 exact controls")
        return 0

    mutations = [
        lambda d: d.__setitem__("classification", "SOURCE_NATIVE"),
        lambda d: d.__setitem__("direction", "native_to_observed"),
        lambda d: d["matched_range"].__setitem__("matched_before_limit", False),
        lambda d: d["matched_range"].__setitem__("isolated_exchange_trace_bounded", True),
        lambda d: d["diagonal_orbit_tail"].__setitem__("tail_after_order_1", "0"),
        lambda d: d["diagonal_orbit_tail"].__setitem__("all_order_diagonal_tail_serialized", False),
        lambda d: d["scalar_metric_resummation"].__setitem__("error_at_J_12", "0"),
        lambda d: d["scalar_metric_resummation"].__setitem__("convergent", False),
        lambda d: d["exchange_tail_audit"].__setitem__("componentwise_four_over_pi_shortcut_valid", True),
        lambda d: d["exchange_tail_audit"].__setitem__("native_complete_exchange_tail_serialized", True),
        lambda d: d["release_test"].__setitem__("scalar_core_action_column_convergent", False),
        lambda d: d["release_test"].__setitem__("coefficient_complete_exchange_action_column_serialized", True),
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
        text.replace("range-specific", "global"),
        text.replace("4/pi", "four divided by pi"),
        text.replace("isolated exchange", "exchange"),
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
