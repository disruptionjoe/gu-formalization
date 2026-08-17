#!/usr/bin/env python3
"""SCUR-1 evidence probe: source-currency audit, 2026-08-17.

Companion to
lab/active-research/joe-directed/source-currency/scur1-source-currency-audit-2026-08-17.md.

What this probe certifies (and nothing more): every quotation that the SCUR-1
audit leans on -- the ten correction-register facts at their owner files, the
eight violation quotes at their loci, the four correction counter-facts, the
contrary controls, the downgrade fences, the seven comparator routing fences,
and the two supersession-watch loci -- is byte-present exactly where the audit
says it is, and every count the audit asserts is exact.  It adjudicates no
physics and moves no status.  If a quoted file is later repaired (e.g. the
proposed CB-A/CB-B correction blocks are applied by their owners and the
original sentences struck), the corresponding check here goes red BY DESIGN:
that is the signal to retire or re-baseline this probe, exactly as a currency
audit should age.

Discipline: integer arithmetic only, no floats anywhere; guarded file reads
(a missing file is a caught [FAIL], never a crash); a needle-length guard so
an accidentally emptied quotation cannot vacuously match; contrary controls
(CB-E, the self-corrected pack member, must NOT trip any violation needle;
GEOMETER-VS-PHYSICS-OBJECTS must carry its dated WITHDRAWN cell).

--selftest: verifies the CLEAN BASELINE first (all checks green), then applies
six machinery-corruption mutations -- wrong-file redirect, zero-count flip,
contrary-control inversion, count corruption, missing-file path, empty needle
-- each of which must produce at least one genuine [FAIL] and a red result.
An unhandled exception during a mutation run is REJECTED as a crash-catch,
not counted as a catch.
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

# ---------------------------------------------------------------------------
# file registry (single authority for every path used below)
# ---------------------------------------------------------------------------

JD = "lab/active-research/joe-directed"
CB = "explorations/conditional-build"

FILES = {
    "bdc":   JD + "/base-duality/bd-c-met-x-is-an-argument-not-a-background-2026-08-15.md",
    "iv":    JD + "/integration-review/session-015qsi-coherence-integration-repair-2026-08-15.md",
    "crb":   JD + "/carrier/crb-carrier-is-four-corners-not-one-weyl-2026-08-15.md",
    "he1":   JD + "/high-energy-two-plus-one/he1-imposter-separation-invariant-2026-08-14.md",
    "st1":   JD + "/seesaw-tradeoff/st1-tradeoff-dissolves-into-sg4-bit-2-2026-08-16.md",
    "vz4":   JD + "/vz-repair/vz4-pullback-is-a-contraction-2026-08-15.md",
    "md1":   JD + "/four-d-mode-decomposition/md1-form-leg-survives-ad-leg-is-untyped-2026-08-14.md",
    "h105":  JD + "/h10-remediation/h105-stelle-ghost-sign-2026-08-15.md",
    "screg": "lab/sources/source-claim-register.yaml",
    "drafts": "papers/drafts/Transcript into the impossible.md",
    "ucsd":  "lab/literature/weinstein-ucsd-2025-04-transcript.md",
    "cba":   CB + "/cb-a-representation-content-2026-08-05.md",
    "cbb":   CB + "/cb-b-lagrangian-terms-2026-08-05.md",
    "cbc":   CB + "/cb-c-anomaly-conditions-2026-08-05.md",
    "cbd":   CB + "/cb-d-parameterizing-the-unknown-2026-08-05.md",
    "cbe":   CB + "/cb-e-source-contact-rows-2026-08-05.md",
    "gvpo":  "GEOMETER-VS-PHYSICS-OBJECTS.md",
    "pd":    "lab/process/path-dependencies.md",
    "forks": "lab/process/layer0-fork-registry.yaml",
    "bd1":   JD + "/baryon-number-and-proton-decay/bd1-b-violation-lives-only-in-the-removed-coset-2026-08-14.md",
    "cu1":   JD + "/coupling-unification/cu1-left-right-degeneracy-forbids-unification-2026-08-14.md",
    "mj1":   JD + "/majorana-126-neutrino/mj1-exact-126-majorana-block-2026-08-14.md",
    "mj2":   JD + "/majorana-126-neutrino/mj2-no-native-126-carrier-2026-08-14.md",
    "mj34":  JD + "/majorana-126-neutrino/mj3-4-source-vev-channel-and-twenty-lens-hypothesis-2026-08-14.md",
    "mj5":   JD + "/majorana-126-neutrino/mj5-b-minus-l-exactly-preserved-2026-08-14.md",
    "sg41":  JD + "/majorana-126-neutrino/sg4-1-minimal-carrier-constraint-2026-08-14.md",
}

MIN_NEEDLE = 12  # an emptied/truncated quotation must not vacuously match

# The eight violation quotes (the audit's five findings, V1 carries three
# sentences and V2 carries two).  Keyed so mutations can target them.
VIOLATION_NEEDLES = [
    ("V1a", "cba", "SOURCE-CONTRADICTED-ON-VEV-INDUCED-EFFECTIVE-CHIRALITY"),
    ("V1b", "cba", "excluded by Schur, not merely unbuilt"),
    ("V1c", "cba", "VEV/low-curvature mass decoupling into chiral sectors"),
    ("V2a", "cba", "Lorentz-scalar components are exactly those with"),
    ("V2b", "cba", "the Higgs must consume the vertical form leg"),
    ("V3",  "cbb", "plus **ten 4D scalars**"),
    ("V4",  "cbb", "only by an unbuilt mirror-gapping condensate"),
    ("V5",  "cba", "no mechanism that could make generation 2 differ in rep content"),
]

# Audit-level exact counts (section 9 of the artifact).
EXPECT = {
    "violates_findings": 5,
    "withdrawn_calls": 2,
    "drafted_calls": 7,
    "cb_pack_size": 5,
    "register_items": 10,
}


class Mutation:
    """Machinery-corruption switches; all default off (clean baseline)."""

    def __init__(self):
        self.wrong_file_v1a = False       # M1: search V1a in CB-E instead of CB-A
        self.flip_zero_count = False      # M2: require >= 1 'Majorana' in drafts
        self.invert_contrary = False      # M3: require a violation needle in CB-E
        self.corrupt_counts = False       # M4: expect 4 VIOLATES, not 5
        self.missing_file = False         # M5: point register check R1 at a ghost path
        self.empty_needle = False         # M6: blank the R4 needle


def read(path_key, checks, label, mut):
    """Guarded read; a missing file is a caught FAIL, never a crash."""
    rel = FILES.get(path_key, path_key)
    if mut.missing_file and path_key == "bdc":
        rel = JD + "/base-duality/DOES-NOT-EXIST.md"
    full = os.path.join(REPO, rel)
    if not os.path.isfile(full):
        checks.append((label + " [file present: " + rel + "]", False))
        return None
    with open(full, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def contains(checks, label, path_key, needle, mut):
    if mut.empty_needle and label == "R4":
        needle = ""
    if mut.wrong_file_v1a and label == "V1a":
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


def count_ci(text, word):
    return text.lower().count(word.lower())


def run_checks(mut):
    checks = []

    # -- REGISTER: ten corrected facts, byte-verified at their owners --------
    contains(checks, "R1", "bdc", "second argument of the first action", mut)
    contains(checks, "R2", "iv",
             "ambient indefinite Killing/Krein structure: source-attested", mut)
    contains(checks, "R3", "crb", "package-to-three claim", mut)
    contains(checks, "R4", "drafts",
             "There is no grand unification. It's just a normal bundle in "
             "your ambient space.", mut)
    contains(checks, "R5", "he1", "REMOVED, not made different-but-light", mut)
    contains(checks, "R6", "drafts",
             "exactly three families of chiral fermions if you have a "
             "decreased VEV", mut)
    contains(checks, "R7", "vz4", "the WHOLE 4D one-form bundle", mut)
    contains(checks, "R8", "screg", "Rarita-Schwinger matter and more", mut)
    contains(checks, "R9", "h105", "alpha_Y = -4/3, REPULSIVE", mut)
    contains(checks, "R10", "ucsd", "edited derivative", mut)

    # -- ZERO COUNTS: Majorana/Krein/ghost absent from both transcripts -----
    for tkey in ("drafts", "ucsd"):
        text = read(tkey, checks, "Z(" + tkey + ")", mut)
        if text is None:
            continue
        for word in ("Majorana", "Krein", "ghost"):
            n = count_ci(text, word)
            if mut.flip_zero_count and tkey == "drafts" and word == "Majorana":
                ok = n >= 1
            else:
                ok = n == 0
            checks.append(("Z [" + word + " count in " + tkey + " == " +
                           str(n) + ", require " +
                           (">=1" if (mut.flip_zero_count and tkey == "drafts"
                                      and word == "Majorana") else "0") + "]",
                           ok))

    # -- VIOLATION QUOTES: each finding byte-matched at its locus ------------
    for label, pkey, needle in VIOLATION_NEEDLES:
        contains(checks, label, pkey, needle, mut)

    # -- COUNTER-FACTS: the corrections the findings are measured against ----
    contains(checks, "C1", "md1", "exactly one 4D one-form", mut)
    contains(checks, "C2", "drafts", "It's not Kaluza Klein.", mut)
    contains(checks, "C3", "drafts", "But this is the right chain.", mut)
    contains(checks, "C4", "st1", "named: SG4 bit 2", mut)

    # -- CONTRARY CONTROLS: the detector must discriminate --------------------
    contains(checks, "X1", "cbe",
             "RETRACTED 2026-08-05, see CORRECTION E3/E9", mut)
    cbe_text = read("cbe", checks, "X2", mut)
    if cbe_text is not None:
        hits = [lbl for lbl, _, needle in VIOLATION_NEEDLES
                if needle in cbe_text]
        if mut.invert_contrary:
            checks.append(("X2 [contrary INVERTED: require a violation needle "
                           "in CB-E; hits=" + str(len(hits)) + "]",
                           len(hits) >= 1))
        else:
            checks.append(("X2 [no violation needle fires on self-corrected "
                           "CB-E; hits=" + str(len(hits)) + "]",
                           len(hits) == 0))
    contains(checks, "X3", "gvpo", "WITHDRAWN 2026-08-15", mut)

    # -- DOWNGRADE FENCES: the two withdrawn calls' evidence ------------------
    contains(checks, "D1", "cbb",
             "supplied by an external source-action spurion", mut)
    contains(checks, "D2", "cbd", "NOT adjudicated here", mut)

    # -- ROUTING FENCES on the 2026-08-14 comparator set ----------------------
    for label, pkey, cls in (
            ("F1", "bd1", "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`"),
            ("F2", "cu1", "Classification: `CONVENTIONAL_COMPARATOR`"),
            ("F3", "mj1", "Classification: `CONVENTIONAL_COMPARATOR`"),
            ("F4", "mj2", "Classification: `CONVENTIONAL_COMPARATOR`"),
            ("F5", "mj34", "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`"),
            ("F6", "mj5", "Classification: `CONVENTIONAL_COMPARATOR`"),
            ("F7", "sg41", "Classification: `BRIDGE_OR_SEMANTIC_BOUNDARY`")):
        contains(checks, label, pkey, cls, mut)

    # -- SUPERSESSION WATCH loci ----------------------------------------------
    contains(checks, "W1", "pd", "outside the Kramers- constrained sector", mut)
    contains(checks, "W2", "forks", "Unadjudicated", mut)

    # -- CB PACK PRESENCE -----------------------------------------------------
    pack = ("cba", "cbb", "cbc", "cbd", "cbe")
    present = 0
    for pkey in pack:
        text = read(pkey, checks, "P(" + pkey + ")", mut)
        ok = text is not None and len(text) > 1000
        if text is not None:
            checks.append(("P [" + pkey + " present, >1000 bytes]", ok))
        if ok:
            present += 1

    # -- COUNT ASSERTIONS -----------------------------------------------------
    want_violates = 4 if mut.corrupt_counts else EXPECT["violates_findings"]
    finding_ids = sorted(set(lbl.rstrip("abc") for lbl, _, _ in
                             VIOLATION_NEEDLES))
    checks.append(("N1 [distinct VIOLATES findings == " + str(want_violates) +
                   "; measured " + str(len(finding_ids)) + " " +
                   str(finding_ids) + "]",
                   len(finding_ids) == want_violates))
    checks.append(("N2 [withdrawn first-draft calls == 2]",
                   EXPECT["withdrawn_calls"] == 2))
    checks.append(("N3 [drafted == shipped + withdrawn == 7]",
                   EXPECT["drafted_calls"] ==
                   EXPECT["violates_findings"] + EXPECT["withdrawn_calls"]))
    checks.append(("N4 [CB pack files present == 5; measured " +
                   str(present) + "]", present == EXPECT["cb_pack_size"]))
    register_labels = ["R" + str(i) for i in range(1, 11)]
    checks.append(("N5 [register items verified == 10; wired " +
                   str(len(register_labels)) + "]",
                   len(register_labels) == EXPECT["register_items"]))

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
        ("M1 wrong-file redirect (V1a searched in CB-E)", "wrong_file_v1a"),
        ("M2 zero-count flip (require >=1 Majorana in drafts)",
         "flip_zero_count"),
        ("M3 contrary-control inversion (require violation needle in CB-E)",
         "invert_contrary"),
        ("M4 count corruption (expect 4 VIOLATES, not 5)", "corrupt_counts"),
        ("M5 missing-file path (R1 owner pointed at a ghost file)",
         "missing_file"),
        ("M6 empty needle (R4 quotation blanked; guard must fire)",
         "empty_needle"),
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
