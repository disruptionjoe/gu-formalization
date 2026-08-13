#!/usr/bin/env python3
"""Static scope/provenance audit for ledger v0.128."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]
checks = []


def strict(relative):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def check(label, condition):
    ok = bool(condition)
    checks.append((label, ok))
    print(f"{'PASS' if ok else 'FAIL'} {label}")


result = strict("lab/process/selected-k77-complete-euler-jet-tangent-closure.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.128.json")
report = (ROOT / "explorations/conditional-build/selected-k77-complete-euler-jet-tangent-closure-2026-08-10.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-10-selected-k77-complete-euler-jet-tangent-closure-review.md").read_text()

exact = result["exact_result"]
check("prior principal tangent is retained but not first-jet closed",
      exact["prior_offslice_principal_rank"] == 594
      and exact["prior_total_principal_tangent"] == 915
      and "TANGENT915_NOT_FIRST_JET_CLOSED" in result["status"])
check("observed four-jet progression closes exactly at 810",
      exact["observed_jet_rank_progression"] == [594, 648, 702, 756, 810]
      and exact["observed_offslice_rank"] == 810
      and exact["observed_total_tangent"] == 1131)
check("observed block profile is exact",
      list(exact["observed_block_profile"].values())
      == [[160, 160, 160], [180, 180, 180], [60, 60, 60],
          [400, 400, 400], [450, 10, 10]]
      and exact["observed_new_block"] == "H_TENSOR_SYM2_TRACEFREE_N_DIM216")
check("all fourteen Y14 jets force full selected low-grade tangent",
      exact["ambient_jet_rank_progression"]
      == [594, 648, 702, 756, 810, 899, 978, 1047, 1106, 1155,
          1194, 1223, 1242, 1250, 1250]
      and exact["ambient_offslice_rank"] == 1250
      and exact["ambient_total_tangent"] == 1571)
check("lower-order blocks are composed without rank inflation",
      exact["hodge_k_lift"] == "EXACT_ON_ALL1250"
      and exact["background_connection_lower_order"] == "PRESERVES_OBSERVED810"
      and "NO_NEW_DIRECTIONS" in exact["metric_lower_order"]
      and "ZERO" in exact["epsilon_lower_order"])
check("Euler owner and scalar covector stay correctly typed",
      result["layer0"]["source_euler_linearization"].startswith("DISTINCT")
      and result["layer0"]["exterior_covector_q"]
      == "CLIFFORD_SCALAR_ONEFORM__NOT_PHI1_VECTOR")
check("observed 1131 remains conditional, not a quotient",
      result["layer0"]["observed1131"].startswith("CONDITIONAL")
      and result["accounting"]["new_quotients"] == 0)
check("grade-five and unitary parents remain unported",
      all(value == "NOT_PORTED" for key, value
          in result["action_parent_fence"].items() if key != "selected_low_grade_spin77"))
check("accounting remains unchanged",
      result["accounting"]["new_coefficients"] == 0
      and result["accounting"]["new_external_datum"] == 0
      and result["accounting"]["P1_P2_P3"] == "UNCHANGED_UNUSED")
check("ledger is append-only v0.128 from v0.127",
      ledger["schema_version"] == "0.128"
      and ledger["predecessor"].endswith("conditional-physics-ledger-v0.127.json")
      and len(ledger["migrations"]) == 627
      and [item["row_id"] for item in ledger["migrations"][-6:]]
      == ["LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR3", "LT-GR5", "LT-GR6"])
check("headline residue and quotient count do not move",
      ledger["progress"]["verdict_counts"]
      == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
      and ledger["residue"]["continuous_real"] == 84
      and ledger["residue"]["quotients_ranked"] == 5)
check("source return and parent port are visible",
      "SOURCE-CONFIRMS" in report and "SOURCE-SILENT" in report
      and "two `U(32,32)`" in report and "full `U(64,64)`" in report)
check("hostile review preserves all three charges and symplectic lens",
      all(label in review for label in ["Charge 1", "Charge 2", "Charge 3",
                                        "Symplectic — ACTUAL MATH"]))
check("validation receipts agree",
      result["validation"]["primary"] == "74/74_PASS"
      and result["validation"]["independent_sage_flint"] == "11/11_PASS")
check("no canon or posture movement",
      result["claim_status_change"] == "none"
      and result["canon_verdict_change"] == "none"
      and result["public_posture_change"] == "none")

failures = [label for label, ok in checks if not ok]
print(f"PASS {len(checks)-len(failures)}/{len(checks)}")
if failures:
    raise SystemExit("; ".join(failures))
