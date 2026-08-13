#!/usr/bin/env python3
"""Fail-closed scope audit for the v0.64 action-companion gate."""

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


registry = strict(ROOT / "lab/process/selected-k77-action-owned-degree14-companion.json")
ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.64.json")
report = (ROOT / "explorations/conditional-build/selected-k77-action-owned-degree14-companion-2026-08-08.md").read_text(encoding="utf-8")
review = (ROOT / "lab/process/hostile-reviews/2026-08-08-selected-k77-action-owned-degree14-companion-review.md").read_text(encoding="utf-8")

assert registry["layer0"]["printed_xi"].endswith("SUPERSEDED_ENDPOINT")
assert registry["layer0"]["action_companion"] == "D_B_ADJOINT_E_B_MINUS_E_T_PLUS_D_EPSILON_SHIAB_ADJOINT_K_S"
assert registry["layer0"]["primitive_epsilon"].startswith("EULER_EQUATION")
assert registry["layer0"]["homogeneous_gauge"].startswith("OFFSHELL_WARD")
assert registry["degree_typing"]["connection_euler_density_duals"] == 13
assert registry["degree_typing"]["epsilon_euler_density_dual"] == 14
assert registry["exact_fixture"]["held_eta_pairing"] == "-103/42"
assert registry["exact_fixture"]["naive_d_a_e_t_rejected_both_signs"] is True
assert registry["open"]["moving_hodge_krein_section_target_green"] is True
assert registry["open"]["antisymmetrized_presymplectic_current"] is True
assert registry["p1_p2_p3"] == "UNCHANGED_AND_UNUSED"
assert ledger["schema_version"] == "0.64"
assert ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5
}
assert ledger["residue"]["continuous_real"] == 84
assert "PASS_WITH_SCOPE_FENCES" in review
assert "Main probe: `37/37 PASS`" in report
for forbidden in ("Einstein equation recovered", "BFV phase space constructed", "P1 consumed"):
    assert forbidden not in report

print("PASS selected K77 action-owned degree-fourteen companion scope audit")
