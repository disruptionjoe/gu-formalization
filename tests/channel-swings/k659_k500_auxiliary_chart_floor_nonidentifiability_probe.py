#!/usr/bin/env python3
"""Independent and hostile controls for K659."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k659_k500_auxiliary_chart_floor_nonidentifiability.py")
MANIFEST = ROOT / "lab/process/k659-k500-auxiliary-chart-floor-nonidentifiability.json"


def load_producer():
    spec = importlib.util.spec_from_file_location("k659_probe_producer", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K659 producer")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


P = load_producer()


def failures(data: dict) -> list[str]:
    out: list[str] = []
    theorem = data.get("compensated_chart_theorem", {})
    semibound = data.get("semiboundedness_nonidentifiability", {})
    native = data.get("native_interface_status", {})
    for key in ("lambda_256_is_native_floor", "arbitrarily_large_chart_shift_improves_floor", "chart_contraction_implies_positive_operator"):
        if theorem.get(key) is not False:
            out.append(key)
    if theorem.get("same_target_operator_required") is not True:
        out.append("same-target")
    if semibound.get("numerical_s_identified") is not False or semibound.get("best_floor_identified") is not False:
        out.append("numerical-floor")
    if semibound.get("fixed_native_operator_has_no_floor") is not False:
        out.append("native-no-floor")
    denied = ("actual_native_s_identified", "actual_native_denominator_serialized", "actual_native_base_floor_r0_identified", "actual_native_target_b_identified", "native_global_m_identified", "native_remainder_alpha_delta_identified", "K473_released", "native_K152_interval_emitted")
    if any(native.get(key) is not False for key in denied):
        out.append("native-status")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("compensated auxiliary", "lambda=256", "does not say the fixed native operator lacks a floor", "No native s"):
        if token not in ceiling:
            out.append(f"ceiling:{token}")
    return out


def exact_checks(data: dict) -> list[tuple[str, bool]]:
    theorem = data["compensated_chart_theorem"]
    semibound = data["semiboundedness_nonidentifiability"]
    controls = data["exact_controls"]
    chart = controls["chart_rows"]
    rows = controls["semibounded_rows"]
    return [
        ("producer and manifest agree", data == P.build()),
        ("K139 compensation is explicit", "held fixed" in theorem["K139_identity"]),
        ("same operator is required", theorem["same_target_operator_required"]),
        ("lambda 256 is rejected as floor", not theorem["lambda_256_is_native_floor"]),
        ("larger chart does not improve floor", not theorem["arbitrarily_large_chart_shift_improves_floor"]),
        ("contraction is not positivity", not theorem["chart_contraction_implies_positive_operator"]),
        ("three chart controls exist", len(chart) == 3),
        ("chart controls share one floor", controls["chart_rows_preserve_one_floor"]),
        ("displayed 256 is tested", chart[1]["auxiliary_chart_shift"] == "256"),
        ("displayed 256 does not match floor", controls["displayed_256_rejected_as_floor"]),
        ("semiboundedness retains existence", "there exists" in semibound["existence_consequence"]),
        ("numerical s remains absent", not semibound["numerical_s_identified"]),
        ("best floor remains absent", not semibound["best_floor_identified"]),
        ("three qualitative controls exist", len(rows) == 3),
        ("qualitative interface is shared", controls["qualitative_rows_share_interface"]),
        ("control floors differ", controls["qualitative_rows_have_distinct_floors"]),
        ("fixed native no-floor is refused", not semibound["fixed_native_operator_has_no_floor"]),
        ("native floor remains absent", not data["decision"]["native_floor_supplied"]),
        ("K660 is named as repair", "K660" in data["decision"]["next_exact_input"]),
        ("source and ledger stay unchanged", data["source_and_ledger_effect"] == "none"),
    ]


def hostile_checks(data: dict) -> list[tuple[str, bool]]:
    mutations = (
        ("promote-256", lambda d: d["compensated_chart_theorem"].__setitem__("lambda_256_is_native_floor", True)),
        ("improve-floor", lambda d: d["compensated_chart_theorem"].__setitem__("arbitrarily_large_chart_shift_improves_floor", True)),
        ("infer-positive", lambda d: d["compensated_chart_theorem"].__setitem__("chart_contraction_implies_positive_operator", True)),
        ("change-target", lambda d: d["compensated_chart_theorem"].__setitem__("same_target_operator_required", False)),
        ("invent-s", lambda d: d["semiboundedness_nonidentifiability"].__setitem__("numerical_s_identified", True)),
        ("invent-best-floor", lambda d: d["semiboundedness_nonidentifiability"].__setitem__("best_floor_identified", True)),
        ("deny-native-floor", lambda d: d["semiboundedness_nonidentifiability"].__setitem__("fixed_native_operator_has_no_floor", True)),
        ("native-s", lambda d: d["native_interface_status"].__setitem__("actual_native_s_identified", True)),
        ("native-denominator", lambda d: d["native_interface_status"].__setitem__("actual_native_denominator_serialized", True)),
        ("native-r0", lambda d: d["native_interface_status"].__setitem__("actual_native_base_floor_r0_identified", True)),
        ("native-b", lambda d: d["native_interface_status"].__setitem__("actual_native_target_b_identified", True)),
        ("native-m", lambda d: d["native_interface_status"].__setitem__("native_global_m_identified", True)),
        ("native-remainder", lambda d: d["native_interface_status"].__setitem__("native_remainder_alpha_delta_identified", True)),
        ("release-k473", lambda d: d["native_interface_status"].__setitem__("K473_released", True)),
        ("release-k152", lambda d: d["native_interface_status"].__setitem__("native_K152_interval_emitted", True)),
        ("erase-ceiling", lambda d: d.__setitem__("claim_ceiling", "Native floor proved.")),
    )
    caught = []
    for name, mutate in mutations:
        mutant = copy.deepcopy(data)
        mutate(mutant)
        caught.append((name, bool(failures(mutant))))
    return caught


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    baseline = exact_checks(data)
    for name, ok in baseline:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    manifest_failures = failures(data)
    for failure in manifest_failures:
        print(f"[FAIL] manifest {failure}")
    print(f"K659 EXACT CONTROL: {sum(int(ok) for _, ok in baseline)}/{len(baseline)} pass")
    if "--selftest" in sys.argv:
        hostile = hostile_checks(data)
        for name, ok in hostile:
            print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
        print(f"HOSTILE SELFTEST: {sum(int(ok) for _, ok in hostile)}/{len(hostile)} caught")
        return 0 if all(ok for _, ok in baseline + hostile) and not manifest_failures else 1
    return 0 if all(ok for _, ok in baseline) and not manifest_failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
