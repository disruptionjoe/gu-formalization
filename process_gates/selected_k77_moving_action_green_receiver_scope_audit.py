#!/usr/bin/env python3
"""Fail-closed scope audit for the v0.65 moving action-Green receiver."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def strict(path):
    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


registry = strict(ROOT / "lab/process/selected-k77-moving-action-green-receiver.json")
ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.65.json")
report = (ROOT / "explorations/conditional-build/selected-k77-moving-action-green-receiver-2026-08-08.md").read_text(encoding="utf-8")
review = (ROOT / "lab/process/hostile-reviews/2026-08-08-selected-k77-moving-action-green-receiver-review.md").read_text(encoding="utf-8")

assert registry["layer0"]["complete_observation"].endswith("NORMAL_FIRST_JET")
assert registry["layer0"]["ordinary_pullback"].startswith("TANGENTIAL_ONLY")
assert registry["exact"]["factorized_receiver_rank"] == 45
assert all(registry["exact"][key] is True for key in (
    "moving_target_live", "moving_section_live", "moving_primalizer_live",
    "moving_euler_live", "degree14_inverse_density_live", "green_flux_nonzero",
))
assert registry["exact"]["actual_k77_conormal_kernel_rank"] == 10
assert registry["exact"]["independent_sage_flint_lowerer_check"] is True
assert registry["open"]["source_native_normal_euler_jet"] is True
assert registry["open"]["antisymmetrized_presymplectic_current"] is True
assert registry["p1_p2_p3"] == "UNCHANGED_AND_UNUSED"
assert ledger["schema_version"] == "0.65"
assert ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5
}
assert ledger["residue"]["continuous_real"] == 84
assert "PASS_WITH_SCOPE_FENCES" in review
assert "Main probe: `42/42 PASS`" in report
for forbidden in ("Einstein equation recovered", "BFV phase space constructed", "P1 consumed"):
    assert forbidden not in report

print("PASS selected K77 moving action-Green receiver scope audit")
