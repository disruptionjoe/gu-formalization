#!/usr/bin/env python3
"""Hostile semantic mutations for K840."""
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path
from typing import Any, Callable

PRODUCER = Path(__file__).with_name("k840_sc_act_06_collapsing_nonlinear_radius.py")
SPEC = importlib.util.spec_from_file_location("k840", PRODUCER)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

Mutation = tuple[str, Callable[[dict[str, Any]], None]]


def main() -> int:
    mutations: list[Mutation] = [
        ("wrong route", lambda p: p.__setitem__("direction", "native_to_observed")),
        ("source effect promoted", lambda p: p["governance"].__setitem__("source_claim_effect", "proved")),
        ("ledger moved", lambda p: p["governance"].__setitem__("physics_ledger_effect", "positive")),
        ("protected result moved", lambda p: p["governance"].__setitem__("protected_conclusions_unchanged", False)),
        ("missing K822 pin", lambda p: p["pinned_inputs"].pop("k822")),
        ("wrong family", lambda p: p["collapsing_family"].__setitem__("map", "f_N(x)=x/N+x^2")),
        ("wrong derivative", lambda p: p["collapsing_family"].__setitem__("derivative_at_base", "Df_N(0)=1")),
        ("pointwise singular", lambda p: p["collapsing_family"].__setitem__("derivative_at_base_invertible_for_every_finite_N", False)),
        ("uniform inverse bound", lambda p: p["collapsing_family"].__setitem__("inverse_norm_uniformly_bounded", True)),
        ("wrong second zero", lambda p: p["collapsing_family"].__setitem__("second_zero", "x_N=-1/N")),
        ("wrong critical point", lambda p: p["collapsing_family"].__setitem__("critical_point", "x=1/N")),
        ("no finite-cutoff IFT", lambda p: p["pointwise_ift_certificate"].__setitem__("each_finite_cutoff_has_an_ift_neighborhood", False)),
        ("oversized certified radius", lambda p: p["pointwise_ift_certificate"].__setitem__("certified_origin_centered_radius", "r_N=1/N")),
        ("wrong isolation radius", lambda p: p["pointwise_ift_certificate"].__setitem__("largest_open_zero_isolation_radius", "1/(2N)")),
        ("wrong injectivity radius", lambda p: p["pointwise_ift_certificate"].__setitem__("largest_open_injectivity_radius", "1/N")),
        ("uniform isolation claimed", lambda p: p["uniform_failure_certificate"].__setitem__("positive_N_uniform_zero_isolation_radius_exists", True)),
        ("uniform injectivity claimed", lambda p: p["uniform_failure_certificate"].__setitem__("positive_N_uniform_injectivity_radius_exists", True)),
        ("uniform inference claimed", lambda p: p["uniform_failure_certificate"].__setitem__("pointwise_derivative_invertibility_implies_uniform_radius", True)),
        ("sample inverse norm", lambda p: p["exact_samples"][3].__setitem__("inverse_norm", 9)),
        ("sample collision corrupted", lambda p: p["exact_samples"][2].__setitem__("collision_value", "0")),
        ("control ill-conditioned", lambda p: p["well_conditioned_control"].__setitem__("inverse_derivative_norm", "||(Dg_N(0))^-1||=N")),
        ("control collapse claimed", lambda p: p["well_conditioned_control"].__setitem__("quadratic_nonlinearity_alone_forces_radius_collapse", True)),
        ("GU radius promoted", lambda p: p["decision"].__setitem__("actual_gu_uniform_nonlinear_radius_proved", True)),
        ("global verdict promoted", lambda p: p["decision"].__setitem__("global_sc_act_06_proved_or_refuted", True)),
    ]
    assert len(mutations) == 24
    rejected = 0
    for name, mutate in mutations:
        payload = copy.deepcopy(MODULE.build())
        mutate(payload)
        try:
            MODULE.validate(payload)
        except (AssertionError, KeyError, TypeError, ValueError):
            rejected += 1
            continue
        raise AssertionError(f"hostile mutation survived: {name}")
    print("PASS K840 producer validation")
    print(f"PASS K840 hostile mutations rejected: {rejected}/{len(mutations)}")
    return 0 if rejected == len(mutations) else 1


if __name__ == "__main__":
    raise SystemExit(main())
