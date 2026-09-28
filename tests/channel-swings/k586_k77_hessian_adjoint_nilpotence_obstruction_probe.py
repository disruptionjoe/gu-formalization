#!/usr/bin/env python3
"""Independent checks and hostile mutations for K586."""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "lab/process/k586-k77-hessian-adjoint-nilpotence-obstruction.json"


def checks(payload):
    test = payload.get("exact_adjoint_test", {})
    decision = payload.get("decision", {})
    return [
        ("result id", payload.get("result_id") == "K586-K77-HESSIAN-ADJOINT-NILPOTENCE-OBSTRUCTION"),
        ("routing", payload.get("classification") == "BRIDGE_OR_SEMANTIC_BOUNDARY" and payload.get("target_claim") == "NONE-NOT-A-KILL"),
        ("block", test.get("block_shape") == [1470, 91] and test.get("block_rank") == 91),
        ("Gram shape", test.get("gram_shape") == [91, 91]),
        ("Gram full rank", test.get("gram_rank") == 91 and test.get("gram_nonzero_entries") == 91),
        ("scalar identity", test.get("gram_is_scalar_identity") is True and test.get("gram_scalar") == "50/257049"),
        ("positive", test.get("positive_definite_over_reals") is True),
        ("not nilpotent", test.get("gram_is_zero") is False and test.get("nilpotence_holds") is False),
        ("reverse rank", test.get("reverse_composition_rank") == 91),
        ("specified rejection", decision.get("canonical_adjoint_completion_rejected") is True),
        ("source preserved", decision.get("source_action_rejected") is False),
        ("completion ceiling", decision.get("all_bv_kt_completions_rejected") is False),
        ("no ledger move", payload.get("source_and_ledger_context", {}).get("ledger_effect") == "none"),
    ]


def selftest(payload):
    mutations = [
        ("drop rank", lambda p: p["exact_adjoint_test"].__setitem__("gram_rank", 90)),
        ("zero Gram", lambda p: p["exact_adjoint_test"].__setitem__("gram_is_zero", True)),
        ("claim nilpotence", lambda p: p["exact_adjoint_test"].__setitem__("nilpotence_holds", True)),
        ("change scalar", lambda p: p["exact_adjoint_test"].__setitem__("gram_scalar", "0")),
        ("lose positivity", lambda p: p["exact_adjoint_test"].__setitem__("positive_definite_over_reals", False)),
        ("accept adjoint", lambda p: p["decision"].__setitem__("canonical_adjoint_completion_rejected", False)),
        ("reject action", lambda p: p["decision"].__setitem__("source_action_rejected", True)),
        ("reject all", lambda p: p["decision"].__setitem__("all_bv_kt_completions_rejected", True)),
    ]
    results = []
    for name, mutate in mutations:
        mutant = copy.deepcopy(payload)
        mutate(mutant)
        results.append((name, not all(ok for _, ok in checks(mutant))))
    for name, ok in results:
        print(f"[{'PASS' if ok else 'FAIL'}] hostile mutation {name}")
    print(f"K586 HOSTILE SELFTEST: {sum(ok for _, ok in results)}/{len(results)} caught")
    return 0 if all(ok for _, ok in results) else 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    payload = json.loads(MANIFEST.read_text(encoding="utf-8"))
    results = checks(payload)
    for name, ok in results:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print(f"K586 controls: {sum(ok for _, ok in results)}/{len(results)}")
    if not all(ok for _, ok in results):
        return 1
    return selftest(payload) if args.selftest else 0


if __name__ == "__main__":
    raise SystemExit(main())
