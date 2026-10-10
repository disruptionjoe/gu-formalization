#!/usr/bin/env python3
"""Certificate for K1685's protected integration."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    data = json.loads((ROOT / "lab/process/k1685-localized-coefficient-admission.json").read_text())
    claim, decision = data["admission"], data["decision"]
    checks = [
        ("schema", data["schema_version"] == "1.0"), ("claim", data["claim_id"] == "K1685"),
        ("explicit functional", "h_g^card-up<h_g^prof" in claim["quantum_result"]),
        ("weak endpoint", "weak-channel endpoint" in claim["quantum_result"]),
        ("lower wake", "unrestricted lower bound" in claim["remaining_quantum_gate"]),
        ("wider trial", "packet shapes" in claim["remaining_quantum_gate"]),
        ("entropy separate", "unknown-profile/growing-latent" in claim["remaining_quantum_gate"]),
        ("physical gate", "K1145/K1150 remain 0/7" in claim["physical_admission"]),
        ("census total", "400 rows" in claim["bridge_census"]),
        ("census satisfied", "321 satisfied" in claim["bridge_census"]),
        ("source state", "SC-ACT-01/02/06 remain ASSERTS" in claim["protected_state"]),
        ("ledger state", "33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED" in claim["protected_state"]),
        ("scope", "Do not promote" in claim["scope_guard"]),
        ("integrated", decision["localized_upper_functional_integrated"]),
        ("coefficient open", decision["true_unrestricted_coefficient_open"]),
        ("source unchanged", not decision["source_status_changed"]),
        ("ledger unchanged", not decision["physics_ledger_changed"]),
        ("public unchanged", not decision["canon_or_public_status_changed"]),
    ]
    for number, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {number:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
