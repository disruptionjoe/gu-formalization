#!/usr/bin/env python3
"""Independent and hostile controls for K660."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k660_k500_boundary_translation_denominator_covariance.py")
MANIFEST = ROOT / "lab/process/k660-k500-boundary-translation-denominator-covariance.json"


def load_producer():
    spec = importlib.util.spec_from_file_location("k660_probe_producer", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K660 producer")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


P = load_producer()


def failures(data: dict) -> list[str]:
    out: list[str] = []
    theorem = data.get("translation_theorem", {})
    composition = data.get("composition", {})
    native = data.get("native_interface_status", {})
    if theorem.get("denominator_identity") != "D'_W(z)=W'-M'(z)=W-M(z)=D_W(z)":
        out.append("denominator")
    for key in ("reference_extension_unchanged", "reference_resolvent_level_unchanged", "friedrichs_status_preserved_if_previously_proved", "complete_denominator_order_unchanged", "same_coordinate_approximant_error_unchanged"):
        if theorem.get(key) is not True:
            out.append(key)
    for key in ("friedrichs_status_created_by_translation", "finite_impurity_translation_sufficient", "unbounded_translation_covered"):
        if theorem.get(key) is not False:
            out.append(key)
    if composition.get("K139_regulator_coordinates_already_authenticated_as_boundary_translation") is not False:
        out.append("native-authentication")
    denied = ("actual_native_boundary_triple_serialized", "actual_native_translation_law_proved", "actual_native_s_identified", "actual_native_denominator_serialized", "actual_native_d_n_identified", "actual_native_eta_n_identified", "actual_native_base_floor_r0_identified", "actual_native_target_b_identified", "native_global_m_identified", "native_remainder_alpha_delta_identified", "K473_released", "native_K152_interval_emitted")
    if any(native.get(key) is not False for key in denied):
        out.append("native-status")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("boundary-coordinate covariance", "D'=W'-M'=D", "cannot create", "No native s"):
        if token not in ceiling:
            out.append(f"ceiling:{token}")
    return out


def exact_checks(data: dict) -> list[tuple[str, bool]]:
    theorem = data["translation_theorem"]
    controls = data["exact_controls"]
    composition = data["composition"]
    return [
        ("producer and manifest agree", data == P.build()),
        ("bounded self-adjoint hypothesis is explicit", "bounded self-adjoint" in theorem["hypothesis"]),
        ("Gamma0 is unchanged", "Gamma_0'=Gamma_0" in theorem["boundary_maps"]),
        ("Gamma1 translation is explicit", "Gamma_1'=Gamma_1+C Gamma_0" in theorem["boundary_maps"]),
        ("Weyl translation is explicit", theorem["weyl_transform"] == "M'(z)=M(z)+C"),
        ("extension translation is explicit", theorem["extension_transform"] == "W'=W+C"),
        ("denominator identity is exact", theorem["denominator_identity"] == "D'_W(z)=W'-M'(z)=W-M(z)=D_W(z)"),
        ("reference extension is unchanged", theorem["reference_extension_unchanged"]),
        ("reference resolvent is unchanged", theorem["reference_resolvent_level_unchanged"]),
        ("Friedrichs status is preserved conditionally", theorem["friedrichs_status_preserved_if_previously_proved"]),
        ("translation does not create Friedrichs proof", not theorem["friedrichs_status_created_by_translation"]),
        ("finite impurity translation is insufficient", not theorem["finite_impurity_translation_sufficient"]),
        ("unbounded translation is excluded", not theorem["unbounded_translation_covered"]),
        ("exact denominator is invariant", controls["denominator_invariant"]),
        ("exact approximant is invariant", controls["approximant_denominator_invariant"]),
        ("operator error is invariant", controls["operator_norm_error_invariant"]),
        ("operator error is one fifth", controls["operator_norm_error"] == "1/5"),
        ("K659 obstruction is consumed", composition["K659_chart_floor_obstruction_consumed"]),
        ("K139 coordinates remain unauthenticated", not composition["K139_regulator_coordinates_already_authenticated_as_boundary_translation"]),
        ("native translation remains absent", not data["decision"]["native_translation_law_authenticated"]),
        ("native floor remains absent", not data["decision"]["native_floor_supplied"]),
        ("source and ledger stay unchanged", data["source_and_ledger_effect"] == "none"),
    ]


def hostile_checks(data: dict) -> list[tuple[str, bool]]:
    mutations = (
        ("break-denominator", lambda d: d["translation_theorem"].__setitem__("denominator_identity", "D'=D+C")),
        ("move-reference", lambda d: d["translation_theorem"].__setitem__("reference_extension_unchanged", False)),
        ("move-resolvent", lambda d: d["translation_theorem"].__setitem__("reference_resolvent_level_unchanged", False)),
        ("drop-friedrichs-preservation", lambda d: d["translation_theorem"].__setitem__("friedrichs_status_preserved_if_previously_proved", False)),
        ("create-friedrichs", lambda d: d["translation_theorem"].__setitem__("friedrichs_status_created_by_translation", True)),
        ("change-order", lambda d: d["translation_theorem"].__setitem__("complete_denominator_order_unchanged", False)),
        ("change-error", lambda d: d["translation_theorem"].__setitem__("same_coordinate_approximant_error_unchanged", False)),
        ("allow-impurity", lambda d: d["translation_theorem"].__setitem__("finite_impurity_translation_sufficient", True)),
        ("allow-unbounded", lambda d: d["translation_theorem"].__setitem__("unbounded_translation_covered", True)),
        ("authenticate-regulator", lambda d: d["composition"].__setitem__("K139_regulator_coordinates_already_authenticated_as_boundary_translation", True)),
        ("native-triple", lambda d: d["native_interface_status"].__setitem__("actual_native_boundary_triple_serialized", True)),
        ("native-translation", lambda d: d["native_interface_status"].__setitem__("actual_native_translation_law_proved", True)),
        ("native-s", lambda d: d["native_interface_status"].__setitem__("actual_native_s_identified", True)),
        ("native-denominator", lambda d: d["native_interface_status"].__setitem__("actual_native_denominator_serialized", True)),
        ("native-d", lambda d: d["native_interface_status"].__setitem__("actual_native_d_n_identified", True)),
        ("native-eta", lambda d: d["native_interface_status"].__setitem__("actual_native_eta_n_identified", True)),
        ("native-r0", lambda d: d["native_interface_status"].__setitem__("actual_native_base_floor_r0_identified", True)),
        ("native-b", lambda d: d["native_interface_status"].__setitem__("actual_native_target_b_identified", True)),
        ("native-m", lambda d: d["native_interface_status"].__setitem__("native_global_m_identified", True)),
        ("native-remainder", lambda d: d["native_interface_status"].__setitem__("native_remainder_alpha_delta_identified", True)),
        ("release-k473", lambda d: d["native_interface_status"].__setitem__("K473_released", True)),
        ("release-k152", lambda d: d["native_interface_status"].__setitem__("native_K152_interval_emitted", True)),
        ("erase-ceiling", lambda d: d.__setitem__("claim_ceiling", "Native denominator proved.")),
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
    print(f"K660 EXACT CONTROL: {sum(int(ok) for _, ok in baseline)}/{len(baseline)} pass")
    if "--selftest" in sys.argv:
        hostile = hostile_checks(data)
        for name, ok in hostile:
            print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
        print(f"HOSTILE SELFTEST: {sum(int(ok) for _, ok in hostile)}/{len(hostile)} caught")
        return 0 if all(ok for _, ok in baseline + hostile) and not manifest_failures else 1
    return 0 if all(ok for _, ok in baseline) and not manifest_failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
