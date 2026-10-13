#!/usr/bin/env python3
"""Hostile probes for K1803's protected slab-two composition."""
import copy
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "tests/channel-swings/k1803_full_fisher_slab_two_global_kkt.py"
ARTIFACT = ROOT / "lab/process/k1803-full-fisher-slab-two-global-kkt.json"
spec = importlib.util.spec_from_file_location("k1803", BASE)
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
    bad = copy.deepcopy(data); bad["certificate"]["complete_slab_two_hessian_or_gradient_cover_available"] = True
    mutations.append(("invented complete cover", bad))
    bad = copy.deepcopy(data); bad["decision"]["unique_local_slab_two_boundary_kkt_point"] = False
    mutations.append(("dropped local KKT", bad))
    bad = copy.deepcopy(data); bad["decision"]["positive_unresolved_projection_complement_at_local_kkt"] = False
    mutations.append(("dropped complement", bad))
    bad = copy.deepcopy(data); bad["decision"]["slab_two_globally_excluded"] = True
    mutations.append(("false slab closure", bad))
    bad = copy.deepcopy(data); bad["decision"]["global_optimizer_proved"] = True
    mutations.append(("false global closure", bad))
    for index, (label, mutation) in enumerate(mutations, 1):
        assert rejected(mutation, got), label
        print(f"PASS {index:02d}: rejects {label}")
    print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")


if __name__ == "__main__":
    main()
