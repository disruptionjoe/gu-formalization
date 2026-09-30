#!/usr/bin/env python3
"""Independent and hostile controls for K655."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k655_k500_shifted_target_custody_obstruction.py")
MANIFEST = ROOT / "lab/process/k655-k500-shifted-target-custody-obstruction.json"


def load_producer():
    spec = importlib.util.spec_from_file_location("k655_probe_producer", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K655 producer")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


P = load_producer()


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    theorem = data.get("interface_theorem", {})
    controls = data.get("exact_controls", {})
    native = data.get("native_interface_status", {})
    if theorem.get("all_finite_targets_defeated_over_interface_class") is not True:
        failures.append("interface-obstruction")
    if theorem.get("fixed_native_operator_proved_unbounded_below") is not False:
        failures.append("native-overclaim")
    if theorem.get("actual_native_sector_row_identified") is not False:
        failures.append("row-overclaim")
    if controls.get("same_interface_not_native") is not True or controls.get("all_rows_fail_first_shifted_diagonal") is not True:
        failures.append("controls")
    denied = (
        "actual_native_target_b_identified", "actual_native_shifted_diagonal_positivity_proved",
        "actual_native_shifted_cross_contraction_proved", "native_global_m_identified",
        "native_remainder_alpha_delta_identified", "K473_released", "native_K152_interval_emitted",
    )
    if any(native.get(key) is not False for key in denied):
        failures.append("native-status")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("data-custody obstruction", "same-interface control", "not sectors", "No native b"):
        if token not in ceiling:
            failures.append(f"claim-ceiling:{token}")
    return failures


def exact_checks(data: dict) -> list[tuple[str, bool]]:
    theorem = data["interface_theorem"]
    controls = data["exact_controls"]
    native = data["native_interface_status"]
    rows = controls["rows"]
    return [
        ("producer and manifest agree", data == P.build()),
        ("five target controls are present", controls["target_count"] == 5),
        ("every shifted gap is negative", all(P.Fraction(row["shifted_gap"]) < 0 for row in rows)),
        ("every row flags the first failure", all(row["first_K653_hypothesis_fails"] for row in rows)),
        ("very negative target is defeated", rows[0]["target_b"] == "-100" and rows[0]["shifted_gap"] == "-5"),
        ("positive target is defeated", rows[-1]["target_b"] == "5/4" and P.Fraction(rows[-1]["shifted_gap"]) < 0),
        ("interface class is the quantified scope", theorem["all_finite_targets_defeated_over_interface_class"]),
        ("fixed operator is not declared unbounded", not theorem["fixed_native_operator_proved_unbounded_below"]),
        ("actual native row is not claimed", not theorem["actual_native_sector_row_identified"]),
        ("new estimate remains a reopener", theorem["new_same_domain_estimate_can_reopen"]),
        ("K653 is consumed", data["decision"]["K653_consumed"]),
        ("current custody selects no target", not data["decision"]["current_custody_selects_numerical_target"]),
        ("target guessing is rejected", not data["decision"]["another_target_guess_before_new_native_evidence_is_decision_grade"]),
        ("K612 is sharpened", native["K612_custody_obstruction_sharpened_to_K653"]),
        ("native target remains absent", not native["actual_native_target_b_identified"]),
        ("native shifted positivity remains absent", not native["actual_native_shifted_diagonal_positivity_proved"]),
        ("native shifted contraction remains absent", not native["actual_native_shifted_cross_contraction_proved"]),
        ("native m remains absent", not native["native_global_m_identified"]),
        ("K473 stays closed", not native["K473_released"]),
        ("source and ledger stay unchanged", data["source_and_ledger_effect"] == "none"),
    ]


def hostile_checks(data: dict) -> list[tuple[str, bool]]:
    mutations = (
        ("erase-interface", lambda d: d["interface_theorem"].__setitem__("all_finite_targets_defeated_over_interface_class", False)),
        ("invent-unbounded", lambda d: d["interface_theorem"].__setitem__("fixed_native_operator_proved_unbounded_below", True)),
        ("invent-native-row", lambda d: d["interface_theorem"].__setitem__("actual_native_sector_row_identified", True)),
        ("promote-control", lambda d: d["exact_controls"].__setitem__("same_interface_not_native", False)),
        ("break-controls", lambda d: d["exact_controls"].__setitem__("all_rows_fail_first_shifted_diagonal", False)),
        ("invent-target", lambda d: d["native_interface_status"].__setitem__("actual_native_target_b_identified", True)),
        ("invent-positivity", lambda d: d["native_interface_status"].__setitem__("actual_native_shifted_diagonal_positivity_proved", True)),
        ("invent-contraction", lambda d: d["native_interface_status"].__setitem__("actual_native_shifted_cross_contraction_proved", True)),
        ("invent-m", lambda d: d["native_interface_status"].__setitem__("native_global_m_identified", True)),
        ("invent-alpha", lambda d: d["native_interface_status"].__setitem__("native_remainder_alpha_delta_identified", True)),
        ("release-K473", lambda d: d["native_interface_status"].__setitem__("K473_released", True)),
        ("release-K152", lambda d: d["native_interface_status"].__setitem__("native_K152_interval_emitted", True)),
        ("erase-ceiling", lambda d: d.__setitem__("claim_ceiling", "The native operator is unbounded below.")),
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
    print(f"K655 EXACT CONTROL: {sum(int(ok) for _, ok in baseline)}/{len(baseline)} pass")
    if "--selftest" in sys.argv:
        hostile = hostile_checks(data)
        for name, ok in hostile:
            print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
        print(f"HOSTILE SELFTEST: {sum(int(ok) for _, ok in hostile)}/{len(hostile)} caught")
        return 0 if all(ok for _, ok in baseline + hostile) and not failures else 1
    return 0 if all(ok for _, ok in baseline) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
