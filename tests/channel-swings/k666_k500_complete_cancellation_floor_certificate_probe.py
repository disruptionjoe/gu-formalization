#!/usr/bin/env python3
"""Independent hostile-mutation probe for K666."""

from __future__ import annotations

from copy import deepcopy
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
PRODUCER = HERE / "k666_k500_complete_cancellation_floor_certificate.py"


def load_producer():
    spec = importlib.util.spec_from_file_location("k666_producer", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K666 producer")
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
        lambda p: p["certificate_theorem"].__setitem__("K647_common_domain_required", False),
        lambda p: p["certificate_theorem"].__setitem__("K648_both_total_parities_required", False),
        lambda p: p["certificate_theorem"].__setitem__("K665_finite_rows_and_two_tails_required", False),
        lambda p: p["certificate_theorem"].__setitem__("matched_trace_same_domain_required", False),
        lambda p: p["certificate_theorem"].__setitem__("finite_prefix_only_sufficient", True),
        lambda p: p["certificate_theorem"].__setitem__("one_parity_only_sufficient", True),
        lambda p: p["certificate_theorem"].__setitem__("uncontrolled_complement_allowed", True),
        lambda p: p["exact_control"].__setitem__("B_arrives_from_K665", False),
        lambda p: p["exact_control"].__setitem__("positive_floor_test_passes", False),
        lambda p: p["exact_control"].__setitem__("matches_K663_sharp_control", False),
        lambda p: p["exact_control"].__setitem__("certified_floor", "1/4"),
        lambda p: p["exact_control"]["endpoint_control"].__setitem__("zero_endpoint_passes", False),
        lambda p: p["exact_control"].__setitem__("negative_determinant_rejected", False),
        lambda p: p["exact_control"].__setitem__("controls_are_synthetic", False),
        lambda p: p["dependency_reconciliation"].__setitem__("K647_common_domain_identity_consumed", False),
        lambda p: p["dependency_reconciliation"].__setitem__("K665_parity_cofinal_B_consumed", False),
        lambda p: p["native_interface_status"].__setitem__("native_complete_floor_emitted", True),
        lambda p: p["decision"].__setitem__("native_floor_supplied", True),
        lambda p: p.__setitem__("source_and_ledger_effect", "changed"),
        lambda p: p.__setitem__("target_claim", "KILL"),
    ]
    caught = sum(rejected(module, payload, mutate) for mutate in mutations)
    assert caught == len(mutations)
    assert payload["exact_control"]["determinant_margin"] == "125/256"
    assert payload["exact_control"]["endpoint_control"]["certified_floor"] == "0"
    print(f"K666 independent probe: 24 controls passed; {caught}/{len(mutations)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
