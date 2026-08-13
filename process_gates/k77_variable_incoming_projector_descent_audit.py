#!/usr/bin/env python3
"""Process gate for ledger v0.180 variable incoming-projector descent."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COUNTS = Counter()
FAILURES = []


def strict(relative):
    path = ROOT / relative

    def reject(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError(f"duplicate key {key!r}: {path}")
            out[key] = value
        return out

    return json.loads(path.read_text(), object_pairs_hook=reject)


def check(kind, label, value):
    COUNTS[kind] += 1
    ok = bool(value)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


ledger = strict("lab/process/conditional-physics-ledger-v0.180.json")
previous = strict("lab/process/conditional-physics-ledger-v0.179.json")
result = strict("lab/process/selected-k77-variable-incoming-projector-descent.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")

check("ledger", "append-only successor identity is exact",
      ledger["schema_version"] == "0.180"
      and ledger["predecessor"].endswith("v0.179.json"))
check("ledger", "headline counts remain unchanged",
      ledger["progress"]["verdict_counts"] == previous["progress"]["verdict_counts"])
check("ledger", "residue and quotient count remain unchanged",
      ledger["residue"]["continuous_real"] == previous["residue"]["continuous_real"] == 84
      and ledger["residue"]["quotients_ranked"] == previous["residue"]["quotients_ranked"] == 5)
check("ledger", "frontier records three closures and no opening",
      ledger["frontier_delta"] == {
          "headline_delta": "NONE", "conditions_closed": 3,
          "conditions_opened": 0, "remaining_named_conditions": 2,
      })
check("ledger", "exactly six current wave rows migrated",
      {item["row_id"] for item in ledger["wave_row_dispositions"]}
      == {"RA-D4", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"})

check("result", "new exact probe has zero failures and six plants",
      result["checks"] == {"total": 63, "failures": 0, "planted": 6})
check("result", "immutable full-carrier half ranks are preserved",
      result["immutable_full_carrier"]["rank"] == 1920
      and result["immutable_full_carrier"]["incoming_rank"]
      == result["immutable_full_carrier"]["outgoing_rank"] == 960)
check("result", "projector is the action polynomial of half rank",
      result["projector_family"]["rank"] == 960
      and result["projector_family"]["rank_fraction"] == "1/2"
      and result["projector_family"]["associated_bundle_descent"])
check("result", "moving derivative and negative flux are exact",
      result["projector_family"]["connection_naturality"]
      and result["projector_family"]["negative_flux"])
check("ownership", "action owns the family but not a unique boundary",
      result["ownership"]["action_owns"].startswith("THE_MAP_FROM")
      and not result["ownership"]["independent_projector_datum_needed"]
      and not result["ownership"]["unique_global_boundary_selected"])
check("layer0", "the member still requires boundary geometry",
      result["projector_family"]["requires_oriented_unit_noncharacteristic_conormal"]
      and "BOUNDARY_HYPERSURFACE" in result["ownership"]["observation_boundary_geometry_owns"])
check("scope", "both horns transport without selection",
      set(result["pairing_horns"].values())
      == {"TRANSPORTED_DOUBLED_MAJORANA_GREEN_ISOTROPIC", "NONE"})
check("scope", "global analytic closure remains fenced",
      "GLOBAL_IN_TIME" in result["analytic_status"]
      and "CLOSURE_OPEN" in result["analytic_status"])
check("scope", "P1/P2/P3, verdict, residue, quotient and canon stay still",
      not result["p1_p2_p3_used"] and not result["verdict_change"]
      and not result["booked_residue_change"] and not result["quotient_change"]
      and not result["canon_verdict_change"] and not result["public_posture_change"])

standing = contract["standing_ledger"]
check("routing", "operating contract points at v0.180",
      standing["ref"].endswith("v0.180.json")
      and standing["human_ref"].endswith("v0.180.md"))
check("routing", "successor starts with constraint/BV and mirror cohomology",
      contract["current_priority_decision"]["main_sequence"][0]
      == "COMPOSE_ACTION_DERIVED_INCOMING_PROJECTOR_WITH_CONSTRAINT_BV_AND_OBSERVATION")

for relative, needles in {
    "NEXT-STEPS.md": ["ledger v0.180", "projector family"],
    "RESEARCH-STATUS.md": ["ledger v0.180", "boundary geometry"],
    "lab/process/CURRENT-RESEARCH-CONTEXT.md": ["Current v0.180", "two `U(32,32)` halves"],
    "lab/process/hostile-reviews/2026-08-11-selected-k77-variable-incoming-projector-descent-review.md": ["SURVIVES_SCOPED", "Symplectic"],
    "lab/sources/selected-k77-variable-incoming-projector-descent-source-return-2026-08-11.md": ["SOURCE-SILENT", "projector"],
}.items():
    text = (ROOT / relative).read_text()
    check("surface", f"{relative} carries the required scope",
          all(needle in text for needle in needles))

print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: v0.180 variable incoming-projector packet is routed and scope-fenced.")
