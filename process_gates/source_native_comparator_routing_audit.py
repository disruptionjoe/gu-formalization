#!/usr/bin/env python3
"""Prevent conventional particle comparators from silently adjudicating GU."""

from __future__ import annotations

import json
import re
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
NON_ARTIFACT_DOC_TYPES = ("overview", "stewardship_record")
REGISTRY_PATH = ROOT / "lab/process/source-native-comparator-routing-registry.json"
METHOD = "lab/methods/source-native-comparator-routing.md"
MARKER = "GU-COMPARATOR-ROUTING"


def classification_pattern(classification: str) -> str:
    """Match a declaration allowing markdown emphasis around the token.

    ROOT CAUSE OF A FALSE BACKLOG (found 2026-08-15).  This test used an exact
    substring, so an author who wrote ``Classification: **`X`.**`` -- correct
    content, ordinary markdown bolding -- read as non-compliant.  EIGHT
    artifacts were fully method-compliant and were counted as an unclassified
    backlog for a full day, which is worse than a missing check: it invented
    work and made a real coverage number untrustworthy.

    The emphasis characters are optional; the token itself is still required
    verbatim inside backticks, so a WRONG classification still fails.
    """
    return r"Classification:\s*[*_]{0,2}`" + re.escape(classification) + r"`"


def discovered_artifacts() -> set[str]:
    result: set[str] = set()
    # Scope is DERIVED FROM CONVENTION, not enumerated.  The previous token
    # list named seven namespaces and rotted as soon as new ones were created:
    # on 2026-08-15 it missed coset-versus-gauge, cosmological-constant-sign,
    # four-d-mode-decomposition, ledger-advancement and metric-cone-boundedness
    # -- 17 of 34 files, half the tree, and 11 of those already carried the
    # routing notice, so the registry and its own audit had drifted apart.
    # Every joe-directed artifact is now in scope automatically.
    # Scope is narrowed by DECLARED DOCUMENT TYPE, not by filename.  An index
    # or a stewardship record does not contain or border a comparator: it
    # points at artifacts that do.  Requiring them to carry a routing
    # classification would permanently inflate the gap with documents that can
    # never legitimately be classified, which trains readers to ignore it.
    # This is the second horn the failure message already offers ("or narrow
    # the derived scope deliberately"), and it is keyed to front matter so a
    # renamed file cannot slip out of scope.
    joe_root = ROOT / "lab/active-research/joe-directed"
    for path in joe_root.rglob("*.md"):
        head = path.read_text(encoding="utf-8")[:400]
        if any(f"doc_type: {kind}" in head for kind in NON_ARTIFACT_DOC_TYPES):
            continue
        result.add(path.relative_to(ROOT).as_posix())
    for path in (ROOT / "explorations/conditional-build").glob("*.md"):
        if any(token in path.name.lower() for token in ("family-index", "higgs", "majorana")):
            result.add(path.relative_to(ROOT).as_posix())
    explicit = (
        "explorations/layer0-pass-on-the-two-higgs-objects-2026-07-29.md",
        "explorations/signature-chirality-conjugation-check-2026-08-13.md",
        "explorations/chirality-grading-and-77-rerun-2026-08-03.md",
        "explorations/b5-chirality-orientation-audit-2026-07-29.md",
        "explorations/no-net-chirality-without-a-boundary-2026-07-10.md",
        "explorations/dk-chirality-fork-2026-07-20.md",
        "explorations/vertical-vev-chirality-bridge-2026-07-29.md",
    )
    result.update(path for path in explicit if (ROOT / path).exists())
    return result


# Unclassified artifacts present when scope was widened from the seven-token
# list to convention (2026-08-15).  Never raise this to make a new gap go green.
# It may only RATCHET DOWN as artifacts are classified: 17 -> 16 once the four
# self-declaring artifacts were registered and index/stewardship documents left
# scope, then 17 -> 9 on 2026-08-15 when the backlog was worked (disposition:
# lab/active-research/joe-directed/base-duality/
# bd-reg-routing-backlog-disposition-2026-08-15.md).  That pass TRANSCRIBED
# eight in-vocabulary self-declarations (LA-1..LA-5, LA-8, LA-9, PHI-1, all
# `BRIDGE_OR_SEMANTIC_BOUNDARY`); it invented none.
#
# KNOWN INCONSISTENCY, recorded rather than papered over.  The method says an
# artifact "may then state" its classification -- optional -- while this gate
# counts every unregistered artifact as a gap.  So an artifact can be fully
# method-compliant and still appear here.  The 9 remaining split three ways and
# each way needs a DIFFERENT owner decision, not a guess:
#   (a) 4 carry no notice and declare no type at all (CG-1, CC-1, MD-1, MC-1).
#       Only these are actual method violations.  CC-1 and MC-1 do carry a
#       section headed "Classification, in target-native vocabulary", but it is
#       claim-status vocabulary (ROUTE KILLED / REFUTED), a homonym, not a
#       routing type.
#   (b) 4 declare a type OUTSIDE this registry's closed three-value vocabulary
#       -- `STRUCTURAL_LEDGER_ONLY` (LA-10) and `STRUCTURAL_PLUS_DEFINITIONAL`
#       (LA-11, OT-1, OT-2).  Each says in prose that it binds no comparator
#       AND is not evidence about the source-native mechanism, i.e. it asserts
#       that none of the three values applies.  Mapping them onto one anyway is
#       guessing; the owner either extends the vocabulary or narrows scope.
#   (c) 1 self-contradicts (PHI-2): its scope paragraph says it "is built
#       entirely inside a conventional particle-physics comparator" and that
#       "Every result below binds only that named model ... without an explicit
#       typed bridge", which describes `CONVENTIONAL_COMPARATOR`, while its
#       label requests `BRIDGE_OR_SEMANTIC_BOUNDARY`.  Its author resolves it,
#       not an auditor.
# Guessing types to close the gap is still forbidden.
UNCLASSIFIED_BASELINE = 9


class SourceNativeComparatorRoutingAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        cls.entries = cls.registry["artifacts"]

    def test_registry_covers_live_comparator_surfaces(self) -> None:
        registered = {entry["path"] for entry in self.entries}
        discovered = discovered_artifacts()
        self.assertEqual(len(registered), len(self.entries), "duplicate registry path")

        # Every registered path must still exist in the derived scope.
        self.assertEqual(registered - discovered, set(),
                         "registry names paths the derived scope no longer finds")

        # Widening scope from the old seven-token list to convention surfaced
        # artifacts the registry has never classified.  They are NOT silently
        # accepted: the gap is printed every run and may not grow.  Classifying
        # them is the method owner's call, not this gate's -- guessing a
        # CONVENTIONAL_COMPARATOR / BRIDGE / SOURCE_NATIVE label here would be
        # exactly the unsourced attribution this method exists to prevent.
        gap = sorted(discovered - registered)
        print(f"\nsource_native_comparator_routing_audit[coverage]: "
              f"{len(discovered)} in derived scope, {len(registered)} registered, "
              f"{len(gap)} UNCLASSIFIED (baseline {UNCLASSIFIED_BASELINE}).")
        for path in gap:
            print(f"  UNCLASSIFIED  {path}")
        self.assertLessEqual(
            len(gap), UNCLASSIFIED_BASELINE,
            "new unclassified comparator-scope artifact; classify it in the "
            "registry or narrow the derived scope deliberately")

    def test_every_registered_artifact_repeats_the_routing_notice(self) -> None:
        for entry in self.entries:
            with self.subTest(path=entry["path"]):
                text = (ROOT / entry["path"]).read_text(encoding="utf-8")
                self.assertIn(MARKER, text)
                self.assertIn(METHOD, text)
                self.assertRegex(text, classification_pattern(entry["classification"]))

    def test_classifications_are_typed(self) -> None:
        allowed = set(self.registry["classifications"])
        self.assertEqual({"CONVENTIONAL_COMPARATOR", "SOURCE_NATIVE_ROUTE", "BRIDGE_OR_SEMANTIC_BOUNDARY"}, allowed)
        for entry in self.entries:
            with self.subTest(path=entry["path"]):
                self.assertIn(entry["classification"], allowed)

    def test_repository_instructions_make_routing_mandatory(self) -> None:
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        geometer = (ROOT / "GEOMETER-VS-PHYSICS-OBJECTS.md").read_text(encoding="utf-8")
        method = (ROOT / METHOD).read_text(encoding="utf-8")
        self.assertIn(METHOD, agents)
        self.assertIn(METHOD, geometer)
        self.assertIn("CONVENTIONAL_ROUTE_EXCLUDED", method)
        self.assertIn("the total theory remains\nnon-chiral", method)
        self.assertIn("there is “no Higgs”", method)

    def test_source_native_entrypoints_resolve(self) -> None:
        required = (
            "lab/active-research/joe-directed/high-energy-two-plus-one/he1-imposter-separation-invariant-2026-08-14.md",
            "explorations/signature-chirality-conjugation-check-2026-08-13.md",
            "explorations/layer0-pass-on-the-two-higgs-objects-2026-07-29.md",
            "explorations/vertical-vev-chirality-bridge-2026-07-29.md",
            "lab/active-research/joe-directed/majorana-126-neutrino/src1-source-steelman-of-the-vev-2026-08-14.md",
            "lab/active-research/pati-salam-chain-verification.md",
        )
        for relative in required:
            with self.subTest(path=relative):
                self.assertTrue((ROOT / relative).is_file())


if __name__ == "__main__":
    unittest.main(verbosity=2)
