#!/usr/bin/env python3
"""Durability audit for ledger v0.141 zero-fermion current-order result."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

from conditional_physics_ledger_v03_scope_audit import reaches_historical_snapshot


ROOT = Path(__file__).resolve().parents[1]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def strict(relative: str):
    path = ROOT / relative

    def hook(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate key {key!r}: {path}")
            result[key] = value
        return result

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


old = strict("lab/process/conditional-physics-ledger-v0.140.json")
new = strict("lab/process/conditional-physics-ledger-v0.141.json")
result = strict("lab/process/selected-k77-zero-fermion-coupled-hessian-current-order.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-k77-zero-fermion-coupled-hessian-current-order-2026-08-10.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-10-selected-k77-zero-fermion-coupled-hessian-current-order-review.md").read_text()
routing = "\n".join((ROOT / name).read_text() for name in (
    "lab/process/RESEARCH-AGENDA.json", "NEXT-STEPS.md", "RESEARCH-STATUS.md", "lab/process/README.md",
    "lab/process/CURRENT-RESEARCH-CONTEXT.md", "lab/process/exploration-absorption-priorities-2026-08-10.md",
))

moved = {"LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR6"}
old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
migrations = [item for item in new["migrations"] if item["to_version"] == "0.141"]

check("ledger", "v0.141 is append-only from v0.140",
      new["predecessor"].endswith("v0.140.json")
      and [row["id"] for row in new["rows"]] == [row["id"] for row in old["rows"]])
check("ledger", "headline counts remain unchanged",
      new["progress"]["verdict_counts"] == old["progress"]["verdict_counts"]
      and new["progress"]["mapped"] == old["progress"]["mapped"] == 82)
check("ledger", "frontier closes three conditions and opens one branch",
      new["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 3,
                                "conditions_opened": 1, "remaining_named_conditions": 2})
check("ledger", "four exact migration edges were added",
      [(m["row_id"], m["from_version"], m["to_version"]) for m in migrations]
      == [(row, "0.140", "0.141") for row in ("LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR6")])
check("ledger", "moved rows cite the current-order result",
      all(new_rows[row]["evidence"] == "selected-k77-zero-fermion-coupled-hessian-current-order-2026-08-10.md"
          for row in moved))
check("ledger", "all nonmoved rows are parsed-object identical",
      all(new_rows[row_id] == old_rows[row_id] for row_id in old_rows if row_id not in moved))
check("ledger", "moved rows preserve verdict and reason kind",
      all(new_rows[row_id]["verdict"] == old_rows[row_id]["verdict"]
          and new_rows[row_id]["reason_kind"] == old_rows[row_id]["reason_kind"]
          for row_id in moved))
check("ledger", "primary queue now advances the bosonic functional branch",
      any(item["rank"] == 1 and set(item["rows"]) == moved for item in new["next_work_queue"]))

exact = result["exact_result"]
check("exact", "zero-fermion current and mixed Hessian ranks are zero",
      exact["zero_fermion_current_rank"] == 0 and exact["zero_fermion_mixed_hessian_rank"] == 0)
check("exact", "fermion Hessian remains live and total fixture Hessian has rank 16",
      exact["fermion_fixture_block_rank"] == 3 and exact["full_fixture_hessian_rank"] == 16)
check("exact", "current first appears in the cubic dD/db vertex",
      exact["current_vertex_order"] == 3 and exact["two_fermion_one_boson_vertex"] == "dD/db")
check("exact", "the carried nonzero metric trace is retained",
      exact["direct_metric_trace_retained"] and exact["direct_metric_trace_rank"] == 1)
check("control", "duplicate bridge is rejected by vertex erasure",
      exact["duplicate_total_current_bridge"] == "ERASES_ACTION_OWNED_VERTEX")
check("ward", "current Ward term is tied to fermion Euler contractions",
      exact["even_ward"] == "CONNECTION_CURRENT_CANCELS_FERMION_EULER_CONTRACTIONS_OFF_SHELL")

check("layer0", "current Hessian and vertex are distinctly typed",
      result["layer0"]["current"].endswith("QUADRATIC_IN_FERMIONS")
      and result["layer0"]["vertex"].startswith("ONE_BOSON_TWO_FERMION"))
check("layer0", "zero and nonzero fermion backgrounds are distinct",
      "ZERO_FERMION_DISTINCT" in result["layer0"]["backgrounds"])
check("source", "confirmation and silence are explicit",
      "SOURCE_CONFIRMS" in result["source_return"] and "SOURCE_SILENT" in result["source_return"])
check("scope", "physical operator spectrum domain and BV quotient remain excluded",
      set(result["scope"]["does_not_decide"]) == {
          "SOURCE_SELECTED_K77_DIRAC_RS_OPERATOR", "NONZERO_FERMION_STATIONARY_SOLUTION",
          "SPECTRUM_OR_INDEX_OR_GENERATION_COUNT", "HYPERBOLIC_OR_KREIN_CLOSED_DOMAIN",
          "BV_COHOMOLOGY_OR_PHYSICAL_QUOTIENT",
      })
check("hostile", "three charges and dissent are explicit",
      all(token in review for token in ("### 1.", "### 2.", "### 3.", "## Dissent")))
check("symplectic", "review refuses Hessian-to-BV inflation",
      "symplectic/BV" in review and "physical direct sum" in review)
check("analytic", "review refuses algebraic-rank-to-domain inflation",
      "Fredholm" in review and "hyperbolic" in review)
check("variational", "report separates first second and third derivatives",
      "first, second and third derivatives" in report)

check("ledger", "current append-only ledger descends to v0.141",
      reaches_historical_snapshot(
          contract, "lab/process/conditional-physics-ledger-v0.141.json"))
check("routing", "front doors prioritize bosonic stress/BV and separate fermion branch",
      "zero-fermion" in routing and "nonzero-fermion" in routing)
check("accounting", "no headline accounting moves",
      all(result["changes"][key] == "none" for key in (
          "verdict_change", "residue_change", "booked_quotient_change",
          "canon_verdict_change", "public_posture_change",
      )))
check("accounting", "residue forks and quotients are unchanged", new["residue"] == old["residue"])

print("COUNTS " + " ".join(f"{kind}={count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    for failure in FAILURES:
        print(f"FAIL: {failure}")
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
