#!/usr/bin/env python3
"""Exact custody gate for the 2026-08-27 analytic-typing corrections."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REQUIRED = {
    "explorations/conditional-build/cb-d-parameterizing-the-unknown-2026-08-05.md": (
        "maximal real dimension `346112`",
        "half-infinite `delta>0` window used an incomplete root set",
    ),
    "lab/process/path-dependencies.md": (
        "determined only up to the commutant",
        "complete set of commuting observables (CSCO)",
    ),
    "explorations/wave13/H37-count-nogo-2026-07-11.md": (
        "real-valued finite-proxy invariant",
        "`{H,V}+V^2=0`",
    ),
    "explorations/analytic-index-fredholm/oc2-b-parametrix-y14-2026-06-23.md": (
        "PROJECTED_DISCRETE_SECTOR_AND_COMPLETE_WEIGHT_WINDOWS_UNOWNED",
        "No half-infinite positive weight window",
    ),
    "explorations/window-index-nonconstancy-2026-08-08.md": (
        "INDEX_NONCONSTANCY_NOT_ESTABLISHED",
        "no index nonconstancy is currently banked",
    ),
}


def violations(texts):
    return [
        f"{path}: missing {needle}"
        for path, needles in REQUIRED.items()
        for needle in needles
        if needle not in texts[path]
    ]


def main():
    texts = {path: (ROOT / path).read_text() for path in REQUIRED}
    assert not violations(texts), violations(texts)
    checks = sum(len(v) for v in REQUIRED.values())

    mutations = 0
    for path, needles in REQUIRED.items():
        for needle in needles[:1]:
            mutant = dict(texts)
            mutant[path] = mutant[path].replace(needle, "PLANTED-MISSING", 1)
            assert violations(mutant), f"mutation escaped: {path} {needle}"
            mutations += 1

    assert checks == 10
    assert mutations == 5
    print(f"ANALYTIC TYPING HARDENING: {checks}/10 checks pass; {mutations}/5 mutations caught")


if __name__ == "__main__":
    main()
