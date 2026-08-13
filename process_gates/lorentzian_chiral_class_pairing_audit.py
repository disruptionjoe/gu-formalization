#!/usr/bin/env python3
"""Durability audit for ledger v0.150 Lorentzian chiral-class/pairing gate."""

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


ledger = load_unique(ROOT / "lab/process/conditional-physics-ledger-v0.150.json")
result = load_unique(ROOT / "lab/process/selected-k77-lorentzian-chiral-class-pairing.json")
report = (ROOT / "explorations/conditional-build/selected-k77-lorentzian-chiral-class-pairing-2026-08-10.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-10-selected-k77-lorentzian-chiral-class-pairing-review.md").read_text()
source = (ROOT / "lab/sources/selected-k77-lorentzian-chiral-class-pairing-source-reinspection-2026-08-10.md").read_text()
correction = (ROOT / "explorations/analytic-index-fredholm/ind-top-x4-atiyah-singer-2026-06-23.md").read_text()
contract = load_unique(ROOT / "lab/process/functional-channel-operating-contract-v1.0.json")
lanes = (ROOT / "LANES.yaml").read_text()
next_steps = (ROOT / "NEXT-STEPS.md").read_text()
status = (ROOT / "RESEARCH-STATUS.md").read_text()
tests_readme = (ROOT / "tests/README.md").read_text()
gates_readme = (ROOT / "process_gates/README.md").read_text()

check("ledger version is v0.150", ledger["schema_version"] == "0.150")
check("predecessor is v0.149", ledger["predecessor"].endswith("v0.149.json"))
check("headline counts freeze", ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("residue freezes at 84", ledger["residue"]["continuous_real"] == 84)
check("five quotients remain", ledger["residue"]["quotients_ranked"] == 5)
check("closed Lorentzian c2 lattice is 12Z", result["closed_lorentzian_spin_c2_lattice"] == "12Z")
check("closed Lorentzian unit class is unavailable", result["closed_lorentzian_spin_unit_class_available"] is False)
check("globally hyperbolic ordinary H4 rank is zero", result["globally_hyperbolic_ordinary_h4_rank"] == 0)
check("globally hyperbolic absolute c2 is unavailable", result["globally_hyperbolic_absolute_c2_available"] is False)
check("relative class is not decided", result["relative_or_compact_support_class_decided"] is False)
check("real invariant pairing space has dimension two", result["invariant_real_chiral_pairing_dimension"] == 2)
check("one projective pairing ratio remains", result["invariant_real_chiral_pairing_projective_ratio_dimension"] == 1)
check("sample pairing is neutral", result["sample_pairing_inertia"] == [3, 3, 0])
check("pairing is not source selected", result["pairing_source_selected"] is False)
check("report distinguishes ordinary and compact-support cohomology", "Ordinary `H^4(X)=0` does not imply" in report)
check("report records K3 convention control", "K3-style planted control" in report)
check("report contains ten specialist lenses", report.count("ACTUAL MATH,") == 10)
check("hostile review contains Layer-0 lens", "**Layer-0 semantics:**" in review)
check("hostile review contains prior-art lens", "**Prior art:**" in review)
check("hostile review contains analytic lens", "**Analytic:**" in review)
check("hostile review contains symplectic lens", "**Symplectic/BV:**" in review)
check("source return is explicit", "SOURCE_CONFIRMS_LORENTZIAN_OBSERVER_SECTOR" in source)
check("Rokhlin scope correction is appended", "Correction of theorem scope (2026-08-10; append-only)" in correction)
check("correction retracts simple-connectivity restriction", "Simple\nconnectivity is not a hypothesis" in correction)
check("contract points at v0.150", contract["standing_ledger"]["ref"].endswith("v0.150.json"))
check("contract carries Lorentzian class directive", "lorentzian_chiral_class_pairing_directive" in contract["standing_ledger"])
check("lanes points at v0.150", "conditional-physics-ledger-v0.150.json" in lanes)
check("next steps leads with v0.150", "LORENTZIAN CHIRAL-CLASS/PAIRING GATE (ledger v0.150)" in next_steps)
check("research status leads with v0.150", "ledger v0.150" in status.split("Predecessor result", 1)[0])
check("tests inventory names probe", "selected_k77_lorentzian_chiral_class_pairing_probe.py" in tests_readme)
check("process inventory names audit", "lorentzian_chiral_class_pairing_audit.py" in gates_readme)
check("P1 P2 P3 unchanged", result["p1_p2_p3_assignment_change"] is False)
check("no canon movement", result["canon_verdict_change"] is False)
check("no public-posture movement", result["public_posture_change"] is False)
check("next gate is relative and precedes action restriction", "RELATIVE_TANGENTIAL_CHIRAL_TRANSGRESSION" in result["next_gate"] and result["next_gate"].endswith("THEN_RESTRICT_ACTION"))

migrations = [m for m in ledger["migrations"] if m["to_version"] == "0.150"]
check("five v0.150 migrations", len(migrations) == 5)
check("all migrations preserve meaning", all(m["meaning_changed"] is False for m in migrations))
rows = {row["id"]: row for row in ledger["rows"]}
check("migration frontier grades match live rows", all(rows[m["row_id"]]["frontier_grade"] == m["new"][2] for m in migrations))

print(f"PASS {CHECKS}/{CHECKS}")
