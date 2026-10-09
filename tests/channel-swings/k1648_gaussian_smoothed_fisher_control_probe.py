#!/usr/bin/env python3
"""Hostile mutations for K1648."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def accepts(d):
    q, z = d["smoothed_law"], d["decision"]
    return all([
        ">0" in q["residual_covariance"], "Gaussian convolution" in q["regularity"],
        "exact covariance S_N^*" in q["matching"], "R_(Omega,N)/4<=C_(F,N)" in q["fisher_ceiling"],
        "O_(g,eta)(N^4)" in q["scale"], "not the actual" in q["scope_guard"],
        "does not prove descent" in q["scope_guard"], z["normalized_positive_smooth_density"],
        z["profiled_covariance_matched"], not z["complete_gap_sign_decided"],
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1648-gaussian-smoothed-fisher-control.json").read_text())
    mutations = [
        ("singular residual", "smoothed_law", "residual_covariance", "s_0=0"),
        ("no convolution", "smoothed_law", "regularity", "Orbit measure only."),
        ("wrong covariance", "smoothed_law", "matching", "Covariance differs."),
        ("wrong fisher direction", "smoothed_law", "fisher_ceiling", "R/4>=C_F"),
        ("superleading cost", "smoothed_law", "scale", "O(N^6)"),
        ("ceiling exact", "smoothed_law", "scope_guard", "The ceiling is exact and proves descent."),
        ("density false", "decision", "normalized_positive_smooth_density", False),
        ("matching false", "decision", "profiled_covariance_matched", False),
        ("sign overclaim", "decision", "complete_gap_sign_decided", True),
    ]
    assert accepts(source)
    for i, (label, section, key, value) in enumerate(mutations, 1):
        d = json.loads(json.dumps(source)); d[section][key] = value
        assert not accepts(d), label
        print(f"PASS {i:02d}: rejected {label}")
    print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")


if __name__ == "__main__":
    main()
