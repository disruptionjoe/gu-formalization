#!/usr/bin/env python3
"""Static scope/provenance audit for the v0.126 minimal-tangent result."""

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


result = strict("lab/process/selected-k77-minimal-hessian-tangent-closure.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.126.json")
report = (ROOT / "explorations/conditional-build/selected-k77-minimal-hessian-tangent-closure-2026-08-09.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-09-selected-k77-minimal-hessian-tangent-closure-review.md").read_text()

exact = result["exact_result"]
check("scope is selected-Spin first-action local principal",
      result["scope"]["action"] == "SOURCE_SHAPED_FIRST_TRANSGRESSION_ACTION"
      and result["scope"]["parent"].startswith("CONDITIONALLY_SELECTED_REAL_SPIN77")
      and result["scope"]["differential_grade"] == "LOCAL_PRINCIPAL_FULL_X4_SYMBOL_FAMILY")
check("K-lift is balanced and nondegenerate",
      exact["grade2_Kloc_inertia"] == [637, 637, 0])
check("exact grade-two Hessian stencil is recorded",
      exact["grade2_hessian_directed_nnz"] == 5642)
check("fixed-symbol ranks separate image from closure",
      exact["fixed_symbol"]["timelike"] == {"seed": 89, "closure": 174, "progression": [89, 174]}
      and exact["fixed_symbol"]["null"]["progression"] == [89, 164, 174])
check("three representatives are not promoted as the field tangent",
      exact["three_representatives_each_branch"] == {"seed": 259, "closure": 464}
      and result["controls"]["three_representatives_as_field_tangent"] == "REJECTED_464_TO594")
check("full X4 and both branches close at rank 594",
      exact["full_X4_each_branch"] == {"seed": 344, "closure": 594}
      and exact["full_X4_both_branches"] == {"seed": 594, "closure": 594})
check("minimal known selected tangent is 915, not full 1571",
      exact["minimal_selected_tangent_dimension"] == 915
      and exact["full_1571_promoted"] is False)
check("no current Noether or BV quotient is promoted",
      exact["equation_quotient_promoted"] is False
      and result["derived_constraint_audit"]["existing_matched_q_noether"] == "FOUR_PARAMETER_KERNEL_IDENTITY"
      and result["derived_constraint_audit"]["existing_offslice_image_differential"] == "NOT_OWNED"
      and result["derived_constraint_audit"]["primitive_epsilon_boundary_moment_map"] == "LIVE")
check("unitary parents remain unported",
      result["action_parent_fence"]["two_U32_32_halves"] == "NOT_PORTED"
      and result["action_parent_fence"]["full_U64_64"] == "NOT_PORTED")
check("accounting remains unchanged",
      result["accounting"]["new_coefficients"] == 0
      and result["accounting"]["new_quotients"] == 0
      and result["accounting"]["new_external_datum"] == 0
      and result["accounting"]["P1_P2_P3"] == "UNCHANGED_UNUSED")
check("ledger is append-only v0.126 from v0.125",
      ledger["schema_version"] == "0.126"
      and ledger["predecessor"].endswith("conditional-physics-ledger-v0.125.json")
      and len(ledger["migrations"]) == 615
      and [m["row_id"] for m in ledger["migrations"][-6:]]
      == ["LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR3", "LT-GR5", "LT-GR6"])
check("headline counts residue and quotients do not move",
      ledger["progress"]["verdict_counts"]
      == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
      and ledger["residue"]["continuous_real"] == 84
      and ledger["residue"]["quotients_ranked"] == 5)
check("report carries source return and exact scope",
      "SOURCE-CONFIRMS" in report and "SOURCE-SILENT" in report
      and "rank `594`" in report and "lower-order and derivative-jet" in report)
check("hostile review records all three scope charges",
      "Charge 1" in review and "Charge 2" in review and "Charge 3" in review
      and "rank `594`" in review and "global subbundle" in review)
check("no canon or posture movement",
      result["claim_status_change"] == "none"
      and result["canon_verdict_change"] == "none"
      and result["public_posture_change"] == "none")

failures = [label for label, ok in checks if not ok]
print(f"PASS {len(checks)-len(failures)}/{len(checks)}")
if failures:
    raise SystemExit("; ".join(failures))
