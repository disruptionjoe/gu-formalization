#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SG-1: the C6a scope defect in `tests/gu-forces/leg_a_forcing_enumeration.py`,
verified independently of CN-2; the disposition (NARROWING, applied OUTSIDE the
predeclaration); and what the dependent gates actually inherit.

THE TARGET.  LEG-A's commitment `C6a` codes GU's field-content declaration as
ALLOW-everything on three axes and glosses it:

    "NEUTRAL at the declaration level."

That is TRUE on the three axes LEG-A codes -- field-space, invariance, phase --
and OVER-BROAD as a sentence, because none of the three is a chirality axis.
C6a's own `source=` cites BOTH an unsubscripted locus [00:49:16] and an
explicitly opposite-half locus [00:32:46], and the note collapses them.

WHAT THIS PROBE IS FOR, AND WHAT IT REFUSES TO DO.  It does NOT edit
`leg_a_forcing_enumeration.py`.  The predeclaration's evidential value rests on
an anti-p-hacking receipt, and LEG 4 below demonstrates MECHANICALLY that the
file's own freeze guard is same-process-only and therefore blind to a post-hoc
edit -- which is exactly why the file must be left alone rather than "safely"
amended.  Instead this probe PINS the predeclaration by SHA-256 from outside, so
that the immutability which was previously a social convention becomes a machine
check that turns red on any future edit.

STRUCTURE
  LEG 1  the defect, verified from the FILE and from the PRIMARY TRANSCRIPT --
         not from CN-2's report of either.
  LEG 2  CONTRARY CONTROLS.  The same detector is pointed at axes the
         enumeration genuinely DOES code (provenance, phase) and must say
         CODED; pointed at chirality it must say UNCODED.  Plus the strongest
         control available: LEG-B, an independently constructed enumeration,
         reads the SAME two loci and does NOT collapse them.
  LEG 3  the narrowing moves NO computed bit -- proved two ways: exhaustively
         (the `note` field enters exactly one computation in the whole file),
         and by a from-scratch shadow recomputation of the intersection.
  LEG 4  what the receipt protects, and the mechanical demonstration that an
         in-file edit would defeat it undetectably.
  LEG 5  the dependent gates, the homonym that propagated the defect, and the
         selector -- including a correction of record about which third gate.

EXACTNESS.  Every count is an exact integer.  No float is load-bearing.  Every
claim about a file is a substring/parse assertion against the file on disk.

Exit 0 == every check passed.  ``--selftest`` FIRST verifies the clean baseline
exits 0 -- a red baseline makes every mutation result meaningless, so it aborts
with exit 1 rather than banking a false "all mutations caught" -- and only then
plants false machinery, requiring each mutant to drive exit 1.  The selftest
itself exits 0 when the baseline was green and every mutation was caught.
"""

from __future__ import annotations

import hashlib
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]

LEG_A = "tests/gu-forces/leg_a_forcing_enumeration.py"
LEG_B = "tests/gu-forces/leg_b_forcing_enumeration_independent.py"
REFEREE = "tests/gu-forces/referee_leg_a_independent.py"
CANON_RESULTS = "canon/gu-forces-field-space-declaration-RESULTS.md"
TRANSCRIPT = "papers/drafts/Transcript into the impossible.md"
REGISTER = "lab/sources/source-claim-register.yaml"
CRB = "lab/active-research/joe-directed/carrier/crb-carrier-is-four-corners-not-one-weyl-2026-08-15.md"
CS1 = "lab/active-research/joe-directed/class-shift/cs1-first-order-shift-is-the-chirality-grading-2026-08-15.md"
CN2_PROBE = "tests/channel-swings/joe_directed_cn2_notation_census.py"
JD_README = "lab/active-research/joe-directed/README.md"
BD_DIR = "lab/active-research/joe-directed/base-duality"

# The predeclaration as found on 2026-08-16, byte-length and SHA-256.  This is
# the receipt the campaign never had.  It is recorded OUTSIDE the predeclared
# file so that pinning it costs the predeclaration nothing.
LEG_A_BYTES = 30243
LEG_A_SHA256 = "3043d29ef2ca97b527113b16a399f7f5256ba8df85902ccff3b3d69a58380197"
REFEREE_BYTES = 4946
REFEREE_SHA256 = "5d84800c867581e4d8376806b9b2b05132f08de99df83c5dc570ba0909817b1f"

# Tokens that would indicate a chirality-half axis if any were coded.  The
# repository's own closed vocabulary (CN-2) plus the raw half-spinor spellings.
CHIRALITY_TOKENS = (
    "S-FULL-DIRAC", "S-HALF-OPPOSITE", "S-HALF-SAME", "S-CHIRALITY-UNTYPED",
    "positive spinner", "negative spinner", "S^+", "S^-", "S_+", "S_-",
    "half-spinor", "HALF", "WEYL",
)

# The three axes LEG-A actually codes, as the kwarg stems of `predeclare`.
CODED_AXIS_KWARGS = ("rules_out_field", "rules_out_inv", "rules_out_phase")

CHECKS: list[tuple[bool, str]] = []


def check(label: str, cond: bool) -> bool:
    CHECKS.append((bool(cond), label))
    print(f"  [{'PASS' if cond else 'FAIL'}] {label}")
    return bool(cond)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def norm(text: str) -> str:
    """Collapse every whitespace run to a single space.  Prose assertions must
    survive the line-wrapping of the file they quote; without this a correct
    finding fails for a newline."""
    return re.sub(r"\s+", " ", text)


def c6a_row(source: str) -> str:
    """Extract the C6a predeclare(...) block from LEG-A's text, exactly."""
    start = source.index('id="C6a"')
    end = source.index("# --- C6b", start)
    return source[start:end]


def field_of(block: str, name: str) -> str:
    """Extract one kwarg's literal text from a predeclare block."""
    m = re.search(rf"{name}=\((.*?)\),\n", block, re.S)
    if m:
        return m.group(1)
    m = re.search(rf"{name}=([^,\n]+)", block)
    return m.group(1) if m else ""


# --------------------------------------------------------------------------
# LEG 1 -- the defect, verified from the file and the PRIMARY source.
# --------------------------------------------------------------------------

def leg1_defect() -> None:
    print("\n" + "=" * 74)
    print("LEG 1 -- the scope defect, verified independently of CN-2")
    print("=" * 74)

    a = read(LEG_A)

    # 1.1  Exactly three declaration axes are coded, and their names are fixed.
    axis_sets = re.findall(r"^(FIELD_SPACE|INVARIANCE|PHASE|INV_PROVENANCE)\s*=", a, re.M)
    check("LEG-A declares exactly 4 axis value-sets (3 declaration axes + 1 "
          "conditional provenance sub-axis)", len(axis_sets) == 4)
    check("the 3 declaration axes are exactly {FIELD_SPACE, INVARIANCE, PHASE}",
          set(axis_sets) == {"FIELD_SPACE", "INVARIANCE", "PHASE", "INV_PROVENANCE"})

    # Every predeclared row codes exactly these three hard-elimination axes.
    rows = re.findall(r"predeclare\((.*?)\n\)", a, re.S)
    check("LEG-A predeclares exactly 10 commitments", len(rows) == 10)
    for stem in CODED_AXIS_KWARGS:
        check(f"every one of the 10 rows codes the axis `{stem}`",
              all(stem in r for r in rows))

    # 1.2  NONE of the coded axes is a chirality axis -- checked on the axis
    # DEFINITIONS, where a chirality axis would have to appear if it existed.
    defs = a[a.index("FIELD_SPACE ="):a.index("# The four vertices")]
    hits = [t for t in CHIRALITY_TOKENS if t in defs]
    check(f"no chirality-half token appears in any axis definition (found {hits})",
          hits == [])
    # Planted-positive control (added 2026-08-17, found via FX-3): an ABSENCE
    # check on a clean corpus cannot demonstrate its detector has power --
    # corrupting the vocabulary leaves `hits == []` exactly as before, so the
    # "vocabulary emptied" mutation was undetectable by construction and only
    # ever "passed" via the path-bug crash.  A synthetic definitions blob
    # carrying the first vocabulary token MUST be flagged; the mutation that
    # corrupts that token now goes red HERE, on a genuine [FAIL].
    planted_defs = 'FIELD_SPACE = {"S-FULL-DIRAC"}  # synthetic control blob'
    check("chirality detector fires on a planted positive (non-vacuity control)",
          any(t in planted_defs for t in CHIRALITY_TOKENS))
    check("the axis value-sets are exactly the carrier/vacuum vocabulary, with "
          "no half-spinor value",
          '{"CONSTRAINED", "FULL", "BARE"}' in defs
          and '{"ABSENT", "PRESENT"}' in defs
          and '{"MASSIVE", "CHIRAL"}' in defs)

    # 1.3  C6a's own source cites BOTH loci.
    block = c6a_row(a)
    src = field_of(block, "source")
    check("C6a cites the UNSUBSCRIPTED locus [00:49:16]", "[00:49:16]" in src)
    check("C6a cites the OPPOSITE-HALF locus [00:32:46]", "[00:32:46]" in src)
    check("C6a's citation of [00:32:46] carries the half words verbatim",
          "positive spinners" in src and "negative spinners" in src)

    # 1.4  The loci verified against the PRIMARY TRANSCRIPT, not the citation.
    # This is what makes the verification independent: a correct citation of a
    # misquoted line would pass 1.3 and fail here.
    lines = read(TRANSCRIPT).split("\n")
    l_3246 = lines[106]   # 1-indexed line 107
    l_4916 = lines[172]   # 1-indexed line 173
    check("primary source line 107 is the OPPOSITE-HALF declaration "
          "(0-forms in positive, 1-forms in negative)",
          "zero forms valued in the positive spinners" in l_3246
          and "one forms valued in the negative spinners" in l_3246)
    check("primary source line 173 is the UNSUBSCRIPTED declaration",
          "zero forms and one forms valued either in add or in the spinners" in l_4916)
    check("primary source line 173 carries NO half-spinor qualifier -- the two "
          "loci genuinely differ in chirality content",
          not any(t in l_4916 for t in
                  ("positive spinners", "negative spinners", "S^+", "S^-")))

    # 1.5  The note's neutrality claim is UNQUALIFIED.  The detector looks for
    # any axis-scoping language in the note; absence is the defect.
    note = norm(field_of(block, "note"))
    check("C6a's note asserts neutrality", "NEUTRAL at the declaration level" in note)
    # The neutrality claim is a COMPLETE, UNQUALIFIED sentence: the words that
    # follow it start a new sentence about the arena, not a scope qualifier.
    check("C6a's neutrality claim is a complete sentence with no axis qualifier",
          "NEUTRAL at the declaration level. Omega^1(S) is the COMMON arena" in note)
    check("C6a's note never says 'axis' or 'axes' at all",
          "axis" not in note.lower() and "axes" not in note.lower())
    # The one occurrence of "three" in the note counts CARRIERS, not axes --
    # which is exactly the conflation at issue.
    check("the note's only 'three' counts CARRIERS, not axes",
          "three carriers" in note and "three axes" not in note)
    check("C6a's note collapses to a single unsubscripted symbol: it names "
          "Omega^1(S) and never distinguishes the two cited loci",
          "Omega^1(S)" in note and "[00:32:46]" not in note)
    # And the scope the note drops is one the FILE ITSELF states elsewhere:
    # SECTION 1's own header names the three axes explicitly.  The narrowing
    # therefore RESTORES a scope the predeclaration already declared.
    check("the file's SECTION 1 header already names the three axes, so the "
          "narrowing restores a scope the predeclaration itself states",
          "what it FORCES / RULES-OUT on the three declaration axes {field-space, "
          "invariance, phase}" in norm(a))
    check("C6a codes zero hard eliminations and zero tilts -- the CELLS are "
          "correct; only the sentence over-reaches",
          "rules_out_field=set()" in block and "tilt_field=None" in block)


# --------------------------------------------------------------------------
# LEG 2 -- CONTRARY CONTROLS.  The detector must distinguish coded from uncoded.
# --------------------------------------------------------------------------

def axis_is_coded(source: str, kwarg: str) -> bool:
    """A commitment axis is CODED iff some predeclared row supplies that kwarg
    AND the leg computes an allowed-set over it."""
    rows = re.findall(r"predeclare\((.*?)\n\)", source, re.S)
    supplied = any(kwarg in r for r in rows)
    stem = kwarg.replace("rules_out_", "").replace("inv_provenance_out", "prov")
    computed = f"allowed_{stem}" in source
    return supplied and computed


def leg2_contrary_controls() -> None:
    print("\n" + "=" * 74)
    print("LEG 2 -- CONTRARY CONTROLS: the detector distinguishes coded/uncoded")
    print("=" * 74)

    a = read(LEG_A)

    # CONTRARY A -- an axis the enumeration genuinely DOES code, and which a
    # commitment genuinely DOES eliminate on.  If the detector called this
    # UNCODED it would be worthless.
    check("CONTRARY A: the PROVENANCE axis IS coded (C1 hard-eliminates "
          "SUGRA_4D and the leg computes allowed_prov)",
          axis_is_coded(a, "inv_provenance_out") is True)
    check("CONTRARY A: and the elimination is real -- the leg asserts "
          "allowed_prov collapses to a singleton",
          'allowed_prov == {"GRADED_IG"}' in a)

    # CONTRARY B -- a second coded axis, this one with NO elimination, to show
    # the detector is not merely detecting eliminations.
    check("CONTRARY B: the PHASE axis IS coded (rows supply it, leg computes "
          "allowed_phase) even though nothing eliminates on it",
          axis_is_coded(a, "rules_out_phase") is True)
    check("CONTRARY B: and no commitment eliminates a phase -- both survive",
          'allowed_phase == {"MASSIVE", "CHIRAL"}' in a)

    # THE TARGET -- same detector, opposite answer.
    check("TARGET: there is NO chirality kwarg on any row -- the axis is UNCODED",
          axis_is_coded(a, "rules_out_chirality") is False)
    check("TARGET: and the leg computes no allowed-set over it",
          "allowed_chirality" not in a and "allowed_half" not in a)

    # CONTRARY C -- the strongest control, and it is native to the repository:
    # a genuinely independent enumeration of the SAME two loci did NOT collapse
    # them.  So the collapse is LEG-A-specific and avoidable, not forced by the
    # source.  Without this control, "the source is ambiguous" would be a live
    # alternative explanation for the defect.
    b = read(LEG_B)
    check("CONTRARY C: LEG-B cites the SAME two loci", "[00:32:46]" in b and "[00:49:16]" in b)
    check("CONTRARY C: LEG-B NAMES the chirality split rather than collapsing it",
          "chirality split (0-forms in S+, 1-forms in S-)" in b)
    check("CONTRARY C: LEG-B codes a TILT for it, so the distinction is "
          "load-bearing there, not decorative",
          'TILT="B",                               # geometric chirality-split texture' in b)
    check("CONTRARY C: LEG-B tallies it as its own datum b4, giving 4 B-passages "
          "where LEG-A's note-level collapse gives 3",
          "b4 [00:32:46] geometric chirality-split field content" in b
          and "b_passages = 4" in b)

    # CONTRARY D -- a NEGATIVE control on the receipt itself.  The "independent
    # referee" commits the SAME collapse, so referee agreement is NOT
    # independent evidence on this particular point.
    ref = read(REFEREE)
    check("CONTRARY D: the independent referee makes the SAME collapse, so its "
          "agreement is not independent evidence HERE",
          "[00:49:16]/[00:32:46] name Omega^1(S)" in ref)


# --------------------------------------------------------------------------
# LEG 3 -- the narrowing moves NO computed bit.  Proved two ways.
# --------------------------------------------------------------------------

def leg3_narrowing_is_inert() -> None:
    print("\n" + "=" * 74)
    print("LEG 3 -- NARROWING vs EXTENSION: the narrowing is computationally inert")
    print("=" * 74)

    a = read(LEG_A)

    # 3.1  EXHAUSTIVE argument: the `note` field enters exactly ONE computation
    # in the entire file -- the firewall's forbidden-string scan.  So no
    # rewording of a note can move a bit, whatever it says.
    note_refs = re.findall(r'c\["note"\]', a)
    check(f"the `note` field is consumed exactly once in the whole file "
          f"(found {len(note_refs)} reference(s))", len(note_refs) == 1)
    check("and that one consumer is the FIREWALL's forbidden-string scan",
          'src_blob = "".join(c["source"] + c["note"] for c in COMMITMENTS)' in a)

    # 3.2  The narrowing text this artifact proposes passes that one consumer.
    proposed = ("NEUTRAL on the THREE AXES THIS LEG CODES (field, invariance, "
                "phase).  SILENT on a fourth axis it does not code: the "
                "chirality assignment on S.  See SG-1, 2026-08-16.")
    forbidden = ("chi(K3)", "A-hat=3", "Ahat=3", "/8 manufacture")
    check("the proposed narrowing text passes the firewall unchanged",
          not any(f in proposed for f in forbidden))

    # 3.3  SHADOW RECOMPUTATION, from scratch, no import.  Under the narrowed
    # reading C6a contributes exactly what it already contributes on the three
    # coded axes: nothing.  So the whole intersection must reproduce.
    field = {"CONSTRAINED", "FULL", "BARE"}
    inv = {"ABSENT", "PRESENT"}
    phase = {"MASSIVE", "CHIRAL"}
    prov = {"SUGRA_4D", "GRADED_IG"}
    prov -= {"SUGRA_4D"}                       # C1, the only hard elimination
    vertex = {
        ("ABSENT", "MASSIVE"): "B",
        ("PRESENT", "CHIRAL"): "A",
        ("PRESENT", "MASSIVE"): "CTRL40",
        ("ABSENT", "CHIRAL"): "INCONSISTENT",
    }

    def survives(i: str, p: str) -> bool:
        if i not in inv or p not in phase:
            return False
        car = vertex[(i, p)]
        if car in ("A", "CTRL40"):
            return "GRADED_IG" in prov
        return True

    survivors = {vertex[k] for k in vertex if survives(*k)}

    def collapse(i=None, p=None) -> set[str]:
        return {vertex[k] for k in vertex
                if survives(*k) and (i is None or k[0] == i) and (p is None or k[1] == p)}

    check("shadow: field-space axis not collapsed (3 values)", len(field) == 3)
    check("shadow: invariance axis not collapsed (2 values)", len(inv) == 2)
    check("shadow: phase axis not collapsed (2 values)", len(phase) == 2)
    check("shadow: provenance collapses to {GRADED_IG}", prov == {"GRADED_IG"})
    check("shadow: all four corners survive -- LEAVES A FAMILY",
          survivors == {"A", "B", "CTRL40", "INCONSISTENT"})
    check("shadow: (ABSENT,MASSIVE) collapses uniquely to B", collapse("ABSENT", "MASSIVE") == {"B"})
    check("shadow: (PRESENT,CHIRAL) collapses uniquely to A", collapse("PRESENT", "CHIRAL") == {"A"})
    check("shadow: neither bit alone forces a unique carrier -> residual is "
          "exactly 2 bits, unchanged by the narrowing",
          len(collapse(i="ABSENT")) == 2 and len(collapse(p="MASSIVE")) == 2)

    # 3.4  CLEAN BASELINE: LEG-A itself is green right now, 32/32.
    res = subprocess.run([sys.executable, str(ROOT / LEG_A)],
                         capture_output=True, text=True)
    check("LEG-A runs GREEN as found (exit 0)", res.returncode == 0)
    check("LEG-A reports exactly 32 checks, 0 failed",
          "CHECKS: 32 passed, 0 failed, 32 total" in res.stdout)
    check("LEG-A's verdict is unchanged: TILT+RESIDUAL (B-leaning)",
          "TILT+RESIDUAL (B-leaning)" in res.stdout)

    # 3.5  Why an EXTENSION would be the retro-fit.  Adding a chirality axis
    # would change the leg's headline number, which the narrowing does not.
    check("the leg's headline is that the residual is exactly 2 bits -- an "
          "added axis would change that number; the narrowing does not",
          "2-bit (invariance x phase) SG4 square" in a)
    check("and the sibling leg + referee both code exactly 3 axes, so an added "
          "axis would also break the cross-leg agreement receipt",
          axis_is_coded(read(LEG_B), "rules_out_chirality") is False)


# --------------------------------------------------------------------------
# LEG 4 -- what the receipt protects, and why it must not be edited.
# --------------------------------------------------------------------------

def leg4_receipt(scratch: pathlib.Path) -> None:
    print("\n" + "=" * 74)
    print("LEG 4 -- the anti-p-hacking receipt: what it is, and its blind spot")
    print("=" * 74)

    a = read(LEG_A)
    canon = read(CANON_RESULTS)

    # 4.1  The receipt's three stated legs, verbatim in canon.
    check("receipt leg 1: two independently constructed enumerations AGREE on "
          "the residual and the 4-corner bijection",
          "Both enumerations constructed independently" in canon
          and "they AGREE on the residual and the 4-corner bijection" in canon)
    check("receipt leg 2: referee verdict refuted=false, p_hacked=false",
          "refuted=false, p_hacked=false" in canon)
    check("receipt leg 3: every commitment coded as ALLOW=all-cells with zero "
          "hard eliminations; no commitment silently deletes a corner",
          "ALLOW=all-cells with ZERO hard eliminations" in canon
          and "No commitment was allowed to silently delete a corner." in canon)

    # 4.2  The file's own stated discipline is UNCONDITIONAL over rows -- not
    # merely over coded cells.  A `note` is part of a row.
    check("LEG-A's own discipline forbids editing a ROW, not merely a cell",
          "Predeclaration is frozen: no row is edited after the intersection is "
          "computed" in norm(a))
    check("and the note IS part of the row: it is a kwarg of predeclare(...) "
          "and is captured by FROZEN_TABLE",
          "note=(" in a and "FROZEN_TABLE = tuple(" in a)

    # 4.3  THE BLIND SPOT, demonstrated mechanically.  There is no hash receipt
    # in the campaign, and the in-file freeze guard is same-process only: it
    # snapshots the table AFTER SECTION 1 and re-compares within the same run,
    # so an edited file simply re-freezes its edited table and passes.
    check("no hash/digest receipt exists anywhere in the predeclaration",
          not any(t in a for t in ("sha256", "hashlib", "hexdigest", "digest")))

    scratch.mkdir(parents=True, exist_ok=True)
    mutant_path = scratch / "_sg1_legA_note_edited.py"
    old_note = "note=('NEUTRAL at the declaration level."
    new_note = "note=('NEUTRAL at the declaration level ON THREE AXES ONLY."
    check("the note text to be edited is present exactly once",
          a.count(old_note) == 1)
    mutant_path.write_text(a.replace(old_note, new_note, 1), encoding="utf-8")
    res = subprocess.run([sys.executable, str(mutant_path)],
                         capture_output=True, text=True)
    check("BLIND SPOT DEMONSTRATED: a copy of LEG-A with C6a's predeclared note "
          "EDITED still exits 0 with 32/32 -- the freeze guard cannot see it",
          res.returncode == 0 and "CHECKS: 32 passed, 0 failed, 32 total" in res.stdout)
    mutant_path.unlink(missing_ok=True)

    # 4.4  Therefore the only trust-free layer of the receipt is that the file
    # has never been touched.  That layer is destroyed by ANY edit, including a
    # provably benign one, and it cannot be restored.  This probe converts it
    # from a social convention into a machine check WITHOUT touching the file.
    raw = (ROOT / LEG_A).read_bytes()
    check(f"predeclaration byte-length pinned at {LEG_A_BYTES}", len(raw) == LEG_A_BYTES)
    check("predeclaration SHA-256 pinned -- any future edit turns this red",
          hashlib.sha256(raw).hexdigest() == LEG_A_SHA256)
    raw_ref = (ROOT / REFEREE).read_bytes()
    check(f"referee byte-length pinned at {REFEREE_BYTES}", len(raw_ref) == REFEREE_BYTES)
    check("referee SHA-256 pinned",
          hashlib.sha256(raw_ref).hexdigest() == REFEREE_SHA256)

    # 4.5  An in-file edit also has a concrete, already-green cost: CN-2's live
    # probe asserts these two files carry ZERO repair tokens.
    cn2 = read(CN2_PROBE)
    check("CN-2's live probe lists the predeclaration as NOT_MINE_TO_EDIT",
          "NOT_MINE_TO_EDIT = {" in cn2 and f'"{LEG_A}",' in cn2)
    check("and machine-asserts it carries ZERO repair tokens, so an in-file "
          "token edit would turn an existing green probe red",
          "ledger/predeclaration surface carries ZERO CN-2 tokens" in cn2)


# --------------------------------------------------------------------------
# LEG 5 -- the dependent gates, the homonym, and the selector.
# --------------------------------------------------------------------------

def leg5_gates_and_selector() -> None:
    print("\n" + "=" * 74)
    print("LEG 5 -- what the dependent gates inherit, and what the selector is")
    print("=" * 74)

    a = read(LEG_A)
    b = read(LEG_B)
    canon = read(CANON_RESULTS)

    # 5.1  Bit 2 is a PHASE bit.  Stated in canon, verbatim.
    check("canon defines bit 2 as a PHASE bit, not a chirality assignment",
          "Bit 2 -- phase:" in canon
          and "chiral/unbroken vs massive/super-Higgs" in canon)
    check("canon defines bit 1 as the invariance-selection bit",
          "Bit 1 -- invariance-selection:" in canon)

    # 5.2  THE HOMONYM -- the propagation mechanism, in the repository's own
    # Layer-0 vocabulary.  The phase axis carries a value literally spelled
    # CHIRAL, meaning massless/unbroken, NOT handed.  A downstream reader
    # needing a chirality selector finds exactly one token named "chiral" in
    # the residual and routes to it.
    check("HOMONYM: LEG-A's PHASE axis has a value literally spelled CHIRAL",
          'PHASE       = {"MASSIVE", "CHIRAL"}' in a)
    check("HOMONYM: and the file glosses it as the MASSLESS/decreased-VEV "
          "point -- a vacuum property, not a handedness",
          "broken massive point / unbroken chiral (decreased-VEV) point" in a)
    check("HOMONYM: the sibling leg uses the same token with the same gloss, "
          "so the collision is systemic, not a typo",
          'PH  (phase)        in {"chiral","massive"}' in b
          and "decreased-VEV/massless vs" in b)
    check("HOMONYM: and no half-spinor sense of the word appears anywhere on "
          "LEG-A's axis or vertex definitions",
          not any(t in a[a.index("FIELD_SPACE ="):a.index("COMMITMENTS = []")]
                  for t in ("positive spinner", "negative spinner", "S^+", "S^-")))

    # 5.3  The enumeration names NO selector for the chirality axis.  Not a
    # missing bit -- an uncoded axis.  Stated as a positive, checkable fact.
    residual = a[a.index("SECTION 2d"):]
    check("the residual section names exactly two bits and neither is a "
          "chirality bit",
          "bit1 = invariance" in residual and "bit2 = phase" in residual
          and not any(t in residual for t in ("S^+", "S^-", "S-HALF", "half-spinor")))

    # 5.4  GATE 1 -- CR-B.  Its 4.3 routing is about which effective split is
    # DYNAMICALLY REALIZED.  That is a VEV question, and bit 2 is the right
    # home for it.  What CR-B must not carry is the content fork.
    crb = read(CRB)
    check("GATE 1 (CR-B): routes its open question to SG4 bit 2",
          "SG4 bit 2" in crb)
    check("GATE 1 (CR-B): the question it routes is which split is DYNAMICALLY "
          "realized -- a VEV question, correctly homed on bit 2",
          "Which effective split is dynamically realized remains SG4 bit 2" in crb)
    check("GATE 1 (CR-B): and CR-B already separates declaration from operative "
          "in its own forbidden-summaries, so it inherits a WORDING debt, "
          "not a result defect",
          "the DECLARATION is decided; the OPERATIVE reading is SG4 bit 2" in norm(crb))

    # 5.5  GATE 2 -- CS-1.  Its question is which of two horns is operative,
    # also a Layer-2 question.  It inherits nothing.
    cs1 = read(CS1)
    check("GATE 2 (CS-1): routes to SG4 bit 2", "SG4 bit 2" in cs1)
    check("GATE 2 (CS-1): its question is which horn is OPERATIVE -- Layer 2, "
          "correctly homed; CS-1 inherits no correction",
          "the selector remains SG4 bit 2" in cs1)

    # 5.6  GATE 3 -- CORRECTION OF RECORD.  The base-duality packet does NOT
    # route anything to SG4 bit 2.  The actual third surface is the
    # joe-directed tree README, which is a more consequential surface.
    bd_files = sorted((ROOT / BD_DIR).glob("*.md"))
    check(f"base-duality directory found ({len(bd_files)} files)", len(bd_files) >= 6)
    bd_blob = "".join(p.read_text(encoding="utf-8") for p in bd_files)
    check("CORRECTION OF RECORD: base-duality routes NOTHING to SG4 -- zero "
          "occurrences of 'SG4' anywhere in the packet set",
          "SG4" not in bd_blob)
    check("CORRECTION OF RECORD: and zero occurrences of 'bit 2'",
          "bit 2" not in bd_blob)

    readme = read(JD_README)
    check("GATE 3 (actual): the joe-directed README routes the selector to "
          "SG4 bit 2", "equivalently SG4 bit 2" in readme)
    check("GATE 3 (actual): and it does so for the three-value CONTENT fork it "
          "has just defined -- this is the one genuine misroute",
          "S-FULL-DIRAC" in readme and "S-HALF-OPPOSITE" in readme
          and "S-HALF-SAME" in readme
          and "this tree does not resolve\nthe fork" in readme)

    # 5.7  WHY the content fork cannot route to bit 2: the condition bit 2
    # encodes PRESUPPOSES one value of that fork.  A condition that assumes an
    # answer cannot select among the alternatives.  This is a circularity, and
    # it is checkable from the register's verbatim.
    reg = read(REGISTER)
    check("SC-CHI-01 is in the register", "id: SC-CHI-01" in reg)
    check("CIRCULARITY: SC-CHI-01's VEV condition takes a NON-CHIRAL TOTAL as "
          "its INPUT -- it presupposes the full-Dirac declaration",
          "non-chiral total theory splits at the emergent level into two separate" in reg)
    check("CIRCULARITY: therefore the VEV condition operates DOWNSTREAM of the "
          "content fork and cannot select between its three values",
          "id: SC-CHI-01" in reg and "S-HALF-SAME" not in reg)

    # 5.8  The correct Layer-1 selector is the SOURCE, already read -- not a
    # bit.  SG4 is by definition the UNWRITTEN declaration; the chirality
    # assignment is written, twice, at two layers.
    check("SG4 is defined as GU's UNWRITTEN source-action declaration",
          "GU's UNWRITTEN source-action field-space declaration (SG4)" in norm(a))
    check("whereas the chirality assignment is WRITTEN -- both loci are printed "
          "in the primary source and cited in C6a itself",
          "[00:49:16]" in a and "[00:32:46]" in a)


# --------------------------------------------------------------------------
# NON-VACUITY -- planted false facts, each required to be observed False.
# --------------------------------------------------------------------------

def planted_false_facts() -> None:
    print("\n" + "=" * 74)
    print("NON-VACUITY -- planted false facts, each required to be observed False")
    print("=" * 74)

    a = read(LEG_A)
    b = read(LEG_B)
    canon = read(CANON_RESULTS)
    bd_blob = "".join(p.read_text(encoding="utf-8")
                      for p in sorted((ROOT / BD_DIR).glob("*.md")))

    planted = [
        ("LEG-A codes a chirality axis", "rules_out_chirality" in a),
        ("LEG-A computes an allowed_chirality set", "allowed_chirality" in a),
        ("C6a hard-eliminates a field value", "rules_out_field={" in c6a_row(a)),
        ("C6a carries a tilt", 'tilt_field="' in c6a_row(a)),
        ("C6a's note already names its axis scope",
         "three axes" in field_of(c6a_row(a), "note").lower()),
        ("the residual is 3 bits", "3-bit" in a),
        ("LEG-A carries a hash receipt", "sha256" in a),
        ("LEG-B collapses the two loci the way LEG-A does",
         "[00:49:16]/[00:32:46] name Omega^1(S)" in b),
        ("canon says the legs DISAGREE on the residual",
         "they DISAGREE on the residual" in canon),
        ("canon reports p_hacked=true", "p_hacked=true" in canon),
        ("base-duality routes to SG4 bit 2", "SG4 bit 2" in bd_blob),
        ("bit 2 is defined as a chirality bit",
         "Bit 2 -- chirality:" in canon),
        ("the phase axis value is spelled HANDED rather than CHIRAL",
         'PHASE       = {"MASSIVE", "HANDED"}' in a),
        # NOTE: the naive needle `predeclare\(` counts 11, because it also
        # matches the `def predeclare(...)` definition.  This planted fact
        # caught that bug in an earlier draft of this probe; the count below
        # is anchored to line-start so it counts CALLS only.
        ("LEG-A predeclares 11 commitments",
         len(re.findall(r"^predeclare\(", a, re.M)) == 11),
        ("LEG-A predeclares 9 commitments",
         len(re.findall(r"^predeclare\(", a, re.M)) == 9),
        ("the note field is consumed twice", len(re.findall(r'c\["note"\]', a)) == 2),
    ]
    for label, observed in planted:
        check(f"planted false fact observed False: {label}", observed is False)


# --------------------------------------------------------------------------
# --selftest -- CLEAN BASELINE FIRST, then mutations.
# --------------------------------------------------------------------------

MUTATIONS = (
    # REPAIRED 2026-08-17 (found by FX-3): the original mutation rewrote the
    # CHECK's predicate to a tautology ("len(axis_sets) >= 0"), which can only
    # make the probe greener -- an unfalsifiable mutation that "passed" solely
    # because every mutant crashed on a path bug before any check ran.  A
    # mutation must corrupt MACHINERY so a check catches it: this one blinds
    # the axis regex to one axis, so the count check and the set check both go
    # red on a genuine [FAIL].
    ("axis detector blinded to the provenance sub-axis",
     'r"^(FIELD_SPACE|INVARIANCE|PHASE|INV_PROVENANCE)\\s*="',
     'r"^(FIELD_SPACE|INVARIANCE|PHASE|ZZ_PROVENANCE)\\s*="'),
    ("chirality token vocabulary emptied",
     'CHIRALITY_TOKENS = (\n    "S-FULL-DIRAC"', 'CHIRALITY_TOKENS = (\n    "ZZ-NOT-A-TOKEN"'),
    ("coded-axis detector always returns True",
     "    return supplied and computed", "    return True"),
    ("coded-axis detector always returns False",
     "    return supplied and computed", "    return False"),
    # REPAIRED 2026-08-17: the original retarget to C6b crashed rather than
    # detected -- the extractor's end marker ("# --- C6b") lies BEFORE the C6b
    # id, so the end search ran past itself and raised ValueError before any
    # check.  Retargeting to C5 (upstream of C6a) yields a well-formed block
    # whose fields belong to the WRONG commitment, which the content checks
    # catch on a genuine [FAIL].
    ("C6a row extractor grabs the wrong commitment",
     "    start = source.index('id=\"C6a\"')", "    start = source.index('id=\"C5\"')"),
    ("transcript opposite-half line index shifted off the locus",
     "    l_3246 = lines[106]", "    l_3246 = lines[105]"),
    ("transcript unsubscripted line index shifted off the locus",
     "    l_4916 = lines[172]", "    l_4916 = lines[171]"),
    # REPAIRED 2026-08-17: same defect class as mutation 1 -- loosening the
    # CHECK's own predicate can only make the probe greener and is
    # undetectable by construction.  Corrupt the DETECTOR instead: blind the
    # note-consumer regex so it finds zero references, and the count check
    # goes red on a genuine [FAIL].
    ("note-consumer detector blinded",
     """note_refs = re.findall(r'c\\["note"\\]', a)""",
     """note_refs = re.findall(r'c\\["zz_no_such_key"\\]', a)"""),
    ("shadow drops C1's provenance elimination",
     '    prov -= {"SUGRA_4D"}', "    prov -= set()"),
    # REPAIRED 2026-08-17: the original added "B" to the survival guard, but
    # the guard's condition ("GRADED_IG" in prov) is TRUE in the clean state,
    # so the widened guard changed nothing observable -- a no-op mutation,
    # undetectable by construction.  Kill the guard instead: guarded carriers
    # die, the survivor set loses two corners, and the all-four-corners check
    # goes red on a genuine [FAIL].
    ("shadow survival guard kills guarded carriers",
     '        return "GRADED_IG" in prov', "        return False"),
    ("shadow vertex map corrupted so B lands at the chiral point",
     '        ("ABSENT", "MASSIVE"): "B",', '        ("ABSENT", "MASSIVE"): "A",'),
    # REPAIRED 2026-08-17: third instance of the assertion-tautology class --
    # replacing the pin comparison with a length check weakens the CHECK and
    # can only stay green.  Corrupt the REFERENCE instead: comparing against
    # the reversed digest must fail on the real file, proving the pin is
    # actually consulted, on a genuine [FAIL].
    ("SHA-256 pin compared against a corrupted reference",
     "hashlib.sha256(raw).hexdigest() == LEG_A_SHA256",
     "hashlib.sha256(raw).hexdigest() == LEG_A_SHA256[::-1]"),
    ("blind-spot demonstration inverted to require the guard to catch the edit",
     'res.returncode == 0 and "CHECKS: 32 passed, 0 failed, 32 total" in res.stdout',
     'res.returncode != 0'),
    # REPAIRED 2026-08-17: fourth instance of the assertion-tautology class --
    # swapping one absent token for another absent token leaves the absence
    # check vacuously green.  Corrupt the probe token to one that IS present:
    # the check then fails on the real blob, proving the blob is actually
    # consulted, on a genuine [FAIL].
    ("base-duality absence check probed with a token that is present",
     '"SG4" not in bd_blob', '"the" not in bd_blob'),
    # REPAIRED 2026-08-17: fifth instance -- replacing the gate's predicate
    # with a constant True loosens the CHECK and stays green forever.  INVERT
    # the gate instead: requiring the planted facts to observe True makes all
    # five fail on the real corpus, proving the gate actually consults the
    # observation, on genuine [FAIL]s.
    ("planted-false-fact gate inverted",
     "check(f\"planted false fact observed False: {label}\", observed is False)",
     "check(f\"planted false fact observed False: {label}\", observed is True)"),
)


def selftest(scratch: pathlib.Path) -> int:
    me = pathlib.Path(__file__)
    source = me.read_text(encoding="utf-8")

    # ---- CLEAN BASELINE FIRST.  A red baseline makes every mutation exit 1
    # for the wrong reason, which would bank a false "all caught".  Abort.
    print("BASELINE -- verifying the UNMUTATED probe exits 0 before mutating")
    base = subprocess.run([sys.executable, str(me)], capture_output=True, text=True)
    if base.returncode != 0:
        print("  BASELINE IS RED (exit "
              f"{base.returncode}).  Mutation results would be meaningless: "
              "every mutant would 'fail' for the pre-existing reason.  ABORTING.")
        tail = [ln for ln in base.stdout.splitlines() if "[FAIL]" in ln]
        for ln in tail[:12]:
            print("   ", ln)
        return 1
    print("  baseline GREEN (exit 0) -- mutations are now meaningful\n")

    # REPAIRED 2026-08-17 (found by FX-3).  The mutant used to run from a
    # scratch SUBDIRECTORY, so its own `parents[2]` resolved one level short
    # and every mutant died on a doubled path before any check ran -- every
    # "caught" was a crash-catch, not a detection.  Two fixes: the mutant now
    # runs at the probe's own depth so ROOT resolves identically, and a catch
    # only counts if the mutant fails via a genuine [FAIL] check -- a nonzero
    # exit with no [FAIL] line is reported as CRASH-NOT-DETECTION and fails
    # the selftest, per the FX-3 convention.
    tmp = me.parent / "_sg1_mutant_tmp.py"
    caught = 0
    for name, old, new in MUTATIONS:
        if old not in source:
            print(f"  MUTATION NOT APPLICABLE (needle missing): {name}")
            tmp.unlink(missing_ok=True)
            return 1
        tmp.write_text(source.replace(old, new, 1), encoding="utf-8")
        result = subprocess.run([sys.executable, str(tmp)], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"  NOT CAUGHT (mutant exited 0): {name}")
            tmp.unlink(missing_ok=True)
            return 1
        if "[FAIL]" not in result.stdout:
            print(f"  CRASH-NOT-DETECTION (exit {result.returncode}, no [FAIL] "
                  f"line): {name}")
            err = result.stderr.strip().splitlines()
            if err:
                print(f"    last stderr line: {err[-1][:120]}")
            tmp.unlink(missing_ok=True)
            return 1
        caught += 1
        print(f"  caught by [FAIL] check (exit {result.returncode}): {name}")
    tmp.unlink(missing_ok=True)
    print(f"\n--selftest: baseline verified GREEN first, then "
          f"{caught}/{len(MUTATIONS)} injected mutations drove exit 1.")
    return 0


def main() -> int:
    scratch = ROOT / "tests" / "channel-swings" / "_sg1_scratch"

    if "--selftest" in sys.argv:
        print("SG-1 C6a scope narrowing -- SELFTEST (baseline first, then "
              "planted false machinery)")
        rc = selftest(scratch)
        try:
            scratch.rmdir()
        except OSError:
            pass
        return rc

    print("=" * 74)
    print("SG-1 -- the C6a scope defect, its disposition, and what the "
          "dependent gates inherit")
    print("=" * 74)

    leg1_defect()
    leg2_contrary_controls()
    leg3_narrowing_is_inert()
    leg4_receipt(scratch)
    leg5_gates_and_selector()
    planted_false_facts()

    try:
        scratch.rmdir()
    except OSError:
        pass

    n_pass = sum(1 for ok, _ in CHECKS if ok)
    n_fail = len(CHECKS) - n_pass
    print("\n" + "=" * 74)
    print(f"CHECKS: {n_pass} passed, {n_fail} failed, {len(CHECKS)} total")
    print("=" * 74)
    if n_fail:
        for ok, label in CHECKS:
            if not ok:
                print(f"  FAILED: {label}")
        return 1

    print("""
DISPOSITION APPLIED
  NARROWING, recorded OUTSIDE the predeclaration.
  `tests/gu-forces/leg_a_forcing_enumeration.py` is NOT edited, and is now
  SHA-256 pinned by this probe so that any future edit turns it red.

  The defect is a SENTENCE that over-reaches its own cell space, not a wrong
  cell.  C6a's three coded cells are correct.  No computed bit moves.

  SELECTOR.  For the DYNAMICAL question -- is the VEV on, is the class-2
  bosonic insertion switched on, which emergent split is realized -- SG4 bit 2
  is correct and CR-B and CS-1 route it correctly.  For the CONTENT question --
  which of {S-FULL-DIRAC, S-HALF-OPPOSITE, S-HALF-SAME} the declaration carries
  -- THIS ENUMERATION NAMES NO SELECTOR, and none is missing from it: SG4 is by
  definition the UNWRITTEN declaration, while the chirality assignment is
  written, twice, at two layers, and was read by CR-B.  The selector is the
  source, already consulted -- not a bit awaiting a build.
""")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
