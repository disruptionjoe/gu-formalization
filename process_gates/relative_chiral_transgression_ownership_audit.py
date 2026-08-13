#!/usr/bin/env python3
"""Durability audit for ledger v0.151 relative chiral-selector ownership."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKS = 0


def check(label, condition):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)
    print(f"PASS {label}")


def load_unique(path):
    def pairs(items):
        keys = [key for key, _ in items]
        if len(keys) != len(set(keys)):
            raise ValueError(f"duplicate key in {path}")
        return dict(items)

    return json.loads(path.read_text(), object_pairs_hook=pairs)


ledger = load_unique(ROOT / "lab/process/conditional-physics-ledger-v0.151.json")
result = load_unique(ROOT / "lab/process/selected-k77-relative-chiral-transgression-ownership.json")
report = (ROOT / "explorations/conditional-build/selected-k77-relative-chiral-transgression-ownership-2026-08-10.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-10-selected-k77-relative-chiral-transgression-ownership-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-relative-chiral-transgression-ownership-source-reinspection-2026-08-10.md").read_text()
contract = load_unique(ROOT / "lab/methods/research-evidence-contract-v1.0.json")
contract_md = (ROOT / "lab/methods/research-evidence-contract-v1.0.md").read_text()
lanes = (ROOT / "lab/process/RESEARCH-AGENDA.json").read_text()
next_steps = (ROOT / "NEXT-STEPS.md").read_text()
status = (ROOT / "RESEARCH-STATUS.md").read_text()
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()
priorities = (ROOT / "lab/process/exploration-absorption-priorities-2026-08-10.md").read_text()
tests_readme = (ROOT / "tests/README.md").read_text()
gates_readme = (ROOT / "process_gates/README.md").read_text()
sources_readme = (ROOT / "lab/sources/README.md").read_text()

check("ledger version is v0.151", ledger["schema_version"] == "0.151")
check("predecessor is v0.150", ledger["predecessor"].endswith("v0.150.json"))
check("headline counts freeze", ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("residue freezes at 84", ledger["residue"]["continuous_real"] == 84)
check("five quotients remain", ledger["residue"]["quotients_ranked"] == 5)
check("same-bundle characteristic difference is zero", result["same_bundle_absolute_characteristic_difference"] == 0)
check("identity winding is zero", result["canonical_identity_relative_winding"] == 0)
check("large-gauge component group is Z", result["large_gauge_component_group"] == "Z")
check("large-gauge component is not selected", result["large_gauge_component_source_selected"] is False)
check("generic transgression is not quantized", result["generic_connection_transgression_quantized"] is False)
check("exact interpolation is recorded", result["normalized_interpolation"] == "q(t)=3*t^2-2*t^3")
check("midpoint is one half", result["normalized_interpolation_midpoint"] == "1/2")
check("ambient A0 is not chiral connection", result["ambient_a0_is_automatically_observed_chiral_connection"] is False)
check("chiral reduction is not source owned", result["tangential_chiral_reduction_source_owned"] is False)
check("pairing dimension remains two", result["invariant_real_pairing_dimension"] == 2)
check("one projective pairing ratio remains", result["projective_pairing_ratio_dimension"] == 1)
check("external relative datum route remains live", result["explicit_external_relative_datum_route_live"] is True)
check("report distinguishes nonemptiness and selection", "nonemptiness versus nonzero selection" in report)
check("report distinguishes ambient and observed boundary", "ambient thirteen-boundary" in report and "observed three-boundary" in report)
check("report contains ten specialist lenses", report.count("ACTUAL MATH,") == 10)
check("hostile review contains Layer-0 lens", "**Layer-0 semantics:**" in review)
check("hostile review contains prior-art lens", "**Prior art:**" in review)
check("hostile review contains analytic lens", "**Analytic:**" in review)
check("hostile review contains symplectic lens", "**Symplectic/BV--BFV:**" in review)
check("hostile review retains external route", "EXPLICIT_EXTERNAL_DATUM_ROUTE_LIVE" in review)
check("source confirms A0", "distinguished A0" in source)
check("source silence is explicit", "SOURCE-SILENT" in source)
check("contract points at v0.151", contract["standing_ledger"]["ref"].endswith("v0.151.json"))
check("contract carries relative ownership directive", "relative_chiral_transgression_ownership_directive" in contract["standing_ledger"])
check("contract prose points at v0.151", "conditional-physics-ledger-v0.151.json" in contract_md)
check("lanes points at v0.151", "conditional-physics-ledger-v0.151.json" in lanes)
check("next steps leads with v0.151", "RELATIVE CHIRAL-TRANSGRESSION OWNERSHIP GATE (ledger v0.151)" in next_steps)
check("research status leads with v0.151", "ledger v0.151" in status.split("Predecessor result", 1)[0])
check("context pack leads with v0.151", "Current v0.151 relative chiral-selector ownership fence" in context)
check("priorities lead with v0.151", "Ledger v0.151 closes" in priorities)
check("tests inventory names probe", "selected_k77_relative_chiral_transgression_ownership_probe.py" in tests_readme)
check("process inventory names audit", "relative_chiral_transgression_ownership_audit.py" in gates_readme)
check("source inventory names receipt", "selected-k77-relative-chiral-transgression-ownership-source-reinspection-2026-08-10.md" in sources_readme)
check("P1 P2 P3 unchanged", result["p1_p2_p3_assignment_change"] is False)
check("no canon movement", result["canon_verdict_change"] is False)
check("no public-posture movement", result["public_posture_change"] is False)
check("next gate computes surplus", "COMPUTE_MULTIROW_CONSTRAINT_SURPLUS" in result["next_gate"])

migrations = [m for m in ledger["migrations"] if m["to_version"] == "0.151"]
check("five v0.151 migrations", len(migrations) == 5)
check("all migrations preserve meaning", all(m["meaning_changed"] is False for m in migrations))
rows = {row["id"]: row for row in ledger["rows"]}
check("migration frontier grades match live rows", all(rows[m["row_id"]]["frontier_grade"] == m["new"][2] for m in migrations))

print(f"PASS {CHECKS}/{CHECKS}")
