#!/usr/bin/env python3
"""Fail-closed scope audit for pre-contract Wave 0C."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
reg = json.loads((ROOT / "lab/process/precontract-wave-0c-typed-identity-theorem-scope.json").read_text())
report = (ROOT / "explorations/precontract-wave-0c-typed-identity-theorem-scope-2026-08-05.md").read_text()
source = (ROOT / "lab/sources/precontract-wave-0c-identity-scope-source-reinspection-2026-08-05.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-05-precontract-wave-0c-identity-scope-review.md").read_text()

assert reg["source_collision"] == "SOURCE-CORRECTS"
assert reg["spinor_identity"]["same_typed_object"] is True
assert reg["spinor_identity"]["full_sa_c2_same_object"] is False
assert reg["spinor_identity"]["projective_chiral_tie_dimension"] == 1
assert reg["shiab_relation"]["same_as_written"] is False
assert reg["shiab_relation"]["trace_reversal_adapter_on_riemann"] is True
assert reg["shiab_relation"]["full_domain_adapter"] == "OPEN"
assert reg["ledger_change"]["new_reason_kind"] == "STALE_PREMISE"
assert "It does not kill vacuum stationarity" in report
assert "supplies no equation identifying them" in source
assert "HOSTILE POST-REVIEW: PASS AFTER REPAIR" in review
assert "full SA-C2" in review
print("PASS: 0C identity, adapter, scale-scope, source, and revival fences retained")
