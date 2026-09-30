#!/usr/bin/env python3
"""Independent and hostile controls for K652."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k652_k500_all_order_parity_tail_certificate.py")
MANIFEST = ROOT / "lab/process/k652-k500-all-order-parity-tail-certificate.json"


def load_producer():
    spec = importlib.util.spec_from_file_location("k652_probe_producer", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K652 producer")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


P = load_producer()


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    theorem = data.get("all_order_tail_theorem", {})
    native = data.get("native_interface_status", {})
    if theorem.get("rho_endpoint_allowed") is not True or theorem.get("all_order_hypotheses_required") is not True:
        failures.append("hypotheses")
    if theorem.get("separately_singular_raw_rows_required") is not False or theorem.get("finite_prefix_alone_sufficient") is not False:
        failures.append("topology")
    if "min(A_s(n)-K_s(n),D_s(n)-K_s(n))" not in str(theorem.get("sector_row_floor", "")):
        failures.append("row-floor")
    controls = data.get("exact_controls", {})
    if controls.get("synthetic_not_native") is not True or controls.get("global_declared_tail") != "7/4" or controls.get("all_rows_pass") is not True:
        failures.append("controls")
    if native.get("all_order_certificate_shape_complete") is not True:
        failures.append("certificate")
    denied = (
        "actual_all_order_diagonal_lower_functions_identified",
        "actual_all_order_residual_upper_functions_identified",
        "actual_uniform_parity_tails_identified", "native_global_m_identified",
        "native_remainder_alpha_delta_identified", "K473_released", "native_K152_interval_emitted",
    )
    if any(native.get(key) is not False for key in denied):
        failures.append("native-status")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("all-order", "min(A-K,D-K)", "no native A,D,K", "No K473"):
        if token not in ceiling:
            failures.append(f"claim-ceiling:{token}")
    return failures


def exact_checks(data: dict) -> list[tuple[str, bool]]:
    theorem = data["all_order_tail_theorem"]
    plus = data["exact_controls"]["plus"]
    minus = data["exact_controls"]["minus"]
    return [
        ("producer and manifest agree", data == P.build()),
        ("three all-order hypotheses are explicit", len(theorem["hypotheses"]) == 3),
        ("rho endpoint one is allowed", theorem["rho_endpoint_allowed"]),
        ("raw singular rows are not required", not theorem["separately_singular_raw_rows_required"]),
        ("all-order hypotheses are required", theorem["all_order_hypotheses_required"]),
        ("finite prefix is insufficient", not theorem["finite_prefix_alone_sufficient"]),
        ("plus tail is two", plus["declared_tail"] == "2"),
        ("minus tail is seven quarters", minus["declared_tail"] == "7/4"),
        ("six plus rows pass", len(plus["rows"]) == 6 and all(row["at_least_declared_tail"] for row in plus["rows"])),
        ("six minus rows pass", len(minus["rows"]) == 6 and all(row["at_least_declared_tail"] for row in minus["rows"])),
        ("global control tail is seven quarters", data["exact_controls"]["global_declared_tail"] == "7/4"),
        ("relative energy is not charged twice", data["asymptotic_corollaries"]["relative_energy_not_charged_twice"]),
        ("K651 obstruction is consumed", data["decision"]["K651_prefix_obstruction_consumed"]),
        ("constructive route closes abstractly", data["decision"]["constructive_all_order_route_closed_abstractly"]),
        ("native tail is not emitted", not data["decision"]["native_numeric_tail_emitted"]),
        ("all-order certificate shape is complete", data["native_interface_status"]["all_order_certificate_shape_complete"]),
        ("native functions remain absent", not data["native_interface_status"]["actual_all_order_diagonal_lower_functions_identified"] and not data["native_interface_status"]["actual_all_order_residual_upper_functions_identified"]),
        ("native m remains absent", not data["native_interface_status"]["native_global_m_identified"]),
        ("K473 stays closed", not data["native_interface_status"]["K473_released"]),
        ("K612 is preserved", not data["dependency_reconciliation"]["K612_custody_obstruction_retracted"]),
        ("source and ledger stay unchanged", data["source_and_ledger_effect"] == "none"),
    ]


def hostile_checks(data: dict) -> list[tuple[str, bool]]:
    mutations = (
        ("erase-rho-endpoint", lambda d: d["all_order_tail_theorem"].__setitem__("rho_endpoint_allowed", False)),
        ("require-raw", lambda d: d["all_order_tail_theorem"].__setitem__("separately_singular_raw_rows_required", True)),
        ("erase-all-order", lambda d: d["all_order_tail_theorem"].__setitem__("all_order_hypotheses_required", False)),
        ("promote-prefix", lambda d: d["all_order_tail_theorem"].__setitem__("finite_prefix_alone_sufficient", True)),
        ("break-row-floor", lambda d: d["all_order_tail_theorem"].__setitem__("sector_row_floor", "g>=min(A,D)")),
        ("promote-control", lambda d: d["exact_controls"].__setitem__("synthetic_not_native", False)),
        ("change-tail", lambda d: d["exact_controls"].__setitem__("global_declared_tail", "2")),
        ("erase-pass", lambda d: d["exact_controls"].__setitem__("all_rows_pass", False)),
        ("erase-certificate", lambda d: d["native_interface_status"].__setitem__("all_order_certificate_shape_complete", False)),
        ("invent-diagonal", lambda d: d["native_interface_status"].__setitem__("actual_all_order_diagonal_lower_functions_identified", True)),
        ("invent-residual", lambda d: d["native_interface_status"].__setitem__("actual_all_order_residual_upper_functions_identified", True)),
        ("invent-tail", lambda d: d["native_interface_status"].__setitem__("actual_uniform_parity_tails_identified", True)),
        ("invent-m", lambda d: d["native_interface_status"].__setitem__("native_global_m_identified", True)),
        ("invent-alpha", lambda d: d["native_interface_status"].__setitem__("native_remainder_alpha_delta_identified", True)),
        ("release-K473", lambda d: d["native_interface_status"].__setitem__("K473_released", True)),
        ("release-K152", lambda d: d["native_interface_status"].__setitem__("native_K152_interval_emitted", True)),
        ("erase-ceiling", lambda d: d.__setitem__("claim_ceiling", "The native parity tail is seven quarters.")),
    )
    caught = []
    for name, mutate in mutations:
        mutant = copy.deepcopy(data)
        mutate(mutant)
        caught.append((name, bool(manifest_failures(mutant))))
    return caught


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    baseline = exact_checks(data)
    for name, ok in baseline:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    failures = manifest_failures(data)
    for failure in failures:
        print(f"[FAIL] manifest {failure}")
    print(f"K652 EXACT CONTROL: {sum(int(ok) for _, ok in baseline)}/{len(baseline)} pass")
    if "--selftest" in sys.argv:
        hostile = hostile_checks(data)
        for name, ok in hostile:
            print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
        print(f"HOSTILE SELFTEST: {sum(int(ok) for _, ok in hostile)}/{len(hostile)} caught")
        return 0 if all(ok for _, ok in baseline + hostile) and not failures else 1
    return 0 if all(ok for _, ok in baseline) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
