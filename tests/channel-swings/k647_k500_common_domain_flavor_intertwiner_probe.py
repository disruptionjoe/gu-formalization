#!/usr/bin/env python3
"""Independent exact and hostile controls for K647."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k647-k500-common-domain-flavor-intertwiner.json"


def load_solver():
    path = Path(__file__).with_name("k647_k500_common_domain_flavor_intertwiner.py")
    spec = importlib.util.spec_from_file_location("k647_probe_solver", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


SOLVER = load_solver()


def failures(data: dict) -> list[str]:
    bad: list[str] = []
    theorem = data.get("intertwiner_theorem", {})
    dep = data.get("dependency_reconciliation", {})
    control = data.get("finite_exact_control", {})
    native = data.get("native_interface_status", {})
    if data.get("classification") != "INTERNAL_STRUCTURAL_ONLY" or data.get("direction") != "observed_to_native":
        bad.append("routing")
    required = ("free_domain_invariance", "same_form_identity", "complete_form_covariance")
    if any(not theorem.get(key) for key in required):
        bad.append("theorem")
    exact_prefixes = {
        "boundary_covariance": "JG=GJ",
        "chart_covariance": "JU=UJ",
        "inverse_covariance": "JS=SJ",
        "physical_gram_covariance": "JM=MJ",
        "base_pullback_covariance": "JR0=R0J",
        "reference_pullback_covariance": "J Delta R=Delta R J",
    }
    if any(not str(theorem.get(key, "")).startswith(prefix) for key, prefix in exact_prefixes.items()):
        bad.append("covariance_chain")
    if theorem.get("recursive_domain") != "D_K139=S Dom(H0)" or theorem.get("recursive_domain_invariance") != "J D_K139=D_K139":
        bad.append("domain")
    if control.get("all_exact_checks_pass") is not True or control.get("finite_regulator_control_only") is not True:
        bad.append("control")
    commute_keys = [key for key in control if key.startswith("J_commutes_with_")]
    if len(commute_keys) != 8 or any(control.get(key) is not True for key in commute_keys):
        bad.append("commutation")
    if dep.get("physical_flavor_symmetry_claimed") is not False or dep.get("source_selected_family_interpretation_claimed") is not False:
        bad.append("scope")
    required_true = ("actual_K139_recursive_domain_J_invariant", "actual_K139_K168_same_form_identity_J_invariant", "actual_physical_gram_J_invariant")
    if any(native.get(key) is not True for key in required_true):
        bad.append("native_true")
    required_false = ("actual_parity_compression_forms_serialized", "actual_parity_block_floors_identified", "actual_uniform_parity_tails_identified", "native_global_m_identified", "native_remainder_alpha_delta_identified", "K473_released", "native_K152_interval_emitted")
    if any(native.get(key) is not False for key in required_false):
        bad.append("native_ceiling")
    if data.get("source_and_ledger_effect") != "none":
        bad.append("ledger")
    ceiling = str(data.get("claim_ceiling", ""))
    for token in ("D_K139=S Dom(H0) is J invariant", "not physical family selection", "no parity block floor"):
        if token not in ceiling:
            bad.append(f"ceiling:{token}")
    return bad


def exact_checks(data: dict) -> list[tuple[str, bool]]:
    fresh = SOLVER.build()
    theorem = data["intertwiner_theorem"]
    control = data["finite_exact_control"]
    native = data["native_interface_status"]
    checks = [
        ("fresh theorem", fresh["intertwiner_theorem"] == theorem),
        ("fresh control", fresh["finite_exact_control"] == control),
        ("free domain", "Dom(H0)" in theorem["free_domain_invariance"]),
        ("boundary commute", theorem["boundary_covariance"].startswith("JG=GJ")),
        ("chart commute", theorem["chart_covariance"].startswith("JU=UJ")),
        ("inverse commute", theorem["inverse_covariance"].startswith("JS=SJ")),
        ("domain identity", theorem["recursive_domain"] == "D_K139=S Dom(H0)"),
        ("domain invariant", theorem["recursive_domain_invariance"] == "J D_K139=D_K139"),
        ("Gram invariant", theorem["physical_gram_covariance"].startswith("JM=MJ")),
        ("base pullback", theorem["base_pullback_identity"].startswith("R0=S*")),
        ("base covariance", theorem["base_pullback_covariance"].startswith("JR0=R0J")),
        ("reference pullback", theorem["reference_pullback_identity"] == "Delta R=S*W_ref S"),
        ("reference covariance", theorem["reference_pullback_covariance"].startswith("J Delta R=Delta R J")),
        ("same form", "single common" in theorem["same_form_identity"]),
        ("complete covariance", "a_ref" in theorem["complete_form_covariance"]),
        ("closed reduction", "(I+J)/2" in theorem["closed_form_consequence"]),
        ("seven-dimensional blocks", control["one_mode_charge_block_dimension_each"] == 7),
        ("fourteen-dimensional direct sum", control["direct_sum_dimension"] == 14),
        ("J self-adjoint", control["J_is_self_adjoint"] is True),
        ("J involutive", control["J_squared_is_identity"] is True),
        ("all finite checks", control["all_exact_checks_pass"] is True),
        ("finite scoped", control["finite_regulator_control_only"] is True),
        ("native domain", native["actual_K139_recursive_domain_J_invariant"] is True),
        ("native form", native["actual_K139_K168_same_form_identity_J_invariant"] is True),
        ("native Gram", native["actual_physical_gram_J_invariant"] is True),
        ("forms pending", native["actual_parity_compression_forms_serialized"] is False),
        ("floors pending", native["actual_parity_block_floors_identified"] is False),
        ("tails pending", native["actual_uniform_parity_tails_identified"] is False),
        ("m withheld", native["native_global_m_identified"] is False),
        ("remainder withheld", native["native_remainder_alpha_delta_identified"] is False),
        ("K473 withheld", native["K473_released"] is False),
        ("ledger unchanged", data["source_and_ledger_effect"] == "none"),
    ]
    return checks


def hostile_checks(data: dict) -> list[tuple[str, bool]]:
    updates = (
        ("erase free domain", lambda d: d["intertwiner_theorem"].__setitem__("free_domain_invariance", "")),
        ("break G", lambda d: d["intertwiner_theorem"].__setitem__("boundary_covariance", "unknown")),
        ("break U", lambda d: d["intertwiner_theorem"].__setitem__("chart_covariance", "unknown")),
        ("break S", lambda d: d["intertwiner_theorem"].__setitem__("inverse_covariance", "unknown")),
        ("wrong domain", lambda d: d["intertwiner_theorem"].__setitem__("recursive_domain", "Dom(H0)")),
        ("noninvariant domain", lambda d: d["intertwiner_theorem"].__setitem__("recursive_domain_invariance", "unknown")),
        ("break Gram", lambda d: d["intertwiner_theorem"].__setitem__("physical_gram_covariance", "unknown")),
        ("break base", lambda d: d["intertwiner_theorem"].__setitem__("base_pullback_covariance", "unknown")),
        ("break reference", lambda d: d["intertwiner_theorem"].__setitem__("reference_pullback_covariance", "unknown")),
        ("erase same form", lambda d: d["intertwiner_theorem"].__setitem__("same_form_identity", "")),
        ("finite failure", lambda d: d["finite_exact_control"].__setitem__("all_exact_checks_pass", False)),
        ("promote finite", lambda d: d["finite_exact_control"].__setitem__("finite_regulator_control_only", False)),
        ("break finite G", lambda d: d["finite_exact_control"].__setitem__("J_commutes_with_G", False)),
        ("claim physical", lambda d: d["dependency_reconciliation"].__setitem__("physical_flavor_symmetry_claimed", True)),
        ("claim source", lambda d: d["dependency_reconciliation"].__setitem__("source_selected_family_interpretation_claimed", True)),
        ("erase native domain", lambda d: d["native_interface_status"].__setitem__("actual_K139_recursive_domain_J_invariant", False)),
        ("erase native form", lambda d: d["native_interface_status"].__setitem__("actual_K139_K168_same_form_identity_J_invariant", False)),
        ("invent compressions", lambda d: d["native_interface_status"].__setitem__("actual_parity_compression_forms_serialized", True)),
        ("invent floors", lambda d: d["native_interface_status"].__setitem__("actual_parity_block_floors_identified", True)),
        ("invent tails", lambda d: d["native_interface_status"].__setitem__("actual_uniform_parity_tails_identified", True)),
        ("invent m", lambda d: d["native_interface_status"].__setitem__("native_global_m_identified", True)),
        ("invent remainder", lambda d: d["native_interface_status"].__setitem__("native_remainder_alpha_delta_identified", True)),
        ("release K473", lambda d: d["native_interface_status"].__setitem__("K473_released", True)),
        ("release K152", lambda d: d["native_interface_status"].__setitem__("native_K152_interval_emitted", True)),
        ("move ledger", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
        ("promote ceiling", lambda d: d.__setitem__("claim_ceiling", "physical family symmetry and floor proved")),
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
    print(f"K647 EXACT CONTROL: {sum(int(ok) for _, ok in baseline)}/{len(baseline)} pass")
    hostile = hostile_checks(data) if "--selftest" in sys.argv else []
    for name, ok in hostile:
        print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
    if hostile:
        print(f"HOSTILE SELFTEST: {sum(int(ok) for _, ok in hostile)}/{len(hostile)} caught")
    return 0 if all(ok for _, ok in baseline + hostile) and not manifest_failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
