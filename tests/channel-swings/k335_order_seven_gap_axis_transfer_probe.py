#!/usr/bin/env python3
"""Independent replay and hostile controls for K335."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE = Path(__file__).with_name("k335_order_seven_gap_axis_transfer.py")
MANIFEST = ROOT / "lab/process/k335-order-seven-gap-axis-transfer.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k335_probe_backend", MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K335 module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rejected(module, payload, mutate) -> bool:
    candidate = copy.deepcopy(payload)
    mutate(candidate)
    try:
        module.validate_payload(candidate)
    except (AssertionError, ValueError):
        return True
    return False


def main() -> int:
    module = load_module()
    stored = json.loads(MANIFEST.read_text())
    replay = module.build()
    if replay != stored:
        raise AssertionError("K335 deterministic replay failed")
    module.validate_payload(replay)
    checks = {
        "orders": stored["fixed_control"]["extended_scaled_derivative_orders"] == [7, 8],
        "five_axes": stored["fixed_control"]["gap_axes"] == ["t0", "t1", "t2", "t3", "t4"],
        "exact": stored["order_seven_eight_scaled_envelopes"]["all_bounds_exact_rational"],
        "controls": stored["order_seven_eight_scaled_envelopes"]["all_controls_contained"],
        "checksum": stored["release_test"]["K334_checksum_replayed_on_every_axis"],
        "no_promotion": stored["numerical_transfer_gate"]["structural_template_counts_are_not_numerical_constants"],
        "four_missing": len(stored["numerical_transfer_gate"]["missing_executable_fields"]) == 4,
        "no_gap_constants": not stored["decision"]["complete_gap_axis_constants_emitted"],
        "no_k294": not stored["decision"]["k294_gamma_join_released"],
    }
    if not all(checks.values()):
        raise AssertionError(f"K335 independent checks failed: {checks}")
    mutations = (
        lambda p: p["fixed_control"].__setitem__("extended_scaled_derivative_orders", [7]),
        lambda p: p["fixed_control"]["gap_axes"].pop(),
        lambda p: p["order_seven_eight_scaled_envelopes"].__setitem__("all_bounds_exact_rational", False),
        lambda p: p["order_seven_eight_scaled_envelopes"].__setitem__("raw_Bessel_evaluation_at_zero_used", True),
        lambda p: p["order_seven_eight_scaled_envelopes"].__setitem__("all_controls_contained", False),
        lambda p: p["axis_transfer"][0].__setitem__("shared_geometry_reuse_released", False),
        lambda p: p["numerical_transfer_gate"].__setitem__("axis_native_numeric_entry_jet_map_serialized", True),
        lambda p: p["numerical_transfer_gate"].__setitem__("missing_executable_fields", []),
        lambda p: p["numerical_transfer_gate"].__setitem__("structural_template_counts_are_not_numerical_constants", False),
        lambda p: p["decision"].__setitem__("complete_gap_axis_constants_emitted", True),
        lambda p: p["decision"].__setitem__("complete_six_axis_peano_norm_emitted", True),
        lambda p: p["decision"].__setitem__("k294_gamma_join_released", True),
    )
    hostile = [rejected(module, stored, mutate) for mutate in mutations]
    if not all(hostile):
        raise AssertionError(f"K335 hostile controls escaped: {hostile}")
    print(f"K335 probe passed {len(checks)}/{len(checks)} checks and rejected {len(hostile)}/{len(hostile)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
