#!/usr/bin/env python3
"""Durability audit for ledger v0.139 K77 graph/lower-left result."""

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


old = strict("lab/process/conditional-physics-ledger-v0.138.json")
new = strict("lab/process/conditional-physics-ledger-v0.139.json")
result = strict("lab/process/selected-k77-southeast-zero-graph-gate.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-k77-southeast-zero-graph-gate-2026-08-10.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-10-selected-k77-southeast-zero-graph-gate-review.md").read_text()
routing = "\n".join((ROOT / name).read_text() for name in (
    "lab/process/RESEARCH-AGENDA.json", "NEXT-STEPS.md", "RESEARCH-STATUS.md", "lab/process/README.md",
    "lab/process/CURRENT-RESEARCH-CONTEXT.md", "lab/process/exploration-absorption-priorities-2026-08-10.md",
))

check("ledger", "v0.139 is append-only from v0.138",
      new["predecessor"].endswith("v0.138.json")
      and [row["id"] for row in new["rows"]] == [row["id"] for row in old["rows"]])
check("ledger", "headline counts remain unchanged",
      new["progress"]["verdict_counts"] == old["progress"]["verdict_counts"]
      and new["progress"]["mapped"] == old["progress"]["mapped"] == 82)
check("ledger", "frontier closes graph and lower-left and opens one source-faithful gate",
      new["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 2,
                                "conditions_opened": 1, "remaining_named_conditions": 1})
check("ledger", "six exact migration edges were appended",
      [(m["row_id"], m["from_version"], m["to_version"]) for m in new["migrations"][-6:]]
      == [(row, "0.138", "0.139") for row in ("RA-D2", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1")])
check("ledger", "six moved rows cite the graph result",
      all(row["evidence"] == "selected-k77-southeast-zero-graph-gate-2026-08-10.md"
          for row in new["rows"] if row["id"] in {"RA-D2", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"}))
old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
moved = {"RA-D2", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"}
check("ledger", "all nonmoved rows are byte-equivalent as parsed objects",
      all(new_rows[row_id] == old_rows[row_id]
          for row_id in old_rows if row_id not in moved))
check("ledger", "moved rows preserve verdict and reason kind",
      all(new_rows[row_id]["verdict"] == old_rows[row_id]["verdict"]
          and new_rows[row_id]["reason_kind"] == old_rows[row_id]["reason_kind"]
          for row_id in moved))
check("ledger", "wave dispositions record the current graph obstruction",
      all("CURRENT_Q_REPAIRED_GRAPH_KILLED" in row["change"]
          for row in new["wave_row_dispositions"]))

fingerprint = result["exact_results"]["uniform_fingerprint"]
check("exact", "unique upper graph is rank 64 with zero residual",
      fingerprint["projected_port_rank"] == 128
      and fingerprint["unique_graph_rank"] == 64
      and fingerprint["upper_residual_rank"] == 0)
check("exact", "induced carrier action vanishes",
      fingerprint["induced_carrier_action_rank"] == 0)
check("exact", "action-tied lower-left and complete residual have rank 64",
      fingerprint["lower_left_on_carrier_rank"] == 64
      and fingerprint["lower_residual_rank"] == 64
      and fingerprint["lower_residual_nonzero_entries"] == 384)
check("exact", "sign flip does not rescue the lower equation",
      fingerprint["sign_flipped_lower_residual_rank"] == 64)
check("exact", "same-carrier southeast postcomposition cannot factor the lower map",
      fingerprint["graph_plus_lower_row_rank"] == 128
      and fingerprint["same_carrier_southeast_factor_exists"] is False)
check("exact", "finite and Gaussian-rational fields and W/mirror equality are recorded",
      result["exact_results"]["fields"] == ["GF(1000033)", "QQ(i)"]
      and result["exact_results"]["w_equals_mirror"] is True)
check("theorem", "only the current q-repaired graph is killed",
      "CURRENT_Q_REPAIRED_GRAPH_KILLED" in result["disposition"]
      and "source-faithful resolution" in result["scope"]["not_closed"][0])

check("layer0", "conditional rival and source-faithful operator remain split",
      result["layer0"]["tested_operator"] == "CURRENT_Q_REPAIRED_K77_CONDITIONAL_RIVAL"
      and result["layer0"]["source_faithful_ambient_half_operator"] == "OPEN_DISTINCT")
check("scope", "replacement Shiab, BV and domain remain open",
      any("different source-family Shiab" in item for item in result["scope"]["not_closed"])
      and result["layer0"]["bv_cohomology"] == "OPEN_DISTINCT"
      and result["layer0"]["analytic_domain"] == "OPEN_DISTINCT")
check("source", "source confirmation correction and silence are separate",
      set(result["source_return"]) == {"SOURCE-CONFIRMS", "SOURCE-CORRECTS", "SOURCE-SILENT"})
check("hostile", "three charges and dissent are explicit",
      all(token in review for token in ("Charge 1", "Charge 2", "Charge 3", "Dissent")))
check("symplectic", "review refuses graph-to-BV inflation",
      "Graph invariance is still not" in report and "no presymplectic or BV quotient" in review)
check("analytic", "review refuses finite-rank-to-domain inflation",
      "No closed" not in report or "domain" in report
      and "no domain, spectrum" in review)
check("variational", "the lower-left adjoint is action-tied",
      "action-tied" in report and "action-tied" in review)

check("ledger", "current append-only ledger descends to v0.139",
      reaches_historical_snapshot(
          contract, "lab/process/conditional-physics-ledger-v0.139.json"))
check("routing", "next gate is the source-faithful sign and degree-duality collision",
      "ambient-half-sign" in routing and "degree-duality" in routing)
check("accounting", "no verdict residue quotient datum or P1/P2/P3 moves",
      all(result["accounting"][key] is False for key in (
          "verdict_change", "residue_change", "quotient_change", "datum_change", "p1_p2_p3_change"
      )))
check("accounting", "residue forks and quotients are unchanged",
      new["residue"] == old["residue"])

print("COUNTS " + " ".join(f"{kind}={count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    for failure in FAILURES:
        print(f"FAIL: {failure}")
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
