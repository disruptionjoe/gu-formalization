#!/usr/bin/env python3
"""Durability audit for ledger v0.140 trace-q degree-duality result."""

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


old = strict("lab/process/conditional-physics-ledger-v0.139.json")
new = strict("lab/process/conditional-physics-ledger-v0.140.json")
result = strict("lab/process/selected-k77-degree-duality-pair-graph-gate.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-k77-degree-duality-pair-graph-gate-2026-08-10.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-10-selected-k77-degree-duality-pair-graph-review.md").read_text()
routing = "\n".join((ROOT / name).read_text() for name in (
    "lab/process/RESEARCH-AGENDA.json", "NEXT-STEPS.md", "RESEARCH-STATUS.md", "lab/process/README.md",
    "lab/process/CURRENT-RESEARCH-CONTEXT.md", "lab/process/exploration-absorption-priorities-2026-08-10.md",
))

moved = {"RA-D2", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"}
old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
check("ledger", "v0.140 is append-only from v0.139",
      new["predecessor"].endswith("v0.139.json")
      and [row["id"] for row in new["rows"]] == [row["id"] for row in old["rows"]])
check("ledger", "headline counts remain unchanged",
      new["progress"]["verdict_counts"] == old["progress"]["verdict_counts"]
      and new["progress"]["mapped"] == old["progress"]["mapped"] == 82)
check("ledger", "frontier closes two conditions and opens one replacement gate",
      new["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 2,
                                "conditions_opened": 1, "remaining_named_conditions": 1})
check("ledger", "six exact migration edges were appended",
      [(m["row_id"], m["from_version"], m["to_version"]) for m in new["migrations"][-6:]]
      == [(row, "0.139", "0.140") for row in ("RA-D2", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1")])
check("ledger", "six moved rows cite the degree-duality result",
      all(row["evidence"] == "selected-k77-degree-duality-pair-graph-gate-2026-08-10.md"
          for row in new["rows"] if row["id"] in moved))
check("ledger", "all nonmoved rows are byte-equivalent as parsed objects",
      all(new_rows[row_id] == old_rows[row_id] for row_id in old_rows if row_id not in moved))
check("ledger", "moved rows preserve verdict and reason kind",
      all(new_rows[row_id]["verdict"] == old_rows[row_id]["verdict"]
          and new_rows[row_id]["reason_kind"] == old_rows[row_id]["reason_kind"]
          for row_id in moved))
check("ledger", "wave dispositions record the source-sign route kill",
      all("CANONICAL_TRACE_Q_SOURCE_SIGN_DEGREE_DUALITY_KILLED" in row["change"]
          for row in new["wave_row_dispositions"]))

exact = result["exact_result"]
check("exact", "bare q leaks rank 64 outside RS", exact["bare_q_outside_rs_rank"] == 64)
check("exact", "Pin q preserves RS and swaps W with mirror both ways",
      exact["pin_q_preserves_rs"] and exact["pin_q_w_to_mirror"] and exact["pin_q_mirror_to_w"])
check("exact", "the resulting pair closure has rank 384", exact["closed_pair_rank"] == 384)
check("exact", "both source-sign upper images are independent rank-128 planes",
      exact["each_source_faithful_projected_port_rank"] == 128
      and exact["each_source_faithful_projected_leak_rank"] == 128
      and exact["each_source_faithful_joined_rank"] == 256
      and exact["upper_graph_exists"] is False)
check("control", "old q family passes the same upper-image gate",
      exact["old_q_family_control_joined_rank"] == 128)
check("exact", "finite and Gaussian-rational fields and three parents are recorded",
      exact["fields"] == ["GF(1000033)", "QQ(i)"] and len(exact["parents"]) == 3)

check("layer0", "source field labels and degree primalizers remain distinct",
      result["layer0"]["source_labels"] == "AMBIENT_HALF_SPINOR"
      and result["layer0"]["degree_duality"] == "EXPLICIT_ROW_COLUMN_PRIMALIZER")
check("layer0", "bare q and Pin-completed q are distinguished",
      result["layer0"]["bare_q"] == "SPINOR_INTERTWINER"
      and result["layer0"]["pin_q"] == "ONE_FORM_REFLECTION_TENSOR_SPINOR_INTERTWINER")
check("source", "source confirmation correction and silence are separate",
      set(result["source_return"]) == {"SOURCE-CONFIRMS", "SOURCE-CORRECTS", "SOURCE-SILENT"})
check("scope", "only canonical trace-q degree duality on this carrier is killed",
      result["scope_fence"].startswith("NOT_A_NO_GO_FOR_FULL_D916_SOURCE_FAMILY"))
check("hostile", "three charges and dissent are explicit",
      all(token in review for token in ("Charge 1", "Charge 2", "Charge 3", "Dissent")))
check("symplectic", "review refuses graph-to-BV inflation",
      "BV" in review and "presymplectic" in review)
check("analytic", "review refuses finite-rank-to-domain inflation",
      "domain" in review and "spectrum" in review)
check("variational", "source-sign primalizers are not field relabelings",
      "not\nfield-subscript relabelings" in report or "not field-subscript relabelings" in report)

check("ledger", "current append-only ledger descends to v0.140",
      reaches_historical_snapshot(
          contract, "lab/process/conditional-physics-ledger-v0.140.json"))
check("routing", "sign-cluster stopping rule routes to new operator or functional build",
      "stopping rule" in routing and "coupled-functional" in routing)
check("accounting", "no verdict residue quotient datum or P1/P2/P3 moves",
      all(result["accounting"][key] is False for key in (
          "verdicts_changed", "residue_changed", "quotients_changed", "datum_changed", "P1_P2_P3_used"
      )))
check("accounting", "residue forks and quotients are unchanged",
      new["residue"] == old["residue"])

print("COUNTS " + " ".join(f"{kind}={count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    for failure in FAILURES:
        print(f"FAIL: {failure}")
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
