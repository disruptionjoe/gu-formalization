#!/usr/bin/env python3
"""Hostile probes for K1804's exact boundary atlas."""
import copy
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "tests/channel-swings/k1804_full_fisher_deduplicated_boundary_atlas.py"
ARTIFACT = ROOT / "lab/process/k1804-full-fisher-deduplicated-boundary-atlas.json"
spec = importlib.util.spec_from_file_location("k1804", BASE)
k = importlib.util.module_from_spec(spec)
sys.modules["k1804"] = k
spec.loader.exec_module(k)


def rejected(data, got):
    try:
        return not all(ok for _, ok in k.validate(data, got))
    except Exception:
        return True


def main():
    data = json.loads(ARTIFACT.read_text())
    got = k.compute()
    mutations = []
    bad = copy.deepcopy(data); bad["certificate"]["retained_boxes"] = 84
    mutations.append(("lost retained box", bad))
    bad = copy.deepcopy(data); bad["certificate"]["by_slab"]["2"] = 8
    mutations.append(("wrong slab split", bad))
    bad = copy.deepcopy(data); bad["certificate"]["shared_internal_atomic_faces"] = 0
    mutations.append(("erased shared faces", bad))
    bad = copy.deepcopy(data); bad["certificate"]["atlas_digest"] = "0" * 64
    mutations.append(("wrong digest", bad))
    bad = copy.deepcopy(data); bad["decision"]["all_exposed_faces_and_corners_certified"] = True
    mutations.append(("false boundary closure", bad))
    bad = copy.deepcopy(data); bad["decision"]["global_optimizer_proved"] = True
    mutations.append(("false global closure", bad))
    for index, (label, mutation) in enumerate(mutations, 1):
        assert rejected(mutation, got), label
        print(f"PASS {index:02d}: rejects {label}")
    print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")


if __name__ == "__main__":
    main()
