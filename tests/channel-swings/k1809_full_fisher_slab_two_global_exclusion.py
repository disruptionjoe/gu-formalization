#!/usr/bin/env python3
"""K1809 composition of the exact slab-two global exclusion."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARTIFACT = ROOT / "lab/process/k1809-full-fisher-slab-two-global-exclusion.json"


def load(name): return json.loads((ROOT / f"lab/process/{name}.json").read_text())


def compute():
    k1792 = load("k1792-full-fisher-slab-one-global-kkt")
    k1796 = load("k1796-full-fisher-retained-box-enclosure-bank")
    k1804 = load("k1804-full-fisher-deduplicated-boundary-atlas")
    k1808 = load("k1808-full-fisher-anchored-score-whole-line")
    slab2 = next(row for row in k1796["enclosure"]["by_slab"] if row["slab"] == 2)
    return {
        "threshold": k1796["enclosure"]["threshold"],
        "prior_exact_pruned_fraction_of_original_input_area": k1796["enclosure"]["excluded_fraction_of_original_input_area"],
        "slab_two_retained_leaf_count": slab2["retained_leaves"],
        "slab_two_retained_union": k1804["certificate"]["slab_two_union_rectangle"],
        "whole_line_witness_margin_lower": k1808["certificate"]["whole_line_cross_margin_lower"],
        "prior_complement_exactly_excluded": k1796["decision"]["strict_retained_area_contraction"],
        "retained_rectangle_strictly_above_threshold": k1808["decision"]["complete_slab_two_whole_line_witness_certified"],
        "slab_one_already_excluded": k1792["decision"]["slab_one_complete_sublevel_excluded"],
    }


def validate(data, got=None):
    got = compute() if got is None else got; cert = data["certificate"]
    return [
        ("schema", data["schema_version"] == "1.0"),
        ("claim", data["claim_id"] == "K1809"),
        ("inputs", data["inputs"] == ["K1792", "K1796", "K1804", "K1808"]),
        ("composition replay", cert == got),
        ("seven leaves", cert["slab_two_retained_leaf_count"] == 7),
        ("positive margin", __import__("decimal").Decimal(cert["whole_line_witness_margin_lower"].split()[0][1:]) > 0),
        ("slab two excluded", data["decision"]["slab_two_complete_sublevel_excluded"]),
        ("boundaries included", data["decision"]["all_slab_two_faces_and_corners_covered_by_uniform_value_bound"]),
        ("global open", not data["decision"]["global_optimizer_proved"]),
    ]


def main():
    if not ARTIFACT.exists() or "--print" in __import__("sys").argv:
        print(json.dumps(compute(), indent=2)); return
    checks = validate(json.loads(ARTIFACT.read_text()))
    for i, (label, ok) in enumerate(checks, 1): assert ok, label; print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
