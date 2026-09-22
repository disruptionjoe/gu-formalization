#!/usr/bin/env python3
"""Independent replay and hostile controls for K317."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE = Path(__file__).with_name("k317_order_seven_boundary_coefficient_discriminator.py")
MANIFEST = ROOT / "lab/process/k317-order-seven-boundary-coefficient-discriminator.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k317_probe_backend", MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K317 module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rejected(module, payload, mutate) -> bool:
    candidate = copy.deepcopy(payload)
    mutate(candidate)
    try:
        module.validate_payload(candidate)
    except AssertionError:
        return True
    return False


def main() -> int:
    module = load_module()
    expected = json.loads(MANIFEST.read_text())
    replay = module.build()
    if replay != expected:
        raise AssertionError("K317 deterministic replay failed")
    checks = {
        "twenty_one_families": replay["release_test"]["all_twenty_one_families_consumed"],
        "fifteen_second_families": replay["release_test"]["all_fifteen_second_derivative_families_present"],
        "split_obstruction": replay["release_test"]["terminal_pointwise_obstruction_replayed"],
        "weighted_repair": replay["release_test"]["weighted_terminal_repair_replayed"],
        "log_obstruction": replay["release_test"]["endpoint_log_obstruction_explicit"],
        "no_divergence_claim": not replay["pointwise_discriminator"]["complete_functional_divergence_claimed"],
        "no_cancellation_claim": not replay["pointwise_discriminator"]["coherent_cancellation_ruled_out"],
        "pointwise_rejected": replay["decision"]["K316_proposed_pointwise_factorization_rejected"],
        "weighted_route": replay["decision"]["weighted_complete_chart_route_required"],
        "no_y_constant": not replay["decision"]["complete_y_master_constant_emitted"],
        "no_gap_release": not replay["decision"]["five_gap_axis_transfer_released"],
        "no_gamma_release": not replay["decision"]["k294_gamma_join_released"],
    }
    if not all(checks.values()):
        raise AssertionError(f"K317 independent checks failed: {checks}")
    mutations = [
        lambda x: x["fixed_control"].__setitem__("bordered_family_count", 20),
        lambda x: x["fixed_control"].__setitem__("second_derivative_family_count", 14),
        lambda x: x["pointwise_discriminator"].__setitem__("second_y_derivative_pointwise_supremum", "finite"),
        lambda x: x["pointwise_discriminator"].__setitem__("complete_functional_divergence_claimed", True),
        lambda x: x["pointwise_discriminator"].__setitem__("coherent_cancellation_ruled_out", True),
        lambda x: x["decision"].__setitem__("full_boundary_pointwise_coefficient_exists", True),
        lambda x: x["decision"].__setitem__("weighted_complete_chart_route_required", False),
        lambda x: x["decision"].__setitem__("complete_y_master_constant_emitted", True),
        lambda x: x["decision"].__setitem__("five_gap_axis_transfer_released", True),
    ]
    hostile = [rejected(module, expected, mutation) for mutation in mutations]
    if not all(hostile):
        raise AssertionError(f"K317 hostile controls escaped: {hostile}")
    print(f"K317 probe passed {len(checks)}/{len(checks)} checks and rejected {len(hostile)}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
