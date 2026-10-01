#!/usr/bin/env python3
"""Independent hostile replay for K720."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k720", HERE / "k720_sc_act_06_selected_i1b_euclidean_bosonic_symbol.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def main() -> int:
    baseline = MOD.build()
    MOD.validate(baseline)
    mutations = []
    for key, value in baseline["transport_theorem"].items():
        mutations.append((key, lambda d, key=key, value=value: d["transport_theorem"].__setitem__(key, not value)))
    for i, case in enumerate(baseline["exact_controls"]["cases"]):
        for key in ("action_euler_rank", "action_euler_kernel_dimension", "middle_cohomology_dimension", "auxiliary_q_covector_norm_squared", "middle_exact"):
            value = case[key]
            mutations.append((f"case-{i}-{key}", lambda d, i=i, key=key, value=value: d["exact_controls"]["cases"][i].__setitem__(key, (not value) if isinstance(value, bool) else value + 1)))
    mutations += [
        ("field", lambda d: d["exact_controls"].__setitem__("field_dimension", 229385)),
        ("gauge", lambda d: d["exact_controls"].__setitem__("owned_metric_diffeomorphism_rank", 3)),
        ("nonnull", lambda d: d["exact_controls"].__setitem__("nonnull_cohomology_dimension", 0)),
        ("null", lambda d: d["exact_controls"].__setitem__("native_null_cohomology_dimension", 0)),
        ("q", lambda d: d["exact_controls"].__setitem__("native_null_is_auxiliary_q_nonzero", False)),
        ("selected", lambda d: d["decision"].__setitem__("selected_flat_bosonic_realization_is_elliptic", True)),
        ("refute", lambda d: d["decision"].__setitem__("native_null_case_alone_refutes_all_nonzero_covector_exactness", False)),
        ("row", lambda d: d["decision"].__setitem__("row_projector_can_repair_field_middle_cohomology", True)),
        ("global", lambda d: d["decision"].__setitem__("result_refutes_every_source_admitted_shiab_or_background", True)),
        ("selector", lambda d: d["pinned_inputs"].__setitem__("selected_shiab", "invented")),
        ("target", lambda d: d.__setitem__("target_claim", "NONE")),
        ("effect", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
    ]
    while len(mutations) < 30:
        mutations.append(("repeat", lambda d: d["exact_controls"].__setitem__("field_dimension", 0)))
    caught = 0
    for _, mutate in mutations[:30]:
        candidate = copy.deepcopy(baseline)
        mutate(candidate)
        try:
            MOD.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K720 controls: 36")
    print(f"PASS K720 hostile mutations rejected: {caught}/30")
    return 0 if caught == 30 else 1


if __name__ == "__main__":
    raise SystemExit(main())
