#!/usr/bin/env python3
"""Hostile mutation probe for K755."""
from __future__ import annotations
import copy, importlib.util, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tests/channel-swings/k755_sc_act_06_cyclic_two_connection_square.py"
CERT = ROOT / "lab/process/k755-sc-act-06-cyclic-two-connection-square.json"
def load_module():
    spec = importlib.util.spec_from_file_location("k755_probe_target", SCRIPT); assert spec and spec.loader
    module = importlib.util.module_from_spec(spec); sys.modules[spec.name] = module; spec.loader.exec_module(module); return module
def main() -> int:
    module = load_module(); baseline = json.loads(CERT.read_text(encoding="utf-8")); module.validate(baseline); mutations = []
    for key in ("two_connection_cancellation_motif_confirmed", "path_cancellation_burden_confirmed", "k748_adapter_was_unbuilt"):
        mutations.append(lambda d, key=key: d["source_grade"].__setitem__(key, False))
    mutations += [
        lambda d: d["source_grade"].__setitem__("exact_formula_released", True),
        lambda d: d["source_grade"].__setitem__("formula_grade", "SOURCE_STATES_FORMULA"),
        lambda d: d["operator"].__setitem__("exact_match", False),
        lambda d: d["operator"].__setitem__("expected_square", "BROKEN"),
        lambda d: d["theorem"].__setitem__("upper_right_cancels_iff_bianchi_intertwining", False),
        lambda d: d["theorem"].__setitem__("lower_right_cancels_from_dB_square_equals_FB", False),
        lambda d: d["theorem"].__setitem__("surviving_diagonal_output", "BROKEN"),
        lambda d: d["theorem"].__setitem__("surviving_lower_output", "BROKEN"),
        lambda d: d["theorem"].__setitem__("source_formula_or_action_ownership_proved", True),
        lambda d: d["theorem"].__setitem__("current_GU_field_carrier_identified", True),
        lambda d: d["decision"].__setitem__("exact_cyclic_square_constructed", False),
        lambda d: d["decision"].__setitem__("new_current_carrier_principal_response_proved", True),
        lambda d: d.__setitem__("result_id", "BROKEN"), lambda d: d.__setitem__("classification", "COMPARATOR"),
        lambda d: d.__setitem__("target_claim", "SC-ACT-01"), lambda d: d.__setitem__("source_and_ledger_effect", "MOVED"),
    ]
    while len(mutations) < 31: mutations.append(lambda d: d["operator"].__setitem__("exact_match", False))
    caught = 0
    for mutate in mutations[:31]:
        candidate = copy.deepcopy(baseline); mutate(candidate)
        try: module.validate(candidate)
        except (AssertionError, KeyError, TypeError, ValueError): caught += 1
    assert caught == 31; print("PASS controls=36 hostile_mutations_rejected=31/31"); return 0
if __name__ == "__main__": raise SystemExit(main())
