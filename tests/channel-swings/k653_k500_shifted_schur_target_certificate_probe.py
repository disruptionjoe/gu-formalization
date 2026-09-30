#!/usr/bin/env python3
"""Independent and hostile controls for K653."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k653_k500_shifted_schur_target_certificate.py")
MANIFEST = ROOT / "lab/process/k653-k500-shifted-schur-target-certificate.json"


def load_producer():
    spec = importlib.util.spec_from_file_location("k653_probe_producer", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K653 producer")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


P = load_producer()


def manifest_failures(data: dict) -> list[str]:
    failures: list[str] = []
    theorem = data.get("shifted_schur_theorem", {})
    controls = data.get("exact_controls", {})
    native = data.get("native_interface_status", {})
    if theorem.get("theta_endpoint_allowed") is not True or theorem.get("same_domain_required") is not True:
        failures.append("domain-endpoint")
    if theorem.get("separately_singular_raw_rows_required") is not False or theorem.get("absolute_A_D_K_serialization_required") is not False:
        failures.append("topology")
    if controls.get("synthetic_not_native") is not True or controls.get("observed_pattern") != [True, True, False, False]:
        failures.append("controls")
    if native.get("shifted_target_certificate_shape_complete") is not True:
        failures.append("certificate")
    denied = (
        "actual_native_target_b_identified", "actual_native_shifted_diagonal_positivity_proved",
        "actual_native_shifted_cross_contraction_proved", "native_global_m_identified",
        "native_remainder_alpha_delta_identified", "K473_released", "native_K152_interval_emitted",
    )
    if any(native.get(key) is not False for key in denied):
        failures.append("native-status")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("shifted-Schur", "prescribed b", "No native target b", "No K473"):
        if token not in ceiling:
            failures.append(f"claim-ceiling:{token}")
    return failures


def exact_checks(data: dict) -> list[tuple[str, bool]]:
    theorem = data["shifted_schur_theorem"]
    controls = data["exact_controls"]
    native = data["native_interface_status"]
    return [
        ("producer and manifest agree", data == P.build()),
        ("strict control passes", controls["strict_pass"]["target_floor_certified"]),
        ("endpoint control passes", controls["endpoint_pass"]["target_floor_certified"]),
        ("endpoint theta square is one", controls["endpoint_pass"]["theta_square"] == "1"),
        ("excessive cross fails", not controls["excessive_cross_fail"]["target_floor_certified"]),
        ("negative shifted diagonal fails", not controls["negative_shifted_diagonal_fail"]["target_floor_certified"]),
        ("sharp scalar inequality is stated", "|c|^2<=" in theorem["scalar_sharp_iff"]),
        ("theta endpoint is allowed", theorem["theta_endpoint_allowed"]),
        ("same domain is required", theorem["same_domain_required"]),
        ("singular raw rows are not required", not theorem["separately_singular_raw_rows_required"]),
        ("absolute envelopes are not required", not theorem["absolute_A_D_K_serialization_required"]),
        ("direct route closes abstractly", data["decision"]["direct_target_route_closed_abstractly"]),
        ("K652 route stays valid", data["decision"]["K652_absolute_envelope_route_remains_valid"]),
        ("native target is not emitted", not data["decision"]["native_target_floor_emitted"]),
        ("certificate shape is complete", native["shifted_target_certificate_shape_complete"]),
        ("native shifted positivity is absent", not native["actual_native_shifted_diagonal_positivity_proved"]),
        ("native shifted contraction is absent", not native["actual_native_shifted_cross_contraction_proved"]),
        ("native m remains absent", not native["native_global_m_identified"]),
        ("K473 stays closed", not native["K473_released"]),
        ("source and ledger stay unchanged", data["source_and_ledger_effect"] == "none"),
    ]


def hostile_checks(data: dict) -> list[tuple[str, bool]]:
    mutations = (
        ("erase-endpoint", lambda d: d["shifted_schur_theorem"].__setitem__("theta_endpoint_allowed", False)),
        ("erase-domain", lambda d: d["shifted_schur_theorem"].__setitem__("same_domain_required", False)),
        ("require-raw", lambda d: d["shifted_schur_theorem"].__setitem__("separately_singular_raw_rows_required", True)),
        ("require-envelopes", lambda d: d["shifted_schur_theorem"].__setitem__("absolute_A_D_K_serialization_required", True)),
        ("promote-control", lambda d: d["exact_controls"].__setitem__("synthetic_not_native", False)),
        ("break-pattern", lambda d: d["exact_controls"].__setitem__("observed_pattern", [True] * 4)),
        ("erase-certificate", lambda d: d["native_interface_status"].__setitem__("shifted_target_certificate_shape_complete", False)),
        ("invent-target", lambda d: d["native_interface_status"].__setitem__("actual_native_target_b_identified", True)),
        ("invent-positivity", lambda d: d["native_interface_status"].__setitem__("actual_native_shifted_diagonal_positivity_proved", True)),
        ("invent-contraction", lambda d: d["native_interface_status"].__setitem__("actual_native_shifted_cross_contraction_proved", True)),
        ("invent-m", lambda d: d["native_interface_status"].__setitem__("native_global_m_identified", True)),
        ("invent-alpha", lambda d: d["native_interface_status"].__setitem__("native_remainder_alpha_delta_identified", True)),
        ("release-K473", lambda d: d["native_interface_status"].__setitem__("K473_released", True)),
        ("release-K152", lambda d: d["native_interface_status"].__setitem__("native_K152_interval_emitted", True)),
        ("erase-ceiling", lambda d: d.__setitem__("claim_ceiling", "The native target is three.")),
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
    print(f"K653 EXACT CONTROL: {sum(int(ok) for _, ok in baseline)}/{len(baseline)} pass")
    if "--selftest" in sys.argv:
        hostile = hostile_checks(data)
        for name, ok in hostile:
            print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
        print(f"HOSTILE SELFTEST: {sum(int(ok) for _, ok in hostile)}/{len(hostile)} caught")
        return 0 if all(ok for _, ok in baseline + hostile) and not failures else 1
    return 0 if all(ok for _, ok in baseline) and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
