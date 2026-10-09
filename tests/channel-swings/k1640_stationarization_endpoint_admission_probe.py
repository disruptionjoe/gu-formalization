#!/usr/bin/env python3
"""Hostile mutations for K1640's protected closeout."""
import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def accept(d):
    c, p, s = d["census"], d["protected_boundaries"], d["scope_fences"]
    return (c["rows"] == c["satisfied"] + c["conditional"] + c["excluded"] + c["missing"]
            and c["rows"] == 355 and c["satisfied"] == 276
            and c["source_asserts"] == ["SC-ACT-01", "SC-ACT-02", "SC-ACT-06"]
            and c["source_uncertain"] == ["SC-META-53"]
            and all(value is False for value in p.values())
            and "finite-full-energy finite-Fisher" in s["stationarization_domain"]
            and "finite fourth moment/Wick expectation" in s["gap_domain"]
            and s["coupling"] == "fixed g>0 independently of N"
            and len(d["next_wakes"]) == 3)


def main():
    d = json.loads((ROOT / "lab/process/k1640-stationarization-endpoint-admission.json").read_text())
    checks = [("baseline", accept(d))]
    for label, key in [
        ("source mutation", "source_register_changed"),
        ("ledger mutation", "physics_ledger_changed"),
        ("canon mutation", "canon_changed"),
        ("coefficient overclaim", "unrestricted_coefficient_claimed"),
        ("sufficiency overclaim", "negative_defect_sufficiency_claimed"),
        ("endpoint necessity overclaim", "endpoint_besov_necessity_claimed"),
        ("source-flow overclaim", "source_owned_flow_claimed"),
    ]:
        m = deepcopy(d); m["protected_boundaries"][key] = True
        checks.append((label, not accept(m)))
    m = deepcopy(d); m["census"]["satisfied"] += 1
    checks.append(("census mutation", not accept(m)))
    for label, key, value in [
        ("stationarization-domain deletion", "stationarization_domain", "all cutoff states"),
        ("moment-domain deletion", "gap_domain", "finite Fisher only"),
        ("coupling-premise deletion", "coupling", "arbitrary coupling"),
    ]:
        m = deepcopy(d); m["scope_fences"][key] = value
        checks.append((label, not accept(m)))
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
