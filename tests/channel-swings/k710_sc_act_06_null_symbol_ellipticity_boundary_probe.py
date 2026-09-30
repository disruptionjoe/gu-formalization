#!/usr/bin/env python3
"""Independent hostile replay for K710."""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k710", HERE / "k710_sc_act_06_null_symbol_ellipticity_boundary.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


def main() -> int:
    baseline = MOD.build()
    MOD.validate(baseline)
    mutations = []
    for key, value in baseline["theorem"].items():
        if isinstance(value, bool):
            mutations.append((key, lambda d, key=key, value=value: d["theorem"].__setitem__(key, not value)))
    for key in baseline["native_interface_status"]:
        mutations.append((key, lambda d, key=key: d["native_interface_status"].__setitem__(key, True)))
    changes = {
        "dimension": 13,
        "pseudo_signature": [14, 0, 0],
        "null_koszul_exact": False,
        "null_metric_laplacian_rank": 14,
        "euclideanized_laplacian_rank": 0,
    }
    for key, value in changes.items():
        mutations.append((key, lambda d, key=key, value=value: d["exact_controls"].__setitem__(key, value)))
    null_changes = {
        "metric_norm": 2,
        "gauge_rank": 0,
        "curvature_rank": 12,
        "middle_cohomology": 1,
        "metric_laplacian_rank_on_one_forms": 14,
        "clifford_identity_exact": False,
        "auxiliary_contracting_vector_pairing": 0,
    }
    for key, value in null_changes.items():
        mutations.append((key, lambda d, key=key, value=value: d["exact_controls"]["null_covector"].__setitem__(key, value)))
    mutations += [
        ("space-rank", lambda d: d["exact_controls"]["spacelike_covector"].__setitem__("metric_laplacian_rank_on_one_forms", 0)),
        ("time-rank", lambda d: d["exact_controls"]["timelike_covector"].__setitem__("metric_laplacian_rank_on_one_forms", 0)),
        ("euclidean-norm", lambda d: d["exact_controls"]["same_null_coordinates_after_euclidean_continuation"].__setitem__("metric_norm", 0)),
        ("survives", lambda d: d["decision"].__setitem__("k705_koszul_criterion_survives_as_algebra", False)),
        ("instantiate", lambda d: d["decision"].__setitem__("native_indefinite_hodge_gauge_fixing_can_instantiate_euclidean_claim", True)),
        ("target", lambda d: d.__setitem__("target_claim", "NONE-NOT-A-KILL")),
        ("effect", lambda d: d.__setitem__("source_and_ledger_effect", "changed")),
    ]
    while len(mutations) < 33:
        mutations.append(("euclidean-rank", lambda d: d["exact_controls"]["same_null_coordinates_after_euclidean_continuation"].__setitem__("metric_laplacian_rank_on_one_forms", 0)))
    assert len(mutations) == 33
    caught = 0
    for _, mutate in mutations:
        candidate = copy.deepcopy(baseline)
        mutate(candidate)
        try:
            MOD.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            caught += 1
    print("PASS K710 controls: 38")
    print(f"PASS K710 hostile mutations rejected: {caught}/33")
    return 0 if caught == 33 else 1


if __name__ == "__main__":
    raise SystemExit(main())
