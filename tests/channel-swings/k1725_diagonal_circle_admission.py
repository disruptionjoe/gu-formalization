#!/usr/bin/env python3
"""Protected admission controls for K1725."""
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1725-diagonal-circle-admission.json").read_text())


def main():
    checks = []
    for key, pin in D["pinned_inputs"].items():
        checks.append((f"{key} pin", hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]))
    a, q = D["admission"], D["decision"]
    checks += [
        ("circle-specific classification", all(s in a["classification"] for s in ("circle-specific", "C has kernel {1,z}", "D is faithful"))),
        ("positive internal result", "gcd-one" in a["positive_result"] and "odd charge" in a["positive_result"]),
        ("ownership boundary", all(s in a["ownership_boundary"] for s in ("does not select D", "hypercharge", "physical carrier/domain", "positive quotient"))),
        ("source unchanged", "SOURCE_REGISTER_UNCHANGED" in a["source_effect"] and "UNCERTAIN" in a["source_effect"]),
        ("ledger unchanged", "STANDING_LEDGER_UNCHANGED" in a["ledger_effect"]),
        ("public unchanged", "UNCHANGED" in a["public_effect"]),
        ("next owner input", "source/action ownership" in a["next_condition"]),
        ("scalar alternative retained", "Wider finite-strength scalar optimization" in a["next_condition"]),
        ("reopener classified", q["different_circle_reopener_classified"]),
        ("nonuniversality decision", q["original_parity_obstruction_is_not_all_circles"]),
        ("source selection fence", not q["source_selects_diagonal_circle"]),
        ("physical fence", not q["physical_positive_quotient_constructed"]),
        ("source register fence", not q["source_register_changed"]),
        ("ledger fence", not q["standing_ledger_changed"]),
        ("public fence", not q["canon_or_public_posture_changed"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label; print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
