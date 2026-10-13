#!/usr/bin/env python3
"""Protected admission controls for K1715."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1715-full-carrier-kernel-admission.json").read_text())


def main():
    checks = []
    for key, pin in D["pinned_inputs"].items():
        checks.append((f"{key} pin", hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]))
    a, q = D["admission"], D["decision"]
    checks += [
        ("original exact kernel", "exact kernel {1,z}" in a["original_circle_result"]),
        ("original primitive obstruction", "no faithful primitive linear observed intertwiner" in a["original_circle_result"]),
        ("effective faithful", "acts faithfully" in a["effective_quotient_result"]),
        ("effective normalization", "c=1/2" in a["effective_quotient_result"]),
        ("source unchanged", "SOURCE_REGISTER_UNCHANGED" in a["source_effect"] and "SC-META-53 remains UNCERTAIN" in a["source_effect"]),
        ("ledger unchanged", "STANDING_LEDGER_UNCHANGED" in a["ledger_effect"] and "LT-SM8" in a["ledger_effect"]),
        ("public unchanged", a["public_effect"] == "CANON_PAPERS_PREDICTIONS_CONFIRMATIONS_PUBLIC_POSTURE_UNCHANGED"),
        ("next condition owned tuple", "source/action-owned" in a["next_condition"] and "physical carrier/domain" in a["next_condition"]),
        ("kernel classified", q["full_carrier_original_circle_kernel_classified"]),
        ("primitive route excluded", q["primitive_original_circle_route_excluded"]),
        ("quotient constructed", q["effective_quotient_escape_constructed"]),
        ("source selection fenced", not q["source_selection_constructed"]),
        ("physical quotient fenced", not q["physical_positive_quotient_constructed"]),
        ("source register protected", not q["source_register_changed"]),
        ("ledger protected", not q["standing_ledger_changed"]),
        ("public protected", not q["canon_or_public_posture_changed"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
