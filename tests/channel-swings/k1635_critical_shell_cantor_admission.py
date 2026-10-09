#!/usr/bin/env python3
"""Certificate for K1635 protected integration."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    d = json.loads((ROOT / "lab/process/k1635-critical-shell-cantor-admission.json").read_text())
    c, p = d["census"], d["protected_boundaries"]
    checks = [
        ("claim", d["claim_id"] == "K1635"),
        ("rows", c["rows"] == 350),
        ("partition", c["satisfied"] + c["conditional"] + c["excluded"] + c["missing"] == c["rows"]),
        ("satisfied", c["satisfied"] == 271),
        ("conditional", c["conditional"] == 10),
        ("excluded", c["excluded"] == 65),
        ("missing", c["missing"] == 4),
    ]
    for key, pin in d["pinned_inputs"].items():
        checks.append((f"pin {key}", sha(ROOT / pin["path"]) == pin["sha256"]))
    checks += [
        ("asserts", c["source_asserts"] == ["SC-ACT-01", "SC-ACT-02", "SC-ACT-06"]),
        ("uncertain", c["source_uncertain"] == ["SC-META-53"]),
        ("ledger", c["physics_ledger"] == {"SAME": 33, "DIFFERS": 22, "NEEDS": 31, "OVER_DETERMINED": 2}),
        ("scorable", c["k1145_k1150_scorable_rows"] == "0/7"),
    ]
    checks += [(key, not value) for key, value in p.items()]
    checks += [
        ("three wakes", len(d["next_wakes"]) == 3),
        ("non-Gaussian wake", "non-Gaussian" in d["next_wakes"][0]),
        ("fractional source wake", "fractional" in d["next_wakes"][1]),
        ("tuple wake", "tuple" in d["next_wakes"][2]),
    ]
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
