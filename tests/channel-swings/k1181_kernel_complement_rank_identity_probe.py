#!/usr/bin/env python3
"""Hostile mutation probe for K1181."""
from __future__ import annotations
import copy, importlib.util, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tests/channel-swings/k1181_kernel_complement_rank_identity.py"
CERT = ROOT / "lab/process/k1181-kernel-complement-rank-identity.json"

def load_module():
    spec = importlib.util.spec_from_file_location("k1181_probe_target", SCRIPT); assert spec and spec.loader
    module = importlib.util.module_from_spec(spec); sys.modules[spec.name] = module; spec.loader.exec_module(module); return module

def main() -> int:
    module = load_module(); packet = json.loads(CERT.read_text()); module.validate(packet)
    mutations = [
        ("result_id", "BROKEN"), ("status", "unverified"), ("identity", "rank(J)"),
        ("sharp", False), ("claim_ceiling", "source ownership proved"),
    ]
    rejected = 0
    for key, value in mutations:
        bad = copy.deepcopy(packet); bad[key] = value
        try: module.validate(bad)
        except (AssertionError, KeyError): rejected += 1
    for index in range(4):
        bad = copy.deepcopy(packet); bad["controls"][index]["rank_j_on_ker_h"] += 1
        try: module.validate(bad)
        except (AssertionError, KeyError): rejected += 1
    assert rejected == 9
    print("PASS controls=12 hostile_mutations_rejected=9/9")
    return 0

if __name__ == "__main__": raise SystemExit(main())
