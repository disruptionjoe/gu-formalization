#!/usr/bin/env python3
"""Independent controls and hostile mutations for K581."""

from __future__ import annotations

import copy
import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k581_probe_target", HERE / "k581_k500_noncyclic_semibound_inheritance.py")
K581 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(K581)


def checks(payload: dict) -> list[bool]:
    native = payload["native_composition"]
    controls = payload["exact_controls"]
    decision = payload["decision"]
    return [
        payload["result_id"] == "K581-K500-NONCYCLIC-SEMIBOUND-INHERITANCE",
        native["existential_native_noncyclic_floor_proved"] is True,
        native["named_quantitative_r0_available"] is False,
        native["named_quantitative_gamma_available"] is False,
        controls["complete_floor"] == "-4",
        controls["noncyclic_floor"] == "2",
        controls["inherited_complete_floor_is_valid_on_noncyclic_space"] is True,
        controls["compression_may_improve_the_floor"] is True,
        controls["family_noncyclic_floors_are_distinct"] is True,
        decision["K500_noncyclic_floor_existence_emitted"] is True,
        decision["K462_complete_sector_semibound_reused_without_retraction"] is True,
        decision["named_quantitative_noncyclic_floor_emitted"] is False,
        decision["K494_target_test_released"] is False,
        decision["K473_native_beta_emitted"] is False,
        decision["native_K152_interval_emitted"] is False,
        payload["source_and_ledger_effect"] == "none",
    ]


def main() -> int:
    payload = K581.build()
    controls = checks(payload)
    mutations = [
        lambda p: p["native_composition"].__setitem__("existential_native_noncyclic_floor_proved", False),
        lambda p: p["native_composition"].__setitem__("named_quantitative_r0_available", True),
        lambda p: p["native_composition"].__setitem__("named_quantitative_gamma_available", True),
        lambda p: p["exact_controls"].__setitem__("inherited_complete_floor_is_valid_on_noncyclic_space", False),
        lambda p: p["exact_controls"].__setitem__("compression_may_improve_the_floor", False),
        lambda p: p["exact_controls"]["existence_without_numeric_uniformity_family"].pop(),
        lambda p: p["decision"].__setitem__("K500_noncyclic_floor_existence_emitted", False),
        lambda p: p["decision"].__setitem__("named_quantitative_noncyclic_floor_emitted", True),
        lambda p: p["decision"].__setitem__("K494_target_test_released", True),
        lambda p: p["decision"].__setitem__("K473_native_beta_emitted", True),
        lambda p: p["decision"].__setitem__("native_K152_interval_emitted", True),
    ]
    rejected = 0
    for mutate in mutations:
        hostile = copy.deepcopy(payload)
        mutate(hostile)
        try:
            K581.validate(hostile)
        except AssertionError:
            rejected += 1
    print(f"K581 controls: {sum(controls)}/{len(controls)}; hostile: {rejected}/{len(mutations)}")
    return 0 if all(controls) and rejected == len(mutations) else 1


if __name__ == "__main__":
    raise SystemExit(main())
