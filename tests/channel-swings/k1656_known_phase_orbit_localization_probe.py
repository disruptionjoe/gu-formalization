#!/usr/bin/env python3
"""Hostile mutations for K1656."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(d):
    q, z = d.get("localization", {}), d.get("decision", {})
    return all([
        d.get("claim_id") == "K1656",
        "known unit phases" in q.get("channel", ""),
        "unitary" in q.get("demodulation", ""),
        "O(N^(-1))" in q.get("risk", ""),
        "O_(g,eta,R)(N^3)" in q.get("score_saturation", ""),
        "unknown coefficients" in q.get("scope_guard", ""),
        z.get("arbitrary_unknown_pattern_localization_proved") is False,
        z.get("unrestricted_coercivity_proved") is False,
        z.get("protected_status_change") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1656-known-phase-orbit-localization.json").read_text())
    assert valid(source)
    changes = [
        (("claim_id",), "K1653"),
        (("localization", "channel"), "unknown phases"),
        (("localization", "demodulation"), "phase multiplication changes noise"),
        (("localization", "risk"), "O(1)"),
        (("localization", "score_saturation"), "O(N^4)"),
        (("localization", "scope_guard"), "all patterns"),
        (("decision", "arbitrary_unknown_pattern_localization_proved"), True),
        (("decision", "unrestricted_coercivity_proved"), True),
        (("decision", "protected_status_change"), True),
    ]
    for i, (path, value) in enumerate(changes, 1):
        m = copy.deepcopy(source)
        cur = m
        for key in path[:-1]:
            cur = cur[key]
        cur[path[-1]] = value
        assert not valid(m), i
        print(f"REJECT {i:02d}: hostile mutation")
    print(f"RESULT: REJECTED {len(changes)}/{len(changes)}")


if __name__ == "__main__":
    main()
