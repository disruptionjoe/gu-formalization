#!/usr/bin/env python3
"""Append-only integrity gate for conditional physics ledger v0.91."""

from collections import Counter
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[2]
COUNTS = Counter()
FAILURES = []


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


def check(kind, label, condition):
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


old = strict("lab/process/conditional-physics-ledger-v0.90.json")
new = strict("lab/process/conditional-physics-ledger-v0.91.json")
registry = strict("lab/process/selected-k77-action-frechet-ward-object-separation.json")

check("ledger", "v0.91 points to immutable v0.90", new["predecessor"].endswith("v0.90.json"))
check("ledger", "denominator and row ids are frozen", new["denominator"] == old["denominator"] and [r["id"] for r in new["rows"]] == [r["id"] for r in old["rows"]])
check("ledger", "verdict counts are frozen", new["progress"]["verdict_counts"] == old["progress"]["verdict_counts"])
check("ledger", "residue and five scoped quotients are frozen", new["residue"] == old["residue"] and new["residue"]["quotients_ranked"] == 5)
check("ledger", "frontier closes two and leaves two", new["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 2, "conditions_opened": 0, "remaining_named_conditions": 2})
check("source", "source return uses the governed vocabulary", new["source_return"] == "SOURCE-CONFIRMS")

row_ids = ["LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"]
tail = new["migrations"][-5:]
check("migration", "five v0.91 migrations append in declared order", [m["row_id"] for m in tail] == row_ids and all(m["from_version"] == "0.90" and m["to_version"] == "0.91" for m in tail))
for row_id in row_ids:
    before = next(r for r in old["rows"] if r["id"] == row_id)
    after = next(r for r in new["rows"] if r["id"] == row_id)
    check("migration", f"{row_id}: verdict and reason kind survive", (after["verdict"], after["reason_kind"]) == (before["verdict"], before["reason_kind"]))
    check("migration", f"{row_id}: evidence points to the object-separation result", after["evidence"] == "selected-k77-action-frechet-ward-object-separation-2026-08-08.md")
    check("migration", f"{row_id}: frontier names an open transverse/J/K burden", "OPEN" in after["frontier_grade"] and any(token in after["frontier_grade"] for token in ("TRANSVERSE", "GRAM", "K_GREEN", "K_ADJOINT")))

check("theorem", "first-action bank remains exact and distinct", registry["exact_results"]["first_action_bank_rank"] == 14 and registry["layer0"]["raw_residual_jacobian"].endswith("DISTINCT_AND_PARTIAL"))
check("theorem", "four Ward versus six transverse is recorded", registry["exact_results"]["physical_ward_orbit_rank"] == 4 and registry["exact_results"]["transverse_metric_rank"] == 6)
check("theorem", "full actual J and K remain open", registry["exact_results"]["actual_full_coefficientwise_J_R_zero"].startswith("OPEN") and registry["exact_results"]["residual_pairing_K"] == "OPEN")
check("signature", "ordinary MW selector is conditional and K95 stays a pseudoreal control", "ONLY_IF" in registry["signature_condition"]["disposition"] and registry["signature_condition"]["K77"]["ordinary_majorana_weyl"] and not registry["signature_condition"]["K95"]["ordinary_majorana_weyl"] and registry["signature_condition"]["K95"]["symplectic_majorana_weyl_with_extra_doublet"])
check("scope", "no datum or residue is consumed", not registry["constraint_accounting"]["external_datum_used"] and not registry["constraint_accounting"]["residue_changed"] and registry["constraint_accounting"]["P1_P2_P3"] == "UNCHANGED_UNUSED")

print("SOURCE_RETURN=SOURCE-CONFIRMS")
print("FRONTIER=FIRST_ACTION_BANK_REUSED__FOUR_WARD_COLUMNS_TYPED__SIX_TRANSVERSE_J_AND_K_OPEN")
print("CHECKS=" + " ".join(f"{kind}:{count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
