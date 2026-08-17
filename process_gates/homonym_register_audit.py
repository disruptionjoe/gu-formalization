#!/usr/bin/env python3
"""Well-formedness gate plus warn-only sensing floor for the homonym register.

THE SURFACE.  lab/process/homonym-register.yaml is the consolidated index of
same-token collisions the program has PAID for (receipts required), plus the
transcription-variant spellings that make exact-substring censuses of the ASR
transcripts silently incomplete.  It consolidates five prior surfaces; the
anti-rival mechanism is HERE: this gate FAILS if lab/process/NAMES.md ever
holds a name cell without a register entry, so the human table and the machine
register cannot diverge silently.

WHAT REDS.  Only registry coherence: the YAML parses; every entry has all
fields for its kind and a receipt; every cited locus resolves (file exists,
line exists); every verbatim quote is present in its cited file
(whitespace-normalized); tokens are unique; the contrary control is present
and is NOT shaped like a homonym; sensing blocks compile.

WHAT NEVER REDS.  The sensing floor.  For a SMALL set of highest-cost tokens
the gate PRINTS a census of current occurrences against a dated baseline and
never fails on it, because prose legitimately uses ambient words.  A gate that
reds on the word "positive" would be removed within a week and deserve it.
Baselines are observations, not thresholds.

Run:      python process_gates/homonym_register_audit.py
Selftest: python process_gates/homonym_register_audit.py --selftest
          (verifies the CLEAN baseline exits 0 FIRST, then plants false facts
          into a scratch copy of the register — each must drive exit 1 — and
          exits 0 itself only if every plant was caught.)

Override: HOMONYM_REGISTER_PATH=<path> points the audit at an alternate
register file; used by the selftest and by the FX-3 certificate.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTER = ROOT / "lab/process/homonym-register.yaml"
REGISTER_PATH = Path(os.environ.get("HOMONYM_REGISTER_PATH", str(DEFAULT_REGISTER)))
NAMES_MD = ROOT / "lab/process/NAMES.md"

KINDS = {
    "homonym",
    "near_collision",
    "prefix_collision",
    "transcription_variant",
}
CONTROL_KIND = "not_a_homonym"
FLAG_MAP = {"IGNORECASE": re.IGNORECASE, "MULTILINE": re.MULTILINE, "NONE": 0}


def norm(text: str) -> str:
    """Collapse whitespace runs so quotes survive the line-wrapping of the
    file they cite (same convention as the SG-1 probe)."""
    return re.sub(r"\s+", " ", text)


def split_locus(locus: str) -> tuple[str, int | None]:
    m = re.match(r"^(.*?):(\d+)$", locus)
    if m:
        return m.group(1), int(m.group(2))
    return locus, None


def load_register() -> dict:
    return yaml.safe_load(REGISTER_PATH.read_text(encoding="utf-8"))


def names_md_first_cells() -> list[str]:
    """Exact first table cells of NAMES.md data rows (after the |---| separator)."""
    cells: list[str] = []
    in_table = False
    for line in NAMES_MD.read_text(encoding="utf-8").splitlines():
        if re.match(r"^\|\s*-+", line):
            in_table = True
            continue
        if in_table and line.startswith("|"):
            parts = line.split("|")
            if len(parts) > 2:
                cells.append(parts[1].strip())
    return cells


class HomonymRegisterAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.reg = load_register()
        cls.entries = cls.reg.get("entries", [])
        cls.controls = cls.reg.get("contrary_controls", [])

    # ---------------- well-formedness (RED on failure) ----------------

    def test_top_level_shape(self) -> None:
        for key in ("version", "updated", "owner", "gate", "seeded", "entries", "contrary_controls"):
            self.assertIn(key, self.reg, f"register missing top-level key {key!r}")
        self.assertTrue(self.entries, "register has no entries")
        self.assertGreaterEqual(
            len(self.entries), int(self.reg["seeded"]["entries"]),
            "entries fell below the seeded floor — the register only grows")

    def test_tokens_unique_and_kinds_typed(self) -> None:
        tokens = [e.get("token") for e in self.entries]
        self.assertEqual(len(tokens), len(set(tokens)), "duplicate token in register")
        for e in self.entries:
            with self.subTest(token=e.get("token")):
                self.assertTrue(e.get("token"), "entry without token")
                self.assertIn(e.get("kind"), KINDS,
                              f"kind {e.get('kind')!r} not in {sorted(KINDS)}")
                self.assertTrue(e.get("provenance"), "entry without provenance")

    def test_every_entry_has_all_fields_for_its_kind(self) -> None:
        for e in self.entries:
            with self.subTest(token=e.get("token")):
                if e["kind"] == "transcription_variant":
                    self.assertTrue(e.get("canonical"), "variant entry without canonical spelling")
                    variants = e.get("variants", [])
                    self.assertGreaterEqual(len(variants), 1, "variant entry without variants")
                    for v in variants:
                        self.assertTrue(v.get("form"), "variant without form")
                        self.assertTrue(v.get("locus"), "variant without locus")
                else:
                    senses = e.get("senses", [])
                    self.assertGreaterEqual(
                        len(senses), 2,
                        "a homonym/collision entry needs at least two senses")
                    for s in senses:
                        self.assertTrue(s.get("definition"), "sense without definition")
                        self.assertTrue(s.get("namespace"), "sense without namespace/layer")
                        self.assertTrue(s.get("locus"), "sense without citation locus")
                dis = e.get("disambiguator", {})
                self.assertTrue(dis.get("rule"), "entry without disambiguator rule")
                self.assertTrue(dis.get("attested_at"),
                                "disambiguator without attestation — the register "
                                "must not coin names nobody uses")

    def test_no_entry_without_a_receipt(self) -> None:
        for e in self.entries:
            with self.subTest(token=e.get("token")):
                r = e.get("receipt", {})
                self.assertTrue(r.get("incident"), "receipt without incident text")
                self.assertTrue(r.get("paid_by"), "receipt without paid_by loci — "
                                "a speculative homonym list decays into noise")

    def test_all_loci_resolve(self) -> None:
        def check_locus(owner: str, locus: str) -> None:
            path, lineno = split_locus(locus)
            fp = ROOT / path
            self.assertTrue(fp.exists(), f"{owner}: locus file missing: {path}")
            if lineno is not None:
                n = len(fp.read_text(encoding="utf-8", errors="ignore").splitlines())
                self.assertLessEqual(lineno, n,
                                     f"{owner}: {path} has {n} lines, cited :{lineno}")

        for e in self.entries + self.controls:
            token = e.get("token", "?")
            for s in e.get("senses", []):
                check_locus(token, s["locus"])
            for v in e.get("variants", []):
                check_locus(token, v["locus"])
            for a in e.get("disambiguator", {}).get("attested_at", []):
                check_locus(token, a)
            for p in e.get("receipt", {}).get("paid_by", []):
                check_locus(token, p)
            if e.get("locus"):
                check_locus(token, e["locus"])

    def test_verbatim_quotes_present_in_cited_files(self) -> None:
        def check_quote(owner: str, quote: str, at: str) -> None:
            fp = ROOT / split_locus(at)[0]
            self.assertTrue(fp.exists(), f"{owner}: quote_at file missing: {at}")
            blob = norm(fp.read_text(encoding="utf-8", errors="ignore"))
            self.assertIn(norm(quote), blob,
                          f"{owner}: verbatim quote not found in {at}: {quote!r}")

        for e in self.entries + self.controls:
            token = e.get("token", "?")
            r = e.get("receipt", {})
            if r.get("quote"):
                self.assertTrue(r.get("quote_at"), f"{token}: receipt quote without quote_at")
                check_quote(token, r["quote"], r["quote_at"])
            for s in e.get("senses", []):
                if s.get("quote"):
                    check_quote(token, s["quote"], s["locus"])
            for v in e.get("variants", []):
                if v.get("quote"):
                    check_quote(token, v["quote"], v["locus"])
            if e.get("quote"):
                check_quote(token, e["quote"], e.get("quote_at", e.get("locus", "")))

    def test_names_md_is_fully_absorbed(self) -> None:
        """The anti-rival check: every NAMES.md name cell has a register entry."""
        cells = names_md_first_cells()
        self.assertGreaterEqual(len(cells), 9, "NAMES.md table parse found fewer rows than seeded")
        carried = {e.get("names_md_row") for e in self.entries if e.get("names_md_row")}
        missing = [c for c in cells if c not in carried]
        self.assertEqual(missing, [],
                         "NAMES.md rows with no register entry (add the entry, "
                         f"carrying names_md_row verbatim): {missing}")

    def test_consolidated_surfaces_resolve(self) -> None:
        for block in ("consolidates", "adjacent_not_consolidated"):
            for s in self.reg.get(block, []):
                with self.subTest(surface=s["path"]):
                    fp = ROOT / s["path"]
                    self.assertTrue(fp.exists(), f"{block} path missing: {s['path']}")
                    if s.get("anchor"):
                        self.assertIn(s["anchor"], fp.read_text(encoding="utf-8"),
                                      f"anchor not found in {s['path']}: {s['anchor']!r}")

    def test_contrary_control_present_and_discriminated(self) -> None:
        self.assertGreaterEqual(len(self.controls), 1, "no contrary control")
        for c in self.controls:
            with self.subTest(token=c.get("token")):
                self.assertEqual(c.get("kind"), CONTROL_KIND)
                self.assertNotIn("senses", c,
                                 "a contrary control must not carry a sense split — "
                                 "that is what registration means")
                self.assertTrue(c.get("evidence_it_is_not"),
                                "contrary control without evidence")
                self.assertTrue(c.get("discrimination"),
                                "contrary control must state the discrimination rule")
        control_tokens = {c["token"] for c in self.controls}
        entry_tokens = {e["token"] for e in self.entries}
        self.assertEqual(control_tokens & entry_tokens, set(),
                         "a token cannot be both registered and a contrary control")

    def test_sensing_blocks_compile(self) -> None:
        for e in self.entries:
            sensing = e.get("sensing")
            if not sensing:
                continue
            with self.subTest(token=e["token"]):
                flags = FLAG_MAP[sensing.get("pattern_flags", "NONE")]
                re.compile(sensing["pattern"], flags)
                scope = ROOT / sensing["scope"]
                self.assertTrue(scope.exists(), f"sensing scope missing: {sensing['scope']}")
                self.assertIsInstance(sensing["baseline"], int)
                self.assertEqual(sensing.get("mode"), "warn_only",
                                 "sensing must be warn_only — this gate is a "
                                 "sensing floor, not a language police")

    # ---------------- sensing floor (PRINTS, never reds) ----------------

    def test_zz_sensing_floor_census_warn_only(self) -> None:
        """Warn-only census. This test PASSES regardless of counts; growth is
        printed for the next steward pass, never enforced."""
        print("\nhomonym_register_audit[sensing floor] — warn-only, never red:")
        for e in self.entries:
            sensing = e.get("sensing")
            if not sensing:
                continue
            flags = FLAG_MAP[sensing.get("pattern_flags", "NONE")]
            pat = re.compile(sensing["pattern"], flags)
            scope = ROOT / sensing["scope"]
            exclude = tuple(sensing.get("exclude", []))
            total = 0
            files = 0
            for fp in scope.rglob(sensing.get("glob", "*.md")):
                rel = fp.relative_to(ROOT).as_posix()
                if any(part in rel for part in exclude):
                    continue
                n = len(pat.findall(fp.read_text(encoding="utf-8", errors="ignore")))
                if n:
                    total += n
                    files += 1
            drift = total - sensing["baseline"]
            marker = "OK at baseline" if drift <= 0 else f"WARN +{drift} vs baseline (advisory only)"
            print(f"  {e['token']!r}: {total} occurrence(s) in {files} file(s) "
                  f"[baseline {sensing['baseline']} @ {sensing['measured']}] — {marker}")
        self.assertTrue(True)


# ----------------------------------------------------------------------
# --selftest: clean baseline FIRST, then planted false facts, each exit 1.
# ----------------------------------------------------------------------

PLANTS = (
    ("receipt deleted from the cone entry",
     "      incident: >-\n        three distinct objects wearing one name repo-wide",
     "      incident_removed: >-\n        three distinct objects wearing one name repo-wide"),
    ("locus pointed at a file that does not exist",
     "explorations/wave-swing3-the-outside-2026-07-21.md:18",
     "explorations/wave-swing3-the-outside-DOES-NOT-EXIST.md:18"),
    ("locus line number pushed past end of file",
     "lab/process/NAMES.md:23",
     "lab/process/NAMES.md:9999"),
    ("verbatim quote corrupted",
     "quote: \"=> they INTERSECT IN ZERO\"",
     "quote: \"=> they INTERSECT IN ONE\""),
    ("homonym reduced to a single sense",
     "      - definition: geometric torsion of a connection — GU's augmented torsion T\n"
     "        namespace: cb-b row GR-5\n"
     "        locus: \"explorations/conditional-build/cb-b-lagrangian-terms-2026-08-05.md:185\"\n",
     ""),
    ("token duplicated",
     "  - token: sigma\n    kind: homonym",
     "  - token: theta\n    kind: homonym"),
    ("NAMES.md row uncarried (names_md_row dropped)",
     "    names_md_row: \"`sigma`\"",
     "    names_md_row: \"`sigma-DROPPED`\""),
    ("kind outside the type system",
     "  - token: vial\n    kind: transcription_variant",
     "  - token: vial\n    kind: vibe"),
    ("contrary control removed",
     "  - token: gimmel\n    kind: not_a_homonym",
     "  - token: gimmel\n    kind_removed: not_a_homonym"),
    ("sensing switched from warn_only to enforcing",
     "      baseline: 122\n      baseline_files: 11\n      measured: 2026-08-16\n      mode: warn_only",
     "      baseline: 122\n      baseline_files: 11\n      measured: 2026-08-16\n      mode: red"),
    ("disambiguator attestation dropped (register coining a name)",
     "      rule: \"cite by namespace, not by prefix (the BD README's own prescription)\"\n      attested_at:\n        - \"lab/active-research/joe-directed/base-duality/README.md:25\"",
     "      rule: \"cite by namespace, not by prefix (the BD README's own prescription)\"\n      attested_at: []"),
    ("YAML syntax broken",
     "version: 1",
     "version: 1\n  broken:\n indent: ["),
)


def run_audit(register_path: Path) -> subprocess.CompletedProcess:
    env = dict(os.environ, HOMONYM_REGISTER_PATH=str(register_path))
    return subprocess.run(
        [sys.executable, str(Path(__file__).resolve())],
        capture_output=True, text=True, env=env, cwd=str(ROOT))


def selftest() -> int:
    source = DEFAULT_REGISTER.read_text(encoding="utf-8")

    print("BASELINE — verifying the UNMUTATED register passes the audit first")
    base = run_audit(DEFAULT_REGISTER)
    if base.returncode != 0:
        print("  BASELINE IS RED. Planted-fact results would be meaningless. ABORTING.")
        print(base.stdout[-2000:])
        print(base.stderr[-2000:])
        return 1
    print("  baseline GREEN (exit 0) — plants are now meaningful\n")

    caught = 0
    with tempfile.TemporaryDirectory(prefix="homonym_selftest_") as td:
        mutant = Path(td) / "homonym-register.mutant.yaml"
        for name, old, new in PLANTS:
            if old not in source:
                print(f"  PLANT NOT APPLICABLE (needle missing): {name}")
                return 1
            mutant.write_text(source.replace(old, new, 1), encoding="utf-8")
            result = run_audit(mutant)
            if result.returncode == 0:
                print(f"  NOT CAUGHT (mutant register passed): {name}")
                return 1
            caught += 1
            print(f"  caught (exit {result.returncode}): {name}")

    print(f"\n--selftest: baseline verified GREEN first, then {caught}/{len(PLANTS)} "
          "planted false facts each drove exit 1.")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        raise SystemExit(selftest())
    unittest.main()
