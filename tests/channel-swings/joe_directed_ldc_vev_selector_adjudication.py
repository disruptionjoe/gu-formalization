#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LD-C: five VEV/decoupling-selector concerns adjudicated — the probe.

Pins the evidence base and the five verdict cards of
`lab/active-research/joe-directed/lens-digs/ldc-vev-selector-adjudication-2026-08-17.md`:

  R  the register: SC-CHI-01 verbatim + both hedges + polarity ASSERTS;
     SC-META-53 polarity UNCERTAIN ("Well, I don't know"); the adherence
     evidence of SC-CHI-01 cites NO SRC file (absence, planted-positive
     controlled).
  E  the p.52 extraction: the ϖ hedge verbatim, including "significantly
     above zero" (small-VEV, not zero-VEV).
  T  the drafts transcript: L158 carries the "if" / "decreased VEV" /
     "mass is actually a variable"; L155's "I don't know what to do" is the
     KILLING-FORM openness declaration, not a VEV statement.
  C  canon SG4: the two bit definitions, "neither bit alone forces", the
     bijective corner map sentence, the B-tilt with ZERO counter-tilts.
  L  the frozen predeclaration `leg_a_forcing_enumeration.py`: the VERTEX
     corner map is PARSED (not restated) and the dependence lemma COMPUTED:
     consistent support has 3 corners (not a product set); on it
     ABSENT => MASSIVE and CHIRAL => PRESENT => carrier A.
  S  the SRC arc: SOURCE_NATIVE_ROUTE classifications, the adverse headline
     clauses, pending_integration, and the UNMADE JOIN (zero SC-CHI-01 /
     bit-2 tokens in SRC-2/3/4; planted-positive controlled).
  D  ledger v0.259: RA-D2 GENUINE_FALSIFICATION; RA-D4's two trigger-conjunct
     buckets; LT-SM8's minted kind; the stationarity/Hessian trigger family;
     the G6-blocked rows all MISSING_CONSTRUCTION and none ONE_BIT.
  X  the banked GP-corner chain (escape-corners canon :59-64; lega1 :257).
  J  the routing/fence surfaces: ST-1 V1 and §6, SG-1's homonym, CN-2 §4.4,
     PCX-1, SCUR-1 row 6 + D2, gu-base-categories L4/G6/LA3.
  V  this dig's own five verdict lines, the dedupe answer, and a
     deliberately-wrong verdict (the parent's uncorrected "nobody's row"
     reading) planted in-probe and required to be ABSENT from the card file
     while the same detector flags it on a synthetic positive.

Twelve planted false facts are evaluated and must each come out False.

Exit 0 == every check passed.  ``--selftest`` FIRST verifies the clean
baseline exits 0 — a red baseline aborts with exit 1 rather than banking a
false "all mutations caught" — then runs 8 machinery-corruption mutations
(parser, path, row-lookup, normalizer, detector, support-builder,
ledger-version, planted-fact evaluator), each required to drive exit 1 via a
genuine [FAIL] line; a nonzero exit WITHOUT a [FAIL] line is counted
CRASH-NOT-DETECTION and fails the selftest.  Mutations corrupt machinery or
references, never a check's predicate.  The selftest itself exits 0.
"""

from __future__ import annotations

import json
import os
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
MUT = os.environ.get("LDC_MUTATE", "")

CARD = "lab/active-research/joe-directed/lens-digs/ldc-vev-selector-adjudication-2026-08-17.md"
REGISTER = "lab/sources/source-claim-register.yaml"
EXTRACTION = "lab/sources/gu-2021-draft-s11-s12-extraction-2026-08-03.md"
TRANSCRIPT = "papers/drafts/Transcript into the impossible.md"
CANON_SG4 = "canon/gu-forces-field-space-declaration-RESULTS.md"
ESCAPE = "canon/escape-corners-campaign-RESULTS.md"
LEGA1 = "tests/escape-corners/lega1_flipped_chiral_adjudication.md"
LEG_A = "tests/gu-forces/leg_a_forcing_enumeration.py"
LEDGER = "lab/process/conditional-physics-ledger-v0.259.json"
ST1 = "lab/active-research/joe-directed/seesaw-tradeoff/st1-tradeoff-dissolves-into-sg4-bit-2-2026-08-16.md"
SG1 = "lab/active-research/joe-directed/sg4-axis/sg1-c6a-scope-narrowing-2026-08-16.md"
CN2 = "lab/active-research/joe-directed/carrier-notation/cn2-notation-carries-the-answer-2026-08-15.md"
PCX1 = "lab/active-research/joe-directed/parity-crosscheck/pcx1-signature-parity-clause-does-not-fire-2026-08-17.md"
SCUR1 = "lab/active-research/joe-directed/source-currency/scur1-source-currency-audit-2026-08-17.md"
BASECAT = "lab/methods/gu-base-categories.md"
SRC1 = "lab/active-research/joe-directed/majorana-126-neutrino/src1-source-steelman-of-the-vev-2026-08-14.md"
SRC2 = "lab/active-research/joe-directed/majorana-126-neutrino/src2-mexican-hat-is-automatic-2026-08-14.md"
SRC3 = "lab/active-research/joe-directed/majorana-126-neutrino/src3-potential-unbounded-below-2026-08-14.md"
SRC4 = "lab/active-research/joe-directed/majorana-126-neutrino/src4-eddy-completion-cannot-rescue-the-potential-2026-08-15.md"
BD2 = "lab/active-research/joe-directed/majorana-126-neutrino/bd2-126-channel-is-repulsive-2026-08-14.md"
BD2SU = "lab/active-research/joe-directed/baryon-number-and-proton-decay/bd2-su32-image-retains-the-classic-xy-half-2026-08-17.md"
TOPLEVEL = ["RESEARCH-STATUS.md", "CANON.md", "CURRENT-STATE.yaml"]

FAILURES: list[str] = []
CHECKS = 0


def check(desc: str, ok: bool) -> None:
    global CHECKS
    CHECKS += 1
    if ok:
        print(f"[ok]   {CHECKS:3d}  {desc}")
    else:
        FAILURES.append(desc)
        print(f"[FAIL] {CHECKS:3d}  {desc}")


# ---------------------------------------------------------------- machinery
def read(rel: str) -> str:
    # M2: register path swapped to a different source file.
    if MUT == "2" and rel == REGISTER:
        rel = "lab/sources/gu-2021-draft-s9-fermionic-operator-extraction-2026-08-04.md"
    return (ROOT / rel).read_text(encoding="utf-8")


def norm(text: str) -> str:
    """Blockquote markers stripped, whitespace collapsed. Case preserved."""
    text = re.sub(r"^\s*>\s?", "", text, flags=re.M)
    if MUT == "4":  # M4: normalizer corrupted — case-folds the corpus.
        text = text.lower()
    return re.sub(r"\s+", " ", text)


VERTEX_RE = r'\("(\w+)",\s*"(\w+)"\):\s*\{"carrier":\s*"(\w+)"'
if MUT == "1":  # M1: parser corrupted — only sees MASSIVE-phase corners.
    VERTEX_RE = r'\("(\w+)",\s*"(MASSIVE)"\):\s*\{"carrier":\s*"(\w+)"'


def parse_vertex(text: str) -> dict[tuple[str, str], str]:
    return {(m[0], m[1]): m[2] for m in re.findall(VERTEX_RE, text)}


def consistent_support(vertex: dict[tuple[str, str], str]) -> dict[tuple[str, str], str]:
    if MUT == "6":  # M6: support-builder corrupted — keeps the dead corner.
        return dict(vertex)
    return {k: v for k, v in vertex.items() if v != "INCONSISTENT"}


def ledger_rows() -> dict[str, dict]:
    path = LEDGER
    if MUT == "7":  # M7: ledger-version rollback.
        path = "lab/process/conditional-physics-ledger-v0.1.json"
    data = json.loads(read(path))
    rows = data["rows"] if isinstance(data, dict) else data
    return {r["id"]: r for r in rows if isinstance(r, dict) and "id" in r}


def get_row(rows: dict[str, dict], rid: str) -> dict:
    if MUT == "3" and rid == "RA-D2":  # M3: row-lookup crosswired.
        rid = "RA-D4"
    return rows.get(rid, {})


def src_join_detector(text: str) -> bool:
    """True iff the text cites the SRC arc or the bit-2 token."""
    if MUT == "5":  # M5: absence detector blinded.
        return False
    return bool(re.search(r"src[234]-|SRC-[234]|(?<![A-Za-z0-9-])[Bb]it[ -]2(?![0-9])", text))


def evaluate_planted(fact_id: str, value: bool) -> bool:
    if MUT == "8" and fact_id == "PF4":  # M8: evaluator inverted for PF4.
        return True
    return value


BIT2_TOKEN = re.compile(r"(?<![A-Za-z0-9-])[Bb]it[ -]2(?![0-9])")


def main() -> int:
    reg = norm(read(REGISTER))
    ext = norm(read(EXTRACTION))
    tr_lines = read(TRANSCRIPT).splitlines()
    tr155 = tr_lines[154] if len(tr_lines) >= 155 else ""
    tr158 = tr_lines[157] if len(tr_lines) >= 158 else ""
    csg4 = norm(read(CANON_SG4))
    esc = norm(read(ESCAPE))
    lega1 = norm(read(LEGA1))
    leg_raw = read(LEG_A)
    leg = norm(leg_raw)
    st1 = norm(read(ST1))
    sg1 = norm(read(SG1))
    cn2 = norm(read(CN2))
    pcx1 = norm(read(PCX1))
    scur1 = norm(read(SCUR1))
    basecat = norm(read(BASECAT))
    card = norm(read(CARD))

    # ---------------------------------------------------------------- R: register
    print("== R: the register")
    sc_chi = reg.split("- id: SC-CHI-01", 1)[-1].split("- id: SC-CHI-02", 1)[0]
    check("R1 SC-CHI-01 verbatim: 'Thus we assert that a non-chiral total theory splits at the emergent'",
          "Thus we assert that a non-chiral total theory splits at the emergent" in sc_chi)
    check("R2 SC-CHI-01 verbatim: 'corresponds to matter in our world' + 'currently dark to us'",
          "corresponds to matter in our world" in sc_chi and "currently dark to us" in sc_chi)
    check("R3 SC-CHI-01 polarity ASSERTS",
          re.search(r"polarity:\s*ASSERTS", sc_chi) is not None)
    check("R4 SC-CHI-01 note carries BOTH hedges: 'significantly above zero' + 'The idea being explored here'",
          "significantly above zero" in sc_chi and "The idea being explored here" in sc_chi)
    sc_meta = reg.split("- id: SC-META-53", 1)[-1].split("- id: SC-", 1)[0] if "- id: SC-META-53" in reg else ""
    check("R5 SC-META-53 polarity UNCERTAIN with 'Well, I don't know'",
          re.search(r"polarity:\s*UNCERTAIN", sc_meta) is not None and "Well, I don't know" in sc_meta)
    adh = sc_chi.split("adherence:", 1)[-1]
    check("R6 SC-CHI-01 adherence cites the frontier index (its actual evidence)",
          "frontier-design-packets-index-2026-08-11.md" in adh)
    check("R7 ABSENCE: SC-CHI-01 adherence cites NO SRC file and no bit-2 token",
          not src_join_detector(adh))
    planted_positive = adh + " lab/active-research/joe-directed/majorana-126-neutrino/src2-mexican-hat-is-automatic-2026-08-14.md"
    check("R8 PLANTED-POSITIVE: the same detector flags a synthetic adherence block citing src2",
          src_join_detector(planted_positive))

    # ---------------------------------------------------------------- E: extraction
    print("== E: the p.52 hedge")
    check("E1 hedge verbatim incl. 'sub-fields of ϖ to values significantly above zero'",
          "when there is no vacuum expectation value pulling the various sub-fields of ϖ to values significantly above zero" in ext)
    check("E2 hedge strength clause 'The idea being explored here is that the full' present at the locus",
          "The idea being explored here is that the full" in ext)

    # ---------------------------------------------------------------- T: transcript
    print("== T: drafts transcript L155/L158")
    check("T1 L158 carries the 'if': 'if you have a decreased VEV'",
          "if you have a decreased VEV" in tr158)
    check("T2 L158 carries 'because the mass is actually a variable'",
          "because the mass is actually a variable" in tr158)
    check("T3 L158 carries the two-Weyl clause ('two vial equations', ASR spelling)",
          "two vial equations" in tr158)
    check("T4 L155 'I don't know what to do' is the KILLING-FORM declaration",
          "I don't know what to do because we're in a maximally compact subgroup" in tr155
          and "indefinite signature on the killing form" in tr155)
    check("T5 L155 contains NO VEV statement (disambiguation: the two openness declarations differ)",
          "VEV" not in tr155 and "vacuum expectation" not in tr155)

    # ---------------------------------------------------------------- C: canon SG4
    print("== C: canon SG4 — the two bits")
    check("C1 'neither bit alone forces a unique carrier'",
          "neither bit alone forces a unique carrier" in csg4)
    check("C2 Bit 1 defined: invariance-selection / graded-IG scalar-spinor eps sub-slot",
          "Bit 1 -- invariance-selection:" in csg4
          and "does SG4 gauge the graded-IG scalar-spinor eps sub-slot?" in csg4)
    check("C3 Bit 2 defined: phase, chiral/unbroken vs massive/super-Higgs",
          "Bit 2 -- phase:" in csg4 and "chiral/unbroken vs massive/super-Higgs" in csg4)
    check("C4 the corner map is claimed bijective onto the four completions",
          "map **bijectively** onto the four known completions" in csg4)
    check("C5 the B-tilt: ~6 commitments, ZERO counter-tilts",
          "ZERO counter-tilts" in csg4)
    check("C6 canon presents the residual as a free '2-dimensional residual' (no dependence note)",
          "2-dimensional residual" in csg4 and "consistent support" not in csg4)

    # ---------------------------------------------------------------- L: the frozen corner map
    print("== L: leg_a — parse VERTEX, compute the dependence lemma")
    vertex = parse_vertex(leg_raw)
    check("L1 VERTEX parses to exactly 4 corners", len(vertex) == 4)
    check("L2 (ABSENT, MASSIVE) -> B", vertex.get(("ABSENT", "MASSIVE")) == "B")
    check("L3 (PRESENT, CHIRAL) -> A", vertex.get(("PRESENT", "CHIRAL")) == "A")
    check("L4 (PRESENT, MASSIVE) -> CTRL40 (-40, super-Higgs)",
          vertex.get(("PRESENT", "MASSIVE")) == "CTRL40")
    check("L5 (ABSENT, CHIRAL) -> INCONSISTENT (the GP corner)",
          vertex.get(("ABSENT", "CHIRAL")) == "INCONSISTENT")
    sup = consistent_support(vertex)
    check("L6 LEMMA: consistent support has exactly 3 corners", len(sup) == 3)
    invs = {k[0] for k in sup}
    phases = {k[1] for k in sup}
    product = {(i, p) for i in invs for p in phases}
    check("L7 LEMMA: the support is NOT a product set (witness: (ABSENT, CHIRAL) in product, not in support)",
          ("ABSENT", "CHIRAL") in product and ("ABSENT", "CHIRAL") not in sup and product != set(sup))
    check("L8 LEMMA: on the support, ABSENT => MASSIVE",
          all(p == "MASSIVE" for (i, p) in sup if i == "ABSENT") and any(i == "ABSENT" for (i, p) in sup))
    check("L9 LEMMA: on the support, CHIRAL => PRESENT and carrier A",
          all(i == "PRESENT" and sup[(i, p)] == "A" for (i, p) in sup if p == "CHIRAL")
          and any(p == "CHIRAL" for (i, p) in sup))
    check("L10 the phase bit's CHIRAL value is the decreased-VEV point (binning semantics)",
          "unbroken chiral (decreased-VEV) point" in leg)
    check("L11 C5 predeclares the phase a free modulus and refuses to pick",
          "Declares the PHASE axis a free MODULUS" in leg and "REFUSES to pick a phase" in leg)
    check("L12 corner assignment in C5's own source string: A chiral, B massive",
          "A at the chiral point, B at the massive point" in leg)
    check("L13 bit 1 is the local fermionic (ghost-subtracting) invariance, ABSENT/PRESENT",
          'INVARIANCE = {"ABSENT", "PRESENT"}' in leg
          and "local fermionic (ghost-subtracting) invariance" in leg)
    check("L14 field-space is DEPENDENT on the pair (the residual is exactly the two bits)",
          "Field-space is DEPENDENT: it is fixed" in leg and "once (invariance, phase) are fixed" in leg)

    # ---------------------------------------------------------------- S: the SRC arc
    print("== S: the SRC arc and the unmade join")
    src1 = norm(read(SRC1))
    src2 = norm(read(SRC2))
    src3 = norm(read(SRC3))
    src4 = norm(read(SRC4))
    check("S1 SRC-1 carries the source mechanism ('Mexican hat potential', no Higgs)",
          "Mexican hat potential" in src1 and "NO Higgs" in src1)
    check("S2 SRC-2 classification SOURCE_NATIVE_ROUTE (not comparator-scoped)",
          "Classification: `SOURCE_NATIVE_ROUTE`" in src2)
    check("S3 SRC-2 adverse headline: the symmetric point is never stable",
          "the symmetric point is never stable" in src2
          and "SYMMETRIC_POINT_NEVER_STABLE" in src2)
    check("S4 SRC-2 canonical_effect pending_integration (un-integrated adverse partial)",
          "canonical_effect: pending_integration" in src2)
    check("S5 SRC-3 classification SOURCE_NATIVE_ROUTE",
          "Classification: `SOURCE_NATIVE_ROUTE`" in src3)
    check("S6 SRC-3 adverse headline: UNBOUNDED BELOW, conditional on the undeclared norm",
          "UNBOUNDED BELOW" in src3 and "SG4 leaves the actual quadratic form undeclared" in src3)
    check("S7 SRC-4 reduces boundedness to one undeclared coefficient sign",
          "kappa_1 * flat_1 >= 0" in src4)
    check("S8 ABSENCE (the unmade join): SRC-2 carries no SC-CHI-01 and no bit-2 token",
          "SC-CHI-01" not in src2 and not BIT2_TOKEN.search(src2))
    check("S9 ABSENCE: SRC-3 and SRC-4 likewise",
          all("SC-CHI-01" not in t and not BIT2_TOKEN.search(t) for t in (src3, src4)))
    check("S10 PLANTED-POSITIVE: the join detector fires on a synthetic SRC-3 citing 'SG4 bit 2'",
          src_join_detector(src3 + " and this dissolves into SG4 bit 2"))

    # ---------------------------------------------------------------- D: ledger v0.259
    print("== D: ledger v0.259")
    rows = ledger_rows()
    d2 = get_row(rows, "RA-D2")
    check("D1 RA-D2 is the stated VEV/mass mechanism row",
          d2.get("summary") == "the stated VEV/mass mechanism produces low-energy chirality")
    check("D2 RA-D2 verdict OVER_DETERMINED / GENUINE_FALSIFICATION (mechanism deader than 'open')",
          d2.get("verdict") == "OVER_DETERMINED" and d2.get("reason_kind") == "GENUINE_FALSIFICATION")
    check("D3 RA-D2 revival is construction-shaped: 'not obtained by equivariant mass splitting'",
          "not obtained by equivariant mass splitting" in d2.get("revival_trigger", ""))
    d4 = rows.get("RA-D4", {})
    buckets = {c.get("bucket") for c in d4.get("trigger_conjuncts", [])}
    check("D4 RA-D4 trigger_conjuncts carry BOTH buckets (the item-16 distinction, executed)",
          buckets == {"SOURCE_DECLARED_OPEN", "SOURCE_STATED_CONDITION"})
    stated = [c for c in d4.get("trigger_conjuncts", []) if c.get("bucket") == "SOURCE_STATED_CONDITION"]
    check("D5 the SOURCE_STATED_CONDITION conjunct is registered to drafts :158",
          bool(stated) and "Transcript into the impossible.md:158" in stated[0].get("register", ""))
    check("D6 LT-SM8 carries IT-C's minted kind (the SC-META-53 shape, NOT the bit-2 shape)",
          rows.get("LT-SM8", {}).get("reason_kind") == "SOURCE_DECLARED_OPEN__NO_MECHANISM_SUPPLIED")
    check("D7 stationarity demands exist: RA-A8 'stationary vacuum'",
          "stationary vacuum" in rows.get("RA-A8", {}).get("revival_trigger", ""))
    check("D8 stationarity demands exist: RA-E6 'vacuum Hessian'",
          "vacuum Hessian" in rows.get("RA-E6", {}).get("revival_trigger", ""))
    check("D9 stationarity demands exist: RA-G3 'stationary odd-form VEV'",
          "stationary odd-form VEV" in rows.get("RA-G3", {}).get("revival_trigger", ""))
    check("D10 stationarity demands exist: RA-A1 'stabilizer theorem'",
          "stabilizer theorem" in rows.get("RA-A1", {}).get("revival_trigger", ""))
    g6_blocked = [rows.get(r, {}).get("reason_kind") for r in ("LT-GR2d", "RA-G3", "AC-F1")]
    check("D11 the G6-blocked rows are all MISSING_CONSTRUCTION (mechanism-shaped debt)",
          g6_blocked == ["MISSING_CONSTRUCTION"] * 3)
    check("D12 none of the G6-blocked rows is ONE_BIT (the value is NOT held as an open bit)",
          "ONE_BIT" not in g6_blocked)

    # ---------------------------------------------------------------- X: the banked GP-corner chain
    print("== X: the GP-corner chain (banked 2026-07-10)")
    check("X1 escape-corners canon: 'At the chiral point GU's phenomenology commits'",
          "At the chiral point GU's phenomenology commits" in esc)
    check("X2 escape-corners canon: 'opposing demands on one dial' resolved only 'Which is corner (b).'",
          "opposing demands on one dial" in esc and "Which is corner (b)." in esc)
    check("X3 lega1 prices the two conjuncts: chiral-point vacuum AND uniform mass map",
          "taken at the chiral point AND" in lega1
          and "the mass map is uniform across the fermionic extension" in lega1)

    # ---------------------------------------------------------------- J: routing and fence surfaces
    print("== J: routing/fence surfaces")
    check("J1 ST-1 V1: bit 2 owned by Lane 1, not decided by design",
          "Owned by Lane 1" in st1 and "Not decided here, by design" in st1)
    check("J2 ST-1 V1 layer name carries the observational anchor: 'Observed, VEV-conditional'",
          "Observed, VEV-conditional" in st1)
    check("J3 ST-1 §6 bins the observed epoch at the VEV-ON side (binning leg A)",
          "the phase with spectrum is the same phase the observed-layer quote already conditions on" in st1)
    check("J4 SCUR-1 bins observed chirality at the m→0 branch (binning leg B — the OPPOSITE bin)",
          "the m→0 branch IS the source's claimed phase" in scur1
          and "Observed chirality VEV-conditional" in scur1)
    check("J5 SCUR-1 states the selector stays open by design in the same breath",
          "OPEN by design" in scur1)
    check("J6 SG-1: bit 2 is a PHASE bit; the CHIRAL homonym is Layer-0",
          "Bit 2 is a PHASE bit" in sg1
          and "literally spelled CHIRAL meaning massless/unbroken" in sg1)
    check("J7 CN-2 §4.4: mapping a content fork onto bit 2 is an unlicensed identification step",
          "identification CR-B makes, not one this enumeration licenses" in cn2)
    check("J8 PCX-1: identifications need constructed receipts ('the layers do not meet')",
          "the layers do not meet" in pcx1)
    check("J9 gu-base-categories: L4 layer named 'VEV-observed'; G6 sits on the DEMAND side",
          "VEV-observed" in basecat and "on the DEMAND side" in basecat)
    check("J10 gu-base-categories LA3 cell carries both halves of the direction flip (flagged, not repaired)",
          "exists only under the `SC-CHI-01` hedge" in basecat
          and "in the `varpi -> 0` phase the arrow is absent" in basecat)

    # ---------------------------------------------------------------- V: this dig's own cards
    print("== V: the five verdict cards")
    check("V1 card 6 verdict pinned: LIVE-MODERATE, premise corrected",
          "VERDICT: LIVE-MODERATE — premise corrected, residue live." in card)
    check("V2 card 10 verdict pinned: LIVE-MODERATE, address corrected",
          "VERDICT: LIVE-MODERATE.** The concern survives with its address corrected" in card)
    check("V3 card 16 verdict pinned: LIVE-MODERATE, mint-and-join",
          "VERDICT: LIVE-MODERATE.** Live: the typed record and the coupling rule" in card)
    check("V4 card 17 verdict pinned: DISSOLVES as posed, residue is a different claim",
          "VERDICT: DISSOLVES as posed — with a LIVE-MODERATE residue that is a different claim" in card)
    check("V5 card 18 verdict pinned: ALREADY-COVERED-IN-SUBSTANCE + typing residue",
          "VERDICT: ALREADY-COVERED-IN-SUBSTANCE (canon escape-corners :59-64" in card)
    check("V6 the dedupe answer pinned: 16 and 17 are NOT duplicates",
          "NOT duplicates — different objects, different verdicts, different repairs." in card)
    wrong_verdict = "VERDICT: LIVE-HIGH — the phase's dynamical stability is nobody's row"
    check("V7 WRONG-VERDICT CONTROL: the parent's uncorrected reading is ABSENT from the card file",
          wrong_verdict not in card and "DUPLICATE-OF(16" not in card)
    check("V8 WRONG-VERDICT CONTROL: the same detector finds it on a synthetic positive",
          wrong_verdict in card + " " + wrong_verdict)

    # ------------------------------------------------------- planted false facts
    print("== PF: twelve planted false facts (each must be False)")
    planted = [
        ("PF1", "SC-CHI-01 polarity is UNCERTAIN",
         re.search(r"polarity:\s*UNCERTAIN", sc_chi) is not None),
        ("PF2", "L155 contains 'decreased VEV'", "decreased VEV" in tr155),
        ("PF3", "RA-D2 reason_kind is MISSING_CONSTRUCTION",
         rows.get("RA-D2", {}).get("reason_kind") == "MISSING_CONSTRUCTION"),
        ("PF4", "(ABSENT, CHIRAL) maps to carrier B",
         vertex.get(("ABSENT", "CHIRAL")) == "B"),
        ("PF5", "SRC-2 is classified CONVENTIONAL_COMPARATOR",
         "Classification: `CONVENTIONAL_COMPARATOR`" in src2),
        ("PF6", "the consistent support IS the full product set",
         set(sup) == product),
        ("PF7", "SRC-3 contains a bit-2 token",
         bool(BIT2_TOKEN.search(src3))),
        ("PF8", "LT-SM8 reason_kind is MISSING_CONSTRUCTION",
         rows.get("LT-SM8", {}).get("reason_kind") == "MISSING_CONSTRUCTION"),
        ("PF9", "canon SG4 lacks the bijection sentence",
         "map **bijectively** onto the four known completions" not in csg4),
        ("PF10", "SC-META-53 polarity is ASSERTS",
         re.search(r"polarity:\s*ASSERTS", sc_meta) is not None),
        ("PF11", "the p.52 hedge demands an EXACTLY ZERO VEV",
         "to values exactly zero" in ext),
        ("PF12", "a top-level surface carries a bit-2 token",
         any(BIT2_TOKEN.search(norm(read(f))) for f in TOPLEVEL)),
    ]
    observed = {fid: evaluate_planted(fid, val) for fid, desc, val in planted}
    for fid, desc, _val in planted:
        check(f"{fid} planted false fact observed False: {desc}", observed[fid] is False)

    # ---------------------------------------------------------------- summary
    print(f"\n{CHECKS} checks, {len(FAILURES)} failures.")
    if FAILURES:
        for f in FAILURES:
            print(f"  FAILED: {f}")
        return 1
    return 0


# ------------------------------------------------------------------ selftest
MUTATIONS = {
    "1": "VERTEX parser corrupted: regex only matches MASSIVE-phase corners",
    "2": "register path swapped to the s9 extraction file",
    "3": "ledger row-lookup crosswired: RA-D2 resolves to RA-D4",
    "4": "quote normalizer corrupted: corpus case-folded",
    "5": "absence/join detector blinded: always False",
    "6": "support-builder corrupted: keeps the INCONSISTENT corner",
    "7": "ledger-version rollback: reads v0.1 instead of v0.259",
    "8": "planted-fact evaluator inverted for PF4",
}


def selftest() -> int:
    env = {k: v for k, v in os.environ.items() if k != "LDC_MUTATE"}
    print("selftest: verifying the CLEAN BASELINE first ...")
    base = subprocess.run([sys.executable, __file__], env=env,
                          capture_output=True, text=True)
    if base.returncode != 0:
        print("selftest ABORT: clean baseline is RED (exit "
              f"{base.returncode}); mutations would be meaningless.")
        print(base.stdout[-2000:])
        return 1
    print("selftest: baseline green. running 8 machinery mutations ...")
    bad = 0
    for key, desc in MUTATIONS.items():
        env_m = dict(env)
        env_m["LDC_MUTATE"] = key
        run = subprocess.run([sys.executable, __file__], env=env_m,
                             capture_output=True, text=True)
        caught = run.returncode != 0 and "[FAIL]" in run.stdout
        crash = run.returncode != 0 and "[FAIL]" not in run.stdout
        tag = "caught" if caught else ("CRASH-NOT-DETECTION" if crash else "NOT CAUGHT")
        print(f"  mutation {key}: {desc} -> exit {run.returncode} ({tag})")
        if not caught:
            bad += 1
    if bad:
        print(f"selftest: {bad} mutation(s) not properly caught. FAIL.")
        return 1
    print("selftest: baseline green first, 8/8 mutations caught via genuine [FAIL] lines. OK.")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    sys.exit(main())
