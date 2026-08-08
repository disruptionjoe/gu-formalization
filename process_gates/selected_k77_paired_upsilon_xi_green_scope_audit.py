#!/usr/bin/env python3
"""Fail-closed scope audit for the v0.63 printed-Xi/Green-owner gate."""

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


registry = strict(ROOT / "lab/process/selected-k77-paired-upsilon-xi-green.json")
ledger = strict(ROOT / "lab/process/conditional-physics-ledger-v0.63.json")
report = (ROOT / "explorations/conditional-build/selected-k77-paired-upsilon-xi-green-2026-08-08.md").read_text(encoding="utf-8")
review = (ROOT / "lab/process/hostile-reviews/2026-08-08-selected-k77-paired-upsilon-xi-green-review.md").read_text(encoding="utf-8")

assert registry["layer0"]["exact_graph_output"].endswith("DEGREE1")
assert registry["layer0"]["source_printed_upsilon"].startswith("EXTERIOR_DEGREE13")
assert registry["layer0"]["source_printed_xi"].startswith("EXTERIOR_DEGREE14")
assert registry["printed_pair"]["source_xi_supports"] == [16, 15, 11, 11]
assert registry["printed_pair"]["xi_independent_rank_after_upsilon_closure"] == 0
assert registry["formal_green"]["unrestricted_flux_nonzero"] is True
assert registry["formal_green"]["dirichlet_flux_zero"] is True
assert registry["formal_green"]["actual_k77_krein_equation_dual"] is False
assert registry["formal_green"]["antisymmetrized_presymplectic_current"] is False
assert registry["p1_p2_p3"] == "UNCHANGED_AND_UNUSED"
assert ledger["schema_version"] == "0.63"
assert ledger["progress"]["verdict_counts"] == {
    "SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5
}
assert ledger["residue"]["continuous_real"] == 84
assert "PASS AFTER CARRIER CORRECTION" in review
assert "independent Xi rank after Upsilon closure   0" in report
for forbidden in ("Einstein equation recovered", "BFV phase space constructed", "P1 consumed"):
    assert forbidden not in report

print("PASS selected K77 paired Upsilon/Xi Green-owner scope audit")
