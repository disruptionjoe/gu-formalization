#!/usr/bin/env python3
"""FIX-A evidence probe: SCUR-1's five conditional-build correction blocks, applied 2026-08-17.

Companion to
lab/active-research/joe-directed/source-currency/fixa-cb-corrections-applied-2026-08-17.md.

What this probe certifies (and nothing more): the five append-only correction
blocks SCUR-1 section 7 proposed for the conditional-build pack are PRESENT at
their owners (V1, V2, V5 in CB-A; V3, V4 in CB-B); every original violation
sentence remains BYTE-PRESENT (struck, never deleted -- the append-only
invariant that keeps SCUR-1's own byte-matched evidence probe green); each
struck span and dated bracket marker is present at its locus; the corrected
content, register-owner citations, and cross-links to the application record
are present; the untouched verdict cells still carry their original tokens;
and the three untouched pack members (CB-C, CB-D, CB-E) carry NO 2026-08-17
correction marker (no silent scope expansion), with the absence detector's
power demonstrated on a planted synthetic positive.  It adjudicates no
physics and moves no status.  The canon-adjacent sixth SCUR-1 diff
(shiab-existence-cl95) is NOT applied and NOT certified here by design; it
awaits independent second verification per repo rule.

Discipline (VERIFICATION.md, "Probe and mutation-harness discipline",
2026-08-17): integer arithmetic only, no floats anywhere; guarded file reads
(a missing file is a caught [FAIL], never a crash); a needle-length guard so
an accidentally emptied quotation cannot vacuously match; absence checks
carry a planted-positive control; the selftest verifies the CLEAN BASELINE
first, counts a catch only via a genuine [FAIL] (a crash is REJECTED), and
exits 0 on success.

--selftest: clean baseline first, then six machinery-corruption mutations --
wrong-file redirect, missing-file path, empty needle, count corruption,
contrary-control inversion, blinded absence detector -- each required to
produce at least one genuine [FAIL].
"""

import os
import sys

# ---------------------------------------------------------------------------
# repo-root anchoring
# ---------------------------------------------------------------------------

def find_repo_root():
    d = os.path.abspath(os.path.dirname(__file__))
    for _ in range(6):
        if os.path.exists(os.path.join(d, "CANON.md")):
            return d
        d = os.path.dirname(d)
    return None


REPO = find_repo_root()

JD = "lab/active-research/joe-directed"
CB = "explorations/conditional-build"

FILES = {
    "cba":   CB + "/cb-a-representation-content-2026-08-05.md",
    "cbb":   CB + "/cb-b-lagrangian-terms-2026-08-05.md",
    "cbc":   CB + "/cb-c-anomaly-conditions-2026-08-05.md",
    "cbd":   CB + "/cb-d-parameterizing-the-unknown-2026-08-05.md",
    "cbe":   CB + "/cb-e-source-contact-rows-2026-08-05.md",
    "scur1": JD + "/source-currency/scur1-source-currency-audit-2026-08-17.md",
    "scur1_probe": "tests/channel-swings/joe_directed_scur1_source_currency_audit.py",
    "fixa":  JD + "/source-currency/fixa-cb-corrections-applied-2026-08-17.md",
}

MIN_NEEDLE = 12  # an emptied/truncated quotation must not vacuously match

# The no-expansion marker: FIX-A's umbrella-heading phrase.  Its ABSENCE is
# asserted on the three untouched pack members; its detection power is
# demonstrated on the planted synthetic below (VERIFICATION.md rule 4).
MARKER = "applied from the SCUR-1 source-currency audit"
SYNTHETIC_POSITIVE = ("planted control text -- a corrections section "
                      "(2026-08-17, applied from the SCUR-1 source-currency "
                      "audit) -- end of planted control")

# Append-only invariant: SCUR-1's eight violation needles, verbatim from its
# probe's VIOLATION_NEEDLES table.  Every one must remain byte-present after
# the correction blocks land (struck in place, quoted in the blocks -- never
# deleted).
SCUR1_NEEDLES = [
    ("A1/V1a", "cba", "SOURCE-CONTRADICTED-ON-VEV-INDUCED-EFFECTIVE-CHIRALITY"),
    ("A2/V1b", "cba", "excluded by Schur, not merely unbuilt"),
    ("A3/V1c", "cba", "VEV/low-curvature mass decoupling into chiral sectors"),
    ("A4/V2a", "cba", "Lorentz-scalar components are exactly those with"),
    ("A5/V2b", "cba", "the Higgs must consume the vertical form leg"),
    ("A6/V3",  "cbb", "plus **ten 4D scalars**"),
    ("A7/V4",  "cbb", "only by an unbuilt mirror-gapping condensate"),
    ("A8/V5",  "cba", "no mechanism that could make generation 2 differ in rep content"),
]

# The five block headings at their owners, plus the two umbrella headings --
# the umbrella phrase IS the absence-detector marker, so its presence is
# positively pinned exactly where it must exist (cba, cbb) and its absence
# asserted on the three untouched pack members below.
BLOCKS = [
    ("B1", "cba", "## CORRECTION V1 (2026-08-17)"),
    ("B2", "cba", "## CORRECTION V2 (2026-08-17)"),
    ("B3", "cba", "## CORRECTION V5 (2026-08-17)"),
    ("B4", "cbb", "## CORRECTION V3 (2026-08-17)"),
    ("B5", "cbb", "## CORRECTION V4 (2026-08-17)"),
    ("U1", "cba", "# CORRECTIONS V1, V2, V5 (2026-08-17, "
                  "applied from the SCUR-1 source-currency audit)"),
    ("U2", "cbb", "# CORRECTIONS V3, V4 (2026-08-17, "
                  "applied from the SCUR-1 source-currency audit)"),
]

# The struck spans, exactly as written (strike wraps the original bytes).
STRIKES = [
    ("S1", "cba", "~~SOURCE-CONTRADICTED-ON-VEV-INDUCED-EFFECTIVE-CHIRALITY~~"),
    ("S2", "cba", "~~the source's stated mechanism — VEV/low-curvature mass "
                  "decoupling into chiral sectors — **cannot work**. See §5.2~~"),
    ("S3", "cba", "~~the Lorentz-scalar components are exactly those with "
                  "**both** legs vertical:~~"),
    ("S4", "cba", "~~, with an exact shape constraint: the Higgs must consume "
                  "the vertical form leg. This is a tightening act of type (iii)~~"),
    ("S5", "cba", "~~GU has no mechanism that could make generation 2 differ "
                  "in rep content~~"),
    ("S6", "cba", "~~the Higgs must consume the vertical form leg (E2)~~"),
    ("S7", "cbb", "~~`Lambda^1(V_14)` gives `Lambda^1(V_4)` plus "
                  "**ten 4D scalars**~~"),
    ("S8", "cbb", "~~only by an unbuilt mirror-gapping condensate~~"),
]

# Dated bracket markers at the three non-strike loci.
BRACKETS = [
    ("K1", "cba", "[title clause CORRECTED 2026-08-17"),
    ("K2", "cba", "[scope re-set 2026-08-17 per CORRECTION V1"),
    ("K3", "cbb", "[2026-08-17: compute this on the corrected observation map"),
]

# Corrected content present (the replacement facts, not just the strikes).
CORRECTED = [
    ("C1", "cba", "and is **NOT excluded by this row**"),
    ("C2", "cba", "SG4 bit 2 (ST-1"),
    ("C3", "cbb", "SG4 bit 2 (ST-1"),
    ("C4", "cba", "exactly ONE 4D one-form"),
    ("C5", "cbb", "exactly ONE 4D one-form"),
    ("C6", "cba", "for representation theoretic reasons"),
]

# Verdict preservation: no verdict cell token moved.
VERDICTS = [
    ("P1", "cba", "| **OVER-DETERMINED** |"),
    ("P2", "cba", "**SAME** (conditionally on `U5` acting by multiplicity)"),
    ("P3", "cba", "| **NEEDS-U4**~~,"),
    ("P4", "cba", "canon_verdict_change: none"),
    ("P5", "cbb", "this leg: exactly-same as physics"),
    ("P6", "cbb", "DETERMINED GIVEN U2 AND U13"),
]

# Register-owner citations inside the appended sections (paths are long
# enough to satisfy the needle guard; SC-FER-03 pinned with context).
CITES = [
    ("R1", "cba", "seesaw-tradeoff/st1-tradeoff-dissolves-into-sg4-bit-2-2026-08-16.md"),
    ("R2", "cba", "carrier/crb-carrier-is-four-corners-not-one-weyl-2026-08-15.md"),
    ("R3", "cba", "four-d-mode-decomposition/md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md"),
    ("R4", "cba", "vz-repair/vz4-pullback-is-a-contraction-2026-08-15.md"),
    ("R5", "cba", "high-energy-two-plus-one/he1-imposter-separation-invariant-2026-08-14.md"),
    ("R6", "cba", "placement (SC-FER-03)"),
    ("R7", "cbb", "four-d-mode-decomposition/md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md"),
    ("R8", "cbb", "vz-repair/vz4-pullback-is-a-contraction-2026-08-15.md"),
    ("R9", "cbb", "seesaw-tradeoff/st1-tradeoff-dissolves-into-sg4-bit-2-2026-08-16.md"),
    ("R10", "cbb", "SC-FER-03; IV-20260815"),
    ("R11", "cbb", "subtractive 2+1 (HE-1)"),
]

# Cross-links and provenance anchors.
LINKS = [
    ("X1", "cba", "fixa-cb-corrections-applied-2026-08-17.md"),
    ("X2", "cbb", "fixa-cb-corrections-applied-2026-08-17.md"),
    ("X3", "fixa", "joe_directed_fixa_cb_corrections.py"),
    ("X4", "fixa", "GU-COMPARATOR-ROUTING"),
    ("X5", "fixa", "```gu-typed-objects"),
    ("X6", "fixa", "target_claim"),
    ("L1", "scur1", "## 7. Proposed diffs (NOT applied; owners named)"),
    ("L2", "scur1_probe", "the signal to retire or re-baseline this probe"),
    ("L3", "scur1_probe", "no mechanism that could make generation 2 differ"),
]

# Exact counts measured at application time (ground truth by grep, then
# pinned; never tuned to green a red).
EXPECT = {
    "cba_blocks": 3,
    "cbb_blocks": 2,
    "total_blocks": 5,
    "cba_pointers": 8,   # "at end of file" pointers at the corrected loci
    "cbb_pointers": 3,
    "cba_tilde_marks": 12,  # 6 struck spans x 2 delimiters
    "cbb_tilde_marks": 4,   # 2 struck spans x 2 delimiters
}


class Mutation:
    """Machinery-corruption switches; all default off (clean baseline)."""

    def __init__(self):
        self.wrong_file_b1 = False    # M1: search B1 in CB-E instead of CB-A
        self.missing_cba = False      # M2: point cba at a ghost path
        self.empty_needle = False     # M3: blank the S5 needle
        self.corrupt_counts = False   # M4: expect 4 total blocks, not 5
        self.invert_contrary = False  # M5: require the marker in CB-D
        self.blind_detector = False   # M6: absence detector always says "absent"


def read(path_key, checks, label, mut):
    """Guarded read; a missing file is a caught FAIL, never a crash."""
    rel = FILES.get(path_key, path_key)
    if mut.missing_cba and path_key == "cba":
        rel = CB + "/DOES-NOT-EXIST.md"
    full = os.path.join(REPO, rel)
    if not os.path.isfile(full):
        checks.append((label + " [file present: " + rel + "]", False))
        return None
    with open(full, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def contains(checks, label, path_key, needle, mut):
    if mut.empty_needle and label == "S5":
        needle = ""
    if mut.wrong_file_b1 and label == "B1":
        path_key = "cbe"
    if len(needle) < MIN_NEEDLE:
        checks.append((label + " [needle guard: quotation too short to be "
                       "non-vacuous]", False))
        return
    text = read(path_key, checks, label, mut)
    if text is None:
        return
    checks.append((label + " [" + needle[:48] + "... @ " + path_key + "]",
                   needle in text))


def detect_marker(text, mut):
    """The absence detector.  M6 blinds it; the planted-positive check is
    what catches a blinded detector (VERIFICATION.md rule 4)."""
    if mut.blind_detector:
        return False
    return MARKER in text


def run_checks(mut):
    checks = []

    for group in (BLOCKS, SCUR1_NEEDLES, STRIKES, BRACKETS, CORRECTED,
                  VERDICTS, CITES, LINKS):
        for label, pkey, needle in group:
            contains(checks, label, pkey, needle, mut)

    # -- NO-EXPANSION: untouched pack members carry no FIX-A marker ----------
    for pkey in ("cbc", "cbd", "cbe"):
        text = read(pkey, checks, "N(" + pkey + ")", mut)
        if text is None:
            continue
        fired = detect_marker(text, mut)
        if mut.invert_contrary and pkey == "cbd":
            checks.append(("N [contrary INVERTED: require FIX-A marker in "
                           "cbd]", fired))
        else:
            checks.append(("N [no FIX-A correction marker in " + pkey + "]",
                           not fired))

    # -- PLANTED POSITIVE: the absence detector must have power --------------
    checks.append(("PP [absence detector flags the planted synthetic "
                   "positive]", detect_marker(SYNTHETIC_POSITIVE, mut)))

    # -- COUNTS ---------------------------------------------------------------
    cba = read("cba", checks, "T(cba)", mut)
    cbb = read("cbb", checks, "T(cbb)", mut)
    if cba is not None and cbb is not None:
        n_cba = cba.count("## CORRECTION V")
        n_cbb = cbb.count("## CORRECTION V")
        want_total = 4 if mut.corrupt_counts else EXPECT["total_blocks"]
        checks.append(("T1 [CB-A correction blocks == " +
                       str(EXPECT["cba_blocks"]) + "; measured " + str(n_cba) +
                       "]", n_cba == EXPECT["cba_blocks"]))
        checks.append(("T2 [CB-B correction blocks == " +
                       str(EXPECT["cbb_blocks"]) + "; measured " + str(n_cbb) +
                       "]", n_cbb == EXPECT["cbb_blocks"]))
        checks.append(("T3 [total blocks == " + str(want_total) +
                       " (SCUR-1's five CB findings); measured " +
                       str(n_cba + n_cbb) + "]",
                       n_cba + n_cbb == want_total))
        p_cba = cba.count("at end of file")
        p_cbb = cbb.count("at end of file")
        checks.append(("T4 [CB-A locus pointers == " +
                       str(EXPECT["cba_pointers"]) + "; measured " +
                       str(p_cba) + "]", p_cba == EXPECT["cba_pointers"]))
        checks.append(("T5 [CB-B locus pointers == " +
                       str(EXPECT["cbb_pointers"]) + "; measured " +
                       str(p_cbb) + "]", p_cbb == EXPECT["cbb_pointers"]))
        t_cba = cba.count("~~")
        t_cbb = cbb.count("~~")
        checks.append(("T6 [CB-A strike delimiters == " +
                       str(EXPECT["cba_tilde_marks"]) + " (6 spans), even; "
                       "measured " + str(t_cba) + "]",
                       t_cba == EXPECT["cba_tilde_marks"] and t_cba % 2 == 0))
        checks.append(("T7 [CB-B strike delimiters == " +
                       str(EXPECT["cbb_tilde_marks"]) + " (2 spans), even; "
                       "measured " + str(t_cbb) + "]",
                       t_cbb == EXPECT["cbb_tilde_marks"] and t_cbb % 2 == 0))

    return checks


def report(checks, verbose=True):
    passed = sum(1 for _, ok in checks if ok)
    total = len(checks)
    if verbose:
        for label, ok in checks:
            print(("[OK]   " if ok else "[FAIL] ") + label)
    print(str(passed) + "/" + str(total) + " checks" +
          ("" if passed == total else "  <-- RED"))
    return passed == total


def selftest():
    print("== SELFTEST: clean baseline FIRST ==")
    baseline = run_checks(Mutation())
    if not report(baseline, verbose=False):
        print("SELFTEST ABORTED: clean baseline is RED; a selftest run on a "
              "red baseline proves nothing.")
        for label, ok in baseline:
            if not ok:
                print("  baseline [FAIL] " + label)
        return 1
    print("baseline green; applying 6 machinery-corruption mutations\n")

    mutations = [
        ("M1 wrong-file redirect (B1 searched in CB-E)", "wrong_file_b1"),
        ("M2 missing-file path (cba pointed at a ghost file)", "missing_cba"),
        ("M3 empty needle (S5 blanked; guard must fire)", "empty_needle"),
        ("M4 count corruption (expect 4 blocks, not 5)", "corrupt_counts"),
        ("M5 contrary-control inversion (require FIX-A marker in CB-D)",
         "invert_contrary"),
        ("M6 blinded absence detector (planted positive must catch it)",
         "blind_detector"),
    ]
    caught = 0
    for name, attr in mutations:
        mut = Mutation()
        setattr(mut, attr, True)
        try:
            checks = run_checks(mut)
        except Exception as exc:  # crash-catch is REJECTED, not a catch
            print("[REJECTED] " + name + " crashed (" +
                  type(exc).__name__ + "): a crash is not a caught failure")
            continue
        fails = [label for label, ok in checks if not ok]
        if fails:
            caught += 1
            print("[CAUGHT]   " + name + " -> " + str(len(fails)) +
                  " genuine [FAIL], first: " + fails[0][:100])
        else:
            print("[MISSED]   " + name + " -> mutation produced no [FAIL]")
    print("\n" + str(caught) + "/6 mutations caught")
    if caught == 6:
        print("SELFTEST PASSED")
        return 0
    print("SELFTEST FAILED")
    return 1


def main():
    if REPO is None:
        print("[FAIL] repo root not found (CANON.md not located above this "
              "file); run from the gu-formalization checkout")
        return 1
    if "--selftest" in sys.argv or "--self-test" in sys.argv:
        return selftest()
    checks = run_checks(Mutation())
    ok = report(checks)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
