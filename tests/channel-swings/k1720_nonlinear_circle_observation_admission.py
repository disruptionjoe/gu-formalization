#!/usr/bin/env python3
"""Protected admission controls for K1720."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
D = json.loads((ROOT / "lab/process/k1720-nonlinear-circle-observation-admission.json").read_text())


def main():
    checks = []
    for key, pin in D["pinned_inputs"].items():
        checks.append((f"{key} pin", hashlib.sha256((ROOT / pin["path"]).read_bytes()).hexdigest() == pin["sha256"]))
    a, q = D["admission"], D["decision"]
    checks += [
        ("obstruction scope", all(s in a["obstruction"] for s in ("deterministic", "joint-product", "randomized", "original-circle-equivariant"))),
        ("factorization scope", "uniquely through X/{1,z}" in a["factorization"]),
        ("faithful-source scope", "faithful" in a["faithful_source"]),
        ("four reopeners", len(a["exact_reopeners"]) == 4),
        ("source unchanged", "SOURCE_REGISTER_UNCHANGED" in a["source_effect"] and "UNCERTAIN" in a["source_effect"]),
        ("ledger unchanged", "STANDING_LEDGER_UNCHANGED" in a["ledger_effect"] and "NEEDS" not in a["ledger_effect"]),
        ("public unchanged", "UNCHANGED" in a["public_effect"]),
        ("next condition", "source/action-owned reopener" in a["next_condition"]),
        ("alternative retained", "Wider finite-strength scalar optimization" in a["next_condition"]),
        ("nonlinear classified", q["typed_nonlinear_alternative_classified"]),
        ("joint/random escape excluded", q["same_kernel_joint_and_randomized_escape_excluded"]),
        ("source selection fence", not q["effective_quotient_selected_by_source"]),
        ("physical fence", not q["physical_positive_quotient_constructed"]),
        ("source register fence", not q["source_register_changed"]),
        ("ledger fence", not q["standing_ledger_changed"]),
        ("public fence", not q["canon_or_public_posture_changed"]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label; print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__": main()
