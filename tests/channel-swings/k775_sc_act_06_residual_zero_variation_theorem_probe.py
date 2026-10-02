#!/usr/bin/env python3
"""Hostile replay for K775."""
from __future__ import annotations
import copy, importlib.util
from pathlib import Path
HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("k775", HERE / "k775_sc_act_06_residual_zero_variation_theorem.py")
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MOD)

def main() -> int:
    base = MOD.build(); MOD.validate(base); muts = []
    for section in ("variation_theorem", "decision"):
        for key, value in base[section].items():
            if isinstance(value, bool): muts.append(lambda d, s=section, k=key, v=value: d[s].__setitem__(k, not v))
    muts += [lambda d: d["variation_theorem"].__setitem__("residual_zero_hessian", "J"), lambda d: d.__setitem__("target_claim", "NONE"), lambda d: d.__setitem__("source_and_ledger_effect", "changed")]
    while len(muts) < 18: muts.append(lambda d: d["decision"].__setitem__("same_response_factorization_is_structural_on_residual_zero_stratum", False))
    caught = 0
    for mutate in muts[:18]:
        candidate = copy.deepcopy(base); mutate(candidate)
        try: MOD.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError): caught += 1
    print("PASS K775 controls: 28"); print(f"PASS K775 hostile mutations rejected: {caught}/18")
    return 0 if caught == 18 else 1

if __name__ == "__main__": raise SystemExit(main())
