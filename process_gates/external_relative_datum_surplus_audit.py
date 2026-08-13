#!/usr/bin/env python3
"""Durability audit for ledger v0.152 external relative-datum surplus."""

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


ledger = load_unique(ROOT / "lab/process/conditional-physics-ledger-v0.152.json")
result = load_unique(ROOT / "lab/process/selected-k77-external-relative-datum-surplus.json")
report = (ROOT / "explorations/conditional-build/selected-k77-external-relative-datum-surplus-2026-08-10.md").read_text()
ledger_md = (ROOT / "explorations/conditional-build/conditional-physics-ledger-v0.152.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-10-selected-k77-external-relative-datum-surplus-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-external-relative-datum-surplus-source-return-2026-08-10.md").read_text()
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

check("ledger version is v0.152", ledger["schema_version"] == "0.152")
check("predecessor is v0.151", ledger["predecessor"].endswith("v0.151.json"))
check("headline counts freeze", ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("residue freezes at 84", ledger["residue"]["continuous_real"] == 84)
check("five quotients remain", ledger["residue"]["quotients_ranked"] == 5)
check("frontier closes two", ledger["frontier_delta"]["conditions_closed"] == 2)
check("frontier opens one", ledger["frontier_delta"]["conditions_opened"] == 1)
check("two named conditions remain", ledger["frontier_delta"]["remaining_named_conditions"] == 2)
check("minimal action term is serialized", result["action_term"] == "I_cond=I_G2+k*CS_Br(a_plus,a0_plus;g_n)")
check("characteristic equation is serialized", result["characteristic_equation"] == "C(r)*t^4=9*n")
check("fixed datum selects finite amplitude", result["fixed_n_r_selects_finite_amplitude"] is True)
check("free pairing fits amplitude", result["free_r_can_fit_any_nonzero_amplitude"] is True)
check("strict datum rank is one", result["strict_parameter_constraint_rank"] == 1)
check("strict surplus is minus one", result["strict_parameter_surplus"] == -1)
check("favorable surplus is zero", result["favorable_row_surplus"] == 0)
check("positive surplus is absent", result["positive_surplus"] is False)
check("small gauge remains basic", result["small_gauge_basic"] is True)
check("large gauge selects no component", result["large_gauge_phase_selects_component"] is False)
check("P3 map is absent", result["p3_identification_built"] is False)
check("full parent remains zero", result["current_full_parent_pairing_nonzero"] is False)
check("reduced chiral term is conditional", result["reduced_chiral_pairing_conditionally_nonzero"] is True)
check("report separates winding and level", "boundary component `n`" in report and "level `k`" in report)
check("report separates winding and P3", "Boundary winding is not the realized count/index datum P3" in report)
check("report contains ten specialist lenses", report.count("ACTUAL MATH,") == 10)
check("hostile review contains Layer-0 lens", "**Layer-0 semantics:**" in review)
check("hostile review contains prior-art lens", "**Prior art:**" in review)
check("hostile review contains analytic lens", "**Analytic/Krein:**" in review)
check("hostile review contains symplectic lens", "**Symplectic/BV--BFV:**" in review)
check("hostile review scopes rather than kills path", "CONDITIONAL_SELECTION_PATH_EXISTS" in review)
check("source confirms grammar", "SOURCE_CONFIRMS" in source and "Chern--Simons-like" in source)
check("source silence is explicit", "SOURCE_SILENT" in source)
check("contract points at v0.152", contract["standing_ledger"]["ref"].endswith("v0.152.json"))
check("contract carries surplus directive", "external_relative_datum_surplus_directive" in contract["standing_ledger"])
check("contract prose points at v0.152", "conditional-physics-ledger-v0.152.json" in contract_md)
check("lanes points at v0.152", "conditional-physics-ledger-v0.152.json" in lanes)
check("next steps leads with v0.152", "EXTERNAL RELATIVE-DATUM SURPLUS GATE (ledger v0.152)" in next_steps)
check("research status leads with v0.152", "ledger v0.152" in status.split("predecessor to v0.152", 1)[0])
check("context pack leads with v0.152", "Current v0.152 external relative-datum surplus fence" in context)
check("priorities lead with v0.152", "Ledger v0.152 establishes" in priorities)
check("human ledger records nonpositive surplus", "strict surplus is `-1`" in ledger_md and "crediting small-gauge/BFV compatibility" in ledger_md)
check("tests inventory names probe", "selected_k77_external_relative_datum_surplus_probe.py" in tests_readme)
check("process inventory names audit", "external_relative_datum_surplus_audit.py" in gates_readme)
check("source inventory names receipt", "selected-k77-external-relative-datum-surplus-source-return-2026-08-10.md" in sources_readme)
check("P1 P2 P3 unchanged", result["p1_p2_p3_assignment_change"] is False)
check("no residue movement", result["residue_change"] is False)
check("no canon movement", result["canon_verdict_change"] is False)
check("no public-posture movement", result["public_posture_change"] is False)
check("next gate derives pairing or P3 bridge", "DERIVE_OR_KILL_REAL_PAIRING_RATIO" in result["next_gate"] and "RELATIVE_INDEX_TO_P3" in result["next_gate"])

migrations = [m for m in ledger["migrations"] if m["to_version"] == "0.152"]
check("six v0.152 migrations", len(migrations) == 6)
check("all migrations preserve meaning", all(m["meaning_changed"] is False for m in migrations))
rows = {row["id"]: row for row in ledger["rows"]}
check("migration frontier grades match live rows", all(rows[m["row_id"]]["frontier_grade"] == m["new"][2] for m in migrations))

print(f"PASS {CHECKS}/{CHECKS}")
