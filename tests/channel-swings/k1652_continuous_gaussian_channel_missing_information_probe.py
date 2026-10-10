#!/usr/bin/env python3
"""Hostile mutations for K1652."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valid(d):
    q, z = d.get("missing_information", {}), d.get("decision", {})
    return all([
        d.get("claim_id") == "K1652",
        "S_*=S_0+Delta" in q.get("channel", ""),
        "E[u_Z-u_*|X]" in q.get("score_identity", ""),
        "-E Tr" in q.get("pythagoras", ""),
        "Cov(m_Z|X)" in q.get("pythagoras", ""),
        "C_(F,N)-M_(F,N)" in q.get("k1648_conversion", ""),
        "K1606" in q.get("scope_guard", ""),
        z.get("posterior_term_subleading_proved") is False,
        z.get("protected_status_change") is False,
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1652-continuous-gaussian-channel-missing-information.json").read_text())
    assert valid(source)
    changes = [
        (("claim_id",), "K1606"),
        (("missing_information", "channel"), "S_*=S_0-Delta"),
        (("missing_information", "score_identity"), "unconditional"),
        (("missing_information", "pythagoras"), "plus posterior variance"),
        (("missing_information", "k1648_conversion"), "C+M"),
        (("missing_information", "scope_guard"), "new theorem"),
        (("decision", "posterior_term_subleading_proved"), True),
        (("decision", "protected_status_change"), True),
    ]
    for i, (path, value) in enumerate(changes, 1):
        m = copy.deepcopy(source); cur = m
        for key in path[:-1]: cur = cur[key]
        cur[path[-1]] = value
        assert not valid(m), i
        print(f"REJECT {i:02d}: hostile mutation")
    print(f"RESULT: REJECTED {len(changes)}/{len(changes)}")


if __name__ == "__main__": main()
