#!/usr/bin/env python3
"""Independent and hostile controls for K654."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k654_k500_all_order_shifted_schur_tail.py")
MANIFEST = ROOT / "lab/process/k654-k500-all-order-shifted-schur-tail.json"


def load_producer():
    spec = importlib.util.spec_from_file_location("k654_probe_producer", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K654 producer")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


P = load_producer()


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    theorem = data.get("all_order_shifted_tail_theorem", {})
    controls = data.get("exact_controls", {})
    native = data.get("native_interface_status", {})
    if theorem.get("single_target_may_be_tested_directly") is not True or theorem.get("all_order_shifted_hypotheses_required") is not True:
        failures.append("target-route")
    if theorem.get("absolute_A_D_K_envelopes_required") is not False or theorem.get("finite_prefix_alone_sufficient") is not False:
        failures.append("topology")
    if theorem.get("equivalent_native_burden_is_not_removed") is not True:
        failures.append("burden")
    if controls.get("synthetic_not_native") is not True or controls.get("target_b") != "5/4" or controls.get("all_tail_rows_pass") is not True or controls.get("finite_sectors_at_least_target") is not True:
        failures.append("controls")
    if native.get("all_order_shifted_tail_shape_complete") is not True:
        failures.append("certificate")
    denied = (
        "actual_native_target_b_identified", "actual_all_order_shifted_hypotheses_proved",
        "actual_uniform_parity_tails_identified", "native_global_m_identified",
        "native_remainder_alpha_delta_identified", "K473_released", "native_K152_interval_emitted",
    )
    if any(native.get(key) is not False for key in denied):
        failures.append("native-status")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("all-order", "prescribed b", "synthetic b=5/4", "No native b"):
        if token not in ceiling:
            failures.append(f"claim-ceiling:{token}")
    return failures


def exact_checks(data: dict) -> list[tuple[str, bool]]:
    theorem = data["all_order_shifted_tail_theorem"]
    controls = data["exact_controls"]
    native = data["native_interface_status"]
    return [
        ("producer and manifest agree", data == P.build()),
        ("three hypotheses are explicit", len(theorem["hypotheses"]) == 3),
        ("direct single target is allowed", theorem["single_target_may_be_tested_directly"]),
        ("absolute envelopes are optional", not theorem["absolute_A_D_K_envelopes_required"]),
        ("all-order shifted hypotheses are required", theorem["all_order_shifted_hypotheses_required"]),
        ("finite prefix is insufficient", not theorem["finite_prefix_alone_sufficient"]),
        ("native burden is preserved", theorem["equivalent_native_burden_is_not_removed"]),
        ("control target is five quarters", controls["target_b"] == "5/4"),
        ("four plus rows pass", len(controls["plus"]["rows"]) == 4 and all(row["target_floor_certified"] for row in controls["plus"]["rows"])),
        ("four minus rows pass", len(controls["minus"]["rows"]) == 4 and all(row["target_floor_certified"] for row in controls["minus"]["rows"])),
        ("finite sectors pass", controls["finite_sectors_at_least_target"]),
        ("K651 obstruction is consumed", data["decision"]["K651_prefix_obstruction_consumed"]),
        ("K653 theorem is consumed", data["decision"]["K653_target_certificate_consumed"]),
        ("direct route closes abstractly", data["decision"]["direct_all_order_target_route_closed_abstractly"]),
        ("native floor is not emitted", not data["decision"]["native_uniform_floor_emitted"]),
        ("certificate shape is complete", native["all_order_shifted_tail_shape_complete"]),
        ("native target remains absent", not native["actual_native_target_b_identified"]),
        ("native tails remain absent", not native["actual_uniform_parity_tails_identified"]),
        ("native m remains absent", not native["native_global_m_identified"]),
        ("K473 stays closed", not native["K473_released"]),
        ("K652 route is preserved", not data["dependency_reconciliation"]["K652_absolute_envelope_route_retracted"]),
        ("source and ledger stay unchanged", data["source_and_ledger_effect"] == "none"),
    ]


def hostile_checks(data: dict) -> list[tuple[str, bool]]:
    mutations = (
        ("erase-target", lambda d: d["all_order_shifted_tail_theorem"].__setitem__("single_target_may_be_tested_directly", False)),
        ("erase-all-order", lambda d: d["all_order_shifted_tail_theorem"].__setitem__("all_order_shifted_hypotheses_required", False)),
        ("require-envelopes", lambda d: d["all_order_shifted_tail_theorem"].__setitem__("absolute_A_D_K_envelopes_required", True)),
        ("promote-prefix", lambda d: d["all_order_shifted_tail_theorem"].__setitem__("finite_prefix_alone_sufficient", True)),
        ("erase-burden", lambda d: d["all_order_shifted_tail_theorem"].__setitem__("equivalent_native_burden_is_not_removed", False)),
        ("promote-control", lambda d: d["exact_controls"].__setitem__("synthetic_not_native", False)),
        ("change-target", lambda d: d["exact_controls"].__setitem__("target_b", "3/2")),
        ("break-tail", lambda d: d["exact_controls"].__setitem__("all_tail_rows_pass", False)),
        ("break-prefix", lambda d: d["exact_controls"].__setitem__("finite_sectors_at_least_target", False)),
        ("erase-certificate", lambda d: d["native_interface_status"].__setitem__("all_order_shifted_tail_shape_complete", False)),
        ("invent-target", lambda d: d["native_interface_status"].__setitem__("actual_native_target_b_identified", True)),
        ("invent-hypotheses", lambda d: d["native_interface_status"].__setitem__("actual_all_order_shifted_hypotheses_proved", True)),
        ("invent-tail", lambda d: d["native_interface_status"].__setitem__("actual_uniform_parity_tails_identified", True)),
        ("invent-m", lambda d: d["native_interface_status"].__setitem__("native_global_m_identified", True)),
        ("invent-alpha", lambda d: d["native_interface_status"].__setitem__("native_remainder_alpha_delta_identified", True)),
        ("release-K473", lambda d: d["native_interface_status"].__setitem__("K473_released", True)),
        ("release-K152", lambda d: d["native_interface_status"].__setitem__("native_K152_interval_emitted", True)),
        ("erase-ceiling", lambda d: d.__setitem__("claim_ceiling", "The native floor is five quarters.")),
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
    print(f"K654 EXACT CONTROL: {sum(int(ok) for _, ok in baseline)}/{len(baseline)} pass")
    if "--selftest" in sys.argv:
        hostile = hostile_checks(data)
        for name, ok in hostile:
            print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
        print(f"HOSTILE SELFTEST: {sum(int(ok) for _, ok in hostile)}/{len(hostile)} caught")
        return 0 if all(ok for _, ok in baseline + hostile) and not failures else 1
    return 0 if all(ok for _, ok in baseline) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
