#!/usr/bin/env python3
"""Exact inertia/coefficient controls for the frozen K104-to-K155 bridge."""
from __future__ import annotations

import copy
import json
import pathlib
import sys


ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k104-k91-k155-action-bridge-obstruction-wave.json"
K155 = ROOT / "lab/process/selected-k155-null-fivefold-third-lower.json"


def finite_checks(data, k155, mutation=None):
    k104_static_coefficients = [(mode + 1) ** 2 for mode in range(448)]
    k104_inertia = [
        sum(value > 0 for value in k104_static_coefficients),
        sum(value < 0 for value in k104_static_coefficients),
        sum(value == 0 for value in k104_static_coefficients),
    ]
    k155_inertia = list(k155["exact_result"]["distortion_lowerer_inertia"])
    if mutation == "erase_negative_directions":
        k155_inertia = [448, 0, 0]
    has_weyl = data["coefficient_test"]["k104_has_same_order_A0"]
    if mutation == "invent_weyl_owner":
        has_weyl = True
    fixture_leak = k155["exact_result"]["rotated_metric_radical_leakage_rank"]
    if mutation == "erase_fixture_leak":
        fixture_leak = 0
    planted_coefficients = [1] * 260 + [-1] * 188
    planted_inertia = [
        sum(value > 0 for value in planted_coefficients),
        sum(value < 0 for value in planted_coefficients),
        sum(value == 0 for value in planted_coefficients),
    ]
    checks = [
        ("K104 can dimensionally embed a 448-vector test packet", data["same_carrier_test"]["dimension_only_embedding"] == "first_448_K104_physical_modes_exists"),
        ("K104 first-448 static energy inertia is positive definite", k104_inertia == [448, 0, 0]),
        ("K155 distortion lowerer has the frozen mixed inertia", k155_inertia == [260, 188, 0]),
        ("the two inertia triples differ", k104_inertia != k155_inertia),
        ("real congruence cannot preserve mismatched inertia", data["same_carrier_test"]["inertia_match"] is False and k104_inertia != k155_inertia),
        ("the obstruction is not mere dimension mismatch", sum(k104_inertia) == sum(k155_inertia) == 448),
        ("a planted 260/188 split removes this discriminator only", planted_inertia == k155_inertia),
        ("K104 owns no curvature or Weyl input", data["coefficient_test"]["k104_has_curvature_or_Weyl_input"] is False),
        ("K104 owns no same-order A0 coefficient", has_weyl is False),
        ("K104 cannot reproduce the Weyl-owned leakage", data["coefficient_test"]["k104_can_reproduce_K155_Weyl_leakage"] is False and not has_weyl),
        ("K104 cannot supply an action-owned same-order correction", data["coefficient_test"]["k104_can_supply_action_owned_same_order_correction"] is False),
        ("fixture recomputation is not licensed", data["coefficient_test"]["K155_fixture_recomputation_licensed"] is False),
        ("K155 rotated metric-radical leakage remains rank one", fixture_leak == 1),
        ("K155 Weyl zero-order bridge remains rank nine", k155["exact_result"]["bridge_zero_order_rank"] == 9),
        ("K155 reference leakage remains zero", k155["exact_result"]["reference_metric_radical_leakage_rank"] == 0),
        ("the preserved verdict names the Weyl zero-order owner", "Weyl_zero_order_term" in data["result"]["preserved_K155_verdict"]),
        ("the result does not change source action custody", data["result"]["source_action_change"] == "none"),
        ("the result does not change canon", data["result"]["canon_verdict_change"] == "none"),
        ("the exact reopener requires a new action rather than a basis rename", "new demand-derived action" in data["exact_reopener"] and "changing basis" in data["exact_reopener"]),
    ]
    return checks


def manifest_failures(data):
    failures = []
    same = data.get("same_carrier_test", {})
    coeff = data.get("coefficient_test", {})
    result = data.get("result", {})
    if same.get("k104_first_448_static_inertia") != [448, 0, 0] or same.get("k155_distortion_inertia") != [260, 188, 0] or same.get("inertia_match") is not False:
        failures.append("inertia")
    required_false = ("k104_has_curvature_or_Weyl_input", "k104_has_same_order_A0", "k104_can_reproduce_K155_Weyl_leakage", "k104_can_supply_action_owned_same_order_correction", "K155_fixture_recomputation_licensed")
    if any(coeff.get(key) is not False for key in required_false):
        failures.append("coefficient")
    if result.get("K155_branch_verdict_changed") is not False or result.get("source_action_change") != "none" or result.get("canon_verdict_change") != "none":
        failures.append("ceilings")
    if "No obstruction to all actions" not in data.get("claim_ceiling", ""):
        failures.append("claim_ceiling")
    return failures


def selftest(data, k155):
    baseline = finite_checks(data, k155)
    if not all(ok for _, ok in baseline) or manifest_failures(data):
        print("BASELINE RED: hostile selftest refused")
        return 1
    mutations = [(name, any(not ok for _, ok in finite_checks(data, k155, name))) for name in (
        "erase_negative_directions", "invent_weyl_owner", "erase_fixture_leak",
    )]
    updates = (
        ("match_inertia", lambda d: d["same_carrier_test"].__setitem__("inertia_match", True)),
        ("wrong_k104_inertia", lambda d: d["same_carrier_test"].__setitem__("k104_first_448_static_inertia", [260, 188, 0])),
        ("wrong_k155_inertia", lambda d: d["same_carrier_test"].__setitem__("k155_distortion_inertia", [448, 0, 0])),
        ("invent_curvature", lambda d: d["coefficient_test"].__setitem__("k104_has_curvature_or_Weyl_input", True)),
        ("invent_A0", lambda d: d["coefficient_test"].__setitem__("k104_has_same_order_A0", True)),
        ("invent_reproduction", lambda d: d["coefficient_test"].__setitem__("k104_can_reproduce_K155_Weyl_leakage", True)),
        ("invent_correction", lambda d: d["coefficient_test"].__setitem__("k104_can_supply_action_owned_same_order_correction", True)),
        ("license_fixture", lambda d: d["coefficient_test"].__setitem__("K155_fixture_recomputation_licensed", True)),
        ("change_branch", lambda d: d["result"].__setitem__("K155_branch_verdict_changed", True)),
        ("source_promotion", lambda d: d["result"].__setitem__("source_action_change", "promoted")),
        ("canon_promotion", lambda d: d["result"].__setitem__("canon_verdict_change", "changed")),
        ("universalize", lambda d: d.__setitem__("claim_ceiling", "all actions fail")),
    )
    for name, update in updates:
        mutant = copy.deepcopy(data)
        update(mutant)
        mutations.append((name, bool(manifest_failures(mutant))))
    for name, caught in mutations:
        print(f"[{'PASS' if caught else 'FAIL'}] hostile mutation {name}")
    print(f"HOSTILE SELFTEST: {sum(caught for _, caught in mutations)}/{len(mutations)} caught")
    return 0 if all(caught for _, caught in mutations) else 1


def main():
    data = json.loads(MANIFEST.read_text())
    k155 = json.loads(K155.read_text())
    if "--selftest" in sys.argv:
        return selftest(data, k155)
    checks = finite_checks(data, k155)
    checks.append(("manifest preserves the inertia, coefficient and claim ceilings", not manifest_failures(data)))
    for label, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    print(f"K104 K91/K155 ACTION BRIDGE: {sum(ok for _, ok in checks)}/{len(checks)} pass")
    return 0 if all(ok for _, ok in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
