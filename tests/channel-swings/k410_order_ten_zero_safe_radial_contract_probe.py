#!/usr/bin/env python3
"""Deterministic replay and hostile controls for K410."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PRODUCER = Path(__file__).with_name("k410_order_ten_zero_safe_radial_contract.py")
STORED = ROOT / "lab/process/k410-order-ten-zero-safe-radial-contract.json"


def load():
    spec = importlib.util.spec_from_file_location("k410_probe_target", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K410 producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load()
    stored = json.loads(STORED.read_text())
    if stored != module.build():
        raise AssertionError("deterministic K410 replay differs")
    checks = [
        stored["fixed_control"]["raw_time_axes"] == 22,
        stored["fixed_control"]["raw_kernel_factors_per_gram_entry"] == 12,
        stored["scaled_bessel_bank"]["continuous_zero_limits"] == ["2", "2", "4"],
        not stored["scaled_bessel_bank"]["raw_Bessel_evaluation_at_zero_used"],
        stored["scaled_bessel_bank"]["all_bounds_exact_rational"],
        all(row["contained"] for row in stored["peano_majorant"]["controls"]),
        stored["all_zero_radial_ledger"]["complete_second_derivative_degree"] == -14,
        stored["all_zero_radial_ledger"]["final_radial_degree"] == 9,
        stored["all_zero_radial_ledger"]["origin_integrable"],
        not stored["decision"]["complete_hybrid_integrals_emitted"],
    ]
    if not all(checks):
        raise AssertionError("K410 control failed")
    mutations = [
        lambda p: p["fixed_control"].__setitem__("raw_time_axes", 21),
        lambda p: p["fixed_control"].__setitem__("raw_kernel_factors_per_gram_entry", 11),
        lambda p: p["scaled_bessel_bank"].__setitem__("raw_Bessel_evaluation_at_zero_used", True),
        lambda p: p["scaled_bessel_bank"].__setitem__("all_bounds_exact_rational", False),
        lambda p: p["scaled_bessel_bank"].__setitem__("continuous_zero_limits", ["2", "2", "3"]),
        lambda p: p["peano_majorant"]["controls"][0].__setitem__("contained", False),
        lambda p: p["all_zero_radial_ledger"].__setitem__("final_radial_degree", 8),
        lambda p: p["all_zero_radial_ledger"].__setitem__("origin_integrable", False),
        lambda p: p["decision"].__setitem__("all_zero_origin_integrability_closed", False),
        lambda p: p["decision"].__setitem__("partial_face_preconditioners_emitted", True),
        lambda p: p["decision"].__setitem__("complete_hybrid_integrals_emitted", True),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(stored)
        mutate(candidate)
        try:
            module.validate_payload(candidate)
        except AssertionError:
            rejected += 1
    if rejected != len(mutations):
        raise AssertionError(f"K410 hostile rejection changed: {rejected}/{len(mutations)}")
    print(f"K410 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
