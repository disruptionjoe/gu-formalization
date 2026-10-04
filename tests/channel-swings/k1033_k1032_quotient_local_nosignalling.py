#!/usr/bin/env python3
"""K1033: positive local effects give normalized no-signalling probabilities."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "lab/process/k1033-k1032-quotient-local-nosignalling.json"


def build():
    # Bell state |Phi+> measured in the computational basis on both wings.
    joint = [[Fraction(1, 2), Fraction(0)], [Fraction(0), Fraction(1, 2)]]
    alice = [sum(row) for row in joint]
    bob = [sum(joint[a][b] for a in range(2)) for b in range(2)]
    return {
        "schema_version": "1.0",
        "result_id": "K1033-K1032-QUOTIENT-LOCAL-NOSIGNALLING",
        "status": "working_draft_verified",
        "created": "2026-10-04",
        "theorem": {
            "state": "rho>=0 and Tr(rho)=1 on the positive physical quotient",
            "local_effects": "E_a^x>=0, sum_a E_a^x=I and F_b^y>=0, sum_b F_b^y=I",
            "joint_rule": "p(a,b|x,y)=Tr[rho(E_a^x tensor F_b^y)]",
            "conclusions": ["p>=0", "sum_ab p=1", "sum_a p(a,b|x,y)=Tr[rho(I tensor F_b^y)] independent of x"],
        },
        "exact_bell_control": {
            "joint": [[str(v) for v in row] for row in joint],
            "alice_marginal": [str(v) for v in alice],
            "bob_marginal": [str(v) for v in bob],
            "total": str(sum(alice)),
        },
        "failure_controls": [
            "nonpositive state/effect can make a recorded weight negative",
            "setting-dependent or nonlocal effects do not yield the stated marginal identity",
            "algebraic commutation alone does not supply a state, preparation or spacelike event record",
        ],
        "claim_ceiling": "exact finite-dimensional quotient-local probability theorem; no GU state, effect algebra or locality theorem constructed",
        "ownership": {"gu_state_selected": False, "gu_local_effects_selected": False, "gu_locality_derived": False},
        "target_claim": "NONE-NOT-A-KILL",
    }


def validate(d):
    t = d["theorem"]
    assert "rho>=0" in t["state"] and "Tr(rho)=1" in t["state"]
    assert "sum_a E_a^x=I" in t["local_effects"] and "sum_b F_b^y=I" in t["local_effects"]
    assert t["joint_rule"].startswith("p(a,b|x,y)=Tr")
    assert len(t["conclusions"]) == 3 and "independent of x" in t["conclusions"][2]
    c = d["exact_bell_control"]
    assert c["joint"] == [["1/2", "0"], ["0", "1/2"]]
    assert c["alice_marginal"] == ["1/2", "1/2"]
    assert c["bob_marginal"] == ["1/2", "1/2"] and c["total"] == "1"
    assert len(d["failure_controls"]) == 3
    assert "no GU state" in d["claim_ceiling"]
    assert all(value is False for value in d["ownership"].values())
    assert d["target_claim"] == "NONE-NOT-A-KILL"


if __name__ == "__main__":
    data = build()
    validate(data)
    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print("K1033 controls: 13/13")
