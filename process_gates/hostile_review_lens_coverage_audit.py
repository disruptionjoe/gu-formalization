#!/usr/bin/env python3
"""Hostile-review lens coverage census, and the over-determined independence rule.

Two halves, deliberately asymmetric in how loudly they fail.

CENSUS (reports, never fails).  Every hostile review declares `mandatory_lenses`
in its front matter.  Nothing has ever read those declarations in aggregate, so a
hole in the corpus is invisible: as of 2026-08-08 the 41 filed perspective passes
contained ZERO coverage of complex analysis, path integrals, saddle points,
steepest descent or Picard-Lefschetz, while every open analytic gate in the
program sits in exactly that territory.  That hole persisted because lens
selection is per-review and per-review choices are never summed.  This half
prints the tally so the next hole is visible without anyone counting by hand.
It does not fail: a lens distribution is evidence, not a violation.

INDEPENDENCE (fails, on a short and fixable list).  AGENTS.md requires that "the
finder of an over-determined row escalates it; an INDEPENDENT OWNER adjudicates
it as genuine falsification, fork artifact, scope error or stale premise."  The
conditional-physics ledger's OVER_DETERMINED rows carry `reason_kind` -- the
adjudication verdict -- but if a row's `evidence` points only at the cluster that
found it, no independent owner has adjudicated and the verdict is the finder's
own.  That is the program's only falsification-shaped output, so this half fails
loudly and names the rows.

WHY THE ASYMMETRY.  This suite already carries ~49 failures dominated by
version-pinned gates that self-break as work advances, so it cannot be read by
absolute count.  A gate that fails on a census would vanish into that noise.  A
gate that fails on a short named list stays legible.
"""

from __future__ import annotations

import copy
import glob
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REVIEWS = ROOT / "lab" / "process" / "hostile-reviews"
LIVE_DISPOSITIONS = ROOT / "lab" / "process" / "phenomenology-disposition-register-v0.1.json"

# Lens families this repository's own open gates live in.  Absence is reported,
# never failed -- the point is visibility, not a quota.
WATCHED = {
    "analytic": ("analytic", "complex", "path_integral", "saddle", "steepest",
                 "picard", "spectral", "pde_domain", "operator", "krein"),
    "layer0_semantics": ("layer0", "semantic", "homonym", "source_criticism"),
    "prior_art": ("prior_art", "already_done", "provenance"),
    "symplectic": ("symplectic",),
    "representation": ("representation", "rep_theory", "branching"),
    "topology": ("topolog", "bordism", "index", "characteristic"),
}


def declared_lenses() -> Counter:
    tally: Counter = Counter()
    for path in sorted(REVIEWS.glob("*.md")):
        head = path.read_text(errors="ignore")[:4000]
        match = re.search(r"^mandatory_lenses:\s*\[(.*?)\]", head, re.M | re.S)
        if not match:
            continue
        for raw in match.group(1).split(","):
            lens = raw.strip().strip("\"'")
            if lens:
                tally[lens] += 1
    return tally


def latest_ledger() -> Path:
    paths = glob.glob(str(ROOT / "lab" / "process" / "conditional-physics-ledger-v0.*.json"))
    return Path(max(paths, key=lambda p: int(re.search(r"v0\.(\d+)", p).group(1))))


def finder_only(ref: str) -> bool:
    return bool(re.match(r"^(?:explorations/conditional-build/)?cb-[a-e]-", ref) or "/cb-" in ref)


def disposition_is_independent(row_id: str, live: dict, registry: dict) -> bool:
    """Verify a live, bounded, non-finder adjudication without rewriting the ledger."""
    live_rows = [item for item in live.get("terminal_row_dispositions", [])
                 if item.get("row_id") == row_id]
    registry_rows = [item for item in registry.get("terminal_rows", [])
                     if item.get("row_id") == row_id]
    if len(live_rows) != 1 or len(registry_rows) != 1:
        return False
    live_row, registry_row = live_rows[0], registry_rows[0]
    if live_row.get("terminal_outcome") != "PRECISE_IMPOSSIBILITY":
        return False
    if registry_row.get("terminal_outcome") != "PRECISE_IMPOSSIBILITY":
        return False
    impossibility_id = live_row.get("impossibility_id")
    if not impossibility_id or registry_row.get("impossibility_id") != impossibility_id:
        return False
    impossibilities = [item for item in registry.get("precise_impossibilities", [])
                       if item.get("id") == impossibility_id]
    if len(impossibilities) != 1:
        return False
    impossibility = impossibilities[0]
    if impossibility.get("rows") != [row_id]:
        return False
    if impossibility.get("target_claim") != "NONE-NOT-A-KILL":
        return False
    for field in ("class", "assumptions", "witness", "escape", "resurrection_trigger"):
        if not impossibility.get(field):
            return False
    source_refs = registry.get("source_evidence", {}).get(row_id, [])
    if not source_refs or not any(not finder_only(str(ref)) for ref in source_refs):
        return False
    effects = registry.get("protected_effects", {})
    if not effects or any(value is not False for value in effects.values()):
        return False
    result_ref = str(registry.get("result_ref", ""))
    return bool(result_ref and not finder_only(result_ref) and (ROOT / result_ref).is_file())


def live_independent_rows() -> set[str]:
    live = json.loads(LIVE_DISPOSITIONS.read_text())
    rows: set[str] = set()
    for item in live.get("terminal_row_dispositions", []):
        row_id = item.get("row_id")
        evidence_ref = str(item.get("evidence_ref", ""))
        evidence_path = ROOT / evidence_ref
        if not row_id or finder_only(evidence_ref) or not evidence_path.is_file():
            continue
        try:
            registry = json.loads(evidence_path.read_text())
        except (json.JSONDecodeError, OSError):
            continue
        if disposition_is_independent(row_id, live, registry):
            rows.add(row_id)
    return rows


def unadjudicated_over_determined() -> list[tuple[str, str]]:
    """Rows with neither direct nor live-register independent adjudication."""
    ledger = json.loads(latest_ledger().read_text())
    registered = live_independent_rows()
    offenders = []
    for row in ledger.get("rows", []):
        if row.get("verdict") != "OVER_DETERMINED":
            continue
        if row.get("row_status") == "SUPERSEDED":
            continue
        evidence = str(row.get("evidence", ""))
        # A finder-only citation looks like "cb-a...md:D2" -- the conditional-build
        # cluster that produced the row.  An independent adjudication would cite an
        # artifact outside the finding cluster.
        if finder_only(evidence) and row["id"] not in registered:
            offenders.append((row["id"], evidence))
    return offenders


class HostileReviewLensCoverage(unittest.TestCase):
    def test_census_is_reportable(self) -> None:
        tally = declared_lenses()
        print(f"\n  hostile reviews declaring lenses: {sum(tally.values())} declarations")
        print(f"  distinct lenses in use          : {len(tally)}")
        print("\n  watched families:")
        joined = " ".join(tally).lower()
        for family, keys in WATCHED.items():
            hits = sum(count for lens, count in tally.items()
                       if any(k in lens.lower() for k in keys))
            flag = "" if hits else "   <- NO COVERAGE"
            print(f"    {family:20} {hits:4}{flag}")
        print("\n  top declared lenses:")
        for lens, count in tally.most_common(10):
            print(f"    {count:4}  {lens}")
        self.assertTrue(True, "census reports; it does not fail")

    def test_over_determined_rows_are_independently_adjudicated(self) -> None:
        offenders = unadjudicated_over_determined()
        self.assertEqual(
            [], offenders,
            "AGENTS.md requires an INDEPENDENT OWNER to adjudicate an "
            "over-determined row. These rows cite only the cluster that found "
            "them, so the reason_kind is the finder's own verdict:\n  "
            + "\n  ".join(f"{rid}  evidence={ev}" for rid, ev in offenders)
            + "\nFile an independent adjudication, or cite one that exists.",
        )

    def test_live_disposition_route_fails_closed(self) -> None:
        live = json.loads(LIVE_DISPOSITIONS.read_text())
        evidence_ref = next(item["evidence_ref"] for item in live["terminal_row_dispositions"]
                            if item.get("row_id") == "LT-GR4")
        registry = json.loads((ROOT / evidence_ref).read_text())
        self.assertTrue(disposition_is_independent("LT-GR4", live, registry))

        mutations = []
        changed = copy.deepcopy(live)
        changed["terminal_row_dispositions"] = [
            item for item in changed["terminal_row_dispositions"]
            if item.get("row_id") != "LT-GR4"
        ]
        mutations.append((changed, registry))
        changed = copy.deepcopy(registry)
        changed["source_evidence"]["LT-GR4"] = ["explorations/conditional-build/cb-b-lagrangian-terms-2026-08-05.md"]
        mutations.append((live, changed))
        changed = copy.deepcopy(registry)
        changed["precise_impossibilities"][0]["target_claim"] = "SC-GR-UNKNOWN"
        mutations.append((live, changed))
        changed = copy.deepcopy(registry)
        changed["protected_effects"]["ledger_verdict_change"] = True
        mutations.append((live, changed))
        outcomes = [disposition_is_independent("LT-GR4", *case) for case in mutations]
        self.assertEqual([False] * len(mutations), outcomes)


if __name__ == "__main__":
    unittest.main(verbosity=2)
