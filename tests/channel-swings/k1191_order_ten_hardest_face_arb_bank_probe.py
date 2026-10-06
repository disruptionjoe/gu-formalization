#!/usr/bin/env python3
"""Independent regeneration and hostile probe for K1191."""
from __future__ import annotations
import copy, importlib.util, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
PRODUCER = ROOT / "tests/channel-swings/k1191_order_ten_hardest_face_arb_bank.py"
STORED = ROOT / "lab/process/k1191-order-ten-hardest-face-arb-bank.json"
spec = importlib.util.spec_from_file_location("k1191_probe_target", PRODUCER)
if spec is None or spec.loader is None: raise RuntimeError("cannot load K1191 producer")
module = importlib.util.module_from_spec(spec); sys.modules[spec.name] = module; spec.loader.exec_module(module)
def main() -> int:
    stored = json.loads(STORED.read_text()); module.validate_payload(stored)
    checks = [stored == module.build(), stored["fixed_control"]["planned_descriptor_control_evaluations"] == 877_800, stored["fixed_control"]["exact_workload_ratio_to_order_eight"] == "1463/216", not stored["fixed_control"]["durable_complete_bank_emitted"], not stored["decision"]["mathematical_face_program_rejected"], all(stored["release_test"].values())]
    if not all(checks): raise AssertionError("K1191 independent control failed")
    mutations = [lambda p: p["fixed_control"].__setitem__("hybrid_terms", 21), lambda p: p["fixed_control"].__setitem__("planned_descriptor_control_evaluations", 877_799), lambda p: p["fixed_control"].__setitem__("exact_workload_ratio_to_order_eight", "1"), lambda p: p["fixed_control"].__setitem__("bounded_attempt_cpu_seconds_lower", 1999), lambda p: p["fixed_control"].__setitem__("durable_complete_bank_emitted", True), lambda p: p["execution_observation"].__setitem__("partial_in_memory_rows_promoted", True), lambda p: p["decision"].__setitem__("mathematical_face_program_rejected", True), lambda p: p["release_test"].__setitem__("native_K152_interval_not_emitted", False)]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(stored); mutate(candidate)
        try: module.validate_payload(candidate)
        except AssertionError: rejected += 1
    if rejected != len(mutations): raise AssertionError(f"K1191 hostile rejection failed: {rejected}/{len(mutations)}")
    print(f"K1191 probe passed {len(checks)}/{len(checks)} controls and rejected {rejected}/{len(mutations)} hostile mutations"); return 0
if __name__ == "__main__": raise SystemExit(main())
