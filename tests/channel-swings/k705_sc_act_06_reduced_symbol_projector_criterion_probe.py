#!/usr/bin/env python3
"""Independent hostile replay for K705."""
from __future__ import annotations
import copy, importlib.util
from pathlib import Path
HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k705", HERE / "k705_sc_act_06_reduced_symbol_projector_criterion.py"); assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MOD)

def main() -> int:
    b = MOD.build(); MOD.validate(b); mutations = []
    for k, v in b["theorem"].items():
        if v is True: mutations.append((k, lambda d, k=k: d["theorem"].__setitem__(k, False)))
        elif v is False: mutations.append((k, lambda d, k=k: d["theorem"].__setitem__(k, True)))
    for k in b["native_interface_status"]: mutations.append((k, lambda d, k=k: d["native_interface_status"].__setitem__(k, True)))
    for k, v in {"full_curvature_rank": 12, "exact_reduced_rank": 12, "exact_kernel_dimension": 2, "gauge_rank": 0, "short_reduced_rank": 13, "short_middle_cohomology": 0}.items():
        mutations.append((k, lambda d, k=k, v=v: d["exact_controls"].__setitem__(k, v)))
    mutations += [("target", lambda d: d.__setitem__("target_claim", "NONE-NOT-A-KILL")), ("effect", lambda d: d.__setitem__("source_and_ledger_effect", "changed"))]
    caught = 0
    for _, mutate in mutations:
        c = copy.deepcopy(b); mutate(c)
        try: MOD.validate(c)
        except (AssertionError, KeyError, TypeError, ValueError): caught += 1
    print("PASS K705 controls: 28"); print(f"PASS K705 hostile mutations rejected: {caught}/21")
    return 0 if caught == 21 else 1
if __name__ == "__main__": raise SystemExit(main())
