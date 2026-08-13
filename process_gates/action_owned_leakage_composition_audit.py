#!/usr/bin/env python3
"""Durability audit for ledger v0.137 action-owned leakage composition."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def strict(relative: str):
    path = ROOT / relative

    def hook(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


old = strict("lab/process/conditional-physics-ledger-v0.136.json")
new = strict("lab/process/conditional-physics-ledger-v0.137.json")
result = strict("lab/process/selected-k77-action-owned-leakage-composition.json")
contract = strict("lab/process/functional-channel-operating-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-k77-action-owned-leakage-composition-2026-08-10.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-10-selected-k77-action-owned-leakage-composition-review.md").read_text()
routing = "\n".join((ROOT / name).read_text() for name in (
    "LANES.yaml", "NEXT-STEPS.md", "RESEARCH-STATUS.md", "lab/process/README.md",
    "lab/process/agent-context-pack.md", "lab/process/exploration-absorption-priorities-2026-08-10.md",
))

check("ledger", "v0.137 is append-only from v0.136",
      new["predecessor"].endswith("v0.136.json")
      and [row["id"] for row in new["rows"]] == [row["id"] for row in old["rows"]])
check("ledger", "headline counts remain unchanged",
      new["progress"]["verdict_counts"] == old["progress"]["verdict_counts"]
      and new["progress"]["mapped"] == old["progress"]["mapped"] == 82)
check("ledger", "frontier closes one gate and opens one successor",
      new["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 1,
                                "conditions_opened": 1, "remaining_named_conditions": 1})
check("ledger", "six exact migration edges were appended",
      [(m["row_id"], m["from_version"], m["to_version"]) for m in new["migrations"][-6:]]
      == [(row, "0.136", "0.137") for row in ("RA-D2", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1")])
check("ledger", "six current rows cite the action-owned composition",
      all(row["evidence"] == "selected-k77-action-owned-leakage-composition-2026-08-10.md"
          for row in new["rows"] if row["id"] in {"RA-D2", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"}))

exact = result["exact_results"]
check("exact", "all three named parent witnesses are admitted",
      all(item["admitted"] for item in exact["witnesses"].values()))
check("exact", "no witness is in the pointwise Hessian radical",
      all(not item["hessian_radical"] for item in exact["witnesses"].values()))
check("exact", "full pointwise Hessian remains rank 229376 with zero radical",
      exact["full_pointwise_hessian_rank"] == exact["full_connection_tangent"] == 229376
      and exact["full_pointwise_hessian_radical"] == 0)
check("exact", "v0.136 preferred leakage fingerprint remains 64 plus 64",
      exact["preferred_leakage_each"] == {"W_to_mirror": 64, "outside_W_plus_mirror": 64}
      and exact["cross_and_outside_coefficient_rank_each"] == 2)
check("theorem", "field-tangent escape closes at exact scoped grade",
      result["disposition"] == "ACTION_OWNS_ALL_THREE_LEAK_WITNESSES__NO_ACTION_DERIVED_FIELD_TANGENT_RESTRICTION")

check("layer0", "five action and physical objects stay split",
      result["layer0"] == {
          "field_tangent": "ADMISSIBLE_CONNECTION_VALUES_AND_VARIATIONS",
          "gauge_orbit": "OPEN_DISTINCT",
          "stationary_solution_tangent": "OPEN_DISTINCT",
          "bv": "OPEN_DISTINCT",
          "domain": "OPEN_DISTINCT",
      })
check("scope", "four-field BV solution and analytic gates remain open",
      len(result["scope"]["not_closed"]) == 6
      and "complete four-field operator cancellation" in result["scope"]["not_closed"])
check("source", "source confirmation and silence are separate",
      set(result["source_return"]) == {"SOURCE-CONFIRMS", "SOURCE-SILENT"})
check("hostile", "three charges and dissent are explicit",
      all(token in review for token in ("Charge 1", "Charge 2", "Charge 3", "Dissent")))
check("symplectic", "review refuses Hessian-to-BV quotient inflation",
      "A Hessian is not a presymplectic" in report
      and "no presymplectic characteristic quotient" in review)
check("analytic", "review refuses finite-rank-to-domain inflation",
      "closed operator, spectrum, index or count" in report and "Analytic" in review)
check("variational", "solution-space tangent is fenced",
      "pointwise field tangent into the gauge orbit" not in report
      and "tangent to the full stationary solution space" in report)

check("routing", "contract and front doors point to v0.137",
      contract["standing_ledger"]["ref"].endswith("v0.137.json")
      and "ledger v0.137" in routing)
check("routing", "next gate is four-field BV/domain or adapter",
      "four-field BV/constraint/domain" in routing and "different adapter" in routing)
check("accounting", "no verdict residue quotient datum or P1/P2/P3 moves",
      all(result["accounting"][key] is False for key in (
          "verdict_change", "residue_change", "quotient_change", "datum_change", "p1_p2_p3_change"
      )))
check("accounting", "residue forks and quotients are unchanged",
      new["residue"] == old["residue"])

summary = " ".join(f"{kind}={count}" for kind, count in sorted(COUNTS.items()))
print(f"COUNTS {summary}")
if FAILURES:
    for failure in FAILURES:
        print(f"FAIL: {failure}")
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
