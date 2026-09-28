#!/usr/bin/env python3
"""Independent controls and hostile mutations for K584."""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOLVER = Path(__file__).with_name("k584_k581_noncyclic_floor_identifiability.py")
MANIFEST = ROOT / "lab/process/k584-k581-noncyclic-floor-identifiability.json"


def load_solver():
    spec = importlib.util.spec_from_file_location("k584_probe_solver", SOLVER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


K584 = load_solver()


def checks(payload: dict) -> list[tuple[str, bool]]:
    theorem = payload.get("theorem", {})
    controls = payload.get("exact_controls", {})
    decision = payload.get("decision", {})
    rows = controls.get("family_rows", [])
    return [
        ("result id", payload.get("result_id") == "K584-K581-NONCYCLIC-FLOOR-IDENTIFIABILITY"),
        ("routing", payload.get("classification") == "INTERNAL_STRUCTURAL_ONLY" and payload.get("target_claim") == "NONE-NOT-A-KILL"),
        ("four rows", len(rows) == 4),
        ("fixed alpha", controls.get("all_rows_share_cyclic_floor") is True and len({row.get("cyclic_compression_floor_alpha") for row in rows}) == 1),
        ("fixed mu", controls.get("all_rows_share_cross_norm") is True and len({row.get("cyclic_noncyclic_cross_norm_mu") for row in rows}) == 1),
        ("all semibounded", controls.get("all_rows_semibounded") is True and all(row.get("shared_complete_sector_floor_valid") is True for row in rows)),
        ("shared floor", controls.get("one_explicit_shared_floor_control") == "-11" and all(row.get("shared_complete_sector_floor_control") == "-11" for row in rows)),
        ("distinct gamma", controls.get("noncyclic_floors_are_distinct") is True and len({row.get("noncyclic_compression_floor_gamma") for row in rows}) == 4),
        ("different target outcomes", controls.get("zero_target_outcomes_differ") is True and len({row.get("zero_target_positive_by_Schur_test") for row in rows}) > 1),
        ("identifiability language", "do not determine" in theorem.get("identifiability_conclusion", "")),
        ("not absence", "exists" in theorem.get("not_an_absence_theorem", "")),
        ("K581 preserved", decision.get("K581_existential_floor_preserved") is True),
        ("cyclic data insufficient", decision.get("K498_cyclic_floor_plus_K500_cross_determine_gamma") is False),
        ("r0 sufficient", decision.get("named_complete_sector_r0_would_supply_conservative_gamma") is True),
        ("r0 absent", decision.get("current_native_named_r0_serialized") is False),
        ("gamma absent", decision.get("current_native_named_gamma_emitted") is False),
        ("no downstream release", decision.get("K494_target_test_released") is False and decision.get("K473_native_beta_emitted") is False and decision.get("native_K152_interval_emitted") is False),
        ("no source move", payload.get("source_and_ledger_effect") == "none"),
    ]


def selftest(payload: dict) -> int:
    mutations = [
        ("drop row", lambda p: p["exact_controls"]["family_rows"].pop()),
        ("change alpha", lambda p: p["exact_controls"]["family_rows"][0].__setitem__("cyclic_compression_floor_alpha", "6")),
        ("change mu", lambda p: p["exact_controls"]["family_rows"][0].__setitem__("cyclic_noncyclic_cross_norm_mu", "2")),
        ("break semibound", lambda p: p["exact_controls"]["family_rows"][0].__setitem__("shared_complete_sector_floor_valid", False)),
        ("change shared floor", lambda p: p["exact_controls"]["family_rows"][0].__setitem__("shared_complete_sector_floor_control", "-10")),
        ("collapse gamma", lambda p: p["exact_controls"]["family_rows"][0].__setitem__("noncyclic_compression_floor_gamma", p["exact_controls"]["family_rows"][1]["noncyclic_compression_floor_gamma"])),
        ("collapse outcomes", lambda p: [row.__setitem__("zero_target_positive_by_Schur_test", True) for row in p["exact_controls"]["family_rows"]]),
        ("erase theorem", lambda p: p["theorem"].__setitem__("identifiability_conclusion", "gamma known")),
        ("claim absence", lambda p: p["theorem"].__setitem__("not_an_absence_theorem", "no floor")),
        ("invent determination", lambda p: p["decision"].__setitem__("K498_cyclic_floor_plus_K500_cross_determine_gamma", True)),
        ("erase r0 route", lambda p: p["decision"].__setitem__("named_complete_sector_r0_would_supply_conservative_gamma", False)),
        ("invent gamma", lambda p: p["decision"].__setitem__("current_native_named_gamma_emitted", True)),
        ("invent K152", lambda p: p["decision"].__setitem__("native_K152_interval_emitted", True)),
    ]
    caught = []
    for name, mutate in mutations:
        mutant = copy.deepcopy(payload)
        mutate(mutant)
        caught.append((name, not all(ok for _, ok in checks(mutant))))
    for name, ok in caught:
        print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
    print(f"K584 HOSTILE SELFTEST: {sum(ok for _, ok in caught)}/{len(caught)} caught")
    return 0 if all(ok for _, ok in caught) else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    payload = json.loads(MANIFEST.read_text())
    results = checks(payload)
    results.append(("deterministic rebuild", payload == K584.build()))
    for name, ok in results:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print(f"K584 controls: {sum(ok for _, ok in results)}/{len(results)}")
    if not all(ok for _, ok in results):
        return 1
    return selftest(payload) if args.selftest else 0


if __name__ == "__main__":
    raise SystemExit(main())
