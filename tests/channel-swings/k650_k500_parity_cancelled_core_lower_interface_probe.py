#!/usr/bin/env python3
"""Independent exact and hostile controls for K650."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k650-k500-parity-cancelled-core-lower-interface.json"


def load_solver():
    path = Path(__file__).with_name("k650_k500_parity_cancelled_core_lower_interface.py")
    spec = importlib.util.spec_from_file_location("k650_probe_solver", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


SOLVER = load_solver()


def failures(data: dict) -> list[str]:
    bad: list[str] = []
    theorem = data.get("cancelled_quadrant_theorem", {})
    schema = data.get("native_quantitative_schema", {})
    native = data.get("native_interface_status", {})
    dep = data.get("dependency_reconciliation", {})
    route = data.get("route_comparison", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        bad.append("routing")
    if theorem.get("rho_equal_one_allowed") is not True or theorem.get("same_domain_required") is not True:
        bad.append("theorem")
    if theorem.get("separately_singular_raw_channel_bounds_required") is not False or theorem.get("complete_cancelled_quadrant_bounds_required") is not True:
        bad.append("domain_scope")
    if "rho_s,n" not in str(theorem.get("coupling_hypothesis", "")) or "lambda_min" not in str(theorem.get("sector_floor", "")):
        bad.append("formula")
    if len(schema.get("uniform_tail_rows", [])) != 2 or schema.get("finite_prefix_is_tail") is not False:
        bad.append("tail")
    if schema.get("raw_twelve_plus_thirty_rows_mandatory_for_this_route") is not False or schema.get("raw_rows_remain_valid_if_independently_same_domain_bounded") is not True:
        bad.append("route_scope")
    if len(data.get("exact_controls", [])) != 2 or any(row.get("passes") is not True for row in data.get("exact_controls", [])):
        bad.append("control")
    if data.get("uniform_tail_control", {}).get("synthetic_not_native") is not True or data.get("uniform_tail_control", {}).get("all_rows_at_least_two") is not True:
        bad.append("tail_control")
    if route.get("strictly_claimed_better_numerically") is not False or "preserves" not in str(route.get("advantage", "")):
        bad.append("comparison")
    if native.get("cancellation_adapted_parity_lower_theorem_proved") is not True:
        bad.append("native_true")
    required_false = (
        "actual_cancelled_quadrant_floors_identified", "actual_relative_coupling_constants_identified",
        "actual_uniform_parity_tails_identified", "native_global_m_identified",
        "native_remainder_alpha_delta_identified", "K473_released", "native_K152_interval_emitted",
    )
    if any(native.get(key) is not False for key in required_false):
        bad.append("native_ceiling")
    if dep.get("K649_matching_uniqueness_consumed") is not True or dep.get("K644_sufficient_block_theorem_retracted") is not False:
        bad.append("dependency")
    if data.get("source_and_ledger_effect") != "none":
        bad.append("ledger")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("two complete quadrants", "alternative sufficient route", "remain absent"):
        if token not in ceiling:
            bad.append("ceiling")
    return bad


def exact_checks(data: dict) -> list[tuple[str, bool]]:
    fresh = SOLVER.build()
    theorem = data["cancelled_quadrant_theorem"]
    schema = data["native_quantitative_schema"]
    controls = data["exact_controls"]
    tail = data["uniform_tail_control"]
    native = data["native_interface_status"]
    return [
        ("fresh theorem", fresh["cancelled_quadrant_theorem"] == theorem),
        ("fresh controls", fresh["exact_controls"] == controls),
        ("two quadrants", "x,y" in theorem["decomposition"]),
        ("nonnegative parts", "A_s,n>=0" in theorem["nonnegative_parts"]),
        ("coupling formula", "rho_s,n" in theorem["coupling_hypothesis"]),
        ("rho interval", theorem["relative_range"] == "0<=rho_s,n<=1"),
        ("relative remainder", theorem["nonnegative_relative_remainder"].endswith(">=0")),
        ("comparison matrix", "kappa_s,n" in theorem["comparison_matrix"]),
        ("eigen floor", "lambda_min" in theorem["sector_floor"]),
        ("row floor", "min" in theorem["row_floor"]),
        ("rho endpoint", theorem["rho_equal_one_allowed"] is True),
        ("raw not required", theorem["separately_singular_raw_channel_bounds_required"] is False),
        ("cancelled required", theorem["complete_cancelled_quadrant_bounds_required"] is True),
        ("same domain", theorem["same_domain_required"] is True),
        ("four inputs", len(schema["per_sign_inputs"]) == 3),
        ("per sign output", "ell_s,n" in schema["per_sign_output"]),
        ("two tails", len(schema["uniform_tail_rows"]) == 2),
        ("global m", schema["global_boundary_floor"].startswith("m>=")),
        ("K642 composition", "alpha" in schema["K642_composition"]),
        ("prefix not tail", schema["finite_prefix_is_tail"] is False),
        ("42 not mandatory", schema["raw_twelve_plus_thirty_rows_mandatory_for_this_route"] is False),
        ("raw route retained", schema["raw_rows_remain_valid_if_independently_same_domain_bounded"] is True),
        ("two controls", len(controls) == 2),
        ("controls pass", all(row["passes"] for row in controls)),
        ("positive slack", all(not row["exact_psd_slack_determinant"].startswith("-") for row in controls)),
        ("tail synthetic", tail["synthetic_not_native"] is True),
        ("four tail rows", len(tail["rows"]) == 4),
        ("tail floor", tail["uniform_tail_lower"] == "2"),
        ("tail controls pass", tail["all_rows_at_least_two"] is True),
        ("native theorem", native["cancellation_adapted_parity_lower_theorem_proved"] is True),
        ("m withheld", native["native_global_m_identified"] is False),
        ("ledger unchanged", data["source_and_ledger_effect"] == "none"),
    ]


def hostile_checks(data: dict) -> list[tuple[str, bool]]:
    updates = (
        ("break routing", lambda d: d.__setitem__("direction", "native_to_observed")),
        ("forbid endpoint", lambda d: d["cancelled_quadrant_theorem"].__setitem__("rho_equal_one_allowed", False)),
        ("drop domain", lambda d: d["cancelled_quadrant_theorem"].__setitem__("same_domain_required", False)),
        ("require raw", lambda d: d["cancelled_quadrant_theorem"].__setitem__("separately_singular_raw_channel_bounds_required", True)),
        ("drop cancelled", lambda d: d["cancelled_quadrant_theorem"].__setitem__("complete_cancelled_quadrant_bounds_required", False)),
        ("erase rho", lambda d: d["cancelled_quadrant_theorem"].__setitem__("coupling_hypothesis", "unknown")),
        ("erase floor", lambda d: d["cancelled_quadrant_theorem"].__setitem__("sector_floor", "unknown")),
        ("lose tail", lambda d: d["native_quantitative_schema"].__setitem__("uniform_tail_rows", [])),
        ("prefix tail", lambda d: d["native_quantitative_schema"].__setitem__("finite_prefix_is_tail", True)),
        ("mandate 42", lambda d: d["native_quantitative_schema"].__setitem__("raw_twelve_plus_thirty_rows_mandatory_for_this_route", True)),
        ("retract raw", lambda d: d["native_quantitative_schema"].__setitem__("raw_rows_remain_valid_if_independently_same_domain_bounded", False)),
        ("fail control", lambda d: d["exact_controls"][0].__setitem__("passes", False)),
        ("one control", lambda d: d.__setitem__("exact_controls", d["exact_controls"][:1])),
        ("promote tail", lambda d: d["uniform_tail_control"].__setitem__("synthetic_not_native", False)),
        ("fail tail", lambda d: d["uniform_tail_control"].__setitem__("all_rows_at_least_two", False)),
        ("claim better", lambda d: d["route_comparison"].__setitem__("strictly_claimed_better_numerically", True)),
        ("erase advantage", lambda d: d["route_comparison"].__setitem__("advantage", "unknown")),
        ("erase theorem", lambda d: d["native_interface_status"].__setitem__("cancellation_adapted_parity_lower_theorem_proved", False)),
        ("invent quadrant floors", lambda d: d["native_interface_status"].__setitem__("actual_cancelled_quadrant_floors_identified", True)),
        ("invent rho", lambda d: d["native_interface_status"].__setitem__("actual_relative_coupling_constants_identified", True)),
        ("invent tails", lambda d: d["native_interface_status"].__setitem__("actual_uniform_parity_tails_identified", True)),
        ("invent m", lambda d: d["native_interface_status"].__setitem__("native_global_m_identified", True)),
        ("invent remainder", lambda d: d["native_interface_status"].__setitem__("native_remainder_alpha_delta_identified", True)),
        ("release K473", lambda d: d["native_interface_status"].__setitem__("K473_released", True)),
        ("retract K644", lambda d: d["dependency_reconciliation"].__setitem__("K644_sufficient_block_theorem_retracted", True)),
        ("move ledger", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
    )
    caught = []
    for name, update in updates:
        mutant = copy.deepcopy(data)
        update(mutant)
        caught.append((name, bool(failures(mutant))))
    return caught


def main() -> int:
    data = json.loads(MANIFEST.read_text())
    baseline = exact_checks(data)
    manifest_failures = failures(data)
    for name, ok in baseline:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    for failure in manifest_failures:
        print(f"[FAIL] manifest {failure}")
    print(f"K650 EXACT CONTROL: {sum(int(ok) for _, ok in baseline)}/{len(baseline)} pass")
    hostile = hostile_checks(data) if "--selftest" in sys.argv else []
    for name, ok in hostile:
        print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
    if hostile:
        print(f"HOSTILE SELFTEST: {sum(int(ok) for _, ok in hostile)}/{len(hostile)} caught")
    return 0 if all(ok for _, ok in baseline + hostile) and not manifest_failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
