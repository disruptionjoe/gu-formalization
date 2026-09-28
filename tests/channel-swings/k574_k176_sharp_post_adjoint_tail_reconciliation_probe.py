#!/usr/bin/env python3
"""Independent controls and hostile mutations for K574."""

from __future__ import annotations

import copy
import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k574_probe_target", HERE / "k574_k176_sharp_post_adjoint_tail_reconciliation.py")
K574 = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(K574)


def checks(payload: dict) -> list[bool]:
    replay = payload["compatibility_replay"]
    sharp = payload["sharp_tail"]
    decision = payload["decision"]
    return [
        payload["result_id"] == "K574-K176-SHARP-POST-ADJOINT-TAIL-RECONCILIATION",
        replay["K176_post_left_adjoint"] is True,
        replay["K176_all_16_exchange_monomials"] is True,
        replay["K496_seed_scope_unchanged"] is True,
        replay["K496_cross_polarity_cancellation_used"] is False,
        replay["same_geometric_tail_shape"] is True,
        replay["same_post_left_adjoint_location"] is True,
        sharp["old_coefficient"] == "40/3",
        sharp["sharp_coefficient"] == "1",
        sharp["exact_improvement_factor"] == "40/3",
        sharp["sharp_tail_strictly_smaller"] is True,
        decision["K570_tail_input_superseded"] is True,
        decision["K569_finite_square_unchanged"] is True,
        decision["K152_shifted_form_residual_emitted"] is False,
        payload["source_and_ledger_effect"] == "none",
    ]


def main() -> int:
    payload = K574.build()
    controls = checks(payload)
    rejected = 0
    mutations = [
        lambda p: p["compatibility_replay"].__setitem__("K176_post_left_adjoint", False),
        lambda p: p["compatibility_replay"].__setitem__("K176_all_16_exchange_monomials", False),
        lambda p: p["compatibility_replay"].__setitem__("K496_seed_scope_unchanged", False),
        lambda p: p["compatibility_replay"].__setitem__("K496_cross_polarity_cancellation_used", True),
        lambda p: p["compatibility_replay"].__setitem__("same_geometric_tail_shape", False),
        lambda p: p["sharp_tail"].__setitem__("exact_improvement_factor", "1"),
        lambda p: p["sharp_tail"].__setitem__("sharp_tail_strictly_smaller", False),
        lambda p: p["decision"].__setitem__("K570_tail_input_superseded", False),
        lambda p: p["decision"].__setitem__("K152_shifted_form_residual_emitted", True),
    ]
    for mutate in mutations:
        hostile = copy.deepcopy(payload)
        mutate(hostile)
        try:
            K574.validate(hostile)
        except AssertionError:
            rejected += 1
    print(f"K574 controls: {sum(controls)}/{len(controls)}; hostile: {rejected}/{len(mutations)}")
    return 0 if all(controls) and rejected == len(mutations) else 1


if __name__ == "__main__":
    raise SystemExit(main())
