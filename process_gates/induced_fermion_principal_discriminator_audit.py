#!/usr/bin/env python3
"""Durability audit for the K77 induced-fermion principal discriminator."""

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


ledger = strict("lab/process/conditional-physics-ledger-v0.135.json")
result = strict("lab/process/selected-k77-induced-fermion-principal-discriminator.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-k77-induced-fermion-principal-discriminator-2026-08-10.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-10-selected-k77-induced-fermion-principal-discriminator-review.md").read_text()
next_steps = (ROOT / "NEXT-STEPS.md").read_text()
status = (ROOT / "RESEARCH-STATUS.md").read_text()
context = (ROOT / "lab/process/CURRENT-RESEARCH-CONTEXT.md").read_text()

check("ledger", "v0.135 is append-only from v0.134",
      ledger["predecessor"].endswith("conditional-physics-ledger-v0.134.json")
      and ledger["status"] == "CURRENT_APPEND_ONLY_LEDGER_V0_135")
check("ledger", "headline counts remain unchanged",
      ledger["progress"]["mapped"] == ledger["progress"]["total"] == 82
      and ledger["progress"]["verdict_counts"]
      == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("ledger", "frontier closes principal selection and opens one lower-order gate",
      ledger["frontier_delta"]
      == {"headline_delta": "NONE", "conditions_closed": 1,
          "conditions_opened": 1, "remaining_named_conditions": 1})
check("ledger", "source return is explicit",
      "SOURCE_CONFIRMS" in ledger["source_return"] and "SOURCE_SILENT" in ledger["source_return"])

sectors = result["exact_result"]["base_null_coupled_sector_ranks"]
check("exact", "full K77 symbol anchors are retained",
      result["exact_result"]["full_symbol"] == {"nonnull_rank": 1920, "null_rank": 1024, "null_kernel": 896})
check("exact", "W and mirror have identical exact 224/96 results",
      sectors["W_sd192"]["rank"] == sectors["mirror_asd192"]["rank"] == 224
      and sectors["W_sd192"]["kernel"] == sectors["mirror_asd192"]["kernel"] == 96)
check("exact", "all natural sectors have half-kernel rule",
      all(2 * row["kernel"] == row["one_form_dimension"] for row in sectors.values()))
check("planted", "all random controls reject the natural half-kernel value",
      all(row["kernel"] != 96 for row in result["exact_result"]["random_192_controls"]))
check("type", "parent ablations share the principal fingerprint for a stated lower-order reason",
      result["parent_ablations"]["source_full_U64_64"]
      == result["parent_ablations"]["moving_Spin"]
      == result["parent_ablations"]["two_U32_32_halves"]
      and "zero-order" in result["parent_ablations"]["reason"])
check("type", "result fires the partial rather than selection horn",
      result["disposition"]["preregistered_horn"] == "PRINCIPAL_PARTIAL")
check("type", "characteristic and physical objects remain fenced",
      any("physical kernel" in item for item in result["layer0"]["not_computed"])
      and "generation count" in result["layer0"]["not_computed"])
check("symplectic", "review forbids quotient inflation",
      "No presymplectic current" in review and "Booking a quotient would be invalid" in review)
check("analytic", "review forbids spectrum and index inflation",
      "do not provide a closed realization" in review and "Fredholm" in review)
check("source", "report carries source confirms and silence separately",
      "SOURCE-CONFIRMS" in report and "SOURCE-SILENT" in report)

changed = {"RA-F1", "RA-F2", "RA-D2", "RA-G2", "LT-SM3", "AC-F1"}
rows = {row["id"]: row for row in ledger["rows"]}
check("ledger", "six intended row dispositions are exact",
      {row["row_id"] for row in ledger["wave_row_dispositions"]} == changed)
check("ledger", "all moved rows cite the new evidence and lower-order successor",
      all(rows[row_id]["evidence"] == "selected-k77-induced-fermion-principal-discriminator-2026-08-10.md"
          and "zero-order" in rows[row_id]["distance"].lower() for row_id in changed))
check("ledger", "six v0.134 to v0.135 migration edges exist",
      sum(edge.get("from_version") == "0.134" and edge.get("to_version") == "0.135"
          for edge in ledger["migrations"]) == 6)
check("ledger", "residue forks quotients and datum remain unchanged",
      ledger["residue"]["continuous_real"] == 84
      and ledger["residue"]["open_discrete_forks"] == 9
      and ledger["residue"]["quotients_ranked"] == 5
      and "P1/P2/P3 remain unchanged/unused" in ledger["residue"]["meter"])

check("routing", "contract points to v0.135 and lower-order discriminator",
      contract["standing_ledger"]["ref"].endswith("v0.135.json")
      and "DRAFT916_ZERO_ORDER" in contract["standing_ledger"]["carrier_selection_directive"])
check("routing", "front doors route to v0.135 successor",
      "v0.135" in next_steps and "v0.135" in status
      and "zero-order" in context.lower() and "mirror" in context.lower())
check("hostile", "three charges and dissent are explicit",
      all(token in review for token in ("Charge 1", "Charge 2", "Charge 3", "Dissent")))
check("accounting", "no status or residue inflation",
      result["accounting"]["claim_status_change"] == "none"
      and result["accounting"]["canon_verdict_change"] == "none"
      and result["accounting"]["residue_change"] == "none"
      and result["accounting"]["quotient_change"] == "none")

print("COUNTS " + " ".join(f"{kind}={count}" for kind, count in sorted(COUNTS.items())))
print(f"PASS {sum(COUNTS.values()) - len(FAILURES)}/{sum(COUNTS.values())}")
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
