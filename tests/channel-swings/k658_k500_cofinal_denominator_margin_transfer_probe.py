#!/usr/bin/env python3
"""Independent and hostile controls for K658."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k658_k500_cofinal_denominator_margin_transfer.py")
MANIFEST = ROOT / "lab/process/k658-k500-cofinal-denominator-margin-transfer.json"


def load_producer():
    spec = importlib.util.spec_from_file_location("k658_probe_producer", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K658 producer")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


P = load_producer()


def failures(data: dict) -> list[str]:
    out: list[str] = []
    theorem = data.get("cofinal_margin_theorem", {})
    native = data.get("native_interface_status", {})
    if theorem.get("order_consequence") != "D(-s)>=(d_N-eta_N)I":
        out.append("order")
    for key in ("same_s_required", "same_extension_coordinate_required", "self_adjointness_required", "complete_boundary_coverage_required"):
        if theorem.get(key) is not True:
            out.append(key)
    for key in ("finite_impurity_only_sufficient", "sectorwise_pointwise_convergence_sufficient", "uncontrolled_complement_sufficient"):
        if theorem.get(key) is not False:
            out.append(key)
    denied = (
        "actual_native_s_identified", "actual_native_d_n_identified", "actual_native_eta_n_identified",
        "actual_complete_boundary_coverage_proved", "actual_native_denominator_nonnegative",
        "actual_native_base_floor_r0_identified", "actual_native_target_b_identified",
        "native_global_m_identified", "native_remainder_alpha_delta_identified",
        "K473_released", "native_K152_interval_emitted",
    )
    if any(native.get(key) is not False for key in denied):
        out.append("native-status")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("complete-space cofinal", "d_N-eta_N", "r0=-s", "Finite impurity blocks", "No native s"):
        if token not in ceiling:
            out.append(f"ceiling:{token}")
    return out


def exact_checks(data: dict) -> list[tuple[str, bool]]:
    theorem = data["cofinal_margin_theorem"]
    controls = data["exact_controls"]
    rows = controls["rows"]
    return [
        ("producer and manifest agree", data == P.build()),
        ("complete approximant order is named", "complete boundary space" in theorem["approximant_hypothesis"]),
        ("complete norm error is named", "same complete boundary space" in theorem["error_hypothesis"]),
        ("margin transfer is sharp", theorem["order_consequence"] == "D(-s)>=(d_N-eta_N)I"),
        ("zero margin is admitted", not theorem["strict_margin_required"]),
        ("same s is required", theorem["same_s_required"]),
        ("same coordinate is required", theorem["same_extension_coordinate_required"]),
        ("complete coverage is required", theorem["complete_boundary_coverage_required"]),
        ("finite impurity is insufficient", not theorem["finite_impurity_only_sufficient"]),
        ("pointwise sectors are insufficient", not theorem["sectorwise_pointwise_convergence_sufficient"]),
        ("four controls are present", len(rows) == 4),
        ("two controls accept", controls["accepted_rows"] == 2),
        ("two controls reject", controls["rejected_rows"] == 2),
        ("zero transferred margin accepts", rows[1]["transferred_margin_d_n_minus_eta_n"] == "0" and rows[1]["certificate_accepts"]),
        ("negative transferred margin rejects", rows[2]["transferred_margin_d_n_minus_eta_n"] == "-1/8" and not rows[2]["certificate_accepts"]),
        ("uncontrolled complement rejects", rows[3]["transferred_margin_d_n_minus_eta_n"] == "9" and not rows[3]["certificate_accepts"]),
        ("K657 is consumed", data["composition"]["K657_equivalence_consumed"] == "A_W>=lambda iff D_W(lambda)>=0"),
        ("K656 target is composed", data["composition"]["K656_consequence"].startswith("b=-s-2")),
        ("native packet remains absent", not data["decision"]["native_cofinal_packet_supplied"]),
        ("source and ledger stay unchanged", data["source_and_ledger_effect"] == "none"),
    ]


def hostile_checks(data: dict) -> list[tuple[str, bool]]:
    mutations = (
        ("break-order", lambda d: d["cofinal_margin_theorem"].__setitem__("order_consequence", "D>=d+eta")),
        ("change-s", lambda d: d["cofinal_margin_theorem"].__setitem__("same_s_required", False)),
        ("change-coordinate", lambda d: d["cofinal_margin_theorem"].__setitem__("same_extension_coordinate_required", False)),
        ("drop-selfadjoint", lambda d: d["cofinal_margin_theorem"].__setitem__("self_adjointness_required", False)),
        ("drop-coverage", lambda d: d["cofinal_margin_theorem"].__setitem__("complete_boundary_coverage_required", False)),
        ("accept-impurity", lambda d: d["cofinal_margin_theorem"].__setitem__("finite_impurity_only_sufficient", True)),
        ("accept-pointwise", lambda d: d["cofinal_margin_theorem"].__setitem__("sectorwise_pointwise_convergence_sufficient", True)),
        ("accept-complement", lambda d: d["cofinal_margin_theorem"].__setitem__("uncontrolled_complement_sufficient", True)),
        ("invent-s", lambda d: d["native_interface_status"].__setitem__("actual_native_s_identified", True)),
        ("invent-d", lambda d: d["native_interface_status"].__setitem__("actual_native_d_n_identified", True)),
        ("invent-eta", lambda d: d["native_interface_status"].__setitem__("actual_native_eta_n_identified", True)),
        ("invent-coverage", lambda d: d["native_interface_status"].__setitem__("actual_complete_boundary_coverage_proved", True)),
        ("invent-positive", lambda d: d["native_interface_status"].__setitem__("actual_native_denominator_nonnegative", True)),
        ("invent-r0", lambda d: d["native_interface_status"].__setitem__("actual_native_base_floor_r0_identified", True)),
        ("invent-b", lambda d: d["native_interface_status"].__setitem__("actual_native_target_b_identified", True)),
        ("invent-m", lambda d: d["native_interface_status"].__setitem__("native_global_m_identified", True)),
        ("invent-remainder", lambda d: d["native_interface_status"].__setitem__("native_remainder_alpha_delta_identified", True)),
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
    print(f"K658 EXACT CONTROL: {sum(int(ok) for _, ok in baseline)}/{len(baseline)} pass")
    if "--selftest" in sys.argv:
        hostile = hostile_checks(data)
        for name, ok in hostile:
            print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
        print(f"HOSTILE SELFTEST: {sum(int(ok) for _, ok in hostile)}/{len(hostile)} caught")
        return 0 if all(ok for _, ok in baseline + hostile) and not manifest_failures else 1
    return 0 if all(ok for _, ok in baseline) and not manifest_failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
