#!/usr/bin/env python3
"""Durability audit for ledger v0.142 local VEV selector exhaustion."""

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
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate key {key!r}: {path}")
            result[key] = value
        return result

    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)


def check(kind: str, label: str, condition: object) -> None:
    COUNTS[kind] += 1
    ok = bool(condition)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {label}")
    if not ok:
        FAILURES.append(label)


old = strict("lab/process/conditional-physics-ledger-v0.141.json")
new = strict("lab/process/conditional-physics-ledger-v0.142.json")
result = strict("lab/process/selected-k77-zero-fermion-vev-selector-exhaustion.json")
contract = strict("lab/process/functional-channel-operating-contract-v1.0.json")
report = (ROOT / "explorations/conditional-build/selected-k77-zero-fermion-vev-selector-exhaustion-2026-08-10.md").read_text()
review = (ROOT / "lab/process/hostile-reviews/2026-08-10-selected-k77-zero-fermion-vev-selector-exhaustion-review.md").read_text()
routing = "\n".join((ROOT / name).read_text() for name in (
    "LANES.yaml", "NEXT-STEPS.md", "RESEARCH-STATUS.md", "lab/process/README.md",
    "lab/process/agent-context-pack.md", "lab/process/exploration-absorption-priorities-2026-08-10.md",
))
tests_readme = (ROOT / "tests/README.md").read_text()
gates_readme = (ROOT / "process_gates/README.md").read_text()

moved_order = ("LT-GR1", "LT-GR2b", "LT-GR2c", "LT-GR2d", "LT-GR3", "LT-GR6")
moved = set(moved_order)
old_rows = {row["id"]: row for row in old["rows"]}
new_rows = {row["id"]: row for row in new["rows"]}
migrations = [item for item in new["migrations"] if item["to_version"] == "0.142"]

check("ledger", "v0.142 is append-only from v0.141",
      new["predecessor"].endswith("v0.141.json")
      and [row["id"] for row in new["rows"]] == [row["id"] for row in old["rows"]])
check("ledger", "headline counts remain unchanged",
      new["progress"]["verdict_counts"] == old["progress"]["verdict_counts"]
      and new["progress"]["mapped"] == old["progress"]["mapped"] == 82)
check("ledger", "frontier closes three conditions and opens one",
      new["frontier_delta"] == {"headline_delta": "NONE", "conditions_closed": 3,
                                "conditions_opened": 1, "remaining_named_conditions": 3})
check("ledger", "six exact migration edges were added",
      [(item["row_id"], item["from_version"], item["to_version"]) for item in migrations]
      == [(row, "0.141", "0.142") for row in moved_order])
check("ledger", "moved rows cite selector exhaustion",
      all(new_rows[row]["evidence"] == "selected-k77-zero-fermion-vev-selector-exhaustion-2026-08-10.md"
          for row in moved))
check("ledger", "all nonmoved rows are parsed-object identical",
      all(new_rows[row_id] == old_rows[row_id] for row_id in old_rows if row_id not in moved))
check("ledger", "moved rows preserve verdict and reason kind",
      all(new_rows[row]["verdict"] == old_rows[row]["verdict"]
          and new_rows[row]["reason_kind"] == old_rows[row]["reason_kind"] for row in moved))
check("ledger", "rank one is global normalization plus common domain",
      new["next_work_queue"][0]["rank"] == 1
      and "global normalized" in new["next_work_queue"][0]["why"]
      and "BV-BFV" in new["next_work_queue"][0]["why"])

exact = result["exact_result"]
check("exact", "source equation rank is two with determinant -97344",
      exact["source_equation_rank"] == 2 and exact["fu_minor_determinant"] == -97344)
check("exact", "one local amplitude and its tangent are explicit",
      exact["family"]["local_amplitude_dimension"] == 1
      and exact["family"]["tangent"][-1] == "1")
check("exact", "the rational representative is retained without uniqueness",
      exact["v0108_representative"]["t"] == "-1/104"
      and "NOT_UNIQUE" in exact["v0108_representative"]["status"])
check("exact", "the ten-component local trace cancels with no new coefficient",
      exact["trace"]["total_density"] == "0"
      and exact["trace"]["zero_components"] == 10
      and exact["trace"]["new_action_coefficients"] == 0)
check("exact", "zero-fermion current adds no amplitude equation",
      exact["selector_composition"]["zero_fermion_current_rank"] == 0)
check("layer0", "pointwise Hessian is not typed as the amplitude tangent",
      exact["selector_composition"]["pointwise_parent_hessian_radical"] == 0
      and not exact["selector_composition"]["pointwise_hessian_types_amplitude_tangent"])
check("symplectic", "classical branch symplectomorphism is retained",
      exact["selector_composition"]["classical_branch_symplectomorphism"])
check("bv", "classical BFV does not select branch or amplitude",
      not exact["selector_composition"]["classical_bfv_selects_branch_or_amplitude"])
check("control", "a genuine independent equation raises rank to three",
      exact["selector_composition"]["planted_third_equation_rank"] == 3)

excluded = set(result["scope"]["does_not_decide"])
check("scope", "global quantum external and observed-magnitude routes remain open",
      {"GLOBAL_NORMALIZED_FUNCTIONAL", "QUANTUM_CONTOUR_MEASURE_OR_DETERMINANT",
       "EXPLICIT_EXTERNAL_NORMALIZER", "OBSERVED_DARK_ENERGY_MAGNITUDE_OR_SCREENING"} <= excluded)
check("source", "source confirmation and silence are explicit",
      "SOURCE_CONFIRMS" in result["source_return"] and "SOURCE_SILENT" in result["source_return"])
check("hostile", "three charges and dissent are explicit",
      all(token in review for token in ("### 1.", "### 2.", "### 3.", "## Dissent")))
check("hostile", "review refuses global no-selector and magnitude inflation",
      "GLOBAL_NO_SELECTOR" in review and "DARK_ENERGY_MAGNITUDE_DERIVED" in review)
check("symplectic", "report includes the mandatory symplectic lens",
      "Symplectic geometry — ACTUAL MATH" in report)
check("analytic", "report keeps quantum measure and common domain open",
      "quantum measure" in report and "coupled bulk--" in report and "boundary BV--BFV" in report)
check("cosmology", "report separates two-to-one tracking from screening",
      "problems become one" in report and "radiative screening" in report)

check("routing", "contract and front doors point to v0.142",
      contract["standing_ledger"]["ref"].endswith("v0.142.json")
      and "ledger v0.142" in routing)
check("routing", "the stale local VEV build is explicitly superseded",
      "Superseded priority" in routing and "Do not rebuild local VEV stress" in routing)
check("routing", "the contract carries the selector-exhaustion directive",
      "vev_selector_exhaustion_directive" in contract["standing_ledger"])
check("inventory", "channel-swing inventory is exact",
      len(list((ROOT / "tests/channel-swings").glob("*.py"))) == 518
      and len(list((ROOT / "tests/channel-swings").glob("*.sage"))) == 92
      and "(518 Python + 92 Sage)" in tests_readme)
check("inventory", "the new process gate is listed",
      "zero_fermion_vev_selector_exhaustion_audit.py" in gates_readme)
check("accounting", "no headline accounting moves",
      all(result["changes"][key] == "none" for key in (
          "verdict_change", "residue_change", "booked_quotient_change",
          "canon_verdict_change", "public_posture_change",
      )))
check("accounting", "residue forks and quotients are unchanged", new["residue"] == old["residue"])
check("accounting", "P1/P2/P3 remain unused", result["controls"]["P1_P2_P3"] == "UNCHANGED_AND_UNUSED")

print("COUNTS " + " ".join(f"{kind}={count}" for kind, count in sorted(COUNTS.items())))
if FAILURES:
    for failure in FAILURES:
        print(f"FAIL: {failure}")
    raise SystemExit(1)
print(f"PASS {sum(COUNTS.values())}/{sum(COUNTS.values())}")
