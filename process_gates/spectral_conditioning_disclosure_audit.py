#!/usr/bin/env python3
"""Spectral claims in a near-defective regime must disclose conditioning.

PROPOSED BY specialist S4 (pseudospectra: Trefethen-Embree) in
explorations/specialist-panel-on-the-degenerate-point-2026-08-08.md, and filed
as register row M-S2.  This gate is the contract half of that proposal.

WHY.  Near a defective (non-diagonalizable) operator, eigenvalues are
exponentially ill-conditioned and the pseudospectrum is vastly larger than the
spectrum, so computed eigenvalues can be artifacts of the arithmetic rather than
properties of the operator.  The repository has results in exactly that regime:
VG-V4 measures a perturbation-splitting exponent of 0.498 (Jordan value 1/2),
eigenvector coalescence overlap 1.000000, and -- the tell -- a K-Gram minimum
eigenvalue that SHRINKS with refinement (2.6e-4 -> 6.2e-6 as N: 12 -> 16).  A
quantity getting worse as resolution improves is the signature of approaching
defectiveness.  No artifact in that line reports a condition number.

WHAT THIS GATE DOES, and deliberately does NOT do.

  It does NOT retroactively fail existing artifacts.  Doing so would turn a
  methodological proposal into a red gate across historical work, which is the
  failure mode this repository has already paid for once (see the standing
  SIGNATURE_AMBIENT_K77 red gate, which nobody can close without rewriting what
  seven waves declared).  Legacy artifacts are CENSUSED and reported.

  It DOES assert that the requirement is recorded (register row M-S2 exists),
  and it fails for artifacts created ON OR AFTER the register entry that make a
  near-defective spectral claim without disclosing a conditioning quantity.
  The requirement therefore binds new work and documents old work.

HONEST LIMIT.  This is a TEXTUAL audit.  It cannot tell whether a reported
condition number is correct, or whether an artifact is truly in a near-defective
regime -- only whether it uses the vocabulary of one without the vocabulary of
conditioning.

ON FALSE POSITIVES, CORRECTED 2026-08-08 (same day this gate landed).  The
original docstring said false positives "should be resolved by adding the
disclosure, not by weakening the marker list".  THAT GUIDANCE WAS WRONG and is
withdrawn.  The bare marker "defective" matched ordinary English -- "defective
as a construction", "the motivation is defective" -- and flagged two artifacts,
one of them another agent's, where a conditioning disclosure would have been
meaningless noise.  A gate that compels meaningless disclosures is worse than no
gate: it trains agents to satisfy it mechanically.  The marker was narrowed to
technical collocations instead.  The correct rule: if the vocabulary match is
NOT about operator defectiveness, fix the MARKER; only add a disclosure when the
artifact really is making a spectral claim in a near-defective regime.
"""

from __future__ import annotations

import datetime as dt
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "lab/process/improvement-register-2026-08-03.md"
BINDING_FROM = dt.date(2026, 8, 8)

SEARCH_DIRS = ("explorations", "canon", "lab/process")

# vocabulary that indicates a near-defective / degenerate spectral regime
DEFECTIVE_MARKERS = (
    "jordan block", "jordan boundary", "jordan pathology",
    "exceptional point", "eigenvector coalescence", "coalescence overlap",
    "splitting exponent", "non-diagonalizable", "nondiagonalizable",
    # "defective" ALONE is ordinary English ("a defective argument") and produced
    # two false positives within hours of this gate landing, one of them on
    # another agent's artifact. Require the technical collocation.
    "defective operator", "defective matrix", "defective eigenvalue",
    "near-defective", "defective point",
)

# vocabulary that constitutes disclosure
CONDITIONING_MARKERS = (
    "condition number", "conditioning", "pseudospectr", "pseudo-spectr",
    "cond(", "kappa(", "well-conditioned", "ill-conditioned",
)

FRONT_DATE = re.compile(r"^created:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})", re.M)


def artifact_date(text: str) -> dt.date | None:
    m = FRONT_DATE.search(text)
    if not m:
        return None
    try:
        return dt.date.fromisoformat(m.group(1))
    except ValueError:
        return None


def scan() -> tuple[list[tuple[str, dt.date | None]], list[tuple[str, dt.date]]]:
    """Return (legacy_undisclosed, binding_undisclosed)."""
    legacy: list[tuple[str, dt.date | None]] = []
    binding: list[tuple[str, dt.date]] = []
    for rel in SEARCH_DIRS:
        base = ROOT / rel
        if not base.exists():
            continue
        for path in base.rglob("*.md"):
            try:
                text = path.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            low = text.lower()
            if not any(mark in low for mark in DEFECTIVE_MARKERS):
                continue
            if any(mark in low for mark in CONDITIONING_MARKERS):
                continue
            created = artifact_date(text)
            name = str(path.relative_to(ROOT))
            if created is not None and created >= BINDING_FROM:
                binding.append((name, created))
            else:
                legacy.append((name, created))
    legacy.sort()
    binding.sort()
    return legacy, binding


class SpectralConditioningDisclosure(unittest.TestCase):

    def test_the_requirement_is_recorded_in_the_register(self) -> None:
        self.assertTrue(REGISTER.exists(), "improvement register not found")
        text = REGISTER.read_text(encoding="utf-8", errors="ignore")
        self.assertIn("M-S2", text,
                      "register row M-S2 must exist -- this gate enforces a "
                      "recorded proposal, not an unrecorded preference")
        self.assertIn("condition number", text.lower(),
                      "M-S2 must state the disclosure requirement in words")

    def test_census_of_legacy_artifacts_is_reported_not_failed(self) -> None:
        legacy, _ = scan()
        print("\n[census] artifacts using near-defective vocabulary WITHOUT a")
        print("         conditioning disclosure, created before "
              f"{BINDING_FROM.isoformat()} -- REPORTED, NOT FAILED:")
        if not legacy:
            print("           (none)")
        for name, created in legacy[:40]:
            stamp = created.isoformat() if created else "no created: field"
            print(f"           {stamp}  {name}")
        if len(legacy) > 40:
            print(f"           ... and {len(legacy) - 40} more")
        print(f"         total: {len(legacy)}")
        print("\n         These are NOT defects. They predate the requirement.")
        print("         VG-V4 is the known live case (splitting exponent 0.498,")
        print("         K-Gram min eig shrinking 2.6e-4 -> 6.2e-6 with refinement).")
        self.assertIsInstance(legacy, list)

    def test_artifacts_from_the_binding_date_must_disclose(self) -> None:
        _, binding = scan()
        print(f"\n[binding] artifacts created on/after {BINDING_FROM.isoformat()} "
              "making a near-defective spectral")
        print("          claim WITHOUT disclosing conditioning:")
        for name, created in binding:
            print(f"            {created.isoformat()}  {name}")
        if not binding:
            print("            (none)")
        self.assertEqual(
            [], [n for n, _ in binding],
            "an artifact created on or after the register entry makes a "
            "near-defective spectral claim without reporting a condition number "
            "or pseudospectral radius (register M-S2). Fix by ADDING the "
            "disclosure, not by removing the vocabulary.",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
