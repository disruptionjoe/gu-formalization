#!/usr/bin/env python3
"""Hostile probes for K1802's projection-complement discriminator."""
import copy
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "tests/channel-swings/k1802_full_fisher_slab_two_taylor_bank.py"
ARTIFACT = ROOT / "lab/process/k1802-full-fisher-slab-two-taylor-bank.json"
spec = importlib.util.spec_from_file_location("k1802", BASE)
k = importlib.util.module_from_spec(spec)
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
    bad = copy.deepcopy(data); bad["certificate"]["odd_projection_degree"] = 11
    mutations.append(("wrong degree", bad))
    bad = copy.deepcopy(data); bad["certificate"]["projection_strictly_below_threshold"] = False
    mutations.append(("reversed projection sign", bad))
    bad = copy.deepcopy(data); bad["certificate"]["full_fisher_minus_projection_gt_2_5e_minus_14"] = False
    mutations.append(("lost complement floor", bad))
    bad = copy.deepcopy(data); bad["decision"]["complete_whole_line_slab_two_taylor_bank_certified"] = True
    mutations.append(("false complete Taylor bank", bad))
    bad = copy.deepcopy(data); bad["decision"]["slab_two_globally_excluded"] = True
    mutations.append(("false slab closure", bad))
    for index, (label, mutation) in enumerate(mutations, 1):
        assert rejected(mutation, got), label
        print(f"PASS {index:02d}: rejects {label}")
    print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")


if __name__ == "__main__":
    main()
