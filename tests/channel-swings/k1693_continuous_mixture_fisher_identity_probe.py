#!/usr/bin/env python3
"""Hostile mutations for K1693."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(data):
    setting = data.get("setting", {})
    return all([
        data.get("claim_id") == "K1693",
        "compact normalized Haar" in setting.get("group", ""),
        "Omega" in setting.get("invariance", ""),
        "rho_a(q)" in setting.get("posterior", ""),
        "integral_G" in setting.get("mixture_score", ""),
        "u_a-bar_u" in data.get("identity", ""),
        "group invariant" in data.get("equality", ""),
        "does not supply a continuum limit" in data.get("scope_guard", ""),
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1693-continuous-mixture-fisher-identity.json").read_text())
    mutations = [
        (("claim_id",), "K1692"),
        (("setting", "group"), "noncompact"),
        (("setting", "invariance"), "none"),
        (("setting", "posterior"), "uniform"),
        (("setting", "mixture_score"), "zero"),
        (("identity",), "Jensen only"),
        (("equality",), "always"),
        (("scope_guard",), "continuum coefficient proved"),
    ]
    assert valid(source)
    for number, (path, value) in enumerate(mutations, 1):
        changed = copy.deepcopy(source)
        cursor = changed
        for key in path[:-1]:
            cursor = cursor[key]
        cursor[path[-1]] = value
        assert not valid(changed), number
        print(f"REJECT {number:02d}: hostile mutation")
    print(f"RESULT: REJECTED {len(mutations)}/{len(mutations)}")


if __name__ == "__main__":
    main()
