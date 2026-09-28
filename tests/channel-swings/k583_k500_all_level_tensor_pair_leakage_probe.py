#!/usr/bin/env python3
"""Independent controls and hostile mutations for K583."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOLVER = Path(__file__).with_name("k583_k500_all_level_tensor_pair_leakage.py")
MANIFEST = ROOT / "lab/process/k583-k500-all-level-tensor-pair-leakage.json"


def load_solver():
    spec = importlib.util.spec_from_file_location("k583_probe_solver", SOLVER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K583 = load_solver()


def checks(payload: dict) -> list[tuple[str, bool]]:
    theorem = payload.get("theorem", {})
    typing = payload.get("native_exchange_typing", {})
    controls = payload.get("exact_controls", {})
    decision = payload.get("decision", {})
    rows = typing.get("K177_rows", [])
    return [
        ("result id", payload.get("result_id") == "K583-K500-ALL-LEVEL-TENSOR-PAIR-LEAKAGE"),
        ("routing", payload.get("classification") == "INTERNAL_STRUCTURAL_ONLY" and payload.get("target_claim") == "NONE-NOT-A-KILL"),
        ("tensor formula", "tensor" in theorem.get("tensor_pair_identity", "")),
        ("self-adjoint orientation", "self-adjoint" in theorem.get("self_adjoint_orientation", "")),
        ("no word lower", theorem.get("word_norm_lower_not_required") is True),
        ("no diagonal assumption", theorem.get("diagonal_multiplier_not_required") is True),
        ("three controls", controls.get("row_count") == 3),
        ("tensor controls", controls.get("all_tensor_identities_pass") is True),
        ("shift controls", controls.get("all_scalar_shift_controls_pass") is True),
        ("exchange control", controls.get("off_diagonal_exchange_control_present") is True),
        ("K501 replay", controls.get("K501_diagonal_value_replayed") is True),
        ("zero replay", controls.get("reducing_line_zero_replayed") is True),
        ("two native rows", len(rows) == 2 and [row.get("charge") for row in rows] == [[0, 0], [1, 0]]),
        ("level one exchange free", typing.get("level_one_exchange_free_for_q00_q10") is True and all(row.get("order_1_matched_exchange_coordinates") == 0 for row in rows)),
        ("higher exchange live", typing.get("higher_exchange_coordinates_present_for_q00_q10") is True and all(row.get("orders_2_through_12_matched_exchange_coordinates", 0) > 0 for row in rows)),
        ("K580 preserved", typing.get("K580_first_level_result_preserved") is True),
        ("no multiplier overextension", typing.get("K580_scalar_multiplier_formula_extended_unchanged_to_all_levels") is False),
        ("identity emitted", decision.get("native_all_level_leakage_identity_emitted") is True),
        ("multiplier assumption rejected", decision.get("higher_level_multiplier_assumption_rejected") is True),
        ("no numeric uniform bound", decision.get("actual_uniform_tensor_pair_upper_emitted") is False and decision.get("complete_K500_uniform_leakage_emitted") is False),
        ("no floor or K152", decision.get("noncyclic_floor_emitted") is False and decision.get("native_K152_interval_emitted") is False),
        ("no source move", payload.get("source_and_ledger_effect") == "none"),
    ]


def selftest(payload: dict) -> int:
    mutations = [
        ("erase tensor identity", lambda p: p["theorem"].__setitem__("tensor_pair_identity", "variance")),
        ("require diagonal", lambda p: p["theorem"].__setitem__("diagonal_multiplier_not_required", False)),
        ("break tensor control", lambda p: p["exact_controls"].__setitem__("all_tensor_identities_pass", False)),
        ("erase exchange control", lambda p: p["exact_controls"].__setitem__("off_diagonal_exchange_control_present", False)),
        ("change K501 value", lambda p: p["exact_controls"].__setitem__("K501_diagonal_value_replayed", False)),
        ("drop native row", lambda p: p["native_exchange_typing"]["K177_rows"].pop()),
        ("invent order one exchange", lambda p: p["native_exchange_typing"]["K177_rows"][0].__setitem__("order_1_matched_exchange_coordinates", 1)),
        ("erase higher exchange", lambda p: p["native_exchange_typing"]["K177_rows"][0].__setitem__("orders_2_through_12_matched_exchange_coordinates", 0)),
        ("overextend multiplier", lambda p: p["native_exchange_typing"].__setitem__("K580_scalar_multiplier_formula_extended_unchanged_to_all_levels", True)),
        ("invent uniform bound", lambda p: p["decision"].__setitem__("complete_K500_uniform_leakage_emitted", True)),
        ("invent K152", lambda p: p["decision"].__setitem__("native_K152_interval_emitted", True)),
    ]
    caught = []
    for name, mutate in mutations:
        mutant = copy.deepcopy(payload)
        mutate(mutant)
        caught.append((name, not all(ok for _, ok in checks(mutant))))
    for name, ok in caught:
        print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
    print(f"K583 HOSTILE SELFTEST: {sum(ok for _, ok in caught)}/{len(caught)} caught")
    return 0 if all(ok for _, ok in caught) else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    payload = json.loads(MANIFEST.read_text())
    results = checks(payload)
    results.append(("deterministic rebuild", payload == K583.build()))
    for name, ok in results:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print(f"K583 controls: {sum(ok for _, ok in results)}/{len(results)}")
    if not all(ok for _, ok in results):
        return 1
    return selftest(payload) if args.selftest else 0


if __name__ == "__main__":
    raise SystemExit(main())
