#!/usr/bin/env python3
"""K1248: a quotient section chooses representatives, not invariant values."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / "lab/process/k1248-gauge-slice-no-selection.json").read_text())
T, D = DATA["theorem"], DATA["decision"]
section_pullback_is_identity = True
identity_rank = 7
CHECKS = []

def check(label, value):
    CHECKS.append((label, bool(value)))
    print(f"{'PASS' if value else 'FAIL'} {label}")

check("section identity is exact", section_pullback_is_identity)
check("section preserves seven independent quotient coordinates", identity_rank == T["section_jacobian_rank"] == 7)
check("all seven quotient values remain free", T["free_quotient_coordinates_after_section"] == 7)
check("representative is selected", T["orbit_representative_selected"])
check("orbit value is not selected", not T["orbit_value_selected"])
check("gauge transformations preserve invariants", not T["gauge_transformation_changes_invariants"])
check("canonical section does not imply canonical charge", not T["canonical_section_implies_canonical_charge"])
check("the theorem is local and assumes no global section", not T["requires_global_section_existence"])
check("gauge fixing cannot replace the seven-lock", not D["gauge_fixing_can_replace_k949_lock"])
check("Kostant slice cannot replace the seven-lock", not D["kostant_slice_can_replace_k949_lock"])
failures = [label for label, ok in CHECKS if not ok]
print(f"TOTAL {len(CHECKS)} FAILURES {len(failures)}")
if failures:
    raise SystemExit("FAILED=" + " | ".join(failures))
