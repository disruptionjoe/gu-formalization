#!/usr/bin/env python3
"""Structural checks for the 25-persona source-action lens vote.

Run: python tests/test_persona_lens_vote.py
"""

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "PERSONA-LENS-VOTE-2026-06-27.md"


class PersonaLensVoteNoteTests(unittest.TestCase):
    def test_note_has_25_personas(self):
        text = NOTE.read_text(encoding="utf-8")
        personas = re.findall(r"^\| P\d{2} ", text, flags=re.MULTILINE)
        self.assertEqual(len(personas), 25)

    def test_note_has_vote_and_actionable_portfolio(self):
        text = NOTE.read_text(encoding="utf-8")
        for phrase in [
            "Idea Catalog",
            "Persona Rankings",
            "Vote Results",
            "Consensus Portfolio",
            "First-Week Work Order",
            "GU-native minimax loss channels",
            "Boundary spectral-section / holonomy finality",
            "Anti-import adversarial oracle",
        ]:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_vote_winner_is_loss_channel_workstream(self):
        text = NOTE.read_text(encoding="utf-8")
        self.assertIn("| 1 | B | 20 |", text)
        self.assertIn("The top cross-lens demand", text)


if __name__ == "__main__":
    unittest.main()
