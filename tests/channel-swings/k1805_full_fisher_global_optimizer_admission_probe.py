#!/usr/bin/env python3
"""Hostile probes for K1805's protected global admission."""
import copy
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "tests/channel-swings/k1805_full_fisher_global_optimizer_admission.py"
ARTIFACT = ROOT / "lab/process/k1805-full-fisher-global-optimizer-admission.json"
spec = importlib.util.spec_from_file_location("k1805", BASE)
k = importlib.util.module_from_spec(spec)
spec.loader.exec_module(k)


def rejected(data, got):
    try:
        return not all(ok for _, ok in k.validate(data, got))
    except Exception:
        return True


def main():
    data, got = json.loads(ARTIFACT.read_text()), k.compute()
    mutations = []
    bad = copy.deepcopy(data); bad["entry_state"]["residual_exposed_atomic_faces"] = 121
    mutations.append(("wrong face count", bad))
    bad = copy.deepcopy(data); bad["entry_state"]["slab_two_globally_excluded"] = True
    mutations.append(("false slab-two closure", bad))
    bad = copy.deepcopy(data); bad["entry_state"]["complete_slab_three_stationary_classification"] = True
    mutations.append(("false slab-three closure", bad))
    bad = copy.deepcopy(data); bad["entry_state"]["all_exposed_boundaries_certified"] = True
    mutations.append(("false boundary closure", bad))
    bad = copy.deepcopy(data); bad["decision"]["global_optimizer_proved"] = True
    mutations.append(("false global optimizer", bad))
    bad = copy.deepcopy(data); bad["decision"]["source_owned_physical_theory"] = True
    mutations.append(("false source ownership", bad))
    for index, (label, mutation) in enumerate(mutations, 1):
        assert rejected(mutation, got), label
        print(f"PASS {index:02d}: rejects {label}")
    print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")


if __name__ == "__main__":
    main()
