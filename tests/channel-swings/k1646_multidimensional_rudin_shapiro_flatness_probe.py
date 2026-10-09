#!/usr/bin/env python3
"""Hostile mutations for K1646."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def accepts(d):
    q, z = d["flat_block"], d["decision"]
    return all([
        "disjoint" in q["support"].lower(),
        "2d_n" in q["complementarity"],
        "16d_n^2-2T_n" in q["fourth_recurrence"],
        "8/3" in q["exact_solution"],
        "<=3/2" in q["selected_flatness"],
        "fixed-ratio" in q["shell_transfer"],
        z["complete_macroscopic_cube_constructed"],
        z["exact_fourth_recurrence_proved"],
        not z["probabilistic_independence_claimed"],
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1646-multidimensional-rudin-shapiro-flatness.json").read_text())
    mutations = [
        ("overlap", "flat_block", "support", "Overlapping support is allowed."),
        ("wrong complement", "flat_block", "complementarity", "Pointwise sum is d_n."),
        ("wrong recurrence", "flat_block", "fourth_recurrence", "T_(n+1)=16d_n^2+2T_n."),
        ("wrong solution", "flat_block", "exact_solution", "T_n/d_n^2=3."),
        ("gaussian ratio", "flat_block", "selected_flatness", "The ratio is 3."),
        ("no shell", "flat_block", "shell_transfer", "Translation changes L4."),
        ("cube false", "decision", "complete_macroscopic_cube_constructed", False),
        ("recurrence false", "decision", "exact_fourth_recurrence_proved", False),
        ("independence overclaim", "decision", "probabilistic_independence_claimed", True),
    ]
    assert accepts(source)
    for i, (label, section, key, value) in enumerate(mutations, 1):
        d = json.loads(json.dumps(source)); d[section][key] = value
        assert not accepts(d), label
        print(f"PASS {i:02d}: rejected {label}")
    print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")


if __name__ == "__main__":
    main()
