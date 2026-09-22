#!/usr/bin/env python3
"""Independent replay and hostile controls for K316."""

from __future__ import annotations

import copy
import importlib.util
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE = Path(__file__).with_name("k316_order_seven_complete_y_master.py")
MANIFEST = ROOT / "lab/process/k316-order-seven-complete-y-master.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k316_probe_backend", MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K316 module")
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
        raise AssertionError("K316 deterministic replay failed")
    rows = replay["homogeneity_composition"]["terminal_radial_projective_moments"]
    checks = {
        "three_orders": [row["terminal_jet_order"] for row in rows] == [0, 1, 2],
        "finite_positive": all(Fraction(row["complete_radial_projective_upper_fraction"]) > 0 for row in rows),
        "minimum_s_power_two": replay["release_test"]["minimum_s_power_after_terminal_substitution"],
        "terminal_join": replay["decision"]["terminal_radial_projective_join_complete"],
        "naive_product_rejected": replay["decision"]["naive_K312_times_K314_times_K315_composition_rejected"],
        "domain_mismatch": replay["release_test"]["domain_mismatch_explicit"],
        "global_coefficient_absent": not replay["sufficiency_audit"]["global_nonterminal_angular_coefficient_available"],
        "inputs_insufficient": not replay["sufficiency_audit"]["complete_y_master_inputs_sufficient"],
        "no_y_overclaim": not replay["decision"]["complete_y_master_constant_emitted"],
        "no_gap_release": not replay["decision"]["five_gap_axis_transfer_released"],
        "no_gamma_release": not replay["decision"]["k294_gamma_join_released"],
    }
    if not all(checks.values()):
        raise AssertionError(f"K316 independent checks failed: {checks}")
    mutations = [
        lambda x: x["fixed_control"].__setitem__("terminal_jet_orders", [0, 1]),
        lambda x: x["fixed_control"].__setitem__("scaled_regularizer_degree", 26),
        lambda x: x["sufficiency_audit"].__setitem__("radial_projective_terminal_moments_complete", False),
        lambda x: x["sufficiency_audit"].__setitem__("global_nonterminal_angular_coefficient_available", True),
        lambda x: x["sufficiency_audit"].__setitem__("complete_y_master_inputs_sufficient", True),
        lambda x: x["decision"].__setitem__("terminal_radial_projective_join_complete", False),
        lambda x: x["decision"].__setitem__("naive_K312_times_K314_times_K315_composition_rejected", False),
        lambda x: x["decision"].__setitem__("complete_y_master_constant_emitted", True),
        lambda x: x["decision"].__setitem__("five_gap_axis_transfer_released", True),
        lambda x: x["decision"].__setitem__("k294_gamma_join_released", True),
    ]
    hostile = [rejected(module, expected, mutation) for mutation in mutations]
    if not all(hostile):
        raise AssertionError(f"K316 hostile controls escaped: {hostile}")
    print(f"K316 probe passed {len(checks)}/{len(checks)} checks and rejected {len(hostile)}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
