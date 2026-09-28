#!/usr/bin/env python3
"""Independent replay and hostile mutations for K602."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
MANIFEST = ROOT / "lab/process/k602-k500-order-two-numerical-moment-enclosure.json"


def load():
    spec = importlib.util.spec_from_file_location("k602_probe_target", HERE / "k602_k500_order_two_numerical_moment_enclosure.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def verify(payload):
    assert payload["result_id"] == "K602-K500-ORDER-TWO-NUMERICAL-MOMENT-ENCLOSURE"
    assert payload["target_claim"] == "NONE-NOT-A-KILL"
    analytic = payload["analytic_reduction"]
    assert analytic["coordinatewise_positive_and_decreasing"] and analytic["b_reused_without_requadrature"]
    c = payload["outward_evaluation"]
    assert c["positive_quadrant_cells"] == 60516 and c["mesh_octaves"] == 40
    n0, n1 = map(Decimal, c["n_interval"])
    a0, a1 = map(Decimal, c["a_interval"])
    b0, b1 = map(Decimal, c["b_interval_reused_from_K180"])
    assert Decimal(0) < n0 <= n1 and Decimal(0) < a0 <= a1 and Decimal(0) < b0 <= b1
    assert a1 * a1 <= n1 * b1 and c["cauchy_consistency"]
    q00 = list(map(Decimal, c["q00_truncation_leakage_square_interval"]))
    q10 = list(map(Decimal, c["q10_q01_truncation_leakage_square_interval"]))
    diff = list(map(Decimal, c["q10_minus_q00_interval"]))
    assert Decimal(0) <= q00[0] <= q00[1]
    assert Decimal(0) < q10[0] <= q10[1]
    assert Decimal(0) < diff[0] <= diff[1]
    assert q10[0] == Decimal(c["q10_strict_lower_uses_cauchy"])
    seeds = payload["seed_moment_intervals"]
    assert seeds["q10"] == seeds["q01"]
    assert Decimal(seeds["q00"]["A_2"][0]) > 0 and Decimal(seeds["q10"]["A_2"][1]) < 0
    decision = payload["decision"]
    assert decision["K601_order_two_moments_numerically_enclosed"]
    assert decision["K180_exchange_norm_reused_once"]
    assert decision["q10_q01_order_two_leakage_strictly_positive_numerically"]
    assert not decision["complete_finite_K456_moments_emitted"]
    assert not decision["complete_K500_uniform_leakage_emitted"]
    assert not decision["native_noncyclic_floor_emitted"]
    assert not decision["K473_released"] and not decision["native_K152_interval_emitted"]
    assert payload["source_and_ledger_effect"] == "none"
    assert "truncation" in payload["claim_ceiling"] and "Higher-order interference" in payload["claim_ceiling"]


def main() -> int:
    module = load()
    stored = json.loads(MANIFEST.read_text())
    replay = module.build()
    assert replay == stored
    checks = [
        stored["result_id"] == "K602-K500-ORDER-TWO-NUMERICAL-MOMENT-ENCLOSURE",
        stored["outward_evaluation"]["positive_quadrant_cells"] == 60516,
        stored["analytic_reduction"]["b_reused_without_requadrature"],
        stored["decision"]["K601_order_two_moments_numerically_enclosed"],
        stored["decision"]["q10_q01_order_two_leakage_strictly_positive_numerically"],
    ]
    mutations = [
        ("result_id", lambda p: p.__setitem__("result_id", "wrong")),
        ("target", lambda p: p.__setitem__("target_claim", "SC-ACT-06")),
        ("monotonicity", lambda p: p["analytic_reduction"].__setitem__("coordinatewise_positive_and_decreasing", False)),
        ("recompute b", lambda p: p["analytic_reduction"].__setitem__("b_reused_without_requadrature", False)),
        ("cell count", lambda p: p["outward_evaluation"].__setitem__("positive_quadrant_cells", 1)),
        ("n sign", lambda p: p["outward_evaluation"].__setitem__("n_interval", ["-1", "1"])),
        ("a order", lambda p: p["outward_evaluation"].__setitem__("a_interval", ["2", "1"])),
        ("b order", lambda p: p["outward_evaluation"].__setitem__("b_interval_reused_from_K180", ["2", "1"])),
        ("cauchy", lambda p: p["outward_evaluation"].__setitem__("cauchy_consistency", False)),
        ("q10 zero", lambda p: p["outward_evaluation"].__setitem__("q10_q01_truncation_leakage_square_interval", ["0", "1"])),
        ("q10 lower", lambda p: p["outward_evaluation"].__setitem__("q10_strict_lower_uses_cauchy", "0")),
        ("charge conjugation", lambda p: p["seed_moment_intervals"].__setitem__("q01", {})),
        ("q00 sign", lambda p: p["seed_moment_intervals"]["q00"].__setitem__("A_2", ["-1", "-1"])),
        ("numeric decision", lambda p: p["decision"].__setitem__("K601_order_two_moments_numerically_enclosed", False)),
        ("uniform overclaim", lambda p: p["decision"].__setitem__("complete_K500_uniform_leakage_emitted", True)),
        ("floor overclaim", lambda p: p["decision"].__setitem__("native_noncyclic_floor_emitted", True)),
        ("K473 overclaim", lambda p: p["decision"].__setitem__("K473_released", True)),
        ("ledger effect", lambda p: p.__setitem__("source_and_ledger_effect", "changed")),
        ("ceiling", lambda p: p.__setitem__("claim_ceiling", "complete theorem")),
    ]
    caught = 0
    for _, mutate in mutations:
        candidate = copy.deepcopy(stored)
        mutate(candidate)
        try:
            verify(candidate)
        except AssertionError:
            caught += 1
    verify(stored)
    assert all(checks) and caught == len(mutations)
    print(f"K602 EXACT CONTROL: {len(checks)}/{len(checks)} pass")
    print(f"K602 HOSTILE SELFTEST: {caught}/{len(mutations)} mutations caught")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
