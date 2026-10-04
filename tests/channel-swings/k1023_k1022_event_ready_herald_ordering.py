#!/usr/bin/env python3
"""K1023: pre-settings herald theorem and post-settings countermodel."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1023-k1022-event-ready-herald-ordering.json"


def build():
    inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    # a(x)=0, b(y)=0 loses only at x=y=1.
    wins = [int((0 ^ 0) == x * y) for x, y in inputs]
    accepted = [int((x, y) != (1, 1)) for x, y in inputs]
    retained = [w for w, h in zip(wins, accepted) if h]
    return {
        "schema_version": "1.0", "result_id": "K1023-K1022-EVENT-READY-HERALD-ORDERING",
        "status": "working_draft_verified", "created": "2026-10-04",
        "safe_order": "H_i is fixed from past/source information before X_i,Y_i are generated, and the conditional setting law remains independent of the local hidden device state given H_i and the past",
        "safe_consequence": "conditioning on H_i=1 preserves the K1014 predictable-input local ceiling 1-min_j pi_i(j)",
        "post_settings_countermodel": {"strategy": "a(x)=0,b(y)=0", "wins_by_pair": wins, "herald_accepts_by_pair": accepted, "acceptance_rate": sum(accepted)/4, "retained_win_rate": sum(retained)/len(retained)},
        "ordering_boundary": "a herald chosen after reading the setting pair can delete the unique losing pair and create a perfect retained local score",
        "memory_scope": "the theorem permits arbitrary past memory and herald-hidden-state correlation; freshness is required after conditioning on the pre-settings herald and past",
        "unowned_assumptions": ["physical event-ready herald", "conditional setting freshness", "spacelike locality", "complete trial record"],
        "ownership": {"gu_herald_constructed": False, "causal_order_proved": False},
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    assert "before X_i,Y_i" in d["safe_order"]
    assert "preserves" in d["safe_consequence"]
    c = d["post_settings_countermodel"]
    assert c["wins_by_pair"] == [1, 1, 1, 0]
    assert c["herald_accepts_by_pair"] == [1, 1, 1, 0]
    assert c["acceptance_rate"] == 0.75
    assert c["retained_win_rate"] == 1
    assert "delete the unique losing pair" in d["ordering_boundary"]
    assert "arbitrary past memory" in d["memory_scope"]
    assert len(d["unowned_assumptions"]) == 4
    assert d["ownership"]["gu_herald_constructed"] is False
    assert d["ownership"]["causal_order_proved"] is False
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    d = build(); validate(d)
    OUTPUT.write_text(json.dumps(d, indent=2, sort_keys=True) + "\n")
    print("K1023 controls: 11/11")
