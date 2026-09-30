#!/usr/bin/env python3
"""Independent hostile-mutation probe for K664."""

from __future__ import annotations

from copy import deepcopy
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
PRODUCER = HERE / "k664_k500_cofinal_effective_margin_transfer.py"


def load_producer():
    spec = importlib.util.spec_from_file_location("k664_producer", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K664 producer")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def rejected(module, payload, mutate) -> bool:
    candidate = deepcopy(payload)
    mutate(candidate)
    try:
        module.validate(candidate)
    except (AssertionError, KeyError, TypeError, ValueError):
        return True
    return False


def main() -> int:
    module = load_producer()
    payload = module.build()
    module.validate(payload)
    mutations = [
        lambda p: p["transfer_theorem"].__setitem__("same_complete_domain_required", False),
        lambda p: p["transfer_theorem"].__setitem__("complete_spectator_complement_required", False),
        lambda p: p["transfer_theorem"].__setitem__("finite_block_only_sufficient", True),
        lambda p: p["transfer_theorem"].__setitem__("sampled_sector_only_sufficient", True),
        lambda p: p["transfer_theorem"].__setitem__("uncontrolled_complement_allowed", True),
        lambda p: p["transfer_theorem"].__setitem__("one_sided_error_orientation_required", False),
        lambda p: p["exact_controls"].__setitem__("all_rows_positive", False),
        lambda p: p["exact_controls"].__setitem__("floors_monotone", False),
        lambda p: p["exact_controls"].__setitem__("floors", ["1/2"]),
        lambda p: p["exact_controls"].__setitem__("terminal_floor_matches_K663_control", False),
        lambda p: p["exact_controls"].__setitem__("finite_block_only_rejected", False),
        lambda p: p["exact_controls"].__setitem__("sampled_sector_only_rejected", False),
        lambda p: p["exact_controls"].__setitem__("uncontrolled_complement_rejected", False),
        lambda p: p["native_interface_status"].__setitem__("actual_native_cofinal_packet_identified", True),
        lambda p: p["native_interface_status"].__setitem__("named_complete_sector_floor_emitted", True),
        lambda p: p["composition"].__setitem__("native_effective_margin_packet_supplied", True),
        lambda p: p["decision"].__setitem__("native_floor_supplied", True),
        lambda p: p["exact_controls"].__setitem__("controls_are_synthetic", False),
        lambda p: p.__setitem__("source_and_ledger_effect", "changed"),
        lambda p: p.__setitem__("target_claim", "KILL"),
    ]
    caught = sum(rejected(module, payload, mutate) for mutate in mutations)
    assert caught == len(mutations)
    rows = payload["exact_controls"]["rows"]
    assert [row["A_lower"] for row in rows] == ["5/8", "11/16", "3/4"]
    assert [row["B_lower"] for row in rows] == ["17/32", "19/32", "21/32"]
    print(f"K664 independent probe: 24 controls passed; {caught}/{len(mutations)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
