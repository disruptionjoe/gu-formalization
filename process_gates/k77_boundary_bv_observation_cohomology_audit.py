#!/usr/bin/env python3
"""Process gate for ledger v0.181 boundary BRST and carrier closure."""

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


ledger = strict("lab/process/conditional-physics-ledger-v0.181.json")
previous = strict("lab/process/conditional-physics-ledger-v0.180.json")
result = strict("lab/process/selected-k77-boundary-bv-observation-cohomology.json")
contract = strict("lab/methods/research-evidence-contract-v1.0.json")

check("ledger", "append-only successor identity is exact",
      ledger["schema_version"] == "0.181"
      and ledger["predecessor"].endswith("v0.180.json"))
check("ledger", "headline counts remain unchanged",
      ledger["progress"]["verdict_counts"] == previous["progress"]["verdict_counts"])
check("ledger", "residue and quotient count remain unchanged",
      ledger["residue"]["continuous_real"] == previous["residue"]["continuous_real"] == 84
      and ledger["residue"]["quotients_ranked"] == previous["residue"]["quotients_ranked"] == 5)
check("ledger", "frontier records three closures and one new discriminator",
      ledger["frontier_delta"] == {
          "headline_delta": "NONE", "conditions_closed": 3,
          "conditions_opened": 1, "remaining_named_conditions": 2,
      })
check("ledger", "exactly six current wave rows migrated",
      {item["row_id"] for item in ledger["wave_row_dispositions"]}
      == {"RA-D4", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"})
check("ledger", "six append-only v0.181 history records exist",
      sum(item.get("to_version") == "0.181" for item in ledger["migration_history"]) == 6)

check("result", "new exact probe has zero failures and four firing plants",
      result["checks"] == {
          "total": 45, "failures": 0, "planted": 4, "two_prime_exact": True,
      })
check("result", "full-carrier incoming split is preserved",
      result["full_carrier"]["rank"] == 1920
      and result["full_carrier"]["incoming_rank"]
      == result["full_carrier"]["outgoing_rank"] == 960)
check("brst", "ordinary gauge boundary relation and observation descent close",
      result["ordinary_gauge_boundary"]["projector_brst_covariant"]
      and result["ordinary_gauge_boundary"]["boundary_relation_chain_natural"]
      and result["ordinary_gauge_boundary"]["three_patch_observation_descent"]
      and "NOT_FULL_BV_KT" in result["ordinary_gauge_boundary"]["scope"])

fingerprint = result["carrier_fingerprint"]
check("carrier", "W and mirror exact fingerprints agree",
      fingerprint["W"] == fingerprint["mirror"]
      and fingerprint["W"]["rank"] == 320
      and fingerprint["W"]["incoming_leakage"] == 128)
check("carrier", "W plus mirror still leaks from the incoming relation",
      fingerprint["W_plus_mirror"]["rank"] == 512
      and fingerprint["W_plus_mirror"]["incoming_leakage"] == 128
      and not result["restricted_w_mirror_boundary_complex_exists"])

hull = result["common_spatial_action_hull"]
check("closure", "all three seeds generate the same rank-640 action hull",
      hull["rank_from_W"] == hull["rank_from_mirror"]
      == hull["rank_from_pair"] == 640
      and hull["same_hull_by_inclusion_and_rank"])
check("closure", "H640 is exactly fenced as 512 plus 128",
      hull["one_form_projection_rank"] == 512
      and hull["zero_form_projection_rank"] == 128
      and not hull["source_selected"]
      and not hull["identified_with_old_one_form_640"])
check("pin", "naive complete Pin lift remains a negative control",
      result["pin_disposition"].startswith("ONE_FORM_PIN_EXCHANGES")
      and "OTHER_FOUR_FIELD_PIN_LIFTS_OPEN" in result["pin_disposition"])
check("scope", "P1/P2/P3 and all public accounting remain still",
      not result["p1_p2_p3_used"] and not result["verdict_change"]
      and not result["booked_residue_change"] and not result["quotient_change"]
      and not result["canon_verdict_change"] and not result["public_posture_change"])

standing = contract["standing_ledger"]
check("routing", "operating contract points at v0.181",
      standing["ref"].endswith("v0.181.json")
      and standing["human_ref"].endswith("v0.181.md"))
check("routing", "successor begins with H640 discriminator controls",
      contract["current_priority_decision"]["main_sequence"][0]
      == "CONTROL_COMMON_H640_AGAINST_RANDOM192_OLD_ONE_FORM640_AND832")

for relative, needles in {
    "NEXT-STEPS.md": ["ledger v0.181", "H640=512+128"],
    "RESEARCH-STATUS.md": ["ledger v0.181", "old one-form 640"],
    "lab/process/CURRENT-RESEARCH-CONTEXT.md": ["Current v0.181", "two `U(32,32)` halves"],
    "lab/process/hostile-reviews/2026-08-11-selected-k77-boundary-bv-observation-cohomology-review.md": ["SURVIVES_SCOPED", "symplectic/BFV"],
    "lab/sources/selected-k77-boundary-bv-observation-cohomology-source-return-2026-08-11.md": ["SOURCE-SILENT", "SOURCE_CONFIRMS_FOUR_FIELD"],
}.items():
    text = (ROOT / relative).read_text()
    check("surface", f"{relative} carries the required scope",
          all(needle in text for needle in needles))

print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: v0.181 boundary BRST and conditional H640 packet is routed and scope-fenced.")
