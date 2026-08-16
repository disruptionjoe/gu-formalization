#!/usr/bin/env python3
"""AR-2 deferral archaeology — mechanical re-run of the sweep and its typing.

Re-runs the deferral sweep of
`lab/active-research/joe-directed/archaeology/ar2-deferral-archaeology-2026-08-15.md`
and asserts every count and every typing decision that artifact publishes.

Design notes, stated so the checks cannot be read as stronger than they are:

1. EXACT vs FLOOR.  The checkout is shared with concurrent agents and files
   appear beside this one mid-run.  Counts over a PINNED file list are asserted
   EXACTLY (`assertEqual`); the repo-wide census is asserted as a FLOOR
   (`assertGreaterEqual`) and printed, because a concurrent writer can only
   raise it.  A floor is labelled a floor everywhere it appears.  No tolerance
   band is used anywhere: a tolerance that swallows a planted control is the
   defect this gate family exists to detect.

2. NEGATIVE assertions carry the OPEN typings.  "Seam S is still open" is
   checked as: the resolution token is ABSENT from the surfaces that would
   carry it.  Absence checks are the ones that rot, so each names the exact
   file and token, and `--selftest` plants a false resolution to prove the
   check can fire.

3. Integers only.  No float appears in any asserted quantity.

Usage
    _local/cas-venv/bin/python tests/channel-swings/joe_directed_ar2_deferral_archaeology.py
    _local/cas-venv/bin/python tests/channel-swings/joe_directed_ar2_deferral_archaeology.py --selftest
    _local/cas-venv/bin/python tests/channel-swings/joe_directed_ar2_deferral_archaeology.py --control <name>

`--selftest` runs every planted control in a subprocess and requires each to
exit 1.  If any planted falsehood passes, the harness itself exits 1: a control
that cannot fail is vacuous.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VENDOR_DIRS = {".git", "_local", ".lake", "node_modules", "__pycache__"}

# THE INSTRUMENT IS NOT THE CORPUS.  `archaeology/` holds deferral catalogues --
# this file's own artifact, and AR-1's sibling, written concurrently into the
# same directory.  They quote every operator phrase they measure, so counting
# them inflates the census they publish.  Excluding the instrument is a
# principle, not a convenience: a deferral census that includes deferral
# censuses is circular and drifts every time a sibling is written.
INSTRUMENT_PREFIX = "lab/active-research/joe-directed/archaeology/"

# ---------------------------------------------------------------------------
# The sweep vocabulary.  CORE = explicit non-resolution operators: the author
# says, in the first person and about THIS artifact, that a question was raised
# and not answered.  HEDGE = the ambient open-state vocabulary, which is 7.4x
# larger and is NOT a deferral signal (see the artifact's detection section).
# ---------------------------------------------------------------------------
CORE_OPERATORS = (
    "not resolved here", "not settled here", "not adjudicated here",
    "not decided here", "not attempted here", "could not determine",
    "remains unclear", "left open", "leaves open", "leave open",
    "leave it open", "leaves it open", "leaves that open", "deferred to",
    "deferred here", "flagged for", "beyond scope", "beyond the scope",
    "known limit",
)
HEDGE_OPERATORS = (
    "remains open", "remain open", "unresolved", "out of scope",
    "attack surface", "later gate", "weakest seam",
)

# WHITESPACE NORMALIZATION IS LOAD-BEARING FOR RECALL.  This repository hard-
# wraps markdown near column 76, so an operator phrase routinely straddles a
# newline ("not adjudicated\nhere").  Naive whole-file substring counting misses
# them: measured 2026-08-15, 16 of 315 repo-wide occurrences and 1 of 24 in the
# joe-directed tree, and the one missed in joe-directed was a real seam (BD-D's
# undecided Delta1 fibre-algebra retyping).  Both counts are asserted so the
# gap itself is a pinned fact, not a footnote.
NAIVE_JD_OCCURRENCES = 23
NAIVE_REPO_OCCURRENCE_FLOOR = 299

# Pinned census, measured at the AR-2 publication cut.  The original probe
# described this as pinned but accidentally enumerated the live tree.  Eight
# same-session artifacts landed after AR-2 and exposed the mismatch.  The
# census is historical; seam status below is intentionally checked live.
JOE_DIRECTED = "lab/active-research/joe-directed"
MEASUREMENT_COMMIT = "805713e8"
PINNED_JD_FILES = 48
PINNED_JD_OCCURRENCES = 24
PINNED_JD_HIT_FILES = 18
PINNED_JD_BY_PHRASE = {
    "left open": 5,
    "not resolved here": 4,
    "not adjudicated here": 3,
    "deferred to": 2,
    "not settled here": 2,
    "not decided here": 2,
    "flagged for": 2,
    "known limit": 1,
    "leaves open": 1,
    "leaves that open": 1,
    "leaves it open": 1,
}
# Repo-wide floors, measured 2026-08-15.  Floors, not equalities: shared checkout.
REPO_MD_FLOOR = 3656
REPO_CORE_OCCURRENCE_FLOOR = 315
REPO_CORE_FILE_FLOOR = 237
REPO_HEDGE_OCCURRENCE_FLOOR = 2306

# ---------------------------------------------------------------------------
# Typed seam catalogue.  Every row the artifact publishes, with the evidence
# substring that establishes it.  `flags` = surfaces that raised the seam.
# `open_absence` = (path, token) pairs whose ABSENCE keeps the seam OPEN.
# ---------------------------------------------------------------------------
LA1 = f"{JOE_DIRECTED}/ledger-advancement/la1-embedding-grant-is-zero-bit-and-group-a-is-already-banked-2026-08-15.md"
LA3 = f"{JOE_DIRECTED}/ledger-advancement/la3-chiral-16-shadow-is-a-comparator-and-the-grant-is-inert-2026-08-15.md"
LA6 = f"{JOE_DIRECTED}/ledger-advancement/la6-the-lagrangian-axis-has-twelve-degrees-of-freedom-and-one-constructible-cover-object-2026-08-15.md"
LA8 = f"{JOE_DIRECTED}/ledger-advancement/la8-rae2-is-refuted-at-the-settled-form-leg-and-the-open-fork-is-not-load-bearing-2026-08-15.md"
LA9 = f"{JOE_DIRECTED}/ledger-advancement/la9-eleven-real-defects-eight-defective-filings-and-one-denominator-mover-2026-08-15.md"
LA4 = f"{JOE_DIRECTED}/ledger-advancement/la4-representation-axis-has-13-grants-and-a-one-vertex-cut-2026-08-15.md"
LA11 = f"{JOE_DIRECTED}/ledger-advancement/la11-b9stat-is-a-base-duality-row-and-four-rows-name-it-as-a-subclause-2026-08-15.md"
OT2 = f"{JOE_DIRECTED}/ownership-theorem/ot2-lt-sm3b-is-not-an-ownership-row-and-the-cheapest-pair-is-the-terminal-pair-2026-08-15.md"
MD1 = f"{JOE_DIRECTED}/four-d-mode-decomposition/md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md"
PHI1 = f"{JOE_DIRECTED}/phi-reduction/phi1-the-reduction-is-rank-one-and-the-14d-kernel-contributes-zero-bits-2026-08-15.md"
PHI2 = f"{JOE_DIRECTED}/phi-reduction/phi2-spin-extended-target-has-rank-five-and-phi1s-containment-survives-2026-08-15.md"
CG1 = f"{JOE_DIRECTED}/coset-versus-gauge/cg1-p-is-a-declared-coset-not-a-gauge-sector-2026-08-14.md"
CC1 = f"{JOE_DIRECTED}/cosmological-constant-sign/cc1-killing-signature-cannot-sign-lambda-2026-08-14.md"
SRC3 = f"{JOE_DIRECTED}/majorana-126-neutrino/src3-potential-unbounded-below-2026-08-14.md"
SRC4 = f"{JOE_DIRECTED}/majorana-126-neutrino/src4-eddy-completion-cannot-rescue-the-potential-2026-08-15.md"
PV1 = f"{JOE_DIRECTED}/photon-extra-vector-spectrum/pv1-available-orbits-retain-an-extra-massless-vector-2026-08-14.md"
PV2 = f"{JOE_DIRECTED}/photon-extra-vector-spectrum/pv2-observation-cannot-reach-the-extra-vectors-2026-08-14.md"
MV1 = f"{JOE_DIRECTED}/massless-vector-cosmology/mv1-the-surviving-massless-vectors-meet-the-data-2026-08-14.md"
BDD = f"{JOE_DIRECTED}/base-duality/bd-d-the-quotient-cures-the-base-not-the-fibre-2026-08-15.md"
BDREG = f"{JOE_DIRECTED}/base-duality/bd-reg-routing-backlog-disposition-2026-08-15.md"
BDPKT = f"{JOE_DIRECTED}/base-duality/bd-disposition-packet-2026-08-15.md"
BDRDM = f"{JOE_DIRECTED}/base-duality/README.md"
JDRDM = f"{JOE_DIRECTED}/README.md"
STEWARD = f"{JOE_DIRECTED}/steward-2026-08-14-research-maintenance-pass.md"
VZ = "explorations/vz-evasion/vz-schur-complement-2026-06-23.md"
NOGO = "canon/no-go-class-relative-map.md"
SHIAB = "canon/shiab-existence-cl95.md"
CARRIER = "canon/carrier-bit-decision-campaign-RESULTS.md"
ROUTING = "lab/methods/source-native-comparator-routing.md"
REGISTER = "lab/sources/source-claim-register.yaml"

SEAMS = [
    # id, type, load_bearing, flags [(path, substring)], open_absence [(path, token)]
    ("AR2-S01", "OPEN", True, [
        (MD1, "`SOLDERED-AD`"),
        (LA8, "`SOLDERED-AD` vs `INERT-AD` named and left open"),
        (PHI2, "raises its stakes and leaves it open"),
        (STEWARD, "`SOLDERED-AD` (MD-1)"),
        (JDRDM, "promoted the `SOLDERED-AD` fork to **verdict-load-bearing**"),
        (LA4, "**Escalation, not adjudication.** MD-1 declares `SOLDERED-AD` vs `INERT-AD` open"),
        (PHI1, "No decision of the `SOLDERED-AD` fork."),
    ], [(BDPKT, "SOLDERED-AD")]),
    ("AR2-S02", "OPEN", True, [
        (LA1, "typing seam"),
        (LA3, "**Flagged for the integrator, not requested:** `AC-C2`"),
        (LA9, "`AC-C2`'s retype and `RA-C1`'s typing are the same unresolved seam"),
    ], [(BDPKT, "RA-C1"), (BDPKT, "AC-C2")]),
    ("AR2-S03", "OPEN", True, [
        (SRC3, "whether GU's norm-square sits above or below the Cartan reduction"),
        (CG1, "norm-square, and GU's kinetic terms, sit ABOVE or BELOW the maximal-compact"),
        (STEWARD, "position relative to the Cartan reduction"),
        (SRC4, "kappa_1 * flat_1 >= 0"),
    ], []),
    ("AR2-S04", "RESOLVED", True, [
        (MD1, "Flagged for the owner of the VZ chain; not"),
        (STEWARD, "**OQ3-V3 was not re-decided.**"),
        (STEWARD, "**Fix the §18.3 defect**"),
        (VZ, "oq3_v3_correction"),
        (VZ, "CORRECTION VZ4-01"),
    ], []),
    ("AR2-S05", "OPEN", True, [
        (MD1, "Whether they reappear as independent 4D fields is a"),
        (LA8, "MD-1 explicitly leaves open whether the 10-dimensional `s^*`-kernel reappears as"),
    ], []),
    ("AR2-S06", "OPEN", True, [
        (BDREG, "cannot both stand. **Not resolved here.**"),
    ], []),
    ("AR2-S07", "UNTYPED", True, [
        (BDPKT, "**Open and NOT settled here:** whether the object belongs in `rows` at all."),
        (LA11, "RA-C1 carries \"a selected embedding outside the unique Weyl orbit\""),
    ], []),
    ("AR2-S08", "OPEN", False, [
        (LA1, "**`LT-SM3b` successor question.**"),
    ], [(OT2, "successor"), (OT2, "AC-G1"), (OT2, "row_status"), (BDPKT, "LT-SM3b")]),
    ("AR2-S09", "OPEN", False, [
        (LA1, "**CB-A `+11` constraint surplus**"),
        (LA9, "+11 constraint surplus overcounts by 5"),
    ], []),
    ("AR2-S10", "OPEN", False, [
        (LA9, "**Decide `coupled_to`.**"),
    ], []),
    ("AR2-S11", "OPEN", False, [
        (BDRDM, "The 2021 draft PDF is **not in the checkout**."),
        (STEWARD, "drops a sentence present in the drafts copy"),
    ], []),
    ("AR2-S12", "OPEN", False, [
        (SHIAB, "is not adjudicated here"),
    ], []),
    ("AR2-S13", "OPEN", False, [
        (PHI2, "**The bit is not adjudicated here.**"),
        (CARRIER, "the bit is NOT decided"),
    ], []),
    ("AR2-S14", "OPEN", False, [
        (PHI2, "It is carried as a fork because"),
    ], []),
    ("AR2-S15", "OPEN", False, [
        (MD1, "is **not** certified"),
    ], []),
    ("AR2-S16", "OPEN", False, [
        (CC1, "which is why it was not adjudicated here"),
    ], []),
    ("AR2-S17", "OPEN", False, [
        (BDRDM, "did **not** adjudicate it"),
        (BDD, "fibre algebra is not adjudicated"),
    ], []),
    ("AR2-S18", "RESOLVED", True, [
        (LA6, "**Not resolved here.**"),
        (OT2, "now resolved, and confirmed"),
    ], []),
    ("AR2-S19", "RESOLVED", True, [
        (PV1, "Two readings survive and are not decided here"),
        (PV2, "first reading fails."),
    ], []),
    ("AR2-S20", "RESOLVED", True, [
        (BDD, "conceded the exact"),
    ], []),
    ("AR2-S21", "SUPERSEDED", False, [
        (MV1, "PV-2 explicitly leaves that open"),
        (JDRDM, "any reading of these files that treats the 24 `p`"),
    ], []),
    ("AR2-S22", "REFUTED", True, [
        (ROUTING, "**Withdrawn clause"),
        (ROUTING, "It’s not extra dimensions. It’s not Kaluza"),
    ], []),
    ("AR2-S23", "DISAVOWED", True, [
        (REGISTER, "SC-GEO-58"),
        (JDRDM, "the source explicitly disavows a Higgs"),
    ], []),
]

EXPECTED_TYPE_COUNTS = {
    "OPEN": 15, "RESOLVED": 4, "SUPERSEDED": 1,
    "REFUTED": 1, "DISAVOWED": 1, "UNTYPED": 1,
}
EXPECTED_SEAMS = 23
EXPECTED_WORKLIST = 5          # OPEN and load-bearing; UNTYPED is excluded
EXPECTED_MULTIPLY_FLAGGED = 14  # seams with >= 2 distinct flagging surfaces

# ---------------------------------------------------------------------------
# Planted controls.  Each name maps to a mutation of the ASSERTED facts.  Every
# one must drive exit 1.
# ---------------------------------------------------------------------------
CONTROLS = {
    "census_occurrences": "joe-directed core-operator count 24 -> 23",
    "census_files": "joe-directed file count 48 -> 47",
    "phrase_table": "'not resolved here' 4 -> 3 in the pinned phrase table",
    "repo_floor": "repo-wide core floor 315 -> 400 (an unreachable floor)",
    "type_counts": "OPEN total 15 -> 14",
    "worklist": "worklist size 6 -> 5",
    "multiply_flagged": "multiply-flagged count 14 -> 13",
    "wrap_blind": "assert the wrap-blind count equals the normalized count",
    # --selftest plants FALSE FACTS about the world, not just about the numbers.
    "false_resolution_soldered_ad": "plant: the disposition packet resolves SOLDERED-AD",
    "false_resolution_lt_sm3b": "plant: OT-2 answers the LT-SM3b successor question",
    "false_repair_vz": "plant: the VZ4 correction marker is absent",
    "false_flag_la6": "plant: LA-6 never wrote 'Not resolved here'",
    "false_hedge_split": "plant: hedge vocabulary is no larger than the core vocabulary",
}

MUT = os.environ.get("AR2_CONTROL", "")


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def read_at_measurement(path: str) -> str:
    proc = subprocess.run(
        ["git", "show", f"{MEASUREMENT_COMMIT}:{path}"],
        cwd=ROOT, capture_output=True, text=True)
    if proc.returncode:
        raise RuntimeError(
            f"cannot read pinned AR-2 corpus at {MEASUREMENT_COMMIT}: {path}\n"
            + proc.stderr)
    return proc.stdout


def pinned_joe_directed_files() -> list[str]:
    proc = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", MEASUREMENT_COMMIT,
         JOE_DIRECTED], cwd=ROOT, capture_output=True, text=True)
    if proc.returncode:
        raise RuntimeError(
            f"cannot enumerate pinned AR-2 corpus at {MEASUREMENT_COMMIT}\n"
            + proc.stderr)
    return sorted(
        p for p in proc.stdout.splitlines()
        if p.endswith(".md") and not p.startswith(INSTRUMENT_PREFIX)
    )


def markdown_files() -> list[str]:
    out = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in VENDOR_DIRS]
        for name in filenames:
            if name.endswith(".md"):
                rel = os.path.relpath(os.path.join(dirpath, name), ROOT)
                if rel.startswith(INSTRUMENT_PREFIX):
                    continue
                out.append(rel)
    out.sort()
    return out


def sweep(paths, vocabulary, normalize=True, reader=read):
    """Occurrence count, hit-file count, per-phrase counter. Integers only.

    `normalize=False` reproduces the WRAP-BLIND detector, kept so the recall
    gap it causes is asserted rather than described.
    """
    per_phrase = Counter()
    hit_files = set()
    total = 0
    for rel in paths:
        try:
            text = reader(rel).lower()
        except OSError:
            continue
        if normalize:
            text = re.sub(r"\s+", " ", text)
        for phrase in vocabulary:
            n = text.count(phrase)
            if n:
                per_phrase[phrase] += n
                hit_files.add(rel)
                total += n
    return total, len(hit_files), per_phrase


class AR2DeferralArchaeology(unittest.TestCase):

    # -- 1. census ---------------------------------------------------------
    def test_01_joe_directed_census_is_exact(self):
        jd = pinned_joe_directed_files()
        expected_files = PINNED_JD_FILES - (1 if MUT == "census_files" else 0)
        self.assertEqual(len(jd), expected_files,
                         "joe-directed markdown file count moved")
        total, nfiles, _ = sweep(jd, CORE_OPERATORS, reader=read_at_measurement)
        expected = PINNED_JD_OCCURRENCES - (1 if MUT == "census_occurrences" else 0)
        self.assertEqual(total, expected)
        self.assertEqual(nfiles, PINNED_JD_HIT_FILES)
        print(f"  census[joe-directed]: {len(jd)} files, "
              f"{total} core-operator occurrences in {nfiles} files")

    def test_02_phrase_table_is_exact(self):
        jd = pinned_joe_directed_files()
        _, _, per_phrase = sweep(
            jd, CORE_OPERATORS, reader=read_at_measurement)
        expected = dict(PINNED_JD_BY_PHRASE)
        if MUT == "phrase_table":
            expected["not resolved here"] = 3
        self.assertEqual(dict(per_phrase), expected)

    def test_03_repo_census_floors_hold(self):
        allmd = markdown_files()
        self.assertGreaterEqual(len(allmd), REPO_MD_FLOOR)
        total, nfiles, _ = sweep(allmd, CORE_OPERATORS)
        floor = 400 if MUT == "repo_floor" else REPO_CORE_OCCURRENCE_FLOOR
        self.assertGreaterEqual(total, floor,
                                "repo-wide core-operator FLOOR breached")
        self.assertGreaterEqual(nfiles, REPO_CORE_FILE_FLOOR)
        hedge_total, _, _ = sweep(allmd, HEDGE_OPERATORS)
        self.assertGreaterEqual(hedge_total, REPO_HEDGE_OCCURRENCE_FLOOR)
        print(f"  census[repo, FLOOR]: {len(allmd)} md files, "
              f"{total} core occurrences in {nfiles} files, "
              f"{hedge_total} hedge occurrences")

    def test_035_wrap_blind_detector_loses_real_seams(self):
        """The naive detector must measurably UNDERCOUNT the normalized one.

        If these two ever agree, either the corpus stopped hard-wrapping or the
        normalization was silently dropped; both make the recall claim false.
        """
        allmd = markdown_files()
        jd = pinned_joe_directed_files()
        naive_repo, _, _ = sweep(allmd, CORE_OPERATORS, normalize=False)
        norm_repo, _, _ = sweep(allmd, CORE_OPERATORS, normalize=True)
        naive_jd, _, _ = sweep(
            jd, CORE_OPERATORS, normalize=False, reader=read_at_measurement)
        norm_jd, _, _ = sweep(
            jd, CORE_OPERATORS, normalize=True, reader=read_at_measurement)
        self.assertEqual(naive_jd, NAIVE_JD_OCCURRENCES)
        self.assertGreaterEqual(naive_repo, NAIVE_REPO_OCCURRENCE_FLOOR)
        if MUT == "wrap_blind":
            self.assertEqual(naive_repo, norm_repo, "planted: no wrap blindness")
            self.assertEqual(naive_jd, norm_jd, "planted: no wrap blindness")
            return
        self.assertLess(naive_jd, norm_jd, "wrap blindness vanished in joe-directed")
        self.assertLess(naive_repo, norm_repo, "wrap blindness vanished repo-wide")
        print(f"  recall gap[wrap-blind vs normalized]: repo {naive_repo} -> "
              f"{norm_repo} ({norm_repo - naive_repo} missed); "
              f"joe-directed {naive_jd} -> {norm_jd} ({norm_jd - naive_jd} missed)")

    def test_04_hedge_vocabulary_dominates_core(self):
        """The detection signature depends on this gap being large."""
        allmd = markdown_files()
        core, _, _ = sweep(allmd, CORE_OPERATORS)
        hedge, _, _ = sweep(allmd, HEDGE_OPERATORS)
        ratio_floor = 1 if MUT == "false_hedge_split" else 7
        self.assertGreaterEqual(hedge // core, ratio_floor,
                                "hedge/core ratio collapsed; the filter is not discriminating")
        if MUT == "false_hedge_split":
            # planted falsehood: assert the two classes are the SAME SIZE
            self.assertEqual(hedge, core, "planted: hedge == core")

    # -- 2. catalogue ------------------------------------------------------
    def test_05_every_flag_substring_is_present(self):
        for seam_id, _kind, _lb, flags, _absent in SEAMS:
            for path, needle in flags:
                with self.subTest(seam=seam_id, path=path):
                    if MUT == "false_flag_la6" and seam_id == "AR2-S18" and path == LA6:
                        self.assertNotIn(needle, read(path), "planted: LA-6 never deferred")
                        continue
                    if (MUT == "false_repair_vz" and seam_id == "AR2-S04"
                            and path == VZ and needle == "CORRECTION VZ4-01"):
                        self.assertNotIn(needle, read(path),
                                         "planted: VZ4 correction marker absent")
                        continue
                    self.assertIn(needle, read(path),
                                  f"{seam_id}: flag evidence missing in {path}")

    def test_06_open_seams_have_no_resolution_token(self):
        for seam_id, kind, _lb, _flags, absent in SEAMS:
            for path, token in absent:
                with self.subTest(seam=seam_id, path=path, token=token):
                    text = read(path)
                    if MUT == "false_resolution_soldered_ad" and token == "SOLDERED-AD":
                        self.assertIn(token, text, "planted: packet resolves SOLDERED-AD")
                        continue
                    if MUT == "false_resolution_lt_sm3b" and path == OT2:
                        self.assertIn(token, text, "planted: OT-2 answers the successor question")
                        continue
                    self.assertNotIn(token, text,
                                     f"{seam_id}: '{token}' now present in {path} — "
                                     f"the seam may have been resolved; re-type it")

    def test_07_type_counts_are_exact(self):
        counts = Counter(kind for _i, kind, _lb, _f, _a in SEAMS)
        expected = dict(EXPECTED_TYPE_COUNTS)
        if MUT == "type_counts":
            expected["OPEN"] = 14
        self.assertEqual(len(SEAMS), EXPECTED_SEAMS)
        self.assertEqual(dict(counts), expected)
        self.assertEqual(sum(counts.values()), len(SEAMS))

    def test_08_worklist_is_open_and_load_bearing(self):
        worklist = [i for i, kind, lb, _f, _a in SEAMS if kind == "OPEN" and lb]
        expected = EXPECTED_WORKLIST - (1 if MUT == "worklist" else 0)
        self.assertEqual(len(worklist), expected, f"worklist: {worklist}")
        # no REFUTED / DISAVOWED / SUPERSEDED item may reach the worklist
        dead = {i for i, kind, _lb, _f, _a in SEAMS
                if kind in ("REFUTED", "DISAVOWED", "SUPERSEDED")}
        self.assertEqual(set(worklist) & dead, set(),
                         "a dead route reached the worklist")

    def test_09_multiply_flagged_count(self):
        multi = [i for i, _k, _lb, flags, _a in SEAMS
                 if len({p for p, _n in flags}) >= 2]
        expected = EXPECTED_MULTIPLY_FLAGGED - (1 if MUT == "multiply_flagged" else 0)
        self.assertEqual(len(multi), expected, f"multiply-flagged: {multi}")

    # -- 3. hazard controls ------------------------------------------------
    def test_10_disavowed_premises_are_registered(self):
        """No worklist item may rest on a premise the source disavows."""
        register = read(REGISTER)
        self.assertIn("core: disavowed-by-source", register)
        n = register.count("core: disavowed-by-source")
        self.assertEqual(n, 11, "disavowed-by-source row count moved")
        for claim in ("SC-GEO-58", "SC-GEN-01", "SC-GEN-04", "SC-META-55"):
            self.assertIn(claim, register)

    def test_11_routing_notice_and_classification_present(self):
        art = ROOT / (JOE_DIRECTED + "/archaeology/ar2-deferral-archaeology-2026-08-15.md")
        if not art.exists():
            self.skipTest("artifact not yet written")
        text = art.read_text(encoding="utf-8")
        self.assertIn("GU-COMPARATOR-ROUTING", text)
        self.assertIn("lab/methods/source-native-comparator-routing.md", text)
        self.assertIn("Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`", text)
        self.assertIn("target_claim: NONE-NOT-A-KILL", text)

    def test_12_kill_language_gate_still_green(self):
        """The artifact must not raise the kill-audit red count above baseline."""
        proc = subprocess.run(
            [sys.executable, "process_gates/kill_target_claim_audit.py"],
            cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0,
                         "kill_target_claim_audit red:\n" + proc.stdout + proc.stderr)


def run_selftest() -> int:
    """Every planted control must exit 1.  A control that passes is vacuous."""
    baseline = subprocess.run(
        [sys.executable, __file__], cwd=ROOT, capture_output=True, text=True)
    if baseline.returncode != 0:
        print("AR-2 selftest REFUSED: the unmutated baseline is not clean.")
        print(baseline.stdout)
        print(baseline.stderr)
        return 1
    print("AR-2 selftest: planted controls, each must exit 1\n")
    failures = []
    for name, description in CONTROLS.items():
        env = dict(os.environ, AR2_CONTROL=name)
        proc = subprocess.run(
            [sys.executable, __file__], cwd=ROOT, env=env,
            capture_output=True, text=True)
        ok = proc.returncode == 1
        print(f"  control {name:32s} exit {proc.returncode}  "
              f"{'OK  ' if ok else 'VACUOUS'}  ({description})")
        if not ok:
            failures.append(name)
    print()
    if failures:
        print(f"SELFTEST FAILED — {len(failures)} vacuous control(s): "
              + ", ".join(failures))
        return 1
    print(f"SELFTEST PASSED — {len(CONTROLS)}/{len(CONTROLS)} planted controls "
          f"each drove exit 1")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(run_selftest())
    if "--control" in sys.argv:
        idx = sys.argv.index("--control")
        os.environ["AR2_CONTROL"] = sys.argv[idx + 1]
        MUT = sys.argv[idx + 1]
        del sys.argv[idx:idx + 2]
    unittest.main(verbosity=2)
