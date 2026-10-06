#!/usr/bin/env python3
"""K1255: integrate the two-weight finite-selector admission boundary."""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1255-two-weight-selector-admission-boundary.json").read_text())
C, D = DATA["certificate"], DATA["decision"]
states = [row["state"] for row in C["rows"]]
checks = [
    ("ten admission rows are explicit", len(C["rows"]) == 10),
    ("three finite rows are satisfied", C["satisfied_count"] == states.count("satisfied") == 3),
    ("single-weight route remains excluded", C["excluded_count"] == states.count("excluded") == 1),
    ("six ownership or functional rows remain missing", C["missing_count"] == states.count("missing") == 6),
    ("K1145 remains zero of seven", C["k1145_pass_count"] == 0),
    ("K1150 remains zero of seven", C["k1150_pass_count"] == 0),
    ("two-weight escape exists mathematically", D["two_weight_escape_exists_mathematically"]),
    ("two-weight escape is not source-owned", not D["two_weight_escape_is_source_owned"]),
    ("regular orbit remains unselected by source", not D["regular_nonzero_orbit_is_source_selected"]),
    ("charged boundary symmetry remains default", D["charged_boundary_symmetry_remains_honest_default"]),
    ("protected status does not move", DATA["protected_status_effect"] == "none"),
]
for name, item in DATA["pinned_inputs"].items():
    checks.append((f"{name} digest is pinned", hashlib.sha256((ROOT / item["path"]).read_bytes()).hexdigest() == item["sha256"]))
for label, ok in checks:
    print(f"{'PASS' if ok else 'FAIL'} {label}")
failures = [label for label, ok in checks if not ok]
print(f"TOTAL {len(checks)} FAILURES {len(failures)}")
if failures:
    raise SystemExit("FAILED=" + " | ".join(failures))
