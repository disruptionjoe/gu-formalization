#!/usr/bin/env python3
"""Durability audit for the K77 zero-order W/mirror parent-leakage gate."""

from collections import Counter
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]
COUNTS = Counter()
FAILURES = []


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


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


ledger = strict("lab/process/conditional-physics-ledger-v0.136.json")
result = strict("lab/process/selected-k77-zero-order-w-mirror-parent-leakage.json")
contract = strict("lab/process/functional-channel-operating-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-k77-zero-order-w-mirror-parent-leakage-2026-08-10.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-10-selected-k77-zero-order-w-mirror-parent-leakage-review.md").read_text()
next_steps = (ROOT / "NEXT-STEPS.md").read_text()
status = (ROOT / "RESEARCH-STATUS.md").read_text()
context = (ROOT / "lab/process/agent-context-pack.md").read_text()

check("ledger", "v0.136 is append-only from v0.135",
      ledger["predecessor"].endswith("conditional-physics-ledger-v0.135.json")
      and ledger["status"] == "CURRENT_APPEND_ONLY_LEDGER_V0_136")
check("ledger", "headline counts remain unchanged",
      ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82
      and ledger["progress"]["verdict_counts"]
      == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("ledger", "frontier closes one gate and opens one named successor",
      ledger["frontier_delta"]
      == {"headline_delta": "NONE", "conditions_closed": 1,
          "conditions_opened": 1, "remaining_named_conditions": 1})
check("ledger", "all three source return classes are explicit",
      all(token in ledger["source_return"]
          for token in ("SOURCE_CONFIRMS", "SOURCE_CORRECTS", "SOURCE_SILENT")))

exact = result["exact_results"]
check("exact", "W and mirror are disjoint rank-192 sectors with rank-384 sum",
      exact["W_rank"] == exact["mirror_rank"] == 192
      and exact["intersection_rank"] == 0 and exact["sum_rank"] == 384)
check("exact", "cross leakage has coefficient rank two for each witness",
      exact["cross_leakage_coefficient_rank_each_witness"] == 2)
check("exact", "outside-pair leakage has coefficient rank two for each witness",
      exact["outside_doubled_pair_coefficient_rank_each_witness"] == 2)
check("exact", "best characteristic-zero witness still leaks rank 64 twice",
      exact["preferred_rank_each_witness"]
      == {"W_internal": 0, "W_to_mirror": 64, "W_outside_pair": 64})
check("type", "parent parity conflict is retained",
      exact["preferred_ratio"]["moving_spin"] == "alpha=beta"
      and exact["preferred_ratio"]["two_u32_32_halves"] == "alpha=beta"
      and exact["preferred_ratio"]["source_full_u64_64_coset"] == "alpha=-beta")
check("type", "W and mirror remain exactly symmetric",
      exact["mirror_symmetry"] == "identical at every tested ratio")
check("type", "scope preserves action-orbit and BV/domain escape classes",
      "action-selected smaller connection orbit" in result["scope"]
      and "BV cohomology" in result["scope"])
check("symplectic", "review forbids presymplectic/BV quotient inflation",
      "no presymplectic or bv quotient is inferred" in review.lower())
check("analytic", "review forbids domain and spectrum inflation",
      "closed domain" in review and "spectrum" in review)
check("source", "report carries confirms, correction and silence separately",
      all(token in report for token in ("SOURCE-CONFIRMS", "SOURCE-CORRECTS", "SOURCE-SILENT")))

changed = {"RA-F1", "RA-F2", "RA-D2", "RA-G2", "LT-SM3", "AC-F1"}
rows = {row["id"]: row for row in ledger["rows"]}
check("ledger", "six intended row dispositions are exact",
      {row["row_id"] for row in ledger["wave_row_dispositions"]} == changed)
check("ledger", "all moved rows cite the new evidence and action-orbit/BV successor",
      all(rows[row_id]["evidence"] == "selected-k77-zero-order-w-mirror-parent-leakage-2026-08-10.md"
          and ("action-owned" in rows[row_id]["distance"] or "action-owned" in rows[row_id]["distance"].lower())
          for row_id in changed))
check("ledger", "six v0.135 to v0.136 migration edges exist",
      sum(edge.get("from_version") == "0.135" and edge.get("to_version") == "0.136"
          for edge in ledger["migrations"]) == 6)
check("ledger", "residue forks quotients and datum remain unchanged",
      ledger["residue"]["continuous_real"] == 84
      and ledger["residue"]["open_discrete_forks"] == 9
      and ledger["residue"]["quotients_ranked"] == 5
      and "P1/P2/P3 remain unchanged/unused" in ledger["residue"]["meter"])

check("routing", "contract points to v0.136 and action-owned orbit/BV successor",
      contract["standing_ledger"]["ref"].endswith("v0.136.json")
      and "ACTION_OWNED" in contract["standing_ledger"]["carrier_selection_directive"])
check("routing", "front doors route to v0.136 successor",
      "v0.136" in next_steps and "v0.136" in status
      and "action-owned" in context.lower() and "mirror" in context.lower())
check("hostile", "three charges and dissent are explicit",
      all(token in review for token in ("Charge 1", "Charge 2", "Charge 3", "Dissent")))
check("accounting", "no status or residue inflation",
      result["verdict_change"] is False and result["residue_change"] is False
      and result["quotient_change"] is False and result["datum_change"] is False)

print("COUNTS " + " ".join(f"{kind}={count}" for kind, count in sorted(COUNTS.items())))
print(f"PASS {sum(COUNTS.values()) - len(FAILURES)}/{sum(COUNTS.values())}")
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
