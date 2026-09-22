#!/usr/bin/env python3
"""Independent replay and hostile controls for K325."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE = Path(__file__).with_name("k325_order_seven_correlated_determinant_jet_algebra.py")
MANIFEST = ROOT / "lab/process/k325-order-seven-correlated-determinant-jet-algebra.json"


def load_module():
    spec = importlib.util.spec_from_file_location("k325_probe_backend", MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K325 module")
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
        raise AssertionError("K325 deterministic replay failed")
    contract = replay["shared_generator_contract"]
    witness = replay["correlation_control"]
    checks = {
        "family_count": replay["fixed_control"]["family_count"] == 21,
        "first_count": replay["fixed_control"]["first_family_count"] == 5,
        "pure_count": replay["fixed_control"]["second_pure_family_count"] == 5,
        "cross_count": replay["fixed_control"]["second_cross_family_count"] == 10,
        "literal_zeros": replay["fixed_control"]["literal_zero_slots"] == [[3, 4], [4, 3], [4, 4]],
        "value_exact": contract["value_coefficient_exact"],
        "first_exact": contract["first_coefficient_exact"],
        "second_exact": contract["second_derivative_coefficient_exact"],
        "weighted_census": replay["census"]["cross_weighted_family_monomials"] == 1674,
        "all_family_monomials": all(row["nonzero_determinant_monomials"] == 54 for row in replay["family_replay"]),
        "signed_zero": witness["complete_signed_second_derivative"] == "0",
        "abs_four": witness["familywise_absolute_sum"] == "4",
        "strict_gain": witness["post_assembly_strictly_tighter"],
        "no_cofactor": not contract["detached_cofactor_used"],
        "no_numeric_overclaim": not replay["decision"]["fixed_slab_derivative_interval_bank_emitted"],
    }
    if not all(checks.values()):
        raise AssertionError(f"K325 independent checks failed: {checks}")
    mutators = (
        lambda p: p["fixed_control"].__setitem__("family_count", 20),
        lambda p: p["fixed_control"].__setitem__("first_family_count", 4),
        lambda p: p["fixed_control"].__setitem__("second_pure_family_count", 4),
        lambda p: p["fixed_control"].__setitem__("second_cross_family_count", 9),
        lambda p: p["fixed_control"].__setitem__("literal_zero_slots", [[4, 4]]),
        lambda p: p["shared_generator_contract"].__setitem__("early_familywise_absolute_enclosure_forbidden", False),
        lambda p: p["shared_generator_contract"].__setitem__("detached_cofactor_used", True),
        lambda p: p["shared_generator_contract"].__setitem__("literal_border_zeros_retained", False),
        lambda p: p["shared_generator_contract"].__setitem__("value_coefficient_exact", False),
        lambda p: p["shared_generator_contract"].__setitem__("first_coefficient_exact", False),
        lambda p: p["shared_generator_contract"].__setitem__("second_derivative_coefficient_exact", False),
        lambda p: p["census"].__setitem__("K315_cross_weighted_census_replayed", False),
        lambda p: p["census"].__setitem__("K319_all_fifteen_second_families_replayed", False),
        lambda p: p["correlation_control"].__setitem__("complete_signed_second_derivative", "1"),
        lambda p: p["correlation_control"].__setitem__("familywise_absolute_sum", "0"),
        lambda p: p["correlation_control"].__setitem__("post_assembly_strictly_tighter", False),
        lambda p: p["decision"].__setitem__("fixed_slab_derivative_interval_bank_emitted", True),
        lambda p: p["decision"].__setitem__("complete_y_master_constant_emitted", True),
    )
    hostile = [rejected(module, expected, mutate) for mutate in mutators]
    if not all(hostile):
        raise AssertionError(f"K325 hostile controls escaped: {hostile}")
    print(f"K325 probe passed {len(checks)}/{len(checks)} checks and rejected {len(hostile)}/{len(hostile)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
