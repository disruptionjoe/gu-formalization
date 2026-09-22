#!/usr/bin/env python3
"""Independent replay and hostile controls for K315."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE = Path(__file__).with_name("k315_order_seven_terminal_bordered_adapter.py")
MANIFEST = ROOT / "lab/process/k315-order-seven-terminal-bordered-adapter.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k315_probe_backend", MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K315 module")
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
        raise AssertionError("K315 deterministic replay failed")
    census = replay["census"]
    checks = {
        "twenty_one_families": len(replay["complete_column_replacement_expansion"]) == 21,
        "terminal_slot": replay["fixed_control"]["terminal_core_slot"] == [3, 3],
        "nonempty_monomials": census["unweighted_nonzero_monomials"] > 0,
        "cross_weights_increase": census["weighted_nonzero_monomials_after_cross_factors"] > census["unweighted_nonzero_monomials"],
        "all_terminal_orders": set(census["terminal_monomials_by_jet_order_with_cross_factors"]) == {"0", "1", "2"},
        "complete_assembly": replay["composition_rule"]["complete_bordered_assembly_retained"],
        "no_cofactor": not replay["composition_rule"]["detached_cofactor_bound_used"],
        "no_occurrence_abs": not replay["composition_rule"]["occurrencewise_coherent_absolute_values_used"],
        "no_cutoff": not replay["decision"]["terminal_split_cutoff_required"],
        "no_master_overclaim": not replay["decision"]["complete_y_master_constant_emitted"],
    }
    if not all(checks.values()):
        raise AssertionError(f"K315 independent checks failed: {checks}")
    mutations = [
        lambda x: x["fixed_control"].__setitem__("terminal_core_slot", [2, 2]),
        lambda x: x["complete_column_replacement_expansion"].pop(),
        lambda x: x["composition_rule"].__setitem__("detached_cofactor_bound_used", True),
        lambda x: x["composition_rule"].__setitem__("occurrencewise_coherent_absolute_values_used", True),
        lambda x: x["composition_rule"].__setitem__("complete_bordered_assembly_retained", False),
        lambda x: x["decision"].__setitem__("K311_inserted_into_all_complete_bordered_jet_monomials", False),
        lambda x: x["decision"].__setitem__("terminal_split_cutoff_required", True),
        lambda x: x["decision"].__setitem__("complete_y_master_constant_emitted", True),
    ]
    hostile = [rejected(module, expected, mutation) for mutation in mutations]
    if not all(hostile):
        raise AssertionError(f"K315 hostile controls escaped: {hostile}")
    print(f"K315 probe passed {len(checks)}/{len(checks)} checks and rejected {len(hostile)}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
