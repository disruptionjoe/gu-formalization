#!/usr/bin/env python3
"""Hostile probes for K1801's normalized third-order compact jet."""
import copy
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "tests/channel-swings/k1801_full_fisher_third_order_compact_jet.py"
ARTIFACT = ROOT / "lab/process/k1801-full-fisher-third-order-compact-jet.json"
spec = importlib.util.spec_from_file_location("k1801", BASE)
k = importlib.util.module_from_spec(spec)
spec.loader.exec_module(k)


def rejected(data):
    try:
        return not all(ok for _, ok in k.validate(data, k.compute()))
    except Exception:
        return True


def main():
    data = json.loads(ARTIFACT.read_text())
    mutations = []
    bad = copy.deepcopy(data)
    bad["claim_id"] = "K1800"
    mutations.append(("wrong claim", bad))
    bad = copy.deepcopy(data)
    bad["certificate"]["parameter_taylor_order"] = 2
    mutations.append(("lowered parameter order", bad))
    bad = copy.deepcopy(data)
    bad["certificate"]["normalized_coefficients"].pop("3,0")
    mutations.append(("missing cubic coefficient", bad))
    bad = copy.deepcopy(data)
    bad["decision"]["whole_line_third_order_parameter_jet_certified"] = True
    mutations.append(("false whole-line promotion", bad))
    bad = copy.deepcopy(data)
    bad["decision"]["global_optimizer_proved"] = True
    mutations.append(("false global promotion", bad))
    for index, (label, mutation) in enumerate(mutations, 1):
        assert rejected(mutation), label
        print(f"PASS {index:02d}: rejects {label}")
    print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")


if __name__ == "__main__":
    main()
