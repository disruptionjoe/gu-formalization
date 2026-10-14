#!/usr/bin/env python3
"""K1818: compose the calibrated slab-three production route."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1818-full-fisher-slab-three-stationary-cover.json"


def load(name):
    return json.loads((ROOT / f"lab/process/{name}.json").read_text())


def compute():
    leaf = load("k1816-full-fisher-slab-three-leafwise-score-bank")
    parent = load("k1817-full-fisher-slab-three-whole-line-value-cover")
    c = leaf["certificate"]
    rows = c["order_seven_completed_leaves"]
    return {
        "input_partition_digest": c["input_partition_digest"],
        "leaf_count": c["leaf_count"],
        "selected_parameter_order": c["selected_parameter_order"],
        "fallback_parameter_order": c["fallback_parameter_order"],
        "completed_leaf_ids": c["completed_order_seven_leaf_ids"],
        "remaining_leaf_count": c["leaf_count"] - c["completed_order_seven_leaf_count"],
        "order_seven_margin_lowers": [row["certificate"]["compact_bounds"]["cross_margin_lower"] for row in rows],
        "order_eight_parent_zero_positive": parent["decision"]["order_eight_parent_zero_compact_margin_positive"],
        "order_eight_leaf_zero_positive": c["order_eight_leaf_zero"]["decision"]["compact_cross_margin_positive"],
        "resume_command": c["resume_command"],
    }


def validate(data, got=None):
    got = compute() if got is None else got
    return [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1818"),
        ("exact replay", data["certificate"] == got),
        ("order seven selected", got["selected_parameter_order"] == 7),
        ("two leaves complete", got["completed_leaf_ids"] == [0, 1]),
        ("76 leaves remain", got["remaining_leaf_count"] == 76),
        ("subdivision decisive", not got["order_eight_parent_zero_positive"] and got["order_eight_leaf_zero_positive"]),
        ("stationary cover open", not data["decision"]["complete_stationary_cover"]),
        ("global withheld", not data["decision"]["global_optimizer_proved"]),
    ]


def main():
    got = compute()
    if not ARTIFACT.exists() or "--print" in __import__("sys").argv:
        print(json.dumps(got, indent=2)); return
    checks = validate(json.loads(ARTIFACT.read_text()), got)
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
