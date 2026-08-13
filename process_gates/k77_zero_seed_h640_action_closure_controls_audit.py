#!/usr/bin/env python3
"""Process gate for ledger v0.182 zero-seed H640 action module."""

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

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=reject)


def check(kind, label, value):
    COUNTS[kind] += 1
    ok = bool(value)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


ledger = strict("lab/process/conditional-physics-ledger-v0.182.json")
previous = strict("lab/process/conditional-physics-ledger-v0.181.json")
result = strict("lab/process/selected-k77-zero-seed-h640-action-closure-controls.json")
contract = strict("lab/process/functional-channel-operating-contract-v1.0.json")

check("ledger", "append-only successor identity is exact",
      ledger["schema_version"] == "0.182"
      and ledger["predecessor"].endswith("v0.181.json"))
check("ledger", "headline counts remain unchanged",
      ledger["progress"]["verdict_counts"] == previous["progress"]["verdict_counts"])
check("ledger", "residue and quotient count remain unchanged",
      ledger["residue"]["continuous_real"] == previous["residue"]["continuous_real"] == 84
      and ledger["residue"]["quotients_ranked"] == previous["residue"]["quotients_ranked"] == 5)
check("ledger", "frontier records four closed conditions and one BV successor",
      ledger["frontier_delta"] == {
          "headline_delta": "NONE", "conditions_closed": 4,
          "conditions_opened": 1, "remaining_named_conditions": 2,
      })
check("ledger", "exactly six current wave rows migrated",
      {item["row_id"] for item in ledger["wave_row_dispositions"]}
      == {"RA-D4", "RA-F1", "RA-F2", "RA-G2", "LT-SM3", "AC-F1"})
check("ledger", "six append-only v0.182 history records exist",
      sum(item.get("to_version") == "0.182" for item in ledger["migration_history"]) == 6)

check("result", "probe has zero failures, two firing plants, QQ and two-prime controls",
      result["checks"] == {
          "total": 45, "failures": 0, "planted": 2,
          "char0_zero_seed": True, "two_prime_all_controls": True,
      })
zero = result["zero_form_seed"]
check("char0", "source-owned zero seed generates exact QQ H640",
      zero["field"] == "QQ" and zero["seed_rank"] == 128
      and zero["generated_rank"] == 640
      and zero["one_form_projection_rank"] == 512
      and zero["zero_form_projection_rank"] == 128
      and zero["generator_invariant"] and zero["fitted_parameters"] == 0)

natural = result["natural_controls"]
check("control", "W mirror and pair close to the zero-seed H640",
      natural["W192_plus_zero_generated_rank"]
      == natural["mirror192_plus_zero_generated_rank"]
      == natural["W_plus_mirror_plus_zero_generated_rank"] == 640
      and natural["all_three_equal_zero_seed_h640"])
check("control", "old 640 and 832 give distinct H1280s meeting in H640 and spanning full",
      natural["old_one_form640_plus_zero_generated_rank"]
      == natural["one_form832_plus_zero_generated_rank"] == 1280
      and natural["old640_and_832_h1280_relation"] == {
          "equal": False, "intersection_rank": 640,
          "intersection_is_h640": True, "joined_rank": 1920,
      })
random_controls = result["random_controls"]
check("planted", "random rank-192 controls produce large non-H640 hulls reproducibly",
      random_controls["generated_ranks"] == [1920, 1916, 1908]
      and random_controls["intersection_with_h640_each"] == 640
      and not random_controls["equal_h640"]
      and random_controls["cross_prime_equal"])
check("clifford", "the complete eight-word action algebra is certified",
      result["clifford_action"] == {
          "three_generators_square_to_identity": True,
          "three_generators_pairwise_anticommute": True,
          "eight_words_noncollapsed": True,
      })
check("scope", "source selection, physical cohomology and public accounting remain fenced",
      "SOURCE_SILENT_ON_H640_PHYSICAL_SELECTION" in result["source_return"]
      and not result["accounting"]["P1_P2_P3_used"]
      and not result["accounting"]["verdict_change"]
      and not result["accounting"]["booked_residue_change"]
      and not result["accounting"]["quotient_change"]
      and not result["accounting"]["canon_verdict_change"]
      and not result["accounting"]["public_posture_change"])

standing = contract["standing_ledger"]
check("routing", "operating contract points at v0.182",
      standing["ref"].endswith("v0.182.json")
      and standing["human_ref"].endswith("v0.182.md"))
check("routing", "successor is full BV/KT on H640 with full-carrier control",
      contract["current_priority_decision"]["main_sequence"][0]
      == "DERIVE_COMPLETE_LOWER_ORDER_BARRED_DUAL_ANTIFIELD_BV_KOSZUL_TATE_ON_H640_WITH_FULL1920_CONTROL")

for relative, needles in {
    "NEXT-STEPS.md": ["ledger v0.182", "mandatory control"],
    "RESEARCH-STATUS.md": ["ledger v0.182", "distinct rank-1280"],
    "lab/process/agent-context-pack.md": ["Current v0.182", "source-selected physical"],
    "lab/process/hostile-reviews/2026-08-11-selected-k77-zero-seed-h640-action-closure-controls-review.md": ["SURVIVES_SCOPED", "Symplectic", "equal rank 1280"],
    "lab/sources/selected-k77-zero-seed-h640-action-closure-controls-source-return-2026-08-11.md": ["SOURCE-SILENT", "repository construction"],
}.items():
    text = (ROOT / relative).read_text(encoding="utf-8")
    check("surface", f"{relative} carries the required scope",
          all(needle in text for needle in needles))

print("SUMMARY " + " + ".join(f"{count} {kind}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    raise SystemExit("FAILURES: " + "; ".join(FAILURES))
print("PASS: v0.182 zero-seed H640 action module is routed and scope-fenced.")
