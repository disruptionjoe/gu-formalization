#!/usr/bin/env python3
"""Deterministic integrity and cross-vote tally for the 27-lens GU council.

This probe certifies the council packet's internal accounting only. It does not
turn modeled specialist judgments into scientific evidence and does not test
the candidate physics hypotheses.
"""

from __future__ import annotations

import json
import hashlib
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PANEL_PATH = ROOT / "lab/process/selected-k77-superposition-hypothesis-27-lens-council.json"
LEDGER_256_PATH = ROOT / "lab/process/conditional-physics-ledger-v0.256.json"
DELTA_PATH = ROOT / "lab/process/conditional-evidence-deltas/gu-tw-coherence-27-lens-2026-08-14.json"
DELTA_INDEX_PATH = ROOT / "lab/process/conditional-evidence-deltas/index.json"
REPORT_PATH = ROOT / "explorations/conditional-build/selected-k77-superposition-hypothesis-27-lens-council-2026-08-14.md"


checks: list[tuple[str, bool]] = []


def check(label: str, condition: bool) -> None:
    checks.append((label, bool(condition)))
    print(("PASS" if condition else "FAIL") + f" [{label}]")


with PANEL_PATH.open(encoding="utf-8") as stream:
    panel = json.load(stream)
with LEDGER_256_PATH.open(encoding="utf-8") as stream:
    ledger_256 = json.load(stream)
with DELTA_PATH.open(encoding="utf-8") as stream:
    delta = json.load(stream)
with DELTA_INDEX_PATH.open(encoding="utf-8") as stream:
    delta_index = json.load(stream)
report = REPORT_PATH.read_text(encoding="utf-8")

candidates = panel["candidates"]
lenses = panel["lenses"]
candidate_ids = set(candidates)

check("schema is version one", panel["schema_version"] == "1.0")
check("council is planning evidence only", panel["status"] == "PLANNING_EVIDENCE_ONLY__NOT_SCIENTIFIC_EVIDENCE")
check("there are exactly twenty-seven lenses", len(lenses) == 27)
check("there are seven candidate hypotheses including the null", len(candidates) == 7 and "H0" in candidates)
check("lens identifiers are unique", len({lens["id"] for lens in lenses}) == len(lenses))
check("lens names are unique", len({lens["lens"] for lens in lenses}) == len(lenses))
check("every confidence lies in the declared percentage range", all(0 <= lens["confidence_percent"] <= 100 for lens in lenses))
check("every lens separates exact math from analogy or transfer", all(lens["exact_math"].strip() and lens["analogy_or_transfer"].strip() for lens in lenses))
check("every lens supplies a falsification or kill gate", all(lens["kill_gate"].strip() for lens in lenses))
check("every lens ranks exactly three distinct candidates", all(len(lens["ranking"]) == 3 and len(set(lens["ranking"])) == 3 for lens in lenses))
check("every ranked candidate is declared", all(set(lens["ranking"]) <= candidate_ids for lens in lenses))
check("MMO and MOO ambiguity is covered by separate lenses", any("MMO" in lens["lens"] for lens in lenses) and any("multi-objective" in lens["lens"] for lens in lenses))
check("Peter Woit name correction is explicit", any("Peter Voigt" in note and "Peter Woit" in note for note in panel["interpretation_notes"]))
check("Schuller programme-name correction is explicit", any("constructive gravity" in note and "direct action energy" in note for note in panel["interpretation_notes"]))

primary = Counter(lens["ranking"][0] for lens in lenses)
approval = Counter(candidate for lens in lenses for candidate in lens["ranking"])
borda = Counter()
for lens in lenses:
    for points, candidate in zip((3, 2, 1), lens["ranking"]):
        borda[candidate] += points

check("primary-vote accounting matches the preregistered tally", dict(primary) == panel["expected_primary_votes"])
check("all twenty-seven lenses place H1 in their top three", approval["H1"] == 27)
check("H1 wins the Borda cross-vote", borda["H1"] == max(borda.values()) and list(borda.values()).count(borda["H1"]) == 1)
check("H1 also wins the primary vote", primary["H1"] == max(primary.values()) and list(primary.values()).count(primary["H1"]) == 1)
check("the strongest single-candidate disposition follows the vote", panel["panel_disposition"]["strongest_single_candidate"] == "H1")
check("the composite preserves action selection before physical cohomology", panel["panel_disposition"]["strongest_composite"].startswith("H2 selects"))
check("the composite tests H3 only after H1", panel["panel_disposition"]["strongest_composite"].find("H1") < panel["panel_disposition"]["strongest_composite"].find("H3"))
check("the null remains mandatory", panel["panel_disposition"]["mandatory_null"] == "H0")
check("the claim ceiling forbids a new theorem or decoherence law", "NO_NEW_GU_THEOREM" in panel["panel_disposition"]["claim_ceiling"] and "NO_DECOHERENCE_LAW" in panel["panel_disposition"]["claim_ceiling"])
check("the exact spine preserves the two-way II/Yang--Mills negative", any("fails in both directions" in item for item in panel["exact_in_repo_spine"]))
check("the exact spine preserves the reduction-current result", any("[R,D_A R]" in item for item in panel["exact_in_repo_spine"]))
check("the exact spine preserves the positive-cohomology gap", any("positive physical cohomology remains unbuilt" in item for item in panel["exact_in_repo_spine"]))

rows_256 = {row["id"]: row for row in ledger_256["rows"]}
ledger_digest = hashlib.sha256(LEDGER_256_PATH.read_bytes()).hexdigest()
check("the pending delta targets immutable ledger v0.256 by exact digest", delta["base"]["ledger_ref"].endswith("conditional-physics-ledger-v0.256.json") and delta["base"]["ledger_sha256"] == ledger_digest)
check("the delta is pending and has no integration claim", delta["status"] == "pending" and delta["integration"] is None)
check("the delta affects LT-SM8 only", delta["affected_rows"] == ["LT-SM8"] and "LT-SM8" in rows_256)
check("the base ledger retains eighty-four row records and eighty-two canonical targets", len(rows_256) == 84 and ledger_256["denominator"]["canonical_target_count"] == 82)
check("the base LT-SM8 verdict remains NEEDS missing construction", rows_256["LT-SM8"]["verdict"] == "NEEDS" and rows_256["LT-SM8"]["reason_kind"] == "MISSING_CONSTRUCTION")
check("the proposed effect requests distance/evidence only", any("distance/evidence only" in change for change in delta["proposed_effect"]["requested_row_changes"]))
check("the proposed effect preserves the exact v0.256 mapping grade", any("preserving NEEDS" in change and "mapping grade" in change for change in delta["proposed_effect"]["requested_row_changes"]))
check("the delta keeps HYP-TW-COHERENCE-01 as a conflict key", "HYP-TW-COHERENCE-01" in delta["conflict_keys"])
check("all delta result references exist", all((ROOT / ref).exists() for ref in delta["result_refs"]))
check("the delta index exactly points at this pending delta", delta_index["deltas"] == [{"delta_id": delta["delta_id"], "path": DELTA_PATH.relative_to(ROOT).as_posix(), "status": "pending"}])
check("the delta claim ceiling rejects a new theorem and decoherence law", "No new GU theorem" in delta["claim_ceiling"] and "decoherence law" in delta["claim_ceiling"])
check("the delta summary preserves H0", "H0" in delta["proposed_effect"]["summary"] and "remains live" in delta["proposed_effect"]["summary"])
check("the report declares modeled lenses rather than human reviewers", "not twenty-seven human reviewers" in report)
check("the report retains the exact-versus-transfer distinction", "Everything after that floor is tagged as theorem transfer" in report)

print("PRIMARY=" + " ".join(f"{key}:{primary[key]}" for key in sorted(candidate_ids)))
print("APPROVAL=" + " ".join(f"{key}:{approval[key]}" for key in sorted(candidate_ids)))
print("BORDA=" + " ".join(f"{key}:{borda[key]}" for key in sorted(candidate_ids)))
print("COMPOSITE=H2_CAUSAL_ACTION_SELECTION__THEN_H1_COUPLED_PHYSICAL_COMPLEX__THEN_H3_PROJECTED_MEMORY_TEST")
print("NULL=H0_CLASSICAL_COMPLEX_GEOMETRY_PLUS_EXTERNAL_QUANTIZATION_RETAINED")

failed = [label for label, passed in checks if not passed]
if failed:
    print(f"FAIL {len(checks) - len(failed)}/{len(checks)}")
    raise SystemExit(1)

print(f"PASS {len(checks)}/{len(checks)}")
