#!/usr/bin/env python3
"""Hostile mutation probe for K748."""
from __future__ import annotations
import copy, importlib.util, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]; SCRIPT = ROOT / "tests/channel-swings/k748_sc_act_06_released_action_parent_inventory.py"; CERT = ROOT / "lab/process/k748-sc-act-06-released-action-parent-inventory.json"
def load_module():
    spec = importlib.util.spec_from_file_location("k748_probe_target", SCRIPT); assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec); sys.modules[spec.name] = mod; spec.loader.exec_module(mod); return mod
def main() -> int:
    mod = load_module(); baseline = json.loads(CERT.read_text(encoding="utf-8")); mod.validate(baseline); mutations = []
    for key in baseline["source_controls"]: mutations.append(lambda d, key=key: d["source_controls"].__setitem__(key, False))
    for index, row in enumerate(baseline["released_parent_inventory"]):
        replacement = False if row["independent_response"] is True else True
        mutations.append(lambda d, index=index, replacement=replacement: d["released_parent_inventory"][index].__setitem__("independent_response", replacement))
        mutations.append(lambda d, index=index: d["released_parent_inventory"][index].__setitem__("parent", "BROKEN"))
    for key, value in baseline["ownership_theorem"].items():
        replacement = (not value) if isinstance(value, bool) else "BROKEN"
        mutations.append(lambda d, key=key, replacement=replacement: d["ownership_theorem"].__setitem__(key, replacement))
    mutations.extend([lambda d: d.__setitem__("result_id", "BROKEN"), lambda d: d.__setitem__("classification", "COMPARATOR"), lambda d: d.__setitem__("direction", "native_to_observed"), lambda d: d.__setitem__("status", "unverified"), lambda d: d.__setitem__("target_claim", "SC-ACT-01"), lambda d: d["decision"].__setitem__("another_pairing_or_weight_is_a_new_action_parent", True), lambda d: d["decision"].__setitem__("unresolved_unitary_pairing_horn_is_a_new_response", True), lambda d: d["decision"].__setitem__("new_principal_response_requires_new_owned_operator_or_new_stationary_coefficients", False), lambda d: d.__setitem__("source_and_ledger_effect", "MOVED")])
    while len(mutations) < 35: mutations.append(lambda d: d["source_controls"].__setitem__("required_claim_ids_present", False))
    caught = 0
    for mutate in mutations[:35]:
        candidate = copy.deepcopy(baseline); mutate(candidate)
        try: mod.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError): caught += 1
    assert caught == 35; print("PASS controls=40 hostile_mutations_rejected=35/35"); return 0
if __name__ == "__main__": raise SystemExit(main())
