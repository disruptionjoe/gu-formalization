#!/usr/bin/env python3
"""Independent and hostile controls for K656."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k656_k500_base_floor_target_lift.py")
MANIFEST = ROOT / "lab/process/k656-k500-base-floor-target-lift.json"


def load_producer():
    spec = importlib.util.spec_from_file_location("k656_probe_producer", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K656 producer")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


P = load_producer()


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    theorem = data.get("base_floor_lift_theorem", {})
    controls = data.get("exact_controls", {})
    native = data.get("native_interface_status", {})
    if theorem.get("selected_target") != "b=r0-2" or theorem.get("same_domain_required") is not True:
        failures.append("target-theorem")
    if theorem.get("two_unit_loss_sharp_over_declared_reference_class") is not True:
        failures.append("sharpness")
    if theorem.get("K653_sector_search_required_after_global_base_lower") is not False:
        failures.append("composition")
    if controls.get("conditional_not_native_number") is not True or controls.get("all_rows_pass") is not True or controls.get("all_rows_sharp") is not True:
        failures.append("controls")
    denied = (
        "actual_native_base_floor_r0_identified", "actual_native_target_b_identified",
        "actual_uniform_parity_tails_identified", "native_global_m_identified",
        "native_remainder_alpha_delta_identified", "K473_released", "native_K152_interval_emitted",
    )
    if any(native.get(key) is not False for key in denied):
        failures.append("native-status")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("conditional target lift", "b=r0-2", "two-unit loss", "No numerical r0"):
        if token not in ceiling:
            failures.append(f"claim-ceiling:{token}")
    return failures


def exact_checks(data: dict) -> list[tuple[str, bool]]:
    theorem = data["base_floor_lift_theorem"]
    controls = data["exact_controls"]
    native = data["native_interface_status"]
    rows = controls["rows"]
    return [
        ("producer and manifest agree", data == P.build()),
        ("four exact controls are present", controls["row_count"] == 4),
        ("target is r0 minus two", theorem["selected_target"] == "b=r0-2"),
        ("complete order is composed", "(r0-2)M" in theorem["composition"]),
        ("all compressions inherit the target", "every bath-number" in theorem["compression_consequence"]),
        ("global lower avoids sector search", not theorem["K653_sector_search_required_after_global_base_lower"]),
        ("two-unit loss is sharp", theorem["two_unit_loss_sharp_over_declared_reference_class"]),
        ("sharp witness names minus-two eigenspace", "-2 eigenspace" in theorem["sharpness_witness"]),
        ("same domain is required", theorem["same_domain_required"]),
        ("every control passes", controls["all_rows_pass"]),
        ("every control saturates", controls["all_rows_sharp"]),
        ("zero base floor gives target minus two", rows[1]["base_floor_r0"] == "0" and rows[1]["target_b"] == "-2"),
        ("fractional base floor is exact", rows[-1]["base_floor_r0"] == "11/4" and rows[-1]["target_b"] == "3/4"),
        ("K655 is consumed", data["decision"]["K655_custody_obstruction_consumed"]),
        ("minimal repair is identified", data["decision"]["minimal_numerical_repair_identified"]),
        ("native r0 is not supplied", not data["decision"]["native_base_floor_r0_supplied"]),
        ("native target is not emitted", not data["decision"]["native_target_floor_emitted"]),
        ("conditional formula is complete", native["conditional_target_formula_complete"]),
        ("native m remains absent", not native["native_global_m_identified"]),
        ("source and ledger stay unchanged", data["source_and_ledger_effect"] == "none"),
    ]


def hostile_checks(data: dict) -> list[tuple[str, bool]]:
    mutations = (
        ("change-target", lambda d: d["base_floor_lift_theorem"].__setitem__("selected_target", "b=r0-1")),
        ("erase-domain", lambda d: d["base_floor_lift_theorem"].__setitem__("same_domain_required", False)),
        ("erase-sharpness", lambda d: d["base_floor_lift_theorem"].__setitem__("two_unit_loss_sharp_over_declared_reference_class", False)),
        ("require-sector-search", lambda d: d["base_floor_lift_theorem"].__setitem__("K653_sector_search_required_after_global_base_lower", True)),
        ("promote-control", lambda d: d["exact_controls"].__setitem__("conditional_not_native_number", False)),
        ("break-pass", lambda d: d["exact_controls"].__setitem__("all_rows_pass", False)),
        ("break-sharp", lambda d: d["exact_controls"].__setitem__("all_rows_sharp", False)),
        ("invent-r0", lambda d: d["native_interface_status"].__setitem__("actual_native_base_floor_r0_identified", True)),
        ("invent-target", lambda d: d["native_interface_status"].__setitem__("actual_native_target_b_identified", True)),
        ("invent-tail", lambda d: d["native_interface_status"].__setitem__("actual_uniform_parity_tails_identified", True)),
        ("invent-m", lambda d: d["native_interface_status"].__setitem__("native_global_m_identified", True)),
        ("invent-alpha", lambda d: d["native_interface_status"].__setitem__("native_remainder_alpha_delta_identified", True)),
        ("release-K473", lambda d: d["native_interface_status"].__setitem__("K473_released", True)),
        ("release-K152", lambda d: d["native_interface_status"].__setitem__("native_K152_interval_emitted", True)),
        ("erase-ceiling", lambda d: d.__setitem__("claim_ceiling", "The native floor is now known.")),
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
    print(f"K656 EXACT CONTROL: {sum(int(ok) for _, ok in baseline)}/{len(baseline)} pass")
    if "--selftest" in sys.argv:
        hostile = hostile_checks(data)
        for name, ok in hostile:
            print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
        print(f"HOSTILE SELFTEST: {sum(int(ok) for _, ok in hostile)}/{len(hostile)} caught")
        return 0 if all(ok for _, ok in baseline + hostile) and not failures else 1
    return 0 if all(ok for _, ok in baseline) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
