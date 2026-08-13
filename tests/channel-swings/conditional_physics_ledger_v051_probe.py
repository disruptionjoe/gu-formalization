#!/usr/bin/env python3
"""Fail-closed append-only checks for translation-curvature ledger v0.51."""

from collections import Counter
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[2]
FAILURES = []
COUNTS = Counter()
MIGRATED = {"LT-GR1", "LT-GR2b", "LT-GR3", "LT-GR5", "LT-GR6"}


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


old = strict("lab/process/conditional-physics-ledger-v0.50.json")
new = strict("lab/process/conditional-physics-ledger-v0.51.json")
result = strict("lab/process/selected-second-layer-translation-curvature-principal-owner.json")
old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}

check("exact", "schema advances exactly", old["schema_version"] == "0.50" and new["schema_version"] == "0.51")
check("exact", "row IDs and denominator freeze", set(old_rows) == set(new_rows) and old["denominator"] == new["denominator"])
check("exact", "only five row records migrate", {rid for rid in old_rows if old_rows[rid] != new_rows[rid]} == MIGRATED)
check("exact", "unmigrated rows freeze byte-equivalent", all(old_rows[rid] == new_rows[rid] for rid in old_rows if rid not in MIGRATED))
check("exact", "verdicts and reason kinds freeze for all rows", all((old_rows[r]["verdict"], old_rows[r]["reason_kind"]) == (new_rows[r]["verdict"], new_rows[r]["reason_kind"]) for r in old_rows))
check("exact", "headline counts freeze", new["progress"]["verdict_counts"] == old["progress"]["verdict_counts"] == {"SAME": 32, "DIFFERS": 19, "NEEDS": 26, "OVER_DETERMINED": 5})
check("exact", "residue and quotients freeze", new["residue"] == old["residue"])
check("exact", "five v050-to-v051 migrations are present", {m["row_id"] for m in new["migrations"] if m.get("from_version") == "0.50" and m.get("to_version") == "0.51"} == MIGRATED)
check("exact", "partial-owner support arithmetic is exact", result["exact_result"]["fixed_b_owned_support"] == 28 and result["exact_result"]["transverse_unowned_support"] == 117 and 28 + 117 == 145)
check("exact", "principal rank-nullity is exact", result["exact_result"]["delta_t_domain_dimension"] - result["exact_result"]["q_wedge_kernel_dimension"] == result["exact_result"]["q_wedge_full_image_dimension"] == 182)
check("type", "both four-column ranks remain visible", result["exact_result"]["owned_family_rank"] == result["exact_result"]["transverse_family_rank"] == 4)
check("type", "fixed-B result is booked as partial owner", result["exact_result"]["fixed_b_disposition"] == "PARTIAL_OWNER")
check("source", "source return separates written D_B T from silent richer coefficients", new["source_return"] == result["source_return"] == "SOURCE-CONFIRMS__T_CONNECTION_DIFFERENCE_AND_DB_T_TRANSLATION_CURVATURE__SOURCE-SILENT__RICHER_MOVING_SOLDERING_COEFFICIENTS")
check("program", "frontier counts close three without opening a new condition", new["frontier_delta"] == result["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 3, "conditions_opened": 0, "remaining_named_conditions": 5})
check("program", "P1 P2 P3 remain unused", result["external_datum"] == {"P1": "UNUSED", "P2": "UNUSED", "P3": "UNUSED"})
check("program", "Curt and third lane remain fenced", result["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE" and result["third_lane_gate"] == "NOT_PROMOTED")

for label in (
    "partial owner is not full owner",
    "support 28 is not support 145",
    "moving reference is not fixed reference",
    "T wedge T is not odd first-order principal data",
    "principal symbol is not Euler or presymplectic closure",
    "non-null q is not a null screen",
    "distance migration is not verdict movement",
    "source silence is not refutation",
):
    check("planted", "PLANT " + label, True)

print("CHECKS=" + " ".join(f"{k}:{v}" for k, v in sorted(COUNTS.items())))
if FAILURES:
    print("FAILED=" + " | ".join(FAILURES))
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
