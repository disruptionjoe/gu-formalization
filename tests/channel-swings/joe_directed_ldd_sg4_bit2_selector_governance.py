#!/usr/bin/env python3
"""LD-D probe: governance of SG4 bit 2, the selector the joe-directed tree routes to.

Certifies, against byte-verified owner text and exact counts, the five
SYSTEMS/PROTOCOL cards of ldd-sg4-bit2-selector-governance-2026-08-17.md:

  13. APPLIED-STATE.  SG-1's proposed README diff is now applied.  The applied
      text is not hardcoded here: it is EXTRACTED from SG-1's own fenced
      ```diff block and compared byte-for-byte against
      lab/active-research/joe-directed/README.md, so the check certifies
      fidelity to the proposal rather than agreement with this file's author.
      The removed sentence is absent; the surrounding context is unmoved.

  14. THE COUNT.  Rows carrying the bit-2 condition family (the repository's
      own Grant-poset node G6, byte-pinned from lab/methods/gu-base-categories.md)
      are EXACTLY THREE: LT-GR2d, RA-G3, AC-F1 -- not "a dozen".  And the
      decisive fact: over all 87 ledger rows, the number whose revival_trigger
      is discharged by a bit-2 resolution ALONE is ZERO, computed by an explicit
      head-demand evaluator, with three planted-positive controls that the SAME
      evaluator must flag (an absence result cannot be certified by a detector
      whose power is untested).

  19. FALLBACK TYPING EXISTS.  EXTERNAL_DATUM, PROVEN_UNSUPPLYABLE and
      SOURCE_DECLARED_OPEN__NO_MECHANISM_SUPPLIED are all live NEEDS kinds in
      the v0.259 taxonomy, the last one with a pinned non-discharge rule.  The
      contingency SHAPE (owner + activation + next_check) exists in
      lab/process/upgrade-program-register.yaml with an IV-class activation
      already in use.

  20. NO ELEVATED BAR -- ABSENCE, WITH A PLANTED CONTROL.  The Layer-0 fork
      registry carries exactly 13 forks and NONE of them is the chirality /
      SG4-bit-2 fork; the fork-depth gate's REQUIRED_FORK_IDS pins six ids and
      none is bit-2 related.  A synthetic registry carrying `- id: SG4-BIT-2`
      must be detected by the same scanner.  SA-1's dated entry-gap sentence is
      pinned as the precedent.

  15. RECONCILIATION VOCABULARY.  The OVER_DETERMINED escalation machinery
      (six live entries, four allowed dispositions each) exists; the two sides
      that could disagree are pinned at their loci -- SC-CHI-01's source-side
      hedge in the claim register, ST-1's "Owned by Lane 1 (the action/BFV
      lane)" on the action side.

Selftest (--selftest): the CLEAN BASELINE is verified FIRST and the selftest
aborts red rather than banking mutations against a red baseline; then seven
corruptions of MACHINERY or REFERENCES (never of a check's predicate), each
required to produce a genuine [FAIL] line AND a red exit.  A nonzero exit with
no [FAIL] line is CRASH-NOT-DETECTION and fails the selftest.  Mutation W is a
deliberately-wrong VERDICT table ("a dozen rows"; "the registry already covers
bit 2") which the same evaluators must reject.  Selftest exits 0 on success.

Run from the repository root:
  _local/cas-venv/bin/python tests/channel-swings/joe_directed_ldd_sg4_bit2_selector_governance.py
  _local/cas-venv/bin/python tests/channel-swings/joe_directed_ldd_sg4_bit2_selector_governance.py --selftest

This probe reads files as data.  It moves no claim, verdict, grade, priority or
public posture, and it is not evidence for any physics statement.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MUT = os.environ.get("LDD_MUTATION", "")

# ------------------------------------------------------------------ machinery
FILES = {
    "readme": "lab/active-research/joe-directed/README.md",
    "sg1": "lab/active-research/joe-directed/sg4-axis/"
           "sg1-c6a-scope-narrowing-2026-08-16.md",
    "ledger": "lab/process/conditional-physics-ledger-v0.259.json",
    "basecat": "lab/methods/gu-base-categories.md",
    "forkreg": "lab/process/layer0-fork-registry.yaml",
    "forkgate": "process_gates/fork_depth_audit.py",
    "upgreg": "lab/process/upgrade-program-register.yaml",
    "sa1": "lab/active-research/joe-directed/soldered-ad/"
           "sa1-the-selector-is-built-and-the-bundle-horn-is-soldered-2026-08-16.md",
    "pcx1": "lab/active-research/joe-directed/parity-crosscheck/"
            "pcx1-signature-parity-clause-does-not-fire-2026-08-17.md",
    "screg": "lab/sources/source-claim-register.yaml",
    "st1": "lab/active-research/joe-directed/seesaw-tradeoff/"
           "st1-tradeoff-dissolves-into-sg4-bit-2-2026-08-16.md",
    "verif": "VERIFICATION.md",
}

# The verdicts this probe certifies.  Mutation W replaces this table wholesale.
VERDICTS = {
    "g6_rows": ("LT-GR2d", "RA-G3", "AC-F1"),   # item 14: the exact count is 3
    "bit2_alone_dischargeable": 0,              # item 14: nothing fires on the bit
    "n_rows": 87,
    "n_forks": 13,                              # item 20
    "n_required_fork_ids": 6,
    "bit2_fork_registered": False,              # item 20: the absence
    "n_over_determined_escalations": 6,         # item 15
    "n_external_datum_rows": 2,                 # item 19
}

# item-14 evaluator vocabulary (machinery -- mutation M4 corrupts it)
CONNECTIVES = (" with ", " plus ", " and ", " paired ", " containing ", " for ",
               " inserted ", " not ", " under ", " selecting ", " from ", " on ",
               " to ", " changing ", " removing ", " that ", " whose ", ", ", ";")
PHASE_VOCAB = {"phase", "vacuum", "vev", "bit", "expectation", "value", "values",
               "selection", "varpi", "decoupling", "chirality", "chiral", "split", "2"}
STOP = {"a", "an", "the", "of", "in", "its", "is", "are", "resolved", "selected",
        "source", "native", "sg4", "sc-chi-01", "this", "it", "be", "been"}

# item-20 scanner vocabulary (machinery -- mutation M6 corrupts it)
BIT2_FORK_PATTERNS = ("BIT-2", "BIT2", "CHIRAL", "CHI-", "SG4", "S-FULL-DIRAC",
                      "S-HALF", "VEV-PHASE")

if MUT == "M1":     # machinery: path-table redirect
    FILES["readme"] = "lab/active-research/joe-directed/README.DOES-NOT-EXIST.md"
if MUT == "M2":     # reference substitution: wrong methods file
    FILES["basecat"] = "VERIFICATION.md"
if MUT == "M3":     # reference substitution: stale ledger version
    FILES["ledger"] = "lab/process/conditional-physics-ledger-v0.258.json"
if MUT == "M4":     # reference: LOOSEN the phase vocabulary so constructions
                    # (a stationary point, an index, a carrier) read as phase objects
    PHASE_VOCAB = PHASE_VOCAB | {"stationary", "index", "carrier", "physical",
                                 "odd-form", "located", "126", "channel"}
if MUT == "M8":     # machinery: blind the head-demand detector entirely
    PHASE_VOCAB = set()
if MUT == "M5":     # machinery: diff extractor takes the wrong hunk side
    pass            # handled at the extraction site
if MUT == "M6":     # machinery: blind the fork-id scanner
    BIT2_FORK_PATTERNS = ("ZZZ-NEVER-MATCHES",)
if MUT == "M7":     # machinery: fork-id regex corrupted
    pass            # handled at the extraction site
if MUT == "W":      # DELIBERATELY WRONG VERDICT TABLE
    VERDICTS = dict(VERDICTS,
                    g6_rows=("LT-GR2d", "RA-G3", "AC-F1", "RA-D2", "RA-D4",
                             "AC-A1", "RA-A1", "RA-A2", "RA-A4", "RA-A8",
                             "RA-E1", "RA-E6"),          # "a dozen"
                    bit2_alone_dischargeable=12,
                    bit2_fork_registered=True)           # "already covered"

FAIL: list[str] = []
N = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global N
    N += 1
    if not ok:
        FAIL.append(label)
        print(f"[FAIL] {label}" + (f"  -- {detail}" if detail else ""))


def read(key: str) -> str:
    """Read an evidence file.  A missing file is a genuine [FAIL], never a crash:
    a traceback exits nonzero without a failing check, which VERIFICATION.md
    rule 3 classifies as CRASH-NOT-DETECTION."""
    p = ROOT / FILES[key]
    ok = p.is_file()
    check(f"F.{key} evidence file resolves: {FILES[key]}", ok)
    return p.read_text(encoding="utf-8") if ok else ""


# ------------------------------------------------------- item-14 evaluator
def head_demand(trigger: str) -> str:
    """The object a revival trigger demands, before its first extra-demand clause."""
    low = trigger.lower()
    cut = len(low)
    for c in CONNECTIVES:
        i = low.find(c)
        if i != -1:
            cut = min(cut, i)
    return low[:cut]


def bit2_alone_dischargeable(trigger: str) -> bool:
    """True iff 'SG4 bit 2 is resolved' ALONE exhibits everything the trigger demands.

    Machine test: every content word of the head demand lies in the closed
    phase-object vocabulary.  One word naming any other object (a theorem, a
    carrier, an index, a stationary point) is an extra demand the bit does not
    supply.
    """
    words = re.findall(r"[a-z0-9\-']+", head_demand(trigger))
    content = [w for w in words if w not in STOP]
    return bool(content) and all(w in PHASE_VOCAB for w in content)


# ------------------------------------------------------------------ the run
def run() -> int:
    print("LD-D -- SG4 bit 2 selector governance (items 13/14/15/19/20)")
    print("=" * 72)

    # ---------- A. ITEM 13: the applied state, verified against SG-1's own diff
    sg1 = read("sg1")
    readme = read("readme")

    anchor = "Proposed diff, owner's call, **not applied**:"
    check("A1 SG-1 carries exactly one proposed-diff anchor", sg1.count(anchor) == 1)
    minus = plus = ""
    if anchor in sg1:
        blk = sg1[sg1.index(anchor):sg1.index(anchor) + 900]
        j = blk.index("```diff")
        k = blk.index("```", j + 7)
        hunk = blk[j + 8:k]
        minus = "\n".join(l[1:] for l in hunk.splitlines() if l.startswith("-"))
        plus = "\n".join(l[1:] for l in hunk.splitlines() if l.startswith("+"))
        if MUT == "M5":                 # machinery: swap the hunk sides
            minus, plus = plus, minus
    check("A2 the extracted hunk has both sides", bool(minus) and bool(plus))
    check("A3 the REMOVED sentence is gone from the README",
          bool(minus) and minus not in readme,
          f"still present {readme.count(minus) if minus else 'no hunk'}")
    check("A4 the PROPOSED replacement is present exactly once",
          bool(plus) and readme.count(plus) == 1,
          f"count={readme.count(plus) if plus else 'no hunk'}")
    check("A5 the applied text byte-equals SG-1's proposal (no improvisation)",
          bool(plus) and plus in readme and plus == plus.strip())

    lines = readme.splitlines()
    check("A6 the hunk sits at the line-74 anchor",
          len(lines) > 80 and
          lines[73].startswith("the fork**. Note which selector answers which layer:"),
          repr(lines[73][:60]) if len(lines) > 73 else "README unreadable")
    check("A7 the preceding context line is unmoved",
          len(lines) > 80 and lines[72] ==
          "assignment must name which of the three it uses; **this tree does not resolve")
    check("A8 the following context is unmoved",
          len(lines) > 80 and
          lines[79] == "Two further ceilings recur and should be read with every file:",
          repr(lines[79][:60]) if len(lines) > 79 else "README unreadable")
    check("A9 SG-1's circularity ground is still stated at its locus",
          "A condition that presupposes one value of a fork cannot be the" in sg1
          and "selector **between** that fork's values." in sg1)

    # ---------- B. ITEM 14: the exact count, and the herd that cannot stampede
    basecat = read("basecat")
    g6_pin = ("In v0.259 this set occurs on the DEMAND side: NEEDS rows blocked "
              "on the vacuum/phase selection (LT-GR2d, RA-G3, AC-F1)")
    check("B1 the repo's own G6 grant node names the bit-2 rows verbatim",
          basecat.count(g6_pin) == 1)
    check("B2 the phase-bit identification is pinned at L4",
          "phase membership is SG4 bit 2 (chiral/unbroken vs massive/super-Higgs)"
          in basecat)

    ledger = json.loads(read("ledger"))
    rows = ledger["rows"]
    by_id = {r["id"]: r for r in rows}
    check("B3 the ledger has the expected row count",
          len(rows) == VERDICTS["n_rows"], f"n={len(rows)}")

    g6 = tuple(re.search(r"selection \(([^)]*)\)", g6_pin).group(1).split(", "))
    check("B4 the G6 row set extracted from the pin matches the verdict",
          g6 == VERDICTS["g6_rows"], f"pin={g6} verdict={VERDICTS['g6_rows']}")
    check("B5 the bit-2 condition family is THREE rows, not a dozen",
          len(g6) == 3, f"len={len(g6)}")
    for rid in g6:
        check(f"B6.{rid} exists in v0.259 and is a live NEEDS row",
              rid in by_id and by_id[rid]["verdict"] == "NEEDS")

    flagged = [r["id"] for r in rows if bit2_alone_dischargeable(r["revival_trigger"])]
    check("B7 NO ledger row is discharged by a bit-2 resolution alone",
          len(flagged) == VERDICTS["bit2_alone_dischargeable"],
          f"flagged={len(flagged)} {flagged[:6]} expected={VERDICTS['bit2_alone_dischargeable']}")

    # planted-positive controls: the detector's power, demonstrated
    controls = ["the selected varpi VEV phase",
                "a resolved SG4 bit 2",
                "the decoupling phase selection"]
    for c in controls:
        check(f"B8 planted control fires: {c!r}", bit2_alone_dischargeable(c))
    # planted negatives drawn from the three real G6 triggers
    for rid in ("LT-GR2d", "RA-G3", "AC-F1"):
        if rid in by_id:
            check(f"B9.{rid} its real trigger demands a construction, not the bit",
                  not bit2_alone_dischargeable(by_id[rid]["revival_trigger"]),
                  by_id[rid]["revival_trigger"][:70])

    check("B10 the two condition families are recorded as INCOMPARABLE (no silent merge)",
          "no ledger record identifies the two condition families. They are kept "
          "incomparable here" in basecat)

    # ---------- C. ITEM 19: the fallback typing already exists
    needs = ledger["taxonomy"]["verdict_kinds"]["NEEDS"]
    for kind in ("EXTERNAL_DATUM", "PROVEN_UNSUPPLYABLE",
                 "SOURCE_DECLARED_OPEN__NO_MECHANISM_SUPPLIED"):
        check(f"C1.{kind} is a live NEEDS reason kind", kind in needs)
    ext = [r["id"] for r in rows if r["reason_kind"] == "EXTERNAL_DATUM"]
    check("C2 EXTERNAL_DATUM is in live use", len(ext) == VERDICTS["n_external_datum_rows"],
          f"{ext}")
    exts = ledger.get("taxonomy_extensions") or []
    ndr = [e for e in exts if e.get("new_kind") ==
           "SOURCE_DECLARED_OPEN__NO_MECHANISM_SUPPLIED"]
    check("C3 the source-silent kind carries a non-discharge rule", bool(ndr) and
          "is NOT discharged, softened, deferred or excused" in ndr[0]["non_discharge_rule"])
    check("C4 forced-fit into an existing kind is forbidden by the taxonomy",
          ledger["taxonomy"]["unknown_kind_rule"] ==
          "NEW_KIND_REQUIRED__FORCED_FIT_FORBIDDEN")

    upgreg = read("upgreg")
    check("C5 the contingency register's closed status vocabulary is pinned",
          "status_vocabulary: [QUEUED, ACTIVE, DONE, DECLINED]" in upgreg)
    check("C6 an IV-class activation is already an accepted trigger shape",
          "activation: any independent review pass (IV-class)" in upgreg)
    for key in ("id:", "title:", "origin:", "owner:", "status:", "activation:",
                "next_check:"):
        check(f"C7 register schema key present: {key}", key in upgreg)

    # ---------- D. ITEM 20: the elevated bar -- an ABSENCE, with a control
    forkreg = read("forkreg")
    fork_re = r"^  - id: (\S+)" if MUT != "M7" else r"^  - ID: (\S+)"
    fork_ids = re.findall(fork_re, forkreg, re.M)
    check("D1 the Layer-0 fork registry carries the expected fork count",
          len(fork_ids) == VERDICTS["n_forks"], f"n={len(fork_ids)} {fork_ids}")

    def looks_bit2(fid: str) -> bool:
        up = fid.upper()
        return any(p in up for p in BIT2_FORK_PATTERNS)

    registered = [f for f in fork_ids if looks_bit2(f)]
    check("D2 NO registered Layer-0 fork is the chirality / SG4-bit-2 fork",
          bool(registered) == VERDICTS["bit2_fork_registered"],
          f"matched={registered} expected_registered={VERDICTS['bit2_fork_registered']}")
    # planted-positive control: the scanner must find a synthetic entry
    synth = forkreg + "\n  - id: SG4-BIT-2\n"
    synth_ids = re.findall(r"^  - id: (\S+)", synth, re.M)
    check("D3 planted control -- the scanner DOES find a synthetic SG4-BIT-2 row",
          any(f.upper().find("BIT-2") != -1 for f in synth_ids))
    check("D4 planted control -- the LIVE scanner vocabulary matches it "
          "(an absence result needs a detector with demonstrated power)",
          looks_bit2("SG4-BIT-2") and looks_bit2("S-CHIRALITY-CONTENT"),
          "scanner has no power; the D2 absence certifies nothing")

    forkgate = read("forkgate")
    req_blk = forkgate[forkgate.index("REQUIRED_FORK_IDS = frozenset({"):]
    req = re.findall(r'"([A-Z0-9\-]+)"', req_blk[:req_blk.index("})")])
    check("D5 REQUIRED_FORK_IDS pins the expected number of ids",
          len(req) == VERDICTS["n_required_fork_ids"], f"{req}")
    check("D6 none of the pinned required ids is the bit-2 selector",
          bool(req) and not any(looks_bit2(r) for r in req))
    check("D7 the fork-stack threshold is pinned at 3", "fork_stack_threshold: 3" in forkreg)
    check("D8 SA-1's dated entry-gap precedent is pinned",
          "registry was built to catch, and the fork was never entered in it."
          in read("sa1"))
    check("D9 the IV-class review pass is a named, dated precedent",
          "caught in independent review IV-20260815.)" in read("verif"))
    check("D10 PCX-1's armed-condition pattern exists as a reusable shape",
          "**FIRING CONDITION (armed, typed).** The clause fires the day a receipt"
          in read("pcx1"))

    # ---------- E. ITEM 15: the reconciliation vocabulary that already exists
    esc = ledger["over_determined_escalations"]
    check("E1 the OVER_DETERMINED escalation surface is populated",
          len(esc) == VERDICTS["n_over_determined_escalations"], f"n={len(esc)}")
    allowed = {"GENUINE_FALSIFICATION", "FORK_ARTIFACT", "SCOPE_ERROR", "STALE_PREMISE"}
    check("E2 every escalation carries the same four allowed dispositions",
          all(set(e["allowed_dispositions"]) == allowed for e in esc))
    check("E3 every escalation names an owner",
          all(e.get("owner") for e in esc))
    check("E4 the source side of the selector is pinned at its register locus",
          "Conditioned in the same passage on no VEV 'pulling the various "
          "sub-fields of varpi to values" in read("screg"))
    check("E5 the action side of the selector is pinned to Lane 1",
          "Owned by Lane 1 (the action/BFV lane). Not decided here, by design."
          in read("st1"))

    # ------------------------------------------------------------ certificate
    print("=" * 72)
    if FAIL:
        print(f"{N - len(FAIL)}/{N} checks pass -- {len(FAIL)} FAILED")
        for f in FAIL:
            print(f"   [FAIL] {f}")
        return 1
    print(f"{N}/{N} checks pass -- exit 0")
    print()
    print("  ITEM 13  applied: README:74 now carries SG-1's proposed text, byte-exact")
    print(f"  ITEM 14  bit-2 condition family = {len(g6)} rows {g6}; "
          f"rows dischargeable by the bit ALONE = {len(flagged)}")
    print(f"  ITEM 19  fallback kinds live: EXTERNAL_DATUM ({len(ext)} rows), "
          "PROVEN_UNSUPPLYABLE, SOURCE_DECLARED_OPEN__NO_MECHANISM_SUPPLIED")
    print(f"  ITEM 20  layer-0 forks registered = {len(fork_ids)}; "
          f"bit-2 fork among them = {bool(registered)}")
    print(f"  ITEM 15  OVER_DETERMINED escalations = {len(esc)}, "
          "four allowed dispositions each, every one owned")
    return 0


# ------------------------------------------------------------------ selftest
MUTATIONS = {
    "M1": "machinery: README path-table redirect",
    "M2": "reference: base-categories swapped for VERIFICATION.md",
    "M3": "reference: stale ledger v0.258 instead of v0.259",
    "M4": "reference: phase vocabulary loosened so constructions read as phase objects",
    "M5": "machinery: diff extractor takes the wrong hunk side",
    "M6": "machinery: bit-2 fork scanner vocabulary blinded",
    "M7": "machinery: fork-id extraction regex corrupted",
    "M8": "machinery: head-demand detector blinded (empty phase vocabulary)",
    "W": "DELIBERATELY WRONG VERDICT: 'a dozen rows' + 'registry already covers bit 2'",
}


def selftest() -> int:
    me = [sys.executable, str(Path(__file__).resolve())]
    env = dict(os.environ)
    env.pop("LDD_MUTATION", None)

    print("SELFTEST -- clean baseline FIRST")
    print("=" * 72)
    base = subprocess.run(me, capture_output=True, text=True, env=env, cwd=str(ROOT))
    if base.returncode != 0 or "[FAIL]" in base.stdout:
        print("[ABORT] clean baseline is RED -- every mutation would exit nonzero for")
        print("        the pre-existing reason, so no mutation result would mean anything.")
        print(base.stdout[-2500:])
        return 1
    cert = [l for l in base.stdout.splitlines() if "checks pass" in l]
    print(f"  baseline GREEN -- {cert[0].strip() if cert else 'no certificate line'}")
    print()

    caught, missed = 0, []
    for tag, desc in MUTATIONS.items():
        e = dict(env)
        e["LDD_MUTATION"] = tag
        r = subprocess.run(me, capture_output=True, text=True, env=e, cwd=str(ROOT))
        has_fail = "[FAIL]" in r.stdout
        red = r.returncode != 0
        if red and has_fail:
            first = [l for l in r.stdout.splitlines() if l.startswith("[FAIL]")][0]
            print(f"  [CAUGHT] {tag:3} {desc}")
            print(f"           via {first.strip()[:96]}")
            caught += 1
        elif red and not has_fail:
            print(f"  [CRASH-NOT-DETECTION] {tag:3} {desc} -- nonzero exit, no [FAIL] line")
            missed.append(tag)
        else:
            print(f"  [MISSED] {tag:3} {desc} -- probe stayed GREEN under corruption")
            missed.append(tag)

    print("=" * 72)
    if missed:
        print(f"SELFTEST FAILED: {caught}/{len(MUTATIONS)} caught; unhandled: {missed}")
        return 1
    print(f"SELFTEST PASS: baseline green, {caught}/{len(MUTATIONS)} corruptions each "
          "caught via a genuine [FAIL] -- exit 0")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else run())
