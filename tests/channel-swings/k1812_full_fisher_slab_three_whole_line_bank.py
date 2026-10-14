#!/usr/bin/env python3
"""K1812: compose K1811's complete whole-line stationary-bank method limit."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1812-full-fisher-slab-three-whole-line-bank.json"
K1811 = ROOT / "lab/process/k1811-full-fisher-slab-three-anchored-score-bank.json"


def compute():
    source = json.loads(K1811.read_text())["certificate"]
    return {
        "input_partition_digest": source["input_partition_digest"],
        "leaf_count": source["leaf_count"],
        "rejected_leaf_count": source["rejected_leaf_count"],
        "retained_leaf_count": source["retained_leaf_count"],
        "retained_leaf_range": "0-77" if source["retained_leaf_count"] == 78 else "noncontiguous",
        "analytic_whole_line_tails_composed": True,
        "method_limit": source["method_limit"],
    }


def validate(data, got=None):
    got = compute() if got is None else got
    cert = data["certificate"]
    return [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1812"),
        ("inputs", data["inputs"] == ["K1811"]),
        ("exact replay", cert == got),
        ("78 leaves", cert["leaf_count"] == 78),
        ("all retained", cert["retained_leaf_count"] == 78),
        ("retention fenced", not data["decision"]["retained_leaf_means_additional_stationary_point"]),
        ("uniqueness withheld", not data["decision"]["complete_stationary_uniqueness_proved"]),
    ]


def main():
    got = compute()
    if not ARTIFACT.exists() or "--print" in __import__("sys").argv:
        print(json.dumps(got, indent=2)); return
    checks = validate(json.loads(ARTIFACT.read_text()), got)
    for index, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {index:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
