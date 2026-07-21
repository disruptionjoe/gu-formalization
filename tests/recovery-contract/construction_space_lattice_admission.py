#!/usr/bin/env python
"""P-LATTICE-SWEEP compiler-admission gate.

This gate confirms that the parked probe's wake condition has fired while the
current human-readable map still lacks the structured grammar needed for safe,
target-free candidate generation.

Run: python tests/recovery-contract/construction_space_lattice_admission.py
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MAP = ROOT / "lab" / "process" / "construction-space-map.json"
PORTFOLIO = ROOT / "lab" / "process" / "research-portfolio.json"
NOTE = ROOT / "explorations" / "p-lattice-sweep-admission-2026-07-21.md"

FAIL: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL") + " :: " + name + ((" -- " + detail) if detail else ""))
    if not ok:
        FAIL.append(name)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    map_data = load(MAP)
    portfolio = load(PORTFOLIO)
    note = NOTE.read_text(encoding="utf-8")
    cells = map_data["cells"]
    rounds = map_data["council_rounds"]
    work = {item["id"]: item for item in portfolio["work_items"]}

    round_11 = next(entry for entry in rounds if entry["round"] == 11)
    round_12 = next(entry for entry in rounds if entry["round"] == 12)
    lattice = map_data["lattice_sweep_admission"]

    check("P-K2 resolved in round 11", "K2: PARTIAL" in round_11["results_digest"])
    check("P-77-REAL-INDEX resolved in round 11", "Real-index:" in round_11["results_digest"])
    check("PP1 frozen in round 12", "PP1 frozen" in round_12["prediction_shelf"])
    check("construction-space item remains active", work["CONSTRUCTION-SPACE-EXPLORATION"]["state"] == "ACTIVE")
    check("Lane 2 packet item remains ready", work["PRED-CANDIDATE-PACKETS"]["state"] == "READY")
    check("B5 remains source-blocked", work["B5-MIDDLE-DIFFERENTIAL"]["state"] == "BLOCKED_SOURCE_GAP")
    check("B5 remains hourly-ineligible", work["B5-MIDDLE-DIFFERENTIAL"]["hourly_eligible"] is False)

    check("map still has 11 declared cells", len(cells) == 11, str(len(cells)))
    check("all cells retain human axis notes", all("axis_notes" in cell for cell in cells))
    structured = lattice["structured_axis_signatures"]
    check("admission recorded zero structured signatures", structured == 0, str(structured))
    check("admission recorded the missing axis-domain blocker", "axis domains" in lattice["blocker"].lower())
    check("admission recorded the missing compatibility blocker", "compatibility" in lattice["blocker"].lower())
    check("admission stops on parameterization", lattice["status"] == "BLOCKED_PARAMETERIZATION")
    check("admission records zero generated cells", lattice["generated_cells"] == 0)
    check("next step is the schema freeze", lattice["next_probe"] == "P-LATTICE-SCHEMA-FREEZE")
    check("note preserves native/conventional fork", "program_native | conventional | imported" in note)
    check("note preserves B5 parking", "B5-MIDDLE-SOURCE-GAP" in note)

    if FAIL:
        raise SystemExit("FAILED: " + ", ".join(FAIL))
    print("RESULT: ALL PASS")


if __name__ == "__main__":
    main()
