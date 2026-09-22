#!/usr/bin/env python3
"""Independent replay and hostile controls for K321."""

from __future__ import annotations

import copy
import importlib.util
from pathlib import Path


MODULE = Path(__file__).with_name("k321_order_seven_radial_projective_tensor_atlas.py")


def load_module():
    spec = importlib.util.spec_from_file_location("k321_backend", MODULE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load K321 module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    module = load_module()
    payload = module.build()
    module.validate_payload(payload)
    ledger = payload["degree_27_origin_ledger"]
    atlas = payload["radial_projective_tensor_atlas"]
    checks = {
        "degree": ledger["complete_regularized_radial_degree"] == -27,
        "scales": len(ledger["exact_normalized_Cauchy_controls"]) == 3,
        "scale_invariance": ledger["all_three_scales_have_identical_normalized_product"],
        "factorizations": all(
            row["raw_D4_factorization_exact"] and row["raw_bordered_B5_factorization_exact"]
            for row in ledger["exact_normalized_Cauchy_controls"]
        ),
        "chart_count": atlas["chart_count"] == 64,
        "radial_power": atlas["origin_measure_power"] == 6,
        "s0_power": atlas["s0_measure_power"] == 3,
        "s1_power": atlas["s1_measure_power"] == 29,
        "endpoint_powers": atlas["endpoint_terminal_remaining_powers"] == [2, 1, 0],
        "nonnegative": atlas["all_recorded_boundary_powers_nonnegative"],
        "no_floor": not payload["composition_contract"]["positive_argument_floor_required_at_r0"],
        "no_release": not payload["decision"]["complete_y_master_constant_emitted"],
    }
    if not all(checks.values()):
        raise AssertionError(f"K321 independent checks failed: {checks}")

    mutations = []
    for mutate in (
        lambda p: p["degree_27_origin_ledger"].__setitem__("D4_regularized_radial_degree", -15),
        lambda p: p["degree_27_origin_ledger"].__setitem__("bordered_B5_regularized_radial_degree", -10),
        lambda p: p["degree_27_origin_ledger"].__setitem__("complete_regularized_radial_degree", -26),
        lambda p: p["degree_27_origin_ledger"].__setitem__("all_three_scales_have_identical_normalized_product", False),
        lambda p: p["radial_projective_tensor_atlas"].__setitem__("chart_count", 63),
        lambda p: p["radial_projective_tensor_atlas"].__setitem__("all_recorded_boundary_powers_nonnegative", False),
        lambda p: p["composition_contract"].__setitem__("positive_argument_floor_required_at_r0", True),
        lambda p: p["composition_contract"].__setitem__("gap_cutoff_required_at_s_faces", True),
        lambda p: p["composition_contract"].__setitem__("detached_terminal_or_cofactor_bound_used", True),
        lambda p: p["decision"].__setitem__("complete_chart_determinant_uppers_emitted", True),
        lambda p: p["decision"].__setitem__("complete_y_master_constant_emitted", True),
    ):
        candidate = copy.deepcopy(payload)
        mutate(candidate)
        try:
            module.validate_payload(candidate)
        except AssertionError:
            mutations.append(True)
        else:
            mutations.append(False)
    if not all(mutations):
        raise AssertionError(f"K321 hostile controls escaped: {mutations}")
    print(f"K321 probe passed {len(checks)}/{len(checks)} checks and rejected {len(mutations)}/{len(mutations)} hostile mutations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
