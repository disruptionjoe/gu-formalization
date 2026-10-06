#!/usr/bin/env python3
"""K1249: classify the remaining source-owned boundary-selector escapes."""

import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1249-source-boundary-escape-classification.json").read_text())
CHECKS = []

def check(label, value):
    CHECKS.append((label, bool(value)))
    print(f"{'PASS' if value else 'FAIL'} {label}")

for name, item in DATA["pinned_inputs"].items():
    digest = hashlib.sha256((ROOT / item["path"]).read_bytes()).hexdigest()
    check(f"{name} input digest is pinned", digest == item["sha256"])
table = {row["candidate"]: row for row in DATA["classification_table"]}
check("six selector classes are separated", len(table) == 6)
check("regular seven-lock is sufficient but unowned", table["regular seven-component full-rank lock"]["finite_regular_selection"] == "sufficient" and not table["regular seven-component full-rank lock"]["source_owned"])
check("singular scalar resolves wrong algebra", table["singular one-scalar sum-of-squares lock"]["finite_regular_selection"] == "wrong degree-zero algebra")
check("homogeneous potential retains rank defect", "rank at most six" in table["scale-free weighted-homogeneous invariant potential"]["finite_regular_selection"] and "nonzero invariant tuple" in table["scale-free weighted-homogeneous invariant potential"]["finite_regular_selection"])
check("gauge slice leaves quotient free", "seven quotient values free" in table["gauge or Kostant representative slice"]["finite_regular_selection"])
check("scale-breaking finite escape stays open", table["scale-breaking inhomogeneous invariant boundary law"]["finite_regular_selection"] == "open if rank seven")
check("broader Green escape is outside the finite theorem", table["nonlocal or noncommutative boundary/Green law"]["finite_regular_selection"] == "outside finite theorem")
register_text = (ROOT / "lab/sources/source-claim-register.yaml").read_text()
claims = {}
for claim_id in ("SC-ACT-01", "SC-ACT-02", "SC-ACT-06", "SC-META-53"):
    match = re.search(rf"^- id: {claim_id}\n  polarity: (\S+)$", register_text, re.MULTILINE)
    claims[claim_id] = match.group(1) if match else None
check("protected source polarities remain exact", claims == {"SC-ACT-01":"ASSERTS","SC-ACT-02":"ASSERTS","SC-ACT-06":"ASSERTS","SC-META-53":"UNCERTAIN"})
failures = [label for label, ok in CHECKS if not ok]
print(f"TOTAL {len(CHECKS)} FAILURES {len(failures)}")
if failures:
    raise SystemExit("FAILED=" + " | ".join(failures))
