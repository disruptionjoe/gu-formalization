#!/usr/bin/env python3
"""Prevent conventional particle comparators from silently adjudicating GU."""

from __future__ import annotations

import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "lab/process/source-native-comparator-routing-registry.json"
METHOD = "lab/methods/source-native-comparator-routing.md"
MARKER = "GU-COMPARATOR-ROUTING"


def discovered_artifacts() -> set[str]:
    result: set[str] = set()
    joe_root = ROOT / "lab/active-research/joe-directed"
    joe_tokens = (
        "high-energy-two-plus-one", "anomaly-cancellation",
        "majorana-126-neutrino", "photon-extra-vector-spectrum",
        "massless-vector-cosmology", "coupling-unification",
        "baryon-number-and-proton-decay",
    )
    for path in joe_root.rglob("*.md"):
        relative = path.relative_to(ROOT).as_posix()
        if any(token in relative for token in joe_tokens):
            result.add(relative)
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


class SourceNativeComparatorRoutingAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        cls.entries = cls.registry["artifacts"]

    def test_registry_exactly_covers_live_comparator_surfaces(self) -> None:
        registered = {entry["path"] for entry in self.entries}
        self.assertEqual(discovered_artifacts(), registered)
        self.assertEqual(len(registered), len(self.entries), "duplicate registry path")

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
