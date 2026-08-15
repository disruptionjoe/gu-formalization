#!/usr/bin/env python3
"""Prevent conventional particle comparators from silently adjudicating GU."""

from __future__ import annotations

import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
NON_ARTIFACT_DOC_TYPES = ("overview", "stewardship_record")
REGISTRY_PATH = ROOT / "lab/process/source-native-comparator-routing-registry.json"
METHOD = "lab/methods/source-native-comparator-routing.md"
MARKER = "GU-COMPARATOR-ROUTING"


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
# scope.
#
# KNOWN INCONSISTENCY, recorded rather than papered over.  The method says an
# artifact "may then state" its classification -- optional -- while this gate
# counts every unregistered artifact as a gap.  So an artifact can be fully
# method-compliant and still appear here.  Of the 16 remaining, 12 carry the
# required notice and simply never declared a type, and 4 carry no notice at
# all; only the latter are actual method violations.  Resolving this means the
# method owner either makes declaration mandatory or this gate separates the
# two populations.  Guessing types to close the gap is still forbidden.
UNCLASSIFIED_BASELINE = 16


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
                self.assertIn(f"Classification: `{entry['classification']}`", text)

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
