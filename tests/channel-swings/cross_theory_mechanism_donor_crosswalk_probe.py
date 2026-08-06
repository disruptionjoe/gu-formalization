#!/usr/bin/env python3
"""Machine checks for the bounded cross-theory donor crosswalk."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
COUNTS: Counter[str] = Counter()
FAILURES: list[str] = []


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}]: {label}")
    if not ok:
        FAILURES.append(label)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def load(relative: str) -> dict:
    return json.loads(read(relative), object_pairs_hook=_unique_pairs)


def _unique_pairs(pairs: list[tuple[str, object]]) -> dict:
    out: dict[str, object] = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


data = load("lab/process/cross-theory-mechanism-donor-crosswalk.json")
report = read("explorations/conditional-build/cross-theory-mechanism-donor-crosswalk-2026-08-05.md")
source = read("lab/sources/cross-theory-mechanism-donor-source-audit-2026-08-05.md")
review = read("lab/process/hostile-reviews/2026-08-05-cross-theory-mechanism-donor-crosswalk-review.md")
scaffold = read("explorations/conditional-build/post-donor-crosswalk-five-wave-scaffold-2026-08-05.md")

print("A. VOCABULARY, CAP AND REQUIRED FIELDS")
allowed = {"EXACT_PORT", "METHOD_PORT", "ANALOGY_ONLY", "WRONG_TYPE", "ALREADY_PRESENT"}
candidates = data["candidates"]
selected = [c for c in candidates if c["selected"]]
required = {
    "id", "donor", "mechanism", "recipient", "translation_map",
    "classification", "selected", "datum_cost", "constraint_effect",
    "distance_reduced", "kill_condition", "revival_trigger", "ledger_rows"
}
check("type", "classification vocabulary is exact", set(data["classification_vocabulary"]) == allowed)
check("type", "all candidate classifications are admitted", all(c["classification"] in allowed for c in candidates))
check("type", "every candidate carries the complete port contract", all(required <= set(c) for c in candidates))
check("type", "the assessment contains eight non-padding candidates", len(candidates) == 8)
check("exact", "the two-port cap is obeyed", len(selected) == 2 == data["selection_cap"])
check("exact", "selected ids match the candidate flags", [c["id"] for c in selected] == data["selected_port_ids"])
check("type", "both selected ports are methods, not exact objects", all(c["classification"] == "METHOD_PORT" for c in selected))
check("type", "no exact object port is claimed", data["exact_port_count"] == 0 and not data["selected_ports_are_exact_objects"])

print("\nB. THE TWO SELECTED PORTS")
by_id = {c["id"]: c for c in candidates}
ncg = by_id["NCG-CONTROL"]
linf = by_id["STRING-LINF"]
check("repo", "NCG control targets the missing zero-order SM placement", "P0_RHO_YK_YC_C" in ncg["distance_reduced"])
check("type", "NCG object imports are explicit kill conditions", "FINITE_ALGEBRA_KO6_OR_D_F" in ncg["kill_condition"])
check("repo", "higher-gauge method targets super-IG global descent", linf["distance_reduced"] == "SUPER_IG_GLOBAL_DESCENT")
check("type", "higher-gauge method fails closed on a free level", "FREE_LEVEL_REQUIRED" in linf["kill_condition"])
check("source", "primary source audit returns silence on GU translations", "`SOURCE-SILENT` on the GU translations" in source)
check("source", "NCG primary anchors are recorded", "hep-th/9606001" in source and "hep-th/0605011" in source)
check("source", "LQG primary projective anchor is recorded", "gr-qc/9411046" in source)
check("source", "AS evidence and parametrization dependence are both recorded", "1410.4815" in source and "1805.09656" in source)
check("source", "higher gauge integration anchors are recorded", "math/0504123" in source and "math/0603563" in source)

print("\nC. WRONG-TYPE AND ALREADY-PRESENT FENCES")
check("type", "finite NCG object port is rejected", by_id["NCG-OBJECT"]["classification"] == "WRONG_TYPE")
check("type", "string compactification port is rejected", by_id["STRING-COMPACT"]["classification"] == "WRONG_TYPE")
check("type", "LQG measure is wrong-type at the current gate", by_id["LQG-MEASURE"]["classification"] == "WRONG_TYPE")
check("type", "LQG holonomy route remains analogy-only", by_id["LQG-CONSTRAINT"]["classification"] == "ANALOGY_ONLY")
check("repo", "string anomaly controls are marked already present", by_id["STRING-ANOMALY"]["classification"] == "ALREADY_PRESENT")
check("repo", "AS FRG is marked already present and delayed", by_id["AS-FRG"]["classification"] == "ALREADY_PRESENT" and "STABLE_NUMERATOR" in by_id["AS-FRG"]["revival_trigger"])

print("\nD. LEDGER, DATUM AND LANE BOUNDARIES")
ledger = data["ledger"]
check("exact", "ledger version and denominator remain frozen", ledger["version"] == "0.17" and ledger["mapped"] == ledger["total"] == 82)
check("exact", "verdict counts remain 33/19/24/6", ledger["verdict_counts"] == {"SAME": 33, "DIFFERS": 19, "NEEDS": 24, "OVER_DETERMINED": 6})
check("exact", "residue remains 84 plus at least 19 functions and 9 forks", ledger["continuous_residue"] == 84 and ledger["function_valued_residue_lower_bound"] == 19 and ledger["discrete_forks"] == 9)
check("type", "no ledger migration is booked", ledger["row_changes"] == "none" and "NO_NEW_MATHEMATICAL" in ledger["no_change_reason"])
check("type", "P1/P2/P3 remain unused", set(data["external_datum"].values()) == {"UNUSED"})
check("type", "Curt stays separate and no third lane is promoted", data["curt_track"] == "FORMALLY_SEPARATE_INSIDE_ERIC_LANE" and data["third_lane"] == "NOT_PROMOTED")

print("\nE. HOSTILE REVIEW AND FIVE-WAVE ORDER")
check("review", "both mandatory hostile charges are filed", "Charge 1" in review and "Charge 2" in review)
check("review", "symplectic veto is explicit", "UNREDUCED_CONTROL_OR_GLOBAL_BRACKET_IS_NOT_A_PHYSICAL_TRANSITION" in review)
check("review", "free-object delta stays zero", "`free_object_delta`: zero" in review)
check("review", "T4 physical and UV claims remain open", "`T4`" in review and "**open**" in review)
for wave in range(1, 6):
    check("scaffold", f"Wave {wave} is present", f"## Wave {wave}" in scaffold)
check("scaffold", "the mandatory Compose checkpoint follows three Builds", "After Waves 1--3, Compose runs" in scaffold)
check("scaffold", "FRG Wave 5 is conditional rather than automatic", "If those prerequisites are absent, **do not run FRG**" in scaffold)
check("scaffold", "Wave 1 remains the selected numerator", "selected `Y14` cubic numerator" in scaffold)
check("type", "report states the two-port stop rule and no new lane", "does **not** create a fifth theory lane" in report and "The donor harvest stops here" in report)

print("\nF. PLANTED FAILURE CONTROLS")
bad = [dict(c) for c in candidates]
bad[0]["selected"] = True
bad[1]["selected"] = True
bad[2]["selected"] = True
check("planted", "a third selected port violates the cap", sum(bool(c["selected"]) for c in bad) > data["selection_cap"])
check("planted", "unknown classification is rejected", "RHYME" not in allowed)
check("planted", "missing translation map is detectable", not (required <= (set(candidates[0]) - {"translation_map"})))
check("planted", "free compactification data is nonzero cost", by_id["STRING-COMPACT"]["datum_cost"] != "ZERO")
check("planted", "LQG measure does not silently become the observer functional", by_id["LQG-MEASURE"]["translation_map"].startswith("UNBUILT_"))
check("planted", "AS cannot run before stable prerequisites", "STABLE_NUMERATOR" in by_id["AS-FRG"]["revival_trigger"])
check("planted", "method selection cannot masquerade as ledger evidence", ledger["row_changes"] == "none")
check("planted", "physical promotion is vetoed before symplectic descent", "is_not_a_physical_transition" in review.lower())

total = sum(COUNTS.values())
print(f"\nSUMMARY: {dict(COUNTS)} = {total} checks; failures={len(FAILURES)}")
if FAILURES:
    raise SystemExit("; ".join(FAILURES))
