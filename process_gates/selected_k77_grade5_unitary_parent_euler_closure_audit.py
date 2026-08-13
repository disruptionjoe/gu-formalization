#!/usr/bin/env python3
"""Static scope/provenance audit for ledger v0.129."""

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


result = strict("lab/process/selected-k77-grade5-unitary-parent-euler-closure.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.129.json")
report = (ROOT / "explorations/conditional-build/selected-k77-grade5-unitary-parent-euler-closure-2026-08-10.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-10-selected-k77-grade5-unitary-parent-euler-closure-review.md").read_text()
exact = result["exact_result"]

check("selected grades 1+2+5 are killed as Euler closed",
      exact["selected_125_closed"] is False
      and 6 in exact["transition_graph"]["5"])
check("complete-grade Spin closure and dimensions are exact",
      exact["grade_saturated_spin_closure"] == [1, 2, 5, 6, 9, 10, 13, 14]
      and exact["spin_coefficient_dimension"] == 8128
      and exact["spin_connection_dimension"] == 113792
      and exact["spin_total_with_metric_epsilon"] == 113893)
check("complement is separately closed and dimensioned",
      exact["self_complement_grades"] == [0, 3, 4, 7, 8, 11, 12]
      and exact["self_complement_dimension"] == 8256)
check("zero-order terms do not enlarge the grade graph",
      exact["background_A"] == "PRESERVES_EACH_CLIFFORD_GRADE"
      and exact["hodge_K_lift"] == "IDENTITY_ON_ALL_16384_INTERNAL_DIRECTIONS")
check("unitary parent carriers acquire their missing centers",
      exact["two_half_prior_residual_carrier_dimension"] == 16382
      and exact["full_U_prior_adjoint_carrier_dimension"] == 16383
      and exact["unitary_completed_coefficient_dimension"] == 16384)
check("unitary total tangent is exact",
      exact["unitary_connection_dimension"] == 229376
      and exact["unitary_total_with_metric_epsilon"] == 229477)
check("unitary covariance escape is explicit",
      "GRADE4" in exact["block_unitary_escape"]
      and "GRADE3" in exact["block_unitary_escape"])
check("equal field carriers do not collapse the parent fork",
      result["parent_disposition"]["two_U32_32_halves"].endswith("THREE_PAIRING_WEIGHTS")
      and result["parent_disposition"]["full_U64_64"].endswith("ONE_PAIRING_WEIGHT")
      and result["parent_disposition"]["selection"] == "OPEN")
check("Layer-0 keeps all five distinctions",
      len(result["layer0"]) == 5
      and all("DISTINCT" in value for value in result["layer0"].values()))
check("ledger is append-only v0.129 from v0.128",
      ledger["schema_version"] == "0.129"
      and ledger["predecessor"].endswith("conditional-physics-ledger-v0.128.json")
      and len(ledger["migrations"]) == 633
      and [item["row_id"] for item in ledger["migrations"][-6:]]
      == ["LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR3", "LT-GR5", "LT-GR6"])
check("headline accounting does not move",
      ledger["progress"]["verdict_counts"]
      == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
      and ledger["residue"]["continuous_real"] == 84
      and ledger["residue"]["quotients_ranked"] == 5)
check("source return and both parents are explicit",
      "SOURCE-CONFIRMS" in report and "SOURCE-SILENT" in report
      and "two-`U(32,32)`" in report and "full `U(64,64)`" in report)
check("hostile review includes all charges and symplectic lens",
      all(label in review for label in ["Charge 1", "Charge 2", "Charge 3",
                                        "Symplectic — ACTUAL MATH"]))
check("validation receipts agree",
      result["validation"]["primary"] == "39/39_PASS__65536_K_LIFTS"
      and result["validation"]["independent_sage_flint"] == "17/17_PASS")
check("datum canon and posture do not move",
      result["accounting"]["P1_P2_P3"] == "UNCHANGED_UNUSED"
      and result["claim_status_change"] == "none"
      and result["canon_verdict_change"] == "none"
      and result["public_posture_change"] == "none")

failures = [label for label, ok in checks if not ok]
print(f"PASS {len(checks)-len(failures)}/{len(checks)}")
if failures:
    raise SystemExit("; ".join(failures))

