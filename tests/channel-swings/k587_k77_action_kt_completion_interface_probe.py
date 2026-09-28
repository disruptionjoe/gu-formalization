#!/usr/bin/env python3
"""Independent checks and hostile mutations for K587."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOLVER = Path(__file__).with_name("k587_k77_action_kt_completion_interface.py")
MANIFEST = ROOT / "lab/process/k587-k77-action-kt-completion-interface.json"


def load_solver():
    spec = importlib.util.spec_from_file_location("k587_probe_solver", SOLVER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K587 = load_solver()


def checks(payload):
    base = payload.get("base_completion_interface", {})
    lift = payload.get("corrected_carrier_lift", {})
    control = payload.get("logical_control", {})
    decision = payload.get("decision", {})
    return [
        ("result id", payload.get("result_id") == "K587-K77-ACTION-KT-COMPLETION-INTERFACE"),
        ("routing", payload.get("classification") == "BRIDGE_OR_SEMANTIC_BOUNDARY" and payload.get("target_claim") == "NONE-NOT-A-KILL"),
        ("base dimensions", base.get("dimensions") == {"H": 21, "Q": 91, "M": 70, "R": 1470}),
        ("B rank", base.get("observed_B_rank") == 91),
        ("required ranks", base.get("required_D1_rank") == 70 and base.get("required_D2_rank") == 21),
        ("kernel", base.get("required_kernel_dimension_if_D1_surjective") == 21),
        ("nilpotence equation", base.get("required_nilpotence_equation") == "(L B) D2 = 0"),
        ("no invented coefficients", base.get("B_injective_is_sufficient_to_select_L") is False and base.get("coefficient_bearing_inputs_present") is False),
        ("control works", control.get("D1_D2_zero") is True and control.get("rank_D2") == 21 and control.get("rank_D1") == 70),
        ("control fenced", control.get("control_is_action_derived") is False),
        ("lift dimensions", lift.get("degree_dimensions") == [10752, 46592, 35840]),
        ("lift ranks", lift.get("required_product_D2_rank") == 10752 and lift.get("required_product_D1_rank") == 35840),
        ("typed squares retained", lift.get("nonfactorized_action_requires_K444_typed_square_checks") is True and lift.get("K444_square_count") == 2),
        ("interface derived", decision.get("minimal_completion_interface_derived") is True),
        ("completion open", decision.get("selected_action_completion_constructed") is False),
        ("source preserved", decision.get("source_action_rejected") is False),
        ("no ledger move", payload.get("source_and_ledger_context", {}).get("ledger_effect") == "none"),
    ]


def selftest(payload):
    mutations = [
        ("change D1 rank", lambda p: p["base_completion_interface"].__setitem__("required_D1_rank", 69)),
        ("change D2 rank", lambda p: p["base_completion_interface"].__setitem__("required_D2_rank", 20)),
        ("invent L selection", lambda p: p["base_completion_interface"].__setitem__("B_injective_is_sufficient_to_select_L", True)),
        ("invent coefficients", lambda p: p["base_completion_interface"].__setitem__("coefficient_bearing_inputs_present", True)),
        ("promote control", lambda p: p["logical_control"].__setitem__("control_is_action_derived", True)),
        ("change lift", lambda p: p["corrected_carrier_lift"].__setitem__("required_product_D1_rank", 35839)),
        ("drop typed squares", lambda p: p["corrected_carrier_lift"].__setitem__("nonfactorized_action_requires_K444_typed_square_checks", False)),
        ("claim completion", lambda p: p["decision"].__setitem__("selected_action_completion_constructed", True)),
        ("reject source", lambda p: p["decision"].__setitem__("source_action_rejected", True)),
    ]
    results = []
    for name, mutate in mutations:
        mutant = copy.deepcopy(payload)
        mutate(mutant)
        results.append((name, not all(ok for _, ok in checks(mutant))))
    for name, ok in results:
        print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
    print(f"K587 HOSTILE SELFTEST: {sum(ok for _, ok in results)}/{len(results)} caught")
    return 0 if all(ok for _, ok in results) else 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    payload = json.loads(MANIFEST.read_text(encoding="utf-8"))
    results = checks(payload)
    results.append(("deterministic rebuild", payload == K587.build()))
    for name, ok in results:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print(f"K587 controls: {sum(ok for _, ok in results)}/{len(results)}")
    if not all(ok for _, ok in results):
        return 1
    return selftest(payload) if args.selftest else 0


if __name__ == "__main__":
    raise SystemExit(main())
