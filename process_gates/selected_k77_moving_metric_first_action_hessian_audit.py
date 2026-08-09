#!/usr/bin/env python3
"""Static scope/provenance audit for the v0.125 metric-Hessian result."""

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


result = strict("lab/process/selected-k77-moving-metric-first-action-hessian.json")
ledger = strict("lab/process/conditional-physics-ledger-v0.125.json")
bank = strict("tests/fixtures/k77_exact_coefficient_bank_v1.json")
report = (ROOT / "explorations/conditional-build/selected-k77-moving-metric-first-action-hessian-2026-08-09.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-09-selected-k77-moving-metric-first-action-hessian-review.md").read_text()

check("registry is principal selected-Spin first action",
      result["scope"]["differential_grade"] == "LOCAL_PRINCIPAL_SYMBOL"
      and result["scope"]["parent"].startswith("CONDITIONALLY_SELECTED_REAL_SPIN77"))
check("complete metric ranks are exact 9/9/4",
      result["exact_result"]["metric_ranks"] == {"full": 9, "horizontal": 9, "offslice": 4})
check("epsilon ranks remain exact 91/6/88",
      result["exact_result"]["epsilon_ranks_inherited_complete"] == {"full": 91, "horizontal": 6, "offslice": 88})
check("321 is not closed but 1571 is not promoted",
      result["exact_result"]["selected_321_hessian_closed"] is False
      and result["exact_result"]["full_1571_promoted"] is False)
check("no equation quotient is promoted",
      result["exact_result"]["equation_quotient_promoted"] is False
      and result["accounting"]["new_quotients"] == 0)
check("both unitary-parent ports remain absent",
      result["action_parent_fence"]["two_U32_32_halves"] == "NOT_PORTED"
      and result["action_parent_fence"]["full_U64_64"] == "NOT_PORTED"
      and bank["scientific_scope"]["two_U32_32_halves"] == "NOT_PORTED"
      and bank["scientific_scope"]["full_U64_64"] == "NOT_PORTED")
check("P1 P2 P3 remain unused", result["accounting"]["P1_P2_P3"] == "UNCHANGED_UNUSED")
check("ledger is append-only v0.125 from v0.124",
      ledger["schema_version"] == "0.125"
      and ledger["predecessor"].endswith("conditional-physics-ledger-v0.124.json"))
check("headline counts and residue do not move",
      ledger["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5}
      and ledger["residue"]["continuous_real"] == 84)
check("report states exact source return and no quotient by fiat",
      "SOURCE-CONFIRMS" in report and "SOURCE-SILENT" in report
      and "NO_QUOTIENT_BY_FIAT" in report)
check("hostile review preserves strongest surviving scope attack",
      "local principal" in review and "algebraic cokernel" in review)
check("no canon or posture movement", result["claim_status_change"] == "none"
      and result["canon_verdict_change"] == "none"
      and result["public_posture_change"] == "none")

failures = [label for label, ok in checks if not ok]
print(f"PASS {len(checks)-len(failures)}/{len(checks)}")
if failures:
    raise SystemExit("; ".join(failures))
