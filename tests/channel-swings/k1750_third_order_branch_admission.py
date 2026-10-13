#!/usr/bin/env python3
"""Protected-state and admission controls for K1750."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main():
    d = json.loads((ROOT / "lab/process/k1750-third-order-branch-admission.json").read_text())
    c, p, z, r = d["bridge_census"], d["protected_state"], d["decision"], d["daily_review_2026_10_13"]
    checks = [
        ("schema", d["schema_version"] == "1.0"),
        ("claim", d["claim_id"] == "K1750"),
        ("classification", "INTERNAL_STRUCTURAL_ONLY" in d["classification"]),
        ("rows", c["row_count"] == 450),
        ("satisfied", c["satisfied_count"] == 371),
        ("conditional", c["conditional_count"] == 10),
        ("excluded", c["excluded_count"] == 65),
        ("missing", c["missing_count"] == 4),
        ("new rows", c["new_satisfied_rows"] == ["K1746", "K1747", "K1748", "K1749", "K1750"]),
        ("protected rows", c["protected_missing_rows"] == ["SC-ACT-01", "SC-ACT-02", "SC-ACT-06", "SC-META-53"]),
        ("source", p["source_claims"] == "SC-ACT-01/02/06 remain ASSERTS; SC-META-53 remains UNCERTAIN."),
        ("ledger", p["physics_ledger"] == "33 SAME / 22 DIFFERS / 31 NEEDS / 2 OVER-DETERMINED"),
        ("candidates", "0/7" in p["candidate_counts"]),
        ("canon", not p["canon_change"]),
        ("paper", not p["paper_change"]),
        ("prediction", not p["prediction_or_confirmation"]),
        ("public", not p["public_posture_change"]),
        ("fourteenth", z["fourteenth_order_fisher_law_proved"]),
        ("half blind", z["q_thirteen_halves_blindness_proved"]),
        ("q7 selector", z["q_seven_third_order_selector_proved"]),
        ("third jet", z["unique_third_order_chart_jet_proved"]),
        ("arb named order", z["named_q_1_over_1024_finite_strength_ordering_arb_proved"]),
        ("singular face", z["u_equals_q_singular_face_typed"]),
        ("branch open", not z["complete_local_branch_identified"]),
        ("chart open", not z["whole_two_radius_chart_ordered"]),
        ("global open", not z["global_two_radius_optimizer_identified"]),
        ("unrestricted open", not z["unrestricted_stationary_lower_bound_proved"]),
        ("physical open", not z["source_owned_physical_theory"]),
        ("review records Arb", "Arb" in r["what_changed"]),
        ("next domain", "branch-and-bound" in d["next_condition"]),
        ("next Haar", "Haar" in d["next_condition"]),
    ]
    assert len(checks) == 31
    for i, (label, ok) in enumerate(checks, 1):
        assert ok, label
        print(f"PASS {i:02d}: {label}")
    print(f"RESULT: PASS {len(checks)}/{len(checks)}")


if __name__ == "__main__":
    main()
