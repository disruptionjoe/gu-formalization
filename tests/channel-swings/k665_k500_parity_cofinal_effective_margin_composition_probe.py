#!/usr/bin/env python3
"""Independent hostile-mutation probe for K665."""

from __future__ import annotations

from copy import deepcopy
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
PRODUCER = HERE / "k665_k500_parity_cofinal_effective_margin_composition.py"


def load_producer():
    spec = importlib.util.spec_from_file_location("k665_producer", PRODUCER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K665 producer")
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
        lambda p: p["composition_theorem"].__setitem__("complete_domain_required", False),
        lambda p: p["composition_theorem"].__setitem__("both_total_parities_required", False),
        lambda p: p["composition_theorem"].__setitem__("all_finite_rows_through_N_required", False),
        lambda p: p["composition_theorem"].__setitem__("independent_tail_for_each_parity_required", False),
        lambda p: p["composition_theorem"].__setitem__("same_effective_form_required", False),
        lambda p: p["composition_theorem"].__setitem__("finite_prefix_only_sufficient", True),
        lambda p: p["composition_theorem"].__setitem__("sampled_sectors_only_sufficient", True),
        lambda p: p["composition_theorem"].__setitem__("uncontrolled_complement_allowed", True),
        lambda p: p["exact_control"].__setitem__("global_B_lower", "3/4"),
        lambda p: p["exact_control"].__setitem__("matches_K663_control_B", False),
        lambda p: p["exact_control"].__setitem__("weakest_row_is_minus_tail", False),
        lambda p: p["exact_control"].__setitem__("controls_are_synthetic", False),
        lambda p: p["exact_control"]["finite_prefix_counterexample"].__setitem__("destroys_global_lower", False),
        lambda p: p["dependency_reconciliation"].__setitem__("K647_common_domain_identity_consumed", False),
        lambda p: p["dependency_reconciliation"].__setitem__("K648_total_parity_forms_consumed", False),
        lambda p: p["dependency_reconciliation"].__setitem__("K651_finite_prefix_obstruction_respected", False),
        lambda p: p["native_interface_status"].__setitem__("actual_complete_B_lower_identified", True),
        lambda p: p["decision"].__setitem__("native_B_supplied", True),
        lambda p: p.__setitem__("source_and_ledger_effect", "changed"),
        lambda p: p.__setitem__("target_claim", "KILL"),
    ]
    caught = sum(rejected(module, payload, mutate) for mutate in mutations)
    assert caught == len(mutations)
    assert payload["exact_control"]["plus_lower"] == "11/16"
    assert payload["exact_control"]["minus_lower"] == "21/32"
    print(f"K665 independent probe: 24 controls passed; {caught}/{len(mutations)} hostile mutations rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
