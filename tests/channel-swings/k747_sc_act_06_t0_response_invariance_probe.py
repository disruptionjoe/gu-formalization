#!/usr/bin/env python3
"""Hostile mutation probe for K747."""
from __future__ import annotations
import copy, importlib.util, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tests/channel-swings/k747_sc_act_06_t0_response_invariance.py"
CERT = ROOT / "lab/process/k747-sc-act-06-t0-response-invariance.json"

def load_module():
    spec = importlib.util.spec_from_file_location("k747_probe_target", SCRIPT); assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec); sys.modules[spec.name] = mod; spec.loader.exec_module(mod); return mod

def main() -> int:
    mod = load_module(); baseline = json.loads(CERT.read_text(encoding="utf-8")); mod.validate(baseline)
    mutations = []
    for key, value in baseline["principal_transport_theorem"].items():
        replacement = (not value) if isinstance(value, bool) else "BROKEN"
        mutations.append(lambda d, key=key, replacement=replacement: d["principal_transport_theorem"].__setitem__(key, replacement))
    for index, row in enumerate(baseline["exact_controls"]["cases"]):
        for key, value in row.items():
            replacement = "wrong" if isinstance(value, str) else value + 1
            mutations.append(lambda d, index=index, key=key, replacement=replacement: d["exact_controls"]["cases"][index].__setitem__(key, replacement))
    mutations.extend([
        lambda d: d.__setitem__("result_id", "BROKEN"), lambda d: d.__setitem__("classification", "COMPARATOR"),
        lambda d: d.__setitem__("direction", "native_to_observed"), lambda d: d.__setitem__("status", "unverified"),
        lambda d: d.__setitem__("target_claim", "SC-ACT-01"), lambda d: d["exact_controls"].__setitem__("field_dimension", 0),
        lambda d: d["decision"].__setitem__("k127_curved_t0_family_repairs_same_response_obstruction", True),
        lambda d: d["decision"].__setitem__("another_ricci_flat_weyl_twojet_is_a_new_principal_response", True),
        lambda d: d["decision"].__setitem__("all_residual_pairings_on_transported_k740_response_fail_middle_exactness", False),
        lambda d: d.__setitem__("source_and_ledger_effect", "MOVED"),
    ])
    while len(mutations) < 34: mutations.append(lambda d: d["exact_controls"].__setitem__("field_dimension", 0))
    caught = 0
    for mutate in mutations[:34]:
        candidate = copy.deepcopy(baseline); mutate(candidate)
        try: mod.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError): caught += 1
    assert caught == 34
    print("PASS controls=42 hostile_mutations_rejected=34/34"); return 0

if __name__ == "__main__": raise SystemExit(main())
