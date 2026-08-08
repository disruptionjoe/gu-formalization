#!/usr/bin/env python3
"""Scope/prose audit for the v0.89 signature-rationale retype."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]


def strict(path):
    def hook(pairs):
        out = {}
        for key, value in pairs:
            assert key not in out, f"duplicate key {key}: {path}"
            out[key] = value
        return out
    return json.loads(path.read_text(), object_pairs_hook=hook)


ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.89.json")
registry = strict(ROOT / "lab/process/signature-rationale-build-branch-retype.json")
report = (ROOT / "explorations/conditional-build/signature-rationale-and-build-branch-retype-2026-08-08.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-08-signature-rationale-build-branch-retype-review.md").read_text()
contract = (ROOT / "lab/process/functional-channel-operating-contract-v1.0.md").read_text()
forks = (ROOT / "lab/process/layer0-fork-registry.yaml").read_text()

assert ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
assert ledger["residue"]["continuous_real"] == 84
assert ledger["residue"]["quotients_ranked"] == 5
assert registry["accounting"] == {
    "new_fields": 0,
    "new_coefficients": 0,
    "new_functions": 0,
    "new_quotients": 0,
    "external_datum_used": False,
    "headline_verdict_change": False,
    "residue_change": False,
}
assert "author-asserted conditional" in report
assert "geometry-derived comparator" in report
assert "Mandatory symplectic geometry" in review
assert "Complex/path-integral" in review
assert "signature-generic" in contract
assert "AUTHOR-ASSERTED" in forks and "GEOMETRY-DERIVED" in forks
assert "settled_side: \"Cl(7,7) = M128(R)\"" in forks
assert "derived the real form from Curt/Eric's exact source-typed arithmetic" not in forks.split("- id: REAL-CLIFFORD-FORM", 1)[1].split("- id:", 1)[0]
print("PASS signature-rationale Build-branch retype scope audit")
