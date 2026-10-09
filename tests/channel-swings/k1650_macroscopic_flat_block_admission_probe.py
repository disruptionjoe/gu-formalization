#!/usr/bin/env python3
"""Hostile mutations for K1650."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def accepts(d):
    q, z = d["protected_integration"], d["decision"]
    return all([
        "365 rows" in q["census"], "remain ASSERTS" in q["source_status"],
        "UNCERTAIN" in q["source_status"], "33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED" in q["ledger_status"],
        "0/7" in q["physical_admission"], "posterior-score residual" in q["next_gate"],
        "Do not replace" in q["scope_guard"], z["complete_gap_sign_open"],
        not z["source_or_ledger_status_moved"], not z["canon_or_public_status_moved"],
        not z["protected_status_change"],
    ])


def main():
    source = json.loads((ROOT / "lab/process/k1650-macroscopic-flat-block-admission.json").read_text())
    mutations = [
        ("wrong census", "protected_integration", "census", "360 rows"),
        ("source moved", "protected_integration", "source_status", "SC-ACT proved"),
        ("ledger moved", "protected_integration", "ledger_status", "34 SAME"),
        ("physical admitted", "protected_integration", "physical_admission", "7/7"),
        ("next gate erased", "protected_integration", "next_gate", "Complete"),
        ("scope erased", "protected_integration", "scope_guard", "Unrestricted theorem"),
        ("sign closed", "decision", "complete_gap_sign_open", False),
        ("source flag", "decision", "source_or_ledger_status_moved", True),
        ("canon flag", "decision", "canon_or_public_status_moved", True),
        ("protected flag", "decision", "protected_status_change", True),
    ]
    assert accepts(source)
    for i, (label, section, key, value) in enumerate(mutations, 1):
        d = json.loads(json.dumps(source)); d[section][key] = value
        assert not accepts(d), label
        print(f"PASS {i:02d}: rejected {label}")
    print(f"RESULT: PASS {len(mutations)}/{len(mutations)}")


if __name__ == "__main__":
    main()
