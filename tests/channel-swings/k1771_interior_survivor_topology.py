#!/usr/bin/env python3
"""Replay and compress K1769's 59 interior survivors into exact slabs."""
import importlib.util
import json
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1771-interior-survivor-topology.json"
SOURCE = ROOT / "tests/channel-swings/k1769_degree_seven_survivor_refinement.py"
spec = importlib.util.spec_from_file_location("k1769", SOURCE)
k1769 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(k1769)


def enc(x):
    return k1769.k1768.encode_fraction(x)


def replay():
    old = k1769.replay()
    cells = [row[0] for row in old["retained"] if row[0][0] != k1769.k1768.T_BOX[0]]
    groups = {}
    for ta, tb, za, zb, *_ in cells:
        groups.setdefault((ta, tb), []).append((za, zb))
    slabs = []
    for (ta, tb), intervals in sorted(groups.items()):
        intervals.sort()
        contiguous = all(intervals[i][1] == intervals[i + 1][0] for i in range(len(intervals) - 1))
        slabs.append({
            "t": [enc(ta), enc(tb)],
            "z": [enc(intervals[0][0]), enc(intervals[-1][1])],
            "cell_count": len(intervals),
            "z_contiguous": contiguous,
        })
    body = "\n".join(
        f"{s['t'][0]}:{s['t'][1]}:{s['z'][0]}:{s['z'][1]}:{s['cell_count']}"
        for s in slabs
    )
    return {
        "input_refinement_digest": old["digest"],
        "input_interior_cells": len(cells),
        "slab_count": len(slabs),
        "slabs": slabs,
        "all_z_intervals_contiguous": all(s["z_contiguous"] for s in slabs),
        "cell_count_conserved": sum(s["cell_count"] for s in slabs) == len(cells),
        "topology_digest": sha256(body.encode()).hexdigest(),
    }


def main():
    got = replay()
    if not ARTIFACT.exists() or "--print" in __import__("sys").argv:
        print(json.dumps(got, indent=2)); return
    data = json.loads(ARTIFACT.read_text())
    checks = [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1771"),
        ("exact replay", data["topology"] == got),
        ("59 cells", got["input_interior_cells"] == 59),
        ("three slabs", got["slab_count"] == 3),
        ("contiguous", got["all_z_intervals_contiguous"]),
        ("conserved", got["cell_count_conserved"]),
        ("not stationary", not data["decision"]["stationarity_proved"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label; print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
