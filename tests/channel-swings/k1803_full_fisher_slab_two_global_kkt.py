#!/usr/bin/env python3
"""Compose K1788 and K1802 without overpromoting slab-two closure."""
import json
from pathlib import Path

from flint import arb

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1803-full-fisher-slab-two-global-kkt.json"
K1788 = ROOT / "lab/process/k1788-full-fisher-first-two-slab-exclusion.json"
K1802 = ROOT / "lab/process/k1802-full-fisher-slab-two-taylor-bank.json"
UPPER = arb("31835729061") / arb("200000000000000000")


def compute():
    k1788 = json.loads(K1788.read_text())
    k1802 = json.loads(K1802.read_text())
    local = k1788["certificate"]["boundary_boxes"][1]
    value = arb(local["boundary_stationary_value_enclosure"])
    return {
        "local_boundary_kkt_strictly_isolated": bool(local["strict_inclusion"]),
        "local_inward_t_gradient_strict": bool(local["strict_kkt_inward_sign"]),
        "local_value_strictly_above_threshold": bool(value > UPPER),
        "degree_thirteen_projection_below_threshold_at_same_point": bool(
            k1802["certificate"]["projection_strictly_below_threshold"]),
        "full_minus_projection_gt_2_5e_minus_14": bool(
            k1802["certificate"]["full_fisher_minus_projection_gt_2_5e_minus_14"]),
        "complete_slab_two_hessian_or_gradient_cover_available": False,
    }


def validate(data, got=None):
    got = compute() if got is None else got
    return [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1803"),
        ("inputs", data["inputs"] == ["K1788", "K1802"]),
        ("composition", data["certificate"] == got),
        ("local KKT retained", data["decision"]["unique_local_slab_two_boundary_kkt_point"]),
        ("projection gap retained", data["decision"]["positive_unresolved_projection_complement_at_local_kkt"]),
        ("not global slab", not data["decision"]["slab_two_globally_excluded"]),
        ("not global", not data["decision"]["global_optimizer_proved"]),
    ]


def main():
    got = compute()
    if not ARTIFACT.exists() or "--print" in __import__("sys").argv:
        print(json.dumps(got, indent=2))
        return
    checks = validate(json.loads(ARTIFACT.read_text()), got)
    for index, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {index:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
